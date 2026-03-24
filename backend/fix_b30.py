with open('data/questions_enhanced.py', 'r', encoding='utf-8') as f:
    content = f.read()

start = content.find('_REPLACEMENT_BATCH_30 = [')
end = content.find('QUESTIONS_POOL_ENHANCED.extend(_REPLACEMENT_BATCH_30)')

batch_section = content[start:end]
count = batch_section.count('"text": ')
fixed = batch_section.replace('"text": ', '"option_text": ')
content = content[:start] + fixed + content[end:]

with open('data/questions_enhanced.py', 'w', encoding='utf-8') as f:
    f.write(content)

print(f'Replaced {count} occurrences. Done.')
