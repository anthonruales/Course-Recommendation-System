# questions_specialized.py - Questions for SPECIALIZED Trait System
"""
================================================================================
SPECIALIZED QUESTIONS - Now using Enhanced Questions
================================================================================

This file now imports from questions_enhanced.py which has:
- 40 comprehensive questions
- 8-10 options per question (10.0 average)
- 400 total options covering all 31 traits
- Better trait-to-course mapping

================================================================================
"""

# Import from the new enhanced questions file
from questions_enhanced import QUESTIONS_POOL_ENHANCED

# Maintain backward compatibility - use the same variable name
QUESTIONS_POOL_SPECIALIZED = QUESTIONS_POOL_ENHANCED

# For testing
if __name__ == "__main__":
    print(f"Questions loaded: {len(QUESTIONS_POOL_SPECIALIZED)}")
    print(f"Total options: {sum(len(q['options']) for q in QUESTIONS_POOL_SPECIALIZED)}")
    print(f"Average options per question: {sum(len(q['options']) for q in QUESTIONS_POOL_SPECIALIZED) / len(QUESTIONS_POOL_SPECIALIZED):.1f}")
