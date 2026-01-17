# seed_data.py - Course Recommendation System Data

# Import SPECIALIZED course traits (unique per career path)
from courses_specialized import COURSES_POOL_SPECIALIZED

# Use specialized traits for accurate matching (no overlap between paths)
COURSES_POOL = COURSES_POOL_SPECIALIZED

# Import specialized questions that match the new unique trait system
from questions_specialized import QUESTIONS_POOL_SPECIALIZED

# Use specialized questions for best accuracy
QUESTIONS_POOL = QUESTIONS_POOL_SPECIALIZED

# ==================== COURSE DIRECT MAPPING ====================
# Maps specific traits (SPECIALIZED unique traits) to recommended courses with weights
COURSE_DIRECT_MAPPING = {
    # ========== HEALTHCARE PATHS ==========
    "Patient-Care-Path": {
        "courses": ["BS Nursing", "BS Midwifery", "BS Respiratory Therapy"],
        "required_traits": ["Patient-Care", "Social", "People-Skill"],
        "boost_weight": 20
    },
    "Medical-Lab-Path": {
        "courses": ["BS Medical Technology", "BS Pharmacy", "BS Radiologic Technology"],
        "required_traits": ["Medical-Lab", "Investigative", "Analytical-Skill"],
        "boost_weight": 20
    },
    "Rehab-Therapy-Path": {
        "courses": ["BS Physical Therapy", "BS Occupational Therapy", "BS Speech-Language Pathology"],
        "required_traits": ["Rehab-Therapy", "Social", "Physical-Skill"],
        "boost_weight": 20
    },
    "Health-Admin-Path": {
        "courses": ["BS Health Information Management", "BS Hospital Administration"],
        "required_traits": ["Health-Admin", "Conventional", "Admin-Skill"],
        "boost_weight": 20
    },
    
    # ========== TECHNOLOGY PATHS ==========
    "Software-Dev-Path": {
        "courses": ["BS Computer Science", "BS Information Technology", "BS Information Systems", "BS Entertainment and Multimedia Computing"],
        "required_traits": ["Software-Dev", "Investigative", "Technical-Skill"],
        "boost_weight": 20
    },
    "Hardware-Systems-Path": {
        "courses": ["BS Computer Engineering", "BS Electronics Engineering"],
        "required_traits": ["Hardware-Systems", "Realistic", "Technical-Skill"],
        "boost_weight": 20
    },
    "Data-Analytics-Path": {
        "courses": ["BS Data Science", "BS Statistics", "BS Applied Mathematics"],
        "required_traits": ["Data-Analytics", "Investigative", "Analytical-Skill"],
        "boost_weight": 20
    },
    "Cyber-Defense-Path": {
        "courses": ["BS Cybersecurity", "BS Information Technology"],
        "required_traits": ["Cyber-Defense", "Investigative", "Technical-Skill"],
        "boost_weight": 20
    },
    
    # ========== ENGINEERING PATHS ==========
    "Civil-Build-Path": {
        "courses": ["BS Civil Engineering", "BS Geodetic Engineering"],
        "required_traits": ["Civil-Build", "Realistic", "Technical-Skill"],
        "boost_weight": 20
    },
    "Electrical-Power-Path": {
        "courses": ["BS Electrical Engineering"],
        "required_traits": ["Electrical-Power", "Realistic", "Technical-Skill"],
        "boost_weight": 20
    },
    "Mechanical-Design-Path": {
        "courses": ["BS Mechanical Engineering", "BS Aerospace Engineering"],
        "required_traits": ["Mechanical-Design", "Realistic", "Technical-Skill"],
        "boost_weight": 20
    },
    "Industrial-Ops-Path": {
        "courses": ["BS Industrial Engineering", "BS Manufacturing Engineering"],
        "required_traits": ["Industrial-Ops", "Enterprising", "Analytical-Skill"],
        "boost_weight": 20
    },
    
    # ========== BUSINESS PATHS ==========
    "Finance-Acct-Path": {
        "courses": ["BS Accountancy", "BS Management Accounting", "BS Business Administration major in Financial Management", "BS Internal Auditing"],
        "required_traits": ["Finance-Acct", "Conventional", "Analytical-Skill"],
        "boost_weight": 20
    },
    "Marketing-Sales-Path": {
        "courses": ["BS Business Administration major in Marketing Management", "BS Advertising", "BS Business Economics"],
        "required_traits": ["Marketing-Sales", "Enterprising", "People-Skill"],
        "boost_weight": 20
    },
    "Startup-Venture-Path": {
        "courses": ["BS Entrepreneurship", "BS Business Administration major in Operations Management", "BS Real Estate Management"],
        "required_traits": ["Startup-Venture", "Enterprising", "People-Skill"],
        "boost_weight": 20
    },
    
    # ========== EDUCATION PATHS ==========
    "Teaching-Ed-Path": {
        "courses": ["Bachelor of Elementary Education", "Bachelor of Secondary Education", "Bachelor of Early Childhood Education", "Bachelor of Special Needs Education", "Bachelor of Physical Education", "Bachelor of Technical-Vocational Teacher Education"],
        "required_traits": ["Teaching-Ed", "Social", "People-Skill"],
        "boost_weight": 20
    },
    
    # ========== ARTS & DESIGN PATHS ==========
    "Visual-Design-Path": {
        "courses": ["Bachelor of Fine Arts", "BA in Photography", "BS Graphic Design"],
        "required_traits": ["Visual-Design", "Artistic", "Creative-Skill"],
        "boost_weight": 20
    },
    "Digital-Media-Path": {
        "courses": ["BA in Animation", "BS Multimedia Arts", "BA in Digital Cinema", "BS Entertainment and Multimedia Computing"],
        "required_traits": ["Digital-Media", "Artistic", "Creative-Skill"],
        "boost_weight": 20
    },
    "Spatial-Design-Path": {
        "courses": ["BS Architecture", "BS Interior Design", "BS Landscape Architecture"],
        "required_traits": ["Spatial-Design", "Artistic", "Creative-Skill"],
        "boost_weight": 20
    },
    
    # ========== SCIENCE & RESEARCH PATHS ==========
    "Lab-Research-Path": {
        "courses": ["BS Biology", "BS Chemistry", "BS Biochemistry", "BS Microbiology", "BS Biotechnology"],
        "required_traits": ["Lab-Research", "Investigative", "Analytical-Skill"],
        "boost_weight": 20
    },
    "Field-Research-Path": {
        "courses": ["BS Environmental Science", "BS Marine Biology", "BS Geology", "BS Physics"],
        "required_traits": ["Field-Research", "Investigative", "Analytical-Skill"],
        "boost_weight": 20
    },
    
    # ========== PUBLIC SERVICE PATHS ==========
    "Law-Enforce-Path": {
        "courses": ["BS Criminology", "BS Forensic Science"],
        "required_traits": ["Law-Enforce", "Realistic", "Physical-Skill"],
        "boost_weight": 20
    },
    "Community-Serve-Path": {
        "courses": ["BS Social Work", "BS Community Development", "Bachelor of Public Administration", "BA in Political Science"],
        "required_traits": ["Community-Serve", "Social", "People-Skill"],
        "boost_weight": 20
    },
    
    # ========== MARITIME PATH ==========
    "Maritime-Sea-Path": {
        "courses": ["BS Marine Transportation", "BS Marine Engineering"],
        "required_traits": ["Maritime-Sea", "Realistic", "Physical-Skill"],
        "boost_weight": 20
    },
    
    # ========== AGRICULTURE & NATURE PATH ==========
    "Agri-Nature-Path": {
        "courses": ["BS Agriculture", "BS Agribusiness", "BS Fisheries", "BS Forestry", "Doctor of Veterinary Medicine"],
        "required_traits": ["Agri-Nature", "Realistic", "Physical-Skill"],
        "boost_weight": 20
    },
    
    # ========== HOSPITALITY PATH ==========
    "Hospitality-Svc-Path": {
        "courses": ["BS Hospitality Management", "BS Tourism Management", "BS Culinary Management", "BS Office Administration"],
        "required_traits": ["Hospitality-Svc", "Enterprising", "People-Skill"],
        "boost_weight": 20
    }
}

