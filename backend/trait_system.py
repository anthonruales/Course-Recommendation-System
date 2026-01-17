"""
Enhanced Trait System - Comprehensive trait matching for accurate course recommendations

This module provides:
1. TRAIT_CATEGORIES - Groups related traits into categories
2. TRAIT_RELATIONSHIPS - Defines which traits are related (for partial matching)
3. Enhanced matching functions for smarter recommendations
4. SPECIALIZED_TRAIT_SYSTEM - New unique traits per career path
"""

from typing import Dict, List, Set, Tuple
from trait_mapping import TRAIT_MAPPING, apply_trait_mapping

# ==================== SPECIALIZED TRAIT SYSTEM (NEW) ====================
# These are UNIQUE traits for each career path - no overlap between fields
SPECIALIZED_TRAITS = {
    # 6 RIASEC Interest Types
    "RIASEC_TYPES": [
        "Realistic", "Investigative", "Artistic", "Social", "Enterprising", "Conventional"
    ],
    
    # 22 Specialized Path Traits (UNIQUE per career field)
    "HEALTHCARE_PATH_TRAITS": ["Patient-Care", "Medical-Lab", "Rehab-Therapy", "Health-Admin"],
    "TECHNOLOGY_PATH_TRAITS": ["Software-Dev", "Hardware-Systems", "Data-Analytics", "Cyber-Defense"],
    "ENGINEERING_PATH_TRAITS": ["Civil-Build", "Electrical-Power", "Mechanical-Design", "Industrial-Ops"],
    "BUSINESS_PATH_TRAITS": ["Finance-Acct", "Marketing-Sales", "Startup-Venture"],
    "EDUCATION_PATH_TRAITS": ["Teaching-Ed"],
    "ARTS_PATH_TRAITS": ["Visual-Design", "Digital-Media", "Spatial-Design"],
    "SCIENCE_PATH_TRAITS": ["Lab-Research", "Field-Research"],
    "PUBLIC_SERVICE_PATH_TRAITS": ["Law-Enforce", "Community-Serve"],
    "MARITIME_PATH_TRAITS": ["Maritime-Sea"],
    "AGRICULTURE_PATH_TRAITS": ["Agri-Nature"],
    "HOSPITALITY_PATH_TRAITS": ["Hospitality-Svc"],
    
    # 6 Skill Traits
    "SKILL_TRAITS": [
        "Technical-Skill", "People-Skill", "Creative-Skill", 
        "Analytical-Skill", "Physical-Skill", "Admin-Skill"
    ]
}

