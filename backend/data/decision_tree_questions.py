# decision_tree_questions.py
"""
================================================================================
DECISION TREE QUESTIONS — Profile-Driven Branching Assessment
================================================================================

Implements a decision tree where questions branch based on the user's profile
(academic interests, skills) and their answers. Each domain has a root question
that branches into more specific sub-areas, guiding the user toward the right
course recommendation.

Example flow for a user interested in "computers":
  Q1001: "What aspect of technology excites you?"
    → Option: "Building software" → Q1002
    → Option: "Digital media/creative" → Q1006
  Q1002: "What type of programming?"
    → Option: "AI/Machine Learning" → Q1008
    → Option: "Web development" → Q1009
  Q1008: "When solving programming challenges, what do you prefer?"
    → (leaf — traits accumulated guide final recommendation)

Question ID Ranges:
  Technology:    1001–1010
  Healthcare:    1101–1106
  Engineering:   1201–1204
  Business:      1301–1302
  Arts:          1401–1404
  Education:     1501
  Science:       1601–1603
  Public Service: 1701–1702
  Maritime:      1801
  Agriculture:   1802
  Hospitality:   1803
  Validation:    1901–1910

Option ID = question_id × 10 + 1-based index  (e.g. Q1001 opt 1 = 10011)
================================================================================
"""

# ================================================================================
# DECISION TREE QUESTIONS
# Each question has options with trait_tags (same format as questions_enhanced.py)
# ================================================================================

