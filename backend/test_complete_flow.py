"""
Test complete flow: Adaptive Assessment -> Recommendations -> API endpoint display
"""
import requests
import json
from database import SessionLocal
from main import get_or_init_adaptive_engine, save_adaptive_session_to_db
import models

# Test configuration
API_BASE = "http://127.0.0.1:8000"
TEST_USER_ID = 48
TEST_USER_EMAIL = "testdirect@test.com"

print("=" * 80)
print("COMPLETE FLOW TEST: Adaptive Assessment -> API Response")
print("=" * 80)

# Step 1: Get database session
db = SessionLocal()
print("\n[1] Getting database session...")

# Step 2: Initialize adaptive engine
print("[2] Initializing adaptive assessment engine...")
engine = get_or_init_adaptive_engine(db)

# Step 3: Create new adaptive session
print("[3] Creating adaptive session...")
session = engine.create_session()
session_id = session['session_id']
print(f"    Session ID: {session_id}")

# Step 4: Answer 15 questions quickly
print("[4] Answering assessment questions...")
answered_questions = {}
for i in range(15):
    next_q = engine.get_next_question(session_id)
    question = next_q.get('question', next_q)
    question_id = question['question_id']
    options = question['options']
    
    # Just pick first option for this test
    chosen_option = options[0]
    option_id = chosen_option['option_id']
    
    # Process answer
    engine.process_answer(session_id, question_id, option_id)
    answered_questions[question_id] = option_id
    print(f"    Q{i+1}/{15}: Question {question_id} answered")

# Step 5: Finish session and get recommendations
print("[5] Completing adaptive session...")
result = engine.finish_early(session_id)
recommendations = result.get('recommendations', [])
print(f"    Recommendations generated: {len(recommendations)}")

# Step 6: Save to database
print("[6] Saving to database...")
save_adaptive_session_to_db(db, engine, session_id, recommendations, TEST_USER_ID, answered_questions)
print(f"    Saved successfully with {len(recommendations)} recommendations")

# Step 7: Query API endpoint
print(f"\n[7] Querying API: /user/{TEST_USER_ID}/assessment-history")
try:
    response = requests.get(f"{API_BASE}/user/{TEST_USER_ID}/assessment-history")
    if response.status_code == 200:
        data = response.json()
        history = data.get('history', [])
        print(f"    Found {len(history)} assessment attempts")
        
        if history:
            latest = history[0]
            rec_count = latest.get('recommendation_count', 0)
            print(f"    Latest attempt has {rec_count} recommendations")
            
            if rec_count > 0:
                print(f"\n[SUCCESS] Recommendations in API response:")
                for rec in latest['recommended_courses']:
                    print(f"      - {rec['course_name']}")
                    print(f"        Reasoning: {rec['reasoning'][:60]}...")
            else:
                print("[WARN] No recommendations in latest attempt")
    else:
        print(f"[ERROR] API returned {response.status_code}")
        print(response.text)
except Exception as e:
    print(f"[ERROR] Failed to call API: {e}")

print("\n" + "=" * 80)
print("TEST COMPLETE")
print("=" * 80)

db.close()
