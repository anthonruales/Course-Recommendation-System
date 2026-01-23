import os
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from dotenv import load_dotenv
import models, database
from security import hash_password, verify_password

# Import enhanced questions if available, fall back to seed_data
try:
    from questions_enhanced import QUESTIONS_POOL_ENHANCED as QUESTIONS_POOL
    print("✓ Using enhanced questions (8-10 options per question)")
except ImportError:
    from seed_data import QUESTIONS_POOL
    print("! Using standard questions from seed_data")

from seed_data import (
    COURSES_POOL, ASSESSMENT_TIERS, COURSE_DIRECT_MAPPING, SCALE_WEIGHTS,
    LEARNING_STYLE_MAPPING, WORK_ENVIRONMENT_MAPPING, COURSE_EMPLOYABILITY, 
    COURSE_PUBLIC_AVAILABILITY, COURSE_SKILL_REQUIREMENTS, CAREER_GOAL_MAPPING,
    PERSONALITY_COMPATIBILITY
)
from sqlalchemy import func
from sqlalchemy.orm import Session, joinedload
from trait_mapping import apply_trait_mapping
from assessment_service import AssessmentService
from recommendation_engine import HybridRecommendationEngine
from adaptive_assessment import AdaptiveAssessmentEngine, initialize_adaptive_engine, get_adaptive_engine
import json

load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🛠️ Synchronizing database schema...")
    models.Base.metadata.create_all(bind=database.engine)
    seed_database()
    yield

app = FastAPI(lifespan=lifespan)
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

def seed_database():
    db = database.SessionLocal()
    try:
        print("🧹 Cleaning out old data...")
        db.query(models.Recommendation).delete()
        db.query(models.StudentAnswer).delete()
        db.query(models.TestAttempt).delete()
        db.query(models.Option).delete()
        db.query(models.Question).delete()
        db.query(models.Test).delete()
        db.query(models.Course).delete()
        db.commit()

        # Create default test
        default_test = models.Test(
            test_name="Career Assessment",
            test_type="assessment",
            description="Comprehensive career interest and aptitude assessment to recommend college courses"
        )
        db.add(default_test)
        db.flush()
        print(f"🌱 Created default test with ID: {default_test.test_id}")

        if COURSES_POOL:
            print(f"🌱 Seeding {len(COURSES_POOL)} courses...")
            for c in COURSES_POOL:
                tags = c.get("trait_tag", [])
                tag_str = ", ".join(tags) if isinstance(tags, list) else str(tags)
                db.add(models.Course(
                    course_name=c.get("course_name"), 
                    description=c.get("description"), 
                    minimum_gwa=c.get("minimum_gwa"), 
                    required_strand=c.get("recommended_strand"),  # Map from recommended_strand to required_strand
                    trait_tag=tag_str
                ))

        if QUESTIONS_POOL:
            print(f"🌱 Seeding {len(QUESTIONS_POOL)} questions...")
            for q in QUESTIONS_POOL:
                question_type = q.get("question_type", "standard")
                # Support both old format ("question") and new format ("question_text")
                question_text = q.get("question_text") or q.get("question")
                new_q = models.Question(
                    test_id=default_test.test_id,
                    question_text=question_text, 
                    category=q.get("category"),
                    question_type=question_type
                )
                db.add(new_q)
                db.flush()
                options_list = q.get("options", [])
                if options_list:
                    for opt in options_list:
                        # Handle different question types
                        trait_tags_json = None
                        recommended_courses_json = None
                        weight = opt.get("weight", 1)
                        
                        # For career_path, extracurricular, and situational_mapped questions
                        if question_type in ["career_path", "extracurricular", "situational_mapped"]:
                            trait_tags_json = json.dumps(opt.get("trait_tags", []))
                            recommended_courses_json = json.dumps(opt.get("recommended_courses", []))
                        
                        # Support both old format ("text"/"tag") and new format ("option_text"/"trait_tag")
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
                else:
                    db.add(models.Option(question_id=new_q.question_id, option_text="Yes", trait_tag=q.get("tag")))
                    db.add(models.Option(question_id=new_q.question_id, option_text="No", trait_tag="None"))
        db.commit()
        print("✅ DATABASE SUCCESSFULLY REBUILT AND SEEDED!")
    except Exception as e:
        print(f"❌ DATABASE ERROR: {e}"); db.rollback()
    finally:
        db.close()

def get_db():
    db = database.SessionLocal()
    try: yield db
    finally: db.close()

class UserCreate(BaseModel): 
    username: str
    fullname: str
    email: str
    password: str

class UserLogin(BaseModel): 
    username: str
    password: str
class AssessmentAnswer(BaseModel):
    questionId: int
    chosenOptionId: int

class AssessmentSubmit(BaseModel):
    userId: int
    answers: List[AssessmentAnswer]
class OptionSchema(BaseModel):
    option_id: int; option_text: str; trait_tag: Optional[str]
    class Config: from_attributes = True
class QuestionSchema(BaseModel):
    question_id: int
    question_text: str
    category: str
    options: List[OptionSchema]

    class Config:
        from_attributes = True


class AcademicInfoUpdate(BaseModel):
    gwa: float
    strand: str
    fullname: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    interests: Optional[str] = None
    skills: Optional[str] = None

class CourseCreate(BaseModel):
    course_name: str
    description: str
    trait_tag: str
    required_strand: Optional[str] = None
    minimum_gwa: Optional[float] = None

class CourseUpdate(BaseModel):
    course_name: Optional[str] = None
    description: Optional[str] = None
    trait_tag: Optional[str] = None
    required_strand: Optional[str] = None
    minimum_gwa: Optional[float] = None

class QuestionCreate(BaseModel):
    question_text: str
    category: str
    options: List[dict]  # [{text: str, trait_tag: str}]

class QuestionUpdate(BaseModel):
    question_text: Optional[str] = None
    category: Optional[str] = None

class OptionCreate(BaseModel):
    option_text: str
    trait_tag: str

class OptionUpdate(BaseModel):
    option_text: Optional[str] = None
    trait_tag: Optional[str] = None


# ========== FEEDBACK SYSTEM SCHEMAS ==========
class FeedbackSubmit(BaseModel):
    recommendation_id: Optional[int] = None  # Optional for overall feedback
    rating: int  # 1-5 stars
    feedback_text: Optional[str] = None


class FeedbackResponse(BaseModel):
    feedback_id: int
    recommendation_id: int
    user_id: int
    rating: int
    feedback_text: Optional[str]
    created_at: str
    
    class Config:
        from_attributes = True


class FeedbackStats(BaseModel):
    recommendation_id: int
    course_name: str
    avg_rating: float
    total_feedbacks: int
    feedback_breakdown: dict  # {1: count, 2: count, ...}


