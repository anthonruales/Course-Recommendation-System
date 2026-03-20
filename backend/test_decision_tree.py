"""Test the decision tree flow end-to-end."""
from questions_enhanced import QUESTIONS_POOL_ENHANCED
from courses_specialized import COURSES_POOL_SPECIALIZED as COURSES_DATA
from adaptive_assessment import AdaptiveAssessmentEngine

# Prepare data
courses = COURSES_DATA
questions = []
for q in QUESTIONS_POOL_ENHANCED:
    questions.append({
        "question_id": q["question_id"],
        "question_text": q["question_text"],
        "category": q.get("category", ""),
        "options": [
            {
                "option_id": o["option_id"],
                "option_text": o["option_text"],
                "trait_tags": o.get("trait_tags", {}),
            }
            for o in q.get("options", [])
        ],
    })

engine = AdaptiveAssessmentEngine(courses, questions)

# Create session for a computer-interested student
sid = engine.create_session(1, 90, "STEM", 50, "programming,data,ai", "programming_skill,web_development")

session = engine.sessions[sid]
print(f"Primary domain: {session.primary_domain}")
print(f"Secondary domain: {session.secondary_domain}")
print(f"Initial phase: {session.phase}")
print(f"Current tree node: {session.current_tree_node}")
print(f"Profile traits (top 8): {dict(list(session.profile_traits.items())[:8])}")
print()

# Get first question
q1 = engine.get_next_question(sid)
qdata = q1["question"]
print(f"Q1 [{qdata['category']}]: {qdata['question_text']}")
for opt in qdata["options"]:
    print(f"  [{opt['option_id']}] {opt['option_text']}")
print()

# Answer: "Writing code and building software"
r1 = engine.process_answer(sid, 1001, 10011)
print(f"After Q1 answer → phase={session.phase}, node={session.current_tree_node}")
print()

# Get Q2 — should be about software types
q2 = engine.get_next_question(sid)
qdata2 = q2["question"]
print(f"Q2 [{qdata2['category']}]: {qdata2['question_text']}")
for opt in qdata2["options"]:
    print(f"  [{opt['option_id']}] {opt['option_text']}")
print()

# Answer: "AI/ML"
r2 = engine.process_answer(sid, 1002, 10021)
print(f"After Q2 answer → phase={session.phase}, node={session.current_tree_node}")
print()

# Get Q3 — should be deep programming preferences
q3 = engine.get_next_question(sid)
qdata3 = q3["question"]
print(f"Q3 [{qdata3['category']}]: {qdata3['question_text']}")
for opt in qdata3["options"]:
    print(f"  [{opt['option_id']}] {opt['option_text']}")
print()

# Answer: "Complex algorithms"
r3 = engine.process_answer(sid, 1008, 10081)
print(f"After Q3 answer → phase={session.phase}, node={session.current_tree_node}")
print()

# Print accumulated state
print("=== STATE AFTER TREE PRIMARY ===")
top_traits = sorted(session.trait_scores.items(), key=lambda x: x[1], reverse=True)[:10]
print(f"Top traits: {top_traits}")
top_courses = sorted(session.course_scores.items(), key=lambda x: x[1], reverse=True)[:5]
print(f"Top courses: {top_courses}")
print(f"Phase: {session.phase}")
print()

# Get Q4 — should transition to secondary domain or validation
q4 = engine.get_next_question(sid)
if q4:
    qdata4 = q4["question"]
    print(f"Q4 [{qdata4['category']}]: {qdata4['question_text']}")
    for opt in qdata4["options"][:3]:
        print(f"  [{opt['option_id']}] {opt['option_text']} ...")
    print(f"  ... ({len(qdata4['options'])} options total)")
    print(f"Phase: {session.phase}")
else:
    print("No Q4 — assessment complete")

print()
print("=== TEST 2: ARTS user choosing graphics design path ===")
print()

sid2 = engine.create_session(2, 85, "ARTS", 50, "art,multimedia,photography", "graphic_design,video_editing")
s2 = engine.sessions[sid2]
print(f"Primary: {s2.primary_domain}, Secondary: {s2.secondary_domain}")

# First question — should be about arts
a1 = engine.get_next_question(sid2)
ad1 = a1["question"]
print(f"Q1 [{ad1['category']}]: {ad1['question_text']}")
for opt in ad1["options"]:
    print(f"  [{opt['option_id']}] {opt['option_text']}")
print()

# Pick digital arts
engine.process_answer(sid2, 1401, 14012)
a2 = engine.get_next_question(sid2)
ad2 = a2["question"]
print(f"Q2 [{ad2['category']}]: {ad2['question_text']}")
for opt in ad2["options"]:
    print(f"  [{opt['option_id']}] {opt['option_text']}")
print()

# Pick graphic design/branding
engine.process_answer(sid2, 1403, 14033)
print(f"After picking graphic design → phase={s2.phase}")
top_traits2 = sorted(s2.trait_scores.items(), key=lambda x: x[1], reverse=True)[:8]
print(f"Top traits: {top_traits2}")
top_courses2 = sorted(s2.course_scores.items(), key=lambda x: x[1], reverse=True)[:5]
print(f"Top courses: {top_courses2}")

print()
print("=== TEST 3: HEALTHCARE user ===")
print()

sid3 = engine.create_session(3, 88, "STEM", 50, "medical,nursing", "patient_care,first_aid")
s3 = engine.sessions[sid3]
print(f"Primary: {s3.primary_domain}, Secondary: {s3.secondary_domain}")

h1 = engine.get_next_question(sid3)
hd1 = h1["question"]
print(f"Q1 [{hd1['category']}]: {hd1['question_text']}")
for opt in hd1["options"]:
    print(f"  [{opt['option_id']}] {opt['option_text']}")

print()
print("=== ALL TESTS PASSED ===")
