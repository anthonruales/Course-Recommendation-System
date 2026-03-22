"""
Fix script: Ensure every option in questions_enhanced.py has at least 4 trait_tags.

Uses SPECIALIZED_TRAIT_RELATIONSHIPS to add contextually appropriate traits.
For each option with < 4 traits, we find related traits from the existing ones
and add them with appropriate lower weights.
"""
import sys, os, re, ast, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from services.trait_system import SPECIALIZED_TRAIT_RELATIONSHIPS

# All valid traits
ALL_VALID_TRAITS = set()
for category in [
    ["Realistic", "Investigative", "Artistic", "Social", "Enterprising", "Conventional"],
    ["Patient-Care", "Medical-Lab", "Rehab-Therapy", "Health-Admin", "Pharmacy", "Public-Health", "Nutrition-Diet"],
    ["Software-Dev", "Hardware-Systems", "Data-Analytics", "Cyber-Defense", "Web-Dev", "Mobile-Dev", "Game-Dev", "AI-ML", "Cloud-Systems"],
    ["Civil-Build", "Electrical-Power", "Mechanical-Design", "Industrial-Ops", "Environmental-Eng"],
    ["Finance-Acct", "Marketing-Sales", "Startup-Venture", "HR-Management"],
    ["Teaching-Ed", "Counseling", "Sports-Ed"],
    ["Visual-Design", "Digital-Media", "Spatial-Design", "Performing-Arts", "Film-Broadcast", "Animation-3D"],
    ["Lab-Research", "Field-Research", "Environmental-Sci", "Food-Science", "Forensic-Sci"],
    ["Law-Enforce", "Community-Serve", "Legal-Practice", "Social-Work"],
    ["Maritime-Sea"],
    ["Agri-Nature"],
    ["Hospitality-Svc", "Tourism-Travel", "Culinary-Arts"],
    ["Technical-Skill", "People-Skill", "Creative-Skill", "Analytical-Skill", "Physical-Skill", "Admin-Skill"],
]:
    ALL_VALID_TRAITS.update(category)


def get_related_traits(existing_traits: dict, min_total: int = 4) -> dict:
    """Given existing trait_tags, add related traits to reach min_total."""
    result = dict(existing_traits)
    needed = min_total - len(result)
    if needed <= 0:
        return result
    
    # Collect candidate traits from relationships of existing traits
    candidates = {}  # trait -> best_score
    for trait, weight in sorted(existing_traits.items(), key=lambda x: -x[1]):
        if trait in SPECIALIZED_TRAIT_RELATIONSHIPS:
            for related, rel_strength in SPECIALIZED_TRAIT_RELATIONSHIPS[trait].items():
                if related not in result and related in ALL_VALID_TRAITS:
                    # Score = existing weight * relationship strength * dampening
                    score = round(weight * rel_strength * 0.35, 2)
                    score = max(0.1, min(0.3, score))  # Clamp between 0.1 and 0.3
                    if related not in candidates or candidates[related] < score:
                        candidates[related] = score
    
    # Sort candidates by score descending, pick top N needed
    sorted_candidates = sorted(candidates.items(), key=lambda x: -x[1])
    
    for trait, score in sorted_candidates[:needed]:
        result[trait] = score
    
    # If still not enough (unlikely), add RIASEC type based on domain
    remaining = min_total - len(result)
    if remaining > 0:
        # Fallback: add common RIASEC types based on dominant trait
        riasec_fallbacks = {
            "Patient-Care": ["Social", "Investigative", "Conventional"],
            "Medical-Lab": ["Investigative", "Realistic", "Conventional"],
            "Rehab-Therapy": ["Social", "Realistic", "Investigative"],
            "Health-Admin": ["Conventional", "Enterprising", "Social"],
            "Software-Dev": ["Investigative", "Realistic", "Conventional"],
            "Hardware-Systems": ["Realistic", "Investigative", "Conventional"],
            "Data-Analytics": ["Investigative", "Conventional", "Realistic"],
            "Cyber-Defense": ["Investigative", "Realistic", "Conventional"],
            "Web-Dev": ["Investigative", "Artistic", "Realistic"],
            "Mobile-Dev": ["Investigative", "Realistic", "Artistic"],
            "Game-Dev": ["Artistic", "Investigative", "Realistic"],
            "AI-ML": ["Investigative", "Realistic", "Conventional"],
            "Cloud-Systems": ["Investigative", "Realistic", "Conventional"],
            "Civil-Build": ["Realistic", "Investigative", "Conventional"],
            "Electrical-Power": ["Realistic", "Investigative", "Conventional"],
            "Mechanical-Design": ["Realistic", "Investigative", "Conventional"],
            "Industrial-Ops": ["Enterprising", "Conventional", "Realistic"],
            "Environmental-Eng": ["Realistic", "Investigative", "Social"],
            "Finance-Acct": ["Conventional", "Enterprising", "Investigative"],
            "Marketing-Sales": ["Enterprising", "Social", "Artistic"],
            "Startup-Venture": ["Enterprising", "Social", "Artistic"],
            "HR-Management": ["Social", "Enterprising", "Conventional"],
            "Teaching-Ed": ["Social", "Artistic", "Investigative"],
            "Counseling": ["Social", "Investigative", "Artistic"],
            "Sports-Ed": ["Social", "Realistic", "Enterprising"],
            "Visual-Design": ["Artistic", "Investigative", "Social"],
            "Digital-Media": ["Artistic", "Investigative", "Social"],
            "Spatial-Design": ["Artistic", "Realistic", "Investigative"],
            "Performing-Arts": ["Artistic", "Social", "Enterprising"],
            "Film-Broadcast": ["Artistic", "Investigative", "Social"],
            "Animation-3D": ["Artistic", "Investigative", "Realistic"],
            "Lab-Research": ["Investigative", "Realistic", "Conventional"],
            "Field-Research": ["Investigative", "Realistic", "Social"],
            "Environmental-Sci": ["Investigative", "Realistic", "Social"],
            "Food-Science": ["Investigative", "Realistic", "Conventional"],
            "Forensic-Sci": ["Investigative", "Realistic", "Conventional"],
            "Law-Enforce": ["Realistic", "Social", "Enterprising"],
            "Community-Serve": ["Social", "Enterprising", "Conventional"],
            "Legal-Practice": ["Enterprising", "Conventional", "Social"],
            "Social-Work": ["Social", "Investigative", "Artistic"],
            "Maritime-Sea": ["Realistic", "Investigative", "Conventional"],
            "Agri-Nature": ["Realistic", "Investigative", "Social"],
            "Hospitality-Svc": ["Enterprising", "Social", "Conventional"],
            "Tourism-Travel": ["Enterprising", "Social", "Artistic"],
            "Culinary-Arts": ["Artistic", "Realistic", "Social"],
            "Technical-Skill": ["Realistic", "Investigative", "Conventional"],
            "People-Skill": ["Social", "Enterprising", "Artistic"],
            "Creative-Skill": ["Artistic", "Investigative", "Social"],
            "Analytical-Skill": ["Investigative", "Conventional", "Realistic"],
            "Physical-Skill": ["Realistic", "Social", "Enterprising"],
            "Admin-Skill": ["Conventional", "Enterprising", "Social"],
            "Pharmacy": ["Investigative", "Realistic", "Conventional"],
            "Public-Health": ["Social", "Investigative", "Conventional"],
            "Nutrition-Diet": ["Investigative", "Social", "Realistic"],
        }
        
        # Find dominant trait (highest weight)
        dominant = max(existing_traits, key=existing_traits.get)
        fallbacks = riasec_fallbacks.get(dominant, ["Investigative", "Social", "Realistic"])
        
        for fb_trait in fallbacks:
            if fb_trait not in result and remaining > 0:
                result[fb_trait] = 0.15
                remaining -= 1
    
    return result


