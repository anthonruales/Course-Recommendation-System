import json

with open('removed_full_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for q in data['removed_questions'][:8]:
    print(f'Q{q["question_id"]} [{q["category"]}]')
    print(f'  Text: {q["question_text"]}')
    print(f'  Parent Q{q["parent_id"]}: {q["parent_text"]}')
    print(f'  Options ({q["option_count"]}):')
    for o in q['options'][:4]:
        tags = o.get('trait_tags', {})
        sorted_tags = sorted(tags.items(), key=lambda x: -x[1])[:3]
        print(f'    - {o["option_text"][:60]}')
        print(f'      Tags: {sorted_tags}')
    print()
