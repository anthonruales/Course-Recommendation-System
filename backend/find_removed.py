"""
Find ALL 88 removed questions by parsing the source file directly.
The expansion builders may have already been deduped, so some removed IDs
aren't in the builder output. We need to search the raw source.
"""
import sys, os, re, json
sys.path.insert(0, os.path.dirname(__file__))

from data.questions_enhanced import _MANUAL_REMOVE_IDS, QUESTIONS_POOL_ENHANCED

# Read the entire source file 
src_path = os.path.join(os.path.dirname(__file__), "data", "questions_enhanced.py")

# Strategy: parse the source to find question dicts with matching IDs
# Questions are defined as dicts with "question_id": <id>
# We'll search for each removed ID

found = {}  # id -> {category, text, traits}
current_pool_by_id = {q["question_id"]: q for q in QUESTIONS_POOL_ENHANCED}

# Read source in chunks and find question_id patterns
with open(src_path, "r", encoding="utf-8") as f:
    content = f.read()

# Find all question definitions - they follow the pattern:
# "question_id": <number>,
# "question_text": "...",  
# "category": "...",
for qid in sorted(_MANUAL_REMOVE_IDS):
    # Search for the question_id definition
    pattern = rf'"question_id":\s*{qid}\s*,'
    matches = list(re.finditer(pattern, content))
    
    if not matches:
        print(f"Q{qid}: NOT FOUND IN SOURCE")
        continue
    
    for m in matches:
        # Extract surrounding context to get question_text and category
        start = max(0, m.start() - 50)
        end = min(len(content), m.end() + 2000)
        ctx = content[start:end]
        
        # Extract question_text
        text_match = re.search(r'"question_text":\s*"([^"]*(?:\\.[^"]*)*)"', ctx)
        cat_match = re.search(r'"category":\s*"([^"]*)"', ctx)
        
        q_text = text_match.group(1) if text_match else "UNKNOWN"
        q_cat = cat_match.group(1) if cat_match else "UNKNOWN"
        
        # Extract option texts
        options = []
        opt_pattern = r'"option_text":\s*"([^"]*(?:\\.[^"]*)*)"'
        for opt_m in re.finditer(opt_pattern, ctx):
            options.append(opt_m.group(1))
        
        # Extract trait tags
        traits = set()
        trait_pattern = r'"([A-Z][a-zA-Z]+-[A-Z][a-zA-Z-]*)":\s*[\d.]+'
        for trait_m in re.finditer(trait_pattern, ctx):
            traits.add(trait_m.group(1))
        
        found[qid] = {
            "question_id": qid,
            "category": q_cat,
            "question_text": q_text,
            "option_count": len(options),
            "option_texts": options[:6],  # max 6 options
            "traits": sorted(traits),
        }
        break  # Take first match

print(f"\n=== Found {len(found)} of {len(_MANUAL_REMOVE_IDS)} removed questions ===\n")

# Group by category
from collections import defaultdict
by_cat = defaultdict(list)
for qid, info in sorted(found.items()):
    by_cat[info["category"]].append(info)

print(f"Categories affected: {len(by_cat)}\n")

for cat in sorted(by_cat.keys()):
    qs = by_cat[cat]
    print(f"\n[{cat}] - {len(qs)} removed")
    for q in qs:
        print(f"  Q{q['question_id']}: {q['question_text'][:80]}")
        print(f"    Options({q['option_count']}): {[o[:40] for o in q['option_texts'][:3]]}...")
        print(f"    Traits: {q['traits'][:5]}...")

# Also show what the "parent" question was (the one it was a rephrase of)
print(f"\n\n=== Parent questions (what each removed Q was a rephrase of) ===")
# Read the _MANUAL_REMOVE_IDS comments from source
remove_section = re.search(r'_MANUAL_REMOVE_IDS\s*=\s*\{([^}]+)\}', content)
if remove_section:
    for line in remove_section.group(1).split('\n'):
        line = line.strip()
        if line and '#' in line:
            # Extract ID and comment
            id_match = re.match(r'(\d+)', line)
            comment = line.split('#', 1)[1].strip() if '#' in line else ''
            if id_match:
                qid = int(id_match.group(1))
                parent_match = re.search(r'Q(\d+)', comment)
                parent_id = int(parent_match.group(1)) if parent_match else None
                parent_q = current_pool_by_id.get(parent_id) if parent_id else None
                parent_text = parent_q["question_text"][:60] if parent_q else "NOT IN POOL"
                print(f"  Q{qid} -> rephrase of Q{parent_id}: {parent_text}")

# Save full data for replacement generation
with open("removed_full_data.json", "w", encoding="utf-8") as f:
    json.dump(found, f, indent=2, ensure_ascii=False, default=str)

print(f"\nSaved to removed_full_data.json")
