import database
from sqlalchemy import text, desc
import models

db = database.SessionLocal()

print("=" * 60)
print("VERIFICATION: test_attempts vs user_test_attempts")
print("=" * 60)

# Get latest attempts from both tables
test_attempts = db.query(models.TestAttempt).order_by(desc(models.TestAttempt.attempt_id)).limit(5).all()
user_test_attempts = db.execute(text('''
    SELECT attempt_id, user_id, test_id, attempt_date 
    FROM user_test_attempts 
    ORDER BY attempt_id DESC 
    LIMIT 5
''')).fetchall()

print("\ntest_attempts (SQLAlchemy model):")
for ta in test_attempts:
    print(f"  ID {ta.attempt_id}: user_id={ta.user_id}, test_id={ta.test_id}, taken_at={ta.taken_at}")

print("\nuser_test_attempts (legacy table):")
for uta in user_test_attempts:
    print(f"  ID {uta[0]}: user_id={uta[1]}, test_id={uta[2]}, attempt_date={uta[3]}")

# Check if IDs match
test_ids = {ta.attempt_id for ta in test_attempts}
user_ids = {uta[0] for uta in user_test_attempts}

print(f"\ntest_attempts IDs: {sorted(test_ids, reverse=True)}")
print(f"user_test_attempts IDs: {sorted(user_ids, reverse=True)}")

if test_ids == user_ids:
    print("\n✅ SYNC SUCCESS: Both tables have identical attempt IDs!")
else:
    missing_in_user = test_ids - user_ids
    missing_in_test = user_ids - test_ids
    if missing_in_user:
        print(f"\n❌ Missing in user_test_attempts: {missing_in_user}")
    if missing_in_test:
        print(f"\n❌ Missing in test_attempts: {missing_in_test}")

# Total count comparison
test_count = db.query(models.TestAttempt).count()
user_count = db.execute(text('SELECT COUNT(*) FROM user_test_attempts')).scalar()

print(f"\nTotal records:")
print(f"  test_attempts: {test_count}")
print(f"  user_test_attempts: {user_count}")

if test_count == user_count:
    print("✅ RECORD COUNT MATCHES")
else:
    print(f"❌ COUNT MISMATCH: difference of {abs(test_count - user_count)}")

db.close()
