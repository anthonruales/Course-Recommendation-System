import os
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from dotenv import load_dotenv
import models, database
from security import hash_password, verify_password
from seed_data import COURSES_POOL, SITUATIONAL_QUESTIONS_POOL, ASSESSMENT_QUESTIONS_POOL, ACADEMIC_QUESTIONS_POOL
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
        db.query(models.Option).delete()
        db.query(models.Question).delete()
        db.query(models.Course).delete()
        db.commit()

        if COURSES_POOL:
            print(f"🌱 Seeding {len(COURSES_POOL)} courses...")
            for c in COURSES_POOL:
                tags = c.get("trait_tag", [])
                tag_str = ", ".join(tags) if isinstance(tags, list) else str(tags)
                db.add(models.Course(course_name=c.get("course_name"), description=c.get("description"), minimum_gwa=c.get("minimum_gwa"), recommended_strand=c.get("recommended_strand"), trait_tag=tag_str))

        all_questions = SITUATIONAL_QUESTIONS_POOL + ASSESSMENT_QUESTIONS_POOL + ACADEMIC_QUESTIONS_POOL
        if all_questions:
            print(f"🌱 Seeding {len(all_questions)} questions...")
            for q in all_questions:
                new_q = models.Question(question_text=q.get("text"), category=q.get("category"))
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
    gwa: float  # GWA on 80-100 scale (e.g., 88.5, 92.0)
    strand: str  # e.g., "STEM", "ABM", "HUMSS", "GAS", "TVL", "Sports"

class CourseCreate(BaseModel):
    course_name: str
    description: str
    trait_tag: str
    recommended_strand: Optional[str] = None
    minimum_gwa: Optional[float] = None

class CourseUpdate(BaseModel):
    course_name: Optional[str] = None
    description: Optional[str] = None
    trait_tag: Optional[str] = None
    recommended_strand: Optional[str] = None
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
    db.add(models.User(fullname=user.fullname, email=user.email, password_hash=hash_password(user.password)))
    db.commit(); return {"message": "Success"}

@app.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if not db_user or not verify_password(user.password, db_user.password_hash):
        raise HTTPException(status_code=400, detail="Invalid email or password")
    return {"user": db_user.fullname, "user_id": db_user.user_id}


@app.put("/user/{user_id}/academic-info")
def update_academic_info(user_id: int, info: AcademicInfoUpdate, db: Session = Depends(get_db)):
    """Update user's academic info (GWA and Strand) for recommendation accuracy"""
    user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    user.academic_info = {
        "gwa": info.gwa,
        "strand": info.strand
    }
    db.commit()
    return {
        "message": "Academic info updated successfully",
        "user_id": user_id,
        "academic_info": user.academic_info
    }

