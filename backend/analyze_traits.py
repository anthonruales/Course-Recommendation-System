import sys
sys.path.insert(0, '.')
from data.questions_enhanced import QUESTIONS_POOL_ENHANCED

# Find the 0-trait options
print("=== Questions with 0-trait options ===")
for q in QUESTIONS_POOL_ENHANCED:
    for opt in q['options']:
        if len(opt['trait_tags']) == 0:
            print(f"Q{q['question_id']}: option {opt['option_id']} has 0 traits")

print("\n=== Early affected questions (Q1-Q130) ===")
for q in QUESTIONS_POOL_ENHANCED:
    traits_per_opt = [len(opt['trait_tags']) for opt in q['options']]
    min_t = min(traits_per_opt)
    if min_t < 4 and q['question_id'] <= 130:
        print(f"Q{q['question_id']}: min={min_t}, all={traits_per_opt}")

print("\n=== Transition zone Q360-Q400 ===")
for q in QUESTIONS_POOL_ENHANCED:
    if 360 <= q['question_id'] <= 400:
        traits_per_opt = [len(opt['trait_tags']) for opt in q['options']]
        min_t = min(traits_per_opt)
        max_t = max(traits_per_opt)
        print(f"Q{q['question_id']}: min={min_t}, max={max_t}, all={traits_per_opt}")

print("\n=== Transition zone Q570-Q590 ===")
for q in QUESTIONS_POOL_ENHANCED:
    if 570 <= q['question_id'] <= 590:
        traits_per_opt = [len(opt['trait_tags']) for opt in q['options']]
        min_t = min(traits_per_opt)
        max_t = max(traits_per_opt)
        print(f"Q{q['question_id']}: min={min_t}, max={max_t}, all={traits_per_opt}")

# The creative skills questions from the screenshots  
print("\n=== Creative Skills (Q664-Q670) from screenshots ===")
for q in QUESTIONS_POOL_ENHANCED:
    if 664 <= q['question_id'] <= 670:
        print(f"\nQ{q['question_id']}: {q['question_text']}")
        for opt in q['options']:
            print(f"  opt {opt['option_id']}: {len(opt['trait_tags'])} traits - {opt['trait_tags']}")
