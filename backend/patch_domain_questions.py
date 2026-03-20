#!/usr/bin/env python3
"""
Phase 1: Add 14 maritime-dedicated questions + reorder ALL TRAIT_FOLLOWUP_MAP
entries so on-topic questions are served first.
"""
import re, sys, os

# ============================================================
# 14 NEW MARITIME-DEDICATED QUESTIONS (Q443-Q456)
# ============================================================
NEW_QUESTIONS = [
    {
        "question_id": 443,
        "question_text": "Which maritime subject are you most eager to study?",
        "weight": 1.5,
        "trait_tags": {"Maritime-Sea": 0.9},
        "options": [
            {"option_id": 3981, "option_text": "Celestial and electronic navigation", "trait_tags": {"Maritime-Sea": 1.0, "Technical-Skill": 0.5, "Analytical-Skill": 0.3}},
            {"option_id": 3982, "option_text": "Marine diesel engineering and propulsion systems", "trait_tags": {"Maritime-Sea": 0.9, "Mechanical-Design": 0.6, "Technical-Skill": 0.4}},
            {"option_id": 3983, "option_text": "Ship construction and naval architecture", "trait_tags": {"Maritime-Sea": 0.9, "Spatial-Design": 0.5, "Mechanical-Design": 0.4}},
            {"option_id": 3984, "option_text": "Maritime law and international conventions", "trait_tags": {"Maritime-Sea": 0.8, "Legal-Practice": 0.5, "Analytical-Skill": 0.3}},
            {"option_id": 3985, "option_text": "Cargo handling and stowage planning", "trait_tags": {"Maritime-Sea": 1.0, "Industrial-Ops": 0.5, "Analytical-Skill": 0.3}},
            {"option_id": 3986, "option_text": "Maritime safety and survival procedures", "trait_tags": {"Maritime-Sea": 0.9, "Physical-Skill": 0.5, "People-Skill": 0.3}}
        ]
    },
    {
        "question_id": 444,
        "question_text": "What type of cargo operation would you most want to oversee?",
        "weight": 1.5,
        "trait_tags": {"Maritime-Sea": 0.9, "Industrial-Ops": 0.3},
        "options": [
            {"option_id": 3987, "option_text": "Container ship loading and logistics", "trait_tags": {"Maritime-Sea": 1.0, "Industrial-Ops": 0.5, "Analytical-Skill": 0.3}},
            {"option_id": 3988, "option_text": "Bulk carrier grain and ore handling", "trait_tags": {"Maritime-Sea": 0.9, "Physical-Skill": 0.4, "Industrial-Ops": 0.4}},
            {"option_id": 3989, "option_text": "Oil and chemical tanker safety management", "trait_tags": {"Maritime-Sea": 0.9, "Environmental-Sci": 0.4, "Technical-Skill": 0.4}},
            {"option_id": 3990, "option_text": "Roll-on/roll-off vehicle transport coordination", "trait_tags": {"Maritime-Sea": 0.8, "Industrial-Ops": 0.5, "Mechanical-Design": 0.3}},
            {"option_id": 3991, "option_text": "Refrigerated cargo temperature monitoring", "trait_tags": {"Maritime-Sea": 0.9, "Technical-Skill": 0.5, "Food-Science": 0.3}},
            {"option_id": 3992, "option_text": "General break-bulk and heavy-lift project cargo", "trait_tags": {"Maritime-Sea": 1.0, "Physical-Skill": 0.4, "Industrial-Ops": 0.3}}
        ]
    },
    {
        "question_id": 445,
        "question_text": "During a maritime emergency drill, which station would you gravitate toward?",
        "weight": 1.5,
        "trait_tags": {"Maritime-Sea": 0.9, "Physical-Skill": 0.3},
        "options": [
            {"option_id": 3993, "option_text": "Bridge command and overall coordination", "trait_tags": {"Maritime-Sea": 1.0, "People-Skill": 0.5, "Analytical-Skill": 0.4}},
            {"option_id": 3994, "option_text": "Engine room emergency shutdown procedures", "trait_tags": {"Maritime-Sea": 0.9, "Mechanical-Design": 0.5, "Technical-Skill": 0.4}},
            {"option_id": 3995, "option_text": "Fire fighting team with hoses and extinguishers", "trait_tags": {"Maritime-Sea": 0.9, "Physical-Skill": 0.6, "People-Skill": 0.3}},
            {"option_id": 3996, "option_text": "Rescue boat launching and man-overboard recovery", "trait_tags": {"Maritime-Sea": 1.0, "Physical-Skill": 0.5, "People-Skill": 0.3}},
            {"option_id": 3997, "option_text": "First aid and onboard medical response", "trait_tags": {"Maritime-Sea": 0.8, "Patient-Care": 0.6, "People-Skill": 0.4}},
            {"option_id": 3998, "option_text": "Emergency communications and distress calling", "trait_tags": {"Maritime-Sea": 0.9, "Technical-Skill": 0.5, "Hardware-Systems": 0.3}}
        ]
    },
    {
        "question_id": 446,
        "question_text": "Which maritime technology advancement excites you most?",
        "weight": 1.5,
        "trait_tags": {"Maritime-Sea": 0.9, "Technical-Skill": 0.3},
        "options": [
            {"option_id": 3999, "option_text": "Electronic Chart Display (ECDIS) navigation", "trait_tags": {"Maritime-Sea": 0.9, "Technical-Skill": 0.6, "Software-Dev": 0.3}},
            {"option_id": 4000, "option_text": "Smart engine monitoring with IoT sensors", "trait_tags": {"Maritime-Sea": 0.8, "Mechanical-Design": 0.5, "Data-Analytics": 0.4}},
            {"option_id": 4001, "option_text": "Automatic Identification System (AIS) vessel tracking", "trait_tags": {"Maritime-Sea": 1.0, "Technical-Skill": 0.5, "Data-Analytics": 0.3}},
            {"option_id": 4002, "option_text": "GMDSS satellite communication systems", "trait_tags": {"Maritime-Sea": 1.0, "Hardware-Systems": 0.5, "Technical-Skill": 0.3}},
            {"option_id": 4003, "option_text": "Autonomous and remote-controlled vessel tech", "trait_tags": {"Maritime-Sea": 0.9, "AI-ML": 0.5, "Software-Dev": 0.4}},
            {"option_id": 4004, "option_text": "Advanced ballast water treatment systems", "trait_tags": {"Maritime-Sea": 0.9, "Environmental-Sci": 0.5, "Technical-Skill": 0.3}}
        ]
    },
    {
        "question_id": 447,
        "question_text": "What aspect of port and harbor operations would you want to manage?",
        "weight": 1.5,
        "trait_tags": {"Maritime-Sea": 0.9, "Admin-Skill": 0.3},
        "options": [
            {"option_id": 4005, "option_text": "Vessel traffic management and channel safety", "trait_tags": {"Maritime-Sea": 1.0, "Analytical-Skill": 0.5, "Technical-Skill": 0.3}},
            {"option_id": 4006, "option_text": "Container terminal scheduling and logistics", "trait_tags": {"Maritime-Sea": 0.8, "Industrial-Ops": 0.6, "Admin-Skill": 0.4}},
            {"option_id": 4007, "option_text": "Harbor pilotage and ship berthing guidance", "trait_tags": {"Maritime-Sea": 1.0, "Physical-Skill": 0.4, "Analytical-Skill": 0.3}},
            {"option_id": 4008, "option_text": "Customs documentation and port clearance", "trait_tags": {"Maritime-Sea": 0.8, "Admin-Skill": 0.5, "Legal-Practice": 0.4}},
            {"option_id": 4009, "option_text": "Cargo surveying and quality inspection", "trait_tags": {"Maritime-Sea": 0.9, "Industrial-Ops": 0.5, "Analytical-Skill": 0.3}},
            {"option_id": 4010, "option_text": "Port security and maritime law enforcement", "trait_tags": {"Maritime-Sea": 0.9, "Law-Enforce": 0.5, "Admin-Skill": 0.3}}
        ]
    },
    {
        "question_id": 448,
        "question_text": "As a maritime professional, which regulation area would you champion?",
        "weight": 1.5,
        "trait_tags": {"Maritime-Sea": 0.9, "Legal-Practice": 0.3},
        "options": [
            {"option_id": 4011, "option_text": "SOLAS \u2014 Safety of Life at Sea standards", "trait_tags": {"Maritime-Sea": 1.0, "People-Skill": 0.4, "Legal-Practice": 0.3}},
            {"option_id": 4012, "option_text": "MARPOL \u2014 Marine pollution prevention rules", "trait_tags": {"Maritime-Sea": 0.9, "Environmental-Sci": 0.5, "Legal-Practice": 0.3}},
            {"option_id": 4013, "option_text": "STCW \u2014 Seafarer training and competency", "trait_tags": {"Maritime-Sea": 0.9, "Teaching-Ed": 0.5, "People-Skill": 0.4}},
            {"option_id": 4014, "option_text": "ISM Code \u2014 Safety management systems", "trait_tags": {"Maritime-Sea": 0.9, "Admin-Skill": 0.5, "Industrial-Ops": 0.3}},
            {"option_id": 4015, "option_text": "MLC \u2014 Maritime Labour Convention crew welfare", "trait_tags": {"Maritime-Sea": 0.8, "HR-Management": 0.6, "People-Skill": 0.4}},
            {"option_id": 4016, "option_text": "Port State Control inspection procedures", "trait_tags": {"Maritime-Sea": 1.0, "Law-Enforce": 0.4, "Analytical-Skill": 0.3}}
        ]
    },
    {
        "question_id": 449,
        "question_text": "What type of ship maintenance work would you find most satisfying?",
        "weight": 1.5,
        "trait_tags": {"Maritime-Sea": 0.9, "Mechanical-Design": 0.3},
        "options": [
            {"option_id": 4017, "option_text": "Main engine overhaul and repair", "trait_tags": {"Maritime-Sea": 0.9, "Mechanical-Design": 0.7, "Physical-Skill": 0.3}},
            {"option_id": 4018, "option_text": "Hull cleaning, inspection, and protective coating", "trait_tags": {"Maritime-Sea": 0.9, "Physical-Skill": 0.5, "Environmental-Eng": 0.3}},
            {"option_id": 4019, "option_text": "Electrical wiring and shipboard power systems", "trait_tags": {"Maritime-Sea": 0.8, "Electrical-Power": 0.6, "Technical-Skill": 0.4}},
            {"option_id": 4020, "option_text": "Radar, GPS, and navigation equipment calibration", "trait_tags": {"Maritime-Sea": 1.0, "Technical-Skill": 0.5, "Hardware-Systems": 0.3}},
            {"option_id": 4021, "option_text": "Life raft, EPIRB, and safety equipment servicing", "trait_tags": {"Maritime-Sea": 0.9, "Physical-Skill": 0.4, "Industrial-Ops": 0.3}},
            {"option_id": 4022, "option_text": "Deck crane, winch, and anchor windlass maintenance", "trait_tags": {"Maritime-Sea": 0.9, "Mechanical-Design": 0.5, "Physical-Skill": 0.4}}
        ]
    },
    {
        "question_id": 450,
        "question_text": "Which maritime career path sounds most fulfilling to you?",
        "weight": 1.5,
        "trait_tags": {"Maritime-Sea": 0.9},
        "options": [
            {"option_id": 4023, "option_text": "Ship captain commanding worldwide voyages", "trait_tags": {"Maritime-Sea": 1.0, "People-Skill": 0.5, "Analytical-Skill": 0.3}},
            {"option_id": 4024, "option_text": "Chief engineer managing vessel propulsion", "trait_tags": {"Maritime-Sea": 0.9, "Mechanical-Design": 0.6, "Technical-Skill": 0.4}},
            {"option_id": 4025, "option_text": "Harbor pilot guiding ships through tight channels", "trait_tags": {"Maritime-Sea": 1.0, "Physical-Skill": 0.4, "Analytical-Skill": 0.3}},
            {"option_id": 4026, "option_text": "Maritime surveyor inspecting vessel safety", "trait_tags": {"Maritime-Sea": 0.9, "Analytical-Skill": 0.5, "Law-Enforce": 0.3}},
            {"option_id": 4027, "option_text": "Maritime instructor at a Philippine academy", "trait_tags": {"Maritime-Sea": 0.8, "Teaching-Ed": 0.6, "People-Skill": 0.4}},
            {"option_id": 4028, "option_text": "Shipping operations manager at a manning agency", "trait_tags": {"Maritime-Sea": 0.8, "Admin-Skill": 0.5, "Finance-Acct": 0.4}}
        ]
    },
    {
        "question_id": 451,
        "question_text": "On a long ocean crossing, what would you focus on most?",
        "weight": 1.5,
        "trait_tags": {"Maritime-Sea": 0.9},
        "options": [
            {"option_id": 4029, "option_text": "Plotting the most fuel-efficient sea route", "trait_tags": {"Maritime-Sea": 1.0, "Analytical-Skill": 0.5, "Data-Analytics": 0.3}},
            {"option_id": 4030, "option_text": "Monitoring engine gauges and fuel consumption", "trait_tags": {"Maritime-Sea": 0.9, "Mechanical-Design": 0.5, "Technical-Skill": 0.4}},
            {"option_id": 4031, "option_text": "Keeping crew morale high during extended voyages", "trait_tags": {"Maritime-Sea": 0.8, "People-Skill": 0.6, "HR-Management": 0.3}},
            {"option_id": 4032, "option_text": "Tracking weather systems and avoiding storms", "trait_tags": {"Maritime-Sea": 1.0, "Environmental-Sci": 0.4, "Analytical-Skill": 0.3}},
            {"option_id": 4033, "option_text": "Maintaining accurate ship logs and records", "trait_tags": {"Maritime-Sea": 0.9, "Admin-Skill": 0.5, "Analytical-Skill": 0.3}},
            {"option_id": 4034, "option_text": "Ensuring all cargo remains secure and stable", "trait_tags": {"Maritime-Sea": 0.9, "Industrial-Ops": 0.4, "Physical-Skill": 0.3}}
        ]
    },
    {
        "question_id": 452,
        "question_text": "Which shipboard communication duty appeals to you most?",
        "weight": 1.5,
        "trait_tags": {"Maritime-Sea": 0.9, "Technical-Skill": 0.3},
        "options": [
            {"option_id": 4035, "option_text": "Managing distress and urgency signal protocols", "trait_tags": {"Maritime-Sea": 1.0, "Technical-Skill": 0.4, "People-Skill": 0.3}},
            {"option_id": 4036, "option_text": "Transmitting weather observations to stations", "trait_tags": {"Maritime-Sea": 0.9, "Environmental-Sci": 0.4, "Data-Analytics": 0.3}},
            {"option_id": 4037, "option_text": "Coordinating with port control for docking", "trait_tags": {"Maritime-Sea": 1.0, "Admin-Skill": 0.4, "People-Skill": 0.3}},
            {"option_id": 4038, "option_text": "Ship-to-ship coordination in congested waters", "trait_tags": {"Maritime-Sea": 0.9, "People-Skill": 0.5, "Analytical-Skill": 0.3}},
            {"option_id": 4039, "option_text": "Operating and maintaining satellite comm systems", "trait_tags": {"Maritime-Sea": 0.8, "Hardware-Systems": 0.6, "Technical-Skill": 0.4}},
            {"option_id": 4040, "option_text": "Testing and maintaining EPIRB emergency beacons", "trait_tags": {"Maritime-Sea": 0.9, "Technical-Skill": 0.5, "Physical-Skill": 0.3}}
        ]
    },
    {
        "question_id": 453,
        "question_text": "Which area of the maritime business world interests you most?",
        "weight": 1.5,
        "trait_tags": {"Maritime-Sea": 0.8, "Finance-Acct": 0.3},
        "options": [
            {"option_id": 4041, "option_text": "Ship chartering and freight rate negotiations", "trait_tags": {"Maritime-Sea": 0.9, "Finance-Acct": 0.5, "People-Skill": 0.4}},
            {"option_id": 4042, "option_text": "Marine insurance and claims assessment", "trait_tags": {"Maritime-Sea": 0.8, "Finance-Acct": 0.5, "Analytical-Skill": 0.4}},
            {"option_id": 4043, "option_text": "Ship brokering and vessel sales", "trait_tags": {"Maritime-Sea": 0.8, "Marketing-Sales": 0.6, "People-Skill": 0.4}},
            {"option_id": 4044, "option_text": "Port authority administration and development", "trait_tags": {"Maritime-Sea": 0.9, "Admin-Skill": 0.5, "Industrial-Ops": 0.3}},
            {"option_id": 4045, "option_text": "Maritime logistics and freight forwarding", "trait_tags": {"Maritime-Sea": 0.9, "Industrial-Ops": 0.5, "Admin-Skill": 0.3}},
            {"option_id": 4046, "option_text": "Crew manning and Filipino seafarer recruitment", "trait_tags": {"Maritime-Sea": 0.8, "HR-Management": 0.6, "People-Skill": 0.4}}
        ]
    },
    {
        "question_id": 454,
        "question_text": "How would you most want to improve maritime safety in the Philippines?",
        "weight": 1.5,
        "trait_tags": {"Maritime-Sea": 0.9, "Law-Enforce": 0.3},
        "options": [
            {"option_id": 4047, "option_text": "Conducting thorough vessel safety inspections", "trait_tags": {"Maritime-Sea": 1.0, "Analytical-Skill": 0.5, "Law-Enforce": 0.3}},
            {"option_id": 4048, "option_text": "Training crews in advanced safety and rescue", "trait_tags": {"Maritime-Sea": 0.9, "Teaching-Ed": 0.5, "People-Skill": 0.4}},
            {"option_id": 4049, "option_text": "Designing better safety management protocols", "trait_tags": {"Maritime-Sea": 0.9, "Admin-Skill": 0.5, "Analytical-Skill": 0.3}},
            {"option_id": 4050, "option_text": "Investigating maritime accidents and finding causes", "trait_tags": {"Maritime-Sea": 0.9, "Forensic-Sci": 0.4, "Analytical-Skill": 0.4}},
            {"option_id": 4051, "option_text": "Upgrading lifesaving and firefighting equipment", "trait_tags": {"Maritime-Sea": 0.8, "Technical-Skill": 0.5, "Mechanical-Design": 0.3}},
            {"option_id": 4052, "option_text": "Leading realistic emergency drills on board", "trait_tags": {"Maritime-Sea": 1.0, "People-Skill": 0.5, "Physical-Skill": 0.3}}
        ]
    },
    {
        "question_id": 455,
        "question_text": "Which maritime environmental concern would you want to address?",
        "weight": 1.5,
        "trait_tags": {"Maritime-Sea": 0.9, "Environmental-Sci": 0.4},
        "options": [
            {"option_id": 4053, "option_text": "Preventing oil spills and chemical leaks at sea", "trait_tags": {"Maritime-Sea": 0.9, "Environmental-Sci": 0.6, "Technical-Skill": 0.3}},
            {"option_id": 4054, "option_text": "Managing ballast water to stop invasive species", "trait_tags": {"Maritime-Sea": 1.0, "Environmental-Sci": 0.5, "Lab-Research": 0.3}},
            {"option_id": 4055, "option_text": "Reducing ship emissions and carbon footprint", "trait_tags": {"Maritime-Sea": 0.9, "Environmental-Eng": 0.5, "Technical-Skill": 0.3}},
            {"option_id": 4056, "option_text": "Protecting marine wildlife from shipping traffic", "trait_tags": {"Maritime-Sea": 0.9, "Environmental-Sci": 0.5, "Field-Research": 0.3}},
            {"option_id": 4057, "option_text": "Proper waste and sewage disposal at sea", "trait_tags": {"Maritime-Sea": 1.0, "Environmental-Sci": 0.4, "Industrial-Ops": 0.3}},
            {"option_id": 4058, "option_text": "Protecting Philippine coral reefs near ports", "trait_tags": {"Maritime-Sea": 0.9, "Environmental-Sci": 0.5, "Community-Serve": 0.3}}
        ]
    },
    {
        "question_id": 456,
        "question_text": "What maritime leadership role do you aspire to long-term?",
        "weight": 1.5,
        "trait_tags": {"Maritime-Sea": 0.9, "People-Skill": 0.3},
        "options": [
            {"option_id": 4059, "option_text": "Commanding your own vessel as ship master", "trait_tags": {"Maritime-Sea": 1.0, "People-Skill": 0.5, "Analytical-Skill": 0.3}},
            {"option_id": 4060, "option_text": "Managing a ship\u2019s entire engineering department", "trait_tags": {"Maritime-Sea": 0.9, "Mechanical-Design": 0.5, "Admin-Skill": 0.4}},
            {"option_id": 4061, "option_text": "Directing operations at a major Philippine port", "trait_tags": {"Maritime-Sea": 0.9, "Admin-Skill": 0.5, "Industrial-Ops": 0.4}},
            {"option_id": 4062, "option_text": "Leading a Philippine maritime training academy", "trait_tags": {"Maritime-Sea": 0.8, "Teaching-Ed": 0.6, "Admin-Skill": 0.4}},
            {"option_id": 4063, "option_text": "Heading a Philippine Coast Guard division", "trait_tags": {"Maritime-Sea": 0.9, "Law-Enforce": 0.5, "People-Skill": 0.4}},
            {"option_id": 4064, "option_text": "Running a maritime regulatory or classification agency", "trait_tags": {"Maritime-Sea": 0.8, "Legal-Practice": 0.5, "Admin-Skill": 0.5}}
        ]
    },
]

