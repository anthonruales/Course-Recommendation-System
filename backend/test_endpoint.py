"""
Direct test of the /user/{user_id}/assessment-history endpoint
"""
from database import SessionLocal
from main import get_assessment_history

db = SessionLocal()

print("=" * 80)
print("TESTING ASSESSMENT HISTORY ENDPOINT")
print("=" * 80)

# Get assessment history for user 48
result = get_assessment_history(user_id=48, db=db)

print(f"\n[RESULT] Total attempts: {result['total_attempts']}")

if result['history']:
    latest = result['history'][0]
    print(f"\n[LATEST ATTEMPT] {latest['attempt_id']}")
    print(f"  Test: {latest['test_name']}")
    print(f"  Questions answered: {latest['questions_answered']}")
    print(f"  Recommendations: {latest['recommendation_count']}")
    
    if latest['recommended_courses']:
        print(f"\n  Recommended Courses:")
        for i, course in enumerate(latest['recommended_courses'], 1):
            print(f"    {i}. {course['course_name']}")
            print(f"       Description: {course['description'][:60]}...")
            print(f"       Reasoning: {course['reasoning'][:60]}...")
    else:
        print(f"\n  [WARN] No recommended courses found")
else:
    print("\n[ERROR] No history found")

print("\n" + "=" * 80)

db.close()
