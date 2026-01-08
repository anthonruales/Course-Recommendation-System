import os
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List, Optional
from dotenv import load_dotenv
import models
import database
from security import hash_password, verify_password
from seed_data import COURSES_POOL, QUESTIONS_POOL

load_dotenv()

# --- LIFESPAN (Database Initialization) ---
@asynccontextmanager
async def lifespan(app: FastAPI):
    # 1. Initialize database tables
    print("🛠️ Synchronizing database schema...")
    models.Base.metadata.create_all(bind=database.engine)
    
    # 2. Trigger Seeding
    seed_database()
    yield

# --- CONFIGURATION ---
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- DATABASE SEEDING LOGIC ---
def seed_database():
    db = database.SessionLocal()
    try:
        # 1. Clear everything to ensure the new schema takes effect
        print("🧹 Cleaning out old data...")
        db.query(models.Course).delete()
        db.query(models.Question).delete()
        db.commit() 

        # 2. Seed Courses
        if COURSES_POOL:
            print(f"🌱 Seeding {len(COURSES_POOL)} courses...")
            for c in COURSES_POOL:
                new_course = models.Course(
                    course_name=c.get("course_name"),
                    description=c.get("description"),
                    minimum_gwa=c.get("minimum_gwa"),
                    recommended_strand=c.get("recommended_strand"),
                    trait_tag=c.get("trait_tag")
                )
                db.add(new_course)

        # 3. Seed Questions
        if QUESTIONS_POOL:
            print(f"🌱 Seeding {len(QUESTIONS_POOL)} questions...")
            for q in QUESTIONS_POOL:
                new_q = models.Question(
                    question_text=q.get("text"), 
                    category=q.get("category"),
                    trait_tag=q.get("tag") 
                )
                db.add(new_q)

        db.commit()
        print("✅ DATABASE SUCCESSFULLY REBUILT AND SEEDED!")

    except Exception as e:
        print(f"❌ DATABASE ERROR: {e}")
        db.rollback()
    finally:
        db.close()


        
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
    
    new_user = models.User(
        fullname=user.fullname, 
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

@app.post("/recommend")
def recommend(data: AssessmentSubmit, db: Session = Depends(get_db)):
    ans = {item.questionId: item.response.lower() for item in data.answers}
    target_course_name = "BS Computer Science" if ans.get(2) == "yes" else "BS Civil Engineering"

    course_from_db = db.query(models.Course).filter(models.Course.course_name == target_course_name).first()

    if course_from_db:
        return {
            "category": course_from_db.recommended_strand, 
            "recommendation": course_from_db.course_name, 
            "explanation": "Based on your technical interest."
        }
    return {"error": "Course not found"}

@app.get("/")
def home(): 
    return {"status": "online", "google_ready": bool(GOOGLE_CLIENT_ID)}