@app.post("/recommend")
def recommend(data: AssessmentSubmit, db: Session = Depends(get_db)):
    """
    Enhanced recommendation system that considers:
    1. User's trait scores from assessment answers
    2. User's academic info (GWA, Strand)
    3. Course requirements and recommendations
    """
    print(f"📝 Received recommendation request for user {data.userId} with {len(data.answers)} answers")
    
    # 1. Fetch user's academic info
    user = db.query(models.User).filter(models.User.user_id == data.userId).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    user_gwa = None
    user_strand = None
    if user.academic_info:
        user_gwa = user.academic_info.get("gwa")
        user_strand = user.academic_info.get("strand")
    
    # 2. Count traits from the assessment answers
    trait_scores = {}
    total_answers = len(data.answers)
    valid_answers = 0
    
    for ans in data.answers:
        option = db.query(models.Option).filter(
            models.Option.option_id == ans.chosenOptionId
        ).first()
        
        if option:
            if option.trait_tag and str(option.trait_tag).strip().lower() not in ["none", ""]:
                tag = option.trait_tag.strip()
                trait_scores[tag] = trait_scores.get(tag, 0) + 1
                valid_answers += 1
        else:
            print(f"⚠️ Warning: Option ID {ans.chosenOptionId} not found in database")
    
    print(f"📊 Assessment Stats: {total_answers} answers, {valid_answers} with valid traits")
    print(f"📊 Trait Scores: {trait_scores}")
    
    if not trait_scores:
        raise HTTPException(
            status_code=400, 
            detail=f"Unable to generate recommendations. No personality traits were identified from your {total_answers} answers. Please ensure you've answered all questions."
        )
    
    # 3. Get sorted traits (highest scoring traits first)
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
        
        # Check GWA requirement
        gwa_match = True
        gwa_penalty = 0
        if user_gwa and course.minimum_gwa:
            if user_gwa >= course.minimum_gwa:
                score += 2  # Bonus for meeting GWA
            else:
                gwa_match = False
                gwa_penalty = 5
        
        # Check Strand recommendation
        strand_match = True
        strand_penalty = 0
        if user_strand and course.recommended_strand:
            if user_strand in course.recommended_strand:
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
        
        # Build detailed reasoning with structured factors
        reasoning_factors = {
            "strand_influence": None,
            "academic_interest": None,
            "gwa_assessment": None,
            "trait_alignment": None,
            "summary": ""
        }
        
        # 1. Trait Alignment
        if rec['matched_traits']:
            reasoning_factors["trait_alignment"] = f"Matches your personality traits: {', '.join(rec['matched_traits'])}"
        else:
            reasoning_factors["trait_alignment"] = "Recommended based on your overall profile"
        
        # 2. Strand Influence - Always show course requirements, compare if user has provided info
        if course.recommended_strand:
            if user_strand:
                if rec["strand_match"]:
                    reasoning_factors["strand_influence"] = f"✓ Your strand ({user_strand}) perfectly aligns with the recommended strand ({course.recommended_strand})"
                else:
                    reasoning_factors["strand_influence"] = f"⚠ Your strand ({user_strand}) differs from recommended ({course.recommended_strand}), but alternative path is available"
            else:
                reasoning_factors["strand_influence"] = f"Recommended strand: {course.recommended_strand} (Please update your academic profile to see compatibility)"
        else:
            reasoning_factors["strand_influence"] = "No specific strand requirement for this course"
        
        # 3. GWA Assessment - Always show course requirements, compare if user has provided GWA
        if course.minimum_gwa:
            if user_gwa:
                if rec["gwa_match"]:
                    gwa_buffer = user_gwa - course.minimum_gwa
                    reasoning_factors["gwa_assessment"] = f"✓ Your GWA ({user_gwa}) exceeds the minimum requirement ({course.minimum_gwa}) by {gwa_buffer:.2f} points"
                else:
                    gwa_gap = course.minimum_gwa - user_gwa
                    reasoning_factors["gwa_assessment"] = f"⚠ Your GWA ({user_gwa}) is {gwa_gap:.2f} points below the minimum requirement ({course.minimum_gwa}). You may need improvement."
            else:
                reasoning_factors["gwa_assessment"] = f"Minimum GWA required: {course.minimum_gwa} (Please update your academic profile to see compatibility)"
        else:
            reasoning_factors["gwa_assessment"] = "No GWA requirement for this course"
        
        # 4. Academic Interest (traits derived from assessment answers)
        if trait_scores:
            top_user_traits = [t[0] for t in sorted(trait_scores.items(), key=lambda x: x[1], reverse=True)[:3]]
            reasoning_factors["academic_interest"] = f"Your assessment revealed interests in: {', '.join(top_user_traits)}"
        else:
            reasoning_factors["academic_interest"] = "Unable to determine academic interests from assessment"
        
        # Build summary reasoning
        reasoning = f"{reasoning_factors['trait_alignment']}. {reasoning_factors['strand_influence']} {reasoning_factors['gwa_assessment']} {reasoning_factors['academic_interest']}"
        reasoning_factors["summary"] = reasoning
        
        recommendations.append({
            "course_name": course.course_name,
            "description": course.description,
            "matched_traits": rec["matched_traits"],
            "minimum_gwa": course.minimum_gwa,
            "recommended_strand": course.recommended_strand,
            "reasoning": reasoning,
            "reasoning_details": reasoning_factors,
            "compatibility_score": rec["score"]
        })
    
    # 7. Save recommendations to database
    try:
        # Clear old recommendations for this user
        db.query(models.Recommendation).filter(models.Recommendation.user_id == data.userId).delete()
        
        # Save new recommendations
        for rec in top_recommendations:
            course = rec["course"]
            db.add(models.Recommendation(
                user_id=data.userId,
                course_id=course.course_id,
                top_trait=primary_trait,
                reasoning=recommendations[top_recommendations.index(rec)]["reasoning"]
            ))
        
        # Save student answers
        db.query(models.StudentAnswer).filter(models.StudentAnswer.user_id == data.userId).delete()
        for ans in data.answers:
            db.add(models.StudentAnswer(
                user_id=data.userId,
                question_id=ans.questionId,
                chosen_option_id=ans.chosenOptionId
            ))
        
        db.commit()
    except Exception as e:
        print(f"❌ Error saving recommendations: {e}")
        db.rollback()
    
    return {
        "user_id": data.userId,
        "user_gwa": user_gwa,
        "user_strand": user_strand,
        "detected_traits": top_3_traits,
        "recommendations": recommendations
    }

