from seed_data import QUESTIONS_POOL, COURSES_POOL

print("="*70)
print("ASSESSMENT QUESTIONS VALIDATION")
print("="*70)

# Validate questions
print(f"\n✓ Total Questions: {len(QUESTIONS_POOL)}")

# Count by category
categories = {}
for q in QUESTIONS_POOL:
    cat = q.get('category', 'Unknown')
    categories[cat] = categories.get(cat, 0) + 1

print(f"\n📊 Questions by Category:")
for cat, count in sorted(categories.items()):
    print(f"   {cat}: {count}")

# Collect all trait tags from questions
question_traits = set()
for q in QUESTIONS_POOL:
    for opt in q.get('options', []):
        tag = opt.get('tag')
        if tag and tag != 'None':
            question_traits.add(tag)

# Collect all trait tags from courses
course_traits = set()
for c in COURSES_POOL:
    for tag in c.get('trait_tag', []):
        course_traits.add(tag)

print(f"\n✓ Unique traits in questions: {len(question_traits)}")
print(f"✓ Unique traits in courses: {len(course_traits)}")

# Find coverage
covered = question_traits.intersection(course_traits)
missing_in_questions = course_traits - question_traits
extra_in_questions = question_traits - course_traits

print(f"\n📈 Coverage Analysis:")
print(f"   ✓ Traits covered by questions: {len(covered)} ({len(covered)/len(course_traits)*100:.1f}%)")
print(f"   ⚠ Course traits not in questions: {len(missing_in_questions)}")
if missing_in_questions:
    print(f"      Missing: {', '.join(sorted(list(missing_in_questions))[:10])}{'...' if len(missing_in_questions) > 10 else ''}")

print(f"\n✅ Question traits not in courses: {len(extra_in_questions)}")
if extra_in_questions:
    print(f"      Extra: {', '.join(sorted(list(extra_in_questions))[:5])}{'...' if len(extra_in_questions) > 5 else ''}")

# Sample questions
print(f"\n📝 Sample Questions:")
for i, q in enumerate(QUESTIONS_POOL[:3], 1):
    print(f"\n{i}. {q['question']}")
    print(f"   Category: {q['category']}")
    print(f"   Options: {len(q['options'])}")
    for opt in q['options']:
        print(f"      - {opt['text'][:50]}... → {opt['tag']}")

# Check for 'None' tags
none_count = sum(1 for q in QUESTIONS_POOL for opt in q['options'] if opt.get('tag') == 'None')
print(f"\n⚠️ Questions with 'None' tag: {none_count} (used for neutral options)")

print("\n" + "="*70)
print("VALIDATION COMPLETE")
print("="*70)
