"""
Deep Rephrase / Redundancy Detector
====================================
Goes beyond the built-in _semantic_dedup() by:
  1. Ignoring the rigid intent classifier — uses pure semantic overlap
  2. Comparing BOTH question text AND option text for similarity
  3. Using aggressive normalization + synonym expansion
  4. Checking every pair within the same category
  5. Also checking across closely-related categories
  6. Reporting ALL flagged pairs with similarity scores

Run:  python deep_rephrase_check.py > rephrase_report.txt
"""

import sys, re, os
from collections import defaultdict
from itertools import combinations

sys.path.insert(0, os.path.dirname(__file__))
from data.questions_enhanced import QUESTIONS_POOL_ENHANCED

# ─── Normalization helpers ───────────────────────────────────────────────
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
    'choose type kind style way really does do see want'.split()
)

# Synonym groups — words that should be treated as identical
SYNONYM_GROUPS = [
    {'excit', 'appeal', 'attract', 'drawn', 'interest', 'fascinat', 'meaningful', 'enjoy', 'motiv', 'inspir', 'passion'},
    {'part', 'aspect', 'area', 'side', 'element', 'component', 'dimension', 'facet'},
    {'build', 'creat', 'develop', 'construct', 'mak', 'design', 'craft', 'produc'},
    {'career', 'job', 'profession', 'role', 'work', 'occupat', 'position', 'employ'},
    {'skill', 'abil', 'talent', 'competent', 'expert', 'profici', 'capabil'},
    {'environ', 'set', 'workplac', 'atmospher', 'context'},
    {'team', 'group', 'collabor', 'partner', 'colleagu'},
    {'specialt', 'specializ', 'focus', 'branch', 'disciplin', 'niche'},
    {'project', 'task', 'assignment', 'undertaking'},
    {'prioriti', 'focus', 'tackl', 'address', 'handl'},
    {'help', 'assist', 'support', 'aid', 'serv'},
    {'technic', 'tech'},
    {'import', 'valu', 'crucial', 'essenti', 'signific', 'critic', 'key'},
]

# Build synonym lookup: stem -> canonical stem
SYNONYM_MAP = {}
for group in SYNONYM_GROUPS:
    canonical = sorted(group)[0]
    for word in group:
        SYNONYM_MAP[word] = canonical

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
    result = []
    for w in words:
        if w in STOP or len(w) <= 2:
            continue
        stemmed = stem(w)
        # Apply synonym mapping
        for syn_stem, canonical in SYNONYM_MAP.items():
            if stemmed.startswith(syn_stem) or syn_stem.startswith(stemmed):
                stemmed = canonical
                break
        result.append(stemmed)
    return result

def content_word_set(text):
    return set(content_words(text))

def jaccard(s1, s2):
    if not s1 or not s2:
        return 0.0
    return len(s1 & s2) / len(s1 | s2)

def overlap_coeff(s1, s2):
    """Overlap coefficient = |intersection| / min(|s1|, |s2|)"""
    if not s1 or not s2:
        return 0.0
    return len(s1 & s2) / min(len(s1), len(s2))

# ─── Option-level similarity ────────────────────────────────────────────
def option_texts(q):
    texts = []
    for o in q.get('options', []):
        t = o.get('option_text', '').strip()
        if t.lower() in ("i don't see what i want", "none of these interest me",
                          "i'm not sure yet", "none of the above", "skip"):
            continue
        texts.append(t)
    return texts

def option_similarity(q1, q2):
    """
    Compare option sets. Returns (best_avg_match, pct_matched).
    For each option in q1, find best match in q2 and vice versa.
    """
    opts1 = [content_word_set(t) for t in option_texts(q1)]
    opts2 = [content_word_set(t) for t in option_texts(q2)]
    if not opts1 or not opts2:
        return 0.0, 0.0
    
    # For each option in q1, best Jaccard match with any option in q2
    matches_1to2 = []
    for o1 in opts1:
        best = max(jaccard(o1, o2) for o2 in opts2)
        matches_1to2.append(best)
    
    matches_2to1 = []
    for o2 in opts2:
        best = max(jaccard(o2, o1) for o1 in opts1)
        matches_2to1.append(best)
    
    avg_match = (sum(matches_1to2)/len(matches_1to2) + sum(matches_2to1)/len(matches_2to1)) / 2
    pct_strong = sum(1 for m in matches_1to2 if m >= 0.3) / len(matches_1to2)
    
    return avg_match, pct_strong

