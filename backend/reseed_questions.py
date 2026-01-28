"""
Reseed Questions Script - Clears old questions and reloads enhanced questions
This is needed when you've updated questions_enhanced.py with new content
"""

from database import SessionLocal
import models
from questions_enhanced import QUESTIONS_POOL_ENHANCED
import json

def reseed_questions():
    db = SessionLocal()
    try:
        print("🔄 Starting question reseed process...")
        
        # Check existing questions
        existing_questions = db.query(models.Question).count()
        print(f"📊 Current questions in database: {existing_questions}")
        
        # Get the default test (or create if needed)
        default_test = db.query(models.Test).filter(
            models.Test.test_name == "Career Assessment"
        ).first()
        
        if not default_test:
            print("❌ No default test found. Creating one...")
            default_test = models.Test(
                test_name="Career Assessment",
                test_type="assessment",
                description="Comprehensive career interest and aptitude assessment to recommend college courses"
            )
            db.add(default_test)
            db.flush()
        
        print(f"✓ Using test ID: {default_test.test_id}")
        
        # Clear old questions, options, and related data
        print("🗑️ Deleting old questions, options, and answers...")
        db.query(models.StudentAnswer).delete()
        db.query(models.Option).delete()
        db.query(models.Question).delete()
        db.commit()
        print("✓ Cleared old data")
        
        # Seed enhanced questions
        print(f"🌱 Adding {len(QUESTIONS_POOL_ENHANCED)} enhanced questions...")
        for q in QUESTIONS_POOL_ENHANCED:
            question_type = q.get("question_type", "standard")
            question_text = q.get("question_text") or q.get("question")
            
            new_q = models.Question(
                test_id=default_test.test_id,
                question_text=question_text,
                category=q.get("category"),
                question_type=question_type
            )
            db.add(new_q)
            db.flush()
            
            # Add options
            options_list = q.get("options", [])
            if options_list:
                for opt in options_list:
                    trait_tags_json = None
                    recommended_courses_json = None
                    weight = opt.get("weight", 1)
                    
                    if question_type in ["career_path", "extracurricular", "situational_mapped"]:
                        trait_tags_json = json.dumps(opt.get("trait_tags", []))
                        recommended_courses_json = json.dumps(opt.get("recommended_courses", []))
                    
                    option_text = opt.get("option_text") or opt.get("text")
                    trait_tag = opt.get("trait_tag") or opt.get("tag")
                    
                    db.add(models.Option(
                        question_id=new_q.question_id,
                        option_text=option_text,
                        trait_tag=trait_tag,
                        weight=weight,
                        trait_tags_json=trait_tags_json,
                        recommended_courses_json=recommended_courses_json
                    ))
        
        db.commit()
        
        # Verify
        final_count = db.query(models.Question).count()
        final_options = db.query(models.Option).count()
        print(f"\n✅ RESEED COMPLETE!")
        print(f"📊 Questions in database: {final_count}")
        print(f"📊 Options in database: {final_options}")
        
    except Exception as e:
        print(f"❌ ERROR: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    reseed_questions()
