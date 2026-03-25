"""Broad cross-category duplicate scanner using option-concept overlap"""
import sys, os, re
from collections import defaultdict
from difflib import SequenceMatcher
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data.questions_enhanced import QUESTIONS_POOL_ENHANCED

def get_option_concepts(opts):
    """Extract first 2-3 key words from each option to get the 'concept'"""
    concepts = set()
    for o in opts:
        t = o["option_text"].lower().strip()
        # Extract the booth/activity/concept keyword
        # e.g. "Healthcare booth - explaining..." -> "healthcare"
        # e.g. "Tech booth showcasing..." -> "tech"
        words = re.findall(r'[a-z]+', t)
        if words:
            concepts.add(words[0])  # First significant word
    return concepts

def get_trait_profile(opts):
    """Get the set of primary traits (weight >= 0.8) across all options"""
    traits = set()
    for o in opts:
        tags = o.get("trait_tags", {})
        if isinstance(tags, dict):
            for t, w in tags.items():
                if w >= 0.8:
                    traits.add(t)
        elif isinstance(tags, list):
            traits.update(tags)
        else:
            tag = o.get("trait_tag")
            if tag:
                traits.add(tag)
    return traits

# Pre-compute for all questions
data = []
for q in QUESTIONS_POOL_ENHANCED:
    concepts = get_option_concepts(q["options"])
    traits = get_trait_profile(q["options"])
    words = set(q["question_text"].lower().split())
    data.append((q, concepts, traits, words))

print("Scanning %d questions...\n" % len(data))
pairs = []
for i in range(len(data)):
    qi, ci, ti, wi = data[i]
    for j in range(i+1, len(data)):
        qj, cj, tj, wj = data[j]
        if qi["category"] == qj["category"]:
            continue
        # Fast filter: word overlap >= 60%
        union = len(wi | wj)
        if union == 0:
            continue
        if len(wi & wj) / union < 0.6:
            continue
        # Check trait profile overlap
        if not ti or not tj:
            continue
        trait_overlap = len(ti & tj) / max(len(ti | tj), 1)
        if trait_overlap < 0.5:
            continue
        # Text similarity
        ratio = SequenceMatcher(None, qi["question_text"].lower(), qj["question_text"].lower()).ratio()
        if ratio < 0.75:
            continue
        pairs.append((
            ratio, trait_overlap,
            qi["question_id"], qi["category"], qi["question_text"][:90],
            qj["question_id"], qj["category"], qj["question_text"][:90],
        ))

pairs.sort(key=lambda x: -(x[0] + x[1]))
print("=== CROSS-CATEGORY PAIRS: similar text + overlapping traits ===\n")
for r, to, q1id, q1cat, q1txt, q2id, q2cat, q2txt in pairs:
    print("text=%d%% traits=%d%% | Q%d vs Q%d" % (r*100, to*100, q1id, q2id))
    print("  Q%d [%s] %s" % (q1id, q1cat, q1txt))
    print("  Q%d [%s] %s" % (q2id, q2cat, q2txt))
    print()

print("Total pairs with >=75%% text + >=50%% trait overlap: %d" % len(pairs))
