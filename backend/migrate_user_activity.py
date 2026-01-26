"""
Database migration to add last_active and is_online columns to users table
"""
import database
from sqlalchemy import text

db = database.SessionLocal()

try:
    print("🔄 Migrating database schema...")
    
    # Check if columns exist
    inspector_result = db.execute(text("""
        SELECT column_name FROM information_schema.columns 
        WHERE table_name='users' AND column_name IN ('last_active', 'is_online')
    """)).fetchall()
    
    existing_cols = [row[0] for row in inspector_result]
    
    # Add last_active column if it doesn't exist
    if 'last_active' not in existing_cols:
        print("Adding last_active column...")
        db.execute(text("""
            ALTER TABLE users ADD COLUMN last_active TIMESTAMP NULL
        """))
        db.commit()
        print("✓ Added last_active column")
    else:
        print("✓ last_active column already exists")
    
    # Add is_online column if it doesn't exist
    if 'is_online' not in existing_cols:
        print("Adding is_online column...")
        db.execute(text("""
            ALTER TABLE users ADD COLUMN is_online INTEGER DEFAULT 0
        """))
        db.commit()
        print("✓ Added is_online column")
    else:
        print("✓ is_online column already exists")
    
    print("\n✅ Migration completed successfully")
    
except Exception as e:
    print(f"❌ Migration error: {e}")
    import traceback
    traceback.print_exc()
    db.rollback()
finally:
    db.close()
