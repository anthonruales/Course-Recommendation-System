"""Duplicate / rephrase checker for Batch 30 against the entire existing pool."""
import sys, re
sys.path.insert(0, r'C:\Users\USer\Downloads\capstone-back-end\Course-Recommendation-System\backend')
from data.questions_enhanced import QUESTIONS_POOL_ENHANCED

BATCH_IDS = set(range(5266, 5286))  # Q5266-Q5285

existing_qs = [q for q in QUESTIONS_POOL_ENHANCED if q['question_id'] not in BATCH_IDS]
new_qs      = [q for q in QUESTIONS_POOL_ENHANCED if q['question_id'] in BATCH_IDS]

def tokenize(text):
    return set(re.findall(r'[a-z]+', text.lower()))

def trigrams(text):
    t = text.lower()
    return set(t[i:i+3] for i in range(len(t)-2))

def jaccard(a, b):
    if not a and not b:
        return 0.0
    return len(a & b) / len(a | b)

# Build existing fingerprints
ex_q_tok = [(q['question_id'], tokenize(q['question_text'])) for q in existing_qs]
ex_q_tri = [(q['question_id'], trigrams(q['question_text'])) for q in existing_qs]

ex_o_tok = []
ex_o_tri = []
for q in existing_qs:
    for o in q['options']:
        txt = o.get('option_text', o.get('text', ''))
        ex_o_tok.append((q['question_id'], o['option_id'], tokenize(txt)))
        ex_o_tri.append((q['question_id'], o['option_id'], trigrams(txt)))

# Method 1: word-overlap Jaccard > 0.70
print('=== METHOD 1: Word-overlap Jaccard > 0.70 ===')
flags1 = 0
for nq in new_qs:
    ntok = tokenize(nq['question_text'])
    for eid, etok in ex_q_tok:
        j = jaccard(ntok, etok)
        if j > 0.70:
            print(f'  Q-FLAG: new Q{nq["question_id"]} vs existing Q{eid}  J={j:.3f}')
            flags1 += 1
    for no in nq['options']:
        ntxt = no.get('option_text', no.get('text', ''))
        notok = tokenize(ntxt)
        for eqid, eoid, etok in ex_o_tok:
            j = jaccard(notok, etok)
            if j > 0.70:
                print(f'  O-FLAG: new Q{nq["question_id"]} O{no["option_id"]} vs existing Q{eqid} O{eoid}  J={j:.3f}')
                flags1 += 1
print(f'Method 1 flags: {flags1}')

# Method 2: char-trigram Jaccard > 0.65
print('=== METHOD 2: Char-trigram Jaccard > 0.65 ===')
flags2 = 0
for nq in new_qs:
    ntri = trigrams(nq['question_text'])
    for eid, etri in ex_q_tri:
        j = jaccard(ntri, etri)
        if j > 0.65:
            print(f'  Q-FLAG: new Q{nq["question_id"]} vs existing Q{eid}  J={j:.3f}')
            flags2 += 1
    for no in nq['options']:
        ntxt = no.get('option_text', no.get('text', ''))
        notri = trigrams(ntxt)
        for eqid, eoid, etri in ex_o_tri:
            j = jaccard(notri, etri)
            if j > 0.65:
                print(f'  O-FLAG: new Q{nq["question_id"]} O{no["option_id"]} vs existing Q{eqid} O{eoid}  J={j:.3f}')
                flags2 += 1
print(f'Method 2 flags: {flags2}')

if flags1 == 0 and flags2 == 0:
    print('\nBATCH 30 PASSED BOTH CHECKS')
else:
    print(f'\nBATCH 30 HAS FLAGS: M1={flags1}, M2={flags2}')