# Specialized trait relationships (for adaptive assessment matching)
SPECIALIZED_TRAIT_RELATIONSHIPS: Dict[str, Dict[str, float]] = {
    # Patient-Care relationships
    "Patient-Care": {
        "Social": 0.8, "People-Skill": 0.9, "Rehab-Therapy": 0.6, "Health-Admin": 0.3,
        "Medical-Lab": 0.4, "Community-Serve": 0.5, "Teaching-Ed": 0.4
    },
    "Medical-Lab": {
        "Investigative": 0.8, "Analytical-Skill": 0.9, "Patient-Care": 0.4,
        "Lab-Research": 0.7, "Technical-Skill": 0.5
    },
    "Rehab-Therapy": {
        "Social": 0.7, "Physical-Skill": 0.8, "Patient-Care": 0.6, "People-Skill": 0.7,
        "Teaching-Ed": 0.4
    },
    "Health-Admin": {
        "Conventional": 0.8, "Admin-Skill": 0.9, "Patient-Care": 0.3, "Finance-Acct": 0.4
    },
    
    # Technology relationships
    "Software-Dev": {
        "Investigative": 0.8, "Technical-Skill": 0.9, "Data-Analytics": 0.6,
        "Cyber-Defense": 0.5, "Hardware-Systems": 0.4, "Digital-Media": 0.3
    },
    "Hardware-Systems": {
        "Realistic": 0.8, "Technical-Skill": 0.9, "Electrical-Power": 0.6,
        "Software-Dev": 0.4, "Mechanical-Design": 0.5
    },
    "Data-Analytics": {
        "Investigative": 0.9, "Analytical-Skill": 0.9, "Software-Dev": 0.6,
        "Lab-Research": 0.5, "Finance-Acct": 0.4
    },
    "Cyber-Defense": {
        "Investigative": 0.7, "Technical-Skill": 0.8, "Software-Dev": 0.5,
        "Law-Enforce": 0.3
    },
    
    # Engineering relationships
    "Civil-Build": {
        "Realistic": 0.9, "Technical-Skill": 0.8, "Spatial-Design": 0.5,
        "Mechanical-Design": 0.4, "Industrial-Ops": 0.3
    },
    "Electrical-Power": {
        "Realistic": 0.8, "Technical-Skill": 0.9, "Hardware-Systems": 0.6,
        "Mechanical-Design": 0.4, "Industrial-Ops": 0.4
    },
    "Mechanical-Design": {
        "Realistic": 0.9, "Technical-Skill": 0.8, "Industrial-Ops": 0.5,
        "Civil-Build": 0.4, "Electrical-Power": 0.4
    },
    "Industrial-Ops": {
        "Enterprising": 0.6, "Analytical-Skill": 0.7, "Mechanical-Design": 0.5,
        "Finance-Acct": 0.3, "Admin-Skill": 0.4
    },
    
    # Business relationships
    "Finance-Acct": {
        "Conventional": 0.9, "Analytical-Skill": 0.8, "Admin-Skill": 0.6,
        "Marketing-Sales": 0.3, "Startup-Venture": 0.4
    },
    "Marketing-Sales": {
        "Enterprising": 0.9, "People-Skill": 0.8, "Startup-Venture": 0.6,
        "Finance-Acct": 0.3, "Hospitality-Svc": 0.4
    },
    "Startup-Venture": {
        "Enterprising": 0.9, "People-Skill": 0.6, "Marketing-Sales": 0.6,
        "Finance-Acct": 0.4, "Creative-Skill": 0.4
    },
    
    # Education relationships
    "Teaching-Ed": {
        "Social": 0.9, "People-Skill": 0.9, "Community-Serve": 0.5,
        "Patient-Care": 0.3, "Rehab-Therapy": 0.3
    },
    
    # Arts relationships
    "Visual-Design": {
        "Artistic": 0.9, "Creative-Skill": 0.9, "Digital-Media": 0.6,
        "Spatial-Design": 0.5
    },
    "Digital-Media": {
        "Artistic": 0.8, "Creative-Skill": 0.8, "Software-Dev": 0.4,
        "Visual-Design": 0.6, "Technical-Skill": 0.4
    },
    "Spatial-Design": {
        "Artistic": 0.7, "Creative-Skill": 0.7, "Civil-Build": 0.5,
        "Visual-Design": 0.5, "Technical-Skill": 0.4
    },
    
    # Science relationships
    "Lab-Research": {
        "Investigative": 0.9, "Analytical-Skill": 0.9, "Medical-Lab": 0.6,
        "Field-Research": 0.5, "Data-Analytics": 0.5
    },
    "Field-Research": {
        "Investigative": 0.8, "Physical-Skill": 0.5, "Agri-Nature": 0.6,
        "Lab-Research": 0.5, "Analytical-Skill": 0.6
    },
    
    # Public service relationships
    "Law-Enforce": {
        "Realistic": 0.7, "Physical-Skill": 0.7, "Community-Serve": 0.4,
        "Cyber-Defense": 0.3
    },
    "Community-Serve": {
        "Social": 0.9, "People-Skill": 0.8, "Teaching-Ed": 0.5,
        "Patient-Care": 0.4, "Law-Enforce": 0.3
    },
    
    # Other paths
    "Maritime-Sea": {
        "Realistic": 0.9, "Physical-Skill": 0.8, "Technical-Skill": 0.5,
        "Mechanical-Design": 0.3
    },
    "Agri-Nature": {
        "Realistic": 0.9, "Physical-Skill": 0.7, "Field-Research": 0.5,
        "Lab-Research": 0.3
    },
    "Hospitality-Svc": {
        "Enterprising": 0.7, "People-Skill": 0.9, "Marketing-Sales": 0.4,
        "Community-Serve": 0.3, "Admin-Skill": 0.4
    },
    
    # Skill trait relationships
    "Technical-Skill": {
        "Realistic": 0.7, "Investigative": 0.5, "Software-Dev": 0.8,
        "Hardware-Systems": 0.8, "Mechanical-Design": 0.7
    },
    "People-Skill": {
        "Social": 0.9, "Enterprising": 0.6, "Patient-Care": 0.8,
        "Teaching-Ed": 0.8, "Hospitality-Svc": 0.8
    },
    "Creative-Skill": {
        "Artistic": 0.9, "Visual-Design": 0.8, "Digital-Media": 0.8,
        "Spatial-Design": 0.7
    },
    "Analytical-Skill": {
        "Investigative": 0.9, "Data-Analytics": 0.8, "Lab-Research": 0.7,
        "Finance-Acct": 0.7, "Medical-Lab": 0.6
    },
    "Physical-Skill": {
        "Realistic": 0.8, "Maritime-Sea": 0.7, "Agri-Nature": 0.7,
        "Law-Enforce": 0.6, "Rehab-Therapy": 0.6
    },
    "Admin-Skill": {
        "Conventional": 0.9, "Finance-Acct": 0.6, "Health-Admin": 0.7,
        "Hospitality-Svc": 0.4, "Industrial-Ops": 0.4
    }
}


