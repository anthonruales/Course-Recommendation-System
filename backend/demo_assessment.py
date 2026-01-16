from seed_data import QUESTIONS_POOL, COURSES_POOL
import random

print("="*70)
print("SAMPLE ASSESSMENT EXPERIENCE FOR FILIPINO SHS STUDENTS")
print("="*70)

# Show sample questions from different categories
categories_to_show = [
    "Core Activities",
    "Work Style", 
    "Learning Style",
    "Work Environment",
    "Healthcare Interest",
    "Project Role"
]

print("\n📝 Sample Questions:\n")
for cat in categories_to_show:
    q = [q for q in QUESTIONS_POOL if q['category'] == cat][0]
    print(f"Category: {cat}")
    print(f"Q: {q['question']}\n")
    for i, opt in enumerate(q['options'], 1):
        print(f"   {i}. {opt['text']}")
        print(f"      → Trait: {opt['tag']}\n")
    print("-" * 70)

# Simulate a student taking the assessment
print("\n🎯 SIMULATION: Student Profile Based on Answers\n")

# Sample student persona: Wants to help people, hands-on, clinical setting
sample_answers = [
    ("What type of activities do you find most fulfilling?", "Helping-others"),
    ("How do you prefer to work on important tasks?", "Collaborative"),
    ("How do you learn best?", "Hands-on"),
    ("What kind of work environment appeals to you most?", "Clinical-setting"),
    ("Are you interested in working directly with patients?", "Patient-focused"),
    ("Which field interests you the most?", "Patient-focused"),
]

trait_scores = {}
for question, trait in sample_answers:
    trait_scores[trait] = trait_scores.get(trait, 0) + 1
    print(f"✓ Answered: {question[:50]}...")
    print(f"  Selected trait: {trait}\n")

print("\n📊 Trait Profile:")
for trait, count in sorted(trait_scores.items(), key=lambda x: x[1], reverse=True):
    print(f"   {trait}: {count} points")

print("\n🎓 Top Matching Courses:")
# Find courses with these traits
matches = []
for course in COURSES_POOL:
    score = 0
    matched_traits = []
    for trait in trait_scores:
        if trait in course['trait_tag']:
            score += trait_scores[trait]
            matched_traits.append(trait)
    if score > 0:
        matches.append((course['course_name'], score, matched_traits))

matches.sort(key=lambda x: x[1], reverse=True)
for i, (name, score, traits) in enumerate(matches[:5], 1):
    print(f"\n{i}. {name}")
    print(f"   Match Score: {score}")
    print(f"   Matched Traits: {', '.join(traits)}")

print("\n" + "="*70)
print("This assessment provides personalized, accurate recommendations!")
print("="*70)