# ─── Core question comparison ────────────────────────────────────────────
def question_core(text):
    """Extract the semantic core of a question, removing filler."""
    t = normalize(text)
    # Remove common question frames
    frames = [
        r'^which of (?:these|the following)\b',
        r'^what (?:kind|type|sort) of\b',
        r'^in your (?:opinion|view)\b',
        r'^if you (?:could|had to|were to)\b',
        r'^scenario\b',
    ]
    for f in frames:
        t = re.sub(f, '', t).strip()
    return t

def are_semantically_similar(q1, q2):
    """
    Comprehensive check: are two questions asking the same thing?
    Returns (is_similar, score, reason)
    """
    t1 = q1['question_text']
    t2 = q2['question_text']
    
    ws1 = content_word_set(t1)
    ws2 = content_word_set(t2)
    
    j = jaccard(ws1, ws2)
    ov = overlap_coeff(ws1, ws2)
    
    # Option similarity
    opt_avg, opt_pct = option_similarity(q1, q2)
    
    reasons = []
    score = 0.0
    
    # 1. Very high question text overlap
    if j >= 0.5:
        score += 0.5
        reasons.append(f"high question Jaccard={j:.2f}")
    elif j >= 0.3:
        score += 0.3
        reasons.append(f"moderate question Jaccard={j:.2f}")
    elif j >= 0.15:
        score += 0.1
        reasons.append(f"some question overlap Jaccard={j:.2f}")
    
    # 2. High overlap coefficient (catches subset relationships)
    if ov >= 0.7:
        score += 0.3
        reasons.append(f"high overlap_coeff={ov:.2f}")
    elif ov >= 0.5:
        score += 0.15
        reasons.append(f"moderate overlap_coeff={ov:.2f}")
    
    # 3. Option text similarity
    if opt_avg >= 0.35:
        score += 0.4
        reasons.append(f"high option_avg={opt_avg:.2f}")
    elif opt_avg >= 0.2:
        score += 0.2
        reasons.append(f"moderate option_avg={opt_avg:.2f}")
    elif opt_avg >= 0.1:
        score += 0.05
        reasons.append(f"some option overlap opt_avg={opt_avg:.2f}")
    
    if opt_pct >= 0.5:
        score += 0.2
        reasons.append(f"many strong option matches pct={opt_pct:.2f}")
    
    # 4. Question text near-identical after normalization
    norm1 = normalize(t1)
    norm2 = normalize(t2)
    if norm1 == norm2:
        return True, 1.0, "identical normalized text"
    
    # Combined score threshold
    is_similar = score >= 0.5
    
    return is_similar, score, "; ".join(reasons) if reasons else "no match"

# ─── Related category grouping ──────────────────────────────────────────
def category_family(cat):
    """Group related categories for cross-category comparison."""
    cat_lower = cat.lower()
    if 'programming' in cat_lower or 'coding' in cat_lower:
        return 'PROGRAMMING'
    if 'computer' in cat_lower or ' it' in cat_lower:
        return 'IT'
    if 'data' in cat_lower or 'analytics' in cat_lower:
        return 'DATA'
    if 'ai' in cat_lower or 'machine learn' in cat_lower:
        return 'AI'
    if 'cybersec' in cat_lower:
        return 'CYBERSEC'
    if 'web' in cat_lower:
        return 'WEB'
    if 'game' in cat_lower:
        return 'GAME'
    if 'engineer' in cat_lower:
        return 'ENGINEERING'
    if 'business' in cat_lower or 'entrepreneur' in cat_lower or 'marketing' in cat_lower:
        return 'BUSINESS'
    if 'art' in cat_lower or 'design' in cat_lower or 'media' in cat_lower or 'film' in cat_lower or 'music' in cat_lower:
        return 'ARTS'
    if 'health' in cat_lower or 'medic' in cat_lower or 'nurs' in cat_lower or 'pharm' in cat_lower:
        return 'HEALTH'
    if 'educ' in cat_lower or 'teach' in cat_lower:
        return 'EDUCATION'
    if 'law' in cat_lower or 'legal' in cat_lower or 'criminol' in cat_lower:
        return 'LAW'
    if 'social' in cat_lower or 'psych' in cat_lower or 'communit' in cat_lower:
        return 'SOCIAL'
    if 'science' in cat_lower or 'bio' in cat_lower or 'chem' in cat_lower or 'physic' in cat_lower:
        return 'SCIENCE'
    if 'agriculture' in cat_lower or 'enviro' in cat_lower:
        return 'AGRI_ENV'
    if 'hospitality' in cat_lower or 'tourism' in cat_lower or 'food' in cat_lower or 'culinar' in cat_lower:
        return 'HOSPITALITY'
    return cat[:30]

