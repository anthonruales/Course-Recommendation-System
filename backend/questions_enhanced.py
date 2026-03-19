# questions_enhanced.py - Enhanced Questions with Weighted Multi-Trait Options
"""
================================================================================
ENHANCED QUESTIONS - Weighted Multi-Trait Options
================================================================================

Each option has a trait_tags dictionary with UNLIMITED trait tags.
Weights indicate how strongly each trait relates to the option:
  - 1.0  = Primary/direct match (the core trait this option represents)
  - 0.8  = Strong secondary trait (closely related)
  - 0.5-0.7 = Moderate relevance
  - 0.2-0.4 = Minor/supporting relevance
  - 0.1  = Tangential but present

TRAIT → COURSE MAPPING:
├── Healthcare
│   ├── Patient-Care → Nursing, Midwifery, Nutrition
│   ├── Medical-Lab → Med Tech, Pharmacy, Radiologic Tech
│   ├── Rehab-Therapy → Physical Therapy, Occupational Therapy
│   └── Health-Admin → Health Information Management
├── Technology
│   ├── Software-Dev → Computer Science, IT, Information Systems
│   ├── Hardware-Systems → Computer Engineering, Electronics Engineering
│   ├── Data-Analytics → Data Science, Statistics
│   ├── Cyber-Defense → Cybersecurity
│   └── Digital-Media → Multimedia, Game Development, Animation
├── Engineering
│   ├── Civil-Build → Civil Engineering, Geodetic Engineering
│   ├── Mechanical-Design → Mechanical Engineering
│   ├── Electrical-Power → Electrical Engineering
│   ├── Industrial-Ops → Industrial Engineering
│   └── Spatial-Design → Architecture, Interior Design
├── Business
│   ├── Finance-Acct → Accountancy, Banking, Finance
│   ├── Marketing-Sales → Marketing, Advertising, Real Estate
│   ├── Startup-Venture → Entrepreneurship, Business Admin
│   └── Admin-Skill → Office Administration, Management
├── Education
│   └── Teaching-Ed → Elementary Ed, Secondary Ed, Early Childhood
├── Arts & Design
│   ├── Visual-Design → Fine Arts, Graphic Design
│   ├── Digital-Media → Multimedia Arts, Animation
│   └── Creative-Skill → Performing Arts, Music
├── Public Service
│   ├── Law-Enforce → Criminology, Forensic Science, Legal Management
│   └── Community-Serve → Public Admin, Social Work, Political Science
├── Maritime
│   └── Maritime-Sea → Marine Transportation, Marine Engineering
├── Agriculture
│   └── Agri-Nature → Agriculture, Forestry, Fisheries
├── Hospitality
│   └── Hospitality-Svc → Tourism, Hotel Management, Culinary Arts
└── Science
    ├── Lab-Research → Biology, Chemistry, Biochemistry
    └── Field-Research → Environmental Science, Geology, Marine Biology

================================================================================
"""

QUESTIONS_POOL_ENHANCED = [
    {
        "question_id": 1,
        "question_text": "What career would make you excited to wake up every morning?",
        "category": "Dream Career",
        "options": [
            {
                "option_id": 1,
                "option_text": "Nurse caring for patients in a hospital",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 2,
                "option_text": "Software developer creating apps and websites",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 3,
                "option_text": "Civil engineer designing buildings and bridges",
                "trait_tags": {"Civil-Build": 1.0, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Mechanical-Design": 0.2, "Industrial-Ops": 0.15}
            },
            {
                "option_id": 4,
                "option_text": "Accountant managing finances for companies",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 5,
                "option_text": "Teacher educating students in a classroom",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 6,
                "option_text": "Police officer protecting the community",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 7,
                "option_text": "Graphic designer creating visual content",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            },
            {
                "option_id": 8,
                "option_text": "Ship captain navigating across oceans",
                "trait_tags": {"Maritime-Sea": 1.0, "Realistic": 0.45, "Physical-Skill": 0.4, "Technical-Skill": 0.25, "Mechanical-Design": 0.15}
            },
            {
                "option_id": 9,
                "option_text": "Business owner running my own company",
                "trait_tags": {"Startup-Venture": 1.0, "Enterprising": 0.45, "People-Skill": 0.3, "Marketing-Sales": 0.3, "Finance-Acct": 0.2, "Creative-Skill": 0.2}
            },
            {
                "option_id": 10,
                "option_text": "Hotel manager in the hospitality industry",
                "trait_tags": {"Hospitality-Svc": 1.0, "People-Skill": 0.45, "Tourism-Travel": 0.4, "Enterprising": 0.35, "Culinary-Arts": 0.3, "Marketing-Sales": 0.2}
            }
        ]
    },
    {
        "question_id": 2,
        "question_text": "Where would you most enjoy working every day?",
        "category": "Work Environment",
        "options": [
            {
                "option_id": 11,
                "option_text": "Hospital or clinic with patients",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 12,
                "option_text": "Medical laboratory analyzing samples",
                "trait_tags": {"Medical-Lab": 1.0, "Analytical-Skill": 0.45, "Investigative": 0.4, "Lab-Research": 0.35, "Technical-Skill": 0.25, "Patient-Care": 0.2}
            },
            {
                "option_id": 13,
                "option_text": "Tech office with computers and code",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 14,
                "option_text": "Construction site or engineering firm",
                "trait_tags": {"Civil-Build": 1.0, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Mechanical-Design": 0.2, "Industrial-Ops": 0.15}
            },
            {
                "option_id": 15,
                "option_text": "Bank or corporate office",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 16,
                "option_text": "School or university classroom",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 17,
                "option_text": "Police station or courtroom",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 18,
                "option_text": "Design studio or creative agency",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            },
            {
                "option_id": 19,
                "option_text": "Ship or port facility",
                "trait_tags": {"Maritime-Sea": 1.0, "Realistic": 0.45, "Physical-Skill": 0.4, "Technical-Skill": 0.25, "Mechanical-Design": 0.15}
            },
            {
                "option_id": 20,
                "option_text": "Farm or outdoor natural environment",
                "trait_tags": {"Agri-Nature": 1.0, "Realistic": 0.45, "Physical-Skill": 0.35, "Field-Research": 0.25, "Lab-Research": 0.15}
            }
        ]
    },
    {
        "question_id": 3,
        "question_text": "What type of daily tasks would you find most fulfilling?",
        "category": "Daily Work",
        "options": [
            {
                "option_id": 21,
                "option_text": "Caring for sick people and checking vital signs",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 22,
                "option_text": "Running tests and analyzing samples in a lab",
                "trait_tags": {"Medical-Lab": 1.0, "Analytical-Skill": 0.45, "Investigative": 0.4, "Lab-Research": 0.35, "Technical-Skill": 0.25, "Patient-Care": 0.2}
            },
            {
                "option_id": 23,
                "option_text": "Writing code and debugging software",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 24,
                "option_text": "Calculating budgets and preparing financial reports",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 25,
                "option_text": "Explaining lessons and helping students understand",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 26,
                "option_text": "Investigating crimes and gathering evidence",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 27,
                "option_text": "Creating designs and visual artwork",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            },
            {
                "option_id": 28,
                "option_text": "Managing hotel guests and tourism services",
                "trait_tags": {"Hospitality-Svc": 1.0, "People-Skill": 0.45, "Tourism-Travel": 0.4, "Enterprising": 0.35, "Culinary-Arts": 0.3, "Marketing-Sales": 0.2}
            },
            {
                "option_id": 29,
                "option_text": "Operating ship equipment and navigation",
                "trait_tags": {"Maritime-Sea": 1.0, "Realistic": 0.45, "Physical-Skill": 0.4, "Technical-Skill": 0.25, "Mechanical-Design": 0.15}
            },
            {
                "option_id": 30,
                "option_text": "Planting crops and managing farmland",
                "trait_tags": {"Agri-Nature": 1.0, "Realistic": 0.45, "Physical-Skill": 0.35, "Field-Research": 0.25, "Lab-Research": 0.15}
            }
        ]
    },
    {
        "question_id": 4,
        "question_text": "Which skill would you most want to become an expert in?",
        "category": "Skill Mastery",
        "options": [
            {
                "option_id": 31,
                "option_text": "Medical procedures and patient care",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 32,
                "option_text": "Laboratory analysis and diagnostics",
                "trait_tags": {"Medical-Lab": 1.0, "Analytical-Skill": 0.45, "Investigative": 0.4, "Lab-Research": 0.35, "Technical-Skill": 0.25, "Patient-Care": 0.2}
            },
            {
                "option_id": 33,
                "option_text": "Programming and software development",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 34,
                "option_text": "Building design and construction",
                "trait_tags": {"Civil-Build": 1.0, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Mechanical-Design": 0.2, "Industrial-Ops": 0.15}
            },
            {
                "option_id": 35,
                "option_text": "Financial analysis and accounting",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 36,
                "option_text": "Teaching and education methods",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 37,
                "option_text": "Criminal investigation techniques",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 38,
                "option_text": "Graphic design and visual arts",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            },
            {
                "option_id": 39,
                "option_text": "Marketing and sales strategies",
                "trait_tags": {"Marketing-Sales": 1.0, "Enterprising": 0.45, "People-Skill": 0.4, "Startup-Venture": 0.3, "Hospitality-Svc": 0.2, "Finance-Acct": 0.15}
            },
            {
                "option_id": 40,
                "option_text": "Data analysis and statistics",
                "trait_tags": {"Data-Analytics": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Software-Dev": 0.3, "Lab-Research": 0.25, "Finance-Acct": 0.2}
            }
        ]
    },
    {
        "question_id": 5,
        "question_text": "What achievement would make you most proud?",
        "category": "Career Achievement",
        "options": [
            {
                "option_id": 41,
                "option_text": "Saving someone's life as a healthcare worker",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 42,
                "option_text": "Discovering a disease through lab analysis",
                "trait_tags": {"Medical-Lab": 1.0, "Analytical-Skill": 0.45, "Investigative": 0.4, "Lab-Research": 0.35, "Technical-Skill": 0.25, "Patient-Care": 0.2}
            },
            {
                "option_id": 43,
                "option_text": "Creating an app used by millions",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 44,
                "option_text": "Building a bridge or skyscraper",
                "trait_tags": {"Civil-Build": 1.0, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Mechanical-Design": 0.2, "Industrial-Ops": 0.15}
            },
            {
                "option_id": 45,
                "option_text": "Helping a company become profitable",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 46,
                "option_text": "Students thanking me for changing their lives",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 47,
                "option_text": "Solving a major crime case",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 48,
                "option_text": "Designing a famous logo or artwork",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            },
            {
                "option_id": 49,
                "option_text": "Building a successful business from scratch",
                "trait_tags": {"Startup-Venture": 1.0, "Enterprising": 0.45, "People-Skill": 0.3, "Marketing-Sales": 0.3, "Finance-Acct": 0.2, "Creative-Skill": 0.2}
            },
            {
                "option_id": 50,
                "option_text": "Helping my community through public service",
                "trait_tags": {"Community-Serve": 1.0, "Social": 0.45, "People-Skill": 0.4, "Teaching-Ed": 0.25, "Patient-Care": 0.2, "Law-Enforce": 0.15}
            }
        ]
    },
    {
        "question_id": 23,
        "question_text": "SITUATION: Someone collapses in front of you. What's your first instinct?",
        "category": "Situational - Emergency",
        "options": [
            {
                "option_id": 221,
                "option_text": "Rush to help - check pulse, do CPR if needed",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 222,
                "option_text": "Call emergency services immediately",
                "trait_tags": {"Admin-Skill": 1.0, "Conventional": 0.45, "Finance-Acct": 0.3, "Hospitality-Svc": 0.2}
            },
            {
                "option_id": 223,
                "option_text": "Look for a medical professional nearby",
                "trait_tags": {"People-Skill": 1.0, "Social": 0.45, "Patient-Care": 0.4, "Teaching-Ed": 0.4, "Hospitality-Svc": 0.4, "Enterprising": 0.3}
            },
            {
                "option_id": 224,
                "option_text": "Control the crowd and maintain order",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 225,
                "option_text": "Document what happened for records",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 226,
                "option_text": "Comfort the person emotionally",
                "trait_tags": {"People-Skill": 1.0, "Social": 0.45, "Patient-Care": 0.4, "Teaching-Ed": 0.4, "Hospitality-Svc": 0.4, "Enterprising": 0.3}
            },
            {
                "option_id": 227,
                "option_text": "Check if they need specific medication",
                "trait_tags": {"Medical-Lab": 1.0, "Analytical-Skill": 0.45, "Investigative": 0.4, "Lab-Research": 0.35, "Technical-Skill": 0.25, "Patient-Care": 0.2}
            },
            {
                "option_id": 228,
                "option_text": "Direct traffic if we're on the road",
                "trait_tags": {"Civil-Build": 1.0, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Mechanical-Design": 0.2, "Industrial-Ops": 0.15}
            },
            {
                "option_id": 229,
                "option_text": "I might freeze - emergencies stress me out",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 230,
                "option_text": "Film it for evidence (with permission)",
                "trait_tags": {"Digital-Media": 1.0, "Artistic": 0.4, "Creative-Skill": 0.4, "Visual-Design": 0.3, "Software-Dev": 0.2, "Technical-Skill": 0.2}
            }
        ]
    },
    {
        "question_id": 24,
        "question_text": "SITUATION: Your group project member isn't contributing. What do you do?",
        "category": "Situational - Teamwork",
        "options": [
            {
                "option_id": 231,
                "option_text": "Talk to them privately and understand why",
                "trait_tags": {"People-Skill": 1.0, "Social": 0.45, "Patient-Care": 0.4, "Teaching-Ed": 0.4, "Hospitality-Svc": 0.4, "Enterprising": 0.3}
            },
            {
                "option_id": 232,
                "option_text": "Take charge and redistribute tasks",
                "trait_tags": {"Startup-Venture": 1.0, "Enterprising": 0.45, "People-Skill": 0.3, "Marketing-Sales": 0.3, "Finance-Acct": 0.2, "Creative-Skill": 0.2}
            },
            {
                "option_id": 233,
                "option_text": "Report to the teacher",
                "trait_tags": {"Admin-Skill": 1.0, "Conventional": 0.45, "Finance-Acct": 0.3, "Hospitality-Svc": 0.2}
            },
            {
                "option_id": 234,
                "option_text": "Do their work myself to ensure quality",
                "trait_tags": {"Technical-Skill": 1.0, "Software-Dev": 0.4, "Hardware-Systems": 0.4, "Realistic": 0.35, "Mechanical-Design": 0.35, "Investigative": 0.25}
            },
            {
                "option_id": 235,
                "option_text": "Create a detailed schedule with deadlines",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 236,
                "option_text": "Focus on my creative part and let others manage",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            },
            {
                "option_id": 237,
                "option_text": "Motivate them with encouragement",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 238,
                "option_text": "Find a compromise that works for everyone",
                "trait_tags": {"Community-Serve": 1.0, "Social": 0.45, "People-Skill": 0.4, "Teaching-Ed": 0.25, "Patient-Care": 0.2, "Law-Enforce": 0.15}
            },
            {
                "option_id": 239,
                "option_text": "Analyze what's causing the delay",
                "trait_tags": {"Data-Analytics": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Software-Dev": 0.3, "Lab-Research": 0.25, "Finance-Acct": 0.2}
            },
            {
                "option_id": 240,
                "option_text": "Document everything for accountability",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            }
        ]
    },
    {
        "question_id": 25,
        "question_text": "SITUATION: You witness a car accident. What's your immediate reaction?",
        "category": "Situational - Accident",
        "options": [
            {
                "option_id": 241,
                "option_text": "Check if anyone is injured and provide first aid",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 242,
                "option_text": "Call 911/emergency services right away",
                "trait_tags": {"Admin-Skill": 1.0, "Conventional": 0.45, "Finance-Acct": 0.3, "Hospitality-Svc": 0.2}
            },
            {
                "option_id": 243,
                "option_text": "Direct traffic to prevent more accidents",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 244,
                "option_text": "Document the scene as a witness",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 245,
                "option_text": "Comfort and calm the people involved",
                "trait_tags": {"People-Skill": 1.0, "Social": 0.45, "Patient-Care": 0.4, "Teaching-Ed": 0.4, "Hospitality-Svc": 0.4, "Enterprising": 0.3}
            },
            {
                "option_id": 246,
                "option_text": "Assess the vehicle damage technically",
                "trait_tags": {"Mechanical-Design": 1.0, "Realistic": 0.45, "Technical-Skill": 0.4, "Industrial-Ops": 0.25, "Civil-Build": 0.2, "Electrical-Power": 0.2}
            },
            {
                "option_id": 247,
                "option_text": "Look for fire hazards or fuel leaks",
                "trait_tags": {"Civil-Build": 1.0, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Mechanical-Design": 0.2, "Industrial-Ops": 0.15}
            },
            {
                "option_id": 248,
                "option_text": "Take photos for insurance purposes",
                "trait_tags": {"Digital-Media": 1.0, "Artistic": 0.4, "Creative-Skill": 0.4, "Visual-Design": 0.3, "Software-Dev": 0.2, "Technical-Skill": 0.2}
            },
            {
                "option_id": 249,
                "option_text": "Help move vehicles off the road",
                "trait_tags": {"Physical-Skill": 1.0, "Realistic": 0.4, "Maritime-Sea": 0.35, "Agri-Nature": 0.35, "Law-Enforce": 0.3, "Rehab-Therapy": 0.3}
            },
            {
                "option_id": 250,
                "option_text": "Find professionals to handle it",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            }
        ]
    },
    {
        "question_id": 26,
        "question_text": "Rate your agreement: 'I enjoy solving complex math problems.'",
        "category": "Scale - Math",
        "options": [
            {
                "option_id": 251,
                "option_text": "Strongly Agree - Math is my favorite subject",
                "trait_tags": {"Data-Analytics": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Software-Dev": 0.3, "Lab-Research": 0.25, "Finance-Acct": 0.2}
            },
            {
                "option_id": 252,
                "option_text": "Agree - I'm good at math",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 253,
                "option_text": "Somewhat Agree - I can do math when I try",
                "trait_tags": {"Civil-Build": 1.0, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Mechanical-Design": 0.2, "Industrial-Ops": 0.15}
            },
            {
                "option_id": 254,
                "option_text": "Neutral - Math is just okay",
                "trait_tags": {"Admin-Skill": 1.0, "Conventional": 0.45, "Finance-Acct": 0.3, "Hospitality-Svc": 0.2}
            },
            {
                "option_id": 255,
                "option_text": "Somewhat Disagree - Math is challenging",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 256,
                "option_text": "Disagree - I prefer other subjects",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            },
            {
                "option_id": 257,
                "option_text": "Strongly Disagree - I avoid math",
                "trait_tags": {"Creative-Skill": 1.0, "Artistic": 0.45, "Visual-Design": 0.4, "Digital-Media": 0.4, "Spatial-Design": 0.35}
            },
            {
                "option_id": 258,
                "option_text": "I prefer applied math in real-world scenarios",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 259,
                "option_text": "I prefer physics/engineering math",
                "trait_tags": {"Electrical-Power": 1.0, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3, "Mechanical-Design": 0.2, "Industrial-Ops": 0.2}
            },
            {
                "option_id": 260,
                "option_text": "I prefer statistics and data math",
                "trait_tags": {"Data-Analytics": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Software-Dev": 0.3, "Lab-Research": 0.25, "Finance-Acct": 0.2}
            }
        ]
    },
    {
        "question_id": 27,
        "question_text": "Rate your agreement: 'I stay calm under pressure and stress.'",
        "category": "Scale - Stress",
        "options": [
            {
                "option_id": 261,
                "option_text": "Strongly Agree - I thrive in emergencies",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 262,
                "option_text": "Agree - I handle stress well",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 263,
                "option_text": "Somewhat Agree - I manage stress reasonably",
                "trait_tags": {"Maritime-Sea": 1.0, "Realistic": 0.45, "Physical-Skill": 0.4, "Technical-Skill": 0.25, "Mechanical-Design": 0.15}
            },
            {
                "option_id": 264,
                "option_text": "Neutral - Depends on the situation",
                "trait_tags": {"Admin-Skill": 1.0, "Conventional": 0.45, "Finance-Acct": 0.3, "Hospitality-Svc": 0.2}
            },
            {
                "option_id": 265,
                "option_text": "Somewhat Disagree - I get anxious sometimes",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 266,
                "option_text": "Disagree - I prefer calm environments",
                "trait_tags": {"Lab-Research": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Medical-Lab": 0.3, "Field-Research": 0.25, "Data-Analytics": 0.25}
            },
            {
                "option_id": 267,
                "option_text": "Strongly Disagree - Stress overwhelms me",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            },
            {
                "option_id": 268,
                "option_text": "I handle physical stress better",
                "trait_tags": {"Physical-Skill": 1.0, "Realistic": 0.4, "Maritime-Sea": 0.35, "Agri-Nature": 0.35, "Law-Enforce": 0.3, "Rehab-Therapy": 0.3}
            },
            {
                "option_id": 269,
                "option_text": "I handle mental/analytical stress better",
                "trait_tags": {"Data-Analytics": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Software-Dev": 0.3, "Lab-Research": 0.25, "Finance-Acct": 0.2}
            },
            {
                "option_id": 270,
                "option_text": "I handle social/people stress better",
                "trait_tags": {"People-Skill": 1.0, "Social": 0.45, "Patient-Care": 0.4, "Teaching-Ed": 0.4, "Hospitality-Svc": 0.4, "Enterprising": 0.3}
            }
        ]
    },
    {
        "question_id": 28,
        "question_text": "Rate your COMMUNICATION skills (1=Needs Work, 5=Excellent)",
        "category": "Scale - Communication",
        "options": [
            {
                "option_id": 271,
                "option_text": "5 - Excellent presenter and speaker",
                "trait_tags": {"Marketing-Sales": 1.0, "Enterprising": 0.45, "People-Skill": 0.4, "Startup-Venture": 0.3, "Hospitality-Svc": 0.2, "Finance-Acct": 0.15}
            },
            {
                "option_id": 272,
                "option_text": "4 - Good communicator",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 273,
                "option_text": "4 - Good writer, prefer writing over speaking",
                "trait_tags": {"Admin-Skill": 1.0, "Conventional": 0.45, "Finance-Acct": 0.3, "Hospitality-Svc": 0.2}
            },
            {
                "option_id": 274,
                "option_text": "3 - Average communication skills",
                "trait_tags": {"Technical-Skill": 1.0, "Software-Dev": 0.4, "Hardware-Systems": 0.4, "Realistic": 0.35, "Mechanical-Design": 0.35, "Investigative": 0.25}
            },
            {
                "option_id": 275,
                "option_text": "3 - Better one-on-one than groups",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 276,
                "option_text": "2 - Communication is challenging",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 277,
                "option_text": "1 - Prefer minimal communication roles",
                "trait_tags": {"Lab-Research": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Medical-Lab": 0.3, "Field-Research": 0.25, "Data-Analytics": 0.25}
            },
            {
                "option_id": 278,
                "option_text": "Better at visual communication",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            },
            {
                "option_id": 279,
                "option_text": "Better at technical communication",
                "trait_tags": {"Data-Analytics": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Software-Dev": 0.3, "Lab-Research": 0.25, "Finance-Acct": 0.2}
            },
            {
                "option_id": 280,
                "option_text": "Better at persuasive communication",
                "trait_tags": {"Startup-Venture": 1.0, "Enterprising": 0.45, "People-Skill": 0.3, "Marketing-Sales": 0.3, "Finance-Acct": 0.2, "Creative-Skill": 0.2}
            }
        ]
    },
    {
        "question_id": 29,
        "question_text": "Rate your PHYSICAL FITNESS level:",
        "category": "Scale - Physical",
        "options": [
            {
                "option_id": 281,
                "option_text": "Excellent - Very athletic, exercise daily",
                "trait_tags": {"Physical-Skill": 1.0, "Realistic": 0.4, "Maritime-Sea": 0.35, "Agri-Nature": 0.35, "Law-Enforce": 0.3, "Rehab-Therapy": 0.3}
            },
            {
                "option_id": 282,
                "option_text": "Very Good - Regular exercise, physically active",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 283,
                "option_text": "Good - Moderately fit, occasional exercise",
                "trait_tags": {"Maritime-Sea": 1.0, "Realistic": 0.45, "Physical-Skill": 0.4, "Technical-Skill": 0.25, "Mechanical-Design": 0.15}
            },
            {
                "option_id": 284,
                "option_text": "Average - Basic fitness, not very active",
                "trait_tags": {"Hospitality-Svc": 1.0, "People-Skill": 0.45, "Tourism-Travel": 0.4, "Enterprising": 0.35, "Culinary-Arts": 0.3, "Marketing-Sales": 0.2}
            },
            {
                "option_id": 285,
                "option_text": "Below Average - Prefer mental activities",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 286,
                "option_text": "Physical fitness not a priority",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 287,
                "option_text": "I prefer standing/walking jobs",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 288,
                "option_text": "I prefer desk/sitting jobs",
                "trait_tags": {"Data-Analytics": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Software-Dev": 0.3, "Lab-Research": 0.25, "Finance-Acct": 0.2}
            },
            {
                "option_id": 289,
                "option_text": "I prefer outdoor/field jobs",
                "trait_tags": {"Agri-Nature": 1.0, "Realistic": 0.45, "Physical-Skill": 0.35, "Field-Research": 0.25, "Lab-Research": 0.15}
            },
            {
                "option_id": 290,
                "option_text": "I prefer hands-on/manual jobs",
                "trait_tags": {"Technical-Skill": 1.0, "Software-Dev": 0.4, "Hardware-Systems": 0.4, "Realistic": 0.35, "Mechanical-Design": 0.35, "Investigative": 0.25}
            }
        ]
    },
    {
        "question_id": 30,
        "question_text": "Rate your CREATIVITY level:",
        "category": "Scale - Creativity",
        "options": [
            {
                "option_id": 291,
                "option_text": "Very High - I create art/designs constantly",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            },
            {
                "option_id": 292,
                "option_text": "High - I'm quite creative and imaginative",
                "trait_tags": {"Digital-Media": 1.0, "Artistic": 0.4, "Creative-Skill": 0.4, "Visual-Design": 0.3, "Software-Dev": 0.2, "Technical-Skill": 0.2}
            },
            {
                "option_id": 293,
                "option_text": "High - Creative in solving problems",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 294,
                "option_text": "Moderate - Creative when inspired",
                "trait_tags": {"Marketing-Sales": 1.0, "Enterprising": 0.45, "People-Skill": 0.4, "Startup-Venture": 0.3, "Hospitality-Svc": 0.2, "Finance-Acct": 0.15}
            },
            {
                "option_id": 295,
                "option_text": "Moderate - More practical than creative",
                "trait_tags": {"Civil-Build": 1.0, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Mechanical-Design": 0.2, "Industrial-Ops": 0.15}
            },
            {
                "option_id": 296,
                "option_text": "Low - Prefer following procedures",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 297,
                "option_text": "Low - More analytical than creative",
                "trait_tags": {"Data-Analytics": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Software-Dev": 0.3, "Lab-Research": 0.25, "Finance-Acct": 0.2}
            },
            {
                "option_id": 298,
                "option_text": "Creative in teaching methods",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 299,
                "option_text": "Creative in spatial/3D design",
                "trait_tags": {"Spatial-Design": 1.0, "Artistic": 0.35, "Creative-Skill": 0.35, "Civil-Build": 0.25, "Visual-Design": 0.25, "Technical-Skill": 0.2}
            },
            {
                "option_id": 300,
                "option_text": "Creative in writing/storytelling",
                "trait_tags": {"Creative-Skill": 1.0, "Artistic": 0.45, "Visual-Design": 0.4, "Digital-Media": 0.4, "Spatial-Design": 0.35}
            }
        ]
    },
    {
        "question_id": 31,
        "question_text": "Which subject do you enjoy MOST in school?",
        "category": "Academic - Favorite",
        "options": [
            {
                "option_id": 301,
                "option_text": "Science",
                "trait_tags": {"Lab-Research": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Medical-Lab": 0.3, "Field-Research": 0.25, "Data-Analytics": 0.25}
            },
            {
                "option_id": 302,
                "option_text": "Mathematics",
                "trait_tags": {"Data-Analytics": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Software-Dev": 0.3, "Lab-Research": 0.25, "Finance-Acct": 0.2}
            },
            {
                "option_id": 303,
                "option_text": "English",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 304,
                "option_text": "Filipino",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 305,
                "option_text": "Social Studies",
                "trait_tags": {"Community-Serve": 1.0, "Social": 0.45, "People-Skill": 0.4, "Teaching-Ed": 0.25, "Patient-Care": 0.2, "Law-Enforce": 0.15}
            },
            {
                "option_id": 306,
                "option_text": "Computer/TLE",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 307,
                "option_text": "Arts",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            },
            {
                "option_id": 308,
                "option_text": "PE",
                "trait_tags": {"Physical-Skill": 1.0, "Realistic": 0.4, "Maritime-Sea": 0.35, "Agri-Nature": 0.35, "Law-Enforce": 0.3, "Rehab-Therapy": 0.3}
            },
            {
                "option_id": 309,
                "option_text": "Accounting/Business subjects",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 310,
                "option_text": "Research/Practical Research",
                "trait_tags": {"Lab-Research": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Medical-Lab": 0.3, "Field-Research": 0.25, "Data-Analytics": 0.25}
            }
        ]
    },
    {
        "question_id": 32,
        "question_text": "Which subject do you find MOST CHALLENGING?",
        "category": "Academic - Challenge",
        "options": [
            {
                "option_id": 311,
                "option_text": "Mathematics - too many formulas",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            },
            {
                "option_id": 312,
                "option_text": "Science - too much memorization",
                "trait_tags": {"People-Skill": 1.0, "Social": 0.45, "Patient-Care": 0.4, "Teaching-Ed": 0.4, "Hospitality-Svc": 0.4, "Enterprising": 0.3}
            },
            {
                "option_id": 313,
                "option_text": "English - grammar is confusing",
                "trait_tags": {"Technical-Skill": 1.0, "Software-Dev": 0.4, "Hardware-Systems": 0.4, "Realistic": 0.35, "Mechanical-Design": 0.35, "Investigative": 0.25}
            },
            {
                "option_id": 314,
                "option_text": "Filipino - I prefer English",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 315,
                "option_text": "Social Studies - too many dates/facts",
                "trait_tags": {"Data-Analytics": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Software-Dev": 0.3, "Lab-Research": 0.25, "Finance-Acct": 0.2}
            },
            {
                "option_id": 316,
                "option_text": "PE - physical activities tire me",
                "trait_tags": {"Lab-Research": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Medical-Lab": 0.3, "Field-Research": 0.25, "Data-Analytics": 0.25}
            },
            {
                "option_id": 317,
                "option_text": "Arts - I'm not creative",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 318,
                "option_text": "Computer - technology confuses me",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 319,
                "option_text": "None - I do well in all subjects",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 320,
                "option_text": "All subjects are equally challenging",
                "trait_tags": {"Admin-Skill": 1.0, "Conventional": 0.45, "Finance-Acct": 0.3, "Hospitality-Svc": 0.2}
            }
        ]
    },
    {
        "question_id": 33,
        "question_text": "How do you prefer to study?",
        "category": "Academic - Study Style",
        "options": [
            {
                "option_id": 321,
                "option_text": "Memorizing notes and flashcards",
                "trait_tags": {"Medical-Lab": 1.0, "Analytical-Skill": 0.45, "Investigative": 0.4, "Lab-Research": 0.35, "Technical-Skill": 0.25, "Patient-Care": 0.2}
            },
            {
                "option_id": 322,
                "option_text": "Solving practice problems repeatedly",
                "trait_tags": {"Data-Analytics": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Software-Dev": 0.3, "Lab-Research": 0.25, "Finance-Acct": 0.2}
            },
            {
                "option_id": 323,
                "option_text": "Group study and discussions",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 324,
                "option_text": "Making visual diagrams and mind maps",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            },
            {
                "option_id": 325,
                "option_text": "Reading and understanding concepts deeply",
                "trait_tags": {"Lab-Research": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Medical-Lab": 0.3, "Field-Research": 0.25, "Data-Analytics": 0.25}
            },
            {
                "option_id": 326,
                "option_text": "Hands-on practice and experiments",
                "trait_tags": {"Technical-Skill": 1.0, "Software-Dev": 0.4, "Hardware-Systems": 0.4, "Realistic": 0.35, "Mechanical-Design": 0.35, "Investigative": 0.25}
            },
            {
                "option_id": 327,
                "option_text": "Watching videos and tutorials",
                "trait_tags": {"Digital-Media": 1.0, "Artistic": 0.4, "Creative-Skill": 0.4, "Visual-Design": 0.3, "Software-Dev": 0.2, "Technical-Skill": 0.2}
            },
            {
                "option_id": 328,
                "option_text": "Teaching others what I learned",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 329,
                "option_text": "Making detailed notes and outlines",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 330,
                "option_text": "Coding/building projects",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            }
        ]
    },
    {
        "question_id": 34,
        "question_text": "What work-life balance do you prefer?",
        "category": "Lifestyle",
        "options": [
            {
                "option_id": 331,
                "option_text": "Willing to work long shifts if the work is meaningful",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 332,
                "option_text": "Willing to be away from home for months",
                "trait_tags": {"Maritime-Sea": 1.0, "Realistic": 0.45, "Physical-Skill": 0.4, "Technical-Skill": 0.25, "Mechanical-Design": 0.15}
            },
            {
                "option_id": 333,
                "option_text": "Flexible hours, can work from home",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 334,
                "option_text": "Regular 9-5 office hours",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 335,
                "option_text": "School schedule with holidays off",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 336,
                "option_text": "Shift work including nights and weekends",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 337,
                "option_text": "Freelance - choose my own hours",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            },
            {
                "option_id": 338,
                "option_text": "Outdoor work following seasons",
                "trait_tags": {"Agri-Nature": 1.0, "Realistic": 0.45, "Physical-Skill": 0.35, "Field-Research": 0.25, "Lab-Research": 0.15}
            },
            {
                "option_id": 339,
                "option_text": "Hospitality hours including weekends",
                "trait_tags": {"Hospitality-Svc": 1.0, "People-Skill": 0.45, "Tourism-Travel": 0.4, "Enterprising": 0.35, "Culinary-Arts": 0.3, "Marketing-Sales": 0.2}
            },
            {
                "option_id": 340,
                "option_text": "Project-based with varying schedules",
                "trait_tags": {"Civil-Build": 1.0, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Mechanical-Design": 0.2, "Industrial-Ops": 0.15}
            }
        ]
    },
    {
        "question_id": 35,
        "question_text": "What salary priority do you have?",
        "category": "Career Values",
        "options": [
            {
                "option_id": 341,
                "option_text": "High salary is most important",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 342,
                "option_text": "High salary working abroad",
                "trait_tags": {"Maritime-Sea": 1.0, "Realistic": 0.45, "Physical-Skill": 0.4, "Technical-Skill": 0.25, "Mechanical-Design": 0.15}
            },
            {
                "option_id": 343,
                "option_text": "Stable salary with government benefits",
                "trait_tags": {"Community-Serve": 1.0, "Social": 0.45, "People-Skill": 0.4, "Teaching-Ed": 0.25, "Patient-Care": 0.2, "Law-Enforce": 0.15}
            },
            {
                "option_id": 344,
                "option_text": "Job satisfaction matters more than salary",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 345,
                "option_text": "Growth potential more than starting salary",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 346,
                "option_text": "Entrepreneurship - unlimited potential",
                "trait_tags": {"Startup-Venture": 1.0, "Enterprising": 0.45, "People-Skill": 0.3, "Marketing-Sales": 0.3, "Finance-Acct": 0.2, "Creative-Skill": 0.2}
            },
            {
                "option_id": 347,
                "option_text": "Balanced salary and work-life",
                "trait_tags": {"Admin-Skill": 1.0, "Conventional": 0.45, "Finance-Acct": 0.3, "Hospitality-Svc": 0.2}
            },
            {
                "option_id": 348,
                "option_text": "Tips and commissions on top of base pay",
                "trait_tags": {"Hospitality-Svc": 1.0, "People-Skill": 0.45, "Tourism-Travel": 0.4, "Enterprising": 0.35, "Culinary-Arts": 0.3, "Marketing-Sales": 0.2}
            },
            {
                "option_id": 349,
                "option_text": "Hazard pay for risky work",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 350,
                "option_text": "Project-based high fees as a freelancer",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            }
        ]
    },
    {
        "question_id": 36,
        "question_text": "Which board exam would you be willing to take?",
        "category": "Professional Licensure",
        "options": [
            {
                "option_id": 351,
                "option_text": "Nursing Licensure Exam (NLE)",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 352,
                "option_text": "CPA Board Exam (Accountancy)",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 353,
                "option_text": "Engineering Board Exam (Civil/ME/EE)",
                "trait_tags": {"Civil-Build": 1.0, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Mechanical-Design": 0.2, "Industrial-Ops": 0.15}
            },
            {
                "option_id": 354,
                "option_text": "Criminology Board Exam",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 355,
                "option_text": "Medical Technologist Board Exam",
                "trait_tags": {"Medical-Lab": 1.0, "Analytical-Skill": 0.45, "Investigative": 0.4, "Lab-Research": 0.35, "Technical-Skill": 0.25, "Patient-Care": 0.2}
            },
            {
                "option_id": 356,
                "option_text": "Licensure Exam for Teachers (LET)",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 357,
                "option_text": "Pharmacy Board Exam",
                "trait_tags": {"Medical-Lab": 1.0, "Analytical-Skill": 0.45, "Investigative": 0.4, "Lab-Research": 0.35, "Technical-Skill": 0.25, "Patient-Care": 0.2}
            },
            {
                "option_id": 358,
                "option_text": "Physical/Occupational Therapy Board",
                "trait_tags": {"Rehab-Therapy": 1.0, "Physical-Skill": 0.4, "Social": 0.35, "People-Skill": 0.35, "Patient-Care": 0.3, "Teaching-Ed": 0.2}
            },
            {
                "option_id": 359,
                "option_text": "Architecture Board Exam",
                "trait_tags": {"Spatial-Design": 1.0, "Artistic": 0.35, "Creative-Skill": 0.35, "Civil-Build": 0.25, "Visual-Design": 0.25, "Technical-Skill": 0.2}
            },
            {
                "option_id": 360,
                "option_text": "I prefer careers without board exams",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            }
        ]
    },
    {
        "question_id": 37,
        "question_text": "Which activity would you choose on a free Saturday?",
        "category": "Interest Type",
        "options": [
            {
                "option_id": 361,
                "option_text": "Fixing or building something",
                "trait_tags": {"Technical-Skill": 1.0, "Software-Dev": 0.4, "Hardware-Systems": 0.4, "Realistic": 0.35, "Mechanical-Design": 0.35, "Investigative": 0.25}
            },
            {
                "option_id": 362,
                "option_text": "Reading about science or doing experiments",
                "trait_tags": {"Lab-Research": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Medical-Lab": 0.3, "Field-Research": 0.25, "Data-Analytics": 0.25}
            },
            {
                "option_id": 363,
                "option_text": "Creating art, music, or writing",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            },
            {
                "option_id": 364,
                "option_text": "Volunteering to help others",
                "trait_tags": {"Community-Serve": 1.0, "Social": 0.45, "People-Skill": 0.4, "Teaching-Ed": 0.25, "Patient-Care": 0.2, "Law-Enforce": 0.15}
            },
            {
                "option_id": 365,
                "option_text": "Working on a business idea",
                "trait_tags": {"Startup-Venture": 1.0, "Enterprising": 0.45, "People-Skill": 0.3, "Marketing-Sales": 0.3, "Finance-Acct": 0.2, "Creative-Skill": 0.2}
            },
            {
                "option_id": 366,
                "option_text": "Organizing my room or files",
                "trait_tags": {"Admin-Skill": 1.0, "Conventional": 0.45, "Finance-Acct": 0.3, "Hospitality-Svc": 0.2}
            },
            {
                "option_id": 367,
                "option_text": "Coding a personal project",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 368,
                "option_text": "Playing sports or exercising",
                "trait_tags": {"Physical-Skill": 1.0, "Realistic": 0.4, "Maritime-Sea": 0.35, "Agri-Nature": 0.35, "Law-Enforce": 0.3, "Rehab-Therapy": 0.3}
            },
            {
                "option_id": 369,
                "option_text": "Cooking or trying new recipes",
                "trait_tags": {"Hospitality-Svc": 1.0, "People-Skill": 0.45, "Tourism-Travel": 0.4, "Enterprising": 0.35, "Culinary-Arts": 0.3, "Marketing-Sales": 0.2}
            },
            {
                "option_id": 370,
                "option_text": "Watching true crime or mystery shows",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            }
        ]
    },
    {
        "question_id": 38,
        "question_text": "In a zombie apocalypse, what role would you take?",
        "category": "Fun - Role",
        "options": [
            {
                "option_id": 371,
                "option_text": "The medic - healing and caring for survivors",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 372,
                "option_text": "The scientist - finding a cure",
                "trait_tags": {"Lab-Research": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Medical-Lab": 0.3, "Field-Research": 0.25, "Data-Analytics": 0.25}
            },
            {
                "option_id": 373,
                "option_text": "The engineer - building fortifications",
                "trait_tags": {"Civil-Build": 1.0, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Mechanical-Design": 0.2, "Industrial-Ops": 0.15}
            },
            {
                "option_id": 374,
                "option_text": "The leader - organizing the group",
                "trait_tags": {"Startup-Venture": 1.0, "Enterprising": 0.45, "People-Skill": 0.3, "Marketing-Sales": 0.3, "Finance-Acct": 0.2, "Creative-Skill": 0.2}
            },
            {
                "option_id": 375,
                "option_text": "The strategist - planning survival",
                "trait_tags": {"Data-Analytics": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Software-Dev": 0.3, "Lab-Research": 0.25, "Finance-Acct": 0.2}
            },
            {
                "option_id": 376,
                "option_text": "The fighter - protecting everyone",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 377,
                "option_text": "The tech expert - communications and hacking",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 378,
                "option_text": "The scout - exploring and gathering intel",
                "trait_tags": {"Field-Research": 1.0, "Investigative": 0.4, "Agri-Nature": 0.3, "Analytical-Skill": 0.3, "Physical-Skill": 0.25, "Lab-Research": 0.25}
            },
            {
                "option_id": 379,
                "option_text": "The farmer - growing food supplies",
                "trait_tags": {"Agri-Nature": 1.0, "Realistic": 0.45, "Physical-Skill": 0.35, "Field-Research": 0.25, "Lab-Research": 0.15}
            },
            {
                "option_id": 380,
                "option_text": "The cook - keeping everyone fed and happy",
                "trait_tags": {"Hospitality-Svc": 1.0, "People-Skill": 0.45, "Tourism-Travel": 0.4, "Enterprising": 0.35, "Culinary-Arts": 0.3, "Marketing-Sales": 0.2}
            }
        ]
    },
    {
        "question_id": 39,
        "question_text": "Which superpower would be most useful for your ideal career?",
        "category": "Fun - Superpower",
        "options": [
            {
                "option_id": 381,
                "option_text": "Healing touch - save patients instantly",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 382,
                "option_text": "Super intelligence - solve any problem",
                "trait_tags": {"Data-Analytics": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Software-Dev": 0.3, "Lab-Research": 0.25, "Finance-Acct": 0.2}
            },
            {
                "option_id": 383,
                "option_text": "Mind reading - understand everyone perfectly",
                "trait_tags": {"People-Skill": 1.0, "Social": 0.45, "Patient-Care": 0.4, "Teaching-Ed": 0.4, "Hospitality-Svc": 0.4, "Enterprising": 0.3}
            },
            {
                "option_id": 384,
                "option_text": "Super strength - build anything easily",
                "trait_tags": {"Civil-Build": 1.0, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Mechanical-Design": 0.2, "Industrial-Ops": 0.15}
            },
            {
                "option_id": 385,
                "option_text": "Time manipulation - meet all deadlines",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 386,
                "option_text": "Truth detection - solve any crime",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 387,
                "option_text": "Teleportation - travel anywhere instantly",
                "trait_tags": {"Maritime-Sea": 1.0, "Realistic": 0.45, "Physical-Skill": 0.4, "Technical-Skill": 0.25, "Mechanical-Design": 0.15}
            },
            {
                "option_id": 388,
                "option_text": "Creativity burst - create amazing art",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            },
            {
                "option_id": 389,
                "option_text": "Tech control - command any computer",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 390,
                "option_text": "Plant growth - perfect farming",
                "trait_tags": {"Agri-Nature": 1.0, "Realistic": 0.45, "Physical-Skill": 0.35, "Field-Research": 0.25, "Lab-Research": 0.15}
            }
        ]
    },
    {
        "question_id": 40,
        "question_text": "What would your ideal Monday morning look like?",
        "category": "Work Lifestyle",
        "options": [
            {
                "option_id": 391,
                "option_text": "Arriving at the hospital for patient rounds",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 392,
                "option_text": "Setting up experiments in a lab",
                "trait_tags": {"Lab-Research": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Medical-Lab": 0.3, "Field-Research": 0.25, "Data-Analytics": 0.25}
            },
            {
                "option_id": 393,
                "option_text": "Opening my laptop to code at a tech company",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 394,
                "option_text": "Reviewing blueprints at a construction site",
                "trait_tags": {"Civil-Build": 1.0, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Mechanical-Design": 0.2, "Industrial-Ops": 0.15}
            },
            {
                "option_id": 395,
                "option_text": "Preparing financial reports at my desk",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 396,
                "option_text": "Greeting students at a classroom",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 397,
                "option_text": "Starting my shift at the police station",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 398,
                "option_text": "Working on designs at my creative studio",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            },
            {
                "option_id": 399,
                "option_text": "Checking systems aboard a ship at sea",
                "trait_tags": {"Maritime-Sea": 1.0, "Realistic": 0.45, "Physical-Skill": 0.4, "Technical-Skill": 0.25, "Mechanical-Design": 0.15}
            },
            {
                "option_id": 400,
                "option_text": "Walking through my farm checking crops",
                "trait_tags": {"Agri-Nature": 1.0, "Realistic": 0.45, "Physical-Skill": 0.35, "Field-Research": 0.25, "Lab-Research": 0.15}
            }
        ]
    },
    {
        "question_id": 41,
        "question_text": "SCENARIO: Your barangay needs help. Which role would you volunteer for?",
        "category": "Community Scenario",
        "options": [
            {
                "option_id": 401,
                "option_text": "Medical mission - taking blood pressure, first aid",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 402,
                "option_text": "Free tutoring for students",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 403,
                "option_text": "Setting up computer systems for the barangay hall",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 404,
                "option_text": "Organizing feeding programs and events",
                "trait_tags": {"Hospitality-Svc": 1.0, "People-Skill": 0.45, "Tourism-Travel": 0.4, "Enterprising": 0.35, "Culinary-Arts": 0.3, "Marketing-Sales": 0.2}
            },
            {
                "option_id": 405,
                "option_text": "Helping with infrastructure repairs",
                "trait_tags": {"Civil-Build": 1.0, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Mechanical-Design": 0.2, "Industrial-Ops": 0.15}
            },
            {
                "option_id": 406,
                "option_text": "Assisting in crime prevention programs",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 407,
                "option_text": "Creating posters and promotional materials",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            },
            {
                "option_id": 408,
                "option_text": "Managing donations and financial records",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 409,
                "option_text": "Environmental cleanup and tree planting",
                "trait_tags": {"Agri-Nature": 1.0, "Realistic": 0.45, "Physical-Skill": 0.35, "Field-Research": 0.25, "Lab-Research": 0.15}
            },
            {
                "option_id": 410,
                "option_text": "Counseling families in need",
                "trait_tags": {"Community-Serve": 1.0, "Social": 0.45, "People-Skill": 0.4, "Teaching-Ed": 0.25, "Patient-Care": 0.2, "Law-Enforce": 0.15}
            }
        ]
    },
    {
        "question_id": 42,
        "question_text": "SCENARIO: You're stranded on an island with your classmates. What's your role?",
        "category": "Survival Scenario",
        "options": [
            {
                "option_id": 411,
                "option_text": "The medic - treating injuries and illnesses",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 412,
                "option_text": "The engineer - building shelter and tools",
                "trait_tags": {"Civil-Build": 1.0, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Mechanical-Design": 0.2, "Industrial-Ops": 0.15}
            },
            {
                "option_id": 413,
                "option_text": "The leader - organizing the group and making decisions",
                "trait_tags": {"Startup-Venture": 1.0, "Enterprising": 0.45, "People-Skill": 0.3, "Marketing-Sales": 0.3, "Finance-Acct": 0.2, "Creative-Skill": 0.2}
            },
            {
                "option_id": 414,
                "option_text": "The hunter/gatherer - finding food",
                "trait_tags": {"Agri-Nature": 1.0, "Realistic": 0.45, "Physical-Skill": 0.35, "Field-Research": 0.25, "Lab-Research": 0.15}
            },
            {
                "option_id": 415,
                "option_text": "The navigator - figuring out how to get rescued",
                "trait_tags": {"Maritime-Sea": 1.0, "Realistic": 0.45, "Physical-Skill": 0.4, "Technical-Skill": 0.25, "Mechanical-Design": 0.15}
            },
            {
                "option_id": 416,
                "option_text": "The peacekeeper - resolving conflicts",
                "trait_tags": {"Community-Serve": 1.0, "Social": 0.45, "People-Skill": 0.4, "Teaching-Ed": 0.25, "Patient-Care": 0.2, "Law-Enforce": 0.15}
            },
            {
                "option_id": 417,
                "option_text": "The strategist - planning long-term survival",
                "trait_tags": {"Data-Analytics": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Software-Dev": 0.3, "Lab-Research": 0.25, "Finance-Acct": 0.2}
            },
            {
                "option_id": 418,
                "option_text": "The teacher - training others in survival skills",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 419,
                "option_text": "The communicator - boosting morale and keeping spirits up",
                "trait_tags": {"People-Skill": 1.0, "Social": 0.45, "Patient-Care": 0.4, "Teaching-Ed": 0.4, "Hospitality-Svc": 0.4, "Enterprising": 0.3}
            },
            {
                "option_id": 420,
                "option_text": "The inventor - creating solutions from limited resources",
                "trait_tags": {"Technical-Skill": 1.0, "Software-Dev": 0.4, "Hardware-Systems": 0.4, "Realistic": 0.35, "Mechanical-Design": 0.35, "Investigative": 0.25}
            }
        ]
    },
    {
        "question_id": 43,
        "question_text": "SCENARIO: A typhoon hit your town. How would you help?",
        "category": "Disaster Response",
        "options": [
            {
                "option_id": 421,
                "option_text": "Medical response - treating injured victims",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 422,
                "option_text": "Search and rescue operations",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 423,
                "option_text": "Distributing relief goods fairly",
                "trait_tags": {"Admin-Skill": 1.0, "Conventional": 0.45, "Finance-Acct": 0.3, "Hospitality-Svc": 0.2}
            },
            {
                "option_id": 424,
                "option_text": "Repairing damaged electrical lines",
                "trait_tags": {"Electrical-Power": 1.0, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3, "Mechanical-Design": 0.2, "Industrial-Ops": 0.2}
            },
            {
                "option_id": 425,
                "option_text": "Clearing roads and debris",
                "trait_tags": {"Civil-Build": 1.0, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Mechanical-Design": 0.2, "Industrial-Ops": 0.15}
            },
            {
                "option_id": 426,
                "option_text": "Setting up communication systems",
                "trait_tags": {"Hardware-Systems": 1.0, "Technical-Skill": 0.45, "Realistic": 0.4, "Electrical-Power": 0.3, "Mechanical-Design": 0.25, "Software-Dev": 0.2}
            },
            {
                "option_id": 427,
                "option_text": "Cooking and preparing food for evacuees",
                "trait_tags": {"Hospitality-Svc": 1.0, "People-Skill": 0.45, "Tourism-Travel": 0.4, "Enterprising": 0.35, "Culinary-Arts": 0.3, "Marketing-Sales": 0.2}
            },
            {
                "option_id": 428,
                "option_text": "Counseling traumatized victims",
                "trait_tags": {"People-Skill": 1.0, "Social": 0.45, "Patient-Care": 0.4, "Teaching-Ed": 0.4, "Hospitality-Svc": 0.4, "Enterprising": 0.3}
            },
            {
                "option_id": 429,
                "option_text": "Documenting damage for insurance/aid",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 430,
                "option_text": "Coordinating volunteer efforts",
                "trait_tags": {"Community-Serve": 1.0, "Social": 0.45, "People-Skill": 0.4, "Teaching-Ed": 0.25, "Patient-Care": 0.2, "Law-Enforce": 0.15}
            }
        ]
    },
    {
        "question_id": 44,
        "question_text": "SCENARIO: Your school is planning a foundation day. What committee would you join?",
        "category": "Event Planning",
        "options": [
            {
                "option_id": 431,
                "option_text": "First aid and medical committee",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 432,
                "option_text": "Stage design and decorations",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            },
            {
                "option_id": 433,
                "option_text": "Sound and lights technical team",
                "trait_tags": {"Hardware-Systems": 1.0, "Technical-Skill": 0.45, "Realistic": 0.4, "Electrical-Power": 0.3, "Mechanical-Design": 0.25, "Software-Dev": 0.2}
            },
            {
                "option_id": 434,
                "option_text": "Budget and finance committee",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 435,
                "option_text": "Food and catering committee",
                "trait_tags": {"Hospitality-Svc": 1.0, "People-Skill": 0.45, "Tourism-Travel": 0.4, "Enterprising": 0.35, "Culinary-Arts": 0.3, "Marketing-Sales": 0.2}
            },
            {
                "option_id": 436,
                "option_text": "Security and crowd control",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 437,
                "option_text": "Program and hosting",
                "trait_tags": {"Creative-Skill": 1.0, "Artistic": 0.45, "Visual-Design": 0.4, "Digital-Media": 0.4, "Spatial-Design": 0.35}
            },
            {
                "option_id": 438,
                "option_text": "Documentation and photography",
                "trait_tags": {"Digital-Media": 1.0, "Artistic": 0.4, "Creative-Skill": 0.4, "Visual-Design": 0.3, "Software-Dev": 0.2, "Technical-Skill": 0.2}
            },
            {
                "option_id": 439,
                "option_text": "Logistics and venue setup",
                "trait_tags": {"Industrial-Ops": 1.0, "Analytical-Skill": 0.35, "Enterprising": 0.3, "Mechanical-Design": 0.25, "Admin-Skill": 0.2, "Finance-Acct": 0.15}
            },
            {
                "option_id": 440,
                "option_text": "Registration and guest relations",
                "trait_tags": {"Admin-Skill": 1.0, "Conventional": 0.45, "Finance-Acct": 0.3, "Hospitality-Svc": 0.2}
            }
        ]
    },
    {
        "question_id": 45,
        "question_text": "SCENARIO: Your friend is crying about a failed exam. What do you do?",
        "category": "Emotional Intelligence",
        "options": [
            {
                "option_id": 441,
                "option_text": "Listen and comfort them emotionally",
                "trait_tags": {"People-Skill": 1.0, "Social": 0.45, "Patient-Care": 0.4, "Teaching-Ed": 0.4, "Hospitality-Svc": 0.4, "Enterprising": 0.3}
            },
            {
                "option_id": 442,
                "option_text": "Offer to tutor them for the next exam",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 443,
                "option_text": "Help them analyze what went wrong",
                "trait_tags": {"Data-Analytics": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Software-Dev": 0.3, "Lab-Research": 0.25, "Finance-Acct": 0.2}
            },
            {
                "option_id": 444,
                "option_text": "Buy them food to cheer them up",
                "trait_tags": {"Hospitality-Svc": 1.0, "People-Skill": 0.45, "Tourism-Travel": 0.4, "Enterprising": 0.35, "Culinary-Arts": 0.3, "Marketing-Sales": 0.2}
            },
            {
                "option_id": 445,
                "option_text": "Create a study schedule/plan for them",
                "trait_tags": {"Admin-Skill": 1.0, "Conventional": 0.45, "Finance-Acct": 0.3, "Hospitality-Svc": 0.2}
            },
            {
                "option_id": 446,
                "option_text": "Distract them with fun activities",
                "trait_tags": {"Creative-Skill": 1.0, "Artistic": 0.45, "Visual-Design": 0.4, "Digital-Media": 0.4, "Spatial-Design": 0.35}
            },
            {
                "option_id": 447,
                "option_text": "Share your own failure stories to relate",
                "trait_tags": {"Community-Serve": 1.0, "Social": 0.45, "People-Skill": 0.4, "Teaching-Ed": 0.25, "Patient-Care": 0.2, "Law-Enforce": 0.15}
            },
            {
                "option_id": 448,
                "option_text": "Encourage them to talk to the teacher",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 449,
                "option_text": "Help them find online resources",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 450,
                "option_text": "Give practical tips for better memorization",
                "trait_tags": {"Medical-Lab": 1.0, "Analytical-Skill": 0.45, "Investigative": 0.4, "Lab-Research": 0.35, "Technical-Skill": 0.25, "Patient-Care": 0.2}
            }
        ]
    },
    {
        "question_id": 51,
        "question_text": "Which Philippine industry would you like to work in?",
        "category": "PH Industry",
        "options": [
            {
                "option_id": 501,
                "option_text": "BPO/Call center industry",
                "trait_tags": {"People-Skill": 1.0, "Social": 0.45, "Patient-Care": 0.4, "Teaching-Ed": 0.4, "Hospitality-Svc": 0.4, "Enterprising": 0.3}
            },
            {
                "option_id": 502,
                "option_text": "OFW - work abroad (healthcare)",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 503,
                "option_text": "OFW - work abroad (maritime/seaman)",
                "trait_tags": {"Maritime-Sea": 1.0, "Realistic": 0.45, "Physical-Skill": 0.4, "Technical-Skill": 0.25, "Mechanical-Design": 0.15}
            },
            {
                "option_id": 504,
                "option_text": "OFW - work abroad (engineering)",
                "trait_tags": {"Civil-Build": 1.0, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Mechanical-Design": 0.2, "Industrial-Ops": 0.15}
            },
            {
                "option_id": 505,
                "option_text": "Government service (LGU, national agencies)",
                "trait_tags": {"Community-Serve": 1.0, "Social": 0.45, "People-Skill": 0.4, "Teaching-Ed": 0.25, "Patient-Care": 0.2, "Law-Enforce": 0.15}
            },
            {
                "option_id": 506,
                "option_text": "Banking and finance sector",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 507,
                "option_text": "Tech startup/IT industry",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 508,
                "option_text": "Tourism and hospitality",
                "trait_tags": {"Hospitality-Svc": 1.0, "People-Skill": 0.45, "Tourism-Travel": 0.4, "Enterprising": 0.35, "Culinary-Arts": 0.3, "Marketing-Sales": 0.2}
            },
            {
                "option_id": 509,
                "option_text": "Manufacturing/factory industry",
                "trait_tags": {"Industrial-Ops": 1.0, "Analytical-Skill": 0.35, "Enterprising": 0.3, "Mechanical-Design": 0.25, "Admin-Skill": 0.2, "Finance-Acct": 0.15}
            },
            {
                "option_id": 510,
                "option_text": "Agriculture and farming",
                "trait_tags": {"Agri-Nature": 1.0, "Realistic": 0.45, "Physical-Skill": 0.35, "Field-Research": 0.25, "Lab-Research": 0.15}
            }
        ]
    },
    {
        "question_id": 52,
        "question_text": "Which board exam would you be most willing to study hard for?",
        "category": "Board Exam Preference",
        "options": [
            {
                "option_id": 511,
                "option_text": "Nursing Licensure Exam (NLE)",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 512,
                "option_text": "CPA Board Exam",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 513,
                "option_text": "Civil Engineering Board Exam",
                "trait_tags": {"Civil-Build": 1.0, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Mechanical-Design": 0.2, "Industrial-Ops": 0.15}
            },
            {
                "option_id": 514,
                "option_text": "Electrical Engineering Board Exam",
                "trait_tags": {"Electrical-Power": 1.0, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3, "Mechanical-Design": 0.2, "Industrial-Ops": 0.2}
            },
            {
                "option_id": 515,
                "option_text": "Mechanical Engineering Board Exam",
                "trait_tags": {"Mechanical-Design": 1.0, "Realistic": 0.45, "Technical-Skill": 0.4, "Industrial-Ops": 0.25, "Civil-Build": 0.2, "Electrical-Power": 0.2}
            },
            {
                "option_id": 516,
                "option_text": "Criminology Board Exam",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 517,
                "option_text": "Licensure Exam for Teachers (LET)",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 518,
                "option_text": "Medical Technologist Board Exam",
                "trait_tags": {"Medical-Lab": 1.0, "Analytical-Skill": 0.45, "Investigative": 0.4, "Lab-Research": 0.35, "Technical-Skill": 0.25, "Patient-Care": 0.2}
            },
            {
                "option_id": 519,
                "option_text": "Pharmacy Board Exam",
                "trait_tags": {"Medical-Lab": 1.0, "Analytical-Skill": 0.45, "Investigative": 0.4, "Lab-Research": 0.35, "Technical-Skill": 0.25, "Patient-Care": 0.2}
            },
            {
                "option_id": 520,
                "option_text": "I prefer careers without board exams",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            }
        ]
    },
    {
        "question_id": 53,
        "question_text": "Where in the Philippines would you prefer to work?",
        "category": "Work Location",
        "options": [
            {
                "option_id": 521,
                "option_text": "Metro Manila - BGC, Makati, Ortigas",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 522,
                "option_text": "Clark/Subic - growing industrial zone",
                "trait_tags": {"Industrial-Ops": 1.0, "Analytical-Skill": 0.35, "Enterprising": 0.3, "Mechanical-Design": 0.25, "Admin-Skill": 0.2, "Finance-Acct": 0.15}
            },
            {
                "option_id": 523,
                "option_text": "Cebu - IT and BPO hub",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 524,
                "option_text": "Davao - agribusiness center",
                "trait_tags": {"Agri-Nature": 1.0, "Realistic": 0.45, "Physical-Skill": 0.35, "Field-Research": 0.25, "Lab-Research": 0.15}
            },
            {
                "option_id": 525,
                "option_text": "Baguio - education and tourism",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 526,
                "option_text": "Boracay/Palawan - tourism hotspots",
                "trait_tags": {"Hospitality-Svc": 1.0, "People-Skill": 0.45, "Tourism-Travel": 0.4, "Enterprising": 0.35, "Culinary-Arts": 0.3, "Marketing-Sales": 0.2}
            },
            {
                "option_id": 527,
                "option_text": "My home province",
                "trait_tags": {"Community-Serve": 1.0, "Social": 0.45, "People-Skill": 0.4, "Teaching-Ed": 0.25, "Patient-Care": 0.2, "Law-Enforce": 0.15}
            },
            {
                "option_id": 528,
                "option_text": "Anywhere with good hospitals",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 529,
                "option_text": "Near ports - Batangas, Subic",
                "trait_tags": {"Maritime-Sea": 1.0, "Realistic": 0.45, "Physical-Skill": 0.4, "Technical-Skill": 0.25, "Mechanical-Design": 0.15}
            },
            {
                "option_id": 530,
                "option_text": "Abroad - international career",
                "trait_tags": {"Marketing-Sales": 1.0, "Enterprising": 0.45, "People-Skill": 0.4, "Startup-Venture": 0.3, "Hospitality-Svc": 0.2, "Finance-Acct": 0.15}
            }
        ]
    },
    {
        "question_id": 54,
        "question_text": "Which Filipino company/organization would you want to work for?",
        "category": "Dream Employer",
        "options": [
            {
                "option_id": 531,
                "option_text": "SM, Ayala, or San Miguel Corporation",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 532,
                "option_text": "PLDT, Globe, or Smart",
                "trait_tags": {"Hardware-Systems": 1.0, "Technical-Skill": 0.45, "Realistic": 0.4, "Electrical-Power": 0.3, "Mechanical-Design": 0.25, "Software-Dev": 0.2}
            },
            {
                "option_id": 533,
                "option_text": "Jollibee, Max's, or Goldilocks",
                "trait_tags": {"Hospitality-Svc": 1.0, "People-Skill": 0.45, "Tourism-Travel": 0.4, "Enterprising": 0.35, "Culinary-Arts": 0.3, "Marketing-Sales": 0.2}
            },
            {
                "option_id": 534,
                "option_text": "St. Luke's, Makati Med, or Philippine Heart Center",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 535,
                "option_text": "DMCI, Megawide, or Ayala Land",
                "trait_tags": {"Civil-Build": 1.0, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Mechanical-Design": 0.2, "Industrial-Ops": 0.15}
            },
            {
                "option_id": 536,
                "option_text": "Accenture, IBM Philippines, or tech startups",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 537,
                "option_text": "PNP, AFP, or NBI",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 538,
                "option_text": "DepEd, CHED, or universities",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 539,
                "option_text": "DOH, PhilHealth, or health agencies",
                "trait_tags": {"Community-Serve": 1.0, "Social": 0.45, "People-Skill": 0.4, "Teaching-Ed": 0.25, "Patient-Care": 0.2, "Law-Enforce": 0.15}
            },
            {
                "option_id": 540,
                "option_text": "Start my own business",
                "trait_tags": {"Startup-Venture": 1.0, "Enterprising": 0.45, "People-Skill": 0.3, "Marketing-Sales": 0.3, "Finance-Acct": 0.2, "Creative-Skill": 0.2}
            }
        ]
    },
    {
        "question_id": 55,
        "question_text": "Rate your ENGLISH proficiency:",
        "category": "Language Skill",
        "options": [
            {
                "option_id": 541,
                "option_text": "Excellent - can debate, write essays fluently",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 542,
                "option_text": "Very Good - comfortable in English conversations",
                "trait_tags": {"Marketing-Sales": 1.0, "Enterprising": 0.45, "People-Skill": 0.4, "Startup-Venture": 0.3, "Hospitality-Svc": 0.2, "Finance-Acct": 0.15}
            },
            {
                "option_id": 543,
                "option_text": "Good - can communicate clearly",
                "trait_tags": {"People-Skill": 1.0, "Social": 0.45, "Patient-Care": 0.4, "Teaching-Ed": 0.4, "Hospitality-Svc": 0.4, "Enterprising": 0.3}
            },
            {
                "option_id": 544,
                "option_text": "Average - understand but struggle speaking",
                "trait_tags": {"Technical-Skill": 1.0, "Software-Dev": 0.4, "Hardware-Systems": 0.4, "Realistic": 0.35, "Mechanical-Design": 0.35, "Investigative": 0.25}
            },
            {
                "option_id": 545,
                "option_text": "Below Average - prefer Filipino",
                "trait_tags": {"Agri-Nature": 1.0, "Realistic": 0.45, "Physical-Skill": 0.35, "Field-Research": 0.25, "Lab-Research": 0.15}
            },
            {
                "option_id": 546,
                "option_text": "I'm better at technical English (IT/Science)",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 547,
                "option_text": "I'm better at medical/scientific terms",
                "trait_tags": {"Medical-Lab": 1.0, "Analytical-Skill": 0.45, "Investigative": 0.4, "Lab-Research": 0.35, "Technical-Skill": 0.25, "Patient-Care": 0.2}
            },
            {
                "option_id": 548,
                "option_text": "I'm better at business English",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 549,
                "option_text": "I'm better at legal/formal English",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 550,
                "option_text": "I'm better at creative writing",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            }
        ]
    },
    {
        "question_id": 56,
        "question_text": "What technology activity are you most comfortable with?",
        "category": "Tech Skill",
        "options": [
            {
                "option_id": 551,
                "option_text": "Coding or building programs and websites",
                "trait_tags": {"Software-Dev": 1.0, "Web-Dev": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25}
            },
            {
                "option_id": 552,
                "option_text": "Gaming - I know my way around PC specs, mods, and setups",
                "trait_tags": {"Game-Dev": 1.0, "Hardware-Systems": 0.8, "Technical-Skill": 0.4, "Software-Dev": 0.4, "Creative-Skill": 0.35, "Animation-3D": 0.35}
            },
            {
                "option_id": 553,
                "option_text": "Working with spreadsheets and organizing data",
                "trait_tags": {"Data-Analytics": 1.0, "Finance-Acct": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Conventional": 0.36, "Software-Dev": 0.3}
            },
            {
                "option_id": 554,
                "option_text": "Editing photos, videos, or creating digital content",
                "trait_tags": {"Digital-Media": 1.0, "Visual-Design": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Software-Dev": 0.2, "Technical-Skill": 0.2}
            },
            {
                "option_id": 555,
                "option_text": "Troubleshooting hardware or setting up networks",
                "trait_tags": {"Hardware-Systems": 1.0, "Cloud-Systems": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Electrical-Power": 0.3, "Software-Dev": 0.28}
            },
            {
                "option_id": 556,
                "option_text": "Browsing social media and online communication",
                "trait_tags": {"Marketing-Sales": 1.0, "People-Skill": 0.8, "Enterprising": 0.45, "Social": 0.36, "Hospitality-Svc": 0.32, "Teaching-Ed": 0.32}
            },
            {
                "option_id": 557,
                "option_text": "Using apps for design - Canva, Photoshop, Figma",
                "trait_tags": {"Visual-Design": 1.0, "Animation-3D": 0.8, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.32, "Game-Dev": 0.28}
            },
            {
                "option_id": 558,
                "option_text": "Exploring AI tools, chatbots, or automation",
                "trait_tags": {"AI-ML": 1.0, "Software-Dev": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Data-Analytics": 0.4, "Technical-Skill": 0.36}
            },
            {
                "option_id": 559,
                "option_text": "Managing files, records, or hospital/office systems",
                "trait_tags": {"Admin-Skill": 1.0, "Health-Admin": 0.8, "Conventional": 0.45, "Finance-Acct": 0.3, "Hospitality-Svc": 0.2}
            },
            {
                "option_id": 560,
                "option_text": "I mostly use my phone/computer for basic tasks only",
                "trait_tags": {"Agri-Nature": 1.0, "Physical-Skill": 0.8, "Realistic": 0.45, "Field-Research": 0.25, "Law-Enforce": 0.24, "Lab-Research": 0.15}
            }
        ]
    },
    {
        "question_id": 57,
        "question_text": "Rate your LEADERSHIP ability:",
        "category": "Leadership Skill",
        "options": [
            {
                "option_id": 561,
                "option_text": "Natural leader - always take charge",
                "trait_tags": {"Startup-Venture": 1.0, "Enterprising": 0.45, "People-Skill": 0.3, "Marketing-Sales": 0.3, "Finance-Acct": 0.2, "Creative-Skill": 0.2}
            },
            {
                "option_id": 562,
                "option_text": "Good leader when needed",
                "trait_tags": {"Admin-Skill": 1.0, "Conventional": 0.45, "Finance-Acct": 0.3, "Hospitality-Svc": 0.2}
            },
            {
                "option_id": 563,
                "option_text": "Prefer to support the leader",
                "trait_tags": {"People-Skill": 1.0, "Social": 0.45, "Patient-Care": 0.4, "Teaching-Ed": 0.4, "Hospitality-Svc": 0.4, "Enterprising": 0.3}
            },
            {
                "option_id": 564,
                "option_text": "Work best independently",
                "trait_tags": {"Lab-Research": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Medical-Lab": 0.3, "Field-Research": 0.25, "Data-Analytics": 0.25}
            },
            {
                "option_id": 565,
                "option_text": "Lead through teaching/mentoring",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 566,
                "option_text": "Lead through expertise/knowledge",
                "trait_tags": {"Medical-Lab": 1.0, "Analytical-Skill": 0.45, "Investigative": 0.4, "Lab-Research": 0.35, "Technical-Skill": 0.25, "Patient-Care": 0.2}
            },
            {
                "option_id": 567,
                "option_text": "Lead through organization/planning",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 568,
                "option_text": "Lead through inspiration/creativity",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            },
            {
                "option_id": 569,
                "option_text": "Lead through authority/discipline",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 570,
                "option_text": "Lead through service/example",
                "trait_tags": {"Community-Serve": 1.0, "Social": 0.45, "People-Skill": 0.4, "Teaching-Ed": 0.25, "Patient-Care": 0.2, "Law-Enforce": 0.15}
            }
        ]
    },
    {
        "question_id": 58,
        "question_text": "How do you handle PRESSURE and DEADLINES?",
        "category": "Stress Management",
        "options": [
            {
                "option_id": 571,
                "option_text": "Thrive under pressure - work better with urgency",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 572,
                "option_text": "Handle it well - stay calm and focused",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 573,
                "option_text": "Manageable - can deal with reasonable deadlines",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 574,
                "option_text": "Prefer steady pace - avoid high-pressure situations",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 575,
                "option_text": "Struggle with pressure - need calm environments",
                "trait_tags": {"Lab-Research": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Medical-Lab": 0.3, "Field-Research": 0.25, "Data-Analytics": 0.25}
            },
            {
                "option_id": 576,
                "option_text": "Good with financial deadlines",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 577,
                "option_text": "Good with project deadlines",
                "trait_tags": {"Civil-Build": 1.0, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Mechanical-Design": 0.2, "Industrial-Ops": 0.15}
            },
            {
                "option_id": 578,
                "option_text": "Good with creative deadlines",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            },
            {
                "option_id": 579,
                "option_text": "Good with people-related pressure",
                "trait_tags": {"Hospitality-Svc": 1.0, "People-Skill": 0.45, "Tourism-Travel": 0.4, "Enterprising": 0.35, "Culinary-Arts": 0.3, "Marketing-Sales": 0.2}
            },
            {
                "option_id": 580,
                "option_text": "Work best with flexible timelines",
                "trait_tags": {"Agri-Nature": 1.0, "Realistic": 0.45, "Physical-Skill": 0.35, "Field-Research": 0.25, "Lab-Research": 0.15}
            }
        ]
    },
    {
        "question_id": 59,
        "question_text": "How would you rate your MATHEMATICAL ability?",
        "category": "Math Skill",
        "options": [
            {
                "option_id": 581,
                "option_text": "Excellent - love calculus, physics, advanced math",
                "trait_tags": {"Data-Analytics": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Software-Dev": 0.3, "Lab-Research": 0.25, "Finance-Acct": 0.2}
            },
            {
                "option_id": 582,
                "option_text": "Very Good - comfortable with algebra, statistics",
                "trait_tags": {"Civil-Build": 1.0, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Mechanical-Design": 0.2, "Industrial-Ops": 0.15}
            },
            {
                "option_id": 583,
                "option_text": "Good - can handle accounting math",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 584,
                "option_text": "Average - basic math is fine",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 585,
                "option_text": "Below Average - struggle with math",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            },
            {
                "option_id": 586,
                "option_text": "Good at programming math/logic",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 587,
                "option_text": "Good at medical calculations (dosages)",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 588,
                "option_text": "Good at engineering calculations",
                "trait_tags": {"Mechanical-Design": 1.0, "Realistic": 0.45, "Technical-Skill": 0.4, "Industrial-Ops": 0.25, "Civil-Build": 0.2, "Electrical-Power": 0.2}
            },
            {
                "option_id": 589,
                "option_text": "Good at measurement/spatial math",
                "trait_tags": {"Spatial-Design": 1.0, "Artistic": 0.35, "Creative-Skill": 0.35, "Civil-Build": 0.25, "Visual-Design": 0.25, "Technical-Skill": 0.2}
            },
            {
                "option_id": 590,
                "option_text": "Math isn't my strength",
                "trait_tags": {"Creative-Skill": 1.0, "Artistic": 0.45, "Visual-Design": 0.4, "Digital-Media": 0.4, "Spatial-Design": 0.35}
            }
        ]
    },
    {
        "question_id": 60,
        "question_text": "How would you rate your SCIENCE ability?",
        "category": "Science Skill",
        "options": [
            {
                "option_id": 591,
                "option_text": "Excellent - love biology, chemistry, physics",
                "trait_tags": {"Lab-Research": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Medical-Lab": 0.3, "Field-Research": 0.25, "Data-Analytics": 0.25}
            },
            {
                "option_id": 592,
                "option_text": "Very Good - enjoy science experiments",
                "trait_tags": {"Medical-Lab": 1.0, "Analytical-Skill": 0.45, "Investigative": 0.4, "Lab-Research": 0.35, "Technical-Skill": 0.25, "Patient-Care": 0.2}
            },
            {
                "option_id": 593,
                "option_text": "Good at biology/life sciences",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 594,
                "option_text": "Good at chemistry",
                "trait_tags": {"Medical-Lab": 1.0, "Analytical-Skill": 0.45, "Investigative": 0.4, "Lab-Research": 0.35, "Technical-Skill": 0.25, "Patient-Care": 0.2}
            },
            {
                "option_id": 595,
                "option_text": "Good at physics/engineering science",
                "trait_tags": {"Electrical-Power": 1.0, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3, "Mechanical-Design": 0.2, "Industrial-Ops": 0.2}
            },
            {
                "option_id": 596,
                "option_text": "Good at earth/environmental science",
                "trait_tags": {"Agri-Nature": 1.0, "Realistic": 0.45, "Physical-Skill": 0.35, "Field-Research": 0.25, "Lab-Research": 0.15}
            },
            {
                "option_id": 597,
                "option_text": "Good at computer science",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 598,
                "option_text": "Average - science is okay",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 599,
                "option_text": "Below Average - not my favorite",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 600,
                "option_text": "Science isn't my strength",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            }
        ]
    },
    {
        "question_id": 61,
        "question_text": "What's MOST important to you in a career?",
        "category": "Career Priority",
        "options": [
            {
                "option_id": 601,
                "option_text": "High salary and financial security",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 602,
                "option_text": "Helping others and making a difference",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 603,
                "option_text": "Job security and stability",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 604,
                "option_text": "Creativity and self-expression",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            },
            {
                "option_id": 605,
                "option_text": "Work-life balance",
                "trait_tags": {"Admin-Skill": 1.0, "Conventional": 0.45, "Finance-Acct": 0.3, "Hospitality-Svc": 0.2}
            },
            {
                "option_id": 606,
                "option_text": "Prestige and respect",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 607,
                "option_text": "Adventure and travel",
                "trait_tags": {"Maritime-Sea": 1.0, "Realistic": 0.45, "Physical-Skill": 0.4, "Technical-Skill": 0.25, "Mechanical-Design": 0.15}
            },
            {
                "option_id": 608,
                "option_text": "Independence and being my own boss",
                "trait_tags": {"Startup-Venture": 1.0, "Enterprising": 0.45, "People-Skill": 0.3, "Marketing-Sales": 0.3, "Finance-Acct": 0.2, "Creative-Skill": 0.2}
            },
            {
                "option_id": 609,
                "option_text": "Intellectual challenge",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 610,
                "option_text": "Contributing to community/nation",
                "trait_tags": {"Community-Serve": 1.0, "Social": 0.45, "People-Skill": 0.4, "Teaching-Ed": 0.25, "Patient-Care": 0.2, "Law-Enforce": 0.15}
            }
        ]
    },
    {
        "question_id": 62,
        "question_text": "How important is SALARY to you?",
        "category": "Salary Importance",
        "options": [
            {
                "option_id": 611,
                "option_text": "Very important - want high-paying career",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 612,
                "option_text": "Important - need good income for family",
                "trait_tags": {"Maritime-Sea": 1.0, "Realistic": 0.45, "Physical-Skill": 0.4, "Technical-Skill": 0.25, "Mechanical-Design": 0.15}
            },
            {
                "option_id": 613,
                "option_text": "Moderate - balance of pay and passion",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 614,
                "option_text": "Less important - passion over pay",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 615,
                "option_text": "Want to earn abroad (OFW)",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 616,
                "option_text": "Want steady government salary",
                "trait_tags": {"Community-Serve": 1.0, "Social": 0.45, "People-Skill": 0.4, "Teaching-Ed": 0.25, "Patient-Care": 0.2, "Law-Enforce": 0.15}
            },
            {
                "option_id": 617,
                "option_text": "Want entrepreneurial income",
                "trait_tags": {"Startup-Venture": 1.0, "Enterprising": 0.45, "People-Skill": 0.3, "Marketing-Sales": 0.3, "Finance-Acct": 0.2, "Creative-Skill": 0.2}
            },
            {
                "option_id": 618,
                "option_text": "Want project-based freelance income",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            },
            {
                "option_id": 619,
                "option_text": "Want commission-based income",
                "trait_tags": {"Marketing-Sales": 1.0, "Enterprising": 0.45, "People-Skill": 0.4, "Startup-Venture": 0.3, "Hospitality-Svc": 0.2, "Finance-Acct": 0.15}
            },
            {
                "option_id": 620,
                "option_text": "Money isn't my main motivation",
                "trait_tags": {"Agri-Nature": 1.0, "Realistic": 0.45, "Physical-Skill": 0.35, "Field-Research": 0.25, "Lab-Research": 0.15}
            }
        ]
    },
    {
        "question_id": 63,
        "question_text": "How do you feel about WORKING ABROAD?",
        "category": "International Work",
        "options": [
            {
                "option_id": 621,
                "option_text": "Dream of it - want to be an OFW",
                "trait_tags": {"Maritime-Sea": 1.0, "Realistic": 0.45, "Physical-Skill": 0.4, "Technical-Skill": 0.25, "Mechanical-Design": 0.15}
            },
            {
                "option_id": 622,
                "option_text": "Open to it for nursing/healthcare",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 623,
                "option_text": "Open to it for engineering/construction",
                "trait_tags": {"Civil-Build": 1.0, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Mechanical-Design": 0.2, "Industrial-Ops": 0.15}
            },
            {
                "option_id": 624,
                "option_text": "Open to it for IT/tech work",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 625,
                "option_text": "Open to it for hospitality/cruise ships",
                "trait_tags": {"Hospitality-Svc": 1.0, "People-Skill": 0.45, "Tourism-Travel": 0.4, "Enterprising": 0.35, "Culinary-Arts": 0.3, "Marketing-Sales": 0.2}
            },
            {
                "option_id": 626,
                "option_text": "Prefer to stay in Philippines",
                "trait_tags": {"Community-Serve": 1.0, "Social": 0.45, "People-Skill": 0.4, "Teaching-Ed": 0.25, "Patient-Care": 0.2, "Law-Enforce": 0.15}
            },
            {
                "option_id": 627,
                "option_text": "Want to work locally for family",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 628,
                "option_text": "Want to build business here",
                "trait_tags": {"Startup-Venture": 1.0, "Enterprising": 0.45, "People-Skill": 0.3, "Marketing-Sales": 0.3, "Finance-Acct": 0.2, "Creative-Skill": 0.2}
            },
            {
                "option_id": 629,
                "option_text": "Want government career here",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 630,
                "option_text": "Undecided about working abroad",
                "trait_tags": {"Admin-Skill": 1.0, "Conventional": 0.45, "Finance-Acct": 0.3, "Hospitality-Svc": 0.2}
            }
        ]
    },
    {
        "question_id": 64,
        "question_text": "What type of WORK SCHEDULE do you prefer?",
        "category": "Work Schedule",
        "options": [
            {
                "option_id": 631,
                "option_text": "Regular 9-5 office hours",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 632,
                "option_text": "Flexible hours / work from home",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 633,
                "option_text": "Shift work (morning/afternoon/night)",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 634,
                "option_text": "School schedule (with summers off)",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 635,
                "option_text": "On-call / emergency response",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 636,
                "option_text": "Contract-based / project work",
                "trait_tags": {"Maritime-Sea": 1.0, "Realistic": 0.45, "Physical-Skill": 0.4, "Technical-Skill": 0.25, "Mechanical-Design": 0.15}
            },
            {
                "option_id": 637,
                "option_text": "Seasonal work (planting/harvest)",
                "trait_tags": {"Agri-Nature": 1.0, "Realistic": 0.45, "Physical-Skill": 0.35, "Field-Research": 0.25, "Lab-Research": 0.15}
            },
            {
                "option_id": 638,
                "option_text": "Self-determined (entrepreneur)",
                "trait_tags": {"Startup-Venture": 1.0, "Enterprising": 0.45, "People-Skill": 0.3, "Marketing-Sales": 0.3, "Finance-Acct": 0.2, "Creative-Skill": 0.2}
            },
            {
                "option_id": 639,
                "option_text": "Creative hours (deadlines-based)",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            },
            {
                "option_id": 640,
                "option_text": "Hospitality hours (weekends/holidays)",
                "trait_tags": {"Hospitality-Svc": 1.0, "People-Skill": 0.45, "Tourism-Travel": 0.4, "Enterprising": 0.35, "Culinary-Arts": 0.3, "Marketing-Sales": 0.2}
            }
        ]
    },
    {
        "question_id": 65,
        "question_text": "How would your friends describe you?",
        "category": "Personality",
        "options": [
            {
                "option_id": 641,
                "option_text": "Caring and nurturing - always helping others",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 642,
                "option_text": "Smart and analytical - the problem solver",
                "trait_tags": {"Data-Analytics": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Software-Dev": 0.3, "Lab-Research": 0.25, "Finance-Acct": 0.2}
            },
            {
                "option_id": 643,
                "option_text": "Creative and artistic - the imaginative one",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            },
            {
                "option_id": 644,
                "option_text": "Outgoing and persuasive - the social butterfly",
                "trait_tags": {"Marketing-Sales": 1.0, "Enterprising": 0.45, "People-Skill": 0.4, "Startup-Venture": 0.3, "Hospitality-Svc": 0.2, "Finance-Acct": 0.15}
            },
            {
                "option_id": 645,
                "option_text": "Organized and reliable - the planner",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 646,
                "option_text": "Patient and understanding - the teacher type",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 647,
                "option_text": "Brave and protective - the defender",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 648,
                "option_text": "Adventurous and daring - the explorer",
                "trait_tags": {"Maritime-Sea": 1.0, "Realistic": 0.45, "Physical-Skill": 0.4, "Technical-Skill": 0.25, "Mechanical-Design": 0.15}
            },
            {
                "option_id": 649,
                "option_text": "Practical and hands-on - the builder",
                "trait_tags": {"Civil-Build": 1.0, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Mechanical-Design": 0.2, "Industrial-Ops": 0.15}
            },
            {
                "option_id": 650,
                "option_text": "Ambitious and driven - the entrepreneur",
                "trait_tags": {"Startup-Venture": 1.0, "Enterprising": 0.45, "People-Skill": 0.3, "Marketing-Sales": 0.3, "Finance-Acct": 0.2, "Creative-Skill": 0.2}
            }
        ]
    },
    {
        "question_id": 66,
        "question_text": "What do you do in your FREE TIME?",
        "category": "Hobbies",
        "options": [
            {
                "option_id": 651,
                "option_text": "Draw, paint, or do arts and crafts",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            },
            {
                "option_id": 652,
                "option_text": "Play video games or use computers",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 653,
                "option_text": "Read books or watch documentaries",
                "trait_tags": {"Lab-Research": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Medical-Lab": 0.3, "Field-Research": 0.25, "Data-Analytics": 0.25}
            },
            {
                "option_id": 654,
                "option_text": "Play sports or exercise",
                "trait_tags": {"Physical-Skill": 1.0, "Realistic": 0.4, "Maritime-Sea": 0.35, "Agri-Nature": 0.35, "Law-Enforce": 0.3, "Rehab-Therapy": 0.3}
            },
            {
                "option_id": 655,
                "option_text": "Volunteer or help in community",
                "trait_tags": {"Community-Serve": 1.0, "Social": 0.45, "People-Skill": 0.4, "Teaching-Ed": 0.25, "Patient-Care": 0.2, "Law-Enforce": 0.15}
            },
            {
                "option_id": 656,
                "option_text": "Cook or try new recipes",
                "trait_tags": {"Hospitality-Svc": 1.0, "People-Skill": 0.45, "Tourism-Travel": 0.4, "Enterprising": 0.35, "Culinary-Arts": 0.3, "Marketing-Sales": 0.2}
            },
            {
                "option_id": 657,
                "option_text": "Build or fix things",
                "trait_tags": {"Technical-Skill": 1.0, "Software-Dev": 0.4, "Hardware-Systems": 0.4, "Realistic": 0.35, "Mechanical-Design": 0.35, "Investigative": 0.25}
            },
            {
                "option_id": 658,
                "option_text": "Care for plants or pets",
                "trait_tags": {"Agri-Nature": 1.0, "Realistic": 0.45, "Physical-Skill": 0.35, "Field-Research": 0.25, "Lab-Research": 0.15}
            },
            {
                "option_id": 659,
                "option_text": "Watch crime/mystery shows",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 660,
                "option_text": "Plan and organize events",
                "trait_tags": {"Admin-Skill": 1.0, "Conventional": 0.45, "Finance-Acct": 0.3, "Hospitality-Svc": 0.2}
            }
        ]
    },
    {
        "question_id": 67,
        "question_text": "What type of TV show/movie do you enjoy most?",
        "category": "Entertainment Preference",
        "options": [
            {
                "option_id": 661,
                "option_text": "Medical dramas (Grey's Anatomy, House)",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 662,
                "option_text": "Crime/detective shows (CSI, NCIS)",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 663,
                "option_text": "Tech/sci-fi (Black Mirror, Silicon Valley)",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 664,
                "option_text": "Business/finance (Suits, Wolf of Wall Street)",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 665,
                "option_text": "Cooking shows (MasterChef, Kitchen Nightmares)",
                "trait_tags": {"Hospitality-Svc": 1.0, "People-Skill": 0.45, "Tourism-Travel": 0.4, "Enterprising": 0.35, "Culinary-Arts": 0.3, "Marketing-Sales": 0.2}
            },
            {
                "option_id": 666,
                "option_text": "Design/makeover shows (home/fashion)",
                "trait_tags": {"Spatial-Design": 1.0, "Artistic": 0.35, "Creative-Skill": 0.35, "Civil-Build": 0.25, "Visual-Design": 0.25, "Technical-Skill": 0.2}
            },
            {
                "option_id": 667,
                "option_text": "Nature/animal documentaries",
                "trait_tags": {"Agri-Nature": 1.0, "Realistic": 0.45, "Physical-Skill": 0.35, "Field-Research": 0.25, "Lab-Research": 0.15}
            },
            {
                "option_id": 668,
                "option_text": "Teacher/school stories",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 669,
                "option_text": "Engineering/building shows (Grand Designs)",
                "trait_tags": {"Civil-Build": 1.0, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Mechanical-Design": 0.2, "Industrial-Ops": 0.15}
            },
            {
                "option_id": 670,
                "option_text": "Social issues/community stories",
                "trait_tags": {"Community-Serve": 1.0, "Social": 0.45, "People-Skill": 0.4, "Teaching-Ed": 0.25, "Patient-Care": 0.2, "Law-Enforce": 0.15}
            }
        ]
    },
    {
        "question_id": 68,
        "question_text": "If you could meet any professional, who would it be?",
        "category": "Role Model",
        "options": [
            {
                "option_id": 671,
                "option_text": "A famous doctor or surgeon",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 672,
                "option_text": "A tech CEO (Elon Musk, Mark Zuckerberg)",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 673,
                "option_text": "A business tycoon (Henry Sy, Manny Pangilinan)",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 674,
                "option_text": "A famous artist or designer",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            },
            {
                "option_id": 675,
                "option_text": "A renowned teacher or educator",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 676,
                "option_text": "A successful chef (Gordon Ramsay)",
                "trait_tags": {"Hospitality-Svc": 1.0, "People-Skill": 0.45, "Tourism-Travel": 0.4, "Enterprising": 0.35, "Culinary-Arts": 0.3, "Marketing-Sales": 0.2}
            },
            {
                "option_id": 677,
                "option_text": "A famous architect or engineer",
                "trait_tags": {"Civil-Build": 1.0, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Mechanical-Design": 0.2, "Industrial-Ops": 0.15}
            },
            {
                "option_id": 678,
                "option_text": "A high-ranking police/military officer",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 679,
                "option_text": "A scientist or researcher",
                "trait_tags": {"Lab-Research": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Medical-Lab": 0.3, "Field-Research": 0.25, "Data-Analytics": 0.25}
            },
            {
                "option_id": 680,
                "option_text": "A social worker or humanitarian",
                "trait_tags": {"Community-Serve": 1.0, "Social": 0.45, "People-Skill": 0.4, "Teaching-Ed": 0.25, "Patient-Care": 0.2, "Law-Enforce": 0.15}
            }
        ]
    },
    {
        "question_id": 69,
        "question_text": "Which school club/organization would you join?",
        "category": "School Involvement",
        "options": [
            {
                "option_id": 681,
                "option_text": "Red Cross Youth / First Aid Club",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 682,
                "option_text": "Computer Club / Robotics Club",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 683,
                "option_text": "Math Club / Science Club",
                "trait_tags": {"Data-Analytics": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Software-Dev": 0.3, "Lab-Research": 0.25, "Finance-Acct": 0.2}
            },
            {
                "option_id": 684,
                "option_text": "Business Club / Junior Achievement",
                "trait_tags": {"Startup-Venture": 1.0, "Enterprising": 0.45, "People-Skill": 0.3, "Marketing-Sales": 0.3, "Finance-Acct": 0.2, "Creative-Skill": 0.2}
            },
            {
                "option_id": 685,
                "option_text": "Art Club / Photography Club",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            },
            {
                "option_id": 686,
                "option_text": "Drama Club / Glee Club",
                "trait_tags": {"Creative-Skill": 1.0, "Artistic": 0.45, "Visual-Design": 0.4, "Digital-Media": 0.4, "Spatial-Design": 0.35}
            },
            {
                "option_id": 687,
                "option_text": "Student Council / Leadership",
                "trait_tags": {"Admin-Skill": 1.0, "Conventional": 0.45, "Finance-Acct": 0.3, "Hospitality-Svc": 0.2}
            },
            {
                "option_id": 688,
                "option_text": "Environmental Club",
                "trait_tags": {"Agri-Nature": 1.0, "Realistic": 0.45, "Physical-Skill": 0.35, "Field-Research": 0.25, "Lab-Research": 0.15}
            },
            {
                "option_id": 689,
                "option_text": "CAT / Citizenship Advancement Training",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 690,
                "option_text": "Peer Tutoring / Academic Mentoring",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            }
        ]
    },
    {
        "question_id": 70,
        "question_text": "Which school project do you enjoy most?",
        "category": "Project Preference",
        "options": [
            {
                "option_id": 691,
                "option_text": "Science investigatory project",
                "trait_tags": {"Lab-Research": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Medical-Lab": 0.3, "Field-Research": 0.25, "Data-Analytics": 0.25}
            },
            {
                "option_id": 692,
                "option_text": "Programming/website project",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 693,
                "option_text": "Business plan/feasibility study",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 694,
                "option_text": "Art project (painting, sculpture)",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            },
            {
                "option_id": 695,
                "option_text": "Community service/outreach",
                "trait_tags": {"Community-Serve": 1.0, "Social": 0.45, "People-Skill": 0.4, "Teaching-Ed": 0.25, "Patient-Care": 0.2, "Law-Enforce": 0.15}
            },
            {
                "option_id": 696,
                "option_text": "Video documentary/film project",
                "trait_tags": {"Digital-Media": 1.0, "Artistic": 0.4, "Creative-Skill": 0.4, "Visual-Design": 0.3, "Software-Dev": 0.2, "Technical-Skill": 0.2}
            },
            {
                "option_id": 697,
                "option_text": "Research paper/case study",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 698,
                "option_text": "Engineering/robotics project",
                "trait_tags": {"Hardware-Systems": 1.0, "Technical-Skill": 0.45, "Realistic": 0.4, "Electrical-Power": 0.3, "Mechanical-Design": 0.25, "Software-Dev": 0.2}
            },
            {
                "option_id": 699,
                "option_text": "Health/nutrition project",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 700,
                "option_text": "Mock trial/debate",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            }
        ]
    },
    {
        "question_id": 71,
        "question_text": "What's your FAVORITE subject in school?",
        "category": "Favorite Subject",
        "options": [
            {
                "option_id": 701,
                "option_text": "Math",
                "trait_tags": {"Data-Analytics": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Software-Dev": 0.3, "Lab-Research": 0.25, "Finance-Acct": 0.2}
            },
            {
                "option_id": 702,
                "option_text": "Science",
                "trait_tags": {"Lab-Research": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Medical-Lab": 0.3, "Field-Research": 0.25, "Data-Analytics": 0.25}
            },
            {
                "option_id": 703,
                "option_text": "English",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 704,
                "option_text": "Filipino",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 705,
                "option_text": "Social Studies",
                "trait_tags": {"Community-Serve": 1.0, "Social": 0.45, "People-Skill": 0.4, "Teaching-Ed": 0.25, "Patient-Care": 0.2, "Law-Enforce": 0.15}
            },
            {
                "option_id": 706,
                "option_text": "Computer/ICT/TLE",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 707,
                "option_text": "Arts",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            },
            {
                "option_id": 708,
                "option_text": "PE",
                "trait_tags": {"Physical-Skill": 1.0, "Realistic": 0.4, "Maritime-Sea": 0.35, "Agri-Nature": 0.35, "Law-Enforce": 0.3, "Rehab-Therapy": 0.3}
            },
            {
                "option_id": 709,
                "option_text": "Accounting/Business subjects",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 710,
                "option_text": "Research/Practical Research",
                "trait_tags": {"Lab-Research": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Medical-Lab": 0.3, "Field-Research": 0.25, "Data-Analytics": 0.25}
            }
        ]
    },
    {
        "question_id": 72,
        "question_text": "What's your LEAST favorite or most challenging subject?",
        "category": "Challenging Subject",
        "options": [
            {
                "option_id": 711,
                "option_text": "Math - too many formulas",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            },
            {
                "option_id": 712,
                "option_text": "Science - hard to memorize",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 713,
                "option_text": "English - grammar is confusing",
                "trait_tags": {"Technical-Skill": 1.0, "Software-Dev": 0.4, "Hardware-Systems": 0.4, "Realistic": 0.35, "Mechanical-Design": 0.35, "Investigative": 0.25}
            },
            {
                "option_id": 714,
                "option_text": "Filipino - prefer English",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 715,
                "option_text": "History - too many dates",
                "trait_tags": {"Data-Analytics": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Software-Dev": 0.3, "Lab-Research": 0.25, "Finance-Acct": 0.2}
            },
            {
                "option_id": 716,
                "option_text": "PE - not athletic",
                "trait_tags": {"Lab-Research": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Medical-Lab": 0.3, "Field-Research": 0.25, "Data-Analytics": 0.25}
            },
            {
                "option_id": 717,
                "option_text": "Arts - not creative",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 718,
                "option_text": "Computer - technology confuses me",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 719,
                "option_text": "None - I do well in all subjects",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 720,
                "option_text": "All are equally challenging",
                "trait_tags": {"Admin-Skill": 1.0, "Conventional": 0.45, "Finance-Acct": 0.3, "Hospitality-Svc": 0.2}
            }
        ]
    },
    {
        "question_id": 73,
        "question_text": "Where do you see yourself in 10 YEARS?",
        "category": "Future Vision",
        "options": [
            {
                "option_id": 721,
                "option_text": "Working in a hospital saving lives",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 722,
                "option_text": "Running my own successful business",
                "trait_tags": {"Startup-Venture": 1.0, "Enterprising": 0.45, "People-Skill": 0.3, "Marketing-Sales": 0.3, "Finance-Acct": 0.2, "Creative-Skill": 0.2}
            },
            {
                "option_id": 723,
                "option_text": "Working as a professional in a corporate office",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 724,
                "option_text": "Teaching and inspiring students",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 725,
                "option_text": "Working abroad earning dollars",
                "trait_tags": {"Maritime-Sea": 1.0, "Realistic": 0.45, "Physical-Skill": 0.4, "Technical-Skill": 0.25, "Mechanical-Design": 0.15}
            },
            {
                "option_id": 726,
                "option_text": "In uniform serving the country",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 727,
                "option_text": "Creating art or designs that people admire",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            },
            {
                "option_id": 728,
                "option_text": "Building structures that last generations",
                "trait_tags": {"Civil-Build": 1.0, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Mechanical-Design": 0.2, "Industrial-Ops": 0.15}
            },
            {
                "option_id": 729,
                "option_text": "Developing technology that changes lives",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 730,
                "option_text": "Serving my community/helping the poor",
                "trait_tags": {"Community-Serve": 1.0, "Social": 0.45, "People-Skill": 0.4, "Teaching-Ed": 0.25, "Patient-Care": 0.2, "Law-Enforce": 0.15}
            }
        ]
    },
    {
        "question_id": 74,
        "question_text": "What LEGACY do you want to leave?",
        "category": "Life Legacy",
        "options": [
            {
                "option_id": 731,
                "option_text": "Saved many lives as a healthcare worker",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 732,
                "option_text": "Built a successful company that employs many",
                "trait_tags": {"Startup-Venture": 1.0, "Enterprising": 0.45, "People-Skill": 0.3, "Marketing-Sales": 0.3, "Finance-Acct": 0.2, "Creative-Skill": 0.2}
            },
            {
                "option_id": 733,
                "option_text": "Inspired thousands of students as a teacher",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 734,
                "option_text": "Created art/designs that people remember",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            },
            {
                "option_id": 735,
                "option_text": "Built structures that stand for centuries",
                "trait_tags": {"Civil-Build": 1.0, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Mechanical-Design": 0.2, "Industrial-Ops": 0.15}
            },
            {
                "option_id": 736,
                "option_text": "Developed technology used by millions",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 737,
                "option_text": "Protected the community from crime",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 738,
                "option_text": "Managed finances that grew wealth",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 739,
                "option_text": "Helped lift families out of poverty",
                "trait_tags": {"Community-Serve": 1.0, "Social": 0.45, "People-Skill": 0.4, "Teaching-Ed": 0.25, "Patient-Care": 0.2, "Law-Enforce": 0.15}
            },
            {
                "option_id": 740,
                "option_text": "Preserved nature for future generations",
                "trait_tags": {"Agri-Nature": 1.0, "Realistic": 0.45, "Physical-Skill": 0.35, "Field-Research": 0.25, "Lab-Research": 0.15}
            }
        ]
    },
    {
        "question_id": 75,
        "question_text": "What's your BIGGEST career fear?",
        "category": "Career Fear",
        "options": [
            {
                "option_id": 741,
                "option_text": "Not passing the board exam",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 742,
                "option_text": "Being stuck in a boring/repetitive job",
                "trait_tags": {"Creative-Skill": 1.0, "Artistic": 0.45, "Visual-Design": 0.4, "Digital-Media": 0.4, "Spatial-Design": 0.35}
            },
            {
                "option_id": 743,
                "option_text": "Not earning enough money",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 744,
                "option_text": "Making a mistake that harms someone",
                "trait_tags": {"Medical-Lab": 1.0, "Analytical-Skill": 0.45, "Investigative": 0.4, "Lab-Research": 0.35, "Technical-Skill": 0.25, "Patient-Care": 0.2}
            },
            {
                "option_id": 745,
                "option_text": "Not being creative enough",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            },
            {
                "option_id": 746,
                "option_text": "Technology becoming obsolete",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 747,
                "option_text": "Not finding a job in my field",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 748,
                "option_text": "Physical danger in the job",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 749,
                "option_text": "Being away from family (OFW)",
                "trait_tags": {"Maritime-Sea": 1.0, "Realistic": 0.45, "Physical-Skill": 0.4, "Technical-Skill": 0.25, "Mechanical-Design": 0.15}
            },
            {
                "option_id": 750,
                "option_text": "Not making a meaningful impact",
                "trait_tags": {"Community-Serve": 1.0, "Social": 0.45, "People-Skill": 0.4, "Teaching-Ed": 0.25, "Patient-Care": 0.2, "Law-Enforce": 0.15}
            }
        ]
    },
    {
        "question_id": 76,
        "question_text": "How do you typically SOLVE PROBLEMS?",
        "category": "Problem Solving",
        "options": [
            {
                "option_id": 751,
                "option_text": "Analyze data and use logic",
                "trait_tags": {"Data-Analytics": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Software-Dev": 0.3, "Lab-Research": 0.25, "Finance-Acct": 0.2}
            },
            {
                "option_id": 752,
                "option_text": "Research and gather information",
                "trait_tags": {"Lab-Research": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Medical-Lab": 0.3, "Field-Research": 0.25, "Data-Analytics": 0.25}
            },
            {
                "option_id": 753,
                "option_text": "Ask experts or people with experience",
                "trait_tags": {"People-Skill": 1.0, "Social": 0.45, "Patient-Care": 0.4, "Teaching-Ed": 0.4, "Hospitality-Svc": 0.4, "Enterprising": 0.3}
            },
            {
                "option_id": 754,
                "option_text": "Trial and error until it works",
                "trait_tags": {"Technical-Skill": 1.0, "Software-Dev": 0.4, "Hardware-Systems": 0.4, "Realistic": 0.35, "Mechanical-Design": 0.35, "Investigative": 0.25}
            },
            {
                "option_id": 755,
                "option_text": "Think creatively, outside the box",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            },
            {
                "option_id": 756,
                "option_text": "Follow established procedures",
                "trait_tags": {"Admin-Skill": 1.0, "Conventional": 0.45, "Finance-Acct": 0.3, "Hospitality-Svc": 0.2}
            },
            {
                "option_id": 757,
                "option_text": "Break it down into smaller steps",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 758,
                "option_text": "Use past experience",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 759,
                "option_text": "Calculate and compute solutions",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 760,
                "option_text": "Take immediate action",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            }
        ]
    },
    {
        "question_id": 77,
        "question_text": "When making DECISIONS, you tend to:",
        "category": "Decision Making",
        "options": [
            {
                "option_id": 761,
                "option_text": "Analyze all the facts and data",
                "trait_tags": {"Data-Analytics": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Software-Dev": 0.3, "Lab-Research": 0.25, "Finance-Acct": 0.2}
            },
            {
                "option_id": 762,
                "option_text": "Consider how it affects others",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 763,
                "option_text": "Think about the financial impact",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 764,
                "option_text": "Go with your gut feeling",
                "trait_tags": {"Creative-Skill": 1.0, "Artistic": 0.45, "Visual-Design": 0.4, "Digital-Media": 0.4, "Spatial-Design": 0.35}
            },
            {
                "option_id": 765,
                "option_text": "Consult with others first",
                "trait_tags": {"People-Skill": 1.0, "Social": 0.45, "Patient-Care": 0.4, "Teaching-Ed": 0.4, "Hospitality-Svc": 0.4, "Enterprising": 0.3}
            },
            {
                "option_id": 766,
                "option_text": "Follow rules and regulations",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 767,
                "option_text": "Think about long-term effects",
                "trait_tags": {"Civil-Build": 1.0, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Mechanical-Design": 0.2, "Industrial-Ops": 0.15}
            },
            {
                "option_id": 768,
                "option_text": "Consider the ethical implications",
                "trait_tags": {"Community-Serve": 1.0, "Social": 0.45, "People-Skill": 0.4, "Teaching-Ed": 0.25, "Patient-Care": 0.2, "Law-Enforce": 0.15}
            },
            {
                "option_id": 769,
                "option_text": "Test with a small experiment first",
                "trait_tags": {"Lab-Research": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Medical-Lab": 0.3, "Field-Research": 0.25, "Data-Analytics": 0.25}
            },
            {
                "option_id": 770,
                "option_text": "Decide quickly and adapt",
                "trait_tags": {"Startup-Venture": 1.0, "Enterprising": 0.45, "People-Skill": 0.3, "Marketing-Sales": 0.3, "Finance-Acct": 0.2, "Creative-Skill": 0.2}
            }
        ]
    },
    {
        "question_id": 78,
        "question_text": "How do you prefer to LEARN new things?",
        "category": "Learning Style",
        "options": [
            {
                "option_id": 771,
                "option_text": "Reading books and articles",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 772,
                "option_text": "Watching videos and tutorials",
                "trait_tags": {"Digital-Media": 1.0, "Artistic": 0.4, "Creative-Skill": 0.4, "Visual-Design": 0.3, "Software-Dev": 0.2, "Technical-Skill": 0.2}
            },
            {
                "option_id": 773,
                "option_text": "Hands-on practice and doing",
                "trait_tags": {"Technical-Skill": 1.0, "Software-Dev": 0.4, "Hardware-Systems": 0.4, "Realistic": 0.35, "Mechanical-Design": 0.35, "Investigative": 0.25}
            },
            {
                "option_id": 774,
                "option_text": "Classroom lectures",
                "trait_tags": {"Lab-Research": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Medical-Lab": 0.3, "Field-Research": 0.25, "Data-Analytics": 0.25}
            },
            {
                "option_id": 775,
                "option_text": "Group discussions",
                "trait_tags": {"People-Skill": 1.0, "Social": 0.45, "Patient-Care": 0.4, "Teaching-Ed": 0.4, "Hospitality-Svc": 0.4, "Enterprising": 0.3}
            },
            {
                "option_id": 776,
                "option_text": "Online courses and apps",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 777,
                "option_text": "Mentorship from experts",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 778,
                "option_text": "Trial and error",
                "trait_tags": {"Startup-Venture": 1.0, "Enterprising": 0.45, "People-Skill": 0.3, "Marketing-Sales": 0.3, "Finance-Acct": 0.2, "Creative-Skill": 0.2}
            },
            {
                "option_id": 779,
                "option_text": "Visual diagrams and maps",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            },
            {
                "option_id": 780,
                "option_text": "Structured step-by-step guides",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            }
        ]
    },
    {
        "question_id": 79,
        "question_text": "How do you handle DISAGREEMENTS with others?",
        "category": "Conflict Resolution",
        "options": [
            {
                "option_id": 781,
                "option_text": "Present facts and logic to convince them",
                "trait_tags": {"Data-Analytics": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Software-Dev": 0.3, "Lab-Research": 0.25, "Finance-Acct": 0.2}
            },
            {
                "option_id": 782,
                "option_text": "Listen to their side first",
                "trait_tags": {"People-Skill": 1.0, "Social": 0.45, "Patient-Care": 0.4, "Teaching-Ed": 0.4, "Hospitality-Svc": 0.4, "Enterprising": 0.3}
            },
            {
                "option_id": 783,
                "option_text": "Find a compromise",
                "trait_tags": {"Community-Serve": 1.0, "Social": 0.45, "People-Skill": 0.4, "Teaching-Ed": 0.25, "Patient-Care": 0.2, "Law-Enforce": 0.15}
            },
            {
                "option_id": 784,
                "option_text": "Stand firm on my position",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 785,
                "option_text": "Avoid confrontation",
                "trait_tags": {"Lab-Research": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Medical-Lab": 0.3, "Field-Research": 0.25, "Data-Analytics": 0.25}
            },
            {
                "option_id": 786,
                "option_text": "Use humor to diffuse tension",
                "trait_tags": {"Hospitality-Svc": 1.0, "People-Skill": 0.45, "Tourism-Travel": 0.4, "Enterprising": 0.35, "Culinary-Arts": 0.3, "Marketing-Sales": 0.2}
            },
            {
                "option_id": 787,
                "option_text": "Seek a mediator",
                "trait_tags": {"Admin-Skill": 1.0, "Conventional": 0.45, "Finance-Acct": 0.3, "Hospitality-Svc": 0.2}
            },
            {
                "option_id": 788,
                "option_text": "Give them time to cool down",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 789,
                "option_text": "Focus on common goals",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 790,
                "option_text": "Propose a creative alternative",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            }
        ]
    },
    {
        "question_id": 80,
        "question_text": "What type of TEAM ROLE do you naturally take?",
        "category": "Team Role",
        "options": [
            {
                "option_id": 791,
                "option_text": "The Leader - directing the team",
                "trait_tags": {"Startup-Venture": 1.0, "Enterprising": 0.45, "People-Skill": 0.3, "Marketing-Sales": 0.3, "Finance-Acct": 0.2, "Creative-Skill": 0.2}
            },
            {
                "option_id": 792,
                "option_text": "The Analyzer - studying the problem",
                "trait_tags": {"Data-Analytics": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Software-Dev": 0.3, "Lab-Research": 0.25, "Finance-Acct": 0.2}
            },
            {
                "option_id": 793,
                "option_text": "The Creative - generating ideas",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            },
            {
                "option_id": 794,
                "option_text": "The Executor - getting things done",
                "trait_tags": {"Technical-Skill": 1.0, "Software-Dev": 0.4, "Hardware-Systems": 0.4, "Realistic": 0.35, "Mechanical-Design": 0.35, "Investigative": 0.25}
            },
            {
                "option_id": 795,
                "option_text": "The Mediator - keeping peace",
                "trait_tags": {"People-Skill": 1.0, "Social": 0.45, "Patient-Care": 0.4, "Teaching-Ed": 0.4, "Hospitality-Svc": 0.4, "Enterprising": 0.3}
            },
            {
                "option_id": 796,
                "option_text": "The Organizer - planning and scheduling",
                "trait_tags": {"Admin-Skill": 1.0, "Conventional": 0.45, "Finance-Acct": 0.3, "Hospitality-Svc": 0.2}
            },
            {
                "option_id": 797,
                "option_text": "The Expert - providing knowledge",
                "trait_tags": {"Lab-Research": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Medical-Lab": 0.3, "Field-Research": 0.25, "Data-Analytics": 0.25}
            },
            {
                "option_id": 798,
                "option_text": "The Supporter - helping wherever needed",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 799,
                "option_text": "The Quality Checker - ensuring accuracy",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 800,
                "option_text": "The Motivator - boosting morale",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            }
        ]
    },
    {
        "question_id": 81,
        "question_text": "Your classmate suddenly collapses during PE class. What would you do first?",
        "category": "Situational - Emergency",
        "options": [
            {
                "option_id": 801,
                "option_text": "Rush to check their pulse and breathing, then perform first aid",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 802,
                "option_text": "Stay calm, take charge and direct others to call for help",
                "trait_tags": {"Startup-Venture": 1.0, "Enterprising": 0.45, "People-Skill": 0.3, "Marketing-Sales": 0.3, "Finance-Acct": 0.2, "Creative-Skill": 0.2}
            },
            {
                "option_id": 803,
                "option_text": "Quickly analyze what might have caused this (heat, dehydration, etc.)",
                "trait_tags": {"Medical-Lab": 1.0, "Analytical-Skill": 0.45, "Investigative": 0.4, "Lab-Research": 0.35, "Technical-Skill": 0.25, "Patient-Care": 0.2}
            },
            {
                "option_id": 804,
                "option_text": "Document the incident and time for the school clinic records",
                "trait_tags": {"Admin-Skill": 1.0, "Conventional": 0.45, "Finance-Acct": 0.3, "Hospitality-Svc": 0.2}
            },
            {
                "option_id": 805,
                "option_text": "Comfort and reassure other classmates who are panicking",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 806,
                "option_text": "Run to get the school nurse or security guard immediately",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 807,
                "option_text": "Think of ways to prevent this from happening again",
                "trait_tags": {"Industrial-Ops": 1.0, "Analytical-Skill": 0.35, "Enterprising": 0.3, "Mechanical-Design": 0.25, "Admin-Skill": 0.2, "Finance-Acct": 0.15}
            },
            {
                "option_id": 808,
                "option_text": "Help create shade or find a cool area for the student",
                "trait_tags": {"Civil-Build": 1.0, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Mechanical-Design": 0.2, "Industrial-Ops": 0.15}
            }
        ]
    },
    {
        "question_id": 82,
        "question_text": "Your barangay is planning a community project. Which role would you volunteer for?",
        "category": "Situational - Community",
        "options": [
            {
                "option_id": 809,
                "option_text": "Organize a free health checkup and first aid station",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 810,
                "option_text": "Design posters and promotional materials for the event",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            },
            {
                "option_id": 811,
                "option_text": "Create a website or social media page to promote it",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 812,
                "option_text": "Handle the budget, collect donations, and track expenses",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 813,
                "option_text": "Lead and coordinate all the volunteer teams",
                "trait_tags": {"Startup-Venture": 1.0, "Enterprising": 0.45, "People-Skill": 0.3, "Marketing-Sales": 0.3, "Finance-Acct": 0.2, "Creative-Skill": 0.2}
            },
            {
                "option_id": 814,
                "option_text": "Teach livelihood skills or conduct tutorials for youth",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 815,
                "option_text": "Set up security and crowd control measures",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 816,
                "option_text": "Plan the venue layout and structural setup",
                "trait_tags": {"Civil-Build": 1.0, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Mechanical-Design": 0.2, "Industrial-Ops": 0.15}
            },
            {
                "option_id": 817,
                "option_text": "Organize a tree planting or clean-up drive",
                "trait_tags": {"Agri-Nature": 1.0, "Realistic": 0.45, "Physical-Skill": 0.35, "Field-Research": 0.25, "Lab-Research": 0.15}
            },
            {
                "option_id": 818,
                "option_text": "Prepare food and refreshments for volunteers",
                "trait_tags": {"Hospitality-Svc": 1.0, "People-Skill": 0.45, "Tourism-Travel": 0.4, "Enterprising": 0.35, "Culinary-Arts": 0.3, "Marketing-Sales": 0.2}
            }
        ]
    },
    {
        "question_id": 83,
        "question_text": "You're assigned to lead a group project with unmotivated members. How do you handle it?",
        "category": "Situational - Leadership",
        "options": [
            {
                "option_id": 819,
                "option_text": "Create a detailed project plan with clear deadlines for everyone",
                "trait_tags": {"Admin-Skill": 1.0, "Conventional": 0.45, "Finance-Acct": 0.3, "Hospitality-Svc": 0.2}
            },
            {
                "option_id": 820,
                "option_text": "Talk to each member personally to understand their concerns",
                "trait_tags": {"People-Skill": 1.0, "Social": 0.45, "Patient-Care": 0.4, "Teaching-Ed": 0.4, "Hospitality-Svc": 0.4, "Enterprising": 0.3}
            },
            {
                "option_id": 821,
                "option_text": "Take charge and assign tasks based on each person's strengths",
                "trait_tags": {"Startup-Venture": 1.0, "Enterprising": 0.45, "People-Skill": 0.3, "Marketing-Sales": 0.3, "Finance-Acct": 0.2, "Creative-Skill": 0.2}
            },
            {
                "option_id": 822,
                "option_text": "Use creative approaches to make the project more interesting",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            },
            {
                "option_id": 823,
                "option_text": "Research the topic thoroughly and share knowledge to help them",
                "trait_tags": {"Lab-Research": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Medical-Lab": 0.3, "Field-Research": 0.25, "Data-Analytics": 0.25}
            },
            {
                "option_id": 824,
                "option_text": "Create a rewards system or gamify the tasks",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 825,
                "option_text": "Build a shared online document or app to track progress",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 826,
                "option_text": "Focus on the practical, hands-on parts to keep them engaged",
                "trait_tags": {"Technical-Skill": 1.0, "Software-Dev": 0.4, "Hardware-Systems": 0.4, "Realistic": 0.35, "Mechanical-Design": 0.35, "Investigative": 0.25}
            }
        ]
    },
    {
        "question_id": 84,
        "question_text": "A typhoon damaged several houses in your area. How would you want to help?",
        "category": "Situational - Disaster Response",
        "options": [
            {
                "option_id": 827,
                "option_text": "Join medical missions to treat injured victims",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 828,
                "option_text": "Help rebuild or repair damaged structures",
                "trait_tags": {"Civil-Build": 1.0, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Mechanical-Design": 0.2, "Industrial-Ops": 0.15}
            },
            {
                "option_id": 829,
                "option_text": "Organize relief goods distribution and logistics",
                "trait_tags": {"Admin-Skill": 1.0, "Conventional": 0.45, "Finance-Acct": 0.3, "Hospitality-Svc": 0.2}
            },
            {
                "option_id": 830,
                "option_text": "Set up communication systems for rescue coordination",
                "trait_tags": {"Hardware-Systems": 1.0, "Technical-Skill": 0.45, "Realistic": 0.4, "Electrical-Power": 0.3, "Mechanical-Design": 0.25, "Software-Dev": 0.2}
            },
            {
                "option_id": 831,
                "option_text": "Document damage and help families with insurance claims",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 832,
                "option_text": "Counsel traumatized victims, especially children",
                "trait_tags": {"Rehab-Therapy": 1.0, "Physical-Skill": 0.4, "Social": 0.35, "People-Skill": 0.35, "Patient-Care": 0.3, "Teaching-Ed": 0.2}
            },
            {
                "option_id": 833,
                "option_text": "Help in rescue operations and maintain order",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 834,
                "option_text": "Cook meals and manage temporary shelters",
                "trait_tags": {"Hospitality-Svc": 1.0, "People-Skill": 0.45, "Tourism-Travel": 0.4, "Enterprising": 0.35, "Culinary-Arts": 0.3, "Marketing-Sales": 0.2}
            },
            {
                "option_id": 835,
                "option_text": "Assess environmental damage and clean-up needs",
                "trait_tags": {"Field-Research": 1.0, "Investigative": 0.4, "Agri-Nature": 0.3, "Analytical-Skill": 0.3, "Physical-Skill": 0.25, "Lab-Research": 0.25}
            },
            {
                "option_id": 836,
                "option_text": "Use social media to spread awareness and call for donations",
                "trait_tags": {"Digital-Media": 1.0, "Artistic": 0.4, "Creative-Skill": 0.4, "Visual-Design": 0.3, "Software-Dev": 0.2, "Technical-Skill": 0.2}
            }
        ]
    },
    {
        "question_id": 85,
        "question_text": "Your school is organizing a career fair. What booth would you want to manage?",
        "category": "Situational - School Event",
        "options": [
            {
                "option_id": 837,
                "option_text": "Healthcare booth with blood pressure and BMI checks",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 838,
                "option_text": "Tech booth showcasing apps and coding demos",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 839,
                "option_text": "Engineering booth with building models and robots",
                "trait_tags": {"Mechanical-Design": 1.0, "Realistic": 0.45, "Technical-Skill": 0.4, "Industrial-Ops": 0.25, "Civil-Build": 0.2, "Electrical-Power": 0.2}
            },
            {
                "option_id": 840,
                "option_text": "Business booth with entrepreneurship tips and mock stocks",
                "trait_tags": {"Startup-Venture": 1.0, "Enterprising": 0.45, "People-Skill": 0.3, "Marketing-Sales": 0.3, "Finance-Acct": 0.2, "Creative-Skill": 0.2}
            },
            {
                "option_id": 841,
                "option_text": "Arts booth with live sketching and design demos",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            },
            {
                "option_id": 842,
                "option_text": "Criminology booth with forensic science activities",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 843,
                "option_text": "Maritime booth with ship models and navigation demos",
                "trait_tags": {"Maritime-Sea": 1.0, "Realistic": 0.45, "Physical-Skill": 0.4, "Technical-Skill": 0.25, "Mechanical-Design": 0.15}
            },
            {
                "option_id": 844,
                "option_text": "Hospitality booth serving sample dishes and drinks",
                "trait_tags": {"Hospitality-Svc": 1.0, "People-Skill": 0.45, "Tourism-Travel": 0.4, "Enterprising": 0.35, "Culinary-Arts": 0.3, "Marketing-Sales": 0.2}
            },
            {
                "option_id": 845,
                "option_text": "Science booth with experiments and lab demonstrations",
                "trait_tags": {"Lab-Research": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Medical-Lab": 0.3, "Field-Research": 0.25, "Data-Analytics": 0.25}
            },
            {
                "option_id": 846,
                "option_text": "Agriculture booth with plant propagation activities",
                "trait_tags": {"Agri-Nature": 1.0, "Realistic": 0.45, "Physical-Skill": 0.35, "Field-Research": 0.25, "Lab-Research": 0.15}
            }
        ]
    },
    {
        "question_id": 86,
        "question_text": "You found a lost wallet with cash and IDs near your school. What do you do?",
        "category": "Situational - Ethics",
        "options": [
            {
                "option_id": 847,
                "option_text": "Turn it in to the school security or police station",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 848,
                "option_text": "Try to contact the owner using the ID information",
                "trait_tags": {"People-Skill": 1.0, "Social": 0.45, "Patient-Care": 0.4, "Teaching-Ed": 0.4, "Hospitality-Svc": 0.4, "Enterprising": 0.3}
            },
            {
                "option_id": 849,
                "option_text": "Post about it on social media to find the owner",
                "trait_tags": {"Digital-Media": 1.0, "Artistic": 0.4, "Creative-Skill": 0.4, "Visual-Design": 0.3, "Software-Dev": 0.2, "Technical-Skill": 0.2}
            },
            {
                "option_id": 850,
                "option_text": "Keep it safe and make an organized list of contents",
                "trait_tags": {"Admin-Skill": 1.0, "Conventional": 0.45, "Finance-Acct": 0.3, "Hospitality-Svc": 0.2}
            },
            {
                "option_id": 851,
                "option_text": "Announce it in school and ask teachers for help",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 852,
                "option_text": "Think about how the owner must be feeling and act quickly",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 853,
                "option_text": "Research the name to find social media accounts",
                "trait_tags": {"Data-Analytics": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Software-Dev": 0.3, "Lab-Research": 0.25, "Finance-Acct": 0.2}
            },
            {
                "option_id": 854,
                "option_text": "Document everything with photos before returning",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            }
        ]
    },
    {
        "question_id": 87,
        "question_text": "Your family is starting a small business. How would you contribute?",
        "category": "Situational - Family Business",
        "options": [
            {
                "option_id": 855,
                "option_text": "Handle the accounting, pricing, and financial records",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 856,
                "option_text": "Create the logo, packaging, and visual branding",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            },
            {
                "option_id": 857,
                "option_text": "Build a website and manage online sales",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 858,
                "option_text": "Develop marketing strategies and social media content",
                "trait_tags": {"Marketing-Sales": 1.0, "Enterprising": 0.45, "People-Skill": 0.4, "Startup-Venture": 0.3, "Hospitality-Svc": 0.2, "Finance-Acct": 0.15}
            },
            {
                "option_id": 859,
                "option_text": "Manage inventory, suppliers, and daily operations",
                "trait_tags": {"Admin-Skill": 1.0, "Conventional": 0.45, "Finance-Acct": 0.3, "Hospitality-Svc": 0.2}
            },
            {
                "option_id": 860,
                "option_text": "Come up with new product ideas and business strategies",
                "trait_tags": {"Startup-Venture": 1.0, "Enterprising": 0.45, "People-Skill": 0.3, "Marketing-Sales": 0.3, "Finance-Acct": 0.2, "Creative-Skill": 0.2}
            },
            {
                "option_id": 861,
                "option_text": "Handle customer service and build client relationships",
                "trait_tags": {"People-Skill": 1.0, "Social": 0.45, "Patient-Care": 0.4, "Teaching-Ed": 0.4, "Hospitality-Svc": 0.4, "Enterprising": 0.3}
            },
            {
                "option_id": 862,
                "option_text": "Set up equipment, fixtures, and technical systems",
                "trait_tags": {"Technical-Skill": 1.0, "Software-Dev": 0.4, "Hardware-Systems": 0.4, "Realistic": 0.35, "Mechanical-Design": 0.35, "Investigative": 0.25}
            },
            {
                "option_id": 863,
                "option_text": "If it's food, focus on recipes and food preparation",
                "trait_tags": {"Hospitality-Svc": 1.0, "People-Skill": 0.45, "Tourism-Travel": 0.4, "Enterprising": 0.35, "Culinary-Arts": 0.3, "Marketing-Sales": 0.2}
            },
            {
                "option_id": 864,
                "option_text": "Ensure legal compliance and business registration",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            }
        ]
    },
    {
        "question_id": 88,
        "question_text": "You notice a classmate seems depressed and withdrawn lately. How do you approach this?",
        "category": "Situational - Mental Health",
        "options": [
            {
                "option_id": 865,
                "option_text": "Talk to them privately and listen without judgment",
                "trait_tags": {"Rehab-Therapy": 1.0, "Physical-Skill": 0.4, "Social": 0.35, "People-Skill": 0.35, "Patient-Care": 0.3, "Teaching-Ed": 0.2}
            },
            {
                "option_id": 866,
                "option_text": "Inform a trusted teacher or guidance counselor",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 867,
                "option_text": "Research about mental health to understand what they might be going through",
                "trait_tags": {"Lab-Research": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Medical-Lab": 0.3, "Field-Research": 0.25, "Data-Analytics": 0.25}
            },
            {
                "option_id": 868,
                "option_text": "Invite them to activities to help them feel included",
                "trait_tags": {"People-Skill": 1.0, "Social": 0.45, "Patient-Care": 0.4, "Teaching-Ed": 0.4, "Hospitality-Svc": 0.4, "Enterprising": 0.3}
            },
            {
                "option_id": 869,
                "option_text": "Create something artistic or a playlist to cheer them up",
                "trait_tags": {"Creative-Skill": 1.0, "Artistic": 0.45, "Visual-Design": 0.4, "Digital-Media": 0.4, "Spatial-Design": 0.35}
            },
            {
                "option_id": 870,
                "option_text": "Organize a support group among trusted friends",
                "trait_tags": {"Community-Serve": 1.0, "Social": 0.45, "People-Skill": 0.4, "Teaching-Ed": 0.25, "Patient-Care": 0.2, "Law-Enforce": 0.15}
            },
            {
                "option_id": 871,
                "option_text": "Monitor the situation and document any concerning changes",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 872,
                "option_text": "Help them with schoolwork to reduce their stress",
                "trait_tags": {"Admin-Skill": 1.0, "Conventional": 0.45, "Finance-Acct": 0.3, "Hospitality-Svc": 0.2}
            }
        ]
    },
    {
        "question_id": 89,
        "question_text": "Your school's computer lab has been hacked and files are encrypted. What's your reaction?",
        "category": "Situational - Technology Crisis",
        "options": [
            {
                "option_id": 873,
                "option_text": "Try to analyze the malware and find a solution",
                "trait_tags": {"Cyber-Defense": 1.0, "Technical-Skill": 0.4, "Investigative": 0.35, "Software-Dev": 0.25, "Law-Enforce": 0.15}
            },
            {
                "option_id": 874,
                "option_text": "Document everything and report to IT authorities",
                "trait_tags": {"Admin-Skill": 1.0, "Conventional": 0.45, "Finance-Acct": 0.3, "Hospitality-Svc": 0.2}
            },
            {
                "option_id": 875,
                "option_text": "Help restore data from backup systems",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 876,
                "option_text": "Investigate who might be responsible",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 877,
                "option_text": "Calm down panicking students and teachers",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 878,
                "option_text": "Calculate the financial impact and insurance claims",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 879,
                "option_text": "Set up alternative systems so classes can continue",
                "trait_tags": {"Hardware-Systems": 1.0, "Technical-Skill": 0.45, "Realistic": 0.4, "Electrical-Power": 0.3, "Mechanical-Design": 0.25, "Software-Dev": 0.2}
            },
            {
                "option_id": 880,
                "option_text": "Create awareness materials about cybersecurity",
                "trait_tags": {"Digital-Media": 1.0, "Artistic": 0.4, "Creative-Skill": 0.4, "Visual-Design": 0.3, "Software-Dev": 0.2, "Technical-Skill": 0.2}
            }
        ]
    },
    {
        "question_id": 90,
        "question_text": "You're stranded on an island with your friends for a survival challenge. What role do you take?",
        "category": "Situational - Survival",
        "options": [
            {
                "option_id": 881,
                "option_text": "Build shelter and secure the campsite",
                "trait_tags": {"Civil-Build": 1.0, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Mechanical-Design": 0.2, "Industrial-Ops": 0.15}
            },
            {
                "option_id": 882,
                "option_text": "Find and purify water, identify safe plants to eat",
                "trait_tags": {"Field-Research": 1.0, "Investigative": 0.4, "Agri-Nature": 0.3, "Analytical-Skill": 0.3, "Physical-Skill": 0.25, "Lab-Research": 0.25}
            },
            {
                "option_id": 883,
                "option_text": "Take care of anyone who gets injured or sick",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 884,
                "option_text": "Lead the group and make strategic decisions",
                "trait_tags": {"Startup-Venture": 1.0, "Enterprising": 0.45, "People-Skill": 0.3, "Marketing-Sales": 0.3, "Finance-Acct": 0.2, "Creative-Skill": 0.2}
            },
            {
                "option_id": 885,
                "option_text": "Create tools and repair equipment",
                "trait_tags": {"Mechanical-Design": 1.0, "Realistic": 0.45, "Technical-Skill": 0.4, "Industrial-Ops": 0.25, "Civil-Build": 0.2, "Electrical-Power": 0.2}
            },
            {
                "option_id": 886,
                "option_text": "Keep everyone's spirits up and resolve conflicts",
                "trait_tags": {"People-Skill": 1.0, "Social": 0.45, "Patient-Care": 0.4, "Teaching-Ed": 0.4, "Hospitality-Svc": 0.4, "Enterprising": 0.3}
            },
            {
                "option_id": 887,
                "option_text": "Figure out navigation and plan an escape route",
                "trait_tags": {"Maritime-Sea": 1.0, "Realistic": 0.45, "Physical-Skill": 0.4, "Technical-Skill": 0.25, "Mechanical-Design": 0.15}
            },
            {
                "option_id": 888,
                "option_text": "Hunt, fish, or forage for food",
                "trait_tags": {"Agri-Nature": 1.0, "Realistic": 0.45, "Physical-Skill": 0.35, "Field-Research": 0.25, "Lab-Research": 0.15}
            },
            {
                "option_id": 889,
                "option_text": "Document the experience and keep a survival log",
                "trait_tags": {"Creative-Skill": 1.0, "Artistic": 0.45, "Visual-Design": 0.4, "Digital-Media": 0.4, "Spatial-Design": 0.35}
            },
            {
                "option_id": 890,
                "option_text": "Create signals or devices to call for rescue",
                "trait_tags": {"Hardware-Systems": 1.0, "Technical-Skill": 0.45, "Realistic": 0.4, "Electrical-Power": 0.3, "Mechanical-Design": 0.25, "Software-Dev": 0.2}
            }
        ]
    },
    {
        "question_id": 91,
        "question_text": "A local store owner asks for advice to compete with online shopping. What do you suggest?",
        "category": "Situational - Business",
        "options": [
            {
                "option_id": 891,
                "option_text": "Build them an e-commerce website and app",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 892,
                "option_text": "Help them with digital marketing and social media",
                "trait_tags": {"Marketing-Sales": 1.0, "Enterprising": 0.45, "People-Skill": 0.4, "Startup-Venture": 0.3, "Hospitality-Svc": 0.2, "Finance-Acct": 0.15}
            },
            {
                "option_id": 893,
                "option_text": "Redesign their store layout and visual branding",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            },
            {
                "option_id": 894,
                "option_text": "Analyze their finances and suggest cost-cutting",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 895,
                "option_text": "Create a loyalty program and customer database",
                "trait_tags": {"Data-Analytics": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Software-Dev": 0.3, "Lab-Research": 0.25, "Finance-Acct": 0.2}
            },
            {
                "option_id": 896,
                "option_text": "Train their staff on customer service",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 897,
                "option_text": "Focus on personalized service that online can't match",
                "trait_tags": {"Hospitality-Svc": 1.0, "People-Skill": 0.45, "Tourism-Travel": 0.4, "Enterprising": 0.35, "Culinary-Arts": 0.3, "Marketing-Sales": 0.2}
            },
            {
                "option_id": 898,
                "option_text": "Develop a unique business strategy to stand out",
                "trait_tags": {"Startup-Venture": 1.0, "Enterprising": 0.45, "People-Skill": 0.3, "Marketing-Sales": 0.3, "Finance-Acct": 0.2, "Creative-Skill": 0.2}
            }
        ]
    },
    {
        "question_id": 92,
        "question_text": "Your town is debating whether to build a factory that will create jobs but may cause pollution. Your stance?",
        "category": "Situational - Environmental",
        "options": [
            {
                "option_id": 899,
                "option_text": "Conduct environmental impact studies first",
                "trait_tags": {"Field-Research": 1.0, "Investigative": 0.4, "Agri-Nature": 0.3, "Analytical-Skill": 0.3, "Physical-Skill": 0.25, "Lab-Research": 0.25}
            },
            {
                "option_id": 900,
                "option_text": "Propose engineering solutions to minimize pollution",
                "trait_tags": {"Industrial-Ops": 1.0, "Analytical-Skill": 0.35, "Enterprising": 0.3, "Mechanical-Design": 0.25, "Admin-Skill": 0.2, "Finance-Acct": 0.15}
            },
            {
                "option_id": 901,
                "option_text": "Focus on the economic benefits and job creation",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 902,
                "option_text": "Advocate for renewable and sustainable alternatives",
                "trait_tags": {"Agri-Nature": 1.0, "Realistic": 0.45, "Physical-Skill": 0.35, "Field-Research": 0.25, "Lab-Research": 0.15}
            },
            {
                "option_id": 903,
                "option_text": "Analyze health risks for the community",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 904,
                "option_text": "Research legal requirements and compliance",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 905,
                "option_text": "Organize community forums for discussion",
                "trait_tags": {"Community-Serve": 1.0, "Social": 0.45, "People-Skill": 0.4, "Teaching-Ed": 0.25, "Patient-Care": 0.2, "Law-Enforce": 0.15}
            },
            {
                "option_id": 906,
                "option_text": "Create awareness campaigns about both sides",
                "trait_tags": {"Digital-Media": 1.0, "Artistic": 0.4, "Creative-Skill": 0.4, "Visual-Design": 0.3, "Software-Dev": 0.2, "Technical-Skill": 0.2}
            }
        ]
    },
    {
        "question_id": 93,
        "question_text": "You're asked to help organize your school's foundation anniversary. What task do you prefer?",
        "category": "Situational - Event Planning",
        "options": [
            {
                "option_id": 907,
                "option_text": "Handle the budget and collect contributions",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 908,
                "option_text": "Design invitations, banners, and stage backdrop",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            },
            {
                "option_id": 909,
                "option_text": "Direct the program and coordinate performances",
                "trait_tags": {"Creative-Skill": 1.0, "Artistic": 0.45, "Visual-Design": 0.4, "Digital-Media": 0.4, "Spatial-Design": 0.35}
            },
            {
                "option_id": 910,
                "option_text": "Set up sound systems, lights, and technical equipment",
                "trait_tags": {"Hardware-Systems": 1.0, "Technical-Skill": 0.45, "Realistic": 0.4, "Electrical-Power": 0.3, "Mechanical-Design": 0.25, "Software-Dev": 0.2}
            },
            {
                "option_id": 911,
                "option_text": "Manage food catering and hospitality for guests",
                "trait_tags": {"Hospitality-Svc": 1.0, "People-Skill": 0.45, "Tourism-Travel": 0.4, "Enterprising": 0.35, "Culinary-Arts": 0.3, "Marketing-Sales": 0.2}
            },
            {
                "option_id": 912,
                "option_text": "Lead the overall organizing committee",
                "trait_tags": {"Startup-Venture": 1.0, "Enterprising": 0.45, "People-Skill": 0.3, "Marketing-Sales": 0.3, "Finance-Acct": 0.2, "Creative-Skill": 0.2}
            },
            {
                "option_id": 913,
                "option_text": "Handle security and crowd management",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 914,
                "option_text": "Document and livestream the event online",
                "trait_tags": {"Digital-Media": 1.0, "Artistic": 0.4, "Creative-Skill": 0.4, "Visual-Design": 0.3, "Software-Dev": 0.2, "Technical-Skill": 0.2}
            },
            {
                "option_id": 915,
                "option_text": "Prepare first aid station in case of emergencies",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 916,
                "option_text": "Coordinate with teachers and handle logistics",
                "trait_tags": {"Admin-Skill": 1.0, "Conventional": 0.45, "Finance-Acct": 0.3, "Hospitality-Svc": 0.2}
            }
        ]
    },
    {
        "question_id": 94,
        "question_text": "A friend confides that they're being bullied online. How do you help?",
        "category": "Situational - Cyberbullying",
        "options": [
            {
                "option_id": 917,
                "option_text": "Listen to them and provide emotional support",
                "trait_tags": {"Rehab-Therapy": 1.0, "Physical-Skill": 0.4, "Social": 0.35, "People-Skill": 0.35, "Patient-Care": 0.3, "Teaching-Ed": 0.2}
            },
            {
                "option_id": 918,
                "option_text": "Document the evidence and report to authorities",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 919,
                "option_text": "Help them adjust privacy settings and block the bully",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 920,
                "option_text": "Inform a teacher or guidance counselor",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 921,
                "option_text": "Research laws about cyberbullying",
                "trait_tags": {"Community-Serve": 1.0, "Social": 0.45, "People-Skill": 0.4, "Teaching-Ed": 0.25, "Patient-Care": 0.2, "Law-Enforce": 0.15}
            },
            {
                "option_id": 922,
                "option_text": "Create a support group with other friends",
                "trait_tags": {"People-Skill": 1.0, "Social": 0.45, "Patient-Care": 0.4, "Teaching-Ed": 0.4, "Hospitality-Svc": 0.4, "Enterprising": 0.3}
            },
            {
                "option_id": 923,
                "option_text": "Help them build confidence through activities",
                "trait_tags": {"Creative-Skill": 1.0, "Artistic": 0.45, "Visual-Design": 0.4, "Digital-Media": 0.4, "Spatial-Design": 0.35}
            },
            {
                "option_id": 924,
                "option_text": "Track down who the bully is using digital clues",
                "trait_tags": {"Cyber-Defense": 1.0, "Technical-Skill": 0.4, "Investigative": 0.35, "Software-Dev": 0.25, "Law-Enforce": 0.15}
            }
        ]
    },
    {
        "question_id": 95,
        "question_text": "Your family member is diagnosed with a chronic illness. How do you cope and help?",
        "category": "Situational - Family Health",
        "options": [
            {
                "option_id": 925,
                "option_text": "Learn about the illness and help with their care",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 926,
                "option_text": "Research the best doctors and treatment options",
                "trait_tags": {"Medical-Lab": 1.0, "Analytical-Skill": 0.45, "Investigative": 0.4, "Lab-Research": 0.35, "Technical-Skill": 0.25, "Patient-Care": 0.2}
            },
            {
                "option_id": 927,
                "option_text": "Manage medical expenses and insurance paperwork",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 928,
                "option_text": "Provide emotional support and stay positive",
                "trait_tags": {"Rehab-Therapy": 1.0, "Physical-Skill": 0.4, "Social": 0.35, "People-Skill": 0.35, "Patient-Care": 0.3, "Teaching-Ed": 0.2}
            },
            {
                "option_id": 929,
                "option_text": "Help with physical therapy exercises at home",
                "trait_tags": {"Rehab-Therapy": 1.0, "Physical-Skill": 0.4, "Social": 0.35, "People-Skill": 0.35, "Patient-Care": 0.3, "Teaching-Ed": 0.2}
            },
            {
                "option_id": 930,
                "option_text": "Prepare nutritious meals for their diet",
                "trait_tags": {"Hospitality-Svc": 1.0, "People-Skill": 0.45, "Tourism-Travel": 0.4, "Enterprising": 0.35, "Culinary-Arts": 0.3, "Marketing-Sales": 0.2}
            },
            {
                "option_id": 931,
                "option_text": "Organize family schedules to share caregiving duties",
                "trait_tags": {"Admin-Skill": 1.0, "Conventional": 0.45, "Finance-Acct": 0.3, "Hospitality-Svc": 0.2}
            },
            {
                "option_id": 932,
                "option_text": "Find support groups and community resources",
                "trait_tags": {"Community-Serve": 1.0, "Social": 0.45, "People-Skill": 0.4, "Teaching-Ed": 0.25, "Patient-Care": 0.2, "Law-Enforce": 0.15}
            }
        ]
    },
    {
        "question_id": 96,
        "question_text": "You witness someone shoplifting at a mall. What's your reaction?",
        "category": "Situational - Ethics",
        "options": [
            {
                "option_id": 933,
                "option_text": "Immediately report to security guards",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 934,
                "option_text": "Discreetly take photos/video as evidence",
                "trait_tags": {"Digital-Media": 1.0, "Artistic": 0.4, "Creative-Skill": 0.4, "Visual-Design": 0.3, "Software-Dev": 0.2, "Technical-Skill": 0.2}
            },
            {
                "option_id": 935,
                "option_text": "Think about why someone might resort to stealing",
                "trait_tags": {"Community-Serve": 1.0, "Social": 0.45, "People-Skill": 0.4, "Teaching-Ed": 0.25, "Patient-Care": 0.2, "Law-Enforce": 0.15}
            },
            {
                "option_id": 936,
                "option_text": "Alert the store staff calmly and privately",
                "trait_tags": {"Admin-Skill": 1.0, "Conventional": 0.45, "Finance-Acct": 0.3, "Hospitality-Svc": 0.2}
            },
            {
                "option_id": 937,
                "option_text": "Consider if it's safe to confront them directly",
                "trait_tags": {"People-Skill": 1.0, "Social": 0.45, "Patient-Care": 0.4, "Teaching-Ed": 0.4, "Hospitality-Svc": 0.4, "Enterprising": 0.3}
            },
            {
                "option_id": 938,
                "option_text": "Think about the store's loss prevention measures",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 939,
                "option_text": "Wonder about the psychological factors involved",
                "trait_tags": {"Rehab-Therapy": 1.0, "Physical-Skill": 0.4, "Social": 0.35, "People-Skill": 0.35, "Patient-Care": 0.3, "Teaching-Ed": 0.2}
            },
            {
                "option_id": 940,
                "option_text": "Think of technical solutions like better security systems",
                "trait_tags": {"Hardware-Systems": 1.0, "Technical-Skill": 0.45, "Realistic": 0.4, "Electrical-Power": 0.3, "Mechanical-Design": 0.25, "Software-Dev": 0.2}
            }
        ]
    },
    {
        "question_id": 97,
        "question_text": "Your school wants to create a mobile app for students. What feature do you want to develop?",
        "category": "Situational - Technology",
        "options": [
            {
                "option_id": 941,
                "option_text": "Grade tracking and academic performance analytics",
                "trait_tags": {"Data-Analytics": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Software-Dev": 0.3, "Lab-Research": 0.25, "Finance-Acct": 0.2}
            },
            {
                "option_id": 942,
                "option_text": "The overall user interface and visual design",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            },
            {
                "option_id": 943,
                "option_text": "The backend programming and database",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 944,
                "option_text": "Security features to protect student data",
                "trait_tags": {"Cyber-Defense": 1.0, "Technical-Skill": 0.4, "Investigative": 0.35, "Software-Dev": 0.25, "Law-Enforce": 0.15}
            },
            {
                "option_id": 945,
                "option_text": "Communication features for student-teacher interaction",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 946,
                "option_text": "Financial modules for tracking fees and payments",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 947,
                "option_text": "Health and wellness tracking features",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 948,
                "option_text": "Event planning and school activity calendar",
                "trait_tags": {"Admin-Skill": 1.0, "Conventional": 0.45, "Finance-Acct": 0.3, "Hospitality-Svc": 0.2}
            }
        ]
    },
    {
        "question_id": 98,
        "question_text": "You're tasked to create a documentary about your local community. What topic would you choose?",
        "category": "Situational - Media",
        "options": [
            {
                "option_id": 949,
                "option_text": "Local healthcare heroes and medical workers",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 950,
                "option_text": "Small businesses and entrepreneurial success stories",
                "trait_tags": {"Startup-Venture": 1.0, "Enterprising": 0.45, "People-Skill": 0.3, "Marketing-Sales": 0.3, "Finance-Acct": 0.2, "Creative-Skill": 0.2}
            },
            {
                "option_id": 951,
                "option_text": "Environmental issues and conservation efforts",
                "trait_tags": {"Field-Research": 1.0, "Investigative": 0.4, "Agri-Nature": 0.3, "Analytical-Skill": 0.3, "Physical-Skill": 0.25, "Lab-Research": 0.25}
            },
            {
                "option_id": 952,
                "option_text": "Local artists, musicians, and creative talents",
                "trait_tags": {"Creative-Skill": 1.0, "Artistic": 0.45, "Visual-Design": 0.4, "Digital-Media": 0.4, "Spatial-Design": 0.35}
            },
            {
                "option_id": 953,
                "option_text": "Education and inspiring teacher stories",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 954,
                "option_text": "Crime prevention and community safety",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 955,
                "option_text": "Farmers and agricultural practices",
                "trait_tags": {"Agri-Nature": 1.0, "Realistic": 0.45, "Physical-Skill": 0.35, "Field-Research": 0.25, "Lab-Research": 0.15}
            },
            {
                "option_id": 956,
                "option_text": "Infrastructure development and urban planning",
                "trait_tags": {"Civil-Build": 1.0, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Mechanical-Design": 0.2, "Industrial-Ops": 0.15}
            },
            {
                "option_id": 957,
                "option_text": "Technology adoption and digital transformation",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 958,
                "option_text": "Local food culture and culinary traditions",
                "trait_tags": {"Hospitality-Svc": 1.0, "People-Skill": 0.45, "Tourism-Travel": 0.4, "Enterprising": 0.35, "Culinary-Arts": 0.3, "Marketing-Sales": 0.2}
            }
        ]
    },
    {
        "question_id": 99,
        "question_text": "A classmate copied your homework and submitted it as their own. How do you handle it?",
        "category": "Situational - Academic Integrity",
        "options": [
            {
                "option_id": 959,
                "option_text": "Report it to the teacher with evidence",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 960,
                "option_text": "Confront them privately and ask why they did it",
                "trait_tags": {"People-Skill": 1.0, "Social": 0.45, "Patient-Care": 0.4, "Teaching-Ed": 0.4, "Hospitality-Svc": 0.4, "Enterprising": 0.3}
            },
            {
                "option_id": 961,
                "option_text": "Offer to tutor them so they don't need to copy again",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 962,
                "option_text": "Keep records and document future incidents",
                "trait_tags": {"Admin-Skill": 1.0, "Conventional": 0.45, "Finance-Acct": 0.3, "Hospitality-Svc": 0.2}
            },
            {
                "option_id": 963,
                "option_text": "Think about their circumstances - maybe they needed help",
                "trait_tags": {"Rehab-Therapy": 1.0, "Physical-Skill": 0.4, "Social": 0.35, "People-Skill": 0.35, "Patient-Care": 0.3, "Teaching-Ed": 0.2}
            },
            {
                "option_id": 964,
                "option_text": "Create a study group to help struggling classmates",
                "trait_tags": {"Community-Serve": 1.0, "Social": 0.45, "People-Skill": 0.4, "Teaching-Ed": 0.25, "Patient-Care": 0.2, "Law-Enforce": 0.15}
            },
            {
                "option_id": 965,
                "option_text": "Develop a system to prevent copying in the future",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 966,
                "option_text": "Let it go this time but protect your work better",
                "trait_tags": {"Cyber-Defense": 1.0, "Technical-Skill": 0.4, "Investigative": 0.35, "Software-Dev": 0.25, "Law-Enforce": 0.15}
            }
        ]
    },
    {
        "question_id": 100,
        "question_text": "You won a significant amount in a school raffle. How would you spend it?",
        "category": "Situational - Financial Decision",
        "options": [
            {
                "option_id": 967,
                "option_text": "Save it and invest for future education",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 968,
                "option_text": "Buy equipment for a skill I want to develop",
                "trait_tags": {"Technical-Skill": 1.0, "Software-Dev": 0.4, "Hardware-Systems": 0.4, "Realistic": 0.35, "Mechanical-Design": 0.35, "Investigative": 0.25}
            },
            {
                "option_id": 969,
                "option_text": "Donate part of it to charity or community causes",
                "trait_tags": {"Community-Serve": 1.0, "Social": 0.45, "People-Skill": 0.4, "Teaching-Ed": 0.25, "Patient-Care": 0.2, "Law-Enforce": 0.15}
            },
            {
                "option_id": 970,
                "option_text": "Start a small business or side hustle",
                "trait_tags": {"Startup-Venture": 1.0, "Enterprising": 0.45, "People-Skill": 0.3, "Marketing-Sales": 0.3, "Finance-Acct": 0.2, "Creative-Skill": 0.2}
            },
            {
                "option_id": 971,
                "option_text": "Buy art supplies or creative tools",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            },
            {
                "option_id": 972,
                "option_text": "Get a new computer or tech gadgets",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 973,
                "option_text": "Help my family with household expenses",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 974,
                "option_text": "Take a course or workshop to learn something new",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 975,
                "option_text": "Travel and explore new places",
                "trait_tags": {"Hospitality-Svc": 1.0, "People-Skill": 0.45, "Tourism-Travel": 0.4, "Enterprising": 0.35, "Culinary-Arts": 0.3, "Marketing-Sales": 0.2}
            },
            {
                "option_id": 976,
                "option_text": "Buy books and study materials",
                "trait_tags": {"Lab-Research": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Medical-Lab": 0.3, "Field-Research": 0.25, "Data-Analytics": 0.25}
            }
        ]
    },
    {
        "question_id": 101,
        "question_text": "Your school is organizing a career fair. Which booth would you volunteer to manage?",
        "category": "Situational - Career Fair",
        "options": [
            {
                "option_id": 1001,
                "option_text": "Healthcare booth - explaining nursing and medical careers",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 1002,
                "option_text": "Technology booth - demonstrating apps and coding projects",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 1003,
                "option_text": "Engineering booth - showing building models and designs",
                "trait_tags": {"Civil-Build": 1.0, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Mechanical-Design": 0.2, "Industrial-Ops": 0.15}
            },
            {
                "option_id": 1004,
                "option_text": "Business booth - presenting entrepreneurship success stories",
                "trait_tags": {"Startup-Venture": 1.0, "Enterprising": 0.45, "People-Skill": 0.3, "Marketing-Sales": 0.3, "Finance-Acct": 0.2, "Creative-Skill": 0.2}
            },
            {
                "option_id": 1005,
                "option_text": "Arts booth - displaying creative works and portfolios",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            },
            {
                "option_id": 1006,
                "option_text": "Education booth - helping students explore teaching careers",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 1007,
                "option_text": "Law & Security booth - discussing criminology and justice",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 1008,
                "option_text": "Maritime booth - explaining ship careers and navigation",
                "trait_tags": {"Maritime-Sea": 1.0, "Realistic": 0.45, "Physical-Skill": 0.4, "Technical-Skill": 0.25, "Mechanical-Design": 0.15}
            },
            {
                "option_id": 1009,
                "option_text": "Agriculture booth - showcasing farming innovations",
                "trait_tags": {"Agri-Nature": 1.0, "Realistic": 0.45, "Physical-Skill": 0.35, "Field-Research": 0.25, "Lab-Research": 0.15}
            },
            {
                "option_id": 1010,
                "option_text": "Hospitality booth - promoting tourism and hotel management",
                "trait_tags": {"Hospitality-Svc": 1.0, "People-Skill": 0.45, "Tourism-Travel": 0.4, "Enterprising": 0.35, "Culinary-Arts": 0.3, "Marketing-Sales": 0.2}
            }
        ]
    },
    {
        "question_id": 102,
        "question_text": "A local barangay asks for help solving a community problem. What role would you take?",
        "category": "Situational - Community Problem",
        "options": [
            {
                "option_id": 1011,
                "option_text": "Organize a health screening for residents",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 1012,
                "option_text": "Set up a computer literacy program for youth",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 1013,
                "option_text": "Help design safer roads and walkways",
                "trait_tags": {"Civil-Build": 1.0, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Mechanical-Design": 0.2, "Industrial-Ops": 0.15}
            },
            {
                "option_id": 1014,
                "option_text": "Start a livelihood program for unemployed residents",
                "trait_tags": {"Startup-Venture": 1.0, "Enterprising": 0.45, "People-Skill": 0.3, "Marketing-Sales": 0.3, "Finance-Acct": 0.2, "Creative-Skill": 0.2}
            },
            {
                "option_id": 1015,
                "option_text": "Create murals and beautify public spaces",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            },
            {
                "option_id": 1016,
                "option_text": "Tutor children who are struggling in school",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 1017,
                "option_text": "Help establish a neighborhood watch program",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 1018,
                "option_text": "Advocate for government services and social welfare",
                "trait_tags": {"Community-Serve": 1.0, "Social": 0.45, "People-Skill": 0.4, "Teaching-Ed": 0.25, "Patient-Care": 0.2, "Law-Enforce": 0.15}
            },
            {
                "option_id": 1019,
                "option_text": "Set up an urban garden for food security",
                "trait_tags": {"Agri-Nature": 1.0, "Realistic": 0.45, "Physical-Skill": 0.35, "Field-Research": 0.25, "Lab-Research": 0.15}
            },
            {
                "option_id": 1020,
                "option_text": "Organize community events and festivals",
                "trait_tags": {"Hospitality-Svc": 1.0, "People-Skill": 0.45, "Tourism-Travel": 0.4, "Enterprising": 0.35, "Culinary-Arts": 0.3, "Marketing-Sales": 0.2}
            }
        ]
    },
    {
        "question_id": 103,
        "question_text": "You discover your friend is making unhealthy life choices. How do you help?",
        "category": "Situational - Friend Support",
        "options": [
            {
                "option_id": 1021,
                "option_text": "Research health information and share it with them",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 1022,
                "option_text": "Find apps or tools that could help them track their habits",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 1023,
                "option_text": "Create a structured plan with goals and timelines",
                "trait_tags": {"Industrial-Ops": 1.0, "Analytical-Skill": 0.35, "Enterprising": 0.3, "Mechanical-Design": 0.25, "Admin-Skill": 0.2, "Finance-Acct": 0.15}
            },
            {
                "option_id": 1024,
                "option_text": "Connect them with a counselor or therapist",
                "trait_tags": {"Rehab-Therapy": 1.0, "Physical-Skill": 0.4, "Social": 0.35, "People-Skill": 0.35, "Patient-Care": 0.3, "Teaching-Ed": 0.2}
            },
            {
                "option_id": 1025,
                "option_text": "Express your feelings through creative activities together",
                "trait_tags": {"Creative-Skill": 1.0, "Artistic": 0.45, "Visual-Design": 0.4, "Digital-Media": 0.4, "Spatial-Design": 0.35}
            },
            {
                "option_id": 1026,
                "option_text": "Teach them about self-care and wellness techniques",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 1027,
                "option_text": "Investigate what triggered their behavior changes",
                "trait_tags": {"Lab-Research": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Medical-Lab": 0.3, "Field-Research": 0.25, "Data-Analytics": 0.25}
            },
            {
                "option_id": 1028,
                "option_text": "Organize group activities to keep them engaged socially",
                "trait_tags": {"People-Skill": 1.0, "Social": 0.45, "Patient-Care": 0.4, "Teaching-Ed": 0.4, "Hospitality-Svc": 0.4, "Enterprising": 0.3}
            },
            {
                "option_id": 1029,
                "option_text": "Encourage physical activities like sports or exercise",
                "trait_tags": {"Physical-Skill": 1.0, "Realistic": 0.4, "Maritime-Sea": 0.35, "Agri-Nature": 0.35, "Law-Enforce": 0.3, "Rehab-Therapy": 0.3}
            },
            {
                "option_id": 1030,
                "option_text": "Help them manage their time and finances better",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            }
        ]
    },
    {
        "question_id": 104,
        "question_text": "Your family is planning to start a small business. What role would you take?",
        "category": "Situational - Family Business",
        "options": [
            {
                "option_id": 1031,
                "option_text": "Handle the bookkeeping and financial records",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 1032,
                "option_text": "Build a website and manage online presence",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 1033,
                "option_text": "Design the store layout and physical setup",
                "trait_tags": {"Spatial-Design": 1.0, "Artistic": 0.35, "Creative-Skill": 0.35, "Civil-Build": 0.25, "Visual-Design": 0.25, "Technical-Skill": 0.2}
            },
            {
                "option_id": 1034,
                "option_text": "Create the business plan and growth strategy",
                "trait_tags": {"Startup-Venture": 1.0, "Enterprising": 0.45, "People-Skill": 0.3, "Marketing-Sales": 0.3, "Finance-Acct": 0.2, "Creative-Skill": 0.2}
            },
            {
                "option_id": 1035,
                "option_text": "Design logos, packaging, and marketing materials",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            },
            {
                "option_id": 1036,
                "option_text": "Train employees and create procedures",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 1037,
                "option_text": "Handle customer relations and sales",
                "trait_tags": {"Marketing-Sales": 1.0, "Enterprising": 0.45, "People-Skill": 0.4, "Startup-Venture": 0.3, "Hospitality-Svc": 0.2, "Finance-Acct": 0.15}
            },
            {
                "option_id": 1038,
                "option_text": "Manage inventory and supply chain logistics",
                "trait_tags": {"Admin-Skill": 1.0, "Conventional": 0.45, "Finance-Acct": 0.3, "Hospitality-Svc": 0.2}
            },
            {
                "option_id": 1039,
                "option_text": "Research market trends and competition",
                "trait_tags": {"Data-Analytics": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Software-Dev": 0.3, "Lab-Research": 0.25, "Finance-Acct": 0.2}
            },
            {
                "option_id": 1040,
                "option_text": "Ensure safety and security measures are in place",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            }
        ]
    },
    {
        "question_id": 105,
        "question_text": "There's a power outage in your area for several hours. How do you spend your time?",
        "category": "Situational - Power Outage",
        "options": [
            {
                "option_id": 1041,
                "option_text": "Check on elderly neighbors and offer assistance",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 1042,
                "option_text": "Think about how to prevent this with better infrastructure",
                "trait_tags": {"Electrical-Power": 1.0, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3, "Mechanical-Design": 0.2, "Industrial-Ops": 0.2}
            },
            {
                "option_id": 1043,
                "option_text": "Plan a backup power solution like solar panels",
                "trait_tags": {"Mechanical-Design": 1.0, "Realistic": 0.45, "Technical-Skill": 0.4, "Industrial-Ops": 0.25, "Civil-Build": 0.2, "Electrical-Power": 0.2}
            },
            {
                "option_id": 1044,
                "option_text": "Calculate how much money was lost due to the outage",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 1045,
                "option_text": "Draw, paint, or work on creative projects by candlelight",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            },
            {
                "option_id": 1046,
                "option_text": "Read books and study without distractions",
                "trait_tags": {"Lab-Research": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Medical-Lab": 0.3, "Field-Research": 0.25, "Data-Analytics": 0.25}
            },
            {
                "option_id": 1047,
                "option_text": "Play games and tell stories with family",
                "trait_tags": {"People-Skill": 1.0, "Social": 0.45, "Patient-Care": 0.4, "Teaching-Ed": 0.4, "Hospitality-Svc": 0.4, "Enterprising": 0.3}
            },
            {
                "option_id": 1048,
                "option_text": "Help organize the neighborhood response",
                "trait_tags": {"Community-Serve": 1.0, "Social": 0.45, "People-Skill": 0.4, "Teaching-Ed": 0.25, "Patient-Care": 0.2, "Law-Enforce": 0.15}
            },
            {
                "option_id": 1049,
                "option_text": "Go outside and explore nature",
                "trait_tags": {"Field-Research": 1.0, "Investigative": 0.4, "Agri-Nature": 0.3, "Analytical-Skill": 0.3, "Physical-Skill": 0.25, "Lab-Research": 0.25}
            },
            {
                "option_id": 1050,
                "option_text": "Cook and prepare food using alternative methods",
                "trait_tags": {"Hospitality-Svc": 1.0, "People-Skill": 0.45, "Tourism-Travel": 0.4, "Enterprising": 0.35, "Culinary-Arts": 0.3, "Marketing-Sales": 0.2}
            }
        ]
    },
    {
        "question_id": 106,
        "question_text": "Your school needs help preparing for an accreditation visit. What would you volunteer to do?",
        "category": "Situational - Accreditation",
        "options": [
            {
                "option_id": 1051,
                "option_text": "Organize health records and first aid stations",
                "trait_tags": {"Health-Admin": 1.0, "Admin-Skill": 0.45, "Conventional": 0.4, "Finance-Acct": 0.2, "Patient-Care": 0.15}
            },
            {
                "option_id": 1052,
                "option_text": "Set up computer systems and presentations",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 1053,
                "option_text": "Help with building maintenance and repairs",
                "trait_tags": {"Civil-Build": 1.0, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Mechanical-Design": 0.2, "Industrial-Ops": 0.15}
            },
            {
                "option_id": 1054,
                "option_text": "Prepare financial reports and budget documents",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 1055,
                "option_text": "Create visual displays and decorations",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            },
            {
                "option_id": 1056,
                "option_text": "Prepare lesson plans and teaching demonstrations",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 1057,
                "option_text": "Manage security and visitor flow",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 1058,
                "option_text": "Organize documents and administrative files",
                "trait_tags": {"Admin-Skill": 1.0, "Conventional": 0.45, "Finance-Acct": 0.3, "Hospitality-Svc": 0.2}
            },
            {
                "option_id": 1059,
                "option_text": "Prepare scientific lab demonstrations",
                "trait_tags": {"Lab-Research": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Medical-Lab": 0.3, "Field-Research": 0.25, "Data-Analytics": 0.25}
            },
            {
                "option_id": 1060,
                "option_text": "Coordinate food and hospitality for guests",
                "trait_tags": {"Hospitality-Svc": 1.0, "People-Skill": 0.45, "Tourism-Travel": 0.4, "Enterprising": 0.35, "Culinary-Arts": 0.3, "Marketing-Sales": 0.2}
            }
        ]
    },
    {
        "question_id": 107,
        "question_text": "You witness someone collapse on the street. What is your immediate response?",
        "category": "Situational - Medical Emergency",
        "options": [
            {
                "option_id": 1061,
                "option_text": "Rush to help and check their vital signs",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 1062,
                "option_text": "Call emergency services immediately",
                "trait_tags": {"Technical-Skill": 1.0, "Software-Dev": 0.4, "Hardware-Systems": 0.4, "Realistic": 0.35, "Mechanical-Design": 0.35, "Investigative": 0.25}
            },
            {
                "option_id": 1063,
                "option_text": "Look for a safe space to move them away from traffic",
                "trait_tags": {"Civil-Build": 1.0, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Mechanical-Design": 0.2, "Industrial-Ops": 0.15}
            },
            {
                "option_id": 1064,
                "option_text": "Start CPR if they're unresponsive",
                "trait_tags": {"Rehab-Therapy": 1.0, "Physical-Skill": 0.4, "Social": 0.35, "People-Skill": 0.35, "Patient-Care": 0.3, "Teaching-Ed": 0.2}
            },
            {
                "option_id": 1065,
                "option_text": "Document what happened in case it's needed",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 1066,
                "option_text": "Calm down bystanders and explain what to do",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 1067,
                "option_text": "Direct traffic to prevent accidents",
                "trait_tags": {"Community-Serve": 1.0, "Social": 0.45, "People-Skill": 0.4, "Teaching-Ed": 0.25, "Patient-Care": 0.2, "Law-Enforce": 0.15}
            },
            {
                "option_id": 1068,
                "option_text": "Search their belongings for medical information",
                "trait_tags": {"Medical-Lab": 1.0, "Analytical-Skill": 0.45, "Investigative": 0.4, "Lab-Research": 0.35, "Technical-Skill": 0.25, "Patient-Care": 0.2}
            },
            {
                "option_id": 1069,
                "option_text": "Stay with them and provide emotional support",
                "trait_tags": {"People-Skill": 1.0, "Social": 0.45, "Patient-Care": 0.4, "Teaching-Ed": 0.4, "Hospitality-Svc": 0.4, "Enterprising": 0.3}
            },
            {
                "option_id": 1070,
                "option_text": "Think about how hospitals could respond faster",
                "trait_tags": {"Health-Admin": 1.0, "Admin-Skill": 0.45, "Conventional": 0.4, "Finance-Acct": 0.2, "Patient-Care": 0.15}
            }
        ]
    },
    {
        "question_id": 108,
        "question_text": "Your group is assigned a research project. What role do you naturally take?",
        "category": "Situational - Group Research",
        "options": [
            {
                "option_id": 1071,
                "option_text": "Conduct interviews and gather primary data",
                "trait_tags": {"People-Skill": 1.0, "Social": 0.45, "Patient-Care": 0.4, "Teaching-Ed": 0.4, "Hospitality-Svc": 0.4, "Enterprising": 0.3}
            },
            {
                "option_id": 1072,
                "option_text": "Analyze data and create statistical reports",
                "trait_tags": {"Data-Analytics": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Software-Dev": 0.3, "Lab-Research": 0.25, "Finance-Acct": 0.2}
            },
            {
                "option_id": 1073,
                "option_text": "Write the research paper and documentation",
                "trait_tags": {"Lab-Research": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Medical-Lab": 0.3, "Field-Research": 0.25, "Data-Analytics": 0.25}
            },
            {
                "option_id": 1074,
                "option_text": "Design the presentation and visual aids",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            },
            {
                "option_id": 1075,
                "option_text": "Present the findings to the class",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 1076,
                "option_text": "Manage the timeline and task assignments",
                "trait_tags": {"Admin-Skill": 1.0, "Conventional": 0.45, "Finance-Acct": 0.3, "Hospitality-Svc": 0.2}
            },
            {
                "option_id": 1077,
                "option_text": "Create digital tools or apps for data collection",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 1078,
                "option_text": "Conduct experiments and lab work",
                "trait_tags": {"Medical-Lab": 1.0, "Analytical-Skill": 0.45, "Investigative": 0.4, "Lab-Research": 0.35, "Technical-Skill": 0.25, "Patient-Care": 0.2}
            },
            {
                "option_id": 1079,
                "option_text": "Do field research and site visits",
                "trait_tags": {"Field-Research": 1.0, "Investigative": 0.4, "Agri-Nature": 0.3, "Analytical-Skill": 0.3, "Physical-Skill": 0.25, "Lab-Research": 0.25}
            },
            {
                "option_id": 1080,
                "option_text": "Handle the budget and resource allocation",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            }
        ]
    },
    {
        "question_id": 109,
        "question_text": "A typhoon warning is issued for your area. How do you prepare?",
        "category": "Situational - Typhoon Preparation",
        "options": [
            {
                "option_id": 1081,
                "option_text": "Prepare first aid kit and medical supplies",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 1082,
                "option_text": "Charge devices and backup important files",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 1083,
                "option_text": "Secure the house structure and check for weak points",
                "trait_tags": {"Civil-Build": 1.0, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Mechanical-Design": 0.2, "Industrial-Ops": 0.15}
            },
            {
                "option_id": 1084,
                "option_text": "Stock up on food and essential supplies",
                "trait_tags": {"Hospitality-Svc": 1.0, "People-Skill": 0.45, "Tourism-Travel": 0.4, "Enterprising": 0.35, "Culinary-Arts": 0.3, "Marketing-Sales": 0.2}
            },
            {
                "option_id": 1085,
                "option_text": "Create evacuation plans and routes",
                "trait_tags": {"Community-Serve": 1.0, "Social": 0.45, "People-Skill": 0.4, "Teaching-Ed": 0.25, "Patient-Care": 0.2, "Law-Enforce": 0.15}
            },
            {
                "option_id": 1086,
                "option_text": "Teach family members about safety protocols",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 1087,
                "option_text": "Check emergency hotlines and communication plans",
                "trait_tags": {"Technical-Skill": 1.0, "Software-Dev": 0.4, "Hardware-Systems": 0.4, "Realistic": 0.35, "Mechanical-Design": 0.35, "Investigative": 0.25}
            },
            {
                "option_id": 1088,
                "option_text": "Prepare flashlights and alternative power sources",
                "trait_tags": {"Electrical-Power": 1.0, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3, "Mechanical-Design": 0.2, "Industrial-Ops": 0.2}
            },
            {
                "option_id": 1089,
                "option_text": "Protect plants and agricultural materials",
                "trait_tags": {"Agri-Nature": 1.0, "Realistic": 0.45, "Physical-Skill": 0.35, "Field-Research": 0.25, "Lab-Research": 0.15}
            },
            {
                "option_id": 1090,
                "option_text": "Calculate potential damage costs for insurance",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            }
        ]
    },
    {
        "question_id": 110,
        "question_text": "You're given the chance to shadow a professional for a day. Who would you choose?",
        "category": "Situational - Job Shadow",
        "options": [
            {
                "option_id": 1091,
                "option_text": "A doctor or nurse in a busy hospital",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 1092,
                "option_text": "A software engineer at a tech company",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 1093,
                "option_text": "An architect designing a new building",
                "trait_tags": {"Spatial-Design": 1.0, "Artistic": 0.35, "Creative-Skill": 0.35, "Civil-Build": 0.25, "Visual-Design": 0.25, "Technical-Skill": 0.2}
            },
            {
                "option_id": 1094,
                "option_text": "A CEO running a successful company",
                "trait_tags": {"Startup-Venture": 1.0, "Enterprising": 0.45, "People-Skill": 0.3, "Marketing-Sales": 0.3, "Finance-Acct": 0.2, "Creative-Skill": 0.2}
            },
            {
                "option_id": 1095,
                "option_text": "A film director or artist in a studio",
                "trait_tags": {"Digital-Media": 1.0, "Artistic": 0.4, "Creative-Skill": 0.4, "Visual-Design": 0.3, "Software-Dev": 0.2, "Technical-Skill": 0.2}
            },
            {
                "option_id": 1096,
                "option_text": "A university professor teaching students",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 1097,
                "option_text": "A detective solving criminal cases",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 1098,
                "option_text": "A marine biologist researching ocean life",
                "trait_tags": {"Field-Research": 1.0, "Investigative": 0.4, "Agri-Nature": 0.3, "Analytical-Skill": 0.3, "Physical-Skill": 0.25, "Lab-Research": 0.25}
            },
            {
                "option_id": 1099,
                "option_text": "A ship captain on an international voyage",
                "trait_tags": {"Maritime-Sea": 1.0, "Realistic": 0.45, "Physical-Skill": 0.4, "Technical-Skill": 0.25, "Mechanical-Design": 0.15}
            },
            {
                "option_id": 1100,
                "option_text": "A physical therapist helping patients recover",
                "trait_tags": {"Rehab-Therapy": 1.0, "Physical-Skill": 0.4, "Social": 0.35, "People-Skill": 0.35, "Patient-Care": 0.3, "Teaching-Ed": 0.2}
            }
        ]
    },
    {
        "question_id": 111,
        "question_text": "Your school website has been hacked. How would you help?",
        "category": "Situational - Cyber Attack",
        "options": [
            {
                "option_id": 1101,
                "option_text": "Identify the vulnerability and fix the security breach",
                "trait_tags": {"Cyber-Defense": 1.0, "Technical-Skill": 0.4, "Investigative": 0.35, "Software-Dev": 0.25, "Law-Enforce": 0.15}
            },
            {
                "option_id": 1102,
                "option_text": "Restore the website from backup systems",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 1103,
                "option_text": "Investigate who was responsible and gather evidence",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 1104,
                "option_text": "Communicate with students about what happened",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 1105,
                "option_text": "Calculate the damage and costs to fix it",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 1106,
                "option_text": "Redesign the website with better security",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            },
            {
                "option_id": 1107,
                "option_text": "Create a report documenting the incident",
                "trait_tags": {"Admin-Skill": 1.0, "Conventional": 0.45, "Finance-Acct": 0.3, "Hospitality-Svc": 0.2}
            },
            {
                "option_id": 1108,
                "option_text": "Train others on cybersecurity best practices",
                "trait_tags": {"Technical-Skill": 1.0, "Software-Dev": 0.4, "Hardware-Systems": 0.4, "Realistic": 0.35, "Mechanical-Design": 0.35, "Investigative": 0.25}
            },
            {
                "option_id": 1109,
                "option_text": "Analyze data logs to understand the attack pattern",
                "trait_tags": {"Data-Analytics": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Software-Dev": 0.3, "Lab-Research": 0.25, "Finance-Acct": 0.2}
            },
            {
                "option_id": 1110,
                "option_text": "Coordinate with the IT team on the response",
                "trait_tags": {"Hardware-Systems": 1.0, "Technical-Skill": 0.45, "Realistic": 0.4, "Electrical-Power": 0.3, "Mechanical-Design": 0.25, "Software-Dev": 0.2}
            }
        ]
    },
    {
        "question_id": 112,
        "question_text": "A new shopping mall is opening in your town. What job would interest you there?",
        "category": "Situational - Mall Jobs",
        "options": [
            {
                "option_id": 1111,
                "option_text": "Clinic staff in the mall's medical center",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 1112,
                "option_text": "IT support for the mall's technology systems",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 1113,
                "option_text": "Facilities manager overseeing building operations",
                "trait_tags": {"Civil-Build": 1.0, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Mechanical-Design": 0.2, "Industrial-Ops": 0.15}
            },
            {
                "option_id": 1114,
                "option_text": "Store owner running my own business there",
                "trait_tags": {"Startup-Venture": 1.0, "Enterprising": 0.45, "People-Skill": 0.3, "Marketing-Sales": 0.3, "Finance-Acct": 0.2, "Creative-Skill": 0.2}
            },
            {
                "option_id": 1115,
                "option_text": "Interior designer for store layouts",
                "trait_tags": {"Spatial-Design": 1.0, "Artistic": 0.35, "Creative-Skill": 0.35, "Civil-Build": 0.25, "Visual-Design": 0.25, "Technical-Skill": 0.2}
            },
            {
                "option_id": 1116,
                "option_text": "Customer service training manager",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 1117,
                "option_text": "Security officer ensuring safety",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 1118,
                "option_text": "Marketing staff promoting mall events",
                "trait_tags": {"Marketing-Sales": 1.0, "Enterprising": 0.45, "People-Skill": 0.4, "Startup-Venture": 0.3, "Hospitality-Svc": 0.2, "Finance-Acct": 0.15}
            },
            {
                "option_id": 1119,
                "option_text": "Restaurant manager in the food court",
                "trait_tags": {"Hospitality-Svc": 1.0, "People-Skill": 0.45, "Tourism-Travel": 0.4, "Enterprising": 0.35, "Culinary-Arts": 0.3, "Marketing-Sales": 0.2}
            },
            {
                "option_id": 1120,
                "option_text": "Accountant managing finances for stores",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            }
        ]
    },
    {
        "question_id": 113,
        "question_text": "Your neighbor's pet is acting strangely and seems sick. What do you do?",
        "category": "Situational - Sick Pet",
        "options": [
            {
                "option_id": 1121,
                "option_text": "Check the pet's symptoms and suggest going to a vet",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 1122,
                "option_text": "Search online for possible causes and treatments",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 1123,
                "option_text": "Think about what in their environment could be causing it",
                "trait_tags": {"Field-Research": 1.0, "Investigative": 0.4, "Agri-Nature": 0.3, "Analytical-Skill": 0.3, "Physical-Skill": 0.25, "Lab-Research": 0.25}
            },
            {
                "option_id": 1124,
                "option_text": "Offer to help pay for veterinary care",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 1125,
                "option_text": "Make the pet comfortable and provide comfort",
                "trait_tags": {"Rehab-Therapy": 1.0, "Physical-Skill": 0.4, "Social": 0.35, "People-Skill": 0.35, "Patient-Care": 0.3, "Teaching-Ed": 0.2}
            },
            {
                "option_id": 1126,
                "option_text": "Explain to the neighbor about pet health care",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 1127,
                "option_text": "Investigate if other neighborhood pets are affected",
                "trait_tags": {"Lab-Research": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Medical-Lab": 0.3, "Field-Research": 0.25, "Data-Analytics": 0.25}
            },
            {
                "option_id": 1128,
                "option_text": "Contact animal rescue organizations for help",
                "trait_tags": {"Community-Serve": 1.0, "Social": 0.45, "People-Skill": 0.4, "Teaching-Ed": 0.25, "Patient-Care": 0.2, "Law-Enforce": 0.15}
            },
            {
                "option_id": 1129,
                "option_text": "Prepare special food or medicine if needed",
                "trait_tags": {"Hospitality-Svc": 1.0, "People-Skill": 0.45, "Tourism-Travel": 0.4, "Enterprising": 0.35, "Culinary-Arts": 0.3, "Marketing-Sales": 0.2}
            },
            {
                "option_id": 1130,
                "option_text": "Check if it might be something agricultural-related",
                "trait_tags": {"Agri-Nature": 1.0, "Realistic": 0.45, "Physical-Skill": 0.35, "Field-Research": 0.25, "Lab-Research": 0.15}
            }
        ]
    },
    {
        "question_id": 114,
        "question_text": "Your school wants to reduce its environmental impact. What initiative would you lead?",
        "category": "Situational - Environmental Initiative",
        "options": [
            {
                "option_id": 1131,
                "option_text": "Health education about environmental pollution effects",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 1132,
                "option_text": "Develop an app to track the school's carbon footprint",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 1133,
                "option_text": "Design eco-friendly building modifications",
                "trait_tags": {"Civil-Build": 1.0, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Mechanical-Design": 0.2, "Industrial-Ops": 0.15}
            },
            {
                "option_id": 1134,
                "option_text": "Create a recycling business that generates funds",
                "trait_tags": {"Startup-Venture": 1.0, "Enterprising": 0.45, "People-Skill": 0.3, "Marketing-Sales": 0.3, "Finance-Acct": 0.2, "Creative-Skill": 0.2}
            },
            {
                "option_id": 1135,
                "option_text": "Design posters and campaigns for awareness",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            },
            {
                "option_id": 1136,
                "option_text": "Teach students about sustainability and conservation",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 1137,
                "option_text": "Conduct scientific research on local environmental issues",
                "trait_tags": {"Field-Research": 1.0, "Investigative": 0.4, "Agri-Nature": 0.3, "Analytical-Skill": 0.3, "Physical-Skill": 0.25, "Lab-Research": 0.25}
            },
            {
                "option_id": 1138,
                "option_text": "Advocate for policy changes with school administration",
                "trait_tags": {"Community-Serve": 1.0, "Social": 0.45, "People-Skill": 0.4, "Teaching-Ed": 0.25, "Patient-Care": 0.2, "Law-Enforce": 0.15}
            },
            {
                "option_id": 1139,
                "option_text": "Start a school garden and composting program",
                "trait_tags": {"Agri-Nature": 1.0, "Realistic": 0.45, "Physical-Skill": 0.35, "Field-Research": 0.25, "Lab-Research": 0.15}
            },
            {
                "option_id": 1140,
                "option_text": "Install solar panels or energy-efficient systems",
                "trait_tags": {"Electrical-Power": 1.0, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3, "Mechanical-Design": 0.2, "Industrial-Ops": 0.2}
            }
        ]
    },
    {
        "question_id": 115,
        "question_text": "You find a wallet with a large amount of cash and no ID. What do you do?",
        "category": "Situational - Found Wallet",
        "options": [
            {
                "option_id": 1141,
                "option_text": "Turn it in to the nearest authority or police station",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 1142,
                "option_text": "Post about it on social media to find the owner",
                "trait_tags": {"Digital-Media": 1.0, "Artistic": 0.4, "Creative-Skill": 0.4, "Visual-Design": 0.3, "Software-Dev": 0.2, "Technical-Skill": 0.2}
            },
            {
                "option_id": 1143,
                "option_text": "Count the money and document everything carefully",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 1144,
                "option_text": "Look for any clues inside about who owns it",
                "trait_tags": {"Lab-Research": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Medical-Lab": 0.3, "Field-Research": 0.25, "Data-Analytics": 0.25}
            },
            {
                "option_id": 1145,
                "option_text": "Ask people in the area if they lost a wallet",
                "trait_tags": {"People-Skill": 1.0, "Social": 0.45, "Patient-Care": 0.4, "Teaching-Ed": 0.4, "Hospitality-Svc": 0.4, "Enterprising": 0.3}
            },
            {
                "option_id": 1146,
                "option_text": "Teach others about honesty and integrity through this",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 1147,
                "option_text": "Leave your contact info in case the owner returns",
                "trait_tags": {"Admin-Skill": 1.0, "Conventional": 0.45, "Finance-Acct": 0.3, "Hospitality-Svc": 0.2}
            },
            {
                "option_id": 1148,
                "option_text": "Think about creating a lost-and-found system",
                "trait_tags": {"Community-Serve": 1.0, "Social": 0.45, "People-Skill": 0.4, "Teaching-Ed": 0.25, "Patient-Care": 0.2, "Law-Enforce": 0.15}
            },
            {
                "option_id": 1149,
                "option_text": "Consider the emotional impact on the person who lost it",
                "trait_tags": {"Rehab-Therapy": 1.0, "Physical-Skill": 0.4, "Social": 0.35, "People-Skill": 0.35, "Patient-Care": 0.3, "Teaching-Ed": 0.2}
            },
            {
                "option_id": 1150,
                "option_text": "Give it to the nearest establishment for safekeeping",
                "trait_tags": {"Hospitality-Svc": 1.0, "People-Skill": 0.45, "Tourism-Travel": 0.4, "Enterprising": 0.35, "Culinary-Arts": 0.3, "Marketing-Sales": 0.2}
            }
        ]
    },
    {
        "question_id": 116,
        "question_text": "A factory near your town is causing pollution. How would you address this?",
        "category": "Situational - Factory Pollution",
        "options": [
            {
                "option_id": 1151,
                "option_text": "Study the health effects on nearby residents",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 1152,
                "option_text": "Develop sensors to monitor pollution levels",
                "trait_tags": {"Hardware-Systems": 1.0, "Technical-Skill": 0.45, "Realistic": 0.4, "Electrical-Power": 0.3, "Mechanical-Design": 0.25, "Software-Dev": 0.2}
            },
            {
                "option_id": 1153,
                "option_text": "Design better waste management systems for the factory",
                "trait_tags": {"Industrial-Ops": 1.0, "Analytical-Skill": 0.35, "Enterprising": 0.3, "Mechanical-Design": 0.25, "Admin-Skill": 0.2, "Finance-Acct": 0.15}
            },
            {
                "option_id": 1154,
                "option_text": "Calculate the economic impact of the pollution",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 1155,
                "option_text": "Create documentary or media content about the issue",
                "trait_tags": {"Digital-Media": 1.0, "Artistic": 0.4, "Creative-Skill": 0.4, "Visual-Design": 0.3, "Software-Dev": 0.2, "Technical-Skill": 0.2}
            },
            {
                "option_id": 1156,
                "option_text": "Educate the community about their rights",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 1157,
                "option_text": "File legal complaints and gather evidence",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 1158,
                "option_text": "Conduct scientific tests on water and air quality",
                "trait_tags": {"Lab-Research": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Medical-Lab": 0.3, "Field-Research": 0.25, "Data-Analytics": 0.25}
            },
            {
                "option_id": 1159,
                "option_text": "Organize community protests and advocacy",
                "trait_tags": {"Community-Serve": 1.0, "Social": 0.45, "People-Skill": 0.4, "Teaching-Ed": 0.25, "Patient-Care": 0.2, "Law-Enforce": 0.15}
            },
            {
                "option_id": 1160,
                "option_text": "Study the environmental damage to local ecosystems",
                "trait_tags": {"Field-Research": 1.0, "Investigative": 0.4, "Agri-Nature": 0.3, "Analytical-Skill": 0.3, "Physical-Skill": 0.25, "Lab-Research": 0.25}
            }
        ]
    },
    {
        "question_id": 117,
        "question_text": "Your classmate is struggling financially and can't afford school supplies. How do you help?",
        "category": "Situational - Helping Classmate",
        "options": [
            {
                "option_id": 1161,
                "option_text": "Share your supplies and offer emotional support",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 1162,
                "option_text": "Help them find online resources and free materials",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 1163,
                "option_text": "Organize a donation drive at school",
                "trait_tags": {"Community-Serve": 1.0, "Social": 0.45, "People-Skill": 0.4, "Teaching-Ed": 0.25, "Patient-Care": 0.2, "Law-Enforce": 0.15}
            },
            {
                "option_id": 1164,
                "option_text": "Help them budget and manage their money better",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 1165,
                "option_text": "Create study materials they can use for free",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            },
            {
                "option_id": 1166,
                "option_text": "Tutor them so they can succeed without expensive materials",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 1167,
                "option_text": "Connect them with school assistance programs",
                "trait_tags": {"Admin-Skill": 1.0, "Conventional": 0.45, "Finance-Acct": 0.3, "Hospitality-Svc": 0.2}
            },
            {
                "option_id": 1168,
                "option_text": "Help them find a part-time job opportunity",
                "trait_tags": {"Startup-Venture": 1.0, "Enterprising": 0.45, "People-Skill": 0.3, "Marketing-Sales": 0.3, "Finance-Acct": 0.2, "Creative-Skill": 0.2}
            },
            {
                "option_id": 1169,
                "option_text": "Advocate to school for more student financial aid",
                "trait_tags": {"People-Skill": 1.0, "Social": 0.45, "Patient-Care": 0.4, "Teaching-Ed": 0.4, "Hospitality-Svc": 0.4, "Enterprising": 0.3}
            },
            {
                "option_id": 1170,
                "option_text": "Research scholarship opportunities for them",
                "trait_tags": {"Lab-Research": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Medical-Lab": 0.3, "Field-Research": 0.25, "Data-Analytics": 0.25}
            }
        ]
    },
    {
        "question_id": 118,
        "question_text": "You're asked to plan your family reunion. What aspect would you focus on?",
        "category": "Situational - Family Reunion",
        "options": [
            {
                "option_id": 1171,
                "option_text": "Ensure everyone's health needs are accommodated",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 1172,
                "option_text": "Create a digital invitation and photo slideshow",
                "trait_tags": {"Digital-Media": 1.0, "Artistic": 0.4, "Creative-Skill": 0.4, "Visual-Design": 0.3, "Software-Dev": 0.2, "Technical-Skill": 0.2}
            },
            {
                "option_id": 1173,
                "option_text": "Choose and set up the perfect venue",
                "trait_tags": {"Spatial-Design": 1.0, "Artistic": 0.35, "Creative-Skill": 0.35, "Civil-Build": 0.25, "Visual-Design": 0.25, "Technical-Skill": 0.2}
            },
            {
                "option_id": 1174,
                "option_text": "Manage the budget and collect contributions",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 1175,
                "option_text": "Design decorations and create a festive atmosphere",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            },
            {
                "option_id": 1176,
                "option_text": "Plan educational activities and games for kids",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 1177,
                "option_text": "Organize the program flow and event timeline",
                "trait_tags": {"Admin-Skill": 1.0, "Conventional": 0.45, "Finance-Acct": 0.3, "Hospitality-Svc": 0.2}
            },
            {
                "option_id": 1178,
                "option_text": "Plan the food menu and catering",
                "trait_tags": {"Hospitality-Svc": 1.0, "People-Skill": 0.45, "Tourism-Travel": 0.4, "Enterprising": 0.35, "Culinary-Arts": 0.3, "Marketing-Sales": 0.2}
            },
            {
                "option_id": 1179,
                "option_text": "Document family history and create a family tree",
                "trait_tags": {"Lab-Research": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Medical-Lab": 0.3, "Field-Research": 0.25, "Data-Analytics": 0.25}
            },
            {
                "option_id": 1180,
                "option_text": "Handle transportation and logistics",
                "trait_tags": {"Industrial-Ops": 1.0, "Analytical-Skill": 0.35, "Enterprising": 0.3, "Mechanical-Design": 0.25, "Admin-Skill": 0.2, "Finance-Acct": 0.15}
            }
        ]
    },
    {
        "question_id": 119,
        "question_text": "Your town is experiencing a water shortage. What solution would you propose?",
        "category": "Situational - Water Shortage",
        "options": [
            {
                "option_id": 1181,
                "option_text": "Ensure clean drinking water reaches vulnerable people first",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 1182,
                "option_text": "Develop a water tracking and distribution app",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 1183,
                "option_text": "Design rainwater collection and storage systems",
                "trait_tags": {"Civil-Build": 1.0, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Mechanical-Design": 0.2, "Industrial-Ops": 0.15}
            },
            {
                "option_id": 1184,
                "option_text": "Calculate costs of different water solutions",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 1185,
                "option_text": "Create awareness campaigns about water conservation",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            },
            {
                "option_id": 1186,
                "option_text": "Teach people how to conserve and recycle water",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 1187,
                "option_text": "Research new water purification technologies",
                "trait_tags": {"Lab-Research": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Medical-Lab": 0.3, "Field-Research": 0.25, "Data-Analytics": 0.25}
            },
            {
                "option_id": 1188,
                "option_text": "Coordinate with government for emergency water supply",
                "trait_tags": {"Community-Serve": 1.0, "Social": 0.45, "People-Skill": 0.4, "Teaching-Ed": 0.25, "Patient-Care": 0.2, "Law-Enforce": 0.15}
            },
            {
                "option_id": 1189,
                "option_text": "Study sustainable agricultural water practices",
                "trait_tags": {"Agri-Nature": 1.0, "Realistic": 0.45, "Physical-Skill": 0.35, "Field-Research": 0.25, "Lab-Research": 0.15}
            },
            {
                "option_id": 1190,
                "option_text": "Design efficient water pumping systems",
                "trait_tags": {"Mechanical-Design": 1.0, "Realistic": 0.45, "Technical-Skill": 0.4, "Industrial-Ops": 0.25, "Civil-Build": 0.2, "Electrical-Power": 0.2}
            }
        ]
    },
    {
        "question_id": 120,
        "question_text": "You have the opportunity to intern anywhere for a month. Where would you go?",
        "category": "Situational - Dream Internship",
        "options": [
            {
                "option_id": 1191,
                "option_text": "A major hospital or healthcare facility",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 1192,
                "option_text": "A tech startup or software company",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 1193,
                "option_text": "A construction company or architecture firm",
                "trait_tags": {"Spatial-Design": 1.0, "Artistic": 0.35, "Creative-Skill": 0.35, "Civil-Build": 0.25, "Visual-Design": 0.25, "Technical-Skill": 0.2}
            },
            {
                "option_id": 1194,
                "option_text": "An investment bank or financial institution",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Startup-Venture": 0.2, "Marketing-Sales": 0.15}
            },
            {
                "option_id": 1195,
                "option_text": "A film studio or creative agency",
                "trait_tags": {"Digital-Media": 1.0, "Artistic": 0.4, "Creative-Skill": 0.4, "Visual-Design": 0.3, "Software-Dev": 0.2, "Technical-Skill": 0.2}
            },
            {
                "option_id": 1196,
                "option_text": "A school or educational organization",
                "trait_tags": {"Teaching-Ed": 1.0, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Patient-Care": 0.15, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 1197,
                "option_text": "A law firm or government agency",
                "trait_tags": {"Law-Enforce": 1.0, "Realistic": 0.35, "Physical-Skill": 0.35, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 1198,
                "option_text": "A research laboratory or university",
                "trait_tags": {"Lab-Research": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.45, "Medical-Lab": 0.3, "Field-Research": 0.25, "Data-Analytics": 0.25}
            },
            {
                "option_id": 1199,
                "option_text": "A shipping company or port authority",
                "trait_tags": {"Maritime-Sea": 1.0, "Realistic": 0.45, "Physical-Skill": 0.4, "Technical-Skill": 0.25, "Mechanical-Design": 0.15}
            },
            {
                "option_id": 1200,
                "option_text": "A resort, hotel, or travel company",
                "trait_tags": {"Hospitality-Svc": 1.0, "People-Skill": 0.45, "Tourism-Travel": 0.4, "Enterprising": 0.35, "Culinary-Arts": 0.3, "Marketing-Sales": 0.2}
            }
        ]
    },
    {
        "question_id": 121,
        "question_text": "When you use your computer or phone, what do you enjoy doing the most?",
        "category": "Domain Entry - Technology",
        "options": [
            {
                "option_id": 1201,
                "option_text": "Building websites or coding small programs",
                "trait_tags": {"Web-Dev": 1.0, "Software-Dev": 0.8, "Technical-Skill": 0.45, "Investigative": 0.35, "Mobile-Dev": 0.3, "Digital-Media": 0.25}
            },
            {
                "option_id": 1202,
                "option_text": "Playing and analyzing video games",
                "trait_tags": {"Game-Dev": 1.0, "Digital-Media": 0.8, "Technical-Skill": 0.4, "Software-Dev": 0.4, "Creative-Skill": 0.35, "Animation-3D": 0.35}
            },
            {
                "option_id": 1203,
                "option_text": "Setting up networks or fixing hardware issues",
                "trait_tags": {"Cloud-Systems": 1.0, "Hardware-Systems": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.35, "Realistic": 0.32, "Investigative": 0.3}
            },
            {
                "option_id": 1204,
                "option_text": "Analyzing data or making spreadsheets",
                "trait_tags": {"Data-Analytics": 1.0, "AI-ML": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Software-Dev": 0.3, "Lab-Research": 0.25}
            },
            {
                "option_id": 1205,
                "option_text": "Creating digital art or editing videos",
                "trait_tags": {"Digital-Media": 1.0, "Animation-3D": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Visual-Design": 0.3, "Game-Dev": 0.28}
            },
            {
                "option_id": 1206,
                "option_text": "Learning about hacking and online security",
                "trait_tags": {"Cyber-Defense": 1.0, "Software-Dev": 0.8, "Technical-Skill": 0.4, "Investigative": 0.35, "Data-Analytics": 0.24, "Hardware-Systems": 0.16}
            },
            {
                "option_id": 1207,
                "option_text": "Developing mobile apps or chatbots",
                "trait_tags": {"Mobile-Dev": 1.0, "AI-ML": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Investigative": 0.36, "Analytical-Skill": 0.36}
            },
            {
                "option_id": 1208,
                "option_text": "Managing cloud servers or databases",
                "trait_tags": {"Cloud-Systems": 1.0, "Data-Analytics": 0.8, "Technical-Skill": 0.45, "Investigative": 0.36, "Analytical-Skill": 0.36, "Software-Dev": 0.35}
            },
            {
                "option_id": 1209,
                "option_text": "Automating tasks with scripts",
                "trait_tags": {"Software-Dev": 1.0, "Data-Analytics": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Analytical-Skill": 0.36, "Cyber-Defense": 0.25}
            },
            {
                "option_id": 1210,
                "option_text": "None of these interest me",
                "trait_tags": {}
            }
        ]
    },
    {
        "question_id": 122,
        "question_text": "In a hospital setting, what would you most want to do?",
        "category": "Domain Entry - Healthcare",
        "options": [
            {
                "option_id": 1211,
                "option_text": "Directly care for patients at their bedside",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.8, "Social": 0.4, "Teaching-Ed": 0.32, "Hospitality-Svc": 0.32, "Rehab-Therapy": 0.3}
            },
            {
                "option_id": 1212,
                "option_text": "Analyze blood and tissue samples in the lab",
                "trait_tags": {"Medical-Lab": 1.0, "Lab-Research": 0.8, "Analytical-Skill": 0.45, "Investigative": 0.4, "Technical-Skill": 0.25, "Patient-Care": 0.2}
            },
            {
                "option_id": 1213,
                "option_text": "Help patients recover through physical exercises",
                "trait_tags": {"Rehab-Therapy": 1.0, "Physical-Skill": 0.8, "Social": 0.35, "People-Skill": 0.35, "Realistic": 0.32, "Patient-Care": 0.3}
            },
            {
                "option_id": 1214,
                "option_text": "Prepare and dispense medications",
                "trait_tags": {"Pharmacy": 1.0, "Medical-Lab": 0.8, "Investigative": 0.4, "Analytical-Skill": 0.4, "Lab-Research": 0.28, "Patient-Care": 0.25}
            },
            {
                "option_id": 1215,
                "option_text": "Manage hospital records and health data",
                "trait_tags": {"Health-Admin": 1.0, "Admin-Skill": 0.8, "Conventional": 0.4, "Finance-Acct": 0.24, "Hospitality-Svc": 0.16, "Patient-Care": 0.15}
            },
            {
                "option_id": 1216,
                "option_text": "Promote health programs for communities",
                "trait_tags": {"Public-Health": 1.0, "Community-Serve": 0.8, "Social": 0.4, "Analytical-Skill": 0.35, "People-Skill": 0.32, "Patient-Care": 0.25}
            },
            {
                "option_id": 1217,
                "option_text": "Plan nutritious diets for patients",
                "trait_tags": {"Nutrition-Diet": 1.0, "Patient-Care": 0.8, "People-Skill": 0.36, "Food-Science": 0.35, "Social": 0.32, "Analytical-Skill": 0.3}
            },
            {
                "option_id": 1218,
                "option_text": "Help people with speech or mental health issues",
                "trait_tags": {"Rehab-Therapy": 1.0, "Counseling": 0.8, "Physical-Skill": 0.4, "Social": 0.36, "People-Skill": 0.36, "Patient-Care": 0.3}
            },
            {
                "option_id": 1219,
                "option_text": "Operate medical imaging equipment (X-ray, MRI)",
                "trait_tags": {"Medical-Lab": 1.0, "Technical-Skill": 0.8, "Analytical-Skill": 0.45, "Investigative": 0.4, "Lab-Research": 0.35, "Software-Dev": 0.32}
            },
            {
                "option_id": 1220,
                "option_text": "None of these interest me",
                "trait_tags": {}
            }
        ]
    },
    {
        "question_id": 123,
        "question_text": "When you see a construction site or factory, what interests you most?",
        "category": "Domain Entry - Engineering",
        "options": [
            {
                "option_id": 1221,
                "option_text": "How buildings and bridges are designed to be strong",
                "trait_tags": {"Civil-Build": 1.0, "Spatial-Design": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Artistic": 0.28, "Creative-Skill": 0.28}
            },
            {
                "option_id": 1222,
                "option_text": "The machines and engines that power everything",
                "trait_tags": {"Mechanical-Design": 1.0, "Industrial-Ops": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Analytical-Skill": 0.28, "Enterprising": 0.24}
            },
            {
                "option_id": 1223,
                "option_text": "The electrical systems and power grids",
                "trait_tags": {"Electrical-Power": 1.0, "Hardware-Systems": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Mechanical-Design": 0.2, "Industrial-Ops": 0.2}
            },
            {
                "option_id": 1224,
                "option_text": "How factories optimize their production process",
                "trait_tags": {"Industrial-Ops": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.36, "Analytical-Skill": 0.35, "Technical-Skill": 0.32, "Enterprising": 0.3}
            },
            {
                "option_id": 1225,
                "option_text": "The environmental impact and sustainability",
                "trait_tags": {"Environmental-Eng": 1.0, "Environmental-Sci": 0.8, "Realistic": 0.4, "Investigative": 0.36, "Technical-Skill": 0.35, "Field-Research": 0.32}
            },
            {
                "option_id": 1226,
                "option_text": "The mapping and surveying of the land",
                "trait_tags": {"Civil-Build": 1.0, "Field-Research": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Investigative": 0.32, "Spatial-Design": 0.25}
            },
            {
                "option_id": 1227,
                "option_text": "The architecture and visual design of the buildings",
                "trait_tags": {"Spatial-Design": 1.0, "Visual-Design": 0.8, "Artistic": 0.36, "Creative-Skill": 0.36, "Civil-Build": 0.25, "Digital-Media": 0.24}
            },
            {
                "option_id": 1228,
                "option_text": "How aircraft and vehicles are engineered",
                "trait_tags": {"Mechanical-Design": 1.0, "Hardware-Systems": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Industrial-Ops": 0.25, "Electrical-Power": 0.24}
            },
            {
                "option_id": 1229,
                "option_text": "The electronics and embedded computer systems",
                "trait_tags": {"Hardware-Systems": 1.0, "Software-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Investigative": 0.32, "Electrical-Power": 0.3}
            },
            {
                "option_id": 1230,
                "option_text": "None of these interest me",
                "trait_tags": {}
            }
        ]
    },
    {
        "question_id": 124,
        "question_text": "When you think about money and business, what excites you most?",
        "category": "Domain Entry - Business",
        "options": [
            {
                "option_id": 1231,
                "option_text": "Managing budgets and analyzing financial reports",
                "trait_tags": {"Finance-Acct": 1.0, "Analytical-Skill": 0.8, "Conventional": 0.45, "Investigative": 0.36, "Data-Analytics": 0.32, "Admin-Skill": 0.3}
            },
            {
                "option_id": 1232,
                "option_text": "Creating ads and marketing campaigns",
                "trait_tags": {"Marketing-Sales": 1.0, "Creative-Skill": 0.8, "Enterprising": 0.45, "People-Skill": 0.4, "Artistic": 0.36, "Visual-Design": 0.32}
            },
            {
                "option_id": 1233,
                "option_text": "Starting my own business from scratch",
                "trait_tags": {"Startup-Venture": 1.0, "Marketing-Sales": 0.8, "Enterprising": 0.45, "People-Skill": 0.32, "Finance-Acct": 0.2, "Creative-Skill": 0.2}
            },
            {
                "option_id": 1234,
                "option_text": "Hiring and managing employees",
                "trait_tags": {"HR-Management": 1.0, "People-Skill": 0.8, "Social": 0.36, "Enterprising": 0.35, "Admin-Skill": 0.35, "Teaching-Ed": 0.32}
            },
            {
                "option_id": 1235,
                "option_text": "Trading stocks and making investments",
                "trait_tags": {"Finance-Acct": 1.0, "Startup-Venture": 0.8, "Conventional": 0.45, "Analytical-Skill": 0.4, "Enterprising": 0.36, "Admin-Skill": 0.3}
            },
            {
                "option_id": 1236,
                "option_text": "Selling products and negotiating deals",
                "trait_tags": {"Marketing-Sales": 1.0, "People-Skill": 0.8, "Enterprising": 0.45, "Social": 0.36, "Hospitality-Svc": 0.32, "Teaching-Ed": 0.32}
            },
            {
                "option_id": 1237,
                "option_text": "Managing real estate properties",
                "trait_tags": {"Marketing-Sales": 1.0, "Admin-Skill": 0.8, "Enterprising": 0.45, "People-Skill": 0.4, "Conventional": 0.36, "Startup-Venture": 0.3}
            },
            {
                "option_id": 1238,
                "option_text": "Running logistics and supply chains",
                "trait_tags": {"Industrial-Ops": 1.0, "Admin-Skill": 0.8, "Conventional": 0.36, "Analytical-Skill": 0.35, "Enterprising": 0.3, "Mechanical-Design": 0.25}
            },
            {
                "option_id": 1239,
                "option_text": "Analyzing economic trends and policies",
                "trait_tags": {"Finance-Acct": 1.0, "Analytical-Skill": 0.8, "Conventional": 0.45, "Investigative": 0.36, "Data-Analytics": 0.32, "Admin-Skill": 0.3}
            },
            {
                "option_id": 1240,
                "option_text": "None of these interest me",
                "trait_tags": {}
            }
        ]
    },
    {
        "question_id": 125,
        "question_text": "Which form of creative expression speaks to you the most?",
        "category": "Domain Entry - Creative",
        "options": [
            {
                "option_id": 1241,
                "option_text": "Drawing, painting, or graphic design",
                "trait_tags": {"Visual-Design": 1.0, "Creative-Skill": 0.8, "Artistic": 0.45, "Digital-Media": 0.32, "Spatial-Design": 0.28}
            },
            {
                "option_id": 1242,
                "option_text": "3D modeling and animation",
                "trait_tags": {"Animation-3D": 1.0, "Digital-Media": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Game-Dev": 0.35, "Visual-Design": 0.3}
            },
            {
                "option_id": 1243,
                "option_text": "Making short films or video content",
                "trait_tags": {"Film-Broadcast": 1.0, "Digital-Media": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Visual-Design": 0.25, "Technical-Skill": 0.2}
            },
            {
                "option_id": 1244,
                "option_text": "Acting, dancing, or performing on stage",
                "trait_tags": {"Performing-Arts": 1.0, "People-Skill": 0.8, "Artistic": 0.45, "Creative-Skill": 0.45, "Social": 0.36, "Teaching-Ed": 0.32}
            },
            {
                "option_id": 1245,
                "option_text": "Music production and sound design",
                "trait_tags": {"Performing-Arts": 1.0, "Digital-Media": 0.8, "Artistic": 0.45, "Creative-Skill": 0.45, "People-Skill": 0.3, "Film-Broadcast": 0.25}
            },
            {
                "option_id": 1246,
                "option_text": "Interior decorating or space design",
                "trait_tags": {"Spatial-Design": 1.0, "Creative-Skill": 0.8, "Artistic": 0.36, "Visual-Design": 0.32, "Digital-Media": 0.32, "Civil-Build": 0.25}
            },
            {
                "option_id": 1247,
                "option_text": "Fashion design and clothing",
                "trait_tags": {"Spatial-Design": 1.0, "Visual-Design": 0.8, "Artistic": 0.36, "Creative-Skill": 0.36, "Civil-Build": 0.25, "Digital-Media": 0.24}
            },
            {
                "option_id": 1248,
                "option_text": "Photography and visual storytelling",
                "trait_tags": {"Visual-Design": 1.0, "Film-Broadcast": 0.8, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.32, "Spatial-Design": 0.25}
            },
            {
                "option_id": 1249,
                "option_text": "Game design and interactive media",
                "trait_tags": {"Game-Dev": 1.0, "Animation-3D": 0.8, "Technical-Skill": 0.4, "Software-Dev": 0.4, "Creative-Skill": 0.35, "Artistic": 0.32}
            },
            {
                "option_id": 1250,
                "option_text": "None of these interest me",
                "trait_tags": {}
            }
        ]
    },
    {
        "question_id": 126,
        "question_text": "What draws you most to sharing knowledge with others?",
        "category": "Domain Entry - Education",
        "options": [
            {
                "option_id": 1251,
                "option_text": "Teaching young children how to read and write",
                "trait_tags": {"Teaching-Ed": 1.0, "People-Skill": 0.8, "Social": 0.45, "Patient-Care": 0.32, "Hospitality-Svc": 0.32, "Community-Serve": 0.25}
            },
            {
                "option_id": 1252,
                "option_text": "Coaching students through difficult subjects",
                "trait_tags": {"Teaching-Ed": 1.0, "Analytical-Skill": 0.8, "Social": 0.45, "People-Skill": 0.45, "Investigative": 0.36, "Lab-Research": 0.28}
            },
            {
                "option_id": 1253,
                "option_text": "Guiding students with personal and career problems",
                "trait_tags": {"Counseling": 1.0, "People-Skill": 0.8, "Social": 0.45, "Teaching-Ed": 0.32, "Patient-Care": 0.32, "Hospitality-Svc": 0.32}
            },
            {
                "option_id": 1254,
                "option_text": "Training athletes and coaching sports teams",
                "trait_tags": {"Sports-Ed": 1.0, "Physical-Skill": 0.8, "Social": 0.35, "Teaching-Ed": 0.35, "Realistic": 0.32, "Maritime-Sea": 0.28}
            },
            {
                "option_id": 1255,
                "option_text": "Teaching technical and vocational skills",
                "trait_tags": {"Teaching-Ed": 1.0, "Technical-Skill": 0.8, "Social": 0.45, "People-Skill": 0.45, "Realistic": 0.28, "Community-Serve": 0.25}
            },
            {
                "option_id": 1256,
                "option_text": "Helping special needs children learn",
                "trait_tags": {"Teaching-Ed": 1.0, "Counseling": 0.8, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Rehab-Therapy": 0.2}
            },
            {
                "option_id": 1257,
                "option_text": "Organizing library resources and research tools",
                "trait_tags": {"Teaching-Ed": 1.0, "Admin-Skill": 0.8, "Social": 0.45, "People-Skill": 0.45, "Conventional": 0.36, "Health-Admin": 0.28}
            },
            {
                "option_id": 1258,
                "option_text": "Developing educational programs and curricula",
                "trait_tags": {"Teaching-Ed": 1.0, "Creative-Skill": 0.8, "Social": 0.45, "People-Skill": 0.45, "Artistic": 0.36, "Visual-Design": 0.32}
            },
            {
                "option_id": 1259,
                "option_text": "Mentoring youth in the community",
                "trait_tags": {"Community-Serve": 1.0, "People-Skill": 0.8, "Social": 0.45, "Teaching-Ed": 0.32, "Patient-Care": 0.32, "Enterprising": 0.24}
            },
            {
                "option_id": 1260,
                "option_text": "None of these interest me",
                "trait_tags": {}
            }
        ]
    },
    {
        "question_id": 127,
        "question_text": "How would you most like to serve your community?",
        "category": "Domain Entry - Public Service",
        "options": [
            {
                "option_id": 1261,
                "option_text": "Protecting people as a police officer or detective",
                "trait_tags": {"Law-Enforce": 1.0, "Physical-Skill": 0.8, "Realistic": 0.35, "Rehab-Therapy": 0.24, "Community-Serve": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 1262,
                "option_text": "Fighting for justice as a lawyer",
                "trait_tags": {"Legal-Practice": 1.0, "Analytical-Skill": 0.8, "Investigative": 0.36, "Enterprising": 0.35, "Data-Analytics": 0.32, "People-Skill": 0.3}
            },
            {
                "option_id": 1263,
                "option_text": "Analyzing forensic evidence at crime scenes",
                "trait_tags": {"Forensic-Sci": 1.0, "Lab-Research": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.4, "Law-Enforce": 0.35, "Medical-Lab": 0.24}
            },
            {
                "option_id": 1264,
                "option_text": "Helping families through social work",
                "trait_tags": {"Social-Work": 1.0, "People-Skill": 0.8, "Social": 0.45, "Community-Serve": 0.4, "Teaching-Ed": 0.32, "Patient-Care": 0.32}
            },
            {
                "option_id": 1265,
                "option_text": "Working in government to create public policy",
                "trait_tags": {"Community-Serve": 1.0, "Admin-Skill": 0.8, "Social": 0.45, "People-Skill": 0.4, "Conventional": 0.36, "Health-Admin": 0.28}
            },
            {
                "option_id": 1266,
                "option_text": "Organizing community development programs",
                "trait_tags": {"Community-Serve": 1.0, "Social-Work": 0.8, "Social": 0.45, "People-Skill": 0.4, "Teaching-Ed": 0.25, "Counseling": 0.24}
            },
            {
                "option_id": 1267,
                "option_text": "Advocating for human rights and social justice",
                "trait_tags": {"Legal-Practice": 1.0, "Community-Serve": 0.8, "Social": 0.36, "Enterprising": 0.35, "Analytical-Skill": 0.35, "People-Skill": 0.32}
            },
            {
                "option_id": 1268,
                "option_text": "Serving as a diplomat or in international relations",
                "trait_tags": {"Community-Serve": 1.0, "People-Skill": 0.8, "Social": 0.45, "Teaching-Ed": 0.32, "Patient-Care": 0.32, "Enterprising": 0.24}
            },
            {
                "option_id": 1269,
                "option_text": "Managing disaster relief and emergency response",
                "trait_tags": {"Community-Serve": 1.0, "Physical-Skill": 0.8, "Social": 0.45, "People-Skill": 0.4, "Realistic": 0.32, "Teaching-Ed": 0.25}
            },
            {
                "option_id": 1270,
                "option_text": "None of these interest me",
                "trait_tags": {}
            }
        ]
    },
    {
        "question_id": 128,
        "question_text": "What kind of scientific discovery excites you the most?",
        "category": "Domain Entry - Science",
        "options": [
            {
                "option_id": 1271,
                "option_text": "Finding a cure for diseases in a laboratory",
                "trait_tags": {"Lab-Research": 1.0, "Medical-Lab": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Field-Research": 0.25, "Data-Analytics": 0.25}
            },
            {
                "option_id": 1272,
                "option_text": "Discovering new species in the wild",
                "trait_tags": {"Field-Research": 1.0, "Environmental-Sci": 0.8, "Investigative": 0.4, "Agri-Nature": 0.3, "Analytical-Skill": 0.3, "Physical-Skill": 0.25}
            },
            {
                "option_id": 1273,
                "option_text": "Developing new food products and preserving food safely",
                "trait_tags": {"Food-Science": 1.0, "Lab-Research": 0.8, "Investigative": 0.4, "Analytical-Skill": 0.36, "Nutrition-Diet": 0.35, "Medical-Lab": 0.24}
            },
            {
                "option_id": 1274,
                "option_text": "Analyzing crime scene evidence in a lab",
                "trait_tags": {"Forensic-Sci": 1.0, "Analytical-Skill": 0.8, "Investigative": 0.45, "Lab-Research": 0.35, "Law-Enforce": 0.35, "Data-Analytics": 0.32}
            },
            {
                "option_id": 1275,
                "option_text": "Studying climate change and protecting the environment",
                "trait_tags": {"Environmental-Sci": 1.0, "Field-Research": 0.8, "Investigative": 0.45, "Environmental-Eng": 0.3, "Lab-Research": 0.25, "Agri-Nature": 0.25}
            },
            {
                "option_id": 1276,
                "option_text": "Exploring the ocean floor and marine life",
                "trait_tags": {"Field-Research": 1.0, "Physical-Skill": 0.8, "Investigative": 0.4, "Realistic": 0.32, "Agri-Nature": 0.3, "Analytical-Skill": 0.3}
            },
            {
                "option_id": 1277,
                "option_text": "Inventing new materials through chemistry",
                "trait_tags": {"Lab-Research": 1.0, "Analytical-Skill": 0.8, "Investigative": 0.45, "Data-Analytics": 0.32, "Medical-Lab": 0.3, "Field-Research": 0.25}
            },
            {
                "option_id": 1278,
                "option_text": "Understanding the universe through physics",
                "trait_tags": {"Lab-Research": 1.0, "Analytical-Skill": 0.8, "Investigative": 0.45, "Data-Analytics": 0.32, "Medical-Lab": 0.3, "Field-Research": 0.25}
            },
            {
                "option_id": 1279,
                "option_text": "Using statistics and math to solve real-world problems",
                "trait_tags": {"Data-Analytics": 1.0, "Analytical-Skill": 0.8, "Investigative": 0.45, "Software-Dev": 0.3, "Lab-Research": 0.28, "Finance-Acct": 0.28}
            },
            {
                "option_id": 1280,
                "option_text": "None of these interest me",
                "trait_tags": {}
            }
        ]
    },
    {
        "question_id": 129,
        "question_text": "What aspect of nature and farming interests you most?",
        "category": "Domain Entry - Agriculture",
        "options": [
            {
                "option_id": 1281,
                "option_text": "Growing crops and managing farmland",
                "trait_tags": {"Agri-Nature": 1.0, "Physical-Skill": 0.8, "Realistic": 0.45, "Field-Research": 0.25, "Law-Enforce": 0.24, "Lab-Research": 0.15}
            },
            {
                "option_id": 1282,
                "option_text": "Raising animals and livestock",
                "trait_tags": {"Agri-Nature": 1.0, "Field-Research": 0.8, "Realistic": 0.45, "Physical-Skill": 0.35, "Investigative": 0.32, "Analytical-Skill": 0.24}
            },
            {
                "option_id": 1283,
                "option_text": "Protecting forests and natural resources",
                "trait_tags": {"Agri-Nature": 1.0, "Environmental-Sci": 0.8, "Realistic": 0.45, "Investigative": 0.36, "Physical-Skill": 0.35, "Field-Research": 0.32}
            },
            {
                "option_id": 1284,
                "option_text": "Fish farming and aquaculture",
                "trait_tags": {"Agri-Nature": 1.0, "Maritime-Sea": 0.8, "Realistic": 0.45, "Physical-Skill": 0.35, "Field-Research": 0.25, "Technical-Skill": 0.2}
            },
            {
                "option_id": 1285,
                "option_text": "Developing agricultural technology",
                "trait_tags": {"Agri-Nature": 1.0, "Technical-Skill": 0.8, "Realistic": 0.45, "Physical-Skill": 0.35, "Mechanical-Design": 0.28, "Field-Research": 0.25}
            },
            {
                "option_id": 1286,
                "option_text": "Soil science and land management",
                "trait_tags": {"Agri-Nature": 1.0, "Lab-Research": 0.8, "Realistic": 0.45, "Investigative": 0.36, "Analytical-Skill": 0.36, "Physical-Skill": 0.35}
            },
            {
                "option_id": 1287,
                "option_text": "Agricultural business and farm marketing",
                "trait_tags": {"Agri-Nature": 1.0, "Startup-Venture": 0.8, "Realistic": 0.45, "Enterprising": 0.36, "Physical-Skill": 0.35, "Field-Research": 0.25}
            },
            {
                "option_id": 1288,
                "option_text": "Studying plant genetics and breeding",
                "trait_tags": {"Agri-Nature": 1.0, "Lab-Research": 0.8, "Realistic": 0.45, "Investigative": 0.36, "Analytical-Skill": 0.36, "Physical-Skill": 0.35}
            },
            {
                "option_id": 1289,
                "option_text": "None of these interest me",
                "trait_tags": {}
            }
        ]
    },
    {
        "question_id": 130,
        "question_text": "What draws you to the sea and maritime industry?",
        "category": "Domain Entry - Maritime",
        "options": [
            {
                "option_id": 1291,
                "option_text": "Navigating ships across the ocean",
                "trait_tags": {"Maritime-Sea": 1.0, "Physical-Skill": 0.8, "Realistic": 0.45, "Agri-Nature": 0.28, "Technical-Skill": 0.25, "Law-Enforce": 0.24}
            },
            {
                "option_id": 1292,
                "option_text": "Maintaining and repairing ship engines",
                "trait_tags": {"Maritime-Sea": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.45, "Physical-Skill": 0.4, "Technical-Skill": 0.32, "Industrial-Ops": 0.2}
            },
            {
                "option_id": 1293,
                "option_text": "Working at a seaport managing cargo",
                "trait_tags": {"Maritime-Sea": 1.0, "Admin-Skill": 0.8, "Realistic": 0.45, "Physical-Skill": 0.4, "Conventional": 0.36, "Technical-Skill": 0.25}
            },
            {
                "option_id": 1294,
                "option_text": "Studying marine ecosystems and biology",
                "trait_tags": {"Field-Research": 1.0, "Environmental-Sci": 0.8, "Investigative": 0.4, "Agri-Nature": 0.3, "Analytical-Skill": 0.3, "Physical-Skill": 0.25}
            },
            {
                "option_id": 1295,
                "option_text": "Building and designing ships or boats",
                "trait_tags": {"Maritime-Sea": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.45, "Physical-Skill": 0.4, "Technical-Skill": 0.32, "Industrial-Ops": 0.2}
            },
            {
                "option_id": 1296,
                "option_text": "The adventure of traveling to different countries",
                "trait_tags": {"Maritime-Sea": 1.0, "Tourism-Travel": 0.8, "Realistic": 0.45, "Physical-Skill": 0.4, "People-Skill": 0.32, "Hospitality-Svc": 0.32}
            },
            {
                "option_id": 1297,
                "option_text": "Fishing industry and aquatic resources",
                "trait_tags": {"Maritime-Sea": 1.0, "Agri-Nature": 0.8, "Realistic": 0.45, "Physical-Skill": 0.4, "Technical-Skill": 0.25, "Field-Research": 0.2}
            },
            {
                "option_id": 1298,
                "option_text": "None of these interest me",
                "trait_tags": {}
            }
        ]
    },
    {
        "question_id": 131,
        "question_text": "What do you enjoy most about serving and hosting people?",
        "category": "Domain Entry - Hospitality",
        "options": [
            {
                "option_id": 1301,
                "option_text": "Managing a hotel and making guests feel welcome",
                "trait_tags": {"Hospitality-Svc": 1.0, "People-Skill": 0.8, "Tourism-Travel": 0.4, "Social": 0.36, "Enterprising": 0.35, "Teaching-Ed": 0.32}
            },
            {
                "option_id": 1302,
                "option_text": "Planning travel itineraries and tour packages",
                "trait_tags": {"Tourism-Travel": 1.0, "Marketing-Sales": 0.8, "People-Skill": 0.4, "Hospitality-Svc": 0.4, "Enterprising": 0.36, "Startup-Venture": 0.24}
            },
            {
                "option_id": 1303,
                "option_text": "Cooking and creating new dishes",
                "trait_tags": {"Culinary-Arts": 1.0, "Creative-Skill": 0.8, "Artistic": 0.36, "Hospitality-Svc": 0.35, "Visual-Design": 0.32, "Digital-Media": 0.32}
            },
            {
                "option_id": 1304,
                "option_text": "Organizing events and conferences",
                "trait_tags": {"Hospitality-Svc": 1.0, "Admin-Skill": 0.8, "People-Skill": 0.45, "Tourism-Travel": 0.4, "Conventional": 0.36, "Enterprising": 0.35}
            },
            {
                "option_id": 1305,
                "option_text": "Running a restaurant or food business",
                "trait_tags": {"Culinary-Arts": 1.0, "Startup-Venture": 0.8, "Enterprising": 0.36, "Creative-Skill": 0.35, "Hospitality-Svc": 0.35, "Artistic": 0.3}
            },
            {
                "option_id": 1306,
                "option_text": "Being a tour guide and sharing culture",
                "trait_tags": {"Tourism-Travel": 1.0, "People-Skill": 0.8, "Hospitality-Svc": 0.4, "Social": 0.36, "Enterprising": 0.35, "Teaching-Ed": 0.32}
            },
            {
                "option_id": 1307,
                "option_text": "Managing a resort or spa",
                "trait_tags": {"Hospitality-Svc": 1.0, "Admin-Skill": 0.8, "People-Skill": 0.45, "Tourism-Travel": 0.4, "Conventional": 0.36, "Enterprising": 0.35}
            },
            {
                "option_id": 1308,
                "option_text": "Food photography and culinary content creation",
                "trait_tags": {"Culinary-Arts": 1.0, "Digital-Media": 0.8, "Creative-Skill": 0.35, "Hospitality-Svc": 0.35, "Artistic": 0.32, "Visual-Design": 0.24}
            },
            {
                "option_id": 1309,
                "option_text": "None of these interest me",
                "trait_tags": {}
            }
        ]
    },
    {
        "question_id": 132,
        "question_text": "What physical activity or career excites you most?",
        "category": "Domain Entry - Physical",
        "options": [
            {
                "option_id": 1311,
                "option_text": "Coaching athletes and training sports teams",
                "trait_tags": {"Sports-Ed": 1.0, "Teaching-Ed": 0.8, "Physical-Skill": 0.45, "Social": 0.36, "People-Skill": 0.36, "Rehab-Therapy": 0.2}
            },
            {
                "option_id": 1312,
                "option_text": "Helping injured athletes recover",
                "trait_tags": {"Rehab-Therapy": 1.0, "Sports-Ed": 0.8, "Physical-Skill": 0.4, "Social": 0.35, "People-Skill": 0.35, "Patient-Care": 0.3}
            },
            {
                "option_id": 1313,
                "option_text": "Working as a fitness trainer",
                "trait_tags": {"Physical-Skill": 1.0, "Sports-Ed": 0.8, "Realistic": 0.4, "Maritime-Sea": 0.35, "Agri-Nature": 0.35, "Law-Enforce": 0.3}
            },
            {
                "option_id": 1314,
                "option_text": "Becoming a professional athlete",
                "trait_tags": {"Physical-Skill": 1.0, "Sports-Ed": 0.8, "Realistic": 0.4, "Maritime-Sea": 0.35, "Agri-Nature": 0.35, "Law-Enforce": 0.3}
            },
            {
                "option_id": 1315,
                "option_text": "Sports management and event organizing",
                "trait_tags": {"Sports-Ed": 1.0, "Admin-Skill": 0.8, "Physical-Skill": 0.45, "Conventional": 0.36, "Social": 0.35, "Teaching-Ed": 0.35}
            },
            {
                "option_id": 1316,
                "option_text": "Outdoor adventure sports and recreation",
                "trait_tags": {"Physical-Skill": 1.0, "Tourism-Travel": 0.8, "Realistic": 0.4, "Maritime-Sea": 0.35, "Agri-Nature": 0.35, "People-Skill": 0.32}
            },
            {
                "option_id": 1317,
                "option_text": "Military or law enforcement fitness",
                "trait_tags": {"Physical-Skill": 1.0, "Law-Enforce": 0.8, "Realistic": 0.4, "Maritime-Sea": 0.35, "Agri-Nature": 0.35, "Rehab-Therapy": 0.3}
            },
            {
                "option_id": 1318,
                "option_text": "None of these interest me",
                "trait_tags": {}
            }
        ]
    },
    {
        "question_id": 133,
        "question_text": "How do you most enjoy connecting with and understanding people?",
        "category": "Domain Entry - Social",
        "options": [
            {
                "option_id": 1321,
                "option_text": "Counseling people through emotional problems",
                "trait_tags": {"Counseling": 1.0, "People-Skill": 0.8, "Social": 0.45, "Teaching-Ed": 0.32, "Patient-Care": 0.32, "Hospitality-Svc": 0.32}
            },
            {
                "option_id": 1322,
                "option_text": "Writing stories and creative content",
                "trait_tags": {"Creative-Skill": 1.0, "Film-Broadcast": 0.8, "Artistic": 0.45, "Visual-Design": 0.4, "Digital-Media": 0.4, "Spatial-Design": 0.35}
            },
            {
                "option_id": 1323,
                "option_text": "Studying how societies and cultures work",
                "trait_tags": {"Community-Serve": 1.0, "Analytical-Skill": 0.8, "Social": 0.45, "People-Skill": 0.4, "Investigative": 0.36, "Data-Analytics": 0.32}
            },
            {
                "option_id": 1324,
                "option_text": "Helping underprivileged communities",
                "trait_tags": {"Social-Work": 1.0, "Community-Serve": 0.8, "Social": 0.45, "People-Skill": 0.45, "Counseling": 0.3, "Teaching-Ed": 0.25}
            },
            {
                "option_id": 1325,
                "option_text": "Researching psychology and human behavior",
                "trait_tags": {"Counseling": 1.0, "Analytical-Skill": 0.8, "Social": 0.45, "People-Skill": 0.45, "Investigative": 0.36, "Teaching-Ed": 0.3}
            },
            {
                "option_id": 1326,
                "option_text": "News reporting and investigative journalism",
                "trait_tags": {"Film-Broadcast": 1.0, "Analytical-Skill": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Digital-Media": 0.4, "Investigative": 0.36}
            },
            {
                "option_id": 1327,
                "option_text": "Understanding languages and communication",
                "trait_tags": {"Teaching-Ed": 1.0, "People-Skill": 0.8, "Social": 0.45, "Patient-Care": 0.32, "Hospitality-Svc": 0.32, "Community-Serve": 0.25}
            },
            {
                "option_id": 1328,
                "option_text": "Political activism and civic engagement",
                "trait_tags": {"Community-Serve": 1.0, "Legal-Practice": 0.8, "Social": 0.45, "People-Skill": 0.4, "Enterprising": 0.28, "Analytical-Skill": 0.28}
            },
            {
                "option_id": 1329,
                "option_text": "None of these interest me",
                "trait_tags": {}
            }
        ]
    },
    {
        "question_id": 134,
        "question_text": "Your school asks you to build their new website. What excites you most about the project?",
        "category": "Situational - Web Development",
        "options": [
            {
                "option_id": 1341,
                "option_text": "Designing the visual layout and user interface",
                "trait_tags": {"Web-Dev": 1.0, "Visual-Design": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Creative-Skill": 0.36, "Artistic": 0.36}
            },
            {
                "option_id": 1342,
                "option_text": "Writing the backend code and database",
                "trait_tags": {"Web-Dev": 1.0, "Software-Dev": 0.8, "Technical-Skill": 0.45, "Investigative": 0.35, "Mobile-Dev": 0.3, "Digital-Media": 0.25}
            },
            {
                "option_id": 1343,
                "option_text": "Setting up the server and hosting",
                "trait_tags": {"Cloud-Systems": 1.0, "Web-Dev": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.36, "Investigative": 0.3, "Cyber-Defense": 0.3}
            },
            {
                "option_id": 1344,
                "option_text": "Making sure it's secure from hackers",
                "trait_tags": {"Cyber-Defense": 1.0, "Web-Dev": 0.8, "Technical-Skill": 0.4, "Software-Dev": 0.36, "Investigative": 0.35, "Mobile-Dev": 0.24}
            },
            {
                "option_id": 1345,
                "option_text": "Adding interactive features and animations",
                "trait_tags": {"Web-Dev": 1.0, "Animation-3D": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Investigative": 0.35, "Digital-Media": 0.32}
            },
            {
                "option_id": 1346,
                "option_text": "Testing it on different devices and browsers",
                "trait_tags": {"Mobile-Dev": 1.0, "Web-Dev": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Investigative": 0.35, "Game-Dev": 0.2}
            },
            {
                "option_id": 1347,
                "option_text": "Analyzing user data to improve the site",
                "trait_tags": {"Data-Analytics": 1.0, "Web-Dev": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Software-Dev": 0.36, "Technical-Skill": 0.36}
            },
            {
                "option_id": 1348,
                "option_text": "Managing the project team and timeline",
                "trait_tags": {"Admin-Skill": 1.0, "Software-Dev": 0.8, "Conventional": 0.45, "Technical-Skill": 0.36, "Investigative": 0.32, "Finance-Acct": 0.3}
            }
        ]
    },
    {
        "question_id": 135,
        "question_text": "You're part of a hackathon team. Which project would you choose?",
        "category": "Situational - Tech Competition",
        "options": [
            {
                "option_id": 1351,
                "option_text": "An AI chatbot that helps students study",
                "trait_tags": {"AI-ML": 1.0, "Software-Dev": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Data-Analytics": 0.4, "Technical-Skill": 0.36}
            },
            {
                "option_id": 1352,
                "option_text": "A mobile app for local businesses",
                "trait_tags": {"Mobile-Dev": 1.0, "Startup-Venture": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Enterprising": 0.36, "Investigative": 0.35}
            },
            {
                "option_id": 1353,
                "option_text": "A cybersecurity tool to detect phishing",
                "trait_tags": {"Cyber-Defense": 1.0, "Software-Dev": 0.8, "Technical-Skill": 0.4, "Investigative": 0.35, "Data-Analytics": 0.24, "Hardware-Systems": 0.16}
            },
            {
                "option_id": 1354,
                "option_text": "A data dashboard tracking COVID cases",
                "trait_tags": {"Data-Analytics": 1.0, "Public-Health": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Social": 0.32, "Software-Dev": 0.3}
            },
            {
                "option_id": 1355,
                "option_text": "A VR game set in Philippine history",
                "trait_tags": {"Game-Dev": 1.0, "Animation-3D": 0.8, "Technical-Skill": 0.4, "Software-Dev": 0.4, "Creative-Skill": 0.35, "Artistic": 0.32}
            },
            {
                "option_id": 1356,
                "option_text": "An IoT system for smart farming",
                "trait_tags": {"Hardware-Systems": 1.0, "Agri-Nature": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Electrical-Power": 0.3, "Physical-Skill": 0.28}
            },
            {
                "option_id": 1357,
                "option_text": "A cloud platform for school management",
                "trait_tags": {"Cloud-Systems": 1.0, "Admin-Skill": 0.8, "Technical-Skill": 0.45, "Conventional": 0.36, "Software-Dev": 0.35, "Investigative": 0.3}
            },
            {
                "option_id": 1358,
                "option_text": "A machine learning model to predict floods",
                "trait_tags": {"AI-ML": 1.0, "Environmental-Sci": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Data-Analytics": 0.4, "Software-Dev": 0.35}
            }
        ]
    },
    {
        "question_id": 136,
        "question_text": "If you could create any app, what would it do?",
        "category": "Situational - App Development",
        "options": [
            {
                "option_id": 1361,
                "option_text": "Help people find the best doctors nearby",
                "trait_tags": {"Mobile-Dev": 1.0, "Patient-Care": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "People-Skill": 0.36, "Investigative": 0.35}
            },
            {
                "option_id": 1362,
                "option_text": "Track personal finances and budgets",
                "trait_tags": {"Mobile-Dev": 1.0, "Finance-Acct": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Conventional": 0.36, "Investigative": 0.35}
            },
            {
                "option_id": 1363,
                "option_text": "Connect local farmers to buyers directly",
                "trait_tags": {"Mobile-Dev": 1.0, "Agri-Nature": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Realistic": 0.36, "Investigative": 0.35}
            },
            {
                "option_id": 1364,
                "option_text": "An AI tutor that adapts to student learning",
                "trait_tags": {"AI-ML": 1.0, "Teaching-Ed": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Data-Analytics": 0.4, "Social": 0.36}
            },
            {
                "option_id": 1365,
                "option_text": "A social platform for Filipino artists",
                "trait_tags": {"Mobile-Dev": 1.0, "Visual-Design": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Artistic": 0.36, "Creative-Skill": 0.36}
            },
            {
                "option_id": 1366,
                "option_text": "A fitness tracker with workout plans",
                "trait_tags": {"Mobile-Dev": 1.0, "Sports-Ed": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Physical-Skill": 0.36, "Investigative": 0.35}
            },
            {
                "option_id": 1367,
                "option_text": "A disaster alert system using real-time data",
                "trait_tags": {"Mobile-Dev": 1.0, "Environmental-Sci": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Investigative": 0.36, "Field-Research": 0.32}
            },
            {
                "option_id": 1368,
                "option_text": "A game that teaches children about science",
                "trait_tags": {"Game-Dev": 1.0, "Teaching-Ed": 0.8, "Technical-Skill": 0.4, "Software-Dev": 0.4, "Social": 0.36, "People-Skill": 0.36}
            }
        ]
    },
    {
        "question_id": 137,
        "question_text": "Your company is hit by a ransomware attack. What's your role in the response?",
        "category": "Situational - Cybersecurity",
        "options": [
            {
                "option_id": 1371,
                "option_text": "Leading the technical incident response team",
                "trait_tags": {"Cyber-Defense": 1.0, "Cloud-Systems": 0.8, "Technical-Skill": 0.4, "Investigative": 0.35, "Software-Dev": 0.28, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 1372,
                "option_text": "Analyzing the malware to find its source",
                "trait_tags": {"Cyber-Defense": 1.0, "Forensic-Sci": 0.8, "Technical-Skill": 0.4, "Investigative": 0.36, "Analytical-Skill": 0.32, "Law-Enforce": 0.28}
            },
            {
                "option_id": 1373,
                "option_text": "Restoring systems from backup servers",
                "trait_tags": {"Cloud-Systems": 1.0, "Software-Dev": 0.8, "Technical-Skill": 0.45, "Investigative": 0.32, "Cyber-Defense": 0.3, "Hardware-Systems": 0.25}
            },
            {
                "option_id": 1374,
                "option_text": "Communicating with stakeholders about the breach",
                "trait_tags": {"Admin-Skill": 1.0, "People-Skill": 0.8, "Conventional": 0.45, "Social": 0.36, "Hospitality-Svc": 0.32, "Teaching-Ed": 0.32}
            },
            {
                "option_id": 1375,
                "option_text": "Working with law enforcement to catch the hackers",
                "trait_tags": {"Cyber-Defense": 1.0, "Law-Enforce": 0.8, "Technical-Skill": 0.4, "Investigative": 0.35, "Realistic": 0.28, "Physical-Skill": 0.28}
            },
            {
                "option_id": 1376,
                "option_text": "Training employees to prevent future attacks",
                "trait_tags": {"Teaching-Ed": 1.0, "Cyber-Defense": 0.8, "Social": 0.45, "People-Skill": 0.45, "Technical-Skill": 0.32, "Investigative": 0.28}
            },
            {
                "option_id": 1377,
                "option_text": "Developing better security protocols",
                "trait_tags": {"Cyber-Defense": 1.0, "Software-Dev": 0.8, "Technical-Skill": 0.4, "Investigative": 0.35, "Data-Analytics": 0.24, "Hardware-Systems": 0.16}
            },
            {
                "option_id": 1378,
                "option_text": "Assessing the financial damage and filing insurance",
                "trait_tags": {"Finance-Acct": 1.0, "Admin-Skill": 0.8, "Conventional": 0.45, "Analytical-Skill": 0.4, "Startup-Venture": 0.2, "Hospitality-Svc": 0.16}
            }
        ]
    },
    {
        "question_id": 138,
        "question_text": "You're asked to create an AI system for your school. What would it do?",
        "category": "Situational - AI/ML",
        "options": [
            {
                "option_id": 1381,
                "option_text": "Predict which students need extra tutoring",
                "trait_tags": {"AI-ML": 1.0, "Teaching-Ed": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Data-Analytics": 0.4, "Social": 0.36}
            },
            {
                "option_id": 1382,
                "option_text": "Automate grading of essays and exams",
                "trait_tags": {"AI-ML": 1.0, "Data-Analytics": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Software-Dev": 0.35, "Lab-Research": 0.2}
            },
            {
                "option_id": 1383,
                "option_text": "Detect cheating in online exams",
                "trait_tags": {"AI-ML": 1.0, "Cyber-Defense": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Data-Analytics": 0.4, "Software-Dev": 0.35}
            },
            {
                "option_id": 1384,
                "option_text": "Generate personalized study materials",
                "trait_tags": {"AI-ML": 1.0, "Teaching-Ed": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Data-Analytics": 0.4, "Social": 0.36}
            },
            {
                "option_id": 1385,
                "option_text": "Analyze campus safety through security cameras",
                "trait_tags": {"AI-ML": 1.0, "Law-Enforce": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Data-Analytics": 0.4, "Software-Dev": 0.35}
            },
            {
                "option_id": 1386,
                "option_text": "Optimize class schedules and room assignments",
                "trait_tags": {"AI-ML": 1.0, "Admin-Skill": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Data-Analytics": 0.4, "Conventional": 0.36}
            },
            {
                "option_id": 1387,
                "option_text": "Create a virtual campus tour using AR",
                "trait_tags": {"AI-ML": 1.0, "Animation-3D": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Data-Analytics": 0.4, "Software-Dev": 0.35}
            },
            {
                "option_id": 1388,
                "option_text": "Monitor campus energy usage to save electricity",
                "trait_tags": {"AI-ML": 1.0, "Environmental-Eng": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Data-Analytics": 0.4, "Software-Dev": 0.35}
            }
        ]
    },
    {
        "question_id": 139,
        "question_text": "A friend asks you to help make their indie video game. What role do you want?",
        "category": "Situational - Game Development",
        "options": [
            {
                "option_id": 1391,
                "option_text": "Programming the game mechanics and physics",
                "trait_tags": {"Game-Dev": 1.0, "Software-Dev": 0.8, "Technical-Skill": 0.4, "Creative-Skill": 0.35, "Animation-3D": 0.35, "Investigative": 0.32}
            },
            {
                "option_id": 1392,
                "option_text": "Creating the 3D character models and environments",
                "trait_tags": {"Animation-3D": 1.0, "Visual-Design": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Digital-Media": 0.4, "Game-Dev": 0.35}
            },
            {
                "option_id": 1393,
                "option_text": "Writing the storyline and dialogue",
                "trait_tags": {"Creative-Skill": 1.0, "Game-Dev": 0.8, "Artistic": 0.45, "Visual-Design": 0.4, "Digital-Media": 0.4, "Spatial-Design": 0.35}
            },
            {
                "option_id": 1394,
                "option_text": "Composing the music and sound effects",
                "trait_tags": {"Performing-Arts": 1.0, "Digital-Media": 0.8, "Artistic": 0.45, "Creative-Skill": 0.45, "People-Skill": 0.3, "Film-Broadcast": 0.25}
            },
            {
                "option_id": 1395,
                "option_text": "Testing and finding bugs",
                "trait_tags": {"Software-Dev": 1.0, "Analytical-Skill": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.32, "Lab-Research": 0.28}
            },
            {
                "option_id": 1396,
                "option_text": "Marketing and publishing the game online",
                "trait_tags": {"Marketing-Sales": 1.0, "Digital-Media": 0.8, "Enterprising": 0.45, "People-Skill": 0.4, "Artistic": 0.32, "Creative-Skill": 0.32}
            },
            {
                "option_id": 1397,
                "option_text": "Designing the UI and menu systems",
                "trait_tags": {"Web-Dev": 1.0, "Visual-Design": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Creative-Skill": 0.36, "Artistic": 0.36}
            },
            {
                "option_id": 1398,
                "option_text": "Managing the project schedule and budget",
                "trait_tags": {"Admin-Skill": 1.0, "Startup-Venture": 0.8, "Conventional": 0.45, "Enterprising": 0.36, "Finance-Acct": 0.3, "People-Skill": 0.24}
            }
        ]
    },
    {
        "question_id": 140,
        "question_text": "Your barangay wants a tech solution for a local problem. What would you build?",
        "category": "Situational - Community Tech",
        "options": [
            {
                "option_id": 1401,
                "option_text": "A database to track residents and health records",
                "trait_tags": {"Software-Dev": 1.0, "Public-Health": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Social": 0.32, "Data-Analytics": 0.3}
            },
            {
                "option_id": 1402,
                "option_text": "A CCTV monitoring system with smart alerts",
                "trait_tags": {"Hardware-Systems": 1.0, "Law-Enforce": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Electrical-Power": 0.3, "Physical-Skill": 0.28}
            },
            {
                "option_id": 1403,
                "option_text": "A Wi-Fi hotspot for students without internet",
                "trait_tags": {"Cloud-Systems": 1.0, "Community-Serve": 0.8, "Technical-Skill": 0.45, "Social": 0.36, "Software-Dev": 0.35, "People-Skill": 0.32}
            },
            {
                "option_id": 1404,
                "option_text": "An app for reporting emergencies and crimes",
                "trait_tags": {"Mobile-Dev": 1.0, "Law-Enforce": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Investigative": 0.35, "Web-Dev": 0.3}
            },
            {
                "option_id": 1405,
                "option_text": "A system to track garbage collection schedules",
                "trait_tags": {"Software-Dev": 1.0, "Environmental-Eng": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Realistic": 0.32, "Data-Analytics": 0.3}
            },
            {
                "option_id": 1406,
                "option_text": "A digital marketplace for local vendors",
                "trait_tags": {"Web-Dev": 1.0, "Marketing-Sales": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Enterprising": 0.36, "Investigative": 0.35}
            },
            {
                "option_id": 1407,
                "option_text": "An SMS alert system for typhoon warnings",
                "trait_tags": {"Mobile-Dev": 1.0, "Environmental-Sci": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Investigative": 0.36, "Field-Research": 0.32}
            },
            {
                "option_id": 1408,
                "option_text": "None — I'd focus on non-tech solutions",
                "trait_tags": {"Community-Serve": 1.0, "People-Skill": 0.8, "Social": 0.45, "Teaching-Ed": 0.32, "Patient-Care": 0.32, "Enterprising": 0.24}
            }
        ]
    },
    {
        "question_id": 141,
        "question_text": "A typhoon hits your province. As a healthcare worker, what's your priority?",
        "category": "Situational - Disaster Healthcare",
        "options": [
            {
                "option_id": 1411,
                "option_text": "Treating injured victims at the evacuation center",
                "trait_tags": {"Patient-Care": 1.0, "Physical-Skill": 0.8, "People-Skill": 0.45, "Social": 0.4, "Realistic": 0.32, "Rehab-Therapy": 0.3}
            },
            {
                "option_id": 1412,
                "option_text": "Setting up a temporary pharmacy for medicine distribution",
                "trait_tags": {"Pharmacy": 1.0, "Public-Health": 0.8, "Investigative": 0.4, "Analytical-Skill": 0.4, "Medical-Lab": 0.35, "Social": 0.32}
            },
            {
                "option_id": 1413,
                "option_text": "Running water and food quality tests",
                "trait_tags": {"Medical-Lab": 1.0, "Food-Science": 0.8, "Analytical-Skill": 0.45, "Investigative": 0.4, "Lab-Research": 0.35, "Nutrition-Diet": 0.28}
            },
            {
                "option_id": 1414,
                "option_text": "Organizing mental health support for survivors",
                "trait_tags": {"Counseling": 1.0, "Rehab-Therapy": 0.8, "Social": 0.45, "People-Skill": 0.45, "Physical-Skill": 0.32, "Teaching-Ed": 0.3}
            },
            {
                "option_id": 1415,
                "option_text": "Coordinating health teams and supply logistics",
                "trait_tags": {"Health-Admin": 1.0, "Admin-Skill": 0.8, "Conventional": 0.4, "Finance-Acct": 0.24, "Hospitality-Svc": 0.16, "Patient-Care": 0.15}
            },
            {
                "option_id": 1416,
                "option_text": "Providing nutritional support and meal planning",
                "trait_tags": {"Nutrition-Diet": 1.0, "Public-Health": 0.8, "Food-Science": 0.35, "Social": 0.32, "Analytical-Skill": 0.3, "Community-Serve": 0.28}
            },
            {
                "option_id": 1417,
                "option_text": "Helping injured people with physical rehabilitation",
                "trait_tags": {"Rehab-Therapy": 1.0, "Physical-Skill": 0.8, "Social": 0.35, "People-Skill": 0.35, "Realistic": 0.32, "Patient-Care": 0.3}
            },
            {
                "option_id": 1418,
                "option_text": "Preventing disease outbreaks through sanitation",
                "trait_tags": {"Public-Health": 1.0, "Environmental-Sci": 0.8, "Social": 0.4, "Investigative": 0.36, "Analytical-Skill": 0.35, "Community-Serve": 0.35}
            }
        ]
    },
    {
        "question_id": 142,
        "question_text": "A patient comes in with an unknown illness. What would you want to do?",
        "category": "Situational - Medical Mystery",
        "options": [
            {
                "option_id": 1421,
                "option_text": "Take their vital signs and comfort them",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.8, "Social": 0.4, "Teaching-Ed": 0.32, "Hospitality-Svc": 0.32, "Rehab-Therapy": 0.3}
            },
            {
                "option_id": 1422,
                "option_text": "Run lab tests on their blood and tissue samples",
                "trait_tags": {"Medical-Lab": 1.0, "Lab-Research": 0.8, "Analytical-Skill": 0.45, "Investigative": 0.4, "Technical-Skill": 0.25, "Patient-Care": 0.2}
            },
            {
                "option_id": 1423,
                "option_text": "Research the symptoms and possible diseases",
                "trait_tags": {"Lab-Research": 1.0, "Analytical-Skill": 0.8, "Investigative": 0.45, "Data-Analytics": 0.32, "Medical-Lab": 0.3, "Field-Research": 0.25}
            },
            {
                "option_id": 1424,
                "option_text": "Check if the right medications are available",
                "trait_tags": {"Pharmacy": 1.0, "Medical-Lab": 0.8, "Investigative": 0.4, "Analytical-Skill": 0.4, "Lab-Research": 0.28, "Patient-Care": 0.25}
            },
            {
                "option_id": 1425,
                "option_text": "Operate the imaging machines for diagnosis",
                "trait_tags": {"Medical-Lab": 1.0, "Technical-Skill": 0.8, "Analytical-Skill": 0.45, "Investigative": 0.4, "Lab-Research": 0.35, "Software-Dev": 0.32}
            },
            {
                "option_id": 1426,
                "option_text": "Track if others in the community have the same illness",
                "trait_tags": {"Public-Health": 1.0, "Data-Analytics": 0.8, "Social": 0.4, "Analytical-Skill": 0.36, "Investigative": 0.36, "Community-Serve": 0.35}
            },
            {
                "option_id": 1427,
                "option_text": "Update the patient's medical records accurately",
                "trait_tags": {"Health-Admin": 1.0, "Admin-Skill": 0.8, "Conventional": 0.4, "Finance-Acct": 0.24, "Hospitality-Svc": 0.16, "Patient-Care": 0.15}
            },
            {
                "option_id": 1428,
                "option_text": "Call a team meeting to discuss the case",
                "trait_tags": {"People-Skill": 1.0, "Analytical-Skill": 0.8, "Social": 0.45, "Patient-Care": 0.4, "Teaching-Ed": 0.4, "Hospitality-Svc": 0.4}
            }
        ]
    },
    {
        "question_id": 143,
        "question_text": "Your barangay health center needs improvements. What would you focus on?",
        "category": "Situational - Community Health",
        "options": [
            {
                "option_id": 1431,
                "option_text": "Training midwives for safer childbirth",
                "trait_tags": {"Patient-Care": 1.0, "Teaching-Ed": 0.8, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25}
            },
            {
                "option_id": 1432,
                "option_text": "Adding a small lab for basic diagnostics",
                "trait_tags": {"Medical-Lab": 1.0, "Lab-Research": 0.8, "Analytical-Skill": 0.45, "Investigative": 0.4, "Technical-Skill": 0.25, "Patient-Care": 0.2}
            },
            {
                "option_id": 1433,
                "option_text": "Starting a vaccination and immunization drive",
                "trait_tags": {"Public-Health": 1.0, "Community-Serve": 0.8, "Social": 0.4, "Analytical-Skill": 0.35, "People-Skill": 0.32, "Patient-Care": 0.25}
            },
            {
                "option_id": 1434,
                "option_text": "Setting up a rehabilitation room for PT",
                "trait_tags": {"Rehab-Therapy": 1.0, "Physical-Skill": 0.8, "Social": 0.35, "People-Skill": 0.35, "Realistic": 0.32, "Patient-Care": 0.3}
            },
            {
                "option_id": 1435,
                "option_text": "Creating a nutrition program for malnourished children",
                "trait_tags": {"Nutrition-Diet": 1.0, "Public-Health": 0.8, "Food-Science": 0.35, "Social": 0.32, "Analytical-Skill": 0.3, "Community-Serve": 0.28}
            },
            {
                "option_id": 1436,
                "option_text": "Digitalizing patient records for better tracking",
                "trait_tags": {"Health-Admin": 1.0, "Software-Dev": 0.8, "Admin-Skill": 0.45, "Conventional": 0.4, "Technical-Skill": 0.36, "Investigative": 0.32}
            },
            {
                "option_id": 1437,
                "option_text": "Adding mental health counseling services",
                "trait_tags": {"Counseling": 1.0, "People-Skill": 0.8, "Social": 0.45, "Teaching-Ed": 0.32, "Patient-Care": 0.32, "Hospitality-Svc": 0.32}
            },
            {
                "option_id": 1438,
                "option_text": "Stocking essential medicines properly",
                "trait_tags": {"Pharmacy": 1.0, "Admin-Skill": 0.8, "Investigative": 0.4, "Analytical-Skill": 0.4, "Conventional": 0.36, "Medical-Lab": 0.35}
            }
        ]
    },
    {
        "question_id": 144,
        "question_text": "At a health fair, which booth would you volunteer at?",
        "category": "Situational - Health Fair",
        "options": [
            {
                "option_id": 1441,
                "option_text": "Free blood pressure and sugar level testing",
                "trait_tags": {"Patient-Care": 1.0, "Medical-Lab": 0.8, "People-Skill": 0.45, "Social": 0.4, "Analytical-Skill": 0.36, "Investigative": 0.32}
            },
            {
                "option_id": 1442,
                "option_text": "Nutrition advice and healthy cooking demos",
                "trait_tags": {"Nutrition-Diet": 1.0, "Culinary-Arts": 0.8, "Food-Science": 0.35, "Social": 0.3, "Analytical-Skill": 0.3, "Creative-Skill": 0.28}
            },
            {
                "option_id": 1443,
                "option_text": "Physical fitness testing and exercise tips",
                "trait_tags": {"Sports-Ed": 1.0, "Rehab-Therapy": 0.8, "Physical-Skill": 0.45, "Social": 0.35, "Teaching-Ed": 0.35, "People-Skill": 0.28}
            },
            {
                "option_id": 1444,
                "option_text": "Mental health awareness and stress management",
                "trait_tags": {"Counseling": 1.0, "People-Skill": 0.8, "Social": 0.45, "Teaching-Ed": 0.32, "Patient-Care": 0.32, "Hospitality-Svc": 0.32}
            },
            {
                "option_id": 1445,
                "option_text": "Free eye exams and vision screening",
                "trait_tags": {"Medical-Lab": 1.0, "Patient-Care": 0.8, "Analytical-Skill": 0.45, "Investigative": 0.4, "People-Skill": 0.36, "Lab-Research": 0.35}
            },
            {
                "option_id": 1446,
                "option_text": "First aid training demonstrations",
                "trait_tags": {"Patient-Care": 1.0, "Teaching-Ed": 0.8, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25}
            },
            {
                "option_id": 1447,
                "option_text": "Distributing medicine and explaining dosages",
                "trait_tags": {"Pharmacy": 1.0, "People-Skill": 0.8, "Investigative": 0.4, "Analytical-Skill": 0.4, "Social": 0.36, "Medical-Lab": 0.35}
            },
            {
                "option_id": 1448,
                "option_text": "Organizing the event logistics and schedule",
                "trait_tags": {"Admin-Skill": 1.0, "Health-Admin": 0.8, "Conventional": 0.45, "Finance-Acct": 0.3, "Hospitality-Svc": 0.2}
            }
        ]
    },
    {
        "question_id": 145,
        "question_text": "Your city needs a new bridge. What aspect of the project would you handle?",
        "category": "Situational - Bridge Project",
        "options": [
            {
                "option_id": 1451,
                "option_text": "Designing the structural framework",
                "trait_tags": {"Civil-Build": 1.0, "Analytical-Skill": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Investigative": 0.36, "Data-Analytics": 0.32}
            },
            {
                "option_id": 1452,
                "option_text": "Planning the electrical and lighting systems",
                "trait_tags": {"Electrical-Power": 1.0, "Civil-Build": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 1453,
                "option_text": "Setting up the construction machinery",
                "trait_tags": {"Mechanical-Design": 1.0, "Physical-Skill": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Agri-Nature": 0.28, "Industrial-Ops": 0.25}
            },
            {
                "option_id": 1454,
                "option_text": "Assessing environmental impact of the bridge",
                "trait_tags": {"Environmental-Eng": 1.0, "Environmental-Sci": 0.8, "Realistic": 0.4, "Investigative": 0.36, "Technical-Skill": 0.35, "Field-Research": 0.32}
            },
            {
                "option_id": 1455,
                "option_text": "Surveying and mapping the terrain",
                "trait_tags": {"Civil-Build": 1.0, "Field-Research": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Investigative": 0.32, "Spatial-Design": 0.25}
            },
            {
                "option_id": 1456,
                "option_text": "Making the bridge aesthetically beautiful",
                "trait_tags": {"Spatial-Design": 1.0, "Visual-Design": 0.8, "Artistic": 0.36, "Creative-Skill": 0.36, "Civil-Build": 0.25, "Digital-Media": 0.24}
            },
            {
                "option_id": 1457,
                "option_text": "Managing the construction timeline and budget",
                "trait_tags": {"Industrial-Ops": 1.0, "Admin-Skill": 0.8, "Conventional": 0.36, "Analytical-Skill": 0.35, "Enterprising": 0.3, "Mechanical-Design": 0.25}
            },
            {
                "option_id": 1458,
                "option_text": "Installing smart sensors for structural monitoring",
                "trait_tags": {"Hardware-Systems": 1.0, "Civil-Build": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Electrical-Power": 0.3, "Mechanical-Design": 0.25}
            }
        ]
    },
    {
        "question_id": 146,
        "question_text": "A factory manager asks you to improve production efficiency. What's your approach?",
        "category": "Situational - Factory Optimization",
        "options": [
            {
                "option_id": 1461,
                "option_text": "Redesigning the assembly line layout",
                "trait_tags": {"Industrial-Ops": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.36, "Analytical-Skill": 0.35, "Technical-Skill": 0.32, "Enterprising": 0.3}
            },
            {
                "option_id": 1462,
                "option_text": "Automating processes with robotics",
                "trait_tags": {"Mechanical-Design": 1.0, "Software-Dev": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Investigative": 0.32, "Industrial-Ops": 0.25}
            },
            {
                "option_id": 1463,
                "option_text": "Upgrading the electrical power systems",
                "trait_tags": {"Electrical-Power": 1.0, "Technical-Skill": 0.8, "Realistic": 0.4, "Hardware-Systems": 0.32, "Software-Dev": 0.32, "Mechanical-Design": 0.28}
            },
            {
                "option_id": 1464,
                "option_text": "Analyzing data to find bottlenecks",
                "trait_tags": {"Industrial-Ops": 1.0, "Data-Analytics": 0.8, "Analytical-Skill": 0.36, "Investigative": 0.36, "Enterprising": 0.3, "Mechanical-Design": 0.25}
            },
            {
                "option_id": 1465,
                "option_text": "Reducing waste and environmental impact",
                "trait_tags": {"Environmental-Eng": 1.0, "Industrial-Ops": 0.8, "Realistic": 0.4, "Technical-Skill": 0.35, "Environmental-Sci": 0.35, "Analytical-Skill": 0.28}
            },
            {
                "option_id": 1466,
                "option_text": "Training workers on new equipment",
                "trait_tags": {"Teaching-Ed": 1.0, "Industrial-Ops": 0.8, "Social": 0.45, "People-Skill": 0.45, "Analytical-Skill": 0.28, "Community-Serve": 0.25}
            },
            {
                "option_id": 1467,
                "option_text": "Building custom machines for specific tasks",
                "trait_tags": {"Mechanical-Design": 1.0, "Hardware-Systems": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Industrial-Ops": 0.25, "Electrical-Power": 0.24}
            },
            {
                "option_id": 1468,
                "option_text": "Implementing quality control systems",
                "trait_tags": {"Industrial-Ops": 1.0, "Analytical-Skill": 0.8, "Investigative": 0.36, "Data-Analytics": 0.32, "Enterprising": 0.3, "Finance-Acct": 0.28}
            }
        ]
    },
    {
        "question_id": 147,
        "question_text": "An earthquake damaged several buildings in your area. What would you inspect first?",
        "category": "Situational - Structural Assessment",
        "options": [
            {
                "option_id": 1471,
                "option_text": "The structural integrity of the foundations",
                "trait_tags": {"Civil-Build": 1.0, "Analytical-Skill": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Investigative": 0.36, "Data-Analytics": 0.32}
            },
            {
                "option_id": 1472,
                "option_text": "The electrical wiring and fire hazards",
                "trait_tags": {"Electrical-Power": 1.0, "Technical-Skill": 0.8, "Realistic": 0.4, "Hardware-Systems": 0.32, "Software-Dev": 0.32, "Mechanical-Design": 0.28}
            },
            {
                "option_id": 1473,
                "option_text": "The water and plumbing systems",
                "trait_tags": {"Mechanical-Design": 1.0, "Civil-Build": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Industrial-Ops": 0.25, "Electrical-Power": 0.2}
            },
            {
                "option_id": 1474,
                "option_text": "Environmental contamination from damaged facilities",
                "trait_tags": {"Environmental-Eng": 1.0, "Lab-Research": 0.8, "Realistic": 0.4, "Investigative": 0.36, "Analytical-Skill": 0.36, "Technical-Skill": 0.35}
            },
            {
                "option_id": 1475,
                "option_text": "Whether the building design followed earthquake codes",
                "trait_tags": {"Spatial-Design": 1.0, "Civil-Build": 0.8, "Realistic": 0.36, "Artistic": 0.35, "Creative-Skill": 0.35, "Technical-Skill": 0.32}
            },
            {
                "option_id": 1476,
                "option_text": "The seismic data to predict aftershocks",
                "trait_tags": {"Data-Analytics": 1.0, "Field-Research": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Software-Dev": 0.3, "Lab-Research": 0.25}
            },
            {
                "option_id": 1477,
                "option_text": "Whether machinery and elevators are safe",
                "trait_tags": {"Mechanical-Design": 1.0, "Industrial-Ops": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Analytical-Skill": 0.28, "Enterprising": 0.24}
            },
            {
                "option_id": 1478,
                "option_text": "I'd focus on helping rescue trapped people",
                "trait_tags": {"Physical-Skill": 1.0, "Community-Serve": 0.8, "Realistic": 0.4, "Social": 0.36, "Maritime-Sea": 0.35, "Agri-Nature": 0.35}
            }
        ]
    },
    {
        "question_id": 148,
        "question_text": "You're launching a food business in your town. What's your first priority?",
        "category": "Situational - Food Business",
        "options": [
            {
                "option_id": 1481,
                "option_text": "Creating a unique menu and recipes",
                "trait_tags": {"Culinary-Arts": 1.0, "Creative-Skill": 0.8, "Artistic": 0.36, "Hospitality-Svc": 0.35, "Visual-Design": 0.32, "Digital-Media": 0.32}
            },
            {
                "option_id": 1482,
                "option_text": "Managing the budget and financial projections",
                "trait_tags": {"Finance-Acct": 1.0, "Startup-Venture": 0.8, "Conventional": 0.45, "Analytical-Skill": 0.4, "Enterprising": 0.36, "Admin-Skill": 0.3}
            },
            {
                "option_id": 1483,
                "option_text": "Marketing on social media to attract customers",
                "trait_tags": {"Marketing-Sales": 1.0, "Digital-Media": 0.8, "Enterprising": 0.45, "People-Skill": 0.4, "Artistic": 0.32, "Creative-Skill": 0.32}
            },
            {
                "option_id": 1484,
                "option_text": "Hiring and training the right staff",
                "trait_tags": {"HR-Management": 1.0, "People-Skill": 0.8, "Social": 0.36, "Enterprising": 0.35, "Admin-Skill": 0.35, "Teaching-Ed": 0.32}
            },
            {
                "option_id": 1485,
                "option_text": "Ensuring food safety and proper storage",
                "trait_tags": {"Food-Science": 1.0, "Nutrition-Diet": 0.8, "Investigative": 0.4, "Lab-Research": 0.35, "Analytical-Skill": 0.3, "Social": 0.24}
            },
            {
                "option_id": 1486,
                "option_text": "Designing the restaurant layout and ambiance",
                "trait_tags": {"Spatial-Design": 1.0, "Visual-Design": 0.8, "Artistic": 0.36, "Creative-Skill": 0.36, "Civil-Build": 0.25, "Digital-Media": 0.24}
            },
            {
                "option_id": 1487,
                "option_text": "Negotiating with suppliers for best prices",
                "trait_tags": {"Startup-Venture": 1.0, "Finance-Acct": 0.8, "Enterprising": 0.45, "Conventional": 0.36, "Analytical-Skill": 0.32, "People-Skill": 0.3}
            },
            {
                "option_id": 1488,
                "option_text": "Building a delivery app or online ordering system",
                "trait_tags": {"Web-Dev": 1.0, "Startup-Venture": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Enterprising": 0.36, "Investigative": 0.35}
            }
        ]
    },
    {
        "question_id": 149,
        "question_text": "Your friend's sari-sari store is struggling. How would you help?",
        "category": "Situational - Small Business",
        "options": [
            {
                "option_id": 1491,
                "option_text": "Analyze their sales data to find what sells best",
                "trait_tags": {"Data-Analytics": 1.0, "Finance-Acct": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Conventional": 0.36, "Software-Dev": 0.3}
            },
            {
                "option_id": 1492,
                "option_text": "Create a Facebook page and promote online",
                "trait_tags": {"Marketing-Sales": 1.0, "Digital-Media": 0.8, "Enterprising": 0.45, "People-Skill": 0.4, "Artistic": 0.32, "Creative-Skill": 0.32}
            },
            {
                "option_id": 1493,
                "option_text": "Redesign the store layout to attract customers",
                "trait_tags": {"Spatial-Design": 1.0, "Marketing-Sales": 0.8, "Enterprising": 0.36, "Artistic": 0.35, "Creative-Skill": 0.35, "People-Skill": 0.32}
            },
            {
                "option_id": 1494,
                "option_text": "Help them manage inventory and expenses",
                "trait_tags": {"Admin-Skill": 1.0, "Finance-Acct": 0.8, "Conventional": 0.45, "Analytical-Skill": 0.32, "Hospitality-Svc": 0.2, "Startup-Venture": 0.16}
            },
            {
                "option_id": 1495,
                "option_text": "Introduce new products based on neighborhood needs",
                "trait_tags": {"Startup-Venture": 1.0, "Community-Serve": 0.8, "Enterprising": 0.45, "Social": 0.36, "People-Skill": 0.32, "Marketing-Sales": 0.3}
            },
            {
                "option_id": 1496,
                "option_text": "Train them on customer service skills",
                "trait_tags": {"HR-Management": 1.0, "People-Skill": 0.8, "Social": 0.36, "Enterprising": 0.35, "Admin-Skill": 0.35, "Teaching-Ed": 0.32}
            },
            {
                "option_id": 1497,
                "option_text": "Set up a simple POS or accounting system",
                "trait_tags": {"Software-Dev": 1.0, "Finance-Acct": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Conventional": 0.36, "Analytical-Skill": 0.32}
            },
            {
                "option_id": 1498,
                "option_text": "Look into franchise or cooperative options",
                "trait_tags": {"Startup-Venture": 1.0, "Admin-Skill": 0.8, "Enterprising": 0.45, "Conventional": 0.36, "People-Skill": 0.3, "Marketing-Sales": 0.3}
            }
        ]
    },
    {
        "question_id": 150,
        "question_text": "You're managing a company's HR department. What task do you enjoy most?",
        "category": "Situational - Human Resources",
        "options": [
            {
                "option_id": 1501,
                "option_text": "Interviewing and selecting the best candidates",
                "trait_tags": {"HR-Management": 1.0, "People-Skill": 0.8, "Social": 0.36, "Enterprising": 0.35, "Admin-Skill": 0.35, "Teaching-Ed": 0.32}
            },
            {
                "option_id": 1502,
                "option_text": "Designing training programs for new employees",
                "trait_tags": {"HR-Management": 1.0, "Teaching-Ed": 0.8, "People-Skill": 0.4, "Social": 0.36, "Enterprising": 0.35, "Admin-Skill": 0.35}
            },
            {
                "option_id": 1503,
                "option_text": "Resolving workplace conflicts between team members",
                "trait_tags": {"HR-Management": 1.0, "Counseling": 0.8, "People-Skill": 0.4, "Social": 0.36, "Enterprising": 0.35, "Admin-Skill": 0.35}
            },
            {
                "option_id": 1504,
                "option_text": "Managing payroll and employee benefits",
                "trait_tags": {"Finance-Acct": 1.0, "Admin-Skill": 0.8, "Conventional": 0.45, "Analytical-Skill": 0.4, "Startup-Venture": 0.2, "Hospitality-Svc": 0.16}
            },
            {
                "option_id": 1505,
                "option_text": "Creating team-building activities and events",
                "trait_tags": {"HR-Management": 1.0, "Creative-Skill": 0.8, "People-Skill": 0.4, "Artistic": 0.36, "Social": 0.35, "Enterprising": 0.35}
            },
            {
                "option_id": 1506,
                "option_text": "Ensuring the company follows labor laws",
                "trait_tags": {"Legal-Practice": 1.0, "Admin-Skill": 0.8, "Conventional": 0.36, "Enterprising": 0.35, "Analytical-Skill": 0.35, "People-Skill": 0.3}
            },
            {
                "option_id": 1507,
                "option_text": "Analyzing employee performance data",
                "trait_tags": {"Data-Analytics": 1.0, "HR-Management": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "People-Skill": 0.32, "Software-Dev": 0.3}
            },
            {
                "option_id": 1508,
                "option_text": "Building the company culture and values",
                "trait_tags": {"HR-Management": 1.0, "Community-Serve": 0.8, "People-Skill": 0.4, "Social": 0.36, "Enterprising": 0.35, "Admin-Skill": 0.35}
            }
        ]
    },
    {
        "question_id": 151,
        "question_text": "Your school is putting on a big cultural show. What role would you take?",
        "category": "Situational - Cultural Event",
        "options": [
            {
                "option_id": 1511,
                "option_text": "Directing the play or dance performance",
                "trait_tags": {"Performing-Arts": 1.0, "People-Skill": 0.8, "Artistic": 0.45, "Creative-Skill": 0.45, "Social": 0.36, "Teaching-Ed": 0.32}
            },
            {
                "option_id": 1512,
                "option_text": "Designing the stage set and costumes",
                "trait_tags": {"Visual-Design": 1.0, "Spatial-Design": 0.8, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Technical-Skill": 0.16}
            },
            {
                "option_id": 1513,
                "option_text": "Filming and editing the event highlights",
                "trait_tags": {"Film-Broadcast": 1.0, "Digital-Media": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Visual-Design": 0.25, "Technical-Skill": 0.2}
            },
            {
                "option_id": 1514,
                "option_text": "Composing or selecting the music",
                "trait_tags": {"Performing-Arts": 1.0, "Creative-Skill": 0.8, "Artistic": 0.45, "Visual-Design": 0.32, "Digital-Media": 0.32, "People-Skill": 0.3}
            },
            {
                "option_id": 1515,
                "option_text": "Creating promotional posters and social media content",
                "trait_tags": {"Visual-Design": 1.0, "Marketing-Sales": 0.8, "Artistic": 0.45, "Creative-Skill": 0.45, "Enterprising": 0.36, "People-Skill": 0.32}
            },
            {
                "option_id": 1516,
                "option_text": "Managing the budget and sponsorships",
                "trait_tags": {"Finance-Acct": 1.0, "Admin-Skill": 0.8, "Conventional": 0.45, "Analytical-Skill": 0.4, "Startup-Venture": 0.2, "Hospitality-Svc": 0.16}
            },
            {
                "option_id": 1517,
                "option_text": "Operating the lights, sound, and tech equipment",
                "trait_tags": {"Technical-Skill": 1.0, "Hardware-Systems": 0.8, "Software-Dev": 0.4, "Realistic": 0.35, "Mechanical-Design": 0.35, "Investigative": 0.25}
            },
            {
                "option_id": 1518,
                "option_text": "Acting or performing on stage",
                "trait_tags": {"Performing-Arts": 1.0, "Creative-Skill": 0.8, "Artistic": 0.45, "Visual-Design": 0.32, "Digital-Media": 0.32, "People-Skill": 0.3}
            }
        ]
    },
    {
        "question_id": 152,
        "question_text": "A local museum asks you to create a digital exhibit. What would you make?",
        "category": "Situational - Digital Art",
        "options": [
            {
                "option_id": 1521,
                "option_text": "A 3D virtual tour of Philippine heritage sites",
                "trait_tags": {"Animation-3D": 1.0, "Tourism-Travel": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Digital-Media": 0.4, "Game-Dev": 0.35}
            },
            {
                "option_id": 1522,
                "option_text": "Interactive animations of historical events",
                "trait_tags": {"Animation-3D": 1.0, "Film-Broadcast": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Digital-Media": 0.4, "Game-Dev": 0.35}
            },
            {
                "option_id": 1523,
                "option_text": "A documentary film about local traditions",
                "trait_tags": {"Film-Broadcast": 1.0, "Community-Serve": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Digital-Media": 0.4, "Social": 0.36}
            },
            {
                "option_id": 1524,
                "option_text": "Digital paintings and visual art installations",
                "trait_tags": {"Visual-Design": 1.0, "Creative-Skill": 0.8, "Artistic": 0.45, "Digital-Media": 0.32, "Spatial-Design": 0.28}
            },
            {
                "option_id": 1525,
                "option_text": "An interactive game that teaches Philippine history",
                "trait_tags": {"Game-Dev": 1.0, "Teaching-Ed": 0.8, "Technical-Skill": 0.4, "Software-Dev": 0.4, "Social": 0.36, "People-Skill": 0.36}
            },
            {
                "option_id": 1526,
                "option_text": "A music and sound experience of Philippine instruments",
                "trait_tags": {"Performing-Arts": 1.0, "Digital-Media": 0.8, "Artistic": 0.45, "Creative-Skill": 0.45, "People-Skill": 0.3, "Film-Broadcast": 0.25}
            },
            {
                "option_id": 1527,
                "option_text": "A mobile app as a museum guide",
                "trait_tags": {"Mobile-Dev": 1.0, "Tourism-Travel": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Investigative": 0.35, "People-Skill": 0.32}
            },
            {
                "option_id": 1528,
                "option_text": "Fashion display of traditional Filipino clothing",
                "trait_tags": {"Spatial-Design": 1.0, "Creative-Skill": 0.8, "Artistic": 0.36, "Visual-Design": 0.32, "Digital-Media": 0.32, "Civil-Build": 0.25}
            }
        ]
    },
    {
        "question_id": 153,
        "question_text": "You're hired to redesign a local park. What's most important to you?",
        "category": "Situational - Design Project",
        "options": [
            {
                "option_id": 1531,
                "option_text": "The landscape architecture and garden layout",
                "trait_tags": {"Spatial-Design": 1.0, "Environmental-Sci": 0.8, "Investigative": 0.36, "Artistic": 0.35, "Creative-Skill": 0.35, "Field-Research": 0.32}
            },
            {
                "option_id": 1532,
                "option_text": "Installing public art and sculptures",
                "trait_tags": {"Visual-Design": 1.0, "Creative-Skill": 0.8, "Artistic": 0.45, "Digital-Media": 0.32, "Spatial-Design": 0.28}
            },
            {
                "option_id": 1533,
                "option_text": "Making it eco-friendly with solar lighting",
                "trait_tags": {"Environmental-Eng": 1.0, "Electrical-Power": 0.8, "Realistic": 0.4, "Technical-Skill": 0.36, "Environmental-Sci": 0.35, "Civil-Build": 0.25}
            },
            {
                "option_id": 1534,
                "option_text": "Adding a sports area and fitness equipment",
                "trait_tags": {"Sports-Ed": 1.0, "Physical-Skill": 0.8, "Social": 0.35, "Teaching-Ed": 0.35, "Realistic": 0.32, "Maritime-Sea": 0.28}
            },
            {
                "option_id": 1535,
                "option_text": "Creating a children's playground with interactive features",
                "trait_tags": {"Creative-Skill": 1.0, "Teaching-Ed": 0.8, "Artistic": 0.45, "Visual-Design": 0.4, "Digital-Media": 0.4, "Social": 0.36}
            },
            {
                "option_id": 1536,
                "option_text": "Designing accessible pathways for disabled visitors",
                "trait_tags": {"Civil-Build": 1.0, "Community-Serve": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Social": 0.36, "People-Skill": 0.32}
            },
            {
                "option_id": 1537,
                "option_text": "Adding a food stall area and gathering space",
                "trait_tags": {"Hospitality-Svc": 1.0, "Culinary-Arts": 0.8, "People-Skill": 0.45, "Tourism-Travel": 0.4, "Enterprising": 0.35, "Creative-Skill": 0.28}
            },
            {
                "option_id": 1538,
                "option_text": "Installing security cameras and lighting",
                "trait_tags": {"Hardware-Systems": 1.0, "Law-Enforce": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Electrical-Power": 0.3, "Physical-Skill": 0.28}
            }
        ]
    },
    {
        "question_id": 154,
        "question_text": "A river in your town is getting polluted. How would you help as a scientist?",
        "category": "Situational - Environmental Crisis",
        "options": [
            {
                "option_id": 1541,
                "option_text": "Collect and analyze water samples in the lab",
                "trait_tags": {"Lab-Research": 1.0, "Environmental-Sci": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Field-Research": 0.32, "Medical-Lab": 0.3}
            },
            {
                "option_id": 1542,
                "option_text": "Track the pollution source using field surveys",
                "trait_tags": {"Field-Research": 1.0, "Environmental-Sci": 0.8, "Investigative": 0.4, "Agri-Nature": 0.3, "Analytical-Skill": 0.3, "Physical-Skill": 0.25}
            },
            {
                "option_id": 1543,
                "option_text": "Study the impact on fish and aquatic life",
                "trait_tags": {"Field-Research": 1.0, "Agri-Nature": 0.8, "Investigative": 0.4, "Realistic": 0.36, "Analytical-Skill": 0.3, "Physical-Skill": 0.28}
            },
            {
                "option_id": 1544,
                "option_text": "Test food safety in crops irrigated by the river",
                "trait_tags": {"Food-Science": 1.0, "Lab-Research": 0.8, "Investigative": 0.4, "Analytical-Skill": 0.36, "Nutrition-Diet": 0.35, "Medical-Lab": 0.24}
            },
            {
                "option_id": 1545,
                "option_text": "Use data modeling to predict pollution spread",
                "trait_tags": {"Data-Analytics": 1.0, "Environmental-Sci": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Field-Research": 0.32, "Software-Dev": 0.3}
            },
            {
                "option_id": 1546,
                "option_text": "Design a water filtration system",
                "trait_tags": {"Environmental-Eng": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.4, "Technical-Skill": 0.35, "Environmental-Sci": 0.35, "Civil-Build": 0.25}
            },
            {
                "option_id": 1547,
                "option_text": "Organize a community cleanup and awareness campaign",
                "trait_tags": {"Community-Serve": 1.0, "Public-Health": 0.8, "Social": 0.45, "People-Skill": 0.4, "Analytical-Skill": 0.28, "Teaching-Ed": 0.25}
            },
            {
                "option_id": 1548,
                "option_text": "Work with the government to enforce pollution laws",
                "trait_tags": {"Legal-Practice": 1.0, "Environmental-Sci": 0.8, "Investigative": 0.36, "Enterprising": 0.35, "Analytical-Skill": 0.35, "Field-Research": 0.32}
            }
        ]
    },
    {
        "question_id": 155,
        "question_text": "A new food product needs testing before it goes to market. What's your job?",
        "category": "Situational - Food Science",
        "options": [
            {
                "option_id": 1551,
                "option_text": "Testing for bacteria and contaminants in the lab",
                "trait_tags": {"Food-Science": 1.0, "Lab-Research": 0.8, "Investigative": 0.4, "Analytical-Skill": 0.36, "Nutrition-Diet": 0.35, "Medical-Lab": 0.24}
            },
            {
                "option_id": 1552,
                "option_text": "Analyzing the nutritional content and labeling",
                "trait_tags": {"Nutrition-Diet": 1.0, "Food-Science": 0.8, "Investigative": 0.32, "Social": 0.3, "Analytical-Skill": 0.3, "Lab-Research": 0.28}
            },
            {
                "option_id": 1553,
                "option_text": "Improving the taste and texture through experiments",
                "trait_tags": {"Food-Science": 1.0, "Culinary-Arts": 0.8, "Investigative": 0.4, "Lab-Research": 0.35, "Nutrition-Diet": 0.35, "Analytical-Skill": 0.3}
            },
            {
                "option_id": 1554,
                "option_text": "Designing the packaging and branding",
                "trait_tags": {"Visual-Design": 1.0, "Marketing-Sales": 0.8, "Artistic": 0.45, "Creative-Skill": 0.45, "Enterprising": 0.36, "People-Skill": 0.32}
            },
            {
                "option_id": 1555,
                "option_text": "Calculating the cost and setting the price",
                "trait_tags": {"Finance-Acct": 1.0, "Industrial-Ops": 0.8, "Conventional": 0.45, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Enterprising": 0.24}
            },
            {
                "option_id": 1556,
                "option_text": "Checking if it meets government food safety rules",
                "trait_tags": {"Food-Science": 1.0, "Legal-Practice": 0.8, "Investigative": 0.4, "Lab-Research": 0.35, "Nutrition-Diet": 0.35, "Analytical-Skill": 0.3}
            },
            {
                "option_id": 1557,
                "option_text": "Running consumer taste tests and focus groups",
                "trait_tags": {"Marketing-Sales": 1.0, "People-Skill": 0.8, "Enterprising": 0.45, "Social": 0.36, "Hospitality-Svc": 0.32, "Teaching-Ed": 0.32}
            },
            {
                "option_id": 1558,
                "option_text": "Developing the production process for mass manufacturing",
                "trait_tags": {"Industrial-Ops": 1.0, "Food-Science": 0.8, "Analytical-Skill": 0.35, "Investigative": 0.32, "Enterprising": 0.3, "Lab-Research": 0.28}
            }
        ]
    },
    {
        "question_id": 156,
        "question_text": "You're working at a forensic science lab. What's your favorite task?",
        "category": "Situational - Forensics",
        "options": [
            {
                "option_id": 1561,
                "option_text": "Analyzing DNA evidence from crime scenes",
                "trait_tags": {"Forensic-Sci": 1.0, "Lab-Research": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.4, "Law-Enforce": 0.35, "Medical-Lab": 0.24}
            },
            {
                "option_id": 1562,
                "option_text": "Examining fingerprints and trace evidence",
                "trait_tags": {"Forensic-Sci": 1.0, "Analytical-Skill": 0.8, "Investigative": 0.45, "Lab-Research": 0.35, "Law-Enforce": 0.35, "Data-Analytics": 0.32}
            },
            {
                "option_id": 1563,
                "option_text": "Performing toxicology tests for poison detection",
                "trait_tags": {"Forensic-Sci": 1.0, "Medical-Lab": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.4, "Lab-Research": 0.35, "Law-Enforce": 0.35}
            },
            {
                "option_id": 1564,
                "option_text": "Using digital forensics to analyze computer evidence",
                "trait_tags": {"Forensic-Sci": 1.0, "Cyber-Defense": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.4, "Lab-Research": 0.35, "Law-Enforce": 0.35}
            },
            {
                "option_id": 1565,
                "option_text": "Testifying as an expert witness in court",
                "trait_tags": {"Forensic-Sci": 1.0, "Legal-Practice": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.4, "Lab-Research": 0.35, "Law-Enforce": 0.35}
            },
            {
                "option_id": 1566,
                "option_text": "Reconstructing how a crime happened",
                "trait_tags": {"Forensic-Sci": 1.0, "Law-Enforce": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.4, "Lab-Research": 0.35, "Realistic": 0.28}
            },
            {
                "option_id": 1567,
                "option_text": "Taking photographs and documenting evidence",
                "trait_tags": {"Visual-Design": 1.0, "Law-Enforce": 0.8, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Realistic": 0.28}
            },
            {
                "option_id": 1568,
                "option_text": "Processing evidence at the actual crime scene",
                "trait_tags": {"Forensic-Sci": 1.0, "Physical-Skill": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.4, "Lab-Research": 0.35, "Law-Enforce": 0.35}
            }
        ]
    },
    {
        "question_id": 157,
        "question_text": "A struggling student asks for your help. How would you assist them?",
        "category": "Situational - Student Support",
        "options": [
            {
                "option_id": 1571,
                "option_text": "Tutor them one-on-one in their weak subject",
                "trait_tags": {"Teaching-Ed": 1.0, "People-Skill": 0.8, "Social": 0.45, "Patient-Care": 0.32, "Hospitality-Svc": 0.32, "Community-Serve": 0.25}
            },
            {
                "option_id": 1572,
                "option_text": "Talk to them about their personal problems first",
                "trait_tags": {"Counseling": 1.0, "People-Skill": 0.8, "Social": 0.45, "Teaching-Ed": 0.32, "Patient-Care": 0.32, "Hospitality-Svc": 0.32}
            },
            {
                "option_id": 1573,
                "option_text": "Create fun study materials and visual aids",
                "trait_tags": {"Teaching-Ed": 1.0, "Creative-Skill": 0.8, "Social": 0.45, "People-Skill": 0.45, "Artistic": 0.36, "Visual-Design": 0.32}
            },
            {
                "option_id": 1574,
                "option_text": "Organize a study group for peer support",
                "trait_tags": {"Teaching-Ed": 1.0, "Community-Serve": 0.8, "Social": 0.45, "People-Skill": 0.45, "Patient-Care": 0.16, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 1575,
                "option_text": "Use sports or games as motivation",
                "trait_tags": {"Sports-Ed": 1.0, "Teaching-Ed": 0.8, "Physical-Skill": 0.45, "Social": 0.36, "People-Skill": 0.36, "Rehab-Therapy": 0.2}
            },
            {
                "option_id": 1576,
                "option_text": "Recommend an online tutorial or learning app",
                "trait_tags": {"Teaching-Ed": 1.0, "Software-Dev": 0.8, "Social": 0.45, "People-Skill": 0.45, "Technical-Skill": 0.36, "Investigative": 0.32}
            },
            {
                "option_id": 1577,
                "option_text": "Talk to their parents about the issue",
                "trait_tags": {"Counseling": 1.0, "Social-Work": 0.8, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.32, "Teaching-Ed": 0.3}
            },
            {
                "option_id": 1578,
                "option_text": "Create a structured study plan and schedule",
                "trait_tags": {"Teaching-Ed": 1.0, "Admin-Skill": 0.8, "Social": 0.45, "People-Skill": 0.45, "Conventional": 0.36, "Health-Admin": 0.28}
            }
        ]
    },
    {
        "question_id": 158,
        "question_text": "You're a guidance counselor and a student is being bullied. What do you do first?",
        "category": "Situational - School Counseling",
        "options": [
            {
                "option_id": 1581,
                "option_text": "Listen to the student's feelings and give emotional support",
                "trait_tags": {"Counseling": 1.0, "People-Skill": 0.8, "Social": 0.45, "Teaching-Ed": 0.32, "Patient-Care": 0.32, "Hospitality-Svc": 0.32}
            },
            {
                "option_id": 1582,
                "option_text": "Investigate the bullying situation thoroughly",
                "trait_tags": {"Law-Enforce": 1.0, "Analytical-Skill": 0.8, "Investigative": 0.36, "Realistic": 0.35, "Physical-Skill": 0.35, "Data-Analytics": 0.32}
            },
            {
                "option_id": 1583,
                "option_text": "Mediate between the bully and the victim",
                "trait_tags": {"Counseling": 1.0, "People-Skill": 0.8, "Social": 0.45, "Teaching-Ed": 0.32, "Patient-Care": 0.32, "Hospitality-Svc": 0.32}
            },
            {
                "option_id": 1584,
                "option_text": "Inform the school administration and parents",
                "trait_tags": {"Admin-Skill": 1.0, "Community-Serve": 0.8, "Conventional": 0.45, "Social": 0.36, "People-Skill": 0.32, "Finance-Acct": 0.3}
            },
            {
                "option_id": 1585,
                "option_text": "Start an anti-bullying awareness program",
                "trait_tags": {"Teaching-Ed": 1.0, "Community-Serve": 0.8, "Social": 0.45, "People-Skill": 0.45, "Patient-Care": 0.16, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 1586,
                "option_text": "Refer them to a professional therapist",
                "trait_tags": {"Counseling": 1.0, "Rehab-Therapy": 0.8, "Social": 0.45, "People-Skill": 0.45, "Physical-Skill": 0.32, "Teaching-Ed": 0.3}
            },
            {
                "option_id": 1587,
                "option_text": "Teach the student coping and self-defense strategies",
                "trait_tags": {"Sports-Ed": 1.0, "Counseling": 0.8, "Physical-Skill": 0.45, "Social": 0.36, "People-Skill": 0.36, "Teaching-Ed": 0.35}
            },
            {
                "option_id": 1588,
                "option_text": "Document everything for potential legal action",
                "trait_tags": {"Legal-Practice": 1.0, "Admin-Skill": 0.8, "Conventional": 0.36, "Enterprising": 0.35, "Analytical-Skill": 0.35, "People-Skill": 0.3}
            }
        ]
    },
    {
        "question_id": 159,
        "question_text": "You discover illegal dumping in a local river. What action do you take?",
        "category": "Situational - Environmental Law",
        "options": [
            {
                "option_id": 1591,
                "option_text": "Gather evidence and file a case with the DENR",
                "trait_tags": {"Legal-Practice": 1.0, "Environmental-Sci": 0.8, "Investigative": 0.36, "Enterprising": 0.35, "Analytical-Skill": 0.35, "Field-Research": 0.32}
            },
            {
                "option_id": 1592,
                "option_text": "Organize a community protest and cleanup",
                "trait_tags": {"Community-Serve": 1.0, "Social-Work": 0.8, "Social": 0.45, "People-Skill": 0.4, "Teaching-Ed": 0.25, "Counseling": 0.24}
            },
            {
                "option_id": 1593,
                "option_text": "Interview witnesses and investigate the source",
                "trait_tags": {"Law-Enforce": 1.0, "Analytical-Skill": 0.8, "Investigative": 0.36, "Realistic": 0.35, "Physical-Skill": 0.35, "Data-Analytics": 0.32}
            },
            {
                "option_id": 1594,
                "option_text": "Write a news report to bring public attention",
                "trait_tags": {"Film-Broadcast": 1.0, "Community-Serve": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Digital-Media": 0.4, "Social": 0.36}
            },
            {
                "option_id": 1595,
                "option_text": "Test water samples to document contamination",
                "trait_tags": {"Lab-Research": 1.0, "Environmental-Sci": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Field-Research": 0.32, "Medical-Lab": 0.3}
            },
            {
                "option_id": 1596,
                "option_text": "Lobby the barangay council for stricter enforcement",
                "trait_tags": {"Community-Serve": 1.0, "Legal-Practice": 0.8, "Social": 0.45, "People-Skill": 0.4, "Enterprising": 0.28, "Analytical-Skill": 0.28}
            },
            {
                "option_id": 1597,
                "option_text": "Design a monitoring system using cameras and sensors",
                "trait_tags": {"Hardware-Systems": 1.0, "Environmental-Eng": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Electrical-Power": 0.3, "Mechanical-Design": 0.25}
            },
            {
                "option_id": 1598,
                "option_text": "Educate the community about proper waste disposal",
                "trait_tags": {"Teaching-Ed": 1.0, "Public-Health": 0.8, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.28, "Analytical-Skill": 0.28}
            }
        ]
    },
    {
        "question_id": 160,
        "question_text": "You work at a social welfare office. A family lost their home to a fire. What's your role?",
        "category": "Situational - Social Welfare",
        "options": [
            {
                "option_id": 1601,
                "option_text": "Process their emergency assistance paperwork",
                "trait_tags": {"Social-Work": 1.0, "Admin-Skill": 0.8, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.4, "Conventional": 0.36}
            },
            {
                "option_id": 1602,
                "option_text": "Provide counseling for the traumatized family",
                "trait_tags": {"Counseling": 1.0, "Social-Work": 0.8, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.32, "Teaching-Ed": 0.3}
            },
            {
                "option_id": 1603,
                "option_text": "Coordinate temporary housing and donations",
                "trait_tags": {"Community-Serve": 1.0, "Admin-Skill": 0.8, "Social": 0.45, "People-Skill": 0.4, "Conventional": 0.36, "Health-Admin": 0.28}
            },
            {
                "option_id": 1604,
                "option_text": "Assess the fire's cause for legal investigation",
                "trait_tags": {"Forensic-Sci": 1.0, "Law-Enforce": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.4, "Lab-Research": 0.35, "Realistic": 0.28}
            },
            {
                "option_id": 1605,
                "option_text": "Enroll their children in a nearby school",
                "trait_tags": {"Teaching-Ed": 1.0, "Social-Work": 0.8, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.32, "Counseling": 0.24}
            },
            {
                "option_id": 1606,
                "option_text": "Help them find new jobs or livelihood programs",
                "trait_tags": {"HR-Management": 1.0, "Social-Work": 0.8, "People-Skill": 0.4, "Social": 0.36, "Enterprising": 0.35, "Admin-Skill": 0.35}
            },
            {
                "option_id": 1607,
                "option_text": "Ensure they get proper medical checkups",
                "trait_tags": {"Public-Health": 1.0, "Patient-Care": 0.8, "Social": 0.4, "People-Skill": 0.36, "Analytical-Skill": 0.35, "Community-Serve": 0.35}
            },
            {
                "option_id": 1608,
                "option_text": "Raise funds through the community or online",
                "trait_tags": {"Marketing-Sales": 1.0, "Community-Serve": 0.8, "Enterprising": 0.45, "People-Skill": 0.4, "Social": 0.36, "Startup-Venture": 0.3}
            }
        ]
    },
    {
        "question_id": 161,
        "question_text": "A farmer in your province wants to modernize their farm. How would you help?",
        "category": "Situational - Modern Farming",
        "options": [
            {
                "option_id": 1611,
                "option_text": "Introduce drone technology for crop monitoring",
                "trait_tags": {"Agri-Nature": 1.0, "Hardware-Systems": 0.8, "Realistic": 0.45, "Technical-Skill": 0.36, "Physical-Skill": 0.35, "Field-Research": 0.25}
            },
            {
                "option_id": 1612,
                "option_text": "Set up an irrigation system for better water use",
                "trait_tags": {"Agri-Nature": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.45, "Physical-Skill": 0.35, "Technical-Skill": 0.32, "Field-Research": 0.25}
            },
            {
                "option_id": 1613,
                "option_text": "Test soil quality to recommend the right fertilizer",
                "trait_tags": {"Agri-Nature": 1.0, "Lab-Research": 0.8, "Realistic": 0.45, "Investigative": 0.36, "Analytical-Skill": 0.36, "Physical-Skill": 0.35}
            },
            {
                "option_id": 1614,
                "option_text": "Help them sell products online or in markets",
                "trait_tags": {"Agri-Nature": 1.0, "Marketing-Sales": 0.8, "Realistic": 0.45, "Enterprising": 0.36, "Physical-Skill": 0.35, "People-Skill": 0.32}
            },
            {
                "option_id": 1615,
                "option_text": "Teach organic farming techniques",
                "trait_tags": {"Agri-Nature": 1.0, "Environmental-Sci": 0.8, "Realistic": 0.45, "Investigative": 0.36, "Physical-Skill": 0.35, "Field-Research": 0.32}
            },
            {
                "option_id": 1616,
                "option_text": "Process and package their harvest for retail",
                "trait_tags": {"Food-Science": 1.0, "Industrial-Ops": 0.8, "Investigative": 0.4, "Lab-Research": 0.35, "Nutrition-Diet": 0.35, "Analytical-Skill": 0.3}
            },
            {
                "option_id": 1617,
                "option_text": "Set up a fishpond alongside the farmland",
                "trait_tags": {"Agri-Nature": 1.0, "Field-Research": 0.8, "Realistic": 0.45, "Physical-Skill": 0.35, "Investigative": 0.32, "Analytical-Skill": 0.24}
            },
            {
                "option_id": 1618,
                "option_text": "Build a simple app to track planting schedules",
                "trait_tags": {"Mobile-Dev": 1.0, "Agri-Nature": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Realistic": 0.36, "Investigative": 0.35}
            }
        ]
    },
    {
        "question_id": 162,
        "question_text": "You're on a cargo ship and the engine breaks down at sea. What's your role?",
        "category": "Situational - Maritime Emergency",
        "options": [
            {
                "option_id": 1621,
                "option_text": "Diagnose and repair the engine problem",
                "trait_tags": {"Maritime-Sea": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.45, "Physical-Skill": 0.4, "Technical-Skill": 0.32, "Industrial-Ops": 0.2}
            },
            {
                "option_id": 1622,
                "option_text": "Navigate to the nearest port for repairs",
                "trait_tags": {"Maritime-Sea": 1.0, "Physical-Skill": 0.8, "Realistic": 0.45, "Agri-Nature": 0.28, "Technical-Skill": 0.25, "Law-Enforce": 0.24}
            },
            {
                "option_id": 1623,
                "option_text": "Radio for help and coordinate with coast guard",
                "trait_tags": {"Maritime-Sea": 1.0, "Community-Serve": 0.8, "Realistic": 0.45, "Physical-Skill": 0.4, "Social": 0.36, "People-Skill": 0.32}
            },
            {
                "option_id": 1624,
                "option_text": "Check the electrical systems for faults",
                "trait_tags": {"Electrical-Power": 1.0, "Maritime-Sea": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Physical-Skill": 0.32, "Hardware-Systems": 0.3}
            },
            {
                "option_id": 1625,
                "option_text": "Manage the crew to keep calm and organized",
                "trait_tags": {"People-Skill": 1.0, "Admin-Skill": 0.8, "Social": 0.45, "Patient-Care": 0.4, "Teaching-Ed": 0.4, "Hospitality-Svc": 0.4}
            },
            {
                "option_id": 1626,
                "option_text": "Assess cargo damage and safety protocols",
                "trait_tags": {"Industrial-Ops": 1.0, "Maritime-Sea": 0.8, "Realistic": 0.36, "Analytical-Skill": 0.35, "Physical-Skill": 0.32, "Enterprising": 0.3}
            },
            {
                "option_id": 1627,
                "option_text": "Document the incident for insurance and legal records",
                "trait_tags": {"Legal-Practice": 1.0, "Admin-Skill": 0.8, "Conventional": 0.36, "Enterprising": 0.35, "Analytical-Skill": 0.35, "People-Skill": 0.3}
            },
            {
                "option_id": 1628,
                "option_text": "Provide first aid to any injured crew members",
                "trait_tags": {"Patient-Care": 1.0, "Physical-Skill": 0.8, "People-Skill": 0.45, "Social": 0.4, "Realistic": 0.32, "Rehab-Therapy": 0.3}
            }
        ]
    },
    {
        "question_id": 163,
        "question_text": "A Boracay resort asks you to improve their guest experience. What do you focus on?",
        "category": "Situational - Resort Management",
        "options": [
            {
                "option_id": 1631,
                "option_text": "Revamp the menu with local Filipino cuisine",
                "trait_tags": {"Culinary-Arts": 1.0, "Hospitality-Svc": 0.8, "People-Skill": 0.36, "Creative-Skill": 0.35, "Tourism-Travel": 0.32, "Artistic": 0.3}
            },
            {
                "option_id": 1632,
                "option_text": "Create exciting tour packages and activities",
                "trait_tags": {"Tourism-Travel": 1.0, "Hospitality-Svc": 0.8, "People-Skill": 0.4, "Enterprising": 0.35, "Marketing-Sales": 0.25, "Culinary-Arts": 0.24}
            },
            {
                "option_id": 1633,
                "option_text": "Train staff for world-class customer service",
                "trait_tags": {"HR-Management": 1.0, "Hospitality-Svc": 0.8, "People-Skill": 0.4, "Social": 0.35, "Enterprising": 0.35, "Admin-Skill": 0.35}
            },
            {
                "option_id": 1634,
                "option_text": "Design a beautiful website for online bookings",
                "trait_tags": {"Web-Dev": 1.0, "Marketing-Sales": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Enterprising": 0.36, "Investigative": 0.35}
            },
            {
                "option_id": 1635,
                "option_text": "Manage the resort's finances and operations",
                "trait_tags": {"Admin-Skill": 1.0, "Finance-Acct": 0.8, "Conventional": 0.45, "Analytical-Skill": 0.32, "Hospitality-Svc": 0.2, "Startup-Venture": 0.16}
            },
            {
                "option_id": 1636,
                "option_text": "Ensure environmental sustainability of the resort",
                "trait_tags": {"Environmental-Sci": 1.0, "Hospitality-Svc": 0.8, "Investigative": 0.45, "Field-Research": 0.4, "People-Skill": 0.36, "Tourism-Travel": 0.32}
            },
            {
                "option_id": 1637,
                "option_text": "Create Instagram-worthy interiors and spaces",
                "trait_tags": {"Spatial-Design": 1.0, "Visual-Design": 0.8, "Artistic": 0.36, "Creative-Skill": 0.36, "Civil-Build": 0.25, "Digital-Media": 0.24}
            },
            {
                "option_id": 1638,
                "option_text": "Set up a spa and wellness program",
                "trait_tags": {"Rehab-Therapy": 1.0, "Hospitality-Svc": 0.8, "Physical-Skill": 0.4, "People-Skill": 0.36, "Social": 0.35, "Tourism-Travel": 0.32}
            }
        ]
    },
    {
        "question_id": 164,
        "question_text": "You're organizing a Philippine food festival. What's your main responsibility?",
        "category": "Situational - Festival Planning",
        "options": [
            {
                "option_id": 1641,
                "option_text": "Curating the food stalls and menu selection",
                "trait_tags": {"Culinary-Arts": 1.0, "Hospitality-Svc": 0.8, "People-Skill": 0.36, "Creative-Skill": 0.35, "Tourism-Travel": 0.32, "Artistic": 0.3}
            },
            {
                "option_id": 1642,
                "option_text": "Marketing the event through flyers and social media",
                "trait_tags": {"Marketing-Sales": 1.0, "Film-Broadcast": 0.8, "Enterprising": 0.45, "People-Skill": 0.4, "Artistic": 0.32, "Creative-Skill": 0.32}
            },
            {
                "option_id": 1643,
                "option_text": "Managing the event budget and vendor payments",
                "trait_tags": {"Finance-Acct": 1.0, "Admin-Skill": 0.8, "Conventional": 0.45, "Analytical-Skill": 0.4, "Startup-Venture": 0.2, "Hospitality-Svc": 0.16}
            },
            {
                "option_id": 1644,
                "option_text": "Coordinating live entertainment and performances",
                "trait_tags": {"Performing-Arts": 1.0, "Admin-Skill": 0.8, "Artistic": 0.45, "Creative-Skill": 0.45, "Conventional": 0.36, "People-Skill": 0.3}
            },
            {
                "option_id": 1645,
                "option_text": "Setting up the venue layout and decorations",
                "trait_tags": {"Spatial-Design": 1.0, "Creative-Skill": 0.8, "Artistic": 0.36, "Visual-Design": 0.32, "Digital-Media": 0.32, "Civil-Build": 0.25}
            },
            {
                "option_id": 1646,
                "option_text": "Ensuring food safety and hygiene standards",
                "trait_tags": {"Food-Science": 1.0, "Public-Health": 0.8, "Investigative": 0.4, "Lab-Research": 0.35, "Nutrition-Diet": 0.35, "Social": 0.32}
            },
            {
                "option_id": 1647,
                "option_text": "Selling tickets and managing the entrance",
                "trait_tags": {"Admin-Skill": 1.0, "Marketing-Sales": 0.8, "Conventional": 0.45, "Enterprising": 0.36, "People-Skill": 0.32, "Finance-Acct": 0.3}
            },
            {
                "option_id": 1648,
                "option_text": "Filming and live-streaming the event",
                "trait_tags": {"Film-Broadcast": 1.0, "Digital-Media": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Visual-Design": 0.25, "Technical-Skill": 0.2}
            }
        ]
    },
    {
        "question_id": 165,
        "question_text": "If you could start any online business tomorrow, what would it be?",
        "category": "Entrepreneurship Vision",
        "options": [
            {
                "option_id": 1651,
                "option_text": "An e-commerce store selling Filipino products",
                "trait_tags": {"Startup-Venture": 1.0, "Web-Dev": 0.8, "Enterprising": 0.45, "Technical-Skill": 0.36, "Software-Dev": 0.36, "People-Skill": 0.3}
            },
            {
                "option_id": 1652,
                "option_text": "A freelance graphic design service",
                "trait_tags": {"Visual-Design": 1.0, "Startup-Venture": 0.8, "Artistic": 0.45, "Creative-Skill": 0.45, "Enterprising": 0.36, "Digital-Media": 0.3}
            },
            {
                "option_id": 1653,
                "option_text": "An online tutoring platform",
                "trait_tags": {"Teaching-Ed": 1.0, "Web-Dev": 0.8, "Social": 0.45, "People-Skill": 0.45, "Technical-Skill": 0.36, "Investigative": 0.28}
            },
            {
                "option_id": 1654,
                "option_text": "A food delivery service for home-cooked meals",
                "trait_tags": {"Culinary-Arts": 1.0, "Startup-Venture": 0.8, "Enterprising": 0.36, "Creative-Skill": 0.35, "Hospitality-Svc": 0.35, "Artistic": 0.3}
            },
            {
                "option_id": 1655,
                "option_text": "A tech consulting company",
                "trait_tags": {"Software-Dev": 1.0, "Startup-Venture": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Enterprising": 0.36, "Data-Analytics": 0.3}
            },
            {
                "option_id": 1656,
                "option_text": "A travel vlog and tourism promotion channel",
                "trait_tags": {"Tourism-Travel": 1.0, "Film-Broadcast": 0.8, "People-Skill": 0.4, "Hospitality-Svc": 0.4, "Enterprising": 0.35, "Artistic": 0.32}
            },
            {
                "option_id": 1657,
                "option_text": "A fitness coaching and workout plan service",
                "trait_tags": {"Sports-Ed": 1.0, "Startup-Venture": 0.8, "Physical-Skill": 0.45, "Enterprising": 0.36, "Social": 0.35, "Teaching-Ed": 0.35}
            },
            {
                "option_id": 1658,
                "option_text": "A virtual mental health counseling platform",
                "trait_tags": {"Counseling": 1.0, "Web-Dev": 0.8, "Social": 0.45, "People-Skill": 0.45, "Technical-Skill": 0.36, "Teaching-Ed": 0.3}
            }
        ]
    },
    {
        "question_id": 166,
        "question_text": "What kind of volunteer work appeals to you the most?",
        "category": "Values - Volunteering",
        "options": [
            {
                "option_id": 1661,
                "option_text": "Teaching in remote areas with no schools",
                "trait_tags": {"Teaching-Ed": 1.0, "Community-Serve": 0.8, "Social": 0.45, "People-Skill": 0.45, "Patient-Care": 0.16, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 1662,
                "option_text": "Medical missions in underserved communities",
                "trait_tags": {"Patient-Care": 1.0, "Public-Health": 0.8, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.28}
            },
            {
                "option_id": 1663,
                "option_text": "Building houses through Habitat for Humanity",
                "trait_tags": {"Civil-Build": 1.0, "Community-Serve": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Social": 0.36, "People-Skill": 0.32}
            },
            {
                "option_id": 1664,
                "option_text": "Environmental cleanup and tree planting",
                "trait_tags": {"Environmental-Sci": 1.0, "Agri-Nature": 0.8, "Investigative": 0.45, "Field-Research": 0.4, "Realistic": 0.36, "Environmental-Eng": 0.3}
            },
            {
                "option_id": 1665,
                "option_text": "Feeding programs for malnourished children",
                "trait_tags": {"Nutrition-Diet": 1.0, "Social-Work": 0.8, "Social": 0.36, "People-Skill": 0.36, "Food-Science": 0.35, "Community-Serve": 0.32}
            },
            {
                "option_id": 1666,
                "option_text": "Teaching computer literacy to senior citizens",
                "trait_tags": {"Software-Dev": 1.0, "Teaching-Ed": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Social": 0.36, "People-Skill": 0.36}
            },
            {
                "option_id": 1667,
                "option_text": "Legal aid for those who can't afford lawyers",
                "trait_tags": {"Legal-Practice": 1.0, "Social-Work": 0.8, "People-Skill": 0.36, "Social": 0.36, "Enterprising": 0.35, "Analytical-Skill": 0.35}
            },
            {
                "option_id": 1668,
                "option_text": "Organizing sports clinics for youth",
                "trait_tags": {"Sports-Ed": 1.0, "Community-Serve": 0.8, "Physical-Skill": 0.45, "Social": 0.36, "Teaching-Ed": 0.35, "People-Skill": 0.32}
            }
        ]
    },
    {
        "question_id": 167,
        "question_text": "What would you study about the Philippines if you could do research?",
        "category": "Research Interest",
        "options": [
            {
                "option_id": 1671,
                "option_text": "How to make Filipino agriculture more productive",
                "trait_tags": {"Agri-Nature": 1.0, "Lab-Research": 0.8, "Realistic": 0.45, "Investigative": 0.36, "Analytical-Skill": 0.36, "Physical-Skill": 0.35}
            },
            {
                "option_id": 1672,
                "option_text": "How social media affects Filipino youth mental health",
                "trait_tags": {"Counseling": 1.0, "Data-Analytics": 0.8, "Social": 0.45, "People-Skill": 0.45, "Investigative": 0.36, "Analytical-Skill": 0.36}
            },
            {
                "option_id": 1673,
                "option_text": "How to combat plastic pollution in Philippine seas",
                "trait_tags": {"Environmental-Sci": 1.0, "Field-Research": 0.8, "Investigative": 0.45, "Environmental-Eng": 0.3, "Lab-Research": 0.25, "Agri-Nature": 0.25}
            },
            {
                "option_id": 1674,
                "option_text": "How AI can improve healthcare access in rural areas",
                "trait_tags": {"AI-ML": 1.0, "Public-Health": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Data-Analytics": 0.4, "Software-Dev": 0.35}
            },
            {
                "option_id": 1675,
                "option_text": "How to make Philippine businesses globally competitive",
                "trait_tags": {"Startup-Venture": 1.0, "Marketing-Sales": 0.8, "Enterprising": 0.45, "People-Skill": 0.32, "Finance-Acct": 0.2, "Creative-Skill": 0.2}
            },
            {
                "option_id": 1676,
                "option_text": "The history and preservation of Filipino indigenous cultures",
                "trait_tags": {"Community-Serve": 1.0, "Field-Research": 0.8, "Social": 0.45, "People-Skill": 0.4, "Investigative": 0.32, "Teaching-Ed": 0.25}
            },
            {
                "option_id": 1677,
                "option_text": "How to reduce traffic congestion in Metro Manila",
                "trait_tags": {"Civil-Build": 1.0, "Data-Analytics": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Investigative": 0.36, "Analytical-Skill": 0.36}
            },
            {
                "option_id": 1678,
                "option_text": "Developing Filipino language technology and NLP",
                "trait_tags": {"AI-ML": 1.0, "Teaching-Ed": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Data-Analytics": 0.4, "Social": 0.36}
            }
        ]
    },
    {
        "question_id": 168,
        "question_text": "Your group project is about climate change. Which part do you want to handle?",
        "category": "Situational - Group Research",
        "options": [
            {
                "option_id": 1681,
                "option_text": "Collecting data and running statistical analysis",
                "trait_tags": {"Data-Analytics": 1.0, "Environmental-Sci": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Field-Research": 0.32, "Software-Dev": 0.3}
            },
            {
                "option_id": 1682,
                "option_text": "Doing field research and environmental surveys",
                "trait_tags": {"Field-Research": 1.0, "Environmental-Sci": 0.8, "Investigative": 0.4, "Agri-Nature": 0.3, "Analytical-Skill": 0.3, "Physical-Skill": 0.25}
            },
            {
                "option_id": 1683,
                "option_text": "Creating the visual presentation and infographics",
                "trait_tags": {"Visual-Design": 1.0, "Digital-Media": 0.8, "Artistic": 0.45, "Creative-Skill": 0.45, "Spatial-Design": 0.25, "Software-Dev": 0.16}
            },
            {
                "option_id": 1684,
                "option_text": "Writing the research paper and conclusions",
                "trait_tags": {"Analytical-Skill": 1.0, "Teaching-Ed": 0.8, "Investigative": 0.45, "Data-Analytics": 0.4, "Social": 0.36, "People-Skill": 0.36}
            },
            {
                "option_id": 1685,
                "option_text": "Presenting and defending the findings",
                "trait_tags": {"People-Skill": 1.0, "Performing-Arts": 0.8, "Social": 0.45, "Patient-Care": 0.4, "Teaching-Ed": 0.4, "Hospitality-Svc": 0.4}
            },
            {
                "option_id": 1686,
                "option_text": "Building a working prototype solution",
                "trait_tags": {"Environmental-Eng": 1.0, "Hardware-Systems": 0.8, "Realistic": 0.4, "Technical-Skill": 0.36, "Environmental-Sci": 0.35, "Civil-Build": 0.25}
            },
            {
                "option_id": 1687,
                "option_text": "Recording a documentary video about the topic",
                "trait_tags": {"Film-Broadcast": 1.0, "Environmental-Sci": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Digital-Media": 0.4, "Investigative": 0.36}
            },
            {
                "option_id": 1688,
                "option_text": "Organizing the group tasks and deadlines",
                "trait_tags": {"Admin-Skill": 1.0, "People-Skill": 0.8, "Conventional": 0.45, "Social": 0.36, "Hospitality-Svc": 0.32, "Teaching-Ed": 0.32}
            }
        ]
    },
    {
        "question_id": 169,
        "question_text": "If your LGU gave you a budget to improve your barangay, what would you prioritize?",
        "category": "Situational - Community Development",
        "options": [
            {
                "option_id": 1691,
                "option_text": "Build a community health center",
                "trait_tags": {"Public-Health": 1.0, "Civil-Build": 0.8, "Social": 0.4, "Realistic": 0.36, "Analytical-Skill": 0.35, "Community-Serve": 0.35}
            },
            {
                "option_id": 1692,
                "option_text": "Set up free Wi-Fi and a computer lab",
                "trait_tags": {"Cloud-Systems": 1.0, "Teaching-Ed": 0.8, "Technical-Skill": 0.45, "Social": 0.36, "People-Skill": 0.36, "Software-Dev": 0.35}
            },
            {
                "option_id": 1693,
                "option_text": "Create a livelihood training center",
                "trait_tags": {"Startup-Venture": 1.0, "Teaching-Ed": 0.8, "Enterprising": 0.45, "People-Skill": 0.36, "Social": 0.36, "Marketing-Sales": 0.3}
            },
            {
                "option_id": 1694,
                "option_text": "Improve the roads and drainage system",
                "trait_tags": {"Civil-Build": 1.0, "Environmental-Eng": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Environmental-Sci": 0.28, "Spatial-Design": 0.25}
            },
            {
                "option_id": 1695,
                "option_text": "Build a basketball court and sports facilities",
                "trait_tags": {"Sports-Ed": 1.0, "Physical-Skill": 0.8, "Social": 0.35, "Teaching-Ed": 0.35, "Realistic": 0.32, "Maritime-Sea": 0.28}
            },
            {
                "option_id": 1696,
                "option_text": "Create a daycare and after-school program",
                "trait_tags": {"Teaching-Ed": 1.0, "Social-Work": 0.8, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.32, "Counseling": 0.24}
            },
            {
                "option_id": 1697,
                "option_text": "Install streetlights and CCTV for safety",
                "trait_tags": {"Electrical-Power": 1.0, "Law-Enforce": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3, "Physical-Skill": 0.28}
            },
            {
                "option_id": 1698,
                "option_text": "Start a community garden and food program",
                "trait_tags": {"Agri-Nature": 1.0, "Nutrition-Diet": 0.8, "Realistic": 0.45, "Physical-Skill": 0.35, "Food-Science": 0.28, "Field-Research": 0.25}
            }
        ]
    },
    {
        "question_id": 170,
        "question_text": "What kind of YouTube channel would you create?",
        "category": "Content Creation Interest",
        "options": [
            {
                "option_id": 1701,
                "option_text": "Coding tutorials and tech reviews",
                "trait_tags": {"Software-Dev": 1.0, "Film-Broadcast": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Digital-Media": 0.32, "Artistic": 0.32}
            },
            {
                "option_id": 1702,
                "option_text": "Cooking shows featuring Filipino recipes",
                "trait_tags": {"Culinary-Arts": 1.0, "Film-Broadcast": 0.8, "Creative-Skill": 0.35, "Hospitality-Svc": 0.35, "Artistic": 0.32, "Digital-Media": 0.32}
            },
            {
                "option_id": 1703,
                "option_text": "Science experiments and educational content",
                "trait_tags": {"Lab-Research": 1.0, "Teaching-Ed": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Social": 0.36, "People-Skill": 0.36}
            },
            {
                "option_id": 1704,
                "option_text": "True crime and forensic analysis",
                "trait_tags": {"Forensic-Sci": 1.0, "Film-Broadcast": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.4, "Lab-Research": 0.35, "Law-Enforce": 0.35}
            },
            {
                "option_id": 1705,
                "option_text": "Travel vlogs of Philippine destinations",
                "trait_tags": {"Tourism-Travel": 1.0, "Film-Broadcast": 0.8, "People-Skill": 0.4, "Hospitality-Svc": 0.4, "Enterprising": 0.35, "Artistic": 0.32}
            },
            {
                "option_id": 1706,
                "option_text": "Fitness workouts and health tips",
                "trait_tags": {"Sports-Ed": 1.0, "Film-Broadcast": 0.8, "Physical-Skill": 0.45, "Social": 0.35, "Teaching-Ed": 0.35, "Artistic": 0.32}
            },
            {
                "option_id": 1707,
                "option_text": "Art tutorials and design process videos",
                "trait_tags": {"Visual-Design": 1.0, "Film-Broadcast": 0.8, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.32, "Spatial-Design": 0.25}
            },
            {
                "option_id": 1708,
                "option_text": "Business advice and entrepreneurship tips",
                "trait_tags": {"Startup-Venture": 1.0, "Film-Broadcast": 0.8, "Enterprising": 0.45, "Creative-Skill": 0.32, "Artistic": 0.32, "Digital-Media": 0.32}
            }
        ]
    },
    {
        "question_id": 171,
        "question_text": "What makes you feel most accomplished at the end of a day?",
        "category": "Values - Accomplishment",
        "options": [
            {
                "option_id": 1711,
                "option_text": "Solving a difficult technical problem",
                "trait_tags": {"Software-Dev": 1.0, "Analytical-Skill": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.32, "Lab-Research": 0.28}
            },
            {
                "option_id": 1712,
                "option_text": "Helping someone feel better emotionally or physically",
                "trait_tags": {"Patient-Care": 1.0, "Counseling": 0.8, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.25}
            },
            {
                "option_id": 1713,
                "option_text": "Creating something beautiful or artistic",
                "trait_tags": {"Visual-Design": 1.0, "Creative-Skill": 0.8, "Artistic": 0.45, "Digital-Media": 0.32, "Spatial-Design": 0.28}
            },
            {
                "option_id": 1714,
                "option_text": "Closing a deal or making a sale",
                "trait_tags": {"Marketing-Sales": 1.0, "Startup-Venture": 0.8, "Enterprising": 0.45, "People-Skill": 0.4, "Hospitality-Svc": 0.2, "Finance-Acct": 0.16}
            },
            {
                "option_id": 1715,
                "option_text": "Teaching someone something they finally understand",
                "trait_tags": {"Teaching-Ed": 1.0, "People-Skill": 0.8, "Social": 0.45, "Patient-Care": 0.32, "Hospitality-Svc": 0.32, "Community-Serve": 0.25}
            },
            {
                "option_id": 1716,
                "option_text": "Discovering new facts through research",
                "trait_tags": {"Lab-Research": 1.0, "Field-Research": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Medical-Lab": 0.3, "Data-Analytics": 0.25}
            },
            {
                "option_id": 1717,
                "option_text": "Completing a physical challenge or workout",
                "trait_tags": {"Physical-Skill": 1.0, "Sports-Ed": 0.8, "Realistic": 0.4, "Maritime-Sea": 0.35, "Agri-Nature": 0.35, "Law-Enforce": 0.3}
            },
            {
                "option_id": 1718,
                "option_text": "Organizing a messy situation into order",
                "trait_tags": {"Admin-Skill": 1.0, "Industrial-Ops": 0.8, "Conventional": 0.45, "Finance-Acct": 0.3, "Analytical-Skill": 0.28, "Enterprising": 0.24}
            }
        ]
    },
    {
        "question_id": 172,
        "question_text": "Which school subject combination do you enjoy the most?",
        "category": "Academic Interest",
        "options": [
            {
                "option_id": 1721,
                "option_text": "Biology and Chemistry",
                "trait_tags": {"Lab-Research": 1.0, "Medical-Lab": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Field-Research": 0.25, "Data-Analytics": 0.25}
            },
            {
                "option_id": 1722,
                "option_text": "Mathematics and Physics",
                "trait_tags": {"Data-Analytics": 1.0, "Mechanical-Design": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Realistic": 0.36, "Technical-Skill": 0.32}
            },
            {
                "option_id": 1723,
                "option_text": "Computer Science and Math",
                "trait_tags": {"Software-Dev": 1.0, "AI-ML": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Analytical-Skill": 0.36, "Data-Analytics": 0.32}
            },
            {
                "option_id": 1724,
                "option_text": "History and Social Studies",
                "trait_tags": {"Community-Serve": 1.0, "Teaching-Ed": 0.8, "Social": 0.45, "People-Skill": 0.4, "Patient-Care": 0.2, "Law-Enforce": 0.15}
            },
            {
                "option_id": 1725,
                "option_text": "Art and Music",
                "trait_tags": {"Visual-Design": 1.0, "Performing-Arts": 0.8, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            },
            {
                "option_id": 1726,
                "option_text": "English and Filipino Literature",
                "trait_tags": {"Creative-Skill": 1.0, "Teaching-Ed": 0.8, "Artistic": 0.45, "Visual-Design": 0.4, "Digital-Media": 0.4, "Social": 0.36}
            },
            {
                "option_id": 1727,
                "option_text": "Physical Education and Health",
                "trait_tags": {"Sports-Ed": 1.0, "Public-Health": 0.8, "Physical-Skill": 0.45, "Social": 0.35, "Teaching-Ed": 0.35, "Analytical-Skill": 0.28}
            },
            {
                "option_id": 1728,
                "option_text": "Business and Economics",
                "trait_tags": {"Finance-Acct": 1.0, "Startup-Venture": 0.8, "Conventional": 0.45, "Analytical-Skill": 0.4, "Enterprising": 0.36, "Admin-Skill": 0.3}
            }
        ]
    },
    {
        "question_id": 173,
        "question_text": "What kind of leader are you in a group project?",
        "category": "Leadership Style",
        "options": [
            {
                "option_id": 1731,
                "option_text": "The organizer who makes checklists and timelines",
                "trait_tags": {"Admin-Skill": 1.0, "Industrial-Ops": 0.8, "Conventional": 0.45, "Finance-Acct": 0.3, "Analytical-Skill": 0.28, "Enterprising": 0.24}
            },
            {
                "option_id": 1732,
                "option_text": "The creative one with all the ideas",
                "trait_tags": {"Creative-Skill": 1.0, "Startup-Venture": 0.8, "Artistic": 0.45, "Visual-Design": 0.4, "Digital-Media": 0.4, "Enterprising": 0.36}
            },
            {
                "option_id": 1733,
                "option_text": "The researcher who digs deep into the topic",
                "trait_tags": {"Lab-Research": 1.0, "Analytical-Skill": 0.8, "Investigative": 0.45, "Data-Analytics": 0.32, "Medical-Lab": 0.3, "Field-Research": 0.25}
            },
            {
                "option_id": 1734,
                "option_text": "The tech person handling presentations and tools",
                "trait_tags": {"Software-Dev": 1.0, "Digital-Media": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Artistic": 0.32, "Creative-Skill": 0.32}
            },
            {
                "option_id": 1735,
                "option_text": "The motivator who keeps everyone going",
                "trait_tags": {"People-Skill": 1.0, "Teaching-Ed": 0.8, "Social": 0.45, "Patient-Care": 0.4, "Hospitality-Svc": 0.4, "Enterprising": 0.3}
            },
            {
                "option_id": 1736,
                "option_text": "The negotiator who deals with disagreements",
                "trait_tags": {"HR-Management": 1.0, "Counseling": 0.8, "People-Skill": 0.4, "Social": 0.36, "Enterprising": 0.35, "Admin-Skill": 0.35}
            },
            {
                "option_id": 1737,
                "option_text": "The presenter who speaks in front of the class",
                "trait_tags": {"People-Skill": 1.0, "Performing-Arts": 0.8, "Social": 0.45, "Patient-Care": 0.4, "Teaching-Ed": 0.4, "Hospitality-Svc": 0.4}
            },
            {
                "option_id": 1738,
                "option_text": "The hands-on builder who makes the prototype",
                "trait_tags": {"Hardware-Systems": 1.0, "Mechanical-Design": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Electrical-Power": 0.3, "Software-Dev": 0.2}
            }
        ]
    },
    {
        "question_id": 174,
        "question_text": "What career do you imagine yourself in 10 years from now?",
        "category": "Future Vision",
        "options": [
            {
                "option_id": 1741,
                "option_text": "Running my own tech startup",
                "trait_tags": {"Startup-Venture": 1.0, "Software-Dev": 0.8, "Enterprising": 0.45, "Technical-Skill": 0.36, "Investigative": 0.32, "People-Skill": 0.3}
            },
            {
                "option_id": 1742,
                "option_text": "A doctor or specialist in a hospital",
                "trait_tags": {"Patient-Care": 1.0, "Medical-Lab": 0.8, "People-Skill": 0.45, "Social": 0.4, "Analytical-Skill": 0.36, "Investigative": 0.32}
            },
            {
                "option_id": 1743,
                "option_text": "A licensed engineer on major projects",
                "trait_tags": {"Civil-Build": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Industrial-Ops": 0.2}
            },
            {
                "option_id": 1744,
                "option_text": "A teacher or professor at a university",
                "trait_tags": {"Teaching-Ed": 1.0, "Lab-Research": 0.8, "Social": 0.45, "People-Skill": 0.45, "Investigative": 0.36, "Analytical-Skill": 0.36}
            },
            {
                "option_id": 1745,
                "option_text": "A famous artist or content creator",
                "trait_tags": {"Visual-Design": 1.0, "Film-Broadcast": 0.8, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.32, "Spatial-Design": 0.25}
            },
            {
                "option_id": 1746,
                "option_text": "A lawyer or judge fighting for justice",
                "trait_tags": {"Legal-Practice": 1.0, "Law-Enforce": 0.8, "Enterprising": 0.35, "Analytical-Skill": 0.35, "People-Skill": 0.3, "Realistic": 0.28}
            },
            {
                "option_id": 1747,
                "option_text": "A scientist making groundbreaking discoveries",
                "trait_tags": {"Lab-Research": 1.0, "Environmental-Sci": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Field-Research": 0.32, "Medical-Lab": 0.3}
            },
            {
                "option_id": 1748,
                "option_text": "A successful business executive or CEO",
                "trait_tags": {"Finance-Acct": 1.0, "Startup-Venture": 0.8, "Conventional": 0.45, "Analytical-Skill": 0.4, "Enterprising": 0.36, "Admin-Skill": 0.3}
            },
            {
                "option_id": 1749,
                "option_text": "A chef or restaurant owner",
                "trait_tags": {"Culinary-Arts": 1.0, "Startup-Venture": 0.8, "Enterprising": 0.36, "Creative-Skill": 0.35, "Hospitality-Svc": 0.35, "Artistic": 0.3}
            },
            {
                "option_id": 1750,
                "option_text": "A sports coach or fitness expert",
                "trait_tags": {"Sports-Ed": 1.0, "Teaching-Ed": 0.8, "Physical-Skill": 0.45, "Social": 0.36, "People-Skill": 0.36, "Rehab-Therapy": 0.2}
            }
        ]
    },
    {
        "question_id": 175,
        "question_text": "What problem in the Philippines do you most want to help solve?",
        "category": "Philippine Issues",
        "options": [
            {
                "option_id": 1751,
                "option_text": "Poverty and unemployment",
                "trait_tags": {"Social-Work": 1.0, "Startup-Venture": 0.8, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.4, "Enterprising": 0.36}
            },
            {
                "option_id": 1752,
                "option_text": "Climate change and typhoon damage",
                "trait_tags": {"Environmental-Sci": 1.0, "Environmental-Eng": 0.8, "Investigative": 0.45, "Field-Research": 0.4, "Realistic": 0.32, "Technical-Skill": 0.28}
            },
            {
                "option_id": 1753,
                "option_text": "Poor access to quality education",
                "trait_tags": {"Teaching-Ed": 1.0, "Software-Dev": 0.8, "Social": 0.45, "People-Skill": 0.45, "Technical-Skill": 0.36, "Investigative": 0.32}
            },
            {
                "option_id": 1754,
                "option_text": "Corruption and poor governance",
                "trait_tags": {"Legal-Practice": 1.0, "Community-Serve": 0.8, "Social": 0.36, "Enterprising": 0.35, "Analytical-Skill": 0.35, "People-Skill": 0.32}
            },
            {
                "option_id": 1755,
                "option_text": "Food insecurity and hunger",
                "trait_tags": {"Agri-Nature": 1.0, "Nutrition-Diet": 0.8, "Realistic": 0.45, "Physical-Skill": 0.35, "Food-Science": 0.28, "Field-Research": 0.25}
            },
            {
                "option_id": 1756,
                "option_text": "Lack of access to healthcare in rural areas",
                "trait_tags": {"Public-Health": 1.0, "Patient-Care": 0.8, "Social": 0.4, "People-Skill": 0.36, "Analytical-Skill": 0.35, "Community-Serve": 0.35}
            },
            {
                "option_id": 1757,
                "option_text": "Traffic and poor transportation systems",
                "trait_tags": {"Civil-Build": 1.0, "Industrial-Ops": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Analytical-Skill": 0.28, "Spatial-Design": 0.25}
            },
            {
                "option_id": 1758,
                "option_text": "Cybercrime and online fraud",
                "trait_tags": {"Cyber-Defense": 1.0, "Law-Enforce": 0.8, "Technical-Skill": 0.4, "Investigative": 0.35, "Realistic": 0.28, "Physical-Skill": 0.28}
            },
            {
                "option_id": 1759,
                "option_text": "Drug abuse and addiction",
                "trait_tags": {"Counseling": 1.0, "Public-Health": 0.8, "Social": 0.45, "People-Skill": 0.45, "Teaching-Ed": 0.3, "Community-Serve": 0.28}
            },
            {
                "option_id": 1760,
                "option_text": "Environmental destruction and deforestation",
                "trait_tags": {"Environmental-Sci": 1.0, "Agri-Nature": 0.8, "Investigative": 0.45, "Field-Research": 0.4, "Realistic": 0.36, "Environmental-Eng": 0.3}
            }
        ]
    },
    {
        "question_id": 176,
        "question_text": "If you receive a scholarship abroad, what would you study?",
        "category": "Study Abroad Interest",
        "options": [
            {
                "option_id": 1761,
                "option_text": "Computer science or artificial intelligence",
                "trait_tags": {"AI-ML": 1.0, "Software-Dev": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Data-Analytics": 0.4, "Technical-Skill": 0.36}
            },
            {
                "option_id": 1762,
                "option_text": "Medicine or public health",
                "trait_tags": {"Patient-Care": 1.0, "Public-Health": 0.8, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.28}
            },
            {
                "option_id": 1763,
                "option_text": "Engineering or architecture",
                "trait_tags": {"Civil-Build": 1.0, "Spatial-Design": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Artistic": 0.28, "Creative-Skill": 0.28}
            },
            {
                "option_id": 1764,
                "option_text": "Business administration or finance",
                "trait_tags": {"Finance-Acct": 1.0, "Startup-Venture": 0.8, "Conventional": 0.45, "Analytical-Skill": 0.4, "Enterprising": 0.36, "Admin-Skill": 0.3}
            },
            {
                "option_id": 1765,
                "option_text": "Film, animation, or digital arts",
                "trait_tags": {"Film-Broadcast": 1.0, "Animation-3D": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Digital-Media": 0.4, "Game-Dev": 0.28}
            },
            {
                "option_id": 1766,
                "option_text": "Law or political science",
                "trait_tags": {"Legal-Practice": 1.0, "Community-Serve": 0.8, "Social": 0.36, "Enterprising": 0.35, "Analytical-Skill": 0.35, "People-Skill": 0.32}
            },
            {
                "option_id": 1767,
                "option_text": "Environmental science or marine biology",
                "trait_tags": {"Environmental-Sci": 1.0, "Field-Research": 0.8, "Investigative": 0.45, "Environmental-Eng": 0.3, "Lab-Research": 0.25, "Agri-Nature": 0.25}
            },
            {
                "option_id": 1768,
                "option_text": "Culinary arts or hospitality management",
                "trait_tags": {"Culinary-Arts": 1.0, "Tourism-Travel": 0.8, "Creative-Skill": 0.35, "Hospitality-Svc": 0.35, "People-Skill": 0.32, "Artistic": 0.3}
            },
            {
                "option_id": 1769,
                "option_text": "Psychology or counseling",
                "trait_tags": {"Counseling": 1.0, "Rehab-Therapy": 0.8, "Social": 0.45, "People-Skill": 0.45, "Physical-Skill": 0.32, "Teaching-Ed": 0.3}
            },
            {
                "option_id": 1770,
                "option_text": "Sports science or physical therapy",
                "trait_tags": {"Sports-Ed": 1.0, "Rehab-Therapy": 0.8, "Physical-Skill": 0.45, "Social": 0.35, "Teaching-Ed": 0.35, "People-Skill": 0.28}
            }
        ]
    },
    {
        "question_id": 177,
        "question_text": "What's your favorite way to learn something new?",
        "category": "Learning Style",
        "options": [
            {
                "option_id": 1771,
                "option_text": "Building something hands-on and experimenting",
                "trait_tags": {"Hardware-Systems": 1.0, "Mechanical-Design": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Electrical-Power": 0.3, "Software-Dev": 0.2}
            },
            {
                "option_id": 1772,
                "option_text": "Reading books and articles about the topic",
                "trait_tags": {"Lab-Research": 1.0, "Analytical-Skill": 0.8, "Investigative": 0.45, "Data-Analytics": 0.32, "Medical-Lab": 0.3, "Field-Research": 0.25}
            },
            {
                "option_id": 1773,
                "option_text": "Watching YouTube tutorials and demo videos",
                "trait_tags": {"Film-Broadcast": 1.0, "Digital-Media": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Visual-Design": 0.25, "Technical-Skill": 0.2}
            },
            {
                "option_id": 1774,
                "option_text": "Asking an expert and learning through conversation",
                "trait_tags": {"People-Skill": 1.0, "Teaching-Ed": 0.8, "Social": 0.45, "Patient-Care": 0.4, "Hospitality-Svc": 0.4, "Enterprising": 0.3}
            },
            {
                "option_id": 1775,
                "option_text": "Practicing by coding or creating projects",
                "trait_tags": {"Software-Dev": 1.0, "Web-Dev": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25}
            },
            {
                "option_id": 1776,
                "option_text": "Drawing diagrams and visual notes",
                "trait_tags": {"Visual-Design": 1.0, "Spatial-Design": 0.8, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Technical-Skill": 0.16}
            },
            {
                "option_id": 1777,
                "option_text": "Going outdoors and experiencing firsthand",
                "trait_tags": {"Field-Research": 1.0, "Physical-Skill": 0.8, "Investigative": 0.4, "Realistic": 0.32, "Agri-Nature": 0.3, "Analytical-Skill": 0.3}
            },
            {
                "option_id": 1778,
                "option_text": "Taking online courses and quizzes",
                "trait_tags": {"Teaching-Ed": 1.0, "Software-Dev": 0.8, "Social": 0.45, "People-Skill": 0.45, "Technical-Skill": 0.36, "Investigative": 0.32}
            }
        ]
    },
    {
        "question_id": 178,
        "question_text": "What type of news story catches your attention most?",
        "category": "News Interest",
        "options": [
            {
                "option_id": 1781,
                "option_text": "New technology and gadget launches",
                "trait_tags": {"Hardware-Systems": 1.0, "Software-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Investigative": 0.32, "Electrical-Power": 0.3}
            },
            {
                "option_id": 1782,
                "option_text": "Medical breakthroughs and health news",
                "trait_tags": {"Patient-Care": 1.0, "Lab-Research": 0.8, "People-Skill": 0.45, "Social": 0.4, "Investigative": 0.36, "Analytical-Skill": 0.36}
            },
            {
                "option_id": 1783,
                "option_text": "Stock market and business news",
                "trait_tags": {"Finance-Acct": 1.0, "Marketing-Sales": 0.8, "Conventional": 0.45, "Analytical-Skill": 0.4, "Enterprising": 0.36, "People-Skill": 0.32}
            },
            {
                "option_id": 1784,
                "option_text": "Crime investigations and court cases",
                "trait_tags": {"Law-Enforce": 1.0, "Forensic-Sci": 0.8, "Investigative": 0.36, "Realistic": 0.35, "Physical-Skill": 0.35, "Analytical-Skill": 0.32}
            },
            {
                "option_id": 1785,
                "option_text": "Environmental issues and climate reports",
                "trait_tags": {"Environmental-Sci": 1.0, "Field-Research": 0.8, "Investigative": 0.45, "Environmental-Eng": 0.3, "Lab-Research": 0.25, "Agri-Nature": 0.25}
            },
            {
                "option_id": 1786,
                "option_text": "Sports results and athlete interviews",
                "trait_tags": {"Sports-Ed": 1.0, "Physical-Skill": 0.8, "Social": 0.35, "Teaching-Ed": 0.35, "Realistic": 0.32, "Maritime-Sea": 0.28}
            },
            {
                "option_id": 1787,
                "option_text": "Celebrity and entertainment news",
                "trait_tags": {"Performing-Arts": 1.0, "Film-Broadcast": 0.8, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.32, "People-Skill": 0.3}
            },
            {
                "option_id": 1788,
                "option_text": "Political news and government policies",
                "trait_tags": {"Community-Serve": 1.0, "Legal-Practice": 0.8, "Social": 0.45, "People-Skill": 0.4, "Enterprising": 0.28, "Analytical-Skill": 0.28}
            }
        ]
    },
    {
        "question_id": 179,
        "question_text": "What's your biggest strength in a team?",
        "category": "Team Strength",
        "options": [
            {
                "option_id": 1791,
                "option_text": "I fix technical problems quickly",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.8, "Investigative": 0.4, "Hardware-Systems": 0.32, "Data-Analytics": 0.3, "Realistic": 0.28}
            },
            {
                "option_id": 1792,
                "option_text": "I support my teammates emotionally",
                "trait_tags": {"Counseling": 1.0, "People-Skill": 0.8, "Social": 0.45, "Teaching-Ed": 0.32, "Patient-Care": 0.32, "Hospitality-Svc": 0.32}
            },
            {
                "option_id": 1793,
                "option_text": "I come up with creative solutions",
                "trait_tags": {"Creative-Skill": 1.0, "Startup-Venture": 0.8, "Artistic": 0.45, "Visual-Design": 0.4, "Digital-Media": 0.4, "Enterprising": 0.36}
            },
            {
                "option_id": 1794,
                "option_text": "I keep everything organized and on schedule",
                "trait_tags": {"Admin-Skill": 1.0, "Industrial-Ops": 0.8, "Conventional": 0.45, "Finance-Acct": 0.3, "Analytical-Skill": 0.28, "Enterprising": 0.24}
            },
            {
                "option_id": 1795,
                "option_text": "I do thorough research and fact-checking",
                "trait_tags": {"Lab-Research": 1.0, "Analytical-Skill": 0.8, "Investigative": 0.45, "Data-Analytics": 0.32, "Medical-Lab": 0.3, "Field-Research": 0.25}
            },
            {
                "option_id": 1796,
                "option_text": "I persuade others and build consensus",
                "trait_tags": {"Marketing-Sales": 1.0, "People-Skill": 0.8, "Enterprising": 0.45, "Social": 0.36, "Hospitality-Svc": 0.32, "Teaching-Ed": 0.32}
            },
            {
                "option_id": 1797,
                "option_text": "I do the physical work and hands-on tasks",
                "trait_tags": {"Physical-Skill": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.4, "Maritime-Sea": 0.35, "Agri-Nature": 0.35, "Technical-Skill": 0.32}
            },
            {
                "option_id": 1798,
                "option_text": "I present our work confidently to others",
                "trait_tags": {"Performing-Arts": 1.0, "People-Skill": 0.8, "Artistic": 0.45, "Creative-Skill": 0.45, "Social": 0.36, "Teaching-Ed": 0.32}
            }
        ]
    },
    {
        "question_id": 180,
        "question_text": "What would you invent if you had unlimited resources?",
        "category": "Innovation Vision",
        "options": [
            {
                "option_id": 1801,
                "option_text": "A robot nurse that helps hospital patients",
                "trait_tags": {"AI-ML": 1.0, "Patient-Care": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Data-Analytics": 0.4, "People-Skill": 0.36}
            },
            {
                "option_id": 1802,
                "option_text": "A machine that converts ocean plastic to fuel",
                "trait_tags": {"Environmental-Eng": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.4, "Technical-Skill": 0.35, "Environmental-Sci": 0.35, "Civil-Build": 0.25}
            },
            {
                "option_id": 1803,
                "option_text": "A virtual reality classroom for any subject",
                "trait_tags": {"Game-Dev": 1.0, "Teaching-Ed": 0.8, "Technical-Skill": 0.4, "Software-Dev": 0.4, "Social": 0.36, "People-Skill": 0.36}
            },
            {
                "option_id": 1804,
                "option_text": "A bulletproof emergency shelter for typhoons",
                "trait_tags": {"Civil-Build": 1.0, "Community-Serve": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Social": 0.36, "People-Skill": 0.32}
            },
            {
                "option_id": 1805,
                "option_text": "An app that translates all Filipino dialects",
                "trait_tags": {"AI-ML": 1.0, "Mobile-Dev": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Data-Analytics": 0.4, "Software-Dev": 0.36}
            },
            {
                "option_id": 1806,
                "option_text": "Vertical farms in cities to end hunger",
                "trait_tags": {"Agri-Nature": 1.0, "Environmental-Eng": 0.8, "Realistic": 0.45, "Physical-Skill": 0.35, "Technical-Skill": 0.28, "Environmental-Sci": 0.28}
            },
            {
                "option_id": 1807,
                "option_text": "A drone system for delivering medicine to remote areas",
                "trait_tags": {"Hardware-Systems": 1.0, "Public-Health": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Social": 0.32, "Electrical-Power": 0.3}
            },
            {
                "option_id": 1808,
                "option_text": "Smart clothes that monitor your health",
                "trait_tags": {"Hardware-Systems": 1.0, "Patient-Care": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "People-Skill": 0.36, "Social": 0.32}
            }
        ]
    },
    {
        "question_id": 181,
        "question_text": "What type of work environment makes you most productive?",
        "category": "Work Style",
        "options": [
            {
                "option_id": 1811,
                "option_text": "A quiet laboratory or research room",
                "trait_tags": {"Lab-Research": 1.0, "Analytical-Skill": 0.8, "Investigative": 0.45, "Data-Analytics": 0.32, "Medical-Lab": 0.3, "Field-Research": 0.25}
            },
            {
                "option_id": 1812,
                "option_text": "A busy hospital or clinic",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.8, "Social": 0.4, "Teaching-Ed": 0.32, "Hospitality-Svc": 0.32, "Rehab-Therapy": 0.3}
            },
            {
                "option_id": 1813,
                "option_text": "An open-plan tech office",
                "trait_tags": {"Software-Dev": 1.0, "Web-Dev": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25}
            },
            {
                "option_id": 1814,
                "option_text": "An outdoor construction or field site",
                "trait_tags": {"Civil-Build": 1.0, "Physical-Skill": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Agri-Nature": 0.28, "Spatial-Design": 0.25}
            },
            {
                "option_id": 1815,
                "option_text": "A creative studio with art supplies",
                "trait_tags": {"Visual-Design": 1.0, "Creative-Skill": 0.8, "Artistic": 0.45, "Digital-Media": 0.32, "Spatial-Design": 0.28}
            },
            {
                "option_id": 1816,
                "option_text": "A classroom full of students",
                "trait_tags": {"Teaching-Ed": 1.0, "People-Skill": 0.8, "Social": 0.45, "Patient-Care": 0.32, "Hospitality-Svc": 0.32, "Community-Serve": 0.25}
            },
            {
                "option_id": 1817,
                "option_text": "A corporate office with meetings",
                "trait_tags": {"Finance-Acct": 1.0, "Admin-Skill": 0.8, "Conventional": 0.45, "Analytical-Skill": 0.4, "Startup-Venture": 0.2, "Hospitality-Svc": 0.16}
            },
            {
                "option_id": 1818,
                "option_text": "A kitchen or food production area",
                "trait_tags": {"Culinary-Arts": 1.0, "Food-Science": 0.8, "Creative-Skill": 0.35, "Hospitality-Svc": 0.35, "Investigative": 0.32, "Artistic": 0.3}
            }
        ]
    },
    {
        "question_id": 182,
        "question_text": "What motivates you most to work hard?",
        "category": "Values - Motivation",
        "options": [
            {
                "option_id": 1821,
                "option_text": "Discovering something new or innovative",
                "trait_tags": {"Lab-Research": 1.0, "AI-ML": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Data-Analytics": 0.32, "Medical-Lab": 0.3}
            },
            {
                "option_id": 1822,
                "option_text": "Helping people who are suffering",
                "trait_tags": {"Patient-Care": 1.0, "Social-Work": 0.8, "People-Skill": 0.45, "Social": 0.4, "Community-Serve": 0.32, "Rehab-Therapy": 0.3}
            },
            {
                "option_id": 1823,
                "option_text": "Earning money and financial success",
                "trait_tags": {"Finance-Acct": 1.0, "Startup-Venture": 0.8, "Conventional": 0.45, "Analytical-Skill": 0.4, "Enterprising": 0.36, "Admin-Skill": 0.3}
            },
            {
                "option_id": 1824,
                "option_text": "Creating something beautiful",
                "trait_tags": {"Visual-Design": 1.0, "Performing-Arts": 0.8, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            },
            {
                "option_id": 1825,
                "option_text": "Teaching the next generation",
                "trait_tags": {"Teaching-Ed": 1.0, "Community-Serve": 0.8, "Social": 0.45, "People-Skill": 0.45, "Patient-Care": 0.16, "Rehab-Therapy": 0.15}
            },
            {
                "option_id": 1826,
                "option_text": "Protecting the environment",
                "trait_tags": {"Environmental-Sci": 1.0, "Agri-Nature": 0.8, "Investigative": 0.45, "Field-Research": 0.4, "Realistic": 0.36, "Environmental-Eng": 0.3}
            },
            {
                "option_id": 1827,
                "option_text": "Being respected as an expert",
                "trait_tags": {"Lab-Research": 1.0, "Legal-Practice": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Medical-Lab": 0.3, "Enterprising": 0.28}
            },
            {
                "option_id": 1828,
                "option_text": "The thrill of competition and winning",
                "trait_tags": {"Sports-Ed": 1.0, "Marketing-Sales": 0.8, "Physical-Skill": 0.45, "Enterprising": 0.36, "Social": 0.35, "Teaching-Ed": 0.35}
            }
        ]
    },
    {
        "question_id": 183,
        "question_text": "How do you handle stress and pressure?",
        "category": "Stress Management",
        "options": [
            {
                "option_id": 1831,
                "option_text": "Exercise, play sports, or go to the gym",
                "trait_tags": {"Sports-Ed": 1.0, "Physical-Skill": 0.8, "Social": 0.35, "Teaching-Ed": 0.35, "Realistic": 0.32, "Maritime-Sea": 0.28}
            },
            {
                "option_id": 1832,
                "option_text": "Draw, paint, or work on creative projects",
                "trait_tags": {"Visual-Design": 1.0, "Creative-Skill": 0.8, "Artistic": 0.45, "Digital-Media": 0.32, "Spatial-Design": 0.28}
            },
            {
                "option_id": 1833,
                "option_text": "Talk to friends or family about my feelings",
                "trait_tags": {"People-Skill": 1.0, "Counseling": 0.8, "Social": 0.45, "Patient-Care": 0.4, "Teaching-Ed": 0.4, "Hospitality-Svc": 0.4}
            },
            {
                "option_id": 1834,
                "option_text": "Organize and plan to feel in control",
                "trait_tags": {"Admin-Skill": 1.0, "Industrial-Ops": 0.8, "Conventional": 0.45, "Finance-Acct": 0.3, "Analytical-Skill": 0.28, "Enterprising": 0.24}
            },
            {
                "option_id": 1835,
                "option_text": "Code, tinker, or work on a tech project",
                "trait_tags": {"Software-Dev": 1.0, "Hardware-Systems": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Realistic": 0.32, "Data-Analytics": 0.3}
            },
            {
                "option_id": 1836,
                "option_text": "Cook or bake something delicious",
                "trait_tags": {"Culinary-Arts": 1.0, "Creative-Skill": 0.8, "Artistic": 0.36, "Hospitality-Svc": 0.35, "Visual-Design": 0.32, "Digital-Media": 0.32}
            },
            {
                "option_id": 1837,
                "option_text": "Go outdoors and be in nature",
                "trait_tags": {"Field-Research": 1.0, "Agri-Nature": 0.8, "Investigative": 0.4, "Realistic": 0.36, "Analytical-Skill": 0.3, "Physical-Skill": 0.28}
            },
            {
                "option_id": 1838,
                "option_text": "Watch documentaries or read educational content",
                "trait_tags": {"Lab-Research": 1.0, "Film-Broadcast": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Artistic": 0.32, "Creative-Skill": 0.32}
            }
        ]
    },
    {
        "question_id": 184,
        "question_text": "Which after-school club would you join or start?",
        "category": "Extracurricular Interest",
        "options": [
            {
                "option_id": 1841,
                "option_text": "Robotics or computer science club",
                "trait_tags": {"Hardware-Systems": 1.0, "Software-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Investigative": 0.32, "Electrical-Power": 0.3}
            },
            {
                "option_id": 1842,
                "option_text": "Red Cross or medical volunteer club",
                "trait_tags": {"Patient-Care": 1.0, "Community-Serve": 0.8, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Medical-Lab": 0.2}
            },
            {
                "option_id": 1843,
                "option_text": "Business and entrepreneurship club",
                "trait_tags": {"Startup-Venture": 1.0, "Finance-Acct": 0.8, "Enterprising": 0.45, "Conventional": 0.36, "Analytical-Skill": 0.32, "People-Skill": 0.3}
            },
            {
                "option_id": 1844,
                "option_text": "Art, photography, or film club",
                "trait_tags": {"Visual-Design": 1.0, "Film-Broadcast": 0.8, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.32, "Spatial-Design": 0.25}
            },
            {
                "option_id": 1845,
                "option_text": "Debate and public speaking club",
                "trait_tags": {"Legal-Practice": 1.0, "People-Skill": 0.8, "Social": 0.36, "Enterprising": 0.35, "Analytical-Skill": 0.35, "Patient-Care": 0.32}
            },
            {
                "option_id": 1846,
                "option_text": "Environmental or science club",
                "trait_tags": {"Environmental-Sci": 1.0, "Lab-Research": 0.8, "Investigative": 0.45, "Field-Research": 0.4, "Analytical-Skill": 0.36, "Environmental-Eng": 0.3}
            },
            {
                "option_id": 1847,
                "option_text": "Theater or dance troupe",
                "trait_tags": {"Performing-Arts": 1.0, "Creative-Skill": 0.8, "Artistic": 0.45, "Visual-Design": 0.32, "Digital-Media": 0.32, "People-Skill": 0.3}
            },
            {
                "option_id": 1848,
                "option_text": "Student government or community service",
                "trait_tags": {"Community-Serve": 1.0, "Legal-Practice": 0.8, "Social": 0.45, "People-Skill": 0.4, "Enterprising": 0.28, "Analytical-Skill": 0.28}
            },
            {
                "option_id": 1849,
                "option_text": "Sports team or fitness club",
                "trait_tags": {"Sports-Ed": 1.0, "Physical-Skill": 0.8, "Social": 0.35, "Teaching-Ed": 0.35, "Realistic": 0.32, "Maritime-Sea": 0.28}
            },
            {
                "option_id": 1850,
                "option_text": "Cooking or food appreciation club",
                "trait_tags": {"Culinary-Arts": 1.0, "Nutrition-Diet": 0.8, "Creative-Skill": 0.35, "Hospitality-Svc": 0.35, "Artistic": 0.3, "Food-Science": 0.28}
            }
        ]
    },
    {
        "question_id": 185,
        "question_text": "What kind of problem do you most enjoy solving?",
        "category": "Problem-Solving Style",
        "options": [
            {
                "option_id": 1851,
                "option_text": "Debugging code or fixing software errors",
                "trait_tags": {"Software-Dev": 1.0, "Web-Dev": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25}
            },
            {
                "option_id": 1852,
                "option_text": "Diagnosing a medical condition",
                "trait_tags": {"Patient-Care": 1.0, "Medical-Lab": 0.8, "People-Skill": 0.45, "Social": 0.4, "Analytical-Skill": 0.36, "Investigative": 0.32}
            },
            {
                "option_id": 1853,
                "option_text": "Calculating the best financial strategy",
                "trait_tags": {"Finance-Acct": 1.0, "Data-Analytics": 0.8, "Conventional": 0.45, "Analytical-Skill": 0.4, "Investigative": 0.36, "Admin-Skill": 0.3}
            },
            {
                "option_id": 1854,
                "option_text": "Figuring out how a machine broke down",
                "trait_tags": {"Mechanical-Design": 1.0, "Hardware-Systems": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Industrial-Ops": 0.25, "Electrical-Power": 0.24}
            },
            {
                "option_id": 1855,
                "option_text": "Understanding why someone is upset",
                "trait_tags": {"Counseling": 1.0, "People-Skill": 0.8, "Social": 0.45, "Teaching-Ed": 0.32, "Patient-Care": 0.32, "Hospitality-Svc": 0.32}
            },
            {
                "option_id": 1856,
                "option_text": "Designing a better layout or structure",
                "trait_tags": {"Spatial-Design": 1.0, "Civil-Build": 0.8, "Realistic": 0.36, "Artistic": 0.35, "Creative-Skill": 0.35, "Technical-Skill": 0.32}
            },
            {
                "option_id": 1857,
                "option_text": "Solving a scientific mystery through experiments",
                "trait_tags": {"Lab-Research": 1.0, "Forensic-Sci": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Medical-Lab": 0.3, "Law-Enforce": 0.28}
            },
            {
                "option_id": 1858,
                "option_text": "Finding the right ingredients for a perfect recipe",
                "trait_tags": {"Culinary-Arts": 1.0, "Food-Science": 0.8, "Creative-Skill": 0.35, "Hospitality-Svc": 0.35, "Investigative": 0.32, "Artistic": 0.3}
            }
        ]
    },
    {
        "question_id": 186,
        "question_text": "A local NGO needs a social media campaign. What's your contribution?",
        "category": "Situational - Digital Marketing",
        "options": [
            {
                "option_id": 1861,
                "option_text": "Writing compelling stories about their cause",
                "trait_tags": {"Creative-Skill": 1.0, "Community-Serve": 0.8, "Artistic": 0.45, "Visual-Design": 0.4, "Digital-Media": 0.4, "Social": 0.36}
            },
            {
                "option_id": 1862,
                "option_text": "Designing graphics and posters",
                "trait_tags": {"Visual-Design": 1.0, "Digital-Media": 0.8, "Artistic": 0.45, "Creative-Skill": 0.45, "Spatial-Design": 0.25, "Software-Dev": 0.16}
            },
            {
                "option_id": 1863,
                "option_text": "Filming and editing a short documentary",
                "trait_tags": {"Film-Broadcast": 1.0, "Digital-Media": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Visual-Design": 0.25, "Technical-Skill": 0.2}
            },
            {
                "option_id": 1864,
                "option_text": "Analyzing which posts get the most engagement",
                "trait_tags": {"Data-Analytics": 1.0, "Marketing-Sales": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Enterprising": 0.36, "People-Skill": 0.32}
            },
            {
                "option_id": 1865,
                "option_text": "Managing the social media accounts daily",
                "trait_tags": {"Marketing-Sales": 1.0, "Admin-Skill": 0.8, "Enterprising": 0.45, "People-Skill": 0.4, "Conventional": 0.36, "Startup-Venture": 0.3}
            },
            {
                "option_id": 1866,
                "option_text": "Reaching out to corporate sponsors",
                "trait_tags": {"Startup-Venture": 1.0, "People-Skill": 0.8, "Enterprising": 0.45, "Social": 0.36, "Teaching-Ed": 0.32, "Hospitality-Svc": 0.32}
            },
            {
                "option_id": 1867,
                "option_text": "Building a fundraising website",
                "trait_tags": {"Web-Dev": 1.0, "Community-Serve": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Social": 0.36, "Investigative": 0.35}
            },
            {
                "option_id": 1868,
                "option_text": "Organizing real-world events to complement the campaign",
                "trait_tags": {"Admin-Skill": 1.0, "Community-Serve": 0.8, "Conventional": 0.45, "Social": 0.36, "People-Skill": 0.32, "Finance-Acct": 0.3}
            }
        ]
    },
    {
        "question_id": 187,
        "question_text": "Your school's science fair is coming up. What's your project?",
        "category": "Situational - Science Fair",
        "options": [
            {
                "option_id": 1871,
                "option_text": "Testing which fertilizer helps plants grow fastest",
                "trait_tags": {"Agri-Nature": 1.0, "Lab-Research": 0.8, "Realistic": 0.45, "Investigative": 0.36, "Analytical-Skill": 0.36, "Physical-Skill": 0.35}
            },
            {
                "option_id": 1872,
                "option_text": "Building a simple robot that follows a line",
                "trait_tags": {"Hardware-Systems": 1.0, "Software-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Investigative": 0.32, "Electrical-Power": 0.3}
            },
            {
                "option_id": 1873,
                "option_text": "Studying bacteria levels in local water sources",
                "trait_tags": {"Lab-Research": 1.0, "Environmental-Sci": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Field-Research": 0.32, "Medical-Lab": 0.3}
            },
            {
                "option_id": 1874,
                "option_text": "Creating a solar-powered phone charger",
                "trait_tags": {"Electrical-Power": 1.0, "Environmental-Eng": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3, "Environmental-Sci": 0.28}
            },
            {
                "option_id": 1875,
                "option_text": "Analyzing the nutritional value of local street food",
                "trait_tags": {"Nutrition-Diet": 1.0, "Food-Science": 0.8, "Investigative": 0.32, "Social": 0.3, "Analytical-Skill": 0.3, "Lab-Research": 0.28}
            },
            {
                "option_id": 1876,
                "option_text": "Building a bridge model that holds the most weight",
                "trait_tags": {"Civil-Build": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Industrial-Ops": 0.2}
            },
            {
                "option_id": 1877,
                "option_text": "An AI program that recognizes Filipino sign language",
                "trait_tags": {"AI-ML": 1.0, "Counseling": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Data-Analytics": 0.4, "Social": 0.36}
            },
            {
                "option_id": 1878,
                "option_text": "A survey of mental health among SHS students",
                "trait_tags": {"Counseling": 1.0, "Data-Analytics": 0.8, "Social": 0.45, "People-Skill": 0.45, "Investigative": 0.36, "Analytical-Skill": 0.36}
            }
        ]
    },
    {
        "question_id": 188,
        "question_text": "You're assigned to a rural health unit for immersion. What task do you choose?",
        "category": "Situational - Rural Health",
        "options": [
            {
                "option_id": 1881,
                "option_text": "Assisting the nurse with check-ups and injections",
                "trait_tags": {"Patient-Care": 1.0, "Public-Health": 0.8, "People-Skill": 0.45, "Social": 0.4, "Rehab-Therapy": 0.3, "Community-Serve": 0.28}
            },
            {
                "option_id": 1882,
                "option_text": "Helping the pharmacy sort and distribute medicines",
                "trait_tags": {"Pharmacy": 1.0, "Admin-Skill": 0.8, "Investigative": 0.4, "Analytical-Skill": 0.4, "Conventional": 0.36, "Medical-Lab": 0.35}
            },
            {
                "option_id": 1883,
                "option_text": "Teaching mothers about proper child nutrition",
                "trait_tags": {"Nutrition-Diet": 1.0, "Teaching-Ed": 0.8, "Social": 0.36, "People-Skill": 0.36, "Food-Science": 0.35, "Analytical-Skill": 0.3}
            },
            {
                "option_id": 1884,
                "option_text": "Recording patient data in their health information system",
                "trait_tags": {"Health-Admin": 1.0, "Software-Dev": 0.8, "Admin-Skill": 0.45, "Conventional": 0.4, "Technical-Skill": 0.36, "Investigative": 0.32}
            },
            {
                "option_id": 1885,
                "option_text": "Running a mini fitness and exercise activity",
                "trait_tags": {"Sports-Ed": 1.0, "Rehab-Therapy": 0.8, "Physical-Skill": 0.45, "Social": 0.35, "Teaching-Ed": 0.35, "People-Skill": 0.28}
            },
            {
                "option_id": 1886,
                "option_text": "Conducting a dengue awareness campaign",
                "trait_tags": {"Public-Health": 1.0, "Community-Serve": 0.8, "Social": 0.4, "Analytical-Skill": 0.35, "People-Skill": 0.32, "Patient-Care": 0.25}
            },
            {
                "option_id": 1887,
                "option_text": "Collecting and organizing health survey data",
                "trait_tags": {"Data-Analytics": 1.0, "Health-Admin": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Admin-Skill": 0.36, "Conventional": 0.32}
            },
            {
                "option_id": 1888,
                "option_text": "Helping with physical therapy for elderly patients",
                "trait_tags": {"Rehab-Therapy": 1.0, "People-Skill": 0.8, "Physical-Skill": 0.4, "Social": 0.36, "Patient-Care": 0.32, "Teaching-Ed": 0.32}
            }
        ]
    },
    {
        "question_id": 189,
        "question_text": "Your professor asks you to lead a capstone project. What topic do you pick?",
        "category": "Situational - Capstone Project",
        "options": [
            {
                "option_id": 1891,
                "option_text": "An automated grading system using machine learning",
                "trait_tags": {"AI-ML": 1.0, "Software-Dev": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Data-Analytics": 0.4, "Technical-Skill": 0.36}
            },
            {
                "option_id": 1892,
                "option_text": "A mobile health app for rural barangays",
                "trait_tags": {"Mobile-Dev": 1.0, "Public-Health": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Investigative": 0.35, "Social": 0.32}
            },
            {
                "option_id": 1893,
                "option_text": "A sustainable building design using local materials",
                "trait_tags": {"Civil-Build": 1.0, "Environmental-Eng": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Environmental-Sci": 0.28, "Spatial-Design": 0.25}
            },
            {
                "option_id": 1894,
                "option_text": "A marketing plan for a local cooperative",
                "trait_tags": {"Marketing-Sales": 1.0, "Agri-Nature": 0.8, "Enterprising": 0.45, "People-Skill": 0.4, "Realistic": 0.36, "Startup-Venture": 0.3}
            },
            {
                "option_id": 1895,
                "option_text": "A documentary about endangered Philippine species",
                "trait_tags": {"Film-Broadcast": 1.0, "Environmental-Sci": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Digital-Media": 0.4, "Investigative": 0.36}
            },
            {
                "option_id": 1896,
                "option_text": "A counseling intervention program for at-risk youth",
                "trait_tags": {"Counseling": 1.0, "Social-Work": 0.8, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.32, "Teaching-Ed": 0.3}
            },
            {
                "option_id": 1897,
                "option_text": "A water quality monitoring system using IoT sensors",
                "trait_tags": {"Hardware-Systems": 1.0, "Environmental-Eng": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Electrical-Power": 0.3, "Mechanical-Design": 0.25}
            },
            {
                "option_id": 1898,
                "option_text": "A food processing facility plan for local farmers",
                "trait_tags": {"Food-Science": 1.0, "Industrial-Ops": 0.8, "Investigative": 0.4, "Lab-Research": 0.35, "Nutrition-Diet": 0.35, "Analytical-Skill": 0.3}
            }
        ]
    },
    {
        "question_id": 190,
        "question_text": "If a company hired you right now, which department would you want to work in?",
        "category": "Department Preference",
        "options": [
            {
                "option_id": 1901,
                "option_text": "IT / Software Engineering",
                "trait_tags": {"Software-Dev": 1.0, "Cloud-Systems": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25}
            },
            {
                "option_id": 1902,
                "option_text": "Marketing and Communications",
                "trait_tags": {"Marketing-Sales": 1.0, "Film-Broadcast": 0.8, "Enterprising": 0.45, "People-Skill": 0.4, "Artistic": 0.32, "Creative-Skill": 0.32}
            },
            {
                "option_id": 1903,
                "option_text": "Finance and Accounting",
                "trait_tags": {"Finance-Acct": 1.0, "Analytical-Skill": 0.8, "Conventional": 0.45, "Investigative": 0.36, "Data-Analytics": 0.32, "Admin-Skill": 0.3}
            },
            {
                "option_id": 1904,
                "option_text": "Human Resources",
                "trait_tags": {"HR-Management": 1.0, "People-Skill": 0.8, "Social": 0.36, "Enterprising": 0.35, "Admin-Skill": 0.35, "Teaching-Ed": 0.32}
            },
            {
                "option_id": 1905,
                "option_text": "Research and Development",
                "trait_tags": {"Lab-Research": 1.0, "AI-ML": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Data-Analytics": 0.32, "Medical-Lab": 0.3}
            },
            {
                "option_id": 1906,
                "option_text": "Operations and Logistics",
                "trait_tags": {"Industrial-Ops": 1.0, "Admin-Skill": 0.8, "Conventional": 0.36, "Analytical-Skill": 0.35, "Enterprising": 0.3, "Mechanical-Design": 0.25}
            },
            {
                "option_id": 1907,
                "option_text": "Legal and Compliance",
                "trait_tags": {"Legal-Practice": 1.0, "Admin-Skill": 0.8, "Conventional": 0.36, "Enterprising": 0.35, "Analytical-Skill": 0.35, "People-Skill": 0.3}
            },
            {
                "option_id": 1908,
                "option_text": "Creative / Design",
                "trait_tags": {"Visual-Design": 1.0, "Digital-Media": 0.8, "Artistic": 0.45, "Creative-Skill": 0.45, "Spatial-Design": 0.25, "Software-Dev": 0.16}
            },
            {
                "option_id": 1909,
                "option_text": "Customer Service",
                "trait_tags": {"People-Skill": 1.0, "Hospitality-Svc": 0.8, "Social": 0.45, "Patient-Care": 0.4, "Teaching-Ed": 0.4, "Tourism-Travel": 0.32}
            },
            {
                "option_id": 1910,
                "option_text": "Health and Safety",
                "trait_tags": {"Public-Health": 1.0, "Physical-Skill": 0.8, "Social": 0.4, "Analytical-Skill": 0.35, "Community-Serve": 0.35, "Realistic": 0.32}
            }
        ]
    },
    {
        "question_id": 191,
        "question_text": "Your city is planning a new public transportation system. What's your role?",
        "category": "Situational - Urban Planning",
        "options": [
            {
                "option_id": 1911,
                "option_text": "Designing the routes and schedules",
                "trait_tags": {"Civil-Build": 1.0, "Data-Analytics": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Investigative": 0.36, "Analytical-Skill": 0.36}
            },
            {
                "option_id": 1912,
                "option_text": "Building the stations and infrastructure",
                "trait_tags": {"Civil-Build": 1.0, "Spatial-Design": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Artistic": 0.28, "Creative-Skill": 0.28}
            },
            {
                "option_id": 1913,
                "option_text": "Developing a mobile app for commuters",
                "trait_tags": {"Mobile-Dev": 1.0, "Web-Dev": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Investigative": 0.35, "Game-Dev": 0.2}
            },
            {
                "option_id": 1914,
                "option_text": "Ensuring it's environmentally sustainable",
                "trait_tags": {"Environmental-Eng": 1.0, "Environmental-Sci": 0.8, "Realistic": 0.4, "Investigative": 0.36, "Technical-Skill": 0.35, "Field-Research": 0.32}
            },
            {
                "option_id": 1915,
                "option_text": "Managing the PR and public communication",
                "trait_tags": {"Marketing-Sales": 1.0, "Community-Serve": 0.8, "Enterprising": 0.45, "People-Skill": 0.4, "Social": 0.36, "Startup-Venture": 0.3}
            },
            {
                "option_id": 1916,
                "option_text": "Handling the budget and financial projections",
                "trait_tags": {"Finance-Acct": 1.0, "Admin-Skill": 0.8, "Conventional": 0.45, "Analytical-Skill": 0.4, "Startup-Venture": 0.2, "Hospitality-Svc": 0.16}
            },
            {
                "option_id": 1917,
                "option_text": "Engineering the actual vehicles and systems",
                "trait_tags": {"Mechanical-Design": 1.0, "Electrical-Power": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Industrial-Ops": 0.25, "Hardware-Systems": 0.24}
            },
            {
                "option_id": 1918,
                "option_text": "Studying the traffic data to optimize flow",
                "trait_tags": {"Data-Analytics": 1.0, "Industrial-Ops": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Software-Dev": 0.3, "Lab-Research": 0.25}
            }
        ]
    },
    {
        "question_id": 192,
        "question_text": "A classmate faints during PE class. What do you instinctively do?",
        "category": "Situational - Emergency Response",
        "options": [
            {
                "option_id": 1921,
                "option_text": "Check their pulse and do CPR if needed",
                "trait_tags": {"Patient-Care": 1.0, "Physical-Skill": 0.8, "People-Skill": 0.45, "Social": 0.4, "Realistic": 0.32, "Rehab-Therapy": 0.3}
            },
            {
                "option_id": 1922,
                "option_text": "Run and get the school nurse immediately",
                "trait_tags": {"People-Skill": 1.0, "Physical-Skill": 0.8, "Social": 0.45, "Patient-Care": 0.4, "Teaching-Ed": 0.4, "Hospitality-Svc": 0.4}
            },
            {
                "option_id": 1923,
                "option_text": "Stay calm and keep the crowd back",
                "trait_tags": {"Admin-Skill": 1.0, "People-Skill": 0.8, "Conventional": 0.45, "Social": 0.36, "Hospitality-Svc": 0.32, "Teaching-Ed": 0.32}
            },
            {
                "option_id": 1924,
                "option_text": "Document the incident for the school report",
                "trait_tags": {"Admin-Skill": 1.0, "Legal-Practice": 0.8, "Conventional": 0.45, "Finance-Acct": 0.3, "Enterprising": 0.28, "Analytical-Skill": 0.28}
            },
            {
                "option_id": 1925,
                "option_text": "Provide emotional support and reassurance",
                "trait_tags": {"Counseling": 1.0, "People-Skill": 0.8, "Social": 0.45, "Teaching-Ed": 0.32, "Patient-Care": 0.32, "Hospitality-Svc": 0.32}
            },
            {
                "option_id": 1926,
                "option_text": "Think about what medical condition might cause this",
                "trait_tags": {"Medical-Lab": 1.0, "Analytical-Skill": 0.8, "Investigative": 0.4, "Lab-Research": 0.35, "Data-Analytics": 0.32, "Finance-Acct": 0.28}
            },
            {
                "option_id": 1927,
                "option_text": "Call 911 and provide location details",
                "trait_tags": {"Community-Serve": 1.0, "Admin-Skill": 0.8, "Social": 0.45, "People-Skill": 0.4, "Conventional": 0.36, "Health-Admin": 0.28}
            },
            {
                "option_id": 1928,
                "option_text": "Check if it's heat-related and move them to shade",
                "trait_tags": {"Sports-Ed": 1.0, "Patient-Care": 0.8, "Physical-Skill": 0.45, "People-Skill": 0.36, "Social": 0.35, "Teaching-Ed": 0.35}
            }
        ]
    },
    {
        "question_id": 193,
        "question_text": "Which internship opportunity would you grab immediately?",
        "category": "Internship Preference",
        "options": [
            {
                "option_id": 1931,
                "option_text": "A tech startup developing new apps",
                "trait_tags": {"Software-Dev": 1.0, "Startup-Venture": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Enterprising": 0.36, "Data-Analytics": 0.3}
            },
            {
                "option_id": 1932,
                "option_text": "A hospital's research and clinical department",
                "trait_tags": {"Medical-Lab": 1.0, "Patient-Care": 0.8, "Analytical-Skill": 0.45, "Investigative": 0.4, "People-Skill": 0.36, "Lab-Research": 0.35}
            },
            {
                "option_id": 1933,
                "option_text": "A construction company for a major project",
                "trait_tags": {"Civil-Build": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Industrial-Ops": 0.2}
            },
            {
                "option_id": 1934,
                "option_text": "A bank's financial analysis department",
                "trait_tags": {"Finance-Acct": 1.0, "Data-Analytics": 0.8, "Conventional": 0.45, "Analytical-Skill": 0.4, "Investigative": 0.36, "Admin-Skill": 0.3}
            },
            {
                "option_id": 1935,
                "option_text": "A TV or film production company",
                "trait_tags": {"Film-Broadcast": 1.0, "Digital-Media": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Visual-Design": 0.25, "Technical-Skill": 0.2}
            },
            {
                "option_id": 1936,
                "option_text": "A government environmental agency",
                "trait_tags": {"Environmental-Sci": 1.0, "Community-Serve": 0.8, "Investigative": 0.45, "Field-Research": 0.4, "Social": 0.36, "People-Skill": 0.32}
            },
            {
                "option_id": 1937,
                "option_text": "A hotel or resort chain",
                "trait_tags": {"Hospitality-Svc": 1.0, "Tourism-Travel": 0.8, "People-Skill": 0.45, "Enterprising": 0.35, "Culinary-Arts": 0.3, "Marketing-Sales": 0.2}
            },
            {
                "option_id": 1938,
                "option_text": "An NGO helping underprivileged communities",
                "trait_tags": {"Social-Work": 1.0, "Community-Serve": 0.8, "Social": 0.45, "People-Skill": 0.45, "Counseling": 0.3, "Teaching-Ed": 0.25}
            },
            {
                "option_id": 1939,
                "option_text": "A law firm or legal aid organization",
                "trait_tags": {"Legal-Practice": 1.0, "Law-Enforce": 0.8, "Enterprising": 0.35, "Analytical-Skill": 0.35, "People-Skill": 0.3, "Realistic": 0.28}
            },
            {
                "option_id": 1940,
                "option_text": "A sports training facility",
                "trait_tags": {"Sports-Ed": 1.0, "Rehab-Therapy": 0.8, "Physical-Skill": 0.45, "Social": 0.35, "Teaching-Ed": 0.35, "People-Skill": 0.28}
            }
        ]
    },
    {
        "question_id": 194,
        "question_text": "Rate your confidence: 'I can explain complex science topics to anyone.'",
        "category": "Scale - Communication",
        "options": [
            {
                "option_id": 1941,
                "option_text": "Strongly Agree - I love teaching and explaining",
                "trait_tags": {"Teaching-Ed": 1.0, "Lab-Research": 0.8, "Social": 0.45, "People-Skill": 0.45, "Investigative": 0.36, "Analytical-Skill": 0.36}
            },
            {
                "option_id": 1942,
                "option_text": "Agree - I'm good at simplifying things",
                "trait_tags": {"Teaching-Ed": 1.0, "People-Skill": 0.8, "Social": 0.45, "Patient-Care": 0.32, "Hospitality-Svc": 0.32, "Community-Serve": 0.25}
            },
            {
                "option_id": 1943,
                "option_text": "Neutral - I prefer doing rather than explaining",
                "trait_tags": {"Technical-Skill": 1.0, "Analytical-Skill": 0.8, "Software-Dev": 0.4, "Hardware-Systems": 0.4, "Investigative": 0.36, "Realistic": 0.35}
            },
            {
                "option_id": 1944,
                "option_text": "Disagree - I understand but can't explain well",
                "trait_tags": {"Lab-Research": 1.0, "Analytical-Skill": 0.8, "Investigative": 0.45, "Data-Analytics": 0.32, "Medical-Lab": 0.3, "Field-Research": 0.25}
            },
            {
                "option_id": 1945,
                "option_text": "Strongly Disagree - Science isn't my area",
                "trait_tags": {"Creative-Skill": 1.0, "People-Skill": 0.8, "Artistic": 0.45, "Visual-Design": 0.4, "Digital-Media": 0.4, "Social": 0.36}
            }
        ]
    },
    {
        "question_id": 195,
        "question_text": "How comfortable are you working with numbers and calculations?",
        "category": "Scale - Math Comfort",
        "options": [
            {
                "option_id": 1951,
                "option_text": "Very comfortable - I love math and statistics",
                "trait_tags": {"Data-Analytics": 1.0, "Finance-Acct": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Conventional": 0.36, "Software-Dev": 0.3}
            },
            {
                "option_id": 1952,
                "option_text": "Comfortable - I use them for practical purposes",
                "trait_tags": {"Analytical-Skill": 1.0, "Industrial-Ops": 0.8, "Investigative": 0.45, "Data-Analytics": 0.4, "Lab-Research": 0.35, "Finance-Acct": 0.35}
            },
            {
                "option_id": 1953,
                "option_text": "Neutral - I can do them when needed",
                "trait_tags": {"Technical-Skill": 1.0, "Admin-Skill": 0.8, "Software-Dev": 0.4, "Hardware-Systems": 0.4, "Conventional": 0.36, "Realistic": 0.35}
            },
            {
                "option_id": 1954,
                "option_text": "Uncomfortable - I prefer words over numbers",
                "trait_tags": {"Creative-Skill": 1.0, "Teaching-Ed": 0.8, "Artistic": 0.45, "Visual-Design": 0.4, "Digital-Media": 0.4, "Social": 0.36}
            },
            {
                "option_id": 1955,
                "option_text": "Very uncomfortable - I avoid math whenever possible",
                "trait_tags": {"Performing-Arts": 1.0, "People-Skill": 0.8, "Artistic": 0.45, "Creative-Skill": 0.45, "Social": 0.36, "Teaching-Ed": 0.32}
            }
        ]
    },
    {
        "question_id": 196,
        "question_text": "How do you feel about working outdoors in the sun and rain?",
        "category": "Scale - Outdoor Work",
        "options": [
            {
                "option_id": 1961,
                "option_text": "Love it - I thrive outdoors",
                "trait_tags": {"Agri-Nature": 1.0, "Field-Research": 0.8, "Realistic": 0.45, "Physical-Skill": 0.35, "Investigative": 0.32, "Analytical-Skill": 0.24}
            },
            {
                "option_id": 1962,
                "option_text": "I'm fine with it when needed",
                "trait_tags": {"Civil-Build": 1.0, "Physical-Skill": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Agri-Nature": 0.28, "Spatial-Design": 0.25}
            },
            {
                "option_id": 1963,
                "option_text": "I prefer a mix of indoor and outdoor",
                "trait_tags": {"Maritime-Sea": 1.0, "Environmental-Sci": 0.8, "Realistic": 0.45, "Physical-Skill": 0.4, "Investigative": 0.36, "Field-Research": 0.32}
            },
            {
                "option_id": 1964,
                "option_text": "I'd rather stay indoors most of the time",
                "trait_tags": {"Software-Dev": 1.0, "Lab-Research": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Analytical-Skill": 0.36, "Data-Analytics": 0.3}
            },
            {
                "option_id": 1965,
                "option_text": "I strongly prefer air-conditioned office work",
                "trait_tags": {"Finance-Acct": 1.0, "Admin-Skill": 0.8, "Conventional": 0.45, "Analytical-Skill": 0.4, "Startup-Venture": 0.2, "Hospitality-Svc": 0.16}
            }
        ]
    },
    {
        "question_id": 197,
        "question_text": "How important is it for you to help other people in your career?",
        "category": "Scale - Helping Others",
        "options": [
            {
                "option_id": 1971,
                "option_text": "Essential — my career should directly help people",
                "trait_tags": {"Patient-Care": 1.0, "Social-Work": 0.8, "People-Skill": 0.45, "Social": 0.4, "Community-Serve": 0.32, "Rehab-Therapy": 0.3}
            },
            {
                "option_id": 1972,
                "option_text": "Very important — I want to serve communities",
                "trait_tags": {"Community-Serve": 1.0, "Teaching-Ed": 0.8, "Social": 0.45, "People-Skill": 0.4, "Patient-Care": 0.2, "Law-Enforce": 0.15}
            },
            {
                "option_id": 1973,
                "option_text": "Somewhat important — I help through my work indirectly",
                "trait_tags": {"Lab-Research": 1.0, "Environmental-Sci": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Field-Research": 0.32, "Medical-Lab": 0.3}
            },
            {
                "option_id": 1974,
                "option_text": "Not very important — I focus on the work itself",
                "trait_tags": {"Software-Dev": 1.0, "Mechanical-Design": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Realistic": 0.36, "Data-Analytics": 0.3}
            },
            {
                "option_id": 1975,
                "option_text": "Not really — I prefer working on things, not people",
                "trait_tags": {"Hardware-Systems": 1.0, "Data-Analytics": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Investigative": 0.36, "Analytical-Skill": 0.36}
            }
        ]
    },
    {
        "question_id": 198,
        "question_text": "If your school had a hackathon for social good, what would your team create?",
        "category": "Situational - Social Innovation",
        "options": [
            {
                "option_id": 1981,
                "option_text": "A telemedicine app for rural doctors",
                "trait_tags": {"Mobile-Dev": 1.0, "Public-Health": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Investigative": 0.35, "Social": 0.32}
            },
            {
                "option_id": 1982,
                "option_text": "A disaster early warning system",
                "trait_tags": {"Hardware-Systems": 1.0, "Environmental-Sci": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Investigative": 0.36, "Field-Research": 0.32}
            },
            {
                "option_id": 1983,
                "option_text": "A crowdsourcing platform for community cleanup",
                "trait_tags": {"Web-Dev": 1.0, "Environmental-Eng": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Investigative": 0.35, "Realistic": 0.32}
            },
            {
                "option_id": 1984,
                "option_text": "An AI tutor in Filipino for underprivileged students",
                "trait_tags": {"AI-ML": 1.0, "Teaching-Ed": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Data-Analytics": 0.4, "Social": 0.36}
            },
            {
                "option_id": 1985,
                "option_text": "A financial literacy game for young Filipinos",
                "trait_tags": {"Game-Dev": 1.0, "Finance-Acct": 0.8, "Technical-Skill": 0.4, "Software-Dev": 0.4, "Conventional": 0.36, "Creative-Skill": 0.35}
            },
            {
                "option_id": 1986,
                "option_text": "A GIS map tracking illegal logging",
                "trait_tags": {"Data-Analytics": 1.0, "Agri-Nature": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Realistic": 0.36, "Software-Dev": 0.3}
            },
            {
                "option_id": 1987,
                "option_text": "A mental health chatbot for students",
                "trait_tags": {"AI-ML": 1.0, "Counseling": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Data-Analytics": 0.4, "Social": 0.36}
            },
            {
                "option_id": 1988,
                "option_text": "A platform connecting small farmers to buyers",
                "trait_tags": {"Web-Dev": 1.0, "Agri-Nature": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Realistic": 0.36, "Investigative": 0.35}
            }
        ]
    },
    {
        "question_id": 199,
        "question_text": "Which TV show genre do you enjoy most?",
        "category": "Media Preference",
        "options": [
            {
                "option_id": 1991,
                "option_text": "Sci-fi and technology (Black Mirror, Westworld)",
                "trait_tags": {"Software-Dev": 1.0, "AI-ML": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Analytical-Skill": 0.36, "Data-Analytics": 0.32}
            },
            {
                "option_id": 1992,
                "option_text": "Medical dramas (Grey's Anatomy, The Good Doctor)",
                "trait_tags": {"Patient-Care": 1.0, "Medical-Lab": 0.8, "People-Skill": 0.45, "Social": 0.4, "Analytical-Skill": 0.36, "Investigative": 0.32}
            },
            {
                "option_id": 1993,
                "option_text": "Crime and legal (CSI, Suits)",
                "trait_tags": {"Forensic-Sci": 1.0, "Legal-Practice": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.4, "Lab-Research": 0.35, "Law-Enforce": 0.35}
            },
            {
                "option_id": 1994,
                "option_text": "Business and finance (Shark Tank, The Profit)",
                "trait_tags": {"Startup-Venture": 1.0, "Finance-Acct": 0.8, "Enterprising": 0.45, "Conventional": 0.36, "Analytical-Skill": 0.32, "People-Skill": 0.3}
            },
            {
                "option_id": 1995,
                "option_text": "Nature and wildlife (Planet Earth, Our Planet)",
                "trait_tags": {"Environmental-Sci": 1.0, "Field-Research": 0.8, "Investigative": 0.45, "Environmental-Eng": 0.3, "Lab-Research": 0.25, "Agri-Nature": 0.25}
            },
            {
                "option_id": 1996,
                "option_text": "Reality competition (MasterChef, Amazing Race)",
                "trait_tags": {"Culinary-Arts": 1.0, "Tourism-Travel": 0.8, "Creative-Skill": 0.35, "Hospitality-Svc": 0.35, "People-Skill": 0.32, "Artistic": 0.3}
            },
            {
                "option_id": 1997,
                "option_text": "Creative arts (Project Runway, Abstract)",
                "trait_tags": {"Visual-Design": 1.0, "Performing-Arts": 0.8, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.3, "Spatial-Design": 0.25}
            },
            {
                "option_id": 1998,
                "option_text": "Sports (ESPN, UFC)",
                "trait_tags": {"Sports-Ed": 1.0, "Physical-Skill": 0.8, "Social": 0.35, "Teaching-Ed": 0.35, "Realistic": 0.32, "Maritime-Sea": 0.28}
            }
        ]
    },
    {
        "question_id": 200,
        "question_text": "What section of a bookstore do you visit first?",
        "category": "Reading Interest",
        "options": [
            {
                "option_id": 2001,
                "option_text": "Technology and programming books",
                "trait_tags": {"Software-Dev": 1.0, "Web-Dev": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25}
            },
            {
                "option_id": 2002,
                "option_text": "Medical and health references",
                "trait_tags": {"Patient-Care": 1.0, "Pharmacy": 0.8, "People-Skill": 0.45, "Social": 0.4, "Investigative": 0.32, "Analytical-Skill": 0.32}
            },
            {
                "option_id": 2003,
                "option_text": "Engineering and science textbooks",
                "trait_tags": {"Mechanical-Design": 1.0, "Lab-Research": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Investigative": 0.36, "Analytical-Skill": 0.36}
            },
            {
                "option_id": 2004,
                "option_text": "Business and self-improvement",
                "trait_tags": {"Startup-Venture": 1.0, "Marketing-Sales": 0.8, "Enterprising": 0.45, "People-Skill": 0.32, "Finance-Acct": 0.2, "Creative-Skill": 0.2}
            },
            {
                "option_id": 2005,
                "option_text": "Art, photography, and design books",
                "trait_tags": {"Visual-Design": 1.0, "Film-Broadcast": 0.8, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.32, "Spatial-Design": 0.25}
            },
            {
                "option_id": 2006,
                "option_text": "Cooking and recipe books",
                "trait_tags": {"Culinary-Arts": 1.0, "Nutrition-Diet": 0.8, "Creative-Skill": 0.35, "Hospitality-Svc": 0.35, "Artistic": 0.3, "Food-Science": 0.28}
            },
            {
                "option_id": 2007,
                "option_text": "True crime and mystery novels",
                "trait_tags": {"Forensic-Sci": 1.0, "Law-Enforce": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.4, "Lab-Research": 0.35, "Realistic": 0.28}
            },
            {
                "option_id": 2008,
                "option_text": "Psychology and social science",
                "trait_tags": {"Counseling": 1.0, "Social-Work": 0.8, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.32, "Teaching-Ed": 0.3}
            },
            {
                "option_id": 2009,
                "option_text": "Travel and adventure books",
                "trait_tags": {"Tourism-Travel": 1.0, "Field-Research": 0.8, "People-Skill": 0.4, "Hospitality-Svc": 0.4, "Enterprising": 0.35, "Investigative": 0.32}
            },
            {
                "option_id": 2010,
                "option_text": "Education and teaching guides",
                "trait_tags": {"Teaching-Ed": 1.0, "Counseling": 0.8, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.25, "Rehab-Therapy": 0.2}
            }
        ]
    },
    {
        "question_id": 201,
        "question_text": "You're assigned to a merchant vessel for your first voyage. What department do you want to join?",
        "category": "Situational - Maritime Career Path",
        "options": [
            {
                "option_id": 2011,
                "option_text": "Deck department - navigation and watchkeeping",
                "trait_tags": {"Maritime-Sea": 1.0, "Physical-Skill": 0.8, "Realistic": 0.45, "Agri-Nature": 0.28, "Technical-Skill": 0.25, "Law-Enforce": 0.24}
            },
            {
                "option_id": 2012,
                "option_text": "Engine department - maintaining propulsion systems",
                "trait_tags": {"Maritime-Sea": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.45, "Physical-Skill": 0.4, "Technical-Skill": 0.32, "Industrial-Ops": 0.2}
            },
            {
                "option_id": 2013,
                "option_text": "Electrical officer - managing ship electronics",
                "trait_tags": {"Maritime-Sea": 1.0, "Electrical-Power": 0.8, "Realistic": 0.45, "Physical-Skill": 0.4, "Technical-Skill": 0.36, "Mechanical-Design": 0.16}
            },
            {
                "option_id": 2014,
                "option_text": "Radio officer - communications and safety signals",
                "trait_tags": {"Maritime-Sea": 1.0, "Hardware-Systems": 0.8, "Realistic": 0.45, "Physical-Skill": 0.4, "Technical-Skill": 0.36, "Electrical-Power": 0.24}
            },
            {
                "option_id": 2015,
                "option_text": "Steward department - hospitality on cruise ships",
                "trait_tags": {"Maritime-Sea": 1.0, "Hospitality-Svc": 0.8, "Realistic": 0.45, "Physical-Skill": 0.4, "People-Skill": 0.36, "Tourism-Travel": 0.32}
            },
            {
                "option_id": 2016,
                "option_text": "Port operations - managing cargo loading/unloading",
                "trait_tags": {"Maritime-Sea": 1.0, "Industrial-Ops": 0.8, "Realistic": 0.45, "Physical-Skill": 0.4, "Analytical-Skill": 0.28, "Technical-Skill": 0.25}
            },
            {
                "option_id": 2017,
                "option_text": "Safety officer - emergency procedures and drills",
                "trait_tags": {"Maritime-Sea": 1.0, "Community-Serve": 0.8, "Realistic": 0.45, "Physical-Skill": 0.4, "Social": 0.36, "People-Skill": 0.32}
            },
            {
                "option_id": 2018,
                "option_text": "None of these appeal to me",
                "trait_tags": {}
            }
        ]
    },
    {
        "question_id": 202,
        "question_text": "What aspect of maritime studies interests you most?",
        "category": "Interest - Maritime Studies",
        "options": [
            {
                "option_id": 2021,
                "option_text": "Celestial and electronic navigation",
                "trait_tags": {"Maritime-Sea": 1.0, "Physical-Skill": 0.8, "Realistic": 0.45, "Agri-Nature": 0.28, "Technical-Skill": 0.25, "Law-Enforce": 0.24}
            },
            {
                "option_id": 2022,
                "option_text": "Marine diesel engines and ship machinery",
                "trait_tags": {"Maritime-Sea": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.45, "Physical-Skill": 0.4, "Technical-Skill": 0.32, "Industrial-Ops": 0.2}
            },
            {
                "option_id": 2023,
                "option_text": "International maritime law and regulations",
                "trait_tags": {"Maritime-Sea": 1.0, "Legal-Practice": 0.8, "Realistic": 0.45, "Physical-Skill": 0.4, "Enterprising": 0.28, "Analytical-Skill": 0.28}
            },
            {
                "option_id": 2024,
                "option_text": "Ship stability, construction, and naval architecture",
                "trait_tags": {"Maritime-Sea": 1.0, "Civil-Build": 0.8, "Realistic": 0.45, "Physical-Skill": 0.4, "Technical-Skill": 0.32, "Spatial-Design": 0.2}
            },
            {
                "option_id": 2025,
                "option_text": "Cargo handling and logistics management",
                "trait_tags": {"Maritime-Sea": 1.0, "Industrial-Ops": 0.8, "Realistic": 0.45, "Physical-Skill": 0.4, "Analytical-Skill": 0.28, "Technical-Skill": 0.25}
            },
            {
                "option_id": 2026,
                "option_text": "Marine environmental protection",
                "trait_tags": {"Maritime-Sea": 1.0, "Environmental-Sci": 0.8, "Realistic": 0.45, "Physical-Skill": 0.4, "Investigative": 0.36, "Field-Research": 0.32}
            },
            {
                "option_id": 2027,
                "option_text": "Meteorology and weather routing at sea",
                "trait_tags": {"Maritime-Sea": 1.0, "Field-Research": 0.8, "Realistic": 0.45, "Physical-Skill": 0.4, "Investigative": 0.32, "Technical-Skill": 0.25}
            },
            {
                "option_id": 2028,
                "option_text": "Seamanship and survival at sea",
                "trait_tags": {"Maritime-Sea": 1.0, "Physical-Skill": 0.8, "Realistic": 0.45, "Agri-Nature": 0.28, "Technical-Skill": 0.25, "Law-Enforce": 0.24}
            }
        ]
    },
    {
        "question_id": 203,
        "question_text": "A typhoon is approaching while your ship is in Philippine waters. What do you focus on?",
        "category": "Situational - Maritime Safety",
        "options": [
            {
                "option_id": 2031,
                "option_text": "Plot an alternative course to avoid the typhoon",
                "trait_tags": {"Maritime-Sea": 1.0, "Physical-Skill": 0.8, "Realistic": 0.45, "Agri-Nature": 0.28, "Technical-Skill": 0.25, "Law-Enforce": 0.24}
            },
            {
                "option_id": 2032,
                "option_text": "Secure the engine room and check all machinery",
                "trait_tags": {"Maritime-Sea": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.45, "Physical-Skill": 0.4, "Technical-Skill": 0.32, "Industrial-Ops": 0.2}
            },
            {
                "option_id": 2033,
                "option_text": "Coordinate with MARINA and coast guard for updates",
                "trait_tags": {"Maritime-Sea": 1.0, "Community-Serve": 0.8, "Realistic": 0.45, "Physical-Skill": 0.4, "Social": 0.36, "People-Skill": 0.32}
            },
            {
                "option_id": 2034,
                "option_text": "Organize the crew for emergency procedures",
                "trait_tags": {"Maritime-Sea": 1.0, "People-Skill": 0.8, "Realistic": 0.45, "Physical-Skill": 0.4, "Social": 0.36, "Hospitality-Svc": 0.32}
            },
            {
                "option_id": 2035,
                "option_text": "Check all safety equipment - lifeboats, life jackets",
                "trait_tags": {"Maritime-Sea": 1.0, "Physical-Skill": 0.8, "Realistic": 0.45, "Agri-Nature": 0.28, "Technical-Skill": 0.25, "Law-Enforce": 0.24}
            },
            {
                "option_id": 2036,
                "option_text": "Monitor weather radar and satellite data",
                "trait_tags": {"Maritime-Sea": 1.0, "Data-Analytics": 0.8, "Realistic": 0.45, "Physical-Skill": 0.4, "Investigative": 0.36, "Analytical-Skill": 0.36}
            },
            {
                "option_id": 2037,
                "option_text": "Secure all cargo to prevent shifting",
                "trait_tags": {"Maritime-Sea": 1.0, "Industrial-Ops": 0.8, "Realistic": 0.45, "Physical-Skill": 0.4, "Analytical-Skill": 0.28, "Technical-Skill": 0.25}
            },
            {
                "option_id": 2038,
                "option_text": "Prepare medical supplies for potential injuries",
                "trait_tags": {"Patient-Care": 1.0, "Maritime-Sea": 0.8, "People-Skill": 0.45, "Social": 0.4, "Realistic": 0.36, "Physical-Skill": 0.32}
            }
        ]
    },
    {
        "question_id": 204,
        "question_text": "Why does a career at sea appeal to you?",
        "category": "Motivation - Maritime",
        "options": [
            {
                "option_id": 2041,
                "option_text": "Traveling to different countries and seeing the world",
                "trait_tags": {"Maritime-Sea": 1.0, "Tourism-Travel": 0.8, "Realistic": 0.45, "Physical-Skill": 0.4, "People-Skill": 0.32, "Hospitality-Svc": 0.32}
            },
            {
                "option_id": 2042,
                "option_text": "High salary potential especially working abroad",
                "trait_tags": {"Maritime-Sea": 1.0, "Physical-Skill": 0.8, "Realistic": 0.45, "Agri-Nature": 0.28, "Technical-Skill": 0.25, "Law-Enforce": 0.24}
            },
            {
                "option_id": 2043,
                "option_text": "Challenging work that tests my physical and mental limits",
                "trait_tags": {"Maritime-Sea": 1.0, "Physical-Skill": 0.8, "Realistic": 0.45, "Agri-Nature": 0.28, "Technical-Skill": 0.25, "Law-Enforce": 0.24}
            },
            {
                "option_id": 2044,
                "option_text": "Following a family tradition of seafaring",
                "trait_tags": {"Maritime-Sea": 1.0, "Community-Serve": 0.8, "Realistic": 0.45, "Physical-Skill": 0.4, "Social": 0.36, "People-Skill": 0.32}
            },
            {
                "option_id": 2045,
                "option_text": "Working with advanced ship technology and systems",
                "trait_tags": {"Maritime-Sea": 1.0, "Hardware-Systems": 0.8, "Realistic": 0.45, "Physical-Skill": 0.4, "Technical-Skill": 0.36, "Electrical-Power": 0.24}
            },
            {
                "option_id": 2046,
                "option_text": "Being part of global trade and shipping industry",
                "trait_tags": {"Maritime-Sea": 1.0, "Industrial-Ops": 0.8, "Realistic": 0.45, "Physical-Skill": 0.4, "Analytical-Skill": 0.28, "Technical-Skill": 0.25}
            },
            {
                "option_id": 2047,
                "option_text": "The discipline and structured life on a ship",
                "trait_tags": {"Maritime-Sea": 1.0, "Admin-Skill": 0.8, "Realistic": 0.45, "Physical-Skill": 0.4, "Conventional": 0.36, "Technical-Skill": 0.25}
            },
            {
                "option_id": 2048,
                "option_text": "A career at sea doesn't really appeal to me",
                "trait_tags": {}
            }
        ]
    },
    {
        "question_id": 205,
        "question_text": "You're choosing between two maritime academies. Which program feature matters most?",
        "category": "Preference - Maritime Training",
        "options": [
            {
                "option_id": 2051,
                "option_text": "More time on training ships with real sea experience",
                "trait_tags": {"Maritime-Sea": 1.0, "Physical-Skill": 0.8, "Realistic": 0.45, "Agri-Nature": 0.28, "Technical-Skill": 0.25, "Law-Enforce": 0.24}
            },
            {
                "option_id": 2052,
                "option_text": "Strong engine room simulation and workshop facilities",
                "trait_tags": {"Maritime-Sea": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.45, "Physical-Skill": 0.4, "Technical-Skill": 0.32, "Industrial-Ops": 0.2}
            },
            {
                "option_id": 2053,
                "option_text": "Modern bridge simulator for navigation training",
                "trait_tags": {"Maritime-Sea": 1.0, "Hardware-Systems": 0.8, "Realistic": 0.45, "Physical-Skill": 0.4, "Technical-Skill": 0.36, "Electrical-Power": 0.24}
            },
            {
                "option_id": 2054,
                "option_text": "Good connections with international shipping companies",
                "trait_tags": {"Maritime-Sea": 1.0, "Marketing-Sales": 0.8, "Realistic": 0.45, "Physical-Skill": 0.4, "Enterprising": 0.36, "People-Skill": 0.32}
            },
            {
                "option_id": 2055,
                "option_text": "Strong MARINA board exam pass rate",
                "trait_tags": {"Maritime-Sea": 1.0, "Analytical-Skill": 0.8, "Realistic": 0.45, "Physical-Skill": 0.4, "Investigative": 0.36, "Lab-Research": 0.28}
            },
            {
                "option_id": 2056,
                "option_text": "Additional certifications like GMDSS, STCW",
                "trait_tags": {"Maritime-Sea": 1.0, "Technical-Skill": 0.8, "Realistic": 0.45, "Physical-Skill": 0.4, "Mechanical-Design": 0.28, "Investigative": 0.2}
            },
            {
                "option_id": 2057,
                "option_text": "Focus on marine environmental protection",
                "trait_tags": {"Maritime-Sea": 1.0, "Environmental-Sci": 0.8, "Realistic": 0.45, "Physical-Skill": 0.4, "Investigative": 0.36, "Field-Research": 0.32}
            },
            {
                "option_id": 2058,
                "option_text": "Dual degree option with business or management",
                "trait_tags": {"Maritime-Sea": 1.0, "Admin-Skill": 0.8, "Realistic": 0.45, "Physical-Skill": 0.4, "Conventional": 0.36, "Technical-Skill": 0.25}
            }
        ]
    },
    {
        "question_id": 206,
        "question_text": "You're designing your own video game. What genre would you choose?",
        "category": "Interest - Game Development",
        "options": [
            {
                "option_id": 2061,
                "option_text": "An action RPG with complex combat mechanics",
                "trait_tags": {"Game-Dev": 1.0, "Software-Dev": 0.8, "Technical-Skill": 0.4, "Creative-Skill": 0.35, "Animation-3D": 0.35, "Investigative": 0.32}
            },
            {
                "option_id": 2062,
                "option_text": "A puzzle game with AI-generated levels",
                "trait_tags": {"Game-Dev": 1.0, "AI-ML": 0.8, "Technical-Skill": 0.4, "Software-Dev": 0.4, "Investigative": 0.36, "Analytical-Skill": 0.36}
            },
            {
                "option_id": 2063,
                "option_text": "A story-driven adventure with cinematic cutscenes",
                "trait_tags": {"Game-Dev": 1.0, "Film-Broadcast": 0.8, "Technical-Skill": 0.4, "Software-Dev": 0.4, "Creative-Skill": 0.35, "Animation-3D": 0.35}
            },
            {
                "option_id": 2064,
                "option_text": "A competitive multiplayer esports game",
                "trait_tags": {"Game-Dev": 1.0, "Cloud-Systems": 0.8, "Technical-Skill": 0.4, "Software-Dev": 0.4, "Creative-Skill": 0.35, "Animation-3D": 0.35}
            },
            {
                "option_id": 2065,
                "option_text": "A mobile casual game with simple but addictive gameplay",
                "trait_tags": {"Game-Dev": 1.0, "Mobile-Dev": 0.8, "Technical-Skill": 0.4, "Software-Dev": 0.4, "Creative-Skill": 0.35, "Animation-3D": 0.35}
            },
            {
                "option_id": 2066,
                "option_text": "A VR simulation with realistic 3D environments",
                "trait_tags": {"Game-Dev": 1.0, "Animation-3D": 0.8, "Technical-Skill": 0.4, "Software-Dev": 0.4, "Creative-Skill": 0.35, "Artistic": 0.32}
            },
            {
                "option_id": 2067,
                "option_text": "An educational game that teaches Filipino history",
                "trait_tags": {"Game-Dev": 1.0, "Teaching-Ed": 0.8, "Technical-Skill": 0.4, "Software-Dev": 0.4, "Social": 0.36, "People-Skill": 0.36}
            },
            {
                "option_id": 2068,
                "option_text": "A pixel art indie game with retro style",
                "trait_tags": {"Game-Dev": 1.0, "Visual-Design": 0.8, "Technical-Skill": 0.4, "Software-Dev": 0.4, "Artistic": 0.36, "Creative-Skill": 0.36}
            }
        ]
    },
    {
        "question_id": 207,
        "question_text": "What part of building a video game excites you the most?",
        "category": "Preference - Game Development",
        "options": [
            {
                "option_id": 2071,
                "option_text": "Writing game physics and collision detection code",
                "trait_tags": {"Game-Dev": 1.0, "Software-Dev": 0.8, "Technical-Skill": 0.4, "Creative-Skill": 0.35, "Animation-3D": 0.35, "Investigative": 0.32}
            },
            {
                "option_id": 2072,
                "option_text": "Creating character sprites and environment art",
                "trait_tags": {"Game-Dev": 1.0, "Animation-3D": 0.8, "Technical-Skill": 0.4, "Software-Dev": 0.4, "Creative-Skill": 0.35, "Artistic": 0.32}
            },
            {
                "option_id": 2073,
                "option_text": "Designing levels and balancing difficulty curves",
                "trait_tags": {"Game-Dev": 1.0, "Data-Analytics": 0.8, "Technical-Skill": 0.4, "Software-Dev": 0.4, "Investigative": 0.36, "Analytical-Skill": 0.36}
            },
            {
                "option_id": 2074,
                "option_text": "Building multiplayer networking and servers",
                "trait_tags": {"Game-Dev": 1.0, "Cloud-Systems": 0.8, "Technical-Skill": 0.4, "Software-Dev": 0.4, "Creative-Skill": 0.35, "Animation-3D": 0.35}
            },
            {
                "option_id": 2075,
                "option_text": "Composing music and creating sound effects",
                "trait_tags": {"Game-Dev": 1.0, "Performing-Arts": 0.8, "Technical-Skill": 0.4, "Software-Dev": 0.4, "Artistic": 0.36, "Creative-Skill": 0.36}
            },
            {
                "option_id": 2076,
                "option_text": "Writing the storyline, quests, and dialogue",
                "trait_tags": {"Game-Dev": 1.0, "Creative-Skill": 0.8, "Technical-Skill": 0.4, "Software-Dev": 0.4, "Artistic": 0.36, "Animation-3D": 0.35}
            },
            {
                "option_id": 2077,
                "option_text": "Designing the UI, menus, and HUD elements",
                "trait_tags": {"Game-Dev": 1.0, "Visual-Design": 0.8, "Technical-Skill": 0.4, "Software-Dev": 0.4, "Artistic": 0.36, "Creative-Skill": 0.36}
            },
            {
                "option_id": 2078,
                "option_text": "Marketing the game and building a community",
                "trait_tags": {"Game-Dev": 1.0, "Marketing-Sales": 0.8, "Technical-Skill": 0.4, "Software-Dev": 0.4, "Enterprising": 0.36, "Creative-Skill": 0.35}
            }
        ]
    },
    {
        "question_id": 208,
        "question_text": "Your game studio is entering a game jam competition. What's your team strategy?",
        "category": "Situational - Game Development Team",
        "options": [
            {
                "option_id": 2081,
                "option_text": "Focus on solid gameplay mechanics - make it fun first",
                "trait_tags": {"Game-Dev": 1.0, "Software-Dev": 0.8, "Technical-Skill": 0.4, "Creative-Skill": 0.35, "Animation-3D": 0.35, "Investigative": 0.32}
            },
            {
                "option_id": 2082,
                "option_text": "Create stunning visuals that stand out from other entries",
                "trait_tags": {"Game-Dev": 1.0, "Animation-3D": 0.8, "Technical-Skill": 0.4, "Software-Dev": 0.4, "Creative-Skill": 0.35, "Artistic": 0.32}
            },
            {
                "option_id": 2083,
                "option_text": "Build a deep narrative that judges will remember",
                "trait_tags": {"Game-Dev": 1.0, "Creative-Skill": 0.8, "Technical-Skill": 0.4, "Software-Dev": 0.4, "Artistic": 0.36, "Animation-3D": 0.35}
            },
            {
                "option_id": 2084,
                "option_text": "Use innovative tech like AR or procedural generation",
                "trait_tags": {"Game-Dev": 1.0, "AI-ML": 0.8, "Technical-Skill": 0.4, "Software-Dev": 0.4, "Investigative": 0.36, "Analytical-Skill": 0.36}
            },
            {
                "option_id": 2085,
                "option_text": "Make a polished mobile version anyone can try",
                "trait_tags": {"Game-Dev": 1.0, "Mobile-Dev": 0.8, "Technical-Skill": 0.4, "Software-Dev": 0.4, "Creative-Skill": 0.35, "Animation-3D": 0.35}
            },
            {
                "option_id": 2086,
                "option_text": "Add online multiplayer so players can compete",
                "trait_tags": {"Game-Dev": 1.0, "Cloud-Systems": 0.8, "Technical-Skill": 0.4, "Software-Dev": 0.4, "Creative-Skill": 0.35, "Animation-3D": 0.35}
            },
            {
                "option_id": 2087,
                "option_text": "Design an unforgettable soundtrack",
                "trait_tags": {"Game-Dev": 1.0, "Performing-Arts": 0.8, "Technical-Skill": 0.4, "Software-Dev": 0.4, "Artistic": 0.36, "Creative-Skill": 0.36}
            },
            {
                "option_id": 2088,
                "option_text": "Create a game trailer and social media hype",
                "trait_tags": {"Game-Dev": 1.0, "Digital-Media": 0.8, "Technical-Skill": 0.4, "Software-Dev": 0.4, "Creative-Skill": 0.35, "Animation-3D": 0.35}
            }
        ]
    },
    {
        "question_id": 209,
        "question_text": "Which game development tool or engine would you most want to master?",
        "category": "Technical Preference - Game Dev",
        "options": [
            {
                "option_id": 2091,
                "option_text": "Unity - it powers most indie and mobile games",
                "trait_tags": {"Game-Dev": 1.0, "Software-Dev": 0.8, "Technical-Skill": 0.4, "Creative-Skill": 0.35, "Animation-3D": 0.35, "Investigative": 0.32}
            },
            {
                "option_id": 2092,
                "option_text": "Unreal Engine - for AAA-quality 3D graphics",
                "trait_tags": {"Game-Dev": 1.0, "Animation-3D": 0.8, "Technical-Skill": 0.4, "Software-Dev": 0.4, "Creative-Skill": 0.35, "Artistic": 0.32}
            },
            {
                "option_id": 2093,
                "option_text": "Godot - the open-source engine for 2D games",
                "trait_tags": {"Game-Dev": 1.0, "Software-Dev": 0.8, "Technical-Skill": 0.4, "Creative-Skill": 0.35, "Animation-3D": 0.35, "Investigative": 0.32}
            },
            {
                "option_id": 2094,
                "option_text": "Blender - for 3D modeling and game assets",
                "trait_tags": {"Animation-3D": 1.0, "Game-Dev": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Digital-Media": 0.4, "Software-Dev": 0.32}
            },
            {
                "option_id": 2095,
                "option_text": "Photoshop/Aseprite - for game sprites and pixel art",
                "trait_tags": {"Visual-Design": 1.0, "Game-Dev": 0.8, "Artistic": 0.45, "Creative-Skill": 0.45, "Technical-Skill": 0.32, "Software-Dev": 0.32}
            },
            {
                "option_id": 2096,
                "option_text": "FL Studio/FMOD - for game audio and music",
                "trait_tags": {"Performing-Arts": 1.0, "Game-Dev": 0.8, "Artistic": 0.45, "Creative-Skill": 0.45, "Technical-Skill": 0.32, "Software-Dev": 0.32}
            },
            {
                "option_id": 2097,
                "option_text": "Python/C++ - raw programming for game logic",
                "trait_tags": {"Software-Dev": 1.0, "Game-Dev": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Creative-Skill": 0.28}
            },
            {
                "option_id": 2098,
                "option_text": "Figma - for designing game UI/UX mockups",
                "trait_tags": {"Visual-Design": 1.0, "Web-Dev": 0.8, "Artistic": 0.45, "Creative-Skill": 0.45, "Technical-Skill": 0.36, "Software-Dev": 0.36}
            }
        ]
    },
    {
        "question_id": 210,
        "question_text": "A game company offers you an internship. Which department do you pick?",
        "category": "Situational - Game Industry Career",
        "options": [
            {
                "option_id": 2101,
                "option_text": "Game programming - working on core engine code",
                "trait_tags": {"Game-Dev": 1.0, "Software-Dev": 0.8, "Technical-Skill": 0.4, "Creative-Skill": 0.35, "Animation-3D": 0.35, "Investigative": 0.32}
            },
            {
                "option_id": 2102,
                "option_text": "3D art - creating characters and worlds",
                "trait_tags": {"Animation-3D": 1.0, "Game-Dev": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Digital-Media": 0.4, "Software-Dev": 0.32}
            },
            {
                "option_id": 2103,
                "option_text": "Game design - planning mechanics and levels",
                "trait_tags": {"Game-Dev": 1.0, "Creative-Skill": 0.8, "Technical-Skill": 0.4, "Software-Dev": 0.4, "Artistic": 0.36, "Animation-3D": 0.35}
            },
            {
                "option_id": 2104,
                "option_text": "QA testing - finding and reporting bugs",
                "trait_tags": {"Game-Dev": 1.0, "Analytical-Skill": 0.8, "Technical-Skill": 0.4, "Software-Dev": 0.4, "Investigative": 0.36, "Creative-Skill": 0.35}
            },
            {
                "option_id": 2105,
                "option_text": "Community management - engaging with players",
                "trait_tags": {"Game-Dev": 1.0, "People-Skill": 0.8, "Technical-Skill": 0.4, "Software-Dev": 0.4, "Social": 0.36, "Creative-Skill": 0.35}
            },
            {
                "option_id": 2106,
                "option_text": "UI/UX design - making interfaces player-friendly",
                "trait_tags": {"Visual-Design": 1.0, "Game-Dev": 0.8, "Artistic": 0.45, "Creative-Skill": 0.45, "Technical-Skill": 0.32, "Software-Dev": 0.32}
            },
            {
                "option_id": 2107,
                "option_text": "Network engineering - building multiplayer systems",
                "trait_tags": {"Cloud-Systems": 1.0, "Game-Dev": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.35, "Investigative": 0.3, "Cyber-Defense": 0.3}
            },
            {
                "option_id": 2108,
                "option_text": "Marketing - creating trailers and campaigns",
                "trait_tags": {"Digital-Media": 1.0, "Marketing-Sales": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Enterprising": 0.36, "People-Skill": 0.32}
            }
        ]
    },
    {
        "question_id": 211,
        "question_text": "You're building a web application from scratch. What feature do you tackle first?",
        "category": "Situational - Web Development",
        "options": [
            {
                "option_id": 2111,
                "option_text": "The responsive frontend design with React or Vue",
                "trait_tags": {"Web-Dev": 1.0, "Visual-Design": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Creative-Skill": 0.36, "Artistic": 0.36}
            },
            {
                "option_id": 2112,
                "option_text": "The backend API with proper database architecture",
                "trait_tags": {"Web-Dev": 1.0, "Software-Dev": 0.8, "Technical-Skill": 0.45, "Investigative": 0.35, "Mobile-Dev": 0.3, "Digital-Media": 0.25}
            },
            {
                "option_id": 2113,
                "option_text": "User authentication and security features",
                "trait_tags": {"Web-Dev": 1.0, "Cyber-Defense": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Investigative": 0.35, "Mobile-Dev": 0.3}
            },
            {
                "option_id": 2114,
                "option_text": "The mobile-responsive layout for all devices",
                "trait_tags": {"Web-Dev": 1.0, "Mobile-Dev": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Investigative": 0.35, "Digital-Media": 0.25}
            },
            {
                "option_id": 2115,
                "option_text": "SEO optimization and analytics dashboard",
                "trait_tags": {"Web-Dev": 1.0, "Data-Analytics": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Investigative": 0.36, "Analytical-Skill": 0.36}
            },
            {
                "option_id": 2116,
                "option_text": "Payment integration and e-commerce features",
                "trait_tags": {"Web-Dev": 1.0, "Finance-Acct": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Conventional": 0.36, "Investigative": 0.35}
            },
            {
                "option_id": 2117,
                "option_text": "Real-time notifications and chat system",
                "trait_tags": {"Web-Dev": 1.0, "Cloud-Systems": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Investigative": 0.35, "Mobile-Dev": 0.3}
            },
            {
                "option_id": 2118,
                "option_text": "Content management system for easy updates",
                "trait_tags": {"Web-Dev": 1.0, "Admin-Skill": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Conventional": 0.36, "Investigative": 0.35}
            }
        ]
    },
    {
        "question_id": 212,
        "question_text": "A startup founder asks you to build their website. What matters most to you?",
        "category": "Situational - Web Dev Project",
        "options": [
            {
                "option_id": 2121,
                "option_text": "Clean, modern UI that users will love",
                "trait_tags": {"Web-Dev": 1.0, "Visual-Design": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Creative-Skill": 0.36, "Artistic": 0.36}
            },
            {
                "option_id": 2122,
                "option_text": "Fast loading speed and server performance",
                "trait_tags": {"Web-Dev": 1.0, "Cloud-Systems": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Investigative": 0.35, "Mobile-Dev": 0.3}
            },
            {
                "option_id": 2123,
                "option_text": "Scalable code architecture for future growth",
                "trait_tags": {"Web-Dev": 1.0, "Software-Dev": 0.8, "Technical-Skill": 0.45, "Investigative": 0.35, "Mobile-Dev": 0.3, "Digital-Media": 0.25}
            },
            {
                "option_id": 2124,
                "option_text": "SEO and marketing tools to attract visitors",
                "trait_tags": {"Web-Dev": 1.0, "Marketing-Sales": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Enterprising": 0.36, "Investigative": 0.35}
            },
            {
                "option_id": 2125,
                "option_text": "Security against hacking and data breaches",
                "trait_tags": {"Web-Dev": 1.0, "Cyber-Defense": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Investigative": 0.35, "Mobile-Dev": 0.3}
            },
            {
                "option_id": 2126,
                "option_text": "Mobile app version alongside the website",
                "trait_tags": {"Mobile-Dev": 1.0, "Web-Dev": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Investigative": 0.35, "Game-Dev": 0.2}
            },
            {
                "option_id": 2127,
                "option_text": "Data analytics to track user behavior",
                "trait_tags": {"Data-Analytics": 1.0, "Web-Dev": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Software-Dev": 0.36, "Technical-Skill": 0.36}
            },
            {
                "option_id": 2128,
                "option_text": "AI-powered chatbot for customer support",
                "trait_tags": {"AI-ML": 1.0, "Web-Dev": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Data-Analytics": 0.4, "Software-Dev": 0.36}
            }
        ]
    },
    {
        "question_id": 213,
        "question_text": "You're creating a 3D animated short film. What role do you want?",
        "category": "Situational - Animation Production",
        "options": [
            {
                "option_id": 2131,
                "option_text": "3D character modeler - sculpting characters",
                "trait_tags": {"Animation-3D": 1.0, "Visual-Design": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Digital-Media": 0.4, "Game-Dev": 0.35}
            },
            {
                "option_id": 2132,
                "option_text": "Animator - bringing characters to life with motion",
                "trait_tags": {"Animation-3D": 1.0, "Creative-Skill": 0.8, "Artistic": 0.4, "Digital-Media": 0.4, "Game-Dev": 0.35, "Visual-Design": 0.32}
            },
            {
                "option_id": 2133,
                "option_text": "Environment artist - building the world and scenes",
                "trait_tags": {"Animation-3D": 1.0, "Spatial-Design": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Digital-Media": 0.4, "Game-Dev": 0.35}
            },
            {
                "option_id": 2134,
                "option_text": "Lighting and rendering specialist",
                "trait_tags": {"Animation-3D": 1.0, "Digital-Media": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Game-Dev": 0.35, "Visual-Design": 0.3}
            },
            {
                "option_id": 2135,
                "option_text": "Technical director - rigging and pipeline tools",
                "trait_tags": {"Animation-3D": 1.0, "Software-Dev": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Digital-Media": 0.4, "Technical-Skill": 0.36}
            },
            {
                "option_id": 2136,
                "option_text": "Storyboard artist - planning shot compositions",
                "trait_tags": {"Animation-3D": 1.0, "Film-Broadcast": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Digital-Media": 0.4, "Game-Dev": 0.35}
            },
            {
                "option_id": 2137,
                "option_text": "Texture and material artist - making surfaces realistic",
                "trait_tags": {"Animation-3D": 1.0, "Visual-Design": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Digital-Media": 0.4, "Game-Dev": 0.35}
            },
            {
                "option_id": 2138,
                "option_text": "VFX artist - explosions, magic, weather effects",
                "trait_tags": {"Animation-3D": 1.0, "Game-Dev": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Digital-Media": 0.4, "Software-Dev": 0.32}
            }
        ]
    },
    {
        "question_id": 214,
        "question_text": "You're developing a mobile app. What kind of app would you build?",
        "category": "Interest - Mobile Development",
        "options": [
            {
                "option_id": 2141,
                "option_text": "A social media app connecting Filipino communities",
                "trait_tags": {"Mobile-Dev": 1.0, "Web-Dev": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Investigative": 0.35, "Game-Dev": 0.2}
            },
            {
                "option_id": 2142,
                "option_text": "A mobile game with leaderboards and achievements",
                "trait_tags": {"Mobile-Dev": 1.0, "Game-Dev": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Investigative": 0.35, "Web-Dev": 0.3}
            },
            {
                "option_id": 2143,
                "option_text": "A fitness tracker with health monitoring",
                "trait_tags": {"Mobile-Dev": 1.0, "Patient-Care": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "People-Skill": 0.36, "Investigative": 0.35}
            },
            {
                "option_id": 2144,
                "option_text": "An e-commerce app for local businesses",
                "trait_tags": {"Mobile-Dev": 1.0, "Marketing-Sales": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Enterprising": 0.36, "Investigative": 0.35}
            },
            {
                "option_id": 2145,
                "option_text": "An AI-powered personal assistant",
                "trait_tags": {"Mobile-Dev": 1.0, "AI-ML": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Investigative": 0.36, "Analytical-Skill": 0.36}
            },
            {
                "option_id": 2146,
                "option_text": "A news aggregator with smart recommendations",
                "trait_tags": {"Mobile-Dev": 1.0, "Data-Analytics": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Investigative": 0.36, "Analytical-Skill": 0.36}
            },
            {
                "option_id": 2147,
                "option_text": "A creative tool for digital drawing or music",
                "trait_tags": {"Mobile-Dev": 1.0, "Creative-Skill": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Artistic": 0.36, "Investigative": 0.35}
            },
            {
                "option_id": 2148,
                "option_text": "A security app with encryption and VPN",
                "trait_tags": {"Mobile-Dev": 1.0, "Cyber-Defense": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Investigative": 0.35, "Web-Dev": 0.3}
            }
        ]
    },
    {
        "question_id": 215,
        "question_text": "Which AI application fascinates you the most?",
        "category": "Interest - Artificial Intelligence",
        "options": [
            {
                "option_id": 2151,
                "option_text": "ChatGPT-style language models that talk like humans",
                "trait_tags": {"AI-ML": 1.0, "Software-Dev": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Data-Analytics": 0.4, "Technical-Skill": 0.36}
            },
            {
                "option_id": 2152,
                "option_text": "AI that generates art, music, or videos",
                "trait_tags": {"AI-ML": 1.0, "Digital-Media": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Data-Analytics": 0.4, "Software-Dev": 0.35}
            },
            {
                "option_id": 2153,
                "option_text": "Self-driving cars and autonomous robots",
                "trait_tags": {"AI-ML": 1.0, "Hardware-Systems": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Data-Analytics": 0.4, "Technical-Skill": 0.36}
            },
            {
                "option_id": 2154,
                "option_text": "AI that detects diseases from medical scans",
                "trait_tags": {"AI-ML": 1.0, "Medical-Lab": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Data-Analytics": 0.4, "Software-Dev": 0.35}
            },
            {
                "option_id": 2155,
                "option_text": "AI for stock market prediction and trading",
                "trait_tags": {"AI-ML": 1.0, "Finance-Acct": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Data-Analytics": 0.4, "Conventional": 0.36}
            },
            {
                "option_id": 2156,
                "option_text": "Game AI that learns and adapts to players",
                "trait_tags": {"AI-ML": 1.0, "Game-Dev": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Data-Analytics": 0.4, "Software-Dev": 0.35}
            },
            {
                "option_id": 2157,
                "option_text": "AI for cybersecurity threat detection",
                "trait_tags": {"AI-ML": 1.0, "Cyber-Defense": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Data-Analytics": 0.4, "Software-Dev": 0.35}
            },
            {
                "option_id": 2158,
                "option_text": "AI that helps farmers predict crop yields",
                "trait_tags": {"AI-ML": 1.0, "Agri-Nature": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Data-Analytics": 0.4, "Realistic": 0.36}
            }
        ]
    },
    {
        "question_id": 216,
        "question_text": "A company hires you as their cybersecurity intern. What do you want to work on?",
        "category": "Situational - Cybersecurity",
        "options": [
            {
                "option_id": 2161,
                "option_text": "Penetration testing - finding system vulnerabilities",
                "trait_tags": {"Cyber-Defense": 1.0, "Software-Dev": 0.8, "Technical-Skill": 0.4, "Investigative": 0.35, "Data-Analytics": 0.24, "Hardware-Systems": 0.16}
            },
            {
                "option_id": 2162,
                "option_text": "Security monitoring - watching for live threats",
                "trait_tags": {"Cyber-Defense": 1.0, "Data-Analytics": 0.8, "Technical-Skill": 0.4, "Investigative": 0.36, "Analytical-Skill": 0.36, "Software-Dev": 0.25}
            },
            {
                "option_id": 2163,
                "option_text": "Digital forensics - investigating hack incidents",
                "trait_tags": {"Cyber-Defense": 1.0, "Forensic-Sci": 0.8, "Technical-Skill": 0.4, "Investigative": 0.36, "Analytical-Skill": 0.32, "Law-Enforce": 0.28}
            },
            {
                "option_id": 2164,
                "option_text": "Network security - protecting firewalls and servers",
                "trait_tags": {"Cyber-Defense": 1.0, "Cloud-Systems": 0.8, "Technical-Skill": 0.4, "Investigative": 0.35, "Software-Dev": 0.28, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 2165,
                "option_text": "Security awareness training for employees",
                "trait_tags": {"Cyber-Defense": 1.0, "Teaching-Ed": 0.8, "Technical-Skill": 0.4, "Social": 0.36, "People-Skill": 0.36, "Investigative": 0.35}
            },
            {
                "option_id": 2166,
                "option_text": "Developing encryption and secure protocols",
                "trait_tags": {"Cyber-Defense": 1.0, "Software-Dev": 0.8, "Technical-Skill": 0.4, "Investigative": 0.35, "Data-Analytics": 0.24, "Hardware-Systems": 0.16}
            },
            {
                "option_id": 2167,
                "option_text": "Compliance and policy - ensuring legal standards",
                "trait_tags": {"Cyber-Defense": 1.0, "Legal-Practice": 0.8, "Technical-Skill": 0.4, "Investigative": 0.35, "Enterprising": 0.28, "Analytical-Skill": 0.28}
            },
            {
                "option_id": 2168,
                "option_text": "Bug bounty hunting - finding flaws for rewards",
                "trait_tags": {"Cyber-Defense": 1.0, "Analytical-Skill": 0.8, "Technical-Skill": 0.4, "Investigative": 0.36, "Data-Analytics": 0.32, "Lab-Research": 0.28}
            }
        ]
    },
    {
        "question_id": 217,
        "question_text": "What interests you most about cloud computing and servers?",
        "category": "Interest - Cloud Computing",
        "options": [
            {
                "option_id": 2171,
                "option_text": "Building scalable websites that handle millions of users",
                "trait_tags": {"Cloud-Systems": 1.0, "Web-Dev": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.36, "Investigative": 0.3, "Cyber-Defense": 0.3}
            },
            {
                "option_id": 2172,
                "option_text": "Setting up game servers for multiplayer games",
                "trait_tags": {"Cloud-Systems": 1.0, "Game-Dev": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.35, "Investigative": 0.3, "Cyber-Defense": 0.3}
            },
            {
                "option_id": 2173,
                "option_text": "Managing databases and data warehouses",
                "trait_tags": {"Cloud-Systems": 1.0, "Data-Analytics": 0.8, "Technical-Skill": 0.45, "Investigative": 0.36, "Analytical-Skill": 0.36, "Software-Dev": 0.35}
            },
            {
                "option_id": 2174,
                "option_text": "DevOps and automating software deployment",
                "trait_tags": {"Cloud-Systems": 1.0, "Software-Dev": 0.8, "Technical-Skill": 0.45, "Investigative": 0.32, "Cyber-Defense": 0.3, "Hardware-Systems": 0.25}
            },
            {
                "option_id": 2175,
                "option_text": "Cloud security and access control",
                "trait_tags": {"Cloud-Systems": 1.0, "Cyber-Defense": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.35, "Investigative": 0.3, "Hardware-Systems": 0.25}
            },
            {
                "option_id": 2176,
                "option_text": "IoT systems connecting physical devices to the cloud",
                "trait_tags": {"Cloud-Systems": 1.0, "Hardware-Systems": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.35, "Realistic": 0.32, "Investigative": 0.3}
            },
            {
                "option_id": 2177,
                "option_text": "Running AI and machine learning models on cloud GPUs",
                "trait_tags": {"Cloud-Systems": 1.0, "AI-ML": 0.8, "Technical-Skill": 0.45, "Investigative": 0.36, "Analytical-Skill": 0.36, "Software-Dev": 0.35}
            },
            {
                "option_id": 2178,
                "option_text": "Hosting and streaming platforms like Netflix or Spotify",
                "trait_tags": {"Cloud-Systems": 1.0, "Digital-Media": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.35, "Artistic": 0.32, "Creative-Skill": 0.32}
            }
        ]
    },
    {
        "question_id": 218,
        "question_text": "You have a massive dataset to analyze. What would you do with it?",
        "category": "Situational - Data Analytics",
        "options": [
            {
                "option_id": 2181,
                "option_text": "Build interactive dashboards and visualizations",
                "trait_tags": {"Data-Analytics": 1.0, "Visual-Design": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Artistic": 0.36, "Creative-Skill": 0.36}
            },
            {
                "option_id": 2182,
                "option_text": "Train a machine learning model to find patterns",
                "trait_tags": {"Data-Analytics": 1.0, "AI-ML": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Software-Dev": 0.3, "Lab-Research": 0.25}
            },
            {
                "option_id": 2183,
                "option_text": "Write SQL queries to extract business insights",
                "trait_tags": {"Data-Analytics": 1.0, "Software-Dev": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Technical-Skill": 0.36, "Lab-Research": 0.25}
            },
            {
                "option_id": 2184,
                "option_text": "Create automated reports for decision-makers",
                "trait_tags": {"Data-Analytics": 1.0, "Admin-Skill": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Conventional": 0.36, "Software-Dev": 0.3}
            },
            {
                "option_id": 2185,
                "option_text": "Analyze player behavior data to improve a game",
                "trait_tags": {"Data-Analytics": 1.0, "Game-Dev": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Software-Dev": 0.32, "Technical-Skill": 0.32}
            },
            {
                "option_id": 2186,
                "option_text": "Study health data to predict disease outbreaks",
                "trait_tags": {"Data-Analytics": 1.0, "Public-Health": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Social": 0.32, "Software-Dev": 0.3}
            },
            {
                "option_id": 2187,
                "option_text": "Analyze social media trends for marketing",
                "trait_tags": {"Data-Analytics": 1.0, "Marketing-Sales": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Enterprising": 0.36, "People-Skill": 0.32}
            },
            {
                "option_id": 2188,
                "option_text": "Map environmental data using GIS",
                "trait_tags": {"Data-Analytics": 1.0, "Environmental-Sci": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Field-Research": 0.32, "Software-Dev": 0.3}
            }
        ]
    },
    {
        "question_id": 219,
        "question_text": "A brand hires you for a creative project. What would you produce?",
        "category": "Situational - Digital Media",
        "options": [
            {
                "option_id": 2191,
                "option_text": "A logo and complete brand identity design",
                "trait_tags": {"Visual-Design": 1.0, "Digital-Media": 0.8, "Artistic": 0.45, "Creative-Skill": 0.45, "Spatial-Design": 0.25, "Software-Dev": 0.16}
            },
            {
                "option_id": 2192,
                "option_text": "A promotional video with motion graphics",
                "trait_tags": {"Digital-Media": 1.0, "Film-Broadcast": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Visual-Design": 0.3, "Software-Dev": 0.2}
            },
            {
                "option_id": 2193,
                "option_text": "Social media content and Instagram reels",
                "trait_tags": {"Digital-Media": 1.0, "Marketing-Sales": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Enterprising": 0.36, "People-Skill": 0.32}
            },
            {
                "option_id": 2194,
                "option_text": "An animated explainer video",
                "trait_tags": {"Animation-3D": 1.0, "Digital-Media": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Game-Dev": 0.35, "Visual-Design": 0.3}
            },
            {
                "option_id": 2195,
                "option_text": "A professional website with eye-catching design",
                "trait_tags": {"Web-Dev": 1.0, "Visual-Design": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Creative-Skill": 0.36, "Artistic": 0.36}
            },
            {
                "option_id": 2196,
                "option_text": "Product packaging and print materials",
                "trait_tags": {"Visual-Design": 1.0, "Creative-Skill": 0.8, "Artistic": 0.45, "Digital-Media": 0.32, "Spatial-Design": 0.28}
            },
            {
                "option_id": 2197,
                "option_text": "A podcast series with professional audio",
                "trait_tags": {"Digital-Media": 1.0, "Performing-Arts": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Visual-Design": 0.3, "People-Skill": 0.24}
            },
            {
                "option_id": 2198,
                "option_text": "A mobile app with beautiful UI design",
                "trait_tags": {"Mobile-Dev": 1.0, "Visual-Design": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Artistic": 0.36, "Creative-Skill": 0.36}
            }
        ]
    },
    {
        "question_id": 220,
        "question_text": "You're starting a tech company with friends. What would the company focus on?",
        "category": "Situational - Tech Startup",
        "options": [
            {
                "option_id": 2201,
                "option_text": "A game development studio making Filipino games",
                "trait_tags": {"Game-Dev": 1.0, "Startup-Venture": 0.8, "Technical-Skill": 0.4, "Software-Dev": 0.4, "Enterprising": 0.36, "Creative-Skill": 0.35}
            },
            {
                "option_id": 2202,
                "option_text": "A web development agency for local businesses",
                "trait_tags": {"Web-Dev": 1.0, "Startup-Venture": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Enterprising": 0.36, "Investigative": 0.35}
            },
            {
                "option_id": 2203,
                "option_text": "A cybersecurity consulting firm",
                "trait_tags": {"Cyber-Defense": 1.0, "Startup-Venture": 0.8, "Technical-Skill": 0.4, "Enterprising": 0.36, "Investigative": 0.35, "Software-Dev": 0.25}
            },
            {
                "option_id": 2204,
                "option_text": "An AI and data analytics company",
                "trait_tags": {"AI-ML": 1.0, "Startup-Venture": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Data-Analytics": 0.4, "Enterprising": 0.36}
            },
            {
                "option_id": 2205,
                "option_text": "A mobile app development company",
                "trait_tags": {"Mobile-Dev": 1.0, "Startup-Venture": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Enterprising": 0.36, "Investigative": 0.35}
            },
            {
                "option_id": 2206,
                "option_text": "A graphic design and branding studio",
                "trait_tags": {"Visual-Design": 1.0, "Startup-Venture": 0.8, "Artistic": 0.45, "Creative-Skill": 0.45, "Enterprising": 0.36, "Digital-Media": 0.3}
            },
            {
                "option_id": 2207,
                "option_text": "A cloud hosting and IT services company",
                "trait_tags": {"Cloud-Systems": 1.0, "Startup-Venture": 0.8, "Technical-Skill": 0.45, "Enterprising": 0.36, "Software-Dev": 0.35, "Investigative": 0.3}
            },
            {
                "option_id": 2208,
                "option_text": "An animation and video production house",
                "trait_tags": {"Animation-3D": 1.0, "Startup-Venture": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Digital-Media": 0.4, "Enterprising": 0.36}
            }
        ]
    },
    {
        "question_id": 221,
        "question_text": "Which YouTube channel topic would you most want to create?",
        "category": "Interest - Content Creation",
        "options": [
            {
                "option_id": 2211,
                "option_text": "Game walkthroughs and esports commentary",
                "trait_tags": {"Game-Dev": 1.0, "Digital-Media": 0.8, "Technical-Skill": 0.4, "Software-Dev": 0.4, "Creative-Skill": 0.35, "Animation-3D": 0.35}
            },
            {
                "option_id": 2212,
                "option_text": "Coding tutorials and tech reviews",
                "trait_tags": {"Software-Dev": 1.0, "Digital-Media": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Artistic": 0.32, "Creative-Skill": 0.32}
            },
            {
                "option_id": 2213,
                "option_text": "Digital art speedpaints and design tips",
                "trait_tags": {"Visual-Design": 1.0, "Digital-Media": 0.8, "Artistic": 0.45, "Creative-Skill": 0.45, "Spatial-Design": 0.25, "Software-Dev": 0.16}
            },
            {
                "option_id": 2214,
                "option_text": "3D animation and VFX breakdowns",
                "trait_tags": {"Animation-3D": 1.0, "Film-Broadcast": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Digital-Media": 0.4, "Game-Dev": 0.35}
            },
            {
                "option_id": 2215,
                "option_text": "Cybersecurity and hacking tutorials",
                "trait_tags": {"Cyber-Defense": 1.0, "Digital-Media": 0.8, "Technical-Skill": 0.4, "Investigative": 0.35, "Artistic": 0.32, "Creative-Skill": 0.32}
            },
            {
                "option_id": 2216,
                "option_text": "Science experiments and tech innovations",
                "trait_tags": {"Lab-Research": 1.0, "Digital-Media": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Artistic": 0.32, "Creative-Skill": 0.32}
            },
            {
                "option_id": 2217,
                "option_text": "Business and finance advice for students",
                "trait_tags": {"Finance-Acct": 1.0, "Digital-Media": 0.8, "Conventional": 0.45, "Analytical-Skill": 0.4, "Artistic": 0.32, "Creative-Skill": 0.32}
            },
            {
                "option_id": 2218,
                "option_text": "Cooking shows and food reviews",
                "trait_tags": {"Culinary-Arts": 1.0, "Film-Broadcast": 0.8, "Creative-Skill": 0.35, "Hospitality-Svc": 0.35, "Artistic": 0.32, "Digital-Media": 0.32}
            }
        ]
    },
    {
        "question_id": 222,
        "question_text": "Your school needs a system built. Which would you volunteer to create?",
        "category": "Situational - School Tech Project",
        "options": [
            {
                "option_id": 2221,
                "option_text": "An online enrollment and grading system",
                "trait_tags": {"Web-Dev": 1.0, "Software-Dev": 0.8, "Technical-Skill": 0.45, "Investigative": 0.35, "Mobile-Dev": 0.3, "Digital-Media": 0.25}
            },
            {
                "option_id": 2222,
                "option_text": "A student information management database",
                "trait_tags": {"Software-Dev": 1.0, "Data-Analytics": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Analytical-Skill": 0.36, "Cyber-Defense": 0.25}
            },
            {
                "option_id": 2223,
                "option_text": "A school mobile app with announcements and schedules",
                "trait_tags": {"Mobile-Dev": 1.0, "Software-Dev": 0.8, "Technical-Skill": 0.45, "Investigative": 0.35, "Web-Dev": 0.3, "Data-Analytics": 0.24}
            },
            {
                "option_id": 2224,
                "option_text": "The school website with an attractive design",
                "trait_tags": {"Web-Dev": 1.0, "Visual-Design": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Creative-Skill": 0.36, "Artistic": 0.36}
            },
            {
                "option_id": 2225,
                "option_text": "A library management and book tracking system",
                "trait_tags": {"Software-Dev": 1.0, "Admin-Skill": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Conventional": 0.36, "Data-Analytics": 0.3}
            },
            {
                "option_id": 2226,
                "option_text": "Network security for the school Wi-Fi",
                "trait_tags": {"Cyber-Defense": 1.0, "Cloud-Systems": 0.8, "Technical-Skill": 0.4, "Investigative": 0.35, "Software-Dev": 0.28, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 2227,
                "option_text": "An interactive game for students to learn math",
                "trait_tags": {"Game-Dev": 1.0, "Teaching-Ed": 0.8, "Technical-Skill": 0.4, "Software-Dev": 0.4, "Social": 0.36, "People-Skill": 0.36}
            },
            {
                "option_id": 2228,
                "option_text": "School social media pages and video content",
                "trait_tags": {"Digital-Media": 1.0, "Marketing-Sales": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Enterprising": 0.36, "People-Skill": 0.32}
            }
        ]
    },
    {
        "question_id": 223,
        "question_text": "A luxury resort is hiring. Which department would you want to work in?",
        "category": "Situational - Hospitality Career",
        "options": [
            {
                "option_id": 2231,
                "option_text": "Front desk and guest relations — welcoming visitors",
                "trait_tags": {"Hospitality-Svc": 1.0, "People-Skill": 0.8, "Tourism-Travel": 0.4, "Social": 0.36, "Enterprising": 0.35, "Teaching-Ed": 0.32}
            },
            {
                "option_id": 2232,
                "option_text": "The kitchen — preparing gourmet dishes",
                "trait_tags": {"Culinary-Arts": 1.0, "Food-Science": 0.8, "Creative-Skill": 0.35, "Hospitality-Svc": 0.35, "Investigative": 0.32, "Artistic": 0.3}
            },
            {
                "option_id": 2233,
                "option_text": "Tour coordination — planning trips for guests",
                "trait_tags": {"Tourism-Travel": 1.0, "Hospitality-Svc": 0.8, "People-Skill": 0.4, "Enterprising": 0.35, "Marketing-Sales": 0.25, "Culinary-Arts": 0.24}
            },
            {
                "option_id": 2234,
                "option_text": "Event management — organizing weddings and parties",
                "trait_tags": {"Hospitality-Svc": 1.0, "Admin-Skill": 0.8, "People-Skill": 0.45, "Tourism-Travel": 0.4, "Conventional": 0.36, "Enterprising": 0.35}
            },
            {
                "option_id": 2235,
                "option_text": "Housekeeping management — ensuring quality standards",
                "trait_tags": {"Hospitality-Svc": 1.0, "HR-Management": 0.8, "People-Skill": 0.45, "Tourism-Travel": 0.4, "Enterprising": 0.35, "Culinary-Arts": 0.3}
            },
            {
                "option_id": 2236,
                "option_text": "Resort marketing — attracting guests through social media",
                "trait_tags": {"Marketing-Sales": 1.0, "Digital-Media": 0.8, "Enterprising": 0.45, "People-Skill": 0.4, "Artistic": 0.32, "Creative-Skill": 0.32}
            },
            {
                "option_id": 2237,
                "option_text": "Resort finance — managing budgets and revenue",
                "trait_tags": {"Finance-Acct": 1.0, "Admin-Skill": 0.8, "Conventional": 0.45, "Analytical-Skill": 0.4, "Startup-Venture": 0.2, "Hospitality-Svc": 0.16}
            },
            {
                "option_id": 2238,
                "option_text": "Spa and wellness — helping guests relax and recover",
                "trait_tags": {"Rehab-Therapy": 1.0, "Hospitality-Svc": 0.8, "Physical-Skill": 0.4, "People-Skill": 0.36, "Social": 0.35, "Tourism-Travel": 0.32}
            }
        ]
    },
    {
        "question_id": 224,
        "question_text": "You're planning the perfect travel experience for tourists visiting the Philippines. What would you focus on?",
        "category": "Situational - Tourism Planning",
        "options": [
            {
                "option_id": 2241,
                "option_text": "Island hopping tours with local guides",
                "trait_tags": {"Tourism-Travel": 1.0, "Hospitality-Svc": 0.8, "People-Skill": 0.4, "Enterprising": 0.35, "Marketing-Sales": 0.25, "Culinary-Arts": 0.24}
            },
            {
                "option_id": 2242,
                "option_text": "Cultural heritage walking tours in historic cities",
                "trait_tags": {"Tourism-Travel": 1.0, "Teaching-Ed": 0.8, "People-Skill": 0.4, "Hospitality-Svc": 0.4, "Social": 0.36, "Enterprising": 0.35}
            },
            {
                "option_id": 2243,
                "option_text": "Adventure and eco-tourism in mountain regions",
                "trait_tags": {"Tourism-Travel": 1.0, "Environmental-Sci": 0.8, "People-Skill": 0.4, "Hospitality-Svc": 0.4, "Investigative": 0.36, "Enterprising": 0.35}
            },
            {
                "option_id": 2244,
                "option_text": "Food and culinary tours featuring regional cuisine",
                "trait_tags": {"Culinary-Arts": 1.0, "Tourism-Travel": 0.8, "Creative-Skill": 0.35, "Hospitality-Svc": 0.35, "People-Skill": 0.32, "Artistic": 0.3}
            },
            {
                "option_id": 2245,
                "option_text": "Luxury resort experiences and spa packages",
                "trait_tags": {"Hospitality-Svc": 1.0, "Marketing-Sales": 0.8, "People-Skill": 0.45, "Tourism-Travel": 0.4, "Enterprising": 0.36, "Culinary-Arts": 0.3}
            },
            {
                "option_id": 2246,
                "option_text": "Building a travel booking app for tourists",
                "trait_tags": {"Web-Dev": 1.0, "Software-Dev": 0.8, "Technical-Skill": 0.45, "Investigative": 0.35, "Mobile-Dev": 0.3, "Digital-Media": 0.25}
            },
            {
                "option_id": 2247,
                "option_text": "Creating travel vlogs and destination videos",
                "trait_tags": {"Film-Broadcast": 1.0, "Digital-Media": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Visual-Design": 0.25, "Technical-Skill": 0.2}
            },
            {
                "option_id": 2248,
                "option_text": "Sustainable tourism that protects local communities",
                "trait_tags": {"Tourism-Travel": 1.0, "Community-Serve": 0.8, "People-Skill": 0.4, "Hospitality-Svc": 0.4, "Social": 0.36, "Enterprising": 0.35}
            }
        ]
    },
    {
        "question_id": 225,
        "question_text": "A hotel chain offers you a management trainee position. What area interests you most?",
        "category": "Preference - Hotel Management",
        "options": [
            {
                "option_id": 2251,
                "option_text": "Guest services — making sure every visitor is happy",
                "trait_tags": {"Hospitality-Svc": 1.0, "People-Skill": 0.8, "Tourism-Travel": 0.4, "Social": 0.36, "Enterprising": 0.35, "Teaching-Ed": 0.32}
            },
            {
                "option_id": 2252,
                "option_text": "Food and beverage management — running restaurants",
                "trait_tags": {"Culinary-Arts": 1.0, "Hospitality-Svc": 0.8, "People-Skill": 0.36, "Creative-Skill": 0.35, "Tourism-Travel": 0.32, "Artistic": 0.3}
            },
            {
                "option_id": 2253,
                "option_text": "Revenue management — pricing rooms for profit",
                "trait_tags": {"Finance-Acct": 1.0, "Hospitality-Svc": 0.8, "Conventional": 0.45, "Analytical-Skill": 0.4, "People-Skill": 0.36, "Tourism-Travel": 0.32}
            },
            {
                "option_id": 2254,
                "option_text": "Human resources — hiring and training hotel staff",
                "trait_tags": {"HR-Management": 1.0, "People-Skill": 0.8, "Social": 0.36, "Enterprising": 0.35, "Admin-Skill": 0.35, "Teaching-Ed": 0.32}
            },
            {
                "option_id": 2255,
                "option_text": "Housekeeping operations — quality and cleanliness",
                "trait_tags": {"Hospitality-Svc": 1.0, "Admin-Skill": 0.8, "People-Skill": 0.45, "Tourism-Travel": 0.4, "Conventional": 0.36, "Enterprising": 0.35}
            },
            {
                "option_id": 2256,
                "option_text": "Convention and banquet management — big events",
                "trait_tags": {"Hospitality-Svc": 1.0, "Marketing-Sales": 0.8, "People-Skill": 0.45, "Tourism-Travel": 0.4, "Enterprising": 0.36, "Culinary-Arts": 0.3}
            },
            {
                "option_id": 2257,
                "option_text": "Hotel technology systems — property management software",
                "trait_tags": {"Software-Dev": 1.0, "Hospitality-Svc": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "People-Skill": 0.36, "Data-Analytics": 0.3}
            },
            {
                "option_id": 2258,
                "option_text": "Sustainability officer — making the hotel eco-friendly",
                "trait_tags": {"Environmental-Sci": 1.0, "Hospitality-Svc": 0.8, "Investigative": 0.45, "Field-Research": 0.4, "People-Skill": 0.36, "Tourism-Travel": 0.32}
            }
        ]
    },
    {
        "question_id": 226,
        "question_text": "You're creating a tourism campaign for your province. What would you do?",
        "category": "Situational - Tourism Marketing",
        "options": [
            {
                "option_id": 2261,
                "option_text": "Design brochures and travel guides with beautiful photos",
                "trait_tags": {"Tourism-Travel": 1.0, "Visual-Design": 0.8, "People-Skill": 0.4, "Hospitality-Svc": 0.4, "Artistic": 0.36, "Creative-Skill": 0.36}
            },
            {
                "option_id": 2262,
                "option_text": "Create a social media campaign with influencer partnerships",
                "trait_tags": {"Marketing-Sales": 1.0, "Digital-Media": 0.8, "Enterprising": 0.45, "People-Skill": 0.4, "Artistic": 0.32, "Creative-Skill": 0.32}
            },
            {
                "option_id": 2263,
                "option_text": "Build a tourism website with online booking features",
                "trait_tags": {"Web-Dev": 1.0, "Tourism-Travel": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Investigative": 0.35, "People-Skill": 0.32}
            },
            {
                "option_id": 2264,
                "option_text": "Produce a documentary about local culture and traditions",
                "trait_tags": {"Film-Broadcast": 1.0, "Tourism-Travel": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Digital-Media": 0.4, "People-Skill": 0.32}
            },
            {
                "option_id": 2265,
                "option_text": "Organize a food festival showcasing regional dishes",
                "trait_tags": {"Culinary-Arts": 1.0, "Tourism-Travel": 0.8, "Creative-Skill": 0.35, "Hospitality-Svc": 0.35, "People-Skill": 0.32, "Artistic": 0.3}
            },
            {
                "option_id": 2266,
                "option_text": "Develop an AR app showing historical landmarks",
                "trait_tags": {"Mobile-Dev": 1.0, "Tourism-Travel": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Investigative": 0.35, "People-Skill": 0.32}
            },
            {
                "option_id": 2267,
                "option_text": "Create adventure tour packages for thrill-seekers",
                "trait_tags": {"Tourism-Travel": 1.0, "Physical-Skill": 0.8, "People-Skill": 0.4, "Hospitality-Svc": 0.4, "Enterprising": 0.35, "Realistic": 0.32}
            },
            {
                "option_id": 2268,
                "option_text": "Work with local communities to promote homestay programs",
                "trait_tags": {"Tourism-Travel": 1.0, "Community-Serve": 0.8, "People-Skill": 0.4, "Hospitality-Svc": 0.4, "Social": 0.36, "Enterprising": 0.35}
            }
        ]
    },
    {
        "question_id": 227,
        "question_text": "You're volunteering at a hospital. Which department would you choose?",
        "category": "Situational - Healthcare Career",
        "options": [
            {
                "option_id": 2271,
                "option_text": "Emergency room — helping in critical situations",
                "trait_tags": {"Patient-Care": 1.0, "Physical-Skill": 0.8, "People-Skill": 0.45, "Social": 0.4, "Realistic": 0.32, "Rehab-Therapy": 0.3}
            },
            {
                "option_id": 2272,
                "option_text": "Laboratory — running diagnostic tests on samples",
                "trait_tags": {"Medical-Lab": 1.0, "Lab-Research": 0.8, "Analytical-Skill": 0.45, "Investigative": 0.4, "Technical-Skill": 0.25, "Patient-Care": 0.2}
            },
            {
                "option_id": 2273,
                "option_text": "Pharmacy — dispensing and managing medications",
                "trait_tags": {"Pharmacy": 1.0, "Patient-Care": 0.8, "Investigative": 0.4, "Analytical-Skill": 0.4, "People-Skill": 0.36, "Medical-Lab": 0.35}
            },
            {
                "option_id": 2274,
                "option_text": "Physical therapy — helping patients recover movement",
                "trait_tags": {"Rehab-Therapy": 1.0, "Physical-Skill": 0.8, "Social": 0.35, "People-Skill": 0.35, "Realistic": 0.32, "Patient-Care": 0.3}
            },
            {
                "option_id": 2275,
                "option_text": "Hospital administration — managing operations and records",
                "trait_tags": {"Health-Admin": 1.0, "Admin-Skill": 0.8, "Conventional": 0.4, "Finance-Acct": 0.24, "Hospitality-Svc": 0.16, "Patient-Care": 0.15}
            },
            {
                "option_id": 2276,
                "option_text": "Nutrition department — planning patient meal programs",
                "trait_tags": {"Nutrition-Diet": 1.0, "Patient-Care": 0.8, "People-Skill": 0.36, "Food-Science": 0.35, "Social": 0.32, "Analytical-Skill": 0.3}
            },
            {
                "option_id": 2277,
                "option_text": "Public health outreach — community vaccination drives",
                "trait_tags": {"Public-Health": 1.0, "Community-Serve": 0.8, "Social": 0.4, "Analytical-Skill": 0.35, "People-Skill": 0.32, "Patient-Care": 0.25}
            },
            {
                "option_id": 2278,
                "option_text": "Medical records and health informatics — digital systems",
                "trait_tags": {"Health-Admin": 1.0, "Software-Dev": 0.8, "Admin-Skill": 0.45, "Conventional": 0.4, "Technical-Skill": 0.36, "Investigative": 0.32}
            }
        ]
    },
    {
        "question_id": 228,
        "question_text": "A pharmaceutical company offers you an internship. What role excites you?",
        "category": "Situational - Pharmacy Career",
        "options": [
            {
                "option_id": 2281,
                "option_text": "Drug formulation research — creating new medicines",
                "trait_tags": {"Pharmacy": 1.0, "Lab-Research": 0.8, "Investigative": 0.4, "Analytical-Skill": 0.4, "Medical-Lab": 0.35, "Patient-Care": 0.25}
            },
            {
                "option_id": 2282,
                "option_text": "Quality control — testing drug safety and purity",
                "trait_tags": {"Pharmacy": 1.0, "Medical-Lab": 0.8, "Investigative": 0.4, "Analytical-Skill": 0.4, "Lab-Research": 0.28, "Patient-Care": 0.25}
            },
            {
                "option_id": 2283,
                "option_text": "Clinical trials — testing medicines on patients",
                "trait_tags": {"Pharmacy": 1.0, "Patient-Care": 0.8, "Investigative": 0.4, "Analytical-Skill": 0.4, "People-Skill": 0.36, "Medical-Lab": 0.35}
            },
            {
                "option_id": 2284,
                "option_text": "Pharmacovigilance — monitoring drug side effects",
                "trait_tags": {"Pharmacy": 1.0, "Public-Health": 0.8, "Investigative": 0.4, "Analytical-Skill": 0.4, "Medical-Lab": 0.35, "Social": 0.32}
            },
            {
                "option_id": 2285,
                "option_text": "Pharmaceutical sales — marketing medicines to doctors",
                "trait_tags": {"Marketing-Sales": 1.0, "Pharmacy": 0.8, "Enterprising": 0.45, "People-Skill": 0.4, "Investigative": 0.32, "Analytical-Skill": 0.32}
            },
            {
                "option_id": 2286,
                "option_text": "Regulatory affairs — ensuring FDA compliance",
                "trait_tags": {"Pharmacy": 1.0, "Legal-Practice": 0.8, "Investigative": 0.4, "Analytical-Skill": 0.4, "Medical-Lab": 0.35, "Enterprising": 0.28}
            },
            {
                "option_id": 2287,
                "option_text": "Natural product research — studying herbal remedies",
                "trait_tags": {"Pharmacy": 1.0, "Field-Research": 0.8, "Investigative": 0.4, "Analytical-Skill": 0.4, "Medical-Lab": 0.35, "Patient-Care": 0.25}
            },
            {
                "option_id": 2288,
                "option_text": "Hospital pharmacy — dispensing prescriptions to patients",
                "trait_tags": {"Pharmacy": 1.0, "Patient-Care": 0.8, "Investigative": 0.4, "Analytical-Skill": 0.4, "People-Skill": 0.36, "Medical-Lab": 0.35}
            }
        ]
    },
    {
        "question_id": 229,
        "question_text": "You want to help people with health issues. What approach appeals to you?",
        "category": "Interest - Rehabilitation",
        "options": [
            {
                "option_id": 2291,
                "option_text": "Physical therapy — helping people walk and move again",
                "trait_tags": {"Rehab-Therapy": 1.0, "Physical-Skill": 0.8, "Social": 0.35, "People-Skill": 0.35, "Realistic": 0.32, "Patient-Care": 0.3}
            },
            {
                "option_id": 2292,
                "option_text": "Occupational therapy — helping people do daily tasks",
                "trait_tags": {"Rehab-Therapy": 1.0, "Patient-Care": 0.8, "Physical-Skill": 0.4, "People-Skill": 0.36, "Social": 0.35, "Teaching-Ed": 0.2}
            },
            {
                "option_id": 2293,
                "option_text": "Speech therapy — helping people communicate better",
                "trait_tags": {"Rehab-Therapy": 1.0, "Teaching-Ed": 0.8, "Physical-Skill": 0.4, "Social": 0.36, "People-Skill": 0.36, "Patient-Care": 0.3}
            },
            {
                "option_id": 2294,
                "option_text": "Sports rehabilitation — getting athletes back in the game",
                "trait_tags": {"Rehab-Therapy": 1.0, "Sports-Ed": 0.8, "Physical-Skill": 0.4, "Social": 0.35, "People-Skill": 0.35, "Patient-Care": 0.3}
            },
            {
                "option_id": 2295,
                "option_text": "Mental health counseling — supporting emotional recovery",
                "trait_tags": {"Counseling": 1.0, "Patient-Care": 0.8, "Social": 0.45, "People-Skill": 0.45, "Teaching-Ed": 0.3, "Rehab-Therapy": 0.25}
            },
            {
                "option_id": 2296,
                "option_text": "Nutritional therapy — using food to heal the body",
                "trait_tags": {"Nutrition-Diet": 1.0, "Rehab-Therapy": 0.8, "Food-Science": 0.35, "Physical-Skill": 0.32, "Social": 0.3, "Analytical-Skill": 0.3}
            },
            {
                "option_id": 2297,
                "option_text": "Medical technology — developing rehabilitation devices",
                "trait_tags": {"Medical-Lab": 1.0, "Hardware-Systems": 0.8, "Analytical-Skill": 0.45, "Investigative": 0.4, "Technical-Skill": 0.36, "Lab-Research": 0.35}
            },
            {
                "option_id": 2298,
                "option_text": "Community health programs — preventing illness in barangays",
                "trait_tags": {"Public-Health": 1.0, "Community-Serve": 0.8, "Social": 0.4, "Analytical-Skill": 0.35, "People-Skill": 0.32, "Patient-Care": 0.25}
            }
        ]
    },
    {
        "question_id": 230,
        "question_text": "A health clinic needs help improving patient care. What would you focus on?",
        "category": "Situational - Health Admin",
        "options": [
            {
                "option_id": 2301,
                "option_text": "Streamlining patient records with a digital system",
                "trait_tags": {"Health-Admin": 1.0, "Software-Dev": 0.8, "Admin-Skill": 0.45, "Conventional": 0.4, "Technical-Skill": 0.36, "Investigative": 0.32}
            },
            {
                "option_id": 2302,
                "option_text": "Training nurses and staff on better care protocols",
                "trait_tags": {"Health-Admin": 1.0, "Teaching-Ed": 0.8, "Admin-Skill": 0.45, "Conventional": 0.4, "Social": 0.36, "People-Skill": 0.36}
            },
            {
                "option_id": 2303,
                "option_text": "Managing the clinic budget and resource allocation",
                "trait_tags": {"Health-Admin": 1.0, "Finance-Acct": 0.8, "Admin-Skill": 0.45, "Conventional": 0.4, "Analytical-Skill": 0.32, "Startup-Venture": 0.16}
            },
            {
                "option_id": 2304,
                "option_text": "Running lab diagnostics to catch diseases early",
                "trait_tags": {"Medical-Lab": 1.0, "Lab-Research": 0.8, "Analytical-Skill": 0.45, "Investigative": 0.4, "Technical-Skill": 0.25, "Patient-Care": 0.2}
            },
            {
                "option_id": 2305,
                "option_text": "Creating public health campaigns for disease prevention",
                "trait_tags": {"Public-Health": 1.0, "Marketing-Sales": 0.8, "Social": 0.4, "Enterprising": 0.36, "Analytical-Skill": 0.35, "Community-Serve": 0.35}
            },
            {
                "option_id": 2306,
                "option_text": "Setting up a community pharmacy with affordable meds",
                "trait_tags": {"Pharmacy": 1.0, "Community-Serve": 0.8, "Investigative": 0.4, "Analytical-Skill": 0.4, "Social": 0.36, "Medical-Lab": 0.35}
            },
            {
                "option_id": 2307,
                "option_text": "Designing meal plans for patients with special diets",
                "trait_tags": {"Nutrition-Diet": 1.0, "Food-Science": 0.8, "Investigative": 0.32, "Social": 0.3, "Analytical-Skill": 0.3, "Lab-Research": 0.28}
            },
            {
                "option_id": 2308,
                "option_text": "Building emergency response protocols for disasters",
                "trait_tags": {"Health-Admin": 1.0, "Public-Health": 0.8, "Admin-Skill": 0.45, "Conventional": 0.4, "Social": 0.32, "Analytical-Skill": 0.28}
            }
        ]
    },
    {
        "question_id": 231,
        "question_text": "What aspect of nutrition and food science interests you most?",
        "category": "Interest - Nutrition Science",
        "options": [
            {
                "option_id": 2311,
                "option_text": "Creating personalized diet plans based on health conditions",
                "trait_tags": {"Nutrition-Diet": 1.0, "Patient-Care": 0.8, "People-Skill": 0.36, "Food-Science": 0.35, "Social": 0.32, "Analytical-Skill": 0.3}
            },
            {
                "option_id": 2312,
                "option_text": "Researching how nutrients affect the human body",
                "trait_tags": {"Nutrition-Diet": 1.0, "Lab-Research": 0.8, "Analytical-Skill": 0.36, "Investigative": 0.36, "Food-Science": 0.35, "Social": 0.3}
            },
            {
                "option_id": 2313,
                "option_text": "Food product development and testing new recipes",
                "trait_tags": {"Food-Science": 1.0, "Culinary-Arts": 0.8, "Investigative": 0.4, "Lab-Research": 0.35, "Nutrition-Diet": 0.35, "Analytical-Skill": 0.3}
            },
            {
                "option_id": 2314,
                "option_text": "Food safety inspection and quality control",
                "trait_tags": {"Food-Science": 1.0, "Health-Admin": 0.8, "Investigative": 0.4, "Lab-Research": 0.35, "Nutrition-Diet": 0.35, "Conventional": 0.32}
            },
            {
                "option_id": 2315,
                "option_text": "Sports nutrition — optimizing athlete performance",
                "trait_tags": {"Nutrition-Diet": 1.0, "Sports-Ed": 0.8, "Physical-Skill": 0.36, "Food-Science": 0.35, "Social": 0.3, "Analytical-Skill": 0.3}
            },
            {
                "option_id": 2316,
                "option_text": "Community nutrition programs for malnourished children",
                "trait_tags": {"Nutrition-Diet": 1.0, "Public-Health": 0.8, "Food-Science": 0.35, "Social": 0.32, "Analytical-Skill": 0.3, "Community-Serve": 0.28}
            },
            {
                "option_id": 2317,
                "option_text": "Food technology — preserving food for longer shelf life",
                "trait_tags": {"Food-Science": 1.0, "Lab-Research": 0.8, "Investigative": 0.4, "Analytical-Skill": 0.36, "Nutrition-Diet": 0.35, "Medical-Lab": 0.24}
            },
            {
                "option_id": 2318,
                "option_text": "Restaurant menu design combining taste and health",
                "trait_tags": {"Culinary-Arts": 1.0, "Nutrition-Diet": 0.8, "Creative-Skill": 0.35, "Hospitality-Svc": 0.35, "Artistic": 0.3, "Food-Science": 0.28}
            }
        ]
    },
    {
        "question_id": 232,
        "question_text": "Your barangay is dealing with a health crisis. What would you do to help?",
        "category": "Situational - Public Health",
        "options": [
            {
                "option_id": 2321,
                "option_text": "Organize vaccination drives and health screenings",
                "trait_tags": {"Public-Health": 1.0, "Community-Serve": 0.8, "Social": 0.4, "Analytical-Skill": 0.35, "People-Skill": 0.32, "Patient-Care": 0.25}
            },
            {
                "option_id": 2322,
                "option_text": "Analyze disease data to identify outbreak patterns",
                "trait_tags": {"Public-Health": 1.0, "Data-Analytics": 0.8, "Social": 0.4, "Analytical-Skill": 0.36, "Investigative": 0.36, "Community-Serve": 0.35}
            },
            {
                "option_id": 2323,
                "option_text": "Train community health workers on first aid",
                "trait_tags": {"Public-Health": 1.0, "Teaching-Ed": 0.8, "Social": 0.4, "People-Skill": 0.36, "Analytical-Skill": 0.35, "Community-Serve": 0.35}
            },
            {
                "option_id": 2324,
                "option_text": "Set up a temporary clinic with basic medical services",
                "trait_tags": {"Patient-Care": 1.0, "Health-Admin": 0.8, "People-Skill": 0.45, "Social": 0.4, "Admin-Skill": 0.36, "Conventional": 0.32}
            },
            {
                "option_id": 2325,
                "option_text": "Create educational materials about disease prevention",
                "trait_tags": {"Public-Health": 1.0, "Visual-Design": 0.8, "Social": 0.4, "Artistic": 0.36, "Creative-Skill": 0.36, "Analytical-Skill": 0.35}
            },
            {
                "option_id": 2326,
                "option_text": "Distribute food and nutrition supplements to families",
                "trait_tags": {"Nutrition-Diet": 1.0, "Community-Serve": 0.8, "Social": 0.36, "Food-Science": 0.35, "People-Skill": 0.32, "Analytical-Skill": 0.3}
            },
            {
                "option_id": 2327,
                "option_text": "Counsel affected families on mental health and coping",
                "trait_tags": {"Counseling": 1.0, "Social-Work": 0.8, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.32, "Teaching-Ed": 0.3}
            },
            {
                "option_id": 2328,
                "option_text": "Test water and food samples for contamination",
                "trait_tags": {"Medical-Lab": 1.0, "Environmental-Sci": 0.8, "Analytical-Skill": 0.45, "Investigative": 0.4, "Lab-Research": 0.35, "Field-Research": 0.32}
            }
        ]
    },
    {
        "question_id": 233,
        "question_text": "You're working in a medical laboratory. What type of testing interests you most?",
        "category": "Interest - Medical Laboratory",
        "options": [
            {
                "option_id": 2331,
                "option_text": "Blood analysis and hematology testing",
                "trait_tags": {"Medical-Lab": 1.0, "Lab-Research": 0.8, "Analytical-Skill": 0.45, "Investigative": 0.4, "Technical-Skill": 0.25, "Patient-Care": 0.2}
            },
            {
                "option_id": 2332,
                "option_text": "Microbiology — identifying bacteria and viruses",
                "trait_tags": {"Medical-Lab": 1.0, "Lab-Research": 0.8, "Analytical-Skill": 0.45, "Investigative": 0.4, "Technical-Skill": 0.25, "Patient-Care": 0.2}
            },
            {
                "option_id": 2333,
                "option_text": "Clinical chemistry — analyzing body fluids",
                "trait_tags": {"Medical-Lab": 1.0, "Pharmacy": 0.8, "Analytical-Skill": 0.45, "Investigative": 0.4, "Lab-Research": 0.35, "Technical-Skill": 0.25}
            },
            {
                "option_id": 2334,
                "option_text": "Histopathology — examining tissue samples for disease",
                "trait_tags": {"Medical-Lab": 1.0, "Patient-Care": 0.8, "Analytical-Skill": 0.45, "Investigative": 0.4, "People-Skill": 0.36, "Lab-Research": 0.35}
            },
            {
                "option_id": 2335,
                "option_text": "Immunology — studying the immune system response",
                "trait_tags": {"Medical-Lab": 1.0, "Lab-Research": 0.8, "Analytical-Skill": 0.45, "Investigative": 0.4, "Technical-Skill": 0.25, "Patient-Care": 0.2}
            },
            {
                "option_id": 2336,
                "option_text": "Forensic laboratory — analyzing evidence for crimes",
                "trait_tags": {"Forensic-Sci": 1.0, "Medical-Lab": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.4, "Lab-Research": 0.35, "Law-Enforce": 0.35}
            },
            {
                "option_id": 2337,
                "option_text": "Food and drug testing — ensuring product safety",
                "trait_tags": {"Food-Science": 1.0, "Medical-Lab": 0.8, "Investigative": 0.4, "Analytical-Skill": 0.36, "Lab-Research": 0.35, "Nutrition-Diet": 0.35}
            },
            {
                "option_id": 2338,
                "option_text": "Molecular diagnostics — DNA and genetic testing",
                "trait_tags": {"Medical-Lab": 1.0, "Lab-Research": 0.8, "Analytical-Skill": 0.45, "Investigative": 0.4, "Technical-Skill": 0.25, "Patient-Care": 0.2}
            }
        ]
    },
    {
        "question_id": 234,
        "question_text": "A crime has been committed in your area. What role would you want to play?",
        "category": "Situational - Law Enforcement",
        "options": [
            {
                "option_id": 2341,
                "option_text": "Investigating the crime scene and collecting evidence",
                "trait_tags": {"Law-Enforce": 1.0, "Forensic-Sci": 0.8, "Investigative": 0.36, "Realistic": 0.35, "Physical-Skill": 0.35, "Analytical-Skill": 0.32}
            },
            {
                "option_id": 2342,
                "option_text": "Interviewing witnesses and analyzing testimonies",
                "trait_tags": {"Law-Enforce": 1.0, "People-Skill": 0.8, "Social": 0.36, "Realistic": 0.35, "Physical-Skill": 0.35, "Patient-Care": 0.32}
            },
            {
                "option_id": 2343,
                "option_text": "Running forensic lab tests on physical evidence",
                "trait_tags": {"Forensic-Sci": 1.0, "Medical-Lab": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.4, "Lab-Research": 0.35, "Law-Enforce": 0.35}
            },
            {
                "option_id": 2344,
                "option_text": "Analyzing digital evidence — phones, computers, CCTV",
                "trait_tags": {"Forensic-Sci": 1.0, "Cyber-Defense": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.4, "Lab-Research": 0.35, "Law-Enforce": 0.35}
            },
            {
                "option_id": 2345,
                "option_text": "Prosecuting the case in court as a lawyer",
                "trait_tags": {"Legal-Practice": 1.0, "Law-Enforce": 0.8, "Enterprising": 0.35, "Analytical-Skill": 0.35, "People-Skill": 0.3, "Realistic": 0.28}
            },
            {
                "option_id": 2346,
                "option_text": "Community policing — building trust with residents",
                "trait_tags": {"Law-Enforce": 1.0, "Community-Serve": 0.8, "Social": 0.36, "Realistic": 0.35, "Physical-Skill": 0.35, "People-Skill": 0.32}
            },
            {
                "option_id": 2347,
                "option_text": "Crime data analysis — finding patterns in criminal activity",
                "trait_tags": {"Law-Enforce": 1.0, "Data-Analytics": 0.8, "Investigative": 0.36, "Analytical-Skill": 0.36, "Realistic": 0.35, "Physical-Skill": 0.35}
            },
            {
                "option_id": 2348,
                "option_text": "Victim support — counseling people affected by crime",
                "trait_tags": {"Counseling": 1.0, "Social-Work": 0.8, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.32, "Teaching-Ed": 0.3}
            }
        ]
    },
    {
        "question_id": 235,
        "question_text": "You're studying criminology. What specialization would you choose?",
        "category": "Interest - Criminology Specialization",
        "options": [
            {
                "option_id": 2351,
                "option_text": "Criminal investigation and detective work",
                "trait_tags": {"Law-Enforce": 1.0, "Analytical-Skill": 0.8, "Investigative": 0.36, "Realistic": 0.35, "Physical-Skill": 0.35, "Data-Analytics": 0.32}
            },
            {
                "option_id": 2352,
                "option_text": "Forensic science — using science to solve crimes",
                "trait_tags": {"Forensic-Sci": 1.0, "Lab-Research": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.4, "Law-Enforce": 0.35, "Medical-Lab": 0.24}
            },
            {
                "option_id": 2353,
                "option_text": "Cybercrime investigation — tracking hackers online",
                "trait_tags": {"Law-Enforce": 1.0, "Cyber-Defense": 0.8, "Realistic": 0.35, "Physical-Skill": 0.35, "Technical-Skill": 0.32, "Investigative": 0.28}
            },
            {
                "option_id": 2354,
                "option_text": "Corrections and rehabilitation — reforming offenders",
                "trait_tags": {"Law-Enforce": 1.0, "Counseling": 0.8, "Social": 0.36, "People-Skill": 0.36, "Realistic": 0.35, "Physical-Skill": 0.35}
            },
            {
                "option_id": 2355,
                "option_text": "Crime prevention through community programs",
                "trait_tags": {"Law-Enforce": 1.0, "Community-Serve": 0.8, "Social": 0.36, "Realistic": 0.35, "Physical-Skill": 0.35, "People-Skill": 0.32}
            },
            {
                "option_id": 2356,
                "option_text": "Drug enforcement and narcotics investigation",
                "trait_tags": {"Law-Enforce": 1.0, "Forensic-Sci": 0.8, "Investigative": 0.36, "Realistic": 0.35, "Physical-Skill": 0.35, "Analytical-Skill": 0.32}
            },
            {
                "option_id": 2357,
                "option_text": "Traffic management and road safety enforcement",
                "trait_tags": {"Law-Enforce": 1.0, "Admin-Skill": 0.8, "Conventional": 0.36, "Realistic": 0.35, "Physical-Skill": 0.35, "Health-Admin": 0.28}
            },
            {
                "option_id": 2358,
                "option_text": "Industrial security and private investigation",
                "trait_tags": {"Law-Enforce": 1.0, "People-Skill": 0.8, "Social": 0.36, "Realistic": 0.35, "Physical-Skill": 0.35, "Patient-Care": 0.32}
            }
        ]
    },
    {
        "question_id": 236,
        "question_text": "What type of forensic work fascinates you?",
        "category": "Interest - Forensic Science",
        "options": [
            {
                "option_id": 2361,
                "option_text": "DNA analysis and genetic profiling",
                "trait_tags": {"Forensic-Sci": 1.0, "Lab-Research": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.4, "Law-Enforce": 0.35, "Medical-Lab": 0.24}
            },
            {
                "option_id": 2362,
                "option_text": "Fingerprint and ballistics analysis",
                "trait_tags": {"Forensic-Sci": 1.0, "Medical-Lab": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.4, "Lab-Research": 0.35, "Law-Enforce": 0.35}
            },
            {
                "option_id": 2363,
                "option_text": "Toxicology — detecting poisons and drugs in the body",
                "trait_tags": {"Forensic-Sci": 1.0, "Pharmacy": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.4, "Lab-Research": 0.35, "Law-Enforce": 0.35}
            },
            {
                "option_id": 2364,
                "option_text": "Digital forensics — recovering deleted computer files",
                "trait_tags": {"Forensic-Sci": 1.0, "Cyber-Defense": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.4, "Lab-Research": 0.35, "Law-Enforce": 0.35}
            },
            {
                "option_id": 2365,
                "option_text": "Crime scene photography and documentation",
                "trait_tags": {"Forensic-Sci": 1.0, "Visual-Design": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.4, "Artistic": 0.36, "Creative-Skill": 0.36}
            },
            {
                "option_id": 2366,
                "option_text": "Forensic accounting — tracking financial crimes",
                "trait_tags": {"Forensic-Sci": 1.0, "Finance-Acct": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.4, "Conventional": 0.36, "Lab-Research": 0.35}
            },
            {
                "option_id": 2367,
                "option_text": "Forensic psychology — profiling criminal behavior",
                "trait_tags": {"Forensic-Sci": 1.0, "Counseling": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.4, "Social": 0.36, "People-Skill": 0.36}
            },
            {
                "option_id": 2368,
                "option_text": "Environmental forensics — investigating pollution crimes",
                "trait_tags": {"Forensic-Sci": 1.0, "Environmental-Sci": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.4, "Lab-Research": 0.35, "Law-Enforce": 0.35}
            }
        ]
    },
    {
        "question_id": 237,
        "question_text": "An engineering company offers you an apprenticeship. Which department would you choose?",
        "category": "Situational - Engineering Career",
        "options": [
            {
                "option_id": 2371,
                "option_text": "Structural design — buildings and bridges",
                "trait_tags": {"Civil-Build": 1.0, "Spatial-Design": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Artistic": 0.28, "Creative-Skill": 0.28}
            },
            {
                "option_id": 2372,
                "option_text": "Electrical systems — power grids and circuits",
                "trait_tags": {"Electrical-Power": 1.0, "Hardware-Systems": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Mechanical-Design": 0.2, "Industrial-Ops": 0.2}
            },
            {
                "option_id": 2373,
                "option_text": "Industrial automation — robots and factory systems",
                "trait_tags": {"Industrial-Ops": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.36, "Analytical-Skill": 0.35, "Technical-Skill": 0.32, "Enterprising": 0.3}
            },
            {
                "option_id": 2374,
                "option_text": "Mechanical design — engines and machinery",
                "trait_tags": {"Mechanical-Design": 1.0, "Technical-Skill": 0.8, "Realistic": 0.45, "Software-Dev": 0.32, "Hardware-Systems": 0.32, "Industrial-Ops": 0.25}
            },
            {
                "option_id": 2375,
                "option_text": "Environmental engineering — water treatment and waste",
                "trait_tags": {"Environmental-Eng": 1.0, "Environmental-Sci": 0.8, "Realistic": 0.4, "Investigative": 0.36, "Technical-Skill": 0.35, "Field-Research": 0.32}
            },
            {
                "option_id": 2376,
                "option_text": "Electronics and embedded systems — circuit boards",
                "trait_tags": {"Electrical-Power": 1.0, "Hardware-Systems": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Mechanical-Design": 0.2, "Industrial-Ops": 0.2}
            },
            {
                "option_id": 2377,
                "option_text": "Computer engineering — hardware-software integration",
                "trait_tags": {"Hardware-Systems": 1.0, "Software-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Investigative": 0.32, "Electrical-Power": 0.3}
            },
            {
                "option_id": 2378,
                "option_text": "Mining and geological engineering",
                "trait_tags": {"Civil-Build": 1.0, "Field-Research": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Investigative": 0.32, "Spatial-Design": 0.25}
            }
        ]
    },
    {
        "question_id": 238,
        "question_text": "Your team needs to solve a power problem in a remote province. What do you suggest?",
        "category": "Situational - Electrical Engineering",
        "options": [
            {
                "option_id": 2381,
                "option_text": "Design a solar panel system for the community",
                "trait_tags": {"Electrical-Power": 1.0, "Environmental-Eng": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3, "Environmental-Sci": 0.28}
            },
            {
                "option_id": 2382,
                "option_text": "Build a micro-hydroelectric power plant on a river",
                "trait_tags": {"Electrical-Power": 1.0, "Civil-Build": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 2383,
                "option_text": "Set up a wind turbine farm in a hilly area",
                "trait_tags": {"Electrical-Power": 1.0, "Mechanical-Design": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3, "Industrial-Ops": 0.2}
            },
            {
                "option_id": 2384,
                "option_text": "Install a diesel generator with smart grid management",
                "trait_tags": {"Electrical-Power": 1.0, "Industrial-Ops": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3, "Analytical-Skill": 0.28}
            },
            {
                "option_id": 2385,
                "option_text": "Design an IoT system to monitor and optimize power usage",
                "trait_tags": {"Hardware-Systems": 1.0, "Cloud-Systems": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Electrical-Power": 0.3, "Software-Dev": 0.28}
            },
            {
                "option_id": 2386,
                "option_text": "Extend the main power grid with new transmission lines",
                "trait_tags": {"Electrical-Power": 1.0, "Civil-Build": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 2387,
                "option_text": "Create a battery storage system for reliable backup",
                "trait_tags": {"Electrical-Power": 1.0, "Technical-Skill": 0.8, "Realistic": 0.4, "Hardware-Systems": 0.32, "Software-Dev": 0.32, "Mechanical-Design": 0.28}
            },
            {
                "option_id": 2388,
                "option_text": "Develop a mobile app for residents to monitor electricity use",
                "trait_tags": {"Mobile-Dev": 1.0, "Electrical-Power": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Investigative": 0.35, "Realistic": 0.32}
            }
        ]
    },
    {
        "question_id": 239,
        "question_text": "What kind of machine or system would you love to design?",
        "category": "Interest - Mechanical Design",
        "options": [
            {
                "option_id": 2391,
                "option_text": "A fuel-efficient engine for Filipino-made vehicles",
                "trait_tags": {"Mechanical-Design": 1.0, "Industrial-Ops": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Analytical-Skill": 0.28, "Enterprising": 0.24}
            },
            {
                "option_id": 2392,
                "option_text": "A robotic arm for automated assembly lines",
                "trait_tags": {"Mechanical-Design": 1.0, "Industrial-Ops": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Analytical-Skill": 0.28, "Enterprising": 0.24}
            },
            {
                "option_id": 2393,
                "option_text": "An HVAC system for energy-efficient buildings",
                "trait_tags": {"Mechanical-Design": 1.0, "Environmental-Eng": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Environmental-Sci": 0.28, "Industrial-Ops": 0.25}
            },
            {
                "option_id": 2394,
                "option_text": "A water purification machine for rural areas",
                "trait_tags": {"Mechanical-Design": 1.0, "Environmental-Eng": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Environmental-Sci": 0.28, "Industrial-Ops": 0.25}
            },
            {
                "option_id": 2395,
                "option_text": "Agricultural machinery for Filipino farmers",
                "trait_tags": {"Mechanical-Design": 1.0, "Agri-Nature": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Physical-Skill": 0.28, "Industrial-Ops": 0.25}
            },
            {
                "option_id": 2396,
                "option_text": "A 3D printer that can build house components",
                "trait_tags": {"Mechanical-Design": 1.0, "Civil-Build": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Industrial-Ops": 0.25, "Electrical-Power": 0.2}
            },
            {
                "option_id": 2397,
                "option_text": "Medical equipment like prosthetic limbs",
                "trait_tags": {"Mechanical-Design": 1.0, "Rehab-Therapy": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Physical-Skill": 0.32, "Social": 0.28}
            },
            {
                "option_id": 2398,
                "option_text": "Ship engines and marine propulsion systems",
                "trait_tags": {"Mechanical-Design": 1.0, "Maritime-Sea": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Physical-Skill": 0.32, "Industrial-Ops": 0.25}
            }
        ]
    },
    {
        "question_id": 240,
        "question_text": "A factory needs to improve its production line. What would you focus on?",
        "category": "Situational - Industrial Engineering",
        "options": [
            {
                "option_id": 2401,
                "option_text": "Automating repetitive tasks with robotic systems",
                "trait_tags": {"Industrial-Ops": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.36, "Analytical-Skill": 0.35, "Technical-Skill": 0.32, "Enterprising": 0.3}
            },
            {
                "option_id": 2402,
                "option_text": "Optimizing workflow to reduce waste and costs",
                "trait_tags": {"Industrial-Ops": 1.0, "Analytical-Skill": 0.8, "Investigative": 0.36, "Data-Analytics": 0.32, "Enterprising": 0.3, "Finance-Acct": 0.28}
            },
            {
                "option_id": 2403,
                "option_text": "Implementing quality control testing procedures",
                "trait_tags": {"Industrial-Ops": 1.0, "Lab-Research": 0.8, "Analytical-Skill": 0.36, "Investigative": 0.36, "Enterprising": 0.3, "Mechanical-Design": 0.25}
            },
            {
                "option_id": 2404,
                "option_text": "Designing the factory layout for safety and efficiency",
                "trait_tags": {"Industrial-Ops": 1.0, "Spatial-Design": 0.8, "Analytical-Skill": 0.35, "Enterprising": 0.3, "Artistic": 0.28, "Creative-Skill": 0.28}
            },
            {
                "option_id": 2405,
                "option_text": "Installing smart sensors for real-time monitoring",
                "trait_tags": {"Industrial-Ops": 1.0, "Hardware-Systems": 0.8, "Technical-Skill": 0.36, "Analytical-Skill": 0.35, "Realistic": 0.32, "Enterprising": 0.3}
            },
            {
                "option_id": 2406,
                "option_text": "Managing supply chain logistics and inventory",
                "trait_tags": {"Industrial-Ops": 1.0, "Admin-Skill": 0.8, "Conventional": 0.36, "Analytical-Skill": 0.35, "Enterprising": 0.3, "Mechanical-Design": 0.25}
            },
            {
                "option_id": 2407,
                "option_text": "Training workers on new equipment and safety protocols",
                "trait_tags": {"Industrial-Ops": 1.0, "Teaching-Ed": 0.8, "Social": 0.36, "People-Skill": 0.36, "Analytical-Skill": 0.35, "Enterprising": 0.3}
            },
            {
                "option_id": 2408,
                "option_text": "Reducing environmental impact of manufacturing",
                "trait_tags": {"Environmental-Eng": 1.0, "Industrial-Ops": 0.8, "Realistic": 0.4, "Technical-Skill": 0.35, "Environmental-Sci": 0.35, "Analytical-Skill": 0.28}
            }
        ]
    },
    {
        "question_id": 241,
        "question_text": "Your city is building new infrastructure. What project would you want to work on?",
        "category": "Situational - Civil Engineering",
        "options": [
            {
                "option_id": 2411,
                "option_text": "Designing earthquake-resistant buildings",
                "trait_tags": {"Civil-Build": 1.0, "Spatial-Design": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Artistic": 0.28, "Creative-Skill": 0.28}
            },
            {
                "option_id": 2412,
                "option_text": "Building a flood control system for low-lying areas",
                "trait_tags": {"Civil-Build": 1.0, "Environmental-Eng": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Environmental-Sci": 0.28, "Spatial-Design": 0.25}
            },
            {
                "option_id": 2413,
                "option_text": "Constructing a modern highway and bridge network",
                "trait_tags": {"Civil-Build": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Industrial-Ops": 0.2}
            },
            {
                "option_id": 2414,
                "option_text": "Designing the water supply and sewage system",
                "trait_tags": {"Civil-Build": 1.0, "Environmental-Eng": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Environmental-Sci": 0.28, "Spatial-Design": 0.25}
            },
            {
                "option_id": 2415,
                "option_text": "Building schools and hospitals in underserved areas",
                "trait_tags": {"Civil-Build": 1.0, "Community-Serve": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Social": 0.36, "People-Skill": 0.32}
            },
            {
                "option_id": 2416,
                "option_text": "Creating smart traffic management systems",
                "trait_tags": {"Civil-Build": 1.0, "Software-Dev": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Investigative": 0.32, "Spatial-Design": 0.25}
            },
            {
                "option_id": 2417,
                "option_text": "Developing sustainable and green buildings",
                "trait_tags": {"Civil-Build": 1.0, "Environmental-Sci": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Investigative": 0.36, "Field-Research": 0.32}
            },
            {
                "option_id": 2418,
                "option_text": "Port and harbor construction for maritime trade",
                "trait_tags": {"Civil-Build": 1.0, "Maritime-Sea": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Physical-Skill": 0.32, "Spatial-Design": 0.25}
            }
        ]
    },
    {
        "question_id": 242,
        "question_text": "What environmental engineering challenge would you want to solve?",
        "category": "Interest - Environmental Engineering",
        "options": [
            {
                "option_id": 2421,
                "option_text": "Cleaning polluted rivers and waterways",
                "trait_tags": {"Environmental-Eng": 1.0, "Environmental-Sci": 0.8, "Realistic": 0.4, "Investigative": 0.36, "Technical-Skill": 0.35, "Field-Research": 0.32}
            },
            {
                "option_id": 2422,
                "option_text": "Designing waste-to-energy systems for cities",
                "trait_tags": {"Environmental-Eng": 1.0, "Electrical-Power": 0.8, "Realistic": 0.4, "Technical-Skill": 0.36, "Environmental-Sci": 0.35, "Civil-Build": 0.25}
            },
            {
                "option_id": 2423,
                "option_text": "Building sustainable drainage to prevent flooding",
                "trait_tags": {"Environmental-Eng": 1.0, "Civil-Build": 0.8, "Realistic": 0.4, "Technical-Skill": 0.35, "Environmental-Sci": 0.35, "Field-Research": 0.25}
            },
            {
                "option_id": 2424,
                "option_text": "Developing air quality monitoring systems",
                "trait_tags": {"Environmental-Eng": 1.0, "Hardware-Systems": 0.8, "Realistic": 0.4, "Technical-Skill": 0.36, "Environmental-Sci": 0.35, "Civil-Build": 0.25}
            },
            {
                "option_id": 2425,
                "option_text": "Creating sewage treatment plants for communities",
                "trait_tags": {"Environmental-Eng": 1.0, "Civil-Build": 0.8, "Realistic": 0.4, "Technical-Skill": 0.35, "Environmental-Sci": 0.35, "Field-Research": 0.25}
            },
            {
                "option_id": 2426,
                "option_text": "Reducing carbon emissions from industrial sites",
                "trait_tags": {"Environmental-Eng": 1.0, "Industrial-Ops": 0.8, "Realistic": 0.4, "Technical-Skill": 0.35, "Environmental-Sci": 0.35, "Analytical-Skill": 0.28}
            },
            {
                "option_id": 2427,
                "option_text": "Designing recyclable packaging for food products",
                "trait_tags": {"Environmental-Eng": 1.0, "Food-Science": 0.8, "Realistic": 0.4, "Technical-Skill": 0.35, "Environmental-Sci": 0.35, "Investigative": 0.32}
            },
            {
                "option_id": 2428,
                "option_text": "Soil remediation for contaminated farmland",
                "trait_tags": {"Environmental-Eng": 1.0, "Agri-Nature": 0.8, "Realistic": 0.4, "Technical-Skill": 0.35, "Environmental-Sci": 0.35, "Physical-Skill": 0.28}
            }
        ]
    },
    {
        "question_id": 243,
        "question_text": "You see a family in your community struggling with poverty. How would you help?",
        "category": "Situational - Social Work",
        "options": [
            {
                "option_id": 2431,
                "option_text": "Connect them with government assistance programs",
                "trait_tags": {"Social-Work": 1.0, "Community-Serve": 0.8, "Social": 0.45, "People-Skill": 0.45, "Counseling": 0.3, "Teaching-Ed": 0.25}
            },
            {
                "option_id": 2432,
                "option_text": "Provide counseling for the parents dealing with stress",
                "trait_tags": {"Counseling": 1.0, "Social-Work": 0.8, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.32, "Teaching-Ed": 0.3}
            },
            {
                "option_id": 2433,
                "option_text": "Help their children with tutoring and school supplies",
                "trait_tags": {"Teaching-Ed": 1.0, "Social-Work": 0.8, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.32, "Counseling": 0.24}
            },
            {
                "option_id": 2434,
                "option_text": "Organize a livelihood training program for the parents",
                "trait_tags": {"Social-Work": 1.0, "HR-Management": 0.8, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.4, "Counseling": 0.3}
            },
            {
                "option_id": 2435,
                "option_text": "Set up a community feeding program for their children",
                "trait_tags": {"Social-Work": 1.0, "Nutrition-Diet": 0.8, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.4, "Counseling": 0.3}
            },
            {
                "option_id": 2436,
                "option_text": "Advocate for better housing policies at the local government",
                "trait_tags": {"Social-Work": 1.0, "Legal-Practice": 0.8, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.4, "Counseling": 0.3}
            },
            {
                "option_id": 2437,
                "option_text": "Document their situation for a fundraising campaign",
                "trait_tags": {"Social-Work": 1.0, "Digital-Media": 0.8, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.4, "Artistic": 0.32}
            },
            {
                "option_id": 2438,
                "option_text": "Help them start a small home-based business",
                "trait_tags": {"Social-Work": 1.0, "Startup-Venture": 0.8, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.4, "Enterprising": 0.36}
            }
        ]
    },
    {
        "question_id": 244,
        "question_text": "You're organizing a community development project. What would it be?",
        "category": "Situational - Community Development",
        "options": [
            {
                "option_id": 2441,
                "option_text": "A skills training center for out-of-school youth",
                "trait_tags": {"Community-Serve": 1.0, "Teaching-Ed": 0.8, "Social": 0.45, "People-Skill": 0.4, "Patient-Care": 0.2, "Law-Enforce": 0.15}
            },
            {
                "option_id": 2442,
                "option_text": "A free legal aid clinic for residents",
                "trait_tags": {"Community-Serve": 1.0, "Legal-Practice": 0.8, "Social": 0.45, "People-Skill": 0.4, "Enterprising": 0.28, "Analytical-Skill": 0.28}
            },
            {
                "option_id": 2443,
                "option_text": "A community garden and urban farming project",
                "trait_tags": {"Community-Serve": 1.0, "Agri-Nature": 0.8, "Social": 0.45, "People-Skill": 0.4, "Realistic": 0.36, "Physical-Skill": 0.28}
            },
            {
                "option_id": 2444,
                "option_text": "A mental health support group for teenagers",
                "trait_tags": {"Counseling": 1.0, "Community-Serve": 0.8, "Social": 0.45, "People-Skill": 0.45, "Teaching-Ed": 0.3, "Rehab-Therapy": 0.25}
            },
            {
                "option_id": 2445,
                "option_text": "A sports and recreation program for at-risk youth",
                "trait_tags": {"Sports-Ed": 1.0, "Community-Serve": 0.8, "Physical-Skill": 0.45, "Social": 0.36, "Teaching-Ed": 0.35, "People-Skill": 0.32}
            },
            {
                "option_id": 2446,
                "option_text": "A cooperative business for local artisans and producers",
                "trait_tags": {"Startup-Venture": 1.0, "Community-Serve": 0.8, "Enterprising": 0.45, "Social": 0.36, "People-Skill": 0.32, "Marketing-Sales": 0.3}
            },
            {
                "option_id": 2447,
                "option_text": "A health and sanitation awareness campaign",
                "trait_tags": {"Public-Health": 1.0, "Community-Serve": 0.8, "Social": 0.4, "Analytical-Skill": 0.35, "People-Skill": 0.32, "Patient-Care": 0.25}
            },
            {
                "option_id": 2448,
                "option_text": "A disaster preparedness and rescue training program",
                "trait_tags": {"Community-Serve": 1.0, "Physical-Skill": 0.8, "Social": 0.45, "People-Skill": 0.4, "Realistic": 0.32, "Teaching-Ed": 0.25}
            }
        ]
    },
    {
        "question_id": 245,
        "question_text": "You're the HR manager of a growing company. What's your first priority?",
        "category": "Situational - HR Management",
        "options": [
            {
                "option_id": 2451,
                "option_text": "Designing a fair and competitive salary structure",
                "trait_tags": {"HR-Management": 1.0, "Finance-Acct": 0.8, "People-Skill": 0.4, "Conventional": 0.36, "Social": 0.35, "Enterprising": 0.35}
            },
            {
                "option_id": 2452,
                "option_text": "Creating employee training and development programs",
                "trait_tags": {"HR-Management": 1.0, "Teaching-Ed": 0.8, "People-Skill": 0.4, "Social": 0.36, "Enterprising": 0.35, "Admin-Skill": 0.35}
            },
            {
                "option_id": 2453,
                "option_text": "Building a positive and inclusive workplace culture",
                "trait_tags": {"HR-Management": 1.0, "People-Skill": 0.8, "Social": 0.36, "Enterprising": 0.35, "Admin-Skill": 0.35, "Teaching-Ed": 0.32}
            },
            {
                "option_id": 2454,
                "option_text": "Streamlining the recruitment and hiring process",
                "trait_tags": {"HR-Management": 1.0, "Admin-Skill": 0.8, "People-Skill": 0.4, "Conventional": 0.36, "Social": 0.35, "Enterprising": 0.35}
            },
            {
                "option_id": 2455,
                "option_text": "Setting up employee wellness and mental health programs",
                "trait_tags": {"HR-Management": 1.0, "Counseling": 0.8, "People-Skill": 0.4, "Social": 0.36, "Enterprising": 0.35, "Admin-Skill": 0.35}
            },
            {
                "option_id": 2456,
                "option_text": "Implementing HR management software systems",
                "trait_tags": {"HR-Management": 1.0, "Software-Dev": 0.8, "People-Skill": 0.4, "Technical-Skill": 0.36, "Social": 0.35, "Enterprising": 0.35}
            },
            {
                "option_id": 2457,
                "option_text": "Handling labor disputes and employee relations",
                "trait_tags": {"HR-Management": 1.0, "Legal-Practice": 0.8, "People-Skill": 0.4, "Social": 0.35, "Enterprising": 0.35, "Admin-Skill": 0.35}
            },
            {
                "option_id": 2458,
                "option_text": "Measuring employee performance with data analytics",
                "trait_tags": {"HR-Management": 1.0, "Data-Analytics": 0.8, "People-Skill": 0.4, "Investigative": 0.36, "Analytical-Skill": 0.36, "Social": 0.35}
            }
        ]
    },
    {
        "question_id": 246,
        "question_text": "What kind of business skill do you think is most valuable?",
        "category": "Interest - Business Skills",
        "options": [
            {
                "option_id": 2461,
                "option_text": "Financial analysis — understanding where money goes",
                "trait_tags": {"Finance-Acct": 1.0, "Analytical-Skill": 0.8, "Conventional": 0.45, "Investigative": 0.36, "Data-Analytics": 0.32, "Admin-Skill": 0.3}
            },
            {
                "option_id": 2462,
                "option_text": "People management — leading and motivating teams",
                "trait_tags": {"People-Skill": 1.0, "HR-Management": 0.8, "Social": 0.45, "Patient-Care": 0.4, "Teaching-Ed": 0.4, "Hospitality-Svc": 0.4}
            },
            {
                "option_id": 2463,
                "option_text": "Marketing strategy — knowing how to sell products",
                "trait_tags": {"Marketing-Sales": 1.0, "Analytical-Skill": 0.8, "Enterprising": 0.45, "People-Skill": 0.4, "Investigative": 0.36, "Data-Analytics": 0.32}
            },
            {
                "option_id": 2464,
                "option_text": "Negotiation — getting the best deals for your company",
                "trait_tags": {"People-Skill": 1.0, "Legal-Practice": 0.8, "Social": 0.45, "Patient-Care": 0.4, "Teaching-Ed": 0.4, "Hospitality-Svc": 0.4}
            },
            {
                "option_id": 2465,
                "option_text": "Project management — keeping teams and timelines on track",
                "trait_tags": {"Admin-Skill": 1.0, "Analytical-Skill": 0.8, "Conventional": 0.45, "Investigative": 0.36, "Data-Analytics": 0.32, "Finance-Acct": 0.3}
            },
            {
                "option_id": 2466,
                "option_text": "Entrepreneurship — starting and growing your own business",
                "trait_tags": {"Startup-Venture": 1.0, "People-Skill": 0.8, "Enterprising": 0.45, "Social": 0.36, "Teaching-Ed": 0.32, "Hospitality-Svc": 0.32}
            },
            {
                "option_id": 2467,
                "option_text": "Data-driven decisions — using numbers to guide choices",
                "trait_tags": {"Analytical-Skill": 1.0, "Data-Analytics": 0.8, "Investigative": 0.45, "Lab-Research": 0.35, "Finance-Acct": 0.35, "Medical-Lab": 0.3}
            },
            {
                "option_id": 2468,
                "option_text": "Public speaking — presenting ideas to stakeholders",
                "trait_tags": {"People-Skill": 1.0, "Teaching-Ed": 0.8, "Social": 0.45, "Patient-Care": 0.4, "Hospitality-Svc": 0.4, "Enterprising": 0.3}
            }
        ]
    },
    {
        "question_id": 247,
        "question_text": "A company asks you to create their brand identity. What do you focus on?",
        "category": "Situational - Digital Media Career",
        "options": [
            {
                "option_id": 2471,
                "option_text": "Designing their logo and visual brand guidelines",
                "trait_tags": {"Visual-Design": 1.0, "Creative-Skill": 0.8, "Artistic": 0.45, "Digital-Media": 0.32, "Spatial-Design": 0.28}
            },
            {
                "option_id": 2472,
                "option_text": "Creating promotional videos and motion graphics",
                "trait_tags": {"Film-Broadcast": 1.0, "Animation-3D": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Digital-Media": 0.4, "Game-Dev": 0.28}
            },
            {
                "option_id": 2473,
                "option_text": "Managing their social media presence and content",
                "trait_tags": {"Digital-Media": 1.0, "Marketing-Sales": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Enterprising": 0.36, "People-Skill": 0.32}
            },
            {
                "option_id": 2474,
                "option_text": "Building their website with interactive elements",
                "trait_tags": {"Web-Dev": 1.0, "Visual-Design": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Creative-Skill": 0.36, "Artistic": 0.36}
            },
            {
                "option_id": 2475,
                "option_text": "Writing compelling copy for ads and campaigns",
                "trait_tags": {"Digital-Media": 1.0, "Creative-Skill": 0.8, "Artistic": 0.4, "Visual-Design": 0.32, "Spatial-Design": 0.28, "Software-Dev": 0.2}
            },
            {
                "option_id": 2476,
                "option_text": "Photography and product shots for their catalog",
                "trait_tags": {"Visual-Design": 1.0, "Creative-Skill": 0.8, "Artistic": 0.45, "Digital-Media": 0.32, "Spatial-Design": 0.28}
            },
            {
                "option_id": 2477,
                "option_text": "Creating 3D product visualizations and renders",
                "trait_tags": {"Animation-3D": 1.0, "Visual-Design": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Digital-Media": 0.4, "Game-Dev": 0.35}
            },
            {
                "option_id": 2478,
                "option_text": "Developing a mobile app for their customers",
                "trait_tags": {"Mobile-Dev": 1.0, "Software-Dev": 0.8, "Technical-Skill": 0.45, "Investigative": 0.35, "Web-Dev": 0.3, "Data-Analytics": 0.24}
            }
        ]
    },
    {
        "question_id": 248,
        "question_text": "You're starting a creative career. What would you specialize in?",
        "category": "Interest - Creative Specialization",
        "options": [
            {
                "option_id": 2481,
                "option_text": "Graphic design — creating visuals for print and digital",
                "trait_tags": {"Visual-Design": 1.0, "Creative-Skill": 0.8, "Artistic": 0.45, "Digital-Media": 0.32, "Spatial-Design": 0.28}
            },
            {
                "option_id": 2482,
                "option_text": "3D modeling and animation for films or games",
                "trait_tags": {"Animation-3D": 1.0, "Game-Dev": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Digital-Media": 0.4, "Software-Dev": 0.32}
            },
            {
                "option_id": 2483,
                "option_text": "Video production and cinematography",
                "trait_tags": {"Film-Broadcast": 1.0, "Creative-Skill": 0.8, "Artistic": 0.4, "Digital-Media": 0.4, "Visual-Design": 0.32, "Spatial-Design": 0.28}
            },
            {
                "option_id": 2484,
                "option_text": "UI/UX design — making apps and websites user-friendly",
                "trait_tags": {"Visual-Design": 1.0, "Web-Dev": 0.8, "Artistic": 0.45, "Creative-Skill": 0.45, "Technical-Skill": 0.36, "Software-Dev": 0.36}
            },
            {
                "option_id": 2485,
                "option_text": "Photography — capturing moments and telling stories",
                "trait_tags": {"Creative-Skill": 1.0, "Visual-Design": 0.8, "Artistic": 0.45, "Digital-Media": 0.4, "Spatial-Design": 0.35}
            },
            {
                "option_id": 2486,
                "option_text": "Music production and sound design",
                "trait_tags": {"Performing-Arts": 1.0, "Creative-Skill": 0.8, "Artistic": 0.45, "Visual-Design": 0.32, "Digital-Media": 0.32, "People-Skill": 0.3}
            },
            {
                "option_id": 2487,
                "option_text": "Interior design and spatial planning",
                "trait_tags": {"Spatial-Design": 1.0, "Creative-Skill": 0.8, "Artistic": 0.36, "Visual-Design": 0.32, "Digital-Media": 0.32, "Civil-Build": 0.25}
            },
            {
                "option_id": 2488,
                "option_text": "Fashion design and clothing illustration",
                "trait_tags": {"Creative-Skill": 1.0, "Visual-Design": 0.8, "Artistic": 0.45, "Digital-Media": 0.4, "Spatial-Design": 0.35}
            }
        ]
    },
    {
        "question_id": 249,
        "question_text": "A Filipino movie studio needs help with their new animated film. What role do you want?",
        "category": "Situational - Animation Career",
        "options": [
            {
                "option_id": 2491,
                "option_text": "3D character modeler — sculpting characters digitally",
                "trait_tags": {"Animation-3D": 1.0, "Visual-Design": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Digital-Media": 0.4, "Game-Dev": 0.35}
            },
            {
                "option_id": 2492,
                "option_text": "Animator — bringing characters to life with movement",
                "trait_tags": {"Animation-3D": 1.0, "Creative-Skill": 0.8, "Artistic": 0.4, "Digital-Media": 0.4, "Game-Dev": 0.35, "Visual-Design": 0.32}
            },
            {
                "option_id": 2493,
                "option_text": "Visual effects artist — creating explosions and magic",
                "trait_tags": {"Animation-3D": 1.0, "Film-Broadcast": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Digital-Media": 0.4, "Game-Dev": 0.35}
            },
            {
                "option_id": 2494,
                "option_text": "Storyboard artist — planning each scene visually",
                "trait_tags": {"Animation-3D": 1.0, "Visual-Design": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Digital-Media": 0.4, "Game-Dev": 0.35}
            },
            {
                "option_id": 2495,
                "option_text": "Rigging specialist — building character skeletons for animation",
                "trait_tags": {"Animation-3D": 1.0, "Software-Dev": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Digital-Media": 0.4, "Technical-Skill": 0.36}
            },
            {
                "option_id": 2496,
                "option_text": "Background and environment artist — creating worlds",
                "trait_tags": {"Animation-3D": 1.0, "Spatial-Design": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Digital-Media": 0.4, "Game-Dev": 0.35}
            },
            {
                "option_id": 2497,
                "option_text": "Motion capture technician — recording actor movements",
                "trait_tags": {"Animation-3D": 1.0, "Hardware-Systems": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Digital-Media": 0.4, "Technical-Skill": 0.36}
            },
            {
                "option_id": 2498,
                "option_text": "Sound design — creating audio effects for the film",
                "trait_tags": {"Film-Broadcast": 1.0, "Performing-Arts": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Digital-Media": 0.4, "Visual-Design": 0.25}
            }
        ]
    },
    {
        "question_id": 250,
        "question_text": "What type of performance or performing arts excites you?",
        "category": "Interest - Performing Arts",
        "options": [
            {
                "option_id": 2501,
                "option_text": "Theater acting and stage performance",
                "trait_tags": {"Performing-Arts": 1.0, "Creative-Skill": 0.8, "Artistic": 0.45, "Visual-Design": 0.32, "Digital-Media": 0.32, "People-Skill": 0.3}
            },
            {
                "option_id": 2502,
                "option_text": "Dance choreography and performance",
                "trait_tags": {"Performing-Arts": 1.0, "Physical-Skill": 0.8, "Artistic": 0.45, "Creative-Skill": 0.45, "Realistic": 0.32, "People-Skill": 0.3}
            },
            {
                "option_id": 2503,
                "option_text": "Music composition and live performance",
                "trait_tags": {"Performing-Arts": 1.0, "Creative-Skill": 0.8, "Artistic": 0.45, "Visual-Design": 0.32, "Digital-Media": 0.32, "People-Skill": 0.3}
            },
            {
                "option_id": 2504,
                "option_text": "Film and TV acting — being in front of the camera",
                "trait_tags": {"Performing-Arts": 1.0, "Film-Broadcast": 0.8, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.32, "People-Skill": 0.3}
            },
            {
                "option_id": 2505,
                "option_text": "Voice acting and dubbing for animation",
                "trait_tags": {"Performing-Arts": 1.0, "Animation-3D": 0.8, "Artistic": 0.45, "Creative-Skill": 0.45, "Digital-Media": 0.32, "People-Skill": 0.3}
            },
            {
                "option_id": 2506,
                "option_text": "Stage direction and production management",
                "trait_tags": {"Performing-Arts": 1.0, "Admin-Skill": 0.8, "Artistic": 0.45, "Creative-Skill": 0.45, "Conventional": 0.36, "People-Skill": 0.3}
            },
            {
                "option_id": 2507,
                "option_text": "Musical theater — combining singing, acting, and dance",
                "trait_tags": {"Performing-Arts": 1.0, "Physical-Skill": 0.8, "Artistic": 0.45, "Creative-Skill": 0.45, "Realistic": 0.32, "People-Skill": 0.3}
            },
            {
                "option_id": 2508,
                "option_text": "Stand-up comedy and improv performance",
                "trait_tags": {"Performing-Arts": 1.0, "People-Skill": 0.8, "Artistic": 0.45, "Creative-Skill": 0.45, "Social": 0.36, "Teaching-Ed": 0.32}
            }
        ]
    },
    {
        "question_id": 251,
        "question_text": "You're designing a new building. What's most important to you?",
        "category": "Interest - Architecture Design",
        "options": [
            {
                "option_id": 2511,
                "option_text": "Making it earthquake-proof with strong structural design",
                "trait_tags": {"Spatial-Design": 1.0, "Civil-Build": 0.8, "Realistic": 0.36, "Artistic": 0.35, "Creative-Skill": 0.35, "Technical-Skill": 0.32}
            },
            {
                "option_id": 2512,
                "option_text": "Creating a beautiful and iconic exterior design",
                "trait_tags": {"Spatial-Design": 1.0, "Creative-Skill": 0.8, "Artistic": 0.36, "Visual-Design": 0.32, "Digital-Media": 0.32, "Civil-Build": 0.25}
            },
            {
                "option_id": 2513,
                "option_text": "Designing efficient interior layouts for people",
                "trait_tags": {"Spatial-Design": 1.0, "Visual-Design": 0.8, "Artistic": 0.36, "Creative-Skill": 0.36, "Civil-Build": 0.25, "Digital-Media": 0.24}
            },
            {
                "option_id": 2514,
                "option_text": "Using sustainable and eco-friendly materials",
                "trait_tags": {"Spatial-Design": 1.0, "Environmental-Eng": 0.8, "Artistic": 0.35, "Creative-Skill": 0.35, "Realistic": 0.32, "Technical-Skill": 0.28}
            },
            {
                "option_id": 2515,
                "option_text": "Integrating smart home technology throughout",
                "trait_tags": {"Spatial-Design": 1.0, "Hardware-Systems": 0.8, "Technical-Skill": 0.36, "Artistic": 0.35, "Creative-Skill": 0.35, "Realistic": 0.32}
            },
            {
                "option_id": 2516,
                "option_text": "Designing accessible spaces for persons with disabilities",
                "trait_tags": {"Spatial-Design": 1.0, "Community-Serve": 0.8, "Social": 0.36, "Artistic": 0.35, "Creative-Skill": 0.35, "People-Skill": 0.32}
            },
            {
                "option_id": 2517,
                "option_text": "Creating 3D models and virtual walkthroughs",
                "trait_tags": {"Spatial-Design": 1.0, "Animation-3D": 0.8, "Artistic": 0.35, "Creative-Skill": 0.35, "Digital-Media": 0.32, "Game-Dev": 0.28}
            },
            {
                "option_id": 2518,
                "option_text": "Urban planning — designing entire neighborhoods",
                "trait_tags": {"Spatial-Design": 1.0, "Civil-Build": 0.8, "Realistic": 0.36, "Artistic": 0.35, "Creative-Skill": 0.35, "Technical-Skill": 0.32}
            }
        ]
    },
    {
        "question_id": 252,
        "question_text": "A local farm needs help modernizing. What would you focus on?",
        "category": "Situational - Agriculture",
        "options": [
            {
                "option_id": 2521,
                "option_text": "Installing smart irrigation systems using sensors",
                "trait_tags": {"Agri-Nature": 1.0, "Hardware-Systems": 0.8, "Realistic": 0.45, "Technical-Skill": 0.36, "Physical-Skill": 0.35, "Field-Research": 0.25}
            },
            {
                "option_id": 2522,
                "option_text": "Soil testing and crop rotation planning",
                "trait_tags": {"Agri-Nature": 1.0, "Field-Research": 0.8, "Realistic": 0.45, "Physical-Skill": 0.35, "Investigative": 0.32, "Analytical-Skill": 0.24}
            },
            {
                "option_id": 2523,
                "option_text": "Organic farming techniques and natural pest control",
                "trait_tags": {"Agri-Nature": 1.0, "Environmental-Sci": 0.8, "Realistic": 0.45, "Investigative": 0.36, "Physical-Skill": 0.35, "Field-Research": 0.32}
            },
            {
                "option_id": 2524,
                "option_text": "Setting up a farm-to-table business model",
                "trait_tags": {"Agri-Nature": 1.0, "Startup-Venture": 0.8, "Realistic": 0.45, "Enterprising": 0.36, "Physical-Skill": 0.35, "Field-Research": 0.25}
            },
            {
                "option_id": 2525,
                "option_text": "Aquaculture and fish farming in ponds",
                "trait_tags": {"Agri-Nature": 1.0, "Maritime-Sea": 0.8, "Realistic": 0.45, "Physical-Skill": 0.35, "Field-Research": 0.25, "Technical-Skill": 0.2}
            },
            {
                "option_id": 2526,
                "option_text": "Developing a farm management app for tracking crops",
                "trait_tags": {"Mobile-Dev": 1.0, "Agri-Nature": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Realistic": 0.36, "Investigative": 0.35}
            },
            {
                "option_id": 2527,
                "option_text": "Processing and packaging farm products for sale",
                "trait_tags": {"Food-Science": 1.0, "Agri-Nature": 0.8, "Investigative": 0.4, "Realistic": 0.36, "Lab-Research": 0.35, "Nutrition-Diet": 0.35}
            },
            {
                "option_id": 2528,
                "option_text": "Training farmers on modern agricultural techniques",
                "trait_tags": {"Agri-Nature": 1.0, "Teaching-Ed": 0.8, "Realistic": 0.45, "Social": 0.36, "People-Skill": 0.36, "Physical-Skill": 0.35}
            }
        ]
    },
    {
        "question_id": 253,
        "question_text": "What environmental issue would you most want to solve in the Philippines?",
        "category": "Interest - Environmental Science",
        "options": [
            {
                "option_id": 2531,
                "option_text": "Coral reef and marine ecosystem restoration",
                "trait_tags": {"Environmental-Sci": 1.0, "Maritime-Sea": 0.8, "Investigative": 0.45, "Field-Research": 0.4, "Realistic": 0.36, "Physical-Skill": 0.32}
            },
            {
                "option_id": 2532,
                "option_text": "Deforestation and reforestation programs",
                "trait_tags": {"Environmental-Sci": 1.0, "Agri-Nature": 0.8, "Investigative": 0.45, "Field-Research": 0.4, "Realistic": 0.36, "Environmental-Eng": 0.3}
            },
            {
                "option_id": 2533,
                "option_text": "Air and water pollution monitoring in cities",
                "trait_tags": {"Environmental-Sci": 1.0, "Environmental-Eng": 0.8, "Investigative": 0.45, "Field-Research": 0.4, "Realistic": 0.32, "Technical-Skill": 0.28}
            },
            {
                "option_id": 2534,
                "option_text": "Wildlife conservation and protected area management",
                "trait_tags": {"Environmental-Sci": 1.0, "Field-Research": 0.8, "Investigative": 0.45, "Environmental-Eng": 0.3, "Lab-Research": 0.25, "Agri-Nature": 0.25}
            },
            {
                "option_id": 2535,
                "option_text": "Climate change research and disaster preparedness",
                "trait_tags": {"Environmental-Sci": 1.0, "Data-Analytics": 0.8, "Investigative": 0.45, "Field-Research": 0.4, "Analytical-Skill": 0.36, "Environmental-Eng": 0.3}
            },
            {
                "option_id": 2536,
                "option_text": "Solid waste management and recycling programs",
                "trait_tags": {"Environmental-Sci": 1.0, "Community-Serve": 0.8, "Investigative": 0.45, "Field-Research": 0.4, "Social": 0.36, "People-Skill": 0.32}
            },
            {
                "option_id": 2537,
                "option_text": "Renewable energy development for rural areas",
                "trait_tags": {"Environmental-Sci": 1.0, "Electrical-Power": 0.8, "Investigative": 0.45, "Field-Research": 0.4, "Technical-Skill": 0.36, "Realistic": 0.32}
            },
            {
                "option_id": 2538,
                "option_text": "Environmental impact assessment for new projects",
                "trait_tags": {"Environmental-Sci": 1.0, "Legal-Practice": 0.8, "Investigative": 0.45, "Field-Research": 0.4, "Environmental-Eng": 0.3, "Enterprising": 0.28}
            }
        ]
    },
    {
        "question_id": 254,
        "question_text": "You're doing field research in a national park. What would you study?",
        "category": "Interest - Field Research",
        "options": [
            {
                "option_id": 2541,
                "option_text": "Cataloging and studying endemic plant species",
                "trait_tags": {"Field-Research": 1.0, "Environmental-Sci": 0.8, "Investigative": 0.4, "Agri-Nature": 0.3, "Analytical-Skill": 0.3, "Physical-Skill": 0.25}
            },
            {
                "option_id": 2542,
                "option_text": "Tracking and observing wildlife behavior",
                "trait_tags": {"Field-Research": 1.0, "Agri-Nature": 0.8, "Investigative": 0.4, "Realistic": 0.36, "Analytical-Skill": 0.3, "Physical-Skill": 0.28}
            },
            {
                "option_id": 2543,
                "option_text": "Testing soil and water quality samples",
                "trait_tags": {"Field-Research": 1.0, "Lab-Research": 0.8, "Investigative": 0.4, "Analytical-Skill": 0.36, "Agri-Nature": 0.3, "Physical-Skill": 0.25}
            },
            {
                "option_id": 2544,
                "option_text": "Mapping terrain using GPS and drone technology",
                "trait_tags": {"Field-Research": 1.0, "Hardware-Systems": 0.8, "Investigative": 0.4, "Technical-Skill": 0.36, "Realistic": 0.32, "Agri-Nature": 0.3}
            },
            {
                "option_id": 2545,
                "option_text": "Studying weather patterns and climate data",
                "trait_tags": {"Field-Research": 1.0, "Data-Analytics": 0.8, "Investigative": 0.4, "Analytical-Skill": 0.36, "Agri-Nature": 0.3, "Physical-Skill": 0.25}
            },
            {
                "option_id": 2546,
                "option_text": "Documenting indigenous communities and their practices",
                "trait_tags": {"Field-Research": 1.0, "Community-Serve": 0.8, "Investigative": 0.4, "Social": 0.36, "People-Skill": 0.32, "Agri-Nature": 0.3}
            },
            {
                "option_id": 2547,
                "option_text": "Collecting mineral and geological samples",
                "trait_tags": {"Field-Research": 1.0, "Civil-Build": 0.8, "Investigative": 0.4, "Realistic": 0.36, "Technical-Skill": 0.32, "Agri-Nature": 0.3}
            },
            {
                "option_id": 2548,
                "option_text": "Marine biology research in coastal areas",
                "trait_tags": {"Field-Research": 1.0, "Maritime-Sea": 0.8, "Investigative": 0.4, "Realistic": 0.36, "Physical-Skill": 0.32, "Agri-Nature": 0.3}
            }
        ]
    },
    {
        "question_id": 255,
        "question_text": "A company's website has been hacked. What would you do first?",
        "category": "Situational - Cybersecurity Response",
        "options": [
            {
                "option_id": 2551,
                "option_text": "Analyze server logs to find how the attacker got in",
                "trait_tags": {"Cyber-Defense": 1.0, "Analytical-Skill": 0.8, "Technical-Skill": 0.4, "Investigative": 0.36, "Data-Analytics": 0.32, "Lab-Research": 0.28}
            },
            {
                "option_id": 2552,
                "option_text": "Isolate compromised systems to prevent further damage",
                "trait_tags": {"Cyber-Defense": 1.0, "Cloud-Systems": 0.8, "Technical-Skill": 0.4, "Investigative": 0.35, "Software-Dev": 0.28, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 2553,
                "option_text": "Run malware analysis on suspicious files found",
                "trait_tags": {"Cyber-Defense": 1.0, "Forensic-Sci": 0.8, "Technical-Skill": 0.4, "Investigative": 0.36, "Analytical-Skill": 0.32, "Law-Enforce": 0.28}
            },
            {
                "option_id": 2554,
                "option_text": "Check if customer data was stolen and notify them",
                "trait_tags": {"Cyber-Defense": 1.0, "Legal-Practice": 0.8, "Technical-Skill": 0.4, "Investigative": 0.35, "Enterprising": 0.28, "Analytical-Skill": 0.28}
            },
            {
                "option_id": 2555,
                "option_text": "Patch the vulnerability and strengthen the firewall",
                "trait_tags": {"Cyber-Defense": 1.0, "Software-Dev": 0.8, "Technical-Skill": 0.4, "Investigative": 0.35, "Data-Analytics": 0.24, "Hardware-Systems": 0.16}
            },
            {
                "option_id": 2556,
                "option_text": "Set up an intrusion detection system to prevent future attacks",
                "trait_tags": {"Cyber-Defense": 1.0, "Hardware-Systems": 0.8, "Technical-Skill": 0.4, "Investigative": 0.35, "Realistic": 0.32, "Software-Dev": 0.25}
            },
            {
                "option_id": 2557,
                "option_text": "Train employees on security awareness",
                "trait_tags": {"Cyber-Defense": 1.0, "Teaching-Ed": 0.8, "Technical-Skill": 0.4, "Social": 0.36, "People-Skill": 0.36, "Investigative": 0.35}
            },
            {
                "option_id": 2558,
                "option_text": "Document the incident and create a response report",
                "trait_tags": {"Cyber-Defense": 1.0, "Admin-Skill": 0.8, "Technical-Skill": 0.4, "Conventional": 0.36, "Investigative": 0.35, "Software-Dev": 0.25}
            }
        ]
    },
    {
        "question_id": 256,
        "question_text": "You're building a cloud infrastructure for a startup. What's your priority?",
        "category": "Situational - Cloud Engineering",
        "options": [
            {
                "option_id": 2561,
                "option_text": "Setting up auto-scaling servers to handle traffic spikes",
                "trait_tags": {"Cloud-Systems": 1.0, "Software-Dev": 0.8, "Technical-Skill": 0.45, "Investigative": 0.32, "Cyber-Defense": 0.3, "Hardware-Systems": 0.25}
            },
            {
                "option_id": 2562,
                "option_text": "Implementing secure authentication and encryption",
                "trait_tags": {"Cloud-Systems": 1.0, "Cyber-Defense": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.35, "Investigative": 0.3, "Hardware-Systems": 0.25}
            },
            {
                "option_id": 2563,
                "option_text": "Creating CI/CD pipelines for automated deployment",
                "trait_tags": {"Cloud-Systems": 1.0, "Software-Dev": 0.8, "Technical-Skill": 0.45, "Investigative": 0.32, "Cyber-Defense": 0.3, "Hardware-Systems": 0.25}
            },
            {
                "option_id": 2564,
                "option_text": "Monitoring system performance with dashboards",
                "trait_tags": {"Cloud-Systems": 1.0, "Data-Analytics": 0.8, "Technical-Skill": 0.45, "Investigative": 0.36, "Analytical-Skill": 0.36, "Software-Dev": 0.35}
            },
            {
                "option_id": 2565,
                "option_text": "Setting up database backups and disaster recovery",
                "trait_tags": {"Cloud-Systems": 1.0, "Admin-Skill": 0.8, "Technical-Skill": 0.45, "Conventional": 0.36, "Software-Dev": 0.35, "Investigative": 0.3}
            },
            {
                "option_id": 2566,
                "option_text": "Container orchestration with Docker and Kubernetes",
                "trait_tags": {"Cloud-Systems": 1.0, "Software-Dev": 0.8, "Technical-Skill": 0.45, "Investigative": 0.32, "Cyber-Defense": 0.3, "Hardware-Systems": 0.25}
            },
            {
                "option_id": 2567,
                "option_text": "Cost optimization — choosing the right cloud services",
                "trait_tags": {"Cloud-Systems": 1.0, "Finance-Acct": 0.8, "Technical-Skill": 0.45, "Conventional": 0.36, "Software-Dev": 0.35, "Analytical-Skill": 0.32}
            },
            {
                "option_id": 2568,
                "option_text": "API gateway and microservices architecture",
                "trait_tags": {"Cloud-Systems": 1.0, "Web-Dev": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.36, "Investigative": 0.3, "Cyber-Defense": 0.3}
            }
        ]
    },
    {
        "question_id": 257,
        "question_text": "You're building an AI project for a thesis. What would you create?",
        "category": "Situational - AI Development",
        "options": [
            {
                "option_id": 2571,
                "option_text": "A chatbot that helps students with enrollment questions",
                "trait_tags": {"AI-ML": 1.0, "Software-Dev": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Data-Analytics": 0.4, "Technical-Skill": 0.36}
            },
            {
                "option_id": 2572,
                "option_text": "An image recognition system for plant disease detection",
                "trait_tags": {"AI-ML": 1.0, "Agri-Nature": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Data-Analytics": 0.4, "Realistic": 0.36}
            },
            {
                "option_id": 2573,
                "option_text": "A recommendation engine for course selection",
                "trait_tags": {"AI-ML": 1.0, "Data-Analytics": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Software-Dev": 0.35, "Lab-Research": 0.2}
            },
            {
                "option_id": 2574,
                "option_text": "A sentiment analysis tool for Filipino social media posts",
                "trait_tags": {"AI-ML": 1.0, "Data-Analytics": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Software-Dev": 0.35, "Lab-Research": 0.2}
            },
            {
                "option_id": 2575,
                "option_text": "A predictive model for natural disaster risk",
                "trait_tags": {"AI-ML": 1.0, "Environmental-Sci": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Data-Analytics": 0.4, "Software-Dev": 0.35}
            },
            {
                "option_id": 2576,
                "option_text": "A voice assistant that understands Filipino languages",
                "trait_tags": {"AI-ML": 1.0, "Software-Dev": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Data-Analytics": 0.4, "Technical-Skill": 0.36}
            },
            {
                "option_id": 2577,
                "option_text": "A fraud detection system for online banking",
                "trait_tags": {"AI-ML": 1.0, "Cyber-Defense": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Data-Analytics": 0.4, "Software-Dev": 0.35}
            },
            {
                "option_id": 2578,
                "option_text": "A computer vision system for traffic monitoring",
                "trait_tags": {"AI-ML": 1.0, "Hardware-Systems": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Data-Analytics": 0.4, "Technical-Skill": 0.36}
            }
        ]
    },
    {
        "question_id": 258,
        "question_text": "You have a large dataset about Filipino consumers. What would you analyze?",
        "category": "Situational - Data Analytics",
        "options": [
            {
                "option_id": 2581,
                "option_text": "Shopping patterns to help businesses target customers",
                "trait_tags": {"Data-Analytics": 1.0, "Marketing-Sales": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Enterprising": 0.36, "People-Skill": 0.32}
            },
            {
                "option_id": 2582,
                "option_text": "Health trends to predict disease outbreaks",
                "trait_tags": {"Data-Analytics": 1.0, "Public-Health": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Social": 0.32, "Software-Dev": 0.3}
            },
            {
                "option_id": 2583,
                "option_text": "Social media behavior to understand public opinion",
                "trait_tags": {"Data-Analytics": 1.0, "Digital-Media": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Artistic": 0.32, "Creative-Skill": 0.32}
            },
            {
                "option_id": 2584,
                "option_text": "Financial data to detect fraud and money laundering",
                "trait_tags": {"Data-Analytics": 1.0, "Finance-Acct": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Conventional": 0.36, "Software-Dev": 0.3}
            },
            {
                "option_id": 2585,
                "option_text": "Educational performance to improve school programs",
                "trait_tags": {"Data-Analytics": 1.0, "Teaching-Ed": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Social": 0.36, "People-Skill": 0.36}
            },
            {
                "option_id": 2586,
                "option_text": "Transportation data to optimize public transit routes",
                "trait_tags": {"Data-Analytics": 1.0, "Civil-Build": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Realistic": 0.36, "Technical-Skill": 0.32}
            },
            {
                "option_id": 2587,
                "option_text": "Environmental sensor data to track pollution levels",
                "trait_tags": {"Data-Analytics": 1.0, "Environmental-Sci": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Field-Research": 0.32, "Software-Dev": 0.3}
            },
            {
                "option_id": 2588,
                "option_text": "Game player statistics to balance game difficulty",
                "trait_tags": {"Data-Analytics": 1.0, "Game-Dev": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Software-Dev": 0.32, "Technical-Skill": 0.32}
            }
        ]
    },
    {
        "question_id": 259,
        "question_text": "You're working in a food laboratory. What project interests you most?",
        "category": "Interest - Food Science",
        "options": [
            {
                "option_id": 2591,
                "option_text": "Developing new food preservation techniques",
                "trait_tags": {"Food-Science": 1.0, "Lab-Research": 0.8, "Investigative": 0.4, "Analytical-Skill": 0.36, "Nutrition-Diet": 0.35, "Medical-Lab": 0.24}
            },
            {
                "option_id": 2592,
                "option_text": "Testing food products for safety and nutrition content",
                "trait_tags": {"Food-Science": 1.0, "Medical-Lab": 0.8, "Investigative": 0.4, "Analytical-Skill": 0.36, "Lab-Research": 0.35, "Nutrition-Diet": 0.35}
            },
            {
                "option_id": 2593,
                "option_text": "Creating plant-based meat alternatives",
                "trait_tags": {"Food-Science": 1.0, "Agri-Nature": 0.8, "Investigative": 0.4, "Realistic": 0.36, "Lab-Research": 0.35, "Nutrition-Diet": 0.35}
            },
            {
                "option_id": 2594,
                "option_text": "Improving the flavor and texture of packaged snacks",
                "trait_tags": {"Food-Science": 1.0, "Culinary-Arts": 0.8, "Investigative": 0.4, "Lab-Research": 0.35, "Nutrition-Diet": 0.35, "Analytical-Skill": 0.3}
            },
            {
                "option_id": 2595,
                "option_text": "Designing healthy school lunch menus",
                "trait_tags": {"Nutrition-Diet": 1.0, "Food-Science": 0.8, "Investigative": 0.32, "Social": 0.3, "Analytical-Skill": 0.3, "Lab-Research": 0.28}
            },
            {
                "option_id": 2596,
                "option_text": "Quality control for a beverage manufacturing plant",
                "trait_tags": {"Food-Science": 1.0, "Industrial-Ops": 0.8, "Investigative": 0.4, "Lab-Research": 0.35, "Nutrition-Diet": 0.35, "Analytical-Skill": 0.3}
            },
            {
                "option_id": 2597,
                "option_text": "Researching traditional Filipino fermented foods",
                "trait_tags": {"Food-Science": 1.0, "Field-Research": 0.8, "Investigative": 0.4, "Lab-Research": 0.35, "Nutrition-Diet": 0.35, "Analytical-Skill": 0.3}
            },
            {
                "option_id": 2598,
                "option_text": "Developing sustainable food packaging solutions",
                "trait_tags": {"Food-Science": 1.0, "Environmental-Eng": 0.8, "Investigative": 0.4, "Lab-Research": 0.35, "Nutrition-Diet": 0.35, "Realistic": 0.32}
            }
        ]
    },
    {
        "question_id": 260,
        "question_text": "You're playing a video game and you notice a bug. What would you want to do about it?",
        "category": "Interest - Game Dev Problem Solving",
        "options": [
            {
                "option_id": 2601,
                "option_text": "Debug the code and fix the game logic error",
                "trait_tags": {"Game-Dev": 1.0, "Software-Dev": 0.8, "Technical-Skill": 0.4, "Creative-Skill": 0.35, "Animation-3D": 0.35, "Investigative": 0.32}
            },
            {
                "option_id": 2602,
                "option_text": "Report it to the developer with detailed reproduction steps",
                "trait_tags": {"Game-Dev": 1.0, "Analytical-Skill": 0.8, "Technical-Skill": 0.4, "Software-Dev": 0.4, "Investigative": 0.36, "Creative-Skill": 0.35}
            },
            {
                "option_id": 2603,
                "option_text": "Make a YouTube video showing the bug and how to exploit it",
                "trait_tags": {"Digital-Media": 1.0, "Game-Dev": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Software-Dev": 0.32, "Technical-Skill": 0.32}
            },
            {
                "option_id": 2604,
                "option_text": "Redesign the game mechanic so the bug can't happen",
                "trait_tags": {"Game-Dev": 1.0, "Software-Dev": 0.8, "Technical-Skill": 0.4, "Creative-Skill": 0.35, "Animation-3D": 0.35, "Investigative": 0.32}
            },
            {
                "option_id": 2605,
                "option_text": "Check if it's a graphics rendering issue and fix the shader",
                "trait_tags": {"Game-Dev": 1.0, "Animation-3D": 0.8, "Technical-Skill": 0.4, "Software-Dev": 0.4, "Creative-Skill": 0.35, "Artistic": 0.32}
            },
            {
                "option_id": 2606,
                "option_text": "Test other parts of the game to find more bugs",
                "trait_tags": {"Game-Dev": 1.0, "Analytical-Skill": 0.8, "Technical-Skill": 0.4, "Software-Dev": 0.4, "Investigative": 0.36, "Creative-Skill": 0.35}
            },
            {
                "option_id": 2607,
                "option_text": "Check the server connection — might be a network issue",
                "trait_tags": {"Cloud-Systems": 1.0, "Game-Dev": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.35, "Investigative": 0.3, "Cyber-Defense": 0.3}
            },
            {
                "option_id": 2608,
                "option_text": "Mod the game to add a workaround for the bug",
                "trait_tags": {"Game-Dev": 1.0, "Software-Dev": 0.8, "Technical-Skill": 0.4, "Creative-Skill": 0.35, "Animation-3D": 0.35, "Investigative": 0.32}
            }
        ]
    },
    {
        "question_id": 261,
        "question_text": "You're creating a multiplayer game. What feature do you build first?",
        "category": "Interest - Game Dev Multiplayer",
        "options": [
            {
                "option_id": 2611,
                "option_text": "Real-time multiplayer networking and matchmaking",
                "trait_tags": {"Game-Dev": 1.0, "Cloud-Systems": 0.8, "Technical-Skill": 0.4, "Software-Dev": 0.4, "Creative-Skill": 0.35, "Animation-3D": 0.35}
            },
            {
                "option_id": 2612,
                "option_text": "Character customization with unique skins and outfits",
                "trait_tags": {"Game-Dev": 1.0, "Visual-Design": 0.8, "Technical-Skill": 0.4, "Software-Dev": 0.4, "Artistic": 0.36, "Creative-Skill": 0.36}
            },
            {
                "option_id": 2613,
                "option_text": "A ranking and leaderboard system for competitive play",
                "trait_tags": {"Game-Dev": 1.0, "Data-Analytics": 0.8, "Technical-Skill": 0.4, "Software-Dev": 0.4, "Investigative": 0.36, "Analytical-Skill": 0.36}
            },
            {
                "option_id": 2614,
                "option_text": "Anti-cheat system to keep the game fair",
                "trait_tags": {"Game-Dev": 1.0, "Cyber-Defense": 0.8, "Technical-Skill": 0.4, "Software-Dev": 0.4, "Creative-Skill": 0.35, "Animation-3D": 0.35}
            },
            {
                "option_id": 2615,
                "option_text": "Voice chat and team communication features",
                "trait_tags": {"Game-Dev": 1.0, "Software-Dev": 0.8, "Technical-Skill": 0.4, "Creative-Skill": 0.35, "Animation-3D": 0.35, "Investigative": 0.32}
            },
            {
                "option_id": 2616,
                "option_text": "In-game economy with virtual currency and shops",
                "trait_tags": {"Game-Dev": 1.0, "Finance-Acct": 0.8, "Technical-Skill": 0.4, "Software-Dev": 0.4, "Conventional": 0.36, "Creative-Skill": 0.35}
            },
            {
                "option_id": 2617,
                "option_text": "Level design with multiple maps and environments",
                "trait_tags": {"Game-Dev": 1.0, "Spatial-Design": 0.8, "Technical-Skill": 0.4, "Software-Dev": 0.4, "Creative-Skill": 0.35, "Animation-3D": 0.35}
            },
            {
                "option_id": 2618,
                "option_text": "A seasonal battle pass with rewards and challenges",
                "trait_tags": {"Game-Dev": 1.0, "Marketing-Sales": 0.8, "Technical-Skill": 0.4, "Software-Dev": 0.4, "Enterprising": 0.36, "Creative-Skill": 0.35}
            }
        ]
    },
    {
        "question_id": 262,
        "question_text": "What type of game would you love to make as your dream project?",
        "category": "Interest - Game Dev Dream Project",
        "options": [
            {
                "option_id": 2621,
                "option_text": "An open-world RPG set in Philippine mythology",
                "trait_tags": {"Game-Dev": 1.0, "Creative-Skill": 0.8, "Technical-Skill": 0.4, "Software-Dev": 0.4, "Artistic": 0.36, "Animation-3D": 0.35}
            },
            {
                "option_id": 2622,
                "option_text": "A competitive esports game like Valorant or DOTA",
                "trait_tags": {"Game-Dev": 1.0, "Software-Dev": 0.8, "Technical-Skill": 0.4, "Creative-Skill": 0.35, "Animation-3D": 0.35, "Investigative": 0.32}
            },
            {
                "option_id": 2623,
                "option_text": "A mobile puzzle game anyone can enjoy",
                "trait_tags": {"Game-Dev": 1.0, "Mobile-Dev": 0.8, "Technical-Skill": 0.4, "Software-Dev": 0.4, "Creative-Skill": 0.35, "Animation-3D": 0.35}
            },
            {
                "option_id": 2624,
                "option_text": "A VR horror experience with immersive environments",
                "trait_tags": {"Game-Dev": 1.0, "Animation-3D": 0.8, "Technical-Skill": 0.4, "Software-Dev": 0.4, "Creative-Skill": 0.35, "Artistic": 0.32}
            },
            {
                "option_id": 2625,
                "option_text": "An educational game that teaches Filipino history",
                "trait_tags": {"Game-Dev": 1.0, "Teaching-Ed": 0.8, "Technical-Skill": 0.4, "Software-Dev": 0.4, "Social": 0.36, "People-Skill": 0.36}
            },
            {
                "option_id": 2626,
                "option_text": "A simulation game like city-building or farming",
                "trait_tags": {"Game-Dev": 1.0, "Data-Analytics": 0.8, "Technical-Skill": 0.4, "Software-Dev": 0.4, "Investigative": 0.36, "Analytical-Skill": 0.36}
            },
            {
                "option_id": 2627,
                "option_text": "A rhythm and music game with original Filipino music",
                "trait_tags": {"Game-Dev": 1.0, "Performing-Arts": 0.8, "Technical-Skill": 0.4, "Software-Dev": 0.4, "Artistic": 0.36, "Creative-Skill": 0.36}
            },
            {
                "option_id": 2628,
                "option_text": "A retro-style pixel art platformer game",
                "trait_tags": {"Game-Dev": 1.0, "Visual-Design": 0.8, "Technical-Skill": 0.4, "Software-Dev": 0.4, "Artistic": 0.36, "Creative-Skill": 0.36}
            }
        ]
    },
    {
        "question_id": 263,
        "question_text": "A client needs a website. What kind of site would you enjoy building most?",
        "category": "Interest - Web Development",
        "options": [
            {
                "option_id": 2631,
                "option_text": "An e-commerce store with shopping cart and payments",
                "trait_tags": {"Web-Dev": 1.0, "Software-Dev": 0.8, "Technical-Skill": 0.45, "Investigative": 0.35, "Mobile-Dev": 0.3, "Digital-Media": 0.25}
            },
            {
                "option_id": 2632,
                "option_text": "A portfolio website with stunning visual design",
                "trait_tags": {"Web-Dev": 1.0, "Visual-Design": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Creative-Skill": 0.36, "Artistic": 0.36}
            },
            {
                "option_id": 2633,
                "option_text": "A social media platform for local communities",
                "trait_tags": {"Web-Dev": 1.0, "Software-Dev": 0.8, "Technical-Skill": 0.45, "Investigative": 0.35, "Mobile-Dev": 0.3, "Digital-Media": 0.25}
            },
            {
                "option_id": 2634,
                "option_text": "A learning management system for schools",
                "trait_tags": {"Web-Dev": 1.0, "Teaching-Ed": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Social": 0.36, "People-Skill": 0.36}
            },
            {
                "option_id": 2635,
                "option_text": "A dashboard for data visualization and analytics",
                "trait_tags": {"Web-Dev": 1.0, "Data-Analytics": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Investigative": 0.36, "Analytical-Skill": 0.36}
            },
            {
                "option_id": 2636,
                "option_text": "A booking system for hotels and restaurants",
                "trait_tags": {"Web-Dev": 1.0, "Hospitality-Svc": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "People-Skill": 0.36, "Investigative": 0.35}
            },
            {
                "option_id": 2637,
                "option_text": "A news and blog platform with content management",
                "trait_tags": {"Web-Dev": 1.0, "Digital-Media": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Investigative": 0.35, "Creative-Skill": 0.32}
            },
            {
                "option_id": 2638,
                "option_text": "A real-time multiplayer game in the browser",
                "trait_tags": {"Web-Dev": 1.0, "Game-Dev": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Investigative": 0.35, "Mobile-Dev": 0.3}
            }
        ]
    },
    {
        "question_id": 264,
        "question_text": "What part of web development excites you the most?",
        "category": "Interest - Web Dev Specialization",
        "options": [
            {
                "option_id": 2641,
                "option_text": "Frontend design — making pages look beautiful and responsive",
                "trait_tags": {"Web-Dev": 1.0, "Visual-Design": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Creative-Skill": 0.36, "Artistic": 0.36}
            },
            {
                "option_id": 2642,
                "option_text": "Backend logic — building APIs and server-side systems",
                "trait_tags": {"Web-Dev": 1.0, "Software-Dev": 0.8, "Technical-Skill": 0.45, "Investigative": 0.35, "Mobile-Dev": 0.3, "Digital-Media": 0.25}
            },
            {
                "option_id": 2643,
                "option_text": "Database design — organizing and managing data efficiently",
                "trait_tags": {"Web-Dev": 1.0, "Data-Analytics": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Investigative": 0.36, "Analytical-Skill": 0.36}
            },
            {
                "option_id": 2644,
                "option_text": "DevOps — deploying and managing servers in the cloud",
                "trait_tags": {"Cloud-Systems": 1.0, "Web-Dev": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.36, "Investigative": 0.3, "Cyber-Defense": 0.3}
            },
            {
                "option_id": 2645,
                "option_text": "Security — protecting websites from hackers",
                "trait_tags": {"Cyber-Defense": 1.0, "Web-Dev": 0.8, "Technical-Skill": 0.4, "Software-Dev": 0.36, "Investigative": 0.35, "Mobile-Dev": 0.24}
            },
            {
                "option_id": 2646,
                "option_text": "Accessibility — making websites usable for everyone",
                "trait_tags": {"Web-Dev": 1.0, "Community-Serve": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Social": 0.36, "Investigative": 0.35}
            },
            {
                "option_id": 2647,
                "option_text": "Performance optimization — making sites load blazing fast",
                "trait_tags": {"Web-Dev": 1.0, "Analytical-Skill": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Investigative": 0.36, "Data-Analytics": 0.32}
            },
            {
                "option_id": 2648,
                "option_text": "Full-stack development — building everything end to end",
                "trait_tags": {"Web-Dev": 1.0, "Software-Dev": 0.8, "Technical-Skill": 0.45, "Investigative": 0.35, "Mobile-Dev": 0.3, "Digital-Media": 0.25}
            }
        ]
    },
    {
        "question_id": 265,
        "question_text": "You're building a mobile app for Filipinos. What would it do?",
        "category": "Interest - Mobile App Ideas",
        "options": [
            {
                "option_id": 2651,
                "option_text": "A ride-sharing app like Grab for local tricycles",
                "trait_tags": {"Mobile-Dev": 1.0, "Software-Dev": 0.8, "Technical-Skill": 0.45, "Investigative": 0.35, "Web-Dev": 0.3, "Data-Analytics": 0.24}
            },
            {
                "option_id": 2652,
                "option_text": "A health tracker app with diet and exercise logs",
                "trait_tags": {"Mobile-Dev": 1.0, "Nutrition-Diet": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Investigative": 0.35, "Web-Dev": 0.3}
            },
            {
                "option_id": 2653,
                "option_text": "A local marketplace for buying and selling goods",
                "trait_tags": {"Mobile-Dev": 1.0, "Marketing-Sales": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Enterprising": 0.36, "Investigative": 0.35}
            },
            {
                "option_id": 2654,
                "option_text": "An emergency alert app for typhoons and disasters",
                "trait_tags": {"Mobile-Dev": 1.0, "Public-Health": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Investigative": 0.35, "Social": 0.32}
            },
            {
                "option_id": 2655,
                "option_text": "A budgeting and savings app for students",
                "trait_tags": {"Mobile-Dev": 1.0, "Finance-Acct": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Conventional": 0.36, "Investigative": 0.35}
            },
            {
                "option_id": 2656,
                "option_text": "A Filipino language learning app for foreigners",
                "trait_tags": {"Mobile-Dev": 1.0, "Teaching-Ed": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Social": 0.36, "People-Skill": 0.36}
            },
            {
                "option_id": 2657,
                "option_text": "A mobile game with Filipino culture themes",
                "trait_tags": {"Mobile-Dev": 1.0, "Game-Dev": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Investigative": 0.35, "Web-Dev": 0.3}
            },
            {
                "option_id": 2658,
                "option_text": "A barangay services and reporting app",
                "trait_tags": {"Mobile-Dev": 1.0, "Community-Serve": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Social": 0.36, "Investigative": 0.35}
            }
        ]
    },
    {
        "question_id": 266,
        "question_text": "What kind of programmer do you want to become?",
        "category": "Interest - Software Dev Path",
        "options": [
            {
                "option_id": 2661,
                "option_text": "A game developer making AAA or indie games",
                "trait_tags": {"Software-Dev": 1.0, "Game-Dev": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Creative-Skill": 0.28}
            },
            {
                "option_id": 2662,
                "option_text": "A web developer building modern websites and apps",
                "trait_tags": {"Software-Dev": 1.0, "Web-Dev": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25}
            },
            {
                "option_id": 2663,
                "option_text": "A mobile app developer for iOS and Android",
                "trait_tags": {"Software-Dev": 1.0, "Mobile-Dev": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25}
            },
            {
                "option_id": 2664,
                "option_text": "An AI/ML engineer building intelligent systems",
                "trait_tags": {"Software-Dev": 1.0, "AI-ML": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Analytical-Skill": 0.36, "Data-Analytics": 0.32}
            },
            {
                "option_id": 2665,
                "option_text": "A cybersecurity expert protecting systems from threats",
                "trait_tags": {"Software-Dev": 1.0, "Cyber-Defense": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 2666,
                "option_text": "A systems programmer working on operating systems",
                "trait_tags": {"Software-Dev": 1.0, "Hardware-Systems": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Realistic": 0.32, "Data-Analytics": 0.3}
            },
            {
                "option_id": 2667,
                "option_text": "A data engineer building pipelines and analytics tools",
                "trait_tags": {"Software-Dev": 1.0, "Data-Analytics": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Analytical-Skill": 0.36, "Cyber-Defense": 0.25}
            },
            {
                "option_id": 2668,
                "option_text": "A DevOps engineer managing cloud infrastructure",
                "trait_tags": {"Software-Dev": 1.0, "Cloud-Systems": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25}
            }
        ]
    },
    {
        "question_id": 267,
        "question_text": "You're starting a content creation channel. What's your niche?",
        "category": "Interest - Digital Media Content",
        "options": [
            {
                "option_id": 2671,
                "option_text": "Tech reviews and gadget unboxing",
                "trait_tags": {"Digital-Media": 1.0, "Hardware-Systems": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Technical-Skill": 0.36, "Realistic": 0.32}
            },
            {
                "option_id": 2672,
                "option_text": "Gaming streams and esports commentary",
                "trait_tags": {"Digital-Media": 1.0, "Game-Dev": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Software-Dev": 0.32, "Technical-Skill": 0.32}
            },
            {
                "option_id": 2673,
                "option_text": "Cooking tutorials and food reviews",
                "trait_tags": {"Digital-Media": 1.0, "Culinary-Arts": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Visual-Design": 0.3, "Hospitality-Svc": 0.28}
            },
            {
                "option_id": 2674,
                "option_text": "Educational content for students",
                "trait_tags": {"Digital-Media": 1.0, "Teaching-Ed": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Social": 0.36, "People-Skill": 0.36}
            },
            {
                "option_id": 2675,
                "option_text": "Travel vlogs showcasing Philippine destinations",
                "trait_tags": {"Digital-Media": 1.0, "Tourism-Travel": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "People-Skill": 0.32, "Hospitality-Svc": 0.32}
            },
            {
                "option_id": 2676,
                "option_text": "Design tutorials for graphic design and art",
                "trait_tags": {"Digital-Media": 1.0, "Visual-Design": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Software-Dev": 0.2, "Technical-Skill": 0.2}
            },
            {
                "option_id": 2677,
                "option_text": "Fitness and wellness lifestyle content",
                "trait_tags": {"Digital-Media": 1.0, "Sports-Ed": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Physical-Skill": 0.36, "Visual-Design": 0.3}
            },
            {
                "option_id": 2678,
                "option_text": "Business and entrepreneurship tips for young Filipinos",
                "trait_tags": {"Digital-Media": 1.0, "Startup-Venture": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Enterprising": 0.36, "Visual-Design": 0.3}
            }
        ]
    },
    {
        "question_id": 268,
        "question_text": "A school asks you to create digital learning content. What do you make?",
        "category": "Situational - Digital Media Education",
        "options": [
            {
                "option_id": 2681,
                "option_text": "Animated explainer videos for science topics",
                "trait_tags": {"Digital-Media": 1.0, "Animation-3D": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Visual-Design": 0.3, "Game-Dev": 0.28}
            },
            {
                "option_id": 2682,
                "option_text": "Interactive online quizzes and learning games",
                "trait_tags": {"Digital-Media": 1.0, "Game-Dev": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Software-Dev": 0.32, "Technical-Skill": 0.32}
            },
            {
                "option_id": 2683,
                "option_text": "A podcast series interviewing experts",
                "trait_tags": {"Digital-Media": 1.0, "Performing-Arts": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Visual-Design": 0.3, "People-Skill": 0.24}
            },
            {
                "option_id": 2684,
                "option_text": "Infographics and visual study guides",
                "trait_tags": {"Digital-Media": 1.0, "Visual-Design": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Software-Dev": 0.2, "Technical-Skill": 0.2}
            },
            {
                "option_id": 2685,
                "option_text": "A YouTube channel with recorded lectures",
                "trait_tags": {"Digital-Media": 1.0, "Teaching-Ed": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Social": 0.36, "People-Skill": 0.36}
            },
            {
                "option_id": 2686,
                "option_text": "An e-learning website with course modules",
                "trait_tags": {"Web-Dev": 1.0, "Digital-Media": 0.8, "Technical-Skill": 0.45, "Software-Dev": 0.45, "Investigative": 0.35, "Creative-Skill": 0.32}
            },
            {
                "option_id": 2687,
                "option_text": "VR field trips to historical places",
                "trait_tags": {"Digital-Media": 1.0, "Animation-3D": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Visual-Design": 0.3, "Game-Dev": 0.28}
            },
            {
                "option_id": 2688,
                "option_text": "Social media campaigns to promote literacy",
                "trait_tags": {"Digital-Media": 1.0, "Marketing-Sales": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Enterprising": 0.36, "People-Skill": 0.32}
            }
        ]
    },
    {
        "question_id": 269,
        "question_text": "What physical activity or sport-related career interests you?",
        "category": "Interest - Physical Sports Career",
        "options": [
            {
                "option_id": 2691,
                "option_text": "Being a PE teacher and coaching school teams",
                "trait_tags": {"Sports-Ed": 1.0, "Teaching-Ed": 0.8, "Physical-Skill": 0.45, "Social": 0.36, "People-Skill": 0.36, "Rehab-Therapy": 0.2}
            },
            {
                "option_id": 2692,
                "option_text": "Athletic training and sports conditioning",
                "trait_tags": {"Sports-Ed": 1.0, "Physical-Skill": 0.8, "Social": 0.35, "Teaching-Ed": 0.35, "Realistic": 0.32, "Maritime-Sea": 0.28}
            },
            {
                "option_id": 2693,
                "option_text": "Sports nutrition and fitness planning",
                "trait_tags": {"Sports-Ed": 1.0, "Nutrition-Diet": 0.8, "Physical-Skill": 0.45, "Social": 0.35, "Teaching-Ed": 0.35, "Food-Science": 0.28}
            },
            {
                "option_id": 2694,
                "option_text": "Physical therapy for injured athletes",
                "trait_tags": {"Rehab-Therapy": 1.0, "Physical-Skill": 0.8, "Social": 0.35, "People-Skill": 0.35, "Realistic": 0.32, "Patient-Care": 0.3}
            },
            {
                "option_id": 2695,
                "option_text": "Sports events management and organization",
                "trait_tags": {"Sports-Ed": 1.0, "Admin-Skill": 0.8, "Physical-Skill": 0.45, "Conventional": 0.36, "Social": 0.35, "Teaching-Ed": 0.35}
            },
            {
                "option_id": 2696,
                "option_text": "Martial arts or self-defense instruction",
                "trait_tags": {"Physical-Skill": 1.0, "Teaching-Ed": 0.8, "Realistic": 0.4, "Social": 0.36, "People-Skill": 0.36, "Maritime-Sea": 0.35}
            },
            {
                "option_id": 2697,
                "option_text": "Outdoor recreation and adventure sports guiding",
                "trait_tags": {"Physical-Skill": 1.0, "Tourism-Travel": 0.8, "Realistic": 0.4, "Maritime-Sea": 0.35, "Agri-Nature": 0.35, "People-Skill": 0.32}
            },
            {
                "option_id": 2698,
                "option_text": "Sports broadcasting and commentary",
                "trait_tags": {"Sports-Ed": 1.0, "Film-Broadcast": 0.8, "Physical-Skill": 0.45, "Social": 0.35, "Teaching-Ed": 0.35, "Artistic": 0.32}
            }
        ]
    },
    {
        "question_id": 270,
        "question_text": "Your school is hosting a sports event. What role would you take?",
        "category": "Situational - Sports Event",
        "options": [
            {
                "option_id": 2701,
                "option_text": "Head coach — training and strategizing with the team",
                "trait_tags": {"Sports-Ed": 1.0, "People-Skill": 0.8, "Physical-Skill": 0.45, "Social": 0.36, "Teaching-Ed": 0.35, "Patient-Care": 0.32}
            },
            {
                "option_id": 2702,
                "option_text": "Event organizer — planning logistics and schedules",
                "trait_tags": {"Admin-Skill": 1.0, "Sports-Ed": 0.8, "Conventional": 0.45, "Physical-Skill": 0.36, "Finance-Acct": 0.3, "Social": 0.28}
            },
            {
                "option_id": 2703,
                "option_text": "Team medic — providing first aid to injured players",
                "trait_tags": {"Patient-Care": 1.0, "Physical-Skill": 0.8, "People-Skill": 0.45, "Social": 0.4, "Realistic": 0.32, "Rehab-Therapy": 0.3}
            },
            {
                "option_id": 2704,
                "option_text": "Sports photographer/videographer",
                "trait_tags": {"Film-Broadcast": 1.0, "Visual-Design": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Digital-Media": 0.4, "Technical-Skill": 0.2}
            },
            {
                "option_id": 2705,
                "option_text": "Data analyst — tracking team performance statistics",
                "trait_tags": {"Data-Analytics": 1.0, "Sports-Ed": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Physical-Skill": 0.36, "Software-Dev": 0.3}
            },
            {
                "option_id": 2706,
                "option_text": "Referee — ensuring fair play and enforcing rules",
                "trait_tags": {"Physical-Skill": 1.0, "Law-Enforce": 0.8, "Realistic": 0.4, "Maritime-Sea": 0.35, "Agri-Nature": 0.35, "Rehab-Therapy": 0.3}
            },
            {
                "option_id": 2707,
                "option_text": "Announcer and live commentator",
                "trait_tags": {"Performing-Arts": 1.0, "Sports-Ed": 0.8, "Artistic": 0.45, "Creative-Skill": 0.45, "Physical-Skill": 0.36, "People-Skill": 0.3}
            },
            {
                "option_id": 2708,
                "option_text": "Nutritionist — preparing meal plans for athletes",
                "trait_tags": {"Nutrition-Diet": 1.0, "Sports-Ed": 0.8, "Physical-Skill": 0.36, "Food-Science": 0.35, "Social": 0.3, "Analytical-Skill": 0.3}
            }
        ]
    },
    {
        "question_id": 271,
        "question_text": "What approach do you use when solving a complex problem?",
        "category": "Interest - Analytical Thinking",
        "options": [
            {
                "option_id": 2711,
                "option_text": "Break it down into smaller parts and solve step by step",
                "trait_tags": {"Analytical-Skill": 1.0, "Software-Dev": 0.8, "Investigative": 0.45, "Data-Analytics": 0.4, "Technical-Skill": 0.36, "Lab-Research": 0.35}
            },
            {
                "option_id": 2712,
                "option_text": "Gather all the data first and look for patterns",
                "trait_tags": {"Analytical-Skill": 1.0, "Data-Analytics": 0.8, "Investigative": 0.45, "Lab-Research": 0.35, "Finance-Acct": 0.35, "Medical-Lab": 0.3}
            },
            {
                "option_id": 2713,
                "option_text": "Research how others solved similar problems",
                "trait_tags": {"Analytical-Skill": 1.0, "Lab-Research": 0.8, "Investigative": 0.45, "Data-Analytics": 0.4, "Finance-Acct": 0.35, "Medical-Lab": 0.3}
            },
            {
                "option_id": 2714,
                "option_text": "Brainstorm creative and unconventional solutions",
                "trait_tags": {"Creative-Skill": 1.0, "Analytical-Skill": 0.8, "Artistic": 0.45, "Visual-Design": 0.4, "Digital-Media": 0.4, "Investigative": 0.36}
            },
            {
                "option_id": 2715,
                "option_text": "Build a prototype and test it immediately",
                "trait_tags": {"Technical-Skill": 1.0, "Analytical-Skill": 0.8, "Software-Dev": 0.4, "Hardware-Systems": 0.4, "Investigative": 0.36, "Realistic": 0.35}
            },
            {
                "option_id": 2716,
                "option_text": "Consult experts and collaborate with a team",
                "trait_tags": {"People-Skill": 1.0, "Analytical-Skill": 0.8, "Social": 0.45, "Patient-Care": 0.4, "Teaching-Ed": 0.4, "Hospitality-Svc": 0.4}
            },
            {
                "option_id": 2717,
                "option_text": "Use mathematical models and calculations",
                "trait_tags": {"Analytical-Skill": 1.0, "Finance-Acct": 0.8, "Investigative": 0.45, "Data-Analytics": 0.4, "Conventional": 0.36, "Lab-Research": 0.35}
            },
            {
                "option_id": 2718,
                "option_text": "Create a flowchart or diagram to visualize the problem",
                "trait_tags": {"Analytical-Skill": 1.0, "Visual-Design": 0.8, "Investigative": 0.45, "Data-Analytics": 0.4, "Artistic": 0.36, "Creative-Skill": 0.36}
            }
        ]
    },
    {
        "question_id": 272,
        "question_text": "What hands-on technical activity do you enjoy most?",
        "category": "Interest - Technical Skills",
        "options": [
            {
                "option_id": 2721,
                "option_text": "Building and repairing electronic circuits",
                "trait_tags": {"Technical-Skill": 1.0, "Electrical-Power": 0.8, "Software-Dev": 0.4, "Hardware-Systems": 0.4, "Realistic": 0.35, "Mechanical-Design": 0.35}
            },
            {
                "option_id": 2722,
                "option_text": "Assembling and upgrading computer hardware",
                "trait_tags": {"Technical-Skill": 1.0, "Hardware-Systems": 0.8, "Software-Dev": 0.4, "Realistic": 0.35, "Mechanical-Design": 0.35, "Investigative": 0.25}
            },
            {
                "option_id": 2723,
                "option_text": "Woodworking and furniture making",
                "trait_tags": {"Technical-Skill": 1.0, "Mechanical-Design": 0.8, "Software-Dev": 0.4, "Hardware-Systems": 0.4, "Realistic": 0.36, "Investigative": 0.25}
            },
            {
                "option_id": 2724,
                "option_text": "Automotive repair and engine maintenance",
                "trait_tags": {"Technical-Skill": 1.0, "Mechanical-Design": 0.8, "Software-Dev": 0.4, "Hardware-Systems": 0.4, "Realistic": 0.36, "Investigative": 0.25}
            },
            {
                "option_id": 2725,
                "option_text": "Welding and metal fabrication",
                "trait_tags": {"Technical-Skill": 1.0, "Industrial-Ops": 0.8, "Software-Dev": 0.4, "Hardware-Systems": 0.4, "Realistic": 0.35, "Mechanical-Design": 0.35}
            },
            {
                "option_id": 2726,
                "option_text": "Plumbing and electrical wiring installation",
                "trait_tags": {"Technical-Skill": 1.0, "Civil-Build": 0.8, "Software-Dev": 0.4, "Hardware-Systems": 0.4, "Realistic": 0.36, "Mechanical-Design": 0.35}
            },
            {
                "option_id": 2727,
                "option_text": "3D printing and prototype fabrication",
                "trait_tags": {"Technical-Skill": 1.0, "Mechanical-Design": 0.8, "Software-Dev": 0.4, "Hardware-Systems": 0.4, "Realistic": 0.36, "Investigative": 0.25}
            },
            {
                "option_id": 2728,
                "option_text": "Network cable installation and server setup",
                "trait_tags": {"Technical-Skill": 1.0, "Cloud-Systems": 0.8, "Software-Dev": 0.4, "Hardware-Systems": 0.4, "Realistic": 0.35, "Mechanical-Design": 0.35}
            }
        ]
    },
    {
        "question_id": 273,
        "question_text": "You're doing a hands-on technical project for school. What do you choose?",
        "category": "Situational - Technical Project",
        "options": [
            {
                "option_id": 2731,
                "option_text": "Build a working robot from scratch",
                "trait_tags": {"Technical-Skill": 1.0, "Hardware-Systems": 0.8, "Software-Dev": 0.4, "Realistic": 0.35, "Mechanical-Design": 0.35, "Investigative": 0.25}
            },
            {
                "option_id": 2732,
                "option_text": "Create a functioning solar-powered device",
                "trait_tags": {"Technical-Skill": 1.0, "Electrical-Power": 0.8, "Software-Dev": 0.4, "Hardware-Systems": 0.4, "Realistic": 0.35, "Mechanical-Design": 0.35}
            },
            {
                "option_id": 2733,
                "option_text": "Wire an entire model house with electricity",
                "trait_tags": {"Technical-Skill": 1.0, "Electrical-Power": 0.8, "Software-Dev": 0.4, "Hardware-Systems": 0.4, "Realistic": 0.35, "Mechanical-Design": 0.35}
            },
            {
                "option_id": 2734,
                "option_text": "Build a water filtration system from local materials",
                "trait_tags": {"Technical-Skill": 1.0, "Environmental-Eng": 0.8, "Software-Dev": 0.4, "Hardware-Systems": 0.4, "Realistic": 0.35, "Mechanical-Design": 0.35}
            },
            {
                "option_id": 2735,
                "option_text": "Construct a scale model bridge that supports weight",
                "trait_tags": {"Technical-Skill": 1.0, "Civil-Build": 0.8, "Software-Dev": 0.4, "Hardware-Systems": 0.4, "Realistic": 0.36, "Mechanical-Design": 0.35}
            },
            {
                "option_id": 2736,
                "option_text": "Program an Arduino-based sensor project",
                "trait_tags": {"Technical-Skill": 1.0, "Software-Dev": 0.8, "Hardware-Systems": 0.4, "Realistic": 0.35, "Mechanical-Design": 0.35, "Investigative": 0.32}
            },
            {
                "option_id": 2737,
                "option_text": "Build a home automation system with smart controls",
                "trait_tags": {"Technical-Skill": 1.0, "Cloud-Systems": 0.8, "Software-Dev": 0.4, "Hardware-Systems": 0.4, "Realistic": 0.35, "Mechanical-Design": 0.35}
            },
            {
                "option_id": 2738,
                "option_text": "Fabricate a mechanical device using 3D printing",
                "trait_tags": {"Technical-Skill": 1.0, "Mechanical-Design": 0.8, "Software-Dev": 0.4, "Hardware-Systems": 0.4, "Realistic": 0.36, "Investigative": 0.25}
            }
        ]
    },
    {
        "question_id": 274,
        "question_text": "A TV network offers you a production job. Which role do you pick?",
        "category": "Situational - Film Broadcast Career",
        "options": [
            {
                "option_id": 2741,
                "option_text": "Camera operator — shooting scenes and live events",
                "trait_tags": {"Film-Broadcast": 1.0, "Creative-Skill": 0.8, "Artistic": 0.4, "Digital-Media": 0.4, "Visual-Design": 0.32, "Spatial-Design": 0.28}
            },
            {
                "option_id": 2742,
                "option_text": "Video editor — cutting and assembling footage",
                "trait_tags": {"Film-Broadcast": 1.0, "Visual-Design": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Digital-Media": 0.4, "Technical-Skill": 0.2}
            },
            {
                "option_id": 2743,
                "option_text": "Director — leading the creative vision of a show",
                "trait_tags": {"Film-Broadcast": 1.0, "Creative-Skill": 0.8, "Artistic": 0.4, "Digital-Media": 0.4, "Visual-Design": 0.32, "Spatial-Design": 0.28}
            },
            {
                "option_id": 2744,
                "option_text": "Scriptwriter — writing stories for TV series",
                "trait_tags": {"Film-Broadcast": 1.0, "Creative-Skill": 0.8, "Artistic": 0.4, "Digital-Media": 0.4, "Visual-Design": 0.32, "Spatial-Design": 0.28}
            },
            {
                "option_id": 2745,
                "option_text": "Production manager — coordinating crews and schedules",
                "trait_tags": {"Film-Broadcast": 1.0, "Admin-Skill": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Digital-Media": 0.4, "Conventional": 0.36}
            },
            {
                "option_id": 2746,
                "option_text": "Audio engineer — recording and mixing sound",
                "trait_tags": {"Film-Broadcast": 1.0, "Performing-Arts": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Digital-Media": 0.4, "Visual-Design": 0.25}
            },
            {
                "option_id": 2747,
                "option_text": "VFX artist — adding visual effects in post-production",
                "trait_tags": {"Film-Broadcast": 1.0, "Animation-3D": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Digital-Media": 0.4, "Game-Dev": 0.28}
            },
            {
                "option_id": 2748,
                "option_text": "News reporter — covering stories in the field",
                "trait_tags": {"Film-Broadcast": 1.0, "People-Skill": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Digital-Media": 0.4, "Social": 0.36}
            }
        ]
    },
    {
        "question_id": 275,
        "question_text": "What area of law interests you the most?",
        "category": "Interest - Legal Specialization",
        "options": [
            {
                "option_id": 2751,
                "option_text": "Criminal law — prosecuting or defending in court",
                "trait_tags": {"Legal-Practice": 1.0, "Law-Enforce": 0.8, "Enterprising": 0.35, "Analytical-Skill": 0.35, "People-Skill": 0.3, "Realistic": 0.28}
            },
            {
                "option_id": 2752,
                "option_text": "Corporate law — advising businesses on legal matters",
                "trait_tags": {"Legal-Practice": 1.0, "Finance-Acct": 0.8, "Conventional": 0.36, "Enterprising": 0.35, "Analytical-Skill": 0.35, "People-Skill": 0.3}
            },
            {
                "option_id": 2753,
                "option_text": "Labor law — protecting workers' rights",
                "trait_tags": {"Legal-Practice": 1.0, "HR-Management": 0.8, "Enterprising": 0.35, "Analytical-Skill": 0.35, "People-Skill": 0.32, "Social": 0.28}
            },
            {
                "option_id": 2754,
                "option_text": "Environmental law — holding polluters accountable",
                "trait_tags": {"Legal-Practice": 1.0, "Environmental-Sci": 0.8, "Investigative": 0.36, "Enterprising": 0.35, "Analytical-Skill": 0.35, "Field-Research": 0.32}
            },
            {
                "option_id": 2755,
                "option_text": "Family law — helping with custody and domestic cases",
                "trait_tags": {"Legal-Practice": 1.0, "Social-Work": 0.8, "People-Skill": 0.36, "Social": 0.36, "Enterprising": 0.35, "Analytical-Skill": 0.35}
            },
            {
                "option_id": 2756,
                "option_text": "Cyber law — dealing with online crimes and digital rights",
                "trait_tags": {"Legal-Practice": 1.0, "Cyber-Defense": 0.8, "Enterprising": 0.35, "Analytical-Skill": 0.35, "Technical-Skill": 0.32, "People-Skill": 0.3}
            },
            {
                "option_id": 2757,
                "option_text": "Public interest law — fighting for social justice",
                "trait_tags": {"Legal-Practice": 1.0, "Community-Serve": 0.8, "Social": 0.36, "Enterprising": 0.35, "Analytical-Skill": 0.35, "People-Skill": 0.32}
            },
            {
                "option_id": 2758,
                "option_text": "Intellectual property — protecting inventions and creative works",
                "trait_tags": {"Legal-Practice": 1.0, "Creative-Skill": 0.8, "Artistic": 0.36, "Enterprising": 0.35, "Analytical-Skill": 0.35, "People-Skill": 0.3}
            }
        ]
    },
    {
        "question_id": 276,
        "question_text": "A friend comes to you with a personal problem. How do you help?",
        "category": "Situational - Counseling Approach",
        "options": [
            {
                "option_id": 2761,
                "option_text": "Listen carefully and help them process their feelings",
                "trait_tags": {"Counseling": 1.0, "People-Skill": 0.8, "Social": 0.45, "Teaching-Ed": 0.32, "Patient-Care": 0.32, "Hospitality-Svc": 0.32}
            },
            {
                "option_id": 2762,
                "option_text": "Give them practical advice based on similar situations",
                "trait_tags": {"Counseling": 1.0, "Analytical-Skill": 0.8, "Social": 0.45, "People-Skill": 0.45, "Investigative": 0.36, "Teaching-Ed": 0.3}
            },
            {
                "option_id": 2763,
                "option_text": "Encourage them to see a professional therapist",
                "trait_tags": {"Counseling": 1.0, "Patient-Care": 0.8, "Social": 0.45, "People-Skill": 0.45, "Teaching-Ed": 0.3, "Rehab-Therapy": 0.25}
            },
            {
                "option_id": 2764,
                "option_text": "Research the issue together to find solutions",
                "trait_tags": {"Counseling": 1.0, "Lab-Research": 0.8, "Social": 0.45, "People-Skill": 0.45, "Investigative": 0.36, "Analytical-Skill": 0.36}
            },
            {
                "option_id": 2765,
                "option_text": "Do something fun together to take their mind off it",
                "trait_tags": {"People-Skill": 1.0, "Performing-Arts": 0.8, "Social": 0.45, "Patient-Care": 0.4, "Teaching-Ed": 0.4, "Hospitality-Svc": 0.4}
            },
            {
                "option_id": 2766,
                "option_text": "Help them create a concrete action plan",
                "trait_tags": {"Counseling": 1.0, "Admin-Skill": 0.8, "Social": 0.45, "People-Skill": 0.45, "Conventional": 0.36, "Teaching-Ed": 0.3}
            },
            {
                "option_id": 2767,
                "option_text": "Share a relevant experience to make them feel understood",
                "trait_tags": {"Counseling": 1.0, "Teaching-Ed": 0.8, "Social": 0.45, "People-Skill": 0.45, "Rehab-Therapy": 0.25, "Community-Serve": 0.2}
            },
            {
                "option_id": 2768,
                "option_text": "Check on them regularly until they feel better",
                "trait_tags": {"Counseling": 1.0, "Social-Work": 0.8, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.32, "Teaching-Ed": 0.3}
            }
        ]
    },
    {
        "question_id": 277,
        "question_text": "You're opening your own restaurant. What's your concept?",
        "category": "Interest - Culinary Concept",
        "options": [
            {
                "option_id": 2771,
                "option_text": "A modern Filipino fusion restaurant with creative dishes",
                "trait_tags": {"Culinary-Arts": 1.0, "Creative-Skill": 0.8, "Artistic": 0.36, "Hospitality-Svc": 0.35, "Visual-Design": 0.32, "Digital-Media": 0.32}
            },
            {
                "option_id": 2772,
                "option_text": "A fast-food chain with affordable prices for students",
                "trait_tags": {"Culinary-Arts": 1.0, "Startup-Venture": 0.8, "Enterprising": 0.36, "Creative-Skill": 0.35, "Hospitality-Svc": 0.35, "Artistic": 0.3}
            },
            {
                "option_id": 2773,
                "option_text": "A health-focused cafe with organic and vegan options",
                "trait_tags": {"Culinary-Arts": 1.0, "Nutrition-Diet": 0.8, "Creative-Skill": 0.35, "Hospitality-Svc": 0.35, "Artistic": 0.3, "Food-Science": 0.28}
            },
            {
                "option_id": 2774,
                "option_text": "A bakery and pastry shop with artisan breads",
                "trait_tags": {"Culinary-Arts": 1.0, "Food-Science": 0.8, "Creative-Skill": 0.35, "Hospitality-Svc": 0.35, "Investigative": 0.32, "Artistic": 0.3}
            },
            {
                "option_id": 2775,
                "option_text": "A food truck serving street food with a twist",
                "trait_tags": {"Culinary-Arts": 1.0, "Startup-Venture": 0.8, "Enterprising": 0.36, "Creative-Skill": 0.35, "Hospitality-Svc": 0.35, "Artistic": 0.3}
            },
            {
                "option_id": 2776,
                "option_text": "A hotel restaurant with five-star dining experience",
                "trait_tags": {"Culinary-Arts": 1.0, "Hospitality-Svc": 0.8, "People-Skill": 0.36, "Creative-Skill": 0.35, "Tourism-Travel": 0.32, "Artistic": 0.3}
            },
            {
                "option_id": 2777,
                "option_text": "A cooking school where people learn Filipino dishes",
                "trait_tags": {"Culinary-Arts": 1.0, "Teaching-Ed": 0.8, "Social": 0.36, "People-Skill": 0.36, "Creative-Skill": 0.35, "Hospitality-Svc": 0.35}
            },
            {
                "option_id": 2778,
                "option_text": "A catering business for events and parties",
                "trait_tags": {"Culinary-Arts": 1.0, "Hospitality-Svc": 0.8, "People-Skill": 0.36, "Creative-Skill": 0.35, "Tourism-Travel": 0.32, "Artistic": 0.3}
            }
        ]
    },
    {
        "question_id": 278,
        "question_text": "You've been elected class president. What's your first project?",
        "category": "Situational - Leadership",
        "options": [
            {
                "option_id": 2781,
                "option_text": "Organize team-building activities for classmates",
                "trait_tags": {"People-Skill": 1.0, "Sports-Ed": 0.8, "Social": 0.45, "Patient-Care": 0.4, "Teaching-Ed": 0.4, "Hospitality-Svc": 0.4}
            },
            {
                "option_id": 2782,
                "option_text": "Set up a student council to address school issues",
                "trait_tags": {"People-Skill": 1.0, "Admin-Skill": 0.8, "Social": 0.45, "Patient-Care": 0.4, "Teaching-Ed": 0.4, "Hospitality-Svc": 0.4}
            },
            {
                "option_id": 2783,
                "option_text": "Create a student mentorship program for freshmen",
                "trait_tags": {"People-Skill": 1.0, "Teaching-Ed": 0.8, "Social": 0.45, "Patient-Care": 0.4, "Hospitality-Svc": 0.4, "Enterprising": 0.3}
            },
            {
                "option_id": 2784,
                "option_text": "Launch a fundraiser for school improvements",
                "trait_tags": {"People-Skill": 1.0, "Marketing-Sales": 0.8, "Social": 0.45, "Patient-Care": 0.4, "Teaching-Ed": 0.4, "Hospitality-Svc": 0.4}
            },
            {
                "option_id": 2785,
                "option_text": "Advocate for better school facilities and resources",
                "trait_tags": {"People-Skill": 1.0, "Community-Serve": 0.8, "Social": 0.45, "Patient-Care": 0.4, "Teaching-Ed": 0.4, "Hospitality-Svc": 0.4}
            },
            {
                "option_id": 2786,
                "option_text": "Plan a school fair or cultural festival",
                "trait_tags": {"People-Skill": 1.0, "Performing-Arts": 0.8, "Social": 0.45, "Patient-Care": 0.4, "Teaching-Ed": 0.4, "Hospitality-Svc": 0.4}
            },
            {
                "option_id": 2787,
                "option_text": "Start a peer counseling program for students in need",
                "trait_tags": {"Counseling": 1.0, "People-Skill": 0.8, "Social": 0.45, "Teaching-Ed": 0.32, "Patient-Care": 0.32, "Hospitality-Svc": 0.32}
            },
            {
                "option_id": 2788,
                "option_text": "Create a class website and social media page",
                "trait_tags": {"Digital-Media": 1.0, "People-Skill": 0.8, "Artistic": 0.4, "Creative-Skill": 0.4, "Social": 0.36, "Teaching-Ed": 0.32}
            }
        ]
    },
    {
        "question_id": 279,
        "question_text": "What aspect of medicine and drugs interests you the most?",
        "category": "Domain - Pharmacy",
        "options": [
            {
                "option_id": 2791,
                "option_text": "Learning how drugs interact with the human body",
                "trait_tags": {"Pharmacy": 1.0, "Medical-Lab": 0.8, "Investigative": 0.4, "Analytical-Skill": 0.4, "Lab-Research": 0.28, "Patient-Care": 0.25}
            },
            {
                "option_id": 2792,
                "option_text": "Formulating new medicines in a laboratory",
                "trait_tags": {"Pharmacy": 1.0, "Lab-Research": 0.8, "Investigative": 0.4, "Analytical-Skill": 0.4, "Medical-Lab": 0.35, "Patient-Care": 0.25}
            },
            {
                "option_id": 2793,
                "option_text": "Dispensing correct prescriptions to patients",
                "trait_tags": {"Pharmacy": 1.0, "Patient-Care": 0.8, "Investigative": 0.4, "Analytical-Skill": 0.4, "People-Skill": 0.36, "Medical-Lab": 0.35}
            },
            {
                "option_id": 2794,
                "option_text": "Checking for drug allergies and side effects",
                "trait_tags": {"Pharmacy": 1.0, "Analytical-Skill": 0.8, "Investigative": 0.4, "Medical-Lab": 0.35, "Data-Analytics": 0.32, "Lab-Research": 0.28}
            },
            {
                "option_id": 2795,
                "option_text": "Managing a pharmacy and its inventory",
                "trait_tags": {"Pharmacy": 1.0, "Admin-Skill": 0.8, "Investigative": 0.4, "Analytical-Skill": 0.4, "Conventional": 0.36, "Medical-Lab": 0.35}
            },
            {
                "option_id": 2796,
                "option_text": "Researching herbal and traditional Filipino medicine",
                "trait_tags": {"Pharmacy": 1.0, "Field-Research": 0.8, "Investigative": 0.4, "Analytical-Skill": 0.4, "Medical-Lab": 0.35, "Patient-Care": 0.25}
            },
            {
                "option_id": 2797,
                "option_text": "Quality control testing of pharmaceutical products",
                "trait_tags": {"Pharmacy": 1.0, "Lab-Research": 0.8, "Investigative": 0.4, "Analytical-Skill": 0.4, "Medical-Lab": 0.35, "Patient-Care": 0.25}
            },
            {
                "option_id": 2798,
                "option_text": "Educating patients on how to take their medications properly",
                "trait_tags": {"Pharmacy": 1.0, "Teaching-Ed": 0.8, "Investigative": 0.4, "Analytical-Skill": 0.4, "Social": 0.36, "People-Skill": 0.36}
            }
        ]
    },
    {
        "question_id": 280,
        "question_text": "SCENARIO: A patient brings in multiple prescriptions from different doctors. What concerns you most?",
        "category": "Situational - Pharmacy",
        "options": [
            {
                "option_id": 2801,
                "option_text": "Checking if any of the drugs interact dangerously",
                "trait_tags": {"Pharmacy": 1.0, "Analytical-Skill": 0.8, "Investigative": 0.4, "Medical-Lab": 0.35, "Data-Analytics": 0.32, "Lab-Research": 0.28}
            },
            {
                "option_id": 2802,
                "option_text": "Verifying the correct dosages for the patient's condition",
                "trait_tags": {"Pharmacy": 1.0, "Medical-Lab": 0.8, "Investigative": 0.4, "Analytical-Skill": 0.4, "Lab-Research": 0.28, "Patient-Care": 0.25}
            },
            {
                "option_id": 2803,
                "option_text": "Counseling the patient on how to take each medication",
                "trait_tags": {"Pharmacy": 1.0, "Patient-Care": 0.8, "Investigative": 0.4, "Analytical-Skill": 0.4, "People-Skill": 0.36, "Medical-Lab": 0.35}
            },
            {
                "option_id": 2804,
                "option_text": "Contacting the doctors to coordinate the treatment plan",
                "trait_tags": {"Pharmacy": 1.0, "People-Skill": 0.8, "Investigative": 0.4, "Analytical-Skill": 0.4, "Social": 0.36, "Medical-Lab": 0.35}
            },
            {
                "option_id": 2805,
                "option_text": "Recording all prescriptions in the patient's file accurately",
                "trait_tags": {"Pharmacy": 1.0, "Health-Admin": 0.8, "Investigative": 0.4, "Analytical-Skill": 0.4, "Admin-Skill": 0.36, "Medical-Lab": 0.35}
            },
            {
                "option_id": 2806,
                "option_text": "Suggesting cheaper generic alternatives to save money",
                "trait_tags": {"Pharmacy": 1.0, "Finance-Acct": 0.8, "Investigative": 0.4, "Analytical-Skill": 0.4, "Conventional": 0.36, "Medical-Lab": 0.35}
            },
            {
                "option_id": 2807,
                "option_text": "Looking up the latest clinical research on the drugs",
                "trait_tags": {"Pharmacy": 1.0, "Lab-Research": 0.8, "Investigative": 0.4, "Analytical-Skill": 0.4, "Medical-Lab": 0.35, "Patient-Care": 0.25}
            },
            {
                "option_id": 2808,
                "option_text": "Ensuring the pharmacy has all the medicines in stock",
                "trait_tags": {"Pharmacy": 1.0, "Admin-Skill": 0.8, "Investigative": 0.4, "Analytical-Skill": 0.4, "Conventional": 0.36, "Medical-Lab": 0.35}
            }
        ]
    },
    {
        "question_id": 281,
        "question_text": "Which pharmacy career path appeals to you most?",
        "category": "Career - Pharmacy",
        "options": [
            {
                "option_id": 2811,
                "option_text": "Community pharmacist helping patients daily",
                "trait_tags": {"Pharmacy": 1.0, "Patient-Care": 0.8, "Investigative": 0.4, "Analytical-Skill": 0.4, "People-Skill": 0.36, "Medical-Lab": 0.35}
            },
            {
                "option_id": 2812,
                "option_text": "Hospital pharmacist working with doctors on treatment plans",
                "trait_tags": {"Pharmacy": 1.0, "Medical-Lab": 0.8, "Investigative": 0.4, "Analytical-Skill": 0.4, "Lab-Research": 0.28, "Patient-Care": 0.25}
            },
            {
                "option_id": 2813,
                "option_text": "Pharmaceutical researcher developing new drugs",
                "trait_tags": {"Pharmacy": 1.0, "Lab-Research": 0.8, "Investigative": 0.4, "Analytical-Skill": 0.4, "Medical-Lab": 0.35, "Patient-Care": 0.25}
            },
            {
                "option_id": 2814,
                "option_text": "Regulatory affairs specialist ensuring drug safety",
                "trait_tags": {"Pharmacy": 1.0, "Analytical-Skill": 0.8, "Investigative": 0.4, "Medical-Lab": 0.35, "Data-Analytics": 0.32, "Lab-Research": 0.28}
            },
            {
                "option_id": 2815,
                "option_text": "Pharmaceutical sales representative",
                "trait_tags": {"Pharmacy": 1.0, "Marketing-Sales": 0.8, "Investigative": 0.4, "Analytical-Skill": 0.4, "Enterprising": 0.36, "Medical-Lab": 0.35}
            },
            {
                "option_id": 2816,
                "option_text": "Clinical trial coordinator testing new medicines",
                "trait_tags": {"Pharmacy": 1.0, "Lab-Research": 0.8, "Investigative": 0.4, "Analytical-Skill": 0.4, "Medical-Lab": 0.35, "Patient-Care": 0.25}
            },
            {
                "option_id": 2817,
                "option_text": "Pharmacy owner running my own drugstore",
                "trait_tags": {"Pharmacy": 1.0, "Startup-Venture": 0.8, "Investigative": 0.4, "Analytical-Skill": 0.4, "Enterprising": 0.36, "Medical-Lab": 0.35}
            },
            {
                "option_id": 2818,
                "option_text": "Industrial pharmacist in drug manufacturing",
                "trait_tags": {"Pharmacy": 1.0, "Industrial-Ops": 0.8, "Investigative": 0.4, "Analytical-Skill": 0.4, "Medical-Lab": 0.35, "Patient-Care": 0.25}
            }
        ]
    },
    {
        "question_id": 282,
        "question_text": "What aspect of hospital management interests you most?",
        "category": "Domain - Health Admin",
        "options": [
            {
                "option_id": 2821,
                "option_text": "Managing patient records and electronic health systems",
                "trait_tags": {"Health-Admin": 1.0, "Software-Dev": 0.8, "Admin-Skill": 0.45, "Conventional": 0.4, "Technical-Skill": 0.36, "Investigative": 0.32}
            },
            {
                "option_id": 2822,
                "option_text": "Ensuring patient data privacy and security compliance",
                "trait_tags": {"Health-Admin": 1.0, "Cyber-Defense": 0.8, "Admin-Skill": 0.45, "Conventional": 0.4, "Technical-Skill": 0.32, "Investigative": 0.28}
            },
            {
                "option_id": 2823,
                "option_text": "Coordinating hospital departments and staff schedules",
                "trait_tags": {"Health-Admin": 1.0, "Admin-Skill": 0.8, "Conventional": 0.4, "Finance-Acct": 0.24, "Hospitality-Svc": 0.16, "Patient-Care": 0.15}
            },
            {
                "option_id": 2824,
                "option_text": "Managing hospital budgets and healthcare financing",
                "trait_tags": {"Health-Admin": 1.0, "Finance-Acct": 0.8, "Admin-Skill": 0.45, "Conventional": 0.4, "Analytical-Skill": 0.32, "Startup-Venture": 0.16}
            },
            {
                "option_id": 2825,
                "option_text": "Implementing health information technology systems",
                "trait_tags": {"Health-Admin": 1.0, "Software-Dev": 0.8, "Admin-Skill": 0.45, "Conventional": 0.4, "Technical-Skill": 0.36, "Investigative": 0.32}
            },
            {
                "option_id": 2826,
                "option_text": "Coding medical procedures for insurance billing",
                "trait_tags": {"Health-Admin": 1.0, "Analytical-Skill": 0.8, "Admin-Skill": 0.45, "Conventional": 0.4, "Investigative": 0.36, "Data-Analytics": 0.32}
            },
            {
                "option_id": 2827,
                "option_text": "Analyzing healthcare data to improve patient outcomes",
                "trait_tags": {"Health-Admin": 1.0, "Data-Analytics": 0.8, "Admin-Skill": 0.45, "Conventional": 0.4, "Investigative": 0.36, "Analytical-Skill": 0.36}
            },
            {
                "option_id": 2828,
                "option_text": "Ensuring hospital compliance with government regulations",
                "trait_tags": {"Health-Admin": 1.0, "Admin-Skill": 0.8, "Conventional": 0.4, "Finance-Acct": 0.24, "Hospitality-Svc": 0.16, "Patient-Care": 0.15}
            }
        ]
    },
    {
        "question_id": 283,
        "question_text": "SCENARIO: A hospital wants to go paperless. What role would you take?",
        "category": "Situational - Health Admin",
        "options": [
            {
                "option_id": 2831,
                "option_text": "Leading the digital transformation project",
                "trait_tags": {"Health-Admin": 1.0, "Admin-Skill": 0.8, "Conventional": 0.4, "Finance-Acct": 0.24, "Hospitality-Svc": 0.16, "Patient-Care": 0.15}
            },
            {
                "option_id": 2832,
                "option_text": "Training hospital staff on the new electronic system",
                "trait_tags": {"Health-Admin": 1.0, "Teaching-Ed": 0.8, "Admin-Skill": 0.45, "Conventional": 0.4, "Social": 0.36, "People-Skill": 0.36}
            },
            {
                "option_id": 2833,
                "option_text": "Migrating patient records to the digital database",
                "trait_tags": {"Health-Admin": 1.0, "Data-Analytics": 0.8, "Admin-Skill": 0.45, "Conventional": 0.4, "Investigative": 0.36, "Analytical-Skill": 0.36}
            },
            {
                "option_id": 2834,
                "option_text": "Ensuring data security and HIPAA-like compliance",
                "trait_tags": {"Health-Admin": 1.0, "Cyber-Defense": 0.8, "Admin-Skill": 0.45, "Conventional": 0.4, "Technical-Skill": 0.32, "Investigative": 0.28}
            },
            {
                "option_id": 2835,
                "option_text": "Setting up the IT infrastructure and servers",
                "trait_tags": {"Health-Admin": 1.0, "Hardware-Systems": 0.8, "Admin-Skill": 0.45, "Conventional": 0.4, "Technical-Skill": 0.36, "Realistic": 0.32}
            },
            {
                "option_id": 2836,
                "option_text": "Designing user-friendly interfaces for doctors and nurses",
                "trait_tags": {"Health-Admin": 1.0, "Software-Dev": 0.8, "Admin-Skill": 0.45, "Conventional": 0.4, "Technical-Skill": 0.36, "Investigative": 0.32}
            },
            {
                "option_id": 2837,
                "option_text": "Managing the budget for the system upgrade",
                "trait_tags": {"Health-Admin": 1.0, "Finance-Acct": 0.8, "Admin-Skill": 0.45, "Conventional": 0.4, "Analytical-Skill": 0.32, "Startup-Venture": 0.16}
            },
            {
                "option_id": 2838,
                "option_text": "Creating reports on how the new system improves efficiency",
                "trait_tags": {"Health-Admin": 1.0, "Analytical-Skill": 0.8, "Admin-Skill": 0.45, "Conventional": 0.4, "Investigative": 0.36, "Data-Analytics": 0.32}
            }
        ]
    },
    {
        "question_id": 284,
        "question_text": "Which health information career sounds most appealing?",
        "category": "Career - Health Admin",
        "options": [
            {
                "option_id": 2841,
                "option_text": "Health information manager at a large hospital",
                "trait_tags": {"Health-Admin": 1.0, "Admin-Skill": 0.8, "Conventional": 0.4, "Finance-Acct": 0.24, "Hospitality-Svc": 0.16, "Patient-Care": 0.15}
            },
            {
                "option_id": 2842,
                "option_text": "Medical coder translating diagnoses into billing codes",
                "trait_tags": {"Health-Admin": 1.0, "Analytical-Skill": 0.8, "Admin-Skill": 0.45, "Conventional": 0.4, "Investigative": 0.36, "Data-Analytics": 0.32}
            },
            {
                "option_id": 2843,
                "option_text": "Healthcare data analyst improving patient care quality",
                "trait_tags": {"Health-Admin": 1.0, "Data-Analytics": 0.8, "Admin-Skill": 0.45, "Conventional": 0.4, "Investigative": 0.36, "Analytical-Skill": 0.36}
            },
            {
                "option_id": 2844,
                "option_text": "PhilHealth or HMO claims processor",
                "trait_tags": {"Health-Admin": 1.0, "Finance-Acct": 0.8, "Admin-Skill": 0.45, "Conventional": 0.4, "Analytical-Skill": 0.32, "Startup-Venture": 0.16}
            },
            {
                "option_id": 2845,
                "option_text": "Health IT specialist maintaining hospital software",
                "trait_tags": {"Health-Admin": 1.0, "Software-Dev": 0.8, "Admin-Skill": 0.45, "Conventional": 0.4, "Technical-Skill": 0.36, "Investigative": 0.32}
            },
            {
                "option_id": 2846,
                "option_text": "Clinical research coordinator managing study data",
                "trait_tags": {"Health-Admin": 1.0, "Lab-Research": 0.8, "Admin-Skill": 0.45, "Conventional": 0.4, "Investigative": 0.36, "Analytical-Skill": 0.36}
            },
            {
                "option_id": 2847,
                "option_text": "Hospital administrator overseeing daily operations",
                "trait_tags": {"Health-Admin": 1.0, "Admin-Skill": 0.8, "Conventional": 0.4, "Finance-Acct": 0.24, "Hospitality-Svc": 0.16, "Patient-Care": 0.15}
            },
            {
                "option_id": 2848,
                "option_text": "Public health records officer for DOH or LGU",
                "trait_tags": {"Health-Admin": 1.0, "Community-Serve": 0.8, "Admin-Skill": 0.45, "Conventional": 0.4, "Social": 0.36, "People-Skill": 0.32}
            }
        ]
    },
    {
        "question_id": 285,
        "question_text": "What aspect of managing people and employees excites you?",
        "category": "Domain - HR Management",
        "options": [
            {
                "option_id": 2851,
                "option_text": "Interviewing and hiring the best candidates",
                "trait_tags": {"HR-Management": 1.0, "People-Skill": 0.8, "Social": 0.36, "Enterprising": 0.35, "Admin-Skill": 0.35, "Teaching-Ed": 0.32}
            },
            {
                "option_id": 2852,
                "option_text": "Designing training programs for employee development",
                "trait_tags": {"HR-Management": 1.0, "Teaching-Ed": 0.8, "People-Skill": 0.4, "Social": 0.36, "Enterprising": 0.35, "Admin-Skill": 0.35}
            },
            {
                "option_id": 2853,
                "option_text": "Resolving workplace conflicts and employee grievances",
                "trait_tags": {"HR-Management": 1.0, "People-Skill": 0.8, "Social": 0.36, "Enterprising": 0.35, "Admin-Skill": 0.35, "Teaching-Ed": 0.32}
            },
            {
                "option_id": 2854,
                "option_text": "Managing payroll, benefits, and compensation packages",
                "trait_tags": {"HR-Management": 1.0, "Finance-Acct": 0.8, "People-Skill": 0.4, "Conventional": 0.36, "Social": 0.35, "Enterprising": 0.35}
            },
            {
                "option_id": 2855,
                "option_text": "Creating company culture and team-building activities",
                "trait_tags": {"HR-Management": 1.0, "Creative-Skill": 0.8, "People-Skill": 0.4, "Artistic": 0.36, "Social": 0.35, "Enterprising": 0.35}
            },
            {
                "option_id": 2856,
                "option_text": "Ensuring compliance with labor laws and regulations",
                "trait_tags": {"HR-Management": 1.0, "Admin-Skill": 0.8, "People-Skill": 0.4, "Conventional": 0.36, "Social": 0.35, "Enterprising": 0.35}
            },
            {
                "option_id": 2857,
                "option_text": "Analyzing employee performance data and productivity",
                "trait_tags": {"HR-Management": 1.0, "Data-Analytics": 0.8, "People-Skill": 0.4, "Investigative": 0.36, "Analytical-Skill": 0.36, "Social": 0.35}
            },
            {
                "option_id": 2858,
                "option_text": "Planning career paths and succession for employees",
                "trait_tags": {"HR-Management": 1.0, "Admin-Skill": 0.8, "People-Skill": 0.4, "Conventional": 0.36, "Social": 0.35, "Enterprising": 0.35}
            }
        ]
    },
    {
        "question_id": 286,
        "question_text": "SCENARIO: An employee files a complaint about unfair treatment. What do you do?",
        "category": "Situational - HR",
        "options": [
            {
                "option_id": 2861,
                "option_text": "Interview both parties privately to understand the situation",
                "trait_tags": {"HR-Management": 1.0, "People-Skill": 0.8, "Social": 0.36, "Enterprising": 0.35, "Admin-Skill": 0.35, "Teaching-Ed": 0.32}
            },
            {
                "option_id": 2862,
                "option_text": "Review company policies and labor law for proper procedures",
                "trait_tags": {"HR-Management": 1.0, "Legal-Practice": 0.8, "People-Skill": 0.4, "Social": 0.35, "Enterprising": 0.35, "Admin-Skill": 0.35}
            },
            {
                "option_id": 2863,
                "option_text": "Document everything carefully for official records",
                "trait_tags": {"HR-Management": 1.0, "Admin-Skill": 0.8, "People-Skill": 0.4, "Conventional": 0.36, "Social": 0.35, "Enterprising": 0.35}
            },
            {
                "option_id": 2864,
                "option_text": "Mediate a meeting between the parties to resolve it",
                "trait_tags": {"HR-Management": 1.0, "Counseling": 0.8, "People-Skill": 0.4, "Social": 0.36, "Enterprising": 0.35, "Admin-Skill": 0.35}
            },
            {
                "option_id": 2865,
                "option_text": "Consult with management on disciplinary actions",
                "trait_tags": {"HR-Management": 1.0, "Admin-Skill": 0.8, "People-Skill": 0.4, "Conventional": 0.36, "Social": 0.35, "Enterprising": 0.35}
            },
            {
                "option_id": 2866,
                "option_text": "Create a training program to prevent future incidents",
                "trait_tags": {"HR-Management": 1.0, "Teaching-Ed": 0.8, "People-Skill": 0.4, "Social": 0.36, "Enterprising": 0.35, "Admin-Skill": 0.35}
            },
            {
                "option_id": 2867,
                "option_text": "Conduct a workplace survey to check team morale",
                "trait_tags": {"HR-Management": 1.0, "Data-Analytics": 0.8, "People-Skill": 0.4, "Investigative": 0.36, "Analytical-Skill": 0.36, "Social": 0.35}
            },
            {
                "option_id": 2868,
                "option_text": "Ensure emotional support is available for the affected employee",
                "trait_tags": {"HR-Management": 1.0, "Counseling": 0.8, "People-Skill": 0.4, "Social": 0.36, "Enterprising": 0.35, "Admin-Skill": 0.35}
            }
        ]
    },
    {
        "question_id": 287,
        "question_text": "Which HR career role appeals to you most?",
        "category": "Career - HR",
        "options": [
            {
                "option_id": 2871,
                "option_text": "Recruitment specialist finding top talent",
                "trait_tags": {"HR-Management": 1.0, "Marketing-Sales": 0.8, "People-Skill": 0.4, "Enterprising": 0.36, "Social": 0.35, "Admin-Skill": 0.35}
            },
            {
                "option_id": 2872,
                "option_text": "Training and development manager",
                "trait_tags": {"HR-Management": 1.0, "Teaching-Ed": 0.8, "People-Skill": 0.4, "Social": 0.36, "Enterprising": 0.35, "Admin-Skill": 0.35}
            },
            {
                "option_id": 2873,
                "option_text": "Compensation and benefits administrator",
                "trait_tags": {"HR-Management": 1.0, "Finance-Acct": 0.8, "People-Skill": 0.4, "Conventional": 0.36, "Social": 0.35, "Enterprising": 0.35}
            },
            {
                "option_id": 2874,
                "option_text": "Employee relations specialist",
                "trait_tags": {"HR-Management": 1.0, "People-Skill": 0.8, "Social": 0.36, "Enterprising": 0.35, "Admin-Skill": 0.35, "Teaching-Ed": 0.32}
            },
            {
                "option_id": 2875,
                "option_text": "Organizational development consultant",
                "trait_tags": {"HR-Management": 1.0, "Startup-Venture": 0.8, "People-Skill": 0.4, "Enterprising": 0.36, "Social": 0.35, "Admin-Skill": 0.35}
            },
            {
                "option_id": 2876,
                "option_text": "HR analytics and workforce planning specialist",
                "trait_tags": {"HR-Management": 1.0, "Data-Analytics": 0.8, "People-Skill": 0.4, "Investigative": 0.36, "Analytical-Skill": 0.36, "Social": 0.35}
            },
            {
                "option_id": 2877,
                "option_text": "Labor compliance and legal affairs officer",
                "trait_tags": {"HR-Management": 1.0, "Legal-Practice": 0.8, "People-Skill": 0.4, "Social": 0.35, "Enterprising": 0.35, "Admin-Skill": 0.35}
            },
            {
                "option_id": 2878,
                "option_text": "HR director overseeing all human resource functions",
                "trait_tags": {"HR-Management": 1.0, "Admin-Skill": 0.8, "People-Skill": 0.4, "Conventional": 0.36, "Social": 0.35, "Enterprising": 0.35}
            }
        ]
    },
    {
        "question_id": 288,
        "question_text": "What aspect of forensic investigation fascinates you most?",
        "category": "Domain - Forensic Science",
        "options": [
            {
                "option_id": 2881,
                "option_text": "Analyzing DNA and biological evidence in a crime lab",
                "trait_tags": {"Forensic-Sci": 1.0, "Lab-Research": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.4, "Law-Enforce": 0.35, "Medical-Lab": 0.24}
            },
            {
                "option_id": 2882,
                "option_text": "Examining fingerprints and trace evidence at crime scenes",
                "trait_tags": {"Forensic-Sci": 1.0, "Analytical-Skill": 0.8, "Investigative": 0.45, "Lab-Research": 0.35, "Law-Enforce": 0.35, "Data-Analytics": 0.32}
            },
            {
                "option_id": 2883,
                "option_text": "Using chemistry to detect poisons and toxins",
                "trait_tags": {"Forensic-Sci": 1.0, "Medical-Lab": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.4, "Lab-Research": 0.35, "Law-Enforce": 0.35}
            },
            {
                "option_id": 2884,
                "option_text": "Analyzing digital evidence from computers and phones",
                "trait_tags": {"Forensic-Sci": 1.0, "Cyber-Defense": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.4, "Lab-Research": 0.35, "Law-Enforce": 0.35}
            },
            {
                "option_id": 2885,
                "option_text": "Reconstructing crime scenes to determine what happened",
                "trait_tags": {"Forensic-Sci": 1.0, "Analytical-Skill": 0.8, "Investigative": 0.45, "Lab-Research": 0.35, "Law-Enforce": 0.35, "Data-Analytics": 0.32}
            },
            {
                "option_id": 2886,
                "option_text": "Testifying in court as an expert witness",
                "trait_tags": {"Forensic-Sci": 1.0, "Legal-Practice": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.4, "Lab-Research": 0.35, "Law-Enforce": 0.35}
            },
            {
                "option_id": 2887,
                "option_text": "Identifying victims through dental or skeletal analysis",
                "trait_tags": {"Forensic-Sci": 1.0, "Medical-Lab": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.4, "Lab-Research": 0.35, "Law-Enforce": 0.35}
            },
            {
                "option_id": 2888,
                "option_text": "Studying ballistics and firearms evidence",
                "trait_tags": {"Forensic-Sci": 1.0, "Law-Enforce": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.4, "Lab-Research": 0.35, "Realistic": 0.28}
            }
        ]
    },
    {
        "question_id": 289,
        "question_text": "SCENARIO: Police find an unidentified substance at a crime scene. How would you help?",
        "category": "Situational - Forensics",
        "options": [
            {
                "option_id": 2891,
                "option_text": "Run chemical tests to identify the substance",
                "trait_tags": {"Forensic-Sci": 1.0, "Lab-Research": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.4, "Law-Enforce": 0.35, "Medical-Lab": 0.24}
            },
            {
                "option_id": 2892,
                "option_text": "Compare it against known drug databases",
                "trait_tags": {"Forensic-Sci": 1.0, "Pharmacy": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.4, "Lab-Research": 0.35, "Law-Enforce": 0.35}
            },
            {
                "option_id": 2893,
                "option_text": "Document the chain of custody for court use",
                "trait_tags": {"Forensic-Sci": 1.0, "Admin-Skill": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.4, "Conventional": 0.36, "Lab-Research": 0.35}
            },
            {
                "option_id": 2894,
                "option_text": "Analyze it under a microscope for trace elements",
                "trait_tags": {"Forensic-Sci": 1.0, "Medical-Lab": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.4, "Lab-Research": 0.35, "Law-Enforce": 0.35}
            },
            {
                "option_id": 2895,
                "option_text": "Check if it matches substances from other cases",
                "trait_tags": {"Forensic-Sci": 1.0, "Data-Analytics": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.4, "Lab-Research": 0.35, "Law-Enforce": 0.35}
            },
            {
                "option_id": 2896,
                "option_text": "Determine if it poses a health risk to first responders",
                "trait_tags": {"Forensic-Sci": 1.0, "Patient-Care": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.4, "People-Skill": 0.36, "Lab-Research": 0.35}
            },
            {
                "option_id": 2897,
                "option_text": "Prepare a detailed report for the investigating officers",
                "trait_tags": {"Forensic-Sci": 1.0, "Law-Enforce": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.4, "Lab-Research": 0.35, "Realistic": 0.28}
            },
            {
                "option_id": 2898,
                "option_text": "Use advanced spectroscopy equipment for precise identification",
                "trait_tags": {"Forensic-Sci": 1.0, "Technical-Skill": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.4, "Lab-Research": 0.35, "Law-Enforce": 0.35}
            }
        ]
    },
    {
        "question_id": 290,
        "question_text": "What excites you most about the tourism and travel industry?",
        "category": "Domain - Tourism",
        "options": [
            {
                "option_id": 2901,
                "option_text": "Planning dream vacations and travel itineraries for clients",
                "trait_tags": {"Tourism-Travel": 1.0, "People-Skill": 0.8, "Hospitality-Svc": 0.4, "Social": 0.36, "Enterprising": 0.35, "Teaching-Ed": 0.32}
            },
            {
                "option_id": 2902,
                "option_text": "Being a tour guide sharing Philippine history and culture",
                "trait_tags": {"Tourism-Travel": 1.0, "Teaching-Ed": 0.8, "People-Skill": 0.4, "Hospitality-Svc": 0.4, "Social": 0.36, "Enterprising": 0.35}
            },
            {
                "option_id": 2903,
                "option_text": "Managing a travel agency or booking office",
                "trait_tags": {"Tourism-Travel": 1.0, "Startup-Venture": 0.8, "People-Skill": 0.4, "Hospitality-Svc": 0.4, "Enterprising": 0.36, "Marketing-Sales": 0.25}
            },
            {
                "option_id": 2904,
                "option_text": "Marketing tourist destinations through social media",
                "trait_tags": {"Tourism-Travel": 1.0, "Marketing-Sales": 0.8, "People-Skill": 0.4, "Hospitality-Svc": 0.4, "Enterprising": 0.36, "Startup-Venture": 0.24}
            },
            {
                "option_id": 2905,
                "option_text": "Developing eco-tourism programs for local communities",
                "trait_tags": {"Tourism-Travel": 1.0, "Environmental-Sci": 0.8, "People-Skill": 0.4, "Hospitality-Svc": 0.4, "Investigative": 0.36, "Enterprising": 0.35}
            },
            {
                "option_id": 2906,
                "option_text": "Working at an airline or cruise ship company",
                "trait_tags": {"Tourism-Travel": 1.0, "Hospitality-Svc": 0.8, "People-Skill": 0.4, "Enterprising": 0.35, "Marketing-Sales": 0.25, "Culinary-Arts": 0.24}
            },
            {
                "option_id": 2907,
                "option_text": "Creating travel content as a vlogger or photographer",
                "trait_tags": {"Tourism-Travel": 1.0, "Digital-Media": 0.8, "People-Skill": 0.4, "Hospitality-Svc": 0.4, "Enterprising": 0.35, "Artistic": 0.32}
            },
            {
                "option_id": 2908,
                "option_text": "Organizing conventions and large-scale tourism events",
                "trait_tags": {"Tourism-Travel": 1.0, "Admin-Skill": 0.8, "People-Skill": 0.4, "Hospitality-Svc": 0.4, "Conventional": 0.36, "Enterprising": 0.35}
            }
        ]
    },
    {
        "question_id": 291,
        "question_text": "SCENARIO: Your province wants to boost tourism. What would you propose?",
        "category": "Situational - Tourism",
        "options": [
            {
                "option_id": 2911,
                "option_text": "Create travel packages highlighting local attractions",
                "trait_tags": {"Tourism-Travel": 1.0, "Marketing-Sales": 0.8, "People-Skill": 0.4, "Hospitality-Svc": 0.4, "Enterprising": 0.36, "Startup-Venture": 0.24}
            },
            {
                "option_id": 2912,
                "option_text": "Train locals as professional tour guides",
                "trait_tags": {"Tourism-Travel": 1.0, "Teaching-Ed": 0.8, "People-Skill": 0.4, "Hospitality-Svc": 0.4, "Social": 0.36, "Enterprising": 0.35}
            },
            {
                "option_id": 2913,
                "option_text": "Build a tourism website and social media campaign",
                "trait_tags": {"Tourism-Travel": 1.0, "Web-Dev": 0.8, "People-Skill": 0.4, "Hospitality-Svc": 0.4, "Technical-Skill": 0.36, "Enterprising": 0.35}
            },
            {
                "option_id": 2914,
                "option_text": "Develop homestay and Airbnb programs for visitors",
                "trait_tags": {"Tourism-Travel": 1.0, "Hospitality-Svc": 0.8, "People-Skill": 0.4, "Enterprising": 0.35, "Marketing-Sales": 0.25, "Culinary-Arts": 0.24}
            },
            {
                "option_id": 2915,
                "option_text": "Organize a food and cultural festival",
                "trait_tags": {"Tourism-Travel": 1.0, "Culinary-Arts": 0.8, "People-Skill": 0.4, "Hospitality-Svc": 0.4, "Enterprising": 0.35, "Creative-Skill": 0.28}
            },
            {
                "option_id": 2916,
                "option_text": "Partner with airlines for discounted travel deals",
                "trait_tags": {"Tourism-Travel": 1.0, "Finance-Acct": 0.8, "People-Skill": 0.4, "Hospitality-Svc": 0.4, "Conventional": 0.36, "Enterprising": 0.35}
            },
            {
                "option_id": 2917,
                "option_text": "Promote adventure tourism like hiking and diving",
                "trait_tags": {"Tourism-Travel": 1.0, "Physical-Skill": 0.8, "People-Skill": 0.4, "Hospitality-Svc": 0.4, "Enterprising": 0.35, "Realistic": 0.32}
            },
            {
                "option_id": 2918,
                "option_text": "Ensure tourist safety and coordinate with local police",
                "trait_tags": {"Tourism-Travel": 1.0, "Law-Enforce": 0.8, "People-Skill": 0.4, "Hospitality-Svc": 0.4, "Enterprising": 0.35, "Realistic": 0.28}
            }
        ]
    },
    {
        "question_id": 292,
        "question_text": "What aspect of helping vulnerable communities appeals to you most?",
        "category": "Domain - Social Work",
        "options": [
            {
                "option_id": 2921,
                "option_text": "Counseling families dealing with abuse or neglect",
                "trait_tags": {"Social-Work": 1.0, "Counseling": 0.8, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.4, "Teaching-Ed": 0.25}
            },
            {
                "option_id": 2922,
                "option_text": "Connecting underprivileged families to government aid programs",
                "trait_tags": {"Social-Work": 1.0, "Community-Serve": 0.8, "Social": 0.45, "People-Skill": 0.45, "Counseling": 0.3, "Teaching-Ed": 0.25}
            },
            {
                "option_id": 2923,
                "option_text": "Working with street children and youth at risk",
                "trait_tags": {"Social-Work": 1.0, "People-Skill": 0.8, "Social": 0.45, "Community-Serve": 0.4, "Teaching-Ed": 0.32, "Patient-Care": 0.32}
            },
            {
                "option_id": 2924,
                "option_text": "Advocating for policy changes to reduce poverty",
                "trait_tags": {"Social-Work": 1.0, "Legal-Practice": 0.8, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.4, "Counseling": 0.3}
            },
            {
                "option_id": 2925,
                "option_text": "Running rehabilitation programs for substance abuse",
                "trait_tags": {"Social-Work": 1.0, "Rehab-Therapy": 0.8, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.4, "Physical-Skill": 0.32}
            },
            {
                "option_id": 2926,
                "option_text": "Organizing livelihood programs for displaced workers",
                "trait_tags": {"Social-Work": 1.0, "Startup-Venture": 0.8, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.4, "Enterprising": 0.36}
            },
            {
                "option_id": 2927,
                "option_text": "Supporting elderly care and senior citizen welfare",
                "trait_tags": {"Social-Work": 1.0, "Patient-Care": 0.8, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.4, "Counseling": 0.3}
            },
            {
                "option_id": 2928,
                "option_text": "Crisis intervention during disasters and emergencies",
                "trait_tags": {"Social-Work": 1.0, "Community-Serve": 0.8, "Social": 0.45, "People-Skill": 0.45, "Counseling": 0.3, "Teaching-Ed": 0.25}
            }
        ]
    },
    {
        "question_id": 293,
        "question_text": "SCENARIO: A family is about to be evicted from their home. As a social worker, what do you do first?",
        "category": "Situational - Social Work",
        "options": [
            {
                "option_id": 2931,
                "option_text": "Assess the family's immediate needs and provide emotional support",
                "trait_tags": {"Social-Work": 1.0, "Counseling": 0.8, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.4, "Teaching-Ed": 0.25}
            },
            {
                "option_id": 2932,
                "option_text": "Connect them with legal aid for tenant rights",
                "trait_tags": {"Social-Work": 1.0, "Legal-Practice": 0.8, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.4, "Counseling": 0.3}
            },
            {
                "option_id": 2933,
                "option_text": "Find temporary housing or shelter options",
                "trait_tags": {"Social-Work": 1.0, "Community-Serve": 0.8, "Social": 0.45, "People-Skill": 0.45, "Counseling": 0.3, "Teaching-Ed": 0.25}
            },
            {
                "option_id": 2934,
                "option_text": "Help them apply for government financial assistance",
                "trait_tags": {"Social-Work": 1.0, "Admin-Skill": 0.8, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.4, "Conventional": 0.36}
            },
            {
                "option_id": 2935,
                "option_text": "Coordinate with the barangay for community support",
                "trait_tags": {"Social-Work": 1.0, "People-Skill": 0.8, "Social": 0.45, "Community-Serve": 0.4, "Teaching-Ed": 0.32, "Patient-Care": 0.32}
            },
            {
                "option_id": 2936,
                "option_text": "Help the parents find employment opportunities",
                "trait_tags": {"Social-Work": 1.0, "HR-Management": 0.8, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.4, "Counseling": 0.3}
            },
            {
                "option_id": 2937,
                "option_text": "Ensure the children can continue attending school",
                "trait_tags": {"Social-Work": 1.0, "Teaching-Ed": 0.8, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.4, "Counseling": 0.3}
            },
            {
                "option_id": 2938,
                "option_text": "Document the case for DSWD follow-up",
                "trait_tags": {"Social-Work": 1.0, "Admin-Skill": 0.8, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.4, "Conventional": 0.36}
            }
        ]
    },
    {
        "question_id": 294,
        "question_text": "What aspect of food science and technology excites you most?",
        "category": "Domain - Food Science",
        "options": [
            {
                "option_id": 2941,
                "option_text": "Developing new food products and flavors",
                "trait_tags": {"Food-Science": 1.0, "Creative-Skill": 0.8, "Investigative": 0.4, "Artistic": 0.36, "Lab-Research": 0.35, "Nutrition-Diet": 0.35}
            },
            {
                "option_id": 2942,
                "option_text": "Testing food for safety and quality in a laboratory",
                "trait_tags": {"Food-Science": 1.0, "Lab-Research": 0.8, "Investigative": 0.4, "Analytical-Skill": 0.36, "Nutrition-Diet": 0.35, "Medical-Lab": 0.24}
            },
            {
                "option_id": 2943,
                "option_text": "Learning how food is preserved and processed industrially",
                "trait_tags": {"Food-Science": 1.0, "Industrial-Ops": 0.8, "Investigative": 0.4, "Lab-Research": 0.35, "Nutrition-Diet": 0.35, "Analytical-Skill": 0.3}
            },
            {
                "option_id": 2944,
                "option_text": "Understanding the chemistry behind cooking and baking",
                "trait_tags": {"Food-Science": 1.0, "Lab-Research": 0.8, "Investigative": 0.4, "Analytical-Skill": 0.36, "Nutrition-Diet": 0.35, "Medical-Lab": 0.24}
            },
            {
                "option_id": 2945,
                "option_text": "Ensuring food products meet FDA and DOH standards",
                "trait_tags": {"Food-Science": 1.0, "Admin-Skill": 0.8, "Investigative": 0.4, "Conventional": 0.36, "Lab-Research": 0.35, "Nutrition-Diet": 0.35}
            },
            {
                "option_id": 2946,
                "option_text": "Studying nutrition labels and dietary guidelines",
                "trait_tags": {"Food-Science": 1.0, "Nutrition-Diet": 0.8, "Investigative": 0.4, "Lab-Research": 0.35, "Analytical-Skill": 0.3, "Social": 0.24}
            },
            {
                "option_id": 2947,
                "option_text": "Running a food manufacturing or packaging company",
                "trait_tags": {"Food-Science": 1.0, "Startup-Venture": 0.8, "Investigative": 0.4, "Enterprising": 0.36, "Lab-Research": 0.35, "Nutrition-Diet": 0.35}
            },
            {
                "option_id": 2948,
                "option_text": "Researching food allergies and intolerances",
                "trait_tags": {"Food-Science": 1.0, "Medical-Lab": 0.8, "Investigative": 0.4, "Analytical-Skill": 0.36, "Lab-Research": 0.35, "Nutrition-Diet": 0.35}
            }
        ]
    },
    {
        "question_id": 295,
        "question_text": "SCENARIO: A new hospital is being built in your town. Which department would you want to work in?",
        "category": "Situational - Hospital Dept",
        "options": [
            {
                "option_id": 2951,
                "option_text": "The pharmacy - dispensing and managing medications",
                "trait_tags": {"Pharmacy": 1.0, "Patient-Care": 0.8, "Investigative": 0.4, "Analytical-Skill": 0.4, "People-Skill": 0.36, "Medical-Lab": 0.35}
            },
            {
                "option_id": 2952,
                "option_text": "Health Information Management - digitalizing patient records",
                "trait_tags": {"Health-Admin": 1.0, "Software-Dev": 0.8, "Admin-Skill": 0.45, "Conventional": 0.4, "Technical-Skill": 0.36, "Investigative": 0.32}
            },
            {
                "option_id": 2953,
                "option_text": "Human Resources - hiring doctors, nurses, and staff",
                "trait_tags": {"HR-Management": 1.0, "People-Skill": 0.8, "Social": 0.36, "Enterprising": 0.35, "Admin-Skill": 0.35, "Teaching-Ed": 0.32}
            },
            {
                "option_id": 2954,
                "option_text": "The forensic laboratory - analyzing evidence for police cases",
                "trait_tags": {"Forensic-Sci": 1.0, "Lab-Research": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.4, "Law-Enforce": 0.35, "Medical-Lab": 0.24}
            },
            {
                "option_id": 2955,
                "option_text": "The nutrition department - planning patient meal programs",
                "trait_tags": {"Nutrition-Diet": 1.0, "Food-Science": 0.8, "Investigative": 0.32, "Social": 0.3, "Analytical-Skill": 0.3, "Lab-Research": 0.28}
            },
            {
                "option_id": 2956,
                "option_text": "The emergency room - treating patients in critical condition",
                "trait_tags": {"Patient-Care": 1.0, "Physical-Skill": 0.8, "People-Skill": 0.45, "Social": 0.4, "Realistic": 0.32, "Rehab-Therapy": 0.3}
            },
            {
                "option_id": 2957,
                "option_text": "The rehabilitation center - helping patients recover",
                "trait_tags": {"Rehab-Therapy": 1.0, "People-Skill": 0.8, "Physical-Skill": 0.4, "Social": 0.36, "Patient-Care": 0.32, "Teaching-Ed": 0.32}
            },
            {
                "option_id": 2958,
                "option_text": "Administration - managing hospital operations and budgets",
                "trait_tags": {"Health-Admin": 1.0, "Finance-Acct": 0.8, "Admin-Skill": 0.45, "Conventional": 0.4, "Analytical-Skill": 0.32, "Startup-Venture": 0.16}
            }
        ]
    },
    {
        "question_id": 296,
        "question_text": "Which Philippine industry trend do you find most promising for your future career?",
        "category": "PH Industry Trends",
        "options": [
            {
                "option_id": 2961,
                "option_text": "Growing demand for pharmacists in drugstore chains (Mercury, Watsons)",
                "trait_tags": {"Pharmacy": 1.0, "Marketing-Sales": 0.8, "Investigative": 0.4, "Analytical-Skill": 0.4, "Enterprising": 0.36, "Medical-Lab": 0.35}
            },
            {
                "option_id": 2962,
                "option_text": "Digital health records mandated by PhilHealth",
                "trait_tags": {"Health-Admin": 1.0, "Software-Dev": 0.8, "Admin-Skill": 0.45, "Conventional": 0.4, "Technical-Skill": 0.36, "Investigative": 0.32}
            },
            {
                "option_id": 2963,
                "option_text": "BPO companies needing HR professionals",
                "trait_tags": {"HR-Management": 1.0, "People-Skill": 0.8, "Social": 0.36, "Enterprising": 0.35, "Admin-Skill": 0.35, "Teaching-Ed": 0.32}
            },
            {
                "option_id": 2964,
                "option_text": "NBI and PNP investing in forensic laboratories",
                "trait_tags": {"Forensic-Sci": 1.0, "Law-Enforce": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.4, "Lab-Research": 0.35, "Realistic": 0.28}
            },
            {
                "option_id": 2965,
                "option_text": "Philippines becoming a top tourist destination in Asia",
                "trait_tags": {"Tourism-Travel": 1.0, "Hospitality-Svc": 0.8, "People-Skill": 0.4, "Enterprising": 0.35, "Marketing-Sales": 0.25, "Culinary-Arts": 0.24}
            },
            {
                "option_id": 2966,
                "option_text": "DSWD expanding social welfare programs nationwide",
                "trait_tags": {"Social-Work": 1.0, "Community-Serve": 0.8, "Social": 0.45, "People-Skill": 0.45, "Counseling": 0.3, "Teaching-Ed": 0.25}
            },
            {
                "option_id": 2967,
                "option_text": "FDA requiring more food safety testing for local products",
                "trait_tags": {"Food-Science": 1.0, "Lab-Research": 0.8, "Investigative": 0.4, "Analytical-Skill": 0.36, "Nutrition-Diet": 0.35, "Medical-Lab": 0.24}
            },
            {
                "option_id": 2968,
                "option_text": "Telemedicine and online healthcare consultations growing",
                "trait_tags": {"Health-Admin": 1.0, "Software-Dev": 0.8, "Admin-Skill": 0.45, "Conventional": 0.4, "Technical-Skill": 0.36, "Investigative": 0.32}
            }
        ]
    },
    {
        "question_id": 297,
        "question_text": "If you could shadow a professional for a week, which would you pick?",
        "category": "Career Shadow Extended",
        "options": [
            {
                "option_id": 2971,
                "option_text": "A pharmacist at a busy hospital pharmacy",
                "trait_tags": {"Pharmacy": 1.0, "Patient-Care": 0.8, "Investigative": 0.4, "Analytical-Skill": 0.4, "People-Skill": 0.36, "Medical-Lab": 0.35}
            },
            {
                "option_id": 2972,
                "option_text": "A health IT specialist managing hospital systems",
                "trait_tags": {"Health-Admin": 1.0, "Software-Dev": 0.8, "Admin-Skill": 0.45, "Conventional": 0.4, "Technical-Skill": 0.36, "Investigative": 0.32}
            },
            {
                "option_id": 2973,
                "option_text": "An HR director at a major corporation",
                "trait_tags": {"HR-Management": 1.0, "Admin-Skill": 0.8, "People-Skill": 0.4, "Conventional": 0.36, "Social": 0.35, "Enterprising": 0.35}
            },
            {
                "option_id": 2974,
                "option_text": "A forensic scientist at the NBI crime lab",
                "trait_tags": {"Forensic-Sci": 1.0, "Lab-Research": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.4, "Law-Enforce": 0.35, "Medical-Lab": 0.24}
            },
            {
                "option_id": 2975,
                "option_text": "A tourism officer at the Department of Tourism",
                "trait_tags": {"Tourism-Travel": 1.0, "Community-Serve": 0.8, "People-Skill": 0.4, "Hospitality-Svc": 0.4, "Social": 0.36, "Enterprising": 0.35}
            },
            {
                "option_id": 2976,
                "option_text": "A social worker at DSWD helping families",
                "trait_tags": {"Social-Work": 1.0, "People-Skill": 0.8, "Social": 0.45, "Community-Serve": 0.4, "Teaching-Ed": 0.32, "Patient-Care": 0.32}
            },
            {
                "option_id": 2977,
                "option_text": "A food scientist at a manufacturing company",
                "trait_tags": {"Food-Science": 1.0, "Lab-Research": 0.8, "Investigative": 0.4, "Analytical-Skill": 0.36, "Nutrition-Diet": 0.35, "Medical-Lab": 0.24}
            },
            {
                "option_id": 2978,
                "option_text": "A nutritionist at a fitness center or hospital",
                "trait_tags": {"Nutrition-Diet": 1.0, "Patient-Care": 0.8, "People-Skill": 0.36, "Food-Science": 0.35, "Social": 0.32, "Analytical-Skill": 0.3}
            }
        ]
    },
    {
        "question_id": 298,
        "question_text": "SCENARIO: Your school cafeteria had a food poisoning outbreak. How would you help investigate?",
        "category": "Situational - Food Safety",
        "options": [
            {
                "option_id": 2981,
                "option_text": "Collect food samples and test them in the laboratory",
                "trait_tags": {"Food-Science": 1.0, "Lab-Research": 0.8, "Investigative": 0.4, "Analytical-Skill": 0.36, "Nutrition-Diet": 0.35, "Medical-Lab": 0.24}
            },
            {
                "option_id": 2982,
                "option_text": "Check if proper food handling procedures were followed",
                "trait_tags": {"Food-Science": 1.0, "Admin-Skill": 0.8, "Investigative": 0.4, "Conventional": 0.36, "Lab-Research": 0.35, "Nutrition-Diet": 0.35}
            },
            {
                "option_id": 2983,
                "option_text": "Treat students who got sick and monitor symptoms",
                "trait_tags": {"Patient-Care": 1.0, "Medical-Lab": 0.8, "People-Skill": 0.45, "Social": 0.4, "Analytical-Skill": 0.36, "Investigative": 0.32}
            },
            {
                "option_id": 2984,
                "option_text": "Interview cafeteria staff about food preparation",
                "trait_tags": {"Forensic-Sci": 1.0, "People-Skill": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.4, "Social": 0.36, "Lab-Research": 0.35}
            },
            {
                "option_id": 2985,
                "option_text": "Review supplier records and ingredient sources",
                "trait_tags": {"Food-Science": 1.0, "Finance-Acct": 0.8, "Investigative": 0.4, "Conventional": 0.36, "Lab-Research": 0.35, "Nutrition-Diet": 0.35}
            },
            {
                "option_id": 2986,
                "option_text": "Check if the cafeteria has proper DOH permits",
                "trait_tags": {"Health-Admin": 1.0, "Admin-Skill": 0.8, "Conventional": 0.4, "Finance-Acct": 0.24, "Hospitality-Svc": 0.16, "Patient-Care": 0.15}
            },
            {
                "option_id": 2987,
                "option_text": "Create a report to prevent future incidents",
                "trait_tags": {"Food-Science": 1.0, "Analytical-Skill": 0.8, "Investigative": 0.4, "Lab-Research": 0.35, "Nutrition-Diet": 0.35, "Data-Analytics": 0.32}
            },
            {
                "option_id": 2988,
                "option_text": "Coordinate with the local health office for proper investigation",
                "trait_tags": {"Health-Admin": 1.0, "Community-Serve": 0.8, "Admin-Skill": 0.45, "Conventional": 0.4, "Social": 0.36, "People-Skill": 0.32}
            }
        ]
    },
    {
        "question_id": 299,
        "question_text": "Which work environment would make you happiest?",
        "category": "Work Environment Extended",
        "options": [
            {
                "option_id": 2991,
                "option_text": "A clean pharmaceutical lab developing medicines",
                "trait_tags": {"Pharmacy": 1.0, "Lab-Research": 0.8, "Investigative": 0.4, "Analytical-Skill": 0.4, "Medical-Lab": 0.35, "Patient-Care": 0.25}
            },
            {
                "option_id": 2992,
                "option_text": "A hospital records office with digital health systems",
                "trait_tags": {"Health-Admin": 1.0, "Admin-Skill": 0.8, "Conventional": 0.4, "Finance-Acct": 0.24, "Hospitality-Svc": 0.16, "Patient-Care": 0.15}
            },
            {
                "option_id": 2993,
                "option_text": "A corporate HR office interviewing and training employees",
                "trait_tags": {"HR-Management": 1.0, "People-Skill": 0.8, "Social": 0.36, "Enterprising": 0.35, "Admin-Skill": 0.35, "Teaching-Ed": 0.32}
            },
            {
                "option_id": 2994,
                "option_text": "A forensic crime lab analyzing evidence",
                "trait_tags": {"Forensic-Sci": 1.0, "Lab-Research": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.4, "Law-Enforce": 0.35, "Medical-Lab": 0.24}
            },
            {
                "option_id": 2995,
                "option_text": "A travel agency or tourist information center",
                "trait_tags": {"Tourism-Travel": 1.0, "Hospitality-Svc": 0.8, "People-Skill": 0.4, "Enterprising": 0.35, "Marketing-Sales": 0.25, "Culinary-Arts": 0.24}
            },
            {
                "option_id": 2996,
                "option_text": "A DSWD field office helping communities",
                "trait_tags": {"Social-Work": 1.0, "Community-Serve": 0.8, "Social": 0.45, "People-Skill": 0.45, "Counseling": 0.3, "Teaching-Ed": 0.25}
            },
            {
                "option_id": 2997,
                "option_text": "A food processing plant ensuring quality standards",
                "trait_tags": {"Food-Science": 1.0, "Industrial-Ops": 0.8, "Investigative": 0.4, "Lab-Research": 0.35, "Nutrition-Diet": 0.35, "Analytical-Skill": 0.3}
            },
            {
                "option_id": 2998,
                "option_text": "A beautiful resort or hotel welcoming guests",
                "trait_tags": {"Tourism-Travel": 1.0, "Hospitality-Svc": 0.8, "People-Skill": 0.4, "Enterprising": 0.35, "Marketing-Sales": 0.25, "Culinary-Arts": 0.24}
            }
        ]
    },
    {
        "question_id": 300,
        "question_text": "SCENARIO: A new government policy requires all businesses to have trained HR staff. What appeals to you about this field?",
        "category": "Situational - HR Policy",
        "options": [
            {
                "option_id": 3001,
                "option_text": "Ensuring fair hiring practices and equal opportunity",
                "trait_tags": {"HR-Management": 1.0, "Legal-Practice": 0.8, "People-Skill": 0.4, "Social": 0.35, "Enterprising": 0.35, "Admin-Skill": 0.35}
            },
            {
                "option_id": 3002,
                "option_text": "Building employee wellness and mental health programs",
                "trait_tags": {"HR-Management": 1.0, "Counseling": 0.8, "People-Skill": 0.4, "Social": 0.36, "Enterprising": 0.35, "Admin-Skill": 0.35}
            },
            {
                "option_id": 3003,
                "option_text": "Managing employee benefits and insurance",
                "trait_tags": {"HR-Management": 1.0, "Finance-Acct": 0.8, "People-Skill": 0.4, "Conventional": 0.36, "Social": 0.35, "Enterprising": 0.35}
            },
            {
                "option_id": 3004,
                "option_text": "Creating onboarding and orientation programs",
                "trait_tags": {"HR-Management": 1.0, "Teaching-Ed": 0.8, "People-Skill": 0.4, "Social": 0.36, "Enterprising": 0.35, "Admin-Skill": 0.35}
            },
            {
                "option_id": 3005,
                "option_text": "Handling workplace safety and OSHA compliance",
                "trait_tags": {"HR-Management": 1.0, "Admin-Skill": 0.8, "People-Skill": 0.4, "Conventional": 0.36, "Social": 0.35, "Enterprising": 0.35}
            },
            {
                "option_id": 3006,
                "option_text": "Conducting employee satisfaction surveys and analysis",
                "trait_tags": {"HR-Management": 1.0, "Data-Analytics": 0.8, "People-Skill": 0.4, "Investigative": 0.36, "Analytical-Skill": 0.36, "Social": 0.35}
            },
            {
                "option_id": 3007,
                "option_text": "Developing diversity and inclusion initiatives",
                "trait_tags": {"HR-Management": 1.0, "Community-Serve": 0.8, "People-Skill": 0.4, "Social": 0.36, "Enterprising": 0.35, "Admin-Skill": 0.35}
            },
            {
                "option_id": 3008,
                "option_text": "Implementing HR software and automation tools",
                "trait_tags": {"HR-Management": 1.0, "Software-Dev": 0.8, "People-Skill": 0.4, "Technical-Skill": 0.36, "Social": 0.35, "Enterprising": 0.35}
            }
        ]
    },
    {
        "question_id": 301,
        "question_text": "Which board exam or certification would you prepare for?",
        "category": "Licensure Extended",
        "options": [
            {
                "option_id": 3011,
                "option_text": "Pharmacy Licensure Exam",
                "trait_tags": {"Pharmacy": 1.0, "Medical-Lab": 0.8, "Investigative": 0.4, "Analytical-Skill": 0.4, "Lab-Research": 0.28, "Patient-Care": 0.25}
            },
            {
                "option_id": 3012,
                "option_text": "Registered Health Information Administrator (RHIA)",
                "trait_tags": {"Health-Admin": 1.0, "Admin-Skill": 0.8, "Conventional": 0.4, "Finance-Acct": 0.24, "Hospitality-Svc": 0.16, "Patient-Care": 0.15}
            },
            {
                "option_id": 3013,
                "option_text": "Professional in Human Resources (PHR)",
                "trait_tags": {"HR-Management": 1.0, "Admin-Skill": 0.8, "People-Skill": 0.4, "Conventional": 0.36, "Social": 0.35, "Enterprising": 0.35}
            },
            {
                "option_id": 3014,
                "option_text": "Forensic Science Board Exam",
                "trait_tags": {"Forensic-Sci": 1.0, "Lab-Research": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.4, "Law-Enforce": 0.35, "Medical-Lab": 0.24}
            },
            {
                "option_id": 3015,
                "option_text": "Tourism Professional Certification",
                "trait_tags": {"Tourism-Travel": 1.0, "Hospitality-Svc": 0.8, "People-Skill": 0.4, "Enterprising": 0.35, "Marketing-Sales": 0.25, "Culinary-Arts": 0.24}
            },
            {
                "option_id": 3016,
                "option_text": "Registered Social Worker Licensure",
                "trait_tags": {"Social-Work": 1.0, "Community-Serve": 0.8, "Social": 0.45, "People-Skill": 0.45, "Counseling": 0.3, "Teaching-Ed": 0.25}
            },
            {
                "option_id": 3017,
                "option_text": "Food Technologist Board Exam",
                "trait_tags": {"Food-Science": 1.0, "Lab-Research": 0.8, "Investigative": 0.4, "Analytical-Skill": 0.36, "Nutrition-Diet": 0.35, "Medical-Lab": 0.24}
            },
            {
                "option_id": 3018,
                "option_text": "Registered Nutritionist-Dietitian Exam",
                "trait_tags": {"Nutrition-Diet": 1.0, "Patient-Care": 0.8, "People-Skill": 0.36, "Food-Science": 0.35, "Social": 0.32, "Analytical-Skill": 0.3}
            }
        ]
    },
    {
        "question_id": 302,
        "question_text": "SCENARIO: Your LGU wants to attract more tourists to your town. What project would you lead?",
        "category": "Situational - Local Tourism",
        "options": [
            {
                "option_id": 3021,
                "option_text": "Create a heritage walking tour showcasing historical sites",
                "trait_tags": {"Tourism-Travel": 1.0, "Teaching-Ed": 0.8, "People-Skill": 0.4, "Hospitality-Svc": 0.4, "Social": 0.36, "Enterprising": 0.35}
            },
            {
                "option_id": 3022,
                "option_text": "Develop a food tourism trail featuring local delicacies",
                "trait_tags": {"Tourism-Travel": 1.0, "Culinary-Arts": 0.8, "People-Skill": 0.4, "Hospitality-Svc": 0.4, "Enterprising": 0.35, "Creative-Skill": 0.28}
            },
            {
                "option_id": 3023,
                "option_text": "Build a tourism center with maps and information booths",
                "trait_tags": {"Tourism-Travel": 1.0, "Admin-Skill": 0.8, "People-Skill": 0.4, "Hospitality-Svc": 0.4, "Conventional": 0.36, "Enterprising": 0.35}
            },
            {
                "option_id": 3024,
                "option_text": "Certify local accommodations for quality standards",
                "trait_tags": {"Tourism-Travel": 1.0, "Hospitality-Svc": 0.8, "People-Skill": 0.4, "Enterprising": 0.35, "Marketing-Sales": 0.25, "Culinary-Arts": 0.24}
            },
            {
                "option_id": 3025,
                "option_text": "Launch social media campaigns showing scenic spots",
                "trait_tags": {"Tourism-Travel": 1.0, "Digital-Media": 0.8, "People-Skill": 0.4, "Hospitality-Svc": 0.4, "Enterprising": 0.35, "Artistic": 0.32}
            },
            {
                "option_id": 3026,
                "option_text": "Partner with travel agencies for package deals",
                "trait_tags": {"Tourism-Travel": 1.0, "Marketing-Sales": 0.8, "People-Skill": 0.4, "Hospitality-Svc": 0.4, "Enterprising": 0.36, "Startup-Venture": 0.24}
            },
            {
                "option_id": 3027,
                "option_text": "Train locals in hospitality and customer service",
                "trait_tags": {"Tourism-Travel": 1.0, "Teaching-Ed": 0.8, "People-Skill": 0.4, "Hospitality-Svc": 0.4, "Social": 0.36, "Enterprising": 0.35}
            },
            {
                "option_id": 3028,
                "option_text": "Develop sustainable eco-tourism activities",
                "trait_tags": {"Tourism-Travel": 1.0, "Environmental-Sci": 0.8, "People-Skill": 0.4, "Hospitality-Svc": 0.4, "Investigative": 0.36, "Enterprising": 0.35}
            }
        ]
    },
    {
        "question_id": 303,
        "question_text": "SCENARIO: A suspicious death occurs and police need scientific help. What forensic role would you take?",
        "category": "Situational - Forensic Investigation",
        "options": [
            {
                "option_id": 3031,
                "option_text": "Toxicology analysis to check for poisoning",
                "trait_tags": {"Forensic-Sci": 1.0, "Pharmacy": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.4, "Lab-Research": 0.35, "Law-Enforce": 0.35}
            },
            {
                "option_id": 3032,
                "option_text": "DNA profiling to identify the victim and suspects",
                "trait_tags": {"Forensic-Sci": 1.0, "Lab-Research": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.4, "Law-Enforce": 0.35, "Medical-Lab": 0.24}
            },
            {
                "option_id": 3033,
                "option_text": "Digital forensics examining computers and phones",
                "trait_tags": {"Forensic-Sci": 1.0, "Cyber-Defense": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.4, "Lab-Research": 0.35, "Law-Enforce": 0.35}
            },
            {
                "option_id": 3034,
                "option_text": "Blood pattern analysis at the scene",
                "trait_tags": {"Forensic-Sci": 1.0, "Medical-Lab": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.4, "Lab-Research": 0.35, "Law-Enforce": 0.35}
            },
            {
                "option_id": 3035,
                "option_text": "Document analysis to check for forged records",
                "trait_tags": {"Forensic-Sci": 1.0, "Analytical-Skill": 0.8, "Investigative": 0.45, "Lab-Research": 0.35, "Law-Enforce": 0.35, "Data-Analytics": 0.32}
            },
            {
                "option_id": 3036,
                "option_text": "Ballistics testing on recovered firearms",
                "trait_tags": {"Forensic-Sci": 1.0, "Law-Enforce": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.4, "Lab-Research": 0.35, "Realistic": 0.28}
            },
            {
                "option_id": 3037,
                "option_text": "Crime scene photography and evidence cataloging",
                "trait_tags": {"Forensic-Sci": 1.0, "Digital-Media": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.4, "Lab-Research": 0.35, "Law-Enforce": 0.35}
            },
            {
                "option_id": 3038,
                "option_text": "Psychological profiling of the suspect",
                "trait_tags": {"Forensic-Sci": 1.0, "Counseling": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.4, "Social": 0.36, "People-Skill": 0.36}
            }
        ]
    },
    {
        "question_id": 304,
        "question_text": "SCENARIO: An abandoned child is found at the barangay hall. As a social worker, what steps do you take?",
        "category": "Situational - Child Welfare",
        "options": [
            {
                "option_id": 3041,
                "option_text": "Ensure the child's immediate safety and basic needs",
                "trait_tags": {"Social-Work": 1.0, "Patient-Care": 0.8, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.4, "Counseling": 0.3}
            },
            {
                "option_id": 3042,
                "option_text": "Coordinate with DSWD for proper custody procedures",
                "trait_tags": {"Social-Work": 1.0, "Admin-Skill": 0.8, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.4, "Conventional": 0.36}
            },
            {
                "option_id": 3043,
                "option_text": "Counsel the child and assess their emotional state",
                "trait_tags": {"Social-Work": 1.0, "Counseling": 0.8, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.4, "Teaching-Ed": 0.25}
            },
            {
                "option_id": 3044,
                "option_text": "Investigate to find the child's parents or relatives",
                "trait_tags": {"Social-Work": 1.0, "Law-Enforce": 0.8, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.4, "Counseling": 0.3}
            },
            {
                "option_id": 3045,
                "option_text": "Arrange temporary foster care placement",
                "trait_tags": {"Social-Work": 1.0, "Community-Serve": 0.8, "Social": 0.45, "People-Skill": 0.45, "Counseling": 0.3, "Teaching-Ed": 0.25}
            },
            {
                "option_id": 3046,
                "option_text": "Document the case for legal proceedings",
                "trait_tags": {"Social-Work": 1.0, "Legal-Practice": 0.8, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.4, "Counseling": 0.3}
            },
            {
                "option_id": 3047,
                "option_text": "Ensure the child gets medical check-up and vaccinations",
                "trait_tags": {"Social-Work": 1.0, "Patient-Care": 0.8, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.4, "Counseling": 0.3}
            },
            {
                "option_id": 3048,
                "option_text": "Connect the child with educational support services",
                "trait_tags": {"Social-Work": 1.0, "Teaching-Ed": 0.8, "Social": 0.45, "People-Skill": 0.45, "Community-Serve": 0.4, "Counseling": 0.3}
            }
        ]
    },
    {
        "question_id": 305,
        "question_text": "What food industry career interests you most?",
        "category": "Career - Food Science",
        "options": [
            {
                "option_id": 3051,
                "option_text": "Food scientist developing new products for companies like Jollibee or Monde",
                "trait_tags": {"Food-Science": 1.0, "Creative-Skill": 0.8, "Investigative": 0.4, "Artistic": 0.36, "Lab-Research": 0.35, "Nutrition-Diet": 0.35}
            },
            {
                "option_id": 3052,
                "option_text": "Quality control inspector at a food manufacturing plant",
                "trait_tags": {"Food-Science": 1.0, "Analytical-Skill": 0.8, "Investigative": 0.4, "Lab-Research": 0.35, "Nutrition-Diet": 0.35, "Data-Analytics": 0.32}
            },
            {
                "option_id": 3053,
                "option_text": "Food safety officer for FDA Philippines",
                "trait_tags": {"Food-Science": 1.0, "Admin-Skill": 0.8, "Investigative": 0.4, "Conventional": 0.36, "Lab-Research": 0.35, "Nutrition-Diet": 0.35}
            },
            {
                "option_id": 3054,
                "option_text": "Research and development chef combining science and cooking",
                "trait_tags": {"Food-Science": 1.0, "Culinary-Arts": 0.8, "Investigative": 0.4, "Lab-Research": 0.35, "Nutrition-Diet": 0.35, "Analytical-Skill": 0.3}
            },
            {
                "option_id": 3055,
                "option_text": "Food packaging engineer designing shelf-stable products",
                "trait_tags": {"Food-Science": 1.0, "Industrial-Ops": 0.8, "Investigative": 0.4, "Lab-Research": 0.35, "Nutrition-Diet": 0.35, "Analytical-Skill": 0.3}
            },
            {
                "option_id": 3056,
                "option_text": "Microbiologist testing food for bacteria and contamination",
                "trait_tags": {"Food-Science": 1.0, "Lab-Research": 0.8, "Investigative": 0.4, "Analytical-Skill": 0.36, "Nutrition-Diet": 0.35, "Medical-Lab": 0.24}
            },
            {
                "option_id": 3057,
                "option_text": "Sensory evaluator testing taste, texture, and appearance",
                "trait_tags": {"Food-Science": 1.0, "Analytical-Skill": 0.8, "Investigative": 0.4, "Lab-Research": 0.35, "Nutrition-Diet": 0.35, "Data-Analytics": 0.32}
            },
            {
                "option_id": 3058,
                "option_text": "Food supply chain manager for a grocery chain",
                "trait_tags": {"Food-Science": 1.0, "Admin-Skill": 0.8, "Investigative": 0.4, "Conventional": 0.36, "Lab-Research": 0.35, "Nutrition-Diet": 0.35}
            }
        ]
    },
    {
        "question_id": 306,
        "question_text": "What kind of complex problem-solving excites you the most?",
        "category": "Engineering CS - Problem Solving",
        "options": [
            {
                "option_id": 3059,
                "option_text": "Designing algorithms to optimize software performance",
                "trait_tags": {"Software-Dev": 1.0, "Data-Analytics": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Analytical-Skill": 0.36, "Cyber-Defense": 0.25}
            },
            {
                "option_id": 3060,
                "option_text": "Calculating structural loads for a high-rise bridge",
                "trait_tags": {"Civil-Build": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Industrial-Ops": 0.2}
            },
            {
                "option_id": 3061,
                "option_text": "Developing high-speed circuitry for computer processors",
                "trait_tags": {"Hardware-Systems": 1.0, "Electrical-Power": 0.8, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Mechanical-Design": 0.25}
            },
            {
                "option_id": 3062,
                "option_text": "Analyzing flight dynamics and wing lift for a new jet",
                "trait_tags": {"Aeronautical-Eng": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.36, "Technical-Skill": 0.32, "Industrial-Ops": 0.2, "Civil-Build": 0.16}
            },
            {
                "option_id": 3063,
                "option_text": "Creating a mathematical model to predict market trends",
                "trait_tags": {"Data-Analytics": 1.0, "Software-Dev": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Technical-Skill": 0.36, "Lab-Research": 0.25}
            },
            {
                "option_id": 3064,
                "option_text": "Designing a more efficient internal combustion engine",
                "trait_tags": {"Mechanical-Design": 1.0, "Aeronautical-Eng": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Industrial-Ops": 0.25, "Civil-Build": 0.2}
            },
            {
                "option_id": 3065,
                "option_text": "Planning a city-wide smart electrical grid",
                "trait_tags": {"Electrical-Power": 1.0, "Electronics-Dev": 0.8, "Civil-Build": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3}
            },
            {
                "option_id": 3066,
                "option_text": "Troubleshooting signal interference in a 5G network",
                "trait_tags": {"Electronics-Dev": 1.0, "Hardware-Systems": 0.8, "Technical-Skill": 0.36, "Realistic": 0.32, "Electrical-Power": 0.24, "Mechanical-Design": 0.2}
            }
        ]
    },
    {
        "question_id": 307,
        "question_text": "If you were part of a team building a 'Smart City,' what would be your role?",
        "category": "Engineering CS - Smart City",
        "options": [
            {
                "option_id": 3067,
                "option_text": "Writing the central OS that runs the city's automation",
                "trait_tags": {"Software-Dev": 1.0, "Hardware-Systems": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Realistic": 0.32, "Data-Analytics": 0.3}
            },
            {
                "option_id": 3068,
                "option_text": "Ensuring the structural integrity of the roads and tunnels",
                "trait_tags": {"Civil-Build": 1.0, "Spatial-Design": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Artistic": 0.28, "Creative-Skill": 0.28}
            },
            {
                "option_id": 3069,
                "option_text": "Designing the physical sensors and embedded hardware",
                "trait_tags": {"Hardware-Systems": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Electrical-Power": 0.3, "Mechanical-Design": 0.25}
            },
            {
                "option_id": 3070,
                "option_text": "Managing the power distribution and high-voltage lines",
                "trait_tags": {"Electrical-Power": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3071,
                "option_text": "Analyzing the 'Big Data' collected from millions of citizens",
                "trait_tags": {"Data-Analytics": 1.0, "Software-Dev": 0.8, "AI-ML": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Technical-Skill": 0.36}
            },
            {
                "option_id": 3072,
                "option_text": "Creating the mechanical systems for automated public transit",
                "trait_tags": {"Mechanical-Design": 1.0, "Industrial-Ops": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Analytical-Skill": 0.28, "Enterprising": 0.24}
            },
            {
                "option_id": 3073,
                "option_text": "Developing the communication systems for city-wide Wi-Fi",
                "trait_tags": {"Electronics-Dev": 1.0, "Hardware-Systems": 0.8, "Technical-Skill": 0.36, "Realistic": 0.32, "Electrical-Power": 0.24, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3074,
                "option_text": "Designing drone-based delivery systems for the city",
                "trait_tags": {"Aeronautical-Eng": 1.0, "Mechanical-Design": 0.8, "Electronics-Dev": 0.8, "Realistic": 0.36, "Technical-Skill": 0.32, "Industrial-Ops": 0.2}
            }
        ]
    },
    {
        "question_id": 308,
        "question_text": "Which specialized tool or environment would you prefer to master?",
        "category": "Engineering CS - Tools",
        "options": [
            {
                "option_id": 3075,
                "option_text": "An Integrated Development Environment (IDE) like VS Code",
                "trait_tags": {"Software-Dev": 1.0, "Web-Dev": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25}
            },
            {
                "option_id": 3076,
                "option_text": "Computer-Aided Design (CAD) for structural blueprints",
                "trait_tags": {"Civil-Build": 1.0, "Spatial-Design": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Artistic": 0.28, "Creative-Skill": 0.28}
            },
            {
                "option_id": 3077,
                "option_text": "A wind tunnel for testing aerodynamic prototypes",
                "trait_tags": {"Aeronautical-Eng": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.36, "Technical-Skill": 0.32, "Industrial-Ops": 0.2, "Civil-Build": 0.16}
            },
            {
                "option_id": 3078,
                "option_text": "Oscilloscopes and breadboards for testing circuits",
                "trait_tags": {"Electronics-Dev": 1.0, "Electrical-Power": 0.8, "Hardware-Systems": 0.8, "Technical-Skill": 0.36, "Realistic": 0.32, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3079,
                "option_text": "Heavy machinery and thermal analysis software",
                "trait_tags": {"Mechanical-Design": 1.0, "Civil-Build": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Industrial-Ops": 0.25, "Electrical-Power": 0.2}
            },
            {
                "option_id": 3080,
                "option_text": "Power system simulators for electrical load shedding",
                "trait_tags": {"Electrical-Power": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3081,
                "option_text": "Statistical programming environments like R or Jupyter",
                "trait_tags": {"Data-Analytics": 1.0, "Software-Dev": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Technical-Skill": 0.36, "Lab-Research": 0.25}
            },
            {
                "option_id": 3082,
                "option_text": "Logic analyzers for debugging motherboard architecture",
                "trait_tags": {"Hardware-Systems": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Electrical-Power": 0.3, "Mechanical-Design": 0.25}
            }
        ]
    },
    {
        "question_id": 309,
        "question_text": "What 'achievement' in a project would make you the most proud?",
        "category": "Engineering CS - Achievement",
        "options": [
            {
                "option_id": 3083,
                "option_text": "Launching an app with a million active users",
                "trait_tags": {"Software-Dev": 1.0, "Web-Dev": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25}
            },
            {
                "option_id": 3084,
                "option_text": "Seeing a skyscraper you designed dominate the skyline",
                "trait_tags": {"Civil-Build": 1.0, "Spatial-Design": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Artistic": 0.28, "Creative-Skill": 0.28}
            },
            {
                "option_id": 3085,
                "option_text": "Successful test flight of an unmanned aerial vehicle (UAV)",
                "trait_tags": {"Aeronautical-Eng": 1.0, "Mechanical-Design": 0.8, "Electronics-Dev": 0.8, "Realistic": 0.36, "Technical-Skill": 0.32, "Industrial-Ops": 0.2}
            },
            {
                "option_id": 3086,
                "option_text": "Patenting a more efficient microchip architecture",
                "trait_tags": {"Hardware-Systems": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Electrical-Power": 0.3, "Mechanical-Design": 0.25}
            },
            {
                "option_id": 3087,
                "option_text": "Finding a hidden pattern in data that saves a company millions",
                "trait_tags": {"Data-Analytics": 1.0, "Software-Dev": 0.8, "AI-ML": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Technical-Skill": 0.36}
            },
            {
                "option_id": 3088,
                "option_text": "Building a robot that can navigate rough terrain mechanically",
                "trait_tags": {"Mechanical-Design": 1.0, "Electronics-Dev": 0.8, "Software-Dev": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Investigative": 0.32}
            },
            {
                "option_id": 3089,
                "option_text": "Restoring power to a massive region after a grid failure",
                "trait_tags": {"Electrical-Power": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3090,
                "option_text": "Developing a clear-signal satellite communication link",
                "trait_tags": {"Electronics-Dev": 1.0, "Electrical-Power": 0.8, "Aeronautical-Eng": 0.8, "Technical-Skill": 0.36, "Realistic": 0.32, "Hardware-Systems": 0.24}
            }
        ]
    },
    {
        "question_id": 310,
        "question_text": "In a 'Zombie Apocalypse' scenario, how would you contribute to the survivor base?",
        "category": "Engineering CS - Zombie Apocalypse",
        "options": [
            {
                "option_id": 3091,
                "option_text": "Coding the security firewall for the base's internal network",
                "trait_tags": {"Software-Dev": 1.0, "Cyber-Defense": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 3092,
                "option_text": "Constructing reinforced walls and watchtowers",
                "trait_tags": {"Civil-Build": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Industrial-Ops": 0.2}
            },
            {
                "option_id": 3093,
                "option_text": "Repairing the hardware of scavenged radios and computers",
                "trait_tags": {"Hardware-Systems": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Electrical-Power": 0.3, "Mechanical-Design": 0.25}
            },
            {
                "option_id": 3094,
                "option_text": "Rigging a solar farm to provide electricity to the camp",
                "trait_tags": {"Electrical-Power": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3095,
                "option_text": "Optimizing the base's mechanical traps and gates",
                "trait_tags": {"Mechanical-Design": 1.0, "Civil-Build": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Industrial-Ops": 0.25, "Electrical-Power": 0.2}
            },
            {
                "option_id": 3096,
                "option_text": "Using weather and resource data to predict the safest move",
                "trait_tags": {"Data-Analytics": 1.0, "Software-Dev": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Technical-Skill": 0.36, "Lab-Research": 0.25}
            },
            {
                "option_id": 3097,
                "option_text": "Maintaining the engines of the getaway vehicles and aircraft",
                "trait_tags": {"Aeronautical-Eng": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.36, "Technical-Skill": 0.32, "Industrial-Ops": 0.2, "Civil-Build": 0.16}
            },
            {
                "option_id": 3098,
                "option_text": "Fixing the communication sensors to detect nearby movements",
                "trait_tags": {"Electronics-Dev": 1.0, "Hardware-Systems": 0.8, "Technical-Skill": 0.36, "Realistic": 0.32, "Electrical-Power": 0.24, "Mechanical-Design": 0.2}
            }
        ]
    },
    {
        "question_id": 311,
        "question_text": "What would you rather spend a Saturday afternoon doing?",
        "category": "Engineering CS - Saturday Activity",
        "options": [
            {
                "option_id": 3099,
                "option_text": "Learning a new programming language or framework",
                "trait_tags": {"Software-Dev": 1.0, "Web-Dev": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25}
            },
            {
                "option_id": 3100,
                "option_text": "Sketching floor plans or bridge designs",
                "trait_tags": {"Civil-Build": 1.0, "Spatial-Design": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Artistic": 0.28, "Creative-Skill": 0.28}
            },
            {
                "option_id": 3101,
                "option_text": "Soldering a custom circuit for a DIY gadget",
                "trait_tags": {"Electronics-Dev": 1.0, "Hardware-Systems": 0.8, "Technical-Skill": 0.36, "Realistic": 0.32, "Electrical-Power": 0.24, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3102,
                "option_text": "Reading about the latest breakthroughs in jet propulsion",
                "trait_tags": {"Aeronautical-Eng": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.36, "Technical-Skill": 0.32, "Industrial-Ops": 0.2, "Civil-Build": 0.16}
            },
            {
                "option_id": 3103,
                "option_text": "Tinkering with a 3D printer or car engine",
                "trait_tags": {"Mechanical-Design": 1.0, "Hardware-Systems": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Industrial-Ops": 0.25, "Electrical-Power": 0.24}
            },
            {
                "option_id": 3104,
                "option_text": "Analyzing a spreadsheet of your personal expenses and habits",
                "trait_tags": {"Data-Analytics": 1.0, "Software-Dev": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Technical-Skill": 0.36, "Lab-Research": 0.25}
            },
            {
                "option_id": 3105,
                "option_text": "Upgrading the RAM or CPU of your PC",
                "trait_tags": {"Hardware-Systems": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Electrical-Power": 0.3, "Mechanical-Design": 0.25}
            },
            {
                "option_id": 3106,
                "option_text": "Learning how high-voltage transformers work",
                "trait_tags": {"Electrical-Power": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3, "Mechanical-Design": 0.2}
            }
        ]
    },
    {
        "question_id": 312,
        "question_text": "Which 'Superpower' relates most to your career goals?",
        "category": "Engineering CS - Superpower",
        "options": [
            {
                "option_id": 3107,
                "option_text": "Technopathy: Controlling and writing code with your mind",
                "trait_tags": {"Software-Dev": 1.0, "AI-ML": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Analytical-Skill": 0.36, "Data-Analytics": 0.32}
            },
            {
                "option_id": 3108,
                "option_text": "Super Strength: Being able to build massive structures easily",
                "trait_tags": {"Civil-Build": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Industrial-Ops": 0.2}
            },
            {
                "option_id": 3109,
                "option_text": "Flight: Understanding the physics of the sky perfectly",
                "trait_tags": {"Aeronautical-Eng": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.36, "Technical-Skill": 0.32, "Industrial-Ops": 0.2, "Civil-Build": 0.16}
            },
            {
                "option_id": 3110,
                "option_text": "Omniscience: Seeing patterns in every piece of information",
                "trait_tags": {"Data-Analytics": 1.0, "Software-Dev": 0.8, "AI-ML": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Technical-Skill": 0.36}
            },
            {
                "option_id": 3111,
                "option_text": "Energy Manipulation: Controlling the flow of electricity",
                "trait_tags": {"Electrical-Power": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3112,
                "option_text": "Material Morphing: Changing the shape of mechanical parts at will",
                "trait_tags": {"Mechanical-Design": 1.0, "Civil-Build": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Industrial-Ops": 0.25, "Electrical-Power": 0.2}
            },
            {
                "option_id": 3113,
                "option_text": "X-Ray Vision: Seeing through the layers of a complex circuit",
                "trait_tags": {"Electronics-Dev": 1.0, "Hardware-Systems": 0.8, "Electrical-Power": 0.8, "Technical-Skill": 0.36, "Realistic": 0.32, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3114,
                "option_text": "Hardware Intuition: Knowing exactly how any computer is built",
                "trait_tags": {"Hardware-Systems": 1.0, "Software-Dev": 0.8, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Investigative": 0.32}
            }
        ]
    },
    {
        "question_id": 313,
        "question_text": "What type of 'System' are you most interested in managing?",
        "category": "Engineering CS - Systems",
        "options": [
            {
                "option_id": 3115,
                "option_text": "A cloud-based web application system",
                "trait_tags": {"Software-Dev": 1.0, "Web-Dev": 0.8, "Cloud-Systems": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3}
            },
            {
                "option_id": 3116,
                "option_text": "A city's drainage and sewage system",
                "trait_tags": {"Civil-Build": 1.0, "Spatial-Design": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Artistic": 0.28, "Creative-Skill": 0.28}
            },
            {
                "option_id": 3117,
                "option_text": "An aircraft's flight control and navigation system",
                "trait_tags": {"Aeronautical-Eng": 1.0, "Electronics-Dev": 0.8, "Software-Dev": 0.8, "Technical-Skill": 0.36, "Investigative": 0.32, "Data-Analytics": 0.24}
            },
            {
                "option_id": 3118,
                "option_text": "A national power grid and substation system",
                "trait_tags": {"Electrical-Power": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3119,
                "option_text": "A manufacturing plant's assembly line system",
                "trait_tags": {"Mechanical-Design": 1.0, "Industrial-Ops": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Analytical-Skill": 0.28, "Enterprising": 0.24}
            },
            {
                "option_id": 3120,
                "option_text": "A global database and information analytics system",
                "trait_tags": {"Data-Analytics": 1.0, "Software-Dev": 0.8, "Cloud-Systems": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Technical-Skill": 0.36}
            },
            {
                "option_id": 3121,
                "option_text": "A computer's hardware and motherboard system",
                "trait_tags": {"Hardware-Systems": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Electrical-Power": 0.3, "Mechanical-Design": 0.25}
            },
            {
                "option_id": 3122,
                "option_text": "A telecommunications and signal broadcasting system",
                "trait_tags": {"Electronics-Dev": 1.0, "Electrical-Power": 0.8, "Technical-Skill": 0.36, "Realistic": 0.32, "Hardware-Systems": 0.24, "Mechanical-Design": 0.16}
            }
        ]
    },
    {
        "question_id": 314,
        "question_text": "If you were to write a book, what would the topic be?",
        "category": "Engineering CS - Book Topic",
        "options": [
            {
                "option_id": 3123,
                "option_text": "The Art of Clean Code and Software Architecture",
                "trait_tags": {"Software-Dev": 1.0, "Web-Dev": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25}
            },
            {
                "option_id": 3124,
                "option_text": "Principles of Modern Urban Planning and Construction",
                "trait_tags": {"Civil-Build": 1.0, "Spatial-Design": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Artistic": 0.28, "Creative-Skill": 0.28}
            },
            {
                "option_id": 3125,
                "option_text": "The Future of Space Travel and Aerodynamics",
                "trait_tags": {"Aeronautical-Eng": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.36, "Technical-Skill": 0.32, "Industrial-Ops": 0.2, "Civil-Build": 0.16}
            },
            {
                "option_id": 3126,
                "option_text": "Deep Learning and the Power of Predictive Analytics",
                "trait_tags": {"Data-Analytics": 1.0, "Software-Dev": 0.8, "AI-ML": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Technical-Skill": 0.36}
            },
            {
                "option_id": 3127,
                "option_text": "Mastering Circuit Design and Signal Processing",
                "trait_tags": {"Electronics-Dev": 1.0, "Electrical-Power": 0.8, "Technical-Skill": 0.36, "Realistic": 0.32, "Hardware-Systems": 0.24, "Mechanical-Design": 0.16}
            },
            {
                "option_id": 3128,
                "option_text": "The History of Engines and Industrial Machinery",
                "trait_tags": {"Mechanical-Design": 1.0, "Industrial-Ops": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Analytical-Skill": 0.28, "Enterprising": 0.24}
            },
            {
                "option_id": 3129,
                "option_text": "Innovations in Sustainable Energy and Power Grids",
                "trait_tags": {"Electrical-Power": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3130,
                "option_text": "Building the Ultimate PC: From Transistors to CPUs",
                "trait_tags": {"Hardware-Systems": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Electrical-Power": 0.3, "Mechanical-Design": 0.25}
            }
        ]
    },
    {
        "question_id": 315,
        "question_text": "What is your ideal 'Work Environment'?",
        "category": "Engineering CS - Work Environment",
        "options": [
            {
                "option_id": 3131,
                "option_text": "A sleek tech startup with multiple monitors",
                "trait_tags": {"Software-Dev": 1.0, "Web-Dev": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25}
            },
            {
                "option_id": 3132,
                "option_text": "An outdoor construction site with hard hats and blueprints",
                "trait_tags": {"Civil-Build": 1.0, "Spatial-Design": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Artistic": 0.28, "Creative-Skill": 0.28}
            },
            {
                "option_id": 3133,
                "option_text": "A clean-room laboratory for assembling microchips",
                "trait_tags": {"Hardware-Systems": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Electrical-Power": 0.3, "Mechanical-Design": 0.25}
            },
            {
                "option_id": 3134,
                "option_text": "A hangar or airfield working with large aircraft",
                "trait_tags": {"Aeronautical-Eng": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.36, "Technical-Skill": 0.32, "Industrial-Ops": 0.2, "Civil-Build": 0.16}
            },
            {
                "option_id": 3135,
                "option_text": "A quiet office focused on data visualizations and charts",
                "trait_tags": {"Data-Analytics": 1.0, "Software-Dev": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Technical-Skill": 0.36, "Lab-Research": 0.25}
            },
            {
                "option_id": 3136,
                "option_text": "A workshop filled with tools, gears, and metal parts",
                "trait_tags": {"Mechanical-Design": 1.0, "Civil-Build": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Industrial-Ops": 0.25, "Electrical-Power": 0.2}
            },
            {
                "option_id": 3137,
                "option_text": "A power plant or high-voltage testing facility",
                "trait_tags": {"Electrical-Power": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3138,
                "option_text": "A telecom lab with antennas and frequency testers",
                "trait_tags": {"Electronics-Dev": 1.0, "Electrical-Power": 0.8, "Hardware-Systems": 0.8, "Technical-Skill": 0.36, "Realistic": 0.32, "Mechanical-Design": 0.2}
            }
        ]
    },
    {
        "question_id": 316,
        "question_text": "Which of these projects sounds most fulfilling?",
        "category": "Engineering CS - Fulfilling Project",
        "options": [
            {
                "option_id": 3139,
                "option_text": "Developing an AI-powered personal assistant",
                "trait_tags": {"Software-Dev": 1.0, "AI-ML": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Analytical-Skill": 0.36, "Data-Analytics": 0.32}
            },
            {
                "option_id": 3140,
                "option_text": "Building a dam to provide water and power to a province",
                "trait_tags": {"Civil-Build": 1.0, "Electrical-Power": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Hardware-Systems": 0.24}
            },
            {
                "option_id": 3141,
                "option_text": "Designing the next-generation fighter jet or spacecraft",
                "trait_tags": {"Aeronautical-Eng": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.36, "Technical-Skill": 0.32, "Industrial-Ops": 0.2, "Civil-Build": 0.16}
            },
            {
                "option_id": 3142,
                "option_text": "Analyzing healthcare data to predict disease outbreaks",
                "trait_tags": {"Data-Analytics": 1.0, "Software-Dev": 0.8, "AI-ML": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Technical-Skill": 0.36}
            },
            {
                "option_id": 3143,
                "option_text": "Developing the circuit boards for a new smartphone",
                "trait_tags": {"Electronics-Dev": 1.0, "Hardware-Systems": 0.8, "Technical-Skill": 0.36, "Realistic": 0.32, "Electrical-Power": 0.24, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3144,
                "option_text": "Designing a prosthetic limb with mechanical joints",
                "trait_tags": {"Mechanical-Design": 1.0, "Electronics-Dev": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Industrial-Ops": 0.25, "Civil-Build": 0.2}
            },
            {
                "option_id": 3145,
                "option_text": "Implementing a solar-powered grid for a remote village",
                "trait_tags": {"Electrical-Power": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3146,
                "option_text": "Optimizing the cooling system for a massive data center",
                "trait_tags": {"Hardware-Systems": 1.0, "Electrical-Power": 0.8, "Mechanical-Design": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Software-Dev": 0.2}
            }
        ]
    },
    {
        "question_id": 317,
        "question_text": "What do you find most annoying?",
        "category": "Engineering CS - Pet Peeve",
        "options": [
            {
                "option_id": 3147,
                "option_text": "A software bug that crashes your favorite app",
                "trait_tags": {"Software-Dev": 1.0, "Web-Dev": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25}
            },
            {
                "option_id": 3148,
                "option_text": "A traffic jam caused by poor road design",
                "trait_tags": {"Civil-Build": 1.0, "Spatial-Design": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Artistic": 0.28, "Creative-Skill": 0.28}
            },
            {
                "option_id": 3149,
                "option_text": "A laptop that overheats because of bad internal design",
                "trait_tags": {"Hardware-Systems": 1.0, "Mechanical-Design": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Electrical-Power": 0.3, "Software-Dev": 0.2}
            },
            {
                "option_id": 3150,
                "option_text": "A flight delay due to mechanical or technical issues",
                "trait_tags": {"Aeronautical-Eng": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.36, "Technical-Skill": 0.32, "Industrial-Ops": 0.2, "Civil-Build": 0.16}
            },
            {
                "option_id": 3151,
                "option_text": "A power outage that lasts for several hours",
                "trait_tags": {"Electrical-Power": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3152,
                "option_text": "A mechanical device that constantly jams or breaks",
                "trait_tags": {"Mechanical-Design": 1.0, "Industrial-Ops": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Analytical-Skill": 0.28, "Enterprising": 0.24}
            },
            {
                "option_id": 3153,
                "option_text": "Misleading statistics or confusing data charts",
                "trait_tags": {"Data-Analytics": 1.0, "Software-Dev": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Technical-Skill": 0.36, "Lab-Research": 0.25}
            },
            {
                "option_id": 3154,
                "option_text": "Poor cell phone reception or dropped calls",
                "trait_tags": {"Electronics-Dev": 1.0, "Hardware-Systems": 0.8, "Technical-Skill": 0.36, "Realistic": 0.32, "Electrical-Power": 0.24, "Mechanical-Design": 0.2}
            }
        ]
    },
    {
        "question_id": 318,
        "question_text": "If you could witness one event in history, which would it be?",
        "category": "Engineering CS - Historical Event",
        "options": [
            {
                "option_id": 3155,
                "option_text": "The creation of the first computer program",
                "trait_tags": {"Software-Dev": 1.0, "Hardware-Systems": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Realistic": 0.32, "Data-Analytics": 0.3}
            },
            {
                "option_id": 3156,
                "option_text": "The construction of the Great Pyramids or Eiffel Tower",
                "trait_tags": {"Civil-Build": 1.0, "Spatial-Design": 0.8, "Mechanical-Design": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Artistic": 0.28}
            },
            {
                "option_id": 3157,
                "option_text": "The Wright brothers' first successful flight",
                "trait_tags": {"Aeronautical-Eng": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.36, "Technical-Skill": 0.32, "Industrial-Ops": 0.2, "Civil-Build": 0.16}
            },
            {
                "option_id": 3158,
                "option_text": "The invention of the light bulb and the first power grid",
                "trait_tags": {"Electrical-Power": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3159,
                "option_text": "The first Industrial Revolution and the steam engine",
                "trait_tags": {"Mechanical-Design": 1.0, "Industrial-Ops": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Analytical-Skill": 0.28, "Enterprising": 0.24}
            },
            {
                "option_id": 3160,
                "option_text": "The moment the first radio signal was transmitted",
                "trait_tags": {"Electronics-Dev": 1.0, "Electrical-Power": 0.8, "Technical-Skill": 0.36, "Realistic": 0.32, "Hardware-Systems": 0.24, "Mechanical-Design": 0.16}
            },
            {
                "option_id": 3161,
                "option_text": "The birth of the internet and global data exchange",
                "trait_tags": {"Data-Analytics": 1.0, "Software-Dev": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Technical-Skill": 0.36, "Lab-Research": 0.25}
            },
            {
                "option_id": 3162,
                "option_text": "The assembly of the first modern microprocessor",
                "trait_tags": {"Hardware-Systems": 1.0, "Electrical-Power": 0.8, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Mechanical-Design": 0.25}
            }
        ]
    },
    {
        "question_id": 319,
        "question_text": "What's your favorite way to spend money on tech?",
        "category": "Engineering CS - Tech Spending",
        "options": [
            {
                "option_id": 3163,
                "option_text": "Buying software licenses or gaming subscriptions",
                "trait_tags": {"Software-Dev": 1.0, "Web-Dev": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25}
            },
            {
                "option_id": 3164,
                "option_text": "Buying architectural model kits or 3D puzzles",
                "trait_tags": {"Civil-Build": 1.0, "Spatial-Design": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Artistic": 0.28, "Creative-Skill": 0.28}
            },
            {
                "option_id": 3165,
                "option_text": "Upgrading your PC's GPU or motherboard",
                "trait_tags": {"Hardware-Systems": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Electrical-Power": 0.3, "Mechanical-Design": 0.25}
            },
            {
                "option_id": 3166,
                "option_text": "Buying a high-end drone with advanced flight controls",
                "trait_tags": {"Aeronautical-Eng": 1.0, "Electronics-Dev": 0.8, "Mechanical-Design": 0.8, "Realistic": 0.36, "Technical-Skill": 0.32, "Industrial-Ops": 0.2}
            },
            {
                "option_id": 3167,
                "option_text": "Subscribing to premium data tools or stock market apps",
                "trait_tags": {"Data-Analytics": 1.0, "Software-Dev": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Technical-Skill": 0.36, "Lab-Research": 0.25}
            },
            {
                "option_id": 3168,
                "option_text": "Buying power tools or mechanical DIY kits",
                "trait_tags": {"Mechanical-Design": 1.0, "Civil-Build": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Industrial-Ops": 0.25, "Electrical-Power": 0.2}
            },
            {
                "option_id": 3169,
                "option_text": "Investing in smart home energy-saving devices",
                "trait_tags": {"Electrical-Power": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3170,
                "option_text": "Buying professional soldering stations or radio kits",
                "trait_tags": {"Electronics-Dev": 1.0, "Hardware-Systems": 0.8, "Technical-Skill": 0.36, "Realistic": 0.32, "Electrical-Power": 0.24, "Mechanical-Design": 0.2}
            }
        ]
    },
    {
        "question_id": 320,
        "question_text": "Which 'Daily Task' would you enjoy most?",
        "category": "Engineering CS - Daily Task",
        "options": [
            {
                "option_id": 3171,
                "option_text": "Reviewing lines of code for logic errors",
                "trait_tags": {"Software-Dev": 1.0, "Data-Analytics": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Analytical-Skill": 0.36, "Cyber-Defense": 0.25}
            },
            {
                "option_id": 3172,
                "option_text": "Checking a building site for safety compliance",
                "trait_tags": {"Civil-Build": 1.0, "Spatial-Design": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Artistic": 0.28, "Creative-Skill": 0.28}
            },
            {
                "option_id": 3173,
                "option_text": "Testing the lift and drag of a prototype wing",
                "trait_tags": {"Aeronautical-Eng": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.36, "Technical-Skill": 0.32, "Industrial-Ops": 0.2, "Civil-Build": 0.16}
            },
            {
                "option_id": 3174,
                "option_text": "Cleaning and organizing a large dataset for analysis",
                "trait_tags": {"Data-Analytics": 1.0, "Software-Dev": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Technical-Skill": 0.36, "Lab-Research": 0.25}
            },
            {
                "option_id": 3175,
                "option_text": "Designing the layout of a PCB (Printed Circuit Board)",
                "trait_tags": {"Electronics-Dev": 1.0, "Hardware-Systems": 0.8, "Technical-Skill": 0.36, "Realistic": 0.32, "Electrical-Power": 0.24, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3176,
                "option_text": "Lubricating and maintaining a large industrial robot",
                "trait_tags": {"Mechanical-Design": 1.0, "Industrial-Ops": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Analytical-Skill": 0.28, "Enterprising": 0.24}
            },
            {
                "option_id": 3177,
                "option_text": "Monitoring the voltage levels of a local substation",
                "trait_tags": {"Electrical-Power": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3178,
                "option_text": "Troubleshooting why a computer won't POST (Power-On Self-Test)",
                "trait_tags": {"Hardware-Systems": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Electrical-Power": 0.3, "Mechanical-Design": 0.25}
            }
        ]
    },
    {
        "question_id": 321,
        "question_text": "What kind of 'Problem' is most satisfying to solve?",
        "category": "Engineering CS - Satisfying Problem",
        "options": [
            {
                "option_id": 3179,
                "option_text": "A logic puzzle that requires a recursive solution",
                "trait_tags": {"Software-Dev": 1.0, "Data-Analytics": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Analytical-Skill": 0.36, "Cyber-Defense": 0.25}
            },
            {
                "option_id": 3180,
                "option_text": "A structural problem where a beam is under too much stress",
                "trait_tags": {"Civil-Build": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Industrial-Ops": 0.2}
            },
            {
                "option_id": 3181,
                "option_text": "A hardware bottleneck that is slowing down a system",
                "trait_tags": {"Hardware-Systems": 1.0, "Software-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Investigative": 0.32, "Electrical-Power": 0.3}
            },
            {
                "option_id": 3182,
                "option_text": "An aerodynamic stall that needs a wing adjustment",
                "trait_tags": {"Aeronautical-Eng": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.36, "Technical-Skill": 0.32, "Industrial-Ops": 0.2, "Civil-Build": 0.16}
            },
            {
                "option_id": 3183,
                "option_text": "An outlier in a graph that changes the whole conclusion",
                "trait_tags": {"Data-Analytics": 1.0, "Analytical-Skill": 0.8, "Investigative": 0.45, "Software-Dev": 0.3, "Lab-Research": 0.28, "Finance-Acct": 0.28}
            },
            {
                "option_id": 3184,
                "option_text": "A mechanical friction issue that is causing heat buildup",
                "trait_tags": {"Mechanical-Design": 1.0, "Electrical-Power": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Industrial-Ops": 0.25, "Hardware-Systems": 0.24}
            },
            {
                "option_id": 3185,
                "option_text": "A short circuit in a complex wiring diagram",
                "trait_tags": {"Electrical-Power": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3186,
                "option_text": "A signal noise issue that is distorting audio/video data",
                "trait_tags": {"Electronics-Dev": 1.0, "Hardware-Systems": 0.8, "Technical-Skill": 0.36, "Realistic": 0.32, "Electrical-Power": 0.24, "Mechanical-Design": 0.2}
            }
        ]
    },
    {
        "question_id": 322,
        "question_text": "If you were a researcher, what would you study?",
        "category": "Engineering CS - Research Topic",
        "options": [
            {
                "option_id": 3187,
                "option_text": "Developing more efficient sorting algorithms",
                "trait_tags": {"Software-Dev": 1.0, "Data-Analytics": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Analytical-Skill": 0.36, "Cyber-Defense": 0.25}
            },
            {
                "option_id": 3188,
                "option_text": "Testing new sustainable materials for concrete",
                "trait_tags": {"Civil-Build": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Industrial-Ops": 0.2}
            },
            {
                "option_id": 3189,
                "option_text": "Investigating the effect of high-altitude on jet engines",
                "trait_tags": {"Aeronautical-Eng": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.36, "Technical-Skill": 0.32, "Industrial-Ops": 0.2, "Civil-Build": 0.16}
            },
            {
                "option_id": 3190,
                "option_text": "Deep-diving into the ethics of Big Data and AI",
                "trait_tags": {"Data-Analytics": 1.0, "Software-Dev": 0.8, "AI-ML": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Technical-Skill": 0.36}
            },
            {
                "option_id": 3191,
                "option_text": "Developing faster ways to transmit data through copper",
                "trait_tags": {"Electronics-Dev": 1.0, "Electrical-Power": 0.8, "Technical-Skill": 0.36, "Realistic": 0.32, "Hardware-Systems": 0.24, "Mechanical-Design": 0.16}
            },
            {
                "option_id": 3192,
                "option_text": "Designing a machine that can harvest energy from waves",
                "trait_tags": {"Mechanical-Design": 1.0, "Electrical-Power": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Industrial-Ops": 0.25, "Hardware-Systems": 0.24}
            },
            {
                "option_id": 3193,
                "option_text": "Exploring wireless power transmission over long distances",
                "trait_tags": {"Electrical-Power": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3194,
                "option_text": "Creating a bio-chip that integrates with human nerves",
                "trait_tags": {"Hardware-Systems": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Electrical-Power": 0.3, "Mechanical-Design": 0.25}
            }
        ]
    },
    {
        "question_id": 323,
        "question_text": "Which 'Hobby' sounds most appealing?",
        "category": "Engineering CS - Hobby",
        "options": [
            {
                "option_id": 3195,
                "option_text": "Building a website for a local non-profit",
                "trait_tags": {"Software-Dev": 1.0, "Web-Dev": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25}
            },
            {
                "option_id": 3196,
                "option_text": "Designing and building your own furniture",
                "trait_tags": {"Civil-Build": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Industrial-Ops": 0.2}
            },
            {
                "option_id": 3197,
                "option_text": "Building and flying RC planes or gliders",
                "trait_tags": {"Aeronautical-Eng": 1.0, "Mechanical-Design": 0.8, "Electronics-Dev": 0.8, "Realistic": 0.36, "Technical-Skill": 0.32, "Industrial-Ops": 0.2}
            },
            {
                "option_id": 3198,
                "option_text": "Playing fantasy sports or tracking stock trends",
                "trait_tags": {"Data-Analytics": 1.0, "Software-Dev": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Technical-Skill": 0.36, "Lab-Research": 0.25}
            },
            {
                "option_id": 3199,
                "option_text": "Restoring old radios or building guitar pedals",
                "trait_tags": {"Electronics-Dev": 1.0, "Hardware-Systems": 0.8, "Technical-Skill": 0.36, "Realistic": 0.32, "Electrical-Power": 0.24, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3200,
                "option_text": "Working on project cars or go-karts",
                "trait_tags": {"Mechanical-Design": 1.0, "Aeronautical-Eng": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Industrial-Ops": 0.25, "Civil-Build": 0.2}
            },
            {
                "option_id": 3201,
                "option_text": "Installing your own solar panels or backup batteries",
                "trait_tags": {"Electrical-Power": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3202,
                "option_text": "Overclocking your PC to its maximum limits",
                "trait_tags": {"Hardware-Systems": 1.0, "Software-Dev": 0.8, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Investigative": 0.32}
            }
        ]
    },
    {
        "question_id": 324,
        "question_text": "How do you prefer to receive 'Feedback' on your work?",
        "category": "Engineering CS - Feedback",
        "options": [
            {
                "option_id": 3203,
                "option_text": "Through a 'Code Review' identifying logic improvements",
                "trait_tags": {"Software-Dev": 1.0, "Data-Analytics": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Analytical-Skill": 0.36, "Cyber-Defense": 0.25}
            },
            {
                "option_id": 3204,
                "option_text": "Through a 'Blueprint Review' checking for safety risks",
                "trait_tags": {"Civil-Build": 1.0, "Spatial-Design": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Artistic": 0.28, "Creative-Skill": 0.28}
            },
            {
                "option_id": 3205,
                "option_text": "Through a 'Stress Test' report on a physical part",
                "trait_tags": {"Mechanical-Design": 1.0, "Civil-Build": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Industrial-Ops": 0.25, "Electrical-Power": 0.2}
            },
            {
                "option_id": 3206,
                "option_text": "Through a 'Flight Log' analyzing pilot performance",
                "trait_tags": {"Aeronautical-Eng": 1.0, "Data-Analytics": 0.8, "Investigative": 0.36, "Analytical-Skill": 0.36, "Software-Dev": 0.24, "Lab-Research": 0.2}
            },
            {
                "option_id": 3207,
                "option_text": "Through a 'Statistical Audit' checking your accuracy",
                "trait_tags": {"Data-Analytics": 1.0, "Analytical-Skill": 0.8, "Investigative": 0.45, "Software-Dev": 0.3, "Lab-Research": 0.28, "Finance-Acct": 0.28}
            },
            {
                "option_id": 3208,
                "option_text": "Through a 'Circuit Simulation' showing where heat builds up",
                "trait_tags": {"Electronics-Dev": 1.0, "Electrical-Power": 0.8, "Hardware-Systems": 0.8, "Technical-Skill": 0.36, "Realistic": 0.32, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3209,
                "option_text": "Through a 'Load Test' on a power distribution model",
                "trait_tags": {"Electrical-Power": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3210,
                "option_text": "Through a 'Hardware Benchmark' comparing speeds",
                "trait_tags": {"Hardware-Systems": 1.0, "Software-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Investigative": 0.32, "Electrical-Power": 0.3}
            }
        ]
    },
    {
        "question_id": 325,
        "question_text": "What would you do if a machine you built stopped working?",
        "category": "Engineering CS - Troubleshooting",
        "options": [
            {
                "option_id": 3211,
                "option_text": "Check the source code for any unhandled exceptions",
                "trait_tags": {"Software-Dev": 1.0, "Data-Analytics": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Analytical-Skill": 0.36, "Cyber-Defense": 0.25}
            },
            {
                "option_id": 3212,
                "option_text": "Inspect the foundation and support beams for cracks",
                "trait_tags": {"Civil-Build": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Industrial-Ops": 0.2}
            },
            {
                "option_id": 3213,
                "option_text": "Open it up to see if any gears or pistons are jammed",
                "trait_tags": {"Mechanical-Design": 1.0, "Industrial-Ops": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Analytical-Skill": 0.28, "Enterprising": 0.24}
            },
            {
                "option_id": 3214,
                "option_text": "Use a multimeter to see where the power flow stops",
                "trait_tags": {"Electrical-Power": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3215,
                "option_text": "Check the sensor data logs to see what happened",
                "trait_tags": {"Data-Analytics": 1.0, "Software-Dev": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Technical-Skill": 0.36, "Lab-Research": 0.25}
            },
            {
                "option_id": 3216,
                "option_text": "Use an oscilloscope to check the signal waveforms",
                "trait_tags": {"Electronics-Dev": 1.0, "Electrical-Power": 0.8, "Technical-Skill": 0.36, "Realistic": 0.32, "Hardware-Systems": 0.24, "Mechanical-Design": 0.16}
            },
            {
                "option_id": 3217,
                "option_text": "Take out the motherboard and check for burnt capacitors",
                "trait_tags": {"Hardware-Systems": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Electrical-Power": 0.3, "Mechanical-Design": 0.25}
            },
            {
                "option_id": 3218,
                "option_text": "Inspect the turbines and fuel lines for any blockage",
                "trait_tags": {"Aeronautical-Eng": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.36, "Technical-Skill": 0.32, "Industrial-Ops": 0.2, "Civil-Build": 0.16}
            }
        ]
    },
    {
        "question_id": 326,
        "question_text": "Which 'Core Subject' do you enjoy most?",
        "category": "Engineering CS - Core Subject",
        "options": [
            {
                "option_id": 3219,
                "option_text": "Logic and Discrete Mathematics",
                "trait_tags": {"Software-Dev": 1.0, "Data-Analytics": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Analytical-Skill": 0.36, "Cyber-Defense": 0.25}
            },
            {
                "option_id": 3220,
                "option_text": "Statics and Dynamics of Structures",
                "trait_tags": {"Civil-Build": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Industrial-Ops": 0.2}
            },
            {
                "option_id": 3221,
                "option_text": "Thermodynamics and Heat Transfer",
                "trait_tags": {"Mechanical-Design": 1.0, "Electrical-Power": 0.8, "Aeronautical-Eng": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Industrial-Ops": 0.25}
            },
            {
                "option_id": 3222,
                "option_text": "Probability and Statistical Inference",
                "trait_tags": {"Data-Analytics": 1.0, "Software-Dev": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Technical-Skill": 0.36, "Lab-Research": 0.25}
            },
            {
                "option_id": 3223,
                "option_text": "Electromagnetics and Circuit Theory",
                "trait_tags": {"Electrical-Power": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3224,
                "option_text": "Digital Logic Design and Computer Architecture",
                "trait_tags": {"Hardware-Systems": 1.0, "Software-Dev": 0.8, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Investigative": 0.32}
            },
            {
                "option_id": 3225,
                "option_text": "Fluid Mechanics and Aerodynamics",
                "trait_tags": {"Aeronautical-Eng": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.36, "Technical-Skill": 0.32, "Industrial-Ops": 0.2, "Civil-Build": 0.16}
            },
            {
                "option_id": 3226,
                "option_text": "Communication Theory and Signal Processing",
                "trait_tags": {"Electronics-Dev": 1.0, "Electrical-Power": 0.8, "Technical-Skill": 0.36, "Realistic": 0.32, "Hardware-Systems": 0.24, "Mechanical-Design": 0.16}
            }
        ]
    },
    {
        "question_id": 327,
        "question_text": "What's your favorite 'Sci-Fi' trope?",
        "category": "Engineering CS - Sci-Fi",
        "options": [
            {
                "option_id": 3227,
                "option_text": "An AI that gains consciousness and hacks the world",
                "trait_tags": {"Software-Dev": 1.0, "Cyber-Defense": 0.8, "AI-ML": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Analytical-Skill": 0.36}
            },
            {
                "option_id": 3228,
                "option_text": "A massive space station or mega-structure in orbit",
                "trait_tags": {"Civil-Build": 1.0, "Spatial-Design": 0.8, "Mechanical-Design": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Artistic": 0.28}
            },
            {
                "option_id": 3229,
                "option_text": "Faster-than-light spaceships and starfighters",
                "trait_tags": {"Aeronautical-Eng": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.36, "Technical-Skill": 0.32, "Industrial-Ops": 0.2, "Civil-Build": 0.16}
            },
            {
                "option_id": 3230,
                "option_text": "A world where every action is predicted by an algorithm",
                "trait_tags": {"Data-Analytics": 1.0, "Software-Dev": 0.8, "AI-ML": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Technical-Skill": 0.36}
            },
            {
                "option_id": 3231,
                "option_text": "Cyborgs with advanced neural-link hardware",
                "trait_tags": {"Hardware-Systems": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Electrical-Power": 0.3, "Mechanical-Design": 0.25}
            },
            {
                "option_id": 3232,
                "option_text": "Giant mechs with complex mechanical joints and gears",
                "trait_tags": {"Mechanical-Design": 1.0, "Electronics-Dev": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Industrial-Ops": 0.25, "Civil-Build": 0.2}
            },
            {
                "option_id": 3233,
                "option_text": "A society that has mastered infinite clean energy",
                "trait_tags": {"Electrical-Power": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3234,
                "option_text": "A planet-wide communication network using lasers",
                "trait_tags": {"Electronics-Dev": 1.0, "Electrical-Power": 0.8, "Technical-Skill": 0.36, "Realistic": 0.32, "Hardware-Systems": 0.24, "Mechanical-Design": 0.16}
            }
        ]
    },
    {
        "question_id": 328,
        "question_text": "What kind of 'Internship' would you apply for?",
        "category": "Engineering CS - Internship",
        "options": [
            {
                "option_id": 3235,
                "option_text": "Software Engineer Intern at a major tech company",
                "trait_tags": {"Software-Dev": 1.0, "Web-Dev": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25}
            },
            {
                "option_id": 3236,
                "option_text": "Site Engineer Intern at a large construction firm",
                "trait_tags": {"Civil-Build": 1.0, "Spatial-Design": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Artistic": 0.28, "Creative-Skill": 0.28}
            },
            {
                "option_id": 3237,
                "option_text": "Maintenance Intern at a commercial airline hangar",
                "trait_tags": {"Aeronautical-Eng": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.36, "Technical-Skill": 0.32, "Industrial-Ops": 0.2, "Civil-Build": 0.16}
            },
            {
                "option_id": 3238,
                "option_text": "Data Analyst Intern at a financial research group",
                "trait_tags": {"Data-Analytics": 1.0, "Software-Dev": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Technical-Skill": 0.36, "Lab-Research": 0.25}
            },
            {
                "option_id": 3239,
                "option_text": "Circuit Design Intern at a smartphone manufacturer",
                "trait_tags": {"Electronics-Dev": 1.0, "Hardware-Systems": 0.8, "Technical-Skill": 0.36, "Realistic": 0.32, "Electrical-Power": 0.24, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3240,
                "option_text": "Design Intern at an automotive or robotics plant",
                "trait_tags": {"Mechanical-Design": 1.0, "Electronics-Dev": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Industrial-Ops": 0.25, "Civil-Build": 0.2}
            },
            {
                "option_id": 3241,
                "option_text": "Operations Intern at a hydroelectric power plant",
                "trait_tags": {"Electrical-Power": 1.0, "Mechanical-Design": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3, "Industrial-Ops": 0.2}
            },
            {
                "option_id": 3242,
                "option_text": "Hardware Systems Intern at a server farm or ISP",
                "trait_tags": {"Hardware-Systems": 1.0, "Software-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Investigative": 0.32, "Electrical-Power": 0.3}
            }
        ]
    },
    {
        "question_id": 329,
        "question_text": "What would you do with a million-dollar grant?",
        "category": "Engineering CS - Million Dollar Grant",
        "options": [
            {
                "option_id": 3243,
                "option_text": "Build an open-source library for developers worldwide",
                "trait_tags": {"Software-Dev": 1.0, "Web-Dev": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25}
            },
            {
                "option_id": 3244,
                "option_text": "Design a low-cost housing system for underserved areas",
                "trait_tags": {"Civil-Build": 1.0, "Spatial-Design": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Artistic": 0.28, "Creative-Skill": 0.28}
            },
            {
                "option_id": 3245,
                "option_text": "Develop a more fuel-efficient jet engine prototype",
                "trait_tags": {"Aeronautical-Eng": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.36, "Technical-Skill": 0.32, "Industrial-Ops": 0.2, "Civil-Build": 0.16}
            },
            {
                "option_id": 3246,
                "option_text": "Build a massive server dedicated to climate research data",
                "trait_tags": {"Data-Analytics": 1.0, "Software-Dev": 0.8, "Cloud-Systems": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Technical-Skill": 0.36}
            },
            {
                "option_id": 3247,
                "option_text": "Create a cheap, reliable communication device for disaster zones",
                "trait_tags": {"Electronics-Dev": 1.0, "Hardware-Systems": 0.8, "Technical-Skill": 0.36, "Realistic": 0.32, "Electrical-Power": 0.24, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3248,
                "option_text": "Invent a new type of high-efficiency cooling system",
                "trait_tags": {"Mechanical-Design": 1.0, "Electrical-Power": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Industrial-Ops": 0.25, "Hardware-Systems": 0.24}
            },
            {
                "option_id": 3249,
                "option_text": "Build a micro-grid for a town without electricity",
                "trait_tags": {"Electrical-Power": 1.0, "Electronics-Dev": 0.8, "Civil-Build": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3}
            },
            {
                "option_id": 3250,
                "option_text": "Design a new high-speed processor for mobile devices",
                "trait_tags": {"Hardware-Systems": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Electrical-Power": 0.3, "Mechanical-Design": 0.25}
            }
        ]
    },
    {
        "question_id": 330,
        "question_text": "Which 'Toy' did you enjoy most as a kid?",
        "category": "Engineering CS - Childhood Toy",
        "options": [
            {
                "option_id": 3251,
                "option_text": "Video games where you could build your own worlds",
                "trait_tags": {"Software-Dev": 1.0, "Web-Dev": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25}
            },
            {
                "option_id": 3252,
                "option_text": "LEGOs or wooden blocks for building towers",
                "trait_tags": {"Civil-Build": 1.0, "Spatial-Design": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Artistic": 0.28, "Creative-Skill": 0.28}
            },
            {
                "option_id": 3253,
                "option_text": "Paper airplanes or balsa wood gliders",
                "trait_tags": {"Aeronautical-Eng": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.36, "Technical-Skill": 0.32, "Industrial-Ops": 0.2, "Civil-Build": 0.16}
            },
            {
                "option_id": 3254,
                "option_text": "Card games or board games involving probability and strategy",
                "trait_tags": {"Data-Analytics": 1.0, "Analytical-Skill": 0.8, "Investigative": 0.45, "Software-Dev": 0.3, "Lab-Research": 0.28, "Finance-Acct": 0.28}
            },
            {
                "option_id": 3255,
                "option_text": "Remote-controlled cars or walkie-talkies",
                "trait_tags": {"Electronics-Dev": 1.0, "Hardware-Systems": 0.8, "Technical-Skill": 0.36, "Realistic": 0.32, "Electrical-Power": 0.24, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3256,
                "option_text": "Action figures with many points of articulation",
                "trait_tags": {"Mechanical-Design": 1.0, "Civil-Build": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Industrial-Ops": 0.25, "Electrical-Power": 0.2}
            },
            {
                "option_id": 3257,
                "option_text": "Science kits involving batteries and light bulbs",
                "trait_tags": {"Electrical-Power": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3258,
                "option_text": "Computer parts or electronic learning kits",
                "trait_tags": {"Hardware-Systems": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Electrical-Power": 0.3, "Mechanical-Design": 0.25}
            }
        ]
    },
    {
        "question_id": 331,
        "question_text": "What is the 'Enemy' of your work?",
        "category": "Engineering CS - Work Enemy",
        "options": [
            {
                "option_id": 3259,
                "option_text": "Spaghetti code and unoptimized logic",
                "trait_tags": {"Software-Dev": 1.0, "Web-Dev": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25}
            },
            {
                "option_id": 3260,
                "option_text": "Soil erosion and structural fatigue",
                "trait_tags": {"Civil-Build": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Industrial-Ops": 0.2}
            },
            {
                "option_id": 3261,
                "option_text": "Drag and air turbulence",
                "trait_tags": {"Aeronautical-Eng": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.36, "Technical-Skill": 0.32, "Industrial-Ops": 0.2, "Civil-Build": 0.16}
            },
            {
                "option_id": 3262,
                "option_text": "Dirty data and biased algorithms",
                "trait_tags": {"Data-Analytics": 1.0, "AI-ML": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Software-Dev": 0.3, "Lab-Research": 0.25}
            },
            {
                "option_id": 3263,
                "option_text": "Signal noise and electromagnetic interference",
                "trait_tags": {"Electronics-Dev": 1.0, "Electrical-Power": 0.8, "Technical-Skill": 0.36, "Realistic": 0.32, "Hardware-Systems": 0.24, "Mechanical-Design": 0.16}
            },
            {
                "option_id": 3264,
                "option_text": "Friction and thermal expansion",
                "trait_tags": {"Mechanical-Design": 1.0, "Electrical-Power": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Industrial-Ops": 0.25, "Hardware-Systems": 0.24}
            },
            {
                "option_id": 3265,
                "option_text": "Power surges and voltage drops",
                "trait_tags": {"Electrical-Power": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3266,
                "option_text": "Short circuits and hardware bottlenecks",
                "trait_tags": {"Hardware-Systems": 1.0, "Electrical-Power": 0.8, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Mechanical-Design": 0.25}
            }
        ]
    },
    {
        "question_id": 332,
        "question_text": "What would you like to 'Optimize'?",
        "category": "Engineering CS - Optimization",
        "options": [
            {
                "option_id": 3267,
                "option_text": "A website's loading speed and responsiveness",
                "trait_tags": {"Software-Dev": 1.0, "Web-Dev": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25}
            },
            {
                "option_id": 3268,
                "option_text": "A bridge's weight-to-strength ratio",
                "trait_tags": {"Civil-Build": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Industrial-Ops": 0.2}
            },
            {
                "option_id": 3269,
                "option_text": "An aircraft's fuel consumption per passenger",
                "trait_tags": {"Aeronautical-Eng": 1.0, "Mechanical-Design": 0.8, "Data-Analytics": 0.8, "Realistic": 0.36, "Investigative": 0.36, "Analytical-Skill": 0.36}
            },
            {
                "option_id": 3270,
                "option_text": "A machine learning model's prediction accuracy",
                "trait_tags": {"Data-Analytics": 1.0, "Software-Dev": 0.8, "AI-ML": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Technical-Skill": 0.36}
            },
            {
                "option_id": 3271,
                "option_text": "A wireless router's signal range and stability",
                "trait_tags": {"Electronics-Dev": 1.0, "Hardware-Systems": 0.8, "Technical-Skill": 0.36, "Realistic": 0.32, "Electrical-Power": 0.24, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3272,
                "option_text": "A car's engine torque and horsepower",
                "trait_tags": {"Mechanical-Design": 1.0, "Aeronautical-Eng": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Industrial-Ops": 0.25, "Civil-Build": 0.2}
            },
            {
                "option_id": 3273,
                "option_text": "A city's energy consumption during peak hours",
                "trait_tags": {"Electrical-Power": 1.0, "Data-Analytics": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Investigative": 0.36, "Analytical-Skill": 0.36}
            },
            {
                "option_id": 3274,
                "option_text": "A computer's boot time and processing efficiency",
                "trait_tags": {"Hardware-Systems": 1.0, "Software-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Investigative": 0.32, "Electrical-Power": 0.3}
            }
        ]
    },
    {
        "question_id": 333,
        "question_text": "Which 'Field Trip' would you enjoy most?",
        "category": "Engineering CS - Field Trip",
        "options": [
            {
                "option_id": 3275,
                "option_text": "A visit to Google's or Microsoft's main campus",
                "trait_tags": {"Software-Dev": 1.0, "Web-Dev": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25}
            },
            {
                "option_id": 3276,
                "option_text": "A tour of a massive bridge under construction",
                "trait_tags": {"Civil-Build": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Industrial-Ops": 0.2}
            },
            {
                "option_id": 3277,
                "option_text": "A tour of an aerospace manufacturing facility",
                "trait_tags": {"Aeronautical-Eng": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.36, "Technical-Skill": 0.32, "Industrial-Ops": 0.2, "Civil-Build": 0.16}
            },
            {
                "option_id": 3278,
                "option_text": "A visit to a large stock exchange's data center",
                "trait_tags": {"Data-Analytics": 1.0, "Software-Dev": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Technical-Skill": 0.36, "Lab-Research": 0.25}
            },
            {
                "option_id": 3279,
                "option_text": "A trip to a semiconductor fabrication plant",
                "trait_tags": {"Electronics-Dev": 1.0, "Hardware-Systems": 0.8, "Technical-Skill": 0.36, "Realistic": 0.32, "Electrical-Power": 0.24, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3280,
                "option_text": "A tour of a car factory or robotics lab",
                "trait_tags": {"Mechanical-Design": 1.0, "Electronics-Dev": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Industrial-Ops": 0.25, "Civil-Build": 0.2}
            },
            {
                "option_id": 3281,
                "option_text": "A visit to a nuclear or geothermal power plant",
                "trait_tags": {"Electrical-Power": 1.0, "Mechanical-Design": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3, "Industrial-Ops": 0.2}
            },
            {
                "option_id": 3282,
                "option_text": "A visit to a massive server farm housing the internet",
                "trait_tags": {"Hardware-Systems": 1.0, "Software-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Investigative": 0.32, "Electrical-Power": 0.3}
            }
        ]
    },
    {
        "question_id": 334,
        "question_text": "Which 'Expert' would you want to have dinner with?",
        "category": "Engineering CS - Expert Dinner",
        "options": [
            {
                "option_id": 3283,
                "option_text": "Linus Torvalds (Creator of Linux)",
                "trait_tags": {"Software-Dev": 1.0, "Hardware-Systems": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Realistic": 0.32, "Data-Analytics": 0.3}
            },
            {
                "option_id": 3284,
                "option_text": "Gustave Eiffel (Designer of the Eiffel Tower)",
                "trait_tags": {"Civil-Build": 1.0, "Spatial-Design": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Artistic": 0.28, "Creative-Skill": 0.28}
            },
            {
                "option_id": 3285,
                "option_text": "Neil Armstrong (Aerospace explorer)",
                "trait_tags": {"Aeronautical-Eng": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.36, "Technical-Skill": 0.32, "Industrial-Ops": 0.2, "Civil-Build": 0.16}
            },
            {
                "option_id": 3286,
                "option_text": "Nate Silver (Data scientist and statistician)",
                "trait_tags": {"Data-Analytics": 1.0, "Software-Dev": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Technical-Skill": 0.36, "Lab-Research": 0.25}
            },
            {
                "option_id": 3287,
                "option_text": "Nikola Tesla (Electrical and radio pioneer)",
                "trait_tags": {"Electrical-Power": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3288,
                "option_text": "Henry Ford (Mechanical and industrial pioneer)",
                "trait_tags": {"Mechanical-Design": 1.0, "Industrial-Ops": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Analytical-Skill": 0.28, "Enterprising": 0.24}
            },
            {
                "option_id": 3289,
                "option_text": "Gordon Moore (Co-founder of Intel)",
                "trait_tags": {"Hardware-Systems": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Electrical-Power": 0.3, "Mechanical-Design": 0.25}
            },
            {
                "option_id": 3290,
                "option_text": "Guglielmo Marconi (Inventor of the radio)",
                "trait_tags": {"Electronics-Dev": 1.0, "Electrical-Power": 0.8, "Technical-Skill": 0.36, "Realistic": 0.32, "Hardware-Systems": 0.24, "Mechanical-Design": 0.16}
            }
        ]
    },
    {
        "question_id": 335,
        "question_text": "What kind of 'Tutorial' would you watch on YouTube?",
        "category": "Engineering CS - Tutorial",
        "options": [
            {
                "option_id": 3291,
                "option_text": "How to build a full-stack web app",
                "trait_tags": {"Software-Dev": 1.0, "Web-Dev": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25}
            },
            {
                "option_id": 3292,
                "option_text": "How to calculate structural stress using software",
                "trait_tags": {"Civil-Build": 1.0, "Software-Dev": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Investigative": 0.32, "Spatial-Design": 0.25}
            },
            {
                "option_id": 3293,
                "option_text": "How jet engines work and how to maintain them",
                "trait_tags": {"Aeronautical-Eng": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.36, "Technical-Skill": 0.32, "Industrial-Ops": 0.2, "Civil-Build": 0.16}
            },
            {
                "option_id": 3294,
                "option_text": "How to use Python for data visualization",
                "trait_tags": {"Data-Analytics": 1.0, "Software-Dev": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Technical-Skill": 0.36, "Lab-Research": 0.25}
            },
            {
                "option_id": 3295,
                "option_text": "How to design your own PCB for a smart device",
                "trait_tags": {"Electronics-Dev": 1.0, "Hardware-Systems": 0.8, "Technical-Skill": 0.36, "Realistic": 0.32, "Electrical-Power": 0.24, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3296,
                "option_text": "How to rebuild a transmission or engine",
                "trait_tags": {"Mechanical-Design": 1.0, "Aeronautical-Eng": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Industrial-Ops": 0.25, "Civil-Build": 0.2}
            },
            {
                "option_id": 3297,
                "option_text": "How to set up a home solar and battery system",
                "trait_tags": {"Electrical-Power": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3298,
                "option_text": "How to build a PC and optimize the airflow",
                "trait_tags": {"Hardware-Systems": 1.0, "Mechanical-Design": 0.8, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Electrical-Power": 0.3}
            }
        ]
    },
    {
        "question_id": 336,
        "question_text": "What would be your 'Dream Office' location?",
        "category": "Engineering CS - Dream Office",
        "options": [
            {
                "option_id": 3299,
                "option_text": "Silicon Valley, California",
                "trait_tags": {"Software-Dev": 1.0, "Web-Dev": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25}
            },
            {
                "option_id": 3300,
                "option_text": "A high-rise construction firm in Dubai",
                "trait_tags": {"Civil-Build": 1.0, "Spatial-Design": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Artistic": 0.28, "Creative-Skill": 0.28}
            },
            {
                "option_id": 3301,
                "option_text": "NASA or a Boeing facility in Seattle",
                "trait_tags": {"Aeronautical-Eng": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.36, "Technical-Skill": 0.32, "Industrial-Ops": 0.2, "Civil-Build": 0.16}
            },
            {
                "option_id": 3302,
                "option_text": "A Wall Street firm or tech hub in London",
                "trait_tags": {"Data-Analytics": 1.0, "Software-Dev": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Technical-Skill": 0.36, "Lab-Research": 0.25}
            },
            {
                "option_id": 3303,
                "option_text": "An electronics innovation hub in Shenzhen",
                "trait_tags": {"Electronics-Dev": 1.0, "Hardware-Systems": 0.8, "Technical-Skill": 0.36, "Realistic": 0.32, "Electrical-Power": 0.24, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3304,
                "option_text": "An automotive design studio in Germany",
                "trait_tags": {"Mechanical-Design": 1.0, "Industrial-Ops": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Analytical-Skill": 0.28, "Enterprising": 0.24}
            },
            {
                "option_id": 3305,
                "option_text": "A renewable energy research center in Iceland",
                "trait_tags": {"Electrical-Power": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3306,
                "option_text": "A hardware research lab in Taiwan or South Korea",
                "trait_tags": {"Hardware-Systems": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Electrical-Power": 0.3, "Mechanical-Design": 0.25}
            }
        ]
    },
    {
        "question_id": 337,
        "question_text": "Which 'Challenge' would you find most exciting?",
        "category": "Engineering CS - Challenge",
        "options": [
            {
                "option_id": 3307,
                "option_text": "Writing a program that can beat a chess grandmaster",
                "trait_tags": {"Software-Dev": 1.0, "Data-Analytics": 0.8, "AI-ML": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Analytical-Skill": 0.36}
            },
            {
                "option_id": 3308,
                "option_text": "Designing a building that can survive a Category 5 typhoon",
                "trait_tags": {"Civil-Build": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Industrial-Ops": 0.2}
            },
            {
                "option_id": 3309,
                "option_text": "Creating a plane that can fly non-stop around the world",
                "trait_tags": {"Aeronautical-Eng": 1.0, "Mechanical-Design": 0.8, "Electrical-Power": 0.8, "Realistic": 0.36, "Technical-Skill": 0.36, "Hardware-Systems": 0.24}
            },
            {
                "option_id": 3310,
                "option_text": "Predicting a stock market crash before it happens",
                "trait_tags": {"Data-Analytics": 1.0, "Software-Dev": 0.8, "AI-ML": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Technical-Skill": 0.36}
            },
            {
                "option_id": 3311,
                "option_text": "Designing a phone battery that lasts for a week",
                "trait_tags": {"Electronics-Dev": 1.0, "Electrical-Power": 0.8, "Technical-Skill": 0.36, "Realistic": 0.32, "Hardware-Systems": 0.24, "Mechanical-Design": 0.16}
            },
            {
                "option_id": 3312,
                "option_text": "Designing a robot that can perform delicate surgery",
                "trait_tags": {"Mechanical-Design": 1.0, "Electronics-Dev": 0.8, "Software-Dev": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Investigative": 0.32}
            },
            {
                "option_id": 3313,
                "option_text": "Preventing a total blackout during a massive storm",
                "trait_tags": {"Electrical-Power": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3314,
                "option_text": "Creating a computer that fits inside a ring",
                "trait_tags": {"Hardware-Systems": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Electrical-Power": 0.3, "Mechanical-Design": 0.25}
            }
        ]
    },
    {
        "question_id": 338,
        "question_text": "What's the 'Coolest' thing about your favorite field?",
        "category": "Engineering CS - Coolest Thing",
        "options": [
            {
                "option_id": 3315,
                "option_text": "Creating something from nothing with just code",
                "trait_tags": {"Software-Dev": 1.0, "Web-Dev": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25}
            },
            {
                "option_id": 3316,
                "option_text": "Building structures that will last for hundreds of years",
                "trait_tags": {"Civil-Build": 1.0, "Spatial-Design": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Artistic": 0.28, "Creative-Skill": 0.28}
            },
            {
                "option_id": 3317,
                "option_text": "The feeling of defying gravity with physics",
                "trait_tags": {"Aeronautical-Eng": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.36, "Technical-Skill": 0.32, "Industrial-Ops": 0.2, "Civil-Build": 0.16}
            },
            {
                "option_id": 3318,
                "option_text": "Being able to 'see the future' through data trends",
                "trait_tags": {"Data-Analytics": 1.0, "AI-ML": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Software-Dev": 0.3, "Lab-Research": 0.25}
            },
            {
                "option_id": 3319,
                "option_text": "Connecting the world through invisible signals",
                "trait_tags": {"Electronics-Dev": 1.0, "Electrical-Power": 0.8, "Technical-Skill": 0.36, "Realistic": 0.32, "Hardware-Systems": 0.24, "Mechanical-Design": 0.16}
            },
            {
                "option_id": 3320,
                "option_text": "Making cold metal come to life with movement",
                "trait_tags": {"Mechanical-Design": 1.0, "Electronics-Dev": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Industrial-Ops": 0.25, "Civil-Build": 0.2}
            },
            {
                "option_id": 3321,
                "option_text": "Managing the 'bloodstream' of civilization — electricity",
                "trait_tags": {"Electrical-Power": 1.0, "Civil-Build": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3322,
                "option_text": "Understanding the 'brain' of the machine — its hardware",
                "trait_tags": {"Hardware-Systems": 1.0, "Software-Dev": 0.8, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Investigative": 0.32}
            }
        ]
    },
    {
        "question_id": 339,
        "question_text": "If you were a superhero, what would be your 'Origin Story'?",
        "category": "Engineering CS - Origin Story",
        "options": [
            {
                "option_id": 3323,
                "option_text": "You were a brilliant hacker who stopped a cyber-war",
                "trait_tags": {"Software-Dev": 1.0, "Cyber-Defense": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 3324,
                "option_text": "You built a sanctuary city for people after a disaster",
                "trait_tags": {"Civil-Build": 1.0, "Spatial-Design": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Artistic": 0.28, "Creative-Skill": 0.28}
            },
            {
                "option_id": 3325,
                "option_text": "You were a test pilot for a revolutionary new jet",
                "trait_tags": {"Aeronautical-Eng": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.36, "Technical-Skill": 0.32, "Industrial-Ops": 0.2, "Civil-Build": 0.16}
            },
            {
                "option_id": 3326,
                "option_text": "You discovered a data pattern that revealed a hidden truth",
                "trait_tags": {"Data-Analytics": 1.0, "AI-ML": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Software-Dev": 0.3, "Lab-Research": 0.25}
            },
            {
                "option_id": 3327,
                "option_text": "You were struck by lightning and gained control of signals",
                "trait_tags": {"Electronics-Dev": 1.0, "Electrical-Power": 0.8, "Technical-Skill": 0.36, "Realistic": 0.32, "Hardware-Systems": 0.24, "Mechanical-Design": 0.16}
            },
            {
                "option_id": 3328,
                "option_text": "You built an armored suit powered by complex gears",
                "trait_tags": {"Mechanical-Design": 1.0, "Electrical-Power": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Industrial-Ops": 0.25, "Hardware-Systems": 0.24}
            },
            {
                "option_id": 3329,
                "option_text": "You saved a city by manually restarting the power grid",
                "trait_tags": {"Electrical-Power": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3330,
                "option_text": "You built your own supercomputer from spare parts",
                "trait_tags": {"Hardware-Systems": 1.0, "Software-Dev": 0.8, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Investigative": 0.32}
            }
        ]
    },
    {
        "question_id": 340,
        "question_text": "What would you like to see on your 'Resume'?",
        "category": "Engineering CS - Resume Goal",
        "options": [
            {
                "option_id": 3331,
                "option_text": "Expert in 5+ Programming Languages and Frameworks",
                "trait_tags": {"Software-Dev": 1.0, "Web-Dev": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25}
            },
            {
                "option_id": 3332,
                "option_text": "Lead Engineer for a major bridge or highway project",
                "trait_tags": {"Civil-Build": 1.0, "Spatial-Design": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Artistic": 0.28, "Creative-Skill": 0.28}
            },
            {
                "option_id": 3333,
                "option_text": "500+ Hours of flight simulation and engine design",
                "trait_tags": {"Aeronautical-Eng": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.36, "Technical-Skill": 0.32, "Industrial-Ops": 0.2, "Civil-Build": 0.16}
            },
            {
                "option_id": 3334,
                "option_text": "Master of Machine Learning and Predictive Modeling",
                "trait_tags": {"Data-Analytics": 1.0, "Software-Dev": 0.8, "AI-ML": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Technical-Skill": 0.36}
            },
            {
                "option_id": 3335,
                "option_text": "Specialist in RF Design and Wireless Communications",
                "trait_tags": {"Electronics-Dev": 1.0, "Electrical-Power": 0.8, "Technical-Skill": 0.36, "Realistic": 0.32, "Hardware-Systems": 0.24, "Mechanical-Design": 0.16}
            },
            {
                "option_id": 3336,
                "option_text": "Expert in Robotics, CNC Machining, and CAD/CAM",
                "trait_tags": {"Mechanical-Design": 1.0, "Industrial-Ops": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Analytical-Skill": 0.28, "Enterprising": 0.24}
            },
            {
                "option_id": 3337,
                "option_text": "Professional Engineer specializing in Power Distribution",
                "trait_tags": {"Electrical-Power": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3338,
                "option_text": "Hardware Architect for high-performance computing",
                "trait_tags": {"Hardware-Systems": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Electrical-Power": 0.3, "Mechanical-Design": 0.25}
            }
        ]
    },
    {
        "question_id": 341,
        "question_text": "What do you do when you see a 'Warning Light' on a system?",
        "category": "Engineering CS - Warning Light",
        "options": [
            {
                "option_id": 3339,
                "option_text": "Check the system logs for an error code",
                "trait_tags": {"Software-Dev": 1.0, "Data-Analytics": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Analytical-Skill": 0.36, "Cyber-Defense": 0.25}
            },
            {
                "option_id": 3340,
                "option_text": "Look for physical cracks or signs of structural stress",
                "trait_tags": {"Civil-Build": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Industrial-Ops": 0.2}
            },
            {
                "option_id": 3341,
                "option_text": "Check the altimeter and fuel pressure immediately",
                "trait_tags": {"Aeronautical-Eng": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.36, "Technical-Skill": 0.32, "Industrial-Ops": 0.2, "Civil-Build": 0.16}
            },
            {
                "option_id": 3342,
                "option_text": "Run a diagnostic report to see where the data is failing",
                "trait_tags": {"Data-Analytics": 1.0, "Software-Dev": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Technical-Skill": 0.36, "Lab-Research": 0.25}
            },
            {
                "option_id": 3343,
                "option_text": "Use a signal tester to see if the frequency is drifting",
                "trait_tags": {"Electronics-Dev": 1.0, "Electrical-Power": 0.8, "Technical-Skill": 0.36, "Realistic": 0.32, "Hardware-Systems": 0.24, "Mechanical-Design": 0.16}
            },
            {
                "option_id": 3344,
                "option_text": "Listen for strange noises or vibrations in the machine",
                "trait_tags": {"Mechanical-Design": 1.0, "Industrial-Ops": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Analytical-Skill": 0.28, "Enterprising": 0.24}
            },
            {
                "option_id": 3345,
                "option_text": "Check the circuit breakers and transformer heat",
                "trait_tags": {"Electrical-Power": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3346,
                "option_text": "Open the case and look for a 'Q-Code' or red LED",
                "trait_tags": {"Hardware-Systems": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Electrical-Power": 0.3, "Mechanical-Design": 0.25}
            }
        ]
    },
    {
        "question_id": 342,
        "question_text": "Which 'Future Tech' are you most excited for?",
        "category": "Engineering CS - Future Tech",
        "options": [
            {
                "option_id": 3347,
                "option_text": "Quantum Computing and self-writing code",
                "trait_tags": {"Software-Dev": 1.0, "Hardware-Systems": 0.8, "AI-ML": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Analytical-Skill": 0.36}
            },
            {
                "option_id": 3348,
                "option_text": "3D-Printed houses and self-healing concrete",
                "trait_tags": {"Civil-Build": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Industrial-Ops": 0.2}
            },
            {
                "option_id": 3349,
                "option_text": "Personal flying vehicles and hypersonic travel",
                "trait_tags": {"Aeronautical-Eng": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.36, "Technical-Skill": 0.32, "Industrial-Ops": 0.2, "Civil-Build": 0.16}
            },
            {
                "option_id": 3350,
                "option_text": "Real-time global prediction systems for everything",
                "trait_tags": {"Data-Analytics": 1.0, "Software-Dev": 0.8, "AI-ML": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Technical-Skill": 0.36}
            },
            {
                "option_id": 3351,
                "option_text": "6G and holographic communication systems",
                "trait_tags": {"Electronics-Dev": 1.0, "Electrical-Power": 0.8, "Technical-Skill": 0.36, "Realistic": 0.32, "Hardware-Systems": 0.24, "Mechanical-Design": 0.16}
            },
            {
                "option_id": 3352,
                "option_text": "Nanobots that can build things at a molecular level",
                "trait_tags": {"Mechanical-Design": 1.0, "Electronics-Dev": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Industrial-Ops": 0.25, "Civil-Build": 0.2}
            },
            {
                "option_id": 3353,
                "option_text": "Wireless power transmission through the air",
                "trait_tags": {"Electrical-Power": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3354,
                "option_text": "Optical computers that use light instead of electricity",
                "trait_tags": {"Hardware-Systems": 1.0, "Electrical-Power": 0.8, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Mechanical-Design": 0.25}
            }
        ]
    },
    {
        "question_id": 343,
        "question_text": "How do you handle a 'Big Project'?",
        "category": "Engineering CS - Big Project",
        "options": [
            {
                "option_id": 3355,
                "option_text": "Breaking it down into modules and writing unit tests",
                "trait_tags": {"Software-Dev": 1.0, "Data-Analytics": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Analytical-Skill": 0.36, "Cyber-Defense": 0.25}
            },
            {
                "option_id": 3356,
                "option_text": "Surveying the land and laying a solid foundation first",
                "trait_tags": {"Civil-Build": 1.0, "Spatial-Design": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Artistic": 0.28, "Creative-Skill": 0.28}
            },
            {
                "option_id": 3357,
                "option_text": "Starting with a small-scale model for wind-tunnel testing",
                "trait_tags": {"Aeronautical-Eng": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.36, "Technical-Skill": 0.32, "Industrial-Ops": 0.2, "Civil-Build": 0.16}
            },
            {
                "option_id": 3358,
                "option_text": "Collecting as much historical data as possible first",
                "trait_tags": {"Data-Analytics": 1.0, "Software-Dev": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Technical-Skill": 0.36, "Lab-Research": 0.25}
            },
            {
                "option_id": 3359,
                "option_text": "Simulating the circuit behavior on a computer first",
                "trait_tags": {"Electronics-Dev": 1.0, "Software-Dev": 0.8, "Technical-Skill": 0.36, "Investigative": 0.32, "Data-Analytics": 0.24, "Cyber-Defense": 0.2}
            },
            {
                "option_id": 3360,
                "option_text": "Sketching the mechanical movement and gear ratios first",
                "trait_tags": {"Mechanical-Design": 1.0, "Civil-Build": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Industrial-Ops": 0.25, "Electrical-Power": 0.2}
            },
            {
                "option_id": 3361,
                "option_text": "Mapping out the load requirements and wiring paths first",
                "trait_tags": {"Electrical-Power": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3362,
                "option_text": "Planning the hardware layout for maximum cooling",
                "trait_tags": {"Hardware-Systems": 1.0, "Mechanical-Design": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Electrical-Power": 0.3, "Software-Dev": 0.2}
            }
        ]
    },
    {
        "question_id": 344,
        "question_text": "What kind of 'Competition' would you enter?",
        "category": "Engineering CS - Competition",
        "options": [
            {
                "option_id": 3363,
                "option_text": "A 24-hour Hackathon to build a new app",
                "trait_tags": {"Software-Dev": 1.0, "Web-Dev": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25}
            },
            {
                "option_id": 3364,
                "option_text": "A bridge-building contest using limited materials",
                "trait_tags": {"Civil-Build": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Industrial-Ops": 0.2}
            },
            {
                "option_id": 3365,
                "option_text": "A design challenge for the fastest model airplane",
                "trait_tags": {"Aeronautical-Eng": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.36, "Technical-Skill": 0.32, "Industrial-Ops": 0.2, "Civil-Build": 0.16}
            },
            {
                "option_id": 3366,
                "option_text": "A Kaggle competition to predict house prices",
                "trait_tags": {"Data-Analytics": 1.0, "Software-Dev": 0.8, "AI-ML": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Technical-Skill": 0.36}
            },
            {
                "option_id": 3367,
                "option_text": "A competition to build the best long-range radio",
                "trait_tags": {"Electronics-Dev": 1.0, "Hardware-Systems": 0.8, "Technical-Skill": 0.36, "Realistic": 0.32, "Electrical-Power": 0.24, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3368,
                "option_text": "A 'BattleBots' tournament with custom-built robots",
                "trait_tags": {"Mechanical-Design": 1.0, "Electronics-Dev": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Industrial-Ops": 0.25, "Civil-Build": 0.2}
            },
            {
                "option_id": 3369,
                "option_text": "A contest to build the most efficient solar car",
                "trait_tags": {"Electrical-Power": 1.0, "Mechanical-Design": 0.8, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3}
            },
            {
                "option_id": 3370,
                "option_text": "A PC-building speed-run or overclocking battle",
                "trait_tags": {"Hardware-Systems": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Electrical-Power": 0.3, "Mechanical-Design": 0.25}
            }
        ]
    },
    {
        "question_id": 345,
        "question_text": "What is your 'Career Goal' for the next 10 years?",
        "category": "Engineering CS - Career Goal",
        "options": [
            {
                "option_id": 3371,
                "option_text": "To become a Senior Software Architect",
                "trait_tags": {"Software-Dev": 1.0, "Web-Dev": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25}
            },
            {
                "option_id": 3372,
                "option_text": "To manage large-scale urban development projects",
                "trait_tags": {"Civil-Build": 1.0, "Spatial-Design": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Artistic": 0.28, "Creative-Skill": 0.28}
            },
            {
                "option_id": 3373,
                "option_text": "To work at the forefront of space exploration tech",
                "trait_tags": {"Aeronautical-Eng": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.36, "Technical-Skill": 0.32, "Industrial-Ops": 0.2, "Civil-Build": 0.16}
            },
            {
                "option_id": 3374,
                "option_text": "To lead a data science team for a global company",
                "trait_tags": {"Data-Analytics": 1.0, "Software-Dev": 0.8, "AI-ML": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Technical-Skill": 0.36}
            },
            {
                "option_id": 3375,
                "option_text": "To invent a new way for devices to communicate",
                "trait_tags": {"Electronics-Dev": 1.0, "Hardware-Systems": 0.8, "Technical-Skill": 0.36, "Realistic": 0.32, "Electrical-Power": 0.24, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3376,
                "option_text": "To design the next generation of industrial robots",
                "trait_tags": {"Mechanical-Design": 1.0, "Electronics-Dev": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Industrial-Ops": 0.25, "Civil-Build": 0.2}
            },
            {
                "option_id": 3377,
                "option_text": "To help a country transition to 100% renewable energy",
                "trait_tags": {"Electrical-Power": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3378,
                "option_text": "To design the most powerful processor in the world",
                "trait_tags": {"Hardware-Systems": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Electrical-Power": 0.3, "Mechanical-Design": 0.25}
            }
        ]
    },
    {
        "question_id": 346,
        "question_text": "Which 'Disaster' would you work hardest to prevent?",
        "category": "Engineering CS - Disaster Prevention",
        "options": [
            {
                "option_id": 3379,
                "option_text": "A massive data breach of personal information",
                "trait_tags": {"Software-Dev": 1.0, "Cyber-Defense": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 3380,
                "option_text": "A dam failure or bridge collapse in a city",
                "trait_tags": {"Civil-Build": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Industrial-Ops": 0.2}
            },
            {
                "option_id": 3381,
                "option_text": "An engine failure during a commercial flight",
                "trait_tags": {"Aeronautical-Eng": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.36, "Technical-Skill": 0.32, "Industrial-Ops": 0.2, "Civil-Build": 0.16}
            },
            {
                "option_id": 3382,
                "option_text": "A global economic crash caused by bad algorithms",
                "trait_tags": {"Data-Analytics": 1.0, "Software-Dev": 0.8, "AI-ML": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Technical-Skill": 0.36}
            },
            {
                "option_id": 3383,
                "option_text": "A complete shutdown of the internet and radio signals",
                "trait_tags": {"Electronics-Dev": 1.0, "Hardware-Systems": 0.8, "Technical-Skill": 0.36, "Realistic": 0.32, "Electrical-Power": 0.24, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3384,
                "option_text": "A factory explosion caused by a mechanical failure",
                "trait_tags": {"Mechanical-Design": 1.0, "Electrical-Power": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Industrial-Ops": 0.25, "Hardware-Systems": 0.24}
            },
            {
                "option_id": 3385,
                "option_text": "A total grid blackout during a freezing winter",
                "trait_tags": {"Electrical-Power": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3386,
                "option_text": "A failure of a data center's cooling and backup systems",
                "trait_tags": {"Hardware-Systems": 1.0, "Electrical-Power": 0.8, "Mechanical-Design": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Software-Dev": 0.2}
            }
        ]
    },
    {
        "question_id": 347,
        "question_text": "What's your 'Technical Superpower' in a group project?",
        "category": "Engineering CS - Technical Superpower",
        "options": [
            {
                "option_id": 3387,
                "option_text": "Being the one who can fix any code-related bug",
                "trait_tags": {"Software-Dev": 1.0, "Web-Dev": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25}
            },
            {
                "option_id": 3388,
                "option_text": "Being the one who understands structural blueprints",
                "trait_tags": {"Civil-Build": 1.0, "Spatial-Design": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Artistic": 0.28, "Creative-Skill": 0.28}
            },
            {
                "option_id": 3389,
                "option_text": "Being the one who can fix the vehicle or flight path",
                "trait_tags": {"Aeronautical-Eng": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.36, "Technical-Skill": 0.32, "Industrial-Ops": 0.2, "Civil-Build": 0.16}
            },
            {
                "option_id": 3390,
                "option_text": "Being the one who can explain what the numbers mean",
                "trait_tags": {"Data-Analytics": 1.0, "Analytical-Skill": 0.8, "Investigative": 0.45, "Software-Dev": 0.3, "Lab-Research": 0.28, "Finance-Acct": 0.28}
            },
            {
                "option_id": 3391,
                "option_text": "Being the one who can solder and fix the circuit boards",
                "trait_tags": {"Electronics-Dev": 1.0, "Hardware-Systems": 0.8, "Technical-Skill": 0.36, "Realistic": 0.32, "Electrical-Power": 0.24, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3392,
                "option_text": "Being the one who can fix any mechanical part or tool",
                "trait_tags": {"Mechanical-Design": 1.0, "Industrial-Ops": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Analytical-Skill": 0.28, "Enterprising": 0.24}
            },
            {
                "option_id": 3393,
                "option_text": "Being the one who knows how to handle the wiring and power",
                "trait_tags": {"Electrical-Power": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3394,
                "option_text": "Being the one who knows how to optimize the computers",
                "trait_tags": {"Hardware-Systems": 1.0, "Software-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Investigative": 0.32, "Electrical-Power": 0.3}
            }
        ]
    },
    {
        "question_id": 348,
        "question_text": "What would you do if you found a 'Bug' in your work?",
        "category": "Engineering CS - Bug Fix",
        "options": [
            {
                "option_id": 3395,
                "option_text": "Trace the logic and write a patch for the code",
                "trait_tags": {"Software-Dev": 1.0, "Data-Analytics": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Analytical-Skill": 0.36, "Cyber-Defense": 0.25}
            },
            {
                "option_id": 3396,
                "option_text": "Re-calculate the load and reinforce the structural beam",
                "trait_tags": {"Civil-Build": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Industrial-Ops": 0.2}
            },
            {
                "option_id": 3397,
                "option_text": "Re-test the aerodynamic lift and adjust the wing flap",
                "trait_tags": {"Aeronautical-Eng": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.36, "Technical-Skill": 0.32, "Industrial-Ops": 0.2, "Civil-Build": 0.16}
            },
            {
                "option_id": 3398,
                "option_text": "Re-run the data cleaning process to find the error",
                "trait_tags": {"Data-Analytics": 1.0, "Software-Dev": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Technical-Skill": 0.36, "Lab-Research": 0.25}
            },
            {
                "option_id": 3399,
                "option_text": "Re-check the circuit diagram and replace the resistor",
                "trait_tags": {"Electronics-Dev": 1.0, "Electrical-Power": 0.8, "Technical-Skill": 0.36, "Realistic": 0.32, "Hardware-Systems": 0.24, "Mechanical-Design": 0.16}
            },
            {
                "option_id": 3400,
                "option_text": "Take the machine apart and replace the worn-out gear",
                "trait_tags": {"Mechanical-Design": 1.0, "Industrial-Ops": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Analytical-Skill": 0.28, "Enterprising": 0.24}
            },
            {
                "option_id": 3401,
                "option_text": "Trace the electrical short and replace the fuse or wire",
                "trait_tags": {"Electrical-Power": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3402,
                "option_text": "Re-seat the hardware components and check the BIOS",
                "trait_tags": {"Hardware-Systems": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Electrical-Power": 0.3, "Mechanical-Design": 0.25}
            }
        ]
    },
    {
        "question_id": 349,
        "question_text": "Which 'Device' are you most curious about inside?",
        "category": "Engineering CS - Device Curiosity",
        "options": [
            {
                "option_id": 3403,
                "option_text": "A server running a complex website or game",
                "trait_tags": {"Software-Dev": 1.0, "Hardware-Systems": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Realistic": 0.32, "Data-Analytics": 0.3}
            },
            {
                "option_id": 3404,
                "option_text": "A suspension bridge's cable tension system",
                "trait_tags": {"Civil-Build": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Industrial-Ops": 0.2}
            },
            {
                "option_id": 3405,
                "option_text": "A jet engine's turbine and combustion chamber",
                "trait_tags": {"Aeronautical-Eng": 1.0, "Mechanical-Design": 0.8, "Electrical-Power": 0.8, "Realistic": 0.36, "Technical-Skill": 0.36, "Hardware-Systems": 0.24}
            },
            {
                "option_id": 3406,
                "option_text": "A supercomputer's data processing array",
                "trait_tags": {"Data-Analytics": 1.0, "Software-Dev": 0.8, "Hardware-Systems": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Technical-Skill": 0.36}
            },
            {
                "option_id": 3407,
                "option_text": "A smartphone's antenna and transceiver system",
                "trait_tags": {"Electronics-Dev": 1.0, "Electrical-Power": 0.8, "Technical-Skill": 0.36, "Realistic": 0.32, "Hardware-Systems": 0.24, "Mechanical-Design": 0.16}
            },
            {
                "option_id": 3408,
                "option_text": "A luxury car's engine and transmission",
                "trait_tags": {"Mechanical-Design": 1.0, "Electrical-Power": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Industrial-Ops": 0.25, "Hardware-Systems": 0.24}
            },
            {
                "option_id": 3409,
                "option_text": "A smart home's electrical panel and solar inverter",
                "trait_tags": {"Electrical-Power": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3410,
                "option_text": "A laptop's motherboard and cooling system",
                "trait_tags": {"Hardware-Systems": 1.0, "Mechanical-Design": 0.8, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Electrical-Power": 0.3}
            }
        ]
    },
    {
        "question_id": 350,
        "question_text": "What would your 'Dream Job' title be?",
        "category": "Engineering CS - Dream Job Title",
        "options": [
            {
                "option_id": 3411,
                "option_text": "Chief Technology Officer (CTO)",
                "trait_tags": {"Software-Dev": 1.0, "Web-Dev": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25}
            },
            {
                "option_id": 3412,
                "option_text": "Principal Structural Engineer",
                "trait_tags": {"Civil-Build": 1.0, "Spatial-Design": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Artistic": 0.28, "Creative-Skill": 0.28}
            },
            {
                "option_id": 3413,
                "option_text": "Chief Aerospace Engineer",
                "trait_tags": {"Aeronautical-Eng": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.36, "Technical-Skill": 0.32, "Industrial-Ops": 0.2, "Civil-Build": 0.16}
            },
            {
                "option_id": 3414,
                "option_text": "Lead Data Scientist",
                "trait_tags": {"Data-Analytics": 1.0, "Software-Dev": 0.8, "AI-ML": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Technical-Skill": 0.36}
            },
            {
                "option_id": 3415,
                "option_text": "Senior Electronics Design Engineer",
                "trait_tags": {"Electronics-Dev": 1.0, "Electrical-Power": 0.8, "Technical-Skill": 0.36, "Realistic": 0.32, "Hardware-Systems": 0.24, "Mechanical-Design": 0.16}
            },
            {
                "option_id": 3416,
                "option_text": "Director of Robotics and Machinery",
                "trait_tags": {"Mechanical-Design": 1.0, "Industrial-Ops": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Analytical-Skill": 0.28, "Enterprising": 0.24}
            },
            {
                "option_id": 3417,
                "option_text": "Grid Operations Manager",
                "trait_tags": {"Electrical-Power": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3418,
                "option_text": "Computer Systems Hardware Architect",
                "trait_tags": {"Hardware-Systems": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Electrical-Power": 0.3, "Mechanical-Design": 0.25}
            }
        ]
    },
    {
        "question_id": 351,
        "question_text": "What's your favorite 'Engineering Concept'?",
        "category": "Engineering CS - Favorite Concept",
        "options": [
            {
                "option_id": 3419,
                "option_text": "Encapsulation and Object-Oriented Logic",
                "trait_tags": {"Software-Dev": 1.0, "Data-Analytics": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Analytical-Skill": 0.36, "Cyber-Defense": 0.25}
            },
            {
                "option_id": 3420,
                "option_text": "Tension, Compression, and Structural Equilibrium",
                "trait_tags": {"Civil-Build": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Industrial-Ops": 0.2}
            },
            {
                "option_id": 3421,
                "option_text": "Lift, Drag, and Bernoulli's Principle",
                "trait_tags": {"Aeronautical-Eng": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.36, "Technical-Skill": 0.32, "Industrial-Ops": 0.2, "Civil-Build": 0.16}
            },
            {
                "option_id": 3422,
                "option_text": "Regression, Correlation, and Probability",
                "trait_tags": {"Data-Analytics": 1.0, "Software-Dev": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Technical-Skill": 0.36, "Lab-Research": 0.25}
            },
            {
                "option_id": 3423,
                "option_text": "Frequency Modulation and Signal Amplification",
                "trait_tags": {"Electronics-Dev": 1.0, "Electrical-Power": 0.8, "Technical-Skill": 0.36, "Realistic": 0.32, "Hardware-Systems": 0.24, "Mechanical-Design": 0.16}
            },
            {
                "option_id": 3424,
                "option_text": "Torque, RPM, and Mechanical Advantage",
                "trait_tags": {"Mechanical-Design": 1.0, "Aeronautical-Eng": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Industrial-Ops": 0.25, "Civil-Build": 0.2}
            },
            {
                "option_id": 3425,
                "option_text": "Ohm's Law, Voltage, and Power Distribution",
                "trait_tags": {"Electrical-Power": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3426,
                "option_text": "Clock Speed, Latency, and Memory Bandwidth",
                "trait_tags": {"Hardware-Systems": 1.0, "Software-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Investigative": 0.32, "Electrical-Power": 0.3}
            }
        ]
    },
    {
        "question_id": 352,
        "question_text": "What kind of 'Problem' would you stay up all night to fix?",
        "category": "Engineering CS - All-Nighter Problem",
        "options": [
            {
                "option_id": 3427,
                "option_text": "A server that is being attacked by a virus or hacker",
                "trait_tags": {"Software-Dev": 1.0, "Cyber-Defense": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Hardware-Systems": 0.2}
            },
            {
                "option_id": 3428,
                "option_text": "A crack in a dam that is threatening a nearby town",
                "trait_tags": {"Civil-Build": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Industrial-Ops": 0.2}
            },
            {
                "option_id": 3429,
                "option_text": "A critical failure in a plane's flight-control software",
                "trait_tags": {"Aeronautical-Eng": 1.0, "Software-Dev": 0.8, "Electronics-Dev": 0.8, "Technical-Skill": 0.36, "Investigative": 0.32, "Data-Analytics": 0.24}
            },
            {
                "option_id": 3430,
                "option_text": "A massive error in a report going to the CEO",
                "trait_tags": {"Data-Analytics": 1.0, "Software-Dev": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Technical-Skill": 0.36, "Lab-Research": 0.25}
            },
            {
                "option_id": 3431,
                "option_text": "A radio station that has lost its signal",
                "trait_tags": {"Electronics-Dev": 1.0, "Electrical-Power": 0.8, "Technical-Skill": 0.36, "Realistic": 0.32, "Hardware-Systems": 0.24, "Mechanical-Design": 0.16}
            },
            {
                "option_id": 3432,
                "option_text": "A machine on an assembly line that has stopped",
                "trait_tags": {"Mechanical-Design": 1.0, "Industrial-Ops": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Analytical-Skill": 0.28, "Enterprising": 0.24}
            },
            {
                "option_id": 3433,
                "option_text": "A power outage during a major hospital operation",
                "trait_tags": {"Electrical-Power": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3434,
                "option_text": "A workstation that won't turn on before a deadline",
                "trait_tags": {"Hardware-Systems": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Electrical-Power": 0.3, "Mechanical-Design": 0.25}
            }
        ]
    },
    {
        "question_id": 353,
        "question_text": "How do you prefer to 'Visualize' your work?",
        "category": "Engineering CS - Visualization",
        "options": [
            {
                "option_id": 3435,
                "option_text": "Using flowcharts and UML diagrams",
                "trait_tags": {"Software-Dev": 1.0, "Data-Analytics": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Analytical-Skill": 0.36, "Cyber-Defense": 0.25}
            },
            {
                "option_id": 3436,
                "option_text": "Using 3D models and blueprints",
                "trait_tags": {"Civil-Build": 1.0, "Spatial-Design": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Artistic": 0.28, "Creative-Skill": 0.28}
            },
            {
                "option_id": 3437,
                "option_text": "Using wind-tunnel simulations and flight paths",
                "trait_tags": {"Aeronautical-Eng": 1.0, "Data-Analytics": 0.8, "Investigative": 0.36, "Analytical-Skill": 0.36, "Software-Dev": 0.24, "Lab-Research": 0.2}
            },
            {
                "option_id": 3438,
                "option_text": "Using pie charts, scatter plots, and heatmaps",
                "trait_tags": {"Data-Analytics": 1.0, "Software-Dev": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Technical-Skill": 0.36, "Lab-Research": 0.25}
            },
            {
                "option_id": 3439,
                "option_text": "Using circuit schematics and signal waveforms",
                "trait_tags": {"Electronics-Dev": 1.0, "Electrical-Power": 0.8, "Technical-Skill": 0.36, "Realistic": 0.32, "Hardware-Systems": 0.24, "Mechanical-Design": 0.16}
            },
            {
                "option_id": 3440,
                "option_text": "Using mechanical cross-sections and gear diagrams",
                "trait_tags": {"Mechanical-Design": 1.0, "Civil-Build": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Industrial-Ops": 0.25, "Electrical-Power": 0.2}
            },
            {
                "option_id": 3441,
                "option_text": "Using single-line diagrams and grid maps",
                "trait_tags": {"Electrical-Power": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3442,
                "option_text": "Using hardware block diagrams and motherboard layouts",
                "trait_tags": {"Hardware-Systems": 1.0, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Electrical-Power": 0.3, "Mechanical-Design": 0.25}
            }
        ]
    },
    {
        "question_id": 354,
        "question_text": "If you were to 'Innovate' something, what would it be?",
        "category": "Engineering CS - Innovation",
        "options": [
            {
                "option_id": 3443,
                "option_text": "A new programming language that is easy to learn",
                "trait_tags": {"Software-Dev": 1.0, "Web-Dev": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25}
            },
            {
                "option_id": 3444,
                "option_text": "A new material for roads that never gets potholes",
                "trait_tags": {"Civil-Build": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Spatial-Design": 0.25, "Industrial-Ops": 0.2}
            },
            {
                "option_id": 3445,
                "option_text": "A jet engine that runs on zero emissions",
                "trait_tags": {"Aeronautical-Eng": 1.0, "Mechanical-Design": 0.8, "Electrical-Power": 0.8, "Realistic": 0.36, "Technical-Skill": 0.36, "Hardware-Systems": 0.24}
            },
            {
                "option_id": 3446,
                "option_text": "A data tool that can perfectly predict the weather",
                "trait_tags": {"Data-Analytics": 1.0, "Software-Dev": 0.8, "AI-ML": 0.8, "Investigative": 0.45, "Analytical-Skill": 0.45, "Technical-Skill": 0.36}
            },
            {
                "option_id": 3447,
                "option_text": "A phone that never loses signal anywhere on Earth",
                "trait_tags": {"Electronics-Dev": 1.0, "Electrical-Power": 0.8, "Technical-Skill": 0.36, "Realistic": 0.32, "Hardware-Systems": 0.24, "Mechanical-Design": 0.16}
            },
            {
                "option_id": 3448,
                "option_text": "A robot that can do all your household chores",
                "trait_tags": {"Mechanical-Design": 1.0, "Electronics-Dev": 0.8, "Software-Dev": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Investigative": 0.32}
            },
            {
                "option_id": 3449,
                "option_text": "A battery that can power a whole house for a month",
                "trait_tags": {"Electrical-Power": 1.0, "Mechanical-Design": 0.8, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3}
            },
            {
                "option_id": 3450,
                "option_text": "A processor that never gets hot no matter the load",
                "trait_tags": {"Hardware-Systems": 1.0, "Mechanical-Design": 0.8, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Electrical-Power": 0.3}
            }
        ]
    },
    {
        "question_id": 355,
        "question_text": "What makes you 'Proud' of your work?",
        "category": "Engineering CS - Source of Pride",
        "options": [
            {
                "option_id": 3451,
                "option_text": "Knowing my code is helping people every day",
                "trait_tags": {"Software-Dev": 1.0, "Web-Dev": 0.8, "Technical-Skill": 0.45, "Investigative": 0.4, "Data-Analytics": 0.3, "Cyber-Defense": 0.25}
            },
            {
                "option_id": 3452,
                "option_text": "Seeing a structure I built standing tall in a city",
                "trait_tags": {"Civil-Build": 1.0, "Spatial-Design": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Artistic": 0.28, "Creative-Skill": 0.28}
            },
            {
                "option_id": 3453,
                "option_text": "Knowing I helped make air travel safer and faster",
                "trait_tags": {"Aeronautical-Eng": 1.0, "Mechanical-Design": 0.8, "Realistic": 0.36, "Technical-Skill": 0.32, "Industrial-Ops": 0.2, "Civil-Build": 0.16}
            },
            {
                "option_id": 3454,
                "option_text": "Helping people make better decisions through facts and data",
                "trait_tags": {"Data-Analytics": 1.0, "Analytical-Skill": 0.8, "Investigative": 0.45, "Software-Dev": 0.3, "Lab-Research": 0.28, "Finance-Acct": 0.28}
            },
            {
                "option_id": 3455,
                "option_text": "Knowing people can talk to each other because of my work",
                "trait_tags": {"Electronics-Dev": 1.0, "Electrical-Power": 0.8, "Technical-Skill": 0.36, "Realistic": 0.32, "Hardware-Systems": 0.24, "Mechanical-Design": 0.16}
            },
            {
                "option_id": 3456,
                "option_text": "Watching a machine I built move exactly as I planned",
                "trait_tags": {"Mechanical-Design": 1.0, "Electronics-Dev": 0.8, "Realistic": 0.45, "Technical-Skill": 0.4, "Industrial-Ops": 0.25, "Civil-Build": 0.2}
            },
            {
                "option_id": 3457,
                "option_text": "Knowing I helped keep the lights on for thousands of homes",
                "trait_tags": {"Electrical-Power": 1.0, "Civil-Build": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Hardware-Systems": 0.3, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 3458,
                "option_text": "Knowing I built the fastest and most reliable machine",
                "trait_tags": {"Hardware-Systems": 1.0, "Mechanical-Design": 0.8, "Electronics-Dev": 0.8, "Technical-Skill": 0.45, "Realistic": 0.4, "Electrical-Power": 0.3}
            }
        ]
    }
]

TRAIT_SECONDARY_MAP = {
    "AI-ML": [("Software-Dev", 0.8), ("Data-Analytics", 0.8), ("Environmental-Sci", 0.8), ("Teaching-Ed", 0.8), ("Cyber-Defense", 0.8), ("Law-Enforce", 0.8), ("Admin-Skill", 0.8), ("Animation-3D", 0.8), ("Environmental-Eng", 0.8), ("Public-Health", 0.8), ("Patient-Care", 0.8), ("Mobile-Dev", 0.8), ("Counseling", 0.8), ("Web-Dev", 0.8), ("Digital-Media", 0.8), ("Hardware-Systems", 0.8), ("Medical-Lab", 0.8), ("Finance-Acct", 0.8), ("Game-Dev", 0.8), ("Agri-Nature", 0.8), ("Startup-Venture", 0.8), ("Investigative", 0.45), ("Analytical-Skill", 0.45), ("Technical-Skill", 0.36), ("Social", 0.36), ("Conventional", 0.36), ("People-Skill", 0.36), ("Realistic", 0.36), ("Enterprising", 0.36), ("Lab-Research", 0.2)],
    "Admin-Skill": [("Finance-Acct", 0.8), ("Health-Admin", 0.8), ("Software-Dev", 0.8), ("People-Skill", 0.8), ("Startup-Venture", 0.8), ("Analytical-Skill", 0.8), ("Community-Serve", 0.8), ("Marketing-Sales", 0.8), ("Industrial-Ops", 0.8), ("Legal-Practice", 0.8), ("Sports-Ed", 0.8), ("Conventional", 0.45), ("Technical-Skill", 0.36), ("Investigative", 0.36), ("Social", 0.36), ("Enterprising", 0.36), ("Physical-Skill", 0.36), ("Hospitality-Svc", 0.32), ("Teaching-Ed", 0.32), ("Data-Analytics", 0.32)],
    "Aeronautical-Eng": [("Mechanical-Design", 0.8), ("Electronics-Dev", 0.8), ("Software-Dev", 0.8), ("Data-Analytics", 0.8), ("Electrical-Power", 0.8), ("Realistic", 0.36), ("Technical-Skill", 0.36), ("Investigative", 0.36), ("Analytical-Skill", 0.36), ("Hardware-Systems", 0.24), ("Industrial-Ops", 0.2), ("Lab-Research", 0.2), ("Civil-Build", 0.16)],
    "Agri-Nature": [("Physical-Skill", 0.8), ("Field-Research", 0.8), ("Lab-Research", 0.8), ("Environmental-Sci", 0.8), ("Maritime-Sea", 0.8), ("Technical-Skill", 0.8), ("Mechanical-Design", 0.8), ("Startup-Venture", 0.8), ("Hardware-Systems", 0.8), ("Marketing-Sales", 0.8), ("Nutrition-Diet", 0.8), ("Environmental-Eng", 0.8), ("Teaching-Ed", 0.8), ("Realistic", 0.45), ("Investigative", 0.36), ("Analytical-Skill", 0.36), ("Enterprising", 0.36), ("People-Skill", 0.36), ("Social", 0.36), ("Food-Science", 0.28), ("Law-Enforce", 0.24)],
    "Analytical-Skill": [("Teaching-Ed", 0.8), ("Data-Analytics", 0.8), ("Industrial-Ops", 0.8), ("Lab-Research", 0.8), ("Finance-Acct", 0.8), ("Software-Dev", 0.8), ("Visual-Design", 0.8), ("Investigative", 0.45), ("Social", 0.36), ("People-Skill", 0.36), ("Technical-Skill", 0.36), ("Conventional", 0.36), ("Artistic", 0.36), ("Creative-Skill", 0.36), ("Medical-Lab", 0.3)],
    "Animation-3D": [("Digital-Media", 0.8), ("Creative-Skill", 0.8), ("Game-Dev", 0.8), ("Visual-Design", 0.8), ("Tourism-Travel", 0.8), ("Film-Broadcast", 0.8), ("Software-Dev", 0.8), ("Spatial-Design", 0.8), ("Startup-Venture", 0.8), ("Hardware-Systems", 0.8), ("Artistic", 0.4), ("Technical-Skill", 0.36), ("Enterprising", 0.36)],
    "Civil-Build": [("Spatial-Design", 0.8), ("Mechanical-Design", 0.8), ("Industrial-Ops", 0.8), ("Field-Research", 0.8), ("Analytical-Skill", 0.8), ("Data-Analytics", 0.8), ("Community-Serve", 0.8), ("Environmental-Eng", 0.8), ("Environmental-Sci", 0.8), ("Physical-Skill", 0.8), ("Software-Dev", 0.8), ("Maritime-Sea", 0.8), ("Electrical-Power", 0.8), ("Realistic", 0.45), ("Technical-Skill", 0.4), ("Investigative", 0.36), ("Social", 0.36), ("People-Skill", 0.32), ("Artistic", 0.28), ("Creative-Skill", 0.28), ("Agri-Nature", 0.28), ("Hardware-Systems", 0.24)],
    "Cloud-Systems": [("Hardware-Systems", 0.8), ("Software-Dev", 0.8), ("Data-Analytics", 0.8), ("Web-Dev", 0.8), ("Cyber-Defense", 0.8), ("Admin-Skill", 0.8), ("Community-Serve", 0.8), ("Teaching-Ed", 0.8), ("Game-Dev", 0.8), ("AI-ML", 0.8), ("Digital-Media", 0.8), ("Startup-Venture", 0.8), ("Finance-Acct", 0.8), ("Technical-Skill", 0.45), ("Investigative", 0.36), ("Analytical-Skill", 0.36), ("Conventional", 0.36), ("Social", 0.36), ("People-Skill", 0.36), ("Enterprising", 0.36), ("Realistic", 0.32), ("Artistic", 0.32), ("Creative-Skill", 0.32)],
    "Community-Serve": [("People-Skill", 0.8), ("Teaching-Ed", 0.8), ("Admin-Skill", 0.8), ("Social-Work", 0.8), ("Physical-Skill", 0.8), ("Analytical-Skill", 0.8), ("Legal-Practice", 0.8), ("Public-Health", 0.8), ("Field-Research", 0.8), ("Agri-Nature", 0.8), ("Social", 0.45), ("Conventional", 0.36), ("Realistic", 0.36), ("Investigative", 0.36), ("Patient-Care", 0.32), ("Data-Analytics", 0.32), ("Enterprising", 0.28), ("Health-Admin", 0.28), ("Counseling", 0.24), ("Law-Enforce", 0.15)],
    "Counseling": [("People-Skill", 0.8), ("Teaching-Ed", 0.8), ("Patient-Care", 0.8), ("Analytical-Skill", 0.8), ("Rehab-Therapy", 0.8), ("Social-Work", 0.8), ("Community-Serve", 0.8), ("Web-Dev", 0.8), ("Data-Analytics", 0.8), ("Public-Health", 0.8), ("Lab-Research", 0.8), ("Admin-Skill", 0.8), ("Social", 0.45), ("Investigative", 0.36), ("Technical-Skill", 0.36), ("Conventional", 0.36), ("Hospitality-Svc", 0.32), ("Physical-Skill", 0.32)],
    "Creative-Skill": [("Visual-Design", 0.8), ("Film-Broadcast", 0.8), ("Game-Dev", 0.8), ("Teaching-Ed", 0.8), ("Startup-Venture", 0.8), ("Community-Serve", 0.8), ("People-Skill", 0.8), ("Analytical-Skill", 0.8), ("Artistic", 0.45), ("Digital-Media", 0.4), ("Social", 0.36), ("Enterprising", 0.36), ("Investigative", 0.36), ("Spatial-Design", 0.35)],
    "Culinary-Arts": [("Creative-Skill", 0.8), ("Hospitality-Svc", 0.8), ("Digital-Media", 0.8), ("Startup-Venture", 0.8), ("Tourism-Travel", 0.8), ("Film-Broadcast", 0.8), ("Food-Science", 0.8), ("Nutrition-Diet", 0.8), ("Teaching-Ed", 0.8), ("Artistic", 0.36), ("Enterprising", 0.36), ("People-Skill", 0.36), ("Social", 0.36), ("Visual-Design", 0.32), ("Investigative", 0.32)],
    "Cyber-Defense": [("Software-Dev", 0.8), ("Law-Enforce", 0.8), ("Data-Analytics", 0.8), ("Hardware-Systems", 0.8), ("Web-Dev", 0.8), ("Cloud-Systems", 0.8), ("Forensic-Sci", 0.8), ("Analytical-Skill", 0.8), ("Teaching-Ed", 0.8), ("Legal-Practice", 0.8), ("Startup-Venture", 0.8), ("Digital-Media", 0.8), ("Admin-Skill", 0.8), ("Technical-Skill", 0.4), ("Investigative", 0.36), ("Social", 0.36), ("People-Skill", 0.36), ("Enterprising", 0.36), ("Conventional", 0.36), ("Realistic", 0.32), ("Artistic", 0.32), ("Creative-Skill", 0.32), ("Physical-Skill", 0.28), ("Lab-Research", 0.28), ("Mobile-Dev", 0.24)],
    "Data-Analytics": [("Analytical-Skill", 0.8), ("Software-Dev", 0.8), ("Finance-Acct", 0.8), ("AI-ML", 0.8), ("Web-Dev", 0.8), ("Public-Health", 0.8), ("Field-Research", 0.8), ("HR-Management", 0.8), ("Environmental-Sci", 0.8), ("Mechanical-Design", 0.8), ("Marketing-Sales", 0.8), ("Health-Admin", 0.8), ("Admin-Skill", 0.8), ("Industrial-Ops", 0.8), ("Agri-Nature", 0.8), ("Visual-Design", 0.8), ("Game-Dev", 0.8), ("Digital-Media", 0.8), ("Teaching-Ed", 0.8), ("Civil-Build", 0.8), ("Sports-Ed", 0.8), ("Cloud-Systems", 0.8), ("Hardware-Systems", 0.8), ("Investigative", 0.45), ("Conventional", 0.36), ("Technical-Skill", 0.36), ("Social", 0.36), ("People-Skill", 0.36), ("Realistic", 0.36), ("Enterprising", 0.36), ("Artistic", 0.36), ("Creative-Skill", 0.36), ("Physical-Skill", 0.36), ("Lab-Research", 0.28)],
    "Digital-Media": [("Creative-Skill", 0.8), ("Visual-Design", 0.8), ("Animation-3D", 0.8), ("Game-Dev", 0.8), ("Marketing-Sales", 0.8), ("People-Skill", 0.8), ("Film-Broadcast", 0.8), ("Performing-Arts", 0.8), ("Hardware-Systems", 0.8), ("Culinary-Arts", 0.8), ("Teaching-Ed", 0.8), ("Tourism-Travel", 0.8), ("Sports-Ed", 0.8), ("Startup-Venture", 0.8), ("Artistic", 0.4), ("Technical-Skill", 0.36), ("Enterprising", 0.36), ("Social", 0.36), ("Physical-Skill", 0.36), ("Software-Dev", 0.32), ("Realistic", 0.32), ("Hospitality-Svc", 0.32), ("Spatial-Design", 0.28)],
    "Electrical-Power": [("Technical-Skill", 0.8), ("Hardware-Systems", 0.8), ("Mechanical-Design", 0.8), ("Industrial-Ops", 0.8), ("Civil-Build", 0.8), ("Maritime-Sea", 0.8), ("Law-Enforce", 0.8), ("Environmental-Eng", 0.8), ("Electronics-Dev", 0.8), ("Data-Analytics", 0.8), ("Realistic", 0.4), ("Analytical-Skill", 0.36), ("Investigative", 0.36), ("Software-Dev", 0.32), ("Physical-Skill", 0.32), ("Environmental-Sci", 0.28)],
    "Electronics-Dev": [("Hardware-Systems", 0.8), ("Electrical-Power", 0.8), ("Aeronautical-Eng", 0.8), ("Software-Dev", 0.8), ("Technical-Skill", 0.36), ("Realistic", 0.32), ("Investigative", 0.32), ("Data-Analytics", 0.24), ("Mechanical-Design", 0.2), ("Cyber-Defense", 0.2)],
    "Environmental-Eng": [("Environmental-Sci", 0.8), ("Industrial-Ops", 0.8), ("Lab-Research", 0.8), ("Electrical-Power", 0.8), ("Civil-Build", 0.8), ("Mechanical-Design", 0.8), ("Hardware-Systems", 0.8), ("Food-Science", 0.8), ("Agri-Nature", 0.8), ("Realistic", 0.4), ("Investigative", 0.36), ("Technical-Skill", 0.36), ("Analytical-Skill", 0.36), ("Field-Research", 0.32), ("Physical-Skill", 0.28)],
    "Environmental-Sci": [("Field-Research", 0.8), ("Environmental-Eng", 0.8), ("Lab-Research", 0.8), ("Agri-Nature", 0.8), ("Hospitality-Svc", 0.8), ("Community-Serve", 0.8), ("Maritime-Sea", 0.8), ("Data-Analytics", 0.8), ("Electrical-Power", 0.8), ("Legal-Practice", 0.8), ("Investigative", 0.45), ("People-Skill", 0.36), ("Realistic", 0.36), ("Technical-Skill", 0.36), ("Analytical-Skill", 0.36), ("Social", 0.36), ("Tourism-Travel", 0.32), ("Physical-Skill", 0.32), ("Enterprising", 0.28)],
    "Field-Research": [("Agri-Nature", 0.8), ("Physical-Skill", 0.8), ("Lab-Research", 0.8), ("Environmental-Sci", 0.8), ("Hardware-Systems", 0.8), ("Data-Analytics", 0.8), ("Community-Serve", 0.8), ("Civil-Build", 0.8), ("Maritime-Sea", 0.8), ("Investigative", 0.4), ("Analytical-Skill", 0.36), ("Realistic", 0.36), ("Technical-Skill", 0.36), ("Social", 0.36), ("People-Skill", 0.32)],
    "Film-Broadcast": [("Digital-Media", 0.8), ("Creative-Skill", 0.8), ("Visual-Design", 0.8), ("Analytical-Skill", 0.8), ("Community-Serve", 0.8), ("Environmental-Sci", 0.8), ("Animation-3D", 0.8), ("Tourism-Travel", 0.8), ("People-Skill", 0.8), ("Performing-Arts", 0.8), ("Admin-Skill", 0.8), ("Artistic", 0.4), ("Investigative", 0.36), ("Social", 0.36), ("Conventional", 0.36), ("Game-Dev", 0.28), ("Spatial-Design", 0.28), ("Technical-Skill", 0.2)],
    "Finance-Acct": [("Analytical-Skill", 0.8), ("Admin-Skill", 0.8), ("Startup-Venture", 0.8), ("Marketing-Sales", 0.8), ("Data-Analytics", 0.8), ("Hospitality-Svc", 0.8), ("Industrial-Ops", 0.8), ("Digital-Media", 0.8), ("Conventional", 0.45), ("Investigative", 0.36), ("Enterprising", 0.36), ("People-Skill", 0.36), ("Artistic", 0.32), ("Creative-Skill", 0.32), ("Tourism-Travel", 0.32)],
    "Food-Science": [("Lab-Research", 0.8), ("Analytical-Skill", 0.8), ("Nutrition-Diet", 0.8), ("Medical-Lab", 0.8), ("Culinary-Arts", 0.8), ("Legal-Practice", 0.8), ("Industrial-Ops", 0.8), ("Public-Health", 0.8), ("Health-Admin", 0.8), ("Agri-Nature", 0.8), ("Field-Research", 0.8), ("Environmental-Eng", 0.8), ("Creative-Skill", 0.8), ("Admin-Skill", 0.8), ("Startup-Venture", 0.8), ("Finance-Acct", 0.8), ("Investigative", 0.4), ("Conventional", 0.36), ("Realistic", 0.36), ("Artistic", 0.36), ("Enterprising", 0.36), ("Social", 0.32), ("Data-Analytics", 0.32)],
    "Forensic-Sci": [("Lab-Research", 0.8), ("Analytical-Skill", 0.8), ("Law-Enforce", 0.8), ("Medical-Lab", 0.8), ("Data-Analytics", 0.8), ("Cyber-Defense", 0.8), ("Legal-Practice", 0.8), ("Physical-Skill", 0.8), ("Film-Broadcast", 0.8), ("Pharmacy", 0.8), ("Visual-Design", 0.8), ("Finance-Acct", 0.8), ("Counseling", 0.8), ("People-Skill", 0.8), ("Environmental-Sci", 0.8), ("Admin-Skill", 0.8), ("Patient-Care", 0.8), ("Technical-Skill", 0.8), ("Digital-Media", 0.8), ("Investigative", 0.45), ("Artistic", 0.36), ("Creative-Skill", 0.36), ("Conventional", 0.36), ("Social", 0.36), ("Realistic", 0.28)],
    "Game-Dev": [("Hardware-Systems", 0.8), ("Software-Dev", 0.8), ("Creative-Skill", 0.8), ("Animation-3D", 0.8), ("Digital-Media", 0.8), ("Teaching-Ed", 0.8), ("People-Skill", 0.8), ("Finance-Acct", 0.8), ("AI-ML", 0.8), ("Analytical-Skill", 0.8), ("Film-Broadcast", 0.8), ("Cloud-Systems", 0.8), ("Mobile-Dev", 0.8), ("Visual-Design", 0.8), ("Data-Analytics", 0.8), ("Performing-Arts", 0.8), ("Marketing-Sales", 0.8), ("Startup-Venture", 0.8), ("Cyber-Defense", 0.8), ("Spatial-Design", 0.8), ("Technical-Skill", 0.4), ("Artistic", 0.36), ("Social", 0.36), ("Investigative", 0.36), ("Conventional", 0.36), ("Enterprising", 0.36)],
    "HR-Management": [("People-Skill", 0.8), ("Admin-Skill", 0.8), ("Teaching-Ed", 0.8), ("Counseling", 0.8), ("Creative-Skill", 0.8), ("Community-Serve", 0.8), ("Social-Work", 0.8), ("Hospitality-Svc", 0.8), ("Finance-Acct", 0.8), ("Software-Dev", 0.8), ("Legal-Practice", 0.8), ("Data-Analytics", 0.8), ("Marketing-Sales", 0.8), ("Startup-Venture", 0.8), ("Social", 0.36), ("Enterprising", 0.36), ("Artistic", 0.36), ("Conventional", 0.36), ("Technical-Skill", 0.36), ("Investigative", 0.36), ("Analytical-Skill", 0.36)],
    "Hardware-Systems": [("Electrical-Power", 0.8), ("Mechanical-Design", 0.8), ("Software-Dev", 0.8), ("Cloud-Systems", 0.8), ("Agri-Nature", 0.8), ("Law-Enforce", 0.8), ("Civil-Build", 0.8), ("Environmental-Eng", 0.8), ("Public-Health", 0.8), ("Patient-Care", 0.8), ("Data-Analytics", 0.8), ("Environmental-Sci", 0.8), ("Electronics-Dev", 0.8), ("Technical-Skill", 0.45), ("Realistic", 0.4), ("Investigative", 0.36), ("People-Skill", 0.36), ("Analytical-Skill", 0.36), ("Social", 0.32), ("Field-Research", 0.32), ("Physical-Skill", 0.28)],
    "Health-Admin": [("Admin-Skill", 0.8), ("Finance-Acct", 0.8), ("Software-Dev", 0.8), ("Teaching-Ed", 0.8), ("Analytical-Skill", 0.8), ("Public-Health", 0.8), ("Cyber-Defense", 0.8), ("Data-Analytics", 0.8), ("Hardware-Systems", 0.8), ("Lab-Research", 0.8), ("Community-Serve", 0.8), ("Conventional", 0.4), ("Technical-Skill", 0.36), ("Investigative", 0.36), ("Social", 0.36), ("People-Skill", 0.36), ("Realistic", 0.32), ("Hospitality-Svc", 0.16), ("Startup-Venture", 0.16), ("Patient-Care", 0.15)],
    "Hospitality-Svc": [("People-Skill", 0.8), ("Tourism-Travel", 0.8), ("Culinary-Arts", 0.8), ("Marketing-Sales", 0.8), ("Admin-Skill", 0.8), ("HR-Management", 0.8), ("Enterprising", 0.36), ("Social", 0.36), ("Conventional", 0.36), ("Teaching-Ed", 0.32), ("Creative-Skill", 0.28)],
    "Industrial-Ops": [("Analytical-Skill", 0.8), ("Mechanical-Design", 0.8), ("Admin-Skill", 0.8), ("Data-Analytics", 0.8), ("Food-Science", 0.8), ("Lab-Research", 0.8), ("Maritime-Sea", 0.8), ("Spatial-Design", 0.8), ("Hardware-Systems", 0.8), ("Teaching-Ed", 0.8), ("Realistic", 0.36), ("Technical-Skill", 0.36), ("Conventional", 0.36), ("Investigative", 0.36), ("Social", 0.36), ("People-Skill", 0.36), ("Physical-Skill", 0.32), ("Enterprising", 0.3), ("Finance-Acct", 0.28), ("Artistic", 0.28), ("Creative-Skill", 0.28)],
    "Lab-Research": [("Analytical-Skill", 0.8), ("Medical-Lab", 0.8), ("Field-Research", 0.8), ("Environmental-Sci", 0.8), ("Teaching-Ed", 0.8), ("AI-ML", 0.8), ("Legal-Practice", 0.8), ("Film-Broadcast", 0.8), ("Forensic-Sci", 0.8), ("Digital-Media", 0.8), ("Investigative", 0.45), ("Social", 0.36), ("People-Skill", 0.36), ("Data-Analytics", 0.32), ("Artistic", 0.32), ("Creative-Skill", 0.32), ("Enterprising", 0.28), ("Law-Enforce", 0.28)],
    "Law-Enforce": [("Physical-Skill", 0.8), ("Community-Serve", 0.8), ("Cyber-Defense", 0.8), ("Analytical-Skill", 0.8), ("Data-Analytics", 0.8), ("Forensic-Sci", 0.8), ("People-Skill", 0.8), ("Counseling", 0.8), ("Admin-Skill", 0.8), ("Investigative", 0.36), ("Social", 0.36), ("Conventional", 0.36), ("Realistic", 0.35), ("Patient-Care", 0.32), ("Technical-Skill", 0.32), ("Health-Admin", 0.28), ("Rehab-Therapy", 0.24)],
    "Legal-Practice": [("Analytical-Skill", 0.8), ("People-Skill", 0.8), ("Community-Serve", 0.8), ("Admin-Skill", 0.8), ("Environmental-Sci", 0.8), ("Social-Work", 0.8), ("Law-Enforce", 0.8), ("Finance-Acct", 0.8), ("HR-Management", 0.8), ("Cyber-Defense", 0.8), ("Creative-Skill", 0.8), ("Investigative", 0.36), ("Social", 0.36), ("Conventional", 0.36), ("Artistic", 0.36), ("Enterprising", 0.35), ("Data-Analytics", 0.32), ("Field-Research", 0.32), ("Patient-Care", 0.32), ("Technical-Skill", 0.32), ("Realistic", 0.28)],
    "Maritime-Sea": [("Physical-Skill", 0.8), ("Technical-Skill", 0.8), ("Mechanical-Design", 0.8), ("Agri-Nature", 0.8), ("Industrial-Ops", 0.8), ("Admin-Skill", 0.8), ("Tourism-Travel", 0.8), ("People-Skill", 0.8), ("Hospitality-Svc", 0.8), ("Field-Research", 0.8), ("Community-Serve", 0.8), ("Environmental-Sci", 0.8), ("Electrical-Power", 0.8), ("Hardware-Systems", 0.8), ("Analytical-Skill", 0.8), ("Legal-Practice", 0.8), ("Civil-Build", 0.8), ("Data-Analytics", 0.8), ("Marketing-Sales", 0.8), ("Realistic", 0.45), ("Conventional", 0.36), ("Social", 0.36), ("Investigative", 0.36), ("Enterprising", 0.36), ("Lab-Research", 0.28), ("Law-Enforce", 0.24), ("Spatial-Design", 0.2)],
    "Marketing-Sales": [("People-Skill", 0.8), ("Startup-Venture", 0.8), ("Creative-Skill", 0.8), ("Admin-Skill", 0.8), ("Digital-Media", 0.8), ("Community-Serve", 0.8), ("Film-Broadcast", 0.8), ("Agri-Nature", 0.8), ("Pharmacy", 0.8), ("Analytical-Skill", 0.8), ("Enterprising", 0.45), ("Social", 0.36), ("Artistic", 0.36), ("Conventional", 0.36), ("Realistic", 0.36), ("Investigative", 0.36), ("Hospitality-Svc", 0.32), ("Teaching-Ed", 0.32), ("Visual-Design", 0.32), ("Data-Analytics", 0.32), ("Finance-Acct", 0.16)],
    "Mechanical-Design": [("Technical-Skill", 0.8), ("Industrial-Ops", 0.8), ("Civil-Build", 0.8), ("Electrical-Power", 0.8), ("Hardware-Systems", 0.8), ("Physical-Skill", 0.8), ("Agri-Nature", 0.8), ("Software-Dev", 0.8), ("Lab-Research", 0.8), ("Environmental-Eng", 0.8), ("Rehab-Therapy", 0.8), ("Maritime-Sea", 0.8), ("Aeronautical-Eng", 0.8), ("Electronics-Dev", 0.8), ("Realistic", 0.45), ("Analytical-Skill", 0.36), ("Investigative", 0.36), ("Environmental-Sci", 0.28), ("Social", 0.28), ("Enterprising", 0.24)],
    "Medical-Lab": [("Analytical-Skill", 0.8), ("Lab-Research", 0.8), ("Technical-Skill", 0.8), ("Patient-Care", 0.8), ("Food-Science", 0.8), ("Hardware-Systems", 0.8), ("Environmental-Sci", 0.8), ("Pharmacy", 0.8), ("Investigative", 0.4), ("People-Skill", 0.36), ("Software-Dev", 0.32), ("Data-Analytics", 0.32), ("Field-Research", 0.32), ("Nutrition-Diet", 0.28), ("Finance-Acct", 0.28)],
    "Mobile-Dev": [("AI-ML", 0.8), ("Software-Dev", 0.8), ("Web-Dev", 0.8), ("Game-Dev", 0.8), ("Startup-Venture", 0.8), ("Patient-Care", 0.8), ("Finance-Acct", 0.8), ("Agri-Nature", 0.8), ("Visual-Design", 0.8), ("Creative-Skill", 0.8), ("Sports-Ed", 0.8), ("Environmental-Sci", 0.8), ("Law-Enforce", 0.8), ("Tourism-Travel", 0.8), ("Public-Health", 0.8), ("Marketing-Sales", 0.8), ("Data-Analytics", 0.8), ("Cyber-Defense", 0.8), ("Electrical-Power", 0.8), ("Nutrition-Diet", 0.8), ("Teaching-Ed", 0.8), ("Community-Serve", 0.8), ("Technical-Skill", 0.45), ("Investigative", 0.36), ("Analytical-Skill", 0.36), ("Enterprising", 0.36), ("People-Skill", 0.36), ("Conventional", 0.36), ("Realistic", 0.36), ("Artistic", 0.36), ("Physical-Skill", 0.36), ("Social", 0.36), ("Field-Research", 0.32)],
    "Nutrition-Diet": [("Patient-Care", 0.8), ("Food-Science", 0.8), ("Public-Health", 0.8), ("Community-Serve", 0.8), ("Culinary-Arts", 0.8), ("Lab-Research", 0.8), ("Social-Work", 0.8), ("Teaching-Ed", 0.8), ("Rehab-Therapy", 0.8), ("Sports-Ed", 0.8), ("People-Skill", 0.36), ("Social", 0.36), ("Analytical-Skill", 0.36), ("Investigative", 0.36), ("Physical-Skill", 0.36), ("Creative-Skill", 0.28)],
    "Patient-Care": [("People-Skill", 0.8), ("Community-Serve", 0.8), ("Medical-Lab", 0.8), ("Teaching-Ed", 0.8), ("Physical-Skill", 0.8), ("Public-Health", 0.8), ("Counseling", 0.8), ("Lab-Research", 0.8), ("Social-Work", 0.8), ("Pharmacy", 0.8), ("Maritime-Sea", 0.8), ("Health-Admin", 0.8), ("Social", 0.4), ("Realistic", 0.36), ("Analytical-Skill", 0.36), ("Investigative", 0.36), ("Admin-Skill", 0.36), ("Hospitality-Svc", 0.32), ("Conventional", 0.32), ("Rehab-Therapy", 0.3)],
    "People-Skill": [("Teaching-Ed", 0.8), ("Hospitality-Svc", 0.8), ("Analytical-Skill", 0.8), ("Admin-Skill", 0.8), ("Performing-Arts", 0.8), ("Counseling", 0.8), ("Physical-Skill", 0.8), ("HR-Management", 0.8), ("Legal-Practice", 0.8), ("Sports-Ed", 0.8), ("Marketing-Sales", 0.8), ("Community-Serve", 0.8), ("Social", 0.45), ("Patient-Care", 0.4), ("Tourism-Travel", 0.32), ("Enterprising", 0.3)],
    "Performing-Arts": [("People-Skill", 0.8), ("Creative-Skill", 0.8), ("Digital-Media", 0.8), ("Film-Broadcast", 0.8), ("Admin-Skill", 0.8), ("Game-Dev", 0.8), ("Physical-Skill", 0.8), ("Animation-3D", 0.8), ("Sports-Ed", 0.8), ("Artistic", 0.45), ("Social", 0.36), ("Conventional", 0.36), ("Teaching-Ed", 0.32), ("Visual-Design", 0.32), ("Technical-Skill", 0.32), ("Software-Dev", 0.32), ("Realistic", 0.32)],
    "Pharmacy": [("Medical-Lab", 0.8), ("Analytical-Skill", 0.8), ("Lab-Research", 0.8), ("Patient-Care", 0.8), ("Public-Health", 0.8), ("Admin-Skill", 0.8), ("People-Skill", 0.8), ("Legal-Practice", 0.8), ("Field-Research", 0.8), ("Community-Serve", 0.8), ("Teaching-Ed", 0.8), ("Health-Admin", 0.8), ("Finance-Acct", 0.8), ("Marketing-Sales", 0.8), ("Startup-Venture", 0.8), ("Industrial-Ops", 0.8), ("Investigative", 0.4), ("Social", 0.36), ("Conventional", 0.36), ("Enterprising", 0.36), ("Data-Analytics", 0.32)],
    "Physical-Skill": [("Law-Enforce", 0.8), ("Sports-Ed", 0.8), ("Tourism-Travel", 0.8), ("Community-Serve", 0.8), ("Mechanical-Design", 0.8), ("Teaching-Ed", 0.8), ("Realistic", 0.4), ("People-Skill", 0.36), ("Social", 0.36), ("Maritime-Sea", 0.35), ("Agri-Nature", 0.35), ("Technical-Skill", 0.32), ("Rehab-Therapy", 0.3)],
    "Public-Health": [("Community-Serve", 0.8), ("Patient-Care", 0.8), ("Environmental-Sci", 0.8), ("Data-Analytics", 0.8), ("Civil-Build", 0.8), ("Physical-Skill", 0.8), ("Marketing-Sales", 0.8), ("Teaching-Ed", 0.8), ("Visual-Design", 0.8), ("Social", 0.4), ("Analytical-Skill", 0.36), ("People-Skill", 0.36), ("Investigative", 0.36), ("Realistic", 0.36), ("Enterprising", 0.36), ("Artistic", 0.36), ("Creative-Skill", 0.36)],
    "Rehab-Therapy": [("Physical-Skill", 0.8), ("People-Skill", 0.8), ("Patient-Care", 0.8), ("Teaching-Ed", 0.8), ("Counseling", 0.8), ("Sports-Ed", 0.8), ("Hospitality-Svc", 0.8), ("Social", 0.36), ("Realistic", 0.32), ("Tourism-Travel", 0.32)],
    "Social-Work": [("People-Skill", 0.8), ("Community-Serve", 0.8), ("Teaching-Ed", 0.8), ("Patient-Care", 0.8), ("Counseling", 0.8), ("Admin-Skill", 0.8), ("Startup-Venture", 0.8), ("HR-Management", 0.8), ("Nutrition-Diet", 0.8), ("Legal-Practice", 0.8), ("Digital-Media", 0.8), ("Rehab-Therapy", 0.8), ("Law-Enforce", 0.8), ("Social", 0.45), ("Conventional", 0.36), ("Enterprising", 0.36), ("Artistic", 0.32), ("Physical-Skill", 0.32)],
    "Software-Dev": [("Technical-Skill", 0.8), ("Data-Analytics", 0.8), ("Cyber-Defense", 0.8), ("Hardware-Systems", 0.8), ("Web-Dev", 0.8), ("Analytical-Skill", 0.8), ("Lab-Research", 0.8), ("Public-Health", 0.8), ("Environmental-Eng", 0.8), ("Finance-Acct", 0.8), ("Startup-Venture", 0.8), ("Teaching-Ed", 0.8), ("Film-Broadcast", 0.8), ("Digital-Media", 0.8), ("AI-ML", 0.8), ("Cloud-Systems", 0.8), ("Mechanical-Design", 0.8), ("Game-Dev", 0.8), ("Admin-Skill", 0.8), ("Hospitality-Svc", 0.8), ("Mobile-Dev", 0.8), ("Investigative", 0.4), ("Social", 0.36), ("Realistic", 0.36), ("Conventional", 0.36), ("Enterprising", 0.36), ("People-Skill", 0.36), ("Artistic", 0.32), ("Creative-Skill", 0.32)],
    "Spatial-Design": [("Creative-Skill", 0.8), ("Civil-Build", 0.8), ("Visual-Design", 0.8), ("Marketing-Sales", 0.8), ("Environmental-Sci", 0.8), ("Environmental-Eng", 0.8), ("Hardware-Systems", 0.8), ("Community-Serve", 0.8), ("Animation-3D", 0.8), ("Artistic", 0.36), ("Technical-Skill", 0.36), ("Realistic", 0.36), ("Enterprising", 0.36), ("Investigative", 0.36), ("Social", 0.36), ("Digital-Media", 0.32), ("People-Skill", 0.32), ("Field-Research", 0.32), ("Game-Dev", 0.28)],
    "Sports-Ed": [("Physical-Skill", 0.8), ("Teaching-Ed", 0.8), ("People-Skill", 0.8), ("Rehab-Therapy", 0.8), ("Admin-Skill", 0.8), ("Counseling", 0.8), ("Startup-Venture", 0.8), ("Community-Serve", 0.8), ("Film-Broadcast", 0.8), ("Public-Health", 0.8), ("Marketing-Sales", 0.8), ("Patient-Care", 0.8), ("Nutrition-Diet", 0.8), ("Social", 0.36), ("Conventional", 0.36), ("Enterprising", 0.36), ("Realistic", 0.32), ("Artistic", 0.32), ("Maritime-Sea", 0.28), ("Analytical-Skill", 0.28), ("Food-Science", 0.28)],
    "Startup-Venture": [("People-Skill", 0.8), ("Marketing-Sales", 0.8), ("Finance-Acct", 0.8), ("Community-Serve", 0.8), ("Admin-Skill", 0.8), ("Web-Dev", 0.8), ("Software-Dev", 0.8), ("Teaching-Ed", 0.8), ("Film-Broadcast", 0.8), ("Enterprising", 0.45), ("Conventional", 0.36), ("Social", 0.36), ("Technical-Skill", 0.36), ("Creative-Skill", 0.32), ("Analytical-Skill", 0.32), ("Artistic", 0.32), ("Digital-Media", 0.32), ("Investigative", 0.32), ("Hospitality-Svc", 0.32)],
    "Teaching-Ed": [("People-Skill", 0.8), ("Community-Serve", 0.8), ("Analytical-Skill", 0.8), ("Lab-Research", 0.8), ("Technical-Skill", 0.8), ("Counseling", 0.8), ("Admin-Skill", 0.8), ("Creative-Skill", 0.8), ("Cyber-Defense", 0.8), ("Industrial-Ops", 0.8), ("Software-Dev", 0.8), ("Public-Health", 0.8), ("Social-Work", 0.8), ("Web-Dev", 0.8), ("Social", 0.45), ("Investigative", 0.36), ("Conventional", 0.36), ("Artistic", 0.36), ("Patient-Care", 0.32), ("Hospitality-Svc", 0.32), ("Visual-Design", 0.32), ("Realistic", 0.28), ("Health-Admin", 0.28), ("Rehab-Therapy", 0.2)],
    "Technical-Skill": [("Software-Dev", 0.8), ("Hardware-Systems", 0.8), ("Mechanical-Design", 0.8), ("Analytical-Skill", 0.8), ("Admin-Skill", 0.8), ("Electrical-Power", 0.8), ("Industrial-Ops", 0.8), ("Civil-Build", 0.8), ("Cloud-Systems", 0.8), ("Environmental-Eng", 0.8), ("Realistic", 0.36), ("Investigative", 0.36), ("Conventional", 0.36)],
    "Tourism-Travel": [("Marketing-Sales", 0.8), ("People-Skill", 0.8), ("Hospitality-Svc", 0.8), ("Startup-Venture", 0.8), ("Teaching-Ed", 0.8), ("Culinary-Arts", 0.8), ("Film-Broadcast", 0.8), ("Field-Research", 0.8), ("Environmental-Sci", 0.8), ("Community-Serve", 0.8), ("Visual-Design", 0.8), ("Physical-Skill", 0.8), ("Digital-Media", 0.8), ("Admin-Skill", 0.8), ("Web-Dev", 0.8), ("Finance-Acct", 0.8), ("Law-Enforce", 0.8), ("Enterprising", 0.36), ("Social", 0.36), ("Artistic", 0.36), ("Investigative", 0.36), ("Creative-Skill", 0.36), ("Conventional", 0.36), ("Technical-Skill", 0.36), ("Realistic", 0.32)],
    "Visual-Design": [("Creative-Skill", 0.8), ("Digital-Media", 0.8), ("Spatial-Design", 0.8), ("Animation-3D", 0.8), ("Game-Dev", 0.8), ("Film-Broadcast", 0.8), ("Marketing-Sales", 0.8), ("Law-Enforce", 0.8), ("Startup-Venture", 0.8), ("Performing-Arts", 0.8), ("Web-Dev", 0.8), ("Artistic", 0.45), ("Technical-Skill", 0.36), ("Enterprising", 0.36), ("Software-Dev", 0.36), ("People-Skill", 0.32), ("Realistic", 0.28)],
    "Web-Dev": [("Software-Dev", 0.8), ("Mobile-Dev", 0.8), ("Digital-Media", 0.8), ("Visual-Design", 0.8), ("Animation-3D", 0.8), ("Marketing-Sales", 0.8), ("Startup-Venture", 0.8), ("Community-Serve", 0.8), ("Environmental-Eng", 0.8), ("Agri-Nature", 0.8), ("Cyber-Defense", 0.8), ("Data-Analytics", 0.8), ("Analytical-Skill", 0.8), ("Finance-Acct", 0.8), ("Cloud-Systems", 0.8), ("Admin-Skill", 0.8), ("Tourism-Travel", 0.8), ("Teaching-Ed", 0.8), ("Hospitality-Svc", 0.8), ("Game-Dev", 0.8), ("Technical-Skill", 0.45), ("Investigative", 0.36), ("Creative-Skill", 0.36), ("Artistic", 0.36), ("Enterprising", 0.36), ("Social", 0.36), ("Realistic", 0.36), ("Conventional", 0.36), ("People-Skill", 0.36)],
}