# ==================== TRAIT CATEGORIES ====================
# These group related traits together for category-level matching
TRAIT_CATEGORIES = {
    "HELPING_OTHERS": {
        "core_traits": ["Helping-others", "Empathetic", "Patient-focused", "Service-oriented", "Compassionate"],
        "related_traits": ["Collaborative", "Mentoring", "Nurturing", "Encouraging", "Supportive"],
        "description": "Traits indicating desire to help and support others"
    },
    "PROBLEM_SOLVING": {
        "core_traits": ["Problem-solving", "Analytical", "Logical", "Critical-thinking", "Investigative"],
        "related_traits": ["Research-oriented", "Methodical", "Detail-focused", "Strategic", "Systematic"],
        "description": "Traits for analytical and problem-solving abilities"
    },
    "CREATIVE": {
        "core_traits": ["Creative-expression", "Artistic-passion", "Innovative", "Visual-learner", "Aesthetic-sense"],
        "related_traits": ["Digital-art", "Expressive", "Imaginative", "Design-thinking", "Experimental"],
        "description": "Traits for creative and artistic inclinations"
    },
    "LEADERSHIP": {
        "core_traits": ["Leading-teams", "Leadership", "Ambitious", "Strategic", "Big-picture"],
        "related_traits": ["Confident", "Decisive", "Motivational", "Organized", "Collaborative"],
        "description": "Traits for leadership and management"
    },
    "TECHNICAL": {
        "core_traits": ["Tech-savvy", "Hands-on", "Technical", "Laboratory", "Precision-oriented"],
        "related_traits": ["Algorithm-focused", "Mechanical-minded", "Circuit-design", "Practical", "Detail-focused"],
        "description": "Traits for technical and hands-on work"
    },
    "HEALTHCARE": {
        "core_traits": ["Patient-focused", "Clinical-setting", "Empathetic", "Helping-others", "Health-conscious"],
        "related_traits": ["Compassionate", "Resilient", "Crisis-management", "Detail-focused", "Service-oriented"],
        "description": "Traits for healthcare and medical fields"
    },
    "BUSINESS": {
        "core_traits": ["Business-minded", "Analytical", "Strategic", "Ambitious", "Risk-taking"],
        "related_traits": ["Quantitative", "Leadership", "Organized", "Persuasive", "Negotiation-skills"],
        "description": "Traits for business and entrepreneurship"
    },
    "SOCIAL": {
        "core_traits": ["Extroverted", "Collaborative", "Social", "Empathetic", "Team-centric"],
        "related_traits": ["Articulate", "Persuasive", "Cultural-awareness", "Mentoring", "Community-focused"],
        "description": "Traits for social and interpersonal work"
    },
    "RESEARCH": {
        "core_traits": ["Research-oriented", "Analytical", "Theoretical", "Investigative", "Independent"],
        "related_traits": ["Detail-focused", "Methodical", "Scientific-thinking", "Observational", "Contemplative"],
        "description": "Traits for research and academic work"
    },
    "OUTDOOR": {
        "core_traits": ["Field-work", "Outdoor-enthusiast", "Active", "Adventurous", "Nature-focused"],
        "related_traits": ["Physical-fitness", "Exploratory", "Independent", "Hands-on", "Practical"],
        "description": "Traits for outdoor and field work"
    }
}

