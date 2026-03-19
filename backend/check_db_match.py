"""Check if DB questions match QUESTIONS_POOL_ENHANCED"""
from questions_enhanced import QUESTIONS_POOL_ENHANCED

# Build lookup of all question_id -> option_ids in enhanced data
enhanced_questions = {}
enhanced_options = {}
for q in QUESTIONS_POOL_ENHANCED:
    qid = q["question_id"]
    enhanced_questions[qid] = q["question_text"]
    for opt in q.get("options", []):
        enhanced_options[(qid, opt["option_id"])] = opt["option_text"]

print(f"Enhanced questions: {len(enhanced_questions)}")
print(f"Enhanced options: {len(enhanced_options)}")

# Check which question IDs exist
all_qids = sorted(enhanced_questions.keys())
print(f"Question ID range: {min(all_qids)} to {max(all_qids)}")
print(f"Question IDs: {all_qids[:20]}...")

# Now try to connect to DB and check
try:
    import sys
    sys.path.insert(0, ".")
    from database import SessionLocal
    import models
    
    db = SessionLocal()
    db_questions = db.query(models.Question).all()
    print(f"\nDB questions: {len(db_questions)}")
    
    missing_questions = []
    for q in db_questions:
        if q.question_id not in enhanced_questions:
            missing_questions.append((q.question_id, q.question_text[:60]))
    
    print(f"DB questions NOT in enhanced data: {len(missing_questions)}")
    for qid, qtext in missing_questions[:20]:
        print(f"  Q{qid}: {qtext}")
    
    # Check options mismatch
    from sqlalchemy.orm import joinedload
    db_questions_full = db.query(models.Question).options(joinedload(models.Question.options)).all()
    missing_opts = 0
    fallback_opts = 0
    for q in db_questions_full:
        for opt in q.options:
            key = (q.question_id, opt.option_id)
            if key not in enhanced_options:
                missing_opts += 1
                if fallback_opts < 10:
                    print(f"  Missing opt: Q{q.question_id} opt{opt.option_id}: \"{opt.option_text[:50]}\" tag={opt.trait_tag}")
                fallback_opts += 1
    
    print(f"\nDB options NOT in enhanced data: {missing_opts} (would fall back to single trait)")
    db.close()
except Exception as e:
    print(f"Could not connect to DB: {e}")
    print("This is expected if running without DB setup")
