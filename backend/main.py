import os
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from dotenv import load_dotenv
import models, database
from security import hash_password, verify_password
from seed_data import COURSES_POOL, QUESTIONS_POOL
from sqlalchemy import func
from sqlalchemy.orm import Session, joinedload

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
                    required_strand=c.get("recommended_strand"), 
                    trait_tag=tag_str
                ))

        if QUESTIONS_POOL:
            print(f"🌱 Seeding {len(QUESTIONS_POOL)} questions...")
            for q in QUESTIONS_POOL:
                new_q = models.Question(
                    test_id=default_test.test_id,
                    question_text=q.get("question"), 
                    category=q.get("category")
                )
                db.add(new_q)
                db.flush()
                options_list = q.get("options", [])
                if options_list:
                    for opt in options_list:
                        db.add(models.Option(question_id=new_q.question_id, option_text=opt.get("text"), trait_tag=opt.get("tag")))
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

class UserCreate(BaseModel): fullname: str; email: str; password: str
class UserLogin(BaseModel): email: str; password: str
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


@app.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    if db.query(models.User).filter(models.User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already exists")
    
    # Parse fullname into first_name and last_name
    name_parts = user.fullname.strip().split(" ", 1)
    first_name = name_parts[0] if name_parts else user.fullname
    last_name = name_parts[1] if len(name_parts) > 1 else ""
    
    # Generate username from email
    username = user.email.split("@")[0]
    
    new_user = models.User(
        username=username,
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
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if not db_user or not verify_password(user.password, db_user.password_hash):
        raise HTTPException(status_code=400, detail="Invalid email or password")
    return {"user": db_user.fullname, "user_id": db_user.user_id}


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

@app.post("/recommend")
def recommend(data: AssessmentSubmit, db: Session = Depends(get_db)):
    """
    DFD Process 5-7: Take a Test → Rule Based-Logic → Decision Tree
    Enhanced recommendation system that considers:
    1. User's trait scores from assessment answers
    2. User's academic info (GWA, Strand) from D4
    3. Course requirements from D3 (Course Database)
    """
    print(f"📝 Received recommendation request for user {data.userId} with {len(data.answers)} answers")
    
    # 1. Fetch user's academic info (D4 - Personal & Academic Database)
    user = db.query(models.User).filter(models.User.user_id == data.userId).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    user_gwa = None
    user_strand = None
    if user.academic_info:
        user_gwa = user.academic_info.get("gwa")
        user_strand = user.academic_info.get("strand")
    
    # Get the default test
    default_test = db.query(models.Test).filter(models.Test.test_type == "assessment").first()
    if not default_test:
        raise HTTPException(status_code=500, detail="No assessment test found in system")
    
    # Create a new test attempt (D5 - Test Attempt Database)
    test_attempt = models.TestAttempt(
        user_id=data.userId,
        test_id=default_test.test_id
    )
    db.add(test_attempt)
    db.flush()  # Get the attempt_id
    print(f"📋 Created test attempt ID: {test_attempt.attempt_id}")
    
    # 2. Process 6: Fetch Q&A - Count traits from the assessment answers
    trait_scores = {}
    total_answers = len(data.answers)
    valid_answers = 0
    
    for ans in data.answers:
        option = db.query(models.Option).filter(
            models.Option.option_id == ans.chosenOptionId
        ).first()
        
        if option:
            # Save student answer linked to test attempt
            db.add(models.StudentAnswer(
                attempt_id=test_attempt.attempt_id,
                question_id=ans.questionId,
                chosen_option_id=ans.chosenOptionId
            ))
            
            if option.trait_tag and str(option.trait_tag).strip().lower() not in ["none", ""]:
                tag = option.trait_tag.strip()
                trait_scores[tag] = trait_scores.get(tag, 0) + 1
                valid_answers += 1
        else:
            print(f"⚠️ Warning: Option ID {ans.chosenOptionId} not found in database")
    
    print(f"📊 Assessment Stats: {total_answers} answers, {valid_answers} with valid traits")
    print(f"📊 Trait Scores: {trait_scores}")
    
    if not trait_scores:
        db.rollback()
        raise HTTPException(
            status_code=400, 
            detail=f"Unable to generate recommendations. No personality traits were identified from your {total_answers} answers. Please ensure you've answered all questions."
        )
    
    # 3. Process 7: Rule Based-Logic - Get sorted traits (highest scoring traits first)
    sorted_traits = sorted(trait_scores.items(), key=lambda x: x[1], reverse=True)
    top_3_traits = sorted_traits[:3]
    primary_trait = top_3_traits[0][0]
    
    # 4. Find matching courses with filtering
    all_matching_courses = db.query(models.Course).all()
    
    # Score each course based on trait matches and academic fit
    scored_courses = []
    for course in all_matching_courses:
        score = 0
        matched_traits = []
        
        # Check trait matches (from user's answers)
        if course.trait_tag:
            course_tags = [tag.strip() for tag in course.trait_tag.split(",")]
            for trait, count in top_3_traits:
                if trait in course_tags:
                    score += count * 3  # Weight by how many times this trait was selected
                    matched_traits.append(trait)
        
        # Check GWA requirement (D3 - Course Database)
        gwa_match = True
        gwa_penalty = 0
        if user_gwa and course.minimum_gwa:
            if user_gwa >= float(course.minimum_gwa):
                score += 2  # Bonus for meeting GWA
            else:
                gwa_match = False
                gwa_penalty = 5
        
        # Check Strand recommendation (D3 - Course Database)
        strand_match = True
        strand_penalty = 0
        if user_strand and course.required_strand:
            if user_strand in course.required_strand:
                score += 2  # Bonus for matching strand
                strand_match = True
            else:
                strand_match = False
                strand_penalty = 3
        
        # Always include course but apply penalties later for ranking
        final_score = score - gwa_penalty - strand_penalty
        
        scored_courses.append({
            "course": course,
            "score": final_score,
            "raw_score": score,
            "matched_traits": matched_traits,
            "gwa_match": gwa_match,
            "strand_match": strand_match
        })
    
    print(f"📊 Scored {len(scored_courses)} courses")
    
    # 5. Sort by score and get top recommendations
    scored_courses.sort(key=lambda x: x["score"], reverse=True)
    
    # If no courses have positive scores, just take top courses by raw score
    if not scored_courses or scored_courses[0]["score"] <= 0:
        print("⚠️ No high-scoring matches found, using best available courses")
        scored_courses.sort(key=lambda x: x["raw_score"], reverse=True)
    
    top_recommendations = scored_courses[:5]
    
    # 6. Format response with detailed reasoning
    recommendations = []
    for rec in top_recommendations:
        course = rec["course"]
        
        # Build reasoning message
        if rec['matched_traits']:
            reasoning = f"This course aligns with your interests in {', '.join(rec['matched_traits'])}. "
        else:
            reasoning = f"This course is recommended based on your overall profile. "
        
        if user_gwa and course.minimum_gwa:
            if not rec["gwa_match"]:
                reasoning += f"Note: Your GWA ({user_gwa}) is below the minimum requirement ({course.minimum_gwa}). "
            elif user_gwa >= float(course.minimum_gwa):
                reasoning += f"Your GWA ({user_gwa}) meets the requirement ({course.minimum_gwa}). "
        
        if user_strand and course.required_strand:
            if not rec["strand_match"]:
                reasoning += f"Your strand ({user_strand}) is different from recommended ({course.required_strand}), but you may still qualify. "
            else:
                reasoning += f"Your strand ({user_strand}) matches perfectly! "
        
        recommendations.append({
            "course_name": course.course_name,
            "description": course.description,
            "matched_traits": rec["matched_traits"],
            "minimum_gwa": float(course.minimum_gwa) if course.minimum_gwa else None,
            "recommended_strand": course.required_strand,
            "reasoning": reasoning,
            "compatibility_score": rec["score"]
        })
    
    # Process 8: Decision Tree - Save recommendations to database
    try:
        # Save new recommendations linked to this test attempt
        for idx, rec in enumerate(top_recommendations):
            course = rec["course"]
            db.add(models.Recommendation(
                attempt_id=test_attempt.attempt_id,
                user_id=data.userId,
                course_id=course.course_id,
                reasoning=recommendations[idx]["reasoning"]
            ))
        
        db.commit()
        print(f"✅ Saved {len(top_recommendations)} recommendations for attempt {test_attempt.attempt_id}")
    except Exception as e:
        print(f"❌ Error saving recommendations: {e}")
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error saving recommendations: {str(e)}")
    
    return {
        "user_id": data.userId,
        "user_gwa": user_gwa,
        "user_strand": user_strand,
        "detected_traits": top_3_traits,
        "recommendations": recommendations
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
    """Get user's test attempts history (D5 - Test Attempt Database)"""
    user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Get all test attempts for this user
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
        
        history.append({
            "attempt_id": attempt.attempt_id,
            "test_name": test.test_name if test else "Assessment",
            "taken_at": attempt.taken_at,
            "questions_answered": answer_count
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

# Run server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)