# ==================== TRAIT RELATIONSHIPS ====================
# Defines similarity between traits (0.0 to 1.0)
# This allows partial matching when exact trait doesn't match
TRAIT_RELATIONSHIPS: Dict[str, Dict[str, float]] = {
    # Helping/Empathy cluster
    "Helping-others": {
        "Empathetic": 0.9, "Patient-focused": 0.85, "Service-oriented": 0.8,
        "Compassionate": 0.9, "Collaborative": 0.6, "Mentoring": 0.7,
        "Nurturing": 0.85, "Encouraging": 0.7, "Social": 0.5
    },
    "Empathetic": {
        "Helping-others": 0.9, "Patient-focused": 0.85, "Compassionate": 0.95,
        "Social": 0.6, "Collaborative": 0.5, "Understanding": 0.8
    },
    "Patient-focused": {
        "Helping-others": 0.85, "Empathetic": 0.85, "Clinical-setting": 0.8,
        "Service-oriented": 0.7, "Compassionate": 0.8, "Health-conscious": 0.6
    },
    
    # Problem-solving cluster
    "Problem-solving": {
        "Analytical": 0.9, "Logical": 0.85, "Critical-thinking": 0.9,
        "Research-oriented": 0.7, "Methodical": 0.6, "Investigative": 0.75,
        "Strategic": 0.65, "Detail-focused": 0.5
    },
    "Analytical": {
        "Problem-solving": 0.9, "Logical": 0.85, "Research-oriented": 0.8,
        "Quantitative": 0.75, "Detail-focused": 0.7, "Methodical": 0.65,
        "Critical-thinking": 0.85, "Data-driven": 0.7
    },
    "Logical": {
        "Problem-solving": 0.85, "Analytical": 0.85, "Methodical": 0.7,
        "Algorithm-focused": 0.75, "Systematic": 0.7, "Abstract-thinking": 0.6
    },
    
    # Creative cluster
    "Creative-expression": {
        "Artistic-passion": 0.9, "Innovative": 0.8, "Visual-learner": 0.7,
        "Aesthetic-sense": 0.85, "Expressive": 0.75, "Digital-art": 0.7,
        "Design-thinking": 0.75, "Imaginative": 0.85
    },
    "Artistic-passion": {
        "Creative-expression": 0.9, "Visual-learner": 0.75, "Aesthetic-sense": 0.85,
        "Studio-work": 0.7, "Expressive": 0.7, "Hands-on": 0.5
    },
    "Visual-learner": {
        "Creative-expression": 0.7, "Aesthetic-sense": 0.75, "Artistic-passion": 0.75,
        "Digital-art": 0.7, "Spatial-thinking": 0.65, "Detail-focused": 0.5
    },
    
    # Leadership cluster
    "Leading-teams": {
        "Leadership": 0.95, "Collaborative": 0.7, "Ambitious": 0.65,
        "Strategic": 0.7, "Big-picture": 0.75, "Confident": 0.6,
        "Organized": 0.5, "Decisive": 0.7
    },
    "Leadership": {
        "Leading-teams": 0.95, "Ambitious": 0.7, "Strategic": 0.65,
        "Big-picture": 0.7, "Confident": 0.65, "Decisive": 0.7,
        "Motivational": 0.6
    },
    
    # Technical cluster
    "Tech-savvy": {
        "Problem-solving": 0.6, "Logical": 0.65, "Algorithm-focused": 0.75,
        "Hands-on": 0.5, "Digital-art": 0.5, "Innovative": 0.5,
        "Remote-friendly": 0.4, "Technical": 0.85
    },
    "Hands-on": {
        "Practical": 0.85, "Field-work": 0.7, "Technical": 0.65,
        "Laboratory": 0.7, "Active": 0.6, "Detail-focused": 0.5
    },
    "Laboratory": {
        "Research-oriented": 0.75, "Scientific-thinking": 0.8, "Hands-on": 0.7,
        "Detail-focused": 0.7, "Methodical": 0.65, "Analytical": 0.6
    },
    
    # Business cluster
    "Business-minded": {
        "Strategic": 0.8, "Analytical": 0.6, "Risk-taking": 0.65,
        "Ambitious": 0.7, "Leadership": 0.6, "Quantitative": 0.5,
        "Organized": 0.5, "Persuasive": 0.5
    },
    
    # Social/Communication cluster
    "Extroverted": {
        "Social": 0.9, "Collaborative": 0.75, "Team-centric": 0.7,
        "Articulate": 0.5, "Persuasive": 0.5, "Confident": 0.6
    },
    "Collaborative": {
        "Team-centric": 0.9, "Social": 0.7, "Extroverted": 0.75,
        "Helping-others": 0.6, "Empathetic": 0.5
    },
    
    # Work environment clusters
    "Office-based": {
        "Remote-friendly": 0.6, "Organized": 0.5, "Detail-focused": 0.4
    },
    "Field-work": {
        "Outdoor-enthusiast": 0.85, "Hands-on": 0.7, "Active": 0.65,
        "Adventurous": 0.6, "Practical": 0.6
    },
    "Clinical-setting": {
        "Patient-focused": 0.85, "Healthcare": 0.9, "Helping-others": 0.7,
        "Empathetic": 0.6, "Detail-focused": 0.5
    },
    
    # Research cluster
    "Research-oriented": {
        "Analytical": 0.8, "Investigative": 0.85, "Theoretical": 0.75,
        "Detail-focused": 0.65, "Independent": 0.6, "Scientific-thinking": 0.8,
        "Methodical": 0.6, "Laboratory": 0.7
    },
    
    # Independent/Introverted cluster
    "Independent": {
        "Introverted": 0.6, "Self-directed": 0.8, "Contemplative": 0.5,
        "Research-oriented": 0.5, "Detail-focused": 0.4
    },
    "Introverted": {
        "Independent": 0.6, "Contemplative": 0.7, "Detail-focused": 0.4,
        "Research-oriented": 0.4
    }
}

