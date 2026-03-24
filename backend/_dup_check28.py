"""Batch 28 duplicate / rephrase checker — two independent methods."""
import re, sys
sys.path.insert(0, ".")
from data.questions_enhanced import QUESTIONS_POOL_ENHANCED as P

BATCH_IDS = set(range(5226, 5246))
batch = [q for q in P if q["question_id"] in BATCH_IDS]
rest  = [q for q in P if q["question_id"] not in BATCH_IDS]

def tokenize(text):
    return set(re.findall(r"[a-z0-9]+", text.lower()))

def jaccard(a, b):
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)

def char_trigrams(text):
    t = re.sub(r"[^a-z0-9 ]", "", text.lower())
    return {t[i:i+3] for i in range(len(t)-2)}

def tri_jaccard(a, b):
    sa, sb = char_trigrams(a), char_trigrams(b)
    if not sa or not sb:
        return 0.0
    return len(sa & sb) / len(sa | sb)

# ── METHOD 1: word-overlap Jaccard ──
print("=== METHOD 1: Word-overlap Jaccard (threshold 0.70) ===")
flags1 = 0
for bq in batch:
    bt = tokenize(bq["question_text"])
    for rq in rest:
        rt = tokenize(rq["question_text"])
        j = jaccard(bt, rt)
        if j > 0.70:
            print(f"  Q-FLAG  {bq['question_id']} vs {rq['question_id']}  J={j:.3f}")
            flags1 += 1
    b_opts = [(o["option_id"], tokenize(o["option_text"])) for o in bq["options"]]
    for rq in rest:
        for ro in rq["options"]:
            rt2 = tokenize(ro["option_text"])
            for oid, bt2 in b_opts:
                j2 = jaccard(bt2, rt2)
                if j2 > 0.70:
                    print(f"  O-FLAG  opt {oid} vs opt {ro['option_id']}  J={j2:.3f}")
                    flags1 += 1
print(f"Method 1 total flags: {flags1}")

# ── METHOD 2: character-trigram Jaccard ──
print("=== METHOD 2: Character-trigram Jaccard (threshold 0.65) ===")
flags2 = 0
for bq in batch:
    for rq in rest:
        j = tri_jaccard(bq["question_text"], rq["question_text"])
        if j > 0.65:
            print(f"  Q-FLAG  {bq['question_id']} vs {rq['question_id']}  triJ={j:.3f}")
            flags2 += 1
    for bo in bq["options"]:
        for rq in rest:
            for ro in rq["options"]:
                j2 = tri_jaccard(bo["option_text"], ro["option_text"])
                if j2 > 0.65:
                    print(f"  O-FLAG  opt {bo['option_id']} vs opt {ro['option_id']}  triJ={j2:.3f}")
                    flags2 += 1
print(f"Method 2 total flags: {flags2}")

if flags1 == 0 and flags2 == 0:
    print("\nBATCH 28 PASSED BOTH CHECKS — no duplicates or rephrases detected")
else:
    print(f"\nBATCH 28 NEEDS REVIEW — {flags1 + flags2} total flags")
