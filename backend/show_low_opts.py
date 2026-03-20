"""Show all DB-only questions with < 6 options."""
from database import SessionLocal
from models import Question, Option

db = SessionLocal()
low = []
for q in db.query(Question).all():
    n = db.query(Option).filter(Option.question_id == q.question_id).count()
    if n < 6 and q.question_id > 1000:
        opts = db.query(Option).filter(Option.question_id == q.question_id).all()
        low.append({
            'qid': q.question_id,
            'text': q.question_text,
            'cat': q.category,
            'opt_count': n,
            'options': [(o.option_id, o.option_text, o.trait_tag) for o in opts]
        })

print(f"DB-only questions needing options: {len(low)}")
for q in low:
    print(f"\nQ{q['qid']} ({q['cat']}): {q['text']}")
    print(f"  Has {q['opt_count']} options:")
    for oid, txt, tag in q['options']:
        print(f"    [{tag}] {txt}")
db.close()
