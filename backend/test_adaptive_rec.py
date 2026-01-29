#!/usr/bin/env python
"""Test adaptive assessment and check if recommendations are saved"""

import requests
import json
import time

BASE_URL = "http://localhost:8000"

# Step 1: Start an adaptive assessment
print("\n🧪 Step 1: Starting adaptive assessment...")
start_response = requests.post(f"{BASE_URL}/adaptive/start", json={
    "userId": 42,
    "numQuestions": 20
})
print(f"Status: {start_response.status_code}")
if start_response.status_code == 200:
    start_data = start_response.json()
    session_id = start_data.get("sessionId")
    print(f"[OK] Session started: {session_id}")
    print(f"   First question ID: {start_data.get('question', {}).get('question_id')}")
else:
    print(f"[ERROR] Error: {start_response.text}")
    exit(1)

# Step 2: Answer a few questions
print("\n🧪 Step 2: Answering questions...")
for i in range(15):  # Answer 15 questions to meet minimum
    answer_response = requests.post(f"{BASE_URL}/adaptive/answer", json={
        "sessionId": session_id,
        "questionId": start_data.get('question', {}).get('question_id'),
        "chosenOptionId": i + 100  # Just pick any option
    })
    if answer_response.status_code == 200:
        answer_data = answer_response.json()
        start_data['question'] = answer_data.get('nextQuestion', {})
        print(f"  [OK] Question {i+1} answered")
    else:
        print(f"  ✗ Error on question {i+1}: {answer_response.status_code}")
        break

# Step 3: Finish assessment early
print("\n🧪 Step 3: Finishing assessment...")
finish_response = requests.post(f"{BASE_URL}/adaptive/finish", json={
    "sessionId": session_id
})
print(f"Status: {finish_response.status_code}")
if finish_response.status_code == 200:
    finish_data = finish_response.json()
    print(f"[OK] Assessment finished")
    print(f"   Total questions: {finish_data.get('total_questions')}")
    print(f"   Recommendations: {len(finish_data.get('recommendations', []))}")
    if finish_data.get('recommendations'):
        for rec in finish_data.get('recommendations', [])[:3]:
            print(f"     - {rec.get('course_name')}: {rec.get('match_percentage')}%")
else:
    print(f"[ERROR] Error: {finish_response.text}")
    exit(1)

# Step 4: Check if recommendations were saved
print("\n🧪 Step 4: Checking saved recommendations...")
time.sleep(2)  # Wait for DB to save
history_response = requests.get(f"{BASE_URL}/user/42/assessment-history")
if history_response.status_code == 200:
    history_data = history_response.json()
    print(f"[OK] Retrieved assessment history")
    print(f"   Total attempts: {history_data.get('total_attempts')}")
    if history_data.get('history'):
        latest = history_data['history'][0]
        print(f"   Latest attempt recommendations: {len(latest.get('recommended_courses', []))}")
        if latest.get('recommended_courses'):
            for rec in latest.get('recommended_courses', [])[:3]:
                print(f"     - {rec.get('course_name')}")
else:
    print(f"[ERROR] Error: {history_response.text}")
