from sqlalchemy import JSON, Column, Integer, String, Text, Float, ForeignKey, DateTime, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

# ========== USER TABLE (D1 - User Database) ==========
class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    password_hash = Column(String(255), nullable=False)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(100), unique=True, index=True, nullable=False)
    academic_info = Column(JSON, nullable=True)  # D4 - Personal & Academic Database (GWA, Strand, Age, Gender, etc.)
    created_at = Column(DateTime, server_default=func.now())
    
    # Relationships
    test_attempts = relationship("TestAttempt", back_populates="user", cascade="all, delete-orphan")
    recommendations = relationship("Recommendation", back_populates="user", cascade="all, delete-orphan")
    
    @property
    def fullname(self):
        """Computed fullname from first_name and last_name"""
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.first_name or self.last_name or self.username or "User"


# ========== TEST TABLE (Test Types) ==========
class Test(Base):
    __tablename__ = "tests"
    test_id = Column(Integer, primary_key=True, index=True)
    test_name = Column(String(100), nullable=False)
    test_type = Column(String(50), nullable=False)  # e.g., "assessment", "aptitude", "interest"
    description = Column(Text)
    
    # Relationships
    questions = relationship("Question", back_populates="test", cascade="all, delete-orphan")
    test_attempts = relationship("TestAttempt", back_populates="test", cascade="all, delete-orphan")


# ========== TEST ATTEMPTS TABLE (D5 - Test Attempt Database) ==========
class TestAttempt(Base):
    __tablename__ = "test_attempts"
    attempt_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    test_id = Column(Integer, ForeignKey("tests.test_id"), nullable=False)
    taken_at = Column(DateTime, server_default=func.now())
    
    # Relationships
    user = relationship("User", back_populates="test_attempts")
    test = relationship("Test", back_populates="test_attempts")
    student_answers = relationship("StudentAnswer", back_populates="attempt", cascade="all, delete-orphan")
    recommendations = relationship("Recommendation", back_populates="attempt", cascade="all, delete-orphan")


# ========== QUESTIONS TABLE (D2 - Question Database) ==========
class Question(Base):
    __tablename__ = "questions"
    question_id = Column(Integer, primary_key=True, index=True)
    test_id = Column(Integer, ForeignKey("tests.test_id"), nullable=True)  # Links to which test this belongs
    question_text = Column(Text, nullable=False)
    category = Column(String(50))  # e.g., "Situational", "Assessment", "Academic"
    
    # Relationships
    test = relationship("Test", back_populates="questions")
    options = relationship("Option", back_populates="question", cascade="all, delete-orphan")


# ========== OPTIONS TABLE ==========
class Option(Base):
    __tablename__ = "options"
    option_id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer, ForeignKey("questions.question_id"), nullable=False)
    option_text = Column(Text, nullable=False)
    trait_tag = Column(String(100))  # This is where "Cinematic", "Fiscal", etc. go
    
    # Relationships
    question = relationship("Question", back_populates="options")


# ========== STUDENT ANSWERS TABLE ==========
class StudentAnswer(Base):
    __tablename__ = "student_answers"
    answer_id = Column(Integer, primary_key=True, index=True)
    attempt_id = Column(Integer, ForeignKey("test_attempts.attempt_id"), nullable=False)
    question_id = Column(Integer, ForeignKey("questions.question_id"), nullable=False)
    chosen_option_id = Column(Integer, ForeignKey("options.option_id"), nullable=False)
    
    # Relationships
    attempt = relationship("TestAttempt", back_populates="student_answers")


# ========== COURSES TABLE (D3 - Course Database) ==========
class Course(Base):
    __tablename__ = "courses"
    course_id = Column(Integer, primary_key=True, index=True)
    course_name = Column(String(100), nullable=False)
    description = Column(Text)
    trait_tag = Column(String)  # Comma-separated trait tags for matching
    required_strand = Column(String(50))  # Required SHS strand
    minimum_gwa = Column(Numeric(5, 2))  # Minimum GWA requirement
    
    # Relationships
    recommendations = relationship("Recommendation", back_populates="course", cascade="all, delete-orphan")


# ========== RECOMMENDATIONS TABLE ==========
class Recommendation(Base):
    __tablename__ = "recommendations"
    recommendation_id = Column(Integer, primary_key=True, index=True)
    attempt_id = Column(Integer, ForeignKey("test_attempts.attempt_id"), nullable=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    course_id = Column(Integer, ForeignKey("courses.course_id"), nullable=False)
    reasoning = Column(Text)
    recommended_at = Column(DateTime, server_default=func.now())
    
    # Relationships
    attempt = relationship("TestAttempt", back_populates="recommendations")
    user = relationship("User", back_populates="recommendations")
    course = relationship("Course", back_populates="recommendations")