# ==================== EXPANDED TRAIT MAPPING ====================
# More comprehensive mapping from course-specific traits to common traits
EXPANDED_TRAIT_MAPPING = {
    **TRAIT_MAPPING,  # Include original mappings
    
    # Additional mappings for better coverage
    "Scientific-thinking": "Research-oriented",
    "Precision-oriented": "Detail-focused",
    "Patient": "Methodical",
    "Adaptive": "Innovative",
    "Resilient": "Problem-solving",
    "Observational": "Analytical",
    "Mathematical": "Logical",
    "Systematic": "Methodical",
    "Quality-oriented": "Detail-focused",
    "Manufacturing-focus": "Hands-on",
    "Structural-thinking": "Analytical",
    "Urban-focus": "Big-picture",
    "Sustainability-minded": "Big-picture",
    "Mapping-focused": "Visual-learner",
    "Investment-minded": "Analytical",
    "Market-analysis": "Analytical",
    "Health-conscious": "Helping-others",
    "Communication-skills": "Articulate",
    "People-skills": "Social",
    "Administrative-skills": "Organized",
    "Information-management": "Organized",
    "Coaching": "Mentoring",
    "Maternal-care": "Nurturing",
    "Vision-care": "Detail-focused",
    "Molecular-focus": "Detail-focused",
    "Earth-science": "Scientific-thinking",
    "Aquatic-passion": "Nature-focused",
    "Conservation-minded": "Environmental-passion",
    "Food-science": "Scientific-thinking",
    "Culinary-passion": "Creative-expression",
    "Weather-passion": "Scientific-thinking",
    "Aviation-passion": "Technical",
    "Aerospace-passion": "Technical",
    "Sea-passion": "Adventurous",
    "Navigation": "Analytical",
    "Farming-passion": "Nature-connected",
    "Governance-focus": "Leadership",
    "Policy-focused": "Analytical",
    "Public-service": "Helping-others",
    "Community-focused": "Helping-others",
    "Grassroots": "Community-focused",
    "Child-focused": "Nurturing",
    "Playful": "Creative-expression",
    "Language-passion": "Articulate",
    "Performative": "Extroverted",
    "Trade-focused": "Business-minded",
    "Regulatory-compliance": "Methodical",
    "Sales-oriented": "Persuasive",
    "Guest-focused": "Service-oriented",
    "Hybrid-thinking": "Analytical",
    "Trend-aware": "Innovative",
    "User-focused": "Empathetic",
    "Versatile": "Innovative",
    "Client-interaction": "Social",
    "Circuit-design": "Technical",
    "Hardware-focused": "Technical",
    "Tangible-design": "Hands-on",
    "Law-enforcement": "Disciplined",
    "Protective": "Helping-others",
    "Crisis-management": "Problem-solving",
    "Animal-care": "Empathetic",
    "Subject-expertise": "Research-oriented",
    "Athletic-passion": "Active",
    "Physical-fitness": "Active",
    "Auditory-skills": "Creative-expression",
    "Ethical": "Methodical",
    "Inquisitive": "Research-oriented",
    "Understanding": "Empathetic",
    "Design-thinking": "Creative-expression",
    "Imaginative": "Creative-expression",
    "Self-directed": "Independent",
    "Decisive": "Leadership",
    
    # Final gap closures (100% coverage)
    "Negotiation-skills": "Persuasive",
    "Numerical-thinking": "Quantitative",
    "Practical-skills": "Hands-on",
    "Quality-control": "Detail-focused",
    "Risk-assessment": "Analytical",
    "Spatial-thinking": "Visual-learner",
    "Statistical-thinking": "Quantitative",
    "Systemic-thinking": "Analytical",
    "Vigilant": "Detail-focused",
    "Motivational": "Leadership",
}


