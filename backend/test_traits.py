from seed_data import COURSES_POOL

print(f"✓ Successfully loaded {len(COURSES_POOL)} courses")
avg_traits = sum(len(c['trait_tag']) for c in COURSES_POOL) / len(COURSES_POOL)
print(f"✓ Average traits per course: {avg_traits:.1f}")

traits = set()
for c in COURSES_POOL:
    traits.update(c['trait_tag'])
print(f"✓ Total unique traits: {len(traits)}")

print("\n📊 Trait Categories:")
personality = [t for t in traits if t in ['Independent', 'Extroverted', 'Introverted', 'Collaborative', 'Detail-focused', 'Big-picture']]
learning = [t for t in traits if t in ['Hands-on', 'Theoretical', 'Visual-learner', 'Research-oriented']]
work_env = [t for t in traits if 'work' in t.lower() or 'office' in t.lower() or 'laboratory' in t.lower() or 'studio' in t.lower() or 'clinical' in t.lower()]
activity = [t for t in traits if t in ['Problem-solving', 'Creative-expression', 'Helping-others', 'Leading-teams']]

print(f"  - Personality traits: {len(personality)}")
print(f"  - Learning style traits: {len(learning)}")
print(f"  - Work environment traits: {len(work_env)}")
print(f"  - Core activity traits: {len(activity)}")

print("\n🔍 Sample comparisons:")
cs = [c for c in COURSES_POOL if c['course_name'] == 'BS Computer Science'][0]
nursing = [c for c in COURSES_POOL if c['course_name'] == 'BS Nursing'][0]
print(f"\nBS Computer Science traits ({len(cs['trait_tag'])}):")
print(f"  {', '.join(cs['trait_tag'][:5])}...")
print(f"\nBS Nursing traits ({len(nursing['trait_tag'])}):")
print(f"  {', '.join(nursing['trait_tag'][:5])}...")