def get_suitable_courses(user: models.User, db: Session):
    """Get courses suitable for the student's academic profile (GWA & Strand)"""
    if not user.academic_info:
        return []
    
    user_gwa = user.academic_info.get("gwa")
    user_strand = user.academic_info.get("strand")
    
    suitable_courses = []
    if user_gwa and user_strand:
        suitable_courses = db.query(models.Course).filter(
            models.Course.minimum_gwa <= user_gwa,
            models.Course.recommended_strand.contains(user_strand)
        ).all()
    
    return suitable_courses

def extract_trait_tags(courses: List[models.Course]):
    """Extract all unique trait tags from a list of courses"""
    trait_tags = set()
    for course in courses:
        if course.trait_tag:
            tags = [tag.strip() for tag in course.trait_tag.split(",")]
            trait_tags.update(tags)
    return trait_tags

@app.get("/questions", response_model=List[QuestionSchema])
def get_questions(user_id: Optional[int] = None, db: Session = Depends(get_db)):
    """
    Fetch 10 random questions from each category (situational, assessment, academic).
    If user_id is provided, bias questions towards traits of suitable courses for that student.
    """
    relevant_traits = set()
    
    # If user provided, get their academic profile and find suitable courses
    if user_id:
        user = db.query(models.User).filter(models.User.user_id == user_id).first()
        if user and user.academic_info:
            suitable_courses = get_suitable_courses(user, db)
            relevant_traits = extract_trait_tags(suitable_courses)
    
    def get_questions_by_category(category: str, limit: int = 10):
        """Fetch questions, prioritizing those with relevant traits"""
        query = db.query(models.Question)\
            .options(joinedload(models.Question.options))\
            .filter(models.Question.category == category)
        
        all_questions = query.all()
        
        # If we have relevant traits, prioritize questions with matching traits
        if relevant_traits:
            prioritized = []
            non_prioritized = []
            
            for question in all_questions:
                # Check if any option in this question has a relevant trait
                question_traits = set()
                for option in question.options:
                    if option.trait_tag:
                        question_traits.add(option.trait_tag)
                
                # If question has relevant traits, prioritize it
                if question_traits & relevant_traits:
                    prioritized.append(question)
                else:
                    non_prioritized.append(question)
            
            # Return prioritized questions first, fill remaining with random non-prioritized
            selected = prioritized[:limit]
            if len(selected) < limit:
                remaining_needed = limit - len(selected)
                selected.extend(non_prioritized[:remaining_needed])
            
            return selected[:limit]
        else:
            # No academic profile, return random questions
            return query.order_by(func.random()).limit(limit).all()
    
    # Fetch from each category
    situational = get_questions_by_category("Situational", 10)
    assessment = get_questions_by_category("Assessment", 10)
    academic = get_questions_by_category("Academic", 10)
    
    questions = situational + assessment + academic
    
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
    """Admin: Create new course"""
    new_course = models.Course(
        course_name=course.course_name,
        description=course.description,
        trait_tag=course.trait_tag,
        recommended_strand=course.recommended_strand,
        minimum_gwa=course.minimum_gwa
    )
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return {"message": "Course created successfully", "course": new_course}