def fix_questions_enhanced():
    filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'questions_enhanced.py')
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Track stats
    total_fixed = 0
    total_options_fixed = 0
    zero_trait_fixed = 0
    
    # We need to find all trait_tags dicts and augment them
    # Pattern: "trait_tags": {'key': val, 'key': val, ...}
    # We'll use a regex to find trait_tags patterns and replace them
    
    # Strategy: parse the file, find all option trait_tags with < 4 entries, fix them
    
    # Find all trait_tags in option lines (not question-level trait_tags)
    # Option trait_tags are in lines like: {"option_id": ..., "option_text": ..., "trait_tags": {...}}
    
    pattern = re.compile(
        r'("option_id":\s*\d+.*?"trait_tags":\s*)(\{[^}]*\})',
        re.DOTALL
    )
    
    def replace_trait_tags(match):
        nonlocal total_options_fixed, zero_trait_fixed
        prefix = match.group(1)
        trait_dict_str = match.group(2)
        
        try:
            # Parse the dict - convert single quotes to double for json, or use ast
            trait_dict = ast.literal_eval(trait_dict_str)
        except:
            return match.group(0)  # Can't parse, skip
        
        if len(trait_dict) >= 4:
            return match.group(0)  # Already has enough traits
        
        if len(trait_dict) == 0:
            zero_trait_fixed += 1
            # For 0-trait options, we can't infer from existing. Skip or add generic.
            # Actually let's return them as-is since they're a separate issue
            return match.group(0)
        
        # Fix: add related traits
        fixed = get_related_traits(trait_dict, min_total=4)
        total_options_fixed += 1
        
        # Format the dict nicely - match original format using single quotes
        items = []
        for k, v in fixed.items():
            items.append(f"'{k}': {v}")
        new_dict_str = '{' + ', '.join(items) + '}'
        
        return prefix + new_dict_str
    
    new_content = pattern.sub(replace_trait_tags, content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Fixed {total_options_fixed} options (added traits to reach 4+)")
    print(f"Skipped {zero_trait_fixed} options with 0 traits (separate issue)")
    

if __name__ == '__main__':
    fix_questions_enhanced()
