"""
Clear all user data from the database while preserving courses, questions, and options
"""
import models, database
from sqlalchemy import text

db = database.SessionLocal()

try:
    print("🧹 Clearing database (keeping courses, questions, options)...\n")
    
    # Delete in order of dependencies (foreign keys)
    tables_to_clear = [
        ('recommendation_feedback', 'feedback'),
        ('recommendations', 'recommendations'),
        ('student_answers', 'student answers'),
        ('test_attempts', 'test attempts'),
        ('users', 'users'),
        ('user_test_attempts', 'user test attempts (legacy)'),
    ]
    
    for table_name, display_name in tables_to_clear:
        try:
            result = db.execute(text(f"DELETE FROM {table_name}"))
            db.commit()
            print(f"✅ Cleared {display_name}: {result.rowcount} rows deleted")
        except Exception as e:
            print(f"⚠️  Could not clear {display_name}: {e}")
            db.rollback()
    
    # Verify that courses, questions, options still exist
    print("\n📊 Verification:")
    courses = db.query(models.Course).count()
    questions = db.query(models.Question).count()
    
    print(f"✅ Courses: {courses} records")
    print(f"✅ Questions: {questions} records")
    
    # Get option count
    options = db.execute(text("SELECT COUNT(*) FROM options")).scalar()
    print(f"✅ Options: {options} records")
    
    print("\n✨ Database cleared successfully!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
finally:
    db.close()
