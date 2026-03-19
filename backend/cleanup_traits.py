"""
Cleanup script for QUESTIONS_POOL_ENHANCED trait assignments.

Goals:
1. Remove obviously irrelevant cross-domain traits from options
2. Cap each option at 6 traits max (primary + 5 secondary)
3. Regenerate TRAIT_SECONDARY_MAP from cleaned data
4. Write cleaned data back to questions_enhanced.py
"""
import sys
import json
import re
import copy

# Import the original data
from questions_enhanced import QUESTIONS_POOL_ENHANCED

# ==============================================================================
# DOMAIN GROUPINGS - traits that belong to the same domain family
# ==============================================================================
DOMAIN_GROUPS = {
    "healthcare": {"Patient-Care", "Medical-Lab", "Rehab-Therapy", "Health-Admin", "Pharmacy", "Public-Health", "Nutrition-Diet"},
    "technology": {"Software-Dev", "Web-Dev", "Mobile-Dev", "Game-Dev", "AI-ML", "Data-Analytics", "Cloud-Systems", "Cyber-Defense", "Hardware-Systems", "Electronics-Dev"},
    "engineering": {"Mechanical-Design", "Civil-Build", "Industrial-Ops", "Electrical-Power", "Aeronautical-Eng"},
    "business": {"Finance-Acct", "Marketing-Sales", "Startup-Venture", "Admin-Skill", "HR-Management"},
    "education": {"Teaching-Ed", "Counseling"},
    "arts": {"Visual-Design", "Artistic", "Performing-Arts", "Animation-3D", "Film-Broadcast", "Digital-Media", "Creative-Skill"},
    "public_service": {"Law-Enforce", "Legal-Practice", "Forensic-Sci", "Community-Serve", "Social-Work"},
    "maritime": {"Maritime-Sea"},
    "agriculture": {"Agri-Nature", "Environmental-Sci", "Environmental-Eng"},
    "hospitality": {"Hospitality-Svc", "Tourism-Travel", "Culinary-Arts"},
    "science": {"Lab-Research", "Field-Research", "Food-Science"},
}

# Holland codes and generic skills - these are "universal" and can pair with anything
UNIVERSAL_TRAITS = {
    "Realistic", "Investigative", "Artistic", "Social", "Enterprising", "Conventional",
    "People-Skill", "Technical-Skill", "Analytical-Skill", "Physical-Skill", 
    "Creative-Skill", "Spatial-Design",
}

# ==============================================================================
# CROSS-DOMAIN EXCLUSION RULES
# Map: primary domain -> set of domains whose traits should NOT appear as secondary
# (unless the option text explicitly suggests a cross-domain activity)
# ==============================================================================
DOMAIN_EXCLUSIONS = {
    "healthcare": {"maritime", "agriculture", "engineering"},
    "technology": {"maritime", "agriculture", "healthcare", "hospitality"},
    "engineering": {"healthcare", "maritime", "hospitality", "arts"},
    "business": {"maritime", "healthcare", "engineering"},
    "education": {"maritime", "engineering", "technology"},
    "arts": {"maritime", "agriculture", "healthcare", "engineering"},
    "public_service": {"maritime", "agriculture", "hospitality", "arts"},
    "maritime": {"healthcare", "technology", "arts", "education", "business"},
    "agriculture": {"technology", "maritime", "arts", "healthcare"},
    "hospitality": {"technology", "engineering", "healthcare", "maritime"},
    "science": {"maritime", "arts", "hospitality", "business"},
}

def get_domain(trait):
    """Get the domain group a trait belongs to"""
    for domain, traits in DOMAIN_GROUPS.items():
        if trait in traits:
            return domain
    return None

def get_primary_domain(trait_tags):
    """Get the domain of the primary trait (weight 1.0)"""
    for trait, weight in trait_tags.items():
        if weight >= 1.0:
            domain = get_domain(trait)
            if domain:
                return domain
    return None

def is_trait_excluded(primary_domain, secondary_trait):
    """Check if a secondary trait should be excluded based on domain rules"""
    if secondary_trait in UNIVERSAL_TRAITS:
        return False  # Universal traits are always OK
    
    secondary_domain = get_domain(secondary_trait)
    if secondary_domain is None:
        return False  # Unknown domain, keep it
    
    if secondary_domain == primary_domain:
        return False  # Same domain, always OK
    
    excluded_domains = DOMAIN_EXCLUSIONS.get(primary_domain, set())
    return secondary_domain in excluded_domains

