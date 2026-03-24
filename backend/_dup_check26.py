"""Batch-26 duplicate/rephrase checker – two independent methods."""
import sys, re
sys.path.insert(0, ".")
from data.questions_enhanced import QUESTIONS_POOL_ENHANCED as Q

STOP = {"a","an","the","is","are","was","were","be","been","being","do","does",
        "did","have","has","had","having","will","would","shall","should","may",
        "might","can","could","must","to","of","in","for","on","with","at","by",
        "from","as","into","through","during","before","after","above","below",
        "between","out","off","over","under","again","further","then","once",
        "and","but","or","nor","not","so","yet","both","either","neither",
        "each","every","all","any","few","more","most","other","some","such",
        "no","only","own","same","than","too","very","just","about","up","down",
        "it","its","you","your","he","she","they","them","their","we","our",
        "this","that","these","those","which","what","who","whom","how","if",
        "when","where","while","i","me","my","her","his","him","us"}

NEW_QIDS = set(range(5186, 5206))
NEW_OIDS = set(range(28243, 28363))

def words(t):
    return {w for w in re.findall(r"[a-z0-9]+", t.lower()) if w not in STOP and len(w) > 2}

def trigrams(t):
    t = re.sub(r"[^a-z0-9]", "", t.lower())
    return {t[i:i+3] for i in range(len(t)-2)}

def jaccard(a, b):
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)

new_qs = [q for q in Q if q["question_id"] in NEW_QIDS]
old_qs = [q for q in Q if q["question_id"] not in NEW_QIDS]

print(f"Pool: {len(Q)} | New: {len(new_qs)} | Old: {len(old_qs)}")

# ── METHOD 1 : word-overlap Jaccard ──────────────────────────────────────────
print("\n=== METHOD 1: Word-overlap Jaccard (threshold > 0.70) ===")
m1_q_hits = []
m1_o_hits = []

for nq in new_qs:
    nw = words(nq["question_text"])
    for oq in old_qs:
        ow = words(oq["question_text"])
        j = jaccard(nw, ow)
        if j > 0.70:
            m1_q_hits.append((nq["question_id"], oq["question_id"], round(j,3), nq["question_text"][:80], oq["question_text"][:80]))

for i, nq1 in enumerate(new_qs):
    for nq2 in new_qs[i+1:]:
        j = jaccard(words(nq1["question_text"]), words(nq2["question_text"]))
        if j > 0.70:
            m1_q_hits.append((nq1["question_id"], nq2["question_id"], round(j,3), nq1["question_text"][:80], nq2["question_text"][:80]))

new_opts = [(o, q["question_id"]) for q in new_qs for o in q.get("options",[])]
old_opts = [(o, q["question_id"]) for q in old_qs for o in q.get("options",[])]

for no, nqid in new_opts:
    nw = words(no["option_text"])
    for oo, oqid in old_opts:
        j = jaccard(nw, words(oo["option_text"]))
        if j > 0.70:
            m1_o_hits.append((no["option_id"], oo["option_id"], nqid, oqid, round(j,3), no["option_text"][:70], oo["option_text"][:70]))

for i, (no1, nqid1) in enumerate(new_opts):
    for no2, nqid2 in new_opts[i+1:]:
        j = jaccard(words(no1["option_text"]), words(no2["option_text"]))
        if j > 0.70:
            m1_o_hits.append((no1["option_id"], no2["option_id"], nqid1, nqid2, round(j,3), no1["option_text"][:70], no2["option_text"][:70]))

if m1_q_hits:
    print(f"  WARNING: Question hits: {len(m1_q_hits)}")
    for h in m1_q_hits:
        print(f"    Q{h[0]} vs Q{h[1]} J={h[2]}  |  {h[3]}  <->  {h[4]}")
else:
    print("  PASS: No similar questions found")

if m1_o_hits:
    print(f"  WARNING: Option hits: {len(m1_o_hits)}")
    for h in m1_o_hits[:30]:
        print(f"    O{h[0]} vs O{h[1]} (Q{h[2]}/Q{h[3]}) J={h[4]}  |  {h[5]}  <->  {h[6]}")
    if len(m1_o_hits) > 30:
        print(f"    ... and {len(m1_o_hits)-30} more")
else:
    print("  PASS: No similar options found")

# ── METHOD 2 : character-trigram Jaccard ─────────────────────────────────────
print("\n=== METHOD 2: Character-trigram Jaccard (threshold > 0.65) ===")
m2_q_hits = []
m2_o_hits = []

for nq in new_qs:
    nt = trigrams(nq["question_text"])
    for oq in old_qs:
        j = jaccard(nt, trigrams(oq["question_text"]))
        if j > 0.65:
            m2_q_hits.append((nq["question_id"], oq["question_id"], round(j,3), nq["question_text"][:80], oq["question_text"][:80]))

for i, nq1 in enumerate(new_qs):
    for nq2 in new_qs[i+1:]:
        j = jaccard(trigrams(nq1["question_text"]), trigrams(nq2["question_text"]))
        if j > 0.65:
            m2_q_hits.append((nq1["question_id"], nq2["question_id"], round(j,3), nq1["question_text"][:80], nq2["question_text"][:80]))

for no, nqid in new_opts:
    nt = trigrams(no["option_text"])
    for oo, oqid in old_opts:
        j = jaccard(nt, trigrams(oo["option_text"]))
        if j > 0.65:
            m2_o_hits.append((no["option_id"], oo["option_id"], nqid, oqid, round(j,3), no["option_text"][:70], oo["option_text"][:70]))

for i, (no1, nqid1) in enumerate(new_opts):
    for no2, nqid2 in new_opts[i+1:]:
        j = jaccard(trigrams(no1["option_text"]), trigrams(no2["option_text"]))
        if j > 0.65:
            m2_o_hits.append((no1["option_id"], no2["option_id"], nqid1, nqid2, round(j,3), no1["option_text"][:70], no2["option_text"][:70]))

if m2_q_hits:
    print(f"  WARNING: Question hits: {len(m2_q_hits)}")
    for h in m2_q_hits:
        print(f"    Q{h[0]} vs Q{h[1]} J={h[2]}  |  {h[3]}  <->  {h[4]}")
else:
    print("  PASS: No similar questions found")

if m2_o_hits:
    print(f"  WARNING: Option hits: {len(m2_o_hits)}")
    for h in m2_o_hits[:30]:
        print(f"    O{h[0]} vs O{h[1]} (Q{h[2]}/Q{h[3]}) J={h[4]}  |  {h[5]}  <->  {h[6]}")
    if len(m2_o_hits) > 30:
        print(f"    ... and {len(m2_o_hits)-30} more")
else:
    print("  PASS: No similar options found")

print("\n=== SUMMARY ===")
total_flags = len(m1_q_hits) + len(m1_o_hits) + len(m2_q_hits) + len(m2_o_hits)
print(f"  Method 1 flags: {len(m1_q_hits)} questions, {len(m1_o_hits)} options")
print(f"  Method 2 flags: {len(m2_q_hits)} questions, {len(m2_o_hits)} options")
print(f"  Total flags: {total_flags}")
if total_flags == 0:
    print("  BATCH 26 PASSED BOTH CHECKS — no duplicates or rephrases detected")
else:
    print("  Review flagged items above")
