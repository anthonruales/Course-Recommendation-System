"""Quick test to verify trait continuity in question selection."""
import adaptive_assessment as aa
from questions_enhanced import QUESTIONS_POOL_ENHANCED
from seed_data import COURSES_POOL

courses = [
    {
        'course_name': c['course_name'],
        'trait_tag': c.get('trait_tag', ''),
        'minimum_gwa': c.get('minimum_gwa', 0),
        'required_strand': c.get('required_strand', '')
    }
    for c in COURSES_POOL
]
engine = aa.AdaptiveAssessmentEngine(courses, QUESTIONS_POOL_ENHANCED)

# Create session with healthcare profile
sid = engine.create_session(
    user_id=1, user_gwa=90.0, user_strand='STEM',
    max_questions=50,
    user_interests='nursing,medical',
    user_skills='patient_care,empathy'
)

session = engine.sessions[sid]
print(f"\nProfile seed traits: {session.profile_seed_traits[:10]}")
print(f"Relevant domains: {sorted(session.relevant_domains)}")

# Get all 50 questions and check trait continuity
print("\n=== QUESTION FLOW (all 50) ===")
accumulated_traits = set(session.profile_seed_traits)
connected_count = 0
total_questions = 0

for i in range(50):
    q = engine.get_next_question(sid)
    if not q:
        print(f"  Assessment ended at round {i+1}")
        break
    qdata = q['question']
    qid = qdata['question_id']
    total_questions += 1
    
    # Get all traits from this question's options
    option_traits = set()
    for opt in qdata.get('options', []):
        tt = opt.get('trait_tags', {})
        if isinstance(tt, dict):
            option_traits.update(tt.keys())
        elif isinstance(tt, list):
            option_traits.update(tt)
        else:
            t = opt.get('trait_tag')
            if t:
                option_traits.add(t)
    
    # Check overlap with accumulated traits (including adjacent traits)
    expanded = set(accumulated_traits)
    for t in accumulated_traits:
        from adaptive_assessment import TOPIC_ADJACENCY
        expanded.update(TOPIC_ADJACENCY.get(t, []))
    
    overlap = option_traits & expanded
    has_continuity = len(overlap) > 0
    if has_continuity:
        connected_count += 1
    
    cat = qdata.get('category', '?')
    status = "CONNECTED" if has_continuity else "NO OVERLAP"
    if not has_continuity:
        print(f"  Round {i+1}: Q{qid} [{cat}] — {status} *** MISSING ***")
        print(f"    Q traits: {sorted(option_traits)[:6]}")
    
    # Pick first option (simulate answer)
    first_opt = qdata['options'][0]
    result = engine.process_answer(sid, qid, first_opt['option_id'])
    
    # Update accumulated traits
    trait = result.get('trait_recorded')
    if trait:
        accumulated_traits.add(trait)
    all_traits = result.get('all_traits', [])
    accumulated_traits.update(all_traits)

print(f"\n=== RESULTS ===")
print(f"Total questions asked: {total_questions}")
print(f"Connected questions: {connected_count}/{total_questions} ({connected_count/total_questions*100:.0f}%)")
print(f"Total unique traits: {len(session.trait_scores)}")
print(f"Top traits: {sorted(session.trait_scores.items(), key=lambda x: x[1], reverse=True)[:8]}")
print("\nTest completed successfully!")
