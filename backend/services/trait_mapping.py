"""
Trait Mapping System - Consolidates similar traits to improve matching accuracy
Maps rare/specific course traits to existing question traits
"""

# Trait consolidation map: course_trait -> question_trait
TRAIT_MAPPING = {
    # Data & Analysis
    "Data-driven": "Quantitative",
    "Data-management": "Organized",
    "Decision-support": "Analytical",
    
    # Critical Thinking
    "Critical-thinking": "Analytical",  # Will be added in questions but also mapped
    "Complex-systems": "Analytical",
    "Experimental": "Investigative",
    
    # Professional Skills
    "Compliance": "Organized",
    "Compliance-oriented": "Methodical",
    "Efficiency-driven": "Strategic",
    "Process-optimization": "Methodical",
    
    # Communication & Social
    "Expressive": "Articulate",
    "Diplomatic": "Collaborative",
    "Debating": "Argumentative",
    "Confident": "Leadership",
    "Encouraging": "Mentoring",
    
    # Clinical & Healthcare
    "Clinical-science": "Laboratory",
    "Bio-science": "Biological",
    "Clinical-setting": "Patient-focused",
    "Patient-interaction": "Patient-focused",  # Will be added but also mapped for backward compatibility
    
    # Business & Finance
    "Business": "Business-minded",
    "Brand-thinking": "Creative-expression",
    "Financial-analysis": "Quantitative",
    
    # Personality Traits
    "Compassionate": "Empathetic",  # Will be added but also mapped
    "Nurturing": "Helping-others",  # Will be added but also mapped
    "Disciplined": "Organized",  # Will be added but also mapped
    "Resourceful": "Innovative",  # Will be added but also mapped
    
    # Environment & Design
    "Environmental-design": "Environmental-passion",
    "Cinematic-vision": "Visual-learner",
    
    # Civic & Social
    "Civic-minded": "Governance-focus",
    "Justice-minded": "Law-oriented",
    "Change-agent": "Advocacy",
    "Global-minded": "Cultural-awareness",
    
    # Creative & Artistic
    "World-building": "Creative-expression",
    "Storytelling": "Articulate",
    
    # Technical & Practical
    "Defensive-thinking": "Strategic",
    "Safety-conscious": "Methodical",
    "Media-savvy": "Tech-savvy",
}

def apply_trait_mapping(trait: str) -> str:
    """
    Apply trait mapping to convert course traits to question traits.
    Returns the mapped trait if exists, otherwise returns original trait.
    
    Usage in main.py recommendation algorithm:
        from trait_mapping import apply_trait_mapping
        
        # When matching course traits:
        if course.trait_tag:
            course_tags = [apply_trait_mapping(tag.strip()) for tag in course.trait_tag.split(",")]
    """
    return TRAIT_MAPPING.get(trait, trait)

def get_all_mappings():
    """Return all trait mappings for documentation"""
    return TRAIT_MAPPING

def get_mapping_stats():
    """Get statistics about trait mappings"""
    return {
        "total_mappings": len(TRAIT_MAPPING),
        "unique_targets": len(set(TRAIT_MAPPING.values())),
        "mapping_rate": f"{len(TRAIT_MAPPING)} rare traits → {len(set(TRAIT_MAPPING.values()))} common traits"
    }

if __name__ == "__main__":
    print("🔄 TRAIT MAPPING SYSTEM\n")
    print(f"Total mappings: {len(TRAIT_MAPPING)}")
    print(f"Maps to {len(set(TRAIT_MAPPING.values()))} unique traits\n")
    
    print("📋 Mapping by category:\n")
    
    categories = {
        "Data & Analysis": ["Data-driven", "Data-management", "Decision-support"],
        "Critical Thinking": ["Critical-thinking", "Complex-systems", "Experimental"],
        "Professional Skills": ["Compliance", "Compliance-oriented", "Efficiency-driven", "Process-optimization"],
        "Communication": ["Expressive", "Diplomatic", "Debating", "Confident", "Encouraging"],
        "Healthcare": ["Clinical-science", "Bio-science", "Clinical-setting", "Patient-interaction"],
        "Business": ["Business", "Brand-thinking", "Financial-analysis"],
        "Personality": ["Compassionate", "Nurturing", "Disciplined", "Resourceful"],
        "Environment": ["Environmental-design", "Cinematic-vision"],
        "Civic": ["Civic-minded", "Justice-minded", "Change-agent", "Global-minded"],
        "Creative": ["World-building", "Storytelling"],
        "Technical": ["Defensive-thinking", "Safety-conscious", "Media-savvy"]
    }
    
    for category, traits in categories.items():
        print(f"{category}:")
        for trait in traits:
            if trait in TRAIT_MAPPING:
                print(f"  {trait} → {TRAIT_MAPPING[trait]}")
        print()
