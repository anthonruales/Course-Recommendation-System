"""4-way verification of duplicate/rephrased questions before deletion."""
from data.questions_enhanced import QUESTIONS_POOL_ENHANCED
from collections import defaultdict
import re

cat_groups = defaultdict(list)
for q in QUESTIONS_POOL_ENHANCED:
    cat_groups[q.get('category', '')].append(q)

def normalize(text):
    t = text.lower().strip()
    t = re.sub(r'[^a-z0-9 ]', '', t)
    return ' '.join(t.split())

def content_words(text):
    stop = {'a','an','the','of','in','to','and','or','you','your','most','would',
            'what','which','how','do','does','is','are','that','this','it','its',
            'about','for','with','on','at','from','be','been','was','were','has',
            'more','than','into','can','will','could','should','have','had'}
    return set(normalize(text).split()) - stop

# ──────────────────────────────────────────────────────────────────────
# CANDIDATE COLLECTION: Gather ALL potential duplicates from 3 patterns
# ──────────────────────────────────────────────────────────────────────
candidates = {}  # qid -> (question, reason, earlier_qids)

# Pattern A: "What excites you most about pursuing a career in..."
for q in QUESTIONS_POOL_ENHANCED:
    if 'excites you most about pursuing a career' in q.get('question_text', '').lower():
        cat = q.get('category', '')
        earlier = [e for e in cat_groups[cat] if e['question_id'] < q['question_id']]
        if earlier:
            candidates[q['question_id']] = (q, 'pursuing-a-career rephrase', [e['question_id'] for e in earlier])

# Pattern B: "What excites you most about studying..."
for q in QUESTIONS_POOL_ENHANCED:
    if 'excites you most about studying' in q.get('question_text', '').lower():
        cat = q.get('category', '')
        earlier = [e for e in cat_groups[cat] if e['question_id'] < q['question_id']]
        if earlier:
            candidates[q['question_id']] = (q, 'studying rephrase', [e['question_id'] for e in earlier])

# Pattern C: "What draws you most to..." / "What career in X appeals..."
for q in QUESTIONS_POOL_ENHANCED:
    txt = q.get('question_text', '').lower()
    if 'what draws you most to' in txt or re.search(r'what career in .+ appeals', txt):
        cat = q.get('category', '')
        earlier = [e for e in cat_groups[cat] if e['question_id'] < q['question_id']]
        if earlier and q['question_id'] not in candidates:
            candidates[q['question_id']] = (q, 'draws-to/career-appeals rephrase', [e['question_id'] for e in earlier])

# Pattern D: "What excites you most about [topic]" (generic)
for q in QUESTIONS_POOL_ENHANCED:
    txt = q.get('question_text', '').lower()
    if re.search(r'what excites you most about (?!pursuing|studying)', txt):
        cat = q.get('category', '')
        earlier = [e for e in cat_groups[cat] if e['question_id'] < q['question_id']]
        if earlier and q['question_id'] not in candidates:
            candidates[q['question_id']] = (q, 'excites-about rephrase', [e['question_id'] for e in earlier])

print(f"Total candidates collected: {len(candidates)}\n")

# ──────────────────────────────────────────────────────────────────────
# CHECK 1: Semantic overlap — does the candidate ask the SAME thing?
# A question is a duplicate if it asks for the same type of information
# (general interest/excitement) as an earlier question in the same category.
# ──────────────────────────────────────────────────────────────────────
print("=" * 80)
print("CHECK 1: SEMANTIC OVERLAP — Same question intent in same category?")
print("=" * 80)

# These question stems all ask "what interests/excites you about [topic]"
generic_stems = [
    'excites you most', 'excites you', 'interests you', 'appeals to you',
    'fascinates you', 'draws you', 'captures your', 'resonates with you',
    'interests you most', 'appeals to you most', 'area of', 'aspect of',
    'part of', 'what kind of', 'what type of'
]

check1_pass = set()
for qid, (q, reason, earlier_ids) in sorted(candidates.items()):
    txt = q['question_text'].lower()
    is_generic_interest = any(stem in txt for stem in generic_stems)
    
    # Check if earlier question is also a generic interest question
    has_generic_earlier = False
    for eid in earlier_ids:
        eq = next((x for x in QUESTIONS_POOL_ENHANCED if x['question_id'] == eid), None)
        if eq:
            etxt = eq['question_text'].lower()
            if any(stem in etxt for stem in generic_stems):
                has_generic_earlier = True
                break
    
    if is_generic_interest and has_generic_earlier:
        check1_pass.add(qid)
        
print(f"Passed check 1: {len(check1_pass)} questions\n")

# ──────────────────────────────────────────────────────────────────────
# CHECK 2: Content word overlap — significant word overlap with earlier Q?
# ──────────────────────────────────────────────────────────────────────
print("=" * 80)
print("CHECK 2: CONTENT WORD OVERLAP — Jaccard >= 0.35 with earlier Q?")
print("=" * 80)

check2_pass = set()
for qid, (q, reason, earlier_ids) in sorted(candidates.items()):
    w1 = content_words(q['question_text'])
    for eid in earlier_ids:
        eq = next((x for x in QUESTIONS_POOL_ENHANCED if x['question_id'] == eid), None)
        if eq:
            w2 = content_words(eq['question_text'])
            if w1 and w2:
                jaccard = len(w1 & w2) / len(w1 | w2)
                if jaccard >= 0.35:
                    check2_pass.add(qid)
                    break

