"""
Migration Script: Add quiz tracking columns to user_test_attempts table

This adds:
- max_questions: Quiz length selected by student (30, 50, 60)
- confidence_score: Final confidence percentage
- traits_found: Number of unique traits discovered

Run this script once to update your database schema.
"""

from database import engine
from sqlalchemy import text

def migrate():
    """Add new columns to user_test_attempts table"""
    
    # Columns to add with their SQL definitions
    columns_to_add = [
        ("max_questions", "INTEGER"),
        ("confidence_score", "FLOAT"),
        ("traits_found", "INTEGER")
    ]
    
    with engine.connect() as conn:
        print(f"[DB] Adding columns to user_test_attempts table...")
        
        for col_name, col_type in columns_to_add:
            try:
                # PostgreSQL syntax with IF NOT EXISTS
                conn.execute(text(f"""
                    ALTER TABLE user_test_attempts 
                    ADD COLUMN IF NOT EXISTS {col_name} {col_type}
                """))
                conn.commit()
                print(f"[OK] Added column: {col_name}")
                        
            except Exception as e:
                if "duplicate column" in str(e).lower() or "already exists" in str(e).lower():
                    print(f"[SKIP] Column already exists: {col_name}")
                else:
                    print(f"[ERROR] Failed to add {col_name}: {e}")
        
        print("\n[DONE] Migration complete!")
        
        # Verify the columns
        print("\n[VERIFY] Current user_test_attempts columns:")
        result = conn.execute(text("""
            SELECT column_name, data_type 
            FROM information_schema.columns 
            WHERE table_name = 'user_test_attempts'
            ORDER BY ordinal_position
        """))
            
        for row in result.fetchall():
            print(f"  - {row[0]}: {row[1]}")


if __name__ == "__main__":
    print("=" * 60)
    print("MIGRATION: Add quiz tracking to user_test_attempts")
    print("=" * 60)
    migrate()
