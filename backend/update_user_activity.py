"""
Quick script to update a specific user's last_active timestamp to current time.
Useful for testing the login tracking feature.
"""

import datetime
from database import SessionLocal
import models

def update_user_last_active(email_or_username):
    db = SessionLocal()
    try:
        # Find user by email or username
        user = db.query(models.User).filter(
            (models.User.email == email_or_username) | 
            (models.User.username == email_or_username)
        ).first()
        
        if not user:
            print(f"✗ User not found: {email_or_username}")
            return False
        
        old_time = user.last_active
        user.last_active = datetime.datetime.now()
        user.is_online = 1
        db.commit()
        
        print(f"✓ Updated {user.fullname} ({user.email})")
        print(f"  Old last_active: {old_time}")
        print(f"  New last_active: {user.last_active}")
        return True
        
    except Exception as e:
        db.rollback()
        print(f"✗ Error: {e}")
        raise
    finally:
        db.close()

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python update_user_activity.py <email_or_username>")
        print("Example: python update_user_activity.py namiaenerson939@gmail.com")
        sys.exit(1)
    
    email_or_username = sys.argv[1]
    update_user_last_active(email_or_username)
