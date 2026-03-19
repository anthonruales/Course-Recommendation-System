"""Test that ALL DB options now get multi-trait enrichment"""
import sys
sys.path.insert(0, ".")
from database import SessionLocal
import models
from sqlalchemy.orm import joinedload
from questions_enhanced import QUESTIONS_POOL_ENHANCED
from curated_trait_map import build_multi_trait

# Build enhanced lookup (same as main.py)
enhanced_trait_lookup = {}
for eq in QUESTIONS_POOL_ENHANCED:
    for eopt in eq.get("options", []):
        key = (eq["question_id"], eopt["option_id"])
        enhanced_trait_lookup[key] = eopt.get("trait_tags", {})

db = SessionLocal()
questions = db.query(models.Question).options(joinedload(models.Question.options)).all()

single_trait = 0
multi_trait = 0
no_trait = 0
total = 0

single_examples = []

for q in questions:
    for opt in q.options:
        total += 1
        trait_tags = enhanced_trait_lookup.get((q.question_id, opt.option_id), {})
        if not trait_tags and opt.trait_tag:
            trait_tags = build_multi_trait(opt.trait_tag)
        
        count = len(trait_tags) if isinstance(trait_tags, dict) else 0
        if count == 0:
            no_trait += 1
        elif count == 1:
            single_trait += 1
            if len(single_examples) < 5:
                single_examples.append((q.question_id, opt.option_id, opt.option_text[:50], opt.trait_tag, trait_tags))
        else:
            multi_trait += 1

print(f"=== DB Option Trait Coverage ===")
print(f"Total options: {total}")
print(f"Multi-trait (2+): {multi_trait} ({multi_trait/total*100:.1f}%)")
print(f"Single trait: {single_trait} ({single_trait/total*100:.1f}%)")
print(f"No trait: {no_trait} ({no_trait/total*100:.1f}%)")

if single_examples:
    print(f"\nSingle-trait examples:")
    for qid, oid, text, tag, tags in single_examples:
        print(f"  Q{qid} opt{oid}: \"{text}\" tag={tag} -> {tags}")

# Show a few DB-only questions with their enriched traits
print(f"\n=== Sample DB-only question enrichments ===")
enhanced_qids = set(q["question_id"] for q in QUESTIONS_POOL_ENHANCED)
shown = 0
for q in questions:
    if q.question_id not in enhanced_qids and shown < 3:
        print(f"Q{q.question_id}: {q.question_text[:60]}")
        for opt in sorted(q.options, key=lambda o: o.option_id)[:3]:
            trait_tags = enhanced_trait_lookup.get((q.question_id, opt.option_id), {})
            if not trait_tags and opt.trait_tag:
                trait_tags = build_multi_trait(opt.trait_tag)
            sorted_tags = sorted(trait_tags.items(), key=lambda x: -x[1])
            print(f"  opt{opt.option_id}: \"{opt.option_text[:50]}\"")
            print(f"    {sorted_tags}")
        print()
        shown += 1

db.close()
