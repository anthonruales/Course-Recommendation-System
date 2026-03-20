"""Add category labels to questions Q443-Q774 that are missing them."""
import re

# Trait-to-readable-name mapping for category generation
TRAIT_DISPLAY = {
    "AI-ML": "Artificial Intelligence",
    "Admin-Skill": "Administration",
    "Agri-Nature": "Agriculture",
    "Analytical-Skill": "Analytical Skills",
    "Animation-3D": "Animation & 3D",
    "Civil-Build": "Civil Engineering",
    "Cloud-Systems": "Cloud Computing",
    "Community-Serve": "Community Service",
    "Counseling": "Counseling",
    "Creative-Skill": "Creative Skills",
    "Culinary-Arts": "Culinary Arts",
    "Cyber-Defense": "Cybersecurity",
    "Data-Analytics": "Data Analytics",
    "Digital-Media": "Digital Media",
    "Electrical-Power": "Electrical Engineering",
    "Environmental-Eng": "Environmental Engineering",
    "Environmental-Sci": "Environmental Science",
    "Field-Research": "Field Research",
    "Film-Broadcast": "Film & Broadcast",
    "Finance-Acct": "Finance & Accounting",
    "Food-Science": "Food Science",
    "Forensic-Sci": "Forensic Science",
    "Game-Dev": "Game Development",
    "HR-Management": "Human Resources",
    "Hardware-Systems": "Hardware & Systems",
    "Health-Admin": "Health Administration",
    "Hospitality-Svc": "Hospitality",
    "Industrial-Ops": "Industrial Operations",
    "Lab-Research": "Laboratory Research",
    "Law-Enforce": "Law Enforcement",
    "Legal-Practice": "Legal Practice",
    "Maritime-Sea": "Maritime",
    "Marketing-Sales": "Marketing & Sales",
    "Mechanical-Design": "Mechanical Engineering",
    "Medical-Lab": "Medical Laboratory",
    "Mobile-Dev": "Mobile Development",
    "Nutrition-Diet": "Nutrition & Dietetics",
    "Patient-Care": "Patient Care",
    "People-Skill": "People Skills",
    "Performing-Arts": "Performing Arts",
    "Pharmacy": "Pharmacy",
    "Physical-Skill": "Physical Skills",
    "Public-Health": "Public Health",
    "Rehab-Therapy": "Rehabilitation",
    "Social-Work": "Social Work",
    "Software-Dev": "Software Development",
    "Spatial-Design": "Architecture & Design",
    "Sports-Ed": "Sports & Education",
    "Startup-Venture": "Entrepreneurship",
    "Teaching-Ed": "Teaching & Education",
    "Technical-Skill": "Technical Skills",
    "Tourism-Travel": "Tourism & Travel",
    "Visual-Design": "Visual Design",
    "Web-Dev": "Web Development",
    # Holland types (generic)
    "Realistic": "Practical Skills",
    "Investigative": "Investigative",
    "Artistic": "Creative Arts",
    "Social": "Social Skills",
    "Enterprising": "Enterprising",
    "Conventional": "Organizational Skills",
}

# Keyword-based category type detection from question text
QUESTION_TYPE_PATTERNS = [
    (r'\bwhat (?:would you|will you|do you) do\b', 'Situational'),
    (r'\byou (?:discover|notice|find|encounter|are asked|receive|observe)\b', 'Situational'),
    (r'\bscenario\b', 'Situational'),
    (r'\bimagine\b', 'Situational'),
    (r'\byour (?:school|company|team|organization|community) (?:is|has|faces|needs)\b', 'Situational'),
    (r'\ba colleague|a friend|your boss|your teacher\b', 'Situational'),
    (r'\bhow (?:would you|do you) (?:handle|approach|respond|react|manage|deal)\b', 'Situational'),
    (r'\bwhich (?:area|field|branch|specialization|specialty|sector|aspect|type|kind|form|style|path|track|focus|concentration)\b', 'Interest'),
    (r'\bwhat (?:area|field|branch|specialization|specialty|sector|aspect|type|kind|form|style|path|track|focus|concentration)\b', 'Interest'),
    (r'\bwhat (?:excites|interests|appeals|attracts|fascinates|motivates|inspires|draws) you\b', 'Interest'),
    (r'\bwhich .* (?:excites|interests|appeals|attracts|fascinates|motivates|inspires|draws) you\b', 'Interest'),
    (r'\bmost eager\b', 'Interest'),
    (r'\bwhat .* career\b', 'Career'),
    (r'\bwhat role\b', 'Career'),
    (r'\bwhere (?:would you|do you) (?:see yourself|want to work|prefer)\b', 'Career'),
    (r'\bwhich (?:career|job|profession|role|position)\b', 'Career'),
    (r'\bhow (?:comfortable|confident|skilled)\b', 'Self-Assessment'),
    (r'\brate your\b', 'Self-Assessment'),
    (r'\bhow (?:much|often|well)\b', 'Self-Assessment'),
    (r'\bwhat (?:skill|ability|strength|talent)\b', 'Skill'),
    (r'\bwhich (?:skill|ability|tool|technology|technique|method|approach)\b', 'Preference'),
    (r'\bwhat (?:tool|technology|technique|method|approach)\b', 'Preference'),
    (r'\bprefer\b', 'Preference'),
    (r'\bwhat (?:is|are) your? (?:favorite|preferred)\b', 'Preference'),
    (r'\bwhy (?:did you|do you|would you)\b', 'Motivation'),
    (r'\bwhat (?:motivates|drives|inspires)\b', 'Motivation'),
]


