"""
Demo Data Seeder for CoursePro
Run this script to create demo accounts for testing/demonstration purposes.

Usage: python seed_demo_data.py
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from database import SessionLocal, engine
import models
from security import hash_password
from datetime import datetime, timedelta
import random
import json

# Demo Users - Realistic Filipino SHS Students
DEMO_USERS = [
    {
        "username": "maria_santos",
        "first_name": "Maria",
        "last_name": "Santos",
        "email": "maria.santos@demo.com",
        "password": "demo123",
        "academic_info": {
            "gwa": 92.5,
            "strand": "STEM",
            "age": 18,
            "gender": "Female",
            "interests": "Science, Technology, Research",
            "skills": "Problem Solving, Critical Thinking, Programming"
        }
    },
    {
        "username": "juan_reyes",
        "first_name": "Juan",
        "last_name": "Reyes",
        "email": "juan.reyes@demo.com",
        "password": "demo123",
        "academic_info": {
            "gwa": 88.0,
            "strand": "ABM",
            "age": 17,
            "gender": "Male",
            "interests": "Business, Marketing, Finance",
            "skills": "Leadership, Communication, Analytical"
        }
    },
    {
        "username": "ana_cruz",
        "first_name": "Ana",
        "last_name": "Cruz",
        "email": "ana.cruz@demo.com",
        "password": "demo123",
        "academic_info": {
            "gwa": 95.0,
            "strand": "HUMSS",
            "age": 18,
            "gender": "Female",
            "interests": "Psychology, Social Sciences, Writing",
            "skills": "Empathy, Communication, Critical Analysis"
        }
    },
    {
        "username": "miguel_garcia",
        "first_name": "Miguel",
        "last_name": "Garcia",
        "email": "miguel.garcia@demo.com",
        "password": "demo123",
        "academic_info": {
            "gwa": 85.5,
            "strand": "TVL-ICT",
            "age": 17,
            "gender": "Male",
            "interests": "Computers, Gaming, Web Development",
            "skills": "Programming, Troubleshooting, Design"
        }
    },
    {
        "username": "sofia_mendoza",
        "first_name": "Sofia",
        "last_name": "Mendoza",
        "email": "sofia.mendoza@demo.com",
        "password": "demo123",
        "academic_info": {
            "gwa": 90.0,
            "strand": "GAS",
            "age": 18,
            "gender": "Female",
            "interests": "Arts, Education, Community Service",
            "skills": "Teaching, Creativity, Organization"
        }
    }
]

# Admin Account
ADMIN_USER = {
    "username": "admin",
    "first_name": "Admin",
    "last_name": "User",
    "email": "admin@coursepro.com",
    "password": "admin123",
    "academic_info": None
}


def seed_demo_users():
    """Seed demo user accounts"""
    db = SessionLocal()
    created_count = 0
    
    try:
        print("\n" + "="*60)
        print("       COURSEPRO DEMO DATA SEEDER")
        print("="*60)
        
        # Create demo users
        print("\n[USERS] Creating demo student accounts...")
        for user_data in DEMO_USERS:
            # Check if user already exists
            existing = db.query(models.User).filter(
                (models.User.email == user_data["email"]) | 
                (models.User.username == user_data["username"])
            ).first()
            
            if existing:
                print(f"  [SKIP] {user_data['username']} already exists")
                continue
            
            user = models.User(
                username=user_data["username"],
                first_name=user_data["first_name"],
                last_name=user_data["last_name"],
                email=user_data["email"],
                password_hash=hash_password(user_data["password"]),
                academic_info=user_data["academic_info"],
                created_at=datetime.now() - timedelta(days=random.randint(1, 30))
            )
            db.add(user)
            created_count += 1
            print(f"  [OK] Created: {user_data['first_name']} {user_data['last_name']} ({user_data['email']})")
        
        # Create admin user
        print("\n[ADMIN] Creating admin account...")
        existing_admin = db.query(models.User).filter(
            models.User.email == ADMIN_USER["email"]
        ).first()
        
        if existing_admin:
            print(f"  [SKIP] Admin account already exists")
        else:
            admin = models.User(
                username=ADMIN_USER["username"],
                first_name=ADMIN_USER["first_name"],
                last_name=ADMIN_USER["last_name"],
                email=ADMIN_USER["email"],
                password_hash=hash_password(ADMIN_USER["password"]),
                academic_info=ADMIN_USER["academic_info"],
                created_at=datetime.now()
            )
            db.add(admin)
            created_count += 1
            print(f"  [OK] Created admin account")
        
        db.commit()
        
        print("\n" + "="*60)
        print(f"  SEEDING COMPLETE: {created_count} accounts created")
        print("="*60)
        
        print("\n[DEMO CREDENTIALS]")
        print("-"*40)
        print("Student Accounts (password: demo123):")
        for user in DEMO_USERS:
            print(f"  - {user['email']}")
        print("\nAdmin Account (password: admin123):")
        print(f"  - {ADMIN_USER['email']}")
        print("-"*40)
        
    except Exception as e:
        print(f"[ERROR] Failed to seed demo data: {e}")
        db.rollback()
        raise
    finally:
        db.close()


def seed_demo_assessments():
    """Seed some demo assessment history for demo users"""
    db = SessionLocal()
    
    try:
        print("\n[ASSESSMENTS] Creating demo assessment history...")
        
        # Get demo users who have academic info
        demo_emails = [u["email"] for u in DEMO_USERS]
        users = db.query(models.User).filter(models.User.email.in_(demo_emails)).all()
        
        # Get the default test
        test = db.query(models.Test).first()
        if not test:
            print("  [SKIP] No test found - run main server first to seed courses/questions")
            return
        
        # Get some courses
        courses = db.query(models.Course).limit(10).all()
        if not courses:
            print("  [SKIP] No courses found - run main server first to seed courses")
            return
        
        assessment_count = 0
        for user in users[:3]:  # Only create for first 3 demo users
            # Check if user already has assessments
            existing = db.query(models.TestAttempt).filter(
                models.TestAttempt.user_id == user.user_id
            ).first()
            
            if existing:
                print(f"  [SKIP] {user.fullname} already has assessment history")
                continue
            
            # Create a test attempt
            attempt = models.TestAttempt(
                user_id=user.user_id,
                test_id=test.test_id,
                taken_at=datetime.now() - timedelta(days=random.randint(1, 14)),
                max_questions=30,
                questions_presented=30,
                questions_answered=30,
                confidence_score=random.uniform(75, 95),
                user_gwa=user.academic_info.get("gwa") if user.academic_info else None,
                user_strand=user.academic_info.get("strand") if user.academic_info else None
            )
            db.add(attempt)
            db.flush()
            
            # Create recommendations
            sample_courses = random.sample(courses, min(5, len(courses)))
            for i, course in enumerate(sample_courses):
                rec = models.Recommendation(
                    attempt_id=attempt.attempt_id,
                    user_id=user.user_id,
                    course_id=course.course_id,
                    score=random.uniform(70, 98) - (i * 5),  # Decreasing scores
                    reasoning=f"Based on your {user.academic_info.get('strand', 'academic')} background and interests in {user.academic_info.get('interests', 'various fields')}."
                )
                db.add(rec)
            
            assessment_count += 1
            print(f"  [OK] Created assessment for {user.fullname}")
        
        db.commit()
        print(f"\n  Created {assessment_count} demo assessments")
        
    except Exception as e:
        print(f"[ERROR] Failed to seed assessments: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    print("\nInitializing database connection...")
    models.Base.metadata.create_all(bind=engine)
    
    seed_demo_users()
    seed_demo_assessments()
    
    print("\n[DONE] Demo data seeding complete!")
    print("You can now log in with the demo accounts listed above.\n")
