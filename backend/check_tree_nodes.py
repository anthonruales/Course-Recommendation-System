"""Verify batch questions are now registered in QUESTION_TREE_NODES."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from data.questions_enhanced import QUESTIONS_POOL_ENHANCED as ENHANCED_QUESTIONS
from services.adaptive_assessment import QUESTION_TREE_NODES, TRAIT_FOLLOWUP_MAP, DOMAIN_ENTRY_QUESTIONS

q_by_id = {q['question_id']: q for q in ENHANCED_QUESTIONS}
qids = sorted(q_by_id.keys())

missing = [qid for qid in qids if qid not in QUESTION_TREE_NODES]
print(f"Total questions: {len(ENHANCED_QUESTIONS)}")
print(f"Total in QUESTION_TREE_NODES: {len(QUESTION_TREE_NODES)}")
print(f"Questions NOT in QUESTION_TREE_NODES: {len(missing)}")
if missing:
    print(f"  Still missing QIDs (first 20): {missing[:20]}")

# Check TRAIT_FOLLOWUP_MAP coverage
all_followup_qids = set()
for trait, fq_list in TRAIT_FOLLOWUP_MAP.items():
    all_followup_qids.update(fq_list)

in_followup = [qid for qid in qids if qid in all_followup_qids]
print(f"\nQuestions in TRAIT_FOLLOWUP_MAP: {len(in_followup)} / {len(qids)}")

# Check domain entry coverage
all_entry_qids = set()
for domain, eq_list in DOMAIN_ENTRY_QUESTIONS.items():
    all_entry_qids.update(eq_list)
in_entry = [qid for qid in qids if qid in all_entry_qids]
print(f"Questions in DOMAIN_ENTRY_QUESTIONS: {len(in_entry)} / {len(qids)}")

# Spot check: batch 30/31 questions (QIDs 5266-5305)
batch_qids = [qid for qid in qids if 5266 <= qid <= 5305]
batch_in_tree = [qid for qid in batch_qids if qid in QUESTION_TREE_NODES]
batch_in_followup = [qid for qid in batch_qids if qid in all_followup_qids]
print(f"\nBatch 30-31 (Q5266-Q5305): {len(batch_qids)} questions")
print(f"  In QUESTION_TREE_NODES: {len(batch_in_tree)}")
print(f"  In TRAIT_FOLLOWUP_MAP: {len(batch_in_followup)}")

# Show branch assignment for batch 31 sample
for qid in [5286, 5290, 5295, 5300, 5305]:
    if qid in QUESTION_TREE_NODES:
        print(f"  Q{qid} branches: {QUESTION_TREE_NODES[qid]['branches']}")
    else:
        print(f"  Q{qid}: NOT REGISTERED")


