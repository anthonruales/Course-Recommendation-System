import sys
sys.path.insert(0, r'C:\Users\USer\Downloads\capstone-back-end\Course-Recommendation-System\backend')
from data.questions_enhanced import QUESTIONS_POOL_ENHANCED
qs = QUESTIONS_POOL_ENHANCED
qids = [q['question_id'] for q in qs]
oids = []
for q in qs:
    for o in q['options']:
        oids.append(o['option_id'])
print('Total:', len(qs))
print('UniqueQIDs:', len(set(qids)))
print('UniqueOIDs:', len(set(oids)))
print('MaxQID:', max(qids))
print('MaxOID:', max(oids))
b30_qids = [q['question_id'] for q in qs if 5266 <= q['question_id'] <= 5285]
print('Batch30 count:', len(b30_qids))
if len(qs) == 1727 and len(set(qids)) == 1727:
    print('PASS')
else:
    print('FAIL')
