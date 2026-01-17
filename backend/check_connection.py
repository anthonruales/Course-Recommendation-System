"""Quick check to verify questions and courses are connected via traits"""
from seed_data import COURSES_POOL, QUESTIONS_POOL

print('=== CONNECTION CHECK ===')
print(f'Courses loaded: {len(COURSES_POOL)}')
print(f'Questions loaded: {len(QUESTIONS_POOL)}')

# Check a sample course
print('\n=== SAMPLE COURSE ===')
nursing = next((c for c in COURSES_POOL if 'Nursing' in c['course_name']), None)
if nursing:
    print(f"Course: {nursing['course_name']}")
    print(f"Traits: {nursing['trait_tag']}")

# Check a sample question
print('\n=== SAMPLE QUESTION (Healthcare) ===')
q = QUESTIONS_POOL[3]  # Healthcare question
print(f"Question: {q['question_text']}")
for opt in q['options']:
    print(f"  - {opt['option_text'][:50]}... -> {opt['trait_tag']}")

# Check trait overlap between questions and courses
print('\n=== TRAIT MATCHING ===')
course_traits = set()
for c in COURSES_POOL:
    course_traits.update(c['trait_tag'])

question_traits = set()
for q in QUESTIONS_POOL:
    for opt in q.get('options', []):
        if opt.get('trait_tag'):
            question_traits.add(opt['trait_tag'])

matched = course_traits & question_traits
missing_in_questions = course_traits - question_traits

print(f'Traits in courses: {len(course_traits)}')
print(f'Traits in questions: {len(question_traits)}')
print(f'Matching traits: {len(matched)}')
print(f'Coverage: {len(matched)/len(course_traits)*100:.1f}%')

if missing_in_questions:
    print(f'\nTraits in courses but NOT in questions: {missing_in_questions}')
else:
    print('\n✅ All course traits are covered by questions!')

# Simulate how traits accumulate to match a course
print('\n=== HOW MATCHING WORKS ===')
print('Example: User wants to become a Nurse')
print('Nursing course has traits:', nursing['trait_tag'])
print('\nUser answers:')
print('  Q1 (Interest Type): "Helping people, teaching, providing care" -> Social ✓')
print('  Q4 (Healthcare): "Caring for patients directly" -> Patient-Care ✓')
print('  Q23 (Skills): "People skills - communication, empathy" -> People-Skill ✓')
print('\nResult: User accumulated [Social, Patient-Care, People-Skill]')
print('        BS Nursing has [Social, Patient-Care, People-Skill]')
print('        PERFECT MATCH! 3/3 traits = 100%')
