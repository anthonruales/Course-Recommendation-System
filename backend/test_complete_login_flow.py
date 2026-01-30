"""
Complete login flow test - simulates what happens when a user logs in
"""

import requests
import time
from database import SessionLocal
import models

def test_complete_login_flow():
    """Test complete login flow with timestamp update"""
    
    db = SessionLocal()
    
    try:
        print("=" * 80)
        print("TEST: Complete Login Flow")
        print("=" * 80)
        
        # Get test user
        test_user = db.query(models.User).filter(
            models.User.email == "namiaenerson939@gmail.com"
        ).first()
        
        if not test_user:
            print("✗ Test user not found!")
            return False
        
        print(f"\n1. Test user: {test_user.fullname} (ID: {test_user.user_id}, Email: {test_user.email})")
        print(f"   BEFORE login - last_active: {test_user.last_active}")
        
        old_timestamp = test_user.last_active
        
        # Wait a second
        print("\n2. Waiting 2 seconds before login simulation...")
        time.sleep(2)
        
        # Simulate Step 1: Call /google-login endpoint
        print("\n3. Step 1 - Simulating /google-login endpoint...")
        google_login_response = requests.post(
            'http://localhost:8000/google-login',
            json={'email': test_user.email, 'name': test_user.fullname}
        )
        
        if google_login_response.status_code != 200:
            print(f"   ✗ /google-login failed with status {google_login_response.status_code}")
            return False
        
        google_data = google_login_response.json()
        user_id = google_data.get('user_id')
        print(f"   ✓ /google-login successful - user_id: {user_id}")
        
        # Wait a second
        time.sleep(1)
        
        # Simulate Step 2: Call /refresh-user-activity endpoint (like the frontend does)
        print("\n4. Step 2 - Simulating /refresh-user-activity endpoint call...")
        refresh_response = requests.post(
            f'http://localhost:8000/refresh-user-activity/{user_id}'
        )
        
        if refresh_response.status_code != 200:
            print(f"   ✗ /refresh-user-activity failed with status {refresh_response.status_code}")
            return False
        
        refresh_data = refresh_response.json()
        print(f"   ✓ /refresh-user-activity successful")
        print(f"   Response: {refresh_data}")
        
        # Check database
        print("\n5. Checking database after login...")
        db.expire(test_user)
        test_user = db.query(models.User).filter(
            models.User.user_id == test_user.user_id
        ).first()
        
        new_timestamp = test_user.last_active
        
        print(f"   BEFORE login: {old_timestamp}")
        print(f"   AFTER login:  {new_timestamp}")
        
        if old_timestamp and new_timestamp and new_timestamp > old_timestamp:
            time_diff = (new_timestamp - old_timestamp).total_seconds()
            print(f"\n✅ SUCCESS! Timestamp updated by {time_diff:.1f} seconds")
            return True
        else:
            print(f"\n❌ FAILED! Timestamp was not updated")
            return False
            
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return False
    finally:
        db.close()

if __name__ == "__main__":
    success = test_complete_login_flow()
    print("\n" + "=" * 80)
    if success:
        print("RESULT: LOGIN FLOW WORKING CORRECTLY ✅")
    else:
        print("RESULT: LOGIN FLOW FAILED ❌")
    print("=" * 80)