# ==================== SCALE QUESTION PROCESSING CONFIG ====================
SCALE_WEIGHTS = {
    5: {"multiplier": 2.0, "confidence_boost": 20},   # Extremely/Very strong
    4: {"multiplier": 1.5, "confidence_boost": 10},   # Very/Strong
    3: {"multiplier": 1.0, "confidence_boost": 0},    # Moderate/Neutral
    2: {"multiplier": 0.5, "confidence_boost": -5},   # Slight/Low
    1: {"multiplier": 0.25, "confidence_boost": -10}  # Not at all/Very low
}

# ==================== ENHANCED ALGORITHM CONFIGURATIONS ====================

# === LEARNING STYLE MAPPING ===
# Maps trait tags to learning style categories
LEARNING_STYLE_MAPPING = {
    "visual": ["Visual-learner", "Creative-expression", "Artistic-passion", "Aesthetic-sense", "Cinematic-vision", "Digital-art"],
    "hands_on": ["Hands-on", "Practical", "Field-work", "Laboratory", "Active", "Technical"],
    "theoretical": ["Theoretical", "Research-oriented", "Analytical", "Abstract-thinking", "Contemplative", "Scientific-thinking"],
    "social": ["Collaborative", "Extroverted", "Team-centric", "Social", "Helping-others", "Mentoring"],
    "independent": ["Independent", "Introverted", "Detail-focused", "Methodical", "Systematic", "Office-based"]
}

