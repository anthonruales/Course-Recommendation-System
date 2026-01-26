"""
Sync test_attempts data to user_test_attempts for backward compatibility
"""
import database
from sqlalchemy import text

db = database.SessionLocal()

try:
    print("Syncing data from test_attempts to user_test_attempts...")
    
    # First, clear the old table (CASCADE to remove dependent records)
    db.execute(text('TRUNCATE TABLE user_test_attempts CASCADE'))
    print("✓ Cleared user_test_attempts")
    
    # Copy data from test_attempts to user_test_attempts
    # Assuming default values for score, total_questions, time_taken
    query = text('''
        INSERT INTO user_test_attempts (attempt_id, user_id, test_id, score, total_questions, attempt_date, time_taken, created_at)
        SELECT 
            attempt_id,
            user_id,
            test_id,
            0 as score,
            0 as total_questions,
            taken_at as attempt_date,
            0 as time_taken,
            NOW() as created_at
        FROM test_attempts
    ''')
    
    result = db.execute(query)
    db.commit()
    
    # Verify
    count = db.execute(text('SELECT COUNT(*) FROM user_test_attempts')).scalar()
    print(f"✓ Synced {count} records to user_test_attempts")
    
except Exception as e:
    print(f"Error: {e}")
    db.rollback()
finally:
    db.close()
