"""
Duplicate / Redundant / Rephrased Question & Option Detector
=============================================================

Checks the entire QUESTIONS_POOL_ENHANCED for:
  1. EXACT duplicates        — identical question_text
  2. NEAR-DUPLICATE text     — high similarity after normalization (Jaccard ≥ 0.75)
  3. OPTION-SET clones       — different question text but identical option texts
  4. TRAIT-FINGERPRINT clones — same set of primary traits (weight ≥ 0.8) across options
  5. OPTION-LEVEL duplicates — individual options across different questions that
                               have nearly identical text AND identical trait profiles

Also verifies that the runtime deduplication in AdaptiveAssessmentEngine prevents
any answered question from reappearing during an assessment.

Usage:
    cd backend
    python check_duplicates.py
"""

import re
import sys
import os
from collections import defaultdict
from itertools import combinations

# ── ensure backend/ is importable ──
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data.questions_enhanced import QUESTIONS_POOL_ENHANCED


# ═══════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════

_STOP_WORDS = frozenset({
    "a", "an", "the", "is", "are", "was", "were", "be", "been", "being",
    "do", "does", "did", "have", "has", "had", "to", "of", "in", "for",
    "on", "with", "at", "by", "from", "it", "its", "this", "that",
    "and", "or", "but", "not", "so", "if", "as", "your", "you",
    "would", "could", "should", "will", "can", "most", "more", "very",
    "about", "into", "what", "which", "who", "how", "when", "where",
})


def normalize_text(text: str) -> str:
    """Lowercase, strip punctuation, collapse whitespace."""
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return " ".join(text.split())


def tokenize(text: str) -> set:
    """Normalize → split → remove stop words."""
    words = normalize_text(text).split()
    return {w for w in words if w not in _STOP_WORDS and len(w) > 1}


def jaccard(a: set, b: set) -> float:
    """Jaccard similarity between two token sets."""
    if not a and not b:
        return 1.0
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def trait_fingerprint(question: dict) -> tuple:
    """Sorted tuple of all primary traits (weight ≥ 0.8) across all options."""
    traits = set()
    for opt in question.get("options", []):
        tt = opt.get("trait_tags", {})
        if isinstance(tt, dict):
            for t, w in tt.items():
                if w >= 0.8:
                    traits.add(t)
        elif isinstance(tt, list):
            for t in tt:
                traits.add(t)
    return tuple(sorted(traits))


def option_texts_fingerprint(question: dict) -> tuple:
    """Sorted tuple of normalized option texts."""
    texts = []
    for opt in question.get("options", []):
        texts.append(normalize_text(opt.get("option_text", "")))
    return tuple(sorted(texts))


def option_trait_profile(option: dict) -> tuple:
    """Sorted tuple of (trait, weight) for an option."""
    tt = option.get("trait_tags", {})
    if isinstance(tt, dict):
        return tuple(sorted(tt.items()))
    elif isinstance(tt, list):
        return tuple(sorted((t, 1.0) for t in tt))
    return ()


# ═══════════════════════════════════════════════════════════════
# CHECK 1: Exact duplicate question texts
# ═══════════════════════════════════════════════════════════════

def check_exact_duplicates(questions):
    """Find questions with identical question_text."""
    text_map = defaultdict(list)
    for q in questions:
        key = normalize_text(q.get("question_text", ""))
        text_map[key].append(q["question_id"])

    dupes = {k: v for k, v in text_map.items() if len(v) > 1}
    return dupes


# ═══════════════════════════════════════════════════════════════
# CHECK 2: Near-duplicate question texts (Jaccard ≥ threshold)
# ═══════════════════════════════════════════════════════════════

def check_near_duplicate_texts(questions, threshold=0.75):
    """Find question pairs with highly similar text (Jaccard ≥ threshold)."""
    # Build token sets once
    q_tokens = []
    for q in questions:
        tokens = tokenize(q.get("question_text", ""))
        q_tokens.append((q["question_id"], q.get("question_text", ""), tokens))

    # Group by category to reduce O(n²) comparisons
    cat_groups = defaultdict(list)
    for qid, text, tokens in q_tokens:
        cat = next((q.get("category", "") for q in questions if q["question_id"] == qid), "")
        cat_groups[cat].append((qid, text, tokens))

    near_dupes = []
    # Compare within same category (most likely source of duplicates)
    for cat, group in cat_groups.items():
        for i, (qid1, text1, tok1) in enumerate(group):
            for qid2, text2, tok2 in group[i + 1:]:
                sim = jaccard(tok1, tok2)
                if sim >= threshold:
                    near_dupes.append((qid1, qid2, sim, text1[:80], text2[:80], cat))

    # Also do cross-category comparison for very high similarity
    all_items = [(qid, text, tokens) for qid, text, tokens in q_tokens]
    # Only check cross-category for similarity >= 0.85
    cross_cat_checked = set()
    for cat1, group1 in cat_groups.items():
        for cat2, group2 in cat_groups.items():
            if cat1 >= cat2:
                continue
            pair_key = (cat1, cat2)
            if pair_key in cross_cat_checked:
                continue
            cross_cat_checked.add(pair_key)
            for qid1, text1, tok1 in group1:
                for qid2, text2, tok2 in group2:
                    sim = jaccard(tok1, tok2)
                    if sim >= 0.85:
                        near_dupes.append((qid1, qid2, sim, text1[:80], text2[:80], f"{cat1} vs {cat2}"))

    return near_dupes