def get_trait_similarity(trait1: str, trait2: str) -> float:
    """
    Calculate similarity between two traits (0.0 to 1.0)
    Returns 1.0 for exact match, relationship score for related traits, 0.0 otherwise
    """
    # Exact match
    if trait1 == trait2:
        return 1.0
    
    # Check mapped equivalence
    mapped1 = EXPANDED_TRAIT_MAPPING.get(trait1, trait1)
    mapped2 = EXPANDED_TRAIT_MAPPING.get(trait2, trait2)
    if mapped1 == mapped2:
        return 0.9  # Very high similarity for mapped equivalents
    
    # Check direct relationship
    if trait1 in TRAIT_RELATIONSHIPS:
        if trait2 in TRAIT_RELATIONSHIPS[trait1]:
            return TRAIT_RELATIONSHIPS[trait1][trait2]
    
    # Check reverse relationship
    if trait2 in TRAIT_RELATIONSHIPS:
        if trait1 in TRAIT_RELATIONSHIPS[trait2]:
            return TRAIT_RELATIONSHIPS[trait2][trait1]
    
    # Check if both traits are in the same category
    for category_data in TRAIT_CATEGORIES.values():
        all_category_traits = set(category_data["core_traits"] + category_data["related_traits"])
        if trait1 in all_category_traits and trait2 in all_category_traits:
            # Both in same category - give base similarity
            if trait1 in category_data["core_traits"] and trait2 in category_data["core_traits"]:
                return 0.6  # Both core traits in same category
            elif trait1 in category_data["core_traits"] or trait2 in category_data["core_traits"]:
                return 0.4  # One core, one related in same category
            return 0.3  # Both related traits in same category
    
    return 0.0  # No relationship found


