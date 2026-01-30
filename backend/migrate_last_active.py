"""
Migration script to populate last_active timestamp for existing users.
Run this once to update all existing user records.
"""

import datetime
from database import SessionLocal
import models

def migrate_last_active():
    db = SessionLocal()
    try:
        # Get all users with NULL last_active
        users = db.query(models.User).filter(models.User.last_active == None).all()
        
        if not users:
            print("✓ All users already have last_active timestamp set!")
            return
        
        print(f"Found {len(users)} users with NULL last_active. Updating...")
        
        # Set last_active to their created_at time (or current time if no created_at)
        for user in users:
            user.last_active = user.created_at or datetime.datetime.now()
            print(f"  ✓ Updated {user.fullname} ({user.email}) - last_active: {user.last_active}")
        
        # Commit all changes
        db.commit()
        print(f"\n✓ Successfully updated {len(users)} users!")
        
    except Exception as e:
        db.rollback()
        print(f"✗ Error during migration: {e}")
        raise
    finally:
        db.close()

if __name__ == "__main__":
    print("=" * 60)
    print("MIGRATION: Populate last_active for existing users")
    print("=" * 60)
    migrate_last_active()
    print("=" * 60)
    print("Migration complete!")
