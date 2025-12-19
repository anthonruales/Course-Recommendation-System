import os
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List
from dotenv import load_dotenv
from security import hash_password, verify_password
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

import models, database
from security import hash_password, verify_password

load_dotenv()

# Variables for future Google Auth use
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], # Or ["*"] to allow everything
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=database.engine)

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
    
    # Use security.py to hash
    hashed_pwd = hash_password(user.password)
    
    new_user = models.User(fullname=user.fullname, email=user.email, password=hashed_pwd)
    db.add(new_user)
    db.commit()
    return {"message": "Success"}

@app.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    
    # Verify hashed password
    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid email or password")
        
    return {"user": db_user.fullname}

@app.post("/recommend")
def recommend(data: AssessmentSubmit, db: Session = Depends(get_db)):
    ans = {item.questionId: item.response for item in data.answers}
    
    if ans.get(4) == "yes":
        if ans.get(1) == "yes": 
            winner, course = "ICT", "BS Information Technology"
            reason = "High logical aptitude and technical interest."
        else:
            winner, course = "Arts", "BS Multimedia Arts"
            reason = "Creative interest with technical tools."
    else: 
        if ans.get(1) == "yes": 
            winner, course = "STEM", "BS Civil Engineering"
            reason = "Strong foundation in mathematics and analysis."
        else:
            winner, course = "Business", "BS Accountancy"
            reason = "Interest in organizational and financial logic."

    new_rec = models.Recommendation(user_email="student", category=winner, course=course, reasoning=reason)
    db.add(new_rec)
    db.commit()
    return {"category": winner, "recommendation": course, "explanation": reason}

@app.get("/history")
def get_history(db: Session = Depends(get_db)):
    return db.query(models.Recommendation).order_by(models.Recommendation.id.desc()).limit(5).all()

@app.get("/")
def home(): 
    return {"status": "online", "google_ready": bool(GOOGLE_CLIENT_ID)}