def get_dominant_trait(question):
    """Get the most common high-weight trait across the question's options."""
    trait_scores = {}
    for opt in question['options']:
        for tag, weight in opt['trait_tags'].items():
            if weight >= 0.6:
                trait_scores[tag] = trait_scores.get(tag, 0) + weight
    
    # Also check question-level trait_tags
    for tag, weight in question.get('trait_tags', {}).items():
        if weight >= 0.5:
            trait_scores[tag] = trait_scores.get(tag, 0) + weight * 3  # boost q-level
    
    if not trait_scores:
        # Fallback: use any trait
        for opt in question['options']:
            for tag, weight in opt['trait_tags'].items():
                trait_scores[tag] = trait_scores.get(tag, 0) + weight
    
    if not trait_scores:
        return "General"
    
    return max(trait_scores, key=trait_scores.get)


def get_question_type(question_text):
    """Detect question type from its text using keyword patterns."""
    text_lower = question_text.lower()
    for pattern, qtype in QUESTION_TYPE_PATTERNS:
        if re.search(pattern, text_lower):
            return qtype
    return "Interest"  # default


def generate_category(question):
    """Generate a category string like 'Interest - Maritime' or 'Situational - Cybersecurity'."""
    trait = get_dominant_trait(question)
    qtype = get_question_type(question['question_text'])
    domain_name = TRAIT_DISPLAY.get(trait, trait.replace('-', ' ').title())
    return f"{qtype} - {domain_name}"


def main():
    filepath = "questions_enhanced.py"
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Import the data to analyze questions
    from questions_enhanced import QUESTIONS_POOL_ENHANCED
    
    # Build category map for questions missing category
    categories = {}
    for q in QUESTIONS_POOL_ENHANCED:
        if 'category' not in q or not q.get('category'):
            qid = q['question_id']
            cat = generate_category(q)
            categories[qid] = cat
    
    print(f"Need to add categories to {len(categories)} questions")
    
    # Now patch the file: for each question missing category, insert it after question_text line
    changes = 0
    for qid, cat in categories.items():
        # Find the question_text line for this question_id
        # Pattern: "question_id": <qid>, followed by "question_text": "...",
        # We insert "category": "..." after "question_text" line
        
        # Look for the question_id definition
        pattern = rf'("question_id":\s*{qid},\s*\n\s*"question_text":\s*["\'].+?["\'],)\s*\n'
        match = re.search(pattern, content)
        if match:
            # Insert category after question_text line
            old_text = match.group(0)
            indent = re.search(r'^(\s*)', old_text.split('\n')[0]).group(1)
            new_text = old_text.rstrip('\n') + f'\n{indent}"category": "{cat}",\n'
            content = content.replace(old_text, new_text, 1)
            changes += 1
        else:
            # Try alternative: question_text might span or have weight after it
            pattern2 = rf'("question_id":\s*{qid},\s*\n\s*"question_text":\s*["\'].+?["\'],\s*\n\s*"weight":\s*[\d.]+,)\s*\n'
            match2 = re.search(pattern2, content)
            if match2:
                old_text = match2.group(0)
                indent = re.search(r'^(\s*)', old_text.split('\n')[0]).group(1)
                new_text = old_text.rstrip('\n') + f'\n{indent}"category": "{cat}",\n'
                content = content.replace(old_text, new_text, 1)
                changes += 1
            else:
                # Try: question_text then trait_tags on next line
                pattern3 = rf'("question_id":\s*{qid},\s*\n\s*"question_text":\s*["\'].+?["\'],\s*\n\s*"trait_tags":)'
                match3 = re.search(pattern3, content)
                if match3:
                    old_text = match3.group(0)
                    # Insert category before trait_tags
                    parts = old_text.rsplit('"trait_tags":', 1)
                    indent = re.search(r'^(\s*)', parts[0].split('\n')[0]).group(1)
                    new_text = parts[0] + f'"category": "{cat}",\n{indent}"trait_tags":' + (parts[1] if len(parts) > 1 else '')
                    content = content.replace(old_text, new_text, 1)
                    changes += 1
                else:
                    print(f"  WARNING: Could not find Q{qid} pattern in file")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"Added categories to {changes} questions")
    
    # Quick sample of what was assigned
    sample_ids = [443, 450, 500, 550, 600, 650, 700, 750, 774]
    for qid in sample_ids:
        if qid in categories:
            print(f"  Q{qid}: {categories[qid]}")


if __name__ == "__main__":
    main()
