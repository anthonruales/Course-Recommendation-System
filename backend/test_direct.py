#!/usr/bin/env python3
"""
Direct test of adaptive assessment and recommendations WITHOUT HTTP calls.
Tests in-process to understand why recommendations aren't being saved.
"""
import sys
sys.path.insert(0, '.')

from database import SessionLocal
from models import User, TestAttempt, Recommendation, Course, Question
import models
import main  # Import to get save_adaptive_session_to_db
import datetime

def test_adaptive_flow():
    db = SessionLocal()
    
    try:
        # Step 1: Get or create a test user
        print("\n[1] Get/create test user...")
        user = db.query(User).filter(User.username == "testdirect").first()
        if not user:
            user = User(
                username="testdirect",
                email="testdirect@test.com",
                password_hash="test"
            )
            db.add(user)
            db.commit()
            db.refresh(user)
        print(f"    User ID: {user.user_id}, Username: {user.username}")
        
        # Step 2: Initialize adaptive engine using the same method as main.py
        print("\n[2] Initialize adaptive assessment engine...")
        engine = main.get_or_init_adaptive_engine(db)
        print(f"    Engine ready with {len(engine.courses)} courses and {len(engine.questions)} questions")
        
        # Step 3: Create session
        print(f"\n[3] Start adaptive session...")
        session_id = engine.create_session(user.user_id, max_questions=15)
        print(f"    Session ID: {session_id}")
        
        # Step 4: Answer 15 questions
        print(f"\n[4] Answer {15} questions...")
        for i in range(15):
            session = engine.sessions.get(session_id)
            if not session:
                print(f"    ERROR: Session lost")
                break
            
            if session.is_complete:
                print(f"    Session marked complete after {i} questions")
                break
            
            next_q = engine.get_next_question(session_id)
            if not next_q:
                print(f"    No more questions")
                break
            
            # Debug: show what we got
            if i == 0:
                print(f"    DEBUG: First question keys: {next_q.keys()}")
                print(f"    DEBUG: Has options? {'options' in next_q}")
                if 'options' in next_q:
                    print(f"    DEBUG: Options count: {len(next_q['options'])}")
            
            # Find first option to answer with
            # The response includes metadata - actual question is in 'question' field
            actual_question = next_q.get('question', next_q)
            options = actual_question.get('options', [])
            if not options:
                print(f"    Q{i+1}: No options available! Question keys: {actual_question.keys() if isinstance(actual_question, dict) else 'not a dict'}")
                break
            
            chosen_option_id = options[0].get('option_id')
            if not chosen_option_id:
                print(f"    Q{i+1}: Option has no option_id!")
                break
            
            question_id = actual_question.get('question_id')
            print(f"    Q{i+1}: '{actual_question.get('question_text', '')[:40]}...' -> Chose option {chosen_option_id}")
            
            # Process answer
            result = engine.process_answer(session_id, question_id, chosen_option_id)
            
            if 'error' in result:
                print(f"    ERROR: {result['error']}")
                break
            
            # Check if complete
            if result.get('status') == 'complete':
                print(f"    Session complete at question {i+1}")
                break
        
        # Step 5: Finish session and get results
        print(f"\n[5] Finish adaptive session...")
        session = engine.sessions.get(session_id)
        if not session or not session.is_complete:
            # Call finish_early to wrap up
            result = engine.finish_early(session_id)
        else:
            result = {"recommendations": session.final_recommendations} if hasattr(session, 'final_recommendations') else None
        
        if not result:
            print(f"    ERROR: No result from finish")
            return
        
        print(f"    Result keys: {result.keys() if result else 'None'}")
        if result:
            recs = result.get('recommendations', [])
            print(f"    Recommendations returned: {len(recs)}")
            for idx, rec in enumerate(recs[:3]):
                print(f"      [{idx}] {rec.get('course_name', 'N/A')} - {rec.get('match_percentage', 0)}%")
        
        # Step 6: Call save function directly
        print(f"\n[6] Call save_adaptive_session_to_db()...")
        if result:
            recs = result.get('recommendations', [])
            session = engine.sessions.get(session_id)
            answered_q = session.answered_questions if session else []
            
            print(f"    Saving with:")
            print(f"      - session_id: {session_id}")
            print(f"      - recommendations: {len(recs)}")
            print(f"      - user_id: {user.user_id}")
            print(f"      - answered_questions: {len(answered_q)}")
            
            main.save_adaptive_session_to_db(
                db,
                engine,
                session_id,
                recs,
                user.user_id,
                answered_q
            )
            print(f"    Save function completed")
        
        # Step 7: Check what's in database
        print(f"\n[7] Check database for saved data...")
        latest_attempt = db.query(TestAttempt).filter(
            TestAttempt.user_id == user.user_id
        ).order_by(TestAttempt.attempt_id.desc()).first()
        
        if latest_attempt:
            print(f"    Latest attempt: {latest_attempt.attempt_id}")
            print(f"    Test ID: {latest_attempt.test_id}")
            
            recs_in_db = db.query(Recommendation).filter(
                Recommendation.attempt_id == latest_attempt.attempt_id
            ).all()
            print(f"    Recommendations in DB: {len(recs_in_db)}")
            for rec in recs_in_db:
                course = db.query(Course).filter(Course.course_id == rec.course_id).first()
                course_name = course.course_name if course else "UNKNOWN"
                print(f"      - {course_name}: {rec.reasoning[:50]}...")
        else:
            print(f"    No attempts found!")
        
        # Summary
        print("\n" + "="*60)
        if latest_attempt and len(recs_in_db) > 0:
            print(f"SUCCESS! Found {len(recs_in_db)} recommendations in database")
        else:
            print(f"FAIL! No recommendations in database")
        print("="*60)
        # Summary
        print("\n" + "="*60)
        if latest_attempt and len(recs_in_db) > 0:
            print(f"SUCCESS! Found {len(recs_in_db)} recommendations in database")
        else:
            print(f"FAIL! No recommendations in database")
        print("="*60)
        
    except Exception as e:
        print(f"ERROR: {e}")
        import traceback
        traceback.print_exc()
    finally:
        db.close()

if __name__ == "__main__":
    test_adaptive_flow()
