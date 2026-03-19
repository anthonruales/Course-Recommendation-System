"""Test that trait cleanup produces correct recommendations"""
import sys
sys.path.insert(0, ".")

from importlib import reload
import questions_enhanced
reload(questions_enhanced)

from questions_enhanced import QUESTIONS_POOL_ENHANCED
from courses_specialized import COURSES_POOL_SPECIALIZED

# Simulate: user picks "Raising animals and livestock" (option 1282)
# What traits get recorded?
target_opt = None
for q in QUESTIONS_POOL_ENHANCED:
    for opt in q.get("options", []):
        if opt["option_id"] == 1282:
            target_opt = opt
            break

print(f'Option: "{target_opt["option_text"]}"')
print(f'Traits: {sorted(target_opt["trait_tags"].items(), key=lambda x: -x[1])}')
print()

# Check which courses match these traits
user_traits = target_opt["trait_tags"]

print("=== Course matching ===")
course_scores = []
for course in COURSES_POOL_SPECIALIZED:
    course_traits = course.get("trait_tag", [])
    if isinstance(course_traits, str):
        course_traits = [course_traits]
    
    score = 0
    matching_traits = []
    for ct in course_traits:
        if ct in user_traits:
            score += user_traits[ct]
            matching_traits.append(f"{ct}({user_traits[ct]})")
    
    if score > 0:
        course_scores.append((course["course_name"], score, matching_traits))

course_scores.sort(key=lambda x: -x[1])
print("Top 15 matching courses:")
for name, score, traits in course_scores[:15]:
    print(f"  {score:.2f} - {name} [{', '.join(traits)}]")

print("\n=== Verify no CS in top 5 for 'Raising animals' ===")
cs_courses = ["BS Computer Science", "BS Information Technology", "BS Computer Engineering"]
for name, score, traits in course_scores[:5]:
    if any(cs in name for cs in cs_courses):
        print(f"  PROBLEM: {name} in top 5!")
    else:
        print(f"  OK: {name}")
