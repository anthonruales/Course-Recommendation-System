"""
Confidence Checker Script

This script helps diagnose confidence calculation discrepancies between
what the student app shows vs what's in the database.

Run: python check_confidence.py <attempt_id>
"""

import sys
from database import SessionLocal
import models
from sqlalchemy import text

def analyze_attempt(attempt_id: int):
    """Analyze a specific test attempt for confidence and question tracking"""
    
    db = SessionLocal()
    
    try:
        # Get the attempt
        attempt = db.query(models.TestAttempt).filter(
            models.TestAttempt.attempt_id == attempt_id
        ).first()
        
        if not attempt:
            print(f"[ERROR] Attempt {attempt_id} not found!")
            return
        
        # Get student answers
        answers = db.query(models.StudentAnswer).filter(
            models.StudentAnswer.attempt_id == attempt_id
        ).all()
        
        # Get recommendations for this attempt
        recommendations = db.query(models.Recommendation).filter(
            models.Recommendation.attempt_id == attempt_id
        ).all()
        
        # Get unique traits from answers
        traits = set()
        for answer in answers:
            option = db.query(models.Option).filter(
                models.Option.option_id == answer.chosen_option_id
            ).first()
            if option and option.trait_tag:
                traits.add(option.trait_tag)
        
        print("=" * 70)
        print(f"ATTEMPT #{attempt_id} ANALYSIS")
        print("=" * 70)
        
        # User info
        user = db.query(models.User).filter(
            models.User.user_id == attempt.user_id
        ).first()
        print(f"\n📋 USER INFO:")
        print(f"   User ID: {attempt.user_id}")
        print(f"   Username: {user.username if user else 'N/A'}")
        print(f"   Taken at: {attempt.taken_at}")
        
        # Quiz configuration (NEW fields)
        print(f"\n🎮 QUIZ CONFIGURATION (from DB):")
        if hasattr(attempt, 'max_questions') and attempt.max_questions:
            print(f"   ✅ Max questions selected: {attempt.max_questions}")
        else:
            print(f"   ⚠️  Max questions: NOT SAVED (column may not exist yet)")
            
        if hasattr(attempt, 'questions_presented') and attempt.questions_presented:
            print(f"   ✅ Questions presented: {attempt.questions_presented}")
        else:
            print(f"   ⚠️  Questions presented: NOT SAVED")
            
        if hasattr(attempt, 'questions_answered') and attempt.questions_answered:
            print(f"   ✅ Questions answered: {attempt.questions_answered}")
        else:
            print(f"   ⚠️  Questions answered: NOT SAVED")
            
        if hasattr(attempt, 'confidence_score') and attempt.confidence_score:
            print(f"   ✅ Confidence score: {attempt.confidence_score}%")
        else:
            print(f"   ⚠️  Confidence score: NOT SAVED")
        
        # Actual data from student_answers table
        print(f"\n📝 ACTUAL DATA (from student_answers):")
        print(f"   Questions answered: {len(answers)}")
        print(f"   Unique traits discovered: {len(traits)}")
        if traits:
            print(f"   Traits: {', '.join(sorted(traits))}")
        
        # Recommendations
        print(f"\n🎯 RECOMMENDATIONS:")
        print(f"   Count: {len(recommendations)}")
        for rec in recommendations:
            course = db.query(models.Course).filter(
                models.Course.course_id == rec.course_id
            ).first()
            print(f"   - {course.course_name if course else 'Unknown'}")
        
        # Confidence calculation explanation
        print(f"\n📊 CONFIDENCE CALCULATION EXPLAINED:")
        print(f"""
   The confidence percentage is calculated as:
   
   confidence = (gap_ratio * 0.7) + (question_factor * 0.3)
   
   Where:
   - gap_ratio = (avg score of top 5 courses - avg score of courses 6-15) / top 5 avg
     This measures how "separated" the top courses are from the rest
     
   - question_factor = min(questions_answered / min_questions, 1.0)
     This ensures at least 50% of selected questions are answered
     
   Example for 30 questions selected:
   - min_questions = 15 (50% of 30)
   - If you answered 15 questions: question_factor = 1.0
   - If you answered 10 questions: question_factor = 0.67
   
   A ~30% confidence likely means:
   - gap_ratio is small (courses not well differentiated yet)
   - OR not enough questions answered
""")
        
        # Diagnose discrepancy
        print(f"\n🔍 DISCREPANCY CHECK:")
        if len(answers) > 0:
            # Try to estimate what confidence might have been
            max_q = getattr(attempt, 'max_questions', None) or 30
            min_q = int(max_q * 0.5)
            estimated_q_factor = min(len(answers) / min_q, 1.0)
            print(f"   Assuming max_questions={max_q}, min_questions={min_q}")
            print(f"   Estimated question_factor: {estimated_q_factor:.2f}")
            print(f"   If gap_ratio was ~0 (courses evenly scored):")
            print(f"     confidence ≈ 0.0 * 0.7 + {estimated_q_factor:.2f} * 0.3 = {0.3 * estimated_q_factor:.1%}")
            print(f"   If gap_ratio was ~0.5 (moderate separation):")
            print(f"     confidence ≈ 0.5 * 0.7 + {estimated_q_factor:.2f} * 0.3 = {0.35 + 0.3 * estimated_q_factor:.1%}")
        
        print("\n" + "=" * 70)
        
    finally:
        db.close()


def list_recent_attempts(count: int = 10):
    """List recent test attempts"""
    db = SessionLocal()
    
    try:
        attempts = db.query(models.TestAttempt).order_by(
            models.TestAttempt.attempt_id.desc()
        ).limit(count).all()
        
        print(f"\n📋 LAST {count} TEST ATTEMPTS:")
        print("-" * 80)
        print(f"{'ID':<6} {'User':<8} {'Date':<20} {'MaxQ':<6} {'Shown':<6} {'Answered':<8} {'Confidence':<10}")
        print("-" * 80)
        
        for a in attempts:
            max_q = getattr(a, 'max_questions', '-') or '-'
            shown = getattr(a, 'questions_presented', '-') or '-'
            answered = getattr(a, 'questions_answered', '-') or '-'
            conf = getattr(a, 'confidence_score', '-')
            conf_str = f"{conf}%" if conf else '-'
            
            print(f"{a.attempt_id:<6} {a.user_id:<8} {str(a.taken_at)[:19]:<20} {str(max_q):<6} {str(shown):<6} {str(answered):<8} {conf_str:<10}")
        
        print("-" * 80)
        
    finally:
        db.close()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            attempt_id = int(sys.argv[1])
            analyze_attempt(attempt_id)
        except ValueError:
            if sys.argv[1] == "list":
                count = int(sys.argv[2]) if len(sys.argv) > 2 else 10
                list_recent_attempts(count)
            else:
                print("Usage:")
                print("  python check_confidence.py <attempt_id>  - Analyze specific attempt")
                print("  python check_confidence.py list [count]  - List recent attempts")
    else:
        print("Usage:")
        print("  python check_confidence.py <attempt_id>  - Analyze specific attempt")
        print("  python check_confidence.py list [count]  - List recent attempts")
        print("\nExample:")
        print("  python check_confidence.py 70")
        print("  python check_confidence.py 71")
        print("  python check_confidence.py list 20")
