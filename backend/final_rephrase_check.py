"""
Final rephrase check: Verify option overlap for all remaining suspicious pairs
from quick_check output. These are categories with 2+ interest-type questions
that could be rephrases.
"""
import sys, os, re
sys.path.insert(0, os.path.dirname(__file__))
from data.questions_enhanced import QUESTIONS_POOL_ENHANCED as pool

by_id = {q["question_id"]: q for q in pool}

# All suspicious pairs from quick_check output
# Format: (keep_id, suspect_id, category_note)
# The "suspect" is the expansion question that might rephrase the static one
suspicious_pairs = [
    # Medical/Health categories with "What excites you most about pursuing a career in..."
    (967, 3111, "Medical Technology & Lab Science"),
    (968, 3261, "Dentistry & Oral Health"),
    (959, 2931, "Medicine & Healthcare"),
    (974, 3351, "Midwifery & Maternal Health"),
    (973, 3321, "Optometry & Vision Care"),
    (964, 3051, "Pharmacy & Pharmaceutical Science"),
    (965, 3081, "Physical Therapy & Rehabilitation"),
    (972, 3291, "Radiology & Imaging"),
    (975, 3021, "Public Health"),
    (962, 2991, "Psychology & Mental Health"),
    (971, 3201, "Respiratory Therapy"),
    (970, 3231, "Speech-Language Pathology"),
    (969, 3171, "Occupational Therapy"),
    (966, 3141, "Nutrition & Dietetics"),
    (961, 2971, "Nursing & Patient Care"),
    # Education/Social categories
    (989, 3381, "Education & Teaching"),
    (991, 3501, "Law & Justice"),
    (992, 3531, "Politics & Government"),
    (996, 3471, "Communication & Journalism"),
    (998, 3561, "Criminology & Public Safety"),
    (995, 3441, "History & Culture"),
    (1031, 3411, "Social Work & Community"),
    (1002, 3591, "Public Administration"),
    (1102, 4161, "Technical-Vocational Training"),
    # Other pairs that look suspicious from quick_check
    (967, 3121, "Medical Technology - practice vs interest"),
    (968, 3271, "Dentistry - practice vs interest"),
    (959, 2941, "Medicine - practice vs interest"),
    (974, 3361, "Midwifery - practice vs interest"),
    (973, 3331, "Optometry - practice vs interest"),
    (964, 3061, "Pharmacy - practice vs interest"),
    (965, 3091, "Physical Therapy - practice vs interest"),
    (972, 3301, "Radiology - practice vs interest"),
    (989, 3391, "Education - day-to-day vs interest"),
    (995, 3451, "History - work vs interest"),
    # Cross-check: "practice fulfilling" vs "career excites" within same category
    (3111, 3121, "MedTech: career excites vs practice fulfilling"),
    (3261, 3271, "Dentistry: career excites vs practice fulfilling"),
    (2931, 2941, "Medicine: career excites vs practice fulfilling"),
    (3351, 3361, "Midwifery: career excites vs practice fulfilling"),
    (3321, 3331, "Optometry: career excites vs practice fulfilling"),
    (3051, 3061, "Pharmacy: career excites vs practice fulfilling"),
    (3081, 3091, "PhysTherapy: career excites vs practice fulfilling"),
    (3291, 3301, "Radiology: career excites vs practice fulfilling"),
    (3381, 3391, "Education: career excites vs day-to-day"),
    (3441, 3451, "History: career excites vs work"),
]

def option_texts(q):
    return set(o["option_text"].lower().strip() for o in q.get("options", []))

def option_overlap(q1, q2):
    s1, s2 = option_texts(q1), option_texts(q2)
    if not s1 or not s2:
        return 0.0
    return len(s1 & s2) / min(len(s1), len(s2))

def word_jaccard(t1, t2):
    w1 = set(re.findall(r'\b\w+\b', t1.lower()))
    w2 = set(re.findall(r'\b\w+\b', t2.lower()))
    if not w1 or not w2:
        return 0.0
    return len(w1 & w2) / len(w1 | w2)

print("=== Final Rephrase Check: Option Overlap for Suspicious Pairs ===\n")
genuinely_rephrase = []

for keep_id, suspect_id, note in suspicious_pairs:
    q1 = by_id.get(keep_id)
    q2 = by_id.get(suspect_id)
    if not q1 or not q2:
        status = "SKIP (one or both already removed)"
        if not q1:
            status += f" Q{keep_id} missing"
        if not q2:
            status += f" Q{suspect_id} missing"
        print(f"  Q{keep_id} vs Q{suspect_id} [{note}]: {status}")
        continue
    
    j = word_jaccard(q1["question_text"], q2["question_text"])
    ov = option_overlap(q1, q2)
    
    # Show details
    print(f"\n  Q{keep_id} vs Q{suspect_id} [{note}]")
    print(f"    Q{keep_id}: {q1['question_text']}")
    print(f"    Q{suspect_id}: {q2['question_text']}")
    print(f"    Jaccard: {j:.2f}  Option overlap: {ov:.2f}")
    
    opts1 = sorted(option_texts(q1))
    opts2 = sorted(option_texts(q2))
    common = sorted(option_texts(q1) & option_texts(q2))
    
    print(f"    Q{keep_id} options ({len(opts1)}): {opts1[:4]}...")
    print(f"    Q{suspect_id} options ({len(opts2)}): {opts2[:4]}...")
    if common:
        print(f"    Common options ({len(common)}): {common[:4]}...")
    
    # Determine if rephrase
    is_rephrase = False
    if ov >= 0.15 and j >= 0.20:
        is_rephrase = True
        reason = f"j={j:.2f}>=0.20 AND ov={ov:.2f}>=0.15"
    elif ov >= 0.30:
        is_rephrase = True
        reason = f"ov={ov:.2f}>=0.30"
    elif j >= 0.50:
        is_rephrase = True
        reason = f"j={j:.2f}>=0.50"
    
    if is_rephrase:
        print(f"    >>> REPHRASE: {reason}")
        genuinely_rephrase.append((keep_id, suspect_id, note, j, ov))
    else:
        print(f"    --- DIFFERENT (below thresholds)")

print(f"\n\n=== SUMMARY ===")
print(f"Total suspicious pairs checked: {len(suspicious_pairs)}")
print(f"Confirmed rephrases: {len(genuinely_rephrase)}")
print(f"\nIDs to remove (keep the first, remove the second):")
remove_ids = set()
for keep_id, suspect_id, note, j, ov in genuinely_rephrase:
    print(f"  Remove Q{suspect_id} (rephrase of Q{keep_id}) [{note}] j={j:.2f} ov={ov:.2f}")
    remove_ids.add(suspect_id)

print(f"\nUnique IDs to add to _MANUAL_REMOVE_IDS: {sorted(remove_ids)}")
print(f"Count: {len(remove_ids)}")