# === WORK ENVIRONMENT MAPPING ===
# Maps courses to their primary work environments
WORK_ENVIRONMENT_MAPPING = {
    "office": ["Office-based", "Remote-friendly", "Systematic", "Administrative-skills"],
    "field": ["Field-work", "Outdoor-enthusiast", "Nature-connected", "Adventurous"],
    "clinical": ["Clinical-setting", "Patient-focused", "Healthcare", "Empathetic"],
    "laboratory": ["Laboratory", "Research-oriented", "Scientific-thinking", "Detail-focused"],
    "creative_studio": ["Studio-work", "Creative-expression", "Artistic-passion", "Visual-learner"],
    "active_physical": ["Active", "Athletic-passion", "Physical-fitness", "Hands-on"]
}

# === COURSE EMPLOYABILITY & DEMAND SCORES ===
# Based on CHED, DOLE, and job market data for Philippines (1-10 scale)
COURSE_EMPLOYABILITY = {
    # Very High Demand (9-10)
    "BS Nursing": {"demand_score": 10, "ofw_opportunity": True, "gov_opportunity": True, "salary_potential": "high"},
    "BS Information Technology": {"demand_score": 9, "ofw_opportunity": True, "gov_opportunity": True, "salary_potential": "high"},
    "BS Computer Science": {"demand_score": 9, "ofw_opportunity": True, "gov_opportunity": True, "salary_potential": "very_high"},
    "BS Accountancy": {"demand_score": 9, "ofw_opportunity": True, "gov_opportunity": True, "salary_potential": "high"},
    "BS Civil Engineering": {"demand_score": 9, "ofw_opportunity": True, "gov_opportunity": True, "salary_potential": "high"},
    "BS Medical Technology": {"demand_score": 9, "ofw_opportunity": True, "gov_opportunity": True, "salary_potential": "high"},
    "BS Pharmacy": {"demand_score": 8, "ofw_opportunity": True, "gov_opportunity": True, "salary_potential": "high"},
    
    # High Demand (7-8)
    "Bachelor of Elementary Education": {"demand_score": 8, "ofw_opportunity": False, "gov_opportunity": True, "salary_potential": "moderate"},
    "Bachelor of Secondary Education": {"demand_score": 8, "ofw_opportunity": False, "gov_opportunity": True, "salary_potential": "moderate"},
    "BS Criminology": {"demand_score": 8, "ofw_opportunity": False, "gov_opportunity": True, "salary_potential": "moderate"},
    "BS Electrical Engineering": {"demand_score": 8, "ofw_opportunity": True, "gov_opportunity": True, "salary_potential": "high"},
    "BS Mechanical Engineering": {"demand_score": 8, "ofw_opportunity": True, "gov_opportunity": True, "salary_potential": "high"},
    "BS Marine Transportation": {"demand_score": 8, "ofw_opportunity": True, "gov_opportunity": False, "salary_potential": "very_high"},
    "BS Marine Engineering": {"demand_score": 8, "ofw_opportunity": True, "gov_opportunity": False, "salary_potential": "very_high"},
    "BS Physical Therapy": {"demand_score": 8, "ofw_opportunity": True, "gov_opportunity": True, "salary_potential": "high"},
    "BS Hospitality Management": {"demand_score": 7, "ofw_opportunity": True, "gov_opportunity": False, "salary_potential": "moderate"},
    "BS Tourism Management": {"demand_score": 7, "ofw_opportunity": True, "gov_opportunity": False, "salary_potential": "moderate"},
    "BS Agriculture": {"demand_score": 7, "ofw_opportunity": False, "gov_opportunity": True, "salary_potential": "moderate"},
    "BS Midwifery": {"demand_score": 7, "ofw_opportunity": True, "gov_opportunity": True, "salary_potential": "moderate"},
    "Bachelor of Public Administration": {"demand_score": 7, "ofw_opportunity": False, "gov_opportunity": True, "salary_potential": "moderate"},
    "BS Social Work": {"demand_score": 7, "ofw_opportunity": False, "gov_opportunity": True, "salary_potential": "moderate"},
    
    # Moderate Demand (5-6)
    "BS Psychology": {"demand_score": 6, "ofw_opportunity": False, "gov_opportunity": True, "salary_potential": "moderate"},
    "BS Architecture": {"demand_score": 6, "ofw_opportunity": True, "gov_opportunity": True, "salary_potential": "high"},
    "BS Business Administration major in Marketing Management": {"demand_score": 6, "ofw_opportunity": False, "gov_opportunity": False, "salary_potential": "moderate"},
    "BS Business Administration major in Financial Management": {"demand_score": 6, "ofw_opportunity": False, "gov_opportunity": True, "salary_potential": "moderate"},
    "BS Entrepreneurship": {"demand_score": 5, "ofw_opportunity": False, "gov_opportunity": False, "salary_potential": "variable"},
    "BS Culinary Management": {"demand_score": 6, "ofw_opportunity": True, "gov_opportunity": False, "salary_potential": "moderate"},
    "BS Multimedia Arts": {"demand_score": 6, "ofw_opportunity": False, "gov_opportunity": False, "salary_potential": "moderate"},
    "BA in Communication": {"demand_score": 5, "ofw_opportunity": False, "gov_opportunity": True, "salary_potential": "moderate"},
    "BS Fisheries": {"demand_score": 5, "ofw_opportunity": False, "gov_opportunity": True, "salary_potential": "low"},
    "BS Forestry": {"demand_score": 5, "ofw_opportunity": False, "gov_opportunity": True, "salary_potential": "low"}
}

