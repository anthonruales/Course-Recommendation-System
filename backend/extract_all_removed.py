"""
Complete extraction of all 88 removed questions with their full data.
Outputs a JSON file with all details needed for replacement generation.
"""
import sys, os, re, json
sys.path.insert(0, os.path.dirname(__file__))

import data.questions_enhanced as qe
from data.questions_enhanced import _MANUAL_REMOVE_IDS, QUESTIONS_POOL_ENHANCED

# Get all expansion questions from ALL 25 builders
all_expansion = []
for name in sorted(dir(qe)):
    if name.startswith('_build_') and callable(getattr(qe, name)):
        all_expansion.extend(getattr(qe, name)())

exp_by_id = {q["question_id"]: q for q in all_expansion}

# Get static removed questions from source
src_path = os.path.join(os.path.dirname(__file__), "data", "questions_enhanced.py")
with open(src_path, "r", encoding="utf-8") as f:
    source = f.read()

static_removed_ids = sorted(qid for qid in _MANUAL_REMOVE_IDS if qid < 1169)

static_by_id = {}
for qid in static_removed_ids:
    pattern = rf'"question_id":\s*{qid}\b'
    match = re.search(pattern, source)
    if not match:
        continue
    
    pos = match.start()
    # Find enclosing dict
    start_pos = pos
    brace_count = 0
    for i in range(pos, max(pos - 500, 0), -1):
        if source[i] == '}':
            brace_count += 1
        elif source[i] == '{':
            if brace_count == 0:
                start_pos = i
                break
            brace_count -= 1
    
    brace_count = 0
    end_pos = pos
    for i in range(start_pos, min(start_pos + 8000, len(source))):
        if source[i] == '{':
            brace_count += 1
        elif source[i] == '}':
            brace_count -= 1
            if brace_count == 0:
                end_pos = i + 1
                break
    
    block = source[start_pos:end_pos]
    
    text_m = re.search(r'"question_text":\s*["\'](.+?)["\']', block)
    cat_m = re.search(r'"category":\s*["\'](.+?)["\']', block)
    
    # Parse options more carefully
    options = []
    # Find options array
    opts_start = block.find('"options"')
    if opts_start >= 0:
        # Find each option dict
        opt_pattern = re.compile(
            r'\{\s*"option_id":\s*(\d+)\s*,\s*"option_text":\s*["\'](.+?)["\']\s*,\s*"trait_tags":\s*\{([^}]*)\}',
            re.DOTALL
        )
        for om in opt_pattern.finditer(block[opts_start:]):
            traits = {}
            for tm in re.finditer(r'["\']([^"\']+)["\']\s*:\s*([\d.]+)', om.group(3)):
                traits[tm.group(1)] = float(tm.group(2))
            options.append({
                "option_id": int(om.group(1)),
                "option_text": om.group(2),
                "trait_tags": traits
            })
    
    static_by_id[qid] = {
        "question_id": qid,
        "question_text": text_m.group(1) if text_m else "?",
        "category": cat_m.group(1) if cat_m else "?",
        "options": options
    }

# Combine all removed questions
all_removed = []
for qid in sorted(_MANUAL_REMOVE_IDS):
    if qid in static_by_id:
        all_removed.append(static_by_id[qid])
    elif qid in exp_by_id:
        all_removed.append(exp_by_id[qid])
    else:
        print(f"WARNING: Q{qid} not found anywhere!")

print(f"Total removed questions extracted: {len(all_removed)}")

# Parse the parent mapping from _MANUAL_REMOVE_IDS comments
parent_map = {}
remove_section = re.search(r'_MANUAL_REMOVE_IDS\s*=\s*\{([^}]+)\}', source)
if remove_section:
    for line in remove_section.group(1).split('\n'):
        line = line.strip()
        if not line:
            continue
        id_match = re.match(r'(\d+)', line)
        if id_match:
            qid = int(id_match.group(1))
            parent_match = re.search(r'Q(\d+)', line.split('#', 1)[-1] if '#' in line else '')
            if parent_match:
                parent_map[qid] = int(parent_match.group(1))

# Get current pool data for comparison
current_by_id = {q["question_id"]: q for q in QUESTIONS_POOL_ENHANCED}

# Build the output
output = {
    "removed_questions": [],
    "pool_size": len(QUESTIONS_POOL_ENHANCED),
    "total_removed": len(all_removed),
}

for q in all_removed:
    qid = q["question_id"]
    parent_id = parent_map.get(qid)
    parent_q = current_by_id.get(parent_id, {})
    
    all_traits = set()
    for o in q.get("options", []):
        all_traits.update(o.get("trait_tags", {}).keys())
    
    entry = {
        "question_id": qid,
        "question_text": q["question_text"],
        "category": q["category"],
        "parent_id": parent_id,
        "parent_text": parent_q.get("question_text", ""),
        "parent_category": parent_q.get("category", ""),
        "option_count": len(q.get("options", [])),
        "traits": sorted(all_traits),
        "options": q.get("options", []),
    }
    output["removed_questions"].append(entry)
    
    print(f"Q{qid} [{q['category']}]")
    print(f"  Text: {q['question_text'][:80]}")
    print(f"  Parent: Q{parent_id} - {parent_q.get('question_text', '?')[:60]}")
    print(f"  Options: {len(q.get('options', []))}, Traits: {sorted(all_traits)[:5]}")

with open("removed_full_data.json", "w", encoding="utf-8") as f:
    json.dump(output, f, indent=2, ensure_ascii=False)

print(f"\nSaved complete data for {len(all_removed)} removed questions")

# Also collect ALL existing question texts and option texts for dedup checking
existing_data = {
    "question_texts": [q["question_text"] for q in QUESTIONS_POOL_ENHANCED],
    "option_texts": list(set(
        o["option_text"] 
        for q in QUESTIONS_POOL_ENHANCED 
        for o in q.get("options", [])
    )),
    "categories": list(set(q["category"] for q in QUESTIONS_POOL_ENHANCED)),
}
with open("existing_pool_data.json", "w", encoding="utf-8") as f:
    json.dump(existing_data, f, indent=2, ensure_ascii=False)

print(f"Saved existing pool data: {len(existing_data['question_texts'])} questions, {len(existing_data['option_texts'])} unique options")
