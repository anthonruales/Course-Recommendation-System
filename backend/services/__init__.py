from .trait_mapping import TRAIT_MAPPING, apply_trait_mapping
from .trait_system import (
    EXPANDED_TRAIT_MAPPING, TRAIT_CATEGORIES, TRAIT_RELATIONSHIPS,
    SPECIALIZED_TRAIT_RELATIONSHIPS, calculate_trait_match_score,
    get_trait_similarity, get_user_profile_from_traits
)
from .assessment_service import AssessmentService
from .recommendation_engine import HybridRecommendationEngine
from .adaptive_assessment import (
    AdaptiveAssessmentEngine, initialize_adaptive_engine, get_adaptive_engine
)
