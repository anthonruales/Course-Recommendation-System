"""Analyze DB questions that are NOT in QUESTIONS_POOL_ENHANCED"""
import sys
sys.path.insert(0, ".")
from database import SessionLocal
import models
from sqlalchemy.orm import joinedload
from questions_enhanced import QUESTIONS_POOL_ENHANCED

# Build enhanced lookup
enhanced_qids = set()
for q in QUESTIONS_POOL_ENHANCED:
    enhanced_qids.add(q["question_id"])

db = SessionLocal()
db_questions = db.query(models.Question).options(joinedload(models.Question.options)).all()

# Show ALL missing questions with their options
missing = [q for q in db_questions if q.question_id not in enhanced_qids]
print(f"Total missing questions: {len(missing)}")
print()

for q in missing:
    print(f"Q{q.question_id}: {q.question_text} (category: {q.category})")
    for opt in q.options:
        print(f"  opt{opt.option_id}: \"{opt.option_text[:70]}\" -> trait_tag={opt.trait_tag}")
    print()

db.close()
