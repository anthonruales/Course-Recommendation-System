"""Audit trait assignments in QUESTIONS_POOL_ENHANCED"""
from questions_enhanced import QUESTIONS_POOL_ENHANCED

# Show options with 10+ traits - check if they have obviously irrelevant ones
print("=== Options with 10+ traits (first 20) ===")
count = 0
for q in QUESTIONS_POOL_ENHANCED:
    for opt in q.get("options", []):
        tags = opt.get("trait_tags", {})
        if isinstance(tags, dict) and len(tags) >= 10:
            count += 1
            if count <= 20:
                trait_list = sorted(tags.items(), key=lambda x: -x[1])
                print(f'Q{q["question_id"]} opt{opt["option_id"]}: "{opt["option_text"][:70]}"')
                print(f"  Traits ({len(tags)}): {trait_list}")
                print()
print(f"Total options with 10+ traits: {count}")

# Show specifically Q1 options
print("\n=== Q1 Options ===")
for q in QUESTIONS_POOL_ENHANCED:
    if q["question_id"] == 1:
        for opt in q.get("options", []):
            tags = opt.get("trait_tags", {})
            trait_list = sorted(tags.items(), key=lambda x: -x[1])
            print(f'opt{opt["option_id"]}: "{opt["option_text"][:70]}"')
            print(f"  Traits ({len(tags)}): {trait_list}")
            print()
        break

# Find the "Raising animals" option
print("\n=== 'Raising animals' options ===")
for q in QUESTIONS_POOL_ENHANCED:
    for opt in q.get("options", []):
        if "raising animal" in opt.get("option_text", "").lower():
            tags = opt.get("trait_tags", {})
            trait_list = sorted(tags.items(), key=lambda x: -x[1])
            print(f'Q{q["question_id"]} opt{opt["option_id"]}: "{opt["option_text"]}"')
            print(f"  Traits ({len(tags)}): {trait_list}")
            print()