# === COURSE ACCESSIBILITY IN PUBLIC SCHOOLS ===
# Availability in SUCs (State Universities and Colleges) - affects affordability
COURSE_PUBLIC_AVAILABILITY = {
    # Widely Available (most SUCs offer these)
    "Bachelor of Elementary Education": {"availability": "very_high", "typical_tuition": "free_in_suc", "scholarship_available": True},
    "Bachelor of Secondary Education": {"availability": "very_high", "typical_tuition": "free_in_suc", "scholarship_available": True},
    "BS Criminology": {"availability": "very_high", "typical_tuition": "free_in_suc", "scholarship_available": True},
    "BS Information Technology": {"availability": "very_high", "typical_tuition": "free_in_suc", "scholarship_available": True},
    "BS Agriculture": {"availability": "very_high", "typical_tuition": "free_in_suc", "scholarship_available": True},
    "BS Fisheries": {"availability": "high", "typical_tuition": "free_in_suc", "scholarship_available": True},
    "BS Forestry": {"availability": "high", "typical_tuition": "free_in_suc", "scholarship_available": True},
    "Bachelor of Public Administration": {"availability": "high", "typical_tuition": "free_in_suc", "scholarship_available": True},
    "BS Social Work": {"availability": "high", "typical_tuition": "free_in_suc", "scholarship_available": True},
    "BS Hospitality Management": {"availability": "high", "typical_tuition": "free_in_suc", "scholarship_available": True},
    "BS Tourism Management": {"availability": "high", "typical_tuition": "free_in_suc", "scholarship_available": True},
    
    # Available in Many SUCs
    "BS Nursing": {"availability": "moderate", "typical_tuition": "subsidized", "scholarship_available": True},
    "BS Civil Engineering": {"availability": "moderate", "typical_tuition": "subsidized", "scholarship_available": True},
    "BS Computer Science": {"availability": "moderate", "typical_tuition": "free_in_suc", "scholarship_available": True},
    "BS Accountancy": {"availability": "moderate", "typical_tuition": "subsidized", "scholarship_available": True},
    "BS Biology": {"availability": "moderate", "typical_tuition": "free_in_suc", "scholarship_available": True},
    "BS Chemistry": {"availability": "moderate", "typical_tuition": "free_in_suc", "scholarship_available": True},
    "BS Mathematics": {"availability": "moderate", "typical_tuition": "free_in_suc", "scholarship_available": True},
    "BS Midwifery": {"availability": "moderate", "typical_tuition": "free_in_suc", "scholarship_available": True},
    
    # Limited Availability (select SUCs only)
    "BS Medical Technology": {"availability": "limited", "typical_tuition": "subsidized", "scholarship_available": True},
    "BS Pharmacy": {"availability": "limited", "typical_tuition": "subsidized", "scholarship_available": True},
    "BS Architecture": {"availability": "limited", "typical_tuition": "subsidized", "scholarship_available": True},
    "BS Marine Transportation": {"availability": "limited", "typical_tuition": "subsidized", "scholarship_available": True},
    "BS Marine Engineering": {"availability": "limited", "typical_tuition": "subsidized", "scholarship_available": True},
    
    # Primarily Private Schools
    "BS Multimedia Arts": {"availability": "low", "typical_tuition": "private_rate", "scholarship_available": False},
    "BA in Animation": {"availability": "low", "typical_tuition": "private_rate", "scholarship_available": False},
    "BS Entertainment and Multimedia Computing": {"availability": "low", "typical_tuition": "private_rate", "scholarship_available": False}
}