DECISION_TREE_QUESTIONS = [

    # ====================================================================
    # TECHNOLOGY DOMAIN  (1001–1010)
    # ====================================================================
    {
        "question_id": 1001,
        "question_text": "Since you're interested in computers and technology, what specific area excites you the most?",
        "category": "Technology",
        "question_type": "tree",
        "options": [
            {
                "option_id": 10011,
                "option_text": "Writing code and building software applications",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.5, "Investigative": 0.3, "Analytical-Skill": 0.25, "Web-Dev": 0.2}
            },
            {
                "option_id": 10012,
                "option_text": "Understanding how computer hardware and electronics work",
                "trait_tags": {"Hardware-Systems": 1.0, "Technical-Skill": 0.5, "Electrical-Power": 0.3, "Investigative": 0.25, "Realistic": 0.2}
            },
            {
                "option_id": 10013,
                "option_text": "Analyzing data and finding patterns or insights",
                "trait_tags": {"Data-Analytics": 1.0, "Analytical-Skill": 0.5, "Investigative": 0.4, "AI-ML": 0.25, "Lab-Research": 0.15}
            },
            {
                "option_id": 10014,
                "option_text": "Protecting systems and networks from cyber threats",
                "trait_tags": {"Cyber-Defense": 1.0, "Technical-Skill": 0.5, "Investigative": 0.3, "Analytical-Skill": 0.25, "Software-Dev": 0.2}
            },
            {
                "option_id": 10015,
                "option_text": "Creating digital art, graphics, or multimedia content using technology",
                "trait_tags": {"Digital-Media": 1.0, "Creative-Skill": 0.6, "Visual-Design": 0.4, "Artistic": 0.3, "Animation-3D": 0.2}
            },
            {
                "option_id": 10016,
                "option_text": "Designing and developing video games",
                "trait_tags": {"Game-Dev": 1.0, "Software-Dev": 0.5, "Creative-Skill": 0.4, "Animation-3D": 0.3, "Visual-Design": 0.2}
            },
        ]
    },

    # Level 1 — Software Development branch
    {
        "question_id": 1002,
        "question_text": "What type of programming and software work interests you the most?",
        "category": "Technology — Software",
        "question_type": "tree",
        "options": [
            {
                "option_id": 10021,
                "option_text": "Building intelligent systems that can learn and make decisions (AI / Machine Learning)",
                "trait_tags": {"AI-ML": 1.0, "Data-Analytics": 0.5, "Software-Dev": 0.4, "Investigative": 0.3, "Analytical-Skill": 0.2}
            },
            {
                "option_id": 10022,
                "option_text": "Creating mobile apps for phones and tablets",
                "trait_tags": {"Mobile-Dev": 1.0, "Software-Dev": 0.6, "Web-Dev": 0.3, "Creative-Skill": 0.2, "Technical-Skill": 0.25}
            },
            {
                "option_id": 10023,
                "option_text": "Building websites and web applications",
                "trait_tags": {"Web-Dev": 1.0, "Software-Dev": 0.6, "Creative-Skill": 0.2, "Technical-Skill": 0.3, "Mobile-Dev": 0.15}
            },
            {
                "option_id": 10024,
                "option_text": "Developing large-scale enterprise and system software",
                "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.5, "Investigative": 0.3, "Cloud-Systems": 0.2, "Analytical-Skill": 0.25}
            },
            {
                "option_id": 10025,
                "option_text": "Automating processes, robotics, and IoT devices",
                "trait_tags": {"Hardware-Systems": 0.6, "Software-Dev": 0.8, "Mechanical-Design": 0.3, "Technical-Skill": 0.4, "Investigative": 0.2}
            },
        ]
    },

    # Level 1 — Hardware / Networks branch
    {
        "question_id": 1003,
        "question_text": "What about computer hardware and networks fascinates you?",
        "category": "Technology — Hardware",
        "question_type": "tree",
        "options": [
            {
                "option_id": 10031,
                "option_text": "Building and configuring computer systems and servers",
                "trait_tags": {"Hardware-Systems": 1.0, "Technical-Skill": 0.6, "Cloud-Systems": 0.3, "Investigative": 0.2, "Cyber-Defense": 0.15}
            },
            {
                "option_id": 10032,
                "option_text": "Designing electronic circuits and components",
                "trait_tags": {"Hardware-Systems": 0.8, "Electrical-Power": 0.6, "Technical-Skill": 0.5, "Investigative": 0.2, "Realistic": 0.15}
            },
            {
                "option_id": 10033,
                "option_text": "Setting up and managing computer networks and cloud infrastructure",
                "trait_tags": {"Cloud-Systems": 0.8, "Hardware-Systems": 0.5, "Technical-Skill": 0.5, "Cyber-Defense": 0.2, "Investigative": 0.15}
            },
            {
                "option_id": 10034,
                "option_text": "Programming embedded systems and microcontrollers",
                "trait_tags": {"Hardware-Systems": 0.8, "Software-Dev": 0.6, "Technical-Skill": 0.5, "Electrical-Power": 0.3, "Investigative": 0.2}
            },
            {
                "option_id": 10035,
                "option_text": "Troubleshooting hardware failures and improving system reliability",
                "trait_tags": {"Hardware-Systems": 1.0, "Technical-Skill": 0.55, "Investigative": 0.35, "Cloud-Systems": 0.2, "Analytical-Skill": 0.2}
            },
        ]
    },

    # Level 1 — Data branch
    {
        "question_id": 1004,
        "question_text": "How would you like to work with data?",
        "category": "Technology — Data",
        "question_type": "tree",
        "options": [
            {
                "option_id": 10041,
                "option_text": "Finding business insights to help companies make better decisions",
                "trait_tags": {"Data-Analytics": 1.0, "Enterprising": 0.3, "Analytical-Skill": 0.5, "Marketing-Sales": 0.25, "Finance-Acct": 0.2}
            },
            {
                "option_id": 10042,
                "option_text": "Building AI models that predict outcomes and spot trends",
                "trait_tags": {"AI-ML": 0.8, "Data-Analytics": 0.6, "Software-Dev": 0.4, "Investigative": 0.3, "Analytical-Skill": 0.25}
            },
            {
                "option_id": 10043,
                "option_text": "Conducting statistical research and scientific data analysis",
                "trait_tags": {"Data-Analytics": 0.8, "Lab-Research": 0.4, "Analytical-Skill": 0.6, "Investigative": 0.3, "Software-Dev": 0.2}
            },
            {
                "option_id": 10044,
                "option_text": "Managing and securing large-scale databases and information systems",
                "trait_tags": {"Data-Analytics": 0.6, "Software-Dev": 0.5, "Cloud-Systems": 0.4, "Technical-Skill": 0.5, "Cyber-Defense": 0.3}
            },
            {
                "option_id": 10045,
                "option_text": "Designing dashboards and reports that turn raw data into clear actions",
                "trait_tags": {"Data-Analytics": 1.0, "Analytical-Skill": 0.5, "Software-Dev": 0.25, "Enterprising": 0.2, "Visual-Design": 0.15}
            },
        ]
    },

    # Level 1 — Cybersecurity branch
    {
        "question_id": 1005,
        "question_text": "What area of cybersecurity interests you the most?",
        "category": "Technology — Security",
        "question_type": "tree",
        "options": [
            {
                "option_id": 10051,
                "option_text": "Finding vulnerabilities and ethical hacking / penetration testing",
                "trait_tags": {"Cyber-Defense": 1.0, "Software-Dev": 0.3, "Investigative": 0.5, "Technical-Skill": 0.4, "Analytical-Skill": 0.3}
            },
            {
                "option_id": 10052,
                "option_text": "Building secure networks and defense systems",
                "trait_tags": {"Cyber-Defense": 0.8, "Cloud-Systems": 0.5, "Technical-Skill": 0.5, "Hardware-Systems": 0.3, "Analytical-Skill": 0.2}
            },
            {
                "option_id": 10053,
                "option_text": "Digital forensics and investigating cyber crimes",
                "trait_tags": {"Cyber-Defense": 0.6, "Forensic-Sci": 0.5, "Law-Enforce": 0.3, "Investigative": 0.5, "Analytical-Skill": 0.3}
            },
            {
                "option_id": 10054,
                "option_text": "Setting security policies and managing organizational risk",
                "trait_tags": {"Cyber-Defense": 0.7, "Admin-Skill": 0.5, "Analytical-Skill": 0.4, "Enterprising": 0.3, "Technical-Skill": 0.2}
            },
            {
                "option_id": 10055,
                "option_text": "Monitoring security operations and responding to active incidents",
                "trait_tags": {"Cyber-Defense": 1.0, "Technical-Skill": 0.45, "Investigative": 0.35, "Analytical-Skill": 0.3, "Cloud-Systems": 0.2}
            },
        ]
    },

    # Level 1 — Digital Media / Creative Tech branch
    {
        "question_id": 1006,
        "question_text": "What type of digital content creation excites you the most?",
        "category": "Technology — Creative",
        "question_type": "tree",
        "options": [
            {
                "option_id": 10061,
                "option_text": "Graphic design and visual communication",
                "trait_tags": {"Visual-Design": 1.0, "Creative-Skill": 0.6, "Digital-Media": 0.4, "Artistic": 0.3, "Spatial-Design": 0.2}
            },
            {
                "option_id": 10062,
                "option_text": "Video production and digital filmmaking",
                "trait_tags": {"Film-Broadcast": 1.0, "Digital-Media": 0.6, "Creative-Skill": 0.4, "Performing-Arts": 0.3, "Artistic": 0.2}
            },
            {
                "option_id": 10063,
                "option_text": "Animation, 3D modeling, and motion graphics",
                "trait_tags": {"Animation-3D": 1.0, "Digital-Media": 0.6, "Creative-Skill": 0.5, "Spatial-Design": 0.35, "Visual-Design": 0.25}
            },
            {
                "option_id": 10064,
                "option_text": "Audio and music production using technology",
                "trait_tags": {"Performing-Arts": 0.6, "Digital-Media": 0.7, "Creative-Skill": 0.5, "Technical-Skill": 0.3, "Artistic": 0.2}
            },
            {
                "option_id": 10065,
                "option_text": "Web design and UI/UX user experience",
                "trait_tags": {"Visual-Design": 0.7, "Web-Dev": 0.5, "Creative-Skill": 0.6, "Software-Dev": 0.3, "Spatial-Design": 0.2}
            },
        ]
    },

    # Level 1 — Game Development branch
    {
        "question_id": 1007,
        "question_text": "What aspect of game development interests you the most?",
        "category": "Technology — Gaming",
        "question_type": "tree",
        "options": [
            {
                "option_id": 10071,
                "option_text": "Programming game mechanics, physics, and systems",
                "trait_tags": {"Game-Dev": 0.8, "Software-Dev": 0.8, "Technical-Skill": 0.4, "Analytical-Skill": 0.3, "Investigative": 0.2}
            },
            {
                "option_id": 10072,
                "option_text": "Game art, character design, and visual world building",
                "trait_tags": {"Game-Dev": 0.5, "Visual-Design": 0.7, "Animation-3D": 0.6, "Creative-Skill": 0.5, "Spatial-Design": 0.3}
            },
            {
                "option_id": 10073,
                "option_text": "Game design — stories, levels, and player experience",
                "trait_tags": {"Game-Dev": 0.7, "Creative-Skill": 0.6, "Digital-Media": 0.3, "People-Skill": 0.2, "Artistic": 0.25}
            },
            {
                "option_id": 10074,
                "option_text": "Game audio, music, and sound design",
                "trait_tags": {"Game-Dev": 0.4, "Performing-Arts": 0.5, "Digital-Media": 0.5, "Creative-Skill": 0.4, "Artistic": 0.3}
            },
            {
                "option_id": 10075,
                "option_text": "Testing gameplay, balancing systems, and improving player experience",
                "trait_tags": {"Game-Dev": 1.0, "Analytical-Skill": 0.35, "People-Skill": 0.2, "Creative-Skill": 0.25, "Investigative": 0.2}
            },
        ]
    },

    # Level 2 — Deep programming preferences
    {
        "question_id": 1008,
        "question_text": "When solving programming challenges, what approach do you naturally prefer?",
        "category": "Technology — Deep",
        "question_type": "tree",
        "options": [
            {
                "option_id": 10081,
                "option_text": "Working on complex algorithms and mathematical problems",
                "trait_tags": {"Software-Dev": 0.8, "Analytical-Skill": 0.7, "Investigative": 0.5, "AI-ML": 0.3, "Data-Analytics": 0.2}
            },
            {
                "option_id": 10082,
                "option_text": "Building user-friendly interfaces and visual experiences",
                "trait_tags": {"Web-Dev": 0.6, "Visual-Design": 0.4, "Mobile-Dev": 0.5, "Creative-Skill": 0.3, "Spatial-Design": 0.2}
            },
            {
                "option_id": 10083,
                "option_text": "Optimizing systems for performance, reliability, and scalability",
                "trait_tags": {"Software-Dev": 0.8, "Cloud-Systems": 0.5, "Technical-Skill": 0.6, "Analytical-Skill": 0.35, "Investigative": 0.2}
            },
            {
                "option_id": 10084,
                "option_text": "Working with data to train AI models or analyze trends",
                "trait_tags": {"Data-Analytics": 0.7, "AI-ML": 0.6, "Software-Dev": 0.4, "Analytical-Skill": 0.5, "Investigative": 0.25}
            },
            {
                "option_id": 10085,
                "option_text": "Debugging complex code by tracing issues step by step until they are fixed",
                "trait_tags": {"Software-Dev": 1.0, "Investigative": 0.45, "Analytical-Skill": 0.4, "Technical-Skill": 0.25, "Cloud-Systems": 0.15}
            },
        ]
    },

    # Level 2 — Web development deeper
    {
        "question_id": 1009,
        "question_text": "What kind of web development work excites you the most?",
        "category": "Technology — Web",
        "question_type": "tree",
        "options": [
            {
                "option_id": 10091,
                "option_text": "Frontend — making visually appealing, interactive websites",
                "trait_tags": {"Web-Dev": 0.8, "Visual-Design": 0.5, "Creative-Skill": 0.4, "Software-Dev": 0.3, "Spatial-Design": 0.2}
            },
            {
                "option_id": 10092,
                "option_text": "Backend — building server logic, APIs, and databases",
                "trait_tags": {"Web-Dev": 0.6, "Software-Dev": 0.7, "Data-Analytics": 0.3, "Technical-Skill": 0.5, "Cloud-Systems": 0.25}
            },
            {
                "option_id": 10093,
                "option_text": "Full-stack — doing both frontend and backend development",
                "trait_tags": {"Web-Dev": 0.8, "Software-Dev": 0.6, "Technical-Skill": 0.4, "Data-Analytics": 0.25, "Investigative": 0.2}
            },
            {
                "option_id": 10094,
                "option_text": "E-commerce and online business platforms",
                "trait_tags": {"Web-Dev": 0.6, "Startup-Venture": 0.4, "Marketing-Sales": 0.3, "Software-Dev": 0.4, "Enterprising": 0.25}
            },
            {
                "option_id": 10095,
                "option_text": "Improving website performance, accessibility, and user experience",
                "trait_tags": {"Web-Dev": 1.0, "Software-Dev": 0.35, "Analytical-Skill": 0.2, "Visual-Design": 0.2, "Technical-Skill": 0.2}
            },
        ]
    },

    # Level 2 — Creative tech environment
    {
        "question_id": 1010,
        "question_text": "What work environment would you prefer for your creative technology work?",
        "category": "Technology — Creative Environment",
        "question_type": "tree",
        "options": [
            {
                "option_id": 10101,
                "option_text": "An advertising or marketing agency doing creative campaigns",
                "trait_tags": {"Marketing-Sales": 0.5, "Visual-Design": 0.5, "Creative-Skill": 0.4, "Digital-Media": 0.3, "Enterprising": 0.25}
            },
            {
                "option_id": 10102,
                "option_text": "A film or TV production studio",
                "trait_tags": {"Film-Broadcast": 0.7, "Digital-Media": 0.5, "Creative-Skill": 0.4, "Performing-Arts": 0.3, "Artistic": 0.2}
            },
            {
                "option_id": 10103,
                "option_text": "A tech company's design and product team",
                "trait_tags": {"Visual-Design": 0.5, "Software-Dev": 0.3, "Web-Dev": 0.4, "Creative-Skill": 0.5, "Spatial-Design": 0.2}
            },
            {
                "option_id": 10104,
                "option_text": "Freelance or running your own creative studio",
                "trait_tags": {"Creative-Skill": 0.6, "Startup-Venture": 0.4, "Visual-Design": 0.4, "Enterprising": 0.3, "Marketing-Sales": 0.2}
            },
            {
                "option_id": 10105,
                "option_text": "A game or animation studio",
                "trait_tags": {"Animation-3D": 0.6, "Game-Dev": 0.5, "Creative-Skill": 0.5, "Digital-Media": 0.4, "Artistic": 0.25}
            },
        ]
    },


    # ====================================================================
    # HEALTHCARE DOMAIN  (1101–1106)
    # ====================================================================
    {
        "question_id": 1101,
        "question_text": "Since you're interested in healthcare, what draws you to this field the most?",
        "category": "Healthcare",
        "question_type": "tree",
        "options": [
            {
                "option_id": 11011,
                "option_text": "Directly caring for and treating patients in hospitals or clinics",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.5, "Social": 0.3, "Community-Serve": 0.3, "Rehab-Therapy": 0.2}
            },
            {
                "option_id": 11012,
                "option_text": "Working in medical laboratories running tests and diagnostics",
                "trait_tags": {"Medical-Lab": 1.0, "Lab-Research": 0.5, "Investigative": 0.3, "Technical-Skill": 0.3, "Analytical-Skill": 0.2}
            },
            {
                "option_id": 11013,
                "option_text": "Helping people recover through therapy and rehabilitation",
                "trait_tags": {"Rehab-Therapy": 1.0, "People-Skill": 0.5, "Physical-Skill": 0.3, "Patient-Care": 0.3, "Community-Serve": 0.2}
            },
            {
                "option_id": 11014,
                "option_text": "Studying medicines, drugs, and pharmaceuticals",
                "trait_tags": {"Pharmacy": 1.0, "Lab-Research": 0.4, "Medical-Lab": 0.3, "Investigative": 0.3, "Analytical-Skill": 0.2}
            },
            {
                "option_id": 11015,
                "option_text": "Promoting public health and community wellness programs",
                "trait_tags": {"Public-Health": 1.0, "Community-Serve": 0.5, "People-Skill": 0.3, "Social": 0.3, "Teaching-Ed": 0.2}
            },
            {
                "option_id": 11016,
                "option_text": "Nutrition, food science, and dietetics",
                "trait_tags": {"Nutrition-Diet": 1.0, "Patient-Care": 0.3, "Lab-Research": 0.2, "Public-Health": 0.3, "People-Skill": 0.2}
            },
        ]
    },

    # Level 1 — Patient Care
    {
        "question_id": 1102,
        "question_text": "What type of patient care role appeals to you the most?",
        "category": "Healthcare — Patient Care",
        "question_type": "tree",
        "options": [
            {
                "option_id": 11021,
                "option_text": "General nursing — caring for patients across different departments",
                "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.6, "Social": 0.4, "Community-Serve": 0.3, "Rehab-Therapy": 0.2}
            },
            {
                "option_id": 11022,
                "option_text": "Midwifery — maternal, newborn, and reproductive health care",
                "trait_tags": {"Patient-Care": 0.8, "People-Skill": 0.6, "Social": 0.4, "Community-Serve": 0.3, "Public-Health": 0.2}
            },
            {
                "option_id": 11023,
                "option_text": "Emergency and critical care — handling urgent medical situations",
                "trait_tags": {"Patient-Care": 0.8, "Physical-Skill": 0.5, "Technical-Skill": 0.3, "Medical-Lab": 0.3, "Realistic": 0.2}
            },
            {
                "option_id": 11024,
                "option_text": "Eye care and vision health (Optometry)",
                "trait_tags": {"Patient-Care": 0.7, "Medical-Lab": 0.4, "Technical-Skill": 0.3, "Investigative": 0.3, "Analytical-Skill": 0.2}
            },
            {
                "option_id": 11025,
                "option_text": "Respiratory care and breathing therapy",
                "trait_tags": {"Patient-Care": 0.7, "Rehab-Therapy": 0.5, "Technical-Skill": 0.4, "Medical-Lab": 0.3, "People-Skill": 0.2}
            },
            {
                "option_id": 11026,
                "option_text": "Healthcare administration and hospital management",
                "trait_tags": {"Health-Admin": 1.0, "Admin-Skill": 0.5, "People-Skill": 0.3, "Analytical-Skill": 0.3, "Enterprising": 0.2}
            },
        ]
    },

    # Level 1 — Medical Lab / Diagnostics
    {
        "question_id": 1103,
        "question_text": "What type of medical laboratory work interests you?",
        "category": "Healthcare — Laboratory",
        "question_type": "tree",
        "options": [
            {
                "option_id": 11031,
                "option_text": "Analyzing blood, tissue, and body fluid samples",
                "trait_tags": {"Medical-Lab": 1.0, "Lab-Research": 0.5, "Investigative": 0.4, "Analytical-Skill": 0.3, "Technical-Skill": 0.2}
            },
            {
                "option_id": 11032,
                "option_text": "Medical imaging — X-rays, CT scans, and radiology",
                "trait_tags": {"Medical-Lab": 0.8, "Technical-Skill": 0.6, "Patient-Care": 0.3, "Investigative": 0.3, "Analytical-Skill": 0.2}
            },
            {
                "option_id": 11033,
                "option_text": "Biotechnology and genetic laboratory research",
                "trait_tags": {"Lab-Research": 0.8, "Medical-Lab": 0.5, "Investigative": 0.5, "Analytical-Skill": 0.3, "Technical-Skill": 0.2}
            },
            {
                "option_id": 11034,
                "option_text": "Veterinary laboratory work and animal health diagnostics",
                "trait_tags": {"Medical-Lab": 0.5, "Agri-Nature": 0.5, "Patient-Care": 0.4, "Lab-Research": 0.3, "Investigative": 0.2}
            },
            {
                "option_id": 11035,
                "option_text": "Operating specialized lab instruments and ensuring test accuracy",
                "trait_tags": {"Medical-Lab": 1.0, "Technical-Skill": 0.45, "Analytical-Skill": 0.35, "Investigative": 0.3, "Lab-Research": 0.25}
            },
        ]
    },

    # Level 1 — Therapy / Rehabilitation
    {
        "question_id": 1104,
        "question_text": "What type of therapy and rehabilitation work interests you?",
        "category": "Healthcare — Therapy",
        "question_type": "tree",
        "options": [
            {
                "option_id": 11041,
                "option_text": "Physical therapy — helping patients with movement and recovery",
                "trait_tags": {"Rehab-Therapy": 1.0, "Physical-Skill": 0.5, "Patient-Care": 0.4, "People-Skill": 0.3, "Community-Serve": 0.2}
            },
            {
                "option_id": 11042,
                "option_text": "Occupational therapy — helping people with daily living skills",
                "trait_tags": {"Rehab-Therapy": 0.8, "People-Skill": 0.5, "Patient-Care": 0.5, "Community-Serve": 0.3, "Social": 0.2}
            },
            {
                "option_id": 11043,
                "option_text": "Speech-language therapy — helping with communication and swallowing",
                "trait_tags": {"Rehab-Therapy": 0.8, "People-Skill": 0.6, "Patient-Care": 0.4, "Social": 0.3, "Teaching-Ed": 0.2}
            },
            {
                "option_id": 11044,
                "option_text": "Mental health counseling and psychological support",
                "trait_tags": {"Counseling": 1.0, "People-Skill": 0.6, "Social": 0.4, "Community-Serve": 0.3, "Patient-Care": 0.2}
            },
            {
                "option_id": 11045,
                "option_text": "Designing long-term rehabilitation plans and tracking patient progress",
                "trait_tags": {"Rehab-Therapy": 1.0, "Patient-Care": 0.45, "People-Skill": 0.35, "Analytical-Skill": 0.2, "Community-Serve": 0.2}
            },
        ]
    },

    # Level 1 — Pharmacy
    {
        "question_id": 1105,
        "question_text": "What about pharmaceuticals and medicines interests you the most?",
        "category": "Healthcare — Pharmacy",
        "question_type": "tree",
        "options": [
            {
                "option_id": 11051,
                "option_text": "Dispensing medication and counseling patients about drug usage",
                "trait_tags": {"Pharmacy": 1.0, "Patient-Care": 0.45, "People-Skill": 0.4, "Community-Serve": 0.25, "Medical-Lab": 0.2}
            },
            {
                "option_id": 11052,
                "option_text": "Researching and developing new drugs and treatments",
                "trait_tags": {"Pharmacy": 0.7, "Lab-Research": 0.7, "Investigative": 0.5, "Analytical-Skill": 0.35, "Medical-Lab": 0.25}
            },
            {
                "option_id": 11053,
                "option_text": "Clinical trials, drug testing, and quality assurance",
                "trait_tags": {"Pharmacy": 0.6, "Lab-Research": 0.5, "Medical-Lab": 0.5, "Analytical-Skill": 0.4, "Investigative": 0.3}
            },
            {
                "option_id": 11054,
                "option_text": "Community pharmacy management and retail healthcare",
                "trait_tags": {"Pharmacy": 0.8, "Admin-Skill": 0.45, "People-Skill": 0.4, "Community-Serve": 0.35, "Patient-Care": 0.2}
            },
            {
                "option_id": 11055,
                "option_text": "Pharmaceutical manufacturing and industrial drug production",
                "trait_tags": {"Pharmacy": 0.8, "Industrial-Ops": 0.5, "Lab-Research": 0.4, "Technical-Skill": 0.35, "Analytical-Skill": 0.25}
            },
        ]
    },

    # Level 1 — Health Info Management (bonus branch)
    {
        "question_id": 1106,
        "question_text": "How would you like to contribute to healthcare management?",
        "category": "Healthcare — Administration",
        "question_type": "tree",
        "options": [
            {
                "option_id": 11061,
                "option_text": "Managing patient records and health information systems",
                "trait_tags": {"Health-Admin": 1.0, "Technical-Skill": 0.45, "Admin-Skill": 0.5, "Data-Analytics": 0.3, "Conventional": 0.2}
            },
            {
                "option_id": 11062,
                "option_text": "Hospital operations and healthcare facility management",
                "trait_tags": {"Health-Admin": 0.8, "Admin-Skill": 0.6, "People-Skill": 0.45, "Enterprising": 0.3, "Community-Serve": 0.2}
            },
            {
                "option_id": 11063,
                "option_text": "Health policy and public health program coordination",
                "trait_tags": {"Public-Health": 0.8, "Community-Serve": 0.55, "Admin-Skill": 0.4, "Social": 0.3, "People-Skill": 0.2}
            },
            {
                "option_id": 11064,
                "option_text": "Health information technology and electronic health records",
                "trait_tags": {"Health-Admin": 0.7, "Software-Dev": 0.45, "Technical-Skill": 0.5, "Data-Analytics": 0.35, "Admin-Skill": 0.25}
            },
            {
                "option_id": 11065,
                "option_text": "Medical billing, coding, and health insurance administration",
                "trait_tags": {"Health-Admin": 0.8, "Finance-Acct": 0.45, "Conventional": 0.45, "Admin-Skill": 0.4, "Analytical-Skill": 0.25}
            },
        ]
    },


    # ====================================================================
    # ENGINEERING DOMAIN  (1201–1204)
    # ====================================================================
    {
        "question_id": 1201,
        "question_text": "What type of engineering work excites you the most?",
        "category": "Engineering",
        "question_type": "tree",
        "options": [
            {
                "option_id": 12011,
                "option_text": "Designing and constructing buildings, roads, and bridges",
                "trait_tags": {"Civil-Build": 1.0, "Spatial-Design": 0.45, "Realistic": 0.4, "Technical-Skill": 0.3, "Analytical-Skill": 0.2}
            },
            {
                "option_id": 12012,
                "option_text": "Working with machines, engines, and mechanical systems",
                "trait_tags": {"Mechanical-Design": 1.0, "Technical-Skill": 0.5, "Realistic": 0.45, "Industrial-Ops": 0.3, "Analytical-Skill": 0.2}
            },
            {
                "option_id": 12013,
                "option_text": "Electrical systems, power generation, and electronics",
                "trait_tags": {"Electrical-Power": 1.0, "Technical-Skill": 0.5, "Hardware-Systems": 0.4, "Realistic": 0.3, "Analytical-Skill": 0.2}
            },
            {
                "option_id": 12014,
                "option_text": "Optimizing industrial and manufacturing processes",
                "trait_tags": {"Industrial-Ops": 1.0, "Analytical-Skill": 0.5, "Admin-Skill": 0.4, "Mechanical-Design": 0.3, "Technical-Skill": 0.25}
            },
            {
                "option_id": 12015,
                "option_text": "Designing spaces — architecture, interiors, and landscapes",
                "trait_tags": {"Spatial-Design": 1.0, "Creative-Skill": 0.6, "Artistic": 0.45, "Visual-Design": 0.35, "Civil-Build": 0.2}
            },
            {
                "option_id": 12016,
                "option_text": "Aircraft, aerospace, and aviation systems",
                "trait_tags": {"Aeronautical-Eng": 1.0, "Mechanical-Design": 0.5, "Technical-Skill": 0.45, "Investigative": 0.35, "Realistic": 0.2}
            },
        ]
    },

    # Level 1 — Civil Engineering
    {
        "question_id": 1202,
        "question_text": "What area of civil engineering interests you the most?",
        "category": "Engineering — Civil",
        "question_type": "tree",
        "options": [
            {
                "option_id": 12021,
                "option_text": "Structural design and building construction",
                "trait_tags": {"Civil-Build": 1.0, "Spatial-Design": 0.45, "Technical-Skill": 0.35, "Realistic": 0.25, "Analytical-Skill": 0.2}
            },
            {
                "option_id": 12022,
                "option_text": "Roads, bridges, and transportation infrastructure planning",
                "trait_tags": {"Civil-Build": 0.8, "Community-Serve": 0.45, "Admin-Skill": 0.4, "Technical-Skill": 0.3, "Spatial-Design": 0.2}
            },
            {
                "option_id": 12023,
                "option_text": "Surveying, land measurement, and geodetic engineering",
                "trait_tags": {"Field-Research": 1.0, "Technical-Skill": 0.5, "Analytical-Skill": 0.45, "Civil-Build": 0.35, "Investigative": 0.25}
            },
            {
                "option_id": 12024,
                "option_text": "Environmental engineering — water treatment and waste management",
                "trait_tags": {"Environmental-Eng": 1.0, "Environmental-Sci": 0.5, "Field-Research": 0.4, "Technical-Skill": 0.35, "Civil-Build": 0.2}
            },
            {
                "option_id": 12025,
                "option_text": "Urban planning and city infrastructure development",
                "trait_tags": {"Community-Serve": 0.8, "Civil-Build": 0.6, "Admin-Skill": 0.5, "Spatial-Design": 0.4, "Analytical-Skill": 0.3}
            },
        ]
    },

    # Level 1 — Mechanical Engineering
    {
        "question_id": 1203,
        "question_text": "What type of mechanical work appeals to you?",
        "category": "Engineering — Mechanical",
        "question_type": "tree",
        "options": [
            {
                "option_id": 12031,
                "option_text": "Designing machines and mechanical components",
                "trait_tags": {"Mechanical-Design": 1.0, "Technical-Skill": 0.5, "Realistic": 0.4, "Analytical-Skill": 0.3, "Industrial-Ops": 0.2}
            },
            {
                "option_id": 12032,
                "option_text": "Automotive and transportation system engineering",
                "trait_tags": {"Mechanical-Design": 0.8, "Industrial-Ops": 0.5, "Technical-Skill": 0.45, "Realistic": 0.3, "Analytical-Skill": 0.2}
            },
            {
                "option_id": 12033,
                "option_text": "Manufacturing processes and production engineering",
                "trait_tags": {"Industrial-Ops": 1.0, "Analytical-Skill": 0.5, "Technical-Skill": 0.4, "Admin-Skill": 0.35, "Mechanical-Design": 0.2}
            },
            {
                "option_id": 12034,
                "option_text": "Marine engineering and ship mechanical systems",
                "trait_tags": {"Maritime-Sea": 1.0, "Mechanical-Design": 0.5, "Technical-Skill": 0.45, "Physical-Skill": 0.3, "Realistic": 0.2}
            },
            {
                "option_id": 12035,
                "option_text": "Aerospace and aeronautical engineering systems",
                "trait_tags": {"Aeronautical-Eng": 1.0, "Mechanical-Design": 0.45, "Technical-Skill": 0.4, "Investigative": 0.35, "Analytical-Skill": 0.25}
            },
        ]
    },

    # Level 1 — Architecture / Spatial Design
    {
        "question_id": 1204,
        "question_text": "What design direction appeals to you the most?",
        "category": "Engineering — Design",
        "question_type": "tree",
        "options": [
            {
                "option_id": 12041,
                "option_text": "Architecture — designing building exteriors and structures",
                "trait_tags": {"Spatial-Design": 1.0, "Civil-Build": 0.45, "Creative-Skill": 0.4, "Artistic": 0.3, "Technical-Skill": 0.2}
            },
            {
                "option_id": 12042,
                "option_text": "Interior design — planning functional and aesthetic indoor spaces",
                "trait_tags": {"Creative-Skill": 1.0, "Spatial-Design": 0.5, "Visual-Design": 0.45, "Artistic": 0.4, "People-Skill": 0.2}
            },
            {
                "option_id": 12043,
                "option_text": "Landscape architecture — designing parks and outdoor environments",
                "trait_tags": {"Agri-Nature": 0.8, "Spatial-Design": 0.6, "Creative-Skill": 0.5, "Environmental-Sci": 0.35, "Field-Research": 0.25}
            },
            {
                "option_id": 12044,
                "option_text": "Industrial and product design — creating everyday objects and products",
                "trait_tags": {"Industrial-Ops": 0.7, "Creative-Skill": 0.7, "Visual-Design": 0.4, "Technical-Skill": 0.35, "Spatial-Design": 0.25}
            },
            {
                "option_id": 12045,
                "option_text": "Urban and environmental planning — designing sustainable communities",
                "trait_tags": {"Community-Serve": 0.8, "Environmental-Sci": 0.6, "Civil-Build": 0.45, "Admin-Skill": 0.4, "Spatial-Design": 0.3}
            },
        ]
    },


    # ====================================================================
    # BUSINESS DOMAIN  (1301–1302)
    # ====================================================================
    {
        "question_id": 1301,
        "question_text": "What area of business interests you the most?",
        "category": "Business",
        "question_type": "tree",
        "options": [
            {
                "option_id": 13011,
                "option_text": "Finance, accounting, and money management",
                "trait_tags": {"Finance-Acct": 1.0, "Analytical-Skill": 0.5, "Conventional": 0.3, "Admin-Skill": 0.3, "Investigative": 0.2}
            },
            {
                "option_id": 13012,
                "option_text": "Marketing, sales, and brand building",
                "trait_tags": {"Marketing-Sales": 1.0, "Creative-Skill": 0.4, "People-Skill": 0.3, "Enterprising": 0.3, "Digital-Media": 0.2}
            },
            {
                "option_id": 13013,
                "option_text": "Starting and managing your own business",
                "trait_tags": {"Startup-Venture": 1.0, "Enterprising": 0.6, "People-Skill": 0.3, "Marketing-Sales": 0.3, "Admin-Skill": 0.2}
            },
            {
                "option_id": 13014,
                "option_text": "Human resources and people management",
                "trait_tags": {"HR-Management": 1.0, "People-Skill": 0.6, "Admin-Skill": 0.4, "Social": 0.3, "Conventional": 0.2}
            },
            {
                "option_id": 13015,
                "option_text": "Operations, logistics, and supply chain management",
                "trait_tags": {"Industrial-Ops": 0.7, "Admin-Skill": 0.6, "Analytical-Skill": 0.3, "Finance-Acct": 0.3, "Conventional": 0.2}
            },
            {
                "option_id": 13016,
                "option_text": "Economics and business policy analysis",
                "trait_tags": {"Finance-Acct": 0.6, "Analytical-Skill": 0.6, "Investigative": 0.4, "Community-Serve": 0.3, "Data-Analytics": 0.2}
            },
        ]
    },

    # Level 1 — Finance / Accounting
    {
        "question_id": 1302,
        "question_text": "What type of financial work interests you the most?",
        "category": "Business — Finance",
        "question_type": "tree",
        "options": [
            {
                "option_id": 13021,
                "option_text": "Auditing, bookkeeping, and professional accounting practice",
                "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.6, "Analytical-Skill": 0.4, "Admin-Skill": 0.3, "Investigative": 0.2}
            },
            {
                "option_id": 13022,
                "option_text": "Financial analysis, investments, and banking",
                "trait_tags": {"Finance-Acct": 0.8, "Analytical-Skill": 0.6, "Enterprising": 0.3, "Data-Analytics": 0.3, "Investigative": 0.2}
            },
            {
                "option_id": 13023,
                "option_text": "Management accounting and cost control systems",
                "trait_tags": {"Finance-Acct": 0.8, "Admin-Skill": 0.4, "Analytical-Skill": 0.5, "Conventional": 0.3, "Industrial-Ops": 0.2}
            },
            {
                "option_id": 13024,
                "option_text": "Real estate management and property development",
                "trait_tags": {"Finance-Acct": 0.5, "Marketing-Sales": 0.5, "Enterprising": 0.4, "Startup-Venture": 0.3, "Admin-Skill": 0.2}
            },
            {
                "option_id": 13025,
                "option_text": "Customs administration and international trade",
                "trait_tags": {"Finance-Acct": 0.4, "Admin-Skill": 0.6, "Conventional": 0.4, "Analytical-Skill": 0.3, "Community-Serve": 0.2}
            },
        ]
    },


    # ====================================================================
    # ARTS & CREATIVE DOMAIN  (1401–1404)
    # ====================================================================
    {
        "question_id": 1401,
        "question_text": "What type of creative and artistic expression interests you the most?",
        "category": "Arts & Creative",
        "question_type": "tree",
        "options": [
            {
                "option_id": 14011,
                "option_text": "Visual arts — painting, drawing, sculpture, and fine arts",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.7, "Creative-Skill": 0.5, "Spatial-Design": 0.3, "Performing-Arts": 0.2}
            },
            {
                "option_id": 14012,
                "option_text": "Digital arts — graphic design, multimedia, and digital content",
                "trait_tags": {"Digital-Media": 1.0, "Creative-Skill": 0.6, "Visual-Design": 0.4, "Animation-3D": 0.3, "Artistic": 0.2}
            },
            {
                "option_id": 14013,
                "option_text": "Performing arts — music, theater, and stage performance",
                "trait_tags": {"Performing-Arts": 1.0, "Creative-Skill": 0.5, "People-Skill": 0.3, "Artistic": 0.3, "Social": 0.2}
            },
            {
                "option_id": 14014,
                "option_text": "Film, video production, and broadcasting",
                "trait_tags": {"Film-Broadcast": 1.0, "Digital-Media": 0.5, "Creative-Skill": 0.4, "Artistic": 0.3, "Performing-Arts": 0.2}
            },
            {
                "option_id": 14015,
                "option_text": "Fashion design and textile arts",
                "trait_tags": {"Visual-Design": 0.7, "Creative-Skill": 0.7, "Artistic": 0.4, "Spatial-Design": 0.3, "Enterprising": 0.2}
            },
            {
                "option_id": 14016,
                "option_text": "Photography — capturing and editing visual stories",
                "trait_tags": {"Visual-Design": 0.7, "Digital-Media": 0.5, "Creative-Skill": 0.5, "Artistic": 0.3, "Film-Broadcast": 0.2}
            },
        ]
    },

    # Level 1 — Visual Arts
    {
        "question_id": 1402,
        "question_text": "What visual arts path interests you the most?",
        "category": "Arts — Visual",
        "question_type": "tree",
        "options": [
            {
                "option_id": 14021,
                "option_text": "Fine arts — painting, sculpture, and mixed media exhibitions",
                "trait_tags": {"Visual-Design": 1.0, "Artistic": 0.8, "Creative-Skill": 0.5, "Performing-Arts": 0.2, "Social": 0.15}
            },
            {
                "option_id": 14022,
                "option_text": "Advertising and commercial art for brands and companies",
                "trait_tags": {"Visual-Design": 0.7, "Marketing-Sales": 0.55, "Creative-Skill": 0.5, "Enterprising": 0.3, "Digital-Media": 0.2}
            },
            {
                "option_id": 14023,
                "option_text": "Art education and teaching art to students",
                "trait_tags": {"Visual-Design": 0.5, "Teaching-Ed": 0.7, "Creative-Skill": 0.45, "People-Skill": 0.4, "Social": 0.25}
            },
            {
                "option_id": 14024,
                "option_text": "Digital illustration and concept art for games or media",
                "trait_tags": {"Visual-Design": 0.8, "Digital-Media": 0.55, "Animation-3D": 0.45, "Creative-Skill": 0.5, "Game-Dev": 0.2}
            },
            {
                "option_id": 14025,
                "option_text": "Photography and visual storytelling",
                "trait_tags": {"Visual-Design": 0.7, "Artistic": 0.6, "Digital-Media": 0.45, "Creative-Skill": 0.4, "Film-Broadcast": 0.25}
            },
        ]
    },

    # Level 1 — Digital Arts
    {
        "question_id": 1403,
        "question_text": "What type of digital arts and content creation excites you?",
        "category": "Arts — Digital",
        "question_type": "tree",
        "options": [
            {
                "option_id": 14031,
                "option_text": "Animation, motion graphics, and visual effects",
                "trait_tags": {"Animation-3D": 1.0, "Digital-Media": 0.6, "Creative-Skill": 0.5, "Visual-Design": 0.35, "Artistic": 0.25}
            },
            {
                "option_id": 14032,
                "option_text": "Game art, 3D modeling, and virtual world design",
                "trait_tags": {"Game-Dev": 0.6, "Animation-3D": 0.7, "Visual-Design": 0.5, "Creative-Skill": 0.4, "Spatial-Design": 0.3}
            },
            {
                "option_id": 14033,
                "option_text": "Graphic design, branding, and print media",
                "trait_tags": {"Visual-Design": 0.8, "Digital-Media": 0.5, "Creative-Skill": 0.5, "Marketing-Sales": 0.3, "Artistic": 0.2}
            },
            {
                "option_id": 14034,
                "option_text": "Multimedia content — interactive media and web experiences",
                "trait_tags": {"Digital-Media": 1.0, "Creative-Skill": 0.5, "Web-Dev": 0.3, "Visual-Design": 0.3, "Animation-3D": 0.2}
            },
            {
                "option_id": 14035,
                "option_text": "Digital illustration for social media, publishing, and online campaigns",
                "trait_tags": {"Visual-Design": 1.0, "Digital-Media": 0.45, "Creative-Skill": 0.4, "Marketing-Sales": 0.2, "Artistic": 0.2}
            },
        ]
    },

    # Level 1 — Performing Arts
    {
        "question_id": 1404,
        "question_text": "What performing arts interest you the most?",
        "category": "Arts — Performing",
        "question_type": "tree",
        "options": [
            {
                "option_id": 14041,
                "option_text": "Theater acting, directing, and stage performance",
                "trait_tags": {"Performing-Arts": 1.0, "Creative-Skill": 0.5, "People-Skill": 0.45, "Artistic": 0.35, "Social": 0.2}
            },
            {
                "option_id": 14042,
                "option_text": "Music performance, composition, and musical studies",
                "trait_tags": {"Performing-Arts": 0.9, "Creative-Skill": 0.55, "Artistic": 0.45, "Visual-Design": 0.2, "Social": 0.15}
            },
            {
                "option_id": 14043,
                "option_text": "Music production, recording, and audio engineering",
                "trait_tags": {"Performing-Arts": 0.5, "Digital-Media": 0.65, "Technical-Skill": 0.45, "Creative-Skill": 0.45, "Software-Dev": 0.2}
            },
            {
                "option_id": 14044,
                "option_text": "Dance and physical performance arts",
                "trait_tags": {"Performing-Arts": 0.9, "Physical-Skill": 0.55, "Creative-Skill": 0.5, "Artistic": 0.35, "People-Skill": 0.2}
            },
            {
                "option_id": 14045,
                "option_text": "Broadcasting, media presenting, and journalism",
                "trait_tags": {"Film-Broadcast": 0.8, "Digital-Media": 0.55, "People-Skill": 0.5, "Creative-Skill": 0.35, "Performing-Arts": 0.25}
            },
        ]
    },


    # ====================================================================
    # EDUCATION DOMAIN  (1501)
    # ====================================================================
    {
        "question_id": 1501,
        "question_text": "What type of teaching and education work interests you the most?",
        "category": "Education",
        "question_type": "tree",
        "options": [
            {
                "option_id": 15011,
                "option_text": "Elementary school teaching — guiding young learners",
                "trait_tags": {"Teaching-Ed": 1.0, "People-Skill": 0.6, "Social": 0.4, "Community-Serve": 0.3, "Counseling": 0.2}
            },
            {
                "option_id": 15012,
                "option_text": "High school / secondary teaching — teaching specific subjects",
                "trait_tags": {"Teaching-Ed": 0.9, "People-Skill": 0.5, "Analytical-Skill": 0.3, "Community-Serve": 0.3, "Social": 0.2}
            },
            {
                "option_id": 15013,
                "option_text": "Early childhood education — nurturing preschool-age children",
                "trait_tags": {"Teaching-Ed": 0.8, "People-Skill": 0.7, "Social": 0.4, "Community-Serve": 0.3, "Counseling": 0.2}
            },
            {
                "option_id": 15014,
                "option_text": "Special education — supporting students with learning disabilities",
                "trait_tags": {"Teaching-Ed": 0.8, "Counseling": 0.5, "People-Skill": 0.6, "Social": 0.3, "Community-Serve": 0.2}
            },
            {
                "option_id": 15015,
                "option_text": "Physical education and sports coaching",
                "trait_tags": {"Sports-Ed": 1.0, "Physical-Skill": 0.5, "Teaching-Ed": 0.4, "People-Skill": 0.3, "Realistic": 0.2}
            },
            {
                "option_id": 15016,
                "option_text": "Technical-vocational education — teaching practical skills and trades",
                "trait_tags": {"Teaching-Ed": 0.7, "Technical-Skill": 0.6, "Realistic": 0.3, "Community-Serve": 0.3, "People-Skill": 0.2}
            },
            {
                "option_id": 15017,
                "option_text": "Library and information science",
                "trait_tags": {"Teaching-Ed": 0.5, "Admin-Skill": 0.6, "Investigative": 0.3, "Analytical-Skill": 0.3, "Data-Analytics": 0.2}
            },
        ]
    },


    # ====================================================================
    # SCIENCE DOMAIN  (1601–1603)
    # ====================================================================
    {
        "question_id": 1601,
        "question_text": "What area of science fascinates you the most?",
        "category": "Science",
        "question_type": "tree",
        "options": [
            {
                "option_id": 16011,
                "option_text": "Biology — studying life, organisms, and living systems",
                "trait_tags": {"Lab-Research": 1.0, "Investigative": 0.5, "Medical-Lab": 0.3, "Analytical-Skill": 0.3, "Field-Research": 0.2}
            },
            {
                "option_id": 16012,
                "option_text": "Chemistry — understanding materials, reactions, and molecular science",
                "trait_tags": {"Lab-Research": 0.9, "Investigative": 0.5, "Technical-Skill": 0.3, "Analytical-Skill": 0.3, "Pharmacy": 0.2}
            },
            {
                "option_id": 16013,
                "option_text": "Physics — exploring forces, energy, and the laws of nature",
                "trait_tags": {"Lab-Research": 0.8, "Analytical-Skill": 0.6, "Investigative": 0.5, "Technical-Skill": 0.3, "Data-Analytics": 0.2}
            },
            {
                "option_id": 16014,
                "option_text": "Environmental and earth sciences — studying our planet",
                "trait_tags": {"Environmental-Sci": 1.0, "Field-Research": 0.5, "Investigative": 0.3, "Agri-Nature": 0.3, "Lab-Research": 0.2}
            },
            {
                "option_id": 16015,
                "option_text": "Mathematics and statistics — the language of patterns and data",
                "trait_tags": {"Analytical-Skill": 1.0, "Data-Analytics": 0.5, "Investigative": 0.4, "Software-Dev": 0.25, "Lab-Research": 0.2}
            },
            {
                "option_id": 16016,
                "option_text": "Food science and technology — the science behind what we eat",
                "trait_tags": {"Food-Science": 1.0, "Lab-Research": 0.4, "Technical-Skill": 0.3, "Nutrition-Diet": 0.3, "Agri-Nature": 0.2}
            },
        ]
    },

    # Level 1 — Biology deeper
    {
        "question_id": 1602,
        "question_text": "What direction in biology interests you the most?",
        "category": "Science — Biology",
        "question_type": "tree",
        "options": [
            {
                "option_id": 16021,
                "option_text": "Marine biology — studying ocean life and aquatic ecosystems",
                "trait_tags": {"Field-Research": 0.7, "Lab-Research": 0.5, "Maritime-Sea": 0.4, "Environmental-Sci": 0.3, "Investigative": 0.2}
            },
            {
                "option_id": 16022,
                "option_text": "Biotechnology and genetics — DNA, gene editing, and biotech applications",
                "trait_tags": {"Lab-Research": 0.9, "Medical-Lab": 0.4, "Investigative": 0.5, "Analytical-Skill": 0.3, "Technical-Skill": 0.2}
            },
            {
                "option_id": 16023,
                "option_text": "Ecology and wildlife — studying animals and natural habitats",
                "trait_tags": {"Field-Research": 0.8, "Environmental-Sci": 0.5, "Agri-Nature": 0.3, "Investigative": 0.3, "Lab-Research": 0.2}
            },
            {
                "option_id": 16024,
                "option_text": "Microbiology and medical research — studying microorganisms and diseases",
                "trait_tags": {"Lab-Research": 0.8, "Medical-Lab": 0.6, "Investigative": 0.4, "Analytical-Skill": 0.3, "Technical-Skill": 0.2}
            },
            {
                "option_id": 16025,
                "option_text": "Bioinformatics and computational biology using data to study life systems",
                "trait_tags": {"Lab-Research": 1.0, "Data-Analytics": 0.35, "Investigative": 0.35, "Analytical-Skill": 0.3, "Technical-Skill": 0.2}
            },
        ]
    },

    # Level 1 — Environmental Science
    {
        "question_id": 1603,
        "question_text": "What environmental science area interests you the most?",
        "category": "Science — Environment",
        "question_type": "tree",
        "options": [
            {
                "option_id": 16031,
                "option_text": "Environmental conservation and policy making",
                "trait_tags": {"Environmental-Sci": 0.8, "Community-Serve": 0.5, "Field-Research": 0.3, "Admin-Skill": 0.3, "Investigative": 0.2}
            },
            {
                "option_id": 16032,
                "option_text": "Weather, climate, and atmospheric science (Meteorology)",
                "trait_tags": {"Environmental-Sci": 0.6, "Data-Analytics": 0.5, "Field-Research": 0.4, "Analytical-Skill": 0.3, "Investigative": 0.2}
            },
            {
                "option_id": 16033,
                "option_text": "Geology — studying rocks, minerals, and earth processes",
                "trait_tags": {"Field-Research": 0.8, "Lab-Research": 0.4, "Environmental-Sci": 0.4, "Investigative": 0.3, "Technical-Skill": 0.2}
            },
            {
                "option_id": 16034,
                "option_text": "Environmental planning and urban sustainability",
                "trait_tags": {"Environmental-Sci": 0.7, "Community-Serve": 0.5, "Admin-Skill": 0.3, "Civil-Build": 0.3, "Spatial-Design": 0.2}
            },
            {
                "option_id": 16035,
                "option_text": "Environmental monitoring using field sensors, mapping, and data collection",
                "trait_tags": {"Environmental-Sci": 1.0, "Field-Research": 0.45, "Data-Analytics": 0.25, "Investigative": 0.25, "Technical-Skill": 0.2}
            },
        ]
    },


    # ====================================================================
    # PUBLIC SERVICE DOMAIN  (1701–1702)
    # ====================================================================
    {
        "question_id": 1701,
        "question_text": "What type of public service work interests you the most?",
        "category": "Public Service",
        "question_type": "tree",
        "options": [
            {
                "option_id": 17011,
                "option_text": "Law enforcement, criminal justice, and keeping communities safe",
                "trait_tags": {"Law-Enforce": 1.0, "Physical-Skill": 0.4, "Investigative": 0.3, "Community-Serve": 0.3, "People-Skill": 0.2}
            },
            {
                "option_id": 17012,
                "option_text": "Law, legal practice, and the justice system",
                "trait_tags": {"Legal-Practice": 1.0, "Analytical-Skill": 0.5, "People-Skill": 0.3, "Investigative": 0.3, "Community-Serve": 0.2}
            },
            {
                "option_id": 17013,
                "option_text": "Social work and community development",
                "trait_tags": {"Social-Work": 1.0, "Community-Serve": 0.6, "People-Skill": 0.5, "Social": 0.3, "Counseling": 0.2}
            },
            {
                "option_id": 17014,
                "option_text": "Government, public administration, and policy",
                "trait_tags": {"Community-Serve": 0.8, "Admin-Skill": 0.6, "People-Skill": 0.3, "Analytical-Skill": 0.3, "Conventional": 0.2}
            },
            {
                "option_id": 17015,
                "option_text": "Politics, diplomacy, and international relations",
                "trait_tags": {"Community-Serve": 0.7, "People-Skill": 0.5, "Analytical-Skill": 0.4, "Legal-Practice": 0.3, "Social": 0.2}
            },
        ]
    },

    # Level 1 — Law Enforcement
    {
        "question_id": 1702,
        "question_text": "What aspect of law enforcement and criminal justice interests you?",
        "category": "Public Service — Justice",
        "question_type": "tree",
        "options": [
            {
                "option_id": 17021,
                "option_text": "Patrol, community policing, and public safety",
                "trait_tags": {"Law-Enforce": 1.0, "Physical-Skill": 0.5, "Community-Serve": 0.45, "People-Skill": 0.3, "Realistic": 0.2}
            },
            {
                "option_id": 17022,
                "option_text": "Criminal investigation, forensics, and crime scene analysis",
                "trait_tags": {"Law-Enforce": 0.7, "Forensic-Sci": 0.75, "Investigative": 0.55, "Analytical-Skill": 0.35, "Lab-Research": 0.2}
            },
            {
                "option_id": 17023,
                "option_text": "Cybercrime investigation and digital forensics",
                "trait_tags": {"Law-Enforce": 0.5, "Cyber-Defense": 0.55, "Forensic-Sci": 0.45, "Technical-Skill": 0.4, "Investigative": 0.3}
            },
            {
                "option_id": 17024,
                "option_text": "Military service, national defense, and tactical operations",
                "trait_tags": {"Law-Enforce": 0.7, "Physical-Skill": 0.7, "Community-Serve": 0.35, "People-Skill": 0.25, "Admin-Skill": 0.2}
            },
            {
                "option_id": 17025,
                "option_text": "Corrections, rehabilitation, and prison management",
                "trait_tags": {"Law-Enforce": 0.6, "Social-Work": 0.55, "Community-Serve": 0.45, "People-Skill": 0.4, "Counseling": 0.25}
            },
        ]
    },


    # ====================================================================
    # MARITIME DOMAIN  (1801)
    # ====================================================================
    {
        "question_id": 1801,
        "question_text": "What maritime and transportation career interests you?",
        "category": "Maritime & Aviation",
        "question_type": "tree",
        "options": [
            {
                "option_id": 18011,
                "option_text": "Ship navigation, captaining, and marine transportation",
                "trait_tags": {"Maritime-Sea": 1.0, "Physical-Skill": 0.4, "Admin-Skill": 0.3, "Technical-Skill": 0.3, "Realistic": 0.2}
            },
            {
                "option_id": 18012,
                "option_text": "Marine engineering — ship engines and mechanical systems",
                "trait_tags": {"Maritime-Sea": 0.7, "Mechanical-Design": 0.7, "Technical-Skill": 0.5, "Physical-Skill": 0.3, "Realistic": 0.2}
            },
            {
                "option_id": 18013,
                "option_text": "Aircraft maintenance and aviation mechanics",
                "trait_tags": {"Mechanical-Design": 0.7, "Technical-Skill": 0.7, "Hardware-Systems": 0.3, "Realistic": 0.3, "Physical-Skill": 0.2}
            },
            {
                "option_id": 18014,
                "option_text": "Aviation electronics and avionics technology",
                "trait_tags": {"Technical-Skill": 0.7, "Hardware-Systems": 0.5, "Electrical-Power": 0.4, "Investigative": 0.25, "Analytical-Skill": 0.2}
            },
            {
                "option_id": 18015,
                "option_text": "Logistics, fleet operations, and coordinating transport schedules",
                "trait_tags": {"Maritime-Sea": 1.0, "Admin-Skill": 0.35, "Technical-Skill": 0.25, "Analytical-Skill": 0.2, "Enterprising": 0.15}
            },
        ]
    },


    # ====================================================================
    # AGRICULTURE DOMAIN  (1802)
    # ====================================================================
    {
        "question_id": 1802,
        "question_text": "What type of agricultural and natural science work interests you?",
        "category": "Agriculture & Nature",
        "question_type": "tree",
        "options": [
            {
                "option_id": 18021,
                "option_text": "Crop farming, agricultural science, and food production",
                "trait_tags": {"Agri-Nature": 1.0, "Field-Research": 0.4, "Realistic": 0.3, "Food-Science": 0.3, "Environmental-Sci": 0.2}
            },
            {
                "option_id": 18022,
                "option_text": "Forestry and natural resource management",
                "trait_tags": {"Agri-Nature": 0.7, "Environmental-Sci": 0.5, "Field-Research": 0.5, "Community-Serve": 0.3, "Realistic": 0.2}
            },
            {
                "option_id": 18023,
                "option_text": "Fisheries, aquaculture, and marine farming",
                "trait_tags": {"Agri-Nature": 0.6, "Maritime-Sea": 0.4, "Field-Research": 0.4, "Environmental-Sci": 0.3, "Realistic": 0.2}
            },
            {
                "option_id": 18024,
                "option_text": "Veterinary medicine and animal care",
                "trait_tags": {"Patient-Care": 0.5, "Agri-Nature": 0.5, "Lab-Research": 0.3, "Medical-Lab": 0.3, "People-Skill": 0.2}
            },
            {
                "option_id": 18025,
                "option_text": "Agricultural technology, farm systems, and improving production efficiency",
                "trait_tags": {"Agri-Nature": 1.0, "Technical-Skill": 0.3, "Field-Research": 0.3, "Realistic": 0.25, "Food-Science": 0.2}
            },
        ]
    },


    # ====================================================================
    # HOSPITALITY DOMAIN  (1803)
    # ====================================================================
    {
        "question_id": 1803,
        "question_text": "What hospitality and service industry area appeals to you?",
        "category": "Hospitality & Tourism",
        "question_type": "tree",
        "options": [
            {
                "option_id": 18031,
                "option_text": "Hotel and resort management",
                "trait_tags": {"Hospitality-Svc": 1.0, "Admin-Skill": 0.5, "People-Skill": 0.4, "Enterprising": 0.3, "Tourism-Travel": 0.2}
            },
            {
                "option_id": 18032,
                "option_text": "Tourism and travel management",
                "trait_tags": {"Tourism-Travel": 1.0, "People-Skill": 0.5, "Enterprising": 0.3, "Admin-Skill": 0.3, "Hospitality-Svc": 0.2}
            },
            {
                "option_id": 18033,
                "option_text": "Culinary arts, cooking, and food service",
                "trait_tags": {"Culinary-Arts": 1.0, "Creative-Skill": 0.4, "Hospitality-Svc": 0.4, "Food-Science": 0.3, "Artistic": 0.2}
            },
            {
                "option_id": 18034,
                "option_text": "Office and business administration",
                "trait_tags": {"Admin-Skill": 1.0, "Conventional": 0.5, "People-Skill": 0.3, "Finance-Acct": 0.3, "Analytical-Skill": 0.2}
            },
            {
                "option_id": 18035,
                "option_text": "Events, guest experiences, and tourism promotions",
                "trait_tags": {"Hospitality-Svc": 1.0, "People-Skill": 0.45, "Tourism-Travel": 0.35, "Creative-Skill": 0.2, "Enterprising": 0.2}
            },
        ]
    },


    # ====================================================================
    # VALIDATION QUESTIONS  (1901–1910)
    # Cross-cutting questions that confirm preferences across domains
    # ====================================================================
    {
        "question_id": 1901,
        "question_text": "How do you prefer to spend your typical work day?",
        "category": "Work Style",
        "question_type": "validation",
        "options": [
            {
                "option_id": 19011,
                "option_text": "Collaborating with a team and working with people",
                "trait_tags": {"People-Skill": 0.8, "Social": 0.5, "Teaching-Ed": 0.2, "Community-Serve": 0.2, "HR-Management": 0.15}
            },
            {
                "option_id": 19012,
                "option_text": "Working independently on focused, technical problems",
                "trait_tags": {"Technical-Skill": 0.6, "Investigative": 0.5, "Analytical-Skill": 0.3, "Software-Dev": 0.25, "Lab-Research": 0.2}
            },
            {
                "option_id": 19013,
                "option_text": "A mix of teamwork and independent work",
                "trait_tags": {"People-Skill": 0.4, "Technical-Skill": 0.4, "Admin-Skill": 0.2, "Analytical-Skill": 0.2, "Social": 0.15}
            },
            {
                "option_id": 19014,
                "option_text": "Interacting with clients and customers directly",
                "trait_tags": {"People-Skill": 0.7, "Enterprising": 0.5, "Hospitality-Svc": 0.2, "Marketing-Sales": 0.2, "Social": 0.15}
            },
            {
                "option_id": 19015,
                "option_text": "Working outdoors or in the field",
                "trait_tags": {"Physical-Skill": 0.6, "Field-Research": 0.5, "Realistic": 0.4, "Agri-Nature": 0.25, "Environmental-Sci": 0.2}
            },
        ]
    },

    {
        "question_id": 1902,
        "question_text": "What problem-solving approach do you naturally prefer?",
        "category": "Problem Solving",
        "question_type": "validation",
        "options": [
            {
                "option_id": 19021,
                "option_text": "Analytical and logical — breaking problems into steps",
                "trait_tags": {"Analytical-Skill": 0.8, "Investigative": 0.5, "Technical-Skill": 0.3, "Data-Analytics": 0.25, "Software-Dev": 0.2}
            },
            {
                "option_id": 19022,
                "option_text": "Creative and intuitive — finding innovative solutions",
                "trait_tags": {"Creative-Skill": 0.8, "Artistic": 0.4, "Visual-Design": 0.2, "Spatial-Design": 0.2, "Enterprising": 0.15}
            },
            {
                "option_id": 19023,
                "option_text": "Practical and hands-on — building and testing solutions",
                "trait_tags": {"Realistic": 0.6, "Technical-Skill": 0.5, "Physical-Skill": 0.3, "Mechanical-Design": 0.25, "Field-Research": 0.2}
            },
            {
                "option_id": 19024,
                "option_text": "Social and collaborative — discussing with others",
                "trait_tags": {"People-Skill": 0.7, "Social": 0.5, "Teaching-Ed": 0.2, "Counseling": 0.2, "Community-Serve": 0.15}
            },
            {
                "option_id": 19025,
                "option_text": "Research and evidence-based — gathering data first",
                "trait_tags": {"Investigative": 0.7, "Lab-Research": 0.5, "Analytical-Skill": 0.3, "Data-Analytics": 0.25, "Field-Research": 0.2}
            },
        ]
    },

    {
        "question_id": 1903,
        "question_text": "What is MOST important to you in choosing a career?",
        "category": "Career Values",
        "question_type": "validation",
        "options": [
            {
                "option_id": 19031,
                "option_text": "High salary and financial stability",
                "trait_tags": {"Enterprising": 0.6, "Finance-Acct": 0.3, "Technical-Skill": 0.2, "Conventional": 0.2, "Admin-Skill": 0.15}
            },
            {
                "option_id": 19032,
                "option_text": "Helping others and making a positive difference",
                "trait_tags": {"Social": 0.7, "Patient-Care": 0.3, "Community-Serve": 0.3, "People-Skill": 0.2, "Teaching-Ed": 0.15}
            },
            {
                "option_id": 19033,
                "option_text": "Creative expression and artistic freedom",
                "trait_tags": {"Creative-Skill": 0.7, "Artistic": 0.5, "Visual-Design": 0.2, "Performing-Arts": 0.2, "Spatial-Design": 0.15}
            },
            {
                "option_id": 19034,
                "option_text": "Job stability and security",
                "trait_tags": {"Conventional": 0.5, "Admin-Skill": 0.3, "Realistic": 0.2, "Technical-Skill": 0.2, "Finance-Acct": 0.15}
            },
            {
                "option_id": 19035,
                "option_text": "Adventure, travel, and new experiences",
                "trait_tags": {"Physical-Skill": 0.4, "Maritime-Sea": 0.3, "Tourism-Travel": 0.3, "Field-Research": 0.2, "Agri-Nature": 0.15}
            },
        ]
    },

    {
        "question_id": 1904,
        "question_text": "What kind of workplace environment do you prefer?",
        "category": "Work Environment",
        "question_type": "validation",
        "options": [
            {
                "option_id": 19041,
                "option_text": "A modern office with computers and technology",
                "trait_tags": {"Technical-Skill": 0.5, "Software-Dev": 0.3, "Data-Analytics": 0.2, "Analytical-Skill": 0.2, "Cloud-Systems": 0.15}
            },
            {
                "option_id": 19042,
                "option_text": "A hospital, clinic, or healthcare facility",
                "trait_tags": {"Patient-Care": 0.5, "Medical-Lab": 0.4, "People-Skill": 0.2, "Community-Serve": 0.2, "Social": 0.15}
            },
            {
                "option_id": 19043,
                "option_text": "A laboratory or research facility",
                "trait_tags": {"Lab-Research": 0.6, "Investigative": 0.4, "Medical-Lab": 0.2, "Analytical-Skill": 0.25, "Technical-Skill": 0.2}
            },
            {
                "option_id": 19044,
                "option_text": "Outdoors — construction sites, farms, or nature",
                "trait_tags": {"Physical-Skill": 0.5, "Civil-Build": 0.3, "Agri-Nature": 0.3, "Field-Research": 0.3, "Realistic": 0.2}
            },
            {
                "option_id": 19045,
                "option_text": "A creative studio — design workshop, art studio, or media house",
                "trait_tags": {"Creative-Skill": 0.5, "Visual-Design": 0.4, "Artistic": 0.3, "Digital-Media": 0.25, "Animation-3D": 0.2}
            },
        ]
    },

    {
        "question_id": 1905,
        "question_text": "How do you prefer to handle new challenges?",
        "category": "Challenge Style",
        "question_type": "validation",
        "options": [
            {
                "option_id": 19051,
                "option_text": "Research and analyze before acting",
                "trait_tags": {"Investigative": 0.7, "Analytical-Skill": 0.5, "Lab-Research": 0.2, "Data-Analytics": 0.2, "Technical-Skill": 0.15}
            },
            {
                "option_id": 19052,
                "option_text": "Try different creative approaches until something works",
                "trait_tags": {"Creative-Skill": 0.6, "Enterprising": 0.4, "Artistic": 0.2, "Visual-Design": 0.2, "Digital-Media": 0.15}
            },
            {
                "option_id": 19053,
                "option_text": "Consult experts and learn from others' experiences",
                "trait_tags": {"People-Skill": 0.5, "Social": 0.4, "Teaching-Ed": 0.2, "Analytical-Skill": 0.2, "Investigative": 0.15}
            },
            {
                "option_id": 19054,
                "option_text": "Take charge and lead a team to solve it",
                "trait_tags": {"Enterprising": 0.6, "People-Skill": 0.4, "Admin-Skill": 0.3, "HR-Management": 0.2, "Social": 0.15}
            },
            {
                "option_id": 19055,
                "option_text": "Follow a methodical, step-by-step process",
                "trait_tags": {"Conventional": 0.5, "Analytical-Skill": 0.4, "Technical-Skill": 0.3, "Admin-Skill": 0.25, "Investigative": 0.2}
            },
        ]
    },

    {
        "question_id": 1906,
        "question_text": "What skill would you most like to develop and master?",
        "category": "Skill Development",
        "question_type": "validation",
        "options": [
            {
                "option_id": 19061,
                "option_text": "Technical and computer skills",
                "trait_tags": {"Technical-Skill": 0.7, "Software-Dev": 0.3, "Hardware-Systems": 0.2, "Analytical-Skill": 0.2, "Data-Analytics": 0.15}
            },
            {
                "option_id": 19062,
                "option_text": "Medical and health sciences knowledge",
                "trait_tags": {"Patient-Care": 0.5, "Medical-Lab": 0.4, "Lab-Research": 0.2, "Public-Health": 0.2, "Investigative": 0.15}
            },
            {
                "option_id": 19063,
                "option_text": "Creative and artistic abilities",
                "trait_tags": {"Creative-Skill": 0.7, "Visual-Design": 0.3, "Artistic": 0.3, "Digital-Media": 0.2, "Spatial-Design": 0.15}
            },
            {
                "option_id": 19064,
                "option_text": "Business and financial expertise",
                "trait_tags": {"Finance-Acct": 0.5, "Enterprising": 0.4, "Admin-Skill": 0.3, "Analytical-Skill": 0.25, "Marketing-Sales": 0.2}
            },
            {
                "option_id": 19065,
                "option_text": "Communication and leadership abilities",
                "trait_tags": {"People-Skill": 0.6, "Enterprising": 0.4, "Teaching-Ed": 0.2, "Social": 0.2, "HR-Management": 0.15}
            },
        ]
    },

    {
        "question_id": 1907,
        "question_text": "Which school subject have you always enjoyed the most?",
        "category": "Academic Preference",
        "question_type": "validation",
        "options": [
            {
                "option_id": 19071,
                "option_text": "Math and Science",
                "trait_tags": {"Analytical-Skill": 0.6, "Investigative": 0.5, "Lab-Research": 0.3, "Data-Analytics": 0.25, "Technical-Skill": 0.2}
            },
            {
                "option_id": 19072,
                "option_text": "English, Literature, and Languages",
                "trait_tags": {"Creative-Skill": 0.4, "People-Skill": 0.4, "Teaching-Ed": 0.3, "Social": 0.25, "Artistic": 0.2}
            },
            {
                "option_id": 19073,
                "option_text": "Social Studies, History, and Civics",
                "trait_tags": {"Community-Serve": 0.5, "Social": 0.4, "People-Skill": 0.3, "Investigative": 0.25, "Teaching-Ed": 0.2}
            },
            {
                "option_id": 19074,
                "option_text": "Arts, Music, and Creative subjects",
                "trait_tags": {"Artistic": 0.6, "Creative-Skill": 0.5, "Visual-Design": 0.2, "Performing-Arts": 0.25, "Digital-Media": 0.2}
            },
            {
                "option_id": 19075,
                "option_text": "Computer and Technology subjects",
                "trait_tags": {"Technical-Skill": 0.6, "Software-Dev": 0.4, "Investigative": 0.2, "Data-Analytics": 0.25, "Analytical-Skill": 0.2}
            },
        ]
    },

    {
        "question_id": 1908,
        "question_text": "What extracurricular activity appeals to you the most?",
        "category": "Activities",
        "question_type": "validation",
        "options": [
            {
                "option_id": 19081,
                "option_text": "Science club, coding, or robotics",
                "trait_tags": {"Technical-Skill": 0.5, "Software-Dev": 0.4, "Investigative": 0.3, "Hardware-Systems": 0.2, "Analytical-Skill": 0.2}
            },
            {
                "option_id": 19082,
                "option_text": "Sports teams and athletic activities",
                "trait_tags": {"Physical-Skill": 0.6, "Sports-Ed": 0.4, "People-Skill": 0.2, "Realistic": 0.2, "Community-Serve": 0.15}
            },
            {
                "option_id": 19083,
                "option_text": "Art club, drama, music, or creative writing",
                "trait_tags": {"Creative-Skill": 0.6, "Artistic": 0.4, "Performing-Arts": 0.3, "Visual-Design": 0.2, "Social": 0.15}
            },
            {
                "option_id": 19084,
                "option_text": "Student government and leadership organizations",
                "trait_tags": {"Enterprising": 0.5, "People-Skill": 0.5, "Admin-Skill": 0.3, "Community-Serve": 0.2, "Social": 0.15}
            },
            {
                "option_id": 19085,
                "option_text": "Community service and volunteer work",
                "trait_tags": {"Community-Serve": 0.6, "Social": 0.5, "People-Skill": 0.3, "Teaching-Ed": 0.2, "Social-Work": 0.15}
            },
        ]
    },

    {
        "question_id": 1909,
        "question_text": "Where do you see yourself working in 10 years?",
        "category": "Future Vision",
        "question_type": "validation",
        "options": [
            {
                "option_id": 19091,
                "option_text": "At a technology or software company",
                "trait_tags": {"Software-Dev": 0.5, "Technical-Skill": 0.4, "Data-Analytics": 0.2, "Analytical-Skill": 0.2, "Investigative": 0.15}
            },
            {
                "option_id": 19092,
                "option_text": "In a hospital, clinic, or healthcare organization",
                "trait_tags": {"Patient-Care": 0.5, "Medical-Lab": 0.3, "Rehab-Therapy": 0.2, "People-Skill": 0.2, "Social": 0.15}
            },
            {
                "option_id": 19093,
                "option_text": "At an engineering or construction firm",
                "trait_tags": {"Civil-Build": 0.4, "Mechanical-Design": 0.4, "Technical-Skill": 0.3, "Realistic": 0.2, "Analytical-Skill": 0.15}
            },
            {
                "option_id": 19094,
                "option_text": "Running your own business or startup",
                "trait_tags": {"Startup-Venture": 0.6, "Enterprising": 0.5, "Marketing-Sales": 0.2, "Finance-Acct": 0.2, "HR-Management": 0.15}
            },
            {
                "option_id": 19095,
                "option_text": "Teaching at a school or university",
                "trait_tags": {"Teaching-Ed": 0.7, "People-Skill": 0.4, "Social": 0.2, "Community-Serve": 0.2, "Counseling": 0.15}
            },
            {
                "option_id": 19096,
                "option_text": "Working at a creative or design studio",
                "trait_tags": {"Creative-Skill": 0.6, "Visual-Design": 0.4, "Digital-Media": 0.2, "Artistic": 0.2, "Animation-3D": 0.15}
            },
        ]
    },

    {
        "question_id": 1910,
        "question_text": "What kind of impact do you want to make in the world?",
        "category": "Life Purpose",
        "question_type": "validation",
        "options": [
            {
                "option_id": 19101,
                "option_text": "Innovate with technology and drive digital transformation",
                "trait_tags": {"Software-Dev": 0.4, "Technical-Skill": 0.4, "AI-ML": 0.3, "Enterprising": 0.2, "Data-Analytics": 0.15}
            },
            {
                "option_id": 19102,
                "option_text": "Save lives and improve people's health",
                "trait_tags": {"Patient-Care": 0.5, "Medical-Lab": 0.3, "Social": 0.3, "Community-Serve": 0.2, "Public-Health": 0.15}
            },
            {
                "option_id": 19103,
                "option_text": "Build infrastructure that improves communities",
                "trait_tags": {"Civil-Build": 0.5, "Community-Serve": 0.4, "Technical-Skill": 0.2, "Environmental-Eng": 0.2, "Analytical-Skill": 0.15}
            },
            {
                "option_id": 19104,
                "option_text": "Create economic growth and business opportunities",
                "trait_tags": {"Enterprising": 0.5, "Finance-Acct": 0.3, "Marketing-Sales": 0.3, "Startup-Venture": 0.2, "Admin-Skill": 0.15}
            },
            {
                "option_id": 19105,
                "option_text": "Inspire and educate future generations",
                "trait_tags": {"Teaching-Ed": 0.6, "People-Skill": 0.4, "Social": 0.3, "Community-Serve": 0.2, "Counseling": 0.15}
            },
            {
                "option_id": 19106,
                "option_text": "Bring beauty and meaning through art and creativity",
                "trait_tags": {"Creative-Skill": 0.6, "Artistic": 0.5, "Visual-Design": 0.2, "Performing-Arts": 0.2, "Digital-Media": 0.15}
            },
        ]
    },
]


