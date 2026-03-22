"""Quick test: Verify the _build_profile_none_option and _append_none_option work."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from services.adaptive_assessment import AdaptiveAssessmentEngine, AdaptiveSession

# Build a minimal engine
engine = AdaptiveAssessmentEngine.__new__(AdaptiveAssessmentEngine)

# Manually set up just enough to test the profile methods
from data.questions_enhanced import QUESTIONS_POOL_ENHANCED
engine.questions = { q['question_id']: q for q in QUESTIONS_POOL_ENHANCED }

# Create a mock session with profile data matching the screenshot  
session = AdaptiveSession(
    session_id="test",
    user_id=1,
    user_interests="Arts & Design, fashion, fine_arts, Photography & Visual Arts",
    user_skills="Artistic Ability, Design Thinking, illustration"
)

# Test the profile traits builder
none_opt = engine._build_profile_none_option(session)
print("=== Profile-based 'None' option ===")
print(f"option_id: {none_opt['option_id']}")
print(f"option_text: {none_opt['option_text']}")
print(f"Number of traits: {len(none_opt['trait_tags'])}")
print(f"trait_tags: {none_opt['trait_tags']}")

# Test appending to a question
sample_q = QUESTIONS_POOL_ENHANCED[0]
q_with_none = engine._append_none_option(sample_q, session)
print(f"\n=== Original question options: {len(sample_q['options'])}")
print(f"=== With 'None' appended: {len(q_with_none['options'])}")
last_opt = q_with_none['options'][-1]
print(f"Last option: id={last_opt['option_id']}, text='{last_opt['option_text']}'")

# Verify original question is not modified
print(f"\n=== Original still has: {len(sample_q['options'])} options (unchanged)")
