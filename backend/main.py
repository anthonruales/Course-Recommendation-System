import os
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List, Optional
from dotenv import load_dotenv
from passlib.context import CryptContext
from sqlalchemy import text  # Added for database operations
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

# 1. Initialize database tables (Creates the tables)
models.Base.metadata.create_all(bind=database.engine)

# 2. SEEDING LOGIC: This function populates the table
def seed_database():
    db = database.SessionLocal()
    try:
        if db.query(models.Course).count() == 0:
            print("Empty courses table detected. Seeding 50 courses...")
            initial_courses = [
                # STEM
                models.Course(course_name="BS Civil Engineering", description="Design and construction of infrastructure.", minimum_gwa=85, recommended_strand="STEM"),
                models.Course(course_name="BS Mechanical Engineering", description="Design and manufacturing of machine systems.", minimum_gwa=85, recommended_strand="STEM"),
                models.Course(course_name="BS Electrical Engineering", description="Study of electricity, electronics, and electromagnetism.", minimum_gwa=85, recommended_strand="STEM"),
                models.Course(course_name="BS Chemical Engineering", description="Converting raw materials into useful products.", minimum_gwa=85, recommended_strand="STEM"),
                models.Course(course_name="BS Computer Science", description="Theory of computation and software design.", minimum_gwa=88, recommended_strand="STEM"),
                models.Course(course_name="BS Biology", description="Study of living organisms and life processes.", minimum_gwa=85, recommended_strand="STEM"),
                models.Course(course_name="BS Chemistry", description="Study of matter and its properties.", minimum_gwa=85, recommended_strand="STEM"),
                models.Course(course_name="BS Physics", description="Study of matter, energy, and the universe.", minimum_gwa=85, recommended_strand="STEM"),
                models.Course(course_name="BS Architecture", description="Planning and designing buildings.", minimum_gwa=86, recommended_strand="STEM"),
                models.Course(course_name="BS Nursing", description="Medical care and health services.", minimum_gwa=88, recommended_strand="STEM"),
                models.Course(course_name="BS Pharmacy", description="Study of medicine and clinical pharmacy.", minimum_gwa=85, recommended_strand="STEM"),
                models.Course(course_name="BS Medical Technology", description="Laboratory science for diagnosis.", minimum_gwa=87, recommended_strand="STEM"),
                models.Course(course_name="BS Statistics", description="Mathematical data analysis.", minimum_gwa=84, recommended_strand="STEM"),
                models.Course(course_name="BS Geology", description="Study of the Earth and its materials.", minimum_gwa=83, recommended_strand="STEM"),
                models.Course(course_name="BS Marine Biology", description="Study of marine life and ecosystems.", minimum_gwa=83, recommended_strand="STEM"),

                # ICT
                models.Course(course_name="BS Information Technology", description="Software development and networking.", minimum_gwa=83, recommended_strand="ICT"),
                models.Course(course_name="BS Information Systems", description="Bridging IT and business needs.", minimum_gwa=83, recommended_strand="ICT"),
                models.Course(course_name="BS Cyber Security", description="Protecting systems and networks.", minimum_gwa=85, recommended_strand="ICT"),
                models.Course(course_name="BS Data Science", description="Extracting knowledge from data.", minimum_gwa=86, recommended_strand="ICT"),
                models.Course(course_name="BS Animation", description="Creating 2D/3D digital art and motion.", minimum_gwa=80, recommended_strand="ICT"),

                # ABM
                models.Course(course_name="BS Accountancy", description="Financial auditing and reporting.", minimum_gwa=90, recommended_strand="ABM"),
                models.Course(course_name="BS Business Administration", description="Management and corporate operations.", minimum_gwa=82, recommended_strand="ABM"),
                models.Course(course_name="BS Marketing", description="Strategic promotion and sales.", minimum_gwa=80, recommended_strand="ABM"),
                models.Course(course_name="BS Entrepreneurship", description="Starting and managing businesses.", minimum_gwa=80, recommended_strand="ABM"),
                models.Course(course_name="BS Hospitality Management", description="Tourism and hotel operations.", minimum_gwa=80, recommended_strand="ABM"),
                models.Course(course_name="BS Customs Administration", description="Tariff and customs laws.", minimum_gwa=82, recommended_strand="ABM"),
                models.Course(course_name="BS Finance", description="Investment and money management.", minimum_gwa=84, recommended_strand="ABM"),
                models.Course(course_name="BS Real Estate Management", description="Property sales and development.", minimum_gwa=80, recommended_strand="ABM"),

                # HUMSS
                models.Course(course_name="BS Psychology", description="Study of human mind and behavior.", minimum_gwa=85, recommended_strand="HUMSS"),
                models.Course(course_name="BA Political Science", description="Study of government and policy.", minimum_gwa=83, recommended_strand="HUMSS"),
                models.Course(course_name="BA Communication", description="Media, news, and broadcasting.", minimum_gwa=80, recommended_strand="HUMSS"),
                models.Course(course_name="BA Philosophy", description="Critical thinking and ethics.", minimum_gwa=80, recommended_strand="HUMSS"),
                models.Course(course_name="BA History", description="Study of past events and civilizations.", minimum_gwa=80, recommended_strand="HUMSS"),
                models.Course(course_name="BA Literature", description="Study of written works and arts.", minimum_gwa=80, recommended_strand="HUMSS"),
                models.Course(course_name="BS Social Work", description="Community welfare and service.", minimum_gwa=82, recommended_strand="HUMSS"),
                models.Course(course_name="BA Sociology", description="Study of social life and change.", minimum_gwa=80, recommended_strand="HUMSS"),
                models.Course(course_name="Bachelor of Laws", description="Legal studies (Pre-Law).", minimum_gwa=88, recommended_strand="HUMSS"),

                # GAS / EDUCATION / OTHERS
                models.Course(course_name="BS Multimedia Arts", description="Graphic design and visual media.", minimum_gwa=82, recommended_strand="GAS"),
                models.Course(course_name="B Elementary Education", description="Teaching for primary grade levels.", minimum_gwa=80, recommended_strand="GAS"),
                models.Course(course_name="B Secondary Education", description="Teaching for high school levels.", minimum_gwa=80, recommended_strand="GAS"),
                models.Course(course_name="BS Criminology", description="Crime prevention and law enforcement.", minimum_gwa=82, recommended_strand="GAS"),
                models.Course(course_name="BS Exercise Science", description="Study of physical fitness and health.", minimum_gwa=80, recommended_strand="GAS"),
                models.Course(course_name="BS Tourism Management", description="Travel industry management.", minimum_gwa=80, recommended_strand="GAS"),
                models.Course(course_name="BS Forestry", description="Management of forest resources.", minimum_gwa=80, recommended_strand="GAS"),
                models.Course(course_name="BS Agriculture", description="Crop and livestock production.", minimum_gwa=80, recommended_strand="GAS"),
                models.Course(course_name="BS Fine Arts", description="Visual arts and creative expression.", minimum_gwa=80, recommended_strand="GAS"),
                models.Course(course_name="BS Interior Design", description="Space planning and aesthetics.", minimum_gwa=83, recommended_strand="GAS"),
                models.Course(course_name="BS Nutrition and Dietetics", description="Food science and nutrition.", minimum_gwa=84, recommended_strand="GAS"),
                models.Course(course_name="BS Library Science", description="Organization of information.", minimum_gwa=80, recommended_strand="GAS"),
                models.Course(course_name="BA Foreign Languages", description="Linguistic and cultural studies.", minimum_gwa=80, recommended_strand="GAS")
            ]
            db.add_all(initial_courses)
            db.commit()
            print("✅ SUCCESS: 50 Courses seeded successfully!")
    except Exception as e:
        print(f"❌ Error seeding: {e}")
    finally:
        db.close()

