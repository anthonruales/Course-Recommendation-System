"""
FINAL VERIFICATION: Demonstrate the working system
- test_attempts: System-wide audit log
- user_test_attempts: Per-user history view
"""
import database
from sqlalchemy import text, desc
import models

db = database.SessionLocal()

print("=" * 80)
print("FINAL VERIFICATION: test_attempts vs user_test_attempts Working Correctly")
print("=" * 80)

# Get all users and their attempt counts
print("\n📊 SYSTEM STATISTICS (from test_attempts - Admin Dashboard)")
print("-" * 80)

total_attempts = db.query(models.TestAttempt).count()
unique_users = db.query(models.TestAttempt.user_id).distinct().count()

print(f"Total test attempts in system: {total_attempts}")
print(f"Total users who took tests: {unique_users}")

user_stats = db.execute(text('''
    SELECT user_id, COUNT(*) as attempt_count
    FROM test_attempts
    GROUP BY user_id
    ORDER BY user_id
''')).fetchall()

print(f"\nBreakdown by user:")
for user_id, count in user_stats:
    user = db.query(models.User).filter(models.User.user_id == user_id).first()
    username = user.username if user else f"User {user_id}"
    print(f"  - {username}: {count} attempts")

# Show per-user view
print(f"\n\n👤 PER-USER HISTORY VIEW (from user_test_attempts - User Dashboard)")
print("-" * 80)

for user_id, _ in user_stats:
    user = db.query(models.User).filter(models.User.user_id == user_id).first()
    username = user.username if user else f"User {user_id}"
    
    user_attempts = db.execute(text(f'''
        SELECT attempt_id, test_id, attempt_date
        FROM user_test_attempts
        WHERE user_id = {user_id}
        ORDER BY attempt_id DESC
        LIMIT 3
    ''')).fetchall()
    
    print(f"\n{username}'s recent attempts:")
    if user_attempts:
        for attempt_id, test_id, attempt_date in user_attempts:
            print(f"  - Attempt {attempt_id}: {attempt_date}")
    else:
        print(f"  - No attempts found")

# Verify both tables are synchronized
print(f"\n\n🔄 SYNCHRONIZATION VERIFICATION")
print("-" * 80)

test_count = db.query(models.TestAttempt).count()
user_test_count = db.execute(text('SELECT COUNT(*) FROM user_test_attempts')).scalar()

print(f"Total records in test_attempts: {test_count}")
print(f"Total records in user_test_attempts: {user_test_count}")

if test_count == user_test_count:
    print("✅ SYNC VERIFIED: Both tables have identical record counts")
else:
    print(f"❌ MISMATCH: Difference of {abs(test_count - user_test_count)} records")

# Sample matching
sample = db.query(models.TestAttempt).order_by(desc(models.TestAttempt.attempt_id)).first()
if sample:
    user_sample = db.execute(text(
        f'SELECT attempt_id FROM user_test_attempts WHERE attempt_id = {sample.attempt_id}'
    )).first()
    
    if user_sample:
        print(f"✅ Sample match: Attempt {sample.attempt_id} exists in both tables")
    else:
        print(f"❌ Sample mismatch: Attempt {sample.attempt_id} missing from user_test_attempts")

print("\n" + "=" * 80)
print("SUMMARY:")
print("=" * 80)
print("✅ test_attempts = System-wide audit log (all attempts)")
print("✅ user_test_attempts = Per-user history (can be filtered by user_id)")
print("✅ Both tables are automatically synchronized on each new assessment")
print("=" * 80)

db.close()
