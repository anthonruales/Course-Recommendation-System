# adaptive_assessment.py
"""
Adaptive Assessment Engine using Decision Tree Principles (Information Gain)

================================================================================
ALGORITHM FOUNDATION: Decision Tree Classification with Information Gain
Based on: Quinlan, J.R. (1986). Induction of Decision Trees. Machine Learning.
================================================================================

This module implements an adaptive question selection system using the same
Information Gain calculation that powers Decision Tree algorithms (ID3/C4.5).

The Decision Tree Approach:
- Uses Information Gain (Shannon Entropy) to select optimal splitting questions
- Each question acts as a decision node that splits the candidate course set
- Answers traverse the implicit decision tree towards leaf nodes (recommendations)
- The tree is dynamically constructed based on real-time user responses

Key Decision Tree Concepts Applied:
1. INFORMATION GAIN: Measures how well a question discriminates between courses
   (same formula used in ID3/C4.5 Decision Tree construction)
2. ENTROPY CALCULATION: Shannon entropy to find questions that best split candidates
3. ATTRIBUTE SELECTION: Choosing the most informative trait-based question
4. PRUNING: Excluding already-answered questions and rejected topics

The algorithm:
- Start with all courses as candidates (root of implicit tree)
- Calculate Information Gain for each potential question (finding best split)
- Select question with highest gain (optimal decision node)
- User's answer updates trait scores (traversing the tree)
- Repeat until confident or max questions reached (reaching leaf nodes)
- Final recommendations are the courses at the terminal leaf nodes

This approach is MORE ADAPTIVE than a pre-built static Decision Tree because:
- The tree structure adapts to each user's unique responses
- No training data required - uses trait-course relationships directly
- Handles new questions/courses without retraining
"""

import math
from collections import defaultdict
from typing import Dict, List, Optional, Tuple, Set
import random
from dataclasses import dataclass, field
from trait_system import (
    EXPANDED_TRAIT_MAPPING, 
    TRAIT_CATEGORIES, 
    TRAIT_RELATIONSHIPS,
    SPECIALIZED_TRAIT_RELATIONSHIPS,  # NEW: Specialized trait relationships
    calculate_trait_match_score,
    get_trait_similarity
)


@dataclass
class AdaptiveSession:
    """State for a single assessment session"""
    session_id: str
    user_id: int
    
    user_gwa: float = None
    user_strand: str = None
    user_interests: str = None
    user_skills: str = None
    
    max_questions: int = 30
    min_questions: int = 15
    
    trait_scores: Dict[str, float] = field(default_factory=dict)
    course_scores: Dict[str, float] = field(default_factory=dict)
    initial_course_scores: Dict[str, float] = field(default_factory=dict)  # Store initial scores with profile bonuses for proper recalculation
    answered_questions: Dict[int, int] = field(default_factory=dict)
    excluded_question_ids: Set[int] = field(default_factory=set)
    rejected_topics: Set[str] = field(default_factory=set)
    question_history: List[int] = field(default_factory=list)  # Track order of answered questions for "Previous"
    answer_trait_changes: Dict[int, Dict[str, float]] = field(default_factory=dict)  # Track trait changes per question for reversal
    answer_rejection_data: Dict[int, Dict] = field(default_factory=dict)  # Track rejected topics and penalties per question for reversal
    
    round_number: int = 0
    active_courses: Set[str] = field(default_factory=set)
    confidence: float = 0.0
    is_complete: bool = False
    final_recommendations: List[dict] = field(default_factory=list)
    
    # --- Topic continuity tracking ---
    recent_traits: List[str] = field(default_factory=list)       # Last N traits chosen by user
    current_topic_thread: str = ""                                # Dominant topic area (e.g. "Software-Dev")
    topic_streak: int = 0                                        # How many consecutive Qs in same topic area
    profile_seed_traits: List[str] = field(default_factory=list) # Traits derived from user profile at session start
    
    # --- Decision Tree State ---
    branch_weights: Dict[str, float] = field(default_factory=dict)   # Weight of each branch (healthcare, technology, etc.)
    current_depth: int = 0                                           # Current depth in the tree (0-3)
    branch_history: List[str] = field(default_factory=list)          # Which branches were followed (for connection tracking)
    question_weights_applied: Dict[int, float] = field(default_factory=dict)  # Track question weight used for each answered Q (for reversal)
    
    # --- Conversation Chain State ---
    primary_domain: str = ""                        # Primary domain from profile (e.g. "technology")
    domain_queue: List[str] = field(default_factory=list)  # Ordered domains to explore (profile -> adjacent only)
    relevant_domains: Set[str] = field(default_factory=set)  # Domains allowed based on profile (no unrelated domains)
    current_chain_trait: str = ""                    # The trait driving the current follow-up chain
    chain_queue: List[int] = field(default_factory=list)   # Ordered question IDs to ask next (from current chain)
    explored_domains: Set[str] = field(default_factory=set)  # Domains that have had at least N questions asked
    domain_question_count: Dict[str, int] = field(default_factory=dict)  # How many questions per domain
    last_answer_trait: str = ""                      # Trait from the most recent answer (drives next question)


# Maps SHS strand to prioritized traits for question selection
STRAND_PRIORITY_TRAITS = {
    "STEM": ["Software-Dev", "Hardware-Systems", "Lab-Research", "Analytical", "Investigative", 
             "Scientific", "Math-Logic", "Realistic", "Data-Analytics"],
    "ABM": ["Finance-Acct", "Marketing-Sales", "Startup-Venture", "Enterprising", "Conventional",
            "Business-Ops", "Corporate-Mgmt", "Communication"],
    "HUMSS": ["Teaching-Ed", "Community-Serve", "Law-Enforce", "Social", "Artistic",
              "Media-Journalism", "Linguistic-Cultural", "Public-Admin"],
    "TVL": ["Software-Dev", "Hospitality-Svc", "Mechanical-Design", "Realistic", "Conventional",
            "Practical", "Manual-Technical", "Agriculture-Env"],
    "GAS": ["Investigative", "Social", "Enterprising", "Analytical", "Communication",
            "Creative", "Leadership", "Critical-Think"],
    "SPORTS": ["Sports-Fitness", "Coaching-Training", "Realistic", "Social",
               "Practical", "Wellness-Health", "Leadership"],
    "ARTS": ["Creative-Design", "Media-Production", "Artistic", "Creative",
             "Visual-Arts", "Performing-Arts", "Communication"]
}

# ==================== TOPIC ADJACENCY MAP ====================
# Defines which traits are "related" or "adjacent" topics.
# When the user is on a topic streak (e.g. 5 questions about computers),
# the engine can smoothly transition to adjacent topics rather than jumping
# to something completely unrelated.
# This ensures the decision-tree "branching" feels natural.
TOPIC_ADJACENCY = {
    # Technology cluster
    "Software-Dev":     ["Data-Analytics", "Hardware-Systems", "Cyber-Defense", "Digital-Media"],
    "Hardware-Systems": ["Software-Dev", "Electrical-Power", "Cyber-Defense"],
    "Data-Analytics":   ["Software-Dev", "Finance-Acct", "Lab-Research"],
    "Cyber-Defense":    ["Software-Dev", "Hardware-Systems", "Law-Enforce"],
    "Digital-Media":    ["Software-Dev", "Visual-Design", "Creative-Skill"],
    # Engineering cluster
    "Civil-Build":      ["Spatial-Design", "Mechanical-Design", "Electrical-Power", "Industrial-Ops"],
    "Mechanical-Design":["Civil-Build", "Industrial-Ops", "Electrical-Power", "Hardware-Systems"],
    "Electrical-Power": ["Mechanical-Design", "Hardware-Systems", "Civil-Build"],
    "Industrial-Ops":   ["Mechanical-Design", "Finance-Acct", "Civil-Build", "Admin-Skill"],
    "Spatial-Design":   ["Civil-Build", "Visual-Design", "Creative-Skill"],
    # Healthcare cluster
    "Patient-Care":     ["Medical-Lab", "Rehab-Therapy", "Health-Admin", "People-Skill"],
    "Medical-Lab":      ["Patient-Care", "Lab-Research", "Rehab-Therapy"],
    "Rehab-Therapy":    ["Patient-Care", "People-Skill", "Physical-Skill"],
    "Health-Admin":     ["Patient-Care", "Admin-Skill", "Finance-Acct"],
    # Business cluster
    "Finance-Acct":     ["Marketing-Sales", "Startup-Venture", "Admin-Skill", "Data-Analytics"],
    "Marketing-Sales":  ["Startup-Venture", "Finance-Acct", "People-Skill", "Digital-Media"],
    "Startup-Venture":  ["Marketing-Sales", "Finance-Acct", "Industrial-Ops"],
    # Education & Social cluster
    "Teaching-Ed":      ["People-Skill", "Community-Serve", "Admin-Skill"],
    "Community-Serve":  ["Teaching-Ed", "Law-Enforce", "People-Skill"],
    "Law-Enforce":      ["Community-Serve", "Physical-Skill", "Cyber-Defense"],
    # Arts cluster
    "Visual-Design":    ["Digital-Media", "Creative-Skill", "Spatial-Design"],
    "Creative-Skill":   ["Visual-Design", "Digital-Media", "Teaching-Ed"],
    # Other
    "Maritime-Sea":     ["Mechanical-Design", "Electrical-Power", "Physical-Skill"],
    "Agri-Nature":      ["Field-Research", "Lab-Research", "Physical-Skill"],
    "Field-Research":   ["Lab-Research", "Agri-Nature", "Community-Serve"],
    "Lab-Research":     ["Medical-Lab", "Field-Research", "Data-Analytics"],
    "Hospitality-Svc":  ["Marketing-Sales", "People-Skill", "Admin-Skill"],
    # Skill traits adjacency
    "Technical-Skill":  ["Software-Dev", "Hardware-Systems", "Mechanical-Design"],
    "People-Skill":     ["Teaching-Ed", "Community-Serve", "Hospitality-Svc", "Patient-Care"],
    "Creative-Skill":   ["Visual-Design", "Digital-Media", "Spatial-Design"],
    "Analytical-Skill": ["Data-Analytics", "Lab-Research", "Finance-Acct"],
    "Physical-Skill":   ["Law-Enforce", "Maritime-Sea", "Rehab-Therapy", "Agri-Nature"],
    "Admin-Skill":      ["Finance-Acct", "Industrial-Ops", "Health-Admin"],
}

# ==================== QUESTION CATEGORY → TRAIT DOMAIN MAPPING ====================
# Maps question categories to the primary trait domain they belong to.
# Used for topic continuity: if user's current thread is "Software-Dev",
# we know "Technology Career" and "Programming Specialization" categories are on-topic.
CATEGORY_TRAIT_DOMAIN = {
    # Broad discovery
    "dream career": "broad", "work environment": "broad", "daily work": "broad",
    "skill mastery": "broad", "career achievement": "broad",
    # Situational
    "situational - emergency": "Patient-Care", "situational - teamwork": "People-Skill",
    "situational - accident": "Patient-Care", "situational - community": "Community-Serve",
    "situational - leadership": "Admin-Skill", "situational - disaster response": "Community-Serve",
    "situational - school event": "Creative-Skill", "situational - ethics": "Law-Enforce",
    "situational - family business": "Finance-Acct", "situational - mental health": "Rehab-Therapy",
    "situational - technology crisis": "Software-Dev", "situational - technology": "Software-Dev",
    "situational - survival": "Physical-Skill", "situational - business": "Finance-Acct",
    "situational - environmental": "Agri-Nature", "situational - event planning": "Hospitality-Svc",
    "situational - cyberbullying": "Cyber-Defense", "situational - family health": "Patient-Care",
    "situational - media": "Digital-Media", "situational - academic integrity": "Teaching-Ed",
    "situational - financial decision": "Finance-Acct", "situational - career fair": "broad",
    "situational - community problem": "Community-Serve", "situational - friend support": "People-Skill",
    "situational - power outage": "Electrical-Power", "situational - accreditation": "Admin-Skill",
    "situational - medical emergency": "Patient-Care", "situational - group research": "Lab-Research",
    "situational - typhoon preparation": "Community-Serve", "situational - job shadow": "broad",
    "situational - cyber attack": "Cyber-Defense", "situational - mall jobs": "broad",
    "situational - sick pet": "Agri-Nature", "situational - environmental initiative": "Agri-Nature",
    "situational - found wallet": "Community-Serve", "situational - factory pollution": "Industrial-Ops",
    "situational - helping classmate": "People-Skill", "situational - family reunion": "Hospitality-Svc",
    "situational - water shortage": "Community-Serve", "situational - dream internship": "broad",
    # Scale-based self-assessment
    "scale - math": "Data-Analytics", "scale - stress": "Patient-Care",
    "scale - communication": "Marketing-Sales", "scale - physical": "Physical-Skill",
    "scale - creativity": "Visual-Design",
    # Academic
    "academic - favorite": "broad", "academic - challenge": "broad",
    "academic - study style": "broad",
    # Lifestyle & Values
    "lifestyle": "broad", "career values": "broad",
    "career priority": "broad", "salary importance": "Finance-Acct",
    "international work": "Hospitality-Svc", "work schedule": "broad",
    # Professional
    "professional licensure": "broad", "interest type": "broad",
    "fun - role": "broad", "fun - superpower": "broad", "work lifestyle": "broad",
    # Philippine-specific
    "ph industry": "broad", "board exam preference": "broad",
    "work location": "broad", "dream employer": "broad",
    # Skills
    "language skill": "People-Skill", "tech skill": "Software-Dev",
    "leadership skill": "Admin-Skill", "stress management": "Patient-Care",
    "math skill": "Data-Analytics", "science skill": "Lab-Research",
    # Personality
    "personality": "broad", "hobbies": "broad",
    "entertainment preference": "broad", "role model": "broad",
    # School
    "school involvement": "broad", "project preference": "broad",
    "favorite subject": "broad", "challenging subject": "broad",
    # Future
    "future vision": "broad", "life legacy": "broad", "career fear": "broad",
    # Problem Solving
    "problem solving": "broad", "decision making": "broad",
    "learning style": "broad", "conflict resolution": "People-Skill",
    "team role": "broad",
    # Community/Disaster/Event
    "community scenario": "Community-Serve", "survival scenario": "Physical-Skill",
    "disaster response": "Community-Serve", "event planning": "Hospitality-Svc",
    "emotional intelligence": "People-Skill",
}


