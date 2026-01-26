"""
Test to see if user_test_attempts is being updated with new attempts
"""
import database
from sqlalchemy import text
import models
from datetime import datetime

db = database.SessionLocal()

print("=" * 70)
print("TESTING: Checking if user_test_attempts sync is working")
print("=" * 70)

# Count before
count_before_test = db.execute(text('SELECT COUNT(*) FROM user_test_attempts')).scalar()
count_before_main = db.query(models.TestAttempt).count()

print(f"\nBefore test:")
print(f"  test_attempts: {count_before_main}")
print(f"  user_test_attempts: {count_before_test}")

# Create a test attempt manually to see if it syncs
print(f"\nCreating a test manual attempt...")

try:
    # Get or create adaptive test
    adaptive_test = db.query(models.Test).filter(models.Test.test_type == "adaptive").first()
    if not adaptive_test:
        adaptive_test = models.Test(
            test_name="Smart Assessment (Adaptive)",
            test_type="adaptive",
            description="Akinator-style adaptive assessment"
        )
        db.add(adaptive_test)
        db.flush()
    
    # Create test attempt
    test_attempt = models.TestAttempt(
        user_id=30,
        test_id=adaptive_test.test_id
    )
    db.add(test_attempt)
    db.flush()
    print(f"✓ Created test attempt ID: {test_attempt.attempt_id}")
    
    # Commit to test_attempts
    db.commit()
    print(f"✓ Committed to test_attempts")
    
    # Now manually test the sync code
    print(f"\nManually testing sync code...")
    
    try:
        db.execute(text('''
            INSERT INTO user_test_attempts 
            (attempt_id, user_id, test_id, score, total_questions, attempt_date, time_taken, created_at)
            VALUES (:attempt_id, :user_id, :test_id, :score, :total_questions, :attempt_date, :time_taken, NOW())
        '''), {
            'attempt_id': test_attempt.attempt_id,
            'user_id': 30,
            'test_id': adaptive_test.test_id,
            'score': 0,
            'total_questions': 0,
            'attempt_date': test_attempt.taken_at,
            'time_taken': 0
        })
        db.commit()
        print(f"✓ Manually synced to user_test_attempts")
    except Exception as e:
        print(f"✗ Error syncing: {e}")
        import traceback
        traceback.print_exc()
        db.rollback()

except Exception as e:
    print(f"✗ Error creating test attempt: {e}")
    import traceback
    traceback.print_exc()
    db.rollback()

# Count after
count_after_test = db.execute(text('SELECT COUNT(*) FROM user_test_attempts')).scalar()
count_after_main = db.query(models.TestAttempt).count()

print(f"\nAfter test:")
print(f"  test_attempts: {count_after_main} (was {count_before_main})")
print(f"  user_test_attempts: {count_after_test} (was {count_before_test})")

if count_after_main > count_before_main and count_after_test > count_before_test:
    print("\n✅ SYNC WORKING: Both tables increased")
elif count_after_main > count_before_main:
    print("\n❌ SYNC NOT WORKING: Only test_attempts increased, user_test_attempts didn't sync")
else:
    print("\n❌ NO DATA WAS SAVED")

# Check latest record in user_test_attempts
latest = db.execute(text(
    'SELECT attempt_id, user_id FROM user_test_attempts ORDER BY attempt_id DESC LIMIT 1'
)).first()
print(f"\nLatest in user_test_attempts: Attempt {latest[0]} by User {latest[1]}")

db.close()
