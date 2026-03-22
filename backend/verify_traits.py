import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data.questions_enhanced import QUESTIONS_POOL_ENHANCED

under4 = []
for q in QUESTIONS_POOL_ENHANCED:
    for opt in q['options']:
        if len(opt['trait_tags']) < 4:
            under4.append((q['question_id'], opt['option_id'], len(opt['trait_tags'])))

if under4:
    print(f"Still {len(under4)} options with < 4 traits:")
    for qid, oid, cnt in under4[:30]:
        print(f"  Q{qid} opt {oid}: {cnt} traits")
    if len(under4) > 30:
        print(f"  ... and {len(under4) - 30} more")
else:
    print("SUCCESS: All options have 4+ traits!")

# Summary stats
all_counts = []
for q in QUESTIONS_POOL_ENHANCED:
    for opt in q['options']:
        all_counts.append(len(opt['trait_tags']))

print(f"\nTotal questions: {len(QUESTIONS_POOL_ENHANCED)}")
print(f"Total options: {len(all_counts)}")
print(f"Min traits per option: {min(all_counts)}")
print(f"Max traits per option: {max(all_counts)}")
print(f"Average traits per option: {sum(all_counts)/len(all_counts):.1f}")

# Distribution
from collections import Counter
dist = Counter(all_counts)
for k in sorted(dist):
    print(f"  {k} traits: {dist[k]} options")
