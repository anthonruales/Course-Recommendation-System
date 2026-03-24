"""
Cluster & Remove Rephrases — Phase 1: Identify removal set
============================================================
For each category, clusters questions by conceptual meaning (ignoring
superficial phrasing differences), then marks expansion duplicates for removal.

KEEP rule: lowest question_id in each cluster (the static / original question).
REMOVE rule: every other question in the cluster.

Outputs:
  - Detailed cluster report
  - Python set of question IDs to remove
"""

import sys, re, os
from collections import defaultdict

sys.path.insert(0, os.path.dirname(__file__))
from data.questions_enhanced import QUESTIONS_POOL_ENHANCED

# ─── Normalization ───────────────────────────────────────────────────────
def normalize(text):
    text = text.lower().strip()
    text = re.sub(r'^scenario:\s*', '', text)
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

STOP = frozenset(
    'a an the is are was were be been being have has had do does did '
    'will would could should may might shall can need dare ought used '
    'to of in for on with at by from as into through during before '
    'after above below between out off over under again further then '
    'once here there when where why how all each every both few more '
    'most other some such no nor not only own same so than too very '
    's t just don now d ll m o re ve y you your yours yourself i me '
    'my mine we our this that these those it its he she they them his '
    'her their what which who whom if about up but and or because '
    'until while one first two second also get got go went much many '
    'like well even still back feel feels sound sounds best fits pick '
    'choose type kind style way really want see'.split()
)

def stem(word):
    for suffix in ['ment','ness','tion','sion','ious','eous','ance','ence',
                   'able','ible','ful','less','ive','ise','ize','ous',
                   'ity','ies','ied','ers','est','ely','ally','ing',
                   'ly','ed','es','er','en','al','s']:
        if len(word) > len(suffix) + 2 and word.endswith(suffix):
            return word[:-len(suffix)]
    return word

def content_words(text):
    words = normalize(text).split()
    return [stem(w) for w in words if w not in STOP and len(w) > 2]

def content_set(text):
    return set(content_words(text))

def jaccard(s1, s2):
    if not s1 or not s2:
        return 0.0
    return len(s1 & s2) / len(s1 | s2)

def overlap_coeff(s1, s2):
    if not s1 or not s2:
        return 0.0
    return len(s1 & s2) / min(len(s1), len(s2))

# ─── Question type classifier (coarse-grained) ──────────────────────────
def question_type(text):
    """
    Classify into a COARSE question type. We intentionally merge types
    that the existing _semantic_dedup separated but are conceptually the same.
    """
    t = normalize(text)
    
    # SCENARIO — specific situation
    if any(w in t for w in ['scenario', 'imagine', 'what if', 'pretend', 'suppose',
                             'you are asked', 'you are hired', 'someone asks',
                             'a friend asks', 'your company', 'a school asks',
                             'a client', 'respond to', 'situation']):
        return 'SCENARIO'
    
    # PROJECT — what would you build/create/design
    if any(w in t for w in ['project', 'portfolio', 'build from scratch',
                             'would you create', 'would you produce',
                             'would you design', 'would you develop',
                             'would you make', 'would you tackle']):
        return 'PROJECT'
    
    # ENVIRONMENT — workplace/setting
    if any(w in t for w in ['environment', 'setting', 'workplace',
                             'work best', 'work in a', 'work in an']):
        return 'ENVIRONMENT'
    
    # CAREER — career path/role/job
    if any(w in t for w in ['career', 'job ', 'role ', 'profession',
                             'position', 'work as', 'would you pursue',
                             'would you work']):
        return 'CAREER'
    
    # SKILL — what skill to master/develop/improve
    if any(w in t for w in ['skill', 'master', 'improve', 'strengthen',
                             'expertise', 'develop first', 'proficiency']):
        return 'SKILL'
    
    # CROSS_FIELD — connecting with other fields
    if any(w in t for w in ['connect with other', 'cross-discipl', 'interdiscipl',
                             'blend', 'broader career', 'other field',
                             'connect with']):
        return 'CROSS_FIELD'
    
    # TEAM — collaboration/group work
    if any(w in t for w in ['team', 'collabor', 'group', 'contribute to a',
                             'working with']):
        return 'TEAM'
    
    # MOTIVATION — why/what motivates/keeps you committed
    if any(w in t for w in ['motivat', 'committed', 'why does', 'value most',
                             'personally', 'resonat', 'handle', 'challenge']):
        return 'MOTIVATION'
    
    # WHAT_ABOUT — all forms of "what about X interests/excites/appeals/draws you"
    # This now MERGES what was previously INTEREST, WHICH_PART, and SPECIALTY
    if any(w in t for w in ['excit', 'interest', 'appeal', 'drawn', 'attract',
                             'fascinat', 'meaningful', 'speaks to',
                             'aspect', 'part ', 'area ', 'side ',
                             'specialty', 'specializ', 'focus', 'branch',
                             'discipline', 'draws you', 'what about']):
        return 'WHAT_ABOUT'
    
    return 'GENERAL'

