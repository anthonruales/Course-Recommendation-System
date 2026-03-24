"""
Generate replacement questions for the 88 removed rephrase/duplicate questions.
Each replacement must:
  - Be in the same category as the removed question
  - Have 6 options with appropriate trait_tags
  - NOT be a rephrase/duplicate of any existing question
  - Cover a DIFFERENT angle/aspect of the field

This script:
  1. Loads the current pool
  2. For each removed ID, finds category, existing questions, and available traits
  3. Prints context needed to craft replacements
"""
import sys, os, re, json
from collections import defaultdict
sys.path.insert(0, os.path.dirname(__file__))

# We need the FULL pool (before filtering) to find the removed questions' details
# Read the raw file to extract removed question data
from data.questions_enhanced import QUESTIONS_POOL_ENHANCED, _MANUAL_REMOVE_IDS

# Current pool (already filtered)
current_by_id = {q["question_id"]: q for q in QUESTIONS_POOL_ENHANCED}
current_ids = set(current_by_id.keys())

# Group current questions by category
by_category = defaultdict(list)
for q in QUESTIONS_POOL_ENHANCED:
    by_category[q["category"]].append(q)

# Collect all traits used across the pool per category
traits_by_category = defaultdict(lambda: defaultdict(float))
for q in QUESTIONS_POOL_ENHANCED:
    cat = q["category"]
    for opt in q["options"]:
        for trait, weight in opt["trait_tags"].items():
            if weight > traits_by_category[cat][trait]:
                traits_by_category[cat][trait] = weight

# All removed IDs
removed_ids = sorted(_MANUAL_REMOVE_IDS)

print(f"Current pool: {len(QUESTIONS_POOL_ENHANCED)} questions")
print(f"Removed IDs: {len(removed_ids)}")
print(f"Categories in pool: {len(by_category)}")

# For each category that had removals, show existing questions and traits
affected_cats = set()
for q_id in removed_ids:
    # We need to find what category this ID belonged to
    # Since it's removed, we can't look it up in current pool
    # We'll need to check the comments in the source or use another approach
    pass

# Instead, let's reload the unfiltered pool by temporarily reading the data
# Actually, the simplest approach: look at what question the removed one was
# a rephrase of, and use THAT question's category
print("\n=== CONTEXT FOR REPLACEMENT GENERATION ===\n")

# Let me map removed IDs to their "rephrase of" targets from our knowledge
rephrase_map = {
    2031: 857, 2781: 940, 104: 87, 465: 458, 489: 483,
    599: 250, 618: 236, 701: 697, 749: 746, 759: 756,
    774: 476, 899: 851, 901: 844, 909: 851, 917: 859,
    1116: 1096, 1401: 794, 1431: 809, 1461: 811, 1551: 817,
    1731: 848, 1821: 834, 1851: 848, 1881: 854, 2001: 901,
    2061: 853, 2066: 853, 2091: 857, 2151: 859, 2211: 871,
    2271: 878, 2301: 875, 2331: 876, 2541: 880, 2576: 933,
    2651: 2636, 2661: 2636, 2666: 2636, 2696: 2691, 2721: 943,
    2751: 943, 2756: 943, 2771: 936, 2811: 936, 2841: 934,
    2871: 940, 2901: 947, 2936: 959, 2961: 961, 2966: 961,
    2996: 962, 3026: 975, 3031: 975, 3056: 964, 3086: 965,
    3116: 967, 3146: 966, 3176: 969, 3181: 969, 3206: 971,
    3236: 970, 3241: 970, 3266: 968, 3296: 972, 3326: 973,
    3356: 973, 3416: 989, 3421: 989, 3431: 988, 3481: 996,
    3511: 991, 3541: 992, 3571: 998, 3601: 1002, 3691: 1005,
    3741: 1003, 3771: 997, 3781: 997, 3801: 1001, 3811: 988,
    3871: 1008, 3891: 999, 3901: 999, 3921: 1079, 3961: 1100,
    3981: 1094, 4041: 1108, 4221: 1094,
}

# For each removed ID, find the category from its "rephrase of" target
cat_for_removed = {}
for rem_id, target_id in rephrase_map.items():
    target_q = current_by_id.get(target_id)
    if target_q:
        cat_for_removed[rem_id] = target_q["category"]
    else:
        # Target might also be removed (e.g. 2001 -> 901 which is also removed)
        # In that case, look up 901's target
        second_target = rephrase_map.get(target_id)
        if second_target:
            target_q2 = current_by_id.get(second_target)
            if target_q2:
                cat_for_removed[rem_id] = target_q2["category"]

# Count replacements needed per category
replacements_per_cat = defaultdict(list)
for rem_id in removed_ids:
    cat = cat_for_removed.get(rem_id, "UNKNOWN")
    replacements_per_cat[cat].append(rem_id)

print(f"\nReplacements needed per category:")
for cat in sorted(replacements_per_cat.keys()):
    ids = replacements_per_cat[cat]
    existing_count = len(by_category.get(cat, []))
    print(f"  {cat}: {len(ids)} replacement(s) needed (currently {existing_count} questions)")
    
print(f"\nTotal categories needing replacements: {len(replacements_per_cat)}")
print(f"Total replacements needed: {sum(len(v) for v in replacements_per_cat.values())}")

# Now dump detailed context per category
print("\n" + "="*80)
print("DETAILED CATEGORY CONTEXT")
print("="*80)

for cat in sorted(replacements_per_cat.keys()):
    if cat == "UNKNOWN":
        print(f"\n--- UNKNOWN CATEGORY ---")
        print(f"  Removed IDs with unknown category: {replacements_per_cat[cat]}")
        continue
    
    ids_needed = replacements_per_cat[cat]
    existing_qs = by_category.get(cat, [])
    
    print(f"\n{'='*60}")
    print(f"CATEGORY: {cat}")
    print(f"Replacements needed: {len(ids_needed)} (IDs: {ids_needed})")
    print(f"Existing questions: {len(existing_qs)}")
    print(f"{'='*60}")
    
    # Show existing question texts
    print(f"\n  Existing questions:")
    for q in existing_qs:
        print(f"    Q{q['question_id']}: {q['question_text']}")
        for opt in q["options"][:3]:
            top_traits = sorted(opt["trait_tags"].items(), key=lambda x: -x[1])[:3]
            trait_str = ", ".join(f"{k}:{v}" for k, v in top_traits)
            print(f"      - {opt['option_text']} [{trait_str}]")
        if len(q["options"]) > 3:
            print(f"      ... and {len(q['options'])-3} more options")
    
    # Show all traits used in this category
    cat_traits = traits_by_category.get(cat, {})
    top_traits = sorted(cat_traits.items(), key=lambda x: -x[1])[:15]
    print(f"\n  Top traits in category: {', '.join(f'{t}({w:.1f})' for t, w in top_traits)}")
