"""Temporary script to find duplicate/rephrased questions."""
from data.questions_enhanced import QUESTIONS_POOL_ENHANCED
from collections import defaultdict
import re

# Group by category
cat_groups = defaultdict(list)
for q in QUESTIONS_POOL_ENHANCED:
    cat_groups[q.get('category', '')].append(q)

# METHOD 2: Find 'What excites you most about pursuing a career in' pattern
excites_career = [q for q in QUESTIONS_POOL_ENHANCED
                  if 'excites you most about pursuing a career' in q.get('question_text', '').lower()]
print(f"=== 'What excites you most about pursuing a career in...' questions: {len(excites_career)} ===")
for eq in sorted(excites_career, key=lambda x: x['question_id']):
    cat = eq.get('category', '')
    originals = [q for q in cat_groups[cat] if q['question_id'] < eq['question_id']]
    print(f"\nQID {eq['question_id']}: {eq['question_text'][:90]}")
    print(f"  Category: {cat} ({len(originals)} earlier Qs)")
    for o in originals[:3]:
        print(f"  EARLIER QID {o['question_id']}: {o['question_text'][:80]}")

# METHOD 3: Find other common rephrase patterns
print("\n\n=== Other rephrase patterns ===")

# Pattern: "What draws you most to X" vs existing "What area/aspect/style of X"
draws_most = [q for q in QUESTIONS_POOL_ENHANCED
              if 'what draws you most to' in q.get('question_text', '').lower()]
print(f"\n'What draws you most to...' questions: {len(draws_most)}")
for eq in sorted(draws_most, key=lambda x: x['question_id']):
    cat = eq.get('category', '')
    originals = [q for q in cat_groups[cat] if q['question_id'] < eq['question_id']]
    print(f"\n  QID {eq['question_id']}: {eq['question_text'][:80]}")
    for o in originals[:3]:
        print(f"    EARLIER QID {o['question_id']}: {o['question_text'][:80]}")

# Pattern: "What career in X" vs existing questions
career_in = [q for q in QUESTIONS_POOL_ENHANCED
             if re.search(r'what career in .+ appeals', q.get('question_text', '').lower())]
print(f"\n'What career in X appeals...' questions: {len(career_in)}")
for eq in sorted(career_in, key=lambda x: x['question_id']):
    cat = eq.get('category', '')
    originals = [q for q in cat_groups[cat] if q['question_id'] < eq['question_id']]
    print(f"\n  QID {eq['question_id']}: {eq['question_text'][:80]}")
    for o in originals[:3]:
        print(f"    EARLIER QID {o['question_id']}: {o['question_text'][:80]}")

# Pattern: "What excites you most about studying X"
excites_studying = [q for q in QUESTIONS_POOL_ENHANCED
                    if 'excites you most about studying' in q.get('question_text', '').lower()]
print(f"\n'What excites you most about studying...' questions: {len(excites_studying)}")
for eq in sorted(excites_studying, key=lambda x: x['question_id']):
    cat = eq.get('category', '')
    originals = [q for q in cat_groups[cat] if q['question_id'] < eq['question_id']]
    print(f"\n  QID {eq['question_id']}: {eq['question_text'][:80]}")
    for o in originals[:3]:
        print(f"    EARLIER QID {o['question_id']}: {o['question_text'][:80]}")

# METHOD 4: Find QID ranges that seem to be batches
print("\n\n=== QID range analysis ===")
all_qids = sorted([q['question_id'] for q in QUESTIONS_POOL_ENHANCED])
print(f"Total questions: {len(all_qids)}")
print(f"QID range: {min(all_qids)} - {max(all_qids)}")

# Find questions in higher QID ranges that duplicate lower ones
# Check for same-category questions where the newer one is a simple rephrase
def normalize_text(text):
    t = text.lower().strip()
    t = re.sub(r'[^a-z0-9 ]', '', t)
    return ' '.join(t.split())

def word_set(text):
    stop = {'a', 'an', 'the', 'of', 'in', 'to', 'and', 'or', 'you', 'your', 'most', 'would'}
    return set(normalize_text(text).split()) - stop

# Find ALL high-QID questions that are rephrases of lower-QID ones
rephrase_pairs = []
for cat, qs in cat_groups.items():
    if len(qs) < 2:
        continue
    qs_sorted = sorted(qs, key=lambda x: x['question_id'])
    for i, later_q in enumerate(qs_sorted):
        for earlier_q in qs_sorted[:i]:
            w1 = word_set(earlier_q['question_text'])
            w2 = word_set(later_q['question_text'])
            if not w1 or not w2:
                continue
            overlap = len(w1 & w2)
            union = len(w1 | w2)
            jaccard = overlap / union if union > 0 else 0
            if jaccard >= 0.5:
                rephrase_pairs.append((
                    jaccard, earlier_q['question_id'], later_q['question_id'],
                    cat, earlier_q['question_text'][:70], later_q['question_text'][:70]
                ))

rephrase_pairs.sort(key=lambda x: -x[0])
print(f"\nHigh-similarity pairs (Jaccard >= 0.5, stop words removed): {len(rephrase_pairs)}")
# Collect all QIDs that are the LATER duplicate
later_dupes = set()
for _, earlier, later, cat, t1, t2 in rephrase_pairs:
    later_dupes.add(later)

print(f"Unique later-QID duplicates to remove: {len(later_dupes)}")
print(f"QIDs: {sorted(later_dupes)}")
