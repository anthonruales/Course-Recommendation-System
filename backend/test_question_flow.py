"""Test script to trace question selection for a programming-interested user."""
import os
import sys
os.environ["DATABASE_URL"] = "sqlite:///./test_temp.db"
sys.path.insert(0, '.')

from services.adaptive_assessment import (
    TRAIT_FOLLOWUP_MAP, DOMAIN_ENTRY_QUESTIONS, QUESTION_TREE_NODES
)
from data.questions_enhanced import QUESTIONS_POOL_ENHANCED
from data.decision_tree_questions import DECISION_TREE_QUESTIONS

# Simulate engine initialization with dedup (same as main.py)
tree_qids = set(q['question_id'] for q in DECISION_TREE_QUESTIONS)

def _trait_fp(q):
    traits = set()
    for opt in q.get('options', []):
        tt = opt.get('trait_tags', {})
        if isinstance(tt, dict):
            for t, w in tt.items():
                if w >= 0.8:
                    traits.add(t)
    return tuple(sorted(traits))

all_q = QUESTIONS_POOL_ENHANCED + DECISION_TREE_QUESTIONS
unique_ids = set()
deduped = []
for q in all_q:
    qid = q['question_id']
    if qid in unique_ids:
        continue
    unique_ids.add(qid)
    deduped.append(q)

seen_fps = {}
final = []
for q in deduped:
    qid = q['question_id']
    if qid in tree_qids or qid <= 57:
        final.append(q)
        continue
    fp = _trait_fp(q)
    if not fp:
        final.append(q)
        continue
    cat = q.get('category', '')
    key = (fp, cat)
    if key not in seen_fps:
        seen_fps[key] = qid
        final.append(q)

engine_qids = set(q['question_id'] for q in final)
q_by_id = {q['question_id']: q for q in final}
print(f"Engine has {len(engine_qids)} questions")

# Build profile_relevant_qids for programming
profile_cats = {"Programming & Coding", "Software Engineering", "Computers & IT"}

def _normalize(cat):
    return cat.replace("Academic Interest -", "").strip().replace("\u2014", "-")

def _tokenize(v):
    c = v.replace("&", " ").replace("/", " ").replace("-", " ").replace("(", " ").replace(")", " ")
    return set(t for t in c.split() if t)

def _score(cat, kw):
    nc = _normalize(cat).lower()
    nk = _normalize(kw).lower()
    if not nc or not nk:
        return 0
    ct = _tokenize(nc)
    kt = _tokenize(nk)
    if not ct or not kt:
        return 0
    if kt.issubset(ct):
        return len(kt)
    return 0

profile_relevant_qids = set()
for q in final:
    qid = q['question_id']
    cat = q.get('category', '')
    best = max((_score(cat, kw) for kw in profile_cats), default=0)
    if best >= 2:
        profile_relevant_qids.add(qid)

print(f"Profile-relevant QIDs: {len(profile_relevant_qids)}")
print(f"Profile QIDs: {sorted(profile_relevant_qids)}")

# Check technology domain entry questions that are in engine AND profile
tech_entry = DOMAIN_ENTRY_QUESTIONS.get("technology", [])
profile_entry = [q for q in tech_entry if q in profile_relevant_qids and q in engine_qids]
print(f"Profile-matching tech entry questions: {profile_entry}")

non_profile_entry = [q for q in tech_entry if q in engine_qids and q not in profile_relevant_qids]
print(f"Non-profile tech entry questions: {non_profile_entry[:10]}")

# Show the first 5 chain queue candidates
for qid in profile_entry[:5]:
    q = q_by_id.get(qid)
    if q:
        print(f"  Chain Q{qid}: [{q.get('category', '')}] {q.get('question_text', '')[:70]}")

# Check what Software-Dev follow-ups are in profile pool AND in engine
sd_followups = TRAIT_FOLLOWUP_MAP.get("Software-Dev", [])
profile_sd = [fq for fq in sd_followups if fq in profile_relevant_qids and fq in engine_qids]
print(f"\nSoftware-Dev follow-ups in profile pool: {profile_sd}")

# Also check: are QIDs like 809, 810 etc in engine?
for qid in [809, 810, 811, 812, 828, 829]:
    in_engine = qid in engine_qids
    in_profile = qid in profile_relevant_qids
    q = q_by_id.get(qid)
    cat = q.get("category", "") if q else "NOT IN ENGINE"
    print(f"  QID {qid}: engine={in_engine}, profile={in_profile}, cat={cat}")

print("\n--- Checking if QID 1 can be reached ---")
print(f"QID 1 in engine: {1 in engine_qids}")
print(f"QID 1 in profile_qids: {1 in profile_relevant_qids}")
print(f"QID 1 category: {q_by_id[1].get('category', '')}")
# Check if it passes _is_relevant_question (branches & relevant overlap)
node = QUESTION_TREE_NODES.get(1)
print(f"QID 1 tree node: {node}")
# For tech domain, relevant_domains would include 'technology'
if node:
    branches = set(node.get("branches", []))
    relevant = {"technology"}
    print(f"QID 1 branches & relevant: {branches & relevant}")