# === SKILL REQUIREMENT MAPPING ===
# Maps courses to required skill levels (for self-assessment matching)
COURSE_SKILL_REQUIREMENTS = {
    # Math-Heavy Courses
    "BS Computer Science": {"math": "high", "communication": "moderate", "physical": "low", "creativity": "moderate"},
    "BS Civil Engineering": {"math": "very_high", "communication": "moderate", "physical": "moderate", "creativity": "moderate"},
    "BS Accountancy": {"math": "high", "communication": "moderate", "physical": "low", "creativity": "low"},
    "BS Mathematics": {"math": "very_high", "communication": "low", "physical": "low", "creativity": "moderate"},
    "BS Statistics": {"math": "very_high", "communication": "moderate", "physical": "low", "creativity": "low"},
    "BS Physics": {"math": "very_high", "communication": "low", "physical": "low", "creativity": "moderate"},
    "BS Data Science": {"math": "high", "communication": "moderate", "physical": "low", "creativity": "moderate"},
    
    # Communication-Heavy Courses
    "Bachelor of Elementary Education": {"math": "moderate", "communication": "high", "physical": "moderate", "creativity": "high"},
    "Bachelor of Secondary Education": {"math": "moderate", "communication": "high", "physical": "low", "creativity": "moderate"},
    "BA in Communication": {"math": "low", "communication": "very_high", "physical": "low", "creativity": "high"},
    "BA in Journalism": {"math": "low", "communication": "very_high", "physical": "moderate", "creativity": "high"},
    "BS Social Work": {"math": "low", "communication": "high", "physical": "moderate", "creativity": "moderate"},
    "Bachelor of Public Administration": {"math": "moderate", "communication": "high", "physical": "low", "creativity": "low"},
    
    # Physical/Active Courses
    "BS Criminology": {"math": "low", "communication": "moderate", "physical": "high", "creativity": "low"},
    "Bachelor of Physical Education": {"math": "low", "communication": "moderate", "physical": "very_high", "creativity": "moderate"},
    "BS Marine Transportation": {"math": "moderate", "communication": "moderate", "physical": "high", "creativity": "low"},
    "BS Agriculture": {"math": "moderate", "communication": "low", "physical": "high", "creativity": "moderate"},
    "BS Nursing": {"math": "moderate", "communication": "high", "physical": "high", "creativity": "low"},
    
    # Creative Courses
    "Bachelor of Fine Arts": {"math": "low", "communication": "moderate", "physical": "moderate", "creativity": "very_high"},
    "BS Architecture": {"math": "high", "communication": "moderate", "physical": "low", "creativity": "very_high"},
    "BS Multimedia Arts": {"math": "low", "communication": "moderate", "physical": "low", "creativity": "very_high"},
    "BA in Animation": {"math": "low", "communication": "low", "physical": "low", "creativity": "very_high"},
    "BS Interior Design": {"math": "moderate", "communication": "moderate", "physical": "low", "creativity": "very_high"},
    
    # Balanced Courses
    "BS Information Technology": {"math": "moderate", "communication": "moderate", "physical": "low", "creativity": "moderate"},
    "BS Hospitality Management": {"math": "low", "communication": "high", "physical": "moderate", "creativity": "moderate"},
    "BS Tourism Management": {"math": "low", "communication": "high", "physical": "moderate", "creativity": "moderate"},
    "BS Psychology": {"math": "moderate", "communication": "high", "physical": "low", "creativity": "moderate"}
}