def calculate_trait_match_score(user_traits: List[str], course_traits: List[str]) -> Tuple[float, List[str], Dict]:
    """
    Calculate comprehensive trait match score between user and course
    
    Returns:
        - match_score: Total score (0 to 100+)
        - matched_traits: List of traits that matched (exact or similar)
        - match_details: Dictionary with breakdown of matches
    """
    if not user_traits or not course_traits:
        return 0.0, [], {"exact": [], "similar": [], "category": []}
    
    # Normalize traits using expanded mapping
    normalized_user = [EXPANDED_TRAIT_MAPPING.get(t, t) for t in user_traits]
    normalized_course = [EXPANDED_TRAIT_MAPPING.get(t, t) for t in course_traits]
    
    exact_matches = []
    similar_matches = []  # (user_trait, course_trait, similarity)
    category_matches = []
    
    total_score = 0.0
    used_course_traits = set()
    
    # First pass: Exact matches (highest value)
    for u_trait in normalized_user:
        for c_trait in normalized_course:
            if u_trait == c_trait and c_trait not in used_course_traits:
                exact_matches.append(u_trait)
                total_score += 15.0  # Full points for exact match
                used_course_traits.add(c_trait)
                break
    
    # Second pass: Similar matches (partial value)
    for u_trait in user_traits:
        for c_trait in course_traits:
            if c_trait in used_course_traits:
                continue
            
            similarity = get_trait_similarity(u_trait, c_trait)
            if similarity >= 0.5:  # Only count significant similarities
                similar_matches.append((u_trait, c_trait, similarity))
                total_score += similarity * 10.0  # Partial points based on similarity
                used_course_traits.add(c_trait)
                break
    
    # Third pass: Category-level matches
    user_categories = set()
    course_categories = set()
    
    for u_trait in user_traits:
        for cat_name, cat_data in TRAIT_CATEGORIES.items():
            if u_trait in cat_data["core_traits"] or u_trait in cat_data["related_traits"]:
                user_categories.add(cat_name)
    
    for c_trait in course_traits:
        for cat_name, cat_data in TRAIT_CATEGORIES.items():
            if c_trait in cat_data["core_traits"] or c_trait in cat_data["related_traits"]:
                course_categories.add(cat_name)
    
    # Bonus for matching categories
    matching_categories = user_categories.intersection(course_categories)
    for cat in matching_categories:
        category_matches.append(cat)
        total_score += 3.0  # Small bonus per matching category
    
    # Create matched traits list for display
    matched_traits = exact_matches + [f"{u}≈{c}" for u, c, _ in similar_matches[:3]]
    
    return total_score, matched_traits[:7], {
        "exact": exact_matches,
        "similar": [(u, c, round(s, 2)) for u, c, s in similar_matches],
        "category": category_matches,
        "user_categories": list(user_categories),
        "course_categories": list(course_categories)
    }


