import database
from sqlalchemy import text
import models

db = database.SessionLocal()

print("=" * 70)
print("DEMONSTRATING: test_attempts (System-Wide) vs user_test_attempts (Per-User)")
print("=" * 70)

# Example: Joe (user_id=30) views his own history
print("\n📋 SCENARIO 1: Joe (user_id=30) checks his test history")
print("-" * 70)

# Query from test_attempts (system total, but filtered by user)
joe_attempts_system = db.query(models.TestAttempt).filter(
    models.TestAttempt.user_id == 30
).all()

# Query from user_test_attempts (user history table)
joe_attempts_user = db.execute(text('''
    SELECT attempt_id, user_id, test_id, attempt_date
    FROM user_test_attempts
    WHERE user_id = 30
''')).fetchall()

print(f"Joe's attempts in test_attempts: {len(joe_attempts_system)} attempts")
for ta in joe_attempts_system:
    print(f"  - Attempt {ta.attempt_id}: {ta.taken_at}")

print(f"\nJoe's attempts in user_test_attempts: {len(joe_attempts_user)} attempts")
for uta in joe_attempts_user:
    print(f"  - Attempt {uta[0]}: {uta[3]}")

print("\n✅ Admin can see Joe's history from either table (filtered by user_id=30)")

# Example 2: Admin views system-wide statistics
print("\n\n📊 SCENARIO 2: Admin views TOTAL system statistics")
print("-" * 70)

total_attempts = db.query(models.TestAttempt).count()
total_users = db.query(models.TestAttempt.user_id).distinct().count()
total_system_user_table = db.execute(text(
    'SELECT COUNT(*) FROM user_test_attempts'
)).scalar()

print(f"Total test attempts in system (test_attempts): {total_attempts}")
print(f"Total unique users who took tests: {total_users}")
print(f"Total records in user_test_attempts: {total_system_user_table}")

print("\n✅ Admin can see system-wide stats from test_attempts")
print("✅ Individual user histories come from user_test_attempts with user_id filter")

# Show data by user
print("\n\n👥 SCENARIO 3: All users' test history")
print("-" * 70)

from sqlalchemy import desc
distinct_users = db.execute(text('''
    SELECT DISTINCT user_id, COUNT(*) as attempt_count
    FROM test_attempts
    GROUP BY user_id
    ORDER BY user_id
''')).fetchall()

print("User test attempt counts:")
for user_id, count in distinct_users:
    print(f"  - User {user_id}: {count} test attempts")

print("\n✅ test_attempts contains ALL attempts from all users")
print("✅ user_test_attempts contains same data, just organized by user")

db.close()
