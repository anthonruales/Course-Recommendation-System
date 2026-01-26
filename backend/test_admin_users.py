"""
Test the admin users endpoint
"""
import requests
import json

print("Testing admin users endpoint...")
print("=" * 70)

response = requests.get('http://localhost:8000/admin/users')

if response.status_code == 200:
    data = response.json()
    users = data.get('users', [])
    
    print(f'\nFound {len(users)} users:\n')
    
    for user in users:
        strand = user['academic_info'].get('strand') if user['academic_info'] else 'N/A'
        gwa = user['academic_info'].get('gwa') if user['academic_info'] else 'N/A'
        
        print(f"User: {user['fullname']} ({user['email']})")
        print(f"  Strand: {strand}")
        print(f"  GWA: {gwa}")
        print(f"  Tests Taken: {user['tests_taken']}")
        print(f"  Last Active: {user['last_active']}")
        print(f"  Status: {user['status']}")
        print()
else:
    print(f'Error: {response.status_code}')
    print(response.text)