# ═══════════════════════════════════════════════════════════════
# CHECK 3: Option-set clones (same options, different question)
# ═══════════════════════════════════════════════════════════════

def check_option_set_clones(questions):
    """Find questions that have identical sets of option texts."""
    fp_map = defaultdict(list)
    for q in questions:
        fp = option_texts_fingerprint(q)
        if len(fp) >= 3:  # Only check questions with meaningful option sets
            fp_map[fp].append(q["question_id"])

    clones = {k: v for k, v in fp_map.items() if len(v) > 1}
    return clones


# ═══════════════════════════════════════════════════════════════
# CHECK 4: Trait-fingerprint clones
# ═══════════════════════════════════════════════════════════════

def check_trait_fingerprint_clones(questions):
    """Find questions with identical primary-trait fingerprints."""
    fp_map = defaultdict(list)
    for q in questions:
        fp = trait_fingerprint(q)
        if len(fp) >= 3:  # Only meaningful when 3+ primary traits
            fp_map[fp].append((q["question_id"], q.get("question_text", "")[:60], q.get("category", "")))

    clones = {k: v for k, v in fp_map.items() if len(v) > 1}
    return clones


# ═══════════════════════════════════════════════════════════════
# CHECK 5: Option-level duplicates across questions
# ═══════════════════════════════════════════════════════════════

def check_option_level_duplicates(questions, threshold=0.80):
    """Find individual options across different questions with near-identical
    text AND the same trait profile."""
    # Build index: normalized_option_text -> [(qid, option_id, trait_profile)]
    option_index = defaultdict(list)
    for q in questions:
        qid = q["question_id"]
        for opt in q.get("options", []):
            norm = normalize_text(opt.get("option_text", ""))
            tp = option_trait_profile(opt)
            option_index[norm].append((qid, opt.get("option_id"), tp))

    # Exact text + same traits
    exact_dupes = []
    for text, entries in option_index.items():
        if len(entries) > 1:
            # Group by trait profile
            trait_groups = defaultdict(list)
            for qid, oid, tp in entries:
                trait_groups[tp].append((qid, oid))
            for tp, group in trait_groups.items():
                if len(group) > 1:
                    exact_dupes.append((text[:60], group, dict(tp) if tp else {}))

    # Near-duplicate option text (Jaccard ≥ threshold) with same trait profile
    # Only check within same trait profile to reduce comparisons
    trait_opt_groups = defaultdict(list)
    for q in questions:
        qid = q["question_id"]
        for opt in q.get("options", []):
            tp = option_trait_profile(opt)
            tokens = tokenize(opt.get("option_text", ""))
            trait_opt_groups[tp].append((qid, opt.get("option_id"), opt.get("option_text", ""), tokens))

    near_dupes = []
    for tp, group in trait_opt_groups.items():
        if len(group) < 2:
            continue
        for i, (qid1, oid1, text1, tok1) in enumerate(group):
            for qid2, oid2, text2, tok2 in group[i + 1:]:
                if qid1 == qid2:
                    continue  # Same question, skip
                sim = jaccard(tok1, tok2)
                if sim >= threshold:
                    near_dupes.append((text1[:60], text2[:60], qid1, qid2, sim))

    return exact_dupes, near_dupes


# ═══════════════════════════════════════════════════════════════
# CHECK 6: Verify answered questions never reappear at runtime
# ═══════════════════════════════════════════════════════════════

