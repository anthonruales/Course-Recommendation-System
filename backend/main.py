import os
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List, Optional
from dotenv import load_dotenv
from passlib.context import CryptContext
import models
import database
from security import hash_password, verify_password

load_dotenv()

# --- CONFIGURATION ---
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize database tables
models.Base.metadata.create_all(bind=database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

        from sqlalchemy import text

def seed_database(db: Session):
    # Check if we already have courses so we don't duplicate them
    course_count = db.query(models.Course).count()
    if course_count == 0:
        print("Empty courses table detected. Seeding initial data...")
        initial_courses = [
            models.Course(
                course_name="BS Information Technology",
                description="Study of software development, networking, and systems.",
                minimum_gwa=85.0,
                recommended_strand="ICT"
            ),
            models.Course(
                course_name="BS Computer Science",
                description="Focus on algorithms, programming, and computing theory.",
                minimum_gwa=88.0,
                recommended_strand="STEM"
            ),
            models.Course(
                course_name="BS Accountancy",
                description="Professional track for certified public accountants.",
                minimum_gwa=90.0,
                recommended_strand="ABM"
            ),
            models.Course(
                course_name="BS Civil Engineering",
                description="Design and construction of infrastructure projects.",
                minimum_gwa=87.0,
                recommended_strand="STEM"
            )
        ]
        db.add_all(initial_courses)
        db.commit()
        print("Database seeded successfully!")

# --- SCHEMAS ---
class UserCreate(BaseModel):
    fullname: str
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class AssessmentAnswer(BaseModel):
    questionId: int
    response: str

class AssessmentSubmit(BaseModel):
    answers: List[AssessmentAnswer]

# --- ROUTES ---

@app.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    # Check if email exists
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already exists")
    
    hashed_pwd = hash_password(user.password)
    
    # CORRECTED: Uses 'password_hash' to match your pgAdmin screenshot
    new_user = models.User(
        fullname=user.fullname, 
        email=user.email, 
        password_hash=hashed_pwd 
    )
    db.add(new_user)
    db.commit()
    return {"message": "Success"}

@app.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    
    # CORRECTED: Uses 'password_hash' and checks for user existence
    if not db_user or not verify_password(user.password, db_user.password_hash):
        raise HTTPException(status_code=400, detail="Invalid email or password")
        
    # CORRECTED: Returns 'user_id' to match your pgAdmin PK
    return {"user": db_user.fullname, "user_id": db_user.user_id}

@app.post("/recommend")
def recommend(data: AssessmentSubmit, db: Session = Depends(get_db)):
    # Create a dictionary: {1: "yes", 2: "no", 3: "no"}
    ans = {item.questionId: item.response.lower() for item in data.answers}
    
    # Check the specific IDs from your AssessmentForm.js
    if ans.get(1) == "yes":
        course = "BS Information Technology"
        reason = "You have a natural talent for troubleshooting and fixing hardware."
    elif ans.get(2) == "yes":
        course = "BS Computer Science"
        reason = "Your analytical mind is perfect for data and logic."
    elif ans.get(3) == "yes":
        course = "BS Business Administration"
        reason = "You show strong leadership and communication skills."
    else:
        course = "Bachelor of Arts"
        reason = "A flexible degree suits your varied interests."

    return {
        "category": "General", 
        "recommendation": course, 
        "explanation": reason
    }

@app.get("/get-recommendations/{user_id}")
def recommend_courses(user_id: int, db: Session = Depends(get_db)):
    # 1. Fetch user data
    user = db.query(models.User).filter(models.User.user_id == user_id).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if not user.academic_info:
        raise HTTPException(status_code=400, detail="Please complete your academic profile first.")

    user_strand = user.academic_info.get("strand", "N/A")
    user_gwa = user.academic_info.get("gwa", 0)

    # 2. Fetch courses and handle potential data errors
    try:
        all_courses = db.query(models.Course).all()
    except Exception as e:
        # This will tell you if the 'courses' table name or columns are wrong
        raise HTTPException(status_code=500, detail=f"Database error in Courses table: {str(e)}")
    
    filtered_list = []
    for course in all_courses:
        try:
            # We use float() carefully here
            course_min_gwa = float(course.minimum_gwa) if course.minimum_gwa else 0
            
            if float(user_gwa) >= course_min_gwa:
                is_aligned = (course.recommended_strand == user_strand)
                filtered_list.append({
                    "course_name": course.course_name,
                    "alignment_score": "High" if is_aligned else "Flexible",
                    "description": course.description
                })
        except Exception:
            continue # Skip any course that has broken data instead of crashing

    return filtered_list

@app.get("/history")
def get_history(db: Session = Depends(get_db)):
    return db.query(models.Recommendation).order_by(models.Recommendation.id.desc()).limit(5).all()

@app.get("/")
def home(): 
    return {"status": "online", "google_ready": bool(GOOGLE_CLIENT_ID)}