# === CAREER GOAL MAPPING ===
# Maps career goals/aspirations to suitable courses
CAREER_GOAL_MAPPING = {
    "ofw_healthcare": ["BS Nursing", "BS Physical Therapy", "BS Medical Technology", "BS Midwifery", "BS Respiratory Therapy"],
    "ofw_maritime": ["BS Marine Transportation", "BS Marine Engineering"],
    "ofw_hospitality": ["BS Hospitality Management", "BS Tourism Management", "BS Culinary Management"],
    "ofw_tech": ["BS Computer Science", "BS Information Technology", "BS Data Science"],
    "government_service": ["Bachelor of Public Administration", "BS Criminology", "Bachelor of Elementary Education", "Bachelor of Secondary Education", "BS Social Work"],
    "teaching": ["Bachelor of Elementary Education", "Bachelor of Secondary Education", "Bachelor of Special Needs Education", "Bachelor of Physical Education", "Bachelor of Technical-Vocational Teacher Education"],
    "healthcare_local": ["BS Nursing", "BS Medical Technology", "BS Pharmacy", "BS Physical Therapy", "BS Midwifery"],
    "business_entrepreneur": ["BS Entrepreneurship", "BS Business Administration major in Marketing Management", "BS Accountancy", "BS Business Administration major in Financial Management"],
    "agriculture_rural": ["BS Agriculture", "BS Agribusiness", "BS Fisheries", "BS Forestry"],
    "tech_startup": ["BS Computer Science", "BS Information Technology", "BS Data Science", "BS Entertainment and Multimedia Computing"],
    "creative_arts": ["Bachelor of Fine Arts", "BS Multimedia Arts", "BA in Animation", "BA in Music Production", "BS Architecture"],
    "law_enforcement": ["BS Criminology", "BS Forensic Science"],
    "community_service": ["BS Social Work", "BS Community Development", "BS Development Communication"]
}