def clean_option_traits(trait_tags, option_text="", max_traits=6):
    """Clean trait assignments for a single option"""
    if not isinstance(trait_tags, dict) or len(trait_tags) == 0:
        return trait_tags
    
    # Find primary trait domain
    primary_domain = get_primary_domain(trait_tags)
    
    # Step 1: Remove excluded cross-domain traits (only for low-weight ones)
    cleaned = {}
    for trait, weight in trait_tags.items():
        if weight >= 1.0:
            # Always keep primary trait
            cleaned[trait] = weight
        elif weight >= 0.6:
            # High-weight secondaries: keep even if cross-domain (intentional)
            cleaned[trait] = weight
        elif primary_domain and is_trait_excluded(primary_domain, trait):
            # Low-weight cross-domain: remove
            continue
        else:
            cleaned[trait] = weight
    
    # Step 2: Cap at max_traits (keep highest weights)
    if len(cleaned) > max_traits:
        sorted_traits = sorted(cleaned.items(), key=lambda x: -x[1])
        cleaned = dict(sorted_traits[:max_traits])
    
    return cleaned


def main():
    # Deep copy to avoid modifying the imported data
    questions = copy.deepcopy(QUESTIONS_POOL_ENHANCED)
    
    total_options = 0
    total_traits_before = 0
    total_traits_after = 0
    traits_removed = 0
    exclusion_removals = 0
    cap_removals = 0
    
    for q in questions:
        for opt in q.get("options", []):
            trait_tags = opt.get("trait_tags", {})
            if not isinstance(trait_tags, dict):
                continue
            
            total_options += 1
            before_count = len(trait_tags)
            total_traits_before += before_count
            
            # Track exclusion removals vs cap removals
            primary_domain = get_primary_domain(trait_tags)
            excluded_count = 0
            if primary_domain:
                for trait, weight in trait_tags.items():
                    if weight < 0.6 and weight < 1.0 and is_trait_excluded(primary_domain, trait):
                        excluded_count += 1
            
            cleaned = clean_option_traits(trait_tags, opt.get("option_text", ""))
            after_count = len(cleaned)
            total_traits_after += after_count
            
            removed = before_count - after_count
            traits_removed += removed
            exclusion_removals += min(excluded_count, removed)
            cap_removals += max(0, removed - excluded_count)
            
            opt["trait_tags"] = cleaned
    
    print(f"=== Cleanup Summary ===")
    print(f"Total options: {total_options}")
    print(f"Total traits before: {total_traits_before} (avg {total_traits_before/total_options:.1f})")
    print(f"Total traits after: {total_traits_after} (avg {total_traits_after/total_options:.1f})")
    print(f"Total traits removed: {traits_removed}")
    print(f"  - Cross-domain exclusions: ~{exclusion_removals}")
    print(f"  - Cap removals: ~{cap_removals}")
    
    # Show some sample cleaned options
    print(f"\n=== Sample cleaned options ===")
    samples = [
        ("Raising animals", None),
        ("Help patients recover", None),
        ("Coding or building programs", None),
        ("Gaming", None),
        ("Managing budgets", None),
        ("Creating ads and marketing", None),
    ]
    for search_text, _ in samples:
        for q in questions:
            for opt in q.get("options", []):
                if search_text.lower() in opt.get("option_text", "").lower():
                    tags = sorted(opt["trait_tags"].items(), key=lambda x: -x[1])
                    print(f'Q{q["question_id"]} "{opt["option_text"][:60]}"')
                    print(f"  Traits ({len(tags)}): {tags}")
                    print()
                    break
            else:
                continue
            break
    
    # Now write to file
    print("\nWriting cleaned data to questions_enhanced.py...")
    
    with open("questions_enhanced.py", "r", encoding="utf-8") as f:
        content = f.read()
    
    # Find the start and end of QUESTIONS_POOL_ENHANCED
    # It starts at "QUESTIONS_POOL_ENHANCED = [" and ends before "TRAIT_SECONDARY_MAP"
    # We need to find where the list ends
    
    # Strategy: find the line "QUESTIONS_POOL_ENHANCED = [" and the line just before
    # "TRAIT_SECONDARY_MAP = {", then replace everything in between
    
    lines = content.split("\n")
    
    # Find start of QUESTIONS_POOL_ENHANCED (the variable assignment line)
    q_start = None
    for i, line in enumerate(lines):
        if line.strip().startswith("QUESTIONS_POOL_ENHANCED") and "=" in line:
            q_start = i
            break
    
    # Find start of TRAIT_SECONDARY_MAP
    t_start = None
    for i, line in enumerate(lines):
        if line.strip().startswith("TRAIT_SECONDARY_MAP") and "=" in line:
            t_start = i
            break
    
    if q_start is None or t_start is None:
        print("ERROR: Could not find section boundaries!")
        sys.exit(1)
    
    print(f"  QUESTIONS_POOL_ENHANCED starts at line {q_start + 1}")
    print(f"  TRAIT_SECONDARY_MAP starts at line {t_start + 1}")
    
    # Find the end of QUESTIONS_POOL_ENHANCED (the closing bracket before TRAIT_SECONDARY_MAP)
    # Look backwards from t_start for the closing "]"
    q_end = None
    for i in range(t_start - 1, q_start, -1):
        stripped = lines[i].strip()
        if stripped == "]" or stripped == "];":
            q_end = i
            break
    
    if q_end is None:
        print("ERROR: Could not find end of QUESTIONS_POOL_ENHANCED!")
        sys.exit(1)
    
    print(f"  QUESTIONS_POOL_ENHANCED ends at line {q_end + 1}")
    
    # Generate the new QUESTIONS_POOL_ENHANCED content
    new_questions_str = generate_questions_string(questions)
    
    # Generate new TRAIT_SECONDARY_MAP from cleaned data
    new_map_str = generate_trait_secondary_map(questions)
    
    # Rebuild the file
    # Header (lines before QUESTIONS_POOL_ENHANCED)
    header = "\n".join(lines[:q_start])
    
    # New content
    new_content = header + "\n" + new_questions_str + "\n\n" + new_map_str + "\n"
    
    with open("questions_enhanced.py", "w", encoding="utf-8") as f:
        f.write(new_content)
    
    # Verify
    new_lines = new_content.split("\n")
    print(f"  File written: {len(new_lines)} lines (was {len(lines)})")
    
    # Verify import works
    import importlib
    import questions_enhanced
    importlib.reload(questions_enhanced)
    print(f"  Import verified: {len(questions_enhanced.QUESTIONS_POOL_ENHANCED)} questions loaded")
    
    # Verify trait counts
    max_traits_after = 0
    for q in questions_enhanced.QUESTIONS_POOL_ENHANCED:
        for opt in q.get("options", []):
            tags = opt.get("trait_tags", {})
            if isinstance(tags, dict):
                max_traits_after = max(max_traits_after, len(tags))
    print(f"  Max traits per option: {max_traits_after}")
    print(f"\nDone!")


