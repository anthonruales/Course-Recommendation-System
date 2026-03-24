"""
Remove duplicate/redundant questions from QUESTIONS_POOL_ENHANCED.

Duplicates identified by check_duplicates.py:
  Q71  (dup of Q31)  - favorite subject
  Q72  (dup of Q32)  - challenging subject
  Q52  (dup of Q36)  - board exam
  Q414 (dup of Q275) - area of law
  Q633 (dup of Q275) - area of law
  Q634 (dup of Q418) - legal career path
  Q639 (dup of Q438) - tourism sector
  Q642 (dup of Q424) - culinary specialization
  Q919 (dup of Q861) - engineer type
  Q920 (dup of Q864) - engineering subject
  Q911 (dup of Q853) - geodetic engineering
  Q915 (dup of Q857) - aircraft maintenance
"""

import sys
import os
import re

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

REMOVE_IDS = {71, 72, 52, 414, 633, 634, 639, 642, 919, 920, 911, 915}

# ── Step 1: Preview ──
from data.questions_enhanced import QUESTIONS_POOL_ENHANCED

print("Questions to REMOVE:")
for q in QUESTIONS_POOL_ENHANCED:
    if q["question_id"] in REMOVE_IDS:
        cat = q.get("category", "?")
        txt = q["question_text"][:70]
        print(f"  Q{q['question_id']:>4d} [{cat}] {txt}")

original_count = len(QUESTIONS_POOL_ENHANCED)
remaining = [q for q in QUESTIONS_POOL_ENHANCED if q["question_id"] not in REMOVE_IDS]
print(f"\nOriginal: {original_count} questions")
print(f"After:    {len(remaining)} questions  (-{original_count - len(remaining)})")

# ── Step 2: Remove from file ──
filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "questions_enhanced.py")

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Each question block starts with { and "question_id": N
# We'll find and remove entire dict entries for each ID
for qid in sorted(REMOVE_IDS):
    # Pattern: match the dict entry for this question_id
    # The dict starts with {  (possibly with whitespace/newline before it)
    # and contains "question_id": qid
    # and ends with },  (closing the dict in the list)
    
    # Strategy: find "question_id": qid, then find the enclosing { ... },
    pattern = rf'(\s*\{{\s*\n\s*"question_id"\s*:\s*{qid}\s*,)'
    match = re.search(pattern, content)
    if not match:
        print(f"  WARNING: Could not find Q{qid} in file!")
        continue
    
    # Find the start of this dict (the opening brace)
    start = match.start()
    
    # Now find the matching closing brace
    # We need to count braces from the { we found
    brace_pos = content.index("{", start)
    depth = 0
    end = brace_pos
    for i in range(brace_pos, len(content)):
        if content[i] == "{":
            depth += 1
        elif content[i] == "}":
            depth -= 1
            if depth == 0:
                end = i
                break
    
    # Include the trailing comma and whitespace
    after = end + 1
    while after < len(content) and content[after] in " \t":
        after += 1
    if after < len(content) and content[after] == ",":
        after += 1
    # Also consume trailing newline
    while after < len(content) and content[after] in "\r\n":
        after += 1
    
    removed_text = content[start:after]
    # Verify it's the right question
    if f'"question_id": {qid}' in removed_text or f'"question_id":{qid}' in removed_text:
        content = content[:start] + content[after:]
        print(f"  Removed Q{qid} ({len(removed_text)} chars)")
    else:
        print(f"  WARNING: Mismatch for Q{qid}, skipping")

# ── Step 3: Write back ──
# Backup first
backup_path = filepath + ".bak"
with open(filepath, "r", encoding="utf-8") as f:
    original_content = f.read()
with open(backup_path, "w", encoding="utf-8") as f:
    f.write(original_content)
print(f"\nBackup saved to: {backup_path}")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)
print(f"Updated file written: {filepath}")

# ── Step 4: Verify ──
# Re-import to check
import importlib
import data.questions_enhanced
importlib.reload(data.questions_enhanced)
from data.questions_enhanced import QUESTIONS_POOL_ENHANCED as UPDATED

print(f"\nVerification: {len(UPDATED)} questions loaded after edit")
remaining_ids = {q["question_id"] for q in UPDATED}
for qid in REMOVE_IDS:
    if qid in remaining_ids:
        print(f"  ERROR: Q{qid} still present!")
    else:
        print(f"  OK: Q{qid} removed successfully")