# ==================== UNIFIED PROFILE-TO-TRAITS MAPPING ====================
# Single source of truth for mapping user profile selections to trait tags.
# Used by: _calculate_profile_bonus(), _get_profile_priority_traits(),
#          _get_profile_priority_traits_ranked(), create_session()
UNIFIED_PROFILE_TO_TRAITS = {
    # Academic Interests
    "science": ["Lab-Research", "Medical-Lab"],
    "biology": ["Medical-Lab", "Lab-Research", "Patient-Care"],
    "chemistry": ["Medical-Lab", "Lab-Research"],
    "physics": ["Mechanical-Design", "Electrical-Power", "Civil-Build"],
    "environment": ["Agri-Nature", "Field-Research"],
    "earth_science": ["Field-Research", "Agri-Nature", "Lab-Research"],
    "programming": ["Software-Dev", "Data-Analytics", "Cyber-Defense"],
    "computer": ["Software-Dev", "Hardware-Systems", "Data-Analytics"],
    "data": ["Data-Analytics", "Software-Dev"],
    "ai": ["Software-Dev", "Data-Analytics"],
    "cybersecurity": ["Cyber-Defense", "Software-Dev"],
    "robotics": ["Hardware-Systems", "Software-Dev", "Mechanical-Design"],
    "game_dev": ["Digital-Media", "Software-Dev", "Game-Dev"],
    "web_tech": ["Software-Dev", "Web-Dev", "Digital-Media"],
    "multimedia": ["Digital-Media", "Animation-3D", "Creative-Skill"],
    "networking": ["Cloud-Systems", "Hardware-Systems", "Software-Dev"],
    "software_eng": ["Software-Dev", "Data-Analytics", "Web-Dev"],
    "database": ["Data-Analytics", "Software-Dev", "Cloud-Systems"],
    "health_info": ["Health-Admin", "Admin-Skill", "Medical-Lab"],
    "engineering": ["Civil-Build", "Mechanical-Design", "Electrical-Power", "Industrial-Ops"],
    "mechanical": ["Mechanical-Design", "Industrial-Ops"],
    "electrical": ["Electrical-Power", "Hardware-Systems"],
    "civil": ["Civil-Build", "Spatial-Design"],
    "architecture": ["Spatial-Design", "Civil-Build", "Visual-Design"],
    "industrial": ["Industrial-Ops", "Mechanical-Design"],
    "aeronautical": ["Mechanical-Design", "Hardware-Systems", "Technical-Skill"],
    "geodetic": ["Civil-Build", "Field-Research", "Technical-Skill"],
    "landscape": ["Spatial-Design", "Creative-Skill", "Environmental-Eng"],
    "industrial_design": ["Spatial-Design", "Creative-Skill", "Mechanical-Design"],
    "aircraft_maint": ["Hardware-Systems", "Mechanical-Design", "Technical-Skill"],
    "marine_eng": ["Maritime-Sea", "Mechanical-Design", "Technical-Skill"],
    "business": ["Startup-Venture", "Marketing-Sales", "Finance-Acct"],
    "finance": ["Finance-Acct", "Startup-Venture"],
    "marketing": ["Marketing-Sales", "Startup-Venture"],
    "accounting": ["Finance-Acct", "Admin-Skill"],
    "economics": ["Finance-Acct"],
    "management": ["Admin-Skill", "Startup-Venture", "Industrial-Ops"],
    "real_estate": ["Marketing-Sales", "Finance-Acct"],
    "human_resource": ["HR-Management", "Admin-Skill", "People-Skill"],
    "operations": ["Industrial-Ops", "Admin-Skill", "Mechanical-Design"],
    "customs": ["Finance-Acct", "Admin-Skill", "Industrial-Ops"],
    "agribusiness": ["Agri-Nature", "Startup-Venture", "Admin-Skill"],
    "office_admin": ["Admin-Skill", "Hospitality-Svc"],
    "startup": ["Startup-Venture", "Marketing-Sales", "Creative-Skill"],
    "art": ["Visual-Design", "Creative-Skill", "Digital-Media"],
    "music": ["Creative-Skill", "Performing-Arts"],
    "film": ["Digital-Media", "Creative-Skill", "Film-Broadcast"],
    "writing": ["Creative-Skill"],
    "photography": ["Visual-Design", "Digital-Media"],
    "animation": ["Digital-Media", "Visual-Design", "Animation-3D"],
    "fashion": ["Visual-Design", "Creative-Skill", "Spatial-Design"],
    "theater": ["Performing-Arts", "Creative-Skill", "Visual-Design"],
    "advertising_arts": ["Visual-Design", "Marketing-Sales", "Creative-Skill"],
    "music_production": ["Performing-Arts", "Digital-Media", "Creative-Skill"],
    "fine_arts": ["Visual-Design", "Creative-Skill"],
    "clothing_tech": ["Spatial-Design", "Technical-Skill", "Creative-Skill"],
    "medical": ["Patient-Care", "Medical-Lab", "Rehab-Therapy"],
    "nursing": ["Patient-Care"],
    "psychology": ["Rehab-Therapy", "Community-Serve", "People-Skill", "Counseling"],
    "pharmacy": ["Medical-Lab", "Lab-Research", "Pharmacy"],
    "physical_therapy": ["Rehab-Therapy", "Patient-Care", "Physical-Skill"],
    "nutrition": ["Patient-Care", "Lab-Research", "Nutrition-Diet"],
    "medical_tech": ["Medical-Lab", "Lab-Research"],
    "dentistry": ["Patient-Care", "Medical-Lab"],
    "occupational_therapy": ["Rehab-Therapy", "Patient-Care", "People-Skill"],
    "speech_therapy": ["Rehab-Therapy", "Patient-Care", "People-Skill"],
    "respiratory": ["Rehab-Therapy", "Patient-Care", "Technical-Skill"],
    "radiology": ["Medical-Lab", "Technical-Skill"],
    "optometry": ["Medical-Lab", "Patient-Care", "Technical-Skill"],
    "midwifery": ["Patient-Care", "People-Skill"],
    "public_health": ["Public-Health", "Community-Serve", "People-Skill"],
    "education": ["Teaching-Ed"],
    "law": ["Law-Enforce", "Legal-Practice"],
    "politics": ["Community-Serve"],
    "social": ["Community-Serve", "Rehab-Therapy", "Social-Work"],
    "history": ["Community-Serve"],
    "communication": ["Marketing-Sales", "Teaching-Ed", "Admin-Skill", "Film-Broadcast"],
    "philosophy": ["Community-Serve", "Teaching-Ed"],
    "criminology": ["Law-Enforce", "Community-Serve", "Forensic-Sci"],
    "early_childhood": ["Teaching-Ed", "People-Skill", "Creative-Skill"],
    "special_education": ["Teaching-Ed", "People-Skill", "Counseling"],
    "library_science": ["Teaching-Ed", "Admin-Skill"],
    "public_admin": ["Community-Serve", "Admin-Skill"],
    "intl_studies": ["Community-Serve", "People-Skill"],
    "sociology": ["Community-Serve", "People-Skill"],
    "linguistics": ["Teaching-Ed", "People-Skill"],
    "dev_communication": ["Community-Serve", "People-Skill", "Marketing-Sales"],
    "community_dev": ["Community-Serve", "Social-Work", "People-Skill"],
    "legal_mgmt": ["Legal-Practice", "Admin-Skill", "Law-Enforce"],
    "maritime": ["Maritime-Sea", "Mechanical-Design"],
    "aviation": ["Hardware-Systems", "Mechanical-Design"],
    "logistics": ["Industrial-Ops", "Admin-Skill"],
    "marine_transport": ["Maritime-Sea", "Physical-Skill"],
    "marine_science": ["Field-Research", "Maritime-Sea", "Lab-Research"],
    "sports": ["Physical-Skill", "Rehab-Therapy", "Teaching-Ed", "Sports-Ed"],
    "tourism": ["Hospitality-Svc", "Tourism-Travel"],
    "food": ["Hospitality-Svc", "Culinary-Arts"],
    "agriculture": ["Agri-Nature", "Field-Research"],
    "veterinary": ["Agri-Nature", "Patient-Care", "Lab-Research"],
    "military": ["Law-Enforce", "Physical-Skill"],
    "forestry": ["Agri-Nature", "Field-Research", "Physical-Skill"],
    "fisheries": ["Agri-Nature", "Maritime-Sea", "Field-Research"],
    "hotel_mgmt": ["Hospitality-Svc", "Admin-Skill", "People-Skill"],
    "exercise_science": ["Physical-Skill", "Rehab-Therapy", "Sports-Ed"],
    "tvet": ["Technical-Skill", "Mechanical-Design", "Teaching-Ed"],
    "culinary_mgmt": ["Culinary-Arts", "Hospitality-Svc", "Startup-Venture"],
    # Skills
    "programming_skill": ["Software-Dev", "Data-Analytics"],
    "data_analysis": ["Data-Analytics", "Software-Dev"],
    "web_development": ["Software-Dev", "Digital-Media", "Web-Dev"],
    "graphic_design": ["Visual-Design", "Digital-Media"],
    "video_editing": ["Digital-Media", "Creative-Skill", "Film-Broadcast"],
    "math_skills": ["Data-Analytics", "Finance-Acct"],
    "laboratory": ["Lab-Research", "Medical-Lab"],
    "technical_writing": ["Admin-Skill", "Software-Dev"],
    "electronics": ["Electrical-Power", "Hardware-Systems"],
    "drafting": ["Spatial-Design", "Civil-Build", "Mechanical-Design"],
    "accounting_skill": ["Finance-Acct", "Admin-Skill"],
    "networking_skill": ["Cloud-Systems", "Hardware-Systems"],
    "database_skill": ["Data-Analytics", "Software-Dev", "Cloud-Systems"],
    "statistical_analysis": ["Data-Analytics", "Lab-Research"],
    "surveying": ["Civil-Build", "Field-Research"],
    "lab_equipment": ["Medical-Lab", "Lab-Research"],
    "machine_operation": ["Mechanical-Design", "Industrial-Ops"],
    "quality_control": ["Industrial-Ops", "Lab-Research"],
    "mobile_dev": ["Mobile-Dev", "Software-Dev"],
    "ux_ui": ["Visual-Design", "Software-Dev", "Creative-Skill"],
    "audio_production": ["Performing-Arts", "Digital-Media"],
    "film_editing": ["Film-Broadcast", "Digital-Media"],
    "navigation": ["Maritime-Sea", "Physical-Skill"],
    "flight_ops": ["Hardware-Systems", "Mechanical-Design"],
    "env_assessment": ["Environmental-Eng", "Field-Research", "Environmental-Sci"],
    "public_speaking": ["Teaching-Ed", "Marketing-Sales"],
    "writing_skill": ["Creative-Skill", "Admin-Skill"],
    "presentation": ["Marketing-Sales", "Teaching-Ed"],
    "negotiation": ["Marketing-Sales", "Startup-Venture"],
    "foreign_language": ["Teaching-Ed", "Hospitality-Svc"],
    "filipino_language": ["Teaching-Ed", "Community-Serve"],
    "social_media": ["Digital-Media", "Marketing-Sales"],
    "journalism_skill": ["Film-Broadcast", "Marketing-Sales"],
    "persuasion": ["Marketing-Sales", "Startup-Venture", "People-Skill"],
    "interviewing": ["People-Skill", "Law-Enforce"],
    "report_writing": ["Admin-Skill", "Lab-Research"],
    "sign_language": ["Teaching-Ed", "People-Skill", "Rehab-Therapy"],
    "leadership": ["Startup-Venture", "Admin-Skill"],
    "project_management": ["Admin-Skill", "Industrial-Ops"],
    "team_management": ["Admin-Skill", "People-Skill"],
    "decision_making": ["Startup-Venture", "Admin-Skill"],
    "planning": ["Admin-Skill", "Industrial-Ops"],
    "time_management": ["Admin-Skill", "Industrial-Ops"],
    "event_management": ["Hospitality-Svc", "Admin-Skill", "Marketing-Sales"],
    "budgeting": ["Finance-Acct", "Admin-Skill"],
    "strategic_thinking": ["Startup-Venture", "Admin-Skill", "Data-Analytics"],
    "delegation": ["Admin-Skill", "Startup-Venture", "People-Skill"],
    "teamwork": ["People-Skill", "Industrial-Ops"],
    "empathy": ["Patient-Care", "Rehab-Therapy"],
    "customer_service": ["Hospitality-Svc", "People-Skill"],
    "mentoring": ["Teaching-Ed"],
    "conflict_resolution": ["People-Skill", "Community-Serve"],
    "counseling": ["Rehab-Therapy", "People-Skill", "Community-Serve", "Counseling"],
    "patient_care": ["Patient-Care", "Rehab-Therapy"],
    "cultural_sensitivity": ["Community-Serve", "People-Skill", "Hospitality-Svc"],
    "networking_people": ["Marketing-Sales", "Startup-Venture", "People-Skill"],
    "child_interaction": ["Teaching-Ed", "People-Skill"],
    "elderly_care": ["Patient-Care", "People-Skill", "Rehab-Therapy"],
    "critical_thinking": ["Data-Analytics", "Lab-Research"],
    "problem_solving": ["Software-Dev", "Mechanical-Design", "Data-Analytics"],
    "research": ["Lab-Research", "Field-Research"],
    "attention_detail": ["Admin-Skill", "Finance-Acct"],
    "logical_reasoning": ["Data-Analytics", "Software-Dev"],
    "case_analysis": ["Legal-Practice", "Law-Enforce"],
    "scientific_method": ["Lab-Research", "Field-Research"],
    "financial_analysis": ["Finance-Acct", "Data-Analytics"],
    "risk_assessment": ["Industrial-Ops", "Admin-Skill"],
    "policy_analysis": ["Community-Serve", "Admin-Skill"],
    "creativity": ["Creative-Skill", "Visual-Design", "Digital-Media"],
    "artistic": ["Visual-Design", "Creative-Skill"],
    "music_skill": ["Creative-Skill", "Performing-Arts"],
    "storytelling": ["Creative-Skill", "Digital-Media"],
    "design_thinking": ["Visual-Design", "Creative-Skill"],
    "photography_skill": ["Visual-Design", "Digital-Media"],
    "cooking": ["Hospitality-Svc", "Culinary-Arts"],
    "first_aid": ["Patient-Care", "Rehab-Therapy"],
    "sports_fitness": ["Physical-Skill", "Rehab-Therapy", "Sports-Ed"],
    "driving": ["Maritime-Sea", "Industrial-Ops"],
    "gardening": ["Agri-Nature", "Field-Research"],
    "repair_maintenance": ["Mechanical-Design", "Electrical-Power"],
    # Strand-related keywords (for free text matching)
    "stem": ["Software-Dev", "Lab-Research", "Data-Analytics"],
    "abm": ["Finance-Acct", "Marketing-Sales", "Startup-Venture"],
    "humss": ["Teaching-Ed", "Community-Serve", "Law-Enforce"],
    "tvl": ["Hospitality-Svc", "Mechanical-Design", "Software-Dev"],
    "gas": ["Community-Serve", "Admin-Skill", "Teaching-Ed"],
    # Common aliases
    "fitness": ["Physical-Skill", "Rehab-Therapy"],
    "sports & fitness": ["Physical-Skill", "Rehab-Therapy"],
    "physical education": ["Physical-Skill", "Teaching-Ed"],
    "musical": ["Creative-Skill", "Performing-Arts"],
    "musical ability": ["Creative-Skill", "Performing-Arts"],
    "singing": ["Creative-Skill", "Performing-Arts"],
    "instrument": ["Creative-Skill", "Performing-Arts"],
    "design": ["Visual-Design", "Spatial-Design", "Digital-Media"],
    "graphic design": ["Visual-Design", "Digital-Media"],
    "interior design": ["Spatial-Design", "Visual-Design"],
    "game": ["Digital-Media", "Software-Dev", "Game-Dev"],
    "seaman": ["Maritime-Sea"],
    "seafaring": ["Maritime-Sea", "Physical-Skill"],
    "ship": ["Maritime-Sea", "Mechanical-Design"],
    "ocean": ["Maritime-Sea", "Field-Research"],
    "port": ["Maritime-Sea", "Industrial-Ops"],
    "vessel": ["Maritime-Sea", "Mechanical-Design"],
    "deck officer": ["Maritime-Sea", "Physical-Skill"],
    "engine officer": ["Maritime-Sea", "Mechanical-Design"],
    "hotel": ["Hospitality-Svc"],
    "culinary": ["Hospitality-Svc", "Culinary-Arts"],
    "sports and fitness": ["Physical-Skill", "Rehab-Therapy"],
    "athletic": ["Physical-Skill"],
}


# ==================== TRAIT-TO-BRANCH MAPPING ====================
# Maps individual trait tags to high-level "branch" domains in the decision tree.
# Each branch represents a major career/interest cluster.
# When a user picks options with a certain trait, that branch gets activated.
TRAIT_TO_BRANCH = {
    # Healthcare branch
    "Patient-Care": "healthcare", "Medical-Lab": "healthcare",
    "Rehab-Therapy": "healthcare", "Health-Admin": "healthcare",
    "Pharmacy": "healthcare", "Public-Health": "healthcare",
    "Nutrition-Diet": "healthcare",
    # Technology branch
    "Software-Dev": "technology", "Hardware-Systems": "technology",
    "Data-Analytics": "technology", "Cyber-Defense": "technology",
    "Web-Dev": "technology", "Mobile-Dev": "technology",
    "Game-Dev": "technology", "AI-ML": "technology",
    "Cloud-Systems": "technology",
    # Engineering branch
    "Civil-Build": "engineering", "Mechanical-Design": "engineering",
    "Electrical-Power": "engineering", "Industrial-Ops": "engineering",
    "Spatial-Design": "engineering", "Environmental-Eng": "engineering",
    # Business branch
    "Finance-Acct": "business", "Marketing-Sales": "business",
    "Startup-Venture": "business", "Admin-Skill": "business",
    "HR-Management": "business",
    # Education & Social branch
    "Teaching-Ed": "education", "Counseling": "education",
    "Sports-Ed": "education",
    "Community-Serve": "public_service",
    "Law-Enforce": "public_service", "Legal-Practice": "public_service",
    "Social-Work": "public_service",
    "People-Skill": "social",
    # Creative branch
    "Visual-Design": "creative", "Creative-Skill": "creative",
    "Digital-Media": "creative", "Performing-Arts": "creative",
    "Film-Broadcast": "creative", "Animation-3D": "creative",
    # Maritime branch
    "Maritime-Sea": "maritime",
    # Agriculture/Environment branch
    "Agri-Nature": "agriculture", "Field-Research": "agriculture",
    "Lab-Research": "science", "Environmental-Sci": "science",
    "Food-Science": "science", "Forensic-Sci": "science",
    # Hospitality branch
    "Hospitality-Svc": "hospitality", "Tourism-Travel": "hospitality",
    "Culinary-Arts": "hospitality",
    # Physical/Practical branch
    "Physical-Skill": "physical",
    "Technical-Skill": "technology",
    # RIASEC-style traits (from course trait_tags)
    "Investigative": "science", "Realistic": "engineering",
    "Artistic": "creative", "Social": "social",
    "Enterprising": "business", "Conventional": "business",
    "Analytical-Skill": "technology",
}

# Maps branch domains to their adjacent/related branches
# Used for smooth transitions in the decision tree
BRANCH_ADJACENCY = {
    "healthcare": ["science", "social", "education"],
    "technology": ["engineering", "science", "creative"],
    "engineering": ["technology", "science", "business"],
    "business": ["technology", "social", "hospitality"],
    "education": ["social", "healthcare", "public_service"],
    "public_service": ["social", "education", "healthcare"],
    "social": ["education", "public_service", "healthcare"],
    "creative": ["technology", "hospitality", "social"],
    "maritime": ["engineering", "physical", "technology"],
    "agriculture": ["science", "physical", "education"],
    "science": ["healthcare", "technology", "agriculture"],
    "hospitality": ["business", "creative", "social"],
    "physical": ["healthcare", "maritime", "agriculture"],
}


# ==================== DECISION TREE: QUESTION NODE CLASSIFICATION ====================
# Every question is classified as a node in the decision tree with:
#   level  : Tree depth (0=root, 1=branch, 2=deep, 3=confirmation)
#   weight : Scoring multiplier - deeper questions carry more weight
#   branches: Which tree branches this question is relevant to
#
# The algorithm traverses deeper as the assessment progresses:
#   Rounds  1-5  → Level 0 (Root: broad discovery)
#   Rounds  6-15 → Level 0-1 (Branch exploration)
#   Rounds 16-30 → Level 1-2 (Deep probing)
#   Rounds 31-50 → Level 2-3 (Situational confirmation)