# ================================================================================
# TREE NAVIGATION — (question_id, option_id) → next_question_id
# Maps each option to the next question in the decision tree.
# If a (question_id, option_id) pair is NOT in this dict, it's a leaf node.
# ================================================================================

TREE_NAVIGATION = {
    # Technology root (1001) → branches
    (1001, 10011): 1002,  # Software → Programming types
    (1001, 10012): 1003,  # Hardware → Hardware/Networks
    (1001, 10013): 1004,  # Data → Data work
    (1001, 10014): 1005,  # Security → Cybersecurity
    (1001, 10015): 1006,  # Digital media → Creative content
    (1001, 10016): 1007,  # Game dev → Game aspects

    # Software (1002) → deeper programming
    (1002, 10021): 1008,  # AI/ML → Deep programming
    (1002, 10022): 1008,  # Mobile → Deep programming
    (1002, 10023): 1009,  # Web → Web deeper
    (1002, 10024): 1008,  # Enterprise → Deep programming
    (1002, 10025): 1008,  # Automation → Deep programming

    # Digital media (1006) → creative environment
    (1006, 10061): 1010,  # Graphic design → Creative env
    (1006, 10062): 1010,  # Video prod → Creative env
    (1006, 10063): 1010,  # Animation → Creative env
    (1006, 10064): 1010,  # Audio → Creative env
    (1006, 10065): 1010,  # Web design → Creative env

    # Healthcare root (1101) → branches
    (1101, 11011): 1102,  # Patient care → Patient care types
    (1101, 11012): 1103,  # Lab → Lab types
    (1101, 11013): 1104,  # Therapy → Therapy types
    (1101, 11014): 1105,  # Pharmacy → Pharmacy types
    # 11015 (Public health) → leaf
    # 11016 (Nutrition) → leaf

    # Patient care (1102) admin branch can go deeper
    (1102, 11026): 1106,  # Health admin → Admin deeper

    # Engineering root (1201) → branches
    (1201, 12011): 1202,  # Civil → Civil types
    (1201, 12012): 1203,  # Mechanical → Mechanical types
    # 12013 (Electrical) → leaf
    # 12014 (Industrial) → leaf
    (1201, 12015): 1204,  # Spatial design → Design types
    # 12016 (Aerospace) → leaf

    # Business root (1301) → branches
    (1301, 13011): 1302,  # Finance → Finance types
    # 13012-13016 → leaf

    # Arts root (1401) → branches
    (1401, 14011): 1402,  # Visual arts → Visual arts types
    (1401, 14012): 1403,  # Digital arts → Digital arts types
    (1401, 14013): 1404,  # Performing → Performing types
    # 14014-14016 → leaf

    # Science root (1601) → branches
    (1601, 16011): 1602,  # Biology → Biology directions
    # 16012 (Chemistry) → leaf
    # 16013 (Physics) → leaf
    (1601, 16014): 1603,  # Environment → Environmental types
    # 16015 (Math) → leaf
    # 16016 (Food science) → leaf

    # Public Service root (1701) → branches
    (1701, 17011): 1702,  # Law enforcement → Law enforcement types
    # 17012-17015 → leaf
}


