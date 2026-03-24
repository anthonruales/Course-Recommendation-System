import json
with open('removed_full_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
for q in data['removed_questions']:
    oc = q['option_count']
    print(f"Q{q['question_id']:4d} | {q['category'][:50]:50s} | {oc} opts | {q['question_text'][:60]}")
    print(f"       parent Q{q['parent_id']}: {q['parent_text'][:60]}")