QUESTION_TREE_NODES = {
    # ===== LEVEL 0: ROOT - Broad Career Discovery (Weight 1.0) =====
    # These are entry points. Profile determines which gets asked first.
    1:  {"level": 0, "weight": 1.0, "branches": ["healthcare", "technology", "engineering", "business", "education", "public_service", "creative", "maritime", "hospitality", "agriculture"]},
    2:  {"level": 0, "weight": 1.0, "branches": ["healthcare", "technology", "engineering", "business", "education", "creative", "agriculture"]},
    3:  {"level": 0, "weight": 1.0, "branches": ["healthcare", "technology", "engineering", "business", "creative", "maritime", "hospitality", "agriculture"]},
    4:  {"level": 0, "weight": 1.0, "branches": ["healthcare", "technology", "engineering", "business", "creative", "science"]},
    5:  {"level": 0, "weight": 1.0, "branches": ["healthcare", "technology", "business", "education", "public_service", "creative"]},

    # ===== LEVEL 1: BRANCH EXPLORATION (Weight 1.5) =====
    # Self-assessment scales
    26: {"level": 1, "weight": 1.5, "branches": ["technology", "engineering", "business", "science"]},  # Scale - Math
    27: {"level": 1, "weight": 1.5, "branches": ["healthcare", "social", "science"]},                   # Scale - Stress
    28: {"level": 1, "weight": 1.5, "branches": ["business", "social", "education"]},                   # Scale - Communication
    29: {"level": 1, "weight": 1.5, "branches": ["healthcare", "physical", "agriculture"]},             # Scale - Physical
    30: {"level": 1, "weight": 1.5, "branches": ["creative", "business", "technology"]},                # Scale - Creativity
    # Academic background
    31: {"level": 1, "weight": 1.5, "branches": ["technology", "science", "creative", "business", "social"]},  # Academic - Favorite
    32: {"level": 1, "weight": 1.5, "branches": ["technology", "science", "healthcare", "business"]},          # Academic - Challenge
    33: {"level": 1, "weight": 1.5, "branches": ["technology", "science", "creative"]},                        # Academic - Study Style
    # Lifestyle & values
    34: {"level": 1, "weight": 1.5, "branches": ["business", "healthcare", "creative", "agriculture"]},       # Lifestyle
    35: {"level": 1, "weight": 1.5, "branches": ["business", "public_service", "creative"]},                  # Career Values
    # Professional
    36: {"level": 1, "weight": 1.5, "branches": ["healthcare", "engineering", "business", "education"]},       # Professional Licensure
    37: {"level": 1, "weight": 1.2, "branches": ["healthcare", "technology", "engineering", "business", "creative", "science", "agriculture", "social"]},  # Interest Type
    38: {"level": 1, "weight": 1.2, "branches": ["healthcare", "technology", "business", "science", "agriculture"]},  # Fun - Role
    39: {"level": 1, "weight": 1.2, "branches": ["healthcare", "technology", "business", "creative", "science"]},     # Fun - Superpower
    40: {"level": 1, "weight": 1.5, "branches": ["healthcare", "business", "education", "science", "creative", "agriculture"]},  # Work Lifestyle
    # Philippine-specific
    51: {"level": 1, "weight": 1.5, "branches": ["healthcare", "business", "hospitality", "agriculture", "engineering"]},  # PH Industry
    52: {"level": 1, "weight": 1.5, "branches": ["healthcare", "engineering", "business", "education"]},                   # Board Exam
    53: {"level": 1, "weight": 1.3, "branches": ["healthcare", "business", "hospitality", "agriculture"]},                 # Work Location
    54: {"level": 1, "weight": 1.3, "branches": ["healthcare", "business", "hospitality", "education", "technology"]},     # Dream Employer

    # ===== LEVEL 2: DEEP PROBING (Weight 2.0) =====
    # Skill assessments
    55: {"level": 2, "weight": 2.0, "branches": ["social", "business", "education"]},                  # Language Skill
    56: {"level": 2, "weight": 2.0, "branches": ["technology", "business", "creative"]},                # Tech Skill
    57: {"level": 2, "weight": 2.0, "branches": ["business", "education", "public_service", "social"]}, # Leadership Skill
    58: {"level": 2, "weight": 2.0, "branches": ["healthcare", "business", "science"]},                 # Stress Management
    59: {"level": 2, "weight": 2.0, "branches": ["technology", "engineering", "business", "science"]},  # Math Skill
    60: {"level": 2, "weight": 2.0, "branches": ["healthcare", "science", "agriculture"]},              # Science Skill
    # Career priorities
    61: {"level": 2, "weight": 2.0, "branches": ["business", "healthcare", "public_service", "creative"]},  # Career Priority
    62: {"level": 2, "weight": 2.0, "branches": ["business", "healthcare", "technology"]},                   # Salary Importance
    63: {"level": 2, "weight": 2.0, "branches": ["healthcare", "hospitality", "maritime", "business"]},      # International Work
    64: {"level": 2, "weight": 2.0, "branches": ["healthcare", "business", "hospitality", "creative"]},      # Work Schedule
    # Personality & interests
    65: {"level": 2, "weight": 2.0, "branches": ["business", "healthcare", "creative", "technology"]},       # Personality
    66: {"level": 2, "weight": 2.0, "branches": ["creative", "science", "physical", "agriculture"]},         # Hobbies
    67: {"level": 2, "weight": 1.8, "branches": ["creative", "healthcare", "business", "agriculture"]},      # Entertainment
    68: {"level": 2, "weight": 1.8, "branches": ["healthcare", "science", "business", "public_service"]},    # Role Model
    # School & academic deep
    69: {"level": 2, "weight": 2.0, "branches": ["technology", "creative", "business", "public_service"]},   # School Involvement
    70: {"level": 2, "weight": 2.0, "branches": ["science", "creative", "social", "technology"]},            # Project Preference
    71: {"level": 2, "weight": 2.0, "branches": ["technology", "science", "creative", "business", "social"]}, # Favorite Subject
    72: {"level": 2, "weight": 2.0, "branches": ["technology", "science", "healthcare", "business"]},        # Challenging Subject
    # Future & philosophy
    73: {"level": 2, "weight": 2.0, "branches": ["business", "healthcare", "public_service", "creative"]},   # Future Vision
    74: {"level": 2, "weight": 1.8, "branches": ["healthcare", "public_service", "creative", "agriculture"]}, # Life Legacy
    75: {"level": 2, "weight": 1.8, "branches": ["healthcare", "business", "creative", "public_service"]},   # Career Fear
    # Problem solving & cognition
    76: {"level": 2, "weight": 2.0, "branches": ["technology", "science", "healthcare", "business"]},        # Problem Solving
    77: {"level": 2, "weight": 2.0, "branches": ["business", "healthcare", "science", "social"]},            # Decision Making
    78: {"level": 2, "weight": 2.0, "branches": ["technology", "science", "creative", "healthcare"]},        # Learning Style
    79: {"level": 2, "weight": 2.0, "branches": ["social", "healthcare", "business"]},                       # Conflict Resolution
    80: {"level": 2, "weight": 2.0, "branches": ["business", "technology", "science", "social"]},            # Team Role

    # ===== LEVEL 3: SITUATIONAL CONFIRMATION (Weight 2.5) =====
    # These scenario questions validate trait patterns through real-world situations
    23: {"level": 3, "weight": 2.5, "branches": ["healthcare", "technology", "public_service"]},          # Situational - Emergency
    24: {"level": 3, "weight": 2.5, "branches": ["business", "social", "technology"]},                    # Situational - Teamwork
    25: {"level": 3, "weight": 2.5, "branches": ["healthcare", "public_service", "business"]},            # Situational - Accident
    41: {"level": 3, "weight": 2.5, "branches": ["healthcare", "business", "agriculture", "creative"]},   # Community Scenario
    42: {"level": 3, "weight": 2.5, "branches": ["agriculture", "healthcare", "social", "business"]},     # Survival Scenario
    43: {"level": 3, "weight": 2.5, "branches": ["healthcare", "engineering", "social", "business"]},     # Disaster Response
    44: {"level": 3, "weight": 2.5, "branches": ["business", "creative", "hospitality"]},                 # Event Planning
    45: {"level": 3, "weight": 2.5, "branches": ["social", "healthcare", "technology", "public_service"]}, # Emotional Intelligence
    81: {"level": 3, "weight": 2.5, "branches": ["engineering", "healthcare", "public_service", "business"]},  # Sit - Emergency 2
    82: {"level": 3, "weight": 2.5, "branches": ["business", "agriculture", "hospitality", "creative"]},      # Sit - Community
    83: {"level": 3, "weight": 2.5, "branches": ["technology", "business", "science", "social"]},              # Sit - Leadership
    84: {"level": 3, "weight": 2.5, "branches": ["public_service", "healthcare", "creative"]},                 # Sit - Disaster Response 2
    85: {"level": 3, "weight": 2.5, "branches": ["creative", "hospitality", "agriculture", "science"]},       # Sit - School Event
    86: {"level": 3, "weight": 2.5, "branches": ["public_service", "technology", "business"]},                 # Sit - Ethics
    87: {"level": 3, "weight": 2.5, "branches": ["business", "hospitality", "creative"]},                      # Sit - Family Business
    88: {"level": 3, "weight": 2.5, "branches": ["healthcare", "social", "science"]},                          # Sit - Mental Health
    89: {"level": 3, "weight": 2.5, "branches": ["technology", "public_service", "business"]},                 # Sit - Technology Crisis
    90: {"level": 3, "weight": 2.5, "branches": ["agriculture", "physical", "science", "business"]},           # Sit - Survival
    91: {"level": 3, "weight": 2.5, "branches": ["business", "creative", "technology"]},                       # Sit - Business
    92: {"level": 3, "weight": 2.5, "branches": ["agriculture", "engineering", "social"]},                     # Sit - Environmental
    93: {"level": 3, "weight": 2.5, "branches": ["business", "hospitality", "creative"]},                      # Sit - Event Planning 2
    94: {"level": 3, "weight": 2.5, "branches": ["technology", "social", "public_service"]},                   # Sit - Cyberbullying
    95: {"level": 3, "weight": 2.5, "branches": ["healthcare", "business", "social"]},                         # Sit - Family Health
    96: {"level": 3, "weight": 2.5, "branches": ["public_service", "social", "business"]},                     # Sit - Ethics 2
    97: {"level": 3, "weight": 2.5, "branches": ["technology", "healthcare", "business"]},                     # Sit - Technology
    98: {"level": 3, "weight": 2.5, "branches": ["agriculture", "hospitality", "public_service"]},             # Sit - Media
    99: {"level": 3, "weight": 2.5, "branches": ["public_service", "technology", "education"]},                # Sit - Academic Integrity
    100: {"level": 3, "weight": 2.5, "branches": ["business", "healthcare", "hospitality", "science"]},        # Sit - Financial Decision
    101: {"level": 3, "weight": 2.0, "branches": ["healthcare", "education", "hospitality", "creative", "agriculture"]},  # Sit - Career Fair
    102: {"level": 3, "weight": 2.5, "branches": ["education", "social", "healthcare", "agriculture"]},        # Sit - Community Problem
    103: {"level": 3, "weight": 2.5, "branches": ["physical", "healthcare", "engineering", "social"]},         # Sit - Friend Support
    104: {"level": 3, "weight": 2.5, "branches": ["business", "creative", "technology"]},                      # Sit - Family Business 2
    105: {"level": 3, "weight": 2.5, "branches": ["engineering", "healthcare", "hospitality", "science"]},     # Sit - Power Outage
    106: {"level": 3, "weight": 2.5, "branches": ["education", "healthcare", "hospitality", "science"]},       # Sit - Accreditation
    107: {"level": 3, "weight": 2.5, "branches": ["healthcare", "education", "social"]},                       # Sit - Medical Emergency
    108: {"level": 3, "weight": 2.5, "branches": ["science", "technology", "business"]},                       # Sit - Group Research
    109: {"level": 3, "weight": 2.5, "branches": ["social", "healthcare", "agriculture", "education"]},        # Sit - Typhoon Preparation
    110: {"level": 3, "weight": 2.0, "branches": ["technology", "public_service", "creative", "science"]},     # Sit - Job Shadow
    111: {"level": 3, "weight": 2.5, "branches": ["technology", "public_service", "business"]},                # Sit - Cyber Attack
    112: {"level": 3, "weight": 2.0, "branches": ["business", "healthcare", "education", "hospitality"]},      # Sit - Mall Jobs
    113: {"level": 3, "weight": 2.5, "branches": ["agriculture", "healthcare", "science"]},                    # Sit - Sick Pet
    114: {"level": 3, "weight": 2.5, "branches": ["agriculture", "education", "engineering", "social"]},       # Sit - Environmental Initiative
    115: {"level": 3, "weight": 2.5, "branches": ["social", "public_service", "hospitality", "creative"]},     # Sit - Found Wallet
    116: {"level": 3, "weight": 2.5, "branches": ["engineering", "science", "social"]},                        # Sit - Factory Pollution
    117: {"level": 3, "weight": 2.5, "branches": ["social", "healthcare", "science", "education"]},            # Sit - Helping Classmate
    118: {"level": 3, "weight": 2.0, "branches": ["hospitality", "creative", "engineering", "healthcare"]},    # Sit - Family Reunion
    119: {"level": 3, "weight": 2.5, "branches": ["agriculture", "social", "healthcare", "science"]},          # Sit - Water Shortage
    120: {"level": 3, "weight": 2.0, "branches": ["healthcare", "science", "creative", "public_service"]},     # Sit - Dream Internship

    # ===== DOMAIN-SPECIFIC ENTRY QUESTIONS (Weight 1.0) =====
    121: {"level": 0, "weight": 1.0, "branches": ["technology"]},                       # Entry - Technology
    122: {"level": 0, "weight": 1.0, "branches": ["healthcare"]},                       # Entry - Healthcare
    123: {"level": 0, "weight": 1.0, "branches": ["engineering"]},                      # Entry - Engineering
    124: {"level": 0, "weight": 1.0, "branches": ["business"]},                         # Entry - Business
    125: {"level": 0, "weight": 1.0, "branches": ["creative"]},                         # Entry - Creative
    126: {"level": 0, "weight": 1.0, "branches": ["education"]},                        # Entry - Education
    127: {"level": 0, "weight": 1.0, "branches": ["public_service"]},                   # Entry - Public Service
    128: {"level": 0, "weight": 1.0, "branches": ["science"]},                          # Entry - Science
    129: {"level": 0, "weight": 1.0, "branches": ["agriculture"]},                      # Entry - Agriculture
    130: {"level": 0, "weight": 1.0, "branches": ["maritime"]},                         # Entry - Maritime
    131: {"level": 0, "weight": 1.0, "branches": ["hospitality"]},                      # Entry - Hospitality
    132: {"level": 0, "weight": 1.0, "branches": ["physical"]},                         # Entry - Physical
    133: {"level": 0, "weight": 1.0, "branches": ["social"]},                           # Entry - Social

    # ===== EXPANDED SITUATIONAL (Weight 2.0-2.5) =====
    # Tech situational
    134: {"level": 2, "weight": 2.0, "branches": ["technology", "creative"]},            # Sit - Website Build
    135: {"level": 2, "weight": 2.0, "branches": ["technology", "science"]},             # Sit - Hackathon
    136: {"level": 2, "weight": 2.0, "branches": ["technology", "healthcare", "business"]}, # Sit - App Creation
    137: {"level": 3, "weight": 2.5, "branches": ["technology", "public_service"]},      # Sit - Ransomware
    138: {"level": 2, "weight": 2.0, "branches": ["technology", "education"]},           # Sit - AI System
    139: {"level": 2, "weight": 2.0, "branches": ["technology", "creative"]},            # Sit - Indie Game
    140: {"level": 3, "weight": 2.5, "branches": ["technology", "public_service", "business"]}, # Sit - Barangay Tech
    # Healthcare situational
    141: {"level": 3, "weight": 2.5, "branches": ["healthcare", "public_service"]},      # Sit - Typhoon Healthcare
    142: {"level": 2, "weight": 2.0, "branches": ["healthcare", "science"]},             # Sit - Unknown Illness
    143: {"level": 2, "weight": 2.0, "branches": ["healthcare", "public_service"]},      # Sit - Health Center
    144: {"level": 2, "weight": 2.0, "branches": ["healthcare", "education", "physical"]},# Sit - Health Fair
    # Engineering situational
    145: {"level": 2, "weight": 2.0, "branches": ["engineering", "creative"]},           # Sit - Bridge Project
    146: {"level": 2, "weight": 2.0, "branches": ["engineering", "technology"]},         # Sit - Factory Optimize
    147: {"level": 3, "weight": 2.5, "branches": ["engineering", "science"]},            # Sit - Earthquake Inspect
    # Business situational
    148: {"level": 2, "weight": 2.0, "branches": ["business", "hospitality", "creative"]},# Sit - Food Business
    149: {"level": 2, "weight": 2.0, "branches": ["business", "technology"]},            # Sit - Sari-sari Store
    150: {"level": 2, "weight": 2.0, "branches": ["business", "education", "social"]},   # Sit - HR Department
    # Creative situational
    151: {"level": 2, "weight": 2.0, "branches": ["creative", "business"]},              # Sit - Cultural Show
    152: {"level": 2, "weight": 2.0, "branches": ["creative", "technology"]},            # Sit - Digital Exhibit
    153: {"level": 2, "weight": 2.0, "branches": ["creative", "engineering", "physical"]},# Sit - Park Design
    # Science situational
    154: {"level": 3, "weight": 2.5, "branches": ["science", "engineering", "public_service"]}, # Sit - River Pollution
    155: {"level": 2, "weight": 2.0, "branches": ["science", "business", "hospitality"]},# Sit - Food Testing
    156: {"level": 3, "weight": 2.5, "branches": ["science", "public_service"]},         # Sit - Forensic Lab
    # Education situational
    157: {"level": 2, "weight": 2.0, "branches": ["education", "social"]},               # Sit - Struggling Student
    158: {"level": 3, "weight": 2.5, "branches": ["education", "public_service", "social"]},# Sit - Bullying
    # Public service situational
    159: {"level": 3, "weight": 2.5, "branches": ["public_service", "science", "technology"]},# Sit - Illegal Dumping
    160: {"level": 3, "weight": 2.5, "branches": ["public_service", "social", "healthcare"]}, # Sit - Fire Victim
    # Agriculture/Maritime/Hospitality situational
    161: {"level": 2, "weight": 2.0, "branches": ["agriculture", "technology"]},         # Sit - Modern Farm
    162: {"level": 3, "weight": 2.5, "branches": ["maritime", "engineering"]},           # Sit - Ship Engine
    163: {"level": 2, "weight": 2.0, "branches": ["hospitality", "business", "creative"]},# Sit - Resort Improve
    164: {"level": 2, "weight": 2.0, "branches": ["hospitality", "creative", "business"]},# Sit - Food Festival

    # ===== CROSS-DOMAIN & PERSONALITY (Weight 1.5-2.0) =====
    165: {"level": 1, "weight": 1.5, "branches": ["business", "technology", "creative", "hospitality"]},# Online Business
    166: {"level": 1, "weight": 1.5, "branches": ["education", "healthcare", "public_service", "science"]},# Volunteering
    167: {"level": 1, "weight": 1.5, "branches": ["science", "technology", "agriculture", "social"]},# PH Research
    168: {"level": 2, "weight": 2.0, "branches": ["science", "creative", "technology"]}, # Group Research
    169: {"level": 2, "weight": 2.0, "branches": ["public_service", "healthcare", "technology", "physical"]},# Barangay Budget
    170: {"level": 1, "weight": 1.5, "branches": ["creative", "technology", "hospitality", "science"]},# YouTube Channel
    171: {"level": 1, "weight": 1.5, "branches": ["technology", "healthcare", "creative", "business", "education"]},# Accomplishment
    172: {"level": 1, "weight": 1.5, "branches": ["science", "technology", "creative", "business"]},# School Subjects
    173: {"level": 1, "weight": 1.5, "branches": ["business", "science", "technology", "creative"]},# Leadership Style
    174: {"level": 1, "weight": 1.5, "branches": ["technology", "healthcare", "engineering", "education", "creative", "business"]},# Future Career
    175: {"level": 1, "weight": 1.5, "branches": ["social", "science", "education", "public_service", "agriculture"]},# PH Problem
    176: {"level": 1, "weight": 1.5, "branches": ["technology", "healthcare", "engineering", "business", "creative", "public_service"]},# Study Abroad
    177: {"level": 1, "weight": 1.5, "branches": ["engineering", "science", "creative", "technology"]},# Learning Style
    178: {"level": 1, "weight": 1.5, "branches": ["technology", "healthcare", "business", "public_service", "science"]},# News Interest
    179: {"level": 1, "weight": 1.5, "branches": ["technology", "creative", "business", "science"]},# Team Strength
    180: {"level": 2, "weight": 2.0, "branches": ["technology", "engineering", "science", "agriculture"]},# Invention
    181: {"level": 1, "weight": 1.5, "branches": ["science", "healthcare", "technology", "creative", "business"]},# Work Environment
    182: {"level": 1, "weight": 1.5, "branches": ["science", "healthcare", "business", "creative", "education"]},# Motivation
    183: {"level": 1, "weight": 1.5, "branches": ["physical", "creative", "social", "technology"]},# Stress Handling
    184: {"level": 1, "weight": 1.5, "branches": ["technology", "healthcare", "business", "creative", "science"]},# After-school Club
    185: {"level": 2, "weight": 2.0, "branches": ["technology", "healthcare", "business", "engineering", "creative", "science"]},# Problem Solving
    186: {"level": 2, "weight": 2.0, "branches": ["creative", "business", "technology"]},# NGO Campaign
    187: {"level": 2, "weight": 2.0, "branches": ["science", "agriculture", "technology"]},# Science Fair
    188: {"level": 2, "weight": 2.0, "branches": ["healthcare", "education"]},           # Rural Health
    189: {"level": 2, "weight": 2.0, "branches": ["technology", "healthcare", "engineering", "business"]},# Capstone Project
    190: {"level": 1, "weight": 1.5, "branches": ["technology", "business", "science", "creative", "healthcare"]},# Department Pref
    191: {"level": 2, "weight": 2.0, "branches": ["engineering", "technology", "business"]},# Urban Planning
    192: {"level": 3, "weight": 2.5, "branches": ["healthcare", "education", "social"]}, # Emergency Response
    193: {"level": 1, "weight": 1.5, "branches": ["technology", "healthcare", "engineering", "business", "creative", "science", "hospitality"]},# Internship
    194: {"level": 1, "weight": 1.5, "branches": ["education", "science"]},              # Scale - Communication
    195: {"level": 1, "weight": 1.5, "branches": ["technology", "science", "business"]}, # Scale - Math Comfort
    196: {"level": 1, "weight": 1.5, "branches": ["agriculture", "engineering", "science"]},# Scale - Outdoor Work
    197: {"level": 1, "weight": 1.5, "branches": ["healthcare", "social", "education"]}, # Scale - Helping Others
    198: {"level": 2, "weight": 2.0, "branches": ["technology", "healthcare", "science", "agriculture"]},# Social Innovation
    199: {"level": 1, "weight": 1.5, "branches": ["technology", "healthcare", "business", "creative", "science"]},# TV Genre
    200: {"level": 1, "weight": 1.5, "branches": ["technology", "healthcare", "business", "creative", "science", "education"]},# Bookstore
    # Maritime dedicated
    201: {"level": 2, "weight": 2.0, "branches": ["maritime", "engineering", "hospitality"]},# Sit - Maritime Department
    202: {"level": 2, "weight": 2.0, "branches": ["maritime", "engineering", "science"]},    # Maritime Studies Interest
    203: {"level": 3, "weight": 2.5, "branches": ["maritime", "engineering"]},               # Sit - Typhoon at Sea
    204: {"level": 1, "weight": 1.5, "branches": ["maritime", "hospitality", "business"]},   # Maritime Motivation
    205: {"level": 2, "weight": 2.0, "branches": ["maritime", "engineering"]},               # Maritime Academy Choice
    # Game Development dedicated
    206: {"level": 2, "weight": 2.0, "branches": ["technology", "creative"]},               # Game Genre Choice
    207: {"level": 2, "weight": 2.0, "branches": ["technology", "creative"]},               # Game Dev Parts
    208: {"level": 3, "weight": 2.5, "branches": ["technology", "creative"]},               # Game Jam Competition
    209: {"level": 2, "weight": 2.0, "branches": ["technology", "creative"]},               # Game Engine Choice
    210: {"level": 2, "weight": 2.0, "branches": ["technology", "creative", "business"]},    # Game Industry Internship
    # Web Development dedicated
    211: {"level": 2, "weight": 2.0, "branches": ["technology", "business"]},               # Web App Build
    212: {"level": 3, "weight": 2.5, "branches": ["technology", "business"]},               # Startup Website
    # Animation dedicated
    213: {"level": 2, "weight": 2.0, "branches": ["creative", "technology"]},               # 3D Animation Roles
    # Mobile Dev dedicated
    214: {"level": 2, "weight": 2.0, "branches": ["technology", "creative"]},               # Mobile App Type
    # AI/ML dedicated
    215: {"level": 2, "weight": 2.0, "branches": ["technology", "science"]},                # AI Applications
    # Cybersecurity dedicated
    216: {"level": 2, "weight": 2.0, "branches": ["technology", "public_service"]},          # Cyber Internship
    # Cloud dedicated
    217: {"level": 2, "weight": 2.0, "branches": ["technology", "engineering"]},             # Cloud Computing Interest
    # Data Analytics dedicated
    218: {"level": 2, "weight": 2.0, "branches": ["technology", "science", "business"]},     # Dataset Analysis
    # Digital Media dedicated
    219: {"level": 2, "weight": 2.0, "branches": ["creative", "technology", "business"]},    # Brand Creative Project
    # Cross-domain tech
    220: {"level": 2, "weight": 2.0, "branches": ["technology", "creative", "business"]},    # Tech Startup Focus
    221: {"level": 1, "weight": 1.5, "branches": ["technology", "creative"]},               # YouTube Channel Topic
    222: {"level": 2, "weight": 2.0, "branches": ["technology", "education"]},              # School Tech Project

    # ===== BATCH 3: Massive trait coverage expansion (Q223-Q278) =====
    # Hospitality & Tourism
    223: {"level": 2, "weight": 2.0, "branches": ["hospitality", "business"]},              # Resort Department
    224: {"level": 2, "weight": 2.0, "branches": ["hospitality", "creative"]},              # Tourism Planning
    225: {"level": 2, "weight": 2.0, "branches": ["hospitality", "business"]},              # Hotel Management
    226: {"level": 2, "weight": 2.0, "branches": ["hospitality", "creative", "technology"]},# Tourism Marketing
    # Health & Medical
    227: {"level": 2, "weight": 2.0, "branches": ["healthcare", "science"]},                # Hospital Department
    228: {"level": 2, "weight": 2.0, "branches": ["healthcare", "science"]},                # Pharmacy Career
    229: {"level": 2, "weight": 2.0, "branches": ["healthcare"]},                           # Rehabilitation
    230: {"level": 2, "weight": 2.0, "branches": ["healthcare", "business"]},               # Health Admin
    231: {"level": 2, "weight": 2.0, "branches": ["healthcare", "science"]},                # Nutrition Science
    232: {"level": 2, "weight": 2.0, "branches": ["healthcare", "education"]},              # Public Health Crisis
    233: {"level": 2, "weight": 2.0, "branches": ["healthcare", "science"]},                # Medical Laboratory
    # Law Enforcement & Forensics
    234: {"level": 2, "weight": 2.0, "branches": ["law", "science"]},                       # Crime Response
    235: {"level": 2, "weight": 2.0, "branches": ["law"]},                                  # Criminology Spec
    236: {"level": 2, "weight": 2.0, "branches": ["law", "science"]},                       # Forensic Science
    # Engineering
    237: {"level": 2, "weight": 2.0, "branches": ["engineering", "technology"]},             # Engineering Career
    238: {"level": 2, "weight": 2.0, "branches": ["engineering"]},                          # Electrical Engineering
    239: {"level": 2, "weight": 2.0, "branches": ["engineering"]},                          # Mechanical Design
    240: {"level": 2, "weight": 2.0, "branches": ["engineering", "business"]},              # Industrial Engineering
    241: {"level": 2, "weight": 2.0, "branches": ["engineering"]},                          # Civil Engineering
    242: {"level": 2, "weight": 2.0, "branches": ["engineering", "science"]},               # Environmental Eng
    # Social Work & Community
    243: {"level": 2, "weight": 2.0, "branches": ["education", "healthcare"]},              # Social Work
    244: {"level": 2, "weight": 2.0, "branches": ["education"]},                            # Community Dev
    # HR & Business
    245: {"level": 2, "weight": 2.0, "branches": ["business"]},                             # HR Management
    246: {"level": 2, "weight": 2.0, "branches": ["business"]},                             # Business Skills
    # Digital Media & Creative
    247: {"level": 2, "weight": 2.0, "branches": ["creative", "business"]},                 # Brand Identity
    248: {"level": 2, "weight": 2.0, "branches": ["creative"]},                             # Creative Specialization
    249: {"level": 2, "weight": 2.0, "branches": ["creative", "technology"]},               # Animation Career
    250: {"level": 2, "weight": 2.0, "branches": ["creative"]},                             # Performing Arts
    251: {"level": 2, "weight": 2.0, "branches": ["creative", "engineering"]},              # Architecture Design
    # Agriculture & Environment
    252: {"level": 2, "weight": 2.0, "branches": ["science", "engineering"]},               # Agriculture
    253: {"level": 2, "weight": 2.0, "branches": ["science"]},                              # Environmental Science
    254: {"level": 2, "weight": 2.0, "branches": ["science"]},                              # Field Research
    # Cybersecurity & Cloud
    255: {"level": 2, "weight": 2.0, "branches": ["technology"]},                           # Cybersecurity Response
    256: {"level": 2, "weight": 2.0, "branches": ["technology"]},                           # Cloud Engineering
    # AI/ML & Data
    257: {"level": 2, "weight": 2.0, "branches": ["technology", "science"]},                # AI Development
    258: {"level": 2, "weight": 2.0, "branches": ["technology", "business"]},               # Data Analytics
    # Food Science
    259: {"level": 2, "weight": 2.0, "branches": ["science", "healthcare"]},                # Food Science Lab
    # Game Dev (more)
    260: {"level": 2, "weight": 2.0, "branches": ["technology"]},                           # Game Bug Fixing
    261: {"level": 2, "weight": 2.0, "branches": ["technology"]},                           # Multiplayer Game
    262: {"level": 2, "weight": 2.0, "branches": ["technology", "creative"]},               # Dream Game Project
    # Web Dev
    263: {"level": 2, "weight": 2.0, "branches": ["technology"]},                           # Web Dev Client
    264: {"level": 2, "weight": 2.0, "branches": ["technology"]},                           # Web Dev Spec
    # Mobile Dev
    265: {"level": 2, "weight": 2.0, "branches": ["technology"]},                           # Mobile App Ideas
    # Software Dev
    266: {"level": 2, "weight": 2.0, "branches": ["technology"]},                           # Software Dev Path
    # Digital Media (more)
    267: {"level": 2, "weight": 2.0, "branches": ["creative", "technology"]},               # Content Creation
    268: {"level": 2, "weight": 2.0, "branches": ["creative", "education"]},                # Digital Media Ed
    # Physical Skill & Sports
    269: {"level": 2, "weight": 2.0, "branches": ["education", "healthcare"]},              # Sports Career
    270: {"level": 2, "weight": 2.0, "branches": ["education"]},                            # Sports Event
    # Technical & Analytical
    271: {"level": 2, "weight": 2.0, "branches": ["technology", "science"]},                # Analytical Thinking
    272: {"level": 2, "weight": 2.0, "branches": ["engineering", "technology"]},            # Technical Skills
    273: {"level": 2, "weight": 2.0, "branches": ["engineering", "technology"]},            # Technical Project
    # Film & Broadcast
    274: {"level": 2, "weight": 2.0, "branches": ["creative"]},                             # Film Broadcast Career
    # Legal Practice
    275: {"level": 2, "weight": 2.0, "branches": ["law", "business"]},                      # Legal Specialization
    # Counseling
    276: {"level": 2, "weight": 2.0, "branches": ["education", "healthcare"]},              # Counseling Approach
    # Culinary
    277: {"level": 2, "weight": 2.0, "branches": ["hospitality"]},                          # Culinary Concept
    # People Skill
    278: {"level": 2, "weight": 2.0, "branches": ["education", "business"]},                # Leadership
}


