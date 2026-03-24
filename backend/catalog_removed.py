"""
Catalog all removed questions: category, text, options, traits.
This helps us understand what needs replacing.
"""
import sys, os, re, json
sys.path.insert(0, os.path.dirname(__file__))

# We need to get the FULL pool BEFORE manual removals
# Re-import the raw pool before the filter
from data.questions_enhanced import QUESTIONS_POOL_ENHANCED, _MANUAL_REMOVE_IDS

# The pool is already filtered. We need to reconstruct removed questions.
# Let's import the raw data differently - read the expansion builders

# Actually, let's just reload and capture before/after
# The simplest approach: the pool is already filtered. 
# Let's find the removed questions by loading the module internals.

# Import the raw pieces
from data.questions_enhanced import (
    _dedup_expansion_questions,
    _semantic_dedup,
)

# The pool was built in module-level code. The QUESTIONS_POOL_ENHANCED 
# already has the manual removals applied. We need to see what was removed.
# Let's just build a fresh copy without the manual filter.

# Re-read the source to find all question definitions
print(f"Manual remove IDs ({len(_MANUAL_REMOVE_IDS)}): {sorted(_MANUAL_REMOVE_IDS)}")
print(f"Current pool size: {len(QUESTIONS_POOL_ENHANCED)}")

# Since we can't easily reconstruct removed questions from the filtered pool,
# let's take a different approach: temporarily bypass the filter
# by reading the module source and finding questions with those IDs

# Actually, the expansion questions are generated dynamically.
# The simplest approach: modify the import to get pre-filter data.
# But we can't do that without changing the source.

# Alternative: parse the _build_*_expansion() output to find the removed questions
# Or: just check which categories lost questions and how many

# Let's count questions per category in current pool
from collections import Counter
cat_counts = Counter(q["category"] for q in QUESTIONS_POOL_ENHANCED)

print(f"\n=== Current questions per category (top 30 by count) ===")
for cat, count in cat_counts.most_common(30):
    print(f"  {count:3d}  {cat}")

print(f"\n=== Categories with fewest questions ===")
for cat, count in cat_counts.most_common()[-30:]:
    print(f"  {count:3d}  {cat}")

print(f"\nTotal categories: {len(cat_counts)}")
print(f"Total questions: {sum(cat_counts.values())}")

# Show distribution
from collections import defaultdict
count_dist = defaultdict(list)
for cat, count in cat_counts.items():
    count_dist[count].append(cat)

print(f"\n=== Distribution of questions per category ===")
for n in sorted(count_dist.keys()):
    cats = count_dist[n]
    print(f"  {n} questions: {len(cats)} categories")
    if len(cats) <= 5:
        for c in cats:
            print(f"    - {c}")
