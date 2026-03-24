import sys
sys.path.insert(0, '.')
from data.questions_enhanced import QUESTIONS_POOL_ENHANCED

ids_to_find = [875, 2301, 938, 2896, 964, 3056, 967, 3111, 962, 2996, 971, 3206, 943, 2751, 809, 1431, 965, 3086, 970, 3231]

q_map = {q['question_id']: q for q in QUESTIONS_POOL_ENHANCED if q['question_id'] in ids_to_find}

for qid in ids_to_find:
    q = q_map.get(qid)
    if q:
        print(f"=== Q{qid} ===")
        print(f"Category: {q['category']}")
        print(f"Text: {q['question_text']}")
        for opt in q.get('options', []):
            print(f"  [{opt['option_id']}] {opt['option_text']}")
        print()
    else:
        print(f"=== Q{qid} === NOT FOUND")
        print()
