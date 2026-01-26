#!/usr/bin/env python
"""
Comprehensive verification script for the activity tracking system.
Tests all user activity scenarios.
"""
import requests
import time
from datetime import datetime

def test_activity_tracking():
    """Test the complete activity tracking flow"""
    
    print("=" * 70)
    print("ACTIVITY TRACKING SYSTEM VERIFICATION".center(70))
    print("=" * 70)
    print()
    
    # Get initial user list
    print("Step 1: Getting initial user list from admin endpoint...")
    response = requests.get('http://localhost:8000/admin/users')
    if response.status_code != 200:
        print(f"❌ FAILED: Could not get admin users (status {response.status_code})")
        return False
    
    users = response.json()['users']
    print(f"✅ Found {len(users)} users in system")
    print()
    
    # Display current status
    print("Current User Status:")
    print("-" * 70)
    for user in users:
        status_icon = "🟢" if user['is_online'] == 1 else "⚫"
        print(f"{status_icon} {user['fullname']:<20} | Last Active: {user['last_active']:<15} | {user['status']}")
    print()
    
    # Test 1: Update activity for a user
    print("=" * 70)
    print("Test 1: User Login / Activity Update")
    print("=" * 70)
    test_user_id = 40  # test_account
    test_user = [u for u in users if u['user_id'] == test_user_id][0]
    
    print(f"User: {test_user['fullname']} (ID: {test_user_id})")
    print(f"Before: Status={test_user['status']}, Last Active={test_user['last_active']}")
    
    response = requests.post(f'http://localhost:8000/user/{test_user_id}/update-activity')
    if response.status_code != 200:
        print(f"❌ FAILED: Activity update failed (status {response.status_code})")
        return False
    
    print(f"✅ Activity updated (200 OK)")
    
    # Check updated status
    time.sleep(0.5)
    response = requests.get('http://localhost:8000/admin/users')
    users = response.json()['users']
    updated_user = [u for u in users if u['user_id'] == test_user_id][0]
    
    print(f"After:  Status={updated_user['status']}, Last Active={updated_user['last_active']}")
    
    if updated_user['status'] == 'Online' and updated_user['last_active'] in ['Just now', '0m ago']:
        print("✅ PASSED: User marked as Online with recent timestamp")
    else:
        print(f"❌ FAILED: Expected Online status and 'Just now' timestamp")
        return False
    print()
    
    # Test 2: Logout user
    print("=" * 70)
    print("Test 2: User Logout")
    print("=" * 70)
    
    response = requests.post('http://localhost:8000/logout', json={'user_id': test_user_id})
    if response.status_code != 200:
        print(f"❌ FAILED: Logout failed (status {response.status_code})")
        return False
    
    print(f"✅ Logout successful (200 OK)")
    
    # Check updated status after logout
    time.sleep(0.5)
    response = requests.get('http://localhost:8000/admin/users')
    users = response.json()['users']
    logged_out_user = [u for u in users if u['user_id'] == test_user_id][0]
    
    print(f"After Logout: Status={logged_out_user['status']}, Last Active={logged_out_user['last_active']}")
    
    if logged_out_user['status'] == 'Offline':
        print("✅ PASSED: User marked as Offline after logout")
    else:
        print(f"❌ FAILED: Expected Offline status")
        return False
    print()
    
    # Test 3: Display all users
    print("=" * 70)
    print("Test 3: Final User Status")
    print("=" * 70)
    response = requests.get('http://localhost:8000/admin/users')
    users = response.json()['users']
    
    print("All Users:")
    print("-" * 70)
    for user in users:
        status_icon = "🟢" if user['is_online'] == 1 else "⚫"
        print(f"{status_icon} {user['fullname']:<20} | Last Active: {user['last_active']:<15} | {user['status']:<10} | Tests: {user['tests_taken']}")
    print()
    
    # Verify at least some users are Online
    online_users = [u for u in users if u['is_online'] == 1]
    if len(online_users) > 0:
        print(f"✅ PASSED: System has {len(online_users)} users marked as Online")
    else:
        print(f"⚠️  WARNING: No users marked as Online")
    
    print()
    print("=" * 70)
    print("✅ ALL TESTS PASSED - ACTIVITY TRACKING SYSTEM WORKING".center(70))
    print("=" * 70)
    
    return True

if __name__ == '__main__':
    try:
        success = test_activity_tracking()
        exit(0 if success else 1)
    except Exception as e:
        print(f"❌ ERROR: {str(e)}")
        exit(1)