def check_no_question_reappears():
    """Simulate a full 30-question assessment and verify no question
    is shown more than once."""
    from data.courses_specialized import COURSES_POOL_SPECIALIZED

    engine_module = __import__("services.adaptive_assessment", fromlist=["AdaptiveAssessmentEngine"])
    AdaptiveAssessmentEngine = engine_module.AdaptiveAssessmentEngine

    engine = AdaptiveAssessmentEngine(COURSES_POOL_SPECIALIZED, QUESTIONS_POOL_ENHANCED)

    # Test with a few different profiles
    profiles = [
        {"interests": "Programming & Coding, Computers & IT, Robotics, AI & Machine Learning",
         "skills": "Programming/Coding, Graphic Design", "strand": "TVL", "gwa": 92.99},
        {"interests": "Nursing & Patient Care, Biology & Life Sciences",
         "skills": "First Aid", "strand": "STEM", "gwa": 88.0},
        {"interests": "Business & Entrepreneurship, Marketing & Advertising",
         "skills": "Leadership, Public Speaking", "strand": "ABM", "gwa": 90.0},
        {"interests": "Music & Arts, Fine Arts & Painting",
         "skills": "Drawing, Photography", "strand": "ARTS", "gwa": 85.0},
    ]

    issues = []
    for idx, profile in enumerate(profiles):
        sid = engine.create_session(
            user_id=idx + 100,
            user_gwa=profile["gwa"],
            user_strand=profile["strand"],
            max_questions=30,
            user_interests=profile["interests"],
            user_skills=profile["skills"],
        )

        seen_qids = []
        for round_num in range(35):  # Try beyond 30 to stress test
            result = engine.get_next_question(sid)
            if not result:
                break

            q = result["question"]
            qid = q.get("question_id", q.get("id"))

            if qid in seen_qids:
                issues.append(
                    f"Profile {idx + 1} ({profile['strand']}): Q{qid} shown AGAIN "
                    f"at round {round_num + 1} (first seen at round {seen_qids.index(qid) + 1})"
                )

            seen_qids.append(qid)

            # Auto-answer with first non-None option
            opts = q.get("options", [])
            answer_oid = None
            for opt in opts:
                if opt.get("option_id", 0) != -1:
                    answer_oid = opt["option_id"]
                    break
            if answer_oid is not None:
                engine.process_answer(sid, qid, answer_oid)

        # Check for duplicates in seen list
        seen_set = set()
        for qid in seen_qids:
            if qid in seen_set:
                pass  # Already caught above
            seen_set.add(qid)

    return issues


# ═══════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════

