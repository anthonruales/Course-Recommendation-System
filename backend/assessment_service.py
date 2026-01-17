"""Assessment Service - Manages assessment tiers and question selection"""

# Try to import enhanced questions first, fall back to seed_data
try:
    from questions_enhanced import QUESTIONS_POOL_ENHANCED as QUESTIONS_POOL
    print("✓ Using enhanced questions (8-10 options each)")
except ImportError:
    from seed_data import QUESTIONS_POOL
    print("! Using standard questions from seed_data")

from seed_data import ASSESSMENT_TIERS
import random

# ==================== STRAND TO TRAITS MAPPING ====================
# Maps SHS strands to their related specialized traits for prioritized questions
STRAND_TRAIT_MAPPING = {
    "STEM": {
        "name": "Science, Technology, Engineering, and Mathematics",
        "priority_traits": [
            # Technology
            "Software-Dev", "Hardware-Systems", "Data-Analytics", "Cyber-Defense",
            # Engineering
            "Civil-Build", "Electrical-Power", "Mechanical-Design", "Industrial-Ops",
            # Science
            "Lab-Research", "Field-Research", "Medical-Lab",
            # Skills
            "Technical-Skill", "Analytical-Skill",
            # RIASEC
            "Investigative", "Realistic"
        ],
        "secondary_traits": ["Patient-Care", "Rehab-Therapy", "Spatial-Design"]
    },
    "ABM": {
        "name": "Accountancy, Business, and Management",
        "priority_traits": [
            # Business
            "Finance-Acct", "Marketing-Sales", "Startup-Venture",
            # Skills
            "Admin-Skill", "Analytical-Skill", "People-Skill",
            # RIASEC
            "Enterprising", "Conventional"
        ],
        "secondary_traits": ["Hospitality-Svc", "Health-Admin", "Industrial-Ops"]
    },
    "HUMSS": {
        "name": "Humanities and Social Sciences",
        "priority_traits": [
            # Education & Social
            "Teaching-Ed", "Community-Serve", "Law-Enforce",
            # Skills
            "People-Skill", "Creative-Skill",
            # RIASEC
            "Social", "Artistic", "Enterprising"
        ],
        "secondary_traits": ["Patient-Care", "Rehab-Therapy", "Visual-Design", "Digital-Media"]
    },
    "TVL": {
        "name": "Technical-Vocational-Livelihood",
        "priority_traits": [
            # Technical
            "Software-Dev", "Hardware-Systems", "Technical-Skill",
            # Hospitality & Tourism
            "Hospitality-Svc", "Agri-Nature",
            # Engineering/Practical
            "Mechanical-Design", "Electrical-Power", "Civil-Build",
            # Skills
            "Physical-Skill", "Technical-Skill",
            # RIASEC
            "Realistic", "Enterprising"
        ],
        "secondary_traits": ["Maritime-Sea", "Industrial-Ops", "Digital-Media"]
    },
    "GAS": {
        "name": "General Academic Strand",
        "priority_traits": [
            # Broad coverage - all RIASEC types
            "Realistic", "Investigative", "Artistic", "Social", "Enterprising", "Conventional",
            # Mix of skills
            "Technical-Skill", "People-Skill", "Creative-Skill", "Analytical-Skill"
        ],
        "secondary_traits": []  # GAS gets general questions, no specific priority
    },
    "SPORTS": {
        "name": "Sports Track",
        "priority_traits": [
            # Physical & Education
            "Physical-Skill", "Teaching-Ed", "Rehab-Therapy",
            # RIASEC
            "Realistic", "Social"
        ],
        "secondary_traits": ["Patient-Care", "Community-Serve", "Hospitality-Svc"]
    },
    "ARTS": {
        "name": "Arts and Design Track",
        "priority_traits": [
            # Arts & Design
            "Visual-Design", "Digital-Media", "Spatial-Design",
            # Skills
            "Creative-Skill",
            # RIASEC
            "Artistic"
        ],
        "secondary_traits": ["Teaching-Ed", "Marketing-Sales", "Hospitality-Svc"]
    }
}