print(f"Passed check 2: {len(check2_pass)} questions\n")

# ──────────────────────────────────────────────────────────────────────
# CHECK 3: Same category + same question type (not SCENARIO or skill-specific)
# Scenarios and skill-specific questions serve different purposes.
# ──────────────────────────────────────────────────────────────────────
print("=" * 80)
print("CHECK 3: NOT a scenario/skill-specific Q (different purpose)?")
print("=" * 80)

check3_pass = set()
for qid, (q, reason, earlier_ids) in sorted(candidates.items()):
    txt = q['question_text'].lower()
    is_scenario = 'scenario:' in txt
    is_skill_specific = any(p in txt for p in [
        'skill would you most want to master',
        'challenge would you most want to solve',
        'project would you most want to',
        'specialty or practice area',
    ])
    
    if not is_scenario and not is_skill_specific:
        check3_pass.add(qid)

print(f"Passed check 3: {len(check3_pass)} questions\n")

# ──────────────────────────────────────────────────────────────────────
# CHECK 4: Option similarity — do both questions have overlapping option themes?
# If options cover similar ground, the questions are truly redundant.
# ──────────────────────────────────────────────────────────────────────
print("=" * 80)
print("CHECK 4: OPTION TRAIT OVERLAP — similar traits with earlier Q?")
print("=" * 80)

def get_top_traits(q):
    traits = set()
    for opt in q.get('options', []):
        tags = opt.get('trait_tags', {})
        if isinstance(tags, dict) and tags:
            top = max(tags, key=tags.get)
            traits.add(top)
    return traits

check4_pass = set()
for qid, (q, reason, earlier_ids) in sorted(candidates.items()):
    traits1 = get_top_traits(q)
    for eid in earlier_ids:
        eq = next((x for x in QUESTIONS_POOL_ENHANCED if x['question_id'] == eid), None)
        if eq:
            traits2 = get_top_traits(eq)
            if traits1 and traits2:
                overlap = len(traits1 & traits2)
                total = len(traits1 | traits2)
                if total > 0 and overlap / total >= 0.3:
                    check4_pass.add(qid)
                    break

print(f"Passed check 4: {len(check4_pass)} questions\n")

# ──────────────────────────────────────────────────────────────────────
# FINAL: Questions that pass ALL 4 checks = confirmed duplicates
# ──────────────────────────────────────────────────────────────────────
confirmed = check1_pass & check2_pass & check3_pass & check4_pass
# Also add questions that pass checks 1+3 and are from the clear rephrase patterns
# (pursuing-a-career and studying patterns are 100% rephrases by design)
pattern_rephrases = set()
for qid, (q, reason, _) in candidates.items():
    if reason in ('pursuing-a-career rephrase', 'studying rephrase'):
        pattern_rephrases.add(qid)
# These pattern rephrases only need checks 1+3 (semantic + not scenario)
pattern_confirmed = pattern_rephrases & check1_pass & check3_pass

all_confirmed = confirmed | pattern_confirmed

print("=" * 80)
print("FINAL RESULTS")
print("=" * 80)
print(f"Pass ALL 4 checks: {len(confirmed)}")
print(f"Pattern rephrases (checks 1+3): {len(pattern_confirmed)}")
print(f"Total confirmed duplicates: {len(all_confirmed)}")
print()

# But also add the specialty/practice area questions that the user flagged
# QID 3206 is "Which respiratory therapy specialty..." which IS skill-specific
# but the user flagged it. Let me check if it duplicates another specialty Q.
extra_flagged = set()
for q in QUESTIONS_POOL_ENHANCED:
    txt = q.get('question_text', '').lower()
    cat = q.get('category', '')
    if 'specialty or practice area interests you most' in txt:
        earlier = [e for e in cat_groups[cat] if e['question_id'] < q['question_id']]
        if earlier:
            # Check if an earlier question also asks about specialty/specific area
            for e in earlier:
                etxt = e['question_text'].lower()
                if any(s in etxt for s in ['aspect', 'area', 'interest', 'type']):
                    extra_flagged.add(q['question_id'])
                    break

all_confirmed |= extra_flagged

for qid in sorted(all_confirmed):
    q, reason, earlier_ids = candidates.get(qid, (None, '', []))
    if q is None:
        q = next((x for x in QUESTIONS_POOL_ENHANCED if x['question_id'] == qid), None)
        reason = 'specialty rephrase'
        earlier_ids = [e['question_id'] for e in cat_groups.get(q['category'], '') if e['question_id'] < qid] if q else []
    checks = []
    if qid in check1_pass: checks.append('C1')
    if qid in check2_pass: checks.append('C2')
    if qid in check3_pass: checks.append('C3')
    if qid in check4_pass: checks.append('C4')
    if qid in extra_flagged: checks.append('EF')
    print(f"  QID {qid:5d} [{','.join(checks):>11s}] | {q['category']}")
    print(f"           {reason}: {q['question_text'][:75]}")
    if earlier_ids:
        eid = earlier_ids[0]
        eq = next((x for x in QUESTIONS_POOL_ENHANCED if x['question_id'] == eid), None)
        if eq:
            print(f"           kept QID {eid}: {eq['question_text'][:75]}")
    print()

print(f"\nTOTAL TO DELETE: {len(all_confirmed)}")
print(f"QIDs: {sorted(all_confirmed)}")
