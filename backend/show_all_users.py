import requests

print('=== ADMIN DASHBOARD - ALL USERS ===')
print()

response = requests.get('http://localhost:8000/admin/users')
users = response.json()['users']

for user in users:
    print(f"ID: {user['user_id']:<3} | {user['fullname']:<20} | Last Active: {user.get('last_active', 'Never'):<15} | Status: {user.get('status', 'Unknown'):<10} | Online: {user.get('is_online', 0)}")
