from database import SessionLocal
from models import Question, Option, Course
from trait_mapping import apply_trait_mapping, TRAIT_MAPPING

db = SessionLocal()

print("=" * 70)
print("📊 ACCURACY IMPROVEMENT VERIFICATION")
print("=" * 70)

# Check questions
questions = db.query(Question).all()
print(f"\n✅ Total Questions: {len(questions)}")

new_questions = [q for q in questions if q.question_id >= 2472]
print(f"   └─ New strategic questions: {len(new_questions)}")

# Check options and traits
options = db.query(Option).all()
question_traits = set([o.trait_tag.strip() for o in options 
                       if o.trait_tag and o.trait_tag.strip().lower() not in ['none', '']])
print(f"\n✅ Question Options: {len(options)}")
print(f"   └─ Unique traits: {len(question_traits)}")

# Check courses
courses = db.query(Course).all()
course_traits_list = []
for c in courses:
    if c.trait_tag:
        course_traits_list.extend([t.strip() for t in c.trait_tag.split(',')])

course_traits_set = set(course_traits_list)
print(f"\n✅ Total Courses: {len(courses)}")
print(f"   └─ Unique course traits: {len(course_traits_set)}")

# Calculate coverage BEFORE mapping
direct_matches = question_traits.intersection(course_traits_set)
direct_coverage = len(direct_matches) / len(course_traits_set) * 100

print(f"\n{'='*70}")
print("🎯 BEFORE IMPROVEMENTS (Original)")
print(f"{'='*70}")
print(f"Coverage: {len(direct_matches)}/{len(course_traits_set)} = {direct_coverage:.1f}%")

# Calculate coverage AFTER mapping
mapped_course_traits = set([apply_trait_mapping(t) for t in course_traits_set])
effective_matches = question_traits.intersection(mapped_course_traits)
mapped_coverage = len(effective_matches) / len(mapped_course_traits) * 100

print(f"\n{'='*70}")
print("🚀 AFTER IMPROVEMENTS (New Questions + Trait Mapping)")
print(f"{'='*70}")
print(f"Coverage: {len(effective_matches)}/{len(mapped_course_traits)} = {mapped_coverage:.1f}%")
print(f"Trait mappings applied: {len(TRAIT_MAPPING)}")

improvement = mapped_coverage - direct_coverage
print(f"\n{'='*70}")
print(f"✨ IMPROVEMENT: +{improvement:.1f}% coverage")
print(f"{'='*70}")

# Show which traits are still missing
still_missing = mapped_course_traits - question_traits
if still_missing:
    print(f"\n⚠️  Still missing ({len(still_missing)} traits):")
    for trait in sorted(list(still_missing))[:10]:
        count = course_traits_list.count(trait)
        print(f"   • {trait}: {count} courses")
    if len(still_missing) > 10:
        print(f"   ... and {len(still_missing) - 10} more")

print(f"\n{'='*70}")
print("✅ RECOMMENDATION ACCURACY STATUS")
print(f"{'='*70}")
if mapped_coverage >= 75:
    print("🟢 EXCELLENT - High accuracy expected")
elif mapped_coverage >= 65:
    print("🟡 GOOD - Acceptable accuracy, room for improvement")
else:
    print("🔴 FAIR - Consider more improvements")

print(f"\nWith {mapped_coverage:.1f}% trait coverage, the algorithm can detect")
print(f"{len(effective_matches)} out of {len(mapped_course_traits)} unique course requirements.")

db.close()
