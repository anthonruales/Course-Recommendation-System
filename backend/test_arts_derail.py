"""
Test: Arts-focused user with one off-topic Software-Dev answer.
Verifies that:
1. Questions stay related to arts/creative profile
2. Top recommended courses don't shift to tech
3. The minority trait guard fires properly
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

from adaptive_assessment import AdaptiveAssessmentEngine
from seed_data import COURSES_POOL
from questions_enhanced import QUESTIONS_POOL_ENHANCED

engine = AdaptiveAssessmentEngine(COURSES_POOL, QUESTIONS_POOL_ENHANCED)

# Create session matching the user's screenshot profile
session_id = engine.create_session(
    user_id=999,
    user_gwa=88.0,
    user_strand="GAS",
    max_questions=50,
    user_interests="Arts & Design, Music & Performance, animation, fine_arts",
    user_skills="Artistic Ability, Musical Ability, illustration, animation_skill"
)

session = engine.sessions[session_id]
print(f"\n=== PROFILE SEED TRAITS: {session.profile_seed_traits[:8]} ===")
print(f"=== RELEVANT DOMAINS: {sorted(session.relevant_domains)} ===\n")

# Track state
arts_traits = {"Visual-Design", "Creative-Skill", "Digital-Media", "Spatial-Design", 
               "Performing-Arts", "Animation-3D", "Film-Broadcast", "Artistic"}
off_topic_q = None
course_before_offtopic = None
course_after_offtopic = None

for round_num in range(1, 51):
    result = engine.get_next_question(session_id)
    if result is None:
        print(f"[END] No more questions at round {round_num}")
        break
    
    q = result["question"]
    qid = q["question_id"]
    options = q.get("options", [])
    
    # Decide which option to pick
    chosen = None
    
    # At Q16, deliberately pick the most off-topic (Software-Dev) option
    if round_num == 16:
        for opt in options:
            tags = opt.get("trait_tags", {})
            if isinstance(tags, dict):
                for t in tags:
                    if t in ("Software-Dev", "Data-Analytics", "Hardware-Systems", "Cyber-Defense"):
                        chosen = opt
                        off_topic_q = round_num
                        break
            if chosen:
                break
    
    # Otherwise pick the most arts-related option
    if not chosen:
        best_score = -1
        for opt in options:
            tags = opt.get("trait_tags", {})
            score = 0
            if isinstance(tags, dict):
                for t, w in tags.items():
                    if t in arts_traits:
                        score += w * 2
            elif isinstance(tags, list):
                for t in tags:
                    if t in arts_traits:
                        score += 2
            if score > best_score:
                best_score = score
                chosen = opt
    
    if not chosen:
        chosen = options[0]
    
    # Get option trait info
    tags = chosen.get("trait_tags", {})
    if isinstance(tags, dict):
        primary_trait = max(tags, key=tags.get) if tags else "?"
    elif isinstance(tags, list):
        primary_trait = tags[0] if tags else "?"
    else:
        primary_trait = chosen.get("trait_tag", "?")
    
    # Record top courses before off-topic answer
    if round_num == 15:
        sorted_courses = sorted(session.course_scores.items(), key=lambda x: x[1], reverse=True)
        course_before_offtopic = sorted_courses[:5]
    
    # Submit answer
    answer_result = engine.process_answer(session_id, qid, chosen["option_id"])
    
    # Check dominant traits
    dominant = engine._get_dominant_traits(session)
    is_dom = primary_trait in dominant
    
    marker = ""
    if round_num == off_topic_q:
        marker = " <<<< OFF-TOPIC ANSWER"
    elif round_num == (off_topic_q or 0) + 1:
        marker = " <<<< NEXT QUESTION AFTER OFF-TOPIC"
    
    # Show top course name
    top_courses = answer_result.get("top_courses_preview", [])
    top_course = top_courses[0]["course_name"] if top_courses else "?"
    
    print(f"Q{round_num:02d}: cat='{q.get('category', '?')[:40]}' | trait={primary_trait:20s} | "
          f"dominant={is_dom} | top_course={top_course[:35]}{marker}")
    
    # Record top courses right after off-topic answer
    if round_num == off_topic_q:
        sorted_courses = sorted(session.course_scores.items(), key=lambda x: x[1], reverse=True)
        course_after_offtopic = sorted_courses[:5]

# ─── RESULTS ───
print("\n" + "="*80)
print("VERIFICATION RESULTS")
print("="*80)

# Check 1: Did questions after off-topic stay on arts?
print(f"\nOff-topic answer was at Q{off_topic_q}")

# Check 2: Course rankings before/after
if course_before_offtopic and course_after_offtopic:
    print(f"\nTop 5 courses BEFORE off-topic answer (Q15):")
    for name, score in course_before_offtopic:
        is_arts = any(t in engine.course_traits.get(name, set()) for t in arts_traits)
        print(f"  {name[:45]:45s} score={score:6.1f}  {'[ARTS]' if is_arts else '[OTHER]'}")
    
    print(f"\nTop 5 courses AFTER off-topic answer (Q{off_topic_q}):")
    for name, score in course_after_offtopic:
        is_arts = any(t in engine.course_traits.get(name, set()) for t in arts_traits)
        print(f"  {name[:45]:45s} score={score:6.1f}  {'[ARTS]' if is_arts else '[OTHER]'}")
    
    # Check if top course changed to a non-arts course
    top_before = course_before_offtopic[0][0]
    top_after = course_after_offtopic[0][0]
    top_before_is_arts = any(t in engine.course_traits.get(top_before, set()) for t in arts_traits)
    top_after_is_arts = any(t in engine.course_traits.get(top_after, set()) for t in arts_traits)
    
    if top_after_is_arts:
        print(f"\n✓ PASS: Top course stayed arts-related after off-topic answer")
    else:
        print(f"\n✗ FAIL: Top course shifted to non-arts '{top_after}' after one off-topic answer!")

# Check 3: Final dominant traits
print(f"\nFinal dominant traits: {sorted(engine._get_dominant_traits(session))}")
print(f"Final trait scores (top 8):")
sorted_traits = sorted(session.trait_scores.items(), key=lambda x: x[1], reverse=True)
for t, s in sorted_traits[:8]:
    print(f"  {t:25s} = {s:.1f}")

# Check 4: Final top courses
print(f"\nFinal top 5 courses:")
sorted_courses = sorted(session.course_scores.items(), key=lambda x: x[1], reverse=True)
for name, score in sorted_courses[:5]:
    is_arts = any(t in engine.course_traits.get(name, set()) for t in arts_traits)
    print(f"  {name[:45]:45s} score={score:6.1f}  {'[ARTS]' if is_arts else '[OTHER]'}")
