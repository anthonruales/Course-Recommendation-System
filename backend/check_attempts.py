#!/usr/bin/env python
"""Check recent test attempts and their data"""

import os
import sys

# Don't import main.py which starts the server
os.environ['NO_SERVER'] = '1'

from database import SessionLocal

# Import models directly
from sqlalchemy import Column, Integer, String, Float, Boolean, Text, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from database import Base

# Minimal model definitions for this script
class TestAttempt(Base):
    __tablename__ = 'test_attempts'
    attempt_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer)
    test_id = Column(Integer)
    taken_at = Column(DateTime)

class StudentAnswer(Base):
    __tablename__ = 'student_answers'
    answer_id = Column(Integer, primary_key=True, autoincrement=True)
    attempt_id = Column(Integer)

class Recommendation(Base):
    __tablename__ = 'recommendations'
    recommendation_id = Column(Integer, primary_key=True, autoincrement=True)
    attempt_id = Column(Integer)
    user_id = Column(Integer)
    course_id = Column(Integer)

db = SessionLocal()

# Check test attempts
print('=== RECENT TEST ATTEMPTS ===')
attempts = db.query(TestAttempt).order_by(TestAttempt.taken_at.desc()).limit(5).all()
for a in attempts:
    print(f'Attempt {a.attempt_id}: user={a.user_id}, test_id={a.test_id}, taken_at={a.taken_at}')
    
    # Count answers
    answers = db.query(StudentAnswer).filter(StudentAnswer.attempt_id == a.attempt_id).count()
    print(f'  -> {answers} answers saved')
    
    # Count recommendations
    recs = db.query(Recommendation).filter(Recommendation.attempt_id == a.attempt_id).count()
    print(f'  -> {recs} recommendations saved')

print()

# Check total recommendations
total_recs = db.query(Recommendation).count()
print(f'Total recommendations in DB: {total_recs}')