# ==================== CONVERSATION CHAIN: DOMAIN ENTRY QUESTIONS ====================
# When a domain is activated (from profile or answers), these are the FIRST questions
# to ask. Ordered by how well they introduce the domain's sub-areas.
DOMAIN_ENTRY_QUESTIONS = {
    "technology":    [121, 220, 134, 135, 136, 266, 56, 37, 1, 31],
    "healthcare":    [122, 227, 141, 142, 143, 36, 60, 29, 40],
    "engineering":   [123, 237, 145, 146, 147, 59, 26, 52],
    "business":      [124, 245, 148, 149, 150, 35, 28, 57, 61],
    "creative":      [125, 248, 219, 151, 213, 152, 153, 30, 37, 33, 66],
    "education":     [126, 157, 158, 269, 28, 57, 31, 71],
    "public_service":[127, 234, 159, 160, 5, 41, 57, 35, 61],
    "science":       [128, 253, 154, 155, 156, 60, 31, 76, 33],
    "agriculture":   [129, 252, 161, 187, 51, 40, 29, 66, 37],
    "maritime":      [130, 201, 202, 162, 203, 204, 205, 51, 29, 63, 34],
    "hospitality":   [131, 223, 224, 163, 164, 51, 53, 63, 34],
    "physical":      [132, 269, 29, 66, 37, 64, 34],
    "social":        [133, 243, 28, 57, 45, 79, 80],
    "law":           [234, 235, 275, 159, 160, 127],
}

# ==================== CONVERSATION CHAIN: TRAIT FOLLOW-UP MAP ====================
# After a user picks an option with trait X, these are the best follow-up questions.
# The system picks the first unanswered one. When a chain runs out, accumulated
# branch weights determine the next domain to explore.

TRAIT_FOLLOWUP_MAP = {
    # ═══════ TECHNOLOGY ═══════
    "Software-Dev":    [266, 222, 134, 135, 97, 89, 111, 56, 70, 69, 83, 76, 108, 189],
    "Hardware-Systems": [272, 237, 187, 89, 111, 56, 70, 105, 44, 84, 76, 140],
    "Data-Analytics":  [258, 218, 135, 97, 108, 56, 76, 59, 80, 69, 91, 191],
    "Cyber-Defense":   [255, 216, 137, 111, 89, 94, 97, 99, 56, 86, 178],
    "Digital-Media":   [267, 268, 219, 221, 152, 93, 44, 98, 118, 30, 70, 78, 110, 186],
    "Technical-Skill": [272, 273, 134, 56, 76, 70, 83, 80, 105, 109],
    "Web-Dev":         [263, 264, 211, 212, 222, 134, 140, 186, 97, 89, 56, 70, 148, 163],
    "Mobile-Dev":      [265, 214, 136, 135, 140, 189, 97, 56, 191, 198],
    "Game-Dev":        [260, 261, 262, 206, 207, 208, 209, 210, 139, 221, 220, 152, 135, 198, 70, 185, 180],
    "AI-ML":           [257, 215, 138, 135, 136, 189, 198, 167, 187, 180],
    "Cloud-Systems":   [256, 217, 137, 134, 140, 135, 97, 189, 191],
    # ═══════ HEALTHCARE ═══════
    "Patient-Care":    [227, 141, 142, 107, 95, 36, 88, 81, 60, 29, 58, 103, 192],
    "Medical-Lab":     [233, 142, 60, 107, 95, 36, 108, 52, 113, 76, 156],
    "Rehab-Therapy":   [229, 143, 107, 88, 95, 103, 36, 29, 45, 113, 188],
    "Health-Admin":    [230, 143, 106, 56, 107, 95, 57, 61, 80, 188],
    "Pharmacy":        [228, 141, 142, 143, 188, 107, 95, 60, 155],
    "Public-Health":   [232, 141, 143, 188, 166, 169, 175, 198, 192],
    "Nutrition-Diet":  [231, 144, 155, 143, 188, 166, 187, 175],
    # ═══════ ENGINEERING ═══════
    "Civil-Build":     [241, 145, 147, 84, 119, 59, 52, 109, 116, 90, 26, 105, 191],
    "Mechanical-Design":[239, 146, 105, 52, 59, 119, 90, 85, 84, 116, 162],
    "Electrical-Power": [238, 146, 105, 52, 109, 114, 43, 59, 116, 187],
    "Industrial-Ops":  [240, 146, 116, 51, 92, 105, 118, 44, 53, 155],
    "Spatial-Design":  [251, 153, 59, 118, 30, 112, 110, 67, 36, 104],
    "Environmental-Eng":[242, 147, 154, 159, 189, 169, 175, 187, 191],
    # ═══════ BUSINESS ═══════
    "Finance-Acct":    [246, 149, 87, 104, 91, 100, 62, 35, 52, 61, 57, 190],
    "Marketing-Sales": [246, 148, 186, 91, 87, 104, 112, 65, 28, 62, 85, 163],
    "Startup-Venture": [246, 148, 149, 165, 87, 104, 91, 100, 85, 61, 65, 57],
    "Admin-Skill":     [245, 150, 106, 93, 87, 44, 80, 118, 57, 104, 190],
    "HR-Management":   [245, 150, 149, 160, 148, 106, 87, 190, 193],
    # ═══════ CREATIVE ═══════
    "Visual-Design":   [248, 247, 219, 152, 153, 221, 93, 44, 69, 30, 56, 78, 110, 118, 33, 186],
    "Creative-Skill":  [248, 151, 219, 152, 30, 44, 93, 69, 75, 66, 88, 98, 153],
    "Animation-3D":    [249, 213, 139, 209, 152, 221, 93, 44, 98, 135, 180, 189],
    "Film-Broadcast":  [274, 151, 219, 152, 186, 170, 93, 44, 98, 167, 164],
    "Performing-Arts": [250, 151, 164, 44, 30, 66, 93, 152, 176],
    # ═══════ EDUCATION ═══════
    "Teaching-Ed":     [157, 158, 83, 88, 45, 31, 71, 81, 86, 99, 106, 117],
    "Sports-Ed":       [269, 270, 157, 144, 166, 169, 193, 176, 183, 187],
    "Counseling":      [276, 158, 157, 160, 176, 192, 198, 187, 167],
    # ═══════ PUBLIC SERVICE ═══════
    "Law-Enforce":     [234, 235, 159, 92, 94, 96, 99, 86, 25, 43, 115, 84, 156],
    "Community-Serve": [244, 160, 159, 102, 41, 92, 94, 117, 114, 109, 74, 43, 169],
    "Forensic-Sci":    [236, 156, 159, 92, 94, 142, 108, 178, 193],
    "Legal-Practice":  [275, 159, 160, 92, 94, 96, 86, 175, 193, 190],
    "Social-Work":     [243, 160, 159, 166, 169, 175, 157, 193, 176],
    # ═══════ SCIENCE ═══════
    "Lab-Research":    [155, 154, 156, 187, 108, 60, 113, 92, 116, 76, 33, 78, 119],
    "Field-Research":  [254, 154, 161, 92, 113, 114, 108, 98, 90, 105, 119, 167],
    "Environmental-Sci":[253, 154, 159, 167, 175, 189, 187, 113, 114, 196],
    "Food-Science":    [259, 155, 164, 148, 187, 161, 108, 113],
    # ═══════ AGRICULTURE ═══════
    "Agri-Nature":     [252, 161, 129, 92, 113, 114, 119, 51, 90, 98, 53, 66, 187],
    # ═══════ MARITIME ═══════
    "Maritime-Sea":    [201, 202, 162, 203, 204, 205, 63, 51, 29, 34, 90, 85, 27, 39, 64],
    # ═══════ HOSPITALITY ═══════
    "Hospitality-Svc": [223, 225, 163, 164, 91, 112, 63, 53, 118, 85, 64, 51, 93],
    "Tourism-Travel":  [224, 226, 163, 164, 152, 170, 176, 193, 199],
    "Culinary-Arts":   [277, 164, 163, 148, 155, 170, 176, 199],
    # ═══════ OTHER ═══════
    "People-Skill":    [278, 150, 157, 83, 45, 79, 88, 94, 28, 117, 80],
    "Physical-Skill":  [269, 132, 29, 66, 90, 103, 37, 25, 64, 34, 192],
    "Analytical-Skill":[271, 194, 195, 172, 108, 80, 76, 56, 97],
}

# ==================== INTEREST KEYWORD → DOMAIN ====================
INTEREST_DOMAIN_MAP = {
    "computer": "technology", "programming": "technology", "coding": "technology",
    "software": "technology", "web_development": "technology", "game_dev": "technology",
    "ai": "technology", "data": "technology", "cybersecurity": "technology",
    "robotics": "technology", "it": "technology", "tech": "technology",
    "programming_skill": "technology", "data_analysis": "technology",
    "electronics": "technology", "web_design": "technology", "mobile_app": "technology",
    "machine_learning": "technology", "artificial_intelligence": "technology",
    "cloud_computing": "technology", "database": "technology", "networking": "technology",
    "game_development": "technology", "hacking": "technology", "app_development": "technology",
    "web_tech": "technology", "multimedia": "technology", "software_eng": "technology",
    "networking_skill": "technology", "database_skill": "technology", "mobile_dev": "technology",
    "ux_ui": "technology", "health_info": "technology",
    "medical": "healthcare", "nursing": "healthcare", "pharmacy": "healthcare",
    "physical_therapy": "healthcare", "nutrition": "healthcare", "psychology": "healthcare",
    "medical_tech": "healthcare", "dentistry": "healthcare", "health": "healthcare",
    "first_aid": "healthcare", "counseling": "healthcare", "dietetics": "healthcare",
    "mental_health": "healthcare", "public_health": "healthcare", "midwifery": "healthcare",
    "radiologic": "healthcare", "occupational_therapy": "healthcare",
    "speech_therapy": "healthcare", "respiratory": "healthcare", "radiology": "healthcare",
    "optometry": "healthcare", "patient_care": "healthcare", "elderly_care": "healthcare",
    "lab_equipment": "healthcare",
    "engineering": "engineering", "mechanical": "engineering", "electrical": "engineering",
    "civil": "engineering", "architecture": "engineering", "industrial": "engineering",
    "drafting": "engineering", "repair_maintenance": "engineering",
    "geodetic": "engineering", "surveying": "engineering", "environmental_engineering": "engineering",
    "aeronautical": "engineering", "landscape": "engineering", "industrial_design": "engineering",
    "aircraft_maint": "engineering", "marine_eng": "maritime",
    "machine_operation": "engineering", "quality_control": "engineering",
    "business": "business", "finance": "business", "marketing": "business",
    "accounting": "business", "economics": "business", "management": "business",
    "real_estate": "business", "entrepreneurship": "business",
    "negotiation": "business", "project_management": "business",
    "human_resources": "business", "banking": "business", "investing": "business",
    "advertising": "business", "sales": "business", "startup": "business",
    "human_resource": "business", "operations": "business", "customs": "business",
    "agribusiness": "business", "office_admin": "business",
    "accounting_skill": "business", "budgeting": "business", "financial_analysis": "business",
    "strategic_thinking": "business", "delegation": "business",
    "event_management": "business",
    "art": "creative", "music": "creative", "film": "creative", "writing": "creative",
    "photography": "creative", "animation": "creative", "fashion": "creative",
    "graphic_design": "creative", "design": "creative", "creativity": "creative",
    "artistic": "creative", "music_skill": "creative", "storytelling": "creative",
    "design_thinking": "creative", "photography_skill": "creative", "video_editing": "creative",
    "filmmaking": "creative", "theater": "creative", "performing_arts": "creative",
    "dance": "creative", "interior_design": "creative", "game_art": "creative",
    "3d_modeling": "creative", "painting": "creative", "drawing": "creative",
    "advertising_arts": "creative", "music_production": "creative", "fine_arts": "creative",
    "clothing_tech": "creative", "audio_production": "creative", "film_editing": "creative",
    "education": "education", "teaching": "education", "mentoring": "education",
    "public_speaking": "education", "presentation": "education",
    "tutoring": "education", "coaching": "education", "special_education": "education",
    "library_science": "education", "curriculum": "education",
    "early_childhood": "education", "child_interaction": "education",
    "sign_language": "education",
    "law": "public_service", "politics": "public_service", "criminology": "public_service",
    "social": "public_service", "communication": "public_service",
    "philosophy": "public_service", "history": "public_service",
    "conflict_resolution": "public_service", "forensics": "public_service",
    "social_work": "public_service", "human_rights": "public_service",
    "diplomacy": "public_service", "public_policy": "public_service",
    "public_admin": "public_service", "intl_studies": "public_service",
    "sociology": "public_service", "linguistics": "public_service",
    "dev_communication": "public_service", "community_dev": "public_service",
    "legal_mgmt": "public_service", "case_analysis": "public_service",
    "policy_analysis": "public_service",
    "science": "science", "biology": "science", "chemistry": "science",
    "physics": "science", "environment": "science", "earth_science": "science",
    "laboratory": "science", "research": "science",
    "food_science": "science", "forensic_science": "science",
    "environmental_science": "science", "marine_biology": "science",
    "marine_science": "science", "biotechnology": "science", "meteorology": "science",
    "statistics": "science", "env_planning": "science", "statistical_analysis": "science",
    "scientific_method": "science", "env_assessment": "science",
    "agriculture": "agriculture", "veterinary": "agriculture", "gardening": "agriculture",
    "farming": "agriculture", "fishery": "agriculture", "forestry": "agriculture",
    "aquaculture": "agriculture", "livestock": "agriculture",
    "fisheries": "agriculture", "agribusiness": "agriculture",
    "maritime": "maritime", "aviation": "maritime", "logistics": "maritime",
    "shipping": "maritime", "navigation": "maritime", "seafaring": "maritime",
    "marine_transport": "maritime", "seaman": "maritime", "flight_ops": "maritime",
    "tourism": "hospitality", "food": "hospitality", "cooking": "hospitality",
    "customer_service": "hospitality", "hotel": "hospitality", "culinary": "hospitality",
    "baking": "hospitality", "travel": "hospitality", "events": "hospitality",
    "restaurant": "hospitality", "resort": "hospitality",
    "hotel_mgmt": "hospitality", "culinary_mgmt": "hospitality",
    "tvet": "hospitality", "food_safety": "hospitality",
    "sports": "physical", "sports_fitness": "physical", "military": "physical",
    "driving": "physical", "fitness": "physical", "athletics": "physical",
    "gym": "physical", "exercise": "physical", "martial_arts": "physical",
    "exercise_science": "physical", "swimming": "physical",
    "heavy_equipment": "physical", "carpentry": "physical", "plumbing": "physical",
    "welding": "physical", "auto_repair": "physical",
    "leadership": "business", "teamwork": "public_service",
    "critical_thinking": "science", "problem_solving": "technology",
    "time_management": "business", "organization": "business",
    "communication_skill": "public_service", "adaptability": "business",
    "empathy": "healthcare", "patience": "education",
    "attention_to_detail": "science", "multitasking": "business",
}

# Maps SHS strand to default domain
STRAND_DOMAIN_MAP = {
    "STEM": "technology", "ABM": "business", "HUMSS": "education",
    "TVL": "technology", "GAS": None, "SPORTS": "physical", "ARTS": "creative",
}

# Minimum questions to ask in a domain before moving on
DOMAIN_MIN_QUESTIONS = 3


