"""Verify cleaned trait data"""
from importlib import reload
import questions_enhanced
reload(questions_enhanced)
from questions_enhanced import QUESTIONS_POOL_ENHANCED, TRAIT_SECONDARY_MAP
from collections import Counter

print("=== Verification ===")
print(f"Questions: {len(QUESTIONS_POOL_ENHANCED)}")
opts = sum(len(q.get("options", [])) for q in QUESTIONS_POOL_ENHANCED)
print(f"Total options: {opts}")

counts = []
for q in QUESTIONS_POOL_ENHANCED:
    for opt in q.get("options", []):
        tags = opt.get("trait_tags", {})
        if isinstance(tags, dict):
            counts.append(len(tags))
dist = Counter(counts)
print("Trait count distribution:")
for k in sorted(dist.keys()):
    print(f"  {k} traits: {dist[k]} options")

print(f"\nTRAIT_SECONDARY_MAP: {len(TRAIT_SECONDARY_MAP)} primary traits")
map_sizes = {k: len(v) for k, v in TRAIT_SECONDARY_MAP.items()}
print(f"  Min secondaries: {min(map_sizes.values())}")
print(f"  Max secondaries: {max(map_sizes.values())}")
print(f"  Avg secondaries: {sum(map_sizes.values())/len(map_sizes):.1f}")

print("\n=== Q1 Options ===")
for q in QUESTIONS_POOL_ENHANCED:
    if q["question_id"] == 1:
        for opt in q.get("options", []):
            tags = sorted(opt["trait_tags"].items(), key=lambda x: -x[1])
            print(f'  opt{opt["option_id"]}: "{opt["option_text"][:50]}" -> {tags}')
        break

# Check no obviously bad pairings remain
bad = 0
checks = [
    ("Agri-Nature", ["Software-Dev", "Cyber-Defense", "Maritime-Sea", "Mechanical-Design", "Hardware-Systems"]),
    ("Patient-Care", ["Maritime-Sea", "Agri-Nature", "Software-Dev"]),
    ("Rehab-Therapy", ["Maritime-Sea", "Agri-Nature", "Law-Enforce"]),
    ("Software-Dev", ["Maritime-Sea", "Agri-Nature", "Patient-Care"]),
    ("Finance-Acct", ["Maritime-Sea", "Medical-Lab", "Agri-Nature"]),
    ("Visual-Design", ["Maritime-Sea", "Agri-Nature", "Law-Enforce", "Mechanical-Design"]),
    ("Maritime-Sea", ["Software-Dev", "Patient-Care", "Finance-Acct"]),
    ("Law-Enforce", ["Agri-Nature", "Culinary-Arts", "Maritime-Sea"]),
]
for primary, excluded_secs in checks:
    for q in QUESTIONS_POOL_ENHANCED:
        for opt in q.get("options", []):
            tags = opt.get("trait_tags", {})
            if tags.get(primary) == 1.0:
                for sec in excluded_secs:
                    if sec in tags:
                        bad += 1
                        print(f'  BAD: Q{q["question_id"]} "{opt["option_text"][:50]}" has {primary}+{sec}')
print(f"\nRemaining bad pairings from spot-checks: {bad}")
