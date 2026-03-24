import os
filepath = r'C:\Users\USer\Downloads\capstone-back-end\Course-Recommendation-System\backend\data\questions_enhanced.py'
print(f'File exists: {os.path.exists(filepath)}')
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()
print(f'File size: {len(content)}')

start = content.find('_REPLACEMENT_BATCH_30 = [')
end = content.find('QUESTIONS_POOL_ENHANCED.extend(_REPLACEMENT_BATCH_30)')
print(f'Batch30 start: {start}, end: {end}')

if start >= 0 and end >= 0:
    batch_section = content[start:end]
    count = batch_section.count('"text": ')
    print(f'Found {count} occurrences of text key')
    fixed = batch_section.replace('"text": ', '"option_text": ')
    content = content[:start] + fixed + content[end:]
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Replaced {count} occurrences. DONE.')
else:
    print('ERROR: Could not find batch 30 markers')