# ─── Main ────────────────────────────────────────────────────────────────
def main():
    print(f"Total questions in pool: {len(QUESTIONS_POOL_ENHANCED)}")
    print(f"Total options: {sum(len(q.get('options',[])) for q in QUESTIONS_POOL_ENHANCED)}")
    print()
    
    # Group by category
    by_cat = defaultdict(list)
    for q in QUESTIONS_POOL_ENHANCED:
        by_cat[q.get('category', 'UNKNOWN')].append(q)
    
    print(f"Categories: {len(by_cat)}")
    for cat, qs in sorted(by_cat.items(), key=lambda x: -len(x[1])):
        print(f"  {cat}: {len(qs)} questions")
    print()
    
    # ── CHECK 1: Within-category rephrase detection ──────────────────────
    print("=" * 80)
    print("CHECK 1: WITHIN-CATEGORY REPHRASE DETECTION")
    print("=" * 80)
    
    all_flagged = []
    
    for cat, qs in sorted(by_cat.items()):
        if len(qs) < 2:
            continue
        for i, q1 in enumerate(qs):
            for q2 in qs[i+1:]:
                is_sim, score, reason = are_semantically_similar(q1, q2)
                if is_sim:
                    all_flagged.append((score, cat, q1, q2, reason))
    
    all_flagged.sort(key=lambda x: -x[0])
    
    if all_flagged:
        print(f"\nFLAGGED: {len(all_flagged)} potential rephrase pairs\n")
        for idx, (score, cat, q1, q2, reason) in enumerate(all_flagged, 1):
            print(f"--- PAIR {idx} (score={score:.2f}) ---")
            print(f"Category: {cat}")
            print(f"Q{q1['question_id']}: {q1['question_text']}")
            for o in q1.get('options', [])[:4]:
                print(f"    - {o['option_text']}")
            if len(q1.get('options', [])) > 4:
                print(f"    ... +{len(q1['options'])-4} more options")
            print(f"Q{q2['question_id']}: {q2['question_text']}")
            for o in q2.get('options', [])[:4]:
                print(f"    - {o['option_text']}")
            if len(q2.get('options', [])) > 4:
                print(f"    ... +{len(q2['options'])-4} more options")
            print(f"Reasons: {reason}")
            print()
    else:
        print("PASS — no within-category rephrases found")
    
    # ── CHECK 2: Cross-category with same family ─────────────────────────
    print("=" * 80)
    print("CHECK 2: CROSS-CATEGORY (SAME FAMILY) REPHRASE DETECTION")
    print("=" * 80)
    
    by_family = defaultdict(list)
    for q in QUESTIONS_POOL_ENHANCED:
        fam = category_family(q.get('category', ''))
        by_family[fam].append(q)
    
    cross_flagged = []
    for fam, qs in by_family.items():
        cats_in_fam = set(q.get('category','') for q in qs)
        if len(cats_in_fam) < 2:
            continue
        # Only compare across different categories
        for i, q1 in enumerate(qs):
            for q2 in qs[i+1:]:
                if q1.get('category','') == q2.get('category',''):
                    continue  # already checked in CHECK 1
                is_sim, score, reason = are_semantically_similar(q1, q2)
                if is_sim and score >= 0.6:  # higher threshold for cross-category
                    cross_flagged.append((score, q1.get('category',''), q2.get('category',''), q1, q2, reason))
    
    cross_flagged.sort(key=lambda x: -x[0])
    
    if cross_flagged:
        print(f"\nFLAGGED: {len(cross_flagged)} cross-category rephrase pairs\n")
        for idx, (score, cat1, cat2, q1, q2, reason) in enumerate(cross_flagged, 1):
            print(f"--- PAIR {idx} (score={score:.2f}) ---")
            print(f"Q{q1['question_id']} [{cat1}]: {q1['question_text']}")
            print(f"Q{q2['question_id']} [{cat2}]: {q2['question_text']}")
            print(f"Reasons: {reason}")
            print()
    else:
        print("PASS — no cross-category rephrases found")
    
    # ── CHECK 3: Near-duplicate option text across all questions ─────────
    print("=" * 80)
    print("CHECK 3: NEAR-DUPLICATE OPTION TEXT (cross-question)")
    print("=" * 80)
    
    # Build option index: normalized text -> [(qid, oid, original)]
    opt_index = defaultdict(list)
    for q in QUESTIONS_POOL_ENHANCED:
        for o in q.get('options', []):
            norm = normalize(o.get('option_text', ''))
            if len(norm) < 10:
                continue
            if norm in ("i dont see what i want", "none of these interest me",
                         "im not sure yet", "none of the above", "skip"):
                continue
            opt_index[norm].append((q['question_id'], o.get('option_id', 0), o.get('option_text', '')))
    
    exact_opt_dupes = {k: v for k, v in opt_index.items() if len(v) > 1}
    
    # Also check fuzzy option matches
    opt_word_sets = []
    for q in QUESTIONS_POOL_ENHANCED:
        for o in q.get('options', []):
            t = o.get('option_text', '').strip()
            if len(t) < 15:
                continue
            if normalize(t) in ("i dont see what i want", "none of these interest me",
                                 "im not sure yet", "none of the above", "skip"):
                continue
            ws = content_word_set(t)
            if ws:
                opt_word_sets.append((q['question_id'], o.get('option_id', 0), t, ws))
    
    fuzzy_opt_dupes = []
    seen_pairs = set()
    for i in range(len(opt_word_sets)):
        for j in range(i+1, len(opt_word_sets)):
            qid1, oid1, t1, ws1 = opt_word_sets[i]
            qid2, oid2, t2, ws2 = opt_word_sets[j]
            if qid1 == qid2:
                continue
            if (oid1, oid2) in seen_pairs:
                continue
            j_score = jaccard(ws1, ws2)
            if j_score >= 0.7:  # very high option similarity
                seen_pairs.add((oid1, oid2))
                fuzzy_opt_dupes.append((j_score, qid1, oid1, t1, qid2, oid2, t2))
    
    fuzzy_opt_dupes.sort(key=lambda x: -x[0])
    
    if exact_opt_dupes:
        print(f"\nExact duplicate option texts: {len(exact_opt_dupes)}")
        for norm, entries in sorted(exact_opt_dupes.items(), key=lambda x: -len(x[1]))[:30]:
            qids = [f"Q{e[0]}" for e in entries]
            print(f"  [{', '.join(qids)}] \"{entries[0][2]}\"")
    else:
        print("No exact duplicate option texts")
    
    print()
    if fuzzy_opt_dupes:
        print(f"Fuzzy near-duplicate options (Jaccard >= 0.7): {len(fuzzy_opt_dupes)}")
        for score, qid1, oid1, t1, qid2, oid2, t2 in fuzzy_opt_dupes[:50]:
            print(f"  [{score:.2f}] Q{qid1}/opt{oid1}: \"{t1}\"")
            print(f"          Q{qid2}/opt{oid2}: \"{t2}\"")
    else:
        print("No fuzzy near-duplicate options")
    
    # ── Summary ──────────────────────────────────────────────────────────
    print()
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Within-category rephrase pairs: {len(all_flagged)}")
    print(f"Cross-category rephrase pairs:  {len(cross_flagged)}")
    print(f"Exact duplicate options:        {len(exact_opt_dupes)}")
    print(f"Fuzzy duplicate options:        {len(fuzzy_opt_dupes)}")
    total = len(all_flagged) + len(cross_flagged)
    if total > 0:
        print(f"\n⚠ TOTAL QUESTION-LEVEL ISSUES: {total}")
        print("\nUnique question IDs flagged:")
        flagged_ids = set()
        for _, cat, q1, q2, _ in all_flagged:
            flagged_ids.add(q1['question_id'])
            flagged_ids.add(q2['question_id'])
        for _, _, _, q1, q2, _ in cross_flagged:
            flagged_ids.add(q1['question_id'])
            flagged_ids.add(q2['question_id'])
        print(f"  {sorted(flagged_ids)}")
    else:
        print("\n✓ ALL CLEAN — no rephrase/redundancy issues detected")

if __name__ == '__main__':
    main()