def generate_questions_string(questions):
    """Generate the QUESTIONS_POOL_ENHANCED = [...] string"""
    lines = ["QUESTIONS_POOL_ENHANCED = ["]
    
    for qi, q in enumerate(questions):
        lines.append("    {")
        lines.append(f'        "question_id": {q["question_id"]},')
        
        # Escape question text for Python string
        qtext = q["question_text"].replace("\\", "\\\\").replace('"', '\\"')
        lines.append(f'        "question_text": "{qtext}",')
        
        cat = q.get("category", "")
        cat_str = cat.replace("\\", "\\\\").replace('"', '\\"')
        lines.append(f'        "category": "{cat_str}",')
        
        lines.append(f'        "options": [')
        
        for oi, opt in enumerate(q.get("options", [])):
            lines.append("            {")
            lines.append(f'                "option_id": {opt["option_id"]},')
            
            otext = opt["option_text"].replace("\\", "\\\\").replace('"', '\\"')
            lines.append(f'                "option_text": "{otext}",')
            
            tags = opt.get("trait_tags", {})
            if isinstance(tags, dict) and len(tags) > 0:
                # Sort by weight descending for readability
                sorted_tags = sorted(tags.items(), key=lambda x: -x[1])
                tag_parts = [f'"{k}": {v}' for k, v in sorted_tags]
                tag_str = ", ".join(tag_parts)
                lines.append(f'                "trait_tags": {{{tag_str}}}')
            else:
                lines.append(f'                "trait_tags": {{}}')
            
            comma = "," if oi < len(q.get("options", [])) - 1 else ""
            lines.append(f"            }}{comma}")
        
        lines.append("        ]")
        comma = "," if qi < len(questions) - 1 else ""
        lines.append(f"    }}{comma}")
    
    lines.append("]")
    return "\n".join(lines)


def generate_trait_secondary_map(questions):
    """Generate TRAIT_SECONDARY_MAP from the cleaned questions data"""
    # Collect: for each primary trait, what secondary traits appear alongside it?
    primary_to_secondaries = {}
    
    for q in questions:
        for opt in q.get("options", []):
            tags = opt.get("trait_tags", {})
            if not isinstance(tags, dict):
                continue
            
            # Find primary trait (weight 1.0)
            primary = None
            for trait, weight in tags.items():
                if weight >= 1.0:
                    primary = trait
                    break
            
            if primary is None:
                continue
            
            if primary not in primary_to_secondaries:
                primary_to_secondaries[primary] = {}
            
            for trait, weight in tags.items():
                if trait == primary:
                    continue
                # Keep the highest weight seen for this secondary
                if trait not in primary_to_secondaries[primary]:
                    primary_to_secondaries[primary][trait] = weight
                else:
                    primary_to_secondaries[primary][trait] = max(
                        primary_to_secondaries[primary][trait], weight
                    )
    
    # Generate the map string
    lines = ["TRAIT_SECONDARY_MAP = {"]
    for primary in sorted(primary_to_secondaries.keys()):
        secondaries = primary_to_secondaries[primary]
        sorted_secs = sorted(secondaries.items(), key=lambda x: -x[1])
        sec_parts = [f'("{k}", {v})' for k, v in sorted_secs]
        sec_str = ", ".join(sec_parts)
        lines.append(f'    "{primary}": [{sec_str}],')
    lines.append("}")
    
    return "\n".join(lines)


if __name__ == "__main__":
    main()
