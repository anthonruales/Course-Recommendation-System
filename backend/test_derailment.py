"""
Test: Verify that a single off-topic answer doesn't derail the question chain.

Scenario: User with art/design profile consistently picks Visual-Design/Spatial-Design
options for 15 questions, then rates math as "Excellent" (which maps to Data-Analytics).
The NEXT question should still be connected to Visual-Design/Spatial-Design, NOT
pivot entirely to Data-Analytics.
"""
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

# Create session with ARTS profile
sid = engine.create_session(
    user_id=1, user_gwa=90.0, user_strand='ARTS',
    max_questions=50,
    user_interests='art,architecture,photography',
    user_skills='graphic_design,creativity,design_thinking'
)

session = engine.sessions[sid]
print(f"Profile seed traits: {session.profile_seed_traits[:8]}")
print(f"Relevant domains: {sorted(session.relevant_domains)}")

# Simulate picking art/design-related options for first 15 questions
print("\n=== BUILDING VISUAL-DESIGN DOMINANCE (15 questions) ===")
for i in range(15):
    q = engine.get_next_question(sid)
    if not q:
        print(f"No more questions at round {i+1}")
        break
    qdata = q['question']
    qid = qdata['question_id']
    
    # Pick the option with Visual-Design, Spatial-Design, or Creative-Skill trait
    best_opt = None
    best_score = -1
    for opt in qdata.get('options', []):
        tt = opt.get('trait_tags', {})
        score = 0
        if isinstance(tt, dict):
            for trait, w in tt.items():
                if trait in ('Visual-Design', 'Spatial-Design', 'Creative-Skill', 'Artistic', 'Digital-Media'):
                    score += w * 10
        if score > best_score:
            best_score = score
            best_opt = opt
    
    if not best_opt:
        best_opt = qdata['options'][0]
    
    result = engine.process_answer(sid, qid, best_opt['option_id'])
    trait = result.get('trait_recorded', '?')
    cat = qdata.get('category', '?')
    print(f"  Q{i+1}: [{cat}] -> trait: {trait}")

# Show dominant traits after 15 questions
dominant = engine._get_dominant_traits(session)
print(f"\nDominant traits after 15 Qs: {sorted(dominant)}")
print(f"Trait scores: {sorted(session.trait_scores.items(), key=lambda x: x[1], reverse=True)[:8]}")

# Now get question 16
q16 = engine.get_next_question(sid)
if q16:
    q16data = q16['question']
    q16id = q16data['question_id']
    cat = q16data.get('category', '?')
    print(f"\n=== QUESTION 16: Q{q16id} [{cat}] ===")
    
    # Find the "Excellent math" / Data-Analytics option if available
    # Or just pick the first option that has Data-Analytics/non-design trait
    off_topic_opt = None
    for opt in q16data.get('options', []):
        tt = opt.get('trait_tags', {})
        if isinstance(tt, dict):
            if 'Data-Analytics' in tt or 'Software-Dev' in tt or 'Finance-Acct' in tt:
                off_topic_opt = opt
                break
    
    if not off_topic_opt:
        off_topic_opt = q16data['options'][0]
    
    # Simulate picking the off-topic option (like "Excellent math")
    off_trait_tags = off_topic_opt.get('trait_tags', {})
    print(f"  Picking OFF-TOPIC option: '{off_topic_opt.get('option_text', '')[:60]}...'")
    print(f"  Option traits: {off_trait_tags}")
    
    result16 = engine.process_answer(sid, q16id, off_topic_opt['option_id'])
    last_trait = result16.get('trait_recorded', '?')
    print(f"  Recorded trait: {last_trait}")
    print(f"  Is dominant? {engine._is_dominant_trait(last_trait, session)}")

# THE KEY TEST: Question 17 should still be connected to Visual-Design/Spatial-Design
q17 = engine.get_next_question(sid)
if q17:
    q17data = q17['question']
    q17id = q17data['question_id']
    cat = q17data.get('category', '?')
    
    # Get all traits in Q17 options
    q17_traits = set()
    for opt in q17data.get('options', []):
        tt = opt.get('trait_tags', {})
        if isinstance(tt, dict):
            q17_traits.update(tt.keys())
        elif isinstance(tt, list):
            q17_traits.update(tt)
    
    has_design_trait = bool(q17_traits & {'Visual-Design', 'Spatial-Design', 'Creative-Skill', 'Artistic', 'Digital-Media'})
    has_dominant_overlap = engine._has_dominant_trait_overlap(q17data, session)
    
    print(f"\n=== QUESTION 17: Q{q17id} [{cat}] ===")
    print(f"  Q17 traits: {sorted(q17_traits)[:10]}")
    print(f"  Has design/art trait in options: {has_design_trait}")
    print(f"  Has dominant trait overlap: {has_dominant_overlap}")
    
    if has_design_trait or has_dominant_overlap:
        print("\n  PASS: Question 17 is connected to the user's dominant design pattern!")
    else:
        print("\n  FAIL: Question 17 is NOT connected to the user's design pattern!")

# Continue for a few more to verify no derailment
print("\n=== QUESTIONS 18-22 (checking continuity) ===")
# Answer Q17 first
if q17:
    engine.process_answer(sid, q17data['question_id'], q17data['options'][0]['option_id'])

for i in range(18, 23):
    q = engine.get_next_question(sid)
    if not q:
        break
    qdata = q['question']
    qid = qdata['question_id']
    q_traits = set()
    for opt in qdata.get('options', []):
        tt = opt.get('trait_tags', {})
        if isinstance(tt, dict):
            q_traits.update(tt.keys())
    
    has_dominant = engine._has_dominant_trait_overlap(qdata, session)
    cat = qdata.get('category', '?')
    status = "OK" if has_dominant else "DRIFT"
    print(f"  Q{i}: [{cat}] dominant_overlap={has_dominant} [{status}]")
    
    # Pick first option
    engine.process_answer(sid, qid, qdata['options'][0]['option_id'])

print("\nTest completed!")
