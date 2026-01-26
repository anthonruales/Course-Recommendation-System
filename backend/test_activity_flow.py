#!/usr/bin/env python
"""
Test script to verify the activity tracking flow:
1. User logs in / updates activity
2. Admin sees user as Online with recent timestamp
3. User logs out
4. Admin sees user as Offline
"""
import requests
import time

print('=== ACTIVITY TRACKING FLOW TEST ===')
print()

# 1. Update activity for user ID 3 (kamansi)
print('1. User 3 (kamansi) logs in / updates activity...')
response = requests.post('http://localhost:8000/user/3/update-activity')
print(f'   Status: {response.status_code}')
print()

# 2. Wait a bit
time.sleep(1)

# 3. Check admin view
print('2. Admin checks user activity...')
response = requests.get('http://localhost:8000/admin/users')
users = response.json()['users']

# Find user 3
user3 = [u for u in users if u['user_id'] == 3][0]
print(f'   User 3 (kamansi):')
print(f'   - Last Active: {user3.get("last_active")}')
print(f'   - Status: {user3.get("status")}')
print()

# 4. Simulate user logout
print('3. User 3 logs out...')
response = requests.post('http://localhost:8000/logout', json={'user_id': 3})
print(f'   Status: {response.status_code}')
print()

# 5. Check admin view after logout
time.sleep(1)
print('4. Admin checks user activity after logout...')
response = requests.get('http://localhost:8000/admin/users')
users = response.json()['users']

user3 = [u for u in users if u['user_id'] == 3][0]
print(f'   User 3 (kamansi):')
print(f'   - Last Active: {user3.get("last_active")}')
print(f'   - Status: {user3.get("status")}')
print()
print('=== TEST COMPLETE ===')
