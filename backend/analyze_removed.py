import json
from collections import Counter

with open('removed_full_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

cats = Counter(q['category'] for q in data['removed_questions'])
print('Categories of removed questions:')
for cat, count in cats.most_common():
    print(f'  {count:2d}  {cat}')
print(f'\nTotal: {len(data["removed_questions"])} across {len(cats)} categories')

trait_counts = Counter()
for q in data['removed_questions']:
    trait_counts.update(q['traits'])
print(f'\nTop traits in removed questions:')
for t, c in trait_counts.most_common(20):
    print(f'  {c:3d}  {t}')
