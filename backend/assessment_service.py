"""Assessment Service - Manages assessment tiers and question selection"""

from seed_data import QUESTIONS_POOL, ASSESSMENT_TIERS
import random

class AssessmentService:
    """Service to manage assessment tiers and question selection"""
    
    @staticmethod
    def get_available_tiers():
        """Return all available assessment tiers"""
        return ASSESSMENT_TIERS
    
    @staticmethod
    def get_assessment_by_tier(tier: str):
        """
        Get assessment configuration and questions for a specific tier
        
        Args:
            tier (str): 'quick', 'standard', or 'comprehensive'
            
        Returns:
            dict: Assessment configuration with selected questions
        """
        if tier not in ASSESSMENT_TIERS:
            raise ValueError(f"Invalid tier. Must be one of: {list(ASSESSMENT_TIERS.keys())}")
        
        tier_config = ASSESSMENT_TIERS[tier]
        question_count = tier_config["question_count"]
        
        # Select random questions from the pool
        selected_questions = random.sample(QUESTIONS_POOL, min(question_count, len(QUESTIONS_POOL)))
        
        return {
            "tier": tier,
            "name": tier_config["name"],
            "description": tier_config["description"],
            "question_count": question_count,
            "estimated_time": tier_config["estimated_time"],
            "accuracy": tier_config["accuracy"],
            "questions": selected_questions
        }
    
    @staticmethod
    def get_specific_questions(tier: str, question_indices: list = None):
        """
        Get specific questions or a random selection for a tier
        
        Args:
            tier (str): Assessment tier
            question_indices (list): Specific question indices to retrieve
            
        Returns:
            list: Selected questions
        """
        if tier not in ASSESSMENT_TIERS:
            raise ValueError(f"Invalid tier. Must be one of: {list(ASSESSMENT_TIERS.keys())}")
        
        question_count = ASSESSMENT_TIERS[tier]["question_count"]
        
        if question_indices:
            return [QUESTIONS_POOL[i] for i in question_indices if i < len(QUESTIONS_POOL)]
        
        return random.sample(QUESTIONS_POOL, min(question_count, len(QUESTIONS_POOL)))
