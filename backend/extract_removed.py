"""
Step 1: Temporarily bypass manual filter to extract removed questions.
Step 2: For each removed question, create a unique replacement with:
  - Same category and similar trait coverage
  - Completely different question text angle
  - Completely different option texts
  - No overlap with existing pool questions
Step 3: Validate all replacements against pool
"""
import sys, os, re, json, copy
sys.path.insert(0, os.path.dirname(__file__))

# ── Step 1: Get the removed questions ──────────────────────────────
# We need to temporarily get the pre-filter pool.
# The filter is applied at module level in questions_enhanced.py.
# We'll re-read the module and reconstruct.

from data.questions_enhanced import _MANUAL_REMOVE_IDS

# Monkey-patch: save the original pool before filter
# Actually, let's just re-import and reconstruct by reading the source
# The cleanest way: temporarily modify the set, reimport

# Better approach: use importlib to get a fresh copy
import importlib
import data.questions_enhanced as qe_mod

# The pool was already filtered on import. We can't undo that easily.
# Instead, let's find the removed questions by looking at the expansion builders.
# Each _build_*_expansion() returns a list of questions.

# Get all expansion builder functions
expansion_fns = []
for name in dir(qe_mod):
    if name.startswith('_build_') and name.endswith('_expansion'):
        fn = getattr(qe_mod, name)
        if callable(fn):
            expansion_fns.append((name, fn))

print(f"Found {len(expansion_fns)} expansion builders")

# Call each one and collect ALL expansion questions (pre-dedup)
all_expansion = []
for name, fn in expansion_fns:
    try:
        qs = fn()
        all_expansion.extend(qs)
    except Exception as e:
        print(f"  Error calling {name}: {e}")

print(f"Total raw expansion questions: {len(all_expansion)}")

# Also get the static questions (IDs < 2000)
# These are in QUESTIONS_POOL_ENHANCED but some were removed
# For static questions, we need to check if any removed IDs are < 2000
static_removed = [qid for qid in _MANUAL_REMOVE_IDS if qid < 2000]
expansion_removed = [qid for qid in _MANUAL_REMOVE_IDS if qid >= 2000]
print(f"\nStatic IDs removed: {len(static_removed)} -> {sorted(static_removed)}")
print(f"Expansion IDs removed: {len(expansion_removed)} -> {sorted(expansion_removed)}")

# Find the removed expansion questions
removed_expansion = [q for q in all_expansion if q["question_id"] in _MANUAL_REMOVE_IDS]
print(f"\nFound {len(removed_expansion)} removed expansion questions in builders")

# For static removed questions, we need to find them from the original static list
# The static questions were defined before expansion. Let's check if the pool
# has them at all (they were removed).
# We need to search the source file for these IDs.

# Let's just work with what we have - enumerate ALL removed questions
removed_by_id = {q["question_id"]: q for q in removed_expansion}

# For static questions, we'll need to read the source file
print(f"\n=== Removed questions we can reconstruct ===")
for qid in sorted(_MANUAL_REMOVE_IDS):
    q = removed_by_id.get(qid)
    if q:
        opts = q.get("options", [])
        all_traits = set()
        for o in opts:
            all_traits.update(o.get("trait_tags", {}).keys())
        print(f"\n  Q{qid} [{q['category']}]")
        print(f"    Text: {q['question_text']}")
        print(f"    Options: {len(opts)}")
        print(f"    Traits: {sorted(all_traits)}")
    else:
        print(f"\n  Q{qid} - NOT FOUND in expansion builders (static question)")

# ── Analyze the current pool for comparison ──────────────────────────
current_pool = qe_mod.QUESTIONS_POOL_ENHANCED
print(f"\n\n=== Current pool stats ===")
print(f"Total: {len(current_pool)} questions")

# Collect all existing question texts and option texts for dedup
existing_q_texts = set()
existing_opt_texts = set()
existing_traits_by_cat = {}

for q in current_pool:
    existing_q_texts.add(q["question_text"].lower().strip())
    cat = q["category"]
    if cat not in existing_traits_by_cat:
        existing_traits_by_cat[cat] = set()
    for o in q.get("options", []):
        existing_opt_texts.add(o["option_text"].lower().strip())
        existing_traits_by_cat[cat].update(o.get("trait_tags", {}).keys())

print(f"Unique question texts: {len(existing_q_texts)}")
print(f"Unique option texts: {len(existing_opt_texts)}")
print(f"Categories with traits: {len(existing_traits_by_cat)}")

# Save removed questions data for the replacement generator
output = {
    "removed_expansion": [],
    "static_removed_ids": static_removed,
    "existing_q_texts_sample": list(existing_q_texts)[:20],
}

for q in removed_expansion:
    output["removed_expansion"].append({
        "question_id": q["question_id"],
        "category": q["category"],
        "question_text": q["question_text"],
        "options": q.get("options", []),
    })

with open("removed_questions_data.json", "w", encoding="utf-8") as f:
    json.dump(output, f, indent=2, ensure_ascii=False)

print(f"\nSaved removed question data to removed_questions_data.json")