def main():
    questions = QUESTIONS_POOL_ENHANCED
    total_questions = len(questions)
    total_options = sum(len(q.get("options", [])) for q in questions)

    print("=" * 70)
    print("  DUPLICATE / REDUNDANT QUESTION & OPTION DETECTOR")
    print("=" * 70)
    print(f"\n  Total questions: {total_questions}")
    print(f"  Total options:   {total_options}")
    print()

    all_clean = True

    # ── CHECK 1: Exact duplicate question texts ──
    print("-" * 70)
    print("  CHECK 1: Exact Duplicate Question Texts")
    print("-" * 70)
    exact_dupes = check_exact_duplicates(questions)
    if exact_dupes:
        all_clean = False
        print(f"  FOUND {len(exact_dupes)} groups of exact duplicates:\n")
        for text, qids in sorted(exact_dupes.items(), key=lambda x: x[1][0]):
            print(f"    QIDs {qids}: \"{text[:80]}...\"")
    else:
        print("  PASS — No exact duplicate question texts found.")
    print()

    # ── CHECK 2: Near-duplicate question texts ──
    print("-" * 70)
    print("  CHECK 2: Near-Duplicate Question Texts (Jaccard >= 0.75)")
    print("-" * 70)
    near_dupes = check_near_duplicate_texts(questions, threshold=0.75)
    if near_dupes:
        # Sort by similarity descending
        near_dupes.sort(key=lambda x: x[2], reverse=True)
        all_clean = False
        print(f"  FOUND {len(near_dupes)} near-duplicate pairs:\n")
        for qid1, qid2, sim, t1, t2, cat in near_dupes[:50]:  # Show top 50
            print(f"    Q{qid1} vs Q{qid2} (similarity={sim:.0%}) [{cat}]")
            print(f"      A: \"{t1}\"")
            print(f"      B: \"{t2}\"")
            print()
        if len(near_dupes) > 50:
            print(f"    ... and {len(near_dupes) - 50} more pairs")
    else:
        print("  PASS — No near-duplicate question texts found.")
    print()

    # ── CHECK 3: Option-set clones ──
    print("-" * 70)
    print("  CHECK 3: Option-Set Clones (identical option text sets)")
    print("-" * 70)
    opt_clones = check_option_set_clones(questions)
    if opt_clones:
        all_clean = False
        print(f"  FOUND {len(opt_clones)} groups of option-set clones:\n")
        q_lookup = {q["question_id"]: q for q in questions}
        for fp, qids in sorted(opt_clones.items(), key=lambda x: x[1][0]):
            print(f"    QIDs {qids}:")
            for qid in qids:
                q = q_lookup.get(qid, {})
                print(f"      Q{qid} [{q.get('category', '?')}]: \"{q.get('question_text', '?')[:70]}\"")
            print()
    else:
        print("  PASS — No option-set clones found.")
    print()

    # ── CHECK 4: Trait-fingerprint clones ──
    print("-" * 70)
    print("  CHECK 4: Trait-Fingerprint Clones (same primary traits >= 0.8)")
    print("-" * 70)
    trait_clones = check_trait_fingerprint_clones(questions)
    if trait_clones:
        # This is common for same-category questions — only flag if question text is also similar
        flagged = []
        for fp, entries in trait_clones.items():
            for i, (qid1, text1, cat1) in enumerate(entries):
                for qid2, text2, cat2 in entries[i + 1:]:
                    tok1 = tokenize(text1)
                    tok2 = tokenize(text2)
                    sim = jaccard(tok1, tok2)
                    if sim >= 0.5:  # Only flag when text is also somewhat similar
                        flagged.append((qid1, qid2, sim, text1, text2, cat1, cat2, fp))

        if flagged:
            all_clean = False
            flagged.sort(key=lambda x: x[2], reverse=True)
            print(f"  FOUND {len(flagged)} trait-clone pairs with similar text:\n")
            for qid1, qid2, sim, t1, t2, c1, c2, fp in flagged[:30]:
                print(f"    Q{qid1} vs Q{qid2} (text_sim={sim:.0%}) traits={fp}")
                print(f"      A [{c1}]: \"{t1}\"")
                print(f"      B [{c2}]: \"{t2}\"")
                print()
            if len(flagged) > 30:
                print(f"    ... and {len(flagged) - 30} more pairs")
        else:
            print("  PASS — Trait-fingerprint clones exist but have sufficiently different text.")
    else:
        print("  PASS — No trait-fingerprint clones found.")
    print()

    # ── CHECK 5: Option-level duplicates ──
    print("-" * 70)
    print("  CHECK 5: Option-Level Duplicates Across Questions")
    print("-" * 70)
    exact_opt_dupes, near_opt_dupes = check_option_level_duplicates(questions)
    if exact_opt_dupes or near_opt_dupes:
        if exact_opt_dupes:
            all_clean = False
            print(f"  FOUND {len(exact_opt_dupes)} exact option duplicates (same text + same traits):\n")
            for text, group, traits in exact_opt_dupes[:20]:
                trait_str = ", ".join(f"{k}:{v}" for k, v in sorted(traits.items())[:3])
                print(f"    \"{text}\" [{trait_str}...]")
                print(f"      In: {group}")
                print()
            if len(exact_opt_dupes) > 20:
                print(f"    ... and {len(exact_opt_dupes) - 20} more")
        if near_opt_dupes:
            near_opt_dupes.sort(key=lambda x: x[4], reverse=True)
            print(f"\n  FOUND {len(near_opt_dupes)} near-duplicate option pairs (Jaccard >= 0.80 + same traits):\n")
            for t1, t2, qid1, qid2, sim in near_opt_dupes[:20]:
                print(f"    Q{qid1} vs Q{qid2} (sim={sim:.0%})")
                print(f"      A: \"{t1}\"")
                print(f"      B: \"{t2}\"")
                print()
            if len(near_opt_dupes) > 20:
                print(f"    ... and {len(near_opt_dupes) - 20} more")
    else:
        print("  PASS — No option-level duplicates found.")
    print()

    # ── CHECK 6: Runtime — no question reappears ──
    print("-" * 70)
    print("  CHECK 6: Runtime — Answered Questions Never Reappear")
    print("-" * 70)
    print("  Simulating 4 full assessments (30 questions each)...")
    reappear_issues = check_no_question_reappears()
    if reappear_issues:
        all_clean = False
        print(f"\n  FAIL — {len(reappear_issues)} reappearance issues:\n")
        for issue in reappear_issues:
            print(f"    {issue}")
    else:
        print("  PASS — No answered question ever reappeared across all 4 profiles.")
    print()

    # ── SUMMARY ──
    print("=" * 70)
    if all_clean:
        print("  ALL CHECKS PASSED — No duplicates or redundancies detected.")
    else:
        print("  ISSUES FOUND — Review the flagged items above.")
    print("=" * 70)


if __name__ == "__main__":
    main()
