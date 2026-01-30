"""
Quick test to verify the API changes work correctly.
This checks that traits_discovered is returned as a number, not a dict.
"""

import requests
import json

BASE_URL = "http://localhost:8000"

def test_assessment_history():
    """Test that assessment history returns traits_found as a number"""
    print("\n🧪 Testing Assessment History API")
    print("=" * 50)
    
    # Test with user 3 (or any user with assessments)
    user_id = 3
    
    try:
        response = requests.get(f"{BASE_URL}/user/{user_id}/assessment-history")
        
        if response.status_code == 200:
            data = response.json()
            
            if data and len(data) > 0:
                # Check the latest attempt
                latest = data[0]
                
                print(f"✅ Got assessment history for user {user_id}")
                print(f"\nLatest Assessment:")
                print(f"  - attempt_id: {latest.get('attempt_id')}")
                print(f"  - max_questions: {latest.get('max_questions')}")
                print(f"  - questions_answered: {latest.get('questions_answered')}")
                print(f"  - traits_found: {latest.get('traits_found')}")
                print(f"  - confidence_score: {latest.get('confidence_score')}")
                
                # Verify types
                traits = latest.get('traits_found')
                print(f"\n📊 Data Type Check:")
                print(f"  - traits_found type: {type(traits).__name__}")
                
                if isinstance(traits, (int, float)):
                    print(f"  ✅ PASS: traits_found is a {type(traits).__name__} (correct)")
                elif isinstance(traits, dict):
                    print(f"  ❌ FAIL: traits_found is a dict (should be int/float)")
                else:
                    print(f"  ❌ FAIL: traits_found is {type(traits).__name__}")
                    
            else:
                print("⚠️  No assessment history found for this user")
        else:
            print(f"❌ API Error: {response.status_code}")
            print(f"   Response: {response.text}")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("API Response Type Verification")
    print("=" * 50)
    
    test_assessment_history()
    
    print("\n" + "=" * 50)
    print("Test Complete!")
    print("=" * 50)
