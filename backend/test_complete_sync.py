"""
Complete test: Start session, answer questions, finish, verify sync
"""
import requests
import time

print("=" * 70)
print("COMPLETE TEST: Adaptive Assessment with user_test_attempts Sync")
print("=" * 70)

# Step 1: Start session
print("\n1️⃣ Starting adaptive assessment session...")
start_data = {'userId': 30, 'maxQuestions': 15}
response = requests.post('http://localhost:8000/adaptive/start', json=start_data)

if response.status_code != 200:
    print(f"❌ Failed to start: {response.status_code}")
    exit(1)

session_id = response.json().get('session_id')
print(f"✓ Session created: {session_id}")

# Step 2: Answer questions
print("\n2️⃣ Answering questions...")
current_question = response.json().get('first_question')
answers_count = 0

for i in range(12):  # Answer 12 questions to exceed minimum
    if not current_question or not current_question.get('question_id'):
        print(f"No more questions")
        break
    
    question_id = current_question['question_id']
    options = current_question.get('options', [])
    
    if not options:
        print(f"No options for question {question_id}")
        break
    
    chosen_option_id = options[0]['option_id']
    
    answer_data = {
        'sessionId': session_id,
        'questionId': question_id,
        'chosenOptionId': chosen_option_id
    }
    
    response = requests.post('http://localhost:8000/adaptive/answer', json=answer_data)
    
    if response.status_code != 200:
        print(f"Error answering question: {response.status_code}")
        break
    
    result = response.json()
    answers_count += 1
    
    if result.get('is_complete'):
        print(f"✓ Assessment completed after {answers_count} questions")
        break
    else:
        current_question = result.get('next_question')
        print(f"✓ Answered question {answers_count}")

# Step 3: Check database
print("\n3️⃣ Checking database sync...")
time.sleep(2)  # Give database time to sync

import database, models
from sqlalchemy import text, desc

db = database.SessionLocal()

# Get latest attempt info
test_latest = db.query(models.TestAttempt).order_by(desc(models.TestAttempt.attempt_id)).first()
user_latest = db.execute(text(
    'SELECT attempt_id, user_id FROM user_test_attempts ORDER BY attempt_id DESC LIMIT 1'
)).first()

print(f"\ntest_attempts (System-wide log):")
if test_latest:
    print(f"  Latest: ID {test_latest.attempt_id}, User {test_latest.user_id}, Time: {test_latest.taken_at}")

print(f"\nuser_test_attempts (Per-user history):")
if user_latest:
    print(f"  Latest: ID {user_latest[0]}, User {user_latest[1]}")

# Verify sync
print(f"\n" + "=" * 70)
if test_latest and user_latest and test_latest.attempt_id == user_latest[0]:
    print("✅ SYNC VERIFIED: New attempt is in BOTH tables!")
    print(f"   Attempt ID {test_latest.attempt_id} is synced for User {test_latest.user_id}")
else:
    print("❌ SYNC FAILED: New attempt NOT in user_test_attempts")

# Show user-specific history
print(f"\n📊 User 30's Test History (from user_test_attempts):")
user_30_attempts = db.execute(text(
    'SELECT attempt_id, attempt_date FROM user_test_attempts WHERE user_id = 30 ORDER BY attempt_id DESC LIMIT 3'
)).fetchall()

for attempt_id, attempt_date in user_30_attempts:
    print(f"  - Attempt {attempt_id}: {attempt_date}")

db.close()
