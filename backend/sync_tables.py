"""
Fix table structure:
- user_test_attempts = tests taken by each specific user (PRIMARY)
- test_attempts = total tests of all users (SECONDARY/SYNC)

This script ensures proper dual-table synchronization
"""
import psycopg2
from datetime import datetime

conn = psycopg2.connect(
    host="localhost",
    database="coursepro_db",
    user="postgres",
    password="admin123"
)

cursor = conn.cursor()

print("=" * 80)
print("FIX TABLE STRUCTURE & SYNC")
print("=" * 80)

# Step 1: Verify both tables exist with correct schemas
print("\n[1] Checking table schemas...")

cursor.execute("""
    SELECT column_name, data_type
    FROM information_schema.columns
    WHERE table_name = 'user_test_attempts'
    ORDER BY ordinal_position
""")
print("  user_test_attempts columns:")
for col, dtype in cursor.fetchall():
    print(f"    {col}: {dtype}")

cursor.execute("""
    SELECT column_name, data_type
    FROM information_schema.columns
    WHERE table_name = 'test_attempts'
    ORDER BY ordinal_position
""")
print("\n  test_attempts columns:")
for col, dtype in cursor.fetchall():
    print(f"    {col}: {dtype}")

# Step 2: Sync data from test_attempts to user_test_attempts
print("\n[2] Syncing test_attempts to user_test_attempts...")

cursor.execute("""
    SELECT ta.attempt_id, ta.user_id, ta.test_id, ta.taken_at
    FROM test_attempts ta
    LEFT JOIN user_test_attempts uta ON ta.attempt_id = uta.attempt_id
    WHERE uta.attempt_id IS NULL
""")
missing = cursor.fetchall()
print(f"  Found {len(missing)} attempts not in user_test_attempts")

for attempt_id, user_id, test_id, taken_at in missing:
    try:
        cursor.execute("""
            INSERT INTO user_test_attempts 
            (attempt_id, user_id, test_id, score, total_questions, attempt_date, time_taken, created_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s, NOW())
        """, (attempt_id, user_id, test_id, 0, 0, taken_at, 0))
        print(f"    + Synced attempt {attempt_id} for user {user_id}")
    except Exception as e:
        print(f"    ! Failed to sync attempt {attempt_id}: {e}")

conn.commit()

# Step 3: Verify sync
print("\n[3] Verification...")
cursor.execute("SELECT COUNT(*) FROM user_test_attempts")
user_count = cursor.fetchone()[0]
cursor.execute("SELECT COUNT(*) FROM test_attempts")
test_count = cursor.fetchone()[0]

print(f"  user_test_attempts: {user_count} records")
print(f"  test_attempts: {test_count} records")

if user_count == test_count:
    print(f"  ✅ Tables synchronized: Both have {user_count} records")
else:
    print(f"  ⚠️  Mismatch: user_test_attempts has {user_count}, test_attempts has {test_count}")

# Step 4: Show per-user breakdown
print("\n[4] Per-user test counts:")
cursor.execute("""
    SELECT user_id, COUNT(*) as tests_taken
    FROM user_test_attempts
    GROUP BY user_id
    ORDER BY tests_taken DESC
""")
for user_id, count in cursor.fetchall():
    print(f"  User {user_id}: {count} tests")

cursor.close()
conn.close()

print("\n" + "=" * 80)
print("STRUCTURE FIXED")
print("=" * 80)
