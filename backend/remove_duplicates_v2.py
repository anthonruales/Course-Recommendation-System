"""
Safely remove duplicate questions from questions_enhanced.py
Uses line-based approach: find each question_id, track braces to find full block, remove it.
"""
import os
import re

REMOVE_IDS = {2031, 2781}

filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "questions_enhanced.py")

with open(filepath, "r", encoding="utf-8") as f:
    lines = f.readlines()

print(f"Original file: {len(lines)} lines")

# For each question_id to remove, find its line range
ranges_to_remove = []  # list of (start_line, end_line) 0-indexed inclusive

for qid in sorted(REMOVE_IDS):
    # Find the line containing "question_id": qid
    qid_line = None
    for i, line in enumerate(lines):
        # Match "question_id": 71, or "question_id": 71 (with possible whitespace)
        if re.search(rf'"question_id"\s*:\s*{qid}\s*,', line):
            qid_line = i
            break
    
    if qid_line is None:
        print(f"  WARNING: Q{qid} not found in file!")
        continue
    
    # Walk backwards from qid_line to find the opening { of this dict
    start = qid_line
    for j in range(qid_line, -1, -1):
        stripped = lines[j].strip()
        if stripped.startswith("{"):
            start = j
            break
        # Also check if the line before has the opening brace
        if "{" in stripped and '"question_id"' not in stripped:
            start = j
            break
    
    # Also check if the { is on the same line or one before
    # The pattern is typically:
    #     {
    #         "question_id": 71,
    # or  {  "question_id": 71,
    # Let's check the line before the question_id line
    if start == qid_line:
        # Check if opening brace is on the line before
        for j in range(qid_line - 1, max(qid_line - 3, -1), -1):
            if "{" in lines[j] and "}" not in lines[j]:
                start = j
                break
    
    # Now find the closing } of this dict by counting braces from start
    depth = 0
    end = start
    found_close = False
    for j in range(start, len(lines)):
        for ch in lines[j]:
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    end = j
                    found_close = True
                    break
        if found_close:
            break
    
    # Check if the next line is just a comma or the closing } has a trailing comma
    # The dict entry in the list ends with },
    # Check if line after end is empty or starts with {
    if end + 1 < len(lines) and lines[end + 1].strip() == "":
        end += 1  # Include trailing blank line
    
    # Verify the block contains the right question_id
    block = "".join(lines[start:end + 1])
    if f'"question_id": {qid}' in block or f'"question_id":{qid}' in block:
        ranges_to_remove.append((start, end, qid))
        print(f"  Q{qid}: lines {start + 1}-{end + 1} ({end - start + 1} lines)")
    else:
        print(f"  WARNING: Block verification failed for Q{qid}")

# Sort ranges in reverse order so removing doesn't shift indices
ranges_to_remove.sort(key=lambda x: x[0], reverse=True)

# Remove the ranges
for start, end, qid in ranges_to_remove:
    del lines[start:end + 1]

print(f"\nNew file: {len(lines)} lines")

# Write the result
with open(filepath, "w", encoding="utf-8") as f:
    f.writelines(lines)

print(f"File updated: {filepath}")

# Verify by importing
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Clear cached module
if "data.questions_enhanced" in sys.modules:
    del sys.modules["data.questions_enhanced"]
if "data" in sys.modules:
    del sys.modules["data"]

from data.questions_enhanced import QUESTIONS_POOL_ENHANCED
print(f"\nVerification: {len(QUESTIONS_POOL_ENHANCED)} questions loaded")

remaining_ids = {q["question_id"] for q in QUESTIONS_POOL_ENHANCED}
all_ok = True
for qid in sorted(REMOVE_IDS):
    if qid in remaining_ids:
        print(f"  ERROR: Q{qid} still present!")
        all_ok = False
    else:
        print(f"  OK: Q{qid} removed")

if all_ok:
    print("\n  ALL 12 DUPLICATES SUCCESSFULLY REMOVED!")
else:
    print("\n  SOME REMOVALS FAILED - check errors above")
