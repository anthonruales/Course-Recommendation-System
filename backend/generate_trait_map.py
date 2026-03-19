#!/usr/bin/env python3
"""Generate TRAIT_SECONDARY_MAP from QUESTIONS_POOL_ENHANCED"""
import sys
sys.path.insert(0, '.')
from questions_enhanced import QUESTIONS_POOL_ENHANCED

# Build TRAIT_SECONDARY_MAP from questions data
trait_secondary_map = {}

for question in QUESTIONS_POOL_ENHANCED:
    for option in question.get('options', []):
        trait_tags = option.get('trait_tags', {})
        if not trait_tags:
            continue
        
        # Find primary trait (weight 1.0)
        primary_trait = None
        for trait, weight in trait_tags.items():
            if weight == 1.0:
                primary_trait = trait
                break
        
        if not primary_trait:
            continue
        
        # Collect secondary traits
        secondaries = []
        for trait, weight in trait_tags.items():
            if trait != primary_trait and weight < 1.0:
                secondaries.append((trait, weight))
        
        # Add to map, avoiding duplicates
        if primary_trait not in trait_secondary_map:
            trait_secondary_map[primary_trait] = []
        
        for secondary_trait, weight in secondaries:
            # Check if already exists
            exists = False
            for existing_trait, existing_weight in trait_secondary_map[primary_trait]:
                if existing_trait == secondary_trait:
                    exists = True
                    break
            if not exists:
                trait_secondary_map[primary_trait].append((secondary_trait, weight))

# Sort for consistency
for key in trait_secondary_map:
    trait_secondary_map[key].sort(key=lambda x: x[1], reverse=True)

# Generate Python code
code_lines = []
code_lines.append('\n# Auto-generated TRAIT_SECONDARY_MAP from QUESTIONS_POOL_ENHANCED')
code_lines.append('# Maps primary traits to their secondary related traits with weights')
code_lines.append('TRAIT_SECONDARY_MAP = {')

for trait in sorted(trait_secondary_map.keys()):
    secondaries = trait_secondary_map[trait]
    code_lines.append(f'    "{trait}": [')
    for secondary_trait, weight in secondaries:
        code_lines.append(f'        ("{secondary_trait}", {weight}),')
    code_lines.append('    ],')

code_lines.append('}')

# Write to file
with open('questions_enhanced.py', 'a', encoding='utf-8') as f:
    f.write('\n' + '\n'.join(code_lines) + '\n')

print("Successfully added TRAIT_SECONDARY_MAP to questions_enhanced.py")
print(f"Total primary traits: {len(trait_secondary_map)}")
