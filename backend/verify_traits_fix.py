"""Verify the traits_found fix"""
from database import SessionLocal
from main import get_assessment_history

db = SessionLocal()
try:
    result = get_assessment_history(user_id=47, db=db)
    # Show the latest 3 attempts
    print("Latest assessment attempts:")
    for h in result['history'][:3]:
        print(f"\nAttempt {h['attempt_id']}:")
        print(f"  max_questions: {h['max_questions']}")
        print(f"  questions_answered: {h['questions_answered']}")
        print(f"  traits_found (from DB): {h['traits_found']}")
        print(f"  confidence_score: {h['confidence_score']}")
finally:
    db.close()
