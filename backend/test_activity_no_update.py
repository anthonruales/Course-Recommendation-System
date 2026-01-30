"""
Test script to verify last_active ONLY updates on login, not during activity
"""

import requests
import time
from database import SessionLocal
import models

def test_activity_does_not_update_timestamp():
    """Verify that update-activity does NOT update last_active"""
    
    db = SessionLocal()
    
    try:
        print("=" * 70)
        print("TEST: Verify last_active does NOT update on activity")
        print("=" * 70)
        
        # Get a test user
        test_user = db.query(models.User).filter(
            models.User.email == "namiaenerson939@gmail.com"
        ).first()
        
        if not test_user:
            print("✗ Test user not found!")
            return False
        
        print(f"\n1. Test user: {test_user.fullname} (ID: {test_user.user_id})")
        print(f"   Current last_active: {test_user.last_active}")
        
        # Record current timestamp
        original_timestamp = test_user.last_active
        
        # Wait 2 seconds
        print("\n2. Waiting 2 seconds...")
        time.sleep(2)
        
        # Call update-activity endpoint (simulating periodic dashboard calls)
        print("\n3. Calling /update-activity endpoint...")
        response = requests.post(
            f"http://localhost:8000/user/{test_user.user_id}/update-activity"
        )
        
        if response.status_code != 200:
            print(f"✗ Endpoint returned status {response.status_code}")
            return False
        
        print(f"   Response: {response.json()}")
        
        # Check the database
        print("\n4. Checking database...")
        db.expire(test_user)
        test_user = db.query(models.User).filter(
            models.User.user_id == test_user.user_id
        ).first()
        
        current_timestamp = test_user.last_active
        
        print(f"   Original last_active: {original_timestamp}")
        print(f"   Current last_active:  {current_timestamp}")
        
        # Verify timestamp was NOT changed
        if original_timestamp == current_timestamp:
            print(f"\n✓ SUCCESS! last_active was NOT updated by update-activity")
            print(f"  (timestamp remained the same)")
            return True
        else:
            print(f"\n✗ FAILED! last_active was updated during activity")
            time_diff = (current_timestamp - original_timestamp).total_seconds()
            print(f"  (difference: {time_diff:.1f} seconds)")
            return False
            
    except Exception as e:
        print(f"\n✗ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return False
    finally:
        db.close()

if __name__ == "__main__":
    test_activity_does_not_update_timestamp()
