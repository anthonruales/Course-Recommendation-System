"""Full list of DB-only questions with their options"""
import sys
sys.path.insert(0, ".")
from database import SessionLocal
import models
from sqlalchemy.orm import joinedload
from questions_enhanced import QUESTIONS_POOL_ENHANCED

enhanced_qids = set()
for q in QUESTIONS_POOL_ENHANCED:
    enhanced_qids.add(q["question_id"])

db = SessionLocal()
db_questions = db.query(models.Question).options(joinedload(models.Question.options)).order_by(models.Question.question_id).all()

missing = [q for q in db_questions if q.question_id not in enhanced_qids]

# Write to a text file instead of console
with open("missing_questions.txt", "w", encoding="utf-8") as f:
    f.write(f"Total missing questions: {len(missing)}\n\n")
    for q in missing:
        f.write(f"Q{q.question_id}: {q.question_text} (category: {q.category})\n")
        for opt in sorted(q.options, key=lambda o: o.option_id):
            f.write(f"  opt{opt.option_id}: \"{opt.option_text}\" -> trait_tag={opt.trait_tag}\n")
        f.write("\n")

# Also check option_id conflicts between DB and enhanced
enhanced_opts = {}
for q in QUESTIONS_POOL_ENHANCED:
    for opt in q.get("options", []):
        enhanced_opts[opt["option_id"]] = (q["question_id"], opt["option_text"][:40])

conflicts = 0
for q in missing:
    for opt in q.options:
        if opt.option_id in enhanced_opts:
            eq_id, eq_text = enhanced_opts[opt.option_id]
            conflicts += 1

print(f"Missing questions: {len(missing)}")
print(f"Option ID conflicts: {conflicts}")
print("Wrote missing_questions.txt")
db.close()
