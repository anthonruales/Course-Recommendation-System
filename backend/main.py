from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List
import models, database

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
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

class AssessmentAnswer(BaseModel):
    questionId: int
    response: str

class AssessmentSubmit(BaseModel):
    answers: List[AssessmentAnswer]

class UserCreate(BaseModel):
    fullname: str
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

@app.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email exists")
    new_user = models.User(fullname=user.fullname, email=user.email, password=user.password)
    db.add(new_user)
    db.commit()
    return {"message": "Success"}

@app.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if not db_user or db_user.password != user.password:
        raise HTTPException(status_code=400, detail="Error")
    return {"user": db_user.fullname}

@app.post("/recommend")
def recommend(data: AssessmentSubmit, db: Session = Depends(get_db)):
    ans = {item.questionId: item.response for item in data.answers}
    
    # DECISION TREE BRANCHING LOGIC
    if ans.get(4) == "yes": # Tech Interest
        if ans.get(1) == "yes": # Math Interest
            winner, course = "ICT", "BS Information Technology"
            reason = "High logical aptitude and technical interest."
        else:
            winner, course = "Arts", "BS Multimedia Arts"
            reason = "Creative interest with technical tools."
    else: # Non-Tech
        if ans.get(1) == "yes": # Math Interest
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
def home(): return {"status": "online"}