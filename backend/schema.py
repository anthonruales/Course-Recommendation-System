from pydantic import BaseModel
from typing import List, Dict

class RecommendationStats(BaseModel):
    rule_based_count: int
    decision_tree_count: int
    accuracy_score: float

class DashboardData(BaseModel):
    total_users: int
    total_courses: int
    algo_performance: RecommendationStats
    top_recommended_courses: List[Dict[str, str]]