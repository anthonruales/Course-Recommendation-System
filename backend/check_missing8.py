import sys, os
sys.path.insert(0, '.')
from data.questions_enhanced import QUESTIONS_POOL_ENHANCED
from services.adaptive_assessment import TRAIT_TO_BRANCH

q_by_id = {q['question_id']: q for q in QUESTIONS_POOL_ENHANCED}
missing = [5266, 5268, 5269, 5274, 5276, 5278, 5280, 5285]
for qid in missing:
    q = q_by_id.get(qid)
    if not q:
        print(f"Q{qid}: NOT FOUND in pool")
        continue
    traits = set()
    for opt in q.get('options', []):
        tt = opt.get('trait_tags', {})
        if isinstance(tt, dict):
            traits.update(tt.keys())
        elif isinstance(tt, list):
            traits.update(tt)
    unmapped = [t for t in traits if t not in TRAIT_TO_BRANCH]
    mapped = [t for t in traits if t in TRAIT_TO_BRANCH]
    print(f"Q{qid} cat={q.get('category','?')}")
    print(f"  Mapped: {sorted(mapped)}")
    print(f"  UNMAPPED: {sorted(unmapped)}")