def get_user_profile_from_traits(trait_scores: Dict[str, float]) -> Dict:
    """
    Analyze user's trait scores to create a profile summary
    
    Returns dict with:
    - primary_category: Main category user fits into
    - secondary_categories: Other relevant categories
    - profile_description: Human-readable description
    - recommended_fields: Suggested career fields
    """
    # Sort traits by score
    sorted_traits = sorted(trait_scores.items(), key=lambda x: x[1], reverse=True)
    top_traits = [t for t, _ in sorted_traits[:10]]
    
    # Count category matches
    category_scores = {}
    for trait in top_traits:
        for cat_name, cat_data in TRAIT_CATEGORIES.items():
            if trait in cat_data["core_traits"]:
                category_scores[cat_name] = category_scores.get(cat_name, 0) + 2
            elif trait in cat_data["related_traits"]:
                category_scores[cat_name] = category_scores.get(cat_name, 0) + 1
    
    # Sort categories by score
    sorted_categories = sorted(category_scores.items(), key=lambda x: x[1], reverse=True)
    
    primary_category = sorted_categories[0][0] if sorted_categories else "GENERAL"
    secondary_categories = [c for c, _ in sorted_categories[1:3] if _ >= 2]
    
    # Map categories to recommended fields
    CATEGORY_TO_FIELDS = {
        "HELPING_OTHERS": ["Healthcare", "Education", "Social Work", "Counseling"],
        "PROBLEM_SOLVING": ["Engineering", "IT", "Science", "Mathematics"],
        "CREATIVE": ["Arts", "Design", "Media", "Entertainment"],
        "LEADERSHIP": ["Business", "Management", "Public Administration"],
        "TECHNICAL": ["Engineering", "IT", "Technology", "Manufacturing"],
        "HEALTHCARE": ["Nursing", "Medicine", "Allied Health", "Pharmacy"],
        "BUSINESS": ["Business Administration", "Finance", "Marketing", "Entrepreneurship"],
        "SOCIAL": ["Communication", "Education", "Social Sciences", "Hospitality"],
        "RESEARCH": ["Science", "Research", "Academia", "Analytics"],
        "OUTDOOR": ["Agriculture", "Environmental Science", "Marine", "Forestry"]
    }
    
    recommended_fields = CATEGORY_TO_FIELDS.get(primary_category, ["General Studies"])
    
    return {
        "primary_category": primary_category,
        "secondary_categories": secondary_categories,
        "top_traits": top_traits[:5],
        "category_scores": category_scores,
        "recommended_fields": recommended_fields,
        "profile_description": TRAIT_CATEGORIES.get(primary_category, {}).get("description", "General profile")
    }


if __name__ == "__main__":
    print("🧠 ENHANCED TRAIT SYSTEM")
    print("=" * 50)
    
    # Test trait similarity
    test_pairs = [
        ("Helping-others", "Empathetic"),
        ("Problem-solving", "Analytical"),
        ("Creative-expression", "Artistic-passion"),
        ("Tech-savvy", "Algorithm-focused"),
        ("Helping-others", "Tech-savvy"),  # Should be low
    ]
    
    print("\n📊 Trait Similarity Tests:")
    for t1, t2 in test_pairs:
        sim = get_trait_similarity(t1, t2)
        print(f"  {t1} ↔ {t2}: {sim:.2f}")
    
    # Test match calculation
    user = ["Problem-solving", "Analytical", "Tech-savvy", "Independent", "Logical"]
    course = ["Problem-solving", "Logical", "Algorithm-focused", "Office-based", "Technical"]
    
    score, matched, details = calculate_trait_match_score(user, course)
    print(f"\n📈 Match Calculation:")
    print(f"  User traits: {user}")
    print(f"  Course traits: {course}")
    print(f"  Score: {score:.1f}")
    print(f"  Matched: {matched}")
    print(f"  Details: {details}")
