"""Fix duplicate questions in questions_enhanced.py."""
with open('questions_enhanced.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all occurrences of TRAIT_SECONDARY_MAP
import re
matches = list(re.finditer(r'^TRAIT_SECONDARY_MAP = \{', content, re.MULTILINE))
print(f"Found {len(matches)} TRAIT_SECONDARY_MAP definitions")

if len(matches) == 2:
    # Keep everything before first match, then everything from second match onwards
    # But we need the list closing ] before TRAIT_SECONDARY_MAP
    first_pos = matches[0].start()
    second_pos = matches[1].start()
    
    # Find the ] that closes QUESTIONS_POOL_ENHANCED before first TRAIT_SECONDARY_MAP
    bracket_before_first = content.rfind(']', 0, first_pos)
    
    # Everything up to and including that ], then the second TRAIT_SECONDARY_MAP onwards
    fixed = content[:bracket_before_first + 1] + "\n\n" + content[second_pos:]
    
    with open('questions_enhanced.py', 'w', encoding='utf-8') as f:
        f.write(fixed)
    print("Fixed! Removed corrupted first TRAIT_SECONDARY_MAP block.")
else:
    print("Unexpected number of matches, not fixing.")