# ─── Option overlap computation ──────────────────────────────────────────
SKIP_OPTS = {
    "i don't see what i want", "none of these interest me",
    "i'm not sure yet", "none of the above", "skip",
}

def get_option_words(q):
    result = []
    for o in q.get('options', []):
        t = o.get('option_text', '').strip()
        if t.lower() in SKIP_OPTS or len(t) < 10:
            continue
        result.append(content_set(t))
    return result

def option_overlap_score(q1, q2):
    """Average best-match Jaccard across option sets."""
    opts1 = get_option_words(q1)
    opts2 = get_option_words(q2)
    if not opts1 or not opts2:
        return 0.0
    
    scores_1to2 = [max(jaccard(o1, o2) for o2 in opts2) for o1 in opts1]
    scores_2to1 = [max(jaccard(o2, o1) for o1 in opts1) for o2 in opts2]
    
    return (sum(scores_1to2)/len(scores_1to2) + sum(scores_2to1)/len(scores_2to1)) / 2

# ─── Rephrase detection ─────────────────────────────────────────────────
def is_rephrase(q1, q2):
    """
    Two questions in the SAME category are rephrases if they ask the same
    conceptual question AND their options cover similar ground.
    
    Strict rules to avoid false positives where questions share a topic
    but probe genuinely different dimensions (e.g., tools vs motivations,
    techniques vs workplaces).
    """
    t1 = q1['question_text']
    t2 = q2['question_text']
    
    type1 = question_type(t1)
    type2 = question_type(t2)
    
    ws1 = content_set(t1)
    ws2 = content_set(t2)
    
    j = jaccard(ws1, ws2)
    ov = overlap_coeff(ws1, ws2)
    opt_ov = option_overlap_score(q1, q2)
    
    same_type = (type1 == type2)
    
    # Rule 1: Very high question text overlap — clearly the same question
    # e.g., "What excites you about X?" vs "What draws you to X?"
    if j >= 0.5 and opt_ov >= 0.15:
        return True, f"high_jaccard={j:.2f} opt={opt_ov:.2f} [{type1}/{type2}]"
    
    # Rule 2: Same type with high question overlap + meaningful option overlap
    # Catches: "What area of X interests you?" vs "Which X specialty interests you?"
    if same_type and j >= 0.3 and opt_ov >= 0.2:
        return True, f"same_type={type1} j={j:.2f} opt={opt_ov:.2f}"
    
    # Rule 3: Same WHAT_ABOUT type with very high option overlap
    # Even if question text differs, if options cover the same ground it's redundant
    if same_type and type1 == 'WHAT_ABOUT' and opt_ov >= 0.3:
        return True, f"same_WHAT_ABOUT opt={opt_ov:.2f} j={j:.2f}"
    
    # Rule 4: High overlap coeff + decent option overlap — one question is a
    # subset/refinement of the other
    if ov >= 0.8 and opt_ov >= 0.2:
        return True, f"high_overlap_coeff={ov:.2f} opt={opt_ov:.2f} [{type1}/{type2}]"
    
    # Rule 5: Very high option overlap regardless of question text
    # If 40%+ of options match strongly, the questions are functionally redundant
    if opt_ov >= 0.4:
        return True, f"very_high_opt={opt_ov:.2f} j={j:.2f} [{type1}/{type2}]"
    
    # Rule 6: Same WHAT_ABOUT type with meaningful question text overlap
    # e.g., "What excites you about X?" vs "Which part of X interests you?"
    # j>=0.20 means they share content words beyond just the field name
    if same_type and type1 == 'WHAT_ABOUT' and j >= 0.20:
        return True, f"same_WHAT_ABOUT_highj j={j:.2f} opt={opt_ov:.2f}"
    
    # Rule 7: Same WHAT_ABOUT type with both question AND option overlap
    if same_type and type1 == 'WHAT_ABOUT' and j >= 0.15 and opt_ov >= 0.15:
        return True, f"same_WHAT_ABOUT j={j:.2f} opt={opt_ov:.2f}"
    
    # Rule 8: Same CAREER type with decent overlap
    if same_type and type1 == 'CAREER' and j >= 0.25:
        return True, f"same_CAREER_highj j={j:.2f} opt={opt_ov:.2f}"
    if same_type and type1 == 'CAREER' and j >= 0.15 and opt_ov >= 0.15:
        return True, f"same_CAREER j={j:.2f} opt={opt_ov:.2f}"
    
    return False, ""