# 3. TRIGGER SEEDING: Run it once when the app starts
seed_database()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

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
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already exists")
    
    hashed_pwd = hash_password(user.password)
    
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
    
    if not db_user or not verify_password(user.password, db_user.password_hash):
        raise HTTPException(status_code=400, detail="Invalid email or password")
        
    return {"user": db_user.fullname, "user_id": db_user.user_id}

@app.post("/recommend")
def recommend(data: AssessmentSubmit, db: Session = Depends(get_db)):
    ans = {item.questionId: item.response.lower() for item in data.answers}
    
    # 1. Determine which course to search for based on answers
    target_course_name = ""
    reason = ""

    if ans.get(1) == "yes":
        target_course_name = "BS Information Technology"
        reason = "You have a natural talent for troubleshooting and fixing hardware."
    elif ans.get(2) == "yes":
        target_course_name = "BS Computer Science"
        reason = "Your analytical mind is perfect for data and logic."
    elif ans.get(3) == "yes":
        target_course_name = "BS Accountancy" # Changed to match your 4 automated courses
        reason = "You show strong leadership and organization skills."
    else:
        # Fallback to the first course in your DB if no 'yes' answers
        target_course_name = "BS Civil Engineering" 
        reason = "Based on your general profile, we suggest exploring engineering."

    # 2. QUERY THE DATABASE to make sure this course actually exists
    course_from_db = db.query(models.Course).filter(models.Course.course_name == target_course_name).first()

    if course_from_db:
        return {
            "category": course_from_db.recommended_strand, 
            "recommendation": course_from_db.course_name, 
            "explanation": reason
        }
    else:
        # Emergency fallback if the database is somehow empty
        return {
            "category": "N/A",
            "recommendation": "Course not found in database",
            "explanation": "Please ensure the courses table is seeded."
        }

@app.get("/get-recommendations/{user_id}")
def recommend_courses(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.user_id == user_id).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if not user.academic_info:
        raise HTTPException(status_code=400, detail="Please complete your academic profile first.")

    user_strand = user.academic_info.get("strand", "N/A")
    user_gwa = user.academic_info.get("gwa", 0)

    try:
        all_courses = db.query(models.Course).all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error in Courses table: {str(e)}")
    
    filtered_list = []
    for course in all_courses:
        try:
            course_min_gwa = float(course.minimum_gwa) if course.minimum_gwa else 0
            
            if float(user_gwa) >= course_min_gwa:
                is_aligned = (course.recommended_strand == user_strand)
                filtered_list.append({
                    "course_name": course.course_name,
                    "alignment_score": "High" if is_aligned else "Flexible",
                    "description": course.description
                })
        except Exception:
            continue 

    return filtered_list

@app.get("/history")
def get_history(db: Session = Depends(get_db)):
    return db.query(models.Recommendation).order_by(models.Recommendation.id.desc()).limit(5).all()

@app.get("/")
def home(): 
    return {"status": "online", "google_ready": bool(GOOGLE_CLIENT_ID)}