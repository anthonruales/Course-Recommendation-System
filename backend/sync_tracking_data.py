"""
Sync Script: Update user_test_attempts with tracking data from test_attempts

This syncs max_questions, confidence_score, and traits_found from test_attempts
to user_test_attempts for existing records.
"""

from database import engine
from sqlalchemy import text

def sync_tracking_data():
    """Update user_test_attempts with tracking data from test_attempts"""
    
    with engine.connect() as conn:
        print("[1] Finding attempts that need syncing...")
        
        # Find attempts where test_attempts has data but user_test_attempts doesn't
        result = conn.execute(text("""
            SELECT 
                ta.attempt_id,
                ta.max_questions,
                ta.questions_presented,
                ta.questions_answered,
                ta.confidence_score,
                uta.max_questions as uta_max_q,
                uta.confidence_score as uta_conf
            FROM test_attempts ta
            JOIN user_test_attempts uta ON ta.attempt_id = uta.attempt_id
            WHERE ta.max_questions IS NOT NULL 
              AND (uta.max_questions IS NULL OR uta.confidence_score IS NULL)
        """))
        
        rows = result.fetchall()
        print(f"[2] Found {len(rows)} attempts to update")
        
        for row in rows:
            attempt_id, max_q, presented, answered, conf, uta_max, uta_conf = row
            print(f"    Updating attempt {attempt_id}: max_q={max_q}, conf={conf}")
            
            conn.execute(text("""
                UPDATE user_test_attempts 
                SET max_questions = :max_questions,
                    confidence_score = :confidence_score
                WHERE attempt_id = :attempt_id
            """), {
                'attempt_id': attempt_id,
                'max_questions': max_q,
                'confidence_score': conf
            })
        
        conn.commit()
        print(f"\n[OK] Updated {len(rows)} records")
        
        # Also count traits from student_answers for each attempt
        print("\n[3] Counting traits from student_answers...")
        
        result = conn.execute(text("""
            SELECT uta.attempt_id
            FROM user_test_attempts uta
            WHERE uta.traits_found IS NULL
        """))
        
        attempts_needing_traits = result.fetchall()
        print(f"    Found {len(attempts_needing_traits)} attempts needing trait counts")
        
        for (attempt_id,) in attempts_needing_traits:
            # Count unique traits for this attempt
            trait_result = conn.execute(text("""
                SELECT COUNT(DISTINCT o.trait_tag)
                FROM student_answers sa
                JOIN options o ON sa.chosen_option_id = o.option_id
                WHERE sa.attempt_id = :attempt_id
                  AND o.trait_tag IS NOT NULL
            """), {'attempt_id': attempt_id})
            
            trait_count = trait_result.fetchone()[0]
            
            conn.execute(text("""
                UPDATE user_test_attempts 
                SET traits_found = :traits_found
                WHERE attempt_id = :attempt_id
            """), {
                'attempt_id': attempt_id,
                'traits_found': trait_count
            })
        
        conn.commit()
        print(f"[OK] Updated trait counts for {len(attempts_needing_traits)} records")
        
        # Verify
        print("\n[4] Verification - Recent attempts:")
        result = conn.execute(text("""
            SELECT attempt_id, user_id, total_questions, max_questions, confidence_score, traits_found
            FROM user_test_attempts 
            ORDER BY attempt_id DESC
            LIMIT 10
        """))
        
        print("-" * 90)
        print(f"{'ID':<8} {'User':<8} {'Answered':<10} {'MaxQ':<8} {'Confidence':<12} {'Traits':<8}")
        print("-" * 90)
        for row in result.fetchall():
            attempt_id, user_id, total_q, max_q, conf, traits = row
            conf_str = f"{conf:.1f}%" if conf else "-"
            print(f"{attempt_id:<8} {user_id:<8} {total_q or '-':<10} {max_q or '-':<8} {conf_str:<12} {traits or '-':<8}")


if __name__ == "__main__":
    print("=" * 60)
    print("SYNC: Update user_test_attempts with tracking data")
    print("=" * 60)
    sync_tracking_data()