class AdaptiveAssessmentEngine:
    """
    Selects questions adaptively based on previous answers.
    Prioritizes questions that best discriminate between remaining course candidates.
    """
    
    # Configuration
    MAX_QUESTIONS = 25  # Maximum questions to ask
    MIN_QUESTIONS = 10  # Minimum before allowing early stop
    CONFIDENCE_THRESHOLD = 0.85  # Stop when top courses are clearly ahead (raised to prevent premature stops)
    TOP_N_RECOMMENDATIONS = 6  # Number of courses to recommend
    
    def __init__(self, courses: List[dict], questions: List[dict]):
        """Initialize with course and question data."""
        self.courses = {c['course_name']: c for c in courses}
        self.questions = {q['question_id']: q for q in questions}
        self.sessions: Dict[str, AdaptiveSession] = {}
        
        # Build lookup tables
        self.trait_to_courses: Dict[str, Set[str]] = defaultdict(set)
        self.course_traits: Dict[str, Set[str]] = {}
        
        for course_name, course in self.courses.items():
            traits = self._parse_traits(course.get('trait_tag', ''))
            self.course_traits[course_name] = traits
            for trait in traits:
                self.trait_to_courses[trait].add(course_name)
        
        # Pre-compute trait -> questions mapping
        self.trait_to_questions: Dict[str, List[int]] = defaultdict(list)
        for qid, question in self.questions.items():
            for opt in question.get('options', []):
                trait_tags = opt.get('trait_tags', {})
                if isinstance(trait_tags, dict):
                    for trait in trait_tags:
                        self.trait_to_questions[trait].append(qid)
                elif isinstance(trait_tags, list):
                    for trait in trait_tags:
                        self.trait_to_questions[trait].append(qid)
                else:
                    trait = opt.get('trait_tag')
                    if trait:
                        self.trait_to_questions[trait].append(qid)
        
        # Pre-compute question-trait affinity matrix for decision tree
        # affinity[qid] = {trait: max_weight_across_options}
        self.question_trait_affinity: Dict[int, Dict[str, float]] = {}
        for qid, question in self.questions.items():
            affinities = {}
            options = question.get('options', [])
            for opt in options:
                trait_tags = opt.get('trait_tags', {})
                if isinstance(trait_tags, dict):
                    for trait, weight in trait_tags.items():
                        affinities[trait] = affinities.get(trait, 0) + weight
                elif isinstance(trait_tags, list):
                    for trait in trait_tags:
                        affinities[trait] = affinities.get(trait, 0) + 1
                else:
                    trait = opt.get('trait_tag')
                    if trait:
                        affinities[trait] = affinities.get(trait, 0) + 1
            total = len(options)
            if total > 0:
                for trait in affinities:
                    affinities[trait] /= total  # Normalize
            self.question_trait_affinity[qid] = affinities
        
        # Pre-compute question-branch affinity
        # branch_affinity[qid] = {branch: max_trait_affinity_in_that_branch}
        self.question_branch_affinity: Dict[int, Dict[str, float]] = {}
        for qid, affinities in self.question_trait_affinity.items():
            branch_scores = {}
            for trait, score in affinities.items():
                branch = TRAIT_TO_BRANCH.get(trait, "")
                if branch:
                    branch_scores[branch] = max(branch_scores.get(branch, 0), score)
            self.question_branch_affinity[qid] = branch_scores
        
        print(f"[ENGINE] Adaptive Engine initialized with {len(self.courses)} courses and {len(self.questions)} questions")
        print(f"[ENGINE] Pre-computed trait affinity for {len(self.question_trait_affinity)} questions")
        print(f"[ENGINE] Decision tree nodes classified: {len(QUESTION_TREE_NODES)} questions")
    
    def _parse_traits(self, trait_tag) -> Set[str]:
        """Parse trait_tag field into set of traits"""
        if not trait_tag:
            return set()
        if isinstance(trait_tag, list):
            return set(trait_tag)
        return set(t.strip() for t in str(trait_tag).split(',') if t.strip())
    
    def _calculate_profile_bonus(self, interests: str, skills: str, course_traits: Set[str]) -> float:
        """Calculate bonus points (0-20) for courses matching user's profile interests/skills.
        
        Scoring strategy:
        - Count each UNIQUE course trait only once (prevents generic traits like Creative-Skill
          from being counted multiple times across different profile selections)
        - Weight specific/path traits higher (e.g. Visual-Design, Digital-Media = 4pts)
          vs generic skill traits (e.g. Creative-Skill = 2pts)
        - Award a breadth bonus when a high fraction of the course's traits are matched
        """
        if not interests and not skills:
            return 0.0
        
        PROFILE_TO_TRAITS = UNIFIED_PROFILE_TO_TRAITS
        
        # Parse user's selections
        interest_list = [i.strip().lower() for i in (interests or "").split(",") if i.strip()]
        skill_list = [s.strip().lower() for s in (skills or "").split(",") if s.strip()]
        user_selections = set(interest_list + skill_list)
        
        # Collect ALL unique traits the user's profile maps to
        user_profile_traits: Set[str] = set()
        for selection in user_selections:
            related_traits = PROFILE_TO_TRAITS.get(selection, [])
            for trait in related_traits:
                user_profile_traits.add(trait.lower())
        
        if not user_profile_traits:
            return 0.0
        
        # Normalize course traits for matching
        course_traits_lower = {t.lower() for t in course_traits}
        
        # Generic/broad traits get lower weight; specific path traits get higher weight
        GENERIC_TRAITS = {"creative-skill", "technical-skill", "people-skill",
                          "analytical-skill", "physical-skill", "admin-skill",
                          "artistic", "realistic", "investigative", "social",
                          "enterprising", "conventional"}
        
        # Find unique course traits that match the user's profile traits
        bonus = 0.0
        matched_course_traits = set()
        
        for course_trait in course_traits_lower:
            for user_trait in user_profile_traits:
                if user_trait == course_trait or user_trait in course_trait or course_trait in user_trait:
                    matched_course_traits.add(course_trait)
                    # Specific path traits score higher than generic ones
                    if course_trait in GENERIC_TRAITS:
                        bonus += 2.0
                    else:
                        bonus += 4.0
                    break  # Don't double-count this course trait
        
        # Breadth bonus: reward courses where MOST of their traits match the profile
        if len(course_traits_lower) > 0:
            match_ratio = len(matched_course_traits) / len(course_traits_lower)
            if match_ratio >= 0.8:
                bonus += 4.0  # Almost all course traits match the profile
            elif match_ratio >= 0.6:
                bonus += 2.0  # Majority of course traits match
        
        # Cap bonus at 20 points
        return min(bonus, 20.0)
    
    def _determine_rejected_topic(self, question: dict, chosen_option: dict) -> Optional[str]:
        """Figure out which topic the user rejected when they selected 'none'."""
        option_text = chosen_option.get('option_text', '').lower()
        question_text = question.get('question_text', '').lower()
        question_category = question.get('category', '').lower()
        
        # Keyword to topic mapping - expanded for better detection
        REJECTION_KEYWORDS = {
            # Healthcare
            "healthcare": "Patient-Care",
            "nursing": "Patient-Care",
            "nurse": "Patient-Care",
            "patient": "Patient-Care",
            "hospital": "Patient-Care",
            "medical": "Medical-Lab",
            "medicine": "Medical-Lab",
            "laboratory": "Medical-Lab",
            "therapy": "Rehab-Therapy",
            "rehabilitation": "Rehab-Therapy",
            
            # Technology
            "technology": "Software-Dev",
            "programming": "Software-Dev",
            "coding": "Software-Dev",
            "software": "Software-Dev",
            "computer": "Software-Dev",
            "tech": "Software-Dev",
            "it career": "Software-Dev",
            
            # Engineering
            "engineering": "Civil-Build",
            "construction": "Civil-Build",
            "building": "Civil-Build",
            "architect": "Spatial-Design",
            
            # Business
            "business": "Finance-Acct",
            "accounting": "Finance-Acct",
            "finance": "Finance-Acct",
            "accountant": "Finance-Acct",
            "banking": "Finance-Acct",
            "entrepreneur": "Startup-Venture",
            "marketing": "Marketing-Sales",
            
            # Education
            "teaching": "Teaching-Ed",
            "education": "Teaching-Ed",
            "teach": "Teaching-Ed",
            "teacher": "Teaching-Ed",
            "instructor": "Teaching-Ed",
            "professor": "Teaching-Ed",
            "classroom": "Teaching-Ed",
            
            # Arts & Creative
            "creative": "Visual-Design",
            "arts": "Visual-Design",
            "art": "Visual-Design",
            "design": "Visual-Design",
            "artist": "Visual-Design",
            "music": "Creative-Skill",
            "film": "Digital-Media",
            "animation": "Digital-Media",
            
            # Maritime
            "maritime": "Maritime-Sea",
            "sea": "Maritime-Sea",
            "ship": "Maritime-Sea",
            "ocean": "Maritime-Sea",
            "sailor": "Maritime-Sea",
            "captain": "Maritime-Sea",
            "navigation": "Maritime-Sea",
            
            # Agriculture
            "agriculture": "Agri-Nature",
            "farming": "Agri-Nature",
            "farm": "Agri-Nature",
            "crops": "Agri-Nature",
            "plants": "Agri-Nature",
            "environmental": "Field-Research",
            
            # Hospitality
            "hospitality": "Hospitality-Svc",
            "hotel": "Hospitality-Svc",
            "tourism": "Hospitality-Svc",
            "travel": "Hospitality-Svc",
            "culinary": "Hospitality-Svc",
            "chef": "Hospitality-Svc",
            "cooking": "Hospitality-Svc",
            
            # Law & Security
            "law": "Law-Enforce",
            "police": "Law-Enforce",
            "criminology": "Law-Enforce",
            "criminal": "Law-Enforce",
            "security": "Law-Enforce",
            "detective": "Law-Enforce",
            
            # Public Service
            "government": "Community-Serve",
            "public": "Community-Serve",
            "social work": "Community-Serve",
            "politics": "Community-Serve",
        }
        
        # Check for direct keyword matches in the rejection text
        for keyword, topic in REJECTION_KEYWORDS.items():
            if keyword in option_text:
                return topic
        
        # Also check the question text for context
        for keyword, topic in REJECTION_KEYWORDS.items():
            if keyword in question_text:
                return topic
        
        # If no direct match, analyze the question's other options
        # The rejected topic is likely what most other options are about
        
        # Category-based rejection
        CATEGORY_TO_TOPIC = {
            "healthcare": "Patient-Care",
            "nursing": "Patient-Care",
            "medical": "Medical-Lab",
            "technology": "Software-Dev",
            "tech": "Software-Dev",
            "programming": "Software-Dev",
            "engineering": "Civil-Build",
            "business": "Finance-Acct",
            "finance": "Finance-Acct",
            "accounting": "Finance-Acct",
            "education": "Teaching-Ed",
            "teaching": "Teaching-Ed",
            "creative": "Visual-Design",
            "arts": "Visual-Design",
            "maritime": "Maritime-Sea",
            "agriculture": "Agri-Nature",
            "hospitality": "Hospitality-Svc",
            "public service": "Community-Serve",
            "law": "Law-Enforce",
            "criminology": "Law-Enforce",
        }
        
        for category_keyword, topic in CATEGORY_TO_TOPIC.items():
            if category_keyword in question_category:
                return topic
        
        # Count traits from other options to determine majority topic
        trait_counts: Dict[str, int] = {}
        for opt in question.get('options', []):
            if opt.get('option_id') != chosen_option.get('option_id'):
                trait_tags = opt.get('trait_tags', {})
                if isinstance(trait_tags, dict):
                    # Use the highest-weighted trait as primary
                    if trait_tags:
                        primary_trait = max(trait_tags, key=trait_tags.get)
                        trait_counts[primary_trait] = trait_counts.get(primary_trait, 0) + 1
                elif isinstance(trait_tags, list):
                    for trait in trait_tags:
                        trait_counts[trait] = trait_counts.get(trait, 0) + 1
                else:
                    trait = opt.get('trait_tag')
                    if trait:
                        trait_counts[trait] = trait_counts.get(trait, 0) + 1
        
        # Return the most common trait from other options (what user rejected)
        if trait_counts:
            most_common = max(trait_counts.items(), key=lambda x: x[1])
            if most_common[1] >= 2:  # At least 2 options had this trait
                return most_common[0]
        
        return None
    
    def _get_profile_priority_traits(self, session: AdaptiveSession) -> Set[str]:
        """Get traits that should be prioritized based on user's profile interests/skills.
        
        When user selects many interests/skills, we prioritize traits that appear
        most frequently across their selections (shows stronger preference).
        We limit to top 6 traits to ensure focused early questions.
        """
        if not session.user_interests and not session.user_skills:
            return set()
        
        PROFILE_TO_TRAITS = UNIFIED_PROFILE_TO_TRAITS
        
        # Count how often each trait appears across all selected interests/skills
        trait_counts = {}
        
        # Parse interests
        if session.user_interests:
            for interest in session.user_interests.split(','):
                interest = interest.strip().lower()
                traits = PROFILE_TO_TRAITS.get(interest, [])
                for trait in traits:
                    trait_counts[trait] = trait_counts.get(trait, 0) + 1
        
        # Parse skills
        if session.user_skills:
            for skill in session.user_skills.split(','):
                skill = skill.strip().lower()
                traits = PROFILE_TO_TRAITS.get(skill, [])
                for trait in traits:
                    trait_counts[trait] = trait_counts.get(trait, 0) + 1
        
        if not trait_counts:
            return set()
        
        # Sort traits by frequency (most common first) and take top 6
        # This ensures early questions focus on the user's STRONGEST interests
        sorted_traits = sorted(trait_counts.items(), key=lambda x: x[1], reverse=True)
        top_traits = [trait for trait, count in sorted_traits[:6]]
        
        print(f"[STATS] User profile traits (top 6 of {len(trait_counts)}): {top_traits}")
        
        return set(top_traits)
    
    def _get_strand_priority_traits(self, strand: str) -> Set[str]:
        """Get traits prioritized by user's SHS strand."""
        return set(STRAND_PRIORITY_TRAITS.get(strand, []))

    def _get_profile_priority_traits_ranked(self, interests: str, skills: str, strand: str) -> List[str]:
        """
        Build a RANKED list of traits from user profile (interests + skills + strand).
        The first trait is the user's STRONGEST stated interest.
        Used to seed the first questions of the assessment.
        """
        PROFILE_TO_TRAITS = UNIFIED_PROFILE_TO_TRAITS

        # Count trait frequency across all profile inputs (interests come first = higher weight)
        trait_counts: Dict[str, float] = {}

        # Interests get weight 2.0 (these are what the user explicitly stated)
        if interests:
            for interest in interests.split(','):
                interest = interest.strip().lower()
                traits = PROFILE_TO_TRAITS.get(interest, [])
                for i, trait in enumerate(traits):
                    # First trait in list is most relevant
                    trait_counts[trait] = trait_counts.get(trait, 0) + (2.0 - i * 0.3)

        # Skills get weight 1.5
        if skills:
            for skill in skills.split(','):
                skill = skill.strip().lower()
                traits = PROFILE_TO_TRAITS.get(skill, [])
                for i, trait in enumerate(traits):
                    trait_counts[trait] = trait_counts.get(trait, 0) + (1.5 - i * 0.2)

        # Strand traits get weight 1.0 (background context)
        strand_traits = STRAND_PRIORITY_TRAITS.get(strand, [])
        for i, trait in enumerate(strand_traits):
            trait_counts[trait] = trait_counts.get(trait, 0) + max(1.0 - i * 0.1, 0.2)

        # Sort by score descending, return ranked list
        sorted_traits = sorted(trait_counts.items(), key=lambda x: x[1], reverse=True)
        ranked = [trait for trait, score in sorted_traits]

        print(f"[PROFILE-SEED] Ranked profile traits: {ranked[:10]}")
        return ranked

    def _get_current_topic_and_adjacent(self, session: AdaptiveSession) -> Tuple[str, Set[str]]:
        """
        Determine the user's current topic thread from their recent answers
        and return (current_topic, set_of_adjacent_topics).
        
        Looks at the last 5 traits the user chose. The most frequent trait
        among those is the "current thread".
        """
        if not session.recent_traits:
            return ("", set())

        # Count recent traits (last 5)
        window = session.recent_traits[-5:]
        counts: Dict[str, int] = {}
        for t in window:
            counts[t] = counts.get(t, 0) + 1

        # Most frequent recent trait = current topic
        current_topic = max(counts, key=counts.get)
        adjacent = set(TOPIC_ADJACENCY.get(current_topic, []))

        return current_topic, adjacent

    def _get_dominant_traits(self, session: AdaptiveSession, top_n: int = 5) -> Set[str]:
        """
        Return the user's dominant traits — the top N traits by accumulated score.
        These represent the user's CONSISTENT pattern across multiple questions,
        not just a single answer.
        """
        if not session.trait_scores:
            return set(session.profile_seed_traits[:top_n])
        
        sorted_traits = sorted(
            session.trait_scores.items(),
            key=lambda x: x[1],
            reverse=True
        )
        dominant = {t for t, s in sorted_traits[:top_n]}
        # Always include top profile seeds as dominant context
        dominant.update(session.profile_seed_traits[:3])
        return dominant

    def _is_dominant_trait(self, trait: str, session: AdaptiveSession) -> bool:
        """
        Check if a trait is part of the user's dominant pattern.
        A trait is dominant ONLY if it is directly in the top 5 accumulated
        traits by score OR among the top 3 profile seed traits.
        
        NO adjacency expansion — this prevents cross-cluster leakage
        (e.g., Digital-Media being adjacent to Software-Dev should NOT
        make Software-Dev count as dominant for an art-focused user).
        """
        dominant = self._get_dominant_traits(session)
        return trait in dominant

    def _has_dominant_trait_overlap(self, question: dict, session: AdaptiveSession) -> bool:
        """
        Check if a question has at least one option with a trait from the user's
        DOMINANT pattern (top accumulated traits + profile seeds).
        
        This is STRICTER than _has_trait_continuity — it requires overlap with
        the user's strongest traits, not just any trait ever encountered.
        Used to prevent a single minority answer from hijacking the question chain.
        
        NO adjacency expansion — prevents cross-cluster leakage where
        Digital-Media (dominant for art user) would expand to include Software-Dev.
        """
        dominant = self._get_dominant_traits(session)
        if not dominant:
            return True  # No dominant traits yet — allow anything
        
        options = question.get('options', [])
        for opt in options:
            trait_tags = opt.get('trait_tags', {})
            if isinstance(trait_tags, dict):
                for trait in trait_tags:
                    if trait in dominant:
                        return True
            elif isinstance(trait_tags, list):
                for trait in trait_tags:
                    if trait in dominant:
                        return True
            else:
                trait = opt.get('trait_tag')
                if trait and trait in dominant:
                    return True
        return False

    def _has_trait_continuity(self, question: dict, session: AdaptiveSession) -> bool:
        """
        Check if a question has at least one option that shares a trait with
        the user's accumulated trait scores OR profile seed traits.
        
        This ensures every question is connected to what the user has already
        expressed interest in, making the assessment feel like a coherent
        conversation rather than random questions.
        """
        # Build the set of active traits: accumulated from answers + profile seeds
        active_traits = set(session.trait_scores.keys())
        active_traits.update(session.profile_seed_traits)
        
        # Also include adjacent/related traits for flexibility
        expanded_active = set(active_traits)
        for trait in active_traits:
            adjacents = TOPIC_ADJACENCY.get(trait, [])
            expanded_active.update(adjacents)
        
        if not expanded_active:
            return True  # No traits yet (first question) — allow anything
        
        options = question.get('options', [])
        for opt in options:
            trait_tags = opt.get('trait_tags', {})
            if isinstance(trait_tags, dict):
                for trait in trait_tags:
                    if trait in expanded_active:
                        return True
            elif isinstance(trait_tags, list):
                for trait in trait_tags:
                    if trait in expanded_active:
                        return True
            else:
                trait = opt.get('trait_tag')
                if trait and trait in expanded_active:
                    return True
        return False

    def _question_profile_relevance_score(self, question: dict, session: AdaptiveSession) -> float:
        """
        Score how relevant a question is to the user's DOMINANT traits.
        Returns a 0-1 score: higher means more options share traits with the user's
        dominant pattern (not just any trait ever encountered).
        
        Used to rank questions so the most pattern-relevant ones are picked first.
        """
        dominant = self._get_dominant_traits(session)
        if not dominant:
            return 0.5  # No profile context yet
        
        options = question.get('options', [])
        if not options:
            return 0.0
        
        matching_options = 0
        total_match_weight = 0.0
        
        for opt in options:
            trait_tags = opt.get('trait_tags', {})
            if isinstance(trait_tags, dict):
                for trait, weight in trait_tags.items():
                    if trait in dominant:
                        matching_options += 1
                        total_match_weight += weight
                        break  # Count each option once
            elif isinstance(trait_tags, list):
                for trait in trait_tags:
                    if trait in dominant:
                        matching_options += 1
                        total_match_weight += 1.0
                        break
            else:
                trait = opt.get('trait_tag')
                if trait and trait in dominant:
                    matching_options += 1
                    total_match_weight += 1.0
        
        # Score: ratio of matching options + weight bonus
        option_ratio = matching_options / len(options)
        weight_bonus = min(total_match_weight / len(options), 1.0)
        return (option_ratio + weight_bonus) / 2.0

    def create_session(self, user_id: int, user_gwa: float = None, user_strand: str = None, max_questions: int = 30, user_interests: str = None, user_skills: str = None) -> str:
        """Start a new assessment session. Returns session_id."""
        import uuid
        session_id = str(uuid.uuid4())[:8]
        
        # Normalize strand
        normalized_strand = user_strand.upper() if user_strand else "GAS"
        if normalized_strand not in STRAND_PRIORITY_TRAITS:
            normalized_strand = "GAS"
        
        # Calculate min questions (50% of max)
        min_questions = int(max_questions * 0.5)
        
        # Initialize all courses with base score
        course_scores = {name: 50.0 for name in self.courses}
        
        # Apply initial GWA/Strand bonuses (not exclusions!)
        for course_name, course in self.courses.items():
            # GWA bonus (preference, not requirement)
            if user_gwa and course.get('minimum_gwa'):
                if user_gwa >= course['minimum_gwa']:
                    course_scores[course_name] += 5  # Bonus for meeting GWA
                elif user_gwa >= course['minimum_gwa'] - 5:
                    course_scores[course_name] += 2  # Small bonus for close
            
            # Strand bonus (preference, not requirement)
            if user_strand and course.get('required_strand'):
                if user_strand.upper() == course['required_strand'].upper():
                    course_scores[course_name] += 5  # Bonus for matching strand
            
            # Add profile bonus from interests/skills
            if user_interests or user_skills:
                course_traits = self.course_traits.get(course_name, set())
                profile_bonus = self._calculate_profile_bonus(user_interests, user_skills, course_traits)
                course_scores[course_name] += profile_bonus
        
        # Build initial branch weights from user profile
        profile_ranked = list(self._get_profile_priority_traits_ranked(user_interests, user_skills, normalized_strand))
        initial_branch_weights = {}
        for i, trait in enumerate(profile_ranked):
            branch = TRAIT_TO_BRANCH.get(trait, "")
            if branch:
                # Earlier traits in the ranked list get higher weight
                weight = max(3.0 - i * 0.2, 0.5)
                initial_branch_weights[branch] = initial_branch_weights.get(branch, 0) + weight
        
        # Ensure all branches have at least a minimal weight (exploration potential)
        for branch in BRANCH_ADJACENCY.keys():
            if branch not in initial_branch_weights:
                initial_branch_weights[branch] = 0.1
        
        print(f"[TREE] Initial branch weights from profile: { {k: round(v, 1) for k, v in sorted(initial_branch_weights.items(), key=lambda x: x[1], reverse=True)[:6]} }")
        
        session = AdaptiveSession(
            session_id=session_id,
            user_id=user_id,
            user_gwa=user_gwa,
            user_strand=normalized_strand,
            user_interests=user_interests,
            user_skills=user_skills,
            max_questions=max_questions,
            min_questions=min_questions,
            course_scores=course_scores,
            initial_course_scores=course_scores.copy(),
            active_courses=set(self.courses.keys()),
            profile_seed_traits=profile_ranked,
            branch_weights=initial_branch_weights,
        )
        
        # ─── CONVERSATION CHAIN: Determine primary domain from profile ───
        # Count how many interest/skill keywords map to each domain
        domain_votes: Dict[str, int] = {}
        all_keywords = []
        if user_interests:
            all_keywords.extend([kw.strip().lower().replace(" ", "_") for kw in user_interests.split(",")])
        if user_skills:
            all_keywords.extend([kw.strip().lower().replace(" ", "_") for kw in user_skills.split(",")])
        
        for kw in all_keywords:
            domain = INTEREST_DOMAIN_MAP.get(kw)
            if domain:
                domain_votes[domain] = domain_votes.get(domain, 0) + 1
        
        # Primary domain: most voted, with strand as tiebreaker
        strand_domain = STRAND_DOMAIN_MAP.get(normalized_strand)
        if domain_votes:
            # Sort by vote count descending
            sorted_domains = sorted(domain_votes.items(), key=lambda x: x[1], reverse=True)
            primary = sorted_domains[0][0]
        elif strand_domain:
            primary = strand_domain
        else:
            # No interests, no strand info → use strongest branch weight
            primary = max(initial_branch_weights, key=initial_branch_weights.get) if initial_branch_weights else "technology"
        
        session.primary_domain = primary
        
        # Build domain exploration queue: ONLY profile-relevant domains
        # (primary → adjacent → voted → strand-related). Never add unrelated domains.
        domain_queue = [primary]
        relevant_domains = {primary}
        # Add adjacent domains of primary
        for adj in BRANCH_ADJACENCY.get(primary, []):
            if adj not in domain_queue:
                domain_queue.append(adj)
            relevant_domains.add(adj)
        # Add other voted domains (from interests/skills)
        for dom, _ in sorted(domain_votes.items(), key=lambda x: x[1], reverse=True):
            if dom not in domain_queue:
                domain_queue.append(dom)
            relevant_domains.add(dom)
            # Also add adjacents of voted domains
            for adj in BRANCH_ADJACENCY.get(dom, []):
                relevant_domains.add(adj)
        # Add strand domain if not yet included
        if strand_domain and strand_domain not in domain_queue:
            domain_queue.append(strand_domain)
            relevant_domains.add(strand_domain)
            for adj in BRANCH_ADJACENCY.get(strand_domain, []):
                relevant_domains.add(adj)
        # DO NOT add remaining unrelated domains — keep questions focused on profile
        
        session.domain_queue = domain_queue
        session.relevant_domains = relevant_domains
        
        # Preload the first chain: entry questions for primary domain
        entry_qs = DOMAIN_ENTRY_QUESTIONS.get(primary, [])
        session.chain_queue = list(entry_qs)
        session.domain_question_count = {primary: 0}
        
        print(f"[CHAIN] Primary domain: {primary} (votes: {domain_votes})")
        print(f"[CHAIN] Relevant domains: {sorted(relevant_domains)}")
        print(f"[CHAIN] Domain queue: {domain_queue[:6]}")
        print(f"[CHAIN] Initial chain: {session.chain_queue[:5]}")
        
        self.sessions[session_id] = session
        print(f"[SESSION] Created adaptive session {session_id} for user {user_id} (strand: {normalized_strand}, questions: {max_questions}, interests: {bool(user_interests)}, skills: {bool(user_skills)})")
        return session_id
    
    def get_next_question(self, session_id: str) -> Optional[dict]:
        """
        ANSWER-DRIVEN CONVERSATION CHAIN ALGORITHM
        
        Questions are NOT randomly scored. Instead, the system follows a conversation
        chain directly connected to the user's profile and answers:
        
        1. PROFILE ENTRY (Rounds 1-3):
           User profile (strand + interests + skills) → primary domain
           → ask domain entry questions to discover sub-interests
           
        2. ANSWER-DRIVEN FOLLOW-UP (Rounds 4+):
           User picks option with trait X → TRAIT_FOLLOWUP_MAP[X] → next question
           explores DEEPER into that specific area
           
        3. DOMAIN TRANSITION:
           When current domain's chain is exhausted (or min questions met),
           move to next domain in queue (adjacent → related → rest)
           
        4. FALLBACK SCORING:
           If all chains exhausted, use information-gain scoring for remaining questions
        
        Example flow for TVL student interested in computers:
          Q1: "What do you want to master?" → picks "programming/coding" (Software-Dev)
          Q2: "Mobile app features?" → picks "data analytics" (Data-Analytics)  
          Q3: "Group research role?" → picks "analyze data" (Data-Analytics)
          Q4: "Rate your tech skills" → picks "spreadsheets" (Data-Analytics)
          → System narrows toward data science / IT courses
        """
        session = self.sessions.get(session_id)
        if not session or session.is_complete:
            return None
        
        if self._should_stop(session):
            self._finalize_session(session)
            return None
        
        asked = session.excluded_question_ids
        round_num = session.round_number + 1
        
        # ═══════════════════════════════════════════════════════════════════
        # PHASE 1: Try to get the next question from the current chain
        # All follow-ups must belong to profile-relevant branches.
        # ═══════════════════════════════════════════════════════════════════
        
        selected_qid = None
        selection_reason = ""
        relevant = session.relevant_domains
        
        def _is_relevant_question(qid):
            """Check if a question belongs to at least one profile-relevant branch."""
            node = QUESTION_TREE_NODES.get(qid)
            if not node:
                return True  # Questions without node classification are broad/general — allow
            return bool(set(node["branches"]) & relevant)
        
        def _passes_trait_continuity(qid):
            """Check if question has trait overlap with user's accumulated/profile traits."""
            q = self.questions.get(qid)
            if not q:
                return False
            return self._has_trait_continuity(q, session)
        
        # --- Step 1A: If we have a last_answer_trait, build a follow-up chain from it ---
        # GUARD: Only follow the last answer's chain if the trait is part of the
        # user's dominant pattern. This prevents a single "off-topic" answer
        # (e.g., rating math as excellent when the user is art-focused) from
        # hijacking the entire question chain away from the user's core interests.
        if session.last_answer_trait and session.last_answer_trait in TRAIT_FOLLOWUP_MAP:
            trait_is_dominant = self._is_dominant_trait(session.last_answer_trait, session)
            # In early rounds (< 5 answers), allow any trait to drive chain (still discovering)
            allow_chain = trait_is_dominant or len(session.answered_questions) < 5
            
            if allow_chain:
                followups = TRAIT_FOLLOWUP_MAP[session.last_answer_trait]
                for fq in followups:
                    if fq not in asked and fq in self.questions and _is_relevant_question(fq):
                        # EXTRA CHECK: the follow-up must also connect to dominant traits
                        fq_question = self.questions[fq]
                        if self._has_dominant_trait_overlap(fq_question, session):
                            selected_qid = fq
                            selection_reason = f"follow-up from trait {session.last_answer_trait}"
                            session.current_chain_trait = session.last_answer_trait
                            break
            else:
                print(f"[GUARD] Skipping chain for minority trait '{session.last_answer_trait}' "
                      f"(not in dominant pattern: {sorted(self._get_dominant_traits(session))[:5]})")
        
        # --- Step 1B: If no follow-up found, try the pre-loaded chain_queue ---
        if not selected_qid and session.chain_queue:
            for cq in list(session.chain_queue):
                if cq not in asked and cq in self.questions and _is_relevant_question(cq):
                    cq_question = self.questions[cq]
                    if self._has_dominant_trait_overlap(cq_question, session):
                        selected_qid = cq
                        selection_reason = f"chain queue (domain entry)"
                        break
                # Remove already-asked or non-qualifying questions from queue
                session.chain_queue = [q for q in session.chain_queue if q != cq]
        
        # ═══════════════════════════════════════════════════════════════════
        # PHASE 2: If chain is exhausted, look at accumulated traits
        # to find the strongest unexplored path
        # ═══════════════════════════════════════════════════════════════════
        
        if not selected_qid:
            # Find the strongest trait that still has unanswered follow-up questions
            # Only follow traits whose follow-ups are in relevant branches AND
            # connect back to the user's dominant traits
            sorted_traits = sorted(
                session.trait_scores.items(),
                key=lambda x: x[1],
                reverse=True
            )
            for trait, score in sorted_traits:
                if trait in TRAIT_FOLLOWUP_MAP:
                    for fq in TRAIT_FOLLOWUP_MAP[trait]:
                        if fq not in asked and fq in self.questions and _is_relevant_question(fq):
                            fq_question = self.questions[fq]
                            if self._has_dominant_trait_overlap(fq_question, session):
                                selected_qid = fq
                                selection_reason = f"strongest trait chain ({trait}, score={score:.1f})"
                                session.current_chain_trait = trait
                                break
                if selected_qid:
                    break
        
        # ═══════════════════════════════════════════════════════════════════
        # PHASE 3: If still nothing, move to the next domain in queue
        # Only transition to domains that are relevant to the user's profile
        # ═══════════════════════════════════════════════════════════════════
        
        if not selected_qid:
            # Find next unexplored domain in queue (already filtered to relevant domains)
            for domain in session.domain_queue:
                # Double-check: skip domains not in relevant set
                if domain not in session.relevant_domains:
                    continue
                domain_count = session.domain_question_count.get(domain, 0)
                if domain_count < DOMAIN_MIN_QUESTIONS or domain not in session.explored_domains:
                    entry_qs = DOMAIN_ENTRY_QUESTIONS.get(domain, [])
                    for eq in entry_qs:
                        if eq not in asked and eq in self.questions:
                            selected_qid = eq
                            selection_reason = f"new domain entry ({domain})"
                            session.chain_queue = [q for q in entry_qs if q != eq and q not in asked]
                            break
                if selected_qid:
                    break
        
        # ═══════════════════════════════════════════════════════════════════
        # PHASE 4: FALLBACK — Score remaining questions by information gain
        # + branch affinity. ONLY consider questions from profile-relevant branches.
        # ═══════════════════════════════════════════════════════════════════
        
        if not selected_qid:
            trait_info_scores = self._calculate_trait_information_gain(session)
            branch_weights = session.branch_weights
            relevant = session.relevant_domains
            
            candidates = []
            for qid, question in self.questions.items():
                if qid in asked:
                    continue
                node = QUESTION_TREE_NODES.get(qid)
                if not node:
                    continue
                
                q_branches = set(node["branches"])
                options = question.get('options', [])
                if not options:
                    continue
                
                # STRICT: Only consider questions that touch at least one relevant branch
                if not q_branches & relevant:
                    continue
                
                # Skip heavily rejected questions
                def _opt_has_rejected(opt, rejected):
                    tt = opt.get('trait_tags', {})
                    if isinstance(tt, dict):
                        return any(t in rejected for t in tt)
                    elif isinstance(tt, list):
                        return any(t in rejected for t in tt)
                    return opt.get('trait_tag') in rejected
                rejected_count = sum(1 for opt in options
                                    if _opt_has_rejected(opt, session.rejected_topics))
                if rejected_count / len(options) > 0.3:
                    continue
                
                score = 0.0
                
                # TRAIT CONTINUITY BONUS — strongly favor questions sharing traits
                # with the user's accumulated trait profile and profile seeds
                profile_relevance = self._question_profile_relevance_score(question, session)
                score += profile_relevance * 10.0  # Strong bonus for trait-continuous questions
                
                # Branch affinity — boost questions whose branches overlap with profile
                relevant_overlap = len(q_branches & relevant)
                score += relevant_overlap * 2.0
                
                for branch, weight in branch_weights.items():
                    if branch in q_branches:
                        score += weight
                if q_branches:
                    score /= len(q_branches)
                
                # Information gain
                for opt in options:
                    tt = opt.get('trait_tags', {})
                    if isinstance(tt, dict):
                        for t, w in tt.items():
                            score += trait_info_scores.get(t, 0) * w
                    elif isinstance(tt, list):
                        for t in tt:
                            score += trait_info_scores.get(t, 0)
                    else:
                        t = opt.get('trait_tag')
                        if t:
                            score += trait_info_scores.get(t, 0)
                
                # Question weight from tree
                score += node.get("weight", 1.0)
                
                candidates.append((score, qid))
            
            if candidates:
                candidates.sort(reverse=True, key=lambda x: x[0])
                # Prefer a candidate with trait continuity
                selected_qid = None
                for c_score, c_qid in candidates:
                    if _passes_trait_continuity(c_qid):
                        selected_qid = c_qid
                        selection_reason = f"fallback scoring with continuity (score={c_score:.1f})"
                        break
                # If no trait-continuous candidate, take the top scorer anyway
                if not selected_qid:
                    selected_qid = candidates[0][1]
                    selection_reason = f"fallback scoring (score={candidates[0][0]:.1f})"
        
        # ═══════════════════════════════════════════════════════════════════
        # PHASE 5: SAFETY NET — If strict filtering found nothing but we
        # haven't reached max_questions, prefer questions with trait continuity
        # before falling back to any unanswered question
        # ═══════════════════════════════════════════════════════════════════
        
        if not selected_qid and session.round_number < session.max_questions:
            # First pass: look for any unanswered question with trait continuity
            for qid, question in self.questions.items():
                if qid not in asked and _passes_trait_continuity(qid):
                    selected_qid = qid
                    selection_reason = "safety net (trait-continuous)"
                    print(f"[SAFETY] Trait-continuous fallback at round {round_num}")
                    break
        
        # Last resort: any unanswered question to avoid premature end
        if not selected_qid and session.round_number < session.max_questions:
            for qid, question in self.questions.items():
                if qid not in asked:
                    selected_qid = qid
                    selection_reason = "safety net (last resort)"
                    print(f"[SAFETY] Last resort fallback at round {round_num}")
                    break
        
        # ═══════════════════════════════════════════════════════════════════
        # NO QUESTION AVAILABLE — finalize
        # ═══════════════════════════════════════════════════════════════════
        
        if not selected_qid:
            self._finalize_session(session)
            return None
        
        # ─── RECORD SELECTION ───
        best_question = self.questions[selected_qid]
        session.round_number = round_num
        
        # Track domain question count
        node = QUESTION_TREE_NODES.get(selected_qid, {})
        q_branches = node.get("branches", [])
        for branch in q_branches:
            session.domain_question_count[branch] = session.domain_question_count.get(branch, 0) + 1
            if session.domain_question_count[branch] >= DOMAIN_MIN_QUESTIONS:
                session.explored_domains.add(branch)
        
        # Determine phase label for logging
        q_level = node.get("level", 0)
        phase_labels = {0: "ENTRY", 1: "EXPLORE", 2: "DEEP", 3: "CONFIRM"}
        phase = phase_labels.get(q_level, "?")
        
        print(f"[CHAIN-{phase}] Round {round_num}: Q{selected_qid} "
              f"cat='{best_question.get('category')}' — {selection_reason}")
        
        # Get top courses preview
        sorted_courses = sorted(
            session.course_scores.items(),
            key=lambda x: x[1],
            reverse=True
        )
        top_courses = [
            {
                "course_name": name,
                "current_score": round(score, 1),
                "traits_matched": len(self.course_traits.get(name, set()) & 
                                    set(session.trait_scores.keys()))
            }
            for name, score in sorted_courses[:5]
        ]
        
        return {
            "session_id": session_id,
            "round": session.round_number,
            "total_max_rounds": session.max_questions,
            "question": best_question,
            "courses_remaining": len(session.active_courses),
            "confidence": round(session.confidence * 100, 1),
            "can_finish_early": session.round_number >= session.min_questions,
            "top_courses_preview": top_courses
        }
    
    def _calculate_profile_question_bonus(self, question: dict, profile_traits: Set[str], bonus_multiplier: float) -> float:
        """Calculate bonus score for questions matching user's profile interests/skills."""
        if not profile_traits:
            return 0
        
        options = question.get('options', [])
        matching_options = 0
        
        for opt in options:
            trait_tags = opt.get('trait_tags', {})
            if isinstance(trait_tags, dict):
                if any(t in profile_traits for t in trait_tags):
                    matching_options += 1
            elif isinstance(trait_tags, list):
                if any(t in profile_traits for t in trait_tags):
                    matching_options += 1
            else:
                trait = opt.get('trait_tag')
                if trait and trait in profile_traits:
                    matching_options += 1
        
        # Bonus based on how many options match profile traits
        if matching_options >= 3:
            return bonus_multiplier * 1.5  # Strong match
        elif matching_options >= 2:
            return bonus_multiplier * 1.0
        elif matching_options >= 1:
            return bonus_multiplier * 0.5
        
        return 0
    
    def _calculate_trait_information_gain(self, session: AdaptiveSession) -> Dict[str, float]:
        """
        Calculate how valuable each trait would be to ask about.
        
        Traits that appear in roughly half the active courses are most valuable
        (they split the candidate set best).
        
        Traits we already know about are less valuable.
        """
        trait_value = {}
        total_active = len(session.active_courses)
        
        if total_active == 0:
            return trait_value
        
        for trait, courses_with_trait in self.trait_to_courses.items():
            # How many active courses have this trait?
            active_with_trait = len(courses_with_trait & session.active_courses)
            
            if active_with_trait == 0 or active_with_trait == total_active:
                # This trait doesn't discriminate at all
                trait_value[trait] = 0
                continue
            
            # Information gain is highest when trait splits courses 50/50
            # Entropy: -p*log(p) - (1-p)*log(1-p)
            p = active_with_trait / total_active
            entropy = -p * math.log2(p) - (1-p) * math.log2(1-p) if 0 < p < 1 else 0
            
            # Reduce value if we already have strong info about this trait
            existing_knowledge = abs(session.trait_scores.get(trait, 0))
            knowledge_penalty = 1 / (1 + existing_knowledge * 0.5)
            
            trait_value[trait] = entropy * knowledge_penalty
        
        return trait_value
    
    def _score_question(self, question: dict, trait_values: Dict[str, float], 
                       session: AdaptiveSession) -> float:
        """Score question value based on trait info gain and strand relevance."""
        score = 0
        options = question.get('options', [])
        
        # Get strand priority traits
        strand_priority_traits = set(STRAND_PRIORITY_TRAITS.get(session.user_strand, []))
        
        # Track if this question is primarily about a rejected topic
        rejected_option_count = 0
        total_options = len(options)
        
        for opt in options:
            trait_tags = opt.get('trait_tags', {})
            if isinstance(trait_tags, dict) and trait_tags:
                for trait, weight in trait_tags.items():
                    if trait in session.rejected_topics:
                        rejected_option_count += weight
                    score += trait_values.get(trait, 0) * weight
                    if trait in strand_priority_traits:
                        score += 0.5 * weight
                    mapped_traits = EXPANDED_TRAIT_MAPPING.get(trait, [])
                    for mapped_trait in mapped_traits:
                        score += trait_values.get(mapped_trait, 0) * 0.5 * weight
                        if mapped_trait in strand_priority_traits:
                            score += 0.25 * weight
            elif isinstance(trait_tags, list) and trait_tags:
                for trait in trait_tags:
                    if trait in session.rejected_topics:
                        rejected_option_count += 1
                    score += trait_values.get(trait, 0)
                    if trait in strand_priority_traits:
                        score += 0.5
                    mapped_traits = EXPANDED_TRAIT_MAPPING.get(trait, [])
                    for mapped_trait in mapped_traits:
                        score += trait_values.get(mapped_trait, 0) * 0.5
                        if mapped_trait in strand_priority_traits:
                            score += 0.25
            else:
                trait = opt.get('trait_tag')
                if trait:
                    if trait in session.rejected_topics:
                        rejected_option_count += 1
                    score += trait_values.get(trait, 0)
                    if trait in strand_priority_traits:
                        score += 0.5
                    mapped_traits = EXPANDED_TRAIT_MAPPING.get(trait, [])
                    for mapped_trait in mapped_traits:
                        score += trait_values.get(mapped_trait, 0) * 0.5
                        if mapped_trait in strand_priority_traits:
                            score += 0.25
                    # Check mapped traits for rejection too
                    if mapped_trait in session.rejected_topics:
                        rejected_option_count += 0.5
        
        # Penalize questions about rejected topics
        if total_options > 0:
            rejection_ratio = rejected_option_count / total_options
            if rejection_ratio > 0.5:
                score *= 0.1
            elif rejection_ratio > 0.3:
                score *= 0.4
            elif rejection_ratio > 0.1:
                score *= 0.7
        
        # Bonus for questions with more options (more information)
        option_bonus = min(len(options) / 4, 1.5)
        score *= option_bonus
        
        # Category diversity bonus (prefer different categories)
        category = question.get('category', '')
        category_count = sum(1 for qid in session.answered_questions 
                           if self.questions.get(qid, {}).get('category') == category)
        diversity_bonus = 1 / (1 + category_count * 0.2)
        score *= diversity_bonus
        
        return score
    
    def process_answer(self, session_id: str, question_id: int, 
                      chosen_option_id: int) -> dict:
        """Process answer and update trait/course scores."""
        session = self.sessions.get(session_id)
        if not session:
            print(f"[WARN] process_answer: Session {session_id} not found!")
            return {"error": "Session not found"}
        
        if session.is_complete:
            print(f"[WARN] process_answer: Session {session_id} already complete, answer NOT recorded for q{question_id}")
            return {
                "status": "complete",
                "recommendations": session.final_recommendations
            }
        
        question = self.questions.get(question_id)
        if not question:
            print(f"[WARN] process_answer: Question {question_id} not found in engine questions!")
            return {"error": "Question not found"}
        
        # Find the chosen option
        chosen_option = None
        for opt in question.get('options', []):
            if opt.get('option_id') == chosen_option_id:
                chosen_option = opt
                break
        
        if not chosen_option:
            print(f"[WARN] process_answer: Option {chosen_option_id} not found for question {question_id}!")
            return {"error": "Option not found"}
        
        # Check if this question was already answered (prevent duplicate answers)
        if question_id in session.answered_questions:
            print(f"[WARN] process_answer: Question {question_id} already answered! Skipping duplicate.")
            # Still return success to not break the flow, but don't overwrite
            return {
                "status": "duplicate",
                "message": "Question already answered",
                "session_id": session_id,
                "round": session.round_number,
                "confidence": round(session.confidence * 100, 1),
                "courses_remaining": len(self.courses),
                "traits_discovered": len(session.trait_scores)
            }
        
        # Record the answer
        session.answered_questions[question_id] = chosen_option_id
        session.excluded_question_ids.add(question_id)
        session.question_history.append(question_id)  # Track for "Previous" button
        print(f"[ANSWER] Q{question_id} answered. Total answers={len(session.answered_questions)}, round={session.round_number}, excluded={len(session.excluded_question_ids)}")
        
        # Check if user rejected this topic (e.g., "none", "not interested")
        option_text = chosen_option.get('option_text', '').lower()
        is_rejection = any(phrase in option_text for phrase in [
            "none", "not interested", "don't want", "prefer not", 
            "i'm not", "im not", "prefer non-", "prefer other",
            "i don't want to", "not for me"
        ])
        
        # Track rejection data for this question (for reversal with "Previous" button)
        rejection_data = {"rejected_topics": [], "course_penalties": {}}
        
        # Also check for specific topic rejections in the option text
        EXPLICIT_REJECTIONS = {
            "don't want to teach": "Teaching-Ed",
            "not teach": "Teaching-Ed",
            "don't want to be a teacher": "Teaching-Ed",
            "not in education": "Teaching-Ed",
            "don't want healthcare": "Patient-Care",
            "not medical": "Patient-Care",
            "don't want engineering": "Civil-Build",
            "not engineering": "Civil-Build",
            "don't want business": "Finance-Acct",
            "not business": "Finance-Acct",
            "don't want technology": "Software-Dev",
            "not tech": "Software-Dev",
            "don't want maritime": "Maritime-Sea",
            "not maritime": "Maritime-Sea",
        }
        
        for phrase, topic in EXPLICIT_REJECTIONS.items():
            if phrase in option_text:
                if topic not in session.rejected_topics:  # Only add if not already rejected
                    session.rejected_topics.add(topic)
                    rejection_data["rejected_topics"].append(topic)
                    print(f"[REJECT] Explicit rejection detected: {topic}")
        
        if is_rejection:
            # Determine what topic was rejected based on the question category and other options
            rejected_topic = self._determine_rejected_topic(question, chosen_option)
            if rejected_topic and rejected_topic not in session.rejected_topics:
                session.rejected_topics.add(rejected_topic)
                rejection_data["rejected_topics"].append(rejected_topic)
                print(f"[REJECT] User rejected topic: {rejected_topic}")
                
                # Penalize courses associated with this rejected topic
                for course_name, course_traits in self.course_traits.items():
                    if rejected_topic in course_traits:
                        session.course_scores[course_name] -= 8  # Penalty for rejected topic
                        # Track the penalty for reversal
                        rejection_data["course_penalties"][course_name] = rejection_data["course_penalties"].get(course_name, 0) + 8
        
        # Store rejection data for this question (for reversal)
        session.answer_rejection_data[question_id] = rejection_data
        
        # Extract trait from chosen option — supports weighted dict format:
        # trait_tags: {"Software-Dev": 1.0, "Data-Analytics": 0.5} (weighted dict)
        chosen_trait_tags = chosen_option.get('trait_tags', {})
        if isinstance(chosen_trait_tags, dict) and chosen_trait_tags:
            chosen_trait = max(chosen_trait_tags, key=chosen_trait_tags.get)
        elif isinstance(chosen_trait_tags, list) and chosen_trait_tags:
            chosen_trait = chosen_trait_tags[0]
        else:
            chosen_trait = chosen_option.get('trait_tag')
        option_text = chosen_option.get('option_text', '').lower()
        
        # Track all trait changes for this question (for reversal with "Previous" button)
        trait_changes = {}
        
        # Check if this is a "None" or "Not interested" option
        is_none_option = any(phrase in option_text for phrase in [
            'none', 'not interested', "don't want", 'prefer not',
            'none of these', 'not for me', "i don't"
        ])
        
        # Track which traits to update course scores for
        traits_to_boost = []
        
        if is_none_option:
            # For "None" options, don't add any traits - the user is rejecting this topic
            # The rejection penalty was already applied above
            # This prevents arbitrary traits from being added
            print(f"[NONE_OPTION] No traits added - user rejected this topic")
            chosen_trait = None
        elif isinstance(chosen_trait_tags, dict) and chosen_trait_tags:
            # Weighted dict format: apply each trait with its weight
            for trait, weight in chosen_trait_tags.items():
                current = session.trait_scores.get(trait, 0)
                session.trait_scores[trait] = current + weight
                trait_changes[trait] = trait_changes.get(trait, 0) + weight
                traits_to_boost.append(trait)
            chosen_trait = max(chosen_trait_tags, key=chosen_trait_tags.get)
        elif isinstance(chosen_trait_tags, list) and chosen_trait_tags:
            # Legacy list format
            for idx, tag in enumerate(chosen_trait_tags):
                weight = 1.0 if idx == 0 else 0.6
                current = session.trait_scores.get(tag, 0)
                session.trait_scores[tag] = current + weight
                trait_changes[tag] = trait_changes.get(tag, 0) + weight
                traits_to_boost.append(tag)
            chosen_trait = chosen_trait_tags[0]
        elif chosen_trait:
            # Fallback: single trait_tag (old format)
            current = session.trait_scores.get(chosen_trait, 0)
            session.trait_scores[chosen_trait] = current + 1.0
            trait_changes[chosen_trait] = 1.0
            traits_to_boost.append(chosen_trait)
            
            # Also add mapped traits (from our enhanced trait system)
            mapped_traits = EXPANDED_TRAIT_MAPPING.get(chosen_trait, [])
            for mapped_trait in mapped_traits:
                current = session.trait_scores.get(mapped_trait, 0)
                session.trait_scores[mapped_trait] = current + 0.5
                trait_changes[mapped_trait] = trait_changes.get(mapped_trait, 0) + 0.5
                traits_to_boost.append(mapped_trait)
        
        # Store the trait changes for this question (for reversal)
        session.answer_trait_changes[question_id] = trait_changes
        
        # Update course scores based on this answer - for all traits boosted
        for trait in traits_to_boost:
            self._update_course_scores(session, trait)
        
        # --- Track topic continuity for profile-driven question selection ---
        if chosen_trait:
            session.recent_traits.append(chosen_trait)
            # Determine new current topic from recent window
            new_topic, _ = self._get_current_topic_and_adjacent(session)
            if new_topic == session.current_topic_thread and new_topic:
                session.topic_streak += 1
            else:
                session.topic_streak = 1 if new_topic else 0
            session.current_topic_thread = new_topic
        
        # --- Conversation Chain: Update last_answer_trait for next question routing ---
        # IMPORTANT: Only let the answer trait drive the chain if it's consistent
        # with the user's dominant pattern. If the trait is a minority (one-off),
        # keep the chain following the dominant trait instead.
        if chosen_trait and not is_none_option:
            session.last_answer_trait = chosen_trait
            is_dominant = self._is_dominant_trait(chosen_trait, session)
            early_stage = len(session.answered_questions) < 5
            
            if is_dominant or early_stage:
                # Trait is part of user's dominant pattern — update chain normally
                if chosen_trait in TRAIT_FOLLOWUP_MAP:
                    new_chain = [q for q in TRAIT_FOLLOWUP_MAP[chosen_trait]
                                 if q not in session.excluded_question_ids and q in self.questions]
                    session.chain_queue = new_chain
                    session.current_chain_trait = chosen_trait
                    print(f"[CHAIN] Answer trait={chosen_trait} (dominant) -> follow-up chain: {new_chain[:5]}")
                else:
                    session.chain_queue = []
                    print(f"[CHAIN] Answer trait={chosen_trait} (dominant, no follow-up map)")
            else:
                # Trait is a minority one-off — do NOT replace the chain queue.
                # Keep following the dominant trait's chain instead.
                dominant = self._get_dominant_traits(session)
                print(f"[CHAIN] Answer trait={chosen_trait} is MINORITY (dominant: {sorted(dominant)[:5]}). "
                      f"Keeping existing chain for continuity.")
                # Don't overwrite chain_queue — let Phase 2 pick up the strongest trait
        else:
            session.last_answer_trait = ""
        
        # --- Decision Tree: Update branch weights based on answer ---
        # When user picks a trait, BOOST the corresponding branch and adjacent branches
        if chosen_trait and not is_none_option:
            chosen_branch = TRAIT_TO_BRANCH.get(chosen_trait, "")
            if chosen_branch:
                # Strong boost to the chosen branch
                session.branch_weights[chosen_branch] = session.branch_weights.get(chosen_branch, 0) + 2.0
                # Moderate boost to adjacent branches
                for adj_branch in BRANCH_ADJACENCY.get(chosen_branch, []):
                    session.branch_weights[adj_branch] = session.branch_weights.get(adj_branch, 0) + 0.5
                session.branch_history.append(chosen_branch)
                
                # Also boost from secondary traits (multi-trait options)
                secondary_traits = chosen_option.get('trait_tags') or chosen_option.get('traits') or {}
                if isinstance(secondary_traits, dict) and secondary_traits:
                    for trait, weight in secondary_traits.items():
                        if trait != chosen_trait:
                            sec_branch = TRAIT_TO_BRANCH.get(trait, "")
                            if sec_branch:
                                session.branch_weights[sec_branch] = session.branch_weights.get(sec_branch, 0) + weight * 0.5
                
                # Dynamically expand relevant_domains if user consistently picks a new domain
                # (allows natural discovery while keeping profile focus)
                if chosen_branch not in session.relevant_domains:
                    branch_count = session.branch_history.count(chosen_branch)
                    if branch_count >= 2:  # User picked this domain at least twice
                        session.relevant_domains.add(chosen_branch)
                        if chosen_branch not in session.domain_queue:
                            session.domain_queue.append(chosen_branch)
                        for adj in BRANCH_ADJACENCY.get(chosen_branch, []):
                            session.relevant_domains.add(adj)
                        print(f"[EXPAND] Domain '{chosen_branch}' added to relevant domains (picked {branch_count}x)")
        
        # Track question weight for this question (for scoring impact)
        node = QUESTION_TREE_NODES.get(question_id, {})
        q_weight = node.get("weight", 1.0)
        session.question_weights_applied[question_id] = q_weight
        
        # Calculate confidence
        session.confidence = self._calculate_confidence(session)
        
        # Get current top courses for preview (from ALL courses, not just active)
        sorted_courses = sorted(
            session.course_scores.items(),
            key=lambda x: x[1],
            reverse=True
        )
        
        # Show top 5 courses with their matched trait count
        top_courses = [
            {
                "course_name": name,
                "current_score": round(score, 1),
                "traits_matched": len(self.course_traits.get(name, set()) & 
                                    set(session.trait_scores.keys()))
            }
            for name, score in sorted_courses[:5]
        ]
        
        # Build all_traits as a list of trait names (sorted by weight descending for dicts)
        if isinstance(chosen_trait_tags, dict) and chosen_trait_tags:
            all_traits_list = sorted(chosen_trait_tags.keys(), key=lambda t: chosen_trait_tags[t], reverse=True)
        elif isinstance(chosen_trait_tags, list) and chosen_trait_tags:
            all_traits_list = list(chosen_trait_tags)
        elif chosen_trait:
            all_traits_list = [chosen_trait]
        else:
            all_traits_list = []
        
        return {
            "status": "continue",
            "session_id": session_id,
            "round": session.round_number,
            "trait_recorded": chosen_trait,
            "all_traits": all_traits_list,
            "courses_remaining": len(self.courses),  # All courses remain in consideration
            "confidence": round(session.confidence * 100, 1),
            "top_courses_preview": top_courses,
            "traits_discovered": len(session.trait_scores)
        }
    
    def _get_specialized_similarity(self, trait1: str, trait2: str) -> float:
        """Get similarity score between two traits (0-1)."""
        # Exact match
        if trait1 == trait2:
            return 1.0
        
        # Check specialized trait relationships first (more accurate for new system)
        if trait1 in SPECIALIZED_TRAIT_RELATIONSHIPS:
            if trait2 in SPECIALIZED_TRAIT_RELATIONSHIPS[trait1]:
                return SPECIALIZED_TRAIT_RELATIONSHIPS[trait1][trait2]
        
        if trait2 in SPECIALIZED_TRAIT_RELATIONSHIPS:
            if trait1 in SPECIALIZED_TRAIT_RELATIONSHIPS[trait2]:
                return SPECIALIZED_TRAIT_RELATIONSHIPS[trait2][trait1]
        
        # Fall back to old trait system for backward compatibility
        return get_trait_similarity(trait1, trait2)
    
    def _update_course_scores(self, session: AdaptiveSession, chosen_trait: str):
        """Boost course scores based on trait matches, weighted by question depth."""
        if not chosen_trait:
            return
        
        # Get the question weight from the decision tree node
        # Deeper questions (higher weight) have MORE impact on scoring
        last_qid = session.question_history[-1] if session.question_history else None
        question_weight = 1.0
        if last_qid:
            node = QUESTION_TREE_NODES.get(last_qid, {})
            question_weight = node.get("weight", 1.0)
        
        # Early answers also have extra impact (profile confirmation)
        early_boost_multiplier = 1.0
        if session.round_number <= 3:
            early_boost_multiplier = 2.0  # First 3 answers: 2x impact
        elif session.round_number <= 7:
            early_boost_multiplier = 1.5  # Next 4 answers: 1.5x impact
        
        # Dampen boost for minority traits — prevents one off-topic answer
        # from swinging course recommendations away from the user's pattern
        is_dominant = self._is_dominant_trait(chosen_trait, session)
        early_stage = len(session.answered_questions) < 5
        dominance_multiplier = 1.0 if (is_dominant or early_stage) else 0.25
        
        # Combined multiplier: question weight × early boost × dominance
        total_multiplier = question_weight * early_boost_multiplier * dominance_multiplier
        
        for course_name in list(session.active_courses):
            course_traits = self.course_traits.get(course_name, set())
            
            # Direct trait match - BIG BOOST (matches unique specialized trait)
            if chosen_trait in course_traits:
                boost = 12.0 * total_multiplier  # Base 12 points × question weight × early boost
                session.course_scores[course_name] += boost
            else:
                # Check for similar traits using our SPECIALIZED trait system
                best_similarity = 0
                for course_trait in course_traits:
                    sim = self._get_specialized_similarity(chosen_trait, course_trait)
                    best_similarity = max(best_similarity, sim)
                
                # Similarity-based score boost (tighter thresholds to prevent spillover)
                if best_similarity > 0.7:
                    session.course_scores[course_name] += 5.0 * total_multiplier
                elif best_similarity > 0.4:
                    session.course_scores[course_name] += 2.0 * total_multiplier
    
    def _calculate_confidence(self, session: AdaptiveSession) -> float:
        """Calculate recommendation confidence based on score separation and trait focus."""
        if len(session.active_courses) == 0:
            return 1.0
        
        sorted_scores = sorted(session.course_scores.values(), reverse=True)
        n = len(sorted_scores)
        
        if n < 2:
            return 0.5
        
        # ── Factor 1: Score separation (top 3 avg vs median) ──
        # Using median instead of rest-10 gives much wider gap since
        # median courses barely move while top courses accumulate boosts
        top_3_avg = sum(sorted_scores[:min(3, n)]) / min(3, n)
        median_score = sorted_scores[n // 2]
        
        if top_3_avg <= 0:
            separation = 0.0
        else:
            separation = (top_3_avg - median_score) / top_3_avg
        separation = min(max(separation, 0), 1)
        
        # ── Factor 2: Top cluster tightness ──
        # If top 3 courses have similar scores, we're more confident
        # in a coherent recommendation group
        top_3_min = sorted_scores[min(2, n - 1)]
        if sorted_scores[0] > 0:
            top_spread = (sorted_scores[0] - top_3_min) / sorted_scores[0]
            cluster_tightness = 1.0 - top_spread
        else:
            cluster_tightness = 0.5
        cluster_tightness = min(max(cluster_tightness, 0), 1)
        
        # ── Factor 3: Question progress ──
        question_factor = min(session.round_number / session.min_questions, 1.0)
        
        # Combined: separation dominates, progress and cluster tightness support
        confidence = separation * 0.50 + question_factor * 0.30 + cluster_tightness * 0.20
        return min(max(confidence, 0), 1)
    
    def _should_stop(self, session: AdaptiveSession) -> bool:
        """Determine if we should stop asking questions"""
        # Must ask minimum questions (use session's min_questions)
        if session.round_number < session.min_questions:
            return False
        
        # Stop at max questions (use session's max_questions)
        if session.round_number >= session.max_questions:
            return True
        
        # Stop if confidence is high enough AND we've answered well past minimum
        # Require at least 60% of max_questions before allowing confidence-based stop
        min_for_confidence = int(session.max_questions * 0.6)
        if session.round_number >= min_for_confidence and session.confidence >= self.CONFIDENCE_THRESHOLD:
            print(f"[STOP] Confidence-based stop at round {session.round_number}: confidence={session.confidence:.2f}")
            return True
        
        return False
    
    def _finalize_session(self, session: AdaptiveSession):
        """Build final course recommendations."""
        print(f"[OK_GREEN] FINALIZE SESSION CALLED - session_id: {session.session_id}")
        session.is_complete = True
        
        # Sort courses by score
        sorted_courses = sorted(
            session.course_scores.items(),
            key=lambda x: x[1],
            reverse=True
        )
        
        print(f"[OK_GREEN] Total courses scored: {len(sorted_courses)}")
        if sorted_courses:
            print(f"[OK_GREEN] Top 5 courses: {sorted_courses[:5]}")
        
        # Normalize scores to percentages
        top_score = sorted_courses[0][1] if sorted_courses else 1
        min_score = sorted_courses[-1][1] if sorted_courses else 0
        score_range = max(top_score - min_score, 0.001)  # Prevent division by zero
        
        recommendations = []
        for i, (course_name, raw_score) in enumerate(sorted_courses[:self.TOP_N_RECOMMENDATIONS]):
            course = self.courses.get(course_name, {})
            course_traits = self.course_traits.get(course_name, set())
            
            # Calculate match percentage (curved for realism)
            normalized = (raw_score - min_score) / score_range
            # Ensure normalized is a valid number
            if not isinstance(normalized, (int, float)) or normalized != normalized:  # NaN check
                normalized = 0.5
            normalized = max(0, min(1, normalized))  # Clamp to 0-1
            # Apply curve: 97% max, 55% min for top 5
            percentage = 55 + (normalized * 42)
            
            # Final safety check for percentage
            if not isinstance(percentage, (int, float)) or percentage != percentage:  # NaN check
                percentage = 75.0  # Default reasonable value
            percentage = max(55, min(97, percentage))  # Clamp to valid range
            
            # Find which traits matched
            matched_traits = list(course_traits & set(session.trait_scores.keys()))
            
            # Calculate profile bonus for display (shows if user's interests/skills helped)
            profile_bonus = 0
            if session.user_interests or session.user_skills:
                profile_bonus = self._calculate_profile_bonus(
                    session.user_interests, 
                    session.user_skills, 
                    course_traits
                )
            
            reasoning = self._generate_recommendation_reasoning(
                session, course_name, course, course_traits, 
                matched_traits, profile_bonus, raw_score
            )
            
            recommendations.append({
                "rank": i + 1,
                "course_name": course_name,
                "description": course.get('description', ''),
                "match_percentage": round(float(percentage), 1),
                "matched_traits": matched_traits[:5],  # Top 5 traits
                "minimum_gwa": course.get('minimum_gwa'),
                "recommended_strand": course.get('required_strand'),
                "profile_bonus_applied": profile_bonus > 0,
                "reasoning": reasoning  # Detailed explanation
            })
        
        session.final_recommendations = recommendations
        print(f"[OK_GREEN] Generated {len(recommendations)} recommendations")
        print(f"[OK_GREEN] Recommendation course names: {[r['course_name'] for r in recommendations]}")
        print(f"[OK] Session {session.session_id} complete after {session.round_number} questions")
    
    def _generate_recommendation_reasoning(self, session: AdaptiveSession, course_name: str,
                                           course: dict, course_traits: Set[str],
                                           matched_traits: List[str], profile_bonus: float,
                                           raw_score: float) -> str:
        """Generate explanation for why this course was recommended."""
        reasons = []
        
        # Trait matches from responses
        if matched_traits:
            trait_labels = self._get_trait_labels(matched_traits[:3])
            if len(matched_traits) >= 3:
                reasons.append(f"Your responses showed strong alignment with {trait_labels}")
            elif len(matched_traits) >= 1:
                reasons.append(f"You demonstrated interest in {trait_labels}")
        
        # Profile interests match
        profile_matches = []
        if session.user_interests:
            interests = [i.strip().lower() for i in session.user_interests.split(',') if i.strip()]
            course_name_lower = course_name.lower()
            course_desc_lower = course.get('description', '').lower()
            
            for interest in interests:
                interest_label = self._get_interest_label(interest)
                if interest_label and (interest in course_name_lower or 
                    any(t.lower() in course_desc_lower for t in self._get_interest_traits(interest))):
                    profile_matches.append(interest_label)
        
        if profile_matches:
            reasons.append(f"This aligns with your stated interests: {', '.join(profile_matches[:2])}")
        
        # Skills match
        skill_matches = []
        if session.user_skills:
            skills = [s.strip().lower() for s in session.user_skills.split(',') if s.strip()]
            for skill in skills:
                skill_label = self._get_skill_label(skill)
                if skill_label and profile_bonus > 0:
                    skill_matches.append(skill_label)
        
        if skill_matches and len(skill_matches) <= 2:
            reasons.append(f"Your skills in {', '.join(skill_matches[:2])} are valuable for this field")
        
        # Strand match
        required_strand = course.get('required_strand', '')
        if session.user_strand and required_strand:
            if session.user_strand.upper() == required_strand.upper():
                reasons.append(f"This is a natural progression from your {session.user_strand} strand")
            elif required_strand.upper() == "GAS":
                reasons.append("This course welcomes students from any strand background")
        
        # Career category bonus
        career_reason = self._get_career_reasoning(course_name, course_traits)
        if career_reason:
            reasons.append(career_reason)
        
        # Strong answer patterns
        strong_traits = [t for t, score in session.trait_scores.items() if score >= 2.0]
        strong_matching = [t for t in strong_traits if t in course_traits]
        if strong_matching:
            trait_label = self._get_trait_labels([strong_matching[0]])
            reasons.append(f"You consistently showed preference for {trait_label}-related activities")
        
        # Combine reasons into a coherent paragraph
        if not reasons:
            # Fallback reasoning
            return f"Based on your assessment responses, {course_name} appears to be a good match for your interests and aptitudes."
        
        # Join first 3 reasons
        reasoning_text = ". ".join(reasons[:3])
        if not reasoning_text.endswith('.'):
            reasoning_text += '.'
        
        return reasoning_text
    
    def _get_trait_labels(self, traits: List[str]) -> str:
        """Convert trait tags to readable labels."""
        TRAIT_LABELS = {
            "Patient-Care": "patient care and healthcare",
            "Medical-Lab": "medical laboratory and diagnostics",
            "Rehab-Therapy": "therapy and rehabilitation",
            "Software-Dev": "software development and programming",
            "Hardware-Systems": "computer hardware and systems",
            "Data-Analytics": "data analysis and statistics",
            "Cyber-Defense": "cybersecurity",
            "Digital-Media": "digital media and multimedia",
            "Civil-Build": "construction and infrastructure",
            "Mechanical-Design": "mechanical systems and design",
            "Electrical-Power": "electrical systems",
            "Industrial-Ops": "industrial operations",
            "Spatial-Design": "spatial design and architecture",
            "Finance-Acct": "finance and accounting",
            "Marketing-Sales": "marketing and sales",
            "Startup-Venture": "entrepreneurship and business",
            "Admin-Skill": "administration and organization",
            "Teaching-Ed": "teaching and education",
            "Visual-Design": "visual arts and design",
            "Creative-Skill": "creative and artistic expression",
            "Law-Enforce": "law enforcement and justice",
            "Community-Serve": "public service and community",
            "Maritime-Sea": "maritime and ocean industries",
            "Agri-Nature": "agriculture and environmental science",
            "Hospitality-Svc": "hospitality and tourism",
            "Lab-Research": "scientific research",
            "Field-Research": "field research and exploration",
            "People-Skill": "interpersonal communication",
            "Technical-Skill": "technical problem-solving",
        }
        labels = [TRAIT_LABELS.get(t, t.replace('-', ' ').lower()) for t in traits]
        if len(labels) == 1:
            return labels[0]
        elif len(labels) == 2:
            return f"{labels[0]} and {labels[1]}"
        else:
            return f"{', '.join(labels[:-1])}, and {labels[-1]}"
    
    def _get_interest_label(self, interest: str) -> str:
        """Map interest ID to display name."""
        INTEREST_LABELS = {
            "science": "Science & Research", "biology": "Biology",
            "chemistry": "Chemistry", "physics": "Physics",
            "environment": "Environmental Science", "earth_science": "Earth Science",
            "programming": "Programming", "computer": "Computers & IT",
            "data": "Data Analytics", "ai": "AI & Machine Learning",
            "cybersecurity": "Cybersecurity", "robotics": "Robotics",
            "game_dev": "Game Development",
            "engineering": "Engineering", "mechanical": "Mechanical Systems",
            "electrical": "Electronics", "civil": "Civil Engineering",
            "architecture": "Architecture", "industrial": "Industrial Engineering",
            "business": "Business", "finance": "Finance",
            "marketing": "Marketing", "accounting": "Accounting",
            "economics": "Economics", "management": "Management",
            "real_estate": "Real Estate",
            "art": "Arts & Design", "music": "Music",
            "film": "Film & Media", "writing": "Writing",
            "photography": "Photography", "animation": "Animation",
            "fashion": "Fashion Design",
            "medical": "Medicine", "nursing": "Nursing",
            "psychology": "Psychology", "pharmacy": "Pharmacy",
            "physical_therapy": "Physical Therapy", "nutrition": "Nutrition",
            "medical_tech": "Medical Technology", "dentistry": "Dentistry",
            "education": "Education", "law": "Law",
            "politics": "Political Science", "social": "Social Work",
            "history": "History", "communication": "Communication",
            "philosophy": "Philosophy", "criminology": "Criminology",
            "maritime": "Maritime", "aviation": "Aviation",
            "logistics": "Logistics",
            "sports": "Sports", "tourism": "Tourism",
            "food": "Culinary Arts", "agriculture": "Agriculture",
            "veterinary": "Veterinary Science", "military": "Military",
        }
        return INTEREST_LABELS.get(interest.lower(), "")
    
    def _get_interest_traits(self, interest: str) -> List[str]:
        """Get keywords associated with an interest."""
        INTEREST_TRAITS = {
            "science": ["scientific", "research", "laboratory"],
            "programming": ["software", "coding", "development", "tech"],
            "business": ["business", "entrepreneurship", "management"],
            "medical": ["medical", "healthcare", "patient"],
            "nursing": ["nursing", "patient care", "healthcare"],
            "engineering": ["engineering", "technical", "mechanical"],
            "education": ["education", "teaching", "pedagogy"],
            "art": ["art", "design", "creative"],
        }
        return INTEREST_TRAITS.get(interest.lower(), [interest])
    
    def _get_skill_label(self, skill: str) -> str:
        """Map skill ID to display name."""
        SKILL_LABELS = {
            "programming_skill": "Programming", "data_analysis": "Data Analysis",
            "web_development": "Web Development", "graphic_design": "Graphic Design",
            "video_editing": "Video Editing", "math_skills": "Mathematics",
            "laboratory": "Laboratory Work", "technical_writing": "Technical Writing",
            "electronics": "Electronics", "drafting": "Drafting & CAD",
            "public_speaking": "Public Speaking", "writing_skill": "Writing",
            "presentation": "Presentation", "negotiation": "Negotiation",
            "foreign_language": "Foreign Languages",
            "filipino_language": "Filipino Communication",
            "social_media": "Social Media",
            "leadership": "Leadership", "project_management": "Project Management",
            "team_management": "Team Management", "decision_making": "Decision Making",
            "planning": "Planning & Organization", "time_management": "Time Management",
            "teamwork": "Teamwork", "empathy": "Empathy",
            "customer_service": "Customer Service", "mentoring": "Mentoring",
            "conflict_resolution": "Conflict Resolution",
            "counseling": "Counseling",
            "critical_thinking": "Critical Thinking", "problem_solving": "Problem Solving",
            "research": "Research", "attention_detail": "Attention to Detail",
            "logical_reasoning": "Logical Reasoning",
            "creativity": "Creativity", "artistic": "Artistic Ability",
            "music_skill": "Musical Ability", "storytelling": "Storytelling",
            "design_thinking": "Design Thinking",
            "photography_skill": "Photography",
            "cooking": "Cooking", "first_aid": "First Aid",
            "sports_fitness": "Sports & Fitness", "driving": "Driving",
            "gardening": "Gardening", "repair_maintenance": "Repair & Maintenance",
        }
        return SKILL_LABELS.get(skill.lower(), "")
    
    def _get_career_reasoning(self, course_name: str, course_traits: Set[str]) -> str:
        """Get career-focused blurb based on course traits."""
        course_lower = course_name.lower()
        
        if any(t in course_traits for t in ["Patient-Care", "Medical-Lab", "Rehab-Therapy"]):
            return "This career path offers opportunities to help others and make a direct impact on people's health and wellbeing"
        
        if any(t in course_traits for t in ["Software-Dev", "Hardware-Systems", "Data-Analytics"]):
            return "The tech industry offers excellent career growth, competitive salaries, and opportunities for innovation"
        
        if any(t in course_traits for t in ["Civil-Build", "Mechanical-Design", "Electrical-Power"]):
            return "Engineering careers are in high demand and offer the chance to build and create tangible solutions"
        
        if any(t in course_traits for t in ["Finance-Acct", "Marketing-Sales", "Startup-Venture"]):
            return "Business careers offer diverse paths from corporate roles to entrepreneurship opportunities"
        
        if any(t in course_traits for t in ["Teaching-Ed"]):
            return "Education careers allow you to shape future generations and make a lasting societal impact"
        
        if any(t in course_traits for t in ["Visual-Design", "Creative-Skill", "Digital-Media"]):
            return "Creative careers let you express yourself while building practical skills valued in many industries"
        
        if any(t in course_traits for t in ["Law-Enforce", "Community-Serve"]):
            return "Public service careers offer the satisfaction of serving your community and upholding justice"
        
        if any(t in course_traits for t in ["Maritime-Sea"]):
            return "Maritime careers offer unique opportunities for travel and are essential to global trade"
        
        if any(t in course_traits for t in ["Hospitality-Svc"]):
            return "Hospitality careers combine service excellence with opportunities in tourism and culinary arts"
        
        if any(t in course_traits for t in ["Agri-Nature", "Field-Research"]):
            return "Careers in agriculture and environmental science address crucial sustainability challenges"
        
        return ""
    
    def get_final_results(self, session_id: str) -> dict:
        """Retrieve final recommendations."""
        print(f"[BLUE] get_final_results called for session: {session_id}")
        session = self.sessions.get(session_id)
        if not session:
            print(f"[RED] Session not found: {session_id}")
            return {"error": "Session not found"}
        
        if not session.is_complete:
            print(f"[YELLOW] Session not complete, forcing finalize...")
            # Force finalize
            self._finalize_session(session)
        
        print(f"[BLUE] Returning {len(session.final_recommendations)} recommendations")
        return {
            "session_id": session_id,
            "is_complete": True,
            "total_questions_asked": session.round_number,
            "traits_discovered": len(session.trait_scores),
            "confidence": round(session.confidence * 100, 1),
            "recommendations": session.final_recommendations
        }
    
    def finish_early(self, session_id: str) -> dict:
        """End session early and return current recommendations."""
        session = self.sessions.get(session_id)
        if not session:
            return {"error": "Session not found"}
        
        if session.round_number < self.MIN_QUESTIONS:
            return {
                "error": f"Please answer at least {self.MIN_QUESTIONS} questions",
                "current_round": session.round_number,
                "minimum_required": self.MIN_QUESTIONS
            }
        
        self._finalize_session(session)
        return self.get_final_results(session_id)
    
    def go_to_previous_question(self, session_id: str) -> dict:
        """Go back to previous question and allow user to change answer."""
        session = self.sessions.get(session_id)
        if not session:
            return {"error": "Session not found"}
        
        if len(session.question_history) == 0:
            return {"error": "No previous questions"}
        
        # Get the last answered question
        previous_question_id = session.question_history.pop()
        
        # Remove from answered and excluded
        if previous_question_id in session.answered_questions:
            del session.answered_questions[previous_question_id]
        session.excluded_question_ids.discard(previous_question_id)
        
        # PROPERLY reverse all trait score changes from this answer
        if previous_question_id in session.answer_trait_changes:
            trait_changes = session.answer_trait_changes[previous_question_id]
            for trait, amount in trait_changes.items():
                if trait in session.trait_scores:
                    session.trait_scores[trait] -= amount
                    # Remove trait if score is 0 or negative
                    if session.trait_scores[trait] <= 0:
                        del session.trait_scores[trait]
            # Remove the stored changes
            del session.answer_trait_changes[previous_question_id]
            print(f"[PREVIOUS] Reversed trait changes: {trait_changes}")
        
        # PROPERLY reverse rejection data (rejected topics and course penalties)
        if previous_question_id in session.answer_rejection_data:
            rejection_data = session.answer_rejection_data[previous_question_id]
            
            # Remove rejected topics that were added by this question
            for topic in rejection_data.get("rejected_topics", []):
                session.rejected_topics.discard(topic)
                print(f"[PREVIOUS] Removed rejected topic: {topic}")
            
            # Reverse course penalties
            for course_name, penalty in rejection_data.get("course_penalties", {}).items():
                if course_name in session.course_scores:
                    session.course_scores[course_name] += penalty  # Add back the penalty
                    print(f"[PREVIOUS] Reversed penalty for {course_name}: +{penalty}")
            
            # Remove the stored rejection data
            del session.answer_rejection_data[previous_question_id]
        
        # Get the question to show again
        question = self.questions.get(previous_question_id)
        
        # Decrement round
        session.round_number -= 1
        
        # Reverse decision tree branch tracking
        if session.branch_history:
            session.branch_history.pop()
        if session.recent_traits:
            session.recent_traits.pop()
        # Remove question weight tracking
        session.question_weights_applied.pop(previous_question_id, None)
        # Rebuild topic thread from remaining recent_traits
        if session.recent_traits:
            new_topic, _ = self._get_current_topic_and_adjacent(session)
            session.current_topic_thread = new_topic
            # Recalculate streak
            streak = 0
            for t in reversed(session.recent_traits):
                branch = TRAIT_TO_BRANCH.get(t, "")
                if branch == TRAIT_TO_BRANCH.get(session.recent_traits[-1], ""):
                    streak += 1
                else:
                    break
            session.topic_streak = streak
        else:
            session.current_topic_thread = ""
            session.topic_streak = 0
        
        # Reverse conversation chain state
        # Set last_answer_trait to the previous answer's trait (if any remain)
        if session.recent_traits:
            session.last_answer_trait = session.recent_traits[-1]
            # Only rebuild chain from this trait if it's a dominant trait
            is_dominant = self._is_dominant_trait(session.last_answer_trait, session)
            early_stage = len(session.answered_questions) < 5
            if (is_dominant or early_stage) and session.last_answer_trait in TRAIT_FOLLOWUP_MAP:
                session.chain_queue = [q for q in TRAIT_FOLLOWUP_MAP[session.last_answer_trait]
                                       if q not in session.excluded_question_ids and q in self.questions]
                session.current_chain_trait = session.last_answer_trait
            else:
                session.chain_queue = []
                session.current_chain_trait = ""
        else:
            session.last_answer_trait = ""
            session.current_chain_trait = ""
            # Restore initial chain from primary domain
            entry_qs = DOMAIN_ENTRY_QUESTIONS.get(session.primary_domain, [])
            session.chain_queue = [q for q in entry_qs
                                   if q not in session.excluded_question_ids and q in self.questions]
        
        # Rebuild domain_question_count from remaining answered questions
        session.domain_question_count = {}
        session.explored_domains = set()
        for answered_qid in session.answered_questions:
            node = QUESTION_TREE_NODES.get(answered_qid, {})
            for branch in node.get("branches", []):
                session.domain_question_count[branch] = session.domain_question_count.get(branch, 0) + 1
                if session.domain_question_count[branch] >= DOMAIN_MIN_QUESTIONS:
                    session.explored_domains.add(branch)
        
        # Rebuild branch_weights from scratch: profile baseline + remaining answers
        # Start from initial profile-based weights
        profile_ranked = session.profile_seed_traits[:10]
        rebuilt_weights = {}
        for i, trait in enumerate(profile_ranked):
            branch = TRAIT_TO_BRANCH.get(trait, "")
            if branch:
                weight = max(3.0 - i * 0.2, 0.5)
                rebuilt_weights[branch] = rebuilt_weights.get(branch, 0) + weight
        for branch in BRANCH_ADJACENCY.keys():
            if branch not in rebuilt_weights:
                rebuilt_weights[branch] = 0.1
        # Replay remaining answers
        for b in session.branch_history:
            rebuilt_weights[b] = rebuilt_weights.get(b, 0) + 2.0
            for adj in BRANCH_ADJACENCY.get(b, []):
                rebuilt_weights[adj] = rebuilt_weights.get(adj, 0) + 0.5
        session.branch_weights = rebuilt_weights
        
        # Recalculate course scores based on current trait scores
        self._recalculate_all_course_scores(session)
        
        # Recalculate confidence
        session.confidence = self._calculate_confidence(session)
        
        # Get top courses preview - ALWAYS show based on current scores (includes profile bonuses)
        sorted_courses = sorted(
            session.course_scores.items(),
            key=lambda x: x[1],
            reverse=True
        )
        top_courses = [
            {
                "course_name": name,
                "current_score": round(score, 1),
                "traits_matched": len(self.course_traits.get(name, set()) & 
                                    set(session.trait_scores.keys()))
            }
            for name, score in sorted_courses[:5]
        ]
        
        print(f"[PREVIOUS] Went back to Q{previous_question_id}. Round: {session.round_number}, answers: {len(session.answered_questions)}, traits: {len(session.trait_scores)}")
        
        return {
            "status": "continue",
            "session_id": session_id,
            "round": session.round_number,
            "question": question,
            "confidence": round(session.confidence * 100, 1),
            "courses_remaining": len(self.courses),
            "traits_discovered": len(session.trait_scores),
            "top_courses_preview": top_courses,
            "message": "Go back to previous question. Select a different answer."
        }
    
    def _recalculate_all_course_scores(self, session: AdaptiveSession):
        """Recalculate all course scores from scratch based on current trait scores."""
        # Reset to INITIAL base scores (includes GWA, strand, and profile bonuses)
        # This preserves the user's academic profile influence
        session.course_scores = session.initial_course_scores.copy()
        
        # Apply trait-based scoring
        for trait, score in session.trait_scores.items():
            if trait in self.trait_to_courses:
                for course_name in self.trait_to_courses[trait]:
                    session.course_scores[course_name] = session.course_scores.get(course_name, 50.0) + (score * 2)


# Singleton instance (will be initialized by FastAPI)
adaptive_engine: Optional[AdaptiveAssessmentEngine] = None


def initialize_adaptive_engine(courses: List[dict], questions: List[dict]):
    """Initialize the global adaptive engine"""
    global adaptive_engine
    adaptive_engine = AdaptiveAssessmentEngine(courses, questions)
    return adaptive_engine


def get_adaptive_engine() -> Optional[AdaptiveAssessmentEngine]:
    """Get the global adaptive engine instance"""
    return adaptive_engine
