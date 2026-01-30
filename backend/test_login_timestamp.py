"""
Test script to verify last_active is updated on login
"""

import requests
import datetime
import time
from database import SessionLocal
import models

def test_login_timestamp_update():
    """Test that last_active is updated when a user logs in"""
    
    db = SessionLocal()
    
    try:
        print("=" * 70)
        print("TEST: Verify last_active updates on login")
        print("=" * 70)
        
        # Get a test user
        test_user = db.query(models.User).filter(
            models.User.email == "namiaenerson939@gmail.com"
        ).first()
        
        if not test_user:
            print("✗ Test user not found!")
            return False
        
        print(f"\n1. Found test user: {test_user.fullname} (ID: {test_user.user_id})")
        print(f"   Current last_active: {test_user.last_active}")
        
        # Record current timestamp
        old_timestamp = test_user.last_active
        
        # Wait a bit to ensure time difference
        print("\n2. Waiting 2 seconds...")
        time.sleep(2)
        
        # Simulate the login by calling the refresh endpoint
        print("\n3. Calling /refresh-user-activity endpoint...")
        response = requests.post(
            f"http://localhost:8000/refresh-user-activity/{test_user.user_id}"
        )
        
        if response.status_code != 200:
            print(f"✗ Endpoint returned status {response.status_code}")
            print(f"  Response: {response.text}")
            return False
        
        result = response.json()
        print(f"   Response: {result}")
        
        # Check the database to verify update
        print("\n4. Checking database...")
        db.expire(test_user)  # Refresh from DB
        test_user = db.query(models.User).filter(
            models.User.user_id == test_user.user_id
        ).first()
        
        new_timestamp = test_user.last_active
        print(f"   Old last_active: {old_timestamp}")
        print(f"   New last_active: {new_timestamp}")
        
        # Verify the timestamp was updated
        if old_timestamp and new_timestamp and new_timestamp > old_timestamp:
            time_diff = (new_timestamp - old_timestamp).total_seconds()
            print(f"\n✓ SUCCESS! Timestamp updated by {time_diff:.1f} seconds")
            return True
        else:
            print(f"\n✗ FAILED! Timestamp was not updated properly")
            return False
            
    except Exception as e:
        print(f"\n✗ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return False
    finally:
        db.close()

if __name__ == "__main__":
    test_login_timestamp_update()
