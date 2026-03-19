"""Quick test to verify traits_discovered and all_traits after answering Q1"""
from adaptive_assessment import AdaptiveAssessmentEngine
from questions_enhanced import QUESTIONS_POOL_ENHANCED
from courses_specialized import COURSES_POOL_SPECIALIZED

engine = AdaptiveAssessmentEngine(COURSES_POOL_SPECIALIZED, QUESTIONS_POOL_ENHANCED)
session_id = engine.create_session(
    user_id=1, user_gwa=90, user_strand='HUMSS', max_questions=50,
    user_interests='art,music,writing,photography,animation',
    user_skills='creativity,artistic,music_skill'
)

q1 = engine.get_next_question(session_id)
q = q1['question']
print(f"Q1: {q['question_text'][:80]}")
print(f"Q1 category: {q['category']}")
print(f"Q1 ID: {q['question_id']}")

# Pick the first non-none option
option = q['options'][0]
print(f"\nAnswering: {option['option_text']}")
print(f"Option trait_tags: {list(option.get('trait_tags', {}).keys())}")

result = engine.process_answer(session_id, q['question_id'], option['option_id'])
print(f"\n=== RESULTS ===")
print(f"traits_discovered: {result['traits_discovered']}")
print(f"all_traits type: {type(result['all_traits']).__name__}")
print(f"all_traits: {result['all_traits']}")
print(f"trait_recorded: {result['trait_recorded']}")

session = engine.sessions[session_id]
print(f"\nsession.trait_scores keys ({len(session.trait_scores)}): {list(session.trait_scores.keys())}")
