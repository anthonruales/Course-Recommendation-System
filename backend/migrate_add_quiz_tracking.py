"""
Migration Script: Add quiz tracking columns to test_attempts table

This adds:
- max_questions: Quiz length selected by student (30, 50, 60)
- questions_presented: How many questions were actually shown
- questions_answered: How many questions were actually answered  
- confidence_score: Final confidence percentage

Run this script once to update your database schema.
"""

from database import engine
from sqlalchemy import text

def migrate():
    """Add new columns to test_attempts table"""
    
    # Columns to add with their SQL definitions
    columns_to_add = [
        ("max_questions", "INTEGER"),
        ("questions_presented", "INTEGER"),
        ("questions_answered", "INTEGER"),
        ("confidence_score", "FLOAT")
    ]
    
    with engine.connect() as conn:
        # Check if we're using PostgreSQL or SQLite
        dialect = engine.dialect.name
        print(f"[DB] Database dialect: {dialect}")
        
        for col_name, col_type in columns_to_add:
            try:
                if dialect == "postgresql":
                    # PostgreSQL syntax
                    conn.execute(text(f"""
                        ALTER TABLE test_attempts 
                        ADD COLUMN IF NOT EXISTS {col_name} {col_type}
                    """))
                else:
                    # SQLite syntax (doesn't support IF NOT EXISTS for columns)
                    # First check if column exists
                    result = conn.execute(text(f"PRAGMA table_info(test_attempts)"))
                    existing_cols = [row[1] for row in result.fetchall()]
                    
                    if col_name not in existing_cols:
                        conn.execute(text(f"""
                            ALTER TABLE test_attempts 
                            ADD COLUMN {col_name} {col_type}
                        """))
                        print(f"[OK] Added column: {col_name}")
                    else:
                        print(f"[SKIP] Column already exists: {col_name}")
                        
                conn.commit()
                
            except Exception as e:
                if "duplicate column" in str(e).lower() or "already exists" in str(e).lower():
                    print(f"[SKIP] Column already exists: {col_name}")
                else:
                    print(f"[ERROR] Failed to add {col_name}: {e}")
        
        print("\n[DONE] Migration complete!")
        
        # Verify the columns
        print("\n[VERIFY] Current test_attempts columns:")
        if dialect == "postgresql":
            result = conn.execute(text("""
                SELECT column_name, data_type 
                FROM information_schema.columns 
                WHERE table_name = 'test_attempts'
                ORDER BY ordinal_position
            """))
        else:
            result = conn.execute(text("PRAGMA table_info(test_attempts)"))
            
        for row in result.fetchall():
            print(f"  - {row}")


if __name__ == "__main__":
    print("=" * 60)
    print("MIGRATION: Add quiz tracking columns to test_attempts")
    print("=" * 60)
    migrate()
