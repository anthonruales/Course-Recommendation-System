#!/usr/bin/env python3
"""
Cleanup script to remove all test user accounts from the database
"""

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker

# Import models
from models import User, TestAttempt, StudentAnswer, Recommendation

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    DATABASE_URL = "sqlite:///./coursepro.db"

# Create engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def cleanup_test_users():
    """Delete all test user accounts"""
    db = SessionLocal()
    
    try:
        # Define patterns for test accounts
        test_patterns = [
            'testadapt',  # Any email starting with testadapt
            'test_adaptive',
            'realtest',
        ]
        
        # Also look for test user names
        test_names = [
            'Test',
            'Test User Adaptive',
            'Real Test',
        ]
        
        # Query users matching test patterns
        test_users = db.query(User).filter(
            or_(
                User.email.ilike('%testadapt%'),
                User.email.ilike('%test_adaptive%'),
                User.email.ilike('%realtest%'),
            )
        ).all()
        
        if not test_users:
            print("✅ No test users found.")
            return
        
        print(f"🗑️ Found {len(test_users)} test user(s) to delete:")
        
        for user in test_users:
            print(f"  - {user.fullname} ({user.email}) [ID: {user.user_id}]")
            
            # Delete related data
            # Delete recommendations
            db.query(Recommendation).filter(Recommendation.user_id == user.user_id).delete()
            
            # Delete student answers and test attempts
            attempts = db.query(TestAttempt).filter(TestAttempt.user_id == user.user_id).all()
            for attempt in attempts:
                db.query(StudentAnswer).filter(StudentAnswer.attempt_id == attempt.attempt_id).delete()
            
            db.query(TestAttempt).filter(TestAttempt.user_id == user.user_id).delete()
            
            # Delete user
            db.delete(user)
        
        db.commit()
        print(f"\n✅ Successfully deleted {len(test_users)} test user(s)!")
        
    except Exception as e:
        db.rollback()
        print(f"❌ Error deleting test users: {e}")
        raise
    
    finally:
        db.close()

if __name__ == "__main__":
    print("=" * 60)
    print("🧹 Cleaning up test user accounts...")
    print("=" * 60)
    cleanup_test_users()
    print("=" * 60)
