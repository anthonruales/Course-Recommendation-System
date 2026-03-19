"""Find all options with 0 or 1 trait"""
from questions_enhanced import QUESTIONS_POOL_ENHANCED

single = []
for q in QUESTIONS_POOL_ENHANCED:
    for opt in q.get("options", []):
        tags = opt.get("trait_tags", {})
        if isinstance(tags, dict) and len(tags) <= 1:
            single.append((q["question_id"], q["question_text"][:70], opt["option_id"], opt["option_text"][:80], dict(tags)))

print(f"Options with 0 or 1 trait: {len(single)}")
for qid, qtext, oid, otext, tags in single:
    print(f"  Q{qid} ({qtext})")
    print(f"    opt{oid}: \"{otext}\"")
    print(f"    traits: {tags}")
    print()

# Also show question 5 fully (the one in the screenshot - sick pet)
print("=== Searching for sick pet question ===")
for q in QUESTIONS_POOL_ENHANCED:
    qtext = q["question_text"].lower()
    if "sick" in qtext or "pet" in qtext:
        print(f"Q{q['question_id']}: {q['question_text']}")
        for opt in q.get("options", []):
            tags = sorted(opt["trait_tags"].items(), key=lambda x: -x[1]) if opt.get("trait_tags") else []
            print(f"  opt{opt['option_id']}: \"{opt['option_text'][:70]}\" -> {tags}")
        print()
