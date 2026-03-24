"""Quick check for remaining rephrases in specific categories."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from data.questions_enhanced import QUESTIONS_POOL_ENHANCED

# Check Medical Technology
print("=== Medical Technology & Lab Science ===")
for q in QUESTIONS_POOL_ENHANCED:
    if 'Medical Technology' in q.get('category', ''):
        print(f"  Q{q['question_id']}: {q['question_text']}")

# Check all remaining within-category same-topic pairs
# Focus on patterns like "What excites/interests/appeals/draws you about X"
from collections import defaultdict
import re

by_cat = defaultdict(list)
for q in QUESTIONS_POOL_ENHANCED:
    by_cat[q.get('category', '')].append(q)

INTEREST_PATTERN = re.compile(
    r'(excit|interest|appeal|draw|attract|fascinat|part of|area of|aspect of|side of|type of)',
    re.IGNORECASE
)

print("\n=== Categories with 2+ interest-type questions ===")
for cat, qs in sorted(by_cat.items()):
    interest_qs = [q for q in qs if INTEREST_PATTERN.search(q['question_text'])]
    if len(interest_qs) >= 2:
        print(f"\n[{cat}] ({len(interest_qs)} interest-type questions)")
        for q in interest_qs:
            print(f"  Q{q['question_id']}: {q['question_text']}")
