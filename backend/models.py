from sqlalchemy import JSON, Column, Integer, String, Text, Float
from database import Base

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    fullname = Column(String)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    academic_info = Column(JSON, nullable=True)

class Recommendation(Base):
    __tablename__ = "recommendations"
    id = Column(Integer, primary_key=True, index=True)
    user_email = Column(String)
    category = Column(String)
    course = Column(String)
    reasoning = Column(String)

class Course(Base):
    __tablename__ = "courses"
    course_id = Column(Integer, primary_key=True, index=True)
    course_name = Column(String, nullable=False)
    description = Column(String)
    trait_tag = Column(String)
    recommended_strand = Column(String)
    minimum_gwa = Column(Float)

class Question(Base):
    __tablename__ = "questions"
    question_id = Column(Integer, primary_key=True, index=True)
    question_text = Column(Text, nullable=False)
    category = Column(String) 
    trait_tag = Column(String)