class AssessmentService:
    """Service to manage assessment tiers and question selection"""
    
    @staticmethod
    def get_available_tiers():
        """Return all available assessment tiers"""
        return ASSESSMENT_TIERS
    
    @staticmethod
    def get_strand_info():
        """Return all available strands with their info"""
        return {strand: {"name": info["name"], "focus_areas": info["priority_traits"][:5]} 
                for strand, info in STRAND_TRAIT_MAPPING.items()}
    
    @staticmethod
    def _get_questions_by_strand(strand: str, question_count: int):
        """
        Select questions prioritizing those related to the user's strand.
        
        Strategy:
        - 50% strand-priority questions (traits matching user's strand)
        - 30% secondary/related questions  
        - 20% general questions (for breadth and discovery)
        """
        strand = strand.upper() if strand else "GAS"
        
        if strand not in STRAND_TRAIT_MAPPING:
            strand = "GAS"  # Default to general if unknown strand
        
        strand_config = STRAND_TRAIT_MAPPING[strand]
        priority_traits = set(strand_config["priority_traits"])
        secondary_traits = set(strand_config.get("secondary_traits", []))
        
        # Categorize questions by relevance to strand
        priority_questions = []
        secondary_questions = []
        general_questions = []
        
        for q in QUESTIONS_POOL:
            question_traits = set()
            for opt in q.get("options", []):
                trait = opt.get("trait_tag")
                if trait:
                    question_traits.add(trait)
            
            # Check if question has traits matching the strand
            priority_match = question_traits & priority_traits
            secondary_match = question_traits & secondary_traits
            
            if priority_match:
                priority_questions.append(q)
            elif secondary_match:
                secondary_questions.append(q)
            else:
                general_questions.append(q)
        
        # Calculate how many of each type to select
        # For GAS strand, use more balanced distribution
        if strand == "GAS":
            priority_count = question_count // 3
            secondary_count = question_count // 3
            general_count = question_count - priority_count - secondary_count
        else:
            priority_count = int(question_count * 0.50)  # 50% priority
            secondary_count = int(question_count * 0.30)  # 30% secondary
            general_count = question_count - priority_count - secondary_count  # 20% general
        
        # Select questions from each category
        selected = []
        
        # Priority questions (shuffle and pick)
        random.shuffle(priority_questions)
        selected.extend(priority_questions[:min(priority_count, len(priority_questions))])
        
        # Secondary questions
        random.shuffle(secondary_questions)
        remaining_secondary = min(secondary_count, len(secondary_questions))
        selected.extend(secondary_questions[:remaining_secondary])
        
        # General questions
        random.shuffle(general_questions)
        remaining_general = min(general_count, len(general_questions))
        selected.extend(general_questions[:remaining_general])
        
        # If we don't have enough, fill from any remaining questions
        all_remaining = [q for q in QUESTIONS_POOL if q not in selected]
        random.shuffle(all_remaining)
        
        while len(selected) < question_count and all_remaining:
            selected.append(all_remaining.pop())
        
        # Shuffle final selection so priority questions aren't all at the start
        random.shuffle(selected)
        
        return selected
    
    @staticmethod
    def get_assessment_by_tier(tier: str, strand: str = None):
        """
        Get assessment configuration and questions for a specific tier.
        Questions are prioritized based on user's SHS strand.
        
        Args:
            tier (str): 'quick', 'standard', or 'comprehensive'
            strand (str): User's SHS strand (STEM, ABM, HUMSS, TVL, GAS, SPORTS, ARTS)
            
        Returns:
            dict: Assessment configuration with selected questions
        """
        if tier not in ASSESSMENT_TIERS:
            raise ValueError(f"Invalid tier. Must be one of: {list(ASSESSMENT_TIERS.keys())}")
        
        tier_config = ASSESSMENT_TIERS[tier]
        question_count = tier_config["question_count"]
        
        # Select questions based on strand
        if strand:
            selected_questions = AssessmentService._get_questions_by_strand(strand, question_count)
        else:
            # No strand specified - random selection
            selected_questions = random.sample(QUESTIONS_POOL, min(question_count, len(QUESTIONS_POOL)))
        
        return {
            "tier": tier,
            "name": tier_config["name"],
            "description": tier_config["description"],
            "question_count": len(selected_questions),
            "estimated_time": tier_config["estimated_time"],
            "accuracy": tier_config["accuracy"],
            "strand": strand,
            "strand_name": STRAND_TRAIT_MAPPING.get(strand.upper() if strand else "GAS", {}).get("name", "General"),
            "questions": selected_questions
        }
    
    @staticmethod
    def get_specific_questions(tier: str, question_indices: list = None, strand: str = None):
        """
        Get specific questions or a random selection for a tier.
        
        Args:
            tier (str): Assessment tier
            question_indices (list): Specific question indices to retrieve
            strand (str): User's SHS strand for prioritized selection
            
        Returns:
            list: Selected questions
        """
        if tier not in ASSESSMENT_TIERS:
            raise ValueError(f"Invalid tier. Must be one of: {list(ASSESSMENT_TIERS.keys())}")
        
        question_count = ASSESSMENT_TIERS[tier]["question_count"]
        
        if question_indices:
            return [QUESTIONS_POOL[i] for i in question_indices if i < len(QUESTIONS_POOL)]
        
        if strand:
            return AssessmentService._get_questions_by_strand(strand, question_count)
        
        return random.sample(QUESTIONS_POOL, min(question_count, len(QUESTIONS_POOL)))