# QUESTION_TREE_NODES branches for new questions
NEW_TREE_NODES = {
    443: {"level": 2, "weight": 1.5, "branches": ["maritime"]},
    444: {"level": 2, "weight": 1.5, "branches": ["maritime"]},
    445: {"level": 2, "weight": 1.5, "branches": ["maritime", "physical"]},
    446: {"level": 2, "weight": 1.5, "branches": ["maritime", "technology"]},
    447: {"level": 2, "weight": 1.5, "branches": ["maritime"]},
    448: {"level": 2, "weight": 1.5, "branches": ["maritime", "law"]},
    449: {"level": 2, "weight": 1.5, "branches": ["maritime", "engineering"]},
    450: {"level": 2, "weight": 1.5, "branches": ["maritime"]},
    451: {"level": 2, "weight": 1.5, "branches": ["maritime"]},
    452: {"level": 2, "weight": 1.5, "branches": ["maritime", "technology"]},
    453: {"level": 2, "weight": 1.5, "branches": ["maritime", "business"]},
    454: {"level": 2, "weight": 1.5, "branches": ["maritime", "law"]},
    455: {"level": 2, "weight": 1.5, "branches": ["maritime", "science"]},
    456: {"level": 2, "weight": 1.5, "branches": ["maritime"]},
}


