import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from data.questions_enhanced import QUESTIONS_POOL_ENHANCED

qs = QUESTIONS_POOL_ENHANCED
all_oids = [o["option_id"] for q in qs for o in q["options"]]
qids = [q["question_id"] for q in qs]
print(f"Total: {len(qs)}")
print(f"MaxQID: {max(qids)}")
print(f"MaxOID: {max(all_oids)}")
print(f"UniqueQ: {len(set(qids))}")
print(f"UniqueO: {len(set(all_oids))}")
print()
for q in qs[-40:]:
    print(f"  Q{q['question_id']}: {q['category']}")
