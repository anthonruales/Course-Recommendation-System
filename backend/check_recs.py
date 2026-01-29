#!/usr/bin/env python
from database import SessionLocal
from models import TestAttempt, Recommendation, Test

db = SessionLocal()

# Get user 42's latest adaptive test attempt
user_id = 42
attempt = db.query(TestAttempt).filter(TestAttempt.user_id == user_id).order_by(TestAttempt.attempt_id.desc()).first()

if attempt:
    test = db.query(Test).filter(Test.test_id == attempt.test_id).first()
    recs = db.query(Recommendation).filter(Recommendation.attempt_id == attempt.attempt_id).all()
    
    print(f'Latest attempt for user {user_id}:')
    print(f'  Attempt ID: {attempt.attempt_id}')
    test_type = test.test_type if test else "N/A"
    print(f'  Test Type: {test_type}')
    print(f'  Recommendations: {len(recs)}')
    if recs:
        for rec in recs:
            print(f'    - {rec.reasoning[:80]}')
else:
    print('No attempts found')

db.close()
