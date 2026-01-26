import models, database
from sqlalchemy import desc

db = database.SessionLocal()

print('📊 ADAPTIVE ASSESSMENT DATA VERIFICATION')
print('=' * 50)

# Check recent test attempts 
attempts = db.query(models.TestAttempt).filter(
    models.TestAttempt.user_id == 30
).order_by(desc(models.TestAttempt.taken_at)).limit(5).all()

print(f'Recent test attempts for user 30: {len(attempts)}')
print()

for i, attempt in enumerate(attempts, 1):
    test = db.query(models.Test).filter(models.Test.test_id == attempt.test_id).first()
    answers = db.query(models.StudentAnswer).filter(
        models.StudentAnswer.attempt_id == attempt.attempt_id
    ).all()
    recs = db.query(models.Recommendation).filter(
        models.Recommendation.attempt_id == attempt.attempt_id
    ).all()
    
    print(f'{i}. Attempt ID: {attempt.attempt_id}')
    print(f'   Test Type: {test.test_type if test else "Unknown"}')
    print(f'   Date: {attempt.taken_at}')
    print(f'   Answers: {len(answers)} questions answered')
    print(f'   Recommendations: {len(recs)} courses recommended')
    
    if recs:
        print(f'   Top recommendation: {recs[0].course_id}')
    print()

# Check total test attempts in database
total_attempts = db.query(models.TestAttempt).count()
adaptive_attempts = db.query(models.TestAttempt).join(models.Test).filter(
    models.Test.test_type == 'adaptive'
).count()
old_attempts = db.query(models.TestAttempt).join(models.Test).filter(
    models.Test.test_type == 'assessment'
).count()

print(f'SUMMARY:')
print(f'Total test attempts in database: {total_attempts}')
print(f'Adaptive assessment attempts: {adaptive_attempts}')
print(f'Old assessment attempts: {old_attempts}')

db.close()