# ================================================================================
# DOMAIN ROOTS — domain name → root question_id
# The first question asked when a user's profile maps to this domain.
# ================================================================================

DOMAIN_ROOTS = {
    "technology":    1001,
    "healthcare":    1101,
    "engineering":   1201,
    "business":      1301,
    "arts":          1401,
    "education":     1501,
    "science":       1601,
    "public_service": 1701,
    "maritime":      1801,
    "agriculture":   1802,
    "hospitality":   1803,
    "creative":      1401,  # alias for arts
    "physical":      1501,  # physical maps to education (sports sub)
}


# ================================================================================
# INTEREST_TO_DOMAIN — maps user's interest/skill IDs to a domain name
# Used to determine which tree branch to start from based on the user's profile.
# ================================================================================

INTEREST_TO_DOMAIN = {
    # Technology interests
    "programming": "technology",
    "computer": "technology",
    "data": "technology",
    "ai": "technology",
    "cybersecurity": "technology",
    "robotics": "technology",
    "game_dev": "technology",
    "web_tech": "technology",
    "multimedia": "technology",
    "networking": "technology",
    "software_eng": "technology",
    "database": "technology",
    "health_info": "technology",

    # Healthcare interests
    "medical": "healthcare",
    "nursing": "healthcare",
    "psychology": "healthcare",
    "pharmacy": "healthcare",
    "physical_therapy": "healthcare",
    "nutrition": "healthcare",
    "medical_tech": "healthcare",
    "dentistry": "healthcare",
    "occupational_therapy": "healthcare",
    "speech_therapy": "healthcare",
    "respiratory": "healthcare",
    "radiology": "healthcare",
    "optometry": "healthcare",
    "midwifery": "healthcare",
    "public_health": "healthcare",
    "biotechnology": "healthcare",

    # Engineering interests
    "engineering": "engineering",
    "mechanical": "engineering",
    "electrical": "engineering",
    "civil": "engineering",
    "architecture": "engineering",
    "industrial": "engineering",
    "aeronautical": "engineering",
    "geodetic": "engineering",
    "landscape": "engineering",
    "industrial_design": "engineering",
    "aircraft_maint": "engineering",
    "marine_eng": "engineering",

    # Business interests
    "business": "business",
    "finance": "business",
    "marketing": "business",
    "accounting": "business",
    "economics": "business",
    "management": "business",
    "real_estate": "business",
    "human_resource": "business",
    "operations": "business",
    "customs": "business",
    "agribusiness": "business",
    "office_admin": "business",
    "startup": "business",

    # Arts & Creative interests
    "art": "arts",
    "music": "arts",
    "film": "arts",
    "writing": "arts",
    "photography": "arts",
    "animation": "arts",
    "fashion": "arts",
    "theater": "arts",
    "advertising_arts": "arts",
    "music_production": "arts",
    "fine_arts": "arts",
    "clothing_tech": "arts",

    # Education
    "education": "education",
    "early_childhood": "education",
    "special_education": "education",
    "library_science": "education",

    # Science
    "science": "science",
    "biology": "science",
    "chemistry": "science",
    "physics": "science",
    "environment": "science",
    "earth_science": "science",
    "marine_science": "science",
    "meteorology": "science",
    "statistics": "science",
    "food_science": "science",
    "forensic_science": "science",
    "env_planning": "science",

    # Public Service
    "law": "public_service",
    "politics": "public_service",
    "social": "public_service",
    "history": "public_service",
    "communication": "public_service",
    "philosophy": "public_service",
    "criminology": "public_service",
    "public_admin": "public_service",
    "intl_studies": "public_service",
    "sociology": "public_service",
    "linguistics": "public_service",
    "dev_communication": "public_service",
    "community_dev": "public_service",
    "legal_mgmt": "public_service",

    # Maritime & Aviation
    "maritime": "maritime",
    "aviation": "maritime",
    "logistics": "maritime",
    "marine_transport": "maritime",

    # Agriculture & Nature
    "agriculture": "agriculture",
    "veterinary": "agriculture",
    "forestry": "agriculture",
    "fisheries": "agriculture",

    # Sports
    "sports": "education",
    "exercise_science": "education",
    "tvet": "education",
    "sports_fitness": "education",

    # Hospitality & Tourism
    "tourism": "hospitality",
    "food": "hospitality",
    "hotel_mgmt": "hospitality",
    "culinary_mgmt": "hospitality",

    # Skills → domain mapping
    "programming_skill": "technology",
    "data_analysis": "technology",
    "web_development": "technology",
    "graphic_design": "arts",
    "video_editing": "arts",
    "mobile_dev": "technology",
    "ux_ui": "technology",
    "networking_skill": "technology",
    "database_skill": "technology",
    "patient_care": "healthcare",
    "counseling": "healthcare",
    "first_aid": "healthcare",
    "lab_equipment": "healthcare",
    "elderly_care": "healthcare",
    "electronics": "engineering",
    "drafting": "engineering",
    "machine_operation": "engineering",
    "quality_control": "engineering",
    "surveying": "engineering",
    "accounting_skill": "business",
    "negotiation": "business",
    "budgeting": "business",
    "strategic_thinking": "business",
    "financial_analysis": "business",
    "artistic": "arts",
    "creativity": "arts",
    "storytelling": "arts",
    "design_thinking": "arts",
    "photography_skill": "arts",
    "music_skill": "arts",
    "audio_production": "arts",
    "film_editing": "arts",
    "mentoring": "education",
    "child_interaction": "education",
    "public_speaking": "education",
    "laboratory": "science",
    "scientific_method": "science",
    "statistical_analysis": "science",
    "env_assessment": "science",
    "research": "science",
    "case_analysis": "public_service",
    "policy_analysis": "public_service",
    "interviewing": "public_service",
    "navigation": "maritime",
    "flight_ops": "maritime",
    "gardening": "agriculture",
    "cooking": "hospitality",
    "customer_service": "hospitality",
    "event_management": "hospitality",
}