@app.put("/admin/courses/{course_id}")
def update_course(course_id: int, course: CourseUpdate, db: Session = Depends(get_db)):
    """Admin: Update existing course"""
    db_course = db.query(models.Course).filter(models.Course.course_id == course_id).first()
    if not db_course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    if course.course_name is not None:
        db_course.course_name = course.course_name
    if course.description is not None:
        db_course.description = course.description
    if course.trait_tag is not None:
        db_course.trait_tag = course.trait_tag
    if course.recommended_strand is not None:
        db_course.recommended_strand = course.recommended_strand
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
        "total_assessments": answers_count // 20 if answers_count > 0 else 0,
        "recommendations_count": len(recommendations),
        "latest_recommendations": [
            {
                "course_id": rec.course_id,
                "top_trait": rec.top_trait,
                "reasoning": rec.reasoning
            } for rec in recommendations
        ]
    }

@app.delete("/admin/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    """Admin: Delete user and all related data"""
    user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Delete related data
    db.query(models.Recommendation).filter(models.Recommendation.user_id == user_id).delete()
    db.query(models.StudentAnswer).filter(models.StudentAnswer.user_id == user_id).delete()
    
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
    total_assessments = db.query(models.StudentAnswer).count() // 20  # Assuming 20 questions per assessment
    total_recommendations = db.query(models.Recommendation).count()
    
    return {
        "total_users": total_users,
        "total_courses": total_courses,
        "total_questions": total_questions,
        "total_assessments_taken": total_assessments,
        "total_recommendations_generated": total_recommendations
    }

@app.get("/admin/reports/popular-courses")
def get_popular_courses(db: Session = Depends(get_db)):
    """Admin: Get most recommended courses"""
    from sqlalchemy import func as sql_func
    
    popular_courses = db.query(
        models.Course.course_name,
        models.Course.course_id,
        sql_func.count(models.Recommendation.id).label('recommendation_count')
    ).join(
        models.Recommendation,
        models.Course.course_id == models.Recommendation.course_id
    ).group_by(
        models.Course.course_id,
        models.Course.course_name
    ).order_by(
        sql_func.count(models.Recommendation.id).desc()
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
    """Admin: Get recent user activity"""
    from sqlalchemy import func as sql_func
    
    recent_assessments = db.query(
        models.User.fullname,
        models.User.email,
        sql_func.max(models.StudentAnswer.taken_at).label('last_assessment')
    ).join(
        models.StudentAnswer,
        models.User.user_id == models.StudentAnswer.user_id
    ).group_by(
        models.User.user_id,
        models.User.fullname,
        models.User.email
    ).order_by(
        sql_func.max(models.StudentAnswer.taken_at).desc()
    ).limit(20).all()
    
    return {
        "recent_activity": [
            {
                "fullname": activity.fullname,
                "email": activity.email,
                "last_assessment": activity.last_assessment
            } for activity in recent_assessments
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
                "top_trait": rec.top_trait,
                "reasoning": rec.reasoning,
                "minimum_gwa": course.minimum_gwa,
                "recommended_strand": course.recommended_strand
            })
    
    return {"user_id": user_id, "recommendations": result}

@app.get("/user/{user_id}/assessment-history")
def get_assessment_history(user_id: int, db: Session = Depends(get_db)):
    """Get user's assessment answer history"""
    user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    answers = db.query(models.StudentAnswer).filter(
        models.StudentAnswer.user_id == user_id
    ).order_by(models.StudentAnswer.taken_at.desc()).all()
    
    # Group by assessment session (assume consecutive answers within 1 hour are same session)
    return {
        "user_id": user_id,
        "total_answers": len(answers),
        "assessments_taken": len(answers) // 20 if len(answers) > 0 else 0,
        "last_assessment": answers[0].taken_at if answers else None
    }

# Run server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)