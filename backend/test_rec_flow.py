#!/usr/bin/env python3
"""
Test the complete adaptive assessment flow and verify recommendations are saved.
"""
import requests
import json
import time
from database import SessionLocal
from models import User, TestAttempt, Recommendation

API_BASE = "http://localhost:8000"

def get_test_user():
    """Get or create a test user"""
    db = SessionLocal()
    user = db.query(User).filter(User.username == "testrec").first()
    if not user:
        user = User(
            username="testrec",
            email="testrec@test.com",
            password_hash="test",
            is_admin=False,
            is_online=0
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        print(f"Created test user: {user.user_id}")
    else:
        print(f"Found test user: {user.user_id}")
    db.close()
    return user

def login(username, password):
    """Login and get token"""
    response = requests.post(f"{API_BASE}/login", json={
        "username": username,
        "password": password
    })
    if response.status_code == 200:
        data = response.json()
        print(f"Login successful: {data}")
        return data.get("access_token")
    else:
        print(f"Login failed: {response.status_code}")
        print(response.text)
        return None

def start_adaptive():
    """Start adaptive assessment"""
    response = requests.post(f"{API_BASE}/adaptive/start", json={
        "test_name": "Test Session"
    })
    if response.status_code == 200:
        data = response.json()
        print(f"Adaptive session started: {data.get('session_id')}")
        return data
    else:
        print(f"Failed to start adaptive: {response.status_code}")
        print(response.text)
        return None

def answer_question(session_id, question_id, answer):
    """Answer a question"""
    response = requests.post(f"{API_BASE}/adaptive/answer", json={
        "session_id": session_id,
        "question_id": question_id,
        "answer": answer
    })
    return response.json() if response.status_code == 200 else None

def finish_assessment(session_id, token):
    """Finish adaptive assessment"""
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(f"{API_BASE}/adaptive/finish", 
        json={"session_id": session_id},
        headers=headers
    )
    if response.status_code == 200:
        data = response.json()
        print(f"Assessment finished. Response keys: {data.keys()}")
        if "recommendations" in data:
            print(f"Recommendations in response: {len(data['recommendations'])}")
            for rec in data['recommendations'][:3]:
                print(f"  - {rec}")
        return data
    else:
        print(f"Failed to finish: {response.status_code}")
        print(response.text)
        return None

def check_db_recommendations(user_id):
    """Check what's in the database"""
    db = SessionLocal()
    
    # Get latest attempt
    attempt = db.query(TestAttempt).filter(
        TestAttempt.user_id == user_id
    ).order_by(TestAttempt.attempt_id.desc()).first()
    
    if not attempt:
        print("No attempts found in database")
        db.close()
        return
    
    print(f"Latest attempt: {attempt.attempt_id} (test_type={attempt.test_type})")
    
    # Get recommendations
    recs = db.query(Recommendation).filter(
        Recommendation.attempt_id == attempt.attempt_id
    ).all()
    
    print(f"Recommendations in DB: {len(recs)}")
    for rec in recs:
        print(f"  - Course ID {rec.course_id}: {rec.reasoning}")
    
    db.close()
    return len(recs)

def main():
    print("=" * 60)
    print("TEST: Complete Adaptive Assessment & Recommendations Flow")
    print("=" * 60)
    
    # Step 1: Get test user
    print("\n[STEP 1] Get test user...")
    user = get_test_user()
    user_id = user.user_id
    
    # Step 2: Login
    print("\n[STEP 2] Login...")
    token = login("testrec", "test")
    if not token:
        print("ERROR: Could not login")
        return
    
    # Step 3: Start adaptive
    print("\n[STEP 3] Start adaptive assessment...")
    session_data = start_adaptive()
    if not session_data:
        print("ERROR: Could not start adaptive")
        return
    session_id = session_data.get("session_id")
    
    # Step 4: Answer some questions
    print("\n[STEP 4] Answer questions...")
    for i in range(15):  # Answer 15 questions
        if "next_question" not in session_data:
            print(f"No more questions after {i} answers")
            break
        
        q = session_data.get("next_question")
        print(f"  Q{i+1}: {q.get('text', '')[:50]}...")
        
        # Simple logic: pick answer based on question
        answer = "Yes" if i % 2 == 0 else "No"
        result = answer_question(session_id, q.get("id"), answer)
        
        if result:
            session_data = result
            if "recommendation_reason" in result:
                print(f"    -> {result.get('recommendation_reason', '')[:40]}...")
        else:
            print(f"    ERROR: Could not answer question")
            break
    
    # Step 5: Finish assessment
    print("\n[STEP 5] Finish assessment...")
    final = finish_assessment(session_id, token)
    if not final:
        print("ERROR: Could not finish assessment")
        return
    
    # Step 6: Check database
    print("\n[STEP 6] Check database for recommendations...")
    time.sleep(1)  # Wait a moment for database commit
    count = check_db_recommendations(user_id)
    
    # Results
    print("\n" + "=" * 60)
    if count and count > 0:
        print(f"SUCCESS! Found {count} recommendations in database")
    else:
        print(f"FAIL! No recommendations found in database")
        print("\nDebugging info:")
        print(f"  - Session ID: {session_id}")
        print(f"  - User ID: {user_id}")
        print(f"  - Recommendations in response: {len(final.get('recommendations', []))}")
    print("=" * 60)

if __name__ == "__main__":
    main()
