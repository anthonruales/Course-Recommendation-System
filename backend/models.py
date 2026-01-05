from sqlalchemy import JSON, Column, Integer, String, Text, Numeric, Float
from database import Base


# models.py
class User(Base):
    __tablename__ = "users"
    
    # Ensure there are no spaces or capital letters here
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
    course_name = Column(String)
    description = Column(String)
    minimum_gwa = Column(Float)  # Must match the numeric data in pgAdmin
    recommended_strand = Column(String)