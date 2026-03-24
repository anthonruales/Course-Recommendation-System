import sys
sys.path.insert(0, r'C:\Users\USer\Downloads\capstone-back-end\Course-Recommendation-System\backend')
from data.questions_enhanced import QUESTIONS_POOL_ENHANCED
from data.courses_specialized import COURSES_POOL_SPECIALIZED
print('OK', len(QUESTIONS_POOL_ENHANCED), len(COURSES_POOL_SPECIALIZED))