def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # ─── Guard: check if already applied ───
    with open("questions_enhanced.py", "r", encoding="utf-8") as f:
        qe_content = f.read()
    if '"question_id": 443' in qe_content:
        print("Q443 already exists — skipping question insertion.")
    else:
        # ─── 1. Insert new questions into questions_enhanced.py ───
        # Find the last question's closing brace + the list close
        # Pattern: last },\n] before TRAIT_SECONDARY_MAP
        insert_point = qe_content.rfind("\n]\n\nTRAIT_SECONDARY_MAP")
        if insert_point == -1:
            insert_point = qe_content.rfind("\n]\n\nTRAIT_SECONDARY")
        if insert_point == -1:
            print("ERROR: Could not find insertion point in questions_enhanced.py")
            sys.exit(1)

        # Build the text for new questions
        lines = []
        lines.append("    # ==================== MARITIME DEDICATED QUESTIONS (Q443-Q456) ====================")
        for q in NEW_QUESTIONS:
            lines.append("    {")
            lines.append(f'        "question_id": {q["question_id"]},')
            lines.append(f'        "question_text": {repr(q["question_text"])},')
            lines.append(f'        "weight": {q["weight"]},')
            lines.append(f'        "trait_tags": {q["trait_tags"]},')
            lines.append('        "options": [')
            for opt in q["options"]:
                lines.append(f'            {{"option_id": {opt["option_id"]}, "option_text": {repr(opt["option_text"])}, "trait_tags": {opt["trait_tags"]}}},')
            lines.append("        ]")
            lines.append("    },")

        insert_text = "\n" + "\n".join(lines)
        # Insert before the closing ] of QUESTIONS_POOL_ENHANCED
        new_content = qe_content[:insert_point] + insert_text + qe_content[insert_point:]
        with open("questions_enhanced.py", "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Added {len(NEW_QUESTIONS)} maritime questions (Q443-Q456)")

    # ─── 2. Now import the modules to compute on-topic ordering ───
    # Need fresh import after file modification
    import importlib
    if "questions_enhanced" in sys.modules:
        del sys.modules["questions_enhanced"]
    if "adaptive_assessment" in sys.modules:
        del sys.modules["adaptive_assessment"]

    from questions_enhanced import QUESTIONS_POOL_ENHANCED
    q_lookup = {q["question_id"]: q for q in QUESTIONS_POOL_ENHANCED}
    print(f"Total questions loaded: {len(QUESTIONS_POOL_ENHANCED)}")

    # ─── 3. Read adaptive_assessment.py ───
    with open("adaptive_assessment.py", "r", encoding="utf-8") as f:
        aa_content = f.read()

    # ─── 4. Add new questions to QUESTION_TREE_NODES ───
    tree_marker = "QUESTION_TREE_NODES = {"
    if "443:" not in aa_content.split("QUESTION_TREE_NODES")[1][:5000] if "QUESTION_TREE_NODES" in aa_content else True:
        # Find end of QUESTION_TREE_NODES dict - look for the closing }
        tree_start = aa_content.find(tree_marker)
        if tree_start != -1:
            # Find the closing brace of QUESTION_TREE_NODES
            brace_depth = 0
            pos = tree_start + len(tree_marker)
            while pos < len(aa_content):
                if aa_content[pos] == '{':
                    brace_depth += 1
                elif aa_content[pos] == '}':
                    if brace_depth == 0:
                        # Insert before closing }
                        insert_lines = []
                        for qid, node in NEW_TREE_NODES.items():
                            insert_lines.append(f'    {qid}: {{"level": {node["level"]}, "weight": {node["weight"]}, "branches": {node["branches"]}}},')
                        tree_insert = "\n" + "\n".join(insert_lines) + "\n"
                        aa_content = aa_content[:pos] + tree_insert + aa_content[pos:]
                        print(f"Added {len(NEW_TREE_NODES)} entries to QUESTION_TREE_NODES")
                        break
                    brace_depth -= 1
                pos += 1
    else:
        print("Q443 already in QUESTION_TREE_NODES — skipping")

    # ─── 5. Compute on-topic scores and reorder TRAIT_FOLLOWUP_MAP ───
    # Extract current TRAIT_FOLLOWUP_MAP
    tfm_match = re.search(r'TRAIT_FOLLOWUP_MAP\s*=\s*\{', aa_content)
    if not tfm_match:
        print("ERROR: Could not find TRAIT_FOLLOWUP_MAP")
        sys.exit(1)

    tfm_start = tfm_match.start()
    # Find matching closing brace
    brace_depth = 0
    pos = tfm_match.end()
    while pos < len(aa_content):
        if aa_content[pos] == '{':
            brace_depth += 1
        elif aa_content[pos] == '}':
            if brace_depth == 0:
                tfm_end = pos + 1
                break
            brace_depth -= 1
        pos += 1

    # Parse TRAIT_FOLLOWUP_MAP using exec
    tfm_text = aa_content[tfm_match.start():tfm_end]
    local_ns = {}
    exec(tfm_text, {}, local_ns)
    current_tfm = local_ns["TRAIT_FOLLOWUP_MAP"]
    print(f"Loaded TRAIT_FOLLOWUP_MAP with {len(current_tfm)} traits")

    # Add new maritime questions to Maritime-Sea if not present
    maritime_list = list(current_tfm.get("Maritime-Sea", []))
    new_ids = [q["question_id"] for q in NEW_QUESTIONS]
    for qid in new_ids:
        if qid not in maritime_list:
            maritime_list.append(qid)
    current_tfm["Maritime-Sea"] = maritime_list

    # Compute on-topic score for each (question, trait) pair
    def compute_ontopic_score(qid, trait):
        """Higher = more on-topic. Based on average trait weight across options."""
        q = q_lookup.get(qid)
        if not q:
            return 0
        total = 0
        for opt in q["options"]:
            total += opt.get("trait_tags", {}).get(trait, 0)
        avg = total / max(len(q["options"]), 1)

        # Also check if trait is the PRIMARY (highest max) trait for this question
        trait_maxes = {}
        for opt in q["options"]:
            for t, v in opt.get("trait_tags", {}).items():
                if t not in trait_maxes or v > trait_maxes[t]:
                    trait_maxes[t] = v
        is_primary = trait_maxes and max(trait_maxes, key=trait_maxes.get) == trait

        # Score: primary questions get a big boost
        score = avg + (10.0 if is_primary else 0)
        return score

    # Reorder each trait's list: on-topic first, then cross-referenced
    reordered_tfm = {}
    for trait, qids in sorted(current_tfm.items()):
        scored = [(qid, compute_ontopic_score(qid, trait)) for qid in qids]
        scored.sort(key=lambda x: -x[1])  # Highest score first
        reordered_tfm[trait] = [qid for qid, _ in scored]

    # Build new TRAIT_FOLLOWUP_MAP text
    tfm_lines = ["TRAIT_FOLLOWUP_MAP = {"]
    for trait in sorted(reordered_tfm.keys()):
        qids = reordered_tfm[trait]
        tfm_lines.append(f'    "{trait}": {qids},')
    tfm_lines.append("}")
    new_tfm_text = "\n".join(tfm_lines)

    # Replace in file
    aa_content = aa_content[:tfm_start] + new_tfm_text + aa_content[tfm_end:]
    print("Reordered TRAIT_FOLLOWUP_MAP — on-topic questions first for all traits")

    # ─── 6. Write adaptive_assessment.py ───
    with open("adaptive_assessment.py", "w", encoding="utf-8") as f:
        f.write(aa_content)
    print("Updated adaptive_assessment.py")

    # ─── 7. Validate ───
    # Reload with changes
    if "adaptive_assessment" in sys.modules:
        del sys.modules["adaptive_assessment"]
    from adaptive_assessment import TRAIT_FOLLOWUP_MAP as new_tfm, QUESTION_TREE_NODES as new_tree

    # Check maritime
    m_ids = new_tfm.get("Maritime-Sea", [])
    m_ontopic = 0
    for qid in m_ids[:30]:
        q = q_lookup.get(qid)
        if not q:
            continue
        trait_maxes = {}
        for opt in q["options"]:
            for t, v in opt.get("trait_tags", {}).items():
                if t not in trait_maxes or v > trait_maxes[t]:
                    trait_maxes[t] = v
        if trait_maxes and max(trait_maxes, key=trait_maxes.get) == "Maritime-Sea":
            m_ontopic += 1
    print(f"\nMaritime-Sea: {m_ontopic}/30 first questions are on-topic (was 16)")

    # Check all traits
    under_10 = {}
    for trait, qids in new_tfm.items():
        ontopic = 0
        for qid in qids[:30]:
            q = q_lookup.get(qid)
            if not q:
                continue
            trait_maxes = {}
            for opt in q["options"]:
                for t, v in opt.get("trait_tags", {}).items():
                    if t not in trait_maxes or v > trait_maxes[t]:
                        trait_maxes[t] = v
            if trait_maxes and max(trait_maxes, key=trait_maxes.get) == trait:
                ontopic += 1
        if ontopic < 10:
            under_10[trait] = ontopic

    if under_10:
        print(f"\nTraits still under 10 on-topic (need more dedicated questions):")
        for t, c in sorted(under_10.items(), key=lambda x: x[1]):
            print(f"  {t}: {c}")
    else:
        print("\nAll traits have 10+ on-topic questions in first 30!")

    # Verify new questions in tree
    missing = [qid for qid in new_ids if qid not in new_tree]
    if missing:
        print(f"WARNING: Missing from tree: {missing}")
    else:
        print(f"All Q443-Q456 in QUESTION_TREE_NODES")


if __name__ == "__main__":
    main()