# ================================================================================
# DOMAIN ADJACENCY — for secondary domain fallback
# When only one domain is detected, the first adjacent domain becomes secondary.
# ================================================================================

DOMAIN_ADJACENCY = {
    "technology":     ["engineering", "science", "arts", "business"],
    "healthcare":     ["science", "education", "public_service"],
    "engineering":    ["technology", "science", "maritime"],
    "business":       ["technology", "hospitality", "public_service"],
    "arts":           ["technology", "education", "hospitality"],
    "education":      ["healthcare", "arts", "public_service"],
    "science":        ["technology", "healthcare", "engineering", "agriculture"],
    "public_service": ["education", "business", "healthcare"],
    "maritime":       ["engineering", "technology"],
    "agriculture":    ["science", "engineering", "hospitality"],
    "hospitality":    ["business", "arts", "agriculture"],
    "creative":       ["technology", "education", "hospitality"],
    "physical":       ["healthcare", "education"],
}


# ================================================================================
# STRAND_TO_DOMAIN — maps SHS strand to a default domain
# Used as fallback when no interests/skills are specified.
# ================================================================================

STRAND_TO_DOMAIN = {
    "STEM":    "technology",
    "ABM":     "business",
    "HUMSS":   "public_service",
    "TVL":     "technology",
    "GAS":     "technology",   # general academic → default technology
    "SPORTS":  "education",
    "ARTS":    "arts",
}


# ================================================================================
# VALIDATION_QUESTION_IDS — questions used in validation phase
# ================================================================================

VALIDATION_QUESTION_IDS = [1901, 1902, 1903, 1904, 1905, 1906, 1907, 1908, 1909, 1910]


# ================================================================================
# DERIVED STRUCTURES (built from DECISION_TREE_QUESTIONS)
# ================================================================================

# TREE_QUESTION_MAP: question_id → full question dict (for fast lookup)
TREE_QUESTION_MAP = {q["question_id"]: q for q in DECISION_TREE_QUESTIONS}

# ALL_TREE_QUESTION_IDS: set of all tree question IDs (for filtering from supplementary pool)
ALL_TREE_QUESTION_IDS = set(TREE_QUESTION_MAP.keys())

# Print summary on import
print(f"[TREE] Loaded {len(DECISION_TREE_QUESTIONS)} decision tree questions across {len(DOMAIN_ROOTS)} domains")
print(f"[TREE] Navigation rules: {len(TREE_NAVIGATION)} branch transitions")
print(f"[TREE] Validation questions: {len(VALIDATION_QUESTION_IDS)}")
