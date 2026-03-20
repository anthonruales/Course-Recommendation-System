"""
Test: User with 10 diverse academic interests across multiple domains.
Verifies that domain rotation ensures ALL domains receive questions,
not just the first domain that happened to get follow-up chains.

Expected domains from interests:
  culinary_mgmt -> hospitality
  physics, chemistry, forensic_science -> science
  programming, game_development, it -> technology
  architecture, electrical, industrial -> engineering
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

from adaptive_assessment import AdaptiveAssessmentEngine, QUESTION_TREE_NODES
from seed_data import COURSES_POOL
from questions_enhanced import QUESTIONS_POOL_ENHANCED

engine = AdaptiveAssessmentEngine(COURSES_POOL, QUESTIONS_POOL_ENHANCED)

session_id = engine.create_session(
    user_id=888,
    user_gwa=85.0,
    user_strand="STEM",
    max_questions=30,
    user_interests="Culinary Management, Physics, Chemistry, Forensic Science, Computers & IT, Programming & Coding, Game Development, Architecture & Interior Design, Electrical & Electronics, Industrial & Manufacturing",
    user_skills="Logical Reasoning, Problem-Solving, Computer Literacy, cooking"
)

session = engine.sessions[session_id]
print(f"Domain queue: {session.domain_queue}")
print(f"Relevant domains: {sorted(session.relevant_domains)}")
print(f"Max questions: {session.max_questions}")
print()

domain_questions = {}

for round_num in range(1, 51):
    result = engine.get_next_question(session_id)
    if result is None:
        print(f"\n[END] Assessment complete at round {round_num - 1}")
        break

    q = result["question"]
    qid = q["question_id"]
    options = q.get("options", [])
    node = QUESTION_TREE_NODES.get(qid, {})
    branches = node.get("branches", [])
    domain = branches[0] if branches else "unknown"

    # Track which domains are getting questions
    domain_questions.setdefault(domain, []).append(round_num)

    # Always pick the first option (simulates a user going through quickly)
    chosen = options[0] if options else None
    if chosen:
        engine.process_answer(session_id, qid, chosen["option_id"])

    print(f"  Q{round_num}: [{domain}] {q['question_text'][:70]}")

print(f"\n{'='*60}")
print("DOMAIN DISTRIBUTION:")
print(f"{'='*60}")
for domain, rounds in sorted(domain_questions.items()):
    print(f"  {domain:20s}: {len(rounds):2d} questions  (rounds: {rounds})")

# Verify that at least 3 different domains got questions
domains_with_questions = set(domain_questions.keys())
print(f"\nDomains that received questions: {sorted(domains_with_questions)}")

# The user selected interests across 4 domains: hospitality, science, technology, engineering
expected_domains = {"hospitality", "science", "technology", "engineering"}
covered = expected_domains & domains_with_questions
missing = expected_domains - domains_with_questions

print(f"Expected domains covered: {sorted(covered)}")
if missing:
    print(f"MISSING domains (not explored): {sorted(missing)}")
else:
    print("ALL expected domains received questions!")

# Check no single domain dominates
max_domain = max(domain_questions.items(), key=lambda x: len(x[1]))
print(f"\nMost-questioned domain: {max_domain[0]} ({len(max_domain[1])} questions)")
if len(max_domain[1]) > 12:
    print("WARNING: One domain is dominating the assessment!")