# === PERSONALITY-COURSE COMPATIBILITY ===
# Maps personality dimensions to course compatibility scores
PERSONALITY_COMPATIBILITY = {
    "introvert_friendly": ["BS Computer Science", "BS Mathematics", "BS Statistics", "BS Accountancy", "BA in Animation", 
                           "Bachelor of Library and Information Science", "BS Data Science", "BS Chemistry", "BS Physics",
                           "BS Biology", "BA in Philosophy"],
    "extrovert_friendly": ["BS Hospitality Management", "BS Tourism Management", "Bachelor of Elementary Education",
                           "BA in Communication", "BS Social Work", "BS Business Administration major in Marketing Management",
                           "Bachelor of Physical Education", "BA in Theater Arts", "BS Nursing"],
    "structured_preference": ["BS Accountancy", "BS Civil Engineering", "BS Criminology", "BS Nursing", 
                              "BS Medical Technology", "Bachelor of Public Administration"],
    "flexible_creative": ["BS Entrepreneurship", "Bachelor of Fine Arts", "BS Multimedia Arts", "BS Architecture",
                          "BA in Communication", "BA in Journalism", "BA in Fashion Design and Merchandising"]
}

# ==================== FILTERED QUESTION LISTS (For Algorithm Use) ====================
# Filter questions by type from the main pool for easy access
SCALE_QUESTIONS = [q for q in QUESTIONS_POOL if q.get("question_type") == "scale"]
CAREER_PATH_QUESTIONS = [q for q in QUESTIONS_POOL if q.get("question_type") == "career_path"]
EXTRACURRICULAR_QUESTIONS = [q for q in QUESTIONS_POOL if q.get("question_type") == "extracurricular"]
SITUATIONAL_MAPPED_QUESTIONS = [q for q in QUESTIONS_POOL if q.get("question_type") == "situational_mapped"]

# Standard questions (without explicit question_type)
STANDARD_QUESTIONS = [q for q in QUESTIONS_POOL if not q.get("question_type") or q.get("question_type") == "standard"]

# ==================== ASSESSMENT CONFIGURATION ====================
# With 70 questions available, we set realistic counts that allow randomization
ASSESSMENT_TIERS = {
    "quick": {
        "name": "Quick Assessment",
        "description": "A brief 15-question assessment for quick recommendations",
        "question_count": 15,
        "estimated_time": "5-8 minutes",
        "accuracy": "Moderate - Good for initial exploration"
    },
    "standard": {
        "name": "Standard Assessment",
        "description": "A comprehensive 30-question assessment for reliable recommendations",
        "question_count": 30,
        "estimated_time": "10-15 minutes",
        "accuracy": "High - Recommended for most users"
    },
    "comprehensive": {
        "name": "Comprehensive Assessment",
        "description": "A thorough 50-question assessment for highly accurate recommendations",
        "question_count": 50,
        "estimated_time": "20-25 minutes",
        "accuracy": "Very High - Most accurate recommendations"
    }
}
