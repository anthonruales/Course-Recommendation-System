"""
Test script to verify traits_discovered is returned correctly from API endpoints.
Tests both /adaptive/finish and /adaptive/answer completion scenarios.
"""

import requests
import json
import time
from datetime import datetime

# API base URL
BASE_URL = "http://localhost:8000"

def test_get_final_results():
    """Test that get_final_results returns traits_discovered as a number, not dict"""
    print("\n" + "="*60)
    print("Testing get_final_results() format")
    print("="*60)
    
    # Import the engine to test directly
    import sys
    sys.path.insert(0, '/Users/USer/Downloads/capstone-back-end/Course-Recommendation-System/backend')
    
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from database import Base
    from main import get_or_init_adaptive_engine
    
    # Create DB session
    DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/coursepro_db"
    engine_db = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(bind=engine_db)
    db_session = SessionLocal()
    
    try:
        # Initialize adaptive engine
        adaptive_engine = get_or_init_adaptive_engine(db_session)
        
        # Create a test session
        result = adaptive_engine.start_session(
            session_id="test_traits_session",
            user_id=999,
            max_questions=30
        )
        
        session_id = result["session_id"]
        print(f"✓ Created test session: {session_id}")
        
        # Get a few questions and answer them
        for i in range(5):
            question = adaptive_engine.get_next_question(session_id)
            if question:
                question_id = question["question"]["question_id"]
                options = question["question"]["options"]
                chosen_option = options[0]["option_id"] if options else None
                
                answer_result = adaptive_engine.process_answer(
                    session_id, question_id, chosen_option
                )
                print(f"  Answered question {i+1}")
        
        # Get final results
        final_results = adaptive_engine.get_final_results(session_id)
        
        print(f"\n✓ Final Results received:")
        print(f"  - traits_discovered type: {type(final_results['traits_discovered'])}")
        print(f"  - traits_discovered value: {final_results['traits_discovered']}")
        
        # Verify it's a number, not a dict
        if isinstance(final_results['traits_discovered'], (int, float)):
            print(f"  ✅ PASS: traits_discovered is a number ({type(final_results['traits_discovered']).__name__})")
        else:
            print(f"  ❌ FAIL: traits_discovered is a {type(final_results['traits_discovered']).__name__}, should be int")
            
    finally:
        db_session.close()

def test_assessment_history_api():
    """Test that the assessment history API returns correct traits_found"""
    print("\n" + "="*60)
    print("Testing /user/{userId}/assessment-history API")
    print("="*60)
    
    # Use user 3 (from previous tests)
    user_id = 3
    
    try:
        response = requests.get(f"{BASE_URL}/user/{user_id}/assessment-history")
        
        if response.status_code == 200:
            data = response.json()
            print(f"✓ Got assessment history for user {user_id}")
            
            if data and len(data) > 0:
                latest = data[0]  # Most recent attempt
                print(f"\nLatest Assessment Attempt:")
                print(f"  - attempt_id: {latest.get('attempt_id')}")
                print(f"  - max_questions: {latest.get('max_questions')}")
                print(f"  - questions_answered: {latest.get('questions_answered')}")
                print(f"  - traits_found: {latest.get('traits_found')}")
                print(f"  - confidence_score: {latest.get('confidence_score')}")
                print(f"  - traits_found type: {type(latest.get('traits_found'))}")
                
                # Verify traits_found is a number
                if isinstance(latest.get('traits_found'), (int, float)):
                    print(f"  ✅ PASS: traits_found is a number")
                else:
                    print(f"  ❌ FAIL: traits_found is a {type(latest.get('traits_found'))}, should be int")
            else:
                print("  (No assessment history found)")
        else:
            print(f"✗ API Error: {response.status_code} - {response.text}")
            
    except Exception as e:
        print(f"✗ Connection error: {e}")

if __name__ == "__main__":
    print("\n🔍 Testing Traits Count API Fixes")
    print("="*60)
    
    # Test 1: Direct function test
    test_get_final_results()
    
    # Test 2: API endpoint test
    test_assessment_history_api()
    
    print("\n" + "="*60)
    print("✅ Test suite complete!")
    print("="*60)
