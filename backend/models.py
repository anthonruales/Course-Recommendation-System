from sqlalchemy import JSON, Column, Integer, String, Text, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    fullname = Column(String)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    academic_info = Column(JSON, nullable=True) # Stores Strand and GWA
    created_at = Column(DateTime, server_default=func.now())

class Course(Base):
    __tablename__ = "courses"
    course_id = Column(Integer, primary_key=True, index=True)
    course_name = Column(String, nullable=False)
    description = Column(Text)
    trait_tag = Column(String) # Matches the specific tags like "Maternal-care"
    recommended_strand = Column(String)
    minimum_gwa = Column(Float)

class Question(Base):
    __tablename__ = "questions"
    question_id = Column(Integer, primary_key=True)
    # ... other fields ...
    options = relationship("Option", back_populates="question")
    question_text = Column(Text, nullable=False)
    category = Column(String)
    
    # Relationship to get all choices for this question
    options = relationship("Option", back_populates="question", cascade="all, delete-orphan")

class Option(Base):
    __tablename__ = "options"
    option_id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer, ForeignKey("questions.question_id"))
    option_text = Column(Text, nullable=False)
    trait_tag = Column(String(100)) # This is where "Cinematic", "Fiscal", etc. go
    
    question = relationship("Question", back_populates="options")

class StudentAnswer(Base):
    __tablename__ = "student_answers"
    answer_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    question_id = Column(Integer, ForeignKey("questions.question_id"))
    chosen_option_id = Column(Integer, ForeignKey("options.option_id"))
    taken_at = Column(DateTime, server_default=func.now())

class Recommendation(Base):
    __tablename__ = "recommendations"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    top_trait = Column(String)
    course_id = Column(Integer, ForeignKey("courses.course_id"))
    reasoning = Column(Text)