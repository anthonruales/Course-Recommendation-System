"""
Test: Force a truly off-topic answer (Data-Analytics) on an art-focused user
and verify the system doesn't derail.
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

sid = engine.create_session(
    user_id=1, user_gwa=90.0, user_strand='ARTS',
    max_questions=50,
    user_interests='art,architecture,photography',
    user_skills='graphic_design,creativity,design_thinking'
)

session = engine.sessions[sid]

# Build 15 questions of Visual-Design dominance
print("=== BUILDING VISUAL-DESIGN DOMINANCE ===")
for i in range(15):
    q = engine.get_next_question(sid)
    if not q:
        break
    qdata = q['question']
    qid = qdata['question_id']
    
    # Always pick option with Visual-Design/Creative-Skill
    best_opt = None
    best_score = -999
    for opt in qdata.get('options', []):
        tt = opt.get('trait_tags', {})
        score = 0
        if isinstance(tt, dict):
            for trait, w in tt.items():
                if trait in ('Visual-Design', 'Spatial-Design', 'Creative-Skill', 'Artistic'):
                    score += w * 10
                elif trait in ('Data-Analytics', 'Software-Dev', 'Finance-Acct'):
                    score -= w * 5  # Avoid these
        if score > best_score:
            best_score = score
            best_opt = opt
    
    if not best_opt:
        best_opt = qdata['options'][0]
    engine.process_answer(sid, qid, best_opt['option_id'])

dominant_before = engine._get_dominant_traits(session)
print(f"Dominant traits: {sorted(dominant_before)}")
print(f"Top scores: {sorted(session.trait_scores.items(), key=lambda x: x[1], reverse=True)[:5]}")

# Now MANUALLY inject a Data-Analytics answer to simulate getting the math question
# and choosing "Excellent" which maps to Data-Analytics
print("\n=== SIMULATING OFF-TOPIC ANSWER (Data-Analytics from math question) ===")
q16 = engine.get_next_question(sid)
q16data = q16['question']
q16id = q16data['question_id']

# Find option with Data-Analytics or non-design trait
off_topic_opt = None
for opt in q16data.get('options', []):
    tt = opt.get('trait_tags', {})
    if isinstance(tt, dict):
        primary = max(tt, key=tt.get) if tt else None
        if primary and primary not in dominant_before:
            off_topic_opt = opt
            break

if not off_topic_opt:
    # Just pick the first option
    off_topic_opt = q16data['options'][0]

off_trait_tags = off_topic_opt.get('trait_tags', {})
primary_trait = max(off_trait_tags, key=off_trait_tags.get) if isinstance(off_trait_tags, dict) and off_trait_tags else 'unknown'
print(f"Q16: [{q16data.get('category','')}] picking option with primary trait: {primary_trait}")
print(f"  Is '{primary_trait}' dominant? {engine._is_dominant_trait(primary_trait, session)}")

result = engine.process_answer(sid, q16id, off_topic_opt['option_id'])
print(f"  Recorded trait: {result.get('trait_recorded')}")

# THE KEY CHECK: What does Q17 look like?
q17 = engine.get_next_question(sid)
if q17:
    q17data = q17['question']
    q17_traits = set()
    for opt in q17data.get('options', []):
        tt = opt.get('trait_tags', {})
        if isinstance(tt, dict):
            q17_traits.update(tt.keys())
    
    has_dominant = engine._has_dominant_trait_overlap(q17data, session)
    dominant_overlap = q17_traits & dominant_before
    
    print(f"\nQ17: [{q17data.get('category','')}]")
    print(f"  Has dominant trait overlap: {has_dominant}")
    print(f"  Overlapping dominant traits: {sorted(dominant_overlap)}")
    
    if has_dominant:
        print("\n  PASS: System did NOT derail after off-topic answer!")
    else:
        print("\n  FAIL: System derailed after off-topic answer!")

    # Verify next 5 questions also stay on track
    engine.process_answer(sid, q17data['question_id'], q17data['options'][0]['option_id'])
    
    print("\n=== QUESTIONS 18-22 ===")
    all_ok = True
    for i in range(18, 23):
        q = engine.get_next_question(sid)
        if not q:
            break
        qdata = q['question']
        has_dom = engine._has_dominant_trait_overlap(qdata, session)
        status = "OK" if has_dom else "DRIFT!"
        if not has_dom:
            all_ok = False
        print(f"  Q{i}: [{qdata.get('category','')}] dominant_overlap={has_dom} [{status}]")
        engine.process_answer(sid, qdata['question_id'], qdata['options'][0]['option_id'])
    
    print(f"\n{'ALL PASS' if all_ok else 'SOME DRIFTED'}: continuity maintained = {all_ok}")
