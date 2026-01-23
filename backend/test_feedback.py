#!/usr/bin/env python3
"""
Quick test script for feedback endpoint
Run this while the backend is running to test feedback submission
"""
import requests
import json

BASE_URL = "http://localhost:8000"

def test_overall_feedback():
    """Test overall feedback submission"""
    print("\n" + "="*60)
    print("Testing Overall Feedback Submission")
    print("="*60)
    
    payload = {
        "rating": 4,
        "feedback_text": "Great recommendations!",
        "user_id": None
    }
    
    print(f"Payload: {json.dumps(payload, indent=2)}")
    print(f"\nSending POST request to {BASE_URL}/feedback/submit...")
    
    try:
        response = requests.post(
            f"{BASE_URL}/feedback/submit",
            json=payload,
            headers={"Content-Type": "application/json"}
        )
        
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        
        if response.status_code == 200:
            print("\n✅ Overall Feedback Test PASSED!")
        else:
            print(f"\n❌ Overall Feedback Test FAILED: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")

def test_specific_feedback():
    """Test specific recommendation feedback submission"""
    print("\n" + "="*60)
    print("Testing Specific Recommendation Feedback")
    print("="*60)
    
    payload = {
        "recommendation_id": 1,
        "user_id": 1,
        "rating": 5,
        "feedback_text": "Perfect match for me!"
    }
    
    print(f"Payload: {json.dumps(payload, indent=2)}")
    print(f"\nSending POST request to {BASE_URL}/feedback/submit...")
    
    try:
        response = requests.post(
            f"{BASE_URL}/feedback/submit",
            json=payload,
            headers={"Content-Type": "application/json"}
        )
        
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        
        if response.status_code == 200:
            print("\n✅ Specific Feedback Test PASSED!")
        else:
            print(f"\n❌ Specific Feedback Test FAILED: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    print("Feedback Endpoint Test Suite")
    print("Make sure the backend is running on http://localhost:8000")
    
    test_overall_feedback()
    test_specific_feedback()
    
    print("\n" + "="*60)
    print("Test completed!")
    print("="*60)