# ─── Clustering ──────────────────────────────────────────────────────────
def cluster_questions(questions):
    """Cluster questions by rephrase similarity using union-find."""
    n = len(questions)
    parent = list(range(n))
    reasons = {}
    
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def union(x, y, reason):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py
            reasons[(min(x,y), max(x,y))] = reason
    
    for i in range(n):
        for j in range(i+1, n):
            is_rep, reason = is_rephrase(questions[i], questions[j])
            if is_rep:
                union(i, j, reason)
    
    # Group by root
    clusters = defaultdict(list)
    for i in range(n):
        clusters[find(i)].append(i)
    
    return clusters, reasons

# ─── Main ────────────────────────────────────────────────────────────────
def main():
    print(f"Pool: {len(QUESTIONS_POOL_ENHANCED)} questions")
    
    # Group by category
    by_cat = defaultdict(list)
    for q in QUESTIONS_POOL_ENHANCED:
        by_cat[q.get('category', 'UNKNOWN')].append(q)
    
    total_remove = set()
    cluster_count = 0
    
    for cat in sorted(by_cat.keys()):
        qs = by_cat[cat]
        if len(qs) < 2:
            continue
        
        clusters, reasons = cluster_questions(qs)
        
        # Find clusters with >1 member
        for root, members in clusters.items():
            if len(members) < 2:
                continue
            
            cluster_count += 1
            cluster_qs = [qs[m] for m in members]
            # Sort by question_id — keep the lowest
            cluster_qs.sort(key=lambda q: q['question_id'])
            
            keep = cluster_qs[0]
            remove = cluster_qs[1:]
            
            print(f"\n{'='*70}")
            print(f"CLUSTER {cluster_count} in [{cat}]")
            print(f"  KEEP   Q{keep['question_id']}: {keep['question_text']}")
            for r in remove:
                print(f"  REMOVE Q{r['question_id']}: {r['question_text']}")
                total_remove.add(r['question_id'])
            
            # Show merge reasons
            for (i,j), reason in reasons.items():
                if i in members or j in members:
                    qi = qs[i]['question_id']
                    qj = qs[j]['question_id']
                    print(f"    merge Q{qi}<->Q{qj}: {reason}")
    
    print(f"\n{'='*70}")
    print(f"TOTAL CLUSTERS: {cluster_count}")
    print(f"TOTAL QUESTIONS TO REMOVE: {len(total_remove)}")
    print(f"POOL AFTER REMOVAL: {len(QUESTIONS_POOL_ENHANCED) - len(total_remove)}")
    
    print(f"\n# Python set for removal:")
    sorted_ids = sorted(total_remove)
    print(f"REMOVE_IDS = {{")
    for i in range(0, len(sorted_ids), 10):
        chunk = sorted_ids[i:i+10]
        print(f"    {', '.join(str(x) for x in chunk)},")
    print(f"}}")
    
    # ── DIAGNOSTIC: uncaught same-type pairs ─────────────────────────────
    print(f"\n{'='*70}")
    print("DIAGNOSTIC: Same-type pairs NOT caught by rules")
    print("Review these manually for potential missed rephrases")
    print(f"{'='*70}")
    
    uncaught = 0
    for cat in sorted(by_cat.keys()):
        qs = by_cat[cat]
        if len(qs) < 2:
            continue
        
        for i, q1 in enumerate(qs):
            t1 = question_type(q1['question_text'])
            for q2 in qs[i+1:]:
                # Skip if already marked
                if q1['question_id'] in total_remove or q2['question_id'] in total_remove:
                    continue
                t2 = question_type(q2['question_text'])
                if t1 != t2:
                    continue
                ws1 = content_set(q1['question_text'])
                ws2 = content_set(q2['question_text'])
                j_val = jaccard(ws1, ws2)
                opt_val = option_overlap_score(q1, q2)
                
                # Only show if there's SOME overlap
                if j_val > 0.0 or opt_val > 0.05:
                    uncaught += 1
                    print(f"\n  [{cat}] type={t1} j={j_val:.2f} opt={opt_val:.2f}")
                    print(f"    Q{q1['question_id']}: {q1['question_text']}")
                    print(f"    Q{q2['question_id']}: {q2['question_text']}")
    
    print(f"\n  Total uncaught same-type pairs with overlap: {uncaught}")

if __name__ == '__main__':
    main()
