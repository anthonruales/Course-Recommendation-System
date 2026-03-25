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
from services.trait_system import (
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
    course_scores_snapshots: Dict[int, Dict[str, float]] = field(default_factory=dict)  # Snapshot of course_scores BEFORE each answer (for exact reversal)
    
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
    domain_vote_weights: Dict[str, float] = field(default_factory=dict)  # Weighted votes per domain (interests 3×, skills 1×)
    last_answer_trait: str = ""                      # Trait from the most recent answer (drives next question)
    option_fingerprints_seen: Set[tuple] = field(default_factory=set)  # Tracks option-set tuples already shown to prevent duplicate choices

    # --- Profile-Category Matching ---
    profile_categories: Set[str] = field(default_factory=set)     # Question categories matching user's stated interests
    profile_relevant_qids: Set[int] = field(default_factory=set)  # QIDs from profile-matching categories
    category_history: List[str] = field(default_factory=list)     # Recently answered question categories
    current_category_focus: str = ""                            # Dominant category thread (e.g. Fine Arts & Painting)


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
    "programming": ["Software-Dev", "Data-Analytics", "Cyber-Defense", "Web-Dev"],
    "computer": ["Software-Dev", "Hardware-Systems", "Data-Analytics", "Web-Dev", "Cloud-Systems"],
    "data": ["Data-Analytics", "Software-Dev"],
    "ai": ["Software-Dev", "Data-Analytics", "AI-ML"],
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
    "respiratory_therapy": ["Rehab-Therapy", "Patient-Care", "Medical-Lab", "Technical-Skill"],
    "speech_pathology": ["Rehab-Therapy", "Patient-Care", "People-Skill", "Counseling"],
    "radiology": ["Medical-Lab", "Technical-Skill"],
    "optometry": ["Medical-Lab", "Patient-Care", "Technical-Skill"],
    "midwifery": ["Patient-Care", "People-Skill"],
    "public_health": ["Public-Health", "Community-Serve", "People-Skill"],
    "education": ["Teaching-Ed"],
    "law": ["Legal-Practice", "Law-Enforce", "Analytical-Skill"],
    "justice": ["Legal-Practice", "Law-Enforce", "Analytical-Skill"],
    "politics": ["Community-Serve", "Admin-Skill", "Analytical-Skill"],
    "social": ["Community-Serve", "Social-Work", "People-Skill"],
    "history": ["Investigative", "Analytical-Skill", "Community-Serve"],
    "communication": ["Marketing-Sales", "Film-Broadcast", "Digital-Media", "People-Skill"],
    "culture": ["Investigative", "Community-Serve", "Creative-Skill"],
    "journalism": ["Investigative", "Film-Broadcast", "Digital-Media", "Analytical-Skill"],
    "community": ["Community-Serve", "People-Skill", "Social-Work"],
    "philosophy": ["Analytical-Skill", "Investigative", "Teaching-Ed", "Community-Serve", "Philosophy-Path"],
    "ethics": ["Analytical-Skill", "Investigative", "People-Skill", "Legal-Practice", "Philosophy-Path"],
    "criminology": ["Law-Enforce", "Forensic-Sci", "Physical-Skill", "Analytical-Skill"],
    "public_safety": ["Law-Enforce", "Physical-Skill", "Community-Serve", "Analytical-Skill"],
    "early_childhood": ["Teaching-Ed", "People-Skill", "Creative-Skill", "Counseling", "Early-Childhood"],
    "early_childhood_education": ["Teaching-Ed", "People-Skill", "Creative-Skill", "Counseling", "Early-Childhood"],
    "special_education": ["Teaching-Ed", "People-Skill", "Counseling", "Analytical-Skill", "Inclusive-Ed"],
    "special_needs": ["Teaching-Ed", "People-Skill", "Counseling", "Community-Serve", "Inclusive-Ed"],
    "library_science": ["Teaching-Ed", "Admin-Skill", "Investigative", "Analytical-Skill", "Library-Info"],
    "library_information_science": ["Teaching-Ed", "Admin-Skill", "Investigative", "Analytical-Skill", "Library-Info"],
    "public_admin": ["Community-Serve", "Admin-Skill", "People-Skill", "Analytical-Skill"],
    "public_administration": ["Community-Serve", "Admin-Skill", "People-Skill", "Analytical-Skill"],
    "government": ["Community-Serve", "Admin-Skill", "Analytical-Skill"],
    "governance": ["Admin-Skill", "Community-Serve", "Analytical-Skill"],
    "intl_studies": ["Community-Serve", "People-Skill", "Analytical-Skill", "Legal-Practice"],
    "international_studies": ["Community-Serve", "People-Skill", "Analytical-Skill", "Legal-Practice"],
    "diplomacy": ["Community-Serve", "People-Skill", "Analytical-Skill", "Legal-Practice"],
    "sociology": ["Community-Serve", "People-Skill", "Investigative", "Analytical-Skill"],
    "linguistics": ["Teaching-Ed", "People-Skill", "Investigative", "Analytical-Skill"],
    "language": ["Teaching-Ed", "People-Skill", "Investigative", "Analytical-Skill"],
    "languages": ["Teaching-Ed", "People-Skill", "Investigative", "Analytical-Skill"],
    "dev_communication": ["Community-Serve", "People-Skill", "Digital-Media", "Marketing-Sales"],
    "development_communication": ["Community-Serve", "People-Skill", "Digital-Media", "Marketing-Sales"],
    "community_dev": ["Community-Serve", "Social-Work", "People-Skill", "Admin-Skill"],
    "community_development": ["Community-Serve", "Social-Work", "People-Skill", "Admin-Skill"],
    "legal_mgmt": ["Legal-Practice", "Admin-Skill", "Law-Enforce", "Analytical-Skill", "Investigative", "Legal-Mgmt"],
    "legal_management": ["Legal-Practice", "Admin-Skill", "Law-Enforce", "Analytical-Skill", "Investigative", "Legal-Mgmt"],
    "maritime": ["Maritime-Sea", "Mechanical-Design"],
    "aviation": ["Hardware-Systems", "Mechanical-Design"],
    "logistics": ["Industrial-Ops", "Admin-Skill"],
    "marine_transport": ["Maritime-Sea", "Physical-Skill"],
    "biotechnology": ["Lab-Research", "Medical-Lab", "Field-Research"],
    "meteorology": ["Field-Research", "Environmental-Sci", "Lab-Research"],
    "statistics": ["Data-Analytics", "Lab-Research", "Finance-Acct"],
    "food_science": ["Food-Science", "Lab-Research", "Culinary-Arts"],
    "forensic_science": ["Forensic-Sci", "Lab-Research", "Law-Enforce"],
    "env_planning": ["Environmental-Eng", "Environmental-Sci", "Field-Research"],
    "marine_science": ["Field-Research", "Maritime-Sea", "Lab-Research"],
    "sports": ["Physical-Skill", "Rehab-Therapy", "Teaching-Ed", "Sports-Ed"],
    "sport_&_fitness": ["Physical-Skill", "Rehab-Therapy", "Sports-Ed", "Sports-Fitness-Path"],
    "sport_and_fitness": ["Physical-Skill", "Rehab-Therapy", "Sports-Ed", "Sports-Fitness-Path"],
    "sports_fitness": ["Physical-Skill", "Rehab-Therapy", "Sports-Ed", "Sports-Fitness-Path"],
    "sports_and_fitness": ["Physical-Skill", "Rehab-Therapy", "Sports-Ed", "Sports-Fitness-Path"],
    "tourism": ["Hospitality-Svc", "Tourism-Travel"],
    "tourism_hospitality": ["Hospitality-Svc", "Tourism-Travel", "People-Skill", "Tourism-Hospitality-Path"],
    "tourism_&_hospitality": ["Hospitality-Svc", "Tourism-Travel", "People-Skill", "Tourism-Hospitality-Path"],
    "tourism_and_hospitality": ["Hospitality-Svc", "Tourism-Travel", "People-Skill", "Tourism-Hospitality-Path"],
    "food": ["Hospitality-Svc", "Culinary-Arts"],
    "agriculture": ["Agri-Nature", "Field-Research", "Environmental-Sci", "Technical-Skill", "Agriculture-Farming-Path"],
    "veterinary": ["Agri-Nature", "Patient-Care", "Lab-Research"],
    "military": ["Law-Enforce", "Physical-Skill"],
    "military_defense": ["Law-Enforce", "Physical-Skill", "Community-Serve", "Investigative", "Military-Defense"],
    "military_&_defense": ["Law-Enforce", "Physical-Skill", "Community-Serve", "Investigative", "Military-Defense"],
    "military_and_defense": ["Law-Enforce", "Physical-Skill", "Community-Serve", "Investigative", "Military-Defense"],
    "forestry": ["Agri-Nature", "Field-Research", "Environmental-Sci", "Community-Serve", "Forestry-Path"],
    "fisheries": ["Agri-Nature", "Maritime-Sea", "Field-Research", "Environmental-Sci", "Fisheries-Agri-Path"],
    "hotel_mgmt": ["Hospitality-Svc", "Admin-Skill", "People-Skill"],
    "hotel_&_resort_management": ["Hospitality-Svc", "Admin-Skill", "People-Skill", "Tourism-Travel", "Hotel-Resort-Path"],
    "hotel_and_resort_management": ["Hospitality-Svc", "Admin-Skill", "People-Skill", "Tourism-Travel", "Hotel-Resort-Path"],
    "exercise_science": ["Physical-Skill", "Rehab-Therapy", "Sports-Ed"],
    "exercise_&_sports_science": ["Physical-Skill", "Rehab-Therapy", "Sports-Ed", "Investigative", "Exercise-Sci-Path"],
    "exercise_and_sports_science": ["Physical-Skill", "Rehab-Therapy", "Sports-Ed", "Investigative", "Exercise-Sci-Path"],
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
    "acting": ["Performing-Arts", "Creative-Skill", "Visual-Design"],
    "illustration": ["Visual-Design", "Creative-Skill", "Digital-Media"],
    "fashion_design": ["Visual-Design", "Creative-Skill", "Spatial-Design"],
    "animation_skill": ["Animation-3D", "Digital-Media", "Creative-Skill"],
    "interior_styling": ["Spatial-Design", "Visual-Design", "Creative-Skill"],
    "content_creation": ["Digital-Media", "Marketing-Sales", "Creative-Skill"],
    "swimming": ["Physical-Skill", "Maritime-Sea", "Sports-Ed"],
    "animal_handling": ["Agri-Nature", "Patient-Care", "Field-Research"],
    "carpentry": ["Mechanical-Design", "Spatial-Design", "Physical-Skill"],
    "farming": ["Agri-Nature", "Field-Research", "Environmental-Sci", "Technical-Skill", "Agriculture-Farming-Path"],
    "fishing": ["Agri-Nature", "Maritime-Sea", "Field-Research", "Environmental-Sci", "Fisheries-Agri-Path"],
    "sewing": ["Creative-Skill", "Spatial-Design", "Technical-Skill"],
    "coaching": ["Sports-Ed", "Teaching-Ed", "Physical-Skill"],
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
    # Technology interest aliases that the frontend sends as-is
    "computers": ["Software-Dev", "Hardware-Systems", "Data-Analytics", "Web-Dev", "Cloud-Systems"],
    "computers_it": ["Software-Dev", "Hardware-Systems", "Data-Analytics", "Technical-Skill", "Web-Dev", "Cloud-Systems"],
    "computers_&_it": ["Software-Dev", "Hardware-Systems", "Data-Analytics", "Technical-Skill", "Web-Dev", "Cloud-Systems"],
    "ai_&_machine_learning": ["Software-Dev", "Data-Analytics", "Investigative", "AI-ML"],
    "ai_and_machine_learning": ["Software-Dev", "Data-Analytics", "Investigative", "AI-ML"],
    "programming_&_coding": ["Software-Dev", "Data-Analytics", "Cyber-Defense", "Web-Dev"],
    "programming_and_coding": ["Software-Dev", "Data-Analytics", "Cyber-Defense", "Web-Dev"],
    "programming_/_coding": ["Software-Dev", "Data-Analytics", "Cyber-Defense", "Web-Dev"],
}

UNIFIED_PROFILE_TO_TRAITS.update({
    "culinary_&_food_science": ["Food-Science", "Lab-Research", "Nutrition-Diet", "Culinary-Arts", "Food-Science-Path"],
    "culinary_and_food_science": ["Food-Science", "Lab-Research", "Nutrition-Diet", "Culinary-Arts", "Food-Science-Path"],
    "culinary_food_science": ["Food-Science", "Lab-Research", "Nutrition-Diet", "Culinary-Arts", "Food-Science-Path"],
    "agriculture_&_farming": ["Agri-Nature", "Field-Research", "Environmental-Sci", "Technical-Skill", "Agriculture-Farming-Path"],
    "agriculture_and_farming": ["Agri-Nature", "Field-Research", "Environmental-Sci", "Technical-Skill", "Agriculture-Farming-Path"],
    "agriculture_farming": ["Agri-Nature", "Field-Research", "Environmental-Sci", "Technical-Skill", "Agriculture-Farming-Path"],
    "forestry_&_natural_resources": ["Agri-Nature", "Field-Research", "Environmental-Sci", "Community-Serve", "Forestry-Path"],
    "forestry_and_natural_resources": ["Agri-Nature", "Field-Research", "Environmental-Sci", "Community-Serve", "Forestry-Path"],
    "forestry_natural_resources": ["Agri-Nature", "Field-Research", "Environmental-Sci", "Community-Serve", "Forestry-Path"],
    "fisheries_&_agriculture": ["Agri-Nature", "Maritime-Sea", "Field-Research", "Environmental-Sci", "Fisheries-Agri-Path"],
    "fisheries_and_agriculture": ["Agri-Nature", "Maritime-Sea", "Field-Research", "Environmental-Sci", "Fisheries-Agri-Path"],
    "fisheries_agriculture": ["Agri-Nature", "Maritime-Sea", "Field-Research", "Environmental-Sci", "Fisheries-Agri-Path"],
    "veterinary_&_animal_science": ["Agri-Nature", "Patient-Care", "Lab-Research", "Investigative", "Veterinary-Path"],
    "veterinary_and_animal_science": ["Agri-Nature", "Patient-Care", "Lab-Research", "Investigative", "Veterinary-Path"],
    "veterinary_animal_science": ["Agri-Nature", "Patient-Care", "Lab-Research", "Investigative", "Veterinary-Path"],
    "culinary_management": ["Culinary-Arts", "Hospitality-Svc", "Startup-Venture", "Admin-Skill", "Culinary-Mgmt-Path"],
    "technical-vocational_training": ["Teaching-Ed", "Technical-Skill", "Mechanical-Design", "Community-Serve", "TVET-Path"],
    "technical_vocational_training": ["Teaching-Ed", "Technical-Skill", "Mechanical-Design", "Community-Serve", "TVET-Path"],
})


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
    "Aeronautical-Eng": "engineering", "Environmental-Eng": "engineering",
    # Spatial-Design belongs to creative (3D environments, architecture as art, game worlds)
    "Spatial-Design": "creative",
    # Business branch
    "Finance-Acct": "business", "Marketing-Sales": "business",
    "Startup-Venture": "business", "Admin-Skill": "business",
    "HR-Management": "business",
    # Education & Social branch
    "Teaching-Ed": "education", "Counseling": "education",
    "Sports-Ed": "education",
    "Community-Serve": "public_service",
    "Law-Enforce": "public_service", "Legal-Practice": "public_service",
    "Social-Work": "social",
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
    "Investigative": "science", "Realistic": "physical",
    "Artistic": "creative", "Social": "social",
    "Enterprising": "business", "Conventional": "business",
    "Analytical-Skill": "technology",
    # Alternate trait names used in batch questions
    "Business-Mgmt": "business", "Finance-Acctg": "business",
    "Marketing-Ads": "business", "Operations-Logistics": "business",
    "Enterprise": "business", "Leadership": "business",
    "Healthcare-Med": "healthcare", "Psychology-Path": "social",
    "Tech-Tic": "technology", "UI-UX": "technology",
    "Creative-Design": "creative", "Creative-Writing": "creative",
    "Film-Media": "creative", "Cultural-Preservation": "creative",
    "Communication-Media": "creative", "Music-Audio": "creative",
    "Public-Admin": "public_service", "Community-Dev": "public_service",
    "Agri-Fisheries": "agriculture", "Sustainability-Path": "science",
    "Architecture-Path": "engineering", "Engineering-Path": "engineering",
    "Electrical-Electronics": "engineering", "Electronics-Dev": "engineering",
    "Scientific-Research": "science", "Nutrition-Food-Sci": "science",
    "Veterinary-Path": "agriculture",
    "Hotel-Resort-Path": "hospitality", "Culinary-Mgmt-Path": "hospitality",
    "Tourism-Hospitality-Path": "hospitality",
    "Automotive-Tech": "engineering", "Geodetic-Surveying": "engineering",
    "Exercise-Sci-Path": "physical", "Sports-Fitness-Path": "physical",
    "Military-Defense": "physical",
    "Inclusive-Ed": "education", "Early-Childhood": "education",
    "Philosophy-Path": "education", "Library-Info": "education",
    "Special-Ed": "education",
    "Forestry-Path": "agriculture", "Fisheries-Agri-Path": "agriculture",
    "Legal-Mgmt": "public_service", "Law-Enforce": "public_service",
    "Criminology": "public_service", "Intl-Studies": "public_service",
    "TVET-Path": "education",
    "Forensic-Sci": "science", "Food-Science": "science",
    "Rehab-Therapy": "healthcare", "Health-Admin": "healthcare",
    "Patient-Care": "healthcare", "Medical-Lab": "healthcare",
    "Pharmacy": "healthcare", "Public-Health": "healthcare",
    "Nutrition-Diet": "healthcare",
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
    # Maritime expansion
    356: {"level": 1, "weight": 1.7, "branches": ["maritime", "engineering", "hospitality"]},
    357: {"level": 2, "weight": 2.1, "branches": ["maritime", "engineering"]},
    358: {"level": 2, "weight": 2.2, "branches": ["maritime", "engineering"]},
    359: {"level": 2, "weight": 2.1, "branches": ["maritime", "science"]},
    360: {"level": 3, "weight": 2.6, "branches": ["maritime", "physical", "healthcare"]},
    361: {"level": 2, "weight": 2.1, "branches": ["maritime", "business", "engineering"]},
    362: {"level": 2, "weight": 2.2, "branches": ["maritime", "engineering", "technology"]},
    363: {"level": 1, "weight": 1.8, "branches": ["maritime", "physical", "hospitality"]},
    364: {"level": 2, "weight": 2.0, "branches": ["maritime", "hospitality", "science"]},
    365: {"level": 3, "weight": 2.5, "branches": ["maritime", "physical", "science"]},
    366: {"level": 2, "weight": 2.1, "branches": ["maritime", "business", "education"]},
    367: {"level": 2, "weight": 2.2, "branches": ["maritime", "engineering", "business", "hospitality"]},
    # Social expansion (368-383)
    368: {"level": 1, "weight": 1.8, "branches": ["social", "education", "healthcare"]},
    369: {"level": 1, "weight": 1.8, "branches": ["social", "public_service"]},
    370: {"level": 2, "weight": 2.0, "branches": ["social", "education", "healthcare"]},
    371: {"level": 2, "weight": 2.0, "branches": ["social", "public_service", "education"]},
    372: {"level": 2, "weight": 2.0, "branches": ["social", "healthcare", "education"]},
    373: {"level": 2, "weight": 2.0, "branches": ["social", "education"]},
    374: {"level": 2, "weight": 2.1, "branches": ["social", "education", "healthcare"]},
    375: {"level": 2, "weight": 2.1, "branches": ["social", "education", "healthcare"]},
    376: {"level": 2, "weight": 2.1, "branches": ["social", "healthcare"]},
    377: {"level": 2, "weight": 2.0, "branches": ["social", "education"]},
    378: {"level": 2, "weight": 2.1, "branches": ["social", "public_service"]},
    379: {"level": 2, "weight": 2.1, "branches": ["social", "education", "healthcare"]},
    380: {"level": 3, "weight": 2.3, "branches": ["social", "healthcare"]},
    381: {"level": 2, "weight": 2.2, "branches": ["social", "healthcare", "education"]},
    382: {"level": 2, "weight": 2.1, "branches": ["social", "science"]},
    383: {"level": 3, "weight": 2.3, "branches": ["social", "public_service", "education"]},
    # Physical/Sports expansion (384-399)
    384: {"level": 1, "weight": 1.8, "branches": ["physical", "education"]},
    385: {"level": 2, "weight": 2.1, "branches": ["physical", "education", "healthcare"]},
    386: {"level": 2, "weight": 2.1, "branches": ["physical", "science", "healthcare"]},
    387: {"level": 2, "weight": 2.1, "branches": ["physical", "education", "healthcare"]},
    388: {"level": 2, "weight": 2.0, "branches": ["physical", "education"]},
    389: {"level": 2, "weight": 2.0, "branches": ["physical", "education"]},
    390: {"level": 2, "weight": 2.1, "branches": ["physical", "healthcare"]},
    391: {"level": 2, "weight": 2.0, "branches": ["physical", "education"]},
    392: {"level": 2, "weight": 2.1, "branches": ["physical", "education"]},
    393: {"level": 2, "weight": 2.2, "branches": ["physical", "science", "healthcare"]},
    394: {"level": 2, "weight": 2.1, "branches": ["physical", "healthcare"]},
    395: {"level": 2, "weight": 2.0, "branches": ["physical", "education"]},
    396: {"level": 3, "weight": 2.3, "branches": ["physical", "education"]},
    397: {"level": 2, "weight": 2.1, "branches": ["physical", "education"]},
    398: {"level": 2, "weight": 2.1, "branches": ["physical", "education", "healthcare"]},
    399: {"level": 2, "weight": 2.0, "branches": ["physical", "education"]},
    # Agriculture expansion (400-413)
    400: {"level": 1, "weight": 1.8, "branches": ["agriculture", "science", "engineering"]},
    401: {"level": 2, "weight": 2.0, "branches": ["agriculture", "science"]},
    402: {"level": 2, "weight": 2.1, "branches": ["agriculture", "science", "healthcare"]},
    403: {"level": 2, "weight": 2.1, "branches": ["agriculture", "science"]},
    404: {"level": 2, "weight": 2.1, "branches": ["agriculture", "engineering", "science"]},
    405: {"level": 2, "weight": 2.0, "branches": ["agriculture", "physical"]},
    406: {"level": 2, "weight": 2.1, "branches": ["agriculture", "science", "business"]},
    407: {"level": 2, "weight": 2.1, "branches": ["agriculture", "science"]},
    408: {"level": 2, "weight": 2.0, "branches": ["agriculture", "business"]},
    409: {"level": 2, "weight": 2.1, "branches": ["agriculture", "science"]},
    410: {"level": 2, "weight": 2.1, "branches": ["agriculture", "science", "healthcare"]},
    411: {"level": 2, "weight": 2.2, "branches": ["agriculture", "science"]},
    412: {"level": 2, "weight": 2.0, "branches": ["agriculture", "science", "engineering"]},
    413: {"level": 2, "weight": 2.1, "branches": ["agriculture", "engineering"]},
    # Law expansion (414-423)
    414: {"level": 1, "weight": 1.8, "branches": ["law", "public_service"]},
    415: {"level": 2, "weight": 2.1, "branches": ["law", "public_service", "science"]},
    416: {"level": 2, "weight": 2.1, "branches": ["law", "public_service"]},
    417: {"level": 2, "weight": 2.1, "branches": ["law", "public_service"]},
    418: {"level": 2, "weight": 2.1, "branches": ["law", "public_service"]},
    419: {"level": 2, "weight": 2.0, "branches": ["law", "public_service", "social"]},
    420: {"level": 2, "weight": 2.2, "branches": ["law", "science"]},
    421: {"level": 2, "weight": 2.1, "branches": ["law", "public_service", "social"]},
    422: {"level": 2, "weight": 2.2, "branches": ["law", "science"]},
    423: {"level": 2, "weight": 2.0, "branches": ["law", "public_service"]},

    # Gap-fill questions (424-442)
    424: {"branches": ['hospitality', 'creative'], "depth": 2},
    425: {"branches": ['engineering', 'science'], "depth": 2},
    426: {"branches": ['business', 'public_service'], "depth": 2},
    427: {"branches": ['business', 'public_service'], "depth": 2},
    428: {"branches": ['business', 'education'], "depth": 2},
    429: {"branches": ['healthcare', 'public_service'], "depth": 2},
    430: {"branches": ['healthcare', 'business'], "depth": 2},
    431: {"branches": ['healthcare', 'public_service'], "depth": 2},
    432: {"branches": ['technology', 'creative'], "depth": 2},
    433: {"branches": ['technology', 'engineering'], "depth": 2},
    434: {"branches": ['healthcare', 'science'], "depth": 2},
    435: {"branches": ['healthcare', 'science'], "depth": 2},
    436: {"branches": ['healthcare', 'public_service'], "depth": 2},
    437: {"branches": ['healthcare', 'science', 'technology'], "depth": 2},
    438: {"branches": ['hospitality', 'business'], "depth": 2},
    439: {"branches": ['hospitality', 'business', 'creative'], "depth": 2},
    440: {"branches": ['hospitality', 'business'], "depth": 2},
    441: {"branches": ['hospitality', 'creative'], "depth": 2},
    442: {"branches": ['hospitality', 'technology'], "depth": 2},

    443: {"level": 2, "weight": 1.5, "branches": ['maritime']},
    444: {"level": 2, "weight": 1.5, "branches": ['maritime']},
    445: {"level": 2, "weight": 1.5, "branches": ['maritime', 'physical']},
    446: {"level": 2, "weight": 1.5, "branches": ['maritime', 'technology']},
    447: {"level": 2, "weight": 1.5, "branches": ['maritime']},
    448: {"level": 2, "weight": 1.5, "branches": ['maritime', 'law']},
    449: {"level": 2, "weight": 1.5, "branches": ['maritime', 'engineering']},
    450: {"level": 2, "weight": 1.5, "branches": ['maritime']},
    451: {"level": 2, "weight": 1.5, "branches": ['maritime']},
    452: {"level": 2, "weight": 1.5, "branches": ['maritime', 'technology']},
    453: {"level": 2, "weight": 1.5, "branches": ['maritime', 'business']},
    454: {"level": 2, "weight": 1.5, "branches": ['maritime', 'law']},
    455: {"level": 2, "weight": 1.5, "branches": ['maritime', 'science']},
    456: {"level": 2, "weight": 1.5, "branches": ['maritime']},

    457: {"level": 2, "weight": 1.5, "branches": ['healthcare']},
    458: {"level": 2, "weight": 1.5, "branches": ['healthcare', 'technology']},
    459: {"level": 2, "weight": 1.5, "branches": ['healthcare', 'social']},
    460: {"level": 2, "weight": 1.5, "branches": ['healthcare']},
    461: {"level": 2, "weight": 1.5, "branches": ['healthcare']},
    462: {"level": 2, "weight": 1.5, "branches": ['healthcare']},
    463: {"level": 2, "weight": 1.5, "branches": ['healthcare', 'technology']},
    464: {"level": 2, "weight": 1.5, "branches": ['healthcare']},
    465: {"level": 2, "weight": 1.5, "branches": ['healthcare']},
    466: {"level": 2, "weight": 1.5, "branches": ['healthcare']},
    467: {"level": 2, "weight": 1.5, "branches": ['healthcare']},
    468: {"level": 2, "weight": 1.5, "branches": ['healthcare', 'science']},
    469: {"level": 2, "weight": 1.5, "branches": ['healthcare']},
    470: {"level": 2, "weight": 1.5, "branches": ['healthcare']},
    471: {"level": 2, "weight": 1.5, "branches": ['healthcare']},
    472: {"level": 2, "weight": 1.5, "branches": ['healthcare']},
    473: {"level": 2, "weight": 1.5, "branches": ['healthcare']},
    474: {"level": 2, "weight": 1.5, "branches": ['healthcare']},
    475: {"level": 2, "weight": 1.5, "branches": ['healthcare', 'science']},
    476: {"level": 2, "weight": 1.5, "branches": ['healthcare']},
    477: {"level": 2, "weight": 1.5, "branches": ['healthcare']},
    478: {"level": 2, "weight": 1.5, "branches": ['healthcare']},
    479: {"level": 2, "weight": 1.5, "branches": ['healthcare', 'social']},
    480: {"level": 2, "weight": 1.5, "branches": ['healthcare']},
    481: {"level": 2, "weight": 1.5, "branches": ['healthcare']},
    482: {"level": 2, "weight": 1.5, "branches": ['healthcare']},
    483: {"level": 2, "weight": 1.5, "branches": ['healthcare']},
    484: {"level": 2, "weight": 1.5, "branches": ['healthcare']},
    485: {"level": 2, "weight": 1.5, "branches": ['healthcare', 'science']},
    486: {"level": 2, "weight": 1.5, "branches": ['healthcare']},
    487: {"level": 2, "weight": 1.5, "branches": ['healthcare']},
    488: {"level": 2, "weight": 1.5, "branches": ['healthcare']},
    489: {"level": 2, "weight": 1.5, "branches": ['healthcare']},
    490: {"level": 2, "weight": 1.5, "branches": ['healthcare']},
    491: {"level": 2, "weight": 1.5, "branches": ['healthcare']},
    492: {"level": 2, "weight": 1.5, "branches": ['healthcare']},
    493: {"level": 2, "weight": 1.5, "branches": ['healthcare']},
    494: {"level": 2, "weight": 1.5, "branches": ['healthcare']},
    495: {"level": 2, "weight": 1.5, "branches": ['healthcare']},
    496: {"level": 2, "weight": 1.5, "branches": ['healthcare']},
    497: {"level": 2, "weight": 1.5, "branches": ['healthcare']},
    498: {"level": 2, "weight": 1.5, "branches": ['healthcare']},
    499: {"level": 2, "weight": 1.5, "branches": ['healthcare']},
    500: {"level": 2, "weight": 1.5, "branches": ['healthcare', 'science']},
    501: {"level": 2, "weight": 1.5, "branches": ['healthcare']},
    502: {"level": 2, "weight": 1.5, "branches": ['healthcare']},
    503: {"level": 2, "weight": 1.5, "branches": ['healthcare']},

    504: {"level": 2, "weight": 1.5, "branches": ['technology']},
    505: {"level": 2, "weight": 1.5, "branches": ['technology']},
    506: {"level": 2, "weight": 1.5, "branches": ['technology']},
    507: {"level": 2, "weight": 1.5, "branches": ['technology']},
    508: {"level": 2, "weight": 1.5, "branches": ['technology']},
    509: {"level": 2, "weight": 1.5, "branches": ['technology']},
    510: {"level": 2, "weight": 1.5, "branches": ['technology']},
    511: {"level": 2, "weight": 1.5, "branches": ['technology']},
    512: {"level": 2, "weight": 1.5, "branches": ['technology']},
    513: {"level": 2, "weight": 1.5, "branches": ['technology']},
    514: {"level": 2, "weight": 1.5, "branches": ['technology', 'creative']},
    515: {"level": 2, "weight": 1.5, "branches": ['technology']},
    516: {"level": 2, "weight": 1.5, "branches": ['technology']},
    517: {"level": 2, "weight": 1.5, "branches": ['technology']},
    518: {"level": 2, "weight": 1.5, "branches": ['technology']},
    519: {"level": 2, "weight": 1.5, "branches": ['technology']},
    520: {"level": 2, "weight": 1.5, "branches": ['technology']},
    521: {"level": 2, "weight": 1.5, "branches": ['technology']},
    522: {"level": 2, "weight": 1.5, "branches": ['technology']},
    523: {"level": 2, "weight": 1.5, "branches": ['technology']},
    524: {"level": 2, "weight": 1.5, "branches": ['technology']},
    525: {"level": 2, "weight": 1.5, "branches": ['technology']},
    526: {"level": 2, "weight": 1.5, "branches": ['technology']},
    527: {"level": 2, "weight": 1.5, "branches": ['technology']},
    528: {"level": 2, "weight": 1.5, "branches": ['technology']},
    529: {"level": 2, "weight": 1.5, "branches": ['technology']},
    530: {"level": 2, "weight": 1.5, "branches": ['technology']},
    531: {"level": 2, "weight": 1.5, "branches": ['technology']},
    532: {"level": 2, "weight": 1.5, "branches": ['technology']},
    533: {"level": 2, "weight": 1.5, "branches": ['technology']},
    534: {"level": 2, "weight": 1.5, "branches": ['technology']},
    535: {"level": 2, "weight": 1.5, "branches": ['technology', 'education']},
    536: {"level": 2, "weight": 1.5, "branches": ['technology']},
    537: {"level": 2, "weight": 1.5, "branches": ['technology']},
    538: {"level": 2, "weight": 1.5, "branches": ['technology', 'creative']},
    539: {"level": 2, "weight": 1.5, "branches": ['technology']},
    540: {"level": 2, "weight": 1.5, "branches": ['technology']},
    541: {"level": 2, "weight": 1.5, "branches": ['technology']},
    542: {"level": 2, "weight": 1.5, "branches": ['technology', 'creative']},
    543: {"level": 2, "weight": 1.5, "branches": ['technology']},
    544: {"level": 2, "weight": 1.5, "branches": ['technology']},
    545: {"level": 2, "weight": 1.5, "branches": ['technology']},
    546: {"level": 2, "weight": 1.5, "branches": ['technology']},

    547: {"level": 2, "weight": 1.5, "branches": ['engineering']},
    548: {"level": 2, "weight": 1.5, "branches": ['engineering']},
    549: {"level": 2, "weight": 1.5, "branches": ['engineering', 'public_service']},
    550: {"level": 2, "weight": 1.5, "branches": ['engineering', 'science']},
    551: {"level": 2, "weight": 1.5, "branches": ['engineering', 'technology']},
    552: {"level": 2, "weight": 1.5, "branches": ['engineering']},
    553: {"level": 2, "weight": 1.5, "branches": ['engineering', 'technology']},
    554: {"level": 2, "weight": 1.5, "branches": ['engineering', 'science']},
    555: {"level": 2, "weight": 1.5, "branches": ['engineering']},
    556: {"level": 2, "weight": 1.5, "branches": ['engineering']},
    557: {"level": 2, "weight": 1.5, "branches": ['engineering', 'science']},
    558: {"level": 2, "weight": 1.5, "branches": ['engineering', 'technology']},
    559: {"level": 2, "weight": 1.5, "branches": ['engineering']},
    560: {"level": 2, "weight": 1.5, "branches": ['engineering', 'science']},
    561: {"level": 2, "weight": 1.5, "branches": ['engineering', 'science']},
    562: {"level": 2, "weight": 1.5, "branches": ['engineering', 'public_service']},
    563: {"level": 2, "weight": 1.5, "branches": ['engineering', 'technology']},
    564: {"level": 2, "weight": 1.5, "branches": ['engineering', 'business']},
    565: {"level": 2, "weight": 1.5, "branches": ['engineering', 'technology']},
    566: {"level": 2, "weight": 1.5, "branches": ['engineering', 'business']},
    567: {"level": 2, "weight": 1.5, "branches": ['engineering', 'technology']},
    568: {"level": 2, "weight": 1.5, "branches": ['business']},
    569: {"level": 2, "weight": 1.5, "branches": ['business', 'technology']},
    570: {"level": 2, "weight": 1.5, "branches": ['business']},
    571: {"level": 2, "weight": 1.5, "branches": ['business']},
    572: {"level": 2, "weight": 1.5, "branches": ['business']},
    573: {"level": 2, "weight": 1.5, "branches": ['business', 'technology']},
    574: {"level": 2, "weight": 1.5, "branches": ['business']},
    575: {"level": 2, "weight": 1.5, "branches": ['business']},
    576: {"level": 2, "weight": 1.5, "branches": ['business']},
    577: {"level": 2, "weight": 1.5, "branches": ['business', 'technology']},
    578: {"level": 2, "weight": 1.5, "branches": ['business', 'social']},
    579: {"level": 2, "weight": 1.5, "branches": ['business']},
    580: {"level": 2, "weight": 1.5, "branches": ['business', 'technology']},
    581: {"level": 2, "weight": 1.5, "branches": ['business']},
    582: {"level": 2, "weight": 1.5, "branches": ['business']},
    583: {"level": 2, "weight": 1.5, "branches": ['business']},
    584: {"level": 2, "weight": 1.5, "branches": ['business', 'technology']},
    585: {"level": 2, "weight": 1.5, "branches": ['business']},
    586: {"level": 2, "weight": 1.5, "branches": ['business']},
    587: {"level": 2, "weight": 1.5, "branches": ['creative']},
    588: {"level": 2, "weight": 1.5, "branches": ['creative', 'technology']},
    589: {"level": 2, "weight": 1.5, "branches": ['creative']},
    590: {"level": 2, "weight": 1.5, "branches": ['creative', 'technology']},
    591: {"level": 2, "weight": 1.5, "branches": ['creative', 'technology']},
    592: {"level": 2, "weight": 1.5, "branches": ['creative']},
    593: {"level": 2, "weight": 1.5, "branches": ['creative']},
    594: {"level": 2, "weight": 1.5, "branches": ['creative']},
    595: {"level": 2, "weight": 1.5, "branches": ['creative', 'technology']},
    596: {"level": 2, "weight": 1.5, "branches": ['creative']},
    597: {"level": 2, "weight": 1.5, "branches": ['creative']},
    598: {"level": 2, "weight": 1.5, "branches": ['creative']},
    599: {"level": 2, "weight": 1.5, "branches": ['creative']},
    600: {"level": 2, "weight": 1.5, "branches": ['creative', 'education']},
    601: {"level": 2, "weight": 1.5, "branches": ['creative']},
    602: {"level": 2, "weight": 1.5, "branches": ['creative', 'engineering']},
    603: {"level": 2, "weight": 1.5, "branches": ['creative', 'technology']},
    604: {"level": 2, "weight": 1.5, "branches": ['creative', 'engineering']},
    605: {"level": 2, "weight": 1.5, "branches": ['science']},
    606: {"level": 2, "weight": 1.5, "branches": ['science']},
    607: {"level": 2, "weight": 1.5, "branches": ['science']},
    608: {"level": 2, "weight": 1.5, "branches": ['science']},
    609: {"level": 2, "weight": 1.5, "branches": ['science', 'agriculture']},
    610: {"level": 2, "weight": 1.5, "branches": ['science']},
    611: {"level": 2, "weight": 1.5, "branches": ['science']},
    612: {"level": 2, "weight": 1.5, "branches": ['science']},
    613: {"level": 2, "weight": 1.5, "branches": ['science', 'public_service']},
    614: {"level": 2, "weight": 1.5, "branches": ['science', 'technology']},
    615: {"level": 2, "weight": 1.5, "branches": ['science']},
    616: {"level": 2, "weight": 1.5, "branches": ['science', 'agriculture']},
    617: {"level": 2, "weight": 1.5, "branches": ['science']},
    618: {"level": 2, "weight": 1.5, "branches": ['science', 'law']},
    619: {"level": 2, "weight": 1.5, "branches": ['science', 'law']},
    620: {"level": 2, "weight": 1.5, "branches": ['science']},
    621: {"level": 2, "weight": 1.5, "branches": ['education']},
    622: {"level": 2, "weight": 1.5, "branches": ['education']},
    623: {"level": 2, "weight": 1.5, "branches": ['education', 'public_service']},
    624: {"level": 2, "weight": 1.5, "branches": ['education']},
    625: {"level": 2, "weight": 1.5, "branches": ['public_service', 'social']},
    626: {"level": 2, "weight": 1.5, "branches": ['public_service', 'social']},
    627: {"level": 2, "weight": 1.5, "branches": ['public_service', 'social']},
    628: {"level": 2, "weight": 1.5, "branches": ['social', 'public_service']},
    629: {"level": 2, "weight": 1.5, "branches": ['social', 'public_service']},
    630: {"level": 2, "weight": 1.5, "branches": ['law', 'public_service']},
    631: {"level": 2, "weight": 1.5, "branches": ['law', 'physical']},
    632: {"level": 2, "weight": 1.5, "branches": ['law', 'public_service']},
    633: {"level": 2, "weight": 1.5, "branches": ['law']},
    634: {"level": 2, "weight": 1.5, "branches": ['law']},
    635: {"level": 2, "weight": 1.5, "branches": ['law']},
    636: {"level": 2, "weight": 1.5, "branches": ['hospitality']},
    637: {"level": 2, "weight": 1.5, "branches": ['hospitality']},
    638: {"level": 2, "weight": 1.5, "branches": ['hospitality']},
    639: {"level": 2, "weight": 1.5, "branches": ['hospitality']},
    640: {"level": 2, "weight": 1.5, "branches": ['hospitality', 'business']},
    641: {"level": 2, "weight": 1.5, "branches": ['hospitality', 'public_service']},
    642: {"level": 2, "weight": 1.5, "branches": ['hospitality']},
    643: {"level": 2, "weight": 1.5, "branches": ['hospitality']},
    644: {"level": 2, "weight": 1.5, "branches": ['hospitality']},
    645: {"level": 2, "weight": 1.5, "branches": ['physical', 'education']},
    646: {"level": 2, "weight": 1.5, "branches": ['physical', 'education']},
    647: {"level": 2, "weight": 1.5, "branches": ['agriculture']},
    648: {"level": 2, "weight": 1.5, "branches": ['agriculture', 'public_service']},

    649: {"level": 2, "weight": 1.5, "branches": ['business']},
    650: {"level": 2, "weight": 1.5, "branches": ['business']},
    651: {"level": 2, "weight": 1.5, "branches": ['business']},
    652: {"level": 2, "weight": 1.5, "branches": ['business']},
    653: {"level": 2, "weight": 1.5, "branches": ['business']},
    654: {"level": 2, "weight": 1.5, "branches": ['business']},
    655: {"level": 2, "weight": 1.5, "branches": ['business']},
    656: {"level": 2, "weight": 1.5, "branches": ['science', 'technology']},
    657: {"level": 2, "weight": 1.5, "branches": ['science']},
    658: {"level": 2, "weight": 1.5, "branches": ['science']},
    659: {"level": 2, "weight": 1.5, "branches": ['science', 'business']},
    660: {"level": 2, "weight": 1.5, "branches": ['science']},
    661: {"level": 2, "weight": 1.5, "branches": ['science', 'business']},
    662: {"level": 2, "weight": 1.5, "branches": ['science', 'technology']},
    663: {"level": 2, "weight": 1.5, "branches": ['science']},
    664: {"level": 2, "weight": 1.5, "branches": ['creative']},
    665: {"level": 2, "weight": 1.5, "branches": ['creative']},
    666: {"level": 2, "weight": 1.5, "branches": ['creative']},
    667: {"level": 2, "weight": 1.5, "branches": ['creative']},
    668: {"level": 2, "weight": 1.5, "branches": ['creative']},
    669: {"level": 2, "weight": 1.5, "branches": ['creative']},
    670: {"level": 2, "weight": 1.5, "branches": ['creative']},
    671: {"level": 2, "weight": 1.5, "branches": ['technology', 'engineering']},
    672: {"level": 2, "weight": 1.5, "branches": ['technology']},
    673: {"level": 2, "weight": 1.5, "branches": ['technology']},
    674: {"level": 2, "weight": 1.5, "branches": ['technology', 'engineering']},
    675: {"level": 2, "weight": 1.5, "branches": ['technology']},
    676: {"level": 2, "weight": 1.5, "branches": ['technology']},
    677: {"level": 2, "weight": 1.5, "branches": ['technology']},
    678: {"level": 2, "weight": 1.5, "branches": ['social']},
    679: {"level": 2, "weight": 1.5, "branches": ['social', 'business']},
    680: {"level": 2, "weight": 1.5, "branches": ['social']},
    681: {"level": 2, "weight": 1.5, "branches": ['social']},
    682: {"level": 2, "weight": 1.5, "branches": ['social', 'education']},
    683: {"level": 2, "weight": 1.5, "branches": ['physical']},
    684: {"level": 2, "weight": 1.5, "branches": ['physical']},
    685: {"level": 2, "weight": 1.5, "branches": ['physical']},
    686: {"level": 2, "weight": 1.5, "branches": ['physical']},
    687: {"level": 2, "weight": 1.5, "branches": ['technology']},
    688: {"level": 2, "weight": 1.5, "branches": ['technology']},
    689: {"level": 2, "weight": 1.5, "branches": ['technology']},
    690: {"level": 2, "weight": 1.5, "branches": ['technology']},
    691: {"level": 2, "weight": 1.5, "branches": ['technology']},
    692: {"level": 2, "weight": 1.5, "branches": ['technology']},
    693: {"level": 2, "weight": 1.5, "branches": ['technology']},
    694: {"level": 2, "weight": 1.5, "branches": ['technology']},
    695: {"level": 2, "weight": 1.5, "branches": ['technology']},
    696: {"level": 2, "weight": 1.5, "branches": ['technology']},
    697: {"level": 2, "weight": 1.5, "branches": ['technology']},
    698: {"level": 2, "weight": 1.5, "branches": ['technology', 'engineering']},
    699: {"level": 2, "weight": 1.5, "branches": ['technology']},
    700: {"level": 2, "weight": 1.5, "branches": ['creative']},
    701: {"level": 2, "weight": 1.5, "branches": ['creative']},
    702: {"level": 2, "weight": 1.5, "branches": ['creative']},
    703: {"level": 2, "weight": 1.5, "branches": ['creative']},
    704: {"level": 2, "weight": 1.5, "branches": ['public_service']},
    705: {"level": 2, "weight": 1.5, "branches": ['public_service', 'social']},
    706: {"level": 2, "weight": 1.5, "branches": ['public_service']},
    707: {"level": 2, "weight": 1.5, "branches": ['public_service', 'social']},
    708: {"level": 2, "weight": 1.5, "branches": ['creative']},
    709: {"level": 2, "weight": 1.5, "branches": ['creative']},
    710: {"level": 2, "weight": 1.5, "branches": ['creative']},
    711: {"level": 2, "weight": 1.5, "branches": ['creative', 'business']},
    712: {"level": 2, "weight": 1.5, "branches": ['engineering']},
    713: {"level": 2, "weight": 1.5, "branches": ['engineering']},
    714: {"level": 2, "weight": 1.5, "branches": ['engineering', 'technology']},
    715: {"level": 2, "weight": 1.5, "branches": ['engineering']},
    716: {"level": 2, "weight": 1.5, "branches": ['engineering']},
    717: {"level": 2, "weight": 1.5, "branches": ['engineering']},
    718: {"level": 2, "weight": 1.5, "branches": ['engineering', 'technology']},
    719: {"level": 2, "weight": 1.5, "branches": ['engineering']},
    720: {"level": 2, "weight": 1.5, "branches": ['science']},
    721: {"level": 2, "weight": 1.5, "branches": ['science']},
    722: {"level": 2, "weight": 1.5, "branches": ['science']},
    723: {"level": 2, "weight": 1.5, "branches": ['science']},
    724: {"level": 2, "weight": 1.5, "branches": ['science']},
    725: {"level": 2, "weight": 1.5, "branches": ['science']},
    726: {"level": 2, "weight": 1.5, "branches": ['science']},
    727: {"level": 2, "weight": 1.5, "branches": ['science']},
    728: {"level": 2, "weight": 1.5, "branches": ['creative']},
    729: {"level": 2, "weight": 1.5, "branches": ['creative', 'technology']},
    730: {"level": 2, "weight": 1.5, "branches": ['creative']},
    731: {"level": 2, "weight": 1.5, "branches": ['creative']},
    732: {"level": 2, "weight": 1.5, "branches": ['science']},
    733: {"level": 2, "weight": 1.5, "branches": ['science']},
    734: {"level": 2, "weight": 1.5, "branches": ['science']},
    735: {"level": 2, "weight": 1.5, "branches": ['science']},
    736: {"level": 2, "weight": 1.5, "branches": ['hospitality']},
    737: {"level": 2, "weight": 1.5, "branches": ['hospitality']},
    738: {"level": 2, "weight": 1.5, "branches": ['hospitality']},
    739: {"level": 2, "weight": 1.5, "branches": ['hospitality']},
    740: {"level": 2, "weight": 1.5, "branches": ['engineering']},
    741: {"level": 2, "weight": 1.5, "branches": ['engineering']},
    742: {"level": 2, "weight": 1.5, "branches": ['engineering', 'business']},
    743: {"level": 2, "weight": 1.5, "branches": ['science']},
    744: {"level": 2, "weight": 1.5, "branches": ['science']},
    745: {"level": 2, "weight": 1.5, "branches": ['science']},
    746: {"level": 2, "weight": 1.5, "branches": ['business']},
    747: {"level": 2, "weight": 1.5, "branches": ['business']},
    748: {"level": 2, "weight": 1.5, "branches": ['business']},
    749: {"level": 2, "weight": 1.5, "branches": ['business']},
    750: {"level": 2, "weight": 1.5, "branches": ['engineering']},
    751: {"level": 2, "weight": 1.5, "branches": ['engineering']},
    752: {"level": 2, "weight": 1.5, "branches": ['engineering']},
    753: {"level": 2, "weight": 1.5, "branches": ['engineering']},
    754: {"level": 2, "weight": 1.5, "branches": ['creative']},
    755: {"level": 2, "weight": 1.5, "branches": ['creative']},
    756: {"level": 2, "weight": 1.5, "branches": ['creative']},
    757: {"level": 2, "weight": 1.5, "branches": ['creative']},
    758: {"level": 2, "weight": 1.5, "branches": ['creative']},
    759: {"level": 2, "weight": 1.5, "branches": ['creative']},
    760: {"level": 2, "weight": 1.5, "branches": ['creative']},
    761: {"level": 2, "weight": 1.5, "branches": ['creative', 'engineering']},
    762: {"level": 2, "weight": 1.5, "branches": ['business']},
    763: {"level": 2, "weight": 1.5, "branches": ['business']},
    764: {"level": 2, "weight": 1.5, "branches": ['business']},
    765: {"level": 2, "weight": 1.5, "branches": ['education']},
    766: {"level": 2, "weight": 1.5, "branches": ['education']},
    767: {"level": 2, "weight": 1.5, "branches": ['education']},
    768: {"level": 2, "weight": 1.5, "branches": ['education']},
    769: {"level": 2, "weight": 1.5, "branches": ['creative']},
    770: {"level": 2, "weight": 1.5, "branches": ['creative']},
    771: {"level": 2, "weight": 1.5, "branches": ['creative']},
    772: {"level": 2, "weight": 1.5, "branches": ['healthcare']},
    773: {"level": 2, "weight": 1.5, "branches": ['healthcare', 'science']},
    774: {"level": 2, "weight": 1.5, "branches": ['healthcare']},
    775: {"level": 2, "weight": 1.5, "branches": ['science', 'public_service']},
    776: {"level": 2, "weight": 1.5, "branches": ['science', 'public_service']},
    777: {"level": 2, "weight": 1.5, "branches": ['public_service']},
    778: {"level": 2, "weight": 1.5, "branches": ['public_service']},

    # ===== DECISION TREE QUESTIONS (Weight 0.8-0.9) =====
    # These are domain-specific branching questions (Q1001–Q1910).
    # Lower weight than broad questions to prevent a single domain-branch
    # answer from over-riding an established preference pattern.

    # Technology domain root + sub-branches
    1001: {"level": 1, "weight": 0.9, "branches": ["technology"]},                          # Tech root — which area?
    1002: {"level": 1, "weight": 0.8, "branches": ["technology"]},                          # Software sub-branch
    1003: {"level": 1, "weight": 0.8, "branches": ["technology"]},                          # Hardware/networks
    1004: {"level": 1, "weight": 0.8, "branches": ["technology", "science"]},               # Data sub-branch
    1005: {"level": 1, "weight": 0.8, "branches": ["technology", "public_service"]},        # Cybersecurity
    1006: {"level": 1, "weight": 0.8, "branches": ["technology", "creative"]},              # Digital media
    1007: {"level": 1, "weight": 0.8, "branches": ["technology", "creative"]},              # Game dev
    1008: {"level": 1, "weight": 0.8, "branches": ["technology"]},                          # Deep programming
    1009: {"level": 1, "weight": 0.8, "branches": ["technology"]},                          # Web dev deeper
    1010: {"level": 1, "weight": 0.8, "branches": ["technology", "creative"]},              # Creative tech env

    # Healthcare domain root + sub-branches
    1101: {"level": 1, "weight": 0.9, "branches": ["healthcare"]},                          # Healthcare root
    1102: {"level": 1, "weight": 0.8, "branches": ["healthcare"]},                          # Patient care
    1103: {"level": 1, "weight": 0.8, "branches": ["healthcare", "science"]},               # Medical lab
    1104: {"level": 1, "weight": 0.8, "branches": ["healthcare"]},                          # Therapy/rehab
    1105: {"level": 1, "weight": 0.8, "branches": ["healthcare", "science"]},               # Pharmacy
    1106: {"level": 1, "weight": 0.8, "branches": ["healthcare", "business"]},              # Health admin

    # Engineering domain root + sub-branches
    1201: {"level": 1, "weight": 0.9, "branches": ["engineering"]},                         # Engineering root
    1202: {"level": 1, "weight": 0.8, "branches": ["engineering", "science"]},              # Civil engineering
    1203: {"level": 1, "weight": 0.8, "branches": ["engineering"]},                         # Mechanical engineering
    1204: {"level": 1, "weight": 0.8, "branches": ["engineering", "creative"]},             # Architecture/design

    # Business domain root + sub-branches
    1301: {"level": 1, "weight": 0.9, "branches": ["business"]},                            # Business root
    1302: {"level": 1, "weight": 0.8, "branches": ["business"]},                            # Finance sub-branch

    # Arts domain root + sub-branches
    1401: {"level": 1, "weight": 0.9, "branches": ["creative"]},                            # Arts root
    1402: {"level": 1, "weight": 0.8, "branches": ["creative"]},                            # Visual arts
    1403: {"level": 1, "weight": 0.8, "branches": ["creative", "technology"]},              # Digital arts
    1404: {"level": 1, "weight": 0.8, "branches": ["creative"]},                            # Performing arts

    # Education domain root
    1501: {"level": 1, "weight": 0.9, "branches": ["education"]},                           # Education root

    # Science domain root + sub-branches
    1601: {"level": 1, "weight": 0.9, "branches": ["science"]},                             # Science root
    1602: {"level": 1, "weight": 0.8, "branches": ["science", "healthcare"]},               # Biology deeper
    1603: {"level": 1, "weight": 0.8, "branches": ["science"]},                             # Environmental sci

    # Public service domain root + sub-branches
    1701: {"level": 1, "weight": 0.9, "branches": ["public_service"]},                      # Public service root
    1702: {"level": 1, "weight": 0.8, "branches": ["public_service"]},                      # Law enforcement

    # Maritime, Agriculture, Hospitality roots
    1801: {"level": 1, "weight": 0.9, "branches": ["maritime"]},                            # Maritime root
    1802: {"level": 1, "weight": 0.9, "branches": ["agriculture"]},                         # Agriculture root
    1803: {"level": 1, "weight": 0.9, "branches": ["hospitality"]},                         # Hospitality root

    # Validation / cross-cutting questions (lower weight — generic, not domain-specific)
    1901: {"level": 1, "weight": 0.6, "branches": ["technology", "healthcare", "engineering", "business", "creative", "science"]},
    1902: {"level": 1, "weight": 0.6, "branches": ["technology", "science", "creative", "business"]},
    1903: {"level": 1, "weight": 0.6, "branches": ["business", "healthcare", "creative", "public_service"]},
    1904: {"level": 1, "weight": 0.6, "branches": ["technology", "healthcare", "science", "creative"]},
    1905: {"level": 1, "weight": 0.6, "branches": ["technology", "science", "creative", "business"]},
    1906: {"level": 1, "weight": 0.6, "branches": ["technology", "healthcare", "creative", "business"]},
    1907: {"level": 1, "weight": 0.6, "branches": ["technology", "science", "creative", "business", "education"]},
    1908: {"level": 1, "weight": 0.6, "branches": ["technology", "healthcare", "creative", "education"]},
    1909: {"level": 1, "weight": 0.6, "branches": ["technology", "healthcare", "engineering", "business", "creative"]},
    1910: {"level": 1, "weight": 0.6, "branches": ["technology", "healthcare", "engineering", "business", "creative", "science"]},
    # Animation / Game Development questions (Q1139-Q1168)
    1139: {"level": 1, "weight": 0.8, "branches": ["technology", "creative"]},
    1140: {"level": 1, "weight": 0.8, "branches": ["technology", "creative"]},
    1141: {"level": 1, "weight": 0.8, "branches": ["creative", "technology"]},
    1142: {"level": 1, "weight": 0.7, "branches": ["creative", "technology"]},
    1143: {"level": 1, "weight": 0.8, "branches": ["technology", "creative"]},
    1144: {"level": 1, "weight": 0.7, "branches": ["creative", "technology"]},
    1145: {"level": 1, "weight": 0.8, "branches": ["technology", "creative"]},
    1146: {"level": 1, "weight": 0.7, "branches": ["creative", "technology"]},
    1147: {"level": 1, "weight": 0.7, "branches": ["technology", "creative", "business"]},
    1148: {"level": 1, "weight": 0.8, "branches": ["technology", "creative"]},
    1149: {"level": 1, "weight": 0.6, "branches": ["creative", "technology"]},
    1150: {"level": 1, "weight": 0.7, "branches": ["creative", "technology"]},
    1151: {"level": 1, "weight": 0.8, "branches": ["creative", "technology"]},
    1152: {"level": 1, "weight": 0.6, "branches": ["creative", "technology"]},
    1153: {"level": 1, "weight": 0.7, "branches": ["creative", "technology"]},
    1154: {"level": 1, "weight": 0.7, "branches": ["creative", "technology"]},
    1155: {"level": 1, "weight": 0.8, "branches": ["technology", "creative"]},
    1156: {"level": 1, "weight": 0.7, "branches": ["creative", "technology"]},
    1157: {"level": 1, "weight": 0.8, "branches": ["technology", "creative"]},
    1158: {"level": 1, "weight": 0.7, "branches": ["creative", "technology", "business"]},
    1159: {"level": 1, "weight": 0.7, "branches": ["technology", "creative", "business"]},
    1160: {"level": 1, "weight": 0.7, "branches": ["technology", "creative", "business"]},
    1161: {"level": 1, "weight": 0.6, "branches": ["creative", "technology"]},
    1162: {"level": 1, "weight": 0.7, "branches": ["creative", "technology"]},
    1163: {"level": 1, "weight": 0.7, "branches": ["technology", "creative"]},
    1164: {"level": 1, "weight": 0.7, "branches": ["creative", "technology"]},
    1165: {"level": 1, "weight": 0.7, "branches": ["technology", "creative"]},
    1166: {"level": 1, "weight": 0.7, "branches": ["technology", "creative"]},
    1167: {"level": 1, "weight": 0.7, "branches": ["technology", "creative", "business"]},
    1168: {"level": 1, "weight": 0.6, "branches": ["creative", "technology"]},
    # ── Arts sub-category expansion: Music & Performance (Q2721-Q2750) ──
    2721: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2722: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2723: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2724: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2725: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2726: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2727: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2728: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2729: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2730: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2731: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2732: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2733: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2734: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2735: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2736: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2737: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2738: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2739: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2740: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2741: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2742: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2743: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2744: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2745: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2746: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2747: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2748: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2749: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2750: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    # ── Arts sub-category expansion: Music Production & Audio (Q2751-Q2780) ──
    2751: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2752: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2753: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2754: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2755: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2756: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2757: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2758: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2759: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2760: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2761: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2762: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2763: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2764: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2765: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2766: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2767: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2768: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2769: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2770: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2771: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2772: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2773: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2774: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2775: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2776: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2777: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2778: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2779: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2780: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    # ── Arts sub-category expansion: Theater & Performing Arts (Q2781-Q2810) ──
    2781: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2782: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2783: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2784: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2785: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2786: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2787: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2788: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2789: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2790: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2791: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2792: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2793: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2794: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2795: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2796: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2797: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2798: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2799: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2800: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2801: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2802: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2803: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2804: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2805: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2806: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2807: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2808: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2809: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2810: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    # ── Arts sub-category expansion: Photography & Visual Arts (Q2811-Q2840) ──
    2811: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2812: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2813: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2814: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2815: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2816: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2817: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2818: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2819: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2820: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2821: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2822: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2823: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2824: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2825: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2826: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2827: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2828: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2829: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2830: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2831: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2832: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2833: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2834: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2835: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2836: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2837: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2838: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2839: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2840: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    # ── Writing & Literature (Q2841-Q2870) ──
    2841: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2842: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2843: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2844: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2845: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2846: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2847: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2848: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2849: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2850: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2851: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2852: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2853: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2854: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2855: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2856: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2857: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2858: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2859: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2860: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2861: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2862: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2863: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2864: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2865: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2866: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2867: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2868: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2869: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2870: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    # ── Animation & Multimedia (Q2871-Q2900) ──
    2871: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2872: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2873: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2874: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2875: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2876: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2877: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2878: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2879: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2880: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2881: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2882: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2883: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2884: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2885: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2886: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2887: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2888: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2889: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2890: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2891: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2892: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2893: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2894: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2895: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2896: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2897: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2898: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2899: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2900: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    # ── Clothing & Textile Technology (Q2901-Q2930) ──
    2901: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2902: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2903: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2904: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2905: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2906: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2907: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2908: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2909: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2910: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2911: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2912: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2913: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2914: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2915: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2916: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2917: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2918: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2919: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2920: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2921: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2922: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2923: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2924: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2925: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2926: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2927: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2928: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2929: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    2930: {"level": 2, "weight": 2.0, "branches": ["creative"]},
    # ── Healthcare expansion: Medicine & Healthcare Q2931-Q2960 ──
    **{qid: {"level": 2, "weight": 2.0, "branches": ["healthcare"]} for qid in range(2931, 2961)},
    # ── Healthcare expansion: Nursing & Patient Care Q2961-Q2990 ──
    **{qid: {"level": 2, "weight": 2.0, "branches": ["healthcare"]} for qid in range(2961, 2991)},
    # ── Healthcare expansion: Psychology & Mental Health Q2991-Q3020 ──
    **{qid: {"level": 2, "weight": 2.0, "branches": ["healthcare"]} for qid in range(2991, 3021)},
    # ── Healthcare expansion: Public Health Q3021-Q3050 ──
    **{qid: {"level": 2, "weight": 2.0, "branches": ["healthcare"]} for qid in range(3021, 3051)},
    # ── Healthcare expansion 2: Pharmacy & Pharmaceutical Science Q3051-Q3080 ──
    **{qid: {"level": 2, "weight": 2.0, "branches": ["healthcare"]} for qid in range(3051, 3081)},
    # ── Healthcare expansion 2: Physical Therapy & Rehabilitation Q3081-Q3110 ──
    **{qid: {"level": 2, "weight": 2.0, "branches": ["healthcare"]} for qid in range(3081, 3111)},
    # ── Healthcare expansion 2: Medical Technology & Lab Science Q3111-Q3140 ──
    **{qid: {"level": 2, "weight": 2.0, "branches": ["healthcare"]} for qid in range(3111, 3141)},
    # ── Healthcare expansion 2: Nutrition & Dietetics Q3141-Q3170 ──
    **{qid: {"level": 2, "weight": 2.0, "branches": ["healthcare"]} for qid in range(3141, 3171)},
    # ── Healthcare expansion 3: Occupational Therapy Q3171-Q3200 ──
    **{qid: {"level": 2, "weight": 2.0, "branches": ["healthcare"]} for qid in range(3171, 3201)},
    # ── Healthcare expansion 3: Respiratory Therapy Q3201-Q3230 ──
    **{qid: {"level": 2, "weight": 2.0, "branches": ["healthcare"]} for qid in range(3201, 3231)},
    # ── Healthcare expansion 3: Speech-Language Pathology Q3231-Q3260 ──
    **{qid: {"level": 2, "weight": 2.0, "branches": ["healthcare"]} for qid in range(3231, 3261)},
    # ── Healthcare expansion 3: Dentistry & Oral Health Q3261-Q3290 ──
    **{qid: {"level": 2, "weight": 2.0, "branches": ["healthcare"]} for qid in range(3261, 3291)},
    # ── Healthcare expansion 4: Radiology & Imaging Q3291-Q3320 ──
    **{qid: {"level": 2, "weight": 2.0, "branches": ["healthcare"]} for qid in range(3291, 3321)},
    # ── Healthcare expansion 4: Optometry & Vision Care Q3321-Q3350 ──
    **{qid: {"level": 2, "weight": 2.0, "branches": ["healthcare"]} for qid in range(3321, 3351)},
    # ── Healthcare expansion 4: Midwifery & Maternal Health Q3351-Q3380 ──
    **{qid: {"level": 2, "weight": 2.0, "branches": ["healthcare"]} for qid in range(3351, 3381)},
    # ── Social expansion 2: Education & Teaching Q3381-Q3410 ──
    **{qid: {"level": 2, "weight": 2.0, "branches": ["social"]} for qid in range(3381, 3411)},
    # ── Social expansion 2: Social Work & Community Q3411-Q3440 ──
    **{qid: {"level": 2, "weight": 2.0, "branches": ["social"]} for qid in range(3411, 3441)},
    # ── Social expansion 2: History & Culture Q3441-Q3470 ──
    **{qid: {"level": 2, "weight": 2.0, "branches": ["social"]} for qid in range(3441, 3471)},
    # ── Social expansion 2: Communication & Journalism Q3471-Q3500 ──
    **{qid: {"level": 2, "weight": 2.0, "branches": ["social"]} for qid in range(3471, 3501)},
    # ── Public service expansion 2: Law & Justice Q3501-Q3530 ──
    **{qid: {"level": 2, "weight": 2.0, "branches": ["public_service", "law"]} for qid in range(3501, 3531)},
    # ── Public service expansion 2: Politics & Government Q3531-Q3560 ──
    **{qid: {"level": 2, "weight": 2.0, "branches": ["public_service"]} for qid in range(3531, 3561)},
    # ── Public service expansion 2: Criminology & Public Safety Q3561-Q3590 ──
    **{qid: {"level": 2, "weight": 2.0, "branches": ["public_service", "law"]} for qid in range(3561, 3591)},
    # ── Public service expansion 2: Public Administration Q3591-Q3620 ──
    **{qid: {"level": 2, "weight": 2.0, "branches": ["public_service"]} for qid in range(3591, 3621)},
    # ── Social/public-service expansion 3: Development Communication Q3621-Q3650 ──
    **{qid: {"level": 2, "weight": 2.0, "branches": ["social"]} for qid in range(3621, 3651)},
    # ── Social/public-service expansion 3: Community Development Q3651-Q3680 ──
    **{qid: {"level": 2, "weight": 2.0, "branches": ["social"]} for qid in range(3651, 3681)},
    # ── Social/public-service expansion 3: Linguistics & Languages Q3681-Q3710 ──
    **{qid: {"level": 2, "weight": 2.0, "branches": ["public_service"]} for qid in range(3681, 3711)},
    # ── Social/public-service expansion 3: Sociology Q3711-Q3740 ──
    **{qid: {"level": 2, "weight": 2.0, "branches": ["social"]} for qid in range(3711, 3741)},
    # ── Social/public-service expansion 3: International Studies & Diplomacy Q3741-Q3770 ──
    **{qid: {"level": 2, "weight": 2.0, "branches": ["public_service"]} for qid in range(3741, 3771)},
    # ── Education/public-service expansion 4: Philosophy & Ethics Q3771-Q3800 ──
    **{qid: {"level": 2, "weight": 2.0, "branches": ["public_service"]} for qid in range(3771, 3801)},
    # ── Education/public-service expansion 4: Special Needs Education Q3801-Q3830 ──
    **{qid: {"level": 2, "weight": 2.0, "branches": ["education"]} for qid in range(3801, 3831)},
    # ── Education/public-service expansion 4: Library & Information Science Q3831-Q3860 ──
    **{qid: {"level": 2, "weight": 2.0, "branches": ["education"]} for qid in range(3831, 3861)},
    # ── Education/public-service expansion 4: Legal Management Q3861-Q3890 ──
    **{qid: {"level": 2, "weight": 2.0, "branches": ["public_service", "law"]} for qid in range(3861, 3891)},
    # ── Education/public-service expansion 4: Early Childhood Education Q3891-Q3920 ──
    **{qid: {"level": 2, "weight": 2.0, "branches": ["education"]} for qid in range(3891, 3921)},
    # ── Physical/hospitality expansion 5: Sports & Fitness Q3921-Q3950 ──
    **{qid: {"level": 2, "weight": 2.0, "branches": ["physical", "education"]} for qid in range(3921, 3951)},
    # ── Physical/hospitality expansion 5: Exercise & Sports Science Q3951-Q3980 ──
    **{qid: {"level": 2, "weight": 2.0, "branches": ["physical", "healthcare"]} for qid in range(3951, 3981)},
    # ── Physical/hospitality expansion 5: Tourism & Hospitality Q3981-Q4010 ──
    **{qid: {"level": 2, "weight": 2.0, "branches": ["hospitality"]} for qid in range(3981, 4011)},
    # ── Physical/hospitality expansion 5: Hotel & Resort Management Q4011-Q4040 ──
    **{qid: {"level": 2, "weight": 2.0, "branches": ["hospitality", "business"]} for qid in range(4011, 4041)},
    # ── Physical/hospitality expansion 5: Military & Defense Q4041-Q4070 ──
    **{qid: {"level": 2, "weight": 2.0, "branches": ["physical", "public_service"]} for qid in range(4041, 4071)},
    # ── Food/veterinary/TVET expansion 6: Culinary & Food Science Q4071-Q4100 ──
    **{qid: {"level": 2, "weight": 2.0, "branches": ["science", "hospitality", "healthcare"]} for qid in range(4071, 4101)},
    # ── Food/veterinary/TVET expansion 6: Veterinary & Animal Science Q4101-Q4130 ──
    **{qid: {"level": 2, "weight": 2.0, "branches": ["agriculture", "healthcare"]} for qid in range(4101, 4131)},
    # ── Food/veterinary/TVET expansion 6: Culinary Management Q4131-Q4160 ──
    **{qid: {"level": 2, "weight": 2.0, "branches": ["hospitality", "business"]} for qid in range(4131, 4161)},
    # ── Food/veterinary/TVET expansion 6: Technical-Vocational Training Q4161-Q4190 ──
    **{qid: {"level": 2, "weight": 2.0, "branches": ["education", "technology"]} for qid in range(4161, 4191)},
    # ── Agriculture/resource expansion 7: Agriculture & Farming Q4191-Q4220 ──
    **{qid: {"level": 2, "weight": 2.0, "branches": ["agriculture", "science", "business"]} for qid in range(4191, 4221)},
    # ── Agriculture/resource expansion 7: Forestry & Natural Resources Q4221-Q4250 ──
    **{qid: {"level": 2, "weight": 2.0, "branches": ["agriculture", "science", "public_service"]} for qid in range(4221, 4251)},
    # ── Agriculture/resource expansion 7: Fisheries & Agriculture Q4251-Q4280 ──
    **{qid: {"level": 2, "weight": 2.0, "branches": ["agriculture", "maritime", "science"]} for qid in range(4251, 4281)},
}


# ==================== CONVERSATION CHAIN: DOMAIN ENTRY QUESTIONS ====================
# When a domain is activated (from profile or answers), these are the FIRST questions
# to ask. Ordered by how well they introduce the domain's sub-areas.
DOMAIN_ENTRY_QUESTIONS = {
    "agriculture": [129, 252, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 161, 187, 51, 40, 29, 66, 37, 1, 2, 3, 34, 38, 41, 42],
    "business": [124, 245, 148, 149, 150, 35, 28, 57, 61, 1, 2, 3, 4, 5, 24, 25, 26, 30, 31, 32, 34, 36, 37, 38, 39, 40, 41, 42, 43, 44],
    "creative": [125, 248, 219, 151, 213, 152, 153, 30, 37, 33, 66, 1, 2, 3, 4, 5, 31, 34, 35, 39, 40, 41, 44, 56, 61, 64, 65, 67, 69, 70],
    "education": [126, 157, 158, 269, 28, 57, 31, 71, 1, 2, 5, 36, 40, 52, 54, 55, 99, 101, 102, 106, 107, 109, 112, 114, 117, 138, 144, 150, 166, 171],
    "engineering": [123, 237, 145, 146, 147, 59, 26, 52, 1, 2, 3, 4, 36, 37, 43, 51, 81, 92, 103, 105, 114, 116, 118, 153, 154, 162, 174, 176, 177, 180],
    "healthcare": [122, 227, 141, 142, 143, 36, 60, 29, 40, 1, 2, 3, 4, 5, 23, 25, 27, 32, 34, 37, 38, 39, 41, 42, 43, 45, 51, 52, 53, 54],
    "hospitality": [131, 223, 224, 163, 164, 51, 53, 63, 34, 1, 3, 44, 54, 64, 82, 85, 87, 93, 98, 100, 101, 105, 106, 112, 115, 118, 148, 155, 165, 170],
    "law": [234, 235, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 275, 159, 160, 127, 236],
    "maritime": [130, 356, 201, 202, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 162, 203, 204, 205, 63, 51, 29, 34, 1, 3],
    "physical": [132, 269, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 29, 66, 37, 64, 34, 90, 103, 144, 153, 169, 183, 360],
    "public_service": [127, 234, 159, 160, 5, 41, 57, 35, 61, 1, 23, 25, 45, 68, 69, 73, 74, 75, 81, 84, 86, 89, 94, 96, 98, 99, 110, 111, 115, 120],
    "science": [128, 253, 154, 155, 156, 60, 31, 76, 33, 4, 26, 27, 32, 37, 38, 39, 40, 58, 59, 66, 68, 70, 71, 72, 77, 78, 80, 83, 85, 88],
    "social": [133, 243, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 28, 57, 45, 79, 80, 24, 27, 31, 37, 42, 43, 55],
    "technology": [121, 220, 134, 135, 136, 266, 56, 37, 1, 31, 2, 3, 4, 5, 23, 24, 26, 30, 32, 33, 38, 39, 45, 54, 59, 62, 65, 69, 70, 71],
}

DOMAIN_ENTRY_QUESTIONS["science"] = [4071, 4072, 4073, 4074, 4075, 4091, 4092, 4093, 4094, 4095] + DOMAIN_ENTRY_QUESTIONS.get("science", [])
DOMAIN_ENTRY_QUESTIONS["agriculture"] = [4101, 4102, 4103, 4104, 4105, 4121, 4122, 4123, 4124, 4125] + DOMAIN_ENTRY_QUESTIONS.get("agriculture", [])
DOMAIN_ENTRY_QUESTIONS["hospitality"] = [4131, 4132, 4133, 4134, 4135, 4151, 4152, 4153, 4154, 4155] + DOMAIN_ENTRY_QUESTIONS.get("hospitality", [])
DOMAIN_ENTRY_QUESTIONS["education"] = [4161, 4162, 4163, 4164, 4165, 4181, 4182, 4183, 4184, 4185] + DOMAIN_ENTRY_QUESTIONS.get("education", [])
DOMAIN_ENTRY_QUESTIONS["technology"] = [4166, 4167, 4168, 4169, 4170] + DOMAIN_ENTRY_QUESTIONS.get("technology", [])
DOMAIN_ENTRY_QUESTIONS["agriculture"] = [4191, 4192, 4193, 4194, 4195, 4211, 4212, 4213, 4214, 4215, 4221, 4222, 4223, 4224, 4225, 4241, 4242, 4243, 4244, 4245, 4251, 4252, 4253, 4254, 4255, 4271, 4272, 4273, 4274, 4275] + DOMAIN_ENTRY_QUESTIONS.get("agriculture", [])

# ==================== CONVERSATION CHAIN: TRAIT FOLLOW-UP MAP ====================
# After a user picks an option with trait X, these are the best follow-up questions.
# The system picks the first unanswered one. When a chain runs out, accumulated
# branch weights determine the next domain to explore.

TRAIT_FOLLOWUP_MAP = {
    "AI-ML": [257, 215, 138, 516, 517, 518, 519, 520, 135, 180, 189, 176, 198, 167, 312, 316, 121, 524, 136, 187, 212, 220, 56, 172, 182, 199, 206, 208, 214, 217, 218, 266, 307, 309, 314, 472, 528, 190, 577, 718, 508, 552, 567, 569, 765],
    "Admin-Skill": [649, 650, 579, 580, 582, 651, 653, 654, 655, 652, 581, 150, 245, 636, 190, 471, 494, 106, 638, 26, 72, 44, 118, 529, 568, 613, 493, 503, 564, 565, 624, 627, 635, 93, 87, 80, 57, 104, 24, 25, 32, 35, 43, 61, 76, 460, 461, 498, 508, 523, 528, 531, 546, 569, 572, 577, 23, 27, 28, 37, 45, 56, 63, 66, 69, 79, 469, 496, 534, 562, 576, 486, 492, 535, 548, 570, 578, 600, 626, 631, 634, 639, 645, 467, 472, 502, 506, 507, 527, 532, 543, 566, 575, 596, 630, 637, 640, 737, 739, 745, 458, 459, 463, 464, 465, 474, 476, 491, 495, 499, 505, 510, 511, 522, 525, 533, 536, 544, 547, 549, 567, 571, 583, 586, 588, 598, 604, 607, 623, 632, 633, 641, 642, 643, 658, 677, 678, 679, 680, 688, 692, 693, 715, 717, 719, 729, 731, 736, 741, 742, 758, 763],
    "Agri-Nature": [252, 647, 648, 129, 402, 410, 409, 401, 407, 413, 161, 411, 400, 403, 405, 404, 412, 408, 406, 187, 92, 66, 29, 609, 113, 114, 90, 98, 119, 51, 53, 2, 3, 519, 584, 611, 617, 684, 470, 499, 500, 563, 612, 698, 718, 750, 752, 475, 477, 561, 602, 616, 642, 643, 716, 723, 734, 762],
    "Analytical-Skill": [656, 658, 663, 657, 660, 661, 662, 271, 659, 128, 571, 246, 142, 156, 194, 567, 517, 568, 509, 133, 195, 524, 550, 585, 619, 159, 554, 146, 490, 505, 518, 564, 172, 147, 124, 467, 507, 527, 190, 168, 471, 484, 504, 547, 565, 635, 751, 108, 171, 492, 606, 463, 488, 521, 540, 553, 573, 582, 127, 181, 498, 510, 545, 548, 608, 694, 741, 145, 158, 177, 173, 179, 469, 477, 478, 493, 514, 523, 552, 570, 583, 586, 615, 621, 630, 634, 744, 80, 76, 468, 530, 651, 655, 669, 692, 770, 97, 139, 465, 500, 531, 533, 535, 558, 569, 576, 581, 596, 605, 631, 756, 766, 56, 460, 501, 522, 542, 555, 579, 601, 622, 624, 126, 458, 466, 485, 520, 528, 557, 560, 645, 697, 740, 742, 746, 768, 461, 473, 487, 495, 497, 513, 526, 538, 551, 559, 562, 572, 575, 577, 587, 593, 597, 599, 602, 607, 614, 617, 623, 626, 632, 633, 640, 646, 653, 654, 664, 665, 676, 689, 690, 696, 713, 714, 732, 738, 748, 753, 763, 771, 747],
    "Animation-3D": [213, 590, 591, 700, 701, 702, 703, 592, 249, 152, 208, 209, 206, 207, 260, 262, 247, 210, 125, 139, 221, 603, 219, 220, 248, 56, 121, 135, 134, 138, 250, 251, 542, 595, 666, 728, 176, 514, 540, 541, 587, 597, 670, 536, 588, 761, 93, 44, 98, 180, 189, 1141, 1142, 1144, 1146, 1150, 1151, 1154, 1156, 1158, 1162, 1164],
    "Civil-Build": [241, 547, 548, 549, 550, 551, 145, 147, 191, 90, 563, 602, 603, 59, 560, 30, 36, 119, 52, 25, 752, 84, 109, 26, 1, 2, 4, 5, 23, 34, 38, 39, 40, 41, 42, 43, 51, 54, 604, 751, 557, 566, 684, 519, 559, 561, 674, 683, 716, 717, 719, 552, 553, 556, 592, 648, 675, 705, 712, 713, 715, 761, 105, 116],
    "Cloud-Systems": [256, 217, 526, 527, 528, 529, 530, 687, 688, 689, 690, 691, 544, 137, 121, 539, 675, 523, 134, 140, 135, 169, 210, 220, 260, 264, 543, 673, 699, 206, 207, 208, 211, 212, 216, 222, 238, 255, 261, 266, 272, 273, 515, 504, 509, 517, 520, 546, 56, 190, 510, 692, 696, 697, 506, 512, 532, 533, 545, 672, 694, 695, 712, 97, 189, 191],
    "Community-Serve": [704, 705, 706, 707, 625, 627, 244, 626, 369, 371, 378, 383, 368, 379, 372, 375, 160, 159, 382, 641, 464, 457, 538, 629, 92, 94, 102, 41, 74, 5, 479, 628, 117, 114, 109, 31, 42, 459, 549, 43, 24, 35, 45, 474, 562, 612, 51, 37, 560, 630, 519, 525, 597, 608, 611, 730, 169, 460, 462, 473, 475, 476, 477, 482, 491, 494, 497, 510, 535, 575, 584, 623, 634, 648, 682, 723, 506, 508, 511, 513, 536, 557, 578, 581, 604, 607, 613, 616, 679, 684, 685, 714, 767, 774, 461, 463, 487, 488, 489, 492, 514, 542, 559, 563, 586, 598, 602, 609, 617, 621, 622, 632, 639, 640, 647, 652, 667, 692, 709, 712, 719, 720, 722, 731, 736, 738, 747, 752, 754, 755, 758, 541, 770],
    "Counseling": [487, 490, 488, 489, 491, 492, 276, 380, 158, 374, 379, 133, 375, 370, 371, 376, 381, 368, 157, 187, 629, 501, 126, 200, 383, 474, 628, 160, 678, 578, 192, 167, 141, 143, 144, 165, 179, 185, 189, 176, 198, 175, 458, 461, 476, 479, 481, 600, 621, 624, 634, 680, 477, 576, 623, 633, 635, 679, 681, 682, 704, 766, 457, 462, 478, 480, 483, 484, 485, 570, 574, 622, 627, 631, 637, 747, 756, 767, 772],
    "Creative-Skill": [664, 665, 666, 667, 668, 669, 670, 186, 248, 219, 151, 152, 599, 139, 153, 587, 195, 590, 594, 596, 642, 30, 588, 597, 93, 194, 600, 602, 771, 44, 591, 593, 172, 179, 59, 271, 540, 601, 173, 69, 133, 488, 589, 604, 703, 75, 26, 572, 758, 88, 94, 98, 77, 90, 511, 514, 592, 759, 766, 45, 103, 124, 595, 622, 640, 657, 760, 516, 541, 542, 583, 644, 701, 730, 553, 555, 615, 621, 639, 682, 700, 708, 728, 746, 748, 770, 477, 486, 503, 505, 508, 509, 513, 522, 538, 574, 575, 579, 585, 586, 598, 603, 608, 609, 617, 624, 636, 643, 653, 662, 676, 679, 702, 711, 735, 754, 755, 767, 768, 66, 725, 616, 1140, 1142, 1149, 1153, 1156, 1161, 1163, 1168, 2721, 2722, 2723, 2724, 2725, 2726, 2727, 2728, 2729, 2730, 2731, 2732, 2733, 2734, 2735, 2736, 2737, 2738, 2739, 2740, 2741, 2742, 2743, 2744, 2745, 2746, 2747, 2748, 2749, 2750, 2751, 2752, 2753, 2754, 2755, 2756, 2757, 2758, 2759, 2760, 2761, 2762, 2763, 2764, 2765, 2766, 2767, 2768, 2769, 2770, 2771, 2772, 2773, 2774, 2775, 2776, 2777, 2778, 2779, 2780, 2781, 2782, 2783, 2784, 2785, 2786, 2787, 2788, 2789, 2790, 2791, 2792, 2793, 2794, 2795, 2796, 2797, 2798, 2799, 2800, 2801, 2802, 2803, 2804, 2805, 2806, 2807, 2808, 2809, 2810, 2811, 2812, 2813, 2814, 2815, 2816, 2817, 2818, 2819, 2820, 2821, 2822, 2823, 2824, 2825, 2826, 2827, 2828, 2829, 2830, 2831, 2832, 2833, 2834, 2835, 2836, 2837, 2838, 2839, 2840],
    "Culinary-Arts": [277, 642, 644, 643, 424, 163, 164, 148, 131, 231, 223, 224, 477, 225, 291, 302, 170, 199, 165, 181, 183, 185, 221, 226, 155, 176, 174, 184, 200, 144, 153, 259, 267, 305, 616, 617, 639, 665, 636, 637, 736, 739],
    "Cyber-Defense": [255, 216, 532, 533, 534, 535, 531, 137, 89, 111, 529, 691, 256, 217, 94, 99, 134, 264, 97, 222, 121, 135, 220, 221, 175, 138, 156, 211, 212, 214, 215, 234, 235, 236, 496, 507, 515, 545, 618, 620, 630, 518, 528, 502, 519, 650, 690, 698, 56, 86, 178],
    "Data-Analytics": [258, 218, 522, 524, 521, 525, 523, 26, 71, 97, 76, 59, 77, 463, 573, 458, 135, 614, 191, 567, 571, 31, 56, 517, 569, 91, 108, 28, 32, 33, 38, 72, 496, 662, 478, 495, 520, 539, 565, 656, 663, 768, 69, 4, 29, 30, 39, 45, 80, 27, 466, 472, 577, 689, 741, 24, 42, 65, 475, 477, 610, 612, 457, 493, 506, 507, 514, 515, 516, 526, 533, 570, 572, 576, 606, 613, 645, 658, 659, 459, 462, 464, 502, 530, 556, 580, 585, 624, 626, 660, 688, 717, 721, 724, 727, 742, 749, 764, 468, 470, 471, 473, 486, 490, 492, 498, 504, 505, 512, 513, 518, 519, 528, 542, 545, 550, 560, 563, 566, 568, 575, 579, 593, 621, 636, 647, 650, 653, 657, 687, 694, 696, 697, 737, 709],
    "Digital-Media": [267, 268, 708, 709, 710, 711, 593, 594, 595, 221, 219, 247, 152, 186, 121, 588, 210, 30, 93, 44, 640, 222, 572, 592, 56, 118, 70, 78, 33, 86, 89, 92, 96, 769, 110, 23, 25, 84, 115, 116, 120, 459, 511, 521, 573, 575, 587, 590, 591, 596, 598, 601, 622, 623, 642, 643, 512, 515, 589, 664, 665, 728, 729, 748, 749, 754, 765, 460, 516, 520, 541, 583, 619, 637, 644, 666, 693, 707, 746, 98, 1143, 1144, 1150, 1158, 1162, 2730, 2746, 2751, 2759, 2760, 2764, 2765, 2769, 2776, 2789, 2808, 2814, 2823, 2826, 2830, 2834],
    "Electrical-Power": [556, 557, 558, 559, 712, 713, 714, 715, 238, 362, 316, 237, 308, 315, 309, 313, 314, 306, 312, 311, 310, 307, 543, 187, 145, 146, 123, 147, 563, 43, 162, 169, 105, 52, 699, 109, 114, 26, 60, 560, 674, 544, 546, 552, 554, 671, 672, 675, 685, 695, 698, 549, 677, 697, 716, 719, 745, 759, 116, 59],
    "Environmental-Eng": [242, 560, 561, 563, 716, 717, 718, 719, 562, 425, 253, 180, 189, 239, 241, 407, 557, 547, 549, 612, 147, 154, 191, 145, 146, 153, 168, 237, 240, 175, 159, 169, 187, 123, 138, 140, 198, 238, 251, 259, 273, 745, 750, 404, 457, 556, 559, 648, 554, 604, 611, 613, 647, 712, 743, 658, 704, 715, 722, 725, 740, 759, 760],
    "Environmental-Sci": [253, 612, 614, 720, 721, 722, 723, 613, 154, 611, 609, 159, 175, 648, 128, 196, 561, 725, 153, 189, 187, 610, 726, 167, 163, 166, 178, 182, 199, 225, 647, 724, 176, 184, 193, 130, 135, 136, 140, 141, 145, 161, 129, 458, 462, 519, 521, 560, 605, 607, 625, 639, 641, 705, 123, 461, 602, 633, 685, 704, 465, 467, 468, 522, 549, 562, 615, 616, 638, 667, 713, 727, 732, 737, 760, 113, 114],
    "Field-Research": [254, 610, 724, 725, 726, 727, 609, 611, 92, 154, 128, 129, 196, 612, 161, 167, 720, 168, 177, 113, 38, 130, 145, 551, 114, 108, 98, 90, 105, 116, 183, 686, 123, 84, 110, 147, 171, 178, 199, 522, 550, 613, 614, 622, 721, 176, 561, 562, 597, 671, 717, 119, 457, 458, 460, 462, 469, 475, 519, 521, 524, 547, 605, 607, 618, 619, 620, 683, 722],
    "Film-Broadcast": [274, 597, 728, 729, 730, 731, 596, 598, 170, 152, 164, 249, 125, 133, 590, 151, 186, 159, 168, 177, 189, 224, 226, 247, 248, 270, 700, 701, 708, 219, 176, 193, 165, 178, 183, 591, 595, 174, 184, 592, 593, 594, 599, 666, 668, 702, 703, 757, 601, 664, 671, 673, 709, 746, 749, 93, 44, 98, 167, 1141, 1144, 1152, 1156, 1162, 2745, 2749, 2758, 2767, 2774, 2789, 2809, 2827],
    "Finance-Acct": [568, 571, 569, 570, 246, 104, 87, 35, 61, 62, 100, 149, 26, 91, 498, 24, 57, 32, 4, 30, 494, 525, 737, 25, 1, 5, 29, 31, 33, 39, 524, 626, 761, 763, 764, 52, 190, 2, 3, 34, 36, 40, 41, 493, 495, 496, 497, 519, 521, 548, 576, 577, 582, 584, 585, 586, 618, 636, 659, 660, 461, 511, 515, 522, 527, 534, 536, 539, 567, 575, 581, 596, 633, 640, 643, 649, 652, 662, 693, 762, 463, 477, 506, 508, 564, 574, 579, 580, 583, 627, 634, 635, 638, 644, 653, 656, 661, 663, 687, 690, 706, 709, 711, 715, 739, 742, 747, 748],
    "Food-Science": [294, 305, 259, 616, 732, 733, 734, 735, 615, 617, 155, 298, 231, 406, 297, 301, 141, 277, 642, 164, 148, 161, 154, 189, 233, 252, 296, 299, 187, 128, 181, 185, 223, 230, 242, 295, 473, 476, 475, 566, 643, 644, 647, 738, 774, 499, 742, 752, 108, 113],
    "Forensic-Sci": [236, 288, 289, 303, 422, 618, 619, 620, 156, 415, 234, 235, 420, 630, 632, 160, 170, 199, 233, 295, 296, 297, 298, 299, 301, 178, 127, 128, 200, 470, 500, 531, 534, 631, 663, 713, 734, 159, 92, 94, 142, 108, 193, 775, 776],
    "Game-Dev": [261, 262, 206, 207, 208, 260, 542, 540, 541, 210, 209, 139, 221, 220, 213, 152, 125, 56, 121, 135, 198, 180, 136, 222, 214, 215, 217, 218, 248, 258, 263, 536, 591, 592, 668, 701, 703, 622, 518, 590, 657, 696, 765, 70, 185, 1139, 1140, 1142, 1143, 1145, 1147, 1148, 1149, 1150, 1152, 1153, 1155, 1157, 1159, 1160, 1161, 1163, 1165, 1166, 1167, 1168],
    "HR-Management": [245, 285, 286, 287, 300, 576, 577, 578, 426, 427, 428, 150, 149, 160, 148, 163, 173, 225, 295, 296, 297, 299, 301, 190, 124, 223, 243, 246, 275, 293, 493, 461, 487, 491, 497, 586, 633, 489, 495, 569, 583, 649, 651, 739, 582, 585, 106, 87, 193],
    "Hardware-Systems": [543, 545, 695, 696, 697, 698, 699, 544, 546, 177, 178, 184, 272, 237, 123, 180, 197, 56, 187, 145, 111, 89, 526, 672, 674, 675, 135, 533, 43, 140, 96, 153, 159, 173, 189, 70, 54, 714, 44, 84, 90, 93, 116, 505, 516, 518, 532, 556, 531, 558, 563, 671, 673, 76, 469, 481, 523, 529, 542, 559, 565, 566, 601, 608, 610, 688, 710, 740, 743, 105],
    "Health-Admin": [282, 283, 284, 493, 494, 496, 497, 498, 495, 429, 431, 430, 230, 106, 227, 295, 296, 298, 188, 143, 141, 142, 297, 299, 301, 107, 122, 144, 231, 232, 280, 506, 521, 56, 492, 604, 693, 774, 463, 476, 482, 503, 584, 628, 712, 758, 95, 57, 61, 80],
    "Hospitality-Svc": [736, 737, 738, 739, 636, 638, 637, 225, 223, 163, 43, 45, 91, 51, 363, 367, 164, 112, 63, 53, 118, 93, 35, 37, 44, 66, 579, 85, 64, 1, 3, 29, 34, 38, 41, 54, 58, 364, 639, 644, 642, 652, 574, 650, 575, 600, 645, 731, 754, 762],
    "Industrial-Ops": [240, 564, 565, 566, 567, 740, 741, 742, 146, 361, 155, 123, 555, 237, 562, 367, 195, 145, 162, 502, 559, 580, 81, 549, 556, 615, 734, 147, 191, 92, 581, 661, 663, 51, 116, 118, 44, 53, 103, 124, 190, 161, 171, 173, 179, 183, 189, 460, 485, 495, 496, 499, 521, 543, 546, 547, 552, 553, 582, 584, 659, 735, 175, 458, 480, 483, 548, 558, 560, 561, 579, 587, 608, 643, 654, 677, 712, 715, 719, 733, 750, 752, 471, 472, 484, 493, 497, 508, 510, 550, 568, 571, 607, 613, 616, 617, 623, 644, 647, 650, 655, 658, 693, 713, 717, 105],
    "Lab-Research": [605, 606, 743, 744, 745, 607, 608, 154, 31, 60, 70, 468, 465, 500, 156, 466, 187, 155, 475, 503, 499, 617, 71, 615, 470, 108, 648, 721, 753, 773, 472, 485, 610, 614, 619, 38, 33, 616, 618, 732, 113, 57, 458, 473, 561, 620, 116, 76, 27, 28, 32, 72, 77, 79, 80, 462, 554, 716, 733, 119, 40, 58, 66, 78, 37, 68, 467, 469, 522, 550, 613, 718, 459, 464, 486, 502, 508, 524, 525, 547, 548, 551, 557, 621, 460, 623, 656, 659, 660, 661, 672, 723, 735, 92, 457, 476, 478, 506, 518, 520, 532, 555, 560, 563, 564, 566, 609, 612, 632, 634, 635, 642, 643, 647, 658, 751, 767],
    "Law-Enforce": [630, 631, 235, 632, 234, 423, 99, 419, 96, 86, 115, 415, 156, 418, 420, 25, 618, 23, 620, 94, 414, 92, 534, 27, 29, 159, 43, 5, 24, 35, 84, 1, 2, 3, 4, 34, 498, 559, 562, 570, 628, 633, 684, 461, 470, 531, 532, 548, 568, 613, 619, 641, 649, 686, 722, 735, 738],
    "Legal-Practice": [275, 634, 635, 416, 417, 414, 633, 421, 418, 420, 159, 419, 127, 184, 415, 150, 154, 158, 162, 166, 234, 461, 493, 498, 175, 193, 190, 174, 176, 155, 570, 629, 133, 499, 503, 531, 576, 578, 586, 652, 459, 523, 568, 581, 625, 658, 659, 705, 471, 496, 497, 529, 560, 571, 582, 617, 619, 620, 624, 626, 627, 628, 691, 707, 713, 717, 722, 734, 761, 160, 92, 94, 96, 86, 777, 778],
    "Maritime-Sea": [202, 205, 203, 455, 443, 444, 445, 446, 448, 451, 452, 454, 447, 449, 450, 356, 357, 359, 456, 201, 204, 360, 364, 363, 366, 367, 453, 365, 162, 63, 361, 685, 29, 27, 720, 51, 34, 90, 85, 39, 64, 1, 2, 3, 35, 40, 632, 612, 638, 647, 724, 725, 549, 609, 611, 683, 686, 718, 722, 723, 481, 646],
    "Marketing-Sales": [572, 573, 574, 746, 747, 748, 749, 575, 28, 124, 149, 186, 155, 164, 91, 594, 87, 112, 223, 589, 104, 65, 62, 53, 521, 592, 595, 163, 246, 148, 139, 160, 171, 179, 189, 191, 226, 586, 711, 769, 4, 30, 55, 56, 190, 587, 661, 513, 525, 583, 588, 593, 598, 637, 640, 498, 538, 580, 643, 648, 660, 665, 668, 670, 680, 709, 739, 763, 85, 459, 503, 512, 514, 516, 524, 542, 585, 616, 626, 638, 639, 641, 655, 678, 681, 701, 703, 707, 728, 764, 770, 501],
    "Mechanical-Design": [239, 552, 554, 555, 750, 751, 752, 753, 553, 358, 146, 310, 306, 312, 307, 308, 311, 123, 147, 309, 237, 145, 367, 313, 90, 485, 52, 566, 185, 191, 105, 59, 119, 25, 674, 85, 162, 200, 547, 550, 481, 548, 549, 556, 557, 563, 672, 116, 486, 516, 545, 561, 564, 605, 615, 657, 660, 671, 673, 676, 695, 697, 698, 714, 718, 740, 743, 84, 760, 362],
    "Medical-Lab": [233, 465, 466, 468, 469, 471, 472, 467, 470, 33, 142, 122, 144, 60, 36, 52, 605, 141, 143, 227, 95, 81, 606, 108, 156, 57, 192, 229, 107, 2, 3, 4, 5, 23, 75, 45, 55, 193, 460, 478, 619, 620, 660, 671, 743, 113, 76, 464, 475, 479, 495, 499, 516, 607, 614, 618, 677, 698, 772, 773, 491],
    "Mobile-Dev": [265, 214, 537, 538, 539, 536, 433, 432, 136, 198, 140, 212, 211, 134, 222, 121, 135, 189, 191, 152, 161, 219, 220, 226, 238, 247, 252, 180, 206, 208, 262, 266, 513, 542, 641, 541, 670, 690, 97, 56],
    "Nutrition-Diet": [474, 479, 477, 772, 773, 774, 473, 475, 478, 476, 231, 394, 259, 294, 155, 616, 297, 301, 141, 386, 144, 143, 188, 166, 187, 227, 229, 230, 232, 270, 295, 122, 148, 169, 243, 265, 269, 277, 457, 615, 645, 735, 175, 184, 200, 462, 705, 732, 734, 459, 643, 566],
    "Patient-Care": [227, 192, 142, 95, 107, 23, 36, 103, 141, 42, 81, 43, 5, 27, 25, 39, 2, 3, 4, 41, 58, 1, 34, 40, 38, 501, 480, 483, 482, 88, 474, 490, 60, 32, 469, 473, 486, 487, 494, 457, 467, 478, 484, 485, 491, 499, 772, 465, 488, 28, 29, 468, 464, 476, 516, 519, 607, 628, 629, 705, 466, 470, 471, 477, 479, 489, 500, 503, 536, 584, 620, 639, 652, 681, 472, 481, 492, 495, 506, 554, 605, 606, 625, 704, 738, 743, 762, 773, 723],
    "People-Skill": [278, 678, 679, 680, 681, 682, 373, 368, 381, 377, 45, 24, 369, 157, 370, 372, 383, 150, 371, 375, 380, 492, 88, 489, 379, 574, 627, 637, 79, 94, 487, 117, 23, 460, 581, 626, 635, 80, 83, 488, 497, 510, 576, 578, 646, 579, 599, 624, 634, 644, 374, 490, 572, 585, 622, 28, 382, 486, 501, 636, 655, 707, 25, 546, 570, 583, 586, 598, 631, 654, 669, 464, 483, 509, 580, 589, 593, 628, 638, 757, 767, 491, 494, 538, 600, 625, 747, 495, 499, 504, 582, 595, 610, 630, 643, 706, 727, 738, 748, 756, 766, 378, 459, 467, 469, 482, 498, 517, 532, 535, 541, 565, 568, 573, 577, 608, 629, 632, 645, 650, 651, 653, 677, 708, 726, 728, 761, 763, 479, 493, 507, 508, 511, 513, 516, 518, 534, 536, 544, 575, 594, 596, 615, 621, 633, 640, 649, 692, 709, 744, 746, 754, 764, 768, 376],
    "Performing-Arts": [250, 599, 754, 755, 756, 757, 600, 601, 151, 125, 195, 164, 152, 139, 178, 179, 209, 248, 270, 593, 184, 168, 172, 173, 182, 199, 207, 208, 219, 249, 262, 268, 274, 488, 540, 597, 594, 595, 596, 598, 602, 664, 666, 667, 683, 710, 728, 731, 585, 635, 669, 680, 702, 708, 759, 744, 44, 30, 66, 93, 176, 1141, 1152, 2721, 2722, 2723, 2724, 2725, 2726, 2727, 2728, 2729, 2730, 2731, 2732, 2733, 2734, 2735, 2736, 2737, 2738, 2739, 2740, 2741, 2742, 2743, 2744, 2745, 2746, 2747, 2748, 2749, 2750, 2751, 2752, 2753, 2754, 2755, 2756, 2757, 2758, 2759, 2760, 2761, 2762, 2763, 2764, 2765, 2766, 2767, 2768, 2769, 2770, 2771, 2772, 2773, 2774, 2775, 2776, 2777, 2778, 2779, 2780, 2781, 2782, 2783, 2784, 2785, 2786, 2787, 2788, 2789, 2790, 2791, 2792, 2793, 2794, 2795, 2796, 2797, 2798, 2799, 2800, 2801, 2802, 2803, 2804, 2805, 2806, 2807, 2808, 2809, 2810],
    "Pharmacy": [279, 280, 281, 228, 501, 500, 502, 499, 435, 503, 434, 436, 437, 295, 296, 297, 299, 301, 605, 141, 142, 143, 188, 144, 227, 230, 122, 233, 236, 289, 303, 461, 462, 470, 566, 607, 743, 200, 606, 618, 465, 616, 733, 107, 95, 60, 155],
    "Physical-Skill": [683, 684, 685, 686, 391, 397, 393, 386, 398, 395, 385, 29, 389, 384, 387, 269, 132, 394, 396, 646, 388, 390, 392, 399, 481, 192, 484, 631, 360, 632, 365, 66, 25, 480, 645, 555, 727, 755, 363, 103, 37, 756, 483, 625, 647, 726, 64, 34, 90, 610, 630, 486, 599, 600, 639, 745, 473, 482, 485, 545, 548, 558, 564, 757, 471, 474, 476, 478, 525, 542, 543, 550, 552, 554, 556, 565, 574, 590, 597, 601, 609, 611, 614, 618, 621, 622, 636, 638, 649, 654, 664, 676, 697, 729, 740, 741, 768],
    "Public-Health": [458, 463, 457, 462, 464, 459, 460, 461, 232, 169, 141, 479, 143, 188, 230, 175, 475, 497, 142, 160, 227, 229, 244, 166, 198, 122, 190, 135, 140, 154, 159, 164, 167, 172, 180, 189, 218, 228, 231, 470, 478, 495, 525, 608, 609, 611, 625, 725, 773, 176, 473, 476, 524, 706, 494, 500, 519, 521, 578, 629, 192],
    "Rehab-Therapy": [484, 480, 481, 482, 483, 485, 486, 229, 390, 88, 94, 95, 387, 188, 141, 122, 176, 132, 103, 143, 227, 295, 269, 107, 36, 113, 110, 99, 144, 84, 96, 163, 223, 158, 115, 491, 554, 645, 494, 623, 629, 29, 564, 600, 636, 641, 646, 736, 750, 45],
    "Social-Work": [292, 293, 304, 243, 628, 629, 376, 378, 160, 383, 175, 374, 380, 379, 381, 368, 375, 372, 370, 166, 127, 489, 296, 297, 299, 301, 487, 133, 159, 169, 157, 193, 182, 627, 704, 462, 464, 584, 597, 625, 680, 681, 479, 482, 491, 575, 623, 626, 633, 634, 730, 731, 176],
    "Software-Dev": [266, 504, 509, 506, 510, 692, 693, 694, 505, 507, 508, 56, 222, 134, 135, 512, 537, 515, 541, 523, 527, 530, 520, 526, 111, 89, 558, 689, 97, 33, 496, 502, 532, 539, 569, 83, 29, 76, 28, 32, 511, 536, 577, 189, 30, 528, 584, 70, 37, 516, 551, 687, 690, 69, 108, 4, 31, 23, 517, 544, 553, 662, 695, 1, 2, 3, 5, 34, 35, 36, 591, 688, 765, 462, 513, 514, 522, 531, 535, 540, 543, 583, 472, 518, 519, 529, 533, 542, 552, 565, 567, 580, 624, 657, 673, 702, 463, 534, 538, 546, 555, 556, 570, 582, 587, 588, 589, 603, 618, 620, 621, 622, 623, 633, 641, 656, 676, 691, 699, 701, 724, 740, 749, 762, 764, 698, 1140, 1143, 1145, 1148, 1155, 1157, 1159],
    "Spatial-Design": [251, 603, 758, 759, 760, 761, 602, 604, 153, 248, 241, 125, 123, 59, 30, 152, 145, 551, 553, 237, 118, 112, 67, 36, 104, 147, 148, 149, 163, 164, 185, 110, 120, 151, 177, 191, 213, 240, 540, 548, 590, 592, 601, 643, 176, 547, 558, 564, 574, 665, 668, 670, 769, 485, 549, 557, 559, 563, 651, 703, 719, 742, 770, 771, 1151, 1153, 1165],
    "Sports-Ed": [646, 645, 392, 269, 132, 388, 270, 384, 389, 399, 396, 387, 183, 398, 385, 394, 393, 395, 390, 391, 386, 684, 397, 157, 144, 166, 169, 153, 158, 683, 686, 193, 176, 126, 473, 474, 476, 480, 482, 483, 525, 621, 685, 774, 772, 481, 484, 536, 639, 682, 698, 710, 187],
    "Startup-Venture": [583, 585, 586, 762, 763, 764, 584, 165, 57, 80, 148, 149, 91, 87, 104, 65, 62, 508, 534, 598, 28, 246, 100, 61, 1, 5, 24, 35, 54, 64, 73, 74, 77, 78, 85, 37, 38, 42, 63, 69, 570, 575, 626, 638, 644, 482, 491, 528, 562, 589, 604, 607, 608, 617, 620, 627, 711, 476, 546, 559, 572, 613, 625, 648, 659, 666, 668, 677, 678, 679, 755, 757, 774],
    "Teaching-Ed": [624, 765, 766, 767, 768, 621, 622, 623, 157, 158, 535, 88, 99, 31, 71, 33, 83, 86, 459, 625, 45, 117, 24, 42, 489, 27, 32, 81, 5, 35, 41, 36, 682, 106, 1, 2, 3, 4, 26, 28, 30, 34, 40, 490, 503, 598, 457, 467, 469, 474, 476, 487, 491, 506, 511, 536, 542, 576, 577, 578, 584, 589, 592, 600, 613, 628, 632, 634, 637, 641, 644, 645, 679, 681, 704, 757, 479, 483, 495, 497, 507, 582, 607, 617, 652, 670, 676, 678, 705, 706, 707, 710, 711, 726, 735, 464, 470, 473, 480, 481, 482, 486, 488, 504, 510, 525, 532, 604, 608, 609, 620, 627, 639, 648, 693, 730, 748, 758, 762, 772, 774],
    "Technical-Skill": [272, 273, 671, 672, 673, 674, 675, 676, 677, 37, 134, 530, 466, 545, 544, 603, 505, 507, 509, 537, 472, 504, 551, 606, 552, 109, 111, 526, 531, 533, 543, 553, 580, 729, 194, 195, 502, 513, 558, 601, 33, 56, 520, 527, 561, 83, 151, 29, 55, 271, 546, 555, 556, 610, 42, 78, 107, 481, 512, 528, 539, 557, 614, 76, 28, 32, 66, 72, 87, 100, 534, 535, 538, 582, 623, 744, 467, 510, 518, 541, 566, 579, 590, 595, 631, 696, 702, 733, 753, 70, 122, 80, 24, 529, 540, 559, 578, 105, 469, 471, 478, 486, 517, 550, 569, 605, 608, 621, 647, 654, 699, 724, 462, 480, 485, 496, 508, 523, 596, 598, 600, 624, 633, 637, 649, 650, 651, 667, 669, 687, 695, 700, 714, 716, 727, 731, 750, 754, 765, 470, 484, 493, 500, 503, 506, 515, 516, 522, 532, 548, 554, 560, 563, 564, 565, 572, 574, 581, 583, 584, 588, 591, 607, 611, 630, 640, 645, 653, 656, 706, 715, 721, 732, 737, 739, 755, 577, 662, 688],
    "Tourism-Travel": [290, 291, 302, 640, 639, 641, 438, 440, 441, 226, 439, 442, 224, 131, 223, 299, 163, 152, 638, 736, 170, 165, 296, 297, 301, 199, 200, 130, 132, 204, 267, 269, 575, 176, 193, 604, 681, 710, 723, 730, 637, 642, 667, 680, 706, 760, 164],
    "Visual-Design": [587, 769, 770, 771, 588, 589, 248, 219, 247, 30, 32, 514, 186, 56, 153, 93, 44, 152, 118, 69, 26, 591, 595, 602, 78, 33, 221, 700, 1, 2, 3, 4, 5, 24, 27, 28, 31, 34, 35, 37, 603, 511, 513, 538, 540, 593, 594, 596, 604, 664, 666, 708, 522, 619, 665, 668, 670, 710, 746, 759, 110, 541, 542, 590, 592, 597, 642, 667, 749, 1139, 1142, 1143, 1146, 1150, 1151, 1165, 2811, 2812, 2813, 2814, 2815, 2816, 2817, 2818, 2819, 2820, 2821, 2822, 2823, 2824, 2825, 2826, 2827, 2828, 2829, 2830, 2831, 2832, 2833, 2834, 2835, 2836, 2837, 2838, 2839, 2840],
    "Web-Dev": [263, 211, 264, 515, 212, 511, 512, 513, 514, 134, 222, 121, 165, 198, 537, 140, 247, 506, 186, 148, 163, 139, 219, 220, 224, 226, 268, 573, 694, 177, 181, 185, 191, 209, 522, 532, 539, 574, 589, 594, 640, 56, 200, 504, 505, 533, 587, 588, 769, 525, 526, 687, 688, 709, 747, 749, 771, 97, 89, 70],
}


def _prepend_unique(existing, new_items, limit=None):
    ordered = []
    seen = set()
    for item in list(new_items) + list(existing):
        if item in seen:
            continue
        seen.add(item)
        ordered.append(item)
    if limit is not None:
        return ordered[:limit]
    return ordered


TRAIT_FOLLOWUP_MAP["Agri-Nature"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Agri-Nature"],
    [4191, 4192, 4193, 4194, 4195, 4201, 4202, 4203, 4204, 4205, 4211, 4212, 4213, 4214, 4215, 4221, 4222, 4223, 4224, 4225, 4231, 4232, 4233, 4234, 4235, 4251, 4252, 4253, 4254, 4255, 4261, 4262, 4263, 4264, 4265, 4271, 4272, 4273, 4274, 4275],
)
TRAIT_FOLLOWUP_MAP["Field-Research"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Field-Research"],
    [4196, 4197, 4198, 4199, 4200, 4221, 4222, 4223, 4224, 4225, 4236, 4237, 4238, 4239, 4240, 4256, 4257, 4258, 4259, 4260],
)
TRAIT_FOLLOWUP_MAP["Environmental-Sci"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Environmental-Sci"],
    [4206, 4207, 4208, 4209, 4210, 4226, 4227, 4228, 4229, 4230, 4246, 4247, 4248, 4249, 4250, 4256, 4257, 4258, 4259, 4260],
)
TRAIT_FOLLOWUP_MAP["Technical-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Technical-Skill"],
    [4206, 4207, 4208, 4209, 4210, 4266, 4267, 4268, 4269, 4270],
)
TRAIT_FOLLOWUP_MAP["Startup-Venture"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Startup-Venture"],
    [4216, 4217, 4218, 4219, 4220],
)
TRAIT_FOLLOWUP_MAP["Community-Serve"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Community-Serve"],
    [4226, 4227, 4228, 4229, 4230, 4241, 4242, 4243, 4244, 4245],
)
TRAIT_FOLLOWUP_MAP["Physical-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Physical-Skill"],
    [4216, 4217, 4218, 4219, 4220, 4246, 4247, 4248, 4249, 4250],
)
TRAIT_FOLLOWUP_MAP["Data-Analytics"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Data-Analytics"],
    [4236, 4237, 4238, 4239, 4240, 4266, 4267, 4268, 4269, 4270],
)
TRAIT_FOLLOWUP_MAP["Maritime-Sea"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Maritime-Sea"],
    [4251, 4252, 4253, 4254, 4255, 4261, 4262, 4263, 4264, 4265, 4271, 4272, 4273, 4274, 4275],
)
TRAIT_FOLLOWUP_MAP["Food-Science"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Food-Science"],
    [4276, 4277, 4278, 4279, 4280],
)


SCIENCE_INTEREST_RESEARCH_QIDS = list(range(1169, 1197))
SCIENCE_BIOLOGY_QIDS = list(range(1197, 1225))
SCIENCE_CHEMISTRY_QIDS = list(range(1225, 1253))
SCIENCE_PHYSICS_QIDS = list(range(1253, 1281))
SCIENCE_ENVIRONMENT_NATURE_QIDS = list(range(1281, 1311))
SCIENCE_EARTH_GEOLOGY_QIDS = list(range(1311, 1341))
SCIENCE_ENV_PLANNING_QIDS = list(range(1341, 1371))
SCIENCE_BIOTECH_GENETICS_QIDS = list(range(1371, 1401))
SCIENCE_WEATHER_ATMOS_QIDS = list(range(1401, 1431))
TECH_PROGRAMMING_QIDS = list(range(1431, 1461))
TECH_COMPUTERS_IT_QIDS = list(range(1461, 1491))
TECH_AI_ML_QIDS = list(range(1491, 1521))
TECH_ROBOTICS_QIDS = list(range(1521, 1551))
TECH_CYBERSECURITY_QIDS = list(range(1551, 1581))
TECH_DATA_ANALYTICS_QIDS = list(range(1581, 1611))
TECH_GAME_DEVELOPMENT_QIDS = list(range(1611, 1641))
TECH_WEB_MOBILE_QIDS = list(range(1641, 1671))
TECH_NETWORKING_QIDS = list(range(1671, 1701))
TECH_SOFTWARE_ENGINEERING_QIDS = list(range(1701, 1731))
TECH_MULTIMEDIA_QIDS = list(range(1731, 1761))
TECH_DATABASE_SYSTEMS_QIDS = list(range(1761, 1791))
TECH_HEALTH_IT_QIDS = list(range(1791, 1821))
ENG_CIVIL_CONSTRUCTION_QIDS = list(range(1821, 1851))
ENG_ARCH_INTERIOR_QIDS = list(range(1851, 1881))
ENG_INDUSTRIAL_MANUFACTURING_QIDS = list(range(1881, 1911))
ENG_LANDSCAPE_ARCH_QIDS = list(range(1911, 1941))
ENG_GENERAL_QIDS = list(range(1941, 1971))
ENG_MECHANICAL_SYSTEMS_QIDS = list(range(1971, 2001))
ENG_ELECTRICAL_ELECTRONICS_QIDS = list(range(2001, 2031))
ENG_AIRCRAFT_AVIONICS_QIDS = list(range(2031, 2061))
ENG_AERONAUTICAL_AEROSPACE_QIDS = list(range(2061, 2091))
ENG_GEODETIC_SURVEYING_QIDS = list(range(2091, 2121))
ENG_PRODUCT_INDUSTRIAL_DESIGN_QIDS = list(range(2121, 2151))
ENG_MARINE_ENGINEERING_QIDS = list(range(2151, 2181))
BUS_ENTREPRENEURSHIP_QIDS = list(range(2181, 2211))
BUS_FINANCE_BANKING_QIDS = list(range(2211, 2241))
BUS_MARKETING_ADVERTISING_QIDS = list(range(2241, 2271))
BUS_MANAGEMENT_ADMIN_QIDS = list(range(2271, 2301))
BUS_ACCOUNTING_QIDS = list(range(2301, 2331))
BUS_ECONOMICS_QIDS = list(range(2331, 2361))
BUS_REAL_ESTATE_PROPERTY_QIDS = list(range(2361, 2391))
BUS_HR_MANAGEMENT_QIDS = list(range(2391, 2421))
BUS_OPERATIONS_SUPPLY_CHAIN_QIDS = list(range(2421, 2451))
BUS_CUSTOMS_INTL_TRADE_QIDS = list(range(2451, 2481))
BUS_AGRIBUSINESS_QIDS = list(range(2481, 2511))
BUS_OFFICE_ADMIN_QIDS = list(range(2511, 2541))
BUS_STARTUP_INNOVATION_QIDS = list(range(2541, 2571))
ARTS_FINE_PAINTING_QIDS = list(range(2571, 2601))
ARTS_FASHION_TEXTILE_QIDS = list(range(2601, 2631))
ARTS_ART_DESIGN_QIDS = list(range(2631, 2661))
ARTS_FILM_MEDIA_QIDS = list(range(2661, 2691))
ARTS_ADVERTISING_GRAPHIC_QIDS = list(range(2691, 2721))
SCIENCE_INTEREST_EXPANSION_QIDS = (
    SCIENCE_INTEREST_RESEARCH_QIDS
    + SCIENCE_BIOLOGY_QIDS
    + SCIENCE_CHEMISTRY_QIDS
    + SCIENCE_PHYSICS_QIDS
    + SCIENCE_ENVIRONMENT_NATURE_QIDS
    + SCIENCE_EARTH_GEOLOGY_QIDS
    + SCIENCE_ENV_PLANNING_QIDS
    + SCIENCE_BIOTECH_GENETICS_QIDS
    + SCIENCE_WEATHER_ATMOS_QIDS
)
TECH_INTEREST_EXPANSION_QIDS = (
    TECH_PROGRAMMING_QIDS
    + TECH_COMPUTERS_IT_QIDS
    + TECH_AI_ML_QIDS
    + TECH_ROBOTICS_QIDS
    + TECH_CYBERSECURITY_QIDS
)
TECH_SPECIALIZATION_EXPANSION_QIDS = (
    TECH_DATA_ANALYTICS_QIDS
    + TECH_GAME_DEVELOPMENT_QIDS
    + TECH_WEB_MOBILE_QIDS
    + TECH_NETWORKING_QIDS
    + TECH_SOFTWARE_ENGINEERING_QIDS
)
TECH_INFORMATION_EXPANSION_QIDS = (
    TECH_MULTIMEDIA_QIDS
    + TECH_DATABASE_SYSTEMS_QIDS
    + TECH_HEALTH_IT_QIDS
)
ENGINEERING_INTEREST_EXPANSION_QIDS = (
    ENG_CIVIL_CONSTRUCTION_QIDS
    + ENG_ARCH_INTERIOR_QIDS
    + ENG_INDUSTRIAL_MANUFACTURING_QIDS
    + ENG_LANDSCAPE_ARCH_QIDS
)
ENGINEERING_SYSTEMS_EXPANSION_QIDS = (
    ENG_GENERAL_QIDS
    + ENG_MECHANICAL_SYSTEMS_QIDS
    + ENG_ELECTRICAL_ELECTRONICS_QIDS
    + ENG_AIRCRAFT_AVIONICS_QIDS
)
ENGINEERING_SPECIALTY_EXPANSION_QIDS = (
    ENG_AERONAUTICAL_AEROSPACE_QIDS
    + ENG_GEODETIC_SURVEYING_QIDS
    + ENG_PRODUCT_INDUSTRIAL_DESIGN_QIDS
    + ENG_MARINE_ENGINEERING_QIDS
)
BUSINESS_INTEREST_EXPANSION_QIDS = (
    BUS_ENTREPRENEURSHIP_QIDS
    + BUS_FINANCE_BANKING_QIDS
    + BUS_MARKETING_ADVERTISING_QIDS
    + BUS_MANAGEMENT_ADMIN_QIDS
)
BUSINESS_SPECIALTY_EXPANSION_QIDS = (
    BUS_ACCOUNTING_QIDS
    + BUS_ECONOMICS_QIDS
    + BUS_REAL_ESTATE_PROPERTY_QIDS
    + BUS_HR_MANAGEMENT_QIDS
)
BUSINESS_APPLIED_EXPANSION_QIDS = (
    BUS_OPERATIONS_SUPPLY_CHAIN_QIDS
    + BUS_CUSTOMS_INTL_TRADE_QIDS
    + BUS_AGRIBUSINESS_QIDS
    + BUS_OFFICE_ADMIN_QIDS
    + BUS_STARTUP_INNOVATION_QIDS
)
ARTS_EXPANSION_QIDS = (
    ARTS_FINE_PAINTING_QIDS
    + ARTS_FASHION_TEXTILE_QIDS
    + ARTS_ART_DESIGN_QIDS
    + ARTS_FILM_MEDIA_QIDS
    + ARTS_ADVERTISING_GRAPHIC_QIDS
)

for qid in SCIENCE_INTEREST_EXPANSION_QIDS:
    if qid in SCIENCE_INTEREST_RESEARCH_QIDS:
        QUESTION_TREE_NODES[qid] = {"level": 1, "weight": 1.6, "branches": ["science"]}
    elif qid in SCIENCE_BIOLOGY_QIDS:
        QUESTION_TREE_NODES[qid] = {"level": 1, "weight": 1.6, "branches": ["science", "healthcare", "agriculture"]}
    elif qid in SCIENCE_CHEMISTRY_QIDS:
        QUESTION_TREE_NODES[qid] = {"level": 1, "weight": 1.6, "branches": ["science", "healthcare", "engineering"]}
    elif qid in SCIENCE_PHYSICS_QIDS:
        QUESTION_TREE_NODES[qid] = {"level": 1, "weight": 1.6, "branches": ["science", "engineering", "technology"]}
    elif qid in SCIENCE_ENVIRONMENT_NATURE_QIDS:
        QUESTION_TREE_NODES[qid] = {"level": 1, "weight": 1.6, "branches": ["science", "agriculture"]}
    elif qid in SCIENCE_EARTH_GEOLOGY_QIDS:
        QUESTION_TREE_NODES[qid] = {"level": 1, "weight": 1.6, "branches": ["science", "engineering", "agriculture"]}
    elif qid in SCIENCE_ENV_PLANNING_QIDS:
        QUESTION_TREE_NODES[qid] = {"level": 1, "weight": 1.6, "branches": ["science", "engineering", "business"]}
    elif qid in SCIENCE_BIOTECH_GENETICS_QIDS:
        QUESTION_TREE_NODES[qid] = {"level": 1, "weight": 1.6, "branches": ["science", "healthcare", "agriculture"]}
    else:
        QUESTION_TREE_NODES[qid] = {"level": 1, "weight": 1.6, "branches": ["science", "technology", "agriculture"]}

for qid in TECH_INTEREST_EXPANSION_QIDS:
    if qid in TECH_PROGRAMMING_QIDS:
        QUESTION_TREE_NODES[qid] = {"level": 1, "weight": 1.6, "branches": ["technology"]}
    elif qid in TECH_COMPUTERS_IT_QIDS:
        QUESTION_TREE_NODES[qid] = {"level": 1, "weight": 1.6, "branches": ["technology", "business"]}
    elif qid in TECH_AI_ML_QIDS:
        QUESTION_TREE_NODES[qid] = {"level": 1, "weight": 1.6, "branches": ["technology", "science"]}
    elif qid in TECH_ROBOTICS_QIDS:
        QUESTION_TREE_NODES[qid] = {"level": 1, "weight": 1.6, "branches": ["technology", "engineering"]}
    else:
        QUESTION_TREE_NODES[qid] = {"level": 1, "weight": 1.6, "branches": ["technology", "public_service", "business"]}

for qid in TECH_SPECIALIZATION_EXPANSION_QIDS:
    if qid in TECH_DATA_ANALYTICS_QIDS:
        QUESTION_TREE_NODES[qid] = {"level": 1, "weight": 1.6, "branches": ["technology", "business", "science"]}
    elif qid in TECH_GAME_DEVELOPMENT_QIDS:
        QUESTION_TREE_NODES[qid] = {"level": 1, "weight": 1.6, "branches": ["technology", "creative"]}
    elif qid in TECH_WEB_MOBILE_QIDS:
        QUESTION_TREE_NODES[qid] = {"level": 1, "weight": 1.6, "branches": ["technology", "business", "creative"]}
    elif qid in TECH_NETWORKING_QIDS:
        QUESTION_TREE_NODES[qid] = {"level": 1, "weight": 1.6, "branches": ["technology", "public_service", "business"]}
    else:
        QUESTION_TREE_NODES[qid] = {"level": 1, "weight": 1.6, "branches": ["technology", "business"]}

for qid in TECH_INFORMATION_EXPANSION_QIDS:
    if qid in TECH_MULTIMEDIA_QIDS:
        QUESTION_TREE_NODES[qid] = {"level": 1, "weight": 1.6, "branches": ["technology", "creative"]}
    elif qid in TECH_DATABASE_SYSTEMS_QIDS:
        QUESTION_TREE_NODES[qid] = {"level": 1, "weight": 1.6, "branches": ["technology", "business"]}
    else:
        QUESTION_TREE_NODES[qid] = {"level": 1, "weight": 1.6, "branches": ["technology", "healthcare", "business"]}

for qid in ENGINEERING_INTEREST_EXPANSION_QIDS:
    if qid in ENG_CIVIL_CONSTRUCTION_QIDS:
        QUESTION_TREE_NODES[qid] = {"level": 1, "weight": 1.6, "branches": ["engineering", "public_service"]}
    elif qid in ENG_ARCH_INTERIOR_QIDS:
        QUESTION_TREE_NODES[qid] = {"level": 1, "weight": 1.6, "branches": ["engineering", "creative"]}
    elif qid in ENG_INDUSTRIAL_MANUFACTURING_QIDS:
        QUESTION_TREE_NODES[qid] = {"level": 1, "weight": 1.6, "branches": ["engineering", "business"]}
    else:
        QUESTION_TREE_NODES[qid] = {"level": 1, "weight": 1.6, "branches": ["engineering", "creative", "agriculture"]}

for qid in ENGINEERING_SYSTEMS_EXPANSION_QIDS:
    if qid in ENG_GENERAL_QIDS:
        QUESTION_TREE_NODES[qid] = {"level": 1, "weight": 1.6, "branches": ["engineering"]}
    elif qid in ENG_MECHANICAL_SYSTEMS_QIDS:
        QUESTION_TREE_NODES[qid] = {"level": 1, "weight": 1.6, "branches": ["engineering", "technology"]}
    elif qid in ENG_ELECTRICAL_ELECTRONICS_QIDS:
        QUESTION_TREE_NODES[qid] = {"level": 1, "weight": 1.6, "branches": ["engineering", "technology"]}
    else:
        QUESTION_TREE_NODES[qid] = {"level": 1, "weight": 1.6, "branches": ["engineering", "technology", "public_service"]}

for qid in ENGINEERING_SPECIALTY_EXPANSION_QIDS:
    if qid in ENG_AERONAUTICAL_AEROSPACE_QIDS:
        QUESTION_TREE_NODES[qid] = {"level": 1, "weight": 1.6, "branches": ["engineering", "technology", "science"]}
    elif qid in ENG_GEODETIC_SURVEYING_QIDS:
        QUESTION_TREE_NODES[qid] = {"level": 1, "weight": 1.6, "branches": ["engineering", "public_service", "agriculture"]}
    elif qid in ENG_PRODUCT_INDUSTRIAL_DESIGN_QIDS:
        QUESTION_TREE_NODES[qid] = {"level": 1, "weight": 1.6, "branches": ["engineering", "creative", "business"]}
    else:
        QUESTION_TREE_NODES[qid] = {"level": 1, "weight": 1.6, "branches": ["engineering", "maritime", "technology"]}

for qid in BUSINESS_INTEREST_EXPANSION_QIDS:
    if qid in BUS_ENTREPRENEURSHIP_QIDS:
        QUESTION_TREE_NODES[qid] = {"level": 1, "weight": 1.6, "branches": ["business"]}
    elif qid in BUS_FINANCE_BANKING_QIDS:
        QUESTION_TREE_NODES[qid] = {"level": 1, "weight": 1.6, "branches": ["business", "science"]}
    elif qid in BUS_MARKETING_ADVERTISING_QIDS:
        QUESTION_TREE_NODES[qid] = {"level": 1, "weight": 1.6, "branches": ["business", "creative"]}
    else:
        QUESTION_TREE_NODES[qid] = {"level": 1, "weight": 1.6, "branches": ["business", "public_service"]}

for qid in BUSINESS_SPECIALTY_EXPANSION_QIDS:
    if qid in BUS_ACCOUNTING_QIDS:
        QUESTION_TREE_NODES[qid] = {"level": 1, "weight": 1.6, "branches": ["business", "science"]}
    elif qid in BUS_ECONOMICS_QIDS:
        QUESTION_TREE_NODES[qid] = {"level": 1, "weight": 1.6, "branches": ["business", "science", "public_service"]}
    elif qid in BUS_REAL_ESTATE_PROPERTY_QIDS:
        QUESTION_TREE_NODES[qid] = {"level": 1, "weight": 1.6, "branches": ["business", "public_service"]}
    else:
        QUESTION_TREE_NODES[qid] = {"level": 1, "weight": 1.6, "branches": ["business", "public_service"]}

for qid in BUSINESS_APPLIED_EXPANSION_QIDS:
    if qid in BUS_OPERATIONS_SUPPLY_CHAIN_QIDS:
        QUESTION_TREE_NODES[qid] = {"level": 1, "weight": 1.6, "branches": ["business", "engineering"]}
    elif qid in BUS_CUSTOMS_INTL_TRADE_QIDS:
        QUESTION_TREE_NODES[qid] = {"level": 1, "weight": 1.6, "branches": ["business", "public_service"]}
    elif qid in BUS_AGRIBUSINESS_QIDS:
        QUESTION_TREE_NODES[qid] = {"level": 1, "weight": 1.6, "branches": ["business", "agriculture"]}
    elif qid in BUS_OFFICE_ADMIN_QIDS:
        QUESTION_TREE_NODES[qid] = {"level": 1, "weight": 1.6, "branches": ["business", "public_service"]}
    else:
        QUESTION_TREE_NODES[qid] = {"level": 1, "weight": 1.6, "branches": ["business", "technology", "creative"]}

for qid in ARTS_EXPANSION_QIDS:
    if qid in ARTS_FINE_PAINTING_QIDS:
        QUESTION_TREE_NODES[qid] = {"level": 1, "weight": 1.6, "branches": ["creative", "arts"]}
    elif qid in ARTS_FASHION_TEXTILE_QIDS:
        QUESTION_TREE_NODES[qid] = {"level": 1, "weight": 1.6, "branches": ["creative", "design", "business"]}
    elif qid in ARTS_ART_DESIGN_QIDS:
        QUESTION_TREE_NODES[qid] = {"level": 1, "weight": 1.6, "branches": ["creative", "design", "technology"]}
    elif qid in ARTS_FILM_MEDIA_QIDS:
        QUESTION_TREE_NODES[qid] = {"level": 1, "weight": 1.6, "branches": ["creative", "technology", "entertainment"]}
    else:
        QUESTION_TREE_NODES[qid] = {"level": 1, "weight": 1.6, "branches": ["creative", "business", "design"]}

DOMAIN_ENTRY_QUESTIONS["science"] = _prepend_unique(
    DOMAIN_ENTRY_QUESTIONS["science"],
    [
        1281, 1286, 1291, 1296, 1301,
        1311, 1316, 1321, 1326, 1331,
        1341, 1346, 1351, 1356, 1361,
        1371, 1376, 1381, 1386, 1391,
        1401, 1406, 1411, 1416, 1421,
        1169, 1197, 1225, 1253,
    ],
    limit=30,
)
DOMAIN_ENTRY_QUESTIONS["technology"] = _prepend_unique(
    DOMAIN_ENTRY_QUESTIONS["technology"],
    [
        1431, 1436, 1441, 1446, 1451,
        1491, 1496, 1501, 1506, 1511,
        1551, 1556, 1561, 1566, 1571,
        1701, 1706, 1711, 1716, 1721,
        1641, 1646, 1651, 1656, 1661,
        1581, 1586, 1591, 1596, 1601,
        1671, 1676, 1681, 1686, 1691,
        1761, 1766, 1771, 1776, 1781,
        1611, 1616, 1621, 1626, 1631,
    ],
    limit=30,
)
DOMAIN_ENTRY_QUESTIONS["engineering"] = _prepend_unique(
    DOMAIN_ENTRY_QUESTIONS["engineering"],
    [
        2061, 2066, 2071, 2076, 2081,
        2091, 2096, 2101, 2106, 2111,
        2121, 2126, 2131, 2136, 2141,
        2151, 2156, 2161, 2166, 2171,
        1941, 1946, 1951, 1956, 1961,
        1971, 1976, 1981, 1986, 1991,
        2001, 2006, 2011, 2016, 2021,
        2031, 2036, 2041, 2046, 2051,
    ],
    limit=30,
)
DOMAIN_ENTRY_QUESTIONS["business"] = _prepend_unique(
    DOMAIN_ENTRY_QUESTIONS["business"],
    [
        2421, 2426, 2431, 2436, 2441,
        2451, 2456, 2461, 2466, 2471,
        2481, 2486, 2491, 2496, 2501,
        2511, 2516, 2521, 2526, 2531,
        2541, 2546, 2551, 2556, 2561,
        2301, 2306, 2311, 2316, 2321,
    ],
    limit=30,
)

DOMAIN_ENTRY_QUESTIONS["creative"] = _prepend_unique(
    DOMAIN_ENTRY_QUESTIONS["creative"],
    [
        2841, 2846, 2851, 2856, 2861,  # Writing & Literature
        2871, 2876, 2881, 2886, 2891,  # Animation & Multimedia
        2901, 2906, 2911, 2916, 2921,  # Clothing & Textile Technology
        2721, 2726, 2731, 2736, 2741,  # Music & Performance
        2751, 2756, 2761, 2766, 2771,  # Music Production & Audio
        2781, 2786, 2791, 2796, 2801,  # Theater & Performing Arts
        2811, 2816, 2821, 2826, 2831,  # Photography & Visual Arts
        1731, 1736, 1741, 1746, 1751,
        2661, 2666, 2671, 2676, 2681,
        2571, 2576, 2581, 2586, 2591,
        2691, 2696, 2701, 2706, 2711,
        2601, 2606, 2611, 2616, 2621,
        2631, 2636, 2641, 2646, 2651,
    ],
    limit=65,
)

TRAIT_FOLLOWUP_MAP["Environmental-Sci"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Environmental-Sci"],
    [1281, 1286, 1291, 1296, 1301, 1306, 1311, 1316, 1321, 1326, 1331, 1341, 1346, 1351, 1356, 1361, 1366, 1401, 1406, 1411, 1416, 1421, 1426],
)
TRAIT_FOLLOWUP_MAP["Field-Research"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Field-Research"],
    [1281, 1286, 1291, 1301, 1306, 1311, 1316, 1321, 1326, 1331, 1336, 1406, 1411, 1421],
)
TRAIT_FOLLOWUP_MAP["Environmental-Eng"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Environmental-Eng"],
    [1296, 1301, 1341, 1346, 1351, 1356, 1361, 1366, 1401, 1416],
)
TRAIT_FOLLOWUP_MAP["Agri-Nature"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Agri-Nature"],
    [1286, 1306, 1331, 1371, 1376, 1386, 1426],
)
TRAIT_FOLLOWUP_MAP["Lab-Research"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Lab-Research"],
    [1316, 1371, 1376, 1381, 1386, 1391, 1396, 1401, 1416],
)
TRAIT_FOLLOWUP_MAP["Data-Analytics"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Data-Analytics"],
    [1291, 1321, 1326, 1336, 1351, 1356, 1366, 1381, 1391, 1396, 1401, 1406, 1411, 1426],
)
TRAIT_FOLLOWUP_MAP["Medical-Lab"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Medical-Lab"],
    [1371, 1376, 1381, 1391, 1396],
)
TRAIT_FOLLOWUP_MAP["Community-Serve"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Community-Serve"],
    [1281, 1301, 1311, 1336, 1341, 1346, 1361, 1366, 1406, 1416, 1421, 1426],
)
TRAIT_FOLLOWUP_MAP["Software-Dev"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Software-Dev"],
    [1431, 1436, 1441, 1446, 1451, 1456, 1491, 1496, 1501, 1523, 1528, 1554],
)
TRAIT_FOLLOWUP_MAP["Hardware-Systems"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Hardware-Systems"],
    [1461, 1466, 1471, 1476, 1481, 1486, 1521, 1526, 1531, 1536, 1541, 1546],
)
TRAIT_FOLLOWUP_MAP["AI-ML"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["AI-ML"],
    [1491, 1496, 1501, 1506, 1511, 1516, 1523, 1534, 1540],
)
TRAIT_FOLLOWUP_MAP["Cyber-Defense"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Cyber-Defense"],
    [1486, 1551, 1556, 1561, 1566, 1571, 1576],
)
TRAIT_FOLLOWUP_MAP["Technical-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Technical-Skill"],
    [1435, 1453, 1465, 1473, 1483, 1505, 1521, 1532, 1548, 1563],
)
TRAIT_FOLLOWUP_MAP["Data-Analytics"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Data-Analytics"],
    [1443, 1458, 1465, 1474, 1491, 1497, 1503, 1514, 1538, 1552, 1563],
)
TRAIT_FOLLOWUP_MAP["Cloud-Systems"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Cloud-Systems"],
    [1462, 1467, 1472, 1477, 1482, 1487, 1503, 1553, 1558, 1563, 1568, 1573, 1578],
)
TRAIT_FOLLOWUP_MAP["Mechanical-Design"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Mechanical-Design"],
    [1522, 1527, 1532, 1537, 1542, 1547],
)
TRAIT_FOLLOWUP_MAP["Electrical-Power"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Electrical-Power"],
    [1524, 1531, 1541, 1545],
)
TRAIT_FOLLOWUP_MAP["Industrial-Ops"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Industrial-Ops"],
    [1525, 1526, 1535, 1540, 1543, 1548],
)
TRAIT_FOLLOWUP_MAP["Data-Analytics"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Data-Analytics"],
    [1581, 1586, 1591, 1596, 1601, 1606, 1613, 1622, 1633, 1656, 1663, 1676, 1683, 1692, 1705, 1724],
)
TRAIT_FOLLOWUP_MAP["Game-Dev"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Game-Dev"],
    [1611, 1616, 1621, 1626, 1631, 1636],
)
TRAIT_FOLLOWUP_MAP["Web-Dev"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Web-Dev"],
    [1641, 1646, 1651, 1656, 1661, 1666, 1702],
)
TRAIT_FOLLOWUP_MAP["Mobile-Dev"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Mobile-Dev"],
    [1643, 1648, 1653, 1658, 1663, 1668],
)
TRAIT_FOLLOWUP_MAP["Cloud-Systems"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Cloud-Systems"],
    [1643, 1654, 1671, 1676, 1681, 1686, 1691, 1696, 1701, 1708, 1714, 1726],
)
TRAIT_FOLLOWUP_MAP["Software-Dev"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Software-Dev"],
    [1611, 1613, 1621, 1634, 1642, 1646, 1653, 1659, 1674, 1689, 1701, 1706, 1711, 1716, 1721, 1726],
)
TRAIT_FOLLOWUP_MAP["Technical-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Technical-Skill"],
    [1586, 1593, 1600, 1611, 1625, 1644, 1659, 1672, 1684, 1695, 1704, 1713, 1728],
)
TRAIT_FOLLOWUP_MAP["Analytical-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Analytical-Skill"],
    [1581, 1584, 1588, 1598, 1606, 1613, 1623, 1645, 1656, 1672, 1680, 1696, 1702, 1711, 1724, 1728],
)
TRAIT_FOLLOWUP_MAP["People-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["People-Skill"],
    [1585, 1598, 1606, 1621, 1626, 1634, 1645, 1659, 1664, 1675, 1686, 1698, 1705, 1715, 1725],
)
TRAIT_FOLLOWUP_MAP["Admin-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Admin-Skill"],
    [1582, 1587, 1593, 1600, 1673, 1678, 1683, 1703, 1712],
)
TRAIT_FOLLOWUP_MAP["Creative-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Creative-Skill"],
    [1612, 1616, 1627, 1630, 1641, 1643, 1660],
)
TRAIT_FOLLOWUP_MAP["Animation-3D"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Animation-3D"],
    [1614, 1616, 1624, 1636],
)
TRAIT_FOLLOWUP_MAP["Hardware-Systems"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Hardware-Systems"],
    [1671, 1674, 1678, 1689, 1693],
)
TRAIT_FOLLOWUP_MAP["Community-Serve"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Community-Serve"],
    [1583, 1599, 1604, 1629, 1644, 1664, 1675, 1695, 1704, 1728],
)
TRAIT_FOLLOWUP_MAP["Startup-Venture"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Startup-Venture"],
    [1585, 1616, 1630, 1651, 1666, 1685, 1706, 1716],
)
TRAIT_FOLLOWUP_MAP["Digital-Media"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Digital-Media"],
    [1731, 1736, 1741, 1746, 1751, 1756],
)
TRAIT_FOLLOWUP_MAP["Animation-3D"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Animation-3D"],
    [1731, 1737, 1743, 1750],
)
TRAIT_FOLLOWUP_MAP["Creative-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Creative-Skill"],
    [1733, 1739, 1746, 1749, 1754],
)
TRAIT_FOLLOWUP_MAP["Visual-Design"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Visual-Design"],
    [1733, 1737, 1751],
)
TRAIT_FOLLOWUP_MAP["Cloud-Systems"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Cloud-Systems"],
    [1761, 1766, 1771, 1776, 1781, 1786, 1791, 1796, 1801, 1806, 1811, 1816],
)
TRAIT_FOLLOWUP_MAP["Admin-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Admin-Skill"],
    [1762, 1768, 1774, 1780, 1792, 1798, 1804, 1810],
)
TRAIT_FOLLOWUP_MAP["Health-Admin"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Health-Admin"],
    [1791, 1796, 1801, 1806, 1811, 1816],
)
TRAIT_FOLLOWUP_MAP["Public-Health"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Public-Health"],
    [1793, 1798, 1806, 1810, 1817],
)
TRAIT_FOLLOWUP_MAP["Medical-Lab"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Medical-Lab"],
    [1801, 1804],
)
TRAIT_FOLLOWUP_MAP["Teaching-Ed"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Teaching-Ed"],
    [1734, 1749, 1795, 1804, 1817],
)
TRAIT_FOLLOWUP_MAP["Community-Serve"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Community-Serve"],
    [1744, 1753, 1763, 1779, 1791, 1794, 1805, 1810, 1817],
)
TRAIT_FOLLOWUP_MAP["Cyber-Defense"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Cyber-Defense"],
    [1764, 1779, 1794, 1798, 1803, 1813],
)
TRAIT_FOLLOWUP_MAP["People-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["People-Skill"],
    [1735, 1748, 1754, 1766, 1775, 1784, 1795, 1805, 1814],
)
TRAIT_FOLLOWUP_MAP["Software-Dev"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Software-Dev"],
    [1732, 1737, 1755, 1763, 1769, 1779, 1796, 1803, 1815],
)
TRAIT_FOLLOWUP_MAP["Technical-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Technical-Skill"],
    [1734, 1743, 1750, 1762, 1768, 1782, 1798, 1809, 1815],
)
TRAIT_FOLLOWUP_MAP["Data-Analytics"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Data-Analytics"],
    [1736, 1742, 1751, 1765, 1771, 1775, 1780, 1793, 1798, 1802, 1817],
)
TRAIT_FOLLOWUP_MAP["Civil-Build"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Civil-Build"],
    [1821, 1826, 1831, 1836, 1841, 1846, 1915, 1922, 1930],
)
TRAIT_FOLLOWUP_MAP["Spatial-Design"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Spatial-Design"],
    [1825, 1851, 1856, 1861, 1866, 1871, 1876, 1911, 1916, 1921, 1926, 1931, 1936],
)
TRAIT_FOLLOWUP_MAP["Industrial-Ops"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Industrial-Ops"],
    [1824, 1828, 1833, 1840, 1881, 1886, 1891, 1896, 1901, 1906],
)
TRAIT_FOLLOWUP_MAP["Environmental-Eng"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Environmental-Eng"],
    [1826, 1834, 1845, 1855, 1866, 1875, 1911, 1916, 1921, 1927, 1934, 1939],
)
TRAIT_FOLLOWUP_MAP["Mechanical-Design"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Mechanical-Design"],
    [1882, 1886, 1891, 1896, 1901, 1906],
)
TRAIT_FOLLOWUP_MAP["Technical-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Technical-Skill"],
    [1826, 1831, 1838, 1843, 1854, 1864, 1881, 1883, 1889, 1895, 1906, 1925],
)
TRAIT_FOLLOWUP_MAP["Analytical-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Analytical-Skill"],
    [1823, 1833, 1844, 1853, 1863, 1873, 1881, 1883, 1889, 1899, 1916, 1923, 1935],
)
TRAIT_FOLLOWUP_MAP["Admin-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Admin-Skill"],
    [1822, 1827, 1838, 1846, 1855, 1864, 1874, 1884, 1892, 1901],
)
TRAIT_FOLLOWUP_MAP["People-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["People-Skill"],
    [1825, 1846, 1852, 1863, 1874, 1890, 1899, 1924, 1930, 1936],
)
TRAIT_FOLLOWUP_MAP["Community-Serve"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Community-Serve"],
    [1825, 1831, 1842, 1856, 1876, 1886, 1893, 1911, 1924, 1936],
)
TRAIT_FOLLOWUP_MAP["Creative-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Creative-Skill"],
    [1851, 1853, 1857, 1862, 1868, 1913, 1929],
)
TRAIT_FOLLOWUP_MAP["Visual-Design"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Visual-Design"],
    [1854, 1858, 1863, 1872],
)
TRAIT_FOLLOWUP_MAP["Field-Research"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Field-Research"],
    [1823, 1835, 1911, 1916, 1921, 1935],
)
TRAIT_FOLLOWUP_MAP["Agri-Nature"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Agri-Nature"],
    [1845, 1860, 1875, 1912, 1917, 1927, 1939],
)
TRAIT_FOLLOWUP_MAP["Aeronautical-Eng"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Aeronautical-Eng", []),
    [2031, 2036, 2041, 2046, 2051, 2056, 1976, 1996, 2008],
)
TRAIT_FOLLOWUP_MAP["Electronics-Dev"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Electronics-Dev", []),
    [2001, 2006, 2011, 2016, 2021, 2026, 2034, 2043, 2052],
)
TRAIT_FOLLOWUP_MAP["Mechanical-Design"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Mechanical-Design"],
    [1946, 1966, 1971, 1976, 1981, 1986, 1991, 1996, 2031, 2043],
)
TRAIT_FOLLOWUP_MAP["Electrical-Power"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Electrical-Power"],
    [1944, 2001, 2006, 2011, 2016, 2021, 2026, 2034, 2048],
)
TRAIT_FOLLOWUP_MAP["Hardware-Systems"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Hardware-Systems"],
    [1944, 1953, 1966, 1976, 1996, 2003, 2007, 2013, 2024, 2033, 2043],
)
TRAIT_FOLLOWUP_MAP["Technical-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Technical-Skill"],
    [1942, 1952, 1961, 1972, 1982, 1991, 2004, 2014, 2022, 2032, 2042, 2056],
)
TRAIT_FOLLOWUP_MAP["Analytical-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Analytical-Skill"],
    [1941, 1951, 1964, 1971, 1984, 1994, 2005, 2011, 2024, 2031, 2041, 2054],
)
TRAIT_FOLLOWUP_MAP["Industrial-Ops"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Industrial-Ops"],
    [1945, 1951, 1965, 1973, 1983, 1993, 2004, 2016, 2035, 2046, 2053],
)
TRAIT_FOLLOWUP_MAP["Admin-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Admin-Skill"],
    [1943, 1954, 1963, 1976, 1986, 1994, 2006, 2016, 2026, 2035, 2045, 2055],
)
TRAIT_FOLLOWUP_MAP["People-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["People-Skill"],
    [1946, 1966, 1976, 1985, 1995, 2006, 2016, 2025, 2036, 2045, 2056],
)
TRAIT_FOLLOWUP_MAP["Community-Serve"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP["Community-Serve"],
    [1945, 1966, 1985, 2001, 2015, 2031, 2043, 2056],
)
TRAIT_FOLLOWUP_MAP["Aeronautical-Eng"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Aeronautical-Eng", []),
    [2061, 2066, 2071, 2076, 2081, 2086],
)
TRAIT_FOLLOWUP_MAP["Field-Research"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Field-Research", []),
    [2091, 2096, 2101, 2106, 2111, 2116],
)
TRAIT_FOLLOWUP_MAP["Civil-Build"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Civil-Build", []),
    [2091, 2094, 2098, 2103, 2109, 2114],
)
TRAIT_FOLLOWUP_MAP["Visual-Design"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Visual-Design", []),
    [2121, 2126, 2131, 2136, 2141, 2146],
)
TRAIT_FOLLOWUP_MAP["Creative-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Creative-Skill", []),
    [2121, 2126, 2131, 2136, 2141, 2146],
)
TRAIT_FOLLOWUP_MAP["Spatial-Design"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Spatial-Design", []),
    [2126, 2131, 2135, 2146],
)
TRAIT_FOLLOWUP_MAP["Maritime-Sea"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Maritime-Sea", []),
    [2151, 2156, 2161, 2166, 2171, 2176],
)
TRAIT_FOLLOWUP_MAP["Mechanical-Design"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Mechanical-Design", []),
    [2063, 2069, 2074, 2123, 2133, 2151, 2157, 2163, 2169],
)
TRAIT_FOLLOWUP_MAP["Electrical-Power"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Electrical-Power", []),
    [2064, 2073, 2083, 2155, 2165, 2175],
)
TRAIT_FOLLOWUP_MAP["Electronics-Dev"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Electronics-Dev", []),
    [2064, 2069, 2073, 2085],
)
TRAIT_FOLLOWUP_MAP["Technical-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Technical-Skill", []),
    [2062, 2072, 2084, 2095, 2105, 2123, 2152, 2162, 2172],
)
TRAIT_FOLLOWUP_MAP["Analytical-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Analytical-Skill", []),
    [2061, 2071, 2081, 2092, 2102, 2112, 2124, 2154, 2164],
)
TRAIT_FOLLOWUP_MAP["Industrial-Ops"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Industrial-Ops", []),
    [2066, 2125, 2134, 2154, 2164, 2174],
)
TRAIT_FOLLOWUP_MAP["Data-Analytics"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Data-Analytics", []),
    [2065, 2075, 2085, 2105, 2115],
)
TRAIT_FOLLOWUP_MAP["People-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("People-Skill", []),
    [2096, 2106, 2122, 2132, 2142, 2156, 2166, 2176],
)
TRAIT_FOLLOWUP_MAP["Admin-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Admin-Skill", []),
    [2066, 2076, 2086, 2106, 2134, 2154, 2164, 2174],
)
TRAIT_FOLLOWUP_MAP["Community-Serve"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Community-Serve", []),
    [2094, 2104, 2122, 2156, 2176],
)
TRAIT_FOLLOWUP_MAP["Startup-Venture"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Startup-Venture", []),
    [2481, 2486, 2491, 2496, 2501, 2506, 2541, 2546, 2551, 2556, 2561, 2566, 2331, 2336, 2341, 2346, 2351, 2356, 2361, 2366, 2371, 2376, 2381, 2386, 2181, 2186, 2191, 2196, 2201, 2206, 2213, 2223, 2233, 2246, 2266, 2286, 2296],
)
TRAIT_FOLLOWUP_MAP["Finance-Acct"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Finance-Acct", []),
    [2424, 2434, 2444, 2453, 2463, 2473, 2484, 2494, 2504, 2515, 2525, 2535, 2544, 2554, 2564, 2301, 2306, 2311, 2316, 2321, 2326, 2331, 2336, 2341, 2346, 2351, 2356, 2361, 2366, 2371, 2376, 2381, 2386, 2184, 2194, 2204, 2211, 2216, 2221, 2226, 2231, 2236, 2274, 2284, 2294],
)
TRAIT_FOLLOWUP_MAP["Marketing-Sales"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Marketing-Sales", []),
    [2456, 2466, 2476, 2485, 2495, 2505, 2543, 2553, 2563, 2361, 2366, 2371, 2376, 2381, 2386, 2183, 2193, 2203, 2241, 2246, 2251, 2256, 2261, 2266, 2181, 2191],
)
TRAIT_FOLLOWUP_MAP["Admin-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Admin-Skill", []),
    [2422, 2432, 2442, 2451, 2461, 2471, 2483, 2493, 2503, 2511, 2516, 2521, 2526, 2531, 2536, 2301, 2306, 2311, 2316, 2321, 2326, 2391, 2396, 2401, 2406, 2411, 2416, 2182, 2192, 2202, 2212, 2222, 2232, 2271, 2276, 2281, 2286, 2291, 2296],
)
TRAIT_FOLLOWUP_MAP["People-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("People-Skill", []),
    [2426, 2436, 2446, 2454, 2464, 2474, 2512, 2522, 2532, 2546, 2556, 2566, 2361, 2366, 2371, 2376, 2381, 2386, 2391, 2396, 2401, 2406, 2411, 2416, 2185, 2195, 2205, 2214, 2224, 2234, 2241, 2245, 2255, 2265, 2272, 2282, 2292],
)
TRAIT_FOLLOWUP_MAP["Data-Analytics"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Data-Analytics", []),
    [2423, 2433, 2443, 2455, 2465, 2475, 2486, 2496, 2506, 2516, 2526, 2536, 2543, 2553, 2563, 2301, 2311, 2321, 2331, 2341, 2351, 2391, 2401, 2411, 2183, 2184, 2211, 2215, 2225, 2235, 2244, 2254, 2264, 2273, 2283],
)
TRAIT_FOLLOWUP_MAP["Creative-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Creative-Skill", []),
    [2186, 2196, 2206, 2242, 2247, 2252, 2257, 2262],
)
TRAIT_FOLLOWUP_MAP["Digital-Media"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Digital-Media", []),
    [2186, 2243, 2247, 2253, 2258, 2263],
)
TRAIT_FOLLOWUP_MAP["Industrial-Ops"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Industrial-Ops", []),
    [2182, 2192, 2271, 2273, 2277, 2283, 2287, 2293, 2297],
)
TRAIT_FOLLOWUP_MAP["Analytical-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Analytical-Skill", []),
    [2301, 2306, 2311, 2316, 2321, 2326, 2331, 2336, 2341, 2346, 2351, 2356, 2361, 2366, 2184, 2194, 2204, 2211, 2216, 2221, 2226, 2231, 2236, 2244, 2254, 2271, 2281],
)
TRAIT_FOLLOWUP_MAP["HR-Management"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("HR-Management", []),
    [2391, 2396, 2401, 2406, 2411, 2416],
)

TRAIT_FOLLOWUP_MAP["Visual-Design"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Visual-Design", []),
    [2870, 2878, 2888, 2893, 2898, 2903, 2913, 2923, 2811, 2816, 2821, 2826, 2831, 2836, 2721, 2731, 2741, 2781, 2791, 2571, 2576, 2581, 2586, 2591, 2596, 2601, 2606, 2611, 2616, 2621, 2626, 2631, 2636, 2641, 2646, 2651, 2656, 2691, 2696, 2701, 2706, 2711, 2716],
)
TRAIT_FOLLOWUP_MAP["Creative-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Creative-Skill", []),
    [2841, 2846, 2851, 2856, 2861, 2866, 2871, 2876, 2881, 2886, 2891, 2896, 2901, 2906, 2911, 2916, 2921, 2926, 2721, 2726, 2731, 2741, 2751, 2756, 2761, 2771, 2781, 2786, 2791, 2801, 2811, 2816, 2821, 2831, 2571, 2576, 2581, 2586, 2591, 2596, 2601, 2606, 2611, 2616, 2621, 2626, 2631, 2636, 2641, 2646, 2651, 2656, 2661, 2666, 2671, 2676, 2681, 2686, 2691, 2696, 2701, 2706, 2711],
)
TRAIT_FOLLOWUP_MAP["Artistic"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Artistic", []),
    [2842, 2847, 2852, 2857, 2862, 2871, 2876, 2881, 2886, 2896, 2901, 2911, 2921, 2926, 2721, 2726, 2731, 2736, 2741, 2746, 2781, 2786, 2791, 2796, 2801, 2806, 2811, 2816, 2821, 2571, 2576, 2581, 2586, 2591, 2596, 2601, 2606, 2611, 2616, 2621, 2626, 2661, 2666, 2671, 2676, 2681, 2686, 2691, 2696, 2701],
)
TRAIT_FOLLOWUP_MAP["Digital-Media"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Digital-Media", []),
    [2844, 2854, 2864, 2869, 2873, 2880, 2885, 2895, 2900, 2912, 2924, 2581, 2591, 2596, 2616, 2626, 2636, 2646, 2656, 2661, 2666, 2671, 2676, 2681, 2686, 2701, 2706, 2711, 2716],
)
TRAIT_FOLLOWUP_MAP["Spatial-Design"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Spatial-Design", []),
    [2904, 2909, 2914, 2925, 2576, 2586, 2596, 2631, 2636, 2641, 2646, 2651, 2656],
)
TRAIT_FOLLOWUP_MAP["Film-Broadcast"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Film-Broadcast", []),
    [2848, 2853, 2858, 2863, 2868, 2874, 2882, 2887, 2892, 2897, 2930, 2745, 2749, 2758, 2767, 2774, 2789, 2809, 2827, 2661, 2666, 2671, 2676, 2681, 2686],
)
TRAIT_FOLLOWUP_MAP["Marketing-Sales"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Marketing-Sales", []),
    [2855, 2860, 2865, 2920, 2925, 2601, 2606, 2611, 2616, 2621, 2626, 2691, 2696, 2701, 2706, 2711, 2716],
)
TRAIT_FOLLOWUP_MAP["Software-Dev"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Software-Dev", []),
    [2858, 2875, 2881, 2885, 2889, 2900, 2912, 2917, 2927, 2929, 2581, 2586, 2596, 2631, 2636, 2641, 2651, 2691, 2696, 2701, 2706, 2711, 2716],
)
TRAIT_FOLLOWUP_MAP["Community-Serve"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Community-Serve", []),
    [2859, 2866, 2870, 2921, 2930, 2631, 2636, 2641, 2646, 2651, 2691, 2696, 2706],
)
TRAIT_FOLLOWUP_MAP["Data-Analytics"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Data-Analytics", []),
    [2606, 2616, 2621, 2626, 2691, 2696, 2701, 2706, 2711, 2716],
)
TRAIT_FOLLOWUP_MAP["Startup-Venture"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Startup-Venture", []),
    [2856, 2862, 2867, 2885, 2906, 2926, 2601, 2611, 2631, 2641, 2651, 2691, 2701, 2711],
)
TRAIT_FOLLOWUP_MAP["Teaching-Ed"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Teaching-Ed", []),
    [2861, 2866, 2870, 2884, 2895, 2930, 2576, 2586, 2591, 2596, 2606, 2616, 2626, 2641, 2651, 2656, 2661, 2671, 2681],
)
TRAIT_FOLLOWUP_MAP["Lab-Research"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Lab-Research", []),
    [2907, 2908, 2917, 2923, 2928, 2571, 2576, 2581, 2586, 2591, 2596, 2631, 2636, 2641, 2646],
)
TRAIT_FOLLOWUP_MAP["Analytical-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Analytical-Skill", []),
    [2843, 2845, 2847, 2853, 2857, 2909, 2918, 2581, 2591, 2596, 2606, 2621, 2631, 2641, 2646, 2651, 2691, 2706, 2711, 2716],
)
TRAIT_FOLLOWUP_MAP["Performing-Arts"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Performing-Arts", []),
    [2850, 2854, 2858, 2883, 2895, 2898, 2926, 2930, 2721, 2726, 2731, 2736, 2741, 2746, 2751, 2756, 2761, 2766, 2771, 2776, 2781, 2786, 2791, 2796, 2801, 2806, 2811, 2816, 2821, 2661, 2666, 2671, 2676, 2681, 2686],
)
TRAIT_FOLLOWUP_MAP["Community-Serve"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Community-Serve", []),
    [2426, 2436, 2446, 2454, 2464, 2474, 2512, 2522, 2532, 2546, 2556, 2566, 2331, 2336, 2341, 2346, 2351, 2356, 2361, 2366, 2391, 2396, 2401, 2406, 2411, 2416],
)
TRAIT_FOLLOWUP_MAP["Teaching-Ed"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Teaching-Ed", []),
    [2391, 2396, 2401, 2406, 2411, 2416],
)
TRAIT_FOLLOWUP_MAP["Industrial-Ops"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Industrial-Ops", []),
    [2902, 2907, 2912, 2917, 2922, 2927, 2421, 2426, 2431, 2436, 2441, 2446, 2452, 2462, 2472, 2482, 2492, 2502],
)
TRAIT_FOLLOWUP_MAP["Agri-Nature"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Agri-Nature", []),
    [2481, 2486, 2491, 2496, 2501, 2506],
)
TRAIT_FOLLOWUP_MAP["Hospitality-Svc"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Hospitality-Svc", []),
    [2511, 2516, 2521, 2526, 2531, 2536],
)
TRAIT_FOLLOWUP_MAP["Conventional"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Conventional", []),
    [2451, 2461, 2471, 2511, 2521, 2531],
)
TRAIT_FOLLOWUP_MAP["Mechanical-Design"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Mechanical-Design", []),
    [2904, 2914, 2927, 2425, 2435, 2445],
)
# ── Arts Expansion 2 new trait entries ──
TRAIT_FOLLOWUP_MAP["Animation-3D"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Animation-3D", []),
    [2871, 2872, 2873, 2874, 2875, 2876, 2877, 2878, 2879, 2880, 2881, 2882, 2883, 2884, 2885, 2886, 2887, 2888, 2889, 2890, 2891, 2892, 2893, 2894, 2895, 2896, 2897, 2898, 2899, 2900],
)
TRAIT_FOLLOWUP_MAP["Game-Dev"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Game-Dev", []),
    [2876, 2882, 2890, 2895, 2897],
)
TRAIT_FOLLOWUP_MAP["Environmental-Eng"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Environmental-Eng", []),
    [2903, 2915, 2921, 2928],
)
TRAIT_FOLLOWUP_MAP["Software-Dev"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Software-Dev", []),
    [2423, 2433, 2443, 2516, 2526, 2536, 2545, 2555, 2565],
)

# ── Healthcare expansion: domain entry points ──
DOMAIN_ENTRY_QUESTIONS["healthcare"] = _prepend_unique(
    DOMAIN_ENTRY_QUESTIONS["healthcare"],
    # 5 entry points per category (every 5th Q for variety)
    [2931, 2936, 2941, 2946, 2951,   # Medicine & Healthcare
     2961, 2966, 2971, 2976, 2981,   # Nursing & Patient Care
     2991, 2996, 3001, 3006, 3011,   # Psychology & Mental Health
     3021, 3026, 3031, 3036, 3041],  # Public Health
)

# ── Healthcare expansion: trait follow-up prepends ──
TRAIT_FOLLOWUP_MAP["Patient-Care"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Patient-Care", []),
    [2931, 2932, 2933, 2934, 2935, 2936, 2937, 2938, 2939, 2940, 2941, 2942, 2943, 2944, 2945, 2946, 2947, 2948, 2949, 2950, 2956, 2957, 2958, 2959, 2960, 2961, 2962, 2963, 2964, 2965, 2966, 2967, 2968, 2969, 2970, 2971, 2972, 2973, 2974, 2975, 2976, 2977, 2978, 2979, 2980, 2981, 2982, 2983, 2984, 2985, 2986, 2987, 2988, 2989, 2990, 3006, 3007, 3008, 3009, 3010],
)
TRAIT_FOLLOWUP_MAP["Medical-Lab"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Medical-Lab", []),
    [2936, 2937, 2938, 2939, 2940, 2941, 2942, 2943, 2944, 2945, 2946, 2947, 2948, 2949, 2950, 2951, 2952, 2953, 2954, 2955],
)
TRAIT_FOLLOWUP_MAP["Rehab-Therapy"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Rehab-Therapy", []),
    [2936, 2937, 2938, 2939, 2940, 2946, 2947, 2948, 2949, 2950, 2956, 2957, 2958, 2959, 2960, 3006, 3007, 3008, 3009, 3010, 3011, 3012, 3013, 3014, 3015, 3016, 3017, 3018, 3019, 3020],
)
TRAIT_FOLLOWUP_MAP["Health-Admin"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Health-Admin", []),
    [2931, 2932, 2933, 2934, 2935, 2941, 2942, 2943, 2944, 2945, 2946, 2947, 2948, 2949, 2950, 2956, 2957, 2958, 2959, 2960, 2961, 2962, 2963, 2964, 2965, 2971, 2972, 2973, 2974, 2975, 2976, 2977, 2978, 2979, 2980, 2981, 2982, 2983, 2984, 2985, 2986, 2987, 2988, 2989, 2990, 3016, 3017, 3018, 3019, 3020, 3021, 3022, 3023, 3024, 3025, 3031, 3032, 3033, 3034, 3035, 3036, 3037, 3038, 3039, 3040, 3041, 3042, 3043, 3044, 3045, 3046, 3047, 3048, 3049, 3050],
)
TRAIT_FOLLOWUP_MAP["Counseling"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Counseling", []),
    [2941, 2942, 2943, 2944, 2945, 2951, 2952, 2953, 2954, 2955, 2966, 2967, 2968, 2969, 2970, 2971, 2972, 2973, 2974, 2975, 2981, 2982, 2983, 2984, 2985, 2991, 2992, 2993, 2994, 2995, 2996, 2997, 2998, 2999, 3000, 3001, 3002, 3003, 3004, 3005, 3006, 3007, 3008, 3009, 3010, 3016, 3017, 3018, 3019, 3020, 3041, 3042, 3043, 3044, 3045],
)
TRAIT_FOLLOWUP_MAP["Public-Health"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Public-Health", []),
    [2951, 2952, 2953, 2954, 2955, 2966, 2967, 2968, 2969, 2970, 2981, 2982, 2983, 2984, 2985, 3021, 3022, 3023, 3024, 3025, 3026, 3027, 3028, 3029, 3030, 3031, 3032, 3033, 3034, 3035, 3041, 3042, 3043, 3044, 3045, 3046, 3047, 3048, 3049, 3050],
)
TRAIT_FOLLOWUP_MAP["Lab-Research"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Lab-Research", []),
    [2931, 2932, 2933, 2934, 2935, 2941, 2942, 2943, 2944, 2945, 2946, 2947, 2948, 2949, 2950, 2956, 2957, 2958, 2959, 2960, 2981, 2982, 2983, 2984, 2985, 2991, 2992, 2993, 2994, 2995, 2996, 2997, 2998, 2999, 3000, 3001, 3002, 3003, 3004, 3005, 3006, 3007, 3008, 3009, 3010, 3011, 3012, 3013, 3014, 3015, 3016, 3017, 3018, 3019, 3020, 3021, 3022, 3023, 3024, 3025, 3031, 3032, 3033, 3034, 3035, 3036, 3037, 3038, 3039, 3040, 3046, 3047, 3048, 3049, 3050],
)
TRAIT_FOLLOWUP_MAP["Pharmacy"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Pharmacy", []),
    [2936, 2937, 2938, 2939, 2940, 2946, 2947, 2948, 2949, 2950, 2971, 2972, 2973, 2974, 2975],
)
TRAIT_FOLLOWUP_MAP["Nutrition-Diet"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Nutrition-Diet", []),
    [2951, 2952, 2953, 2954, 2955, 3041, 3042, 3043, 3044, 3045],
)
TRAIT_FOLLOWUP_MAP["People-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("People-Skill", []),
    [2971, 2972, 2973, 2974, 2975, 2986, 2987, 2988, 2989, 2990, 2996, 2997, 2998, 2999, 3000, 3001, 3002, 3003, 3004, 3005],
)
TRAIT_FOLLOWUP_MAP["Analytical-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Analytical-Skill", []),
    [2941, 2942, 2943, 2944, 2945, 2956, 2957, 2958, 2959, 2960, 2971, 2972, 2973, 2974, 2975, 2996, 2997, 2998, 2999, 3000, 3001, 3002, 3003, 3004, 3005, 3011, 3012, 3013, 3014, 3015, 3021, 3022, 3023, 3024, 3025, 3026, 3027, 3028, 3029, 3030, 3031, 3032, 3033, 3034, 3035, 3036, 3037, 3038, 3039, 3040, 3046, 3047, 3048, 3049, 3050],
)
TRAIT_FOLLOWUP_MAP["Community-Serve"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Community-Serve", []),
    [2961, 2962, 2963, 2964, 2965, 2966, 2967, 2968, 2969, 2970, 2986, 2987, 2988, 2989, 2990, 2991, 2992, 2993, 2994, 2995, 3006, 3007, 3008, 3009, 3010, 3011, 3012, 3013, 3014, 3015, 3016, 3017, 3018, 3019, 3020, 3021, 3022, 3023, 3024, 3025, 3026, 3027, 3028, 3029, 3030, 3031, 3032, 3033, 3034, 3035, 3036, 3037, 3038, 3039, 3040, 3046, 3047, 3048, 3049, 3050],
)
TRAIT_FOLLOWUP_MAP["Teaching-Ed"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Teaching-Ed", []),
    [2976, 2977, 2978, 2979, 2980, 2981, 2982, 2983, 2984, 2985, 2986, 2987, 2988, 2989, 2990, 2996, 2997, 2998, 2999, 3000, 3006, 3007, 3008, 3009, 3010, 3011, 3012, 3013, 3014, 3015, 3041, 3042, 3043, 3044, 3045],
)

# ── Healthcare expansion 2: domain entry points ──
DOMAIN_ENTRY_QUESTIONS["healthcare"] = _prepend_unique(
    DOMAIN_ENTRY_QUESTIONS["healthcare"],
    [3051, 3056, 3061, 3066, 3071,   # Pharmacy & Pharmaceutical Science
     3081, 3086, 3091, 3096, 3101,   # Physical Therapy & Rehabilitation
     3111, 3116, 3121, 3126, 3131,   # Medical Technology & Lab Science
     3141, 3146, 3151, 3156, 3161],  # Nutrition & Dietetics
)

# ── Healthcare expansion 2: trait follow-up prepends ──
TRAIT_FOLLOWUP_MAP["Pharmacy"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Pharmacy", []),
    list(range(3051, 3081)),
)
TRAIT_FOLLOWUP_MAP["Rehab-Therapy"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Rehab-Therapy", []),
    list(range(3081, 3111)),
)
TRAIT_FOLLOWUP_MAP["Medical-Lab"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Medical-Lab", []),
    list(range(3111, 3141)),
)
TRAIT_FOLLOWUP_MAP["Nutrition-Diet"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Nutrition-Diet", []),
    list(range(3141, 3171)),
)
TRAIT_FOLLOWUP_MAP["Patient-Care"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Patient-Care", []),
    [3051, 3052, 3053, 3054, 3055, 3056, 3057, 3058, 3059, 3060, 3066, 3067, 3068, 3069, 3070,
     3076, 3077, 3078, 3079, 3080, 3081, 3082, 3083, 3084, 3085, 3086, 3087, 3088, 3089, 3090,
     3091, 3092, 3093, 3094, 3095, 3096, 3097, 3098, 3099, 3100, 3101, 3102, 3103, 3104, 3105,
     3111, 3112, 3113, 3114, 3115, 3121, 3122, 3123, 3124, 3125, 3126, 3127, 3128, 3129, 3130,
     3141, 3142, 3143, 3144, 3145, 3146, 3147, 3148, 3149, 3150, 3151, 3152, 3153, 3154, 3155,
     3161, 3162, 3163, 3164, 3165, 3166, 3167, 3168, 3169, 3170],
)
TRAIT_FOLLOWUP_MAP["Lab-Research"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Lab-Research", []),
    [3051, 3052, 3053, 3054, 3055, 3056, 3057, 3058, 3059, 3060, 3061, 3062, 3063, 3064, 3065,
     3071, 3072, 3073, 3074, 3075, 3076, 3077, 3078, 3079, 3080, 3096, 3097, 3098, 3099, 3100,
     3101, 3102, 3103, 3104, 3105, 3111, 3112, 3113, 3114, 3115, 3116, 3117, 3118, 3119, 3120,
     3121, 3122, 3123, 3124, 3125, 3126, 3127, 3128, 3129, 3130, 3131, 3132, 3133, 3134, 3135,
     3136, 3137, 3138, 3139, 3140, 3141, 3142, 3143, 3144, 3145, 3156, 3157, 3158, 3159, 3160,
     3166, 3167, 3168, 3169, 3170],
)
TRAIT_FOLLOWUP_MAP["Analytical-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Analytical-Skill", []),
    [3051, 3052, 3053, 3054, 3055, 3056, 3057, 3058, 3059, 3060, 3061, 3062, 3063, 3064, 3065,
     3066, 3067, 3068, 3069, 3070, 3071, 3072, 3073, 3074, 3075, 3081, 3082, 3083, 3084, 3085,
     3091, 3092, 3093, 3094, 3095, 3101, 3102, 3103, 3104, 3105,
     3111, 3112, 3113, 3114, 3115, 3116, 3117, 3118, 3119, 3120, 3121, 3122, 3123, 3124, 3125,
     3126, 3127, 3128, 3129, 3130, 3131, 3132, 3133, 3134, 3135, 3136, 3137, 3138, 3139, 3140,
     3141, 3142, 3143, 3144, 3145, 3151, 3152, 3153, 3154, 3155, 3156, 3157, 3158, 3159, 3160,
     3166, 3167, 3168, 3169, 3170],
)
TRAIT_FOLLOWUP_MAP["People-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("People-Skill", []),
    [3051, 3052, 3053, 3054, 3055, 3061, 3062, 3063, 3064, 3065, 3066, 3067, 3068, 3069, 3070,
     3071, 3072, 3073, 3074, 3075, 3081, 3082, 3083, 3084, 3085, 3091, 3092, 3093, 3094, 3095,
     3096, 3097, 3098, 3099, 3100, 3101, 3102, 3103, 3104, 3105,
     3126, 3127, 3128, 3129, 3130, 3136, 3137, 3138, 3139, 3140,
     3141, 3142, 3143, 3144, 3145, 3156, 3157, 3158, 3159, 3160, 3161, 3162, 3163, 3164, 3165],
)
TRAIT_FOLLOWUP_MAP["Community-Serve"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Community-Serve", []),
    [3051, 3052, 3053, 3054, 3055, 3071, 3072, 3073, 3074, 3075, 3076, 3077, 3078, 3079, 3080,
     3081, 3082, 3083, 3084, 3085, 3096, 3097, 3098, 3099, 3100, 3101, 3102, 3103, 3104, 3105,
     3131, 3132, 3133, 3134, 3135, 3141, 3142, 3143, 3144, 3145, 3146, 3147, 3148, 3149, 3150,
     3151, 3152, 3153, 3154, 3155, 3156, 3157, 3158, 3159, 3160, 3161, 3162, 3163, 3164, 3165,
     3166, 3167, 3168, 3169, 3170],
)
TRAIT_FOLLOWUP_MAP["Health-Admin"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Health-Admin", []),
    [3056, 3057, 3058, 3059, 3060, 3061, 3062, 3063, 3064, 3065, 3066, 3067, 3068, 3069, 3070,
     3071, 3072, 3073, 3074, 3075, 3081, 3082, 3083, 3084, 3085, 3101, 3102, 3103, 3104, 3105,
     3116, 3117, 3118, 3119, 3120, 3126, 3127, 3128, 3129, 3130, 3131, 3132, 3133, 3134, 3135,
     3136, 3137, 3138, 3139, 3140, 3146, 3147, 3148, 3149, 3150, 3151, 3152, 3153, 3154, 3155,
     3156, 3157, 3158, 3159, 3160, 3166, 3167, 3168, 3169, 3170],
)
TRAIT_FOLLOWUP_MAP["Public-Health"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Public-Health", []),
    [3071, 3072, 3073, 3074, 3075, 3096, 3097, 3098, 3099, 3100, 3101, 3102, 3103, 3104, 3105,
     3111, 3112, 3113, 3114, 3115, 3116, 3117, 3118, 3119, 3120, 3131, 3132, 3133, 3134, 3135,
     3136, 3137, 3138, 3139, 3140, 3146, 3147, 3148, 3149, 3150, 3156, 3157, 3158, 3159, 3160,
     3161, 3162, 3163, 3164, 3165, 3166, 3167, 3168, 3169, 3170],
)
TRAIT_FOLLOWUP_MAP["Teaching-Ed"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Teaching-Ed", []),
    [3076, 3077, 3078, 3079, 3080, 3091, 3092, 3093, 3094, 3095, 3101, 3102, 3103, 3104, 3105,
     3126, 3127, 3128, 3129, 3130, 3131, 3132, 3133, 3134, 3135, 3136, 3137, 3138, 3139, 3140,
     3146, 3147, 3148, 3149, 3150, 3156, 3157, 3158, 3159, 3160, 3161, 3162, 3163, 3164, 3165],
)
TRAIT_FOLLOWUP_MAP["Counseling"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Counseling", []),
    [3051, 3052, 3053, 3054, 3055, 3076, 3077, 3078, 3079, 3080, 3081, 3082, 3083, 3084, 3085,
     3086, 3087, 3088, 3089, 3090, 3091, 3092, 3093, 3094, 3095,
     3141, 3142, 3143, 3144, 3145, 3146, 3147, 3148, 3149, 3150, 3151, 3152, 3153, 3154, 3155,
     3156, 3157, 3158, 3159, 3160],
)
TRAIT_FOLLOWUP_MAP["Physical-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Physical-Skill", []),
    [3081, 3082, 3083, 3084, 3085, 3086, 3087, 3088, 3089, 3090, 3091, 3092, 3093, 3094, 3095,
     3096, 3097, 3098, 3099, 3100, 3101, 3102, 3103, 3104, 3105,
     3146, 3147, 3148, 3149, 3150, 3161, 3162, 3163, 3164, 3165],
)

# ── Healthcare expansion 3: domain entry points ──
DOMAIN_ENTRY_QUESTIONS["healthcare"] = _prepend_unique(
    DOMAIN_ENTRY_QUESTIONS["healthcare"],
    [3171, 3176, 3181, 3186, 3191,   # Occupational Therapy
     3201, 3206, 3211, 3216, 3221,   # Respiratory Therapy
     3231, 3236, 3241, 3246, 3251,   # Speech-Language Pathology
     3261, 3266, 3271, 3276, 3281],  # Dentistry & Oral Health
)

# ── Healthcare expansion 3: trait follow-up prepends ──
TRAIT_FOLLOWUP_MAP["Rehab-Therapy"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Rehab-Therapy", []),
    [3171, 3172, 3173, 3174, 3175, 3176, 3177, 3178, 3179, 3180,
     3181, 3182, 3183, 3184, 3185, 3186, 3187, 3188, 3189, 3190,
     3191, 3192, 3193, 3194, 3195, 3196, 3197, 3198, 3199, 3200,
     3201, 3202, 3203, 3204, 3205, 3206, 3207, 3208, 3209, 3210,
     3211, 3212, 3213, 3214, 3215, 3216, 3217, 3218, 3219, 3220,
     3221, 3222, 3223, 3224, 3225, 3226, 3227, 3228, 3229, 3230,
     3231, 3232, 3233, 3234, 3235, 3236, 3237, 3238, 3239, 3240,
     3241, 3242, 3243, 3244, 3245, 3246, 3247, 3248, 3249, 3250,
     3251, 3252, 3253, 3254, 3255, 3256, 3257, 3258, 3259, 3260],
)
TRAIT_FOLLOWUP_MAP["Patient-Care"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Patient-Care", []),
    [3171, 3172, 3173, 3174, 3175, 3176, 3177, 3178, 3179, 3180,
     3181, 3182, 3183, 3184, 3185, 3186, 3187, 3188, 3189, 3190,
     3191, 3192, 3193, 3194, 3195, 3196, 3197, 3198, 3199, 3200,
     3201, 3202, 3203, 3204, 3205, 3206, 3207, 3208, 3209, 3210,
     3211, 3212, 3213, 3214, 3215, 3216, 3217, 3218, 3219, 3220,
     3221, 3222, 3223, 3224, 3225, 3226, 3227, 3228, 3229, 3230,
     3231, 3232, 3233, 3234, 3235, 3236, 3237, 3238, 3239, 3240,
     3241, 3242, 3243, 3244, 3245, 3246, 3247, 3248, 3249, 3250,
     3251, 3252, 3253, 3254, 3255, 3256, 3257, 3258, 3259, 3260,
     3261, 3262, 3263, 3264, 3265, 3266, 3267, 3268, 3269, 3270,
     3271, 3272, 3273, 3274, 3275, 3276, 3277, 3278, 3279, 3280,
     3281, 3282, 3283, 3284, 3285, 3286, 3287, 3288, 3289, 3290],
)
TRAIT_FOLLOWUP_MAP["People-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("People-Skill", []),
    [3171, 3172, 3173, 3174, 3175, 3176, 3177, 3178, 3179, 3180,
     3181, 3182, 3183, 3184, 3185, 3186, 3187, 3188, 3189, 3190,
     3191, 3192, 3193, 3194, 3195, 3196, 3197, 3198, 3199, 3200,
     3231, 3232, 3233, 3234, 3235, 3236, 3237, 3238, 3239, 3240,
     3241, 3242, 3243, 3244, 3245, 3246, 3247, 3248, 3249, 3250,
     3251, 3252, 3253, 3254, 3255, 3256, 3257, 3258, 3259, 3260,
     3261, 3262, 3263, 3264, 3265, 3266, 3267, 3268, 3269, 3270,
     3281, 3282, 3283, 3284, 3285, 3286, 3287, 3288, 3289, 3290],
)
TRAIT_FOLLOWUP_MAP["Counseling"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Counseling", []),
    [3171, 3172, 3173, 3174, 3175, 3176, 3177, 3178, 3179, 3180,
     3186, 3187, 3188, 3189, 3190, 3191, 3192, 3193, 3194, 3195,
     3196, 3197, 3198, 3199, 3200,
     3231, 3232, 3233, 3234, 3235, 3236, 3237, 3238, 3239, 3240,
     3246, 3247, 3248, 3249, 3250, 3251, 3252, 3253, 3254, 3255,
     3281, 3282, 3283, 3284, 3285],
)
TRAIT_FOLLOWUP_MAP["Community-Serve"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Community-Serve", []),
    [3171, 3172, 3173, 3174, 3175, 3186, 3187, 3188, 3189, 3190,
     3191, 3192, 3193, 3194, 3195, 3196, 3197, 3198, 3199, 3200,
     3221, 3222, 3223, 3224, 3225, 3226, 3227, 3228, 3229, 3230,
     3231, 3232, 3233, 3234, 3235, 3251, 3252, 3253, 3254, 3255,
     3256, 3257, 3258, 3259, 3260,
     3261, 3262, 3263, 3264, 3265, 3276, 3277, 3278, 3279, 3280,
     3286, 3287, 3288, 3289, 3290],
)
TRAIT_FOLLOWUP_MAP["Teaching-Ed"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Teaching-Ed", []),
    [3171, 3172, 3173, 3174, 3175, 3181, 3182, 3183, 3184, 3185,
     3186, 3187, 3188, 3189, 3190, 3196, 3197, 3198, 3199, 3200,
     3221, 3222, 3223, 3224, 3225,
     3236, 3237, 3238, 3239, 3240, 3241, 3242, 3243, 3244, 3245,
     3251, 3252, 3253, 3254, 3255, 3256, 3257, 3258, 3259, 3260,
     3271, 3272, 3273, 3274, 3275, 3286, 3287, 3288, 3289, 3290],
)
TRAIT_FOLLOWUP_MAP["Health-Admin"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Health-Admin", []),
    [3176, 3177, 3178, 3179, 3180, 3186, 3187, 3188, 3189, 3190,
     3191, 3192, 3193, 3194, 3195, 3196, 3197, 3198, 3199, 3200,
     3211, 3212, 3213, 3214, 3215, 3216, 3217, 3218, 3219, 3220,
     3226, 3227, 3228, 3229, 3230,
     3246, 3247, 3248, 3249, 3250,
     3261, 3262, 3263, 3264, 3265, 3276, 3277, 3278, 3279, 3280,
     3281, 3282, 3283, 3284, 3285],
)
TRAIT_FOLLOWUP_MAP["Analytical-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Analytical-Skill", []),
    [3176, 3177, 3178, 3179, 3180, 3181, 3182, 3183, 3184, 3185,
     3191, 3192, 3193, 3194, 3195, 3196, 3197, 3198, 3199, 3200,
     3201, 3202, 3203, 3204, 3205, 3206, 3207, 3208, 3209, 3210,
     3211, 3212, 3213, 3214, 3215, 3216, 3217, 3218, 3219, 3220,
     3226, 3227, 3228, 3229, 3230,
     3236, 3237, 3238, 3239, 3240, 3241, 3242, 3243, 3244, 3245,
     3251, 3252, 3253, 3254, 3255, 3256, 3257, 3258, 3259, 3260,
     3261, 3262, 3263, 3264, 3265, 3266, 3267, 3268, 3269, 3270,
     3271, 3272, 3273, 3274, 3275, 3281, 3282, 3283, 3284, 3285,
     3286, 3287, 3288, 3289, 3290],
)
TRAIT_FOLLOWUP_MAP["Medical-Lab"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Medical-Lab", []),
    [3176, 3177, 3178, 3179, 3180, 3181, 3182, 3183, 3184, 3185,
     3201, 3202, 3203, 3204, 3205, 3206, 3207, 3208, 3209, 3210,
     3211, 3212, 3213, 3214, 3215, 3216, 3217, 3218, 3219, 3220,
     3226, 3227, 3228, 3229, 3230,
     3236, 3237, 3238, 3239, 3240, 3241, 3242, 3243, 3244, 3245,
     3261, 3262, 3263, 3264, 3265, 3266, 3267, 3268, 3269, 3270,
     3271, 3272, 3273, 3274, 3275, 3281, 3282, 3283, 3284, 3285,
     3286, 3287, 3288, 3289, 3290],
)
TRAIT_FOLLOWUP_MAP["Lab-Research"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Lab-Research", []),
    [3176, 3177, 3178, 3179, 3180, 3191, 3192, 3193, 3194, 3195,
     3196, 3197, 3198, 3199, 3200,
     3216, 3217, 3218, 3219, 3220, 3221, 3222, 3223, 3224, 3225,
     3241, 3242, 3243, 3244, 3245, 3246, 3247, 3248, 3249, 3250,
     3256, 3257, 3258, 3259, 3260,
     3261, 3262, 3263, 3264, 3265, 3266, 3267, 3268, 3269, 3270,
     3276, 3277, 3278, 3279, 3280, 3286, 3287, 3288, 3289, 3290],
)
TRAIT_FOLLOWUP_MAP["Public-Health"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Public-Health", []),
    [3191, 3192, 3193, 3194, 3195, 3221, 3222, 3223, 3224, 3225,
     3251, 3252, 3253, 3254, 3255, 3256, 3257, 3258, 3259, 3260,
     3261, 3262, 3263, 3264, 3265, 3271, 3272, 3273, 3274, 3275,
     3276, 3277, 3278, 3279, 3280, 3281, 3282, 3283, 3284, 3285,
     3286, 3287, 3288, 3289, 3290],
)
TRAIT_FOLLOWUP_MAP["Technical-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Technical-Skill", []),
    [3201, 3202, 3203, 3204, 3205, 3206, 3207, 3208, 3209, 3210,
     3211, 3212, 3213, 3214, 3215, 3216, 3217, 3218, 3219, 3220,
     3221, 3222, 3223, 3224, 3225, 3226, 3227, 3228, 3229, 3230],
)
TRAIT_FOLLOWUP_MAP["Physical-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Physical-Skill", []),
    [3176, 3177, 3178, 3179, 3180, 3191, 3192, 3193, 3194, 3195,
     3206, 3207, 3208, 3209, 3210, 3221, 3222, 3223, 3224, 3225,
     3261, 3262, 3263, 3264, 3265, 3266, 3267, 3268, 3269, 3270,
     3271, 3272, 3273, 3274, 3275, 3281, 3282, 3283, 3284, 3285,
     3286, 3287, 3288, 3289, 3290],
)
TRAIT_FOLLOWUP_MAP["Pharmacy"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Pharmacy", []),
    [3261, 3262, 3263, 3264, 3265, 3266, 3267, 3268, 3269, 3270,
     3271, 3272, 3273, 3274, 3275, 3281, 3282, 3283, 3284, 3285],
)

# ── Healthcare expansion 4: domain entry points ──
DOMAIN_ENTRY_QUESTIONS["healthcare"] = _prepend_unique(
    DOMAIN_ENTRY_QUESTIONS["healthcare"],
    [3291, 3296, 3301, 3306, 3311,   # Radiology & Imaging
     3321, 3326, 3331, 3336, 3341,   # Optometry & Vision Care
     3351, 3356, 3361, 3366, 3371],  # Midwifery & Maternal Health
)

# ── Healthcare expansion 4: trait follow-up prepends ──
TRAIT_FOLLOWUP_MAP["Medical-Lab"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Medical-Lab", []),
    [3291, 3292, 3293, 3294, 3295, 3296, 3297, 3298, 3299, 3300,
     3301, 3302, 3303, 3304, 3305, 3306, 3307, 3308, 3309, 3310,
     3311, 3312, 3313, 3314, 3315, 3316, 3317, 3318, 3319, 3320,
     3321, 3322, 3323, 3324, 3325, 3326, 3327, 3328, 3329, 3330,
     3331, 3332, 3333, 3334, 3335, 3336, 3337, 3338, 3339, 3340,
     3341, 3342, 3343, 3344, 3345, 3346, 3347, 3348, 3349, 3350,
     3351, 3352, 3353, 3354, 3355, 3356, 3357, 3358, 3359, 3360,
     3361, 3362, 3363, 3364, 3365, 3371, 3372, 3373, 3374, 3375,
     3376, 3377, 3378, 3379, 3380],
)
TRAIT_FOLLOWUP_MAP["Technical-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Technical-Skill", []),
    [3291, 3292, 3293, 3294, 3295, 3296, 3297, 3298, 3299, 3300,
     3301, 3302, 3303, 3304, 3305, 3306, 3307, 3308, 3309, 3310,
     3311, 3312, 3313, 3314, 3315, 3316, 3317, 3318, 3319, 3320,
     3321, 3322, 3323, 3324, 3325, 3326, 3327, 3328, 3329, 3330,
     3331, 3332, 3333, 3334, 3335, 3341, 3342, 3343, 3344, 3345,
     3351, 3352, 3353, 3354, 3355, 3361, 3362, 3363, 3364, 3365,
     3371, 3372, 3373, 3374, 3375, 3376, 3377, 3378, 3379, 3380],
)
TRAIT_FOLLOWUP_MAP["Analytical-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Analytical-Skill", []),
    [3291, 3292, 3293, 3294, 3295, 3296, 3297, 3298, 3299, 3300,
     3301, 3302, 3303, 3304, 3305, 3306, 3307, 3308, 3309, 3310,
     3311, 3312, 3313, 3314, 3315, 3316, 3317, 3318, 3319, 3320,
     3321, 3322, 3323, 3324, 3325, 3326, 3327, 3328, 3329, 3330,
     3331, 3332, 3333, 3334, 3335, 3336, 3341, 3346,
     3356, 3357, 3358, 3359, 3360, 3361, 3362, 3363, 3364, 3365,
     3376, 3377, 3378, 3379, 3380],
)
TRAIT_FOLLOWUP_MAP["Patient-Care"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Patient-Care", []),
    [3291, 3292, 3293, 3294, 3295, 3296, 3297, 3298, 3299, 3300,
     3301, 3302, 3303, 3304, 3305, 3306, 3307, 3308, 3309, 3310,
     3311, 3312, 3313, 3314, 3315, 3316, 3317, 3318, 3319, 3320,
     3321, 3322, 3323, 3324, 3325, 3326, 3327, 3328, 3329, 3330,
     3331, 3332, 3333, 3334, 3335, 3336, 3337, 3338, 3339, 3340,
     3341, 3342, 3343, 3344, 3345, 3346, 3347, 3348, 3349, 3350,
     3351, 3352, 3353, 3354, 3355, 3356, 3357, 3358, 3359, 3360,
     3361, 3362, 3363, 3364, 3365, 3366, 3367, 3368, 3369, 3370,
     3371, 3372, 3373, 3374, 3375, 3376, 3377, 3378, 3379, 3380],
)
TRAIT_FOLLOWUP_MAP["People-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("People-Skill", []),
    [3291, 3292, 3293, 3294, 3295, 3301, 3302, 3303, 3304, 3305,
     3306, 3307, 3308, 3309, 3310, 3316, 3317, 3318, 3319, 3320,
     3321, 3322, 3323, 3324, 3325, 3326, 3327, 3328, 3329, 3330,
     3331, 3332, 3333, 3334, 3335, 3336, 3337, 3338, 3339, 3340,
     3341, 3342, 3343, 3344, 3345, 3346, 3347, 3348, 3349, 3350,
     3351, 3352, 3353, 3354, 3355, 3356, 3357, 3358, 3359, 3360,
     3361, 3362, 3363, 3364, 3365, 3366, 3367, 3368, 3369, 3370,
     3371, 3372, 3373, 3374, 3375, 3376, 3377, 3378, 3379, 3380],
)
TRAIT_FOLLOWUP_MAP["Lab-Research"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Lab-Research", []),
    [3291, 3292, 3293, 3294, 3295, 3296, 3297, 3298, 3299, 3300,
     3301, 3302, 3303, 3304, 3305, 3306, 3307, 3308, 3309, 3310,
     3311, 3312, 3313, 3314, 3315, 3316, 3317, 3318, 3319, 3320,
     3326, 3327, 3328, 3329, 3330, 3331, 3332, 3333, 3334, 3335,
     3336, 3337, 3338, 3339, 3340, 3341, 3342, 3343, 3344, 3345,
     3346, 3347, 3348, 3349, 3350,
     3366, 3367, 3368, 3369, 3370],
)
TRAIT_FOLLOWUP_MAP["Health-Admin"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Health-Admin", []),
    [3291, 3292, 3293, 3294, 3295, 3301, 3302, 3303, 3304, 3305,
     3306, 3307, 3308, 3309, 3310, 3311, 3312, 3313, 3314, 3315,
     3316, 3317, 3318, 3319, 3320,
     3331, 3332, 3333, 3334, 3335, 3336, 3337, 3338, 3339, 3340,
     3346, 3347, 3348, 3349, 3350,
     3351, 3352, 3353, 3354, 3355, 3356, 3357, 3358, 3359, 3360,
     3361, 3362, 3363, 3364, 3365, 3366, 3367, 3368, 3369, 3370,
     3376, 3377, 3378, 3379, 3380],
)
TRAIT_FOLLOWUP_MAP["Teaching-Ed"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Teaching-Ed", []),
    [3316, 3317, 3318, 3319, 3320,
     3321, 3322, 3323, 3324, 3325, 3326, 3327, 3328, 3329, 3330,
     3336, 3337, 3338, 3339, 3340, 3341, 3342, 3343, 3344, 3345,
     3346, 3347, 3348, 3349, 3350,
     3351, 3352, 3353, 3354, 3355, 3356, 3357, 3358, 3359, 3360,
     3361, 3362, 3363, 3364, 3365, 3366, 3367, 3368, 3369, 3370,
     3371, 3372, 3373, 3374, 3375, 3376, 3377, 3378, 3379, 3380],
)
TRAIT_FOLLOWUP_MAP["Counseling"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Counseling", []),
    [3301, 3302, 3303, 3304, 3305, 3316, 3317, 3318, 3319, 3320,
     3326, 3327, 3328, 3329, 3330, 3331, 3332, 3333, 3334, 3335,
     3351, 3352, 3353, 3354, 3355, 3356, 3357, 3358, 3359, 3360,
     3361, 3362, 3363, 3364, 3365, 3371, 3372, 3373, 3374, 3375,
     3376, 3377, 3378, 3379, 3380],
)
TRAIT_FOLLOWUP_MAP["Community-Serve"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Community-Serve", []),
    [3336, 3337, 3338, 3339, 3340, 3346, 3347, 3348, 3349, 3350,
     3351, 3352, 3353, 3354, 3355, 3356, 3357, 3358, 3359, 3360,
     3361, 3362, 3363, 3364, 3365, 3366, 3367, 3368, 3369, 3370,
     3371, 3372, 3373, 3374, 3375, 3376, 3377, 3378, 3379, 3380],
)
TRAIT_FOLLOWUP_MAP["Public-Health"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Public-Health", []),
    [3311, 3312, 3313, 3314, 3315,
     3341, 3342, 3343, 3344, 3345, 3346, 3347, 3348, 3349, 3350,
     3351, 3352, 3353, 3354, 3355,
     3366, 3367, 3368, 3369, 3370, 3371, 3372, 3373, 3374, 3375,
     3376, 3377, 3378, 3379, 3380],
)

# ── Social expansion 2: domain entry points ──
DOMAIN_ENTRY_QUESTIONS["social"] = _prepend_unique(
    DOMAIN_ENTRY_QUESTIONS["social"],
    [3621, 3626, 3631, 3651, 3656, 3661, 3711, 3716, 3721,
     3411, 3416, 3421, 3426, 3431,
     3441, 3446, 3451, 3456, 3461,
     3471, 3476, 3481, 3486, 3491,
     3381, 3386, 3391, 3396, 3401],
)

# ── Public service expansion 2: domain entry points ──
DOMAIN_ENTRY_QUESTIONS["public_service"] = _prepend_unique(
    DOMAIN_ENTRY_QUESTIONS["public_service"],
    [3861, 3866, 3871, 3876, 3881,
    3771, 3776, 3781, 3786, 3791,
    3741, 3746, 3751, 3756, 3761,
    3531, 3536, 3541, 3546, 3551,
    3591, 3596, 3601, 3606, 3611,
    3501, 3506, 3511, 3516, 3521,
    3561, 3566, 3571, 3576, 3581],
)
DOMAIN_ENTRY_QUESTIONS["education"] = _prepend_unique(
    DOMAIN_ENTRY_QUESTIONS["education"],
    [3801, 3806, 3811, 3816, 3821,
     3891, 3896, 3901, 3906, 3911,
     3831, 3836, 3841, 3846, 3851,
     3381, 3386, 3391, 3396, 3401],
)
DOMAIN_ENTRY_QUESTIONS["hospitality"] = _prepend_unique(
    DOMAIN_ENTRY_QUESTIONS["hospitality"],
    [3981, 3986, 3991, 3996, 4001,
     4011, 4016, 4021, 4026, 4031],
)
DOMAIN_ENTRY_QUESTIONS["law"] = _prepend_unique(
    DOMAIN_ENTRY_QUESTIONS["law"],
    [3861, 3866, 3871, 3876, 3881,
    3501, 3506, 3511, 3516, 3521,
    3561, 3566, 3571, 3576, 3581],
)
DOMAIN_ENTRY_QUESTIONS["physical"] = _prepend_unique(
    DOMAIN_ENTRY_QUESTIONS["physical"],
    [4041, 4046, 4051, 4056, 4061,
     3951, 3956, 3961, 3966, 3971,
     3921, 3926, 3931, 3936, 3941],
)
DOMAIN_ENTRY_QUESTIONS["public_service"] = _prepend_unique(
    DOMAIN_ENTRY_QUESTIONS["public_service"],
    [4041, 4046, 4051, 4056, 4061,
    3861, 3866, 3871, 3876, 3881,
    3771, 3776, 3781, 3786, 3791,
    3741, 3746, 3751, 3756, 3761,
    3531, 3536, 3541, 3546, 3551,
    3591, 3596, 3601, 3606, 3611,
    3501, 3506, 3511, 3516, 3521,
    3561, 3566, 3571, 3576, 3581],
)

# ── Social expansion 2: trait follow-up prepends ──
TRAIT_FOLLOWUP_MAP["Teaching-Ed"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Teaching-Ed", []),
    [3381, 3382, 3383, 3384, 3385, 3386, 3387, 3388, 3389, 3390,
     3391, 3392, 3393, 3394, 3395, 3396, 3397, 3398, 3399, 3400,
     3401, 3402, 3403, 3404, 3405, 3406, 3407, 3408, 3409, 3410,
     3421, 3422, 3423, 3424, 3425, 3426, 3427, 3428, 3429, 3430,
     3451, 3452, 3453, 3454, 3455,
     3491, 3492, 3493, 3494, 3495],
)
TRAIT_FOLLOWUP_MAP["Social-Work"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Social-Work", []),
    [3411, 3412, 3413, 3414, 3415, 3416, 3417, 3418, 3419, 3420,
     3421, 3422, 3423, 3424, 3425, 3426, 3427, 3428, 3429, 3430,
     3431, 3432, 3433, 3434, 3435, 3436, 3437, 3438, 3439, 3440],
)
TRAIT_FOLLOWUP_MAP["Film-Broadcast"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Film-Broadcast", []),
    [3451, 3452, 3453, 3454, 3455, 3461, 3462, 3463, 3464, 3465,
     3471, 3472, 3473, 3474, 3475, 3476, 3477, 3478, 3479, 3480,
     3481, 3482, 3483, 3484, 3485, 3496, 3497, 3498, 3499, 3500],
)
TRAIT_FOLLOWUP_MAP["Digital-Media"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Digital-Media", []),
    [3471, 3472, 3473, 3474, 3475, 3476, 3477, 3478, 3479, 3480,
     3481, 3482, 3483, 3484, 3485, 3486, 3487, 3488, 3489, 3490,
     3491, 3492, 3493, 3494, 3495, 3496, 3497, 3498, 3499, 3500],
)
TRAIT_FOLLOWUP_MAP["People-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("People-Skill", []),
    [3381, 3382, 3383, 3384, 3385, 3386, 3387, 3388, 3389, 3390,
     3391, 3392, 3393, 3394, 3395, 3401, 3402, 3403, 3404, 3405,
     3411, 3412, 3413, 3414, 3415, 3416, 3417, 3418, 3419, 3420,
     3421, 3422, 3423, 3424, 3425, 3431, 3432, 3433, 3434, 3435,
     3471, 3472, 3473, 3474, 3475, 3476, 3477, 3478, 3479, 3480,
     3481, 3482, 3483, 3484, 3485, 3491, 3492, 3493, 3494, 3495],
)
TRAIT_FOLLOWUP_MAP["Counseling"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Counseling", []),
    [3381, 3382, 3383, 3384, 3385, 3391, 3392, 3393, 3394, 3395,
     3401, 3402, 3403, 3404, 3405,
     3411, 3412, 3413, 3414, 3415, 3416, 3417, 3418, 3419, 3420,
     3421, 3422, 3423, 3424, 3425, 3431, 3432, 3433, 3434, 3435],
)
TRAIT_FOLLOWUP_MAP["Community-Serve"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Community-Serve", []),
    [3401, 3402, 3403, 3404, 3405,
     3411, 3412, 3413, 3414, 3415, 3416, 3417, 3418, 3419, 3420,
     3421, 3422, 3423, 3424, 3425, 3426, 3427, 3428, 3429, 3430,
     3431, 3432, 3433, 3434, 3435, 3436, 3437, 3438, 3439, 3440,
     3441, 3442, 3443, 3444, 3445, 3456, 3457, 3458, 3459, 3460,
     3461, 3462, 3463, 3464, 3465,
     3471, 3472, 3473, 3474, 3475, 3491, 3492, 3493, 3494, 3495],
)
TRAIT_FOLLOWUP_MAP["Admin-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Admin-Skill", []),
    [3391, 3392, 3393, 3394, 3395, 3396, 3397, 3398, 3399, 3400,
     3401, 3402, 3403, 3404, 3405,
     3411, 3412, 3413, 3414, 3415, 3426, 3427, 3428, 3429, 3430,
     3431, 3432, 3433, 3434, 3435,
     3446, 3447, 3448, 3449, 3450, 3456, 3457, 3458, 3459, 3460,
     3466, 3467, 3468, 3469, 3470,
     3481, 3482, 3483, 3484, 3485, 3491, 3492, 3493, 3494, 3495,
     3496, 3497, 3498, 3499, 3500],
)
TRAIT_FOLLOWUP_MAP["Analytical-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Analytical-Skill", []),
    [3381, 3382, 3383, 3384, 3385, 3386, 3387, 3388, 3389, 3390,
     3441, 3442, 3443, 3444, 3445, 3446, 3447, 3448, 3449, 3450,
     3451, 3452, 3453, 3454, 3455, 3456, 3457, 3458, 3459, 3460,
     3461, 3462, 3463, 3464, 3465, 3466, 3467, 3468, 3469, 3470,
     3471, 3472, 3473, 3474, 3475, 3486, 3487, 3488, 3489, 3490,
     3491, 3492, 3493, 3494, 3495, 3496, 3497, 3498, 3499, 3500],
)
TRAIT_FOLLOWUP_MAP["Investigative"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Investigative", []),
    [3441, 3442, 3443, 3444, 3445, 3446, 3447, 3448, 3449, 3450,
     3451, 3452, 3453, 3454, 3455, 3456, 3457, 3458, 3459, 3460,
     3461, 3462, 3463, 3464, 3465, 3466, 3467, 3468, 3469, 3470,
     3471, 3472, 3473, 3474, 3475, 3476, 3477, 3478, 3479, 3480,
     3496, 3497, 3498, 3499, 3500],
)
TRAIT_FOLLOWUP_MAP["Creative-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Creative-Skill", []),
    [3381, 3382, 3383, 3384, 3385, 3441, 3442, 3443, 3444, 3445,
     3451, 3452, 3453, 3454, 3455, 3461, 3462, 3463, 3464, 3465,
     3471, 3472, 3473, 3474, 3475, 3481, 3482, 3483, 3484, 3485],
)
TRAIT_FOLLOWUP_MAP["Technical-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Technical-Skill", []),
    [3386, 3387, 3388, 3389, 3390, 3391, 3392, 3393, 3394, 3395,
     3471, 3472, 3473, 3474, 3475, 3476, 3477, 3478, 3479, 3480,
     3491, 3492, 3493, 3494, 3495],
)
TRAIT_FOLLOWUP_MAP["Marketing-Sales"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Marketing-Sales", []),
    [3471, 3472, 3473, 3474, 3475, 3476, 3477, 3478, 3479, 3480,
     3481, 3482, 3483, 3484, 3485, 3486, 3487, 3488, 3489, 3490,
     3491, 3492, 3493, 3494, 3495, 3496, 3497, 3498, 3499, 3500],
)
TRAIT_FOLLOWUP_MAP["People-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("People-Skill", []),
    [3411, 3412, 3413, 3414, 3415, 3416, 3417, 3418, 3419, 3420,
     3421, 3422, 3423, 3424, 3425, 3431, 3432, 3433, 3434, 3435,
     3471, 3472, 3473, 3474, 3475, 3476, 3477, 3478, 3479, 3480,
     3481, 3482, 3483, 3484, 3485, 3491, 3492, 3493, 3494, 3495,
     3381, 3382, 3383, 3384, 3385, 3386, 3387, 3388, 3389, 3390,
     3391, 3392, 3393, 3394, 3395, 3401, 3402, 3403, 3404, 3405],
)
TRAIT_FOLLOWUP_MAP["Counseling"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Counseling", []),
    [3411, 3412, 3413, 3414, 3415, 3416, 3417, 3418, 3419, 3420,
     3421, 3422, 3423, 3424, 3425, 3431, 3432, 3433, 3434, 3435,
     3381, 3382, 3383, 3384, 3385, 3391, 3392, 3393, 3394, 3395,
     3401, 3402, 3403, 3404, 3405],
)
TRAIT_FOLLOWUP_MAP["Community-Serve"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Community-Serve", []),
    [3411, 3412, 3413, 3414, 3415, 3416, 3417, 3418, 3419, 3420,
     3421, 3422, 3423, 3424, 3425, 3426, 3427, 3428, 3429, 3430,
     3431, 3432, 3433, 3434, 3435, 3436, 3437, 3438, 3439, 3440,
     3441, 3442, 3443, 3444, 3445, 3456, 3457, 3458, 3459, 3460,
     3461, 3462, 3463, 3464, 3465,
     3471, 3472, 3473, 3474, 3475, 3491, 3492, 3493, 3494, 3495,
     3401, 3402, 3403, 3404, 3405],
)
TRAIT_FOLLOWUP_MAP["Legal-Practice"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Legal-Practice", []),
    [3501, 3502, 3503, 3504, 3505, 3506, 3507, 3508, 3509, 3510,
     3511, 3512, 3513, 3514, 3515, 3516, 3517, 3518, 3519, 3520,
     3521, 3522, 3523, 3524, 3525, 3526, 3527, 3528, 3529, 3530,
     3531, 3532, 3533, 3534, 3535, 3546, 3547, 3548, 3549, 3550,
     3591, 3592, 3593, 3594, 3595, 3601, 3602, 3603, 3604, 3605],
)
TRAIT_FOLLOWUP_MAP["Law-Enforce"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Law-Enforce", []),
    [3561, 3562, 3563, 3564, 3565, 3566, 3567, 3568, 3569, 3570,
     3571, 3572, 3573, 3574, 3575, 3576, 3577, 3578, 3579, 3580,
     3581, 3582, 3583, 3584, 3585, 3586, 3587, 3588, 3589, 3590,
     3501, 3502, 3503, 3504, 3505, 3511, 3512, 3513, 3514, 3515,
     3521, 3522, 3523, 3524, 3525],
)
TRAIT_FOLLOWUP_MAP["Forensic-Sci"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Forensic-Sci", []),
    [3561, 3562, 3563, 3564, 3565, 3571, 3572, 3573, 3574, 3575,
     3581, 3582, 3583, 3584, 3585],
)
TRAIT_FOLLOWUP_MAP["Physical-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Physical-Skill", []),
    [3561, 3562, 3563, 3564, 3565, 3566, 3567, 3568, 3569, 3570,
     3586, 3587, 3588, 3589, 3590],
)
TRAIT_FOLLOWUP_MAP["Community-Serve"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Community-Serve", []),
    [3531, 3532, 3533, 3534, 3535, 3536, 3537, 3538, 3539, 3540,
     3551, 3552, 3553, 3554, 3555, 3591, 3592, 3593, 3594, 3595,
     3596, 3597, 3598, 3599, 3600, 3616, 3617, 3618, 3619, 3620,
     3501, 3502, 3503, 3504, 3505, 3511, 3512, 3513, 3514, 3515,
     3571, 3572, 3573, 3574, 3575],
)
TRAIT_FOLLOWUP_MAP["Admin-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Admin-Skill", []),
    [3546, 3547, 3548, 3549, 3550, 3551, 3552, 3553, 3554, 3555,
     3591, 3592, 3593, 3594, 3595, 3596, 3597, 3598, 3599, 3600,
     3601, 3602, 3603, 3604, 3605, 3606, 3607, 3608, 3609, 3610,
     3506, 3507, 3508, 3509, 3510, 3516, 3517, 3518, 3519, 3520,
     3581, 3582, 3583, 3584, 3585],
)
TRAIT_FOLLOWUP_MAP["Analytical-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Analytical-Skill", []),
    [3531, 3532, 3533, 3534, 3535, 3541, 3542, 3543, 3544, 3545,
     3501, 3502, 3503, 3504, 3505, 3506, 3507, 3508, 3509, 3510,
     3591, 3592, 3593, 3594, 3595, 3601, 3602, 3603, 3604, 3605,
     3561, 3562, 3563, 3564, 3565, 3571, 3572, 3573, 3574, 3575],
)
TRAIT_FOLLOWUP_MAP["Investigative"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Investigative", []),
    [3501, 3502, 3503, 3504, 3505, 3526, 3527, 3528, 3529, 3530,
     3541, 3542, 3543, 3544, 3545, 3556, 3557, 3558, 3559, 3560,
     3561, 3562, 3563, 3564, 3565, 3576, 3577, 3578, 3579, 3580,
     3606, 3607, 3608, 3609, 3610],
)
TRAIT_FOLLOWUP_MAP["People-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("People-Skill", []),
    [3536, 3537, 3538, 3539, 3540, 3556, 3557, 3558, 3559, 3560,
     3596, 3597, 3598, 3599, 3600, 3611, 3612, 3613, 3614, 3615,
     3501, 3502, 3503, 3504, 3505, 3516, 3517, 3518, 3519, 3520,
     3571, 3572, 3573, 3574, 3575],
)
TRAIT_FOLLOWUP_MAP["Admin-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Admin-Skill", []),
    [3591, 3592, 3593, 3594, 3595, 3596, 3597, 3598, 3599, 3600,
     3601, 3602, 3603, 3604, 3605, 3606, 3607, 3608, 3609, 3610,
     3546, 3547, 3548, 3549, 3550, 3551, 3552, 3553, 3554, 3555],
)
TRAIT_FOLLOWUP_MAP["Community-Serve"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Community-Serve", []),
    [3621, 3622, 3623, 3624, 3625, 3631, 3632, 3633, 3634, 3635,
     3651, 3652, 3653, 3654, 3655, 3666, 3667, 3668, 3669, 3670,
     3711, 3712, 3713, 3714, 3715, 3726, 3727, 3728, 3729, 3730,
     3741, 3742, 3743, 3744, 3745, 3766, 3767, 3768, 3769, 3770],
)
TRAIT_FOLLOWUP_MAP["People-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("People-Skill", []),
    [3621, 3622, 3623, 3624, 3625, 3636, 3637, 3638, 3639, 3640,
     3651, 3652, 3653, 3654, 3655, 3661, 3662, 3663, 3664, 3665,
     3681, 3682, 3683, 3684, 3685, 3696, 3697, 3698, 3699, 3700,
     3711, 3712, 3713, 3714, 3715, 3721, 3722, 3723, 3724, 3725,
     3746, 3747, 3748, 3749, 3750, 3751, 3752, 3753, 3754, 3755],
)
TRAIT_FOLLOWUP_MAP["Teaching-Ed"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Teaching-Ed", []),
    [3621, 3622, 3623, 3624, 3625, 3641, 3642, 3643, 3644, 3645,
     3651, 3652, 3653, 3654, 3655, 3661, 3662, 3663, 3664, 3665,
     3681, 3682, 3683, 3684, 3685, 3686, 3687, 3688, 3689, 3690,
     3706, 3707, 3708, 3709, 3710],
)
TRAIT_FOLLOWUP_MAP["Digital-Media"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Digital-Media", []),
    [3621, 3622, 3623, 3624, 3625, 3626, 3627, 3628, 3629, 3630,
     3636, 3637, 3638, 3639, 3640, 3646, 3647, 3648, 3649, 3650],
)
TRAIT_FOLLOWUP_MAP["Marketing-Sales"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Marketing-Sales", []),
    [3621, 3622, 3623, 3624, 3625, 3626, 3627, 3628, 3629, 3630,
     3636, 3637, 3638, 3639, 3640, 3646, 3647, 3648, 3649, 3650],
)
TRAIT_FOLLOWUP_MAP["Social-Work"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Social-Work", []),
    [3651, 3652, 3653, 3654, 3655, 3656, 3657, 3658, 3659, 3660,
     3671, 3672, 3673, 3674, 3675, 3711, 3712, 3713, 3714, 3715,
     3726, 3727, 3728, 3729, 3730],
)
TRAIT_FOLLOWUP_MAP["Analytical-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Analytical-Skill", []),
    [3626, 3627, 3628, 3629, 3630, 3631, 3632, 3633, 3634, 3635,
     3661, 3662, 3663, 3664, 3665, 3666, 3667, 3668, 3669, 3670,
     3686, 3687, 3688, 3689, 3690, 3701, 3702, 3703, 3704, 3705,
     3711, 3712, 3713, 3714, 3715, 3716, 3717, 3718, 3719, 3720,
     3741, 3742, 3743, 3744, 3745, 3756, 3757, 3758, 3759, 3760],
)
TRAIT_FOLLOWUP_MAP["Investigative"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Investigative", []),
    [3631, 3632, 3633, 3634, 3635, 3666, 3667, 3668, 3669, 3670,
     3686, 3687, 3688, 3689, 3690, 3691, 3692, 3693, 3694, 3695,
     3711, 3712, 3713, 3714, 3715, 3716, 3717, 3718, 3719, 3720,
     3741, 3742, 3743, 3744, 3745, 3761, 3762, 3763, 3764, 3765],
)
TRAIT_FOLLOWUP_MAP["Legal-Practice"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Legal-Practice", []),
    [3741, 3742, 3743, 3744, 3745, 3746, 3747, 3748, 3749, 3750,
     3751, 3752, 3753, 3754, 3755, 3766, 3767, 3768, 3769, 3770],
)
TRAIT_FOLLOWUP_MAP["Admin-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Admin-Skill", []),
    [3631, 3632, 3633, 3634, 3635, 3646, 3647, 3648, 3649, 3650,
     3656, 3657, 3658, 3659, 3660, 3676, 3677, 3678, 3679, 3680,
     3741, 3742, 3743, 3744, 3745, 3756, 3757, 3758, 3759, 3760],
)
TRAIT_FOLLOWUP_MAP["Community-Serve"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Community-Serve", []),
    [3651, 3652, 3653, 3654, 3655, 3666, 3667, 3668, 3669, 3670,
     3711, 3712, 3713, 3714, 3715, 3726, 3727, 3728, 3729, 3730,
     3741, 3742, 3743, 3744, 3745, 3766, 3767, 3768, 3769, 3770,
     3621, 3622, 3623, 3624, 3625, 3631, 3632, 3633, 3634, 3635],
)
TRAIT_FOLLOWUP_MAP["People-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("People-Skill", []),
    [3746, 3747, 3748, 3749, 3750, 3751, 3752, 3753, 3754, 3755,
     3651, 3652, 3653, 3654, 3655, 3661, 3662, 3663, 3664, 3665,
     3711, 3712, 3713, 3714, 3715, 3721, 3722, 3723, 3724, 3725,
     3681, 3682, 3683, 3684, 3685, 3696, 3697, 3698, 3699, 3700,
     3621, 3622, 3623, 3624, 3625, 3636, 3637, 3638, 3639, 3640],
)
TRAIT_FOLLOWUP_MAP["Analytical-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Analytical-Skill", []),
    [3711, 3712, 3713, 3714, 3715, 3716, 3717, 3718, 3719, 3720,
     3741, 3742, 3743, 3744, 3745, 3756, 3757, 3758, 3759, 3760,
     3686, 3687, 3688, 3689, 3690, 3701, 3702, 3703, 3704, 3705,
     3661, 3662, 3663, 3664, 3665, 3666, 3667, 3668, 3669, 3670,
     3626, 3627, 3628, 3629, 3630, 3631, 3632, 3633, 3634, 3635],
)
TRAIT_FOLLOWUP_MAP["Investigative"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Investigative", []),
    [3711, 3712, 3713, 3714, 3715, 3716, 3717, 3718, 3719, 3720,
     3741, 3742, 3743, 3744, 3745, 3761, 3762, 3763, 3764, 3765,
     3686, 3687, 3688, 3689, 3690, 3691, 3692, 3693, 3694, 3695,
     3666, 3667, 3668, 3669, 3670, 3631, 3632, 3633, 3634, 3635],
)
TRAIT_FOLLOWUP_MAP["Admin-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Admin-Skill", []),
    [3741, 3742, 3743, 3744, 3745, 3756, 3757, 3758, 3759, 3760,
     3656, 3657, 3658, 3659, 3660, 3676, 3677, 3678, 3679, 3680,
     3631, 3632, 3633, 3634, 3635, 3646, 3647, 3648, 3649, 3650],
)
TRAIT_FOLLOWUP_MAP["Teaching-Ed"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Teaching-Ed", []),
    [3801, 3802, 3803, 3804, 3805, 3806, 3807, 3808, 3809, 3810,
     3811, 3812, 3813, 3814, 3815, 3891, 3892, 3893, 3894, 3895,
     3896, 3897, 3898, 3899, 3900, 3901, 3902, 3903, 3904, 3905,
     3831, 3832, 3833, 3834, 3835, 3841, 3842, 3843, 3844, 3845,
     3771, 3772, 3773, 3774, 3775],
)
TRAIT_FOLLOWUP_MAP["Counseling"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Counseling", []),
    [3801, 3802, 3803, 3804, 3805, 3811, 3812, 3813, 3814, 3815,
     3821, 3822, 3823, 3824, 3825, 3891, 3892, 3893, 3894, 3895,
     3901, 3902, 3903, 3904, 3905, 3911, 3912, 3913, 3914, 3915],
)
TRAIT_FOLLOWUP_MAP["Creative-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Creative-Skill", []),
    [3801, 3802, 3803, 3804, 3805, 3816, 3817, 3818, 3819, 3820,
     3891, 3892, 3893, 3894, 3895, 3906, 3907, 3908, 3909, 3910],
)
TRAIT_FOLLOWUP_MAP["Admin-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Admin-Skill", []),
    [3831, 3832, 3833, 3834, 3835, 3846, 3847, 3848, 3849, 3850,
     3861, 3862, 3863, 3864, 3865, 3876, 3877, 3878, 3879, 3880,
     3891, 3892, 3893, 3894, 3895, 3906, 3907, 3908, 3909, 3910],
)
TRAIT_FOLLOWUP_MAP["Investigative"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Investigative", []),
    [3771, 3772, 3773, 3774, 3775, 3776, 3777, 3778, 3779, 3780,
     3831, 3832, 3833, 3834, 3835, 3836, 3837, 3838, 3839, 3840,
     3861, 3862, 3863, 3864, 3865, 3871, 3872, 3873, 3874, 3875],
)
TRAIT_FOLLOWUP_MAP["Analytical-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Analytical-Skill", []),
    [3771, 3772, 3773, 3774, 3775, 3781, 3782, 3783, 3784, 3785,
     3801, 3802, 3803, 3804, 3805, 3806, 3807, 3808, 3809, 3810,
     3831, 3832, 3833, 3834, 3835, 3836, 3837, 3838, 3839, 3840,
     3861, 3862, 3863, 3864, 3865, 3866, 3867, 3868, 3869, 3870],
)
TRAIT_FOLLOWUP_MAP["People-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("People-Skill", []),
    [3771, 3772, 3773, 3774, 3775, 3786, 3787, 3788, 3789, 3790,
     3801, 3802, 3803, 3804, 3805, 3811, 3812, 3813, 3814, 3815,
     3831, 3832, 3833, 3834, 3835, 3851, 3852, 3853, 3854, 3855,
     3861, 3862, 3863, 3864, 3865, 3871, 3872, 3873, 3874, 3875,
     3891, 3892, 3893, 3894, 3895, 3901, 3902, 3903, 3904, 3905],
)
TRAIT_FOLLOWUP_MAP["Community-Serve"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Community-Serve", []),
    [3771, 3772, 3773, 3774, 3775, 3791, 3792, 3793, 3794, 3795,
     3801, 3802, 3803, 3804, 3805, 3816, 3817, 3818, 3819, 3820,
     3831, 3832, 3833, 3834, 3835, 3841, 3842, 3843, 3844, 3845,
     3861, 3862, 3863, 3864, 3865, 3886, 3887, 3888, 3889, 3890,
     3891, 3892, 3893, 3894, 3895, 3901, 3902, 3903, 3904, 3905],
)
TRAIT_FOLLOWUP_MAP["Legal-Practice"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Legal-Practice", []),
    [3771, 3772, 3773, 3774, 3775, 3796, 3797, 3798, 3799, 3800,
     3861, 3862, 3863, 3864, 3865, 3866, 3867, 3868, 3869, 3870,
     3871, 3872, 3873, 3874, 3875, 3881, 3882, 3883, 3884, 3885],
)
TRAIT_FOLLOWUP_MAP["Sports-Ed"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Sports-Ed", []),
    [3921, 3922, 3923, 3924, 3925, 3926, 3927, 3928, 3929, 3930,
     3931, 3932, 3933, 3934, 3935, 3951, 3952, 3953, 3954, 3955,
     3971, 3972, 3973, 3974, 3975],
)
TRAIT_FOLLOWUP_MAP["Physical-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Physical-Skill", []),
    [3921, 3922, 3923, 3924, 3925, 3936, 3937, 3938, 3939, 3940,
     3951, 3952, 3953, 3954, 3955, 3961, 3962, 3963, 3964, 3965,
     4041, 4042, 4043, 4044, 4045, 4046, 4047, 4048, 4049, 4050],
)
TRAIT_FOLLOWUP_MAP["Rehab-Therapy"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Rehab-Therapy", []),
    [3926, 3927, 3928, 3929, 3930, 3956, 3957, 3958, 3959, 3960,
     3961, 3962, 3963, 3964, 3965, 3981, 3982, 3983, 3984, 3985],
)
TRAIT_FOLLOWUP_MAP["Hospitality-Svc"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Hospitality-Svc", []),
    [3981, 3982, 3983, 3984, 3985, 3991, 3992, 3993, 3994, 3995,
     4011, 4012, 4013, 4014, 4015, 4021, 4022, 4023, 4024, 4025,
     4031, 4032, 4033, 4034, 4035],
)
TRAIT_FOLLOWUP_MAP["Tourism-Travel"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Tourism-Travel", []),
    [3981, 3982, 3983, 3984, 3985, 3986, 3987, 3988, 3989, 3990,
     4006, 4007, 4008, 4009, 4010, 4036, 4037, 4038, 4039, 4040],
)
TRAIT_FOLLOWUP_MAP["Marketing-Sales"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Marketing-Sales", []),
    [3991, 3992, 3993, 3994, 3995, 4001, 4002, 4003, 4004, 4005,
     4011, 4012, 4013, 4014, 4015, 4026, 4027, 4028, 4029, 4030],
)
TRAIT_FOLLOWUP_MAP["Law-Enforce"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Law-Enforce", []),
    [4041, 4042, 4043, 4044, 4045, 4051, 4052, 4053, 4054, 4055,
     4061, 4062, 4063, 4064, 4065],
)
TRAIT_FOLLOWUP_MAP["Investigative"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Investigative", []),
    [3951, 3952, 3953, 3954, 3955, 3966, 3967, 3968, 3969, 3970,
     4041, 4042, 4043, 4044, 4045, 4056, 4057, 4058, 4059, 4060],
)
TRAIT_FOLLOWUP_MAP["Analytical-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Analytical-Skill", []),
    [3956, 3957, 3958, 3959, 3960, 3966, 3967, 3968, 3969, 3970,
     4056, 4057, 4058, 4059, 4060, 4061, 4062, 4063, 4064, 4065,
     4016, 4017, 4018, 4019, 4020],
)
TRAIT_FOLLOWUP_MAP["People-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("People-Skill", []),
    [3921, 3922, 3923, 3924, 3925, 3986, 3987, 3988, 3989, 3990,
     4011, 4012, 4013, 4014, 4015, 4046, 4047, 4048, 4049, 4050,
     4066, 4067, 4068, 4069, 4070],
)
TRAIT_FOLLOWUP_MAP["Community-Serve"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Community-Serve", []),
    [3931, 3932, 3933, 3934, 3935, 3996, 3997, 3998, 3999, 4000,
     4031, 4032, 4033, 4034, 4035, 4051, 4052, 4053, 4054, 4055,
     4066, 4067, 4068, 4069, 4070],
)
TRAIT_FOLLOWUP_MAP["Teaching-Ed"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Teaching-Ed", []),
    [3921, 3922, 3923, 3924, 3925, 3941, 3942, 3943, 3944, 3945,
     3971, 3972, 3973, 3974, 3975],
)
TRAIT_FOLLOWUP_MAP["Admin-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Admin-Skill", []),
    [3946, 3947, 3948, 3949, 3950, 4001, 4002, 4003, 4004, 4005,
     4016, 4017, 4018, 4019, 4020, 4021, 4022, 4023, 4024, 4025],
)
TRAIT_FOLLOWUP_MAP["Food-Science"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Food-Science", []),
    [4071, 4072, 4073, 4074, 4075, 4081, 4082, 4083, 4084, 4085,
     4091, 4092, 4093, 4094, 4095],
)
TRAIT_FOLLOWUP_MAP["Lab-Research"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Lab-Research", []),
    [4076, 4077, 4078, 4079, 4080, 4106, 4107, 4108, 4109, 4110],
)
TRAIT_FOLLOWUP_MAP["Nutrition-Diet"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Nutrition-Diet", []),
    [4086, 4087, 4088, 4089, 4090],
)
TRAIT_FOLLOWUP_MAP["Culinary-Arts"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Culinary-Arts", []),
    [4131, 4132, 4133, 4134, 4135, 4076, 4077, 4078, 4079, 4080],
)
TRAIT_FOLLOWUP_MAP["Patient-Care"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Patient-Care", []),
    [4101, 4102, 4103, 4104, 4105, 4126, 4127, 4128, 4129, 4130],
)
TRAIT_FOLLOWUP_MAP["Investigative"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Investigative", []),
    [4106, 4107, 4108, 4109, 4110, 4116, 4117, 4118, 4119, 4120],
)
TRAIT_FOLLOWUP_MAP["Agri-Nature"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Agri-Nature", []),
    [4111, 4112, 4113, 4114, 4115],
)
TRAIT_FOLLOWUP_MAP["Hospitality-Svc"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Hospitality-Svc", []),
    [4136, 4137, 4138, 4139, 4140, 4141, 4142, 4143, 4144, 4145],
)
TRAIT_FOLLOWUP_MAP["Startup-Venture"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Startup-Venture", []),
    [4146, 4147, 4148, 4149, 4150],
)
TRAIT_FOLLOWUP_MAP["Teaching-Ed"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Teaching-Ed", []),
    [4161, 4162, 4163, 4164, 4165, 4181, 4182, 4183, 4184, 4185],
)
TRAIT_FOLLOWUP_MAP["Technical-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Technical-Skill", []),
    [4166, 4167, 4168, 4169, 4170, 4171, 4172, 4173, 4174, 4175],
)
TRAIT_FOLLOWUP_MAP["Mechanical-Design"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Mechanical-Design", []),
    [4171, 4172, 4173, 4174, 4175],
)
TRAIT_FOLLOWUP_MAP["Community-Serve"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("Community-Serve", []),
    [4111, 4112, 4113, 4114, 4115, 4176, 4177, 4178, 4179, 4180],
)
TRAIT_FOLLOWUP_MAP["People-Skill"] = _prepend_unique(
    TRAIT_FOLLOWUP_MAP.get("People-Skill", []),
    [4156, 4157, 4158, 4159, 4160, 4176, 4177, 4178, 4179, 4180],
)

# ==================== APPLY EXPANSION QID REMAP ====================
# Expansion dedup removed rephrased duplicate questions from the pool.
# Remap stale QIDs in TRAIT_FOLLOWUP_MAP and DOMAIN_ENTRY_QUESTIONS so
# they point to the canonical (kept) question IDs.
try:
    from data.questions_enhanced import EXPANSION_QID_REMAP as _QID_REMAP
    if _QID_REMAP:
        for _trait, _qids in TRAIT_FOLLOWUP_MAP.items():
            _seen = set()
            _remapped = []
            for _qid in _qids:
                _resolved = _QID_REMAP.get(_qid, _qid)
                if _resolved not in _seen:
                    _remapped.append(_resolved)
                    _seen.add(_resolved)
            TRAIT_FOLLOWUP_MAP[_trait] = _remapped
        for _domain, _qids in DOMAIN_ENTRY_QUESTIONS.items():
            _seen = set()
            _remapped = []
            for _qid in _qids:
                _resolved = _QID_REMAP.get(_qid, _qid)
                if _resolved not in _seen:
                    _remapped.append(_resolved)
                    _seen.add(_resolved)
            DOMAIN_ENTRY_QUESTIONS[_domain] = _remapped
except ImportError:
    pass

# ==================== APPLY SEMANTIC QID REMAP ====================
# Semantic dedup removed same-meaning questions (different options but
# identical conceptual question) from the pool. Remap stale QIDs.
try:
    from data.questions_enhanced import SEMANTIC_QID_REMAP as _SEM_REMAP
    if _SEM_REMAP:
        for _trait, _qids in TRAIT_FOLLOWUP_MAP.items():
            _seen = set()
            _remapped = []
            for _qid in _qids:
                _resolved = _SEM_REMAP.get(_qid, _qid)
                if _resolved not in _seen:
                    _remapped.append(_resolved)
                    _seen.add(_resolved)
            TRAIT_FOLLOWUP_MAP[_trait] = _remapped
        for _domain, _qids in DOMAIN_ENTRY_QUESTIONS.items():
            _seen = set()
            _remapped = []
            for _qid in _qids:
                _resolved = _SEM_REMAP.get(_qid, _qid)
                if _resolved not in _seen:
                    _remapped.append(_resolved)
                    _seen.add(_resolved)
            DOMAIN_ENTRY_QUESTIONS[_domain] = _remapped
except ImportError:
    pass

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
    "web_tech": "technology", "multimedia": "creative", "software_eng": "technology",
    "networking_skill": "technology", "database_skill": "technology", "mobile_dev": "technology",
    "ux_ui": "technology", "health_info": "healthcare",
    "medical": "healthcare", "nursing": "healthcare", "pharmacy": "healthcare",
    "medicine": "healthcare", "healthcare": "healthcare",
    "physical_therapy": "healthcare", "nutrition": "healthcare", "psychology": "healthcare",
    "medical_tech": "healthcare", "dentistry": "healthcare", "health": "healthcare",
    "first_aid": "healthcare", "counseling": "healthcare", "dietetics": "healthcare",
    "mental_health": "healthcare", "public_health": "healthcare", "midwifery": "healthcare",
    "radiologic": "healthcare", "occupational_therapy": "healthcare",
    "speech_therapy": "healthcare", "respiratory": "healthcare", "radiology": "healthcare",
    "optometry": "healthcare", "patient_care": "healthcare", "elderly_care": "healthcare",
    "lab_equipment": "healthcare", "respiratory_therapy": "healthcare",
    "speech_pathology": "healthcare",
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
    "law": "public_service", "justice": "public_service", "legal": "public_service",
    "politics": "public_service", "government": "public_service", "governance": "public_service",
    "criminology": "public_service", "public_safety": "public_service",
    "social": "social", "communication": "social",
    "philosophy": "public_service", "ethics": "public_service", "history": "social",
    "conflict_resolution": "public_service", "forensics": "public_service",
    "social_work": "social", "human_rights": "public_service",
    "diplomacy": "public_service", "public_policy": "public_service",
    "public_admin": "public_service", "public_administration": "public_service",
    "intl_studies": "public_service",
    "international_studies": "public_service",
    "sociology": "social", "linguistics": "public_service",
    "language": "public_service", "languages": "public_service",
    "dev_communication": "social", "development_communication": "social",
    "community_dev": "social", "community_development": "social",
    "special_needs": "education", "early_childhood_education": "education",
    "library_information_science": "education",
    "legal_mgmt": "public_service", "legal_management": "public_service", "case_analysis": "public_service",
    "policy_analysis": "public_service",
    "culture": "social", "journalism": "social", "community": "social",
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
    "tourism_hospitality": "hospitality", "tourism_&_hospitality": "hospitality",
    "tourism_and_hospitality": "hospitality",
    "customer_service": "hospitality", "hotel": "hospitality", "culinary": "hospitality",
    "baking": "hospitality", "travel": "hospitality", "events": "hospitality",
    "restaurant": "hospitality", "resort": "hospitality",
    "hotel_mgmt": "hospitality", "culinary_mgmt": "hospitality",
    "hotel_&_resort_management": "hospitality", "hotel_and_resort_management": "hospitality",
    "tvet": "hospitality", "food_safety": "hospitality",
    "sports": "physical", "sports_fitness": "physical", "military": "physical",
    "sport_&_fitness": "physical", "sport_and_fitness": "physical",
    "sports_and_fitness": "physical",
    "driving": "physical", "fitness": "physical", "athletics": "physical",
    "gym": "physical", "exercise": "physical", "martial_arts": "physical",
    "exercise_science": "physical", "swimming": "physical",
    "exercise_&_sports_science": "physical", "exercise_and_sports_science": "physical",
    "military_defense": "physical", "military_&_defense": "physical",
    "military_and_defense": "physical",
    "heavy_equipment": "physical", "carpentry": "physical", "plumbing": "physical",
    "welding": "physical", "auto_repair": "physical",
    "acting": "creative", "illustration": "creative",
    "fashion_design": "creative", "animation_skill": "creative",
    "interior_styling": "creative", "content_creation": "creative",
    "animal_handling": "agriculture", "fishing": "agriculture",
    "sewing": "creative", "coaching": "education",
    "leadership": "business", "teamwork": "public_service",
    "critical_thinking": "science", "problem_solving": "technology",
    "time_management": "business", "organization": "business",
    "communication_skill": "public_service", "adaptability": "business",
    "empathy": "healthcare", "patience": "education",
    "attention_to_detail": "science", "multitasking": "business",
}

INTEREST_DOMAIN_MAP.update({
    "culinary_&_food_science": "science",
    "culinary_and_food_science": "science",
    "culinary_food_science": "science",
    "agriculture_&_farming": "agriculture",
    "agriculture_and_farming": "agriculture",
    "agriculture_farming": "agriculture",
    "forestry_&_natural_resources": "agriculture",
    "forestry_and_natural_resources": "agriculture",
    "forestry_natural_resources": "agriculture",
    "fisheries_&_agriculture": "agriculture",
    "fisheries_and_agriculture": "agriculture",
    "fisheries_agriculture": "agriculture",
    "veterinary_&_animal_science": "agriculture",
    "veterinary_and_animal_science": "agriculture",
    "veterinary_animal_science": "agriculture",
    "culinary_management": "hospitality",
    "technical-vocational_training": "education",
    "technical_vocational_training": "education",
})

# Maps SHS strand to default domain
STRAND_DOMAIN_MAP = {
    "STEM": "technology", "ABM": "business", "HUMSS": "education",
    "TVL": "technology", "GAS": None, "SPORTS": "physical", "ARTS": "creative",
}

# ==================== INTEREST KEYWORD → QUESTION CATEGORY PATTERNS ====================
# Maps user profile interest names to substrings that match question categories.
# Used to pre-filter the question pool so users get questions directly related
# to their stated interests.
INTEREST_CATEGORY_KEYWORDS = {
    # Technology
    "programming": ["Programming & Coding", "Software Engineering", "Computers & IT"],
    "programming_&_coding": ["Programming & Coding", "Software Engineering", "Computers & IT"],
    "coding": ["Programming & Coding", "Software Engineering"],
    "computers_&_it": ["Computers & IT", "Programming & Coding", "Software Engineering", "Data & Analytics", "Cybersecurity", "Computer Networking", "Web & Mobile", "Database & Information"],
    "ai_&_machine_learning": ["AI & Machine Learning", "Data & Analytics", "Robotics & Automation"],
    "machine_learning": ["AI & Machine Learning", "Data & Analytics"],
    "artificial_intelligence": ["AI & Machine Learning", "Robotics & Automation"],
    "cybersecurity": ["Cybersecurity", "Computer Networking"],
    "software": ["Software Engineering", "Programming & Coding", "Computers & IT"],
    "software_eng": ["Software Engineering", "Programming & Coding"],
    "web_development": ["Web & Mobile Technologies", "Programming & Coding"],
    "web_design": ["Web & Mobile Technologies"],
    "web_tech": ["Web & Mobile Technologies"],
    "mobile_app": ["Web & Mobile Technologies"],
    "mobile_dev": ["Web & Mobile Technologies"],
    "game_dev": ["Game Development", "Animation"],
    "game_development": ["Game Development"],
    "data": ["Data & Analytics", "Database & Information"],
    "data_analysis": ["Data & Analytics"],
    "database": ["Database & Information Systems"],
    "networking": ["Computer Networking"],
    "robotics": ["Robotics & Automation"],
    "multimedia": ["Multimedia & Digital Entertainment", "Film & Media"],
    "ux_ui": ["Web & Mobile Technologies", "Art & Design"],
    "cloud_computing": ["Computers & IT", "Software Engineering"],
    "health_info": ["Health Information Technology"],
    # Healthcare
    "medical": ["Healthcare General", "Medicine"],
    "nursing": ["Nursing", "Patient Care"],
    "pharmacy": ["Pharmacy"],
    "health": ["Healthcare General", "Health Information"],
    "nutrition": ["Nutrition"],
    "psychology": ["Psychology"],
    "physical_therapy": ["Physical Therapy"],
    "dentistry": ["Dentistry"],
    # Engineering
    "engineering": ["Engineering"],
    "mechanical": ["Mechanical Systems"],
    "electrical": ["Electrical & Electronics"],
    "civil": ["Civil & Construction"],
    "architecture": ["Architecture & Interior Design"],
    "industrial": ["Industrial & Manufacturing"],
    "aeronautical": ["Aeronautical & Aerospace"],
    "geodetic": ["Geodetic & Surveying"],
    "robotics": ["Robotics & Automation"],
    # Business
    "business": ["Business", "Management", "Entrepreneurship"],
    "finance": ["Finance & Banking", "Accounting"],
    "marketing": ["Marketing & Advertising"],
    "accounting": ["Accounting"],
    "economics": ["Economics"],
    "management": ["Management & Administration"],
    "entrepreneurship": ["Startup & Innovation", "Business & Entrepreneurship"],
    "human_resources": ["Human Resource Management"],
    "real_estate": ["Real Estate & Property"],
    "operations": ["Operations & Supply Chain"],
    "customs": ["Customs & International Trade"],
    "office_admin": ["Office Administration"],
    # Creative/Arts
    "art": ["Art & Design", "Fine Arts", "Arts General"],
    "arts": ["Art & Design", "Fine Arts & Painting", "Arts General"],
    "arts_and_design": ["Art & Design", "Fine Arts & Painting", "Advertising & Graphic Arts"],
    "music_and_arts": ["Music & Performance", "Music Production & Audio", "Fine Arts & Painting", "Art & Design"],
    "multimedia_arts": ["Animation & Multimedia", "Multimedia & Digital Entertainment", "Art & Design"],
    "fine_arts": ["Fine Arts & Painting"],
    "music": ["Music"],
    "music_production": ["Music Production & Audio", "Music & Performance"],
    "film": ["Film & Media Production"],
    "writing": ["Writing & Literature"],
    "photography": ["Photography"],
    "animation": ["Animation"],
    "fashion": ["Fashion & Textile Design", "Clothing & Textile Technology"],
    "clothing_tech": ["Clothing & Textile Technology", "Fashion & Textile Design"],
    "graphic_design": ["Advertising & Graphic Arts", "Art & Design"],
    "design": ["Art & Design", "Architecture & Interior Design"],
    "advertising_arts": ["Advertising & Graphic Arts"],
    "filmmaking": ["Film & Media Production"],
    "theater": ["Theater & Performing Arts"],
    # Science
    "science": ["Science & Research", "Science General"],
    "biology": ["Biology & Life Sciences", "Biotechnology & Genetics", "Marine Science & Oceanography"],
    "chemistry": ["Chemistry"],
    "physics": ["Physics"],
    "environment": ["Environment & Nature", "Environmental Planning"],
    "biotechnology": ["Biotechnology & Genetics"],
    "earth_science": ["Earth Science & Geology", "Environment & Nature", "Environmental Planning & Sustainability", "Geodetic & Surveying", "Weather & Atmospheric Science"],
    "geology": ["Earth Science & Geology", "Geodetic & Surveying"],
    "earth": ["Earth Science & Geology", "Environment & Nature"],
    "meteorology": ["Weather & Atmospheric Science"],
    "food_science": ["Culinary & Food Science", "Food Science"],
    # Education
    "education": ["Education & Teaching"],
    "teaching": ["Education & Teaching"],
    # Agriculture
    "agriculture": ["Agriculture & Farming", "Agriculture", "Agribusiness"],
    "farming": ["Agriculture & Farming"],
    "veterinary": ["Veterinary & Animal Science"],
    "fishery": ["Fisheries & Agriculture", "Fisheries & Aquaculture"],
    "fisheries": ["Fisheries & Agriculture", "Fisheries & Aquaculture"],
    "forestry": ["Forestry & Natural Resources"],
    # Maritime
    "maritime": ["Maritime", "Marine", "Maritime & Seafaring", "Maritime General", "Marine Engineering", "Marine Transportation & Navigation", "Marine Science & Oceanography"],
    "marine": ["Marine", "Marine Engineering", "Marine Transportation & Navigation", "Marine Science & Oceanography", "Maritime", "Maritime & Seafaring", "Maritime General"],
    "marine_transport": ["Marine Transportation & Navigation", "Maritime & Seafaring", "Maritime General", "Marine Engineering"],
    "marine_transport": ["Marine Transportation & Navigation", "Maritime & Seafaring", "Maritime General", "Marine Engineering"],
    "marine_transportation": ["Marine Transportation & Navigation", "Maritime & Seafaring"],
    "marine_engineering": ["Marine Engineering", "Maritime"],
    "marine_science": ["Marine Science & Oceanography", "Marine"],
    "oceanography": ["Marine Science & Oceanography"],
    "seafaring": ["Maritime & Seafaring", "Maritime", "Marine"],
    "aviation": ["Aviation & Aerospace", "Aeronautical"],
    # Hospitality
    "tourism": ["Tourism & Hospitality"],
    "tourism_hospitality": ["Tourism & Hospitality"],
    "tourism_&_hospitality": ["Tourism & Hospitality"],
    "tourism_and_hospitality": ["Tourism & Hospitality"],
    "cooking": ["Culinary"],
    "culinary": ["Culinary"],
    "hotel": ["Hotel & Resort Management"],
    "hotel_&_resort_management": ["Hotel & Resort Management"],
    "hotel_and_resort_management": ["Hotel & Resort Management"],
    # Physical/Sports
    "sports": ["Sports & Fitness", "Exercise"],
    "sport_&_fitness": ["Sports & Fitness"],
    "sport_and_fitness": ["Sports & Fitness"],
    "sports_fitness": ["Sports & Fitness"],
    "sports_and_fitness": ["Sports & Fitness"],
    "exercise_&_sports_science": ["Exercise & Sports Science"],
    "exercise_and_sports_science": ["Exercise & Sports Science"],
    "military": ["Military & Defense"],
    "military_defense": ["Military & Defense"],
    "military_&_defense": ["Military & Defense"],
    "military_and_defense": ["Military & Defense"],
    # Social/Public Service
    "law": ["Law & Justice", "Legal"],
    "justice": ["Law & Justice", "Legal"],
    "legal": ["Law & Justice", "Legal"],
    "criminology": ["Criminology & Public Safety"],
    "public_safety": ["Criminology & Public Safety"],
    "social": ["Sociology", "Social Work & Community"],
    "social_work": ["Social Work & Community"],
    "community": ["Community Development", "Social Work & Community"],
    "history": ["History & Culture"],
    "culture": ["History & Culture"],
    "communication": ["Development Communication", "Communication & Journalism"],
    "journalism": ["Communication & Journalism"],
    "media": ["Communication & Journalism"],
    "politics": ["Politics & Government"],
    "government": ["Politics & Government", "Public Administration"],
    "governance": ["Politics & Government", "Public Administration"],
    "public_admin": ["Public Administration"],
    "public_administration": ["Public Administration"],
    "policy": ["Politics & Government", "Public Administration"],
    "intl_studies": ["International Studies & Diplomacy"],
    "international_studies": ["International Studies & Diplomacy"],
    "diplomacy": ["International Studies & Diplomacy"],
    "sociology": ["Sociology"],
    "linguistics": ["Linguistics & Languages"],
    "language": ["Linguistics & Languages"],
    "languages": ["Linguistics & Languages"],
    "dev_communication": ["Development Communication"],
    "development_communication": ["Development Communication"],
    "community_dev": ["Community Development"],
    "community_development": ["Community Development"],
    "philosophy": ["Philosophy & Ethics"],
    "ethics": ["Philosophy & Ethics"],
    "special_education": ["Special Needs Education"],
    "special_needs": ["Special Needs Education"],
    "library_science": ["Library & Information Science"],
    "library_information_science": ["Library & Information Science"],
    "legal_mgmt": ["Legal Management"],
    "legal_management": ["Legal Management"],
    "early_childhood": ["Early Childhood Education"],
    "early_childhood_education": ["Early Childhood Education"],
    # Healthcare
    "medical": ["Medicine & Healthcare", "Healthcare General", "Medical Technology"],
    "nursing": ["Nursing & Patient Care", "Nursing & Emergency Health"],
    "ai": ["AI & Machine Learning", "Computer Science", "Data & Analytics"],
    "psychology": ["Psychology & Mental Health"],
    "mental_health": ["Psychology & Mental Health"],
    "public_health": ["Public Health"],
    "health": ["Medicine & Healthcare", "Nursing & Patient Care"],
    "pharmacy": ["Pharmacy & Pharmaceutical Science"],
    "physical_therapy": ["Physical Therapy & Rehabilitation"],
    "nutrition": ["Nutrition & Dietetics"],
    "dentistry": ["Dentistry & Oral Health"],
    "counseling": ["Psychology & Mental Health"],
    "patient_care": ["Nursing & Patient Care", "Medicine & Healthcare"],
    "midwifery": ["Midwifery & Maternal Health"],
    "maternal_health": ["Midwifery & Maternal Health"],
    "radiology": ["Radiology & Imaging"],
    "radiologic": ["Radiology & Imaging"],
    "imaging": ["Radiology & Imaging"],
    "optometry": ["Optometry & Vision Care"],
    "vision_care": ["Optometry & Vision Care"],
    "occupational_therapy": ["Occupational Therapy"],
    "medical_tech": ["Medical Technology & Lab Science"],
    "lab_science": ["Medical Technology & Lab Science"],
    "laboratory": ["Laboratory Research", "Science & Research", "Medical Technology & Lab Science"],
    "laboratory_work": ["Laboratory Research", "Science & Research"],
    "machine_operation": ["Mechanical Systems", "Industrial & Manufacturing", "Engineering General"],
    "machine": ["Mechanical Systems", "Industrial & Manufacturing"],
    "dietetics": ["Nutrition & Dietetics"],
    "pharmaceutical": ["Pharmacy & Pharmaceutical Science"],
    "rehabilitation": ["Physical Therapy & Rehabilitation"],
    "respiratory": ["Respiratory Therapy"],
    "respiratory_therapy": ["Respiratory Therapy"],
    "speech_therapy": ["Speech-Language Pathology"],
    "speech_pathology": ["Speech-Language Pathology"],
}

INTEREST_CATEGORY_KEYWORDS.update({
    "culinary_&_food_science": ["Culinary & Food Science", "Food Science"],
    "culinary_and_food_science": ["Culinary & Food Science", "Food Science"],
    "culinary_food_science": ["Culinary & Food Science", "Food Science"],
    "agriculture_&_farming": ["Agriculture & Farming"],
    "agriculture_and_farming": ["Agriculture & Farming"],
    "agriculture_farming": ["Agriculture & Farming"],
    "forestry_&_natural_resources": ["Forestry & Natural Resources"],
    "forestry_and_natural_resources": ["Forestry & Natural Resources"],
    "forestry_natural_resources": ["Forestry & Natural Resources"],
    "fisheries_&_agriculture": ["Fisheries & Agriculture"],
    "fisheries_and_agriculture": ["Fisheries & Agriculture"],
    "fisheries_agriculture": ["Fisheries & Agriculture"],
    "veterinary_&_animal_science": ["Veterinary & Animal Science"],
    "veterinary_and_animal_science": ["Veterinary & Animal Science"],
    "veterinary_animal_science": ["Veterinary & Animal Science"],
    "culinary_management": ["Culinary Management"],
    "technical-vocational_training": ["Technical-Vocational Training"],
    "technical_vocational_training": ["Technical-Vocational Training"],
})

QUESTION_CATEGORY_DOMAIN_HINTS = {
    "creative": [
        "Fine Arts", "Art & Design", "Music", "Film", "Animation", "Photography",
        "Fashion", "Graphic Arts", "Advertising", "Multimedia", "Writing", "Theater",
        "Performing", "Arts General", "Audio", "Performance", "Production",
        "Literature", "Clothing", "Textile",
    ],
    "technology": [
        "Programming", "Software", "Computers", "Cybersecurity", "Database",
        "Web & Mobile", "Computer Networking", "AI & Machine Learning", "Data & Analytics",
        "Robotics", "Information Systems", "Information Technology",
    ],
    "healthcare": [
        "Healthcare", "Nursing", "Patient Care", "Medicine", "Pharmacy",
        "Dentistry", "Psychology", "Nutrition", "Physical Therapy", "Health Information",
        "Medical", "Clinical", "Mental Health", "Public Health",
        "Lab Science", "Dietetics", "Pharmaceutical", "Rehabilitation", "Technology & Lab",
        "Occupational Therapy", "Respiratory Therapy", "Speech-Language Pathology",
        "Oral Health", "Speech", "Respiratory", "Occupational",
        "Radiology", "Imaging", "Optometry", "Vision", "Midwifery", "Maternal",
    ],
    "engineering": [
        "Civil & Construction", "Electrical & Electronics", "Architecture & Interior Design",
        "Mechanical", "Engineering", "Industrial & Manufacturing", "Aeronautical",
        "Geodetic", "Surveying",
    ],
    "business": [
        "Business & Entrepreneurship", "Finance & Banking", "Accounting", "Management & Administration",
        "Marketing & Advertising", "Human Resource", "Real Estate", "Operations", "Customs",
        "Office Administration",
    ],
    "science": [
        "Biology", "Chemistry", "Physics", "Weather & Atmospheric Science", "Earth Science",
        "Biotechnology", "Science", "Environmental", "Research", "Geology",
    ],
    "hospitality": [
        "Tourism & Hospitality", "Hotel & Resort Management", "Culinary", "Hospitality",
        "Tourism", "Food Science",
    ],
    "agriculture": [
        "Agriculture", "Agribusiness", "Veterinary", "Forestry", "Fisheries", "Aquaculture",
    ],
    "maritime": [
        "Maritime", "Marine", "Aviation", "Aeronautical & Aerospace", "Marine Engineering",
    ],
    "education": [
        "Education & Teaching", "Teaching", "Early Childhood", "Special Education",
    ],
    "public_service": [
        "Law & Justice", "Criminology", "Politics", "Public Safety", "Government", "Social Work",
        "Public Administration", "Justice", "Legal", "Governance", "Policy", "Administration",
        "International Studies & Diplomacy", "International Studies", "Diplomacy",
        "Linguistics & Languages", "Linguistics", "Languages",
        "Philosophy & Ethics", "Philosophy", "Ethics", "Legal Management",
    ],
    "social": [
        "Psychology", "Social Work", "Community", "Mental Health", "Counseling",
        "Education & Teaching", "History & Culture", "Communication & Journalism",
        "Teaching", "History", "Culture", "Communication", "Journalism", "Media",
        "Development Communication", "Community Development", "Sociology",
    ],
    "education": [
        "Education & Teaching", "Teaching", "Early Childhood", "Special Education",
        "Special Needs Education", "Library & Information Science", "Library", "Information Science",
        "Early Childhood Education",
    ],
    "physical": [
        "Sports", "Fitness", "Exercise", "Exercise & Sports Science", "Military", "Defense",
    ],
}

QUESTION_CATEGORY_DOMAIN_HINTS["science"].extend(["Culinary & Food Science", "Food Science"])
QUESTION_CATEGORY_DOMAIN_HINTS["agriculture"].extend(["Veterinary & Animal Science", "Animal Science"])
QUESTION_CATEGORY_DOMAIN_HINTS["agriculture"].extend(["Agriculture & Farming", "Forestry & Natural Resources", "Fisheries & Agriculture"])
QUESTION_CATEGORY_DOMAIN_HINTS["hospitality"].extend(["Culinary Management"])
QUESTION_CATEGORY_DOMAIN_HINTS["education"].extend(["Technical-Vocational Training"])
QUESTION_CATEGORY_DOMAIN_HINTS["technology"].extend(["Technical-Vocational Training"])
# General/broad category hints for remaining unclassified questions
QUESTION_CATEGORY_DOMAIN_HINTS["social"].extend(["Social General"])
QUESTION_CATEGORY_DOMAIN_HINTS["business"].extend(["Business General", "Logistics & Supply Chain", "Economics", "Statistics & Probability"])
QUESTION_CATEGORY_DOMAIN_HINTS["technology"].extend(["Technology General", "Game Development", "Statistics & Probability"])
QUESTION_CATEGORY_DOMAIN_HINTS["engineering"].extend(["Product & Industrial Design", "Aircraft Maintenance & Avionics"])
QUESTION_CATEGORY_DOMAIN_HINTS["physical"].extend(["Aircraft Maintenance & Avionics"])
QUESTION_CATEGORY_DOMAIN_HINTS["science"].extend(["Environment & Nature"])
QUESTION_CATEGORY_DOMAIN_HINTS["healthcare"].extend(["Health Admin", "Hospital Dept"])
QUESTION_CATEGORY_DOMAIN_HINTS["business"].extend(["HR Management", "HR", "Health Admin"])
QUESTION_CATEGORY_DOMAIN_HINTS["public_service"].extend(["Social Work", "Child Welfare"])
QUESTION_CATEGORY_DOMAIN_HINTS["science"].extend(["Forensic", "Food Safety"])
QUESTION_CATEGORY_DOMAIN_HINTS["hospitality"].extend(["Tourism", "Local Tourism"])
# Catch-all for remaining edge cases
QUESTION_CATEGORY_DOMAIN_HINTS["creative"].extend(["Arts & Design", "Landscape Architecture"])
QUESTION_CATEGORY_DOMAIN_HINTS["engineering"].extend(["Landscape Architecture"])
QUESTION_CATEGORY_DOMAIN_HINTS["business"].extend(["Startup & Innovation", "PH Industry Trends",
                                                    "Career Shadow Extended", "Work Environment Extended",
                                                    "Licensure Extended"])

# ── EXPLICIT REGISTRATION: Batches 32-34 (Q5306-Q5365) ─────────────
# Batch 32 – Q5306-Q5325
QUESTION_TREE_NODES[5306] = {"level": 2, "weight": 2.0, "branches": ["maritime"]}                           # Maritime Studies
QUESTION_TREE_NODES[5307] = {"level": 2, "weight": 2.0, "branches": ["law", "public_service"]}              # Criminology & Public Safety
QUESTION_TREE_NODES[5308] = {"level": 2, "weight": 2.0, "branches": ["engineering", "creative"]}            # Architecture & Interior Design
QUESTION_TREE_NODES[5309] = {"level": 2, "weight": 2.0, "branches": ["healthcare", "education"]}            # Psychology & Counseling
QUESTION_TREE_NODES[5310] = {"level": 2, "weight": 2.0, "branches": ["agriculture", "science"]}             # Agriculture & Farming
QUESTION_TREE_NODES[5311] = {"level": 2, "weight": 2.0, "branches": ["creative", "business"]}               # Communication & Journalism
QUESTION_TREE_NODES[5312] = {"level": 2, "weight": 2.0, "branches": ["technology", "business", "science"]}  # Data & Analytics
QUESTION_TREE_NODES[5313] = {"level": 2, "weight": 2.0, "branches": ["hospitality", "business"]}            # Tourism & Hospitality
QUESTION_TREE_NODES[5314] = {"level": 2, "weight": 2.0, "branches": ["engineering", "technology"]}           # Electrical & Electronics
QUESTION_TREE_NODES[5315] = {"level": 2, "weight": 2.0, "branches": ["business", "science"]}                # Accounting
QUESTION_TREE_NODES[5316] = {"level": 2, "weight": 2.0, "branches": ["education"]}                          # Education & Teaching
QUESTION_TREE_NODES[5317] = {"level": 2, "weight": 2.0, "branches": ["technology", "public_service"]}       # Cybersecurity
QUESTION_TREE_NODES[5318] = {"level": 2, "weight": 2.0, "branches": ["agriculture", "maritime", "science"]} # Marine Biology & Fisheries
QUESTION_TREE_NODES[5319] = {"level": 2, "weight": 2.0, "branches": ["business"]}                           # Business & Entrepreneurship
QUESTION_TREE_NODES[5320] = {"level": 2, "weight": 2.0, "branches": ["technology", "creative"]}             # Game Development
QUESTION_TREE_NODES[5321] = {"level": 2, "weight": 2.0, "branches": ["public_service", "business"]}         # Public Administration
QUESTION_TREE_NODES[5322] = {"level": 2, "weight": 2.0, "branches": ["science", "healthcare"]}              # Biotechnology & Genetics
QUESTION_TREE_NODES[5323] = {"level": 2, "weight": 2.0, "branches": ["creative", "business"]}               # Fashion & Textile Design
QUESTION_TREE_NODES[5324] = {"level": 2, "weight": 2.0, "branches": ["agriculture", "science"]}             # Forestry & Environmental Science
QUESTION_TREE_NODES[5325] = {"level": 2, "weight": 2.0, "branches": ["education", "healthcare"]}            # Special Needs Education

# Batch 33 – Q5326-Q5345
QUESTION_TREE_NODES[5326] = {"level": 2, "weight": 2.0, "branches": ["agriculture", "healthcare"]}                   # Veterinary Medicine
QUESTION_TREE_NODES[5327] = {"level": 2, "weight": 2.0, "branches": ["science", "engineering", "technology"]}         # Physics & Mathematics
QUESTION_TREE_NODES[5328] = {"level": 2, "weight": 2.0, "branches": ["technology", "education"]}                      # Library & Information Science
QUESTION_TREE_NODES[5329] = {"level": 2, "weight": 2.0, "branches": ["public_service", "education"]}                  # Sociology & Social Research
QUESTION_TREE_NODES[5330] = {"level": 2, "weight": 2.0, "branches": ["education", "creative"]}                        # Linguistics & Language Studies
QUESTION_TREE_NODES[5331] = {"level": 2, "weight": 2.0, "branches": ["creative"]}                                     # Theater & Performing Arts
QUESTION_TREE_NODES[5332] = {"level": 2, "weight": 2.0, "branches": ["physical", "healthcare"]}                       # Exercise & Sports Science
QUESTION_TREE_NODES[5333] = {"level": 2, "weight": 2.0, "branches": ["engineering", "technology", "science"]}          # Aviation Technology
QUESTION_TREE_NODES[5334] = {"level": 2, "weight": 2.0, "branches": ["engineering", "public_service", "agriculture"]} # Geodetic Engineering
QUESTION_TREE_NODES[5335] = {"level": 2, "weight": 2.0, "branches": ["engineering", "creative", "business"]}           # Industrial Design
QUESTION_TREE_NODES[5336] = {"level": 2, "weight": 2.0, "branches": ["creative"]}                                     # Photography & Visual Arts
QUESTION_TREE_NODES[5337] = {"level": 2, "weight": 2.0, "branches": ["creative", "technology"]}                        # Music Production
QUESTION_TREE_NODES[5338] = {"level": 2, "weight": 2.0, "branches": ["engineering", "creative"]}                       # Landscape Architecture
QUESTION_TREE_NODES[5339] = {"level": 2, "weight": 2.0, "branches": ["business", "public_service"]}                   # Real Estate Management
QUESTION_TREE_NODES[5340] = {"level": 2, "weight": 2.0, "branches": ["business", "public_service"]}                   # Office Administration
QUESTION_TREE_NODES[5341] = {"level": 2, "weight": 2.0, "branches": ["business", "public_service"]}                   # Customs Administration
QUESTION_TREE_NODES[5342] = {"level": 2, "weight": 2.0, "branches": ["science", "hospitality", "healthcare"]}         # Food Technology
QUESTION_TREE_NODES[5343] = {"level": 2, "weight": 2.0, "branches": ["science", "engineering"]}                        # Geology & Meteorology
QUESTION_TREE_NODES[5344] = {"level": 2, "weight": 2.0, "branches": ["public_service", "education"]}                  # Community Development
QUESTION_TREE_NODES[5345] = {"level": 2, "weight": 2.0, "branches": ["public_service", "business"]}                   # Political Science & Intl Studies

# Batch 34 – Q5346-Q5365
QUESTION_TREE_NODES[5346] = {"level": 2, "weight": 2.0, "branches": ["technology", "science"]}              # Computer Science & AI
QUESTION_TREE_NODES[5347] = {"level": 2, "weight": 2.0, "branches": ["technology", "business"]}             # Information Technology
QUESTION_TREE_NODES[5348] = {"level": 2, "weight": 2.0, "branches": ["engineering", "technology"]}           # Computer Engineering
QUESTION_TREE_NODES[5349] = {"level": 2, "weight": 2.0, "branches": ["engineering", "technology"]}           # Electronics & Electrical Eng
QUESTION_TREE_NODES[5350] = {"level": 2, "weight": 2.0, "branches": ["engineering", "public_service"]}      # Civil Engineering
QUESTION_TREE_NODES[5351] = {"level": 2, "weight": 2.0, "branches": ["engineering", "technology"]}           # Mechanical Engineering
QUESTION_TREE_NODES[5352] = {"level": 2, "weight": 2.0, "branches": ["engineering", "business"]}             # Industrial Engineering
QUESTION_TREE_NODES[5353] = {"level": 2, "weight": 2.0, "branches": ["engineering", "technology", "science"]}# Aeronautical Engineering
QUESTION_TREE_NODES[5354] = {"level": 2, "weight": 2.0, "branches": ["creative", "technology"]}              # Animation & Multimedia
QUESTION_TREE_NODES[5355] = {"level": 2, "weight": 2.0, "branches": ["creative"]}                            # Fine Arts & Visual Design
QUESTION_TREE_NODES[5356] = {"level": 2, "weight": 2.0, "branches": ["business", "creative"]}                # Marketing Management
QUESTION_TREE_NODES[5357] = {"level": 2, "weight": 2.0, "branches": ["business", "public_service"]}          # Human Resource Management
QUESTION_TREE_NODES[5358] = {"level": 2, "weight": 2.0, "branches": ["business", "agriculture"]}             # Agribusiness
QUESTION_TREE_NODES[5359] = {"level": 2, "weight": 2.0, "branches": ["science", "healthcare"]}               # Biology & Life Sciences
QUESTION_TREE_NODES[5360] = {"level": 2, "weight": 2.0, "branches": ["science", "healthcare"]}               # Chemistry & Laboratory Science
QUESTION_TREE_NODES[5361] = {"level": 2, "weight": 2.0, "branches": ["technology", "business", "science"]}   # Statistics & Data Science
QUESTION_TREE_NODES[5362] = {"level": 2, "weight": 2.0, "branches": ["science", "engineering", "public_service"]} # Environmental Planning
QUESTION_TREE_NODES[5363] = {"level": 2, "weight": 2.0, "branches": ["education", "public_service"]}         # Philosophy & Ethics
QUESTION_TREE_NODES[5364] = {"level": 2, "weight": 2.0, "branches": ["healthcare"]}                          # Nursing & Emergency Health
QUESTION_TREE_NODES[5365] = {"level": 2, "weight": 2.0, "branches": ["creative", "public_service"]}          # Development Communication

# Batch 35 – Q5366-Q5385
QUESTION_TREE_NODES[5366] = {"level": 2, "weight": 2.0, "branches": ["healthcare", "science"]}               # Pharmacy & Pharmaceutical Science
QUESTION_TREE_NODES[5367] = {"level": 2, "weight": 2.0, "branches": ["healthcare", "science"]}               # Nutrition & Dietetics
QUESTION_TREE_NODES[5368] = {"level": 2, "weight": 2.0, "branches": ["science", "public_service"]}           # Forensic Science & Criminology
QUESTION_TREE_NODES[5369] = {"level": 2, "weight": 2.0, "branches": ["healthcare"]}                          # Physical Therapy & Rehabilitation
QUESTION_TREE_NODES[5370] = {"level": 2, "weight": 2.0, "branches": ["public_service"]}                      # Social Work & Community Services
QUESTION_TREE_NODES[5371] = {"level": 2, "weight": 2.0, "branches": ["healthcare", "science"]}               # Medical Technology & Laboratory
QUESTION_TREE_NODES[5372] = {"level": 2, "weight": 2.0, "branches": ["public_service", "business"]}          # Public Administration & Governance
QUESTION_TREE_NODES[5373] = {"level": 2, "weight": 2.0, "branches": ["business", "creative"]}                # Hospitality & Hotel Management
QUESTION_TREE_NODES[5374] = {"level": 2, "weight": 2.0, "branches": ["public_service"]}                      # Legal Studies & Law
QUESTION_TREE_NODES[5375] = {"level": 2, "weight": 2.0, "branches": ["creative", "engineering"]}             # Architecture & Spatial Design
QUESTION_TREE_NODES[5376] = {"level": 2, "weight": 2.0, "branches": ["creative", "science"]}                 # Culinary Arts & Food Science
QUESTION_TREE_NODES[5377] = {"level": 2, "weight": 2.0, "branches": ["engineering", "technology"]}           # Electrical Engineering & Renewable Energy
QUESTION_TREE_NODES[5378] = {"level": 2, "weight": 2.0, "branches": ["business", "science"]}                 # Tourism & Ecotourism Management
QUESTION_TREE_NODES[5379] = {"level": 2, "weight": 2.0, "branches": ["technology"]}                          # Software Engineering & Web Development
QUESTION_TREE_NODES[5380] = {"level": 2, "weight": 2.0, "branches": ["science", "agriculture"]}              # Environmental Science & Ecology
QUESTION_TREE_NODES[5381] = {"level": 2, "weight": 2.0, "branches": ["healthcare", "public_service"]}        # Nursing & Public Health
QUESTION_TREE_NODES[5382] = {"level": 2, "weight": 2.0, "branches": ["engineering", "technology"]}           # Mechanical Engineering & Automotive
QUESTION_TREE_NODES[5383] = {"level": 2, "weight": 2.0, "branches": ["education", "public_service"]}         # Education & Inclusive Learning
QUESTION_TREE_NODES[5384] = {"level": 2, "weight": 2.0, "branches": ["technology"]}                          # Cybersecurity & Information Assurance
QUESTION_TREE_NODES[5385] = {"level": 2, "weight": 2.0, "branches": ["engineering", "public_service"]}       # Maritime & Naval Architecture

# ── AUTO-CLASSIFY UNCLASSIFIED QUESTIONS ────────────────────────────
# Many enhanced questions are not explicitly added to QUESTION_TREE_NODES.
# Without classification, _is_relevant_question() cannot filter them,
# so veterinary questions appear for healthcare users, etc.
# Infer branches from the question's category string using the
# QUESTION_CATEGORY_DOMAIN_HINTS mapping.

def _infer_branches_from_category(category: str) -> list:
    """Infer branch domains from a question's category string."""
    if not category:
        return []
    cat_lower = category.lower()
    # Strip common prefixes
    for prefix in ("academic interest - ", "career - ", "situational - ",
                   "domain - ", "work environment ", "licensure ",
                   "ph industry "):
        if cat_lower.startswith(prefix):
            cat_lower = cat_lower[len(prefix):]
            break

    matched = []
    for domain, keywords in QUESTION_CATEGORY_DOMAIN_HINTS.items():
        for kw in keywords:
            if kw.lower() in cat_lower or cat_lower in kw.lower():
                matched.append(domain)
                break
    # Special handling for "Engineering CS" prefix categories
    if "engineering cs" in category.lower():
        matched = list(set(matched) | {"engineering", "technology"})
    return list(set(matched)) if matched else []

# Apply to all questions not already in QUESTION_TREE_NODES
try:
    from data.questions_enhanced import QUESTIONS_POOL_ENHANCED
    _all_questions_to_classify = QUESTIONS_POOL_ENHANCED
except (ImportError, NameError):
    _all_questions_to_classify = []

def _infer_branches_from_traits(question: dict) -> list:
    """Fallback: infer branch domains from a question's option trait_tags."""
    branch_votes: Dict[str, int] = {}
    for opt in question.get("options", []):
        tt = opt.get("trait_tags", {})
        traits = tt.keys() if isinstance(tt, dict) else (tt if isinstance(tt, list) else [])
        for t in traits:
            branch = TRAIT_TO_BRANCH.get(t, "")
            if branch:
                branch_votes[branch] = branch_votes.get(branch, 0) + 1
    if not branch_votes:
        return []
    # Return branches that appear in at least 10% of the votes (min 1)
    max_count = max(branch_votes.values())
    threshold = max(1, max_count * 0.2)
    return sorted([b for b, c in branch_votes.items() if c >= threshold],
                  key=lambda b: branch_votes[b], reverse=True)

_auto_classified = 0
_trait_classified = 0
for _q in _all_questions_to_classify:
    _qid = _q.get("question_id")
    if _qid and _qid not in QUESTION_TREE_NODES:
        _branches = _infer_branches_from_category(_q.get("category", ""))
        if not _branches:
            _branches = _infer_branches_from_traits(_q)
            if _branches:
                _trait_classified += 1
        if _branches:
            QUESTION_TREE_NODES[_qid] = {
                "level": 2,
                "weight": 1.6,
                "branches": _branches,
            }
            _auto_classified += 1

if _auto_classified:
    print(f"[TREE] Auto-classified {_auto_classified} unclassified questions "
          f"({_auto_classified - _trait_classified} by category, {_trait_classified} by trait analysis)")

# ── AUTO-REGISTER INTO TRAIT_FOLLOWUP_MAP & DOMAIN_ENTRY_QUESTIONS ──
# For every auto-classified question, register it as a follow-up for its
# dominant traits so the conversation chain can reach it.
_followup_added = 0
for _q in _all_questions_to_classify:
    _qid = _q.get("question_id")
    if not _qid or _qid not in QUESTION_TREE_NODES:
        continue
    # Collect all traits this question covers
    _trait_counts: Dict[str, float] = {}
    for _opt in _q.get("options", []):
        _tt = _opt.get("trait_tags", {})
        if isinstance(_tt, dict):
            for _t, _w in _tt.items():
                _trait_counts[_t] = _trait_counts.get(_t, 0) + (float(_w) if isinstance(_w, (int, float)) else 1.0)
        elif isinstance(_tt, list):
            for _t in _tt:
                _trait_counts[_t] = _trait_counts.get(_t, 0) + 1.0
    # Add this question to the follow-up list of its top traits
    _sorted_traits = sorted(_trait_counts.items(), key=lambda x: x[1], reverse=True)
    for _t, _w in _sorted_traits[:5]:  # Top 5 traits only
        if _t in TRAIT_FOLLOWUP_MAP:
            if _qid not in TRAIT_FOLLOWUP_MAP[_t]:
                TRAIT_FOLLOWUP_MAP[_t].append(_qid)
                _followup_added += 1
        else:
            TRAIT_FOLLOWUP_MAP[_t] = [_qid]
            _followup_added += 1

# Also add auto-classified questions to DOMAIN_ENTRY_QUESTIONS
_domain_entry_added = 0
for _q in _all_questions_to_classify:
    _qid = _q.get("question_id")
    if not _qid or _qid not in QUESTION_TREE_NODES:
        continue
    _node = QUESTION_TREE_NODES[_qid]
    for _branch in _node.get("branches", [])[:2]:  # Primary + secondary branch
        if _branch in DOMAIN_ENTRY_QUESTIONS:
            if _qid not in DOMAIN_ENTRY_QUESTIONS[_branch]:
                DOMAIN_ENTRY_QUESTIONS[_branch].append(_qid)
                _domain_entry_added += 1

if _followup_added:
    print(f"[TREE] Added {_followup_added} trait follow-up entries for auto-classified questions")
if _domain_entry_added:
    print(f"[TREE] Added {_domain_entry_added} domain entry entries for auto-classified questions")

# ────────────────────────────────────────────────────────────────────

# Minimum questions to ask in a domain before moving on
DOMAIN_MIN_QUESTIONS = 3

# Hard cap per domain — set to 30 so a dominant domain can fill the full session.
DOMAIN_MAX_QUESTIONS_HARD_CAP = 30


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
        # Skip rejection/none options so their traits don't make questions
        # appear relevant to unrelated profiles.
        self.trait_to_questions: Dict[str, List[int]] = defaultdict(list)
        for qid, question in self.questions.items():
            for opt in question.get('options', []):
                if self._is_rejection_option(opt):
                    continue
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
        # Skip rejection/none options so their traits don't inflate affinity.
        self.question_trait_affinity: Dict[int, Dict[str, float]] = {}
        for qid, question in self.questions.items():
            affinities = {}
            options = question.get('options', [])
            substantive_opts = [o for o in options if not self._is_rejection_option(o)]
            for opt in substantive_opts:
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
            total = len(substantive_opts)
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
        
        # Auto-classify any questions not already in QUESTION_TREE_NODES
        _auto_n = 0
        for _qid, _q in self.questions.items():
            if _qid not in QUESTION_TREE_NODES:
                _branches = _infer_branches_from_category(_q.get("category", ""))
                if _branches:
                    QUESTION_TREE_NODES[_qid] = {
                        "level": 1,
                        "weight": 1.4,
                        "branches": _branches,
                    }
                    _auto_n += 1
        if _auto_n:
            print(f"[ENGINE] Auto-classified {_auto_n} previously unclassified questions by category")
        
        print(f"[ENGINE] Decision tree nodes classified: {len(QUESTION_TREE_NODES)} questions")
    
    def _parse_traits(self, trait_tag) -> Set[str]:
        """Parse trait_tag field into set of traits"""
        if not trait_tag:
            return set()
        if isinstance(trait_tag, list):
            return set(trait_tag)
        return set(t.strip() for t in str(trait_tag).split(',') if t.strip())

    def _profile_lookup_keys(self, selection: str) -> List[str]:
        """Generate normalized lookup variants for profile selections."""
        if not selection:
            return []

        raw = selection.strip().lower()
        normalized_words = " ".join(
            raw.replace("&", " ")
               .replace("/", " ")
               .replace("-", " ")
               .replace("_", " ")
               .split()
        )
        snake = normalized_words.replace(" ", "_")

        candidates = [
            raw,
            raw.replace(" ", "_"),
            raw.replace(" & ", "_").replace("&", "_").replace(" ", "_"),
            snake,
            normalized_words,
        ]

        if normalized_words:
            candidates.extend(normalized_words.split())

        ordered = []
        seen = set()
        for candidate in candidates:
            if candidate and candidate not in seen:
                ordered.append(candidate)
                seen.add(candidate)
        return ordered

    def _build_profile_none_option(self, session: AdaptiveSession) -> dict:
        """Build a dynamic 'I don't see what I want' option with traits from user profile."""
        trait_scores = {}  # trait -> accumulated weight

        # Gather traits from academic interests
        if session.user_interests:
            for interest in session.user_interests.split(','):
                for trait in self._get_profile_traits_for_selection(interest.strip()):
                    trait_scores[trait] = trait_scores.get(trait, 0) + 0.4

        # Gather traits from skills
        if session.user_skills:
            for skill in session.user_skills.split(','):
                for trait in self._get_profile_traits_for_selection(skill.strip()):
                    trait_scores[trait] = trait_scores.get(trait, 0) + 0.3

        if not trait_scores:
            # Fallback: no profile data, return empty option with no traits
            return {
                "option_id": -1,
                "option_text": "I don't see what I want",
                "trait_tags": {}
            }

        # Normalize: primary trait = 1.0, others scaled proportionally
        max_score = max(trait_scores.values())
        normalized = {}
        for trait, score in sorted(trait_scores.items(), key=lambda x: -x[1]):
            normalized[trait] = round(min(score / max_score, 1.0), 2)

        return {
            "option_id": -1,
            "option_text": "I don't see what I want",
            "trait_tags": normalized
        }

    def _append_none_option(self, question: dict, session: AdaptiveSession) -> dict:
        """Return a copy of the question with the profile-based 'None' option appended."""
        none_opt = self._build_profile_none_option(session)
        q_copy = dict(question)
        q_copy["options"] = list(question.get("options", [])) + [none_opt]
        return q_copy

    def _get_profile_traits_for_selection(self, selection: str) -> List[str]:
        """Resolve a profile selection to traits using tolerant key matching.

        Prefers compound (multi-word) key matches over individual word matches
        to prevent overly broad trait expansion (e.g. 'graphic_design' should
        NOT also match 'design' → 'Spatial-Design').
        """
        traits = []
        seen = set()
        all_keys = self._profile_lookup_keys(selection)

        # Phase 1: try compound keys first
        compound_found = False
        for key in all_keys:
            is_compound = any(c in key for c in '_& /')
            if not is_compound:
                continue
            for trait in UNIFIED_PROFILE_TO_TRAITS.get(key, []):
                if trait not in seen:
                    traits.append(trait)
                    seen.add(trait)
                    compound_found = True

        # Phase 2: only fall back to single-word keys when no compound matched
        if not compound_found:
            for key in all_keys:
                for trait in UNIFIED_PROFILE_TO_TRAITS.get(key, []):
                    if trait not in seen:
                        traits.append(trait)
                        seen.add(trait)

        return traits

    def _get_profile_category_keywords_for_selection(self, selection: str) -> List[str]:
        """Resolve a profile selection to question-category keywords using tolerant matching.

        Prefers compound (multi-word) key matches over individual word matches
        to prevent overly broad expansion (e.g. 'graphic_design' should NOT
        also match 'design' → 'Architecture & Interior Design').
        """
        categories = []
        seen = set()
        all_keys = self._profile_lookup_keys(selection)

        # Phase 1: try compound keys (contain separator characters)
        compound_found = False
        for key in all_keys:
            is_compound = any(c in key for c in '_& /')
            if not is_compound:
                continue
            for category in INTEREST_CATEGORY_KEYWORDS.get(key, []):
                if category not in seen:
                    categories.append(category)
                    seen.add(category)
                    compound_found = True

        # Phase 2: only fall back to single-word keys when no compound matched
        if not compound_found:
            for key in all_keys:
                for category in INTEREST_CATEGORY_KEYWORDS.get(key, []):
                    if category not in seen:
                        categories.append(category)
                        seen.add(category)

        return categories

    def _normalize_category_name(self, category: str) -> str:
        """Normalize question category labels for continuity matching."""
        if not category:
            return ""
        normalized = category.replace("Academic Interest -", "").strip()
        normalized = normalized.replace("—", "-")
        return normalized

    def _category_match_score(self, category: str, keyword: str) -> int:
        """Return a token-based match score between a question category and a profile keyword."""
        normalized_category = self._normalize_category_name(category).lower()
        normalized_keyword = self._normalize_category_name(keyword).lower()
        if not normalized_category or not normalized_keyword:
            return 0

        def _tokenize(value: str) -> Set[str]:
            cleaned = (
                value.replace("&", " ")
                     .replace("/", " ")
                     .replace("-", " ")
                     .replace("(", " ")
                     .replace(")", " ")
            )
            return {token for token in cleaned.split() if token}

        category_tokens = _tokenize(normalized_category)
        keyword_tokens = _tokenize(normalized_keyword)
        if not category_tokens or not keyword_tokens:
            return 0

        if keyword_tokens.issubset(category_tokens):
            return len(keyword_tokens)
        return 0

    def _question_in_profile_pool(self, qid: int, session: AdaptiveSession) -> bool:
        """When a profile pool exists, require questions to come from it."""
        return not session.profile_relevant_qids or qid in session.profile_relevant_qids

    def _infer_question_domains(self, question: dict) -> Set[str]:
        """Infer branch domains from question metadata when tree node metadata is missing."""
        inferred: Set[str] = set()
        category = question.get("category", "")
        for domain, hints in QUESTION_CATEGORY_DOMAIN_HINTS.items():
            for hint in hints:
                if self._category_match_score(category, hint) > 0:
                    inferred.add(domain)
                    break
        return inferred

    def _question_in_domain(self, qid: int, domain: str) -> bool:
        """Check whether a question belongs to a branch/domain."""
        if not domain:
            return True
        node = QUESTION_TREE_NODES.get(qid)
        if node:
            return domain in set(node.get("branches", []))
        question = self.questions.get(qid)
        if not question:
            return False
        return domain in self._infer_question_domains(question)

    def _get_session_category_focus(self, session: AdaptiveSession) -> str:
        """Return the dominant recent category thread for the session."""
        if session.current_category_focus:
            return session.current_category_focus
        if not session.category_history:
            return ""

        recent = session.category_history[-5:]
        counts: Dict[str, int] = {}
        for category in recent:
            counts[category] = counts.get(category, 0) + 1
        return max(counts.items(), key=lambda item: item[1])[0]

    def _question_matches_category_focus(self, qid: int, session: AdaptiveSession) -> bool:
        """Prefer questions from the same category family the user keeps choosing."""
        focus = self._get_session_category_focus(session)
        if not focus:
            return False

        question = self.questions.get(qid)
        if not question:
            return False

        q_category = self._normalize_category_name(question.get("category", ""))
        if not q_category:
            return False

        if q_category == focus:
            return True

        focus_tokens = {token for token in focus.lower().replace("&", " ").replace("/", " ").replace("-", " ").split() if len(token) > 2}
        q_tokens = {token for token in q_category.lower().replace("&", " ").replace("/", " ").replace("-", " ").split() if len(token) > 2}
        if not focus_tokens or not q_tokens:
            return False
        return len(focus_tokens & q_tokens) >= 2

    def _get_profile_domain_for_selection(self, selection: str) -> Optional[str]:
        """Resolve a profile selection to its most relevant domain."""
        for key in self._profile_lookup_keys(selection):
            domain = INTEREST_DOMAIN_MAP.get(key)
            if domain:
                return domain

        branch_votes: Dict[str, int] = {}
        for trait in self._get_profile_traits_for_selection(selection):
            branch = TRAIT_TO_BRANCH.get(trait, "")
            if branch:
                branch_votes[branch] = branch_votes.get(branch, 0) + 1

        if branch_votes:
            return max(branch_votes.items(), key=lambda item: item[1])[0]

        return None
    
    def _calculate_profile_bonus(self, interests: str, skills: str, course_traits: Set[str]) -> float:
        """Calculate bonus points (0-20) for courses matching user's profile interests/skills.

        Uses a WEIGHTED approach: a trait that appears in many of the user's profile
        selections (or appears as the PRIMARY trait in a selection) gets a high weight,
        while a trait that appears as a peripheral/secondary result of one selection
        gets a low weight.  This prevents courses that only match a peripheral interest
        (e.g. Hardware-Systems from 'robotics') from tying with courses that match the
        user's core interest (e.g. Software-Dev from Programming, AI, Computers & IT).

        Academic Interests carry 2× the weight of Technical & Soft Skills so that
        a user's field of study is always the primary driver of Top Matches.
        Skills still influence the score but cannot override an explicit interest.
        """
        if not interests and not skills:
            return 0.0

        # Academic Interests contribute at 5.0× weight; Skills at 3.0×.
        # This ensures interest-matched courses always rank above skill-only courses
        # in the initial Top Matches, regardless of how many skill selections there are.
        INTEREST_WEIGHT = 2.0
        SKILL_WEIGHT = 0.3

        interest_list = [i.strip().lower() for i in (interests or "").split(",") if i.strip()]
        skill_list = [s.strip().lower() for s in (skills or "").split(",") if s.strip()]

        # Build a weighted trait map.
        # For each selection, the first trait gets weight 1.0/(i+1) × source_multiplier.
        # A trait that shows up in many selections accumulates weight across all of them.
        user_trait_weights: Dict[str, float] = {}
        for selection in interest_list:
            related_traits = self._get_profile_traits_for_selection(selection)
            for i, trait in enumerate(related_traits):
                key = trait.lower()
                user_trait_weights[key] = user_trait_weights.get(key, 0.0) + INTEREST_WEIGHT / (i + 1)
        for selection in skill_list:
            related_traits = self._get_profile_traits_for_selection(selection)
            for i, trait in enumerate(related_traits):
                key = trait.lower()
                user_trait_weights[key] = user_trait_weights.get(key, 0.0) + SKILL_WEIGHT / (i + 1)

        if not user_trait_weights:
            return 0.0

        # Normalize: the most-central user trait gets weight 1.0
        max_w = max(user_trait_weights.values())
        normalized: Dict[str, float] = {t: w / max_w for t, w in user_trait_weights.items()}

        # Normalize course traits for matching
        course_traits_lower = {t.lower() for t in course_traits}

        # Generic/broad traits get a lower base than specific path traits
        GENERIC_TRAITS = {"creative-skill", "technical-skill", "people-skill",
                          "analytical-skill", "physical-skill", "admin-skill",
                          "artistic", "realistic", "investigative", "social",
                          "enterprising", "conventional"}

        # Score each course trait by best-matching user trait weight
        bonus = 0.0
        best_weights: Dict[str, float] = {}

        for course_trait in course_traits_lower:
            best_weight = 0.0
            for user_trait, ut_weight in normalized.items():
                if user_trait == course_trait or user_trait in course_trait or course_trait in user_trait:
                    best_weight = max(best_weight, ut_weight)
            if best_weight > 0:
                best_weights[course_trait] = best_weight
                base = 3.0 if course_trait in GENERIC_TRAITS else 6.0
                bonus += base * best_weight  # Scales from full pts (core trait) to near-0 (peripheral)

        # Breadth bonus: only awarded when matched traits are STRONGLY relevant
        # (average match-weight is high). This stops a course with many weak peripheral
        # matches from outscoring a course with one strong primary match.
        if course_traits_lower:
            avg_weight = sum(best_weights.get(ct, 0.0) for ct in course_traits_lower) / len(course_traits_lower)
            if avg_weight >= 0.5:
                bonus += 4.0  # Most course traits are central to the user's profile
            elif avg_weight >= 0.3:
                bonus += 2.0  # Moderate overall relevance

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
                traits = self._get_profile_traits_for_selection(interest)
                for trait in traits:
                    trait_counts[trait] = trait_counts.get(trait, 0) + 1
        
        # Parse skills
        if session.user_skills:
            for skill in session.user_skills.split(','):
                skill = skill.strip().lower()
                traits = self._get_profile_traits_for_selection(skill)
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
                traits = self._get_profile_traits_for_selection(interest)
                for i, trait in enumerate(traits):
                    # First trait in list is most relevant
                    trait_counts[trait] = trait_counts.get(trait, 0) + (2.0 - i * 0.3)

        # Skills get weight 0.8 (secondary to academic interests)
        if skills:
            for skill in skills.split(','):
                skill = skill.strip().lower()
                traits = self._get_profile_traits_for_selection(skill)
                for i, trait in enumerate(traits):
                    trait_counts[trait] = trait_counts.get(trait, 0) + (0.8 - i * 0.1)

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
        # Include profile seeds as dominant only during the warm-up phase
        # (first 10 answers). After that, dominance is driven purely by
        # the user's actual accumulated trait scores, so a pivot in their
        # answers (e.g., from animation to programming) is reflected in
        # the ranking instead of being permanently anchored to the profile.
        if len(session.answered_questions) < 10:
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

    @staticmethod
    def _is_rejection_option(opt: dict) -> bool:
        """Check if an option is a 'none'/'not interested' rejection choice.
        These options should be excluded from trait-relevance checks during
        question selection, because their traits don't represent the question's
        actual topic."""
        if opt.get('option_id') == -1:
            return True
        text = opt.get('option_text', '').lower()
        return any(phrase in text for phrase in [
            'none', 'not interested', "don't want", 'prefer not',
            'not for me', "i don't", 'none of these', 'not really',
            "i'm not", 'im not'
        ])

    def _has_dominant_trait_overlap(self, question: dict, session: AdaptiveSession) -> bool:
        """
        Check if a question has meaningful overlap with the user's DOMINANT pattern
        (top accumulated traits + profile seeds).
        
        For questions with many options: require at least 2 options to match
        dominant traits, OR require the question to be in the profile category pool.
        For questions with few options (<=4): require at least 1 match.
        
        This prevents off-topic questions (where only 1 out of 8+ options 
        tangentially matches) from being served.
        """
        dominant = self._get_dominant_traits(session)
        if not dominant:
            return True  # No dominant traits yet — allow anything
        
        # If question is in profile category pool, always allow
        qid = question.get('question_id')
        if qid and qid in session.profile_relevant_qids:
            return True
        
        options = question.get('options', [])
        matching_options = 0
        substantive_count = 0
        for opt in options:
            if self._is_rejection_option(opt):
                continue
            substantive_count += 1
            trait_tags = opt.get('trait_tags', {})
            opt_matches = False
            if isinstance(trait_tags, dict):
                for trait in trait_tags:
                    if trait in dominant:
                        opt_matches = True
                        break
            elif isinstance(trait_tags, list):
                for trait in trait_tags:
                    if trait in dominant:
                        opt_matches = True
                        break
            else:
                trait = opt.get('trait_tag')
                if trait and trait in dominant:
                    opt_matches = True
            if opt_matches:
                matching_options += 1
        
        # For questions with many options, require at least 2 matches
        # to ensure the question is genuinely relevant, not tangentially connected
        if substantive_count >= 6:
            return matching_options >= 2
        return matching_options >= 1

    def _has_primary_trait_alignment(self, question: dict, session: AdaptiveSession) -> bool:
        """
        STRICT check: a question is aligned only if its options' PRIMARY traits
        (the highest-weight trait per option) overlap with the user's dominant
        traits or profile seed traits.

        This is stricter than _has_dominant_trait_overlap because it ignores
        secondary/tangential trait matches. For example, a Writing & Literature
        question whose primary trait is Writing-Comm (not in the user's profile)
        will NOT pass even if it has Creative-Skill as a secondary trait.

        Requires at least 2 options (for questions with 6+ options) or 1 option
        (for smaller questions) to have their primary trait in the dominant set.
        """
        dominant = self._get_dominant_traits(session, top_n=8)
        if not dominant:
            return True  # No dominant traits yet

        # Always allow profile-category questions
        qid = question.get('question_id')
        if qid and qid in session.profile_relevant_qids:
            return True

        # Also check profile seed traits (covers early rounds before accumulation)
        all_ref_traits = dominant | set(session.profile_seed_traits)

        options = question.get('options', [])
        matching_primary = 0
        substantive_count = 0
        for opt in options:
            if self._is_rejection_option(opt):
                continue
            substantive_count += 1
            trait_tags = opt.get('trait_tags', {})
            if isinstance(trait_tags, dict) and trait_tags:
                # Get the primary trait (highest weight)
                primary_trait = max(trait_tags, key=trait_tags.get)
                if primary_trait in all_ref_traits:
                    matching_primary += 1
            elif isinstance(trait_tags, list) and trait_tags:
                # First in list is primary
                if trait_tags[0] in all_ref_traits:
                    matching_primary += 1
            else:
                trait = opt.get('trait_tag')
                if trait and trait in all_ref_traits:
                    matching_primary += 1

        if substantive_count >= 6:
            return matching_primary >= 2
        return matching_primary >= 1

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
            if self._is_rejection_option(opt):
                continue
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
        
        # Only count substantive options (not rejection/none choices)
        substantive_options = [opt for opt in options if not self._is_rejection_option(opt)]
        if not substantive_options:
            return 0.0
        
        matching_options = 0
        total_match_weight = 0.0
        
        for opt in substantive_options:
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
        option_ratio = matching_options / len(substantive_options)
        weight_bonus = min(total_match_weight / len(substantive_options), 1.0)
        return (option_ratio + weight_bonus) / 2.0

    def create_session(self, user_id: int, user_gwa: float = None, user_strand: str = None, max_questions: int = 30, user_interests: str = None, user_skills: str = None) -> str:
        """Start a new assessment session. Returns session_id."""
        import uuid
        session_id = str(uuid.uuid4())[:8]
        
        # Normalize strand
        normalized_strand = user_strand.upper() if user_strand else "GAS"
        if normalized_strand not in STRAND_PRIORITY_TRAITS:
            normalized_strand = "GAS"
        
        # Always run all questions — min equals max so no early stop
        min_questions = max_questions
        
        # Initialize all courses with base score
        course_scores = {name: 50.0 for name in self.courses}
        
        # Apply initial GWA/Strand/Profile bonuses
        for course_name, course in self.courses.items():
            # Profile bonus is computed first so GWA bonus can be applied conditionally.
            # When a user has profile data, courses with no trait overlap with the user's
            # interests/skills should NOT be lifted by the GWA bonus — otherwise dozens of
            # irrelevant courses (e.g. Animation, Education, Agriculture) will flood the
            # initial Top Matches when the user has low GWA for the "right" courses.
            course_traits = self.course_traits.get(course_name, set())
            profile_bonus = 0.0
            if user_interests or user_skills:
                profile_bonus = self._calculate_profile_bonus(user_interests, user_skills, course_traits)
                course_scores[course_name] += profile_bonus

            # GWA bonus — only awarded when the course has some relevance to the user's
            # profile (profile_bonus >= 1.0), OR when no profile data is available at all.
            has_profile_relevance = (not (user_interests or user_skills)) or (profile_bonus >= 1.0)
            if has_profile_relevance and user_gwa and course.get('minimum_gwa'):
                gap = float(user_gwa) - float(course['minimum_gwa'])
                if gap >= 5:
                    course_scores[course_name] += 6   # Well above requirement
                elif gap >= 0:
                    course_scores[course_name] += 4   # Meets requirement
                elif gap >= -3:
                    course_scores[course_name] += 2   # Close to requirement
                elif gap >= -7:
                    course_scores[course_name] += 1   # Within reach
            
            # Strand bonus — exact match gets strong boost, trait-overlap gets moderate
            if user_strand and course.get('required_strand'):
                if user_strand.upper() == course['required_strand'].upper():
                    course_scores[course_name] += 10  # Exact strand match
                else:
                    # Check trait overlap between user's strand and course traits
                    user_strand_traits = set(STRAND_PRIORITY_TRAITS.get(normalized_strand, []))
                    course_trait_tags = self.course_traits.get(course_name, set())
                    overlap = user_strand_traits & course_trait_tags
                    if len(overlap) >= 3:
                        course_scores[course_name] += 5   # Strong trait overlap
                    elif len(overlap) >= 1:
                        course_scores[course_name] += 2   # Some trait overlap
        
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
        # Count how many explicit interest/skill keywords map to each domain.
        # Academic Interests carry 3× the vote weight of Technical & Soft Skills
        # so that the user's field of study drives question distribution.
        domain_votes: Dict[str, int] = {}
        interest_keywords = []
        skill_keywords = []
        if user_interests:
            interest_keywords = [kw.strip().lower().replace(" ", "_") for kw in user_interests.split(",") if kw.strip()]
        if user_skills:
            skill_keywords = [kw.strip().lower().replace(" ", "_") for kw in user_skills.split(",") if kw.strip()]
        all_keywords = interest_keywords + skill_keywords
        
        INTEREST_VOTE_WEIGHT = 3  # Academic interests = primary driver
        SKILL_VOTE_WEIGHT = 1    # Soft skills = bonus/secondary
        for kw in interest_keywords:
            domain = self._get_profile_domain_for_selection(kw)
            if domain:
                domain_votes[domain] = domain_votes.get(domain, 0) + INTEREST_VOTE_WEIGHT
        for kw in skill_keywords:
            domain = self._get_profile_domain_for_selection(kw)
            if domain:
                domain_votes[domain] = domain_votes.get(domain, 0) + SKILL_VOTE_WEIGHT

        # ─── FIELD-LEVEL BALANCING ───
        # Problem: If a user picks 3 healthcare interests and 1 business
        # interest, healthcare would get 9 votes vs 3 → 75% of questions.
        # From the user's POV these are 2 career fields deserving equal time.
        #
        # Fix: Normalize so each distinct domain gets the same base weight.
        # Multiple interests in the same domain add a small bonus (+1 each)
        # for richer sub-topic coverage, but don't multiply linearly.
        if domain_votes and interest_keywords:
            # Count how many interest keywords mapped to each domain
            domain_interest_count = {}
            for kw in interest_keywords:
                domain = self._get_profile_domain_for_selection(kw)
                if domain:
                    domain_interest_count[domain] = domain_interest_count.get(domain, 0) + 1

            # Normalize: every domain with interests gets base weight = INTEREST_VOTE_WEIGHT
            # plus +1 for each additional sub-interest beyond the first
            for domain in list(domain_votes.keys()):
                n_interests = domain_interest_count.get(domain, 0)
                if n_interests > 0:
                    # Skill votes for this domain (keep them as-is)
                    skill_portion = domain_votes[domain] - (n_interests * INTEREST_VOTE_WEIGHT)
                    skill_portion = max(skill_portion, 0)
                    # Base weight + diminishing bonus for extra sub-interests
                    normalized_interest_weight = INTEREST_VOTE_WEIGHT + max(0, n_interests - 1)
                    domain_votes[domain] = normalized_interest_weight + skill_portion

            print(f"[BALANCE] Normalized domain votes: {domain_votes} (interests per domain: {domain_interest_count})")

        explicit_domain_votes = domain_votes.copy()

        # Only fall back to trait-derived domain votes when the user did not
        # give clear interests/skills. This prevents strand-derived technology
        # traits from hijacking a creative profile.
        if not explicit_domain_votes:
            for trait in profile_ranked:
                branch = TRAIT_TO_BRANCH.get(trait, "")
                if branch:
                    domain_votes[branch] = domain_votes.get(branch, 0) + 1
        
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
        
        # Build domain exploration queue: ONLY profile-selected domains.
        # Do not include adjacent domains by default. This keeps a user who
        # explicitly chose arts/music from drifting into science or technology
        # unless their answers repeatedly establish a new path.
        domain_queue = [primary]
        relevant_domains = {primary}
        # Add other voted domains (from interests/skills) to BOTH queue and relevant
        for dom, _ in sorted(domain_votes.items(), key=lambda x: x[1], reverse=True):
            if dom != primary:
                if dom not in domain_queue:
                    domain_queue.append(dom)
                relevant_domains.add(dom)
        # Add strand domain only when the profile did not already specify domains.
        if strand_domain and not explicit_domain_votes and strand_domain not in domain_queue:
            domain_queue.append(strand_domain)
            relevant_domains.add(strand_domain)
        # DO NOT add adjacent or unrelated domains here — keep questions focused on profile

        # If the user explicitly selected domains, keep branch weights focused on
        # those domains so fallback scoring cannot drift to unrelated branches.
        if explicit_domain_votes:
            explicit_domains = set(explicit_domain_votes.keys())
            for branch in list(initial_branch_weights.keys()):
                if branch in explicit_domains:
                    initial_branch_weights[branch] = max(initial_branch_weights.get(branch, 0.0), 4.0 + explicit_domain_votes.get(branch, 0))
                else:
                    initial_branch_weights[branch] = min(initial_branch_weights.get(branch, 0.0), 0.1)
            session.branch_weights = initial_branch_weights.copy()
        
        session.domain_queue = domain_queue
        session.relevant_domains = relevant_domains
        session.domain_vote_weights = dict(explicit_domain_votes) if explicit_domain_votes else {}
        
        # ─── PROFILE CATEGORY MATCHING: Build focused question pool ───
        # Map user's interest/skill keywords to question categories so
        # questions directly related to their stated interests are prioritized.
        profile_categories = set()
        for kw in all_keywords:
            cat_keywords = self._get_profile_category_keywords_for_selection(kw)
            for cat_kw in cat_keywords:
                profile_categories.add(cat_kw)
        
        # Build the set of QIDs whose categories match profile interests.
        # Use token-based matching so broad labels like "Business" do not
        # accidentally match "Agribusiness", while multi-word labels like
        # "Database & Information" still match "Database & Information Systems".
        profile_relevant_qids = set()
        if profile_categories:
            # Per-keyword threshold: each keyword must have ALL its tokens
            # present in the category.  _category_match_score already returns
            # len(keyword_tokens) on a full subset match and 0 otherwise,
            # so threshold = 1 is sufficient (a 1-token keyword like "Maritime"
            # scores 1 when matched, a 3-token keyword scores 3).
            for qid, question in self.questions.items():
                q_cat = question.get('category', '')
                for cat_kw in profile_categories:
                    if self._category_match_score(q_cat, cat_kw) >= 1:
                        profile_relevant_qids.add(qid)
                        break

        # ── TRAIT-BASED POOL EXPANSION ──
        # Category keyword matching misses newer questions with different
        # category naming conventions.  Also include branch-relevant questions
        # whose option traits overlap with the user's profile traits — this
        # pulls Batch 15+ scenario-style questions into the candidate pool.
        _profile_trait_set = set(profile_ranked[:10]) if profile_ranked else set()
        if _profile_trait_set and relevant_domains:
            for qid, question in self.questions.items():
                if qid in profile_relevant_qids:
                    continue
                node = QUESTION_TREE_NODES.get(qid)
                if not node or not set(node.get("branches", [])) & relevant_domains:
                    continue
                # Collect traits this question covers
                _q_traits = set()
                for _opt in question.get("options", []):
                    _tt = _opt.get("trait_tags", {})
                    if isinstance(_tt, dict):
                        for _t, _w in _tt.items():
                            if isinstance(_w, (int, float)) and _w >= 0.5:
                                _q_traits.add(_t)
                    elif isinstance(_tt, list):
                        _q_traits.update(_tt)
                # Require at least 2 profile traits present to avoid
                # overly loose matching on single generic traits
                if len(_q_traits & _profile_trait_set) >= 2:
                    profile_relevant_qids.add(qid)
        
        session.profile_categories = profile_categories
        session.profile_relevant_qids = profile_relevant_qids
        
        print(f"[PROFILE] Category keywords: {sorted(profile_categories)[:8]}")
        print(f"[PROFILE] Matching QIDs: {len(profile_relevant_qids)} questions in profile pool")
        
        # Preload the first chain: entry questions for primary domain
        # PRIORITIZE profile-relevant questions at the front
        entry_qs = DOMAIN_ENTRY_QUESTIONS.get(primary, [])
        if profile_relevant_qids:
            # Put profile-matching entry questions first, then others
            profile_entry = [q for q in entry_qs if q in profile_relevant_qids]
            if profile_entry:
                session.chain_queue = profile_entry
            else:
                session.chain_queue = [
                    qid for qid in sorted(profile_relevant_qids)
                    if self._question_in_domain(qid, primary)
                ]
        else:
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

        current_chain_domain = ""
        if session.current_chain_trait:
            current_chain_domain = TRAIT_TO_BRANCH.get(session.current_chain_trait, "")
        elif session.last_answer_trait:
            current_chain_domain = TRAIT_TO_BRANCH.get(session.last_answer_trait, "")

        # Calculate per-domain budget PROPORTIONAL to vote weights.
        # Academic interests carry 3× the vote weight, so interest-driven domains
        # get proportionally more questions than skill-derived domains.
        num_voted_domains = max(len(session.domain_queue), 1)
        if current_chain_domain and session.domain_vote_weights:
            total_weight = sum(session.domain_vote_weights.get(d, 1) for d in session.domain_queue) or 1
            current_weight = session.domain_vote_weights.get(current_chain_domain, 1)
            proportion = current_weight / total_weight
            domain_budget = max(int(session.max_questions * proportion), DOMAIN_MIN_QUESTIONS)
        else:
            domain_budget = max(session.max_questions // num_voted_domains, DOMAIN_MIN_QUESTIONS)
        domain_budget = min(domain_budget, DOMAIN_MAX_QUESTIONS_HARD_CAP)

        current_domain_count = session.domain_question_count.get(current_chain_domain, 0)
        sorted_branch_weights = sorted(session.branch_weights.values(), reverse=True)
        dominant_branch = max(session.branch_weights, key=session.branch_weights.get) if session.branch_weights else ""
        top_branch_weight = sorted_branch_weights[0] if sorted_branch_weights else 0.0
        second_branch_weight = sorted_branch_weights[1] if len(sorted_branch_weights) > 1 else 0.0
        recent_same_branch = session.branch_history[-4:].count(current_chain_domain) if current_chain_domain else 0
        # Also check recent history for dominant branch (even if current chain domain differs)
        recent_dominant_count = sum(1 for b in session.branch_history[-4:] if b == dominant_branch) if dominant_branch else 0
        strong_branch_lock = (
            current_chain_domain and
            current_chain_domain == dominant_branch and
            (
                top_branch_weight >= second_branch_weight + 2.5 or
                recent_same_branch >= 3
            )
        )
        # Secondary lock: if the dominant branch is overwhelmingly strong,
        # prevent rotation even when current_chain_domain differs (e.g., chain
        # was cleared by a previous rotation or user answered an off-domain question).
        # This prevents bouncing away from the user's clear interest area.
        if not strong_branch_lock and dominant_branch:
            dominant_is_overwhelming = (
                top_branch_weight >= second_branch_weight + 4.0 or
                recent_dominant_count >= 3
            )
            if dominant_is_overwhelming and current_chain_domain != dominant_branch:
                # Redirect to the dominant domain instead of rotating away
                current_chain_domain = dominant_branch
                current_domain_count = session.domain_question_count.get(current_chain_domain, 0)
                strong_branch_lock = True
                print(f"[LOCK-REDIRECT] Redirecting to dominant domain '{dominant_branch}' "
                      f"(weight gap: {top_branch_weight - second_branch_weight:.1f}, recent: {recent_dominant_count})")
        
        # Override: when other explicitly-voted domains with similar weight
        # haven't received their fair share, force rotation even if the current
        # domain has strong branch lock. This prevents the first-served domain
        # from monopolizing questions when the user selected equal-weight interests.
        other_domains_starved = False
        if current_chain_domain and current_domain_count >= domain_budget and strong_branch_lock and session.domain_vote_weights:
            current_vote_w = session.domain_vote_weights.get(current_chain_domain, 0)
            for dom in session.domain_queue:
                if dom == current_chain_domain:
                    continue
                dom_vote_w = session.domain_vote_weights.get(dom, 0)
                if dom_vote_w < current_vote_w * 0.5:
                    continue  # Skip low-weight domains
                dom_count = session.domain_question_count.get(dom, 0)
                total_w = sum(session.domain_vote_weights.get(d, 1) for d in session.domain_queue) or 1
                dom_proportion = dom_vote_w / total_w
                dom_target = max(int(session.max_questions * dom_proportion), DOMAIN_MIN_QUESTIONS)
                if dom_count < dom_target:
                    other_domains_starved = True
                    print(f"[ROTATE-FAIRNESS] Domain '{dom}' has {dom_count}/{dom_target} questions "
                          f"(weight {dom_vote_w}) — overriding branch lock on '{current_chain_domain}'.")
                    break

        force_domain_rotation = (
            current_chain_domain and
            current_domain_count >= domain_budget
        )

        if current_chain_domain and current_domain_count >= domain_budget and strong_branch_lock and not other_domains_starved:
            # Even with strong branch lock, always enforce budget to ensure
            # equal question distribution across career fields.
            print(f"[ROTATE-BUDGET] Domain '{current_chain_domain}' hit budget {domain_budget} — rotating despite branch lock.")

        if force_domain_rotation:
            print(f"[ROTATE] Domain '{current_chain_domain}' has {current_domain_count} questions "
                  f"(budget={domain_budget}). Skipping chain to rotate.")
            session.current_chain_trait = ""
            session.chain_queue = []
        
        # ═══════════════════════════════════════════════════════════════════
        # PHASE 1: Try to get the next question from the current chain
        # All follow-ups must belong to profile-relevant branches.
        # ═══════════════════════════════════════════════════════════════════
        
        selected_qid = None
        selection_reason = ""
        relevant = session.relevant_domains
        profile_qids = session.profile_relevant_qids
        
        def _is_relevant_question(qid):
            """GATE: question must belong to a relevant branch.

            Profile-category matching (profile_relevant_qids) is used as a
            PREFERENCE in the multi-pass selection logic, not as a hard gate
            here. This ensures newer batch questions with scenario-style
            categories are reachable through the wider passes.
            """
            node = QUESTION_TREE_NODES.get(qid)
            if not node:
                return False  # Unclassified questions must not bypass filtering
            if not set(node["branches"]) & relevant:
                return False  # Wrong branch entirely
            return True
        
        def _passes_trait_continuity(qid):
            """Check if question has trait overlap with user's accumulated/profile traits."""
            q = self.questions.get(qid)
            if not q:
                return False
            return self._has_trait_continuity(q, session)
        
        def _is_profile_category_question(qid):
            """Check if question's category matches user's stated interests."""
            return qid in profile_qids

        remaining_profile_qids = {
            qid for qid in profile_qids
            if qid not in asked and qid in self.questions and _is_relevant_question(qid)
        }
        strict_profile_lock = bool(remaining_profile_qids)

        def _is_allowed_profile_question(qid):
            """Require profile-pool membership while relevant profile questions remain.

            Once the profile pool is exhausted, widen within the same relevant
            domain instead of ending the assessment early.
            """
            if strict_profile_lock:
                return qid in profile_qids
            return True

        def _matches_current_category_focus(qid):
            """Check if question stays in the user's current category thread."""
            return self._question_matches_category_focus(qid, session)
        
        # --- Step 1A: If we have a last_answer_trait, build a follow-up chain from it ---
        # GUARD: Only follow the last answer's chain if the trait is part of the
        # user's dominant pattern. This prevents a single "off-topic" answer
        # (e.g., rating math as excellent when the user is art-focused) from
        # hijacking the entire question chain away from the user's core interests.
        if not force_domain_rotation and session.last_answer_trait and session.last_answer_trait in TRAIT_FOLLOWUP_MAP:
            trait_is_dominant = self._is_dominant_trait(session.last_answer_trait, session)
            # In early rounds (< 5 answers), allow any trait to drive chain (still discovering)
            allow_chain = trait_is_dominant or len(session.answered_questions) < 5
            
            if allow_chain:
                followups = list(TRAIT_FOLLOWUP_MAP[session.last_answer_trait])
                random.shuffle(followups)
                # FIRST PASS: if the user is already consistent in a category family,
                # keep the follow-up in that same category before widening out.
                if profile_qids and session.current_category_focus:
                    for fq in followups:
                        if fq not in asked and fq in self.questions and _is_relevant_question(fq) and _is_profile_category_question(fq) and _matches_current_category_focus(fq):
                            fq_question = self.questions[fq]
                            if self._has_dominant_trait_overlap(fq_question, session):
                                selected_qid = fq
                                selection_reason = f"follow-up from trait {session.last_answer_trait} (category focus)"
                                session.current_chain_trait = session.last_answer_trait
                                break
                # FIRST PASS: prefer follow-ups that match user's profile categories
                if profile_qids and not selected_qid:
                    for fq in followups:
                        if fq not in asked and fq in self.questions and _is_relevant_question(fq) and _is_profile_category_question(fq):
                            fq_question = self.questions[fq]
                            if self._has_dominant_trait_overlap(fq_question, session):
                                selected_qid = fq
                                selection_reason = f"follow-up from trait {session.last_answer_trait} (profile match)"
                                session.current_chain_trait = session.last_answer_trait
                                break
                # SECOND PASS: allow any relevant follow-up
                if not selected_qid:
                    for fq in followups:
                        if fq not in asked and fq in self.questions and _is_relevant_question(fq):
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
        if not force_domain_rotation and not selected_qid and session.chain_queue:
            ordered_chain = list(session.chain_queue)
            random.shuffle(ordered_chain)
            if session.current_category_focus:
                # Re-sort: category-focus first, rest after (both halves already shuffled)
                ordered_chain = [q for q in ordered_chain if _matches_current_category_focus(q)] + [q for q in ordered_chain if not _matches_current_category_focus(q)]
            for cq in ordered_chain:
                if cq not in asked and cq in self.questions and _is_relevant_question(cq) and _is_allowed_profile_question(cq):
                    cq_question = self.questions[cq]
                    if self._has_dominant_trait_overlap(cq_question, session):
                        selected_qid = cq
                        selection_reason = f"chain queue (domain entry)"
                        break
                # Remove already-asked or non-qualifying questions from queue
                session.chain_queue = [q for q in session.chain_queue if q != cq]

        # --- Step 1C: If the user is staying consistent in one category family,
        # exhaust unanswered questions from that same category before widening out.
        if not force_domain_rotation and not selected_qid and session.current_category_focus:
            focused_qids = []
            for qid, question in self.questions.items():
                if qid in asked:
                    continue
                if not _is_relevant_question(qid):
                    continue
                if not _matches_current_category_focus(qid):
                    continue
                if profile_qids and qid not in profile_qids:
                    continue
                focused_qids.append(qid)

            random.shuffle(focused_qids)
            for fq in focused_qids:
                fq_question = self.questions[fq]
                if self._has_dominant_trait_overlap(fq_question, session):
                    selected_qid = fq
                    selection_reason = f"category focus ({session.current_category_focus})"
                    break
        
        # ═══════════════════════════════════════════════════════════════════
        # PHASE 2: If chain is exhausted, look at accumulated traits
        # to find the strongest unexplored path
        # ═══════════════════════════════════════════════════════════════════
        
        if not force_domain_rotation and not selected_qid:
            # Find the strongest trait that still has unanswered follow-up questions
            # Only follow traits whose follow-ups are in relevant branches AND
            # connect back to the user's dominant traits
            # FIRST: prefer profile-category matches
            sorted_traits = sorted(
                session.trait_scores.items(),
                key=lambda x: x[1],
                reverse=True
            )
            focus_only = bool(session.current_category_focus)
            if focus_only:
                for trait, score in sorted_traits:
                    if trait in TRAIT_FOLLOWUP_MAP:
                        _p2_followups = list(TRAIT_FOLLOWUP_MAP[trait])
                        random.shuffle(_p2_followups)
                        for fq in _p2_followups:
                            if fq not in asked and fq in self.questions and _is_relevant_question(fq) and _matches_current_category_focus(fq) and _is_allowed_profile_question(fq):
                                fq_question = self.questions[fq]
                                if self._has_dominant_trait_overlap(fq_question, session):
                                    selected_qid = fq
                                    selection_reason = f"strongest trait chain ({trait}, score={score:.1f}, category focus)"
                                    session.current_chain_trait = trait
                                    break
                    if selected_qid:
                        break
            if profile_qids:
                for trait, score in sorted_traits:
                    if trait in TRAIT_FOLLOWUP_MAP:
                        _p2b_followups = list(TRAIT_FOLLOWUP_MAP[trait])
                        random.shuffle(_p2b_followups)
                        for fq in _p2b_followups:
                            if fq not in asked and fq in self.questions and _is_relevant_question(fq) and _is_profile_category_question(fq):
                                fq_question = self.questions[fq]
                                if self._has_dominant_trait_overlap(fq_question, session):
                                    selected_qid = fq
                                    selection_reason = f"strongest trait chain ({trait}, score={score:.1f}, profile match)"
                                    session.current_chain_trait = trait
                                    break
                    if selected_qid:
                        break
            # THEN: allow any relevant follow-up
            if not selected_qid:
                for trait, score in sorted_traits:
                    if trait in TRAIT_FOLLOWUP_MAP:
                        _p2c_followups = list(TRAIT_FOLLOWUP_MAP[trait])
                        random.shuffle(_p2c_followups)
                        for fq in _p2c_followups:
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
                    # Prefer profile-matching entry questions when entering a new domain
                    if profile_qids:
                        sorted_entry = [q for q in entry_qs if q in profile_qids]
                        if not sorted_entry:
                            sorted_entry = [
                                qid for qid in sorted(profile_qids)
                                if self._question_in_domain(qid, domain) and qid not in asked
                            ]
                        if not sorted_entry:
                            sorted_entry = entry_qs
                    else:
                        sorted_entry = entry_qs
                    random.shuffle(sorted_entry)
                    if session.current_category_focus:
                        sorted_entry = [q for q in sorted_entry if _matches_current_category_focus(q)] + [q for q in sorted_entry if not _matches_current_category_focus(q)]
                    for eq in sorted_entry:
                        if eq not in asked and eq in self.questions and _is_relevant_question(eq) and _is_allowed_profile_question(eq):
                            selected_qid = eq
                            selection_reason = f"new domain entry ({domain})"
                            session.chain_queue = [q for q in sorted_entry if q != eq and q not in asked]
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
                if not _is_allowed_profile_question(qid):
                    continue
                # HARD GATE: must pass full relevance + alignment check
                if not _is_relevant_question(qid):
                    continue
                node = QUESTION_TREE_NODES.get(qid)
                if not node:
                    continue
                
                q_branches = set(node["branches"])
                options = question.get('options', [])
                if not options:
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
                
                # PROFILE CATEGORY BONUS — strongly prioritize questions whose
                # category directly matches user's stated interests
                if qid in profile_qids:
                    score += 15.0  # Major bonus for interest-matching questions

                # CATEGORY FOCUS BONUS — if the user has been consistently in a
                # sub-path like Fine Arts or Music, keep serving that path.
                if _matches_current_category_focus(qid):
                    score += 18.0
                
                # TRAIT CONTINUITY BONUS — strongly favor questions sharing traits
                # with the user's accumulated trait profile and profile seeds
                profile_relevance = self._question_profile_relevance_score(question, session)
                score += profile_relevance * 10.0  # Strong bonus for trait-continuous questions
                
                # DOMINANT TRAIT OVERLAP PENALTY — questions with NO overlap with
                # the user's dominant traits get a heavy penalty to push them out of
                # contention. Prevents "Writing & Literature" from appearing when
                # the user's profile is about Programming/Game Dev/Visual Arts.
                if not self._has_dominant_trait_overlap(question, session):
                    score -= 25.0
                
                # Branch affinity — boost questions whose branches overlap with profile
                relevant_overlap = len(q_branches & relevant)
                score += relevant_overlap * 2.0
                
                for branch, weight in branch_weights.items():
                    if branch in q_branches:
                        score += weight
                if q_branches:
                    score /= len(q_branches)
                
                # Information gain (skip rejection/none options)
                for opt in options:
                    if self._is_rejection_option(opt):
                        continue
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

                # Intent diversity penalty — penalize questions whose "shape"
                # matches recently asked questions (e.g. same template with
                # different category name)
                _q_intent = self._classify_question_intent(question)
                _recent = getattr(session, '_recent_intents', [])
                if _q_intent != 'GENERAL' and _q_intent in _recent[-3:]:
                    score -= 8.0

                if force_domain_rotation:
                    for branch in q_branches:
                        branch_count = session.domain_question_count.get(branch, 0)
                        if branch_count >= domain_budget:
                            score *= 0.5
                            break
                
                candidates.append((score, qid))
            
            if candidates:
                candidates.sort(reverse=True, key=lambda x: x[0])
                # Prefer a candidate with BOTH trait continuity AND dominant trait overlap
                selected_qid = None
                for c_score, c_qid in candidates:
                    c_question = self.questions.get(c_qid)
                    if c_question and self._has_dominant_trait_overlap(c_question, session) and _passes_trait_continuity(c_qid):
                        selected_qid = c_qid
                        selection_reason = f"fallback scoring with continuity (score={c_score:.1f})"
                        break
                # Second pass: relax to trait continuity only (without dominant overlap)
                if not selected_qid:
                    for c_score, c_qid in candidates:
                        if _passes_trait_continuity(c_qid):
                            selected_qid = c_qid
                            selection_reason = f"fallback scoring with trait continuity (score={c_score:.1f})"
                            break
                # Third pass: relax to dominant trait overlap only
                if not selected_qid:
                    for c_score, c_qid in candidates:
                        c_question = self.questions.get(c_qid)
                        if c_question and self._has_dominant_trait_overlap(c_question, session):
                            selected_qid = c_qid
                            selection_reason = f"fallback scoring with dominant overlap (score={c_score:.1f})"
                            break
                # Last resort: take the top scorer
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
            _safety_candidates = [qid for qid in self.questions if qid not in asked and _passes_trait_continuity(qid) and _is_relevant_question(qid) and _is_allowed_profile_question(qid)]
            if _safety_candidates:
                selected_qid = random.choice(_safety_candidates)
                selection_reason = "safety net (trait-continuous)"
                print(f"[SAFETY] Trait-continuous fallback at round {round_num}")
        
        # Last resort: any unanswered RELEVANT question to avoid premature end
        # Do NOT serve questions from unrelated branches — better to end the
        # assessment early than ask about agriculture for a programming student.
        if not selected_qid and session.round_number < session.max_questions:
            _last_resort = [qid for qid in self.questions if qid not in asked and _is_relevant_question(qid)]
            if _last_resort:
                selected_qid = random.choice(_last_resort)
                selection_reason = "safety net (last resort, relevant)"
                print(f"[SAFETY] Last resort fallback at round {round_num}")
        
        # ═══════════════════════════════════════════════════════════════════
        # NO QUESTION AVAILABLE — finalize
        # ═══════════════════════════════════════════════════════════════════
        
        if not selected_qid:
            self._finalize_session(session)
            return None
        
        # ─── RECORD SELECTION ───
        best_question = self.questions[selected_qid]

        # --- INTENT DIVERSITY SWAP ---
        # Avoid repeating the same question "shape" (e.g. "What excites you
        # about [X]?") across consecutive categories.  If the selected
        # question has the same intent as a recent question, try to swap it
        # for a same-category question with a DIFFERENT intent.
        if not hasattr(session, '_recent_intents'):
            session._recent_intents = []
            for _prev_qid in session.answered_questions:
                _prev_q = self.questions.get(_prev_qid)
                if _prev_q:
                    session._recent_intents.append(
                        self._classify_question_intent(_prev_q))

        _cur_intent = self._classify_question_intent(best_question)
        if (_cur_intent != 'GENERAL'
                and _cur_intent in session._recent_intents[-3:]):
            _cat = best_question.get('category', '')
            for _alt_qid, _alt_q in self.questions.items():
                if _alt_qid in asked or _alt_qid == selected_qid:
                    continue
                if _alt_q.get('category', '') != _cat:
                    continue
                _alt_intent = self._classify_question_intent(_alt_q)
                if (_alt_intent != 'GENERAL'
                        and _alt_intent not in session._recent_intents[-3:]):
                    selected_qid = _alt_qid
                    best_question = _alt_q
                    _cur_intent = _alt_intent
                    print(f"[INTENT-DIV] Swapped to Q{_alt_qid} "
                          f"(intent={_alt_intent}) to avoid repeating "
                          f"{session._recent_intents[-1]}")
                    break

        # --- ENHANCED SEMANTIC DEDUPLICATION ---
        # Prevents showing two questions that look or measure the same thing.
        # Uses THREE fingerprints:
        #   1. Exact option text tuple  (catches verbatim duplicates)
        #   2. Trait fingerprint: sorted primary traits (weight ≥ 0.8) across
        #      all options — catches rephrased questions with identical choices
        #   3. Specific sub-category: e.g. "Academic Interest - Programming & Coding"
        #      so the same narrow topic is never asked twice

        def _option_text_fp(q):
            return tuple(o.get("option_text", "") for o in q.get("options", []))

        def _trait_fp(q):
            """Sorted tuple of primary traits (w ≥ 0.8) across all options."""
            traits = set()
            for opt in q.get("options", []):
                tt = opt.get("trait_tags", {})
                if isinstance(tt, dict):
                    for t, w in tt.items():
                        if w >= 0.8:
                            traits.add(t)
            return tuple(sorted(traits)) if traits else ()

        def _category_key(q):
            """Return the question's narrow sub-category (if any)."""
            cat = q.get("category", "")
            # Only enforce for narrow "Academic Interest - X" categories
            if cat.startswith("Academic Interest"):
                return cat
            return None

        # Track how many times each Academic Interest sub-category has been shown
        if not hasattr(session, '_category_shown_count'):
            session._category_shown_count = {}
            for prev_qid in session.answered_questions:
                prev_q = self.questions.get(prev_qid)
                if prev_q:
                    ckey = _category_key(prev_q)
                    if ckey:
                        session._category_shown_count[ckey] = session._category_shown_count.get(ckey, 0) + 1

        # Allow up to this many questions per Academic Interest sub-category
        # before considering further questions in that category as duplicates.
        # This ensures that interest-aligned questions are not exhausted in 1 round.
        _MAX_PER_INTEREST_CATEGORY = 3

        def _is_dup(q):
            """Return True if this question is a semantic duplicate of one already shown."""
            # Check 1: exact option text
            txt_fp = _option_text_fp(q)
            if len(txt_fp) >= 4 and txt_fp in session.option_fingerprints_seen:
                return True
            # Check 2: trait fingerprint
            tfp = _trait_fp(q)
            if tfp and tfp in session._trait_fingerprints_seen:
                return True
            # Check 3: narrow category already covered (allow up to N per sub-category)
            ckey = _category_key(q)
            if ckey:
                shown = session._category_shown_count.get(ckey, 0)
                if shown >= _MAX_PER_INTEREST_CATEGORY:
                    return True
            return False

        def _record_fingerprints(q):
            """Record all fingerprints for a shown question."""
            txt_fp = _option_text_fp(q)
            session.option_fingerprints_seen.add(txt_fp)
            tfp = _trait_fp(q)
            if tfp:
                session._trait_fingerprints_seen.add(tfp)
            ckey = _category_key(q)
            if ckey:
                session._categories_seen.add(ckey)
                session._category_shown_count[ckey] = session._category_shown_count.get(ckey, 0) + 1

        # Lazily initialize the new tracking sets (avoids dataclass change)
        if not hasattr(session, '_trait_fingerprints_seen'):
            session._trait_fingerprints_seen = set()
            # Back-fill from questions already answered in this session
            for prev_qid in session.answered_questions:
                prev_q = self.questions.get(prev_qid)
                if prev_q:
                    tfp = _trait_fp(prev_q)
                    if tfp:
                        session._trait_fingerprints_seen.add(tfp)
        if not hasattr(session, '_categories_seen'):
            session._categories_seen = set()
            for prev_qid in session.answered_questions:
                prev_q = self.questions.get(prev_qid)
                if prev_q:
                    ckey = _category_key(prev_q)
                    if ckey:
                        session._categories_seen.add(ckey)

        if _is_dup(best_question):
            replacement_found = False
            # Pass 1: respect profile + relevance restrictions
            for alt_qid, alt_q in self.questions.items():
                if alt_qid in asked or alt_qid == selected_qid:
                    continue
                if not _is_relevant_question(alt_qid) or not _is_allowed_profile_question(alt_qid):
                    continue
                if _is_dup(alt_q):
                    continue
                selected_qid = alt_qid
                best_question = alt_q
                replacement_found = True
                print(f"[DEDUP] Swapped Q with semantic-duplicate -> Q{alt_qid}")
                break
            # Pass 1.5: When profile lock is active, prefer ANY profile question
            # (even a sub-category duplicate) over leaving the profile pool.
            # A repeated interest-area question is better than a generic one.
            if not replacement_found and strict_profile_lock:
                for alt_qid, alt_q in self.questions.items():
                    if alt_qid in asked or alt_qid == selected_qid:
                        continue
                    if not _is_allowed_profile_question(alt_qid):
                        continue
                    if not _is_relevant_question(alt_qid):
                        continue
                    # Allow category duplicates here — skip only exact option/trait dups
                    txt_fp = _option_text_fp(alt_q)
                    if len(txt_fp) >= 4 and txt_fp in session.option_fingerprints_seen:
                        continue
                    tfp = _trait_fp(alt_q)
                    if tfp and tfp in session._trait_fingerprints_seen:
                        continue
                    selected_qid = alt_qid
                    best_question = alt_q
                    replacement_found = True
                    print(f"[DEDUP] Swapped Q (profile priority, relaxed category) -> Q{alt_qid}")
                    break
            # Pass 2: widen to relevant unanswered questions — only when profile lock is OFF
            # IMPORTANT: Still enforce branch relevance AND trait continuity to
            # prevent unrelated topics (e.g. Writing & Literature for a
            # Programming/Arts profile)
            if not replacement_found and not strict_profile_lock:
                # Pass 2a: prefer trait-continuous + relevant
                for alt_qid, alt_q in self.questions.items():
                    if alt_qid in asked or alt_qid == selected_qid:
                        continue
                    if not _is_relevant_question(alt_qid):
                        continue
                    if not _passes_trait_continuity(alt_qid):
                        continue
                    if _is_dup(alt_q):
                        continue
                    selected_qid = alt_qid
                    best_question = alt_q
                    replacement_found = True
                    print(f"[DEDUP] Swapped Q (widened, trait-continuous) -> Q{alt_qid}")
                    break
                # Pass 2b: relax to relevant-only if no trait-continuous match
                if not replacement_found:
                    for alt_qid, alt_q in self.questions.items():
                        if alt_qid in asked or alt_qid == selected_qid:
                            continue
                        if not _is_relevant_question(alt_qid):
                            continue
                        if _is_dup(alt_q):
                            continue
                        selected_qid = alt_qid
                        best_question = alt_q
                        replacement_found = True
                        print(f"[DEDUP] Swapped Q (widened, relevant) -> Q{alt_qid}")
                        break
            # Pass 3: if still no replacement, skip and recurse (depth limit)
            if not replacement_found:
                _depth = getattr(session, '_dedup_depth', 0)
                if _depth < 5:
                    session._dedup_depth = _depth + 1
                    session.excluded_question_ids.add(selected_qid)
                    print(f"[DEDUP] No unique replacement for Q{selected_qid}, skipping")
                    return self.get_next_question(session_id)
                else:
                    session._dedup_depth = 0
        _record_fingerprints(best_question)

        # ─── HARD BUDGET GATE ───
        # Determine the question's primary domain (first match from voted domains).
        # If that domain is already at or over budget, reject and re-select.
        node = QUESTION_TREE_NODES.get(selected_qid, {})
        q_branches = set(node.get("branches", []))
        q_primary_domain = ""
        for dom in session.domain_queue:
            if dom in q_branches:
                q_primary_domain = dom
                break
        if not q_primary_domain and q_branches:
            q_primary_domain = next(iter(q_branches))

        if q_primary_domain and session.domain_vote_weights:
            total_w = sum(session.domain_vote_weights.get(d, 1) for d in session.domain_queue) or 1
            q_dom_weight = session.domain_vote_weights.get(q_primary_domain, 1)
            q_dom_budget = max(int(session.max_questions * q_dom_weight / total_w), DOMAIN_MIN_QUESTIONS)
            q_dom_count = session.domain_question_count.get(q_primary_domain, 0)
            _budget_depth = getattr(session, '_budget_gate_depth', 0)
            if q_dom_count >= q_dom_budget:
                if _budget_depth < 12:
                    session._budget_gate_depth = _budget_depth + 1
                    session.excluded_question_ids.add(selected_qid)
                    return self.get_next_question(session_id)
                else:
                    # Depth exhausted — force pick from an under-budget domain
                    session._budget_gate_depth = 0
                    under_budget_domains = []
                    for dom in session.domain_queue:
                        d_w = session.domain_vote_weights.get(dom, 1)
                        d_budget = max(int(session.max_questions * d_w / total_w), DOMAIN_MIN_QUESTIONS)
                        d_count = session.domain_question_count.get(dom, 0)
                        if d_count < d_budget:
                            under_budget_domains.append(dom)
                    if under_budget_domains:
                        for dom in under_budget_domains:
                            entry_qs = DOMAIN_ENTRY_QUESTIONS.get(dom, [])
                            for eq in entry_qs:
                                if eq not in session.answered_questions and eq not in session.excluded_question_ids and eq in self.questions and _is_relevant_question(eq):
                                    selected_qid = eq
                                    best_question = self.questions[eq]
                                    node = QUESTION_TREE_NODES.get(selected_qid, {})
                                    q_branches = set(node.get("branches", []))
                                    q_primary_domain = dom
                                    break
                            else:
                                continue
                            break
            session._budget_gate_depth = 0

        # Track the intent of the final selected question (after all swaps)
        _final_intent = self._classify_question_intent(best_question)
        session._recent_intents.append(_final_intent)
        if len(session._recent_intents) > 8:
            session._recent_intents = session._recent_intents[-8:]

        session.round_number = round_num
        
        # Track domain question count — use PRIMARY domain only to prevent
        # multi-branch questions from inflating counts across all domains.
        if q_primary_domain:
            session.domain_question_count[q_primary_domain] = session.domain_question_count.get(q_primary_domain, 0) + 1
            if session.domain_question_count[q_primary_domain] >= DOMAIN_MIN_QUESTIONS:
                session.explored_domains.add(q_primary_domain)
        else:
            # Fallback: increment all branches for unclassified questions
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
        
        # Get top courses preview (with unique-trait affinity adjustment)
        top_courses = self._get_affinity_adjusted_preview(session)
        
        return {
            "session_id": session_id,
            "round": session.round_number,
            "total_max_rounds": session.max_questions,
            "question": self._append_none_option(best_question, session),
            "courses_remaining": len(session.active_courses),
            "confidence": round(session.confidence * 100, 1),
            "can_finish_early": session.round_number >= session.min_questions,
            "top_courses_preview": top_courses
        }
    
    # ═══════════════════════════════════════════════════════════════════
    # INTENT DIVERSITY — prevents the same question "shape" across
    # consecutive categories (e.g. "What excites you about [X]?" N times)
    # ═══════════════════════════════════════════════════════════════════

    @staticmethod
    def _classify_question_intent(question: dict) -> str:
        """Classify what conceptual angle a question asks from.

        Returns one of: CAREER, SKILL, SCENARIO, CROSS_FIELD, BUILD,
        ENVIRONMENT, TEAM, SPECIALTY, WHICH_PART, INTEREST, GENERAL.
        Used to rotate question *shapes* across consecutive categories.
        """
        text = question.get('question_text', '').lower()
        if any(w in text for w in ['career', 'job ', 'role ', 'profession',
                                    'position', 'work as', 'career path',
                                    'where would you work']):
            return 'CAREER'
        if any(w in text for w in ['skill', 'master', 'learn', 'improve',
                                    'strengthen', 'expertise', 'develop first']):
            return 'SKILL'
        if any(w in text for w in ['scenario', 'imagine', 'what if', 'pretend',
                                    'suppose', 'struggling', 'situation',
                                    'challenge', 'respond to', 'how would you']):
            return 'SCENARIO'
        if any(w in text for w in ['connect with other', 'cross-disciplin',
                                    'interdisciplin', 'blend', 'other fields',
                                    'broader']):
            return 'CROSS_FIELD'
        if any(w in text for w in ['build', 'create', 'project', 'design from',
                                    'portfolio', 'showcase']):
            return 'BUILD'
        if any(w in text for w in ['environment', 'setting', 'workplace',
                                    'setup', 'work best']):
            return 'ENVIRONMENT'
        if any(w in text for w in ['team', 'collabor', 'group',
                                    'contribute to a']):
            return 'TEAM'
        if any(w in text for w in ['specialty', 'specializ', 'practice area',
                                    'branch', 'discipline', 'focus on one',
                                    'dedicated']):
            return 'SPECIALTY'
        if any(w in text for w in ['aspect', 'part ', 'workflow', 'stage ',
                                    'fulfilling', 'enjoy most', 'appeals to you']):
            return 'WHICH_PART'
        if any(w in text for w in ['excit', 'interest', 'appeal', 'drawn',
                                    'attract', 'fascinat', 'meaningful']):
            return 'INTEREST'
        return 'GENERAL'

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
        # Only count substantive options for rejection ratio
        substantive_options = [opt for opt in options if not self._is_rejection_option(opt)]
        total_options = len(substantive_options)
        
        for opt in substantive_options:
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
        if chosen_option_id == -1:
            # Special "I don't see what I want" option — build dynamically from profile
            chosen_option = self._build_profile_none_option(session)
        else:
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
        answered_category = self._normalize_category_name(question.get('category', ''))
        if answered_category:
            session.category_history.append(answered_category)
            recent_categories = session.category_history[-5:]
            category_counts: Dict[str, int] = {}
            for category in recent_categories:
                category_counts[category] = category_counts.get(category, 0) + 1
            session.current_category_focus = max(category_counts.items(), key=lambda item: item[1])[0]
        print(f"[ANSWER] Q{question_id} answered. Total answers={len(session.answered_questions)}, round={session.round_number}, excluded={len(session.excluded_question_ids)}")
        
        # Snapshot course scores BEFORE any changes (for exact reversal with "Previous" button)
        session.course_scores_snapshots[question_id] = session.course_scores.copy()
        
        # The special "I don't see what I want" option (option_id == -1) is NOT a rejection.
        # It carries profile-derived traits and should be processed like a normal answer.
        is_profile_none_option = (chosen_option_id == -1)
        
        # Check if user rejected this topic (e.g., "none", "not interested")
        option_text = chosen_option.get('option_text', '').lower()
        is_rejection = not is_profile_none_option and any(phrase in option_text for phrase in [
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
        
        # Check if this is a "None" or "Not interested" option (but NOT the profile-based option)
        is_none_option = not is_profile_none_option and any(phrase in option_text for phrase in [
            'none', 'not interested', "don't want", 'prefer not',
            'none of these', 'not for me', "i don't"
        ])
        
        # Track which traits to update course scores for: list of (trait, weight) tuples
        traits_to_boost = []
        primary_trait = None
        
        if is_none_option:
            # For "None" options, don't add any traits - the user is rejecting this topic
            # The rejection penalty was already applied above
            # This prevents arbitrary traits from being added
            print(f"[NONE_OPTION] No traits added - user rejected this topic")
            chosen_trait = None
        elif is_profile_none_option:
            # "I don't see what I want" — update course scores using profile traits
            # but do NOT add them to trait_scores (which drives question selection).
            # This prevents the profile-derived traits from making every question
            # in the database appear relevant.
            if isinstance(chosen_trait_tags, dict) and chosen_trait_tags:
                primary_trait = max(chosen_trait_tags, key=chosen_trait_tags.get)
                for trait, weight in chosen_trait_tags.items():
                    traits_to_boost.append((trait, weight))
                chosen_trait = primary_trait
            print(f"[NONE_OPTION_PROFILE] Course scores updated but traits NOT added to trait_scores")
        elif isinstance(chosen_trait_tags, dict) and chosen_trait_tags:
            # Weighted dict format: apply each trait with its weight
            primary_trait = max(chosen_trait_tags, key=chosen_trait_tags.get)
            for trait, weight in chosen_trait_tags.items():
                current = session.trait_scores.get(trait, 0)
                session.trait_scores[trait] = current + weight
                trait_changes[trait] = trait_changes.get(trait, 0) + weight
                traits_to_boost.append((trait, weight))
            chosen_trait = primary_trait
        elif isinstance(chosen_trait_tags, list) and chosen_trait_tags:
            # Legacy list format
            primary_trait = chosen_trait_tags[0]
            for idx, tag in enumerate(chosen_trait_tags):
                weight = 1.0 if idx == 0 else 0.6
                current = session.trait_scores.get(tag, 0)
                session.trait_scores[tag] = current + weight
                trait_changes[tag] = trait_changes.get(tag, 0) + weight
                traits_to_boost.append((tag, weight))
            chosen_trait = chosen_trait_tags[0]
        elif chosen_trait:
            # Fallback: single trait_tag (old format)
            primary_trait = chosen_trait
            current = session.trait_scores.get(chosen_trait, 0)
            session.trait_scores[chosen_trait] = current + 1.0
            trait_changes[chosen_trait] = 1.0
            traits_to_boost.append((chosen_trait, 1.0))
            
            # Also add mapped traits (from our enhanced trait system)
            mapped_traits = EXPANDED_TRAIT_MAPPING.get(chosen_trait, [])
            for mapped_trait in mapped_traits:
                current = session.trait_scores.get(mapped_trait, 0)
                session.trait_scores[mapped_trait] = current + 0.5
                trait_changes[mapped_trait] = trait_changes.get(mapped_trait, 0) + 0.5
                traits_to_boost.append((mapped_trait, 0.5))
        
        # Store the trait changes for this question (for reversal)
        session.answer_trait_changes[question_id] = trait_changes
        
        # Update course scores based on this answer - preserve weighted influence for multi-trait options.
        for trait, weight in traits_to_boost:
            is_primary = trait == primary_trait
            self._update_course_scores(session, trait, trait_weight=weight, is_primary=is_primary)
        
        # --- Track topic continuity for profile-driven question selection ---
        # --- Track topic continuity for profile-driven question selection ---
        # Skip for profile-based "none" option — its traits should not steer questions
        if chosen_trait and not is_profile_none_option:
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
        # Skip for profile-based "none" option — its traits should not steer questions
        if chosen_trait and not is_none_option and not is_profile_none_option:
            session.last_answer_trait = chosen_trait
            is_dominant = self._is_dominant_trait(chosen_trait, session)
            early_stage = len(session.answered_questions) < 5
            
            if is_dominant or early_stage:
                # Trait is part of user's dominant pattern — update chain normally
                if chosen_trait in TRAIT_FOLLOWUP_MAP:
                    new_chain = [q for q in TRAIT_FOLLOWUP_MAP[chosen_trait]
                                 if q not in session.excluded_question_ids and q in self.questions]
                    # Prioritize profile-matching follow-ups at the front
                    if session.profile_relevant_qids:
                        profile_chain = [q for q in new_chain if q in session.profile_relevant_qids]
                        other_chain = [q for q in new_chain if q not in session.profile_relevant_qids]
                        new_chain = profile_chain + other_chain
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
        # Skip for profile-based "none" option — its traits should not steer questions
        if chosen_trait and not is_none_option and not is_profile_none_option:
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
                
                # Dynamically expand relevant_domains if user consistently picks a new domain.
                # Guard: require higher threshold for domains far from the user's profile,
                # and never inject entry-questions for expanded domains so they don't
                # hijack the question flow.
                if chosen_branch not in session.relevant_domains:
                    branch_count = session.branch_history.count(chosen_branch)
                    # Check if this domain is adjacent to any profile domain
                    profile_domains = set(session.domain_queue[:len(session.domain_vote_weights)])
                    is_adjacent = any(
                        chosen_branch in BRANCH_ADJACENCY.get(pd, [])
                        for pd in profile_domains
                    )
                    threshold = 3 if is_adjacent else 5
                    if branch_count >= threshold:
                        session.relevant_domains.add(chosen_branch)
                        # Do NOT add to domain_queue — expanded domains should only
                        # pass the relevance filter, not receive dedicated questions.
                        print(f"[EXPAND] Domain '{chosen_branch}' added to relevant domains (picked {branch_count}x, adjacent={is_adjacent})")
        
        # Track question weight for this question (for scoring impact)
        node = QUESTION_TREE_NODES.get(question_id, {})
        q_weight = node.get("weight", 1.0)
        session.question_weights_applied[question_id] = q_weight
        
        # Calculate confidence
        session.confidence = self._calculate_confidence(session)
        
        # Get current top courses for preview (with unique-trait affinity)
        top_courses = self._get_affinity_adjusted_preview(session)
        
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
    
    def _update_course_scores(self, session: AdaptiveSession, chosen_trait: str,
                             trait_weight: float = 1.0, is_primary: bool = True):
        """Boost course scores based on trait matches, weighted by question depth and trait importance.

        Trait *rarity* is factored in: a match on a rare/specialized trait
        (e.g. Rehab-Therapy in 6 courses) gives a much bigger signal than a
        match on a common trait (e.g. Analytical-Skill in 41 courses).  This
        prevents courses that only share broad traits from out-scoring courses
        whose specialized traits actually match the user's answers.
        """
        if not chosen_trait:
            return
        
        # Get the question weight from the decision tree node
        # Deeper questions (higher weight) have MORE impact on scoring
        last_qid = session.question_history[-1] if session.question_history else None
        question_weight = 1.0
        if last_qid:
            node = QUESTION_TREE_NODES.get(last_qid, {})
            question_weight = node.get("weight", 1.0)
        
        primary_bonus = 1.3 if is_primary else 1.0

        # Combined multiplier: question weight × trait weight × primary bonus
        total_multiplier = (
            question_weight *
            trait_weight *
            primary_bonus
        )

        # Trait rarity discount: traits shared by many courses carry less
        # discriminating signal.  _TRAIT_COURSE_COUNT is computed once on init.
        if not hasattr(self, '_trait_course_count'):
            from collections import Counter
            self._trait_course_count = Counter()
            for _cname, _ctraits in self.course_traits.items():
                for _t in _ctraits:
                    self._trait_course_count[_t] += 1
            self._total_courses = max(len(self.courses), 1)

        def _rarity_factor(trait_name: str) -> float:
            """Return 1.0 for rare traits, scaling down to 0.3 for very common ones."""
            count = self._trait_course_count.get(trait_name, 1)
            prevalence = count / self._total_courses  # 0.0 – 1.0
            # rare (≤5%) → 1.0; common (≥40%) → 0.3; linear between
            if prevalence <= 0.05:
                return 1.0
            if prevalence >= 0.40:
                return 0.3
            return 1.0 - (prevalence - 0.05) * (0.7 / 0.35)
        
        for course_name in list(session.active_courses):
            course_traits = self.course_traits.get(course_name, set())
            
            # Direct trait match — rarity-weighted boost
            if chosen_trait in course_traits:
                rf = _rarity_factor(chosen_trait)
                boost = 12.0 * total_multiplier * rf
                session.course_scores[course_name] += boost
            else:
                # Check for similar traits using our SPECIALIZED trait system
                best_similarity = 0
                best_course_trait = ""
                for course_trait in course_traits:
                    sim = self._get_specialized_similarity(chosen_trait, course_trait)
                    if sim > best_similarity:
                        best_similarity = sim
                        best_course_trait = course_trait
                
                # Similarity-based score boost — tighter thresholds & smaller
                # boosts to prevent cross-domain spillover
                if best_similarity > 0.7:
                    rf = _rarity_factor(best_course_trait)
                    session.course_scores[course_name] += 3.0 * total_multiplier * rf
                elif best_similarity > 0.5:
                    rf = _rarity_factor(best_course_trait)
                    session.course_scores[course_name] += 1.0 * total_multiplier * rf
    
    # ── Common traits list (shared between preview & finalization) ──
    _COMMON_TRAITS = frozenset({
        "Analytical-Skill", "Investigative", "People-Skill",
        "Technical-Skill", "Community-Serve", "Social", "Admin-Skill",
        "Realistic", "Artistic", "Creative-Skill", "Teaching-Ed",
        "Enterprising", "Conventional", "Physical-Skill", "Patient-Care",
    })

    def _get_affinity_adjusted_preview(self, session) -> list:
        """Return top-5 courses with unique-trait affinity factored in.

        Courses whose rare/defining traits (unique_traits = course_traits −
        COMMON_TRAITS) were never triggered by the user's answers get a 0.6×
        penalty.  Courses with ≥50 % unique trait matches get 1.15× boost.
        This prevents generic-trait spillover from pushing irrelevant courses
        to the top of the live sidebar.

        Before any answers are given, profile seed traits are used as a proxy
        so that the initial Top Matches reflect the user's stated interests
        rather than defaulting to courses with only common traits.
        """
        user_traits = set(session.trait_scores.keys())

        # Before any answers, trait_scores is empty.  Use profile seed traits
        # so the initial sidebar reflects the user's stated interests/skills
        # instead of penalizing every specialized course to 0.6×.
        if not user_traits and session.profile_seed_traits:
            user_traits = set(session.profile_seed_traits)

        adjusted = {}
        for name, raw in session.course_scores.items():
            course_traits = self.course_traits.get(name, set())
            unique_traits = course_traits - self._COMMON_TRAITS
            if unique_traits:
                matched = unique_traits & user_traits
                ratio = len(matched) / len(unique_traits)
                if ratio >= 0.5:
                    adjusted[name] = raw * 1.15
                elif ratio == 0:
                    adjusted[name] = raw * 0.6
                else:
                    adjusted[name] = raw
            else:
                adjusted[name] = raw

        sorted_courses = sorted(adjusted.items(), key=lambda x: x[1], reverse=True)
        return [
            {
                "course_name": name,
                "current_score": round(score, 1),
                "traits_matched": len(self.course_traits.get(name, set())
                                      & user_traits),
            }
            for name, score in sorted_courses[:5]
        ]

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
        """Determine if we should stop asking questions - always run all max_questions."""
        return session.round_number >= session.max_questions
    
    def _finalize_session(self, session: AdaptiveSession):
        """Build final course recommendations."""
        print(f"[OK_GREEN] FINALIZE SESSION CALLED - session_id: {session.session_id}")
        session.is_complete = True

        # ── UNIQUE TRAIT AFFINITY ADJUSTMENT ──
        # Same logic as _get_affinity_adjusted_preview, but applied to the
        # actual session scores before final ranking.
        user_traits = set(session.trait_scores.keys())
        for course_name in list(session.course_scores.keys()):
            course_traits = self.course_traits.get(course_name, set())
            unique_traits = course_traits - self._COMMON_TRAITS
            if not unique_traits:
                continue
            matched_unique = unique_traits & user_traits
            ratio = len(matched_unique) / len(unique_traits)
            if ratio >= 0.5:
                session.course_scores[course_name] *= 1.15
            elif ratio == 0:
                session.course_scores[course_name] *= 0.6

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
        
        # Rebuild option_fingerprints_seen from remaining answered questions.
        # The "next" question that was displayed (but never answered) had its
        # fingerprint recorded when get_next_question selected it.  Without
        # removing that stale fingerprint the dedup logic would replace the
        # correct follow-up with an unrelated question on re-answer.
        session.option_fingerprints_seen = set()
        for qid in session.answered_questions:
            q = self.questions.get(qid)
            if q:
                fp = tuple(o.get("option_text", "") for o in q.get("options", []))
                if len(fp) >= 4:
                    session.option_fingerprints_seen.add(fp)

        # Rebuild semantic dedup tracking sets from remaining answered questions
        if hasattr(session, '_trait_fingerprints_seen'):
            session._trait_fingerprints_seen = set()
            session._categories_seen = set()
            for qid in session.answered_questions:
                q = self.questions.get(qid)
                if q:
                    # Trait fingerprint
                    traits = set()
                    for opt in q.get("options", []):
                        tt = opt.get("trait_tags", {})
                        if isinstance(tt, dict):
                            for t, w in tt.items():
                                if w >= 0.8:
                                    traits.add(t)
                    if traits:
                        session._trait_fingerprints_seen.add(tuple(sorted(traits)))
                    # Category key
                    cat = q.get("category", "")
                    if cat.startswith("Academic Interest"):
                        session._categories_seen.add(cat)
        
        # Clean up category_history for the undone question and recalculate focus
        if question:
            undone_category = self._normalize_category_name(question.get('category', ''))
            if undone_category and session.category_history and session.category_history[-1] == undone_category:
                session.category_history.pop()
        if session.category_history:
            recent_cats = session.category_history[-5:]
            cat_counts = {}
            for c in recent_cats:
                cat_counts[c] = cat_counts.get(c, 0) + 1
            session.current_category_focus = max(cat_counts.items(), key=lambda item: item[1])[0]
        else:
            session.current_category_focus = ""
        
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
        # Use PRIMARY domain only (first match from domain_queue) to stay
        # consistent with the budget gate in get_next_question.
        session.domain_question_count = {}
        session.explored_domains = set()
        for answered_qid in session.answered_questions:
            node = QUESTION_TREE_NODES.get(answered_qid, {})
            q_branches = set(node.get("branches", []))
            primary = ""
            for dom in session.domain_queue:
                if dom in q_branches:
                    primary = dom
                    break
            if not primary and q_branches:
                primary = next(iter(q_branches))
            if primary:
                session.domain_question_count[primary] = session.domain_question_count.get(primary, 0) + 1
                if session.domain_question_count[primary] >= DOMAIN_MIN_QUESTIONS:
                    session.explored_domains.add(primary)
            else:
                for branch in q_branches:
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
        
        # Restore course scores from the snapshot taken BEFORE this answer was processed.
        # This guarantees the scores revert to exactly what they were, using the same
        # scoring formula that was applied going forward (no simplified recalculation).
        if previous_question_id in session.course_scores_snapshots:
            session.course_scores = session.course_scores_snapshots.pop(previous_question_id)
            print(f"[PREVIOUS] Restored course scores from snapshot for Q{previous_question_id}")
        else:
            # Fallback: recalculate if no snapshot (shouldn't happen for normal flow)
            self._recalculate_all_course_scores(session)
            print(f"[PREVIOUS] No snapshot for Q{previous_question_id}, used recalculation fallback")
        
        # Recalculate confidence
        session.confidence = self._calculate_confidence(session)
        
        # Get top courses preview (with unique-trait affinity adjustment)
        top_courses = self._get_affinity_adjusted_preview(session)
        
        print(f"[PREVIOUS] Went back to Q{previous_question_id}. Round: {session.round_number}, answers: {len(session.answered_questions)}, traits: {len(session.trait_scores)}")
        
        return {
            "status": "continue",
            "session_id": session_id,
            "round": session.round_number,
            "question": self._append_none_option(question, session),
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
