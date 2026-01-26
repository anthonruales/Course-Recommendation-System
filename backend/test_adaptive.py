#!/usr/bin/env python3
"""
Test script for adaptive assessment functionality
"""
import requests
import json

def test_adaptive_assessment():
    print("Testing adaptive assessment flow...")
    
    # Step 1: Start session
    start_data = {"userId": 30, "maxQuestions": 10}
    response = requests.post("http://localhost:8000/adaptive/start", json=start_data)
    print(f"Step 1 - Start session: {response.status_code}")
    
    if response.status_code != 200:
        print(f"Failed to start session: {response.text}")
        return
    
    session_data = response.json()
    session_id = session_data.get("session_id")
    print(f"Session ID: {session_id}")
    
    # Step 2: Answer a few questions
    current_question = session_data.get("first_question")
    
    for round_num in range(5):  # Answer up to 5 questions
        if not current_question or not current_question.get("question_id"):
            print("No question available")
            break
            
        question_id = current_question["question_id"]
        options = current_question.get("options", [])
        if not options:
            print("No options available")
            break
            
        # Choose first option
        chosen_option_id = options[0]["option_id"]
        
        answer_data = {
            "sessionId": session_id,
            "questionId": question_id,
            "chosenOptionId": chosen_option_id
        }
        
        response = requests.post("http://localhost:8000/adaptive/answer", json=answer_data)
        print(f"Step 2.{round_num+1} - Answer question: {response.status_code}")
        
        if response.status_code != 200:
            print(f"Error: {response.text[:100]}")
            break
            
        result = response.json()
        if result.get("is_complete"):
            print("Assessment completed!")
            recommendations = result.get("recommendations", [])
            print(f"Recommendations received: {len(recommendations)}")
            if recommendations:
                print(f"Top recommendation: {recommendations[0].get('course_name')}")
            break
        else:
            current_question = result.get("next_question")
            current_round = result.get("current_round", "?")
            confidence = result.get("confidence", 0)
            print(f"  Round {current_round}, Confidence: {confidence}%")
    
    print("Flow test completed!")
    
    # Step 3: Check database
    print("\nChecking database for saved data...")
    import models, database
    db = database.SessionLocal()
    
    # Get test attempts for user 30
    attempts = db.query(models.TestAttempt).filter(
        models.TestAttempt.user_id == 30
    ).order_by(models.TestAttempt.taken_at.desc()).limit(3).all()
    
    print(f"Recent test attempts for user 30: {len(attempts)}")
    for attempt in attempts:
        test = db.query(models.Test).filter(models.Test.test_id == attempt.test_id).first()
        answers = db.query(models.StudentAnswer).filter(
            models.StudentAnswer.attempt_id == attempt.attempt_id
        ).count()
        recs = db.query(models.Recommendation).filter(
            models.Recommendation.attempt_id == attempt.attempt_id
        ).count()
        
        print(f"  Attempt {attempt.attempt_id}: {test.test_type if test else 'Unknown'} test, {answers} answers, {recs} recommendations, {attempt.taken_at}")
    
    db.close()

if __name__ == "__main__":
    test_adaptive_assessment()