@app.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    # Check for duplicate username
    if db.query(models.User).filter(models.User.username == user.username).first():
        raise HTTPException(status_code=400, detail="Username already exists")
    
    # Check for duplicate email
    if db.query(models.User).filter(models.User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already exists")
    
    # Parse fullname into first_name and last_name
    name_parts = user.fullname.strip().split(" ", 1)
    first_name = name_parts[0] if name_parts else user.fullname
    last_name = name_parts[1] if len(name_parts) > 1 else ""
    
    new_user = models.User(
        username=user.username,
        first_name=first_name,
        last_name=last_name,
        email=user.email,
        password_hash=hash_password(user.password)
    )
    db.add(new_user)
    db.commit()
    return {"message": "Success"}

@app.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if not db_user or not verify_password(user.password, db_user.password_hash):
        raise HTTPException(status_code=400, detail="Invalid username or password")
    return {"user": db_user.fullname, "user_id": db_user.user_id}

@app.post("/google-login")
def google_login(user: dict, db: Session = Depends(get_db)):
    """Handle Google OAuth login - returns existing user or indicates new user needs username"""
    email = user.get("email")
    name = user.get("name", "")
    
    if not email:
        raise HTTPException(status_code=400, detail="Email is required")
    
    # Check if user exists
    db_user = db.query(models.User).filter(models.User.email == email).first()
    
    if db_user:
        # User exists, return their info
        return {"user": db_user.fullname, "user_id": db_user.user_id, "needs_username": False}
    else:
        # New user - they need to choose a username
        return {
            "needs_username": True,
            "email": email,
            "name": name
        }


@app.post("/google-register")
def google_register(user: dict, db: Session = Depends(get_db)):
    """Complete Google registration with chosen username"""
    email = user.get("email")
    name = user.get("name", "")
    username = user.get("username")
    
    if not email:
        raise HTTPException(status_code=400, detail="Email is required")
    if not username:
        raise HTTPException(status_code=400, detail="Username is required")
    
    # Check if username is taken
    if db.query(models.User).filter(models.User.username == username).first():
        raise HTTPException(status_code=400, detail="Username already taken")
    
    # Check if email already exists
    if db.query(models.User).filter(models.User.email == email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Create new user with chosen username
    name_parts = name.strip().split(" ", 1)
    first_name = name_parts[0] if name_parts else name
    last_name = name_parts[1] if len(name_parts) > 1 else ""
    
    new_user = models.User(
        username=username,
        first_name=first_name,
        last_name=last_name,
        email=email,
        password_hash=hash_password(f"google_oauth_{email}")  # Dummy password for Google users
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"user": new_user.fullname, "user_id": new_user.user_id}


@app.get("/user/{user_id}/academic-info")
def get_academic_info(user_id: int, db: Session = Depends(get_db)):
    """Get user's academic info including GWA, Strand, and personal info"""
    user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return {
        "user_id": user_id,
        "fullname": user.fullname,
        "academic_info": user.academic_info,
        "has_academic_info": user.academic_info is not None and user.academic_info.get("gwa") is not None and user.academic_info.get("strand") is not None
    }

@app.put("/user/{user_id}/academic-info")
def update_academic_info(user_id: int, info: AcademicInfoUpdate, db: Session = Depends(get_db)):
    """Update user's academic info (GWA, Strand, and personal info) for recommendation accuracy"""
    user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Update fullname if provided (parse into first_name and last_name)
    if info.fullname:
        name_parts = info.fullname.strip().split(" ", 1)
        user.first_name = name_parts[0] if name_parts else info.fullname
        user.last_name = name_parts[1] if len(name_parts) > 1 else ""
    
    # Update academic_info JSON with all fields (D4 - Personal & Academic Database)
    user.academic_info = {
        "gwa": info.gwa,
        "strand": info.strand,
        "age": info.age,
        "gender": info.gender,
        "interests": info.interests,
        "skills": info.skills
    }
    db.commit()
    return {
        "message": "Profile updated successfully",
        "user_id": user_id,
        "fullname": user.fullname,
        "academic_info": user.academic_info
    }

# Initialize the Hybrid Recommendation Engine (Rule-Based + Decision Tree)
recommendation_engine = HybridRecommendationEngine()

@app.post("/recommend")
def recommend(data: AssessmentSubmit, db: Session = Depends(get_db)):
    """
    ================================================================================
    COURSE RECOMMENDATION SYSTEM - THESIS IMPLEMENTATION
    ================================================================================
    
    This endpoint implements the hybrid recommendation system as described in the thesis:
    
    DFD Process 5-7: Take a Test → Rule Based-Logic → Decision Tree
    
    PHASE 1: RULE-BASED FILTERING (Giarratano & Riley, 2005)
    -------------------------------------------------------
    - Uses explicit IF-THEN rules to filter courses
    - Applies eligibility rules (GWA requirements, strand alignment)
    - Applies preference rules (trait matching, career path preferences)
    - Applies penalty rules (mismatches and shortfalls)
    
    PHASE 2: DECISION TREE CLASSIFICATION (Quinlan, 1986)
    ----------------------------------------------------
    - Classifies user into a career category using hierarchical decisions
    - Ranks courses based on decision tree path
    - Provides confidence scores for predictions
    
    HYBRID APPROACH (Burke, 2002)
    ----------------------------
    - Combines scores from both phases
    - Provides transparent, explainable recommendations
    
    ================================================================================
    """
    print("=" * 80)
    print("🎓 COURSE RECOMMENDATION SYSTEM - THESIS IMPLEMENTATION")
    print("=" * 80)
    print(f"📝 Processing recommendation for user {data.userId} with {len(data.answers)} answers")
    
    # ==================== STEP 1: FETCH USER DATA ====================
    # D4 - Personal & Academic Database
    user = db.query(models.User).filter(models.User.user_id == data.userId).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    user_gwa = None
    user_strand = None
    user_interests = None
    user_skills = None
    if user.academic_info:
        user_gwa = user.academic_info.get("gwa")
        user_strand = user.academic_info.get("strand")
        user_interests = user.academic_info.get("interests", "")
        user_skills = user.academic_info.get("skills", "")
    
    print(f"👤 User Profile: GWA={user_gwa}, Strand={user_strand}")
    print(f"📝 Qualitative: Interests='{user_interests}', Skills='{user_skills}'")
    
    # ==================== STEP 2: CREATE TEST ATTEMPT ====================
    # D5 - Test Attempt Database
    default_test = db.query(models.Test).filter(models.Test.test_type == "assessment").first()
    if not default_test:
        raise HTTPException(status_code=500, detail="No assessment test found in system")
    
    test_attempt = models.TestAttempt(
        user_id=data.userId,
        test_id=default_test.test_id
    )
    db.add(test_attempt)
    db.flush()
    print(f"📋 Created test attempt ID: {test_attempt.attempt_id}")
    
    # ==================== STEP 3: PROCESS ASSESSMENT ANSWERS ====================
    # Extract traits from user's answers
    trait_scores = {}
    career_path_courses = []  # Direct course preferences from career path questions
    
    for ans in data.answers:
        option = db.query(models.Option).filter(
            models.Option.option_id == ans.chosenOptionId
        ).first()
        
        if option:
            question = db.query(models.Question).filter(
                models.Question.question_id == ans.questionId
            ).first()
            
            # Save student answer
            db.add(models.StudentAnswer(
                attempt_id=test_attempt.attempt_id,
                question_id=ans.questionId,
                chosen_option_id=ans.chosenOptionId
            ))
            
            question_type = question.question_type if question else "standard"
            
            # === SCALE QUESTIONS: Apply weighted scoring ===
            if question_type == "scale" and option.weight:
                weight = option.weight
                scale_config = SCALE_WEIGHTS.get(weight, {"multiplier": 1.0})
                multiplier = scale_config["multiplier"]
                
                if option.trait_tag and str(option.trait_tag).strip().lower() not in ["none", ""]:
                    tag = option.trait_tag.strip()
                    trait_scores[tag] = trait_scores.get(tag, 0) + (1 * multiplier)
            
            # === CAREER PATH / EXTRACURRICULAR / SITUATIONAL QUESTIONS ===
            elif question_type in ["career_path", "extracurricular", "situational_mapped"]:
                # Process multiple trait tags
                if option.trait_tags_json:
                    try:
                        trait_tags = json.loads(option.trait_tags_json)
                        for tag in trait_tags:
                            trait_scores[tag] = trait_scores.get(tag, 0) + 1.5
                    except json.JSONDecodeError:
                        pass
                
                # Collect direct course recommendations
                if option.recommended_courses_json:
                    try:
                        recommended = json.loads(option.recommended_courses_json)
                        career_path_courses.extend(recommended)
                    except json.JSONDecodeError:
                        pass
                
                # Process primary trait tag
                if option.trait_tag and str(option.trait_tag).strip().lower() not in ["none", ""]:
                    tag = option.trait_tag.strip()
                    trait_scores[tag] = trait_scores.get(tag, 0) + 2
                    
                    # Check direct mapping
                    if tag in COURSE_DIRECT_MAPPING:
                        mapping = COURSE_DIRECT_MAPPING[tag]
                        career_path_courses.extend(mapping.get("courses", []))
            
            # === STANDARD QUESTIONS ===
            else:
                if option.trait_tag and str(option.trait_tag).strip().lower() not in ["none", ""]:
                    tag = option.trait_tag.strip()
                    trait_scores[tag] = trait_scores.get(tag, 0) + 1
    
    print(f"📊 Extracted {len(trait_scores)} unique traits from assessment")
    print(f"📊 Career path preferences: {len(set(career_path_courses))} courses")
    
    if not trait_scores:
        db.rollback()
        raise HTTPException(
            status_code=400, 
            detail=f"Unable to generate recommendations. No personality traits were identified from your answers."
        )
    
    # Sort traits by score
    sorted_traits = sorted(trait_scores.items(), key=lambda x: x[1], reverse=True)
    top_traits = sorted_traits[:7]
    primary_trait = sorted_traits[0][0] if sorted_traits else None
    
    print(f"🎯 Primary Trait: {primary_trait}")
    print(f"🌈 Top 7 Traits: {[t[0] for t in top_traits]}")
    
    # ==================== STEP 4: FETCH ALL COURSES ====================
    all_courses = db.query(models.Course).all()
    print(f"📚 Total courses in database: {len(all_courses)}")
    
    # ==================== STEP 5: RUN HYBRID RECOMMENDATION ENGINE ====================
    # This implements PHASE 1 (Rule-Based Filtering) + PHASE 2 (Decision Tree Classification)
    
    user_profile = {
        "gwa": user_gwa,
        "strand": user_strand,
        "interests": user_interests or "",
        "skills": user_skills or ""
    }
    
    result = recommendation_engine.generate_recommendations(
        courses=all_courses,
        user_profile=user_profile,
        trait_scores=trait_scores,
        career_path_courses=list(set(career_path_courses)),
        top_n=5
    )
    
    recommendations = result["recommendations"]
    algorithm_details = result["algorithm_details"]
    user_analysis = result["user_analysis"]
    
    # ==================== STEP 6: SAVE RECOMMENDATIONS TO DATABASE ====================
    # D7 - Course Recommendation Database
    try:
        for rec in recommendations:
            course = db.query(models.Course).filter(
                models.Course.course_name == rec["course_name"]
            ).first()
            
            if course:
                db.add(models.Recommendation(
                    attempt_id=test_attempt.attempt_id,
                    user_id=data.userId,
                    course_id=course.course_id,
                    reasoning=rec["reasoning"]
                ))
        
        db.commit()
        print(f"✅ Saved {len(recommendations)} recommendations to database")
    except Exception as e:
        print(f"❌ Error saving recommendations: {e}")
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error saving recommendations: {str(e)}")
    
    # ==================== STEP 7: GENERATE RESPONSE ====================
    # Calculate algorithm metrics
    avg_confidence = sum(r["confidence_score"] for r in recommendations) / len(recommendations) if recommendations else 0
    priority_breakdown = {
        "excellent": len([r for r in recommendations if r["priority_tier"] == "EXCELLENT"]),
        "good": len([r for r in recommendations if r["priority_tier"] == "GOOD"]),
        "fair": len([r for r in recommendations if r["priority_tier"] == "FAIR"]),
        "exploratory": len([r for r in recommendations if r["priority_tier"] == "EXPLORATORY"])
    }
    
    print("=" * 80)
    print("✅ RECOMMENDATION COMPLETE")
    print(f"   → {len(recommendations)} recommendations generated")
    print(f"   → Average confidence: {avg_confidence:.1f}%")
    print(f"   → Phase 1 filtered: {algorithm_details['phase1_rule_based']['eligible_courses']} eligible courses")
    print(f"   → Phase 2 classification: {algorithm_details['phase2_decision_tree']['classification']}")
    print("=" * 80)
    
    return {
        "user_id": data.userId,
        "user_gwa": user_gwa,
        "user_strand": user_strand,
        "detected_traits": list(top_traits),
        "trait_analysis": {
            "primary_trait": primary_trait,
            "top_traits": user_analysis["top_traits"],
            "predicted_career_category": user_analysis["predicted_career_category"],
            "work_environments": user_analysis["work_environments"],
            "total_traits_detected": len(trait_scores)
        },
        "recommendations": recommendations,
        "algorithm_metrics": {
            "average_confidence": round(avg_confidence, 1),
            "priority_distribution": priority_breakdown,
            "total_courses_analyzed": len(all_courses),
            "matching_algorithm_version": "3.0-RuleBased-DecisionTree"
        },
        "algorithm_details": {
            "phase1_rule_based": {
                "description": "Rule-Based Filtering using IF-THEN logic (Giarratano & Riley, 2005)",
                "rules_applied": algorithm_details["phase1_rule_based"]["rules_applied"],
                "eligible_courses": algorithm_details["phase1_rule_based"]["eligible_courses"],
                "ineligible_courses": algorithm_details["phase1_rule_based"]["ineligible_courses"]
            },
            "phase2_decision_tree": {
                "description": "Decision Tree Classification (Quinlan, 1986)",
                "classification": algorithm_details["phase2_decision_tree"]["classification"],
                "confidence": algorithm_details["phase2_decision_tree"]["confidence"],
                "decision_path": algorithm_details["phase2_decision_tree"]["decision_path"]
            }
        }
    }

@app.get("/questions", response_model=List[QuestionSchema])
def get_questions(db: Session = Depends(get_db)):
    # Using func.random() (for SQLite/Postgres) or func.rand() (for MySQL) 
    # to pull 20 random questions from the database
    questions = db.query(models.Question)\
        .options(joinedload(models.Question.options))\
        .order_by(func.random())\
        .limit(20)\
        .all()
    
    if not questions:
        raise HTTPException(status_code=404, detail="No questions found")
        
    return questions

# ==================== ASSESSMENT TIER ENDPOINTS ====================

@app.get("/assessment/tiers")
def get_assessment_tiers():
    """Get all available assessment tiers with their details"""
    try:
        tiers = AssessmentService.get_available_tiers()
        return {
            "success": True,
            "message": "Assessment tiers retrieved successfully",
            "tiers": tiers,
            "total_tiers": len(tiers)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/assessment/strands")
def get_available_strands():
    """Get all available SHS strands with their focus areas"""
    try:
        from assessment_service import STRAND_TRAIT_MAPPING
        strands = {
            strand: {
                "name": info["name"],
                "focus_areas": info["priority_traits"][:5]
            }
            for strand, info in STRAND_TRAIT_MAPPING.items()
        }
        return {
            "success": True,
            "strands": strands
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/assessment/start/{tier}")
def start_assessment(tier: str, strand: str = None, db: Session = Depends(get_db)):
    """
    Start an assessment with a specific tier and fetch questions from database.
    Questions are prioritized based on user's SHS strand.
    
    Args:
        tier: Assessment tier (quick, standard, comprehensive)
        strand: User's SHS strand (STEM, ABM, HUMSS, TVL, GAS, SPORTS, ARTS)
    """
    try:
        # Validate tier
        tier_config = AssessmentService.get_available_tiers()
        if tier not in tier_config:
            raise ValueError(f"Invalid tier. Must be one of: {list(tier_config.keys())}")
        
        question_count = tier_config[tier]["question_count"]
        
        # Fetch all questions from database
        all_questions = db.query(models.Question)\
            .options(joinedload(models.Question.options))\
            .all()
        
        if not all_questions:
            raise ValueError("No questions found in database")
        
        # Get strand-based trait priorities
        from assessment_service import STRAND_TRAIT_MAPPING
        strand_upper = strand.upper() if strand else "GAS"
        if strand_upper not in STRAND_TRAIT_MAPPING:
            strand_upper = "GAS"
        
        strand_config = STRAND_TRAIT_MAPPING[strand_upper]
        priority_traits = set(strand_config["priority_traits"])
        secondary_traits = set(strand_config.get("secondary_traits", []))
        
        # Categorize questions by relevance to strand
        priority_questions = []
        secondary_questions = []
        general_questions = []
        
        for q in all_questions:
            question_traits = set()
            for opt in q.options:
                if opt.trait_tag:
                    question_traits.add(opt.trait_tag)
            
            priority_match = question_traits & priority_traits
            secondary_match = question_traits & secondary_traits
            
            if priority_match:
                priority_questions.append(q)
            elif secondary_match:
                secondary_questions.append(q)
            else:
                general_questions.append(q)
        
        # Calculate distribution
        import random
        if strand_upper == "GAS":
            priority_count = question_count // 3
            secondary_count = question_count // 3
            general_count = question_count - priority_count - secondary_count
        else:
            priority_count = int(question_count * 0.50)
            secondary_count = int(question_count * 0.30)
            general_count = question_count - priority_count - secondary_count
        
        # Select questions
        selected_questions = []
        random.shuffle(priority_questions)
        selected_questions.extend(priority_questions[:min(priority_count, len(priority_questions))])
        
        random.shuffle(secondary_questions)
        selected_questions.extend(secondary_questions[:min(secondary_count, len(secondary_questions))])
        
        random.shuffle(general_questions)
        selected_questions.extend(general_questions[:min(general_count, len(general_questions))])
        
        # Fill remaining if needed
        all_remaining = [q for q in all_questions if q not in selected_questions]
        random.shuffle(all_remaining)
        while len(selected_questions) < question_count and all_remaining:
            selected_questions.append(all_remaining.pop())
        
        # Shuffle final selection
        random.shuffle(selected_questions)
        
        # Format questions with database IDs
        formatted_questions = []
        for q in selected_questions:
            formatted_questions.append({
                "question_id": q.question_id,
                "question_text": q.question_text,
                "category": q.category,
                "options": [
                    {
                        "option_id": opt.option_id,
                        "option_text": opt.option_text,
                        "trait_tag": opt.trait_tag
                    }
                    for opt in q.options
                ]
            })
        
        return {
            "success": True,
            "message": f"{tier_config[tier]['name']} started successfully",
            "tier": tier,
            "name": tier_config[tier]['name'],
            "description": tier_config[tier]['description'],
            "question_count": len(formatted_questions),
            "estimated_time": tier_config[tier]['estimated_time'],
            "accuracy": tier_config[tier]['accuracy'],
            "strand": strand_upper,
            "strand_name": strand_config["name"],
            "questions": formatted_questions
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/assessment/questions/{tier}")
def get_assessment_questions(tier: str, strand: str = None):
    """
    Get questions for a specific assessment tier without full assessment metadata.
    Questions are prioritized based on user's SHS strand.
    """
    try:
        questions = AssessmentService.get_specific_questions(tier, strand=strand)
        from assessment_service import STRAND_TRAIT_MAPPING
        strand_upper = strand.upper() if strand else "GAS"
        strand_name = STRAND_TRAIT_MAPPING.get(strand_upper, {}).get("name", "General")
        
        return {
            "success": True,
            "tier": tier,
            "strand": strand_upper if strand else None,
            "strand_name": strand_name if strand else None,
            "question_count": len(questions),
            "questions": questions
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def home(): return {"status": "online"}

# ========== ADMIN: COURSE MANAGEMENT ==========

@app.get("/admin/courses")
def get_all_courses(db: Session = Depends(get_db)):
    """Admin: Get all courses with full details"""
    courses = db.query(models.Course).all()
    return {"courses": courses}

@app.get("/admin/courses/{course_id}")
def get_course(course_id: int, db: Session = Depends(get_db)):
    """Admin: Get specific course details"""
    course = db.query(models.Course).filter(models.Course.course_id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@app.post("/admin/courses")
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    """Admin: Create new course (D3 - Course Database)"""
    new_course = models.Course(
        course_name=course.course_name,
        description=course.description,
        trait_tag=course.trait_tag,
        required_strand=course.required_strand,
        minimum_gwa=course.minimum_gwa
    )
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return {"message": "Course created successfully", "course": new_course}

@app.put("/admin/courses/{course_id}")
def update_course(course_id: int, course: CourseUpdate, db: Session = Depends(get_db)):
    """Admin: Update existing course (D3 - Course Database)"""
    db_course = db.query(models.Course).filter(models.Course.course_id == course_id).first()
    if not db_course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    if course.course_name is not None:
        db_course.course_name = course.course_name
    if course.description is not None:
        db_course.description = course.description
    if course.trait_tag is not None:
        db_course.trait_tag = course.trait_tag
    if course.required_strand is not None:
        db_course.required_strand = course.required_strand
    if course.minimum_gwa is not None:
        db_course.minimum_gwa = course.minimum_gwa
    
    db.commit()
    db.refresh(db_course)
    return {"message": "Course updated successfully", "course": db_course}

@app.delete("/admin/courses/{course_id}")
def delete_course(course_id: int, db: Session = Depends(get_db)):
    """Admin: Delete course"""
    course = db.query(models.Course).filter(models.Course.course_id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    db.delete(course)
    db.commit()
    return {"message": f"Course '{course.course_name}' deleted successfully"}

# ========== ADMIN: QUESTION MANAGEMENT ==========

@app.get("/admin/questions")
def get_all_questions_admin(db: Session = Depends(get_db)):
    """Admin: Get all questions with options"""
    questions = db.query(models.Question).options(joinedload(models.Question.options)).all()
    return {"questions": questions}

@app.get("/admin/questions/{question_id}")
def get_question_admin(question_id: int, db: Session = Depends(get_db)):
    """Admin: Get specific question with options"""
    question = db.query(models.Question).options(joinedload(models.Question.options))\
        .filter(models.Question.question_id == question_id).first()
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    return question

@app.post("/admin/questions")
def create_question(question: QuestionCreate, db: Session = Depends(get_db)):
    """Admin: Create new question with options"""
    new_question = models.Question(
        question_text=question.question_text,
        category=question.category
    )
    db.add(new_question)
    db.flush()
    
    # Add options
    for opt in question.options:
        new_option = models.Option(
            question_id=new_question.question_id,
            option_text=opt.get("text"),
            trait_tag=opt.get("trait_tag")
        )
        db.add(new_option)
    
    db.commit()
    db.refresh(new_question)
    return {"message": "Question created successfully", "question_id": new_question.question_id}

@app.put("/admin/questions/{question_id}")
def update_question(question_id: int, question: QuestionUpdate, db: Session = Depends(get_db)):
    """Admin: Update question text/category"""
    db_question = db.query(models.Question).filter(models.Question.question_id == question_id).first()
    if not db_question:
        raise HTTPException(status_code=404, detail="Question not found")
    
    if question.question_text is not None:
        db_question.question_text = question.question_text
    if question.category is not None:
        db_question.category = question.category
    
    db.commit()
    return {"message": "Question updated successfully"}

@app.delete("/admin/questions/{question_id}")
def delete_question(question_id: int, db: Session = Depends(get_db)):
    """Admin: Delete question (cascades to options)"""
    question = db.query(models.Question).filter(models.Question.question_id == question_id).first()
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    
    db.delete(question)
    db.commit()
    return {"message": "Question deleted successfully"}

# ========== ADMIN: OPTION MANAGEMENT ==========

@app.post("/admin/questions/{question_id}/options")
def add_option(question_id: int, option: OptionCreate, db: Session = Depends(get_db)):
    """Admin: Add option to existing question"""
    question = db.query(models.Question).filter(models.Question.question_id == question_id).first()
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    
    new_option = models.Option(
        question_id=question_id,
        option_text=option.option_text,
        trait_tag=option.trait_tag
    )
    db.add(new_option)
    db.commit()
    db.refresh(new_option)
    return {"message": "Option added successfully", "option": new_option}

@app.put("/admin/options/{option_id}")
def update_option(option_id: int, option: OptionUpdate, db: Session = Depends(get_db)):
    """Admin: Update option"""
    db_option = db.query(models.Option).filter(models.Option.option_id == option_id).first()
    if not db_option:
        raise HTTPException(status_code=404, detail="Option not found")
    
    if option.option_text is not None:
        db_option.option_text = option.option_text
    if option.trait_tag is not None:
        db_option.trait_tag = option.trait_tag
    
    db.commit()
    return {"message": "Option updated successfully"}

@app.delete("/admin/options/{option_id}")
def delete_option(option_id: int, db: Session = Depends(get_db)):
    """Admin: Delete option"""
    option = db.query(models.Option).filter(models.Option.option_id == option_id).first()
    if not option:
        raise HTTPException(status_code=404, detail="Option not found")
    
    db.delete(option)
    db.commit()
    return {"message": "Option deleted successfully"}

# ========== ADMIN: USER MANAGEMENT ==========

@app.get("/admin/users")
def get_all_users(db: Session = Depends(get_db)):
    """Admin: Get all users with their info"""
    users = db.query(models.User).all()
    user_list = []
    for user in users:
        user_list.append({
            "user_id": user.user_id,
            "fullname": user.fullname,
            "email": user.email,
            "academic_info": user.academic_info,
            "created_at": user.created_at
        })
    return {"users": user_list}

@app.get("/admin/users/{user_id}")
def get_user_details(user_id: int, db: Session = Depends(get_db)):
    """Admin: Get specific user details with assessment history"""
    user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Get user's recommendations
    recommendations = db.query(models.Recommendation).filter(
        models.Recommendation.user_id == user_id
    ).all()
    
    # Get user's assessment answers count
    answers_count = db.query(models.StudentAnswer).filter(
        models.StudentAnswer.user_id == user_id
    ).count()
    
    return {
        "user_id": user.user_id,
        "fullname": user.fullname,
        "email": user.email,
        "academic_info": user.academic_info,
        "created_at": user.created_at,
        "total_assessments": db.query(models.TestAttempt).filter(models.TestAttempt.user_id == user_id).count(),
        "recommendations_count": len(recommendations),
        "latest_recommendations": [
            {
                "course_id": rec.course_id,
                "reasoning": rec.reasoning,
                "recommended_at": rec.recommended_at
            } for rec in recommendations
        ]
    }

@app.delete("/admin/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    """Admin: Delete user and all related data"""
    user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Delete related data (cascade will handle most)
    db.query(models.Recommendation).filter(models.Recommendation.user_id == user_id).delete()
    
    # Get all test attempts for user
    attempts = db.query(models.TestAttempt).filter(models.TestAttempt.user_id == user_id).all()
    for attempt in attempts:
        db.query(models.StudentAnswer).filter(models.StudentAnswer.attempt_id == attempt.attempt_id).delete()
    db.query(models.TestAttempt).filter(models.TestAttempt.user_id == user_id).delete()
    
    db.delete(user)
    db.commit()
    return {"message": f"User '{user.fullname}' and all related data deleted successfully"}

# ========== ADMIN: REPORTS & ANALYTICS ==========

@app.get("/admin/reports/overview")
def get_system_overview(db: Session = Depends(get_db)):
    """Admin: Get system-wide statistics"""
    total_users = db.query(models.User).count()
    total_courses = db.query(models.Course).count()
    total_questions = db.query(models.Question).count()
    total_test_attempts = db.query(models.TestAttempt).count()
    total_recommendations = db.query(models.Recommendation).count()
    total_tests = db.query(models.Test).count()
    
    return {
        "total_users": total_users,
        "total_courses": total_courses,
        "total_questions": total_questions,
        "total_tests": total_tests,
        "total_test_attempts": total_test_attempts,
        "total_recommendations_generated": total_recommendations
    }

@app.get("/admin/reports/popular-courses")
def get_popular_courses(db: Session = Depends(get_db)):
    """Admin: Get most recommended courses"""
    from sqlalchemy import func as sql_func
    
    popular_courses = db.query(
        models.Course.course_name,
        models.Course.course_id,
        sql_func.count(models.Recommendation.recommendation_id).label('recommendation_count')
    ).join(
        models.Recommendation,
        models.Course.course_id == models.Recommendation.course_id
    ).group_by(
        models.Course.course_id,
        models.Course.course_name
    ).order_by(
        sql_func.count(models.Recommendation.recommendation_id).desc()
    ).limit(10).all()
    
    return {
        "popular_courses": [
            {
                "course_name": course.course_name,
                "course_id": course.course_id,
                "times_recommended": course.recommendation_count
            } for course in popular_courses
        ]
    }

@app.get("/admin/reports/trait-distribution")
def get_trait_distribution(db: Session = Depends(get_db)):
    """Admin: Get distribution of personality traits from assessments"""
    from sqlalchemy import func as sql_func
    
    trait_counts = db.query(
        models.Option.trait_tag,
        sql_func.count(models.StudentAnswer.answer_id).label('count')
    ).join(
        models.StudentAnswer,
        models.Option.option_id == models.StudentAnswer.chosen_option_id
    ).filter(
        models.Option.trait_tag.isnot(None),
        models.Option.trait_tag != '',
        models.Option.trait_tag != 'None'
    ).group_by(
        models.Option.trait_tag
    ).order_by(
        sql_func.count(models.StudentAnswer.answer_id).desc()
    ).all()
    
    return {
        "trait_distribution": [
            {
                "trait": trait.trait_tag,
                "count": trait.count
            } for trait in trait_counts
        ]
    }

@app.get("/admin/reports/user-activity")
def get_user_activity(db: Session = Depends(get_db)):
    """Admin: Get recent user activity based on test attempts"""
    from sqlalchemy import func as sql_func
    
    recent_activity = db.query(
        models.User.first_name,
        models.User.last_name,
        models.User.email,
        sql_func.max(models.TestAttempt.taken_at).label('last_assessment')
    ).join(
        models.TestAttempt,
        models.User.user_id == models.TestAttempt.user_id
    ).group_by(
        models.User.user_id,
        models.User.first_name,
        models.User.last_name,
        models.User.email
    ).order_by(
        sql_func.max(models.TestAttempt.taken_at).desc()
    ).limit(20).all()
    
    return {
        "recent_activity": [
            {
                "fullname": f"{activity.first_name} {activity.last_name}".strip(),
                "email": activity.email,
                "last_assessment": activity.last_assessment
            } for activity in recent_activity
        ]
    }

# ========== USER: VIEW HISTORY ==========

@app.get("/user/{user_id}/recommendations")
def get_user_recommendations(user_id: int, db: Session = Depends(get_db)):
    """Get user's saved recommendations"""
    user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    recommendations = db.query(models.Recommendation).filter(
        models.Recommendation.user_id == user_id
    ).all()
    
    result = []
    for rec in recommendations:
        course = db.query(models.Course).filter(
            models.Course.course_id == rec.course_id
        ).first()
        
        if course:
            result.append({
                "course_name": course.course_name,
                "description": course.description,
                "reasoning": rec.reasoning,
                "minimum_gwa": float(course.minimum_gwa) if course.minimum_gwa else None,
                "required_strand": course.required_strand,
                "recommended_at": rec.recommended_at
            })
    
    return {"user_id": user_id, "recommendations": result}

@app.get("/user/{user_id}/assessment-history")
def get_assessment_history(user_id: int, db: Session = Depends(get_db)):
    """Get user's test attempts history with recommendations and answered questions (D5 - Test Attempt Database)"""
    user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Get all test attempts for this user with recommendations
    attempts = db.query(models.TestAttempt).filter(
        models.TestAttempt.user_id == user_id
    ).order_by(models.TestAttempt.taken_at.desc()).all()
    
    history = []
    for attempt in attempts:
        # Count answers for this attempt
        answer_count = db.query(models.StudentAnswer).filter(
            models.StudentAnswer.attempt_id == attempt.attempt_id
        ).count()
        
        # Get test name
        test = db.query(models.Test).filter(
            models.Test.test_id == attempt.test_id
        ).first()
        
        # Get all student answers with questions and options
        student_answers = db.query(models.StudentAnswer).filter(
            models.StudentAnswer.attempt_id == attempt.attempt_id
        ).all()
        
        answered_questions = []
        for answer in student_answers:
            question = db.query(models.Question).filter(
                models.Question.question_id == answer.question_id
            ).first()
            
            chosen_option = db.query(models.Option).filter(
                models.Option.option_id == answer.chosen_option_id
            ).first()
            
            if question and chosen_option:
                answered_questions.append({
                    "question_id": question.question_id,
                    "question_text": question.question_text,
                    "category": question.category,
                    "chosen_option_id": chosen_option.option_id,
                    "chosen_option_text": chosen_option.option_text,
                    "trait_tag": chosen_option.trait_tag
                })
        
        # Get recommendations for this attempt
        recommendations = db.query(models.Recommendation).filter(
            models.Recommendation.attempt_id == attempt.attempt_id
        ).all()
        
        recommended_courses = []
        for rec in recommendations:
            course = db.query(models.Course).filter(
                models.Course.course_id == rec.course_id
            ).first()
            if course:
                recommended_courses.append({
                    "course_id": course.course_id,
                    "course_name": course.course_name,
                    "description": course.description,
                    "reasoning": rec.reasoning
                })
        
        history.append({
            "attempt_id": attempt.attempt_id,
            "test_name": test.test_name if test else "Assessment",
            "taken_at": attempt.taken_at,
            "questions_answered": answer_count,
            "answered_questions": answered_questions,
            "recommended_courses": recommended_courses,
            "recommendation_count": len(recommended_courses)
        })
    
    return {
        "user_id": user_id,
        "total_attempts": len(attempts),
        "history": history
    }

# ========== ADMIN: TEST MANAGEMENT ==========

@app.get("/admin/tests")
def get_all_tests(db: Session = Depends(get_db)):
    """Admin: Get all tests"""
    tests = db.query(models.Test).all()
    return {"tests": tests}

@app.get("/admin/test-attempts")
def get_all_test_attempts(db: Session = Depends(get_db)):
    """Admin: Get all test attempts with user info"""
    attempts = db.query(models.TestAttempt).order_by(models.TestAttempt.taken_at.desc()).limit(50).all()
    
    result = []
    for attempt in attempts:
        user = db.query(models.User).filter(models.User.user_id == attempt.user_id).first()
        test = db.query(models.Test).filter(models.Test.test_id == attempt.test_id).first()
        
        result.append({
            "attempt_id": attempt.attempt_id,
            "user_name": user.fullname if user else "Unknown",
            "user_email": user.email if user else "Unknown",
            "test_name": test.test_name if test else "Unknown",
            "taken_at": attempt.taken_at
        })
    
    return {"test_attempts": result}

# ========== FEEDBACK SYSTEM ENDPOINTS ==========

@app.post("/feedback/submit")
def submit_recommendation_feedback(
    feedback: FeedbackSubmit,
    db: Session = Depends(get_db)
):
    """User: Submit feedback/rating on a recommendation or overall recommendations"""
    
    # Validate rating is 1-5
    if feedback.rating < 1 or feedback.rating > 5:
        raise HTTPException(status_code=400, detail="Rating must be between 1 and 5")
    
    # Handle overall feedback (no specific recommendation)
    if feedback.recommendation_id is None:
        new_feedback = models.RecommendationFeedback(
            recommendation_id=None,
            user_id=None,  # Overall feedback not tied to user
            rating=feedback.rating,
            feedback_text=feedback.feedback_text
        )
        db.add(new_feedback)
        db.commit()
        db.refresh(new_feedback)
        
        return {
            "success": True,
            "message": "Overall feedback submitted successfully",
            "feedback_id": new_feedback.feedback_id,
            "rating": new_feedback.rating
        }
    
    # Handle specific recommendation feedback
    recommendation = db.query(models.Recommendation).filter(
        models.Recommendation.recommendation_id == feedback.recommendation_id
    ).first()
    
    if not recommendation:
        raise HTTPException(status_code=404, detail="Recommendation not found")
    
    # Check if user already gave feedback on this recommendation
    existing_feedback = db.query(models.RecommendationFeedback).filter(
        models.RecommendationFeedback.recommendation_id == feedback.recommendation_id,
        models.RecommendationFeedback.user_id == recommendation.user_id
    ).first()
    
    if existing_feedback:
        # Update existing feedback
        existing_feedback.rating = feedback.rating
        existing_feedback.feedback_text = feedback.feedback_text
        db.commit()
        return {
            "success": True,
            "message": "Feedback updated successfully",
            "feedback_id": existing_feedback.feedback_id
        }
    
    # Create new feedback
    new_feedback = models.RecommendationFeedback(
        recommendation_id=feedback.recommendation_id,
        user_id=recommendation.user_id,
        rating=feedback.rating,
        feedback_text=feedback.feedback_text
    )
    
    db.add(new_feedback)
    db.commit()
    db.refresh(new_feedback)
    
    return {
        "success": True,
        "message": "Feedback submitted successfully",
        "feedback_id": new_feedback.feedback_id,
        "rating": new_feedback.rating
    }


@app.get("/feedback/recommendation/{recommendation_id}")
def get_recommendation_feedback(
    recommendation_id: int,
    db: Session = Depends(get_db)
):
    """Get all feedback for a specific recommendation"""
    
    recommendation = db.query(models.Recommendation).filter(
        models.Recommendation.recommendation_id == recommendation_id
    ).first()
    
    if not recommendation:
        raise HTTPException(status_code=404, detail="Recommendation not found")
    
    feedbacks = db.query(models.RecommendationFeedback).filter(
        models.RecommendationFeedback.recommendation_id == recommendation_id
    ).all()
    
    feedback_list = [
        {
            "feedback_id": f.feedback_id,
            "rating": f.rating,
            "feedback_text": f.feedback_text,
            "created_at": f.created_at.isoformat(),
            "user_fullname": db.query(models.User).filter(
                models.User.user_id == f.user_id
            ).first().fullname
        }
        for f in feedbacks
    ]
    
    return {
        "recommendation_id": recommendation_id,
        "course_name": recommendation.course.course_name,
        "total_feedbacks": len(feedback_list),
        "feedbacks": feedback_list
    }


@app.get("/user/{user_id}/feedback")
def get_user_feedback_history(
    user_id: int,
    db: Session = Depends(get_db)
):
    """Get all feedback submitted by a user"""
    
    user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    feedbacks = db.query(models.RecommendationFeedback).filter(
        models.RecommendationFeedback.user_id == user_id
    ).order_by(models.RecommendationFeedback.created_at.desc()).all()
    
    feedback_list = [
        {
            "feedback_id": f.feedback_id,
            "course_name": f.recommendation.course.course_name,
            "rating": f.rating,
            "feedback_text": f.feedback_text,
            "created_at": f.created_at.isoformat(),
            "reasoning": f.recommendation.reasoning
        }
        for f in feedbacks
    ]
    
    return {
        "user_id": user_id,
        "user_name": user.fullname,
        "total_feedbacks": len(feedback_list),
        "feedbacks": feedback_list
    }


@app.get("/admin/feedback/stats")
def get_feedback_statistics(db: Session = Depends(get_db)):
    """Admin: Get overall feedback statistics"""
    
    total_feedbacks = db.query(models.RecommendationFeedback).count()
    
    # Average rating
    avg_rating_query = db.query(
        func.avg(models.RecommendationFeedback.rating)
    ).scalar()
    avg_rating = round(float(avg_rating_query) if avg_rating_query else 0, 2)
    
    # Rating distribution
    rating_dist = {}
    for rating in range(1, 6):
        count = db.query(models.RecommendationFeedback).filter(
            models.RecommendationFeedback.rating == rating
        ).count()
        rating_dist[str(rating)] = count
    
    # Most feedback on courses (top 10)
    top_courses = db.query(
        models.Course.course_name,
        func.count(models.RecommendationFeedback.feedback_id).label('feedback_count'),
        func.avg(models.RecommendationFeedback.rating).label('avg_rating')
    ).join(
        models.Recommendation,
        models.Course.course_id == models.Recommendation.course_id
    ).join(
        models.RecommendationFeedback,
        models.Recommendation.recommendation_id == models.RecommendationFeedback.recommendation_id
    ).group_by(models.Course.course_name).order_by(
        func.count(models.RecommendationFeedback.feedback_id).desc()
    ).limit(10).all()
    
    top_courses_list = [
        {
            "course_name": course[0],
            "feedback_count": course[1],
            "avg_rating": round(float(course[2]), 2) if course[2] else 0
        }
        for course in top_courses
    ]
    
    return {
        "total_feedbacks": total_feedbacks,
        "average_rating": avg_rating,
        "rating_distribution": rating_dist,
        "top_courses": top_courses_list
    }


@app.get("/admin/feedback/courses/{course_id}")
def get_course_feedback_detailed(
    course_id: int,
    db: Session = Depends(get_db)
):
    """Admin: Get detailed feedback for a specific course"""
    
    course = db.query(models.Course).filter(models.Course.course_id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    feedbacks = db.query(models.RecommendationFeedback).join(
        models.Recommendation,
        models.RecommendationFeedback.recommendation_id == models.Recommendation.recommendation_id
    ).filter(
        models.Recommendation.course_id == course_id
    ).order_by(models.RecommendationFeedback.created_at.desc()).all()
    
    feedback_list = [
        {
            "feedback_id": f.feedback_id,
            "rating": f.rating,
            "feedback_text": f.feedback_text,
            "created_at": f.created_at.isoformat(),
            "user_name": f.user.fullname
        }
        for f in feedbacks
    ]
    
    # Calculate stats
    total = len(feedback_list)
    avg_rating = sum([f["rating"] for f in feedback_list]) / total if total > 0 else 0
    
    rating_breakdown = {}
    for rating in range(1, 6):
        rating_breakdown[str(rating)] = len([f for f in feedback_list if f["rating"] == rating])
    
    return {
        "course_id": course_id,
        "course_name": course.course_name,
        "total_feedbacks": total,
        "average_rating": round(avg_rating, 2),
        "rating_breakdown": rating_breakdown,
        "feedbacks": feedback_list
    }


@app.get("/admin/feedback/low-rated")
def get_low_rated_recommendations(
    min_rating: int = 3,
    db: Session = Depends(get_db)
):
    """Admin: Get recommendations that received ratings below threshold (alerts for improvement)"""
    
    # Get feedback with ratings below threshold
    low_rated = db.query(models.RecommendationFeedback).filter(
        models.RecommendationFeedback.rating < min_rating
    ).order_by(models.RecommendationFeedback.created_at.desc()).all()
    
    alerts = [
        {
            "feedback_id": f.feedback_id,
            "course_name": f.recommendation.course.course_name,
            "rating": f.rating,
            "feedback_text": f.feedback_text,
            "user_name": f.user.fullname,
            "created_at": f.created_at.isoformat(),
            "recommendation_reasoning": f.recommendation.reasoning
        }
        for f in low_rated
    ]
    
    return {
        "threshold": min_rating,
        "total_low_rated": len(alerts),
        "alerts": alerts[:20]  # Return latest 20
    }


@app.delete("/admin/feedback/{feedback_id}")
def delete_feedback(
    feedback_id: int,
    db: Session = Depends(get_db)
):
    """Admin: Delete a feedback entry"""
    
    feedback = db.query(models.RecommendationFeedback).filter(
        models.RecommendationFeedback.feedback_id == feedback_id
    ).first()
    
    if not feedback:
        raise HTTPException(status_code=404, detail="Feedback not found")
    
    db.delete(feedback)
    db.commit()
    
    return {"success": True, "message": "Feedback deleted successfully"}

# Run server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)


# ==================== AKINATOR-STYLE ADAPTIVE ASSESSMENT ====================
# These endpoints implement an intelligent question-by-question assessment
# that selects the BEST next question based on previous answers

# Global adaptive engine (initialized after database is seeded)
_adaptive_engine: AdaptiveAssessmentEngine = None

def get_or_init_adaptive_engine(db: Session) -> AdaptiveAssessmentEngine:
    """Get or initialize the adaptive engine with courses and questions from DB"""
    global _adaptive_engine
    
    if _adaptive_engine is None:
        # Load courses from database
        courses = db.query(models.Course).all()
        courses_data = [
            {
                "course_name": c.course_name,
                "description": c.description,
                "minimum_gwa": c.minimum_gwa,
                "required_strand": c.required_strand,
                "trait_tag": c.trait_tag
            }
            for c in courses
        ]
        
        # Load questions from database
        questions = db.query(models.Question).options(joinedload(models.Question.options)).all()
        questions_data = [
            {
                "question_id": q.question_id,
                "question_text": q.question_text,
                "category": q.category,
                "options": [
                    {
                        "option_id": opt.option_id,
                        "option_text": opt.option_text,
                        "trait_tag": opt.trait_tag
                    }
                    for opt in q.options
                ]
            }
            for q in questions
        ]
        
        _adaptive_engine = AdaptiveAssessmentEngine(courses_data, questions_data)
    
    return _adaptive_engine


class AdaptiveSessionStart(BaseModel):
    userId: int
    maxQuestions: int = 30


class AdaptiveAnswerSubmit(BaseModel):
    sessionId: str
    questionId: int
    chosenOptionId: int


@app.post("/adaptive/start")
def start_adaptive_assessment(data: AdaptiveSessionStart, db: Session = Depends(get_db)):
    """
    🧠 SMART ASSESSMENT - Start Session
    
    Starts an adaptive assessment that asks questions ONE AT A TIME.
    Each subsequent question is intelligently selected based on previous answers.
    User can choose 30, 50, or 60 questions.
    
    Returns: session_id and first question
    """
    # Get user info for initial scoring
    user = db.query(models.User).filter(models.User.user_id == data.userId).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    user_gwa = None
    user_strand = None
    if user.academic_info:
        user_gwa = user.academic_info.get("gwa")
        user_strand = user.academic_info.get("strand")
    
    # Initialize adaptive engine
    engine = get_or_init_adaptive_engine(db)
    
    # Update engine settings based on user selection
    max_questions = data.maxQuestions
    if max_questions not in [30, 50, 60]:
        max_questions = 30  # Default to 30 if invalid
    
    # Create session with custom max questions
    session_id = engine.create_session(data.userId, user_gwa, user_strand, max_questions)
    
    # Get first question
    first_question = engine.get_next_question(session_id)
    
    if not first_question:
        raise HTTPException(status_code=500, detail="Failed to start adaptive assessment")
    
    # Get session to return correct max/min values
    session = engine.sessions.get(session_id)
    
    return {
        "success": True,
        "message": f"🧠 Smart Assessment started with {max_questions} questions!",
        "session_id": session_id,
        "mode": "adaptive",
        "description": "Questions are selected based on your previous answers to find the best course match.",
        "max_questions": session.max_questions if session else max_questions,
        "min_questions": session.min_questions if session else int(max_questions * 0.5),
        "first_question": first_question
    }


def save_adaptive_session_to_db(db: Session, engine, session_id: str, recommendations: list):
    """Helper function to save adaptive assessment results to database for history tracking"""
    try:
        session = engine.sessions.get(session_id)
        if not session:
            return
        
        # Get or create adaptive test type
        adaptive_test = db.query(models.Test).filter(models.Test.test_type == "adaptive").first()
        if not adaptive_test:
            adaptive_test = models.Test(
                test_name="Smart Assessment (Adaptive)",
                test_type="adaptive",
                description="Akinator-style adaptive assessment"
            )
            db.add(adaptive_test)
            db.flush()
        
        # Create test attempt
        test_attempt = models.TestAttempt(
            user_id=session.user_id,
            test_id=adaptive_test.test_id
        )
        db.add(test_attempt)
        db.flush()
        
        # Save answered questions
        for question_id, option_id in session.answered_questions.items():
            db.add(models.StudentAnswer(
                attempt_id=test_attempt.attempt_id,
                question_id=question_id,
                chosen_option_id=option_id
            ))
        
        # Save recommendations
        for rec in recommendations:
            course = db.query(models.Course).filter(
                models.Course.course_name == rec["course_name"]
            ).first()
            if course:
                db.add(models.Recommendation(
                    attempt_id=test_attempt.attempt_id,
                    user_id=session.user_id,
                    course_id=course.course_id,
                    reasoning=f"Match: {rec.get('match_percentage', 75)}% - Matched traits: {', '.join(rec.get('matched_traits', []))}"
                ))
        
        db.commit()
        print(f"✅ Saved adaptive assessment to database: attempt_id={test_attempt.attempt_id}")
    except Exception as e:
        print(f"⚠️ Warning: Could not save to history: {e}")
        db.rollback()


@app.post("/adaptive/answer")
def submit_adaptive_answer(data: AdaptiveAnswerSubmit, db: Session = Depends(get_db)):
    """
    🧠 AKINATOR-STYLE ASSESSMENT - Submit Answer & Get Next Question
    
    Processes your answer and intelligently selects the NEXT BEST question.
    Shows you how courses are narrowing down in real-time.
    """
    engine = get_or_init_adaptive_engine(db)
    
    # Process the answer
    result = engine.process_answer(data.sessionId, data.questionId, data.chosenOptionId)
    
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    
    # If session is complete, return final results
    if result.get("status") == "complete":
        # Save to database for history
        save_adaptive_session_to_db(db, engine, data.sessionId, result["recommendations"])
        return {
            "success": True,
            "is_complete": True,
            "message": "Assessment complete! Here are your personalized recommendations.",
            "recommendations": result["recommendations"]
        }
    
    # Get next question
    next_question = engine.get_next_question(data.sessionId)
    
    if next_question is None:
        # Assessment complete
        final_results = engine.get_final_results(data.sessionId)
        # Save to database for history
        save_adaptive_session_to_db(db, engine, data.sessionId, final_results["recommendations"])
        return {
            "success": True,
            "is_complete": True,
            "message": f"Assessment complete after {result['round']} questions!",
            "total_questions": result["round"],
            "confidence": result["confidence"],
            "recommendations": final_results["recommendations"]
        }
    
    return {
        "success": True,
        "is_complete": False,
        "current_round": next_question["round"],
        "trait_recorded": result.get("trait_recorded"),
        "courses_remaining": result["courses_remaining"],
        "confidence": result["confidence"],
        "top_courses_preview": result.get("top_courses_preview", []),
        "traits_discovered": result.get("traits_discovered", 0),
        "next_question": next_question,
        "can_finish_early": next_question.get("can_finish_early", False)
    }


@app.post("/adaptive/finish")
def finish_adaptive_early(data: dict, db: Session = Depends(get_db)):
    """
    🧠 AKINATOR-STYLE ASSESSMENT - Finish Early
    
    If you've answered enough questions and want to see results now.
    Requires at least 10 questions answered.
    """
    session_id = data.get("sessionId")
    if not session_id:
        raise HTTPException(status_code=400, detail="Session ID required")
    
    engine = get_or_init_adaptive_engine(db)
    result = engine.finish_early(session_id)
    
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    
    # Save to database for history using the helper function
    save_adaptive_session_to_db(db, engine, session_id, result.get("recommendations", []))
    
    return {
        "success": True,
        "message": f"Assessment finished early after {result['total_questions_asked']} questions!",
        "total_questions": result["total_questions_asked"],
        "confidence": result["confidence"],
        "traits_discovered": result["traits_discovered"],
        "recommendations": result["recommendations"]
    }


@app.get("/adaptive/status/{session_id}")
def get_adaptive_status(session_id: str, db: Session = Depends(get_db)):
    """Get current status of an adaptive assessment session"""
    engine = get_or_init_adaptive_engine(db)
    
    if not engine.sessions.get(session_id):
        raise HTTPException(status_code=404, detail="Session not found")
    
    session = engine.sessions[session_id]
    
    return {
        "session_id": session_id,
        "is_complete": session.is_complete,
        "round": session.round_number,
        "confidence": round(session.confidence * 100, 1),
        "traits_discovered": len(session.trait_scores),
        "courses_remaining": len(session.active_courses),
        "questions_answered": len(session.answered_questions)
    }