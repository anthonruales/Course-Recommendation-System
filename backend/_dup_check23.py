import sys, re
sys.path.insert(0, r"C:\Users\USer\Downloads\capstone-back-end\Course-Recommendation-System\backend")
from data.questions_enhanced import QUESTIONS_POOL_ENHANCED

STOP = {'a','an','the','is','are','was','were','do','does','did','will','would','could','should','can','may','might',
        'of','in','on','at','to','for','with','by','from','as','into','through','about','between','after','before',
        'and','or','but','not','no','nor','so','yet','both','either','neither','if','then','than','that','this',
        'it','its','you','your','they','their','them','he','she','his','her','him','we','our','us','my','me',
        'who','whom','which','what','when','where','how','why','be','been','being','have','has','had','having',
        'most','more','very','just','also','only','even','still','already','each','every','all','any','some','such',
        'new','one','two','three','four','five','six'}

def words(t):
    return {w for w in re.findall(r'[a-z]+', t.lower()) if w not in STOP and len(w) > 2}

def trigrams(t):
    t = re.sub(r'[^a-z]', '', t.lower())
    return {t[i:i+3] for i in range(len(t)-2)}

def jaccard(a, b):
    if not a or not b:
        return 0
    return len(a & b) / len(a | b)

batch23_ids = set(range(5126, 5146))
batch_qs = [q for q in QUESTIONS_POOL_ENHANCED if q["question_id"] in batch23_ids]
other_qs = [q for q in QUESTIONS_POOL_ENHANCED if q["question_id"] not in batch23_ids]

print("=== METHOD 1: Word-overlap Jaccard (threshold > 0.7) ===")
hits1 = 0
for bq in batch_qs:
    bw = words(bq["question_text"])
    for oq in other_qs:
        ow = words(oq["question_text"])
        j = jaccard(bw, ow)
        if j > 0.7:
            hits1 += 1
            print(f"  Q{bq['question_id']} vs Q{oq['question_id']}  Jaccard={j:.3f}")
            print(f"    NEW: {bq['question_text'][:100]}")
            print(f"    OLD: {oq['question_text'][:100]}")
if hits1 == 0:
    print("  No question-level word-overlap duplicates found.")

batch_opts = [(bq["question_id"], o) for bq in batch_qs for o in bq.get("options", [])]
other_opts = [(oq["question_id"], o) for oq in other_qs for o in oq.get("options", [])]

print()
print("=== METHOD 1 (options): Word-overlap Jaccard > 0.7 ===")
ohits1 = 0
for bqid, bo in batch_opts:
    bw = words(bo["option_text"])
    for oqid, oo in other_opts:
        j = jaccard(bw, words(oo["option_text"]))
        if j > 0.7:
            ohits1 += 1
            print(f"  Q{bqid}/O{bo['option_id']} vs Q{oqid}/O{oo['option_id']}  Jaccard={j:.3f}")
            print(f"    NEW: {bo['option_text'][:100]}")
            print(f"    OLD: {oo['option_text'][:100]}")
if ohits1 == 0:
    print("  No option-level word-overlap duplicates found.")
print(f"\nMethod 1 summary - Question hits: {hits1}  Option hits: {ohits1}")
print(f"Comparisons: Q {len(batch_qs)}x{len(other_qs)}={len(batch_qs)*len(other_qs)}, O {len(batch_opts)}x{len(other_opts)}={len(batch_opts)*len(other_opts)}")

print("\n" + "="*70)
print("=== METHOD 2: Character-trigram Jaccard (Q>0.65 AND O>0.65) ===")
hits2 = 0
for bq in batch_qs:
    bt = trigrams(bq["question_text"])
    for oq in other_qs:
        jq = jaccard(bt, trigrams(oq["question_text"]))
        if jq > 0.65:
            # also check options
            for bo in bq.get("options", []):
                bto = trigrams(bo["option_text"])
                for oo in oq.get("options", []):
                    jo = jaccard(bto, trigrams(oo["option_text"]))
                    if jo > 0.65:
                        hits2 += 1
                        print(f"  Q{bq['question_id']} vs Q{oq['question_id']}  Q-tri={jq:.3f}  O-tri={jo:.3f}")
                        print(f"    NEW-Q: {bq['question_text'][:100]}")
                        print(f"    OLD-Q: {oq['question_text'][:100]}")
                        print(f"    NEW-O: {bo['option_text'][:100]}")
                        print(f"    OLD-O: {oo['option_text'][:100]}")
if hits2 == 0:
    print("  No trigram duplicates found (both question AND option above threshold).")
print(f"\nMethod 2 summary - Hits: {hits2}")
print("\n*** DOUBLE-CHECK COMPLETE ***")
