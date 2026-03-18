# questions_enhanced.py - Enhanced Questions with 8-10 Options Each
"""
================================================================================
ENHANCED QUESTIONS - Course-Specific Options (8-10 options per question)
================================================================================

Each question has 8-10 options that lead to SPECIFIC courses or course groups:
- Every option maps to a trait that connects to real courses
- Options cover diverse career paths for comprehensive matching
- Questions are designed for Filipino SHS students

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
    # ==================== CAREER DISCOVERY QUESTIONS ====================
    {
        "question_id": 1,
        "question_text": "What career would make you excited to wake up every morning?",
        "category": "Dream Career",
        "options": [
            {"option_id": 1, "option_text": "Nurse caring for patients in a hospital", "trait_tag": "Patient-Care"},
            {"option_id": 2, "option_text": "Software developer creating apps and websites", "trait_tag": "Software-Dev"},
            {"option_id": 3, "option_text": "Civil engineer designing buildings and bridges", "trait_tag": "Civil-Build"},
            {"option_id": 4, "option_text": "Accountant managing finances for companies", "trait_tag": "Finance-Acct"},
            {"option_id": 5, "option_text": "Teacher educating students in a classroom", "trait_tag": "Teaching-Ed"},
            {"option_id": 6, "option_text": "Police officer protecting the community", "trait_tag": "Law-Enforce"},
            {"option_id": 7, "option_text": "Graphic designer creating visual content", "trait_tag": "Visual-Design"},
            {"option_id": 8, "option_text": "Ship captain navigating across oceans", "trait_tag": "Maritime-Sea"},
            {"option_id": 9, "option_text": "Business owner running my own company", "trait_tag": "Startup-Venture"},
            {"option_id": 10, "option_text": "Hotel manager in the hospitality industry", "trait_tag": "Hospitality-Svc"}
        ]
    },
    {
        "question_id": 2,
        "question_text": "Where would you most enjoy working every day?",
        "category": "Work Environment",
        "options": [
            {"option_id": 11, "option_text": "Hospital or clinic with patients", "trait_tag": "Patient-Care"},
            {"option_id": 12, "option_text": "Medical laboratory analyzing samples", "trait_tag": "Medical-Lab"},
            {"option_id": 13, "option_text": "Tech office with computers and code", "trait_tag": "Software-Dev"},
            {"option_id": 14, "option_text": "Construction site or engineering firm", "trait_tag": "Civil-Build"},
            {"option_id": 15, "option_text": "Bank or corporate office", "trait_tag": "Finance-Acct"},
            {"option_id": 16, "option_text": "School or university classroom", "trait_tag": "Teaching-Ed"},
            {"option_id": 17, "option_text": "Police station or courtroom", "trait_tag": "Law-Enforce"},
            {"option_id": 18, "option_text": "Design studio or creative agency", "trait_tag": "Visual-Design"},
            {"option_id": 19, "option_text": "Ship or port facility", "trait_tag": "Maritime-Sea"},
            {"option_id": 20, "option_text": "Farm or outdoor natural environment", "trait_tag": "Agri-Nature"}
        ]
    },
    {
        "question_id": 3,
        "question_text": "What type of daily tasks would you find most fulfilling?",
        "category": "Daily Work",
        "options": [
            {"option_id": 21, "option_text": "Caring for sick people and checking vital signs", "trait_tag": "Patient-Care"},
            {"option_id": 22, "option_text": "Running tests and analyzing samples in a lab", "trait_tag": "Medical-Lab"},
            {"option_id": 23, "option_text": "Writing code and debugging software", "trait_tag": "Software-Dev"},
            {"option_id": 24, "option_text": "Calculating budgets and preparing financial reports", "trait_tag": "Finance-Acct"},
            {"option_id": 25, "option_text": "Explaining lessons and helping students understand", "trait_tag": "Teaching-Ed"},
            {"option_id": 26, "option_text": "Investigating crimes and gathering evidence", "trait_tag": "Law-Enforce"},
            {"option_id": 27, "option_text": "Creating designs and visual artwork", "trait_tag": "Visual-Design"},
            {"option_id": 28, "option_text": "Managing hotel guests and tourism services", "trait_tag": "Hospitality-Svc"},
            {"option_id": 29, "option_text": "Operating ship equipment and navigation", "trait_tag": "Maritime-Sea"},
            {"option_id": 30, "option_text": "Planting crops and managing farmland", "trait_tag": "Agri-Nature"}
        ]
    },
    {
        "question_id": 4,
        "question_text": "Which skill would you most want to become an expert in?",
        "category": "Skill Mastery",
        "options": [
            {"option_id": 31, "option_text": "Medical procedures and patient care", "trait_tag": "Patient-Care"},
            {"option_id": 32, "option_text": "Laboratory analysis and diagnostics", "trait_tag": "Medical-Lab"},
            {"option_id": 33, "option_text": "Programming and software development", "trait_tag": "Software-Dev"},
            {"option_id": 34, "option_text": "Building design and construction", "trait_tag": "Civil-Build"},
            {"option_id": 35, "option_text": "Financial analysis and accounting", "trait_tag": "Finance-Acct"},
            {"option_id": 36, "option_text": "Teaching and education methods", "trait_tag": "Teaching-Ed"},
            {"option_id": 37, "option_text": "Criminal investigation techniques", "trait_tag": "Law-Enforce"},
            {"option_id": 38, "option_text": "Graphic design and visual arts", "trait_tag": "Visual-Design"},
            {"option_id": 39, "option_text": "Marketing and sales strategies", "trait_tag": "Marketing-Sales"},
            {"option_id": 40, "option_text": "Data analysis and statistics", "trait_tag": "Data-Analytics"}
        ]
    },
    {
        "question_id": 5,
        "question_text": "What achievement would make you most proud?",
        "category": "Career Achievement",
        "options": [
            {"option_id": 41, "option_text": "Saving someone's life as a healthcare worker", "trait_tag": "Patient-Care"},
            {"option_id": 42, "option_text": "Discovering a disease through lab analysis", "trait_tag": "Medical-Lab"},
            {"option_id": 43, "option_text": "Creating an app used by millions", "trait_tag": "Software-Dev"},
            {"option_id": 44, "option_text": "Building a bridge or skyscraper", "trait_tag": "Civil-Build"},
            {"option_id": 45, "option_text": "Helping a company become profitable", "trait_tag": "Finance-Acct"},
            {"option_id": 46, "option_text": "Students thanking me for changing their lives", "trait_tag": "Teaching-Ed"},
            {"option_id": 47, "option_text": "Solving a major crime case", "trait_tag": "Law-Enforce"},
            {"option_id": 48, "option_text": "Designing a famous logo or artwork", "trait_tag": "Visual-Design"},
            {"option_id": 49, "option_text": "Building a successful business from scratch", "trait_tag": "Startup-Venture"},
            {"option_id": 50, "option_text": "Helping my community through public service", "trait_tag": "Community-Serve"}
        ]
    },


        # ==================== SITUATIONAL QUESTIONS ====================
    {
        "question_id": 23,
        "question_text": "SITUATION: Someone collapses in front of you. What's your first instinct?",
        "category": "Situational - Emergency",
        "options": [
            {"option_id": 221, "option_text": "Rush to help - check pulse, do CPR if needed", "trait_tag": "Patient-Care"},
            {"option_id": 222, "option_text": "Call emergency services immediately", "trait_tag": "Admin-Skill"},
            {"option_id": 223, "option_text": "Look for a medical professional nearby", "trait_tag": "People-Skill"},
            {"option_id": 224, "option_text": "Control the crowd and maintain order", "trait_tag": "Law-Enforce"},
            {"option_id": 225, "option_text": "Document what happened for records", "trait_tag": "Law-Enforce"},
            {"option_id": 226, "option_text": "Comfort the person emotionally", "trait_tag": "People-Skill"},
            {"option_id": 227, "option_text": "Check if they need specific medication", "trait_tag": "Medical-Lab"},
            {"option_id": 228, "option_text": "Direct traffic if we're on the road", "trait_tag": "Civil-Build"},
            {"option_id": 229, "option_text": "I might freeze - emergencies stress me out", "trait_tag": "Software-Dev"},
            {"option_id": 230, "option_text": "Film it for evidence (with permission)", "trait_tag": "Digital-Media"}
        ]
    },
    {
        "question_id": 24,
        "question_text": "SITUATION: Your group project member isn't contributing. What do you do?",
        "category": "Situational - Teamwork",
        "options": [
            {"option_id": 231, "option_text": "Talk to them privately and understand why", "trait_tag": "People-Skill"},
            {"option_id": 232, "option_text": "Take charge and redistribute tasks", "trait_tag": "Startup-Venture"},
            {"option_id": 233, "option_text": "Report to the teacher", "trait_tag": "Admin-Skill"},
            {"option_id": 234, "option_text": "Do their work myself to ensure quality", "trait_tag": "Technical-Skill"},
            {"option_id": 235, "option_text": "Create a detailed schedule with deadlines", "trait_tag": "Finance-Acct"},
            {"option_id": 236, "option_text": "Focus on my creative part and let others manage", "trait_tag": "Visual-Design"},
            {"option_id": 237, "option_text": "Motivate them with encouragement", "trait_tag": "Teaching-Ed"},
            {"option_id": 238, "option_text": "Find a compromise that works for everyone", "trait_tag": "Community-Serve"},
            {"option_id": 239, "option_text": "Analyze what's causing the delay", "trait_tag": "Data-Analytics"},
            {"option_id": 240, "option_text": "Document everything for accountability", "trait_tag": "Law-Enforce"}
        ]
    },
    {
        "question_id": 25,
        "question_text": "SITUATION: You witness a car accident. What's your immediate reaction?",
        "category": "Situational - Accident",
        "options": [
            {"option_id": 241, "option_text": "Check if anyone is injured and provide first aid", "trait_tag": "Patient-Care"},
            {"option_id": 242, "option_text": "Call 911/emergency services right away", "trait_tag": "Admin-Skill"},
            {"option_id": 243, "option_text": "Direct traffic to prevent more accidents", "trait_tag": "Law-Enforce"},
            {"option_id": 244, "option_text": "Document the scene as a witness", "trait_tag": "Law-Enforce"},
            {"option_id": 245, "option_text": "Comfort and calm the people involved", "trait_tag": "People-Skill"},
            {"option_id": 246, "option_text": "Assess the vehicle damage technically", "trait_tag": "Mechanical-Design"},
            {"option_id": 247, "option_text": "Look for fire hazards or fuel leaks", "trait_tag": "Civil-Build"},
            {"option_id": 248, "option_text": "Take photos for insurance purposes", "trait_tag": "Digital-Media"},
            {"option_id": 249, "option_text": "Help move vehicles off the road", "trait_tag": "Physical-Skill"},
            {"option_id": 250, "option_text": "Find professionals to handle it", "trait_tag": "Finance-Acct"}
        ]
    },

    # ==================== SCALE-BASED SELF-ASSESSMENT ====================
    {
        "question_id": 26,
        "question_text": "Rate your agreement: 'I enjoy solving complex math problems.'",
        "category": "Scale - Math",
        "options": [
            {"option_id": 251, "option_text": "Strongly Agree - Math is my favorite subject", "trait_tag": "Data-Analytics"},
            {"option_id": 252, "option_text": "Agree - I'm good at math", "trait_tag": "Finance-Acct"},
            {"option_id": 253, "option_text": "Somewhat Agree - I can do math when I try", "trait_tag": "Civil-Build"},
            {"option_id": 254, "option_text": "Neutral - Math is just okay", "trait_tag": "Admin-Skill"},
            {"option_id": 255, "option_text": "Somewhat Disagree - Math is challenging", "trait_tag": "Teaching-Ed"},
            {"option_id": 256, "option_text": "Disagree - I prefer other subjects", "trait_tag": "Visual-Design"},
            {"option_id": 257, "option_text": "Strongly Disagree - I avoid math", "trait_tag": "Creative-Skill"},
            {"option_id": 258, "option_text": "I prefer applied math in real-world scenarios", "trait_tag": "Finance-Acct"},
            {"option_id": 259, "option_text": "I prefer physics/engineering math", "trait_tag": "Electrical-Power"},
            {"option_id": 260, "option_text": "I prefer statistics and data math", "trait_tag": "Data-Analytics"}
        ]
    },
    {
        "question_id": 27,
        "question_text": "Rate your agreement: 'I stay calm under pressure and stress.'",
        "category": "Scale - Stress",
        "options": [
            {"option_id": 261, "option_text": "Strongly Agree - I thrive in emergencies", "trait_tag": "Patient-Care"},
            {"option_id": 262, "option_text": "Agree - I handle stress well", "trait_tag": "Law-Enforce"},
            {"option_id": 263, "option_text": "Somewhat Agree - I manage stress reasonably", "trait_tag": "Maritime-Sea"},
            {"option_id": 264, "option_text": "Neutral - Depends on the situation", "trait_tag": "Admin-Skill"},
            {"option_id": 265, "option_text": "Somewhat Disagree - I get anxious sometimes", "trait_tag": "Teaching-Ed"},
            {"option_id": 266, "option_text": "Disagree - I prefer calm environments", "trait_tag": "Lab-Research"},
            {"option_id": 267, "option_text": "Strongly Disagree - Stress overwhelms me", "trait_tag": "Visual-Design"},
            {"option_id": 268, "option_text": "I handle physical stress better", "trait_tag": "Physical-Skill"},
            {"option_id": 269, "option_text": "I handle mental/analytical stress better", "trait_tag": "Data-Analytics"},
            {"option_id": 270, "option_text": "I handle social/people stress better", "trait_tag": "People-Skill"}
        ]
    },
    {
        "question_id": 28,
        "question_text": "Rate your COMMUNICATION skills (1=Needs Work, 5=Excellent)",
        "category": "Scale - Communication",
        "options": [
            {"option_id": 271, "option_text": "5 - Excellent presenter and speaker", "trait_tag": "Marketing-Sales"},
            {"option_id": 272, "option_text": "4 - Good communicator", "trait_tag": "Teaching-Ed"},
            {"option_id": 273, "option_text": "4 - Good writer, prefer writing over speaking", "trait_tag": "Admin-Skill"},
            {"option_id": 274, "option_text": "3 - Average communication skills", "trait_tag": "Technical-Skill"},
            {"option_id": 275, "option_text": "3 - Better one-on-one than groups", "trait_tag": "Patient-Care"},
            {"option_id": 276, "option_text": "2 - Communication is challenging", "trait_tag": "Software-Dev"},
            {"option_id": 277, "option_text": "1 - Prefer minimal communication roles", "trait_tag": "Lab-Research"},
            {"option_id": 278, "option_text": "Better at visual communication", "trait_tag": "Visual-Design"},
            {"option_id": 279, "option_text": "Better at technical communication", "trait_tag": "Data-Analytics"},
            {"option_id": 280, "option_text": "Better at persuasive communication", "trait_tag": "Startup-Venture"}
        ]
    },
    {
        "question_id": 29,
        "question_text": "Rate your PHYSICAL FITNESS level:",
        "category": "Scale - Physical",
        "options": [
            {"option_id": 281, "option_text": "Excellent - Very athletic, exercise daily", "trait_tag": "Physical-Skill"},
            {"option_id": 282, "option_text": "Very Good - Regular exercise, physically active", "trait_tag": "Law-Enforce"},
            {"option_id": 283, "option_text": "Good - Moderately fit, occasional exercise", "trait_tag": "Maritime-Sea"},
            {"option_id": 284, "option_text": "Average - Basic fitness, not very active", "trait_tag": "Hospitality-Svc"},
            {"option_id": 285, "option_text": "Below Average - Prefer mental activities", "trait_tag": "Software-Dev"},
            {"option_id": 286, "option_text": "Physical fitness not a priority", "trait_tag": "Finance-Acct"},
            {"option_id": 287, "option_text": "I prefer standing/walking jobs", "trait_tag": "Patient-Care"},
            {"option_id": 288, "option_text": "I prefer desk/sitting jobs", "trait_tag": "Data-Analytics"},
            {"option_id": 289, "option_text": "I prefer outdoor/field jobs", "trait_tag": "Agri-Nature"},
            {"option_id": 290, "option_text": "I prefer hands-on/manual jobs", "trait_tag": "Technical-Skill"}
        ]
    },
    {
        "question_id": 30,
        "question_text": "Rate your CREATIVITY level:",
        "category": "Scale - Creativity",
        "options": [
            {"option_id": 291, "option_text": "Very High - I create art/designs constantly", "trait_tag": "Visual-Design"},
            {"option_id": 292, "option_text": "High - I'm quite creative and imaginative", "trait_tag": "Digital-Media"},
            {"option_id": 293, "option_text": "High - Creative in solving problems", "trait_tag": "Software-Dev"},
            {"option_id": 294, "option_text": "Moderate - Creative when inspired", "trait_tag": "Marketing-Sales"},
            {"option_id": 295, "option_text": "Moderate - More practical than creative", "trait_tag": "Civil-Build"},
            {"option_id": 296, "option_text": "Low - Prefer following procedures", "trait_tag": "Finance-Acct"},
            {"option_id": 297, "option_text": "Low - More analytical than creative", "trait_tag": "Data-Analytics"},
            {"option_id": 298, "option_text": "Creative in teaching methods", "trait_tag": "Teaching-Ed"},
            {"option_id": 299, "option_text": "Creative in spatial/3D design", "trait_tag": "Spatial-Design"},
            {"option_id": 300, "option_text": "Creative in writing/storytelling", "trait_tag": "Creative-Skill"}
        ]
    },

    # ==================== ACADEMIC BACKGROUND QUESTIONS ====================
    {
        "question_id": 31,
        "question_text": "Which subject do you enjoy MOST in school?",
        "category": "Academic - Favorite",
        "options": [
            {"option_id": 301, "option_text": "Science", "trait_tag": "Lab-Research"},
            {"option_id": 302, "option_text": "Mathematics", "trait_tag": "Data-Analytics"},
            {"option_id": 303, "option_text": "English", "trait_tag": "Teaching-Ed"},
            {"option_id": 304, "option_text": "Filipino", "trait_tag": "Teaching-Ed"},
            {"option_id": 305, "option_text": "Social Studies", "trait_tag": "Community-Serve"},
            {"option_id": 306, "option_text": "Computer/TLE", "trait_tag": "Software-Dev"},
            {"option_id": 307, "option_text": "Arts", "trait_tag": "Visual-Design"},
            {"option_id": 308, "option_text": "PE", "trait_tag": "Physical-Skill"},
            {"option_id": 309, "option_text": "Accounting/Business subjects", "trait_tag": "Finance-Acct"},
            {"option_id": 310, "option_text": "Research/Practical Research", "trait_tag": "Lab-Research"}
        ]
    },
    {
        "question_id": 32,
        "question_text": "Which subject do you find MOST CHALLENGING?",
        "category": "Academic - Challenge",
        "options": [
            {"option_id": 311, "option_text": "Mathematics - too many formulas", "trait_tag": "Visual-Design"},
            {"option_id": 312, "option_text": "Science - too much memorization", "trait_tag": "People-Skill"},
            {"option_id": 313, "option_text": "English - grammar is confusing", "trait_tag": "Technical-Skill"},
            {"option_id": 314, "option_text": "Filipino - I prefer English", "trait_tag": "Software-Dev"},
            {"option_id": 315, "option_text": "Social Studies - too many dates/facts", "trait_tag": "Data-Analytics"},
            {"option_id": 316, "option_text": "PE - physical activities tire me", "trait_tag": "Lab-Research"},
            {"option_id": 317, "option_text": "Arts - I'm not creative", "trait_tag": "Finance-Acct"},
            {"option_id": 318, "option_text": "Computer - technology confuses me", "trait_tag": "Patient-Care"},
            {"option_id": 319, "option_text": "None - I do well in all subjects", "trait_tag": "Teaching-Ed"},
            {"option_id": 320, "option_text": "All subjects are equally challenging", "trait_tag": "Admin-Skill"}
        ]
    },
    {
        "question_id": 33,
        "question_text": "How do you prefer to study?",
        "category": "Academic - Study Style",
        "options": [
            {"option_id": 321, "option_text": "Memorizing notes and flashcards", "trait_tag": "Medical-Lab"},
            {"option_id": 322, "option_text": "Solving practice problems repeatedly", "trait_tag": "Data-Analytics"},
            {"option_id": 323, "option_text": "Group study and discussions", "trait_tag": "Teaching-Ed"},
            {"option_id": 324, "option_text": "Making visual diagrams and mind maps", "trait_tag": "Visual-Design"},
            {"option_id": 325, "option_text": "Reading and understanding concepts deeply", "trait_tag": "Lab-Research"},
            {"option_id": 326, "option_text": "Hands-on practice and experiments", "trait_tag": "Technical-Skill"},
            {"option_id": 327, "option_text": "Watching videos and tutorials", "trait_tag": "Digital-Media"},
            {"option_id": 328, "option_text": "Teaching others what I learned", "trait_tag": "Teaching-Ed"},
            {"option_id": 329, "option_text": "Making detailed notes and outlines", "trait_tag": "Finance-Acct"},
            {"option_id": 330, "option_text": "Coding/building projects", "trait_tag": "Software-Dev"}
        ]
    },

    # ==================== LIFESTYLE & VALUES QUESTIONS ====================
    {
        "question_id": 34,
        "question_text": "What work-life balance do you prefer?",
        "category": "Lifestyle",
        "options": [
            {"option_id": 331, "option_text": "Willing to work long shifts if the work is meaningful", "trait_tag": "Patient-Care"},
            {"option_id": 332, "option_text": "Willing to be away from home for months", "trait_tag": "Maritime-Sea"},
            {"option_id": 333, "option_text": "Flexible hours, can work from home", "trait_tag": "Software-Dev"},
            {"option_id": 334, "option_text": "Regular 9-5 office hours", "trait_tag": "Finance-Acct"},
            {"option_id": 335, "option_text": "School schedule with holidays off", "trait_tag": "Teaching-Ed"},
            {"option_id": 336, "option_text": "Shift work including nights and weekends", "trait_tag": "Law-Enforce"},
            {"option_id": 337, "option_text": "Freelance - choose my own hours", "trait_tag": "Visual-Design"},
            {"option_id": 338, "option_text": "Outdoor work following seasons", "trait_tag": "Agri-Nature"},
            {"option_id": 339, "option_text": "Hospitality hours including weekends", "trait_tag": "Hospitality-Svc"},
            {"option_id": 340, "option_text": "Project-based with varying schedules", "trait_tag": "Civil-Build"}
        ]
    },
    {
        "question_id": 35,
        "question_text": "What salary priority do you have?",
        "category": "Career Values",
        "options": [
            {"option_id": 341, "option_text": "High salary is most important", "trait_tag": "Finance-Acct"},
            {"option_id": 342, "option_text": "High salary working abroad", "trait_tag": "Maritime-Sea"},
            {"option_id": 343, "option_text": "Stable salary with government benefits", "trait_tag": "Community-Serve"},
            {"option_id": 344, "option_text": "Job satisfaction matters more than salary", "trait_tag": "Teaching-Ed"},
            {"option_id": 345, "option_text": "Growth potential more than starting salary", "trait_tag": "Software-Dev"},
            {"option_id": 346, "option_text": "Entrepreneurship - unlimited potential", "trait_tag": "Startup-Venture"},
            {"option_id": 347, "option_text": "Balanced salary and work-life", "trait_tag": "Admin-Skill"},
            {"option_id": 348, "option_text": "Tips and commissions on top of base pay", "trait_tag": "Hospitality-Svc"},
            {"option_id": 349, "option_text": "Hazard pay for risky work", "trait_tag": "Law-Enforce"},
            {"option_id": 350, "option_text": "Project-based high fees as a freelancer", "trait_tag": "Visual-Design"}
        ]
    },

    # ==================== BOARD EXAM / LICENSURE QUESTIONS ====================
    {
        "question_id": 36,
        "question_text": "Which board exam would you be willing to take?",
        "category": "Professional Licensure",
        "options": [
            {"option_id": 351, "option_text": "Nursing Licensure Exam (NLE)", "trait_tag": "Patient-Care"},
            {"option_id": 352, "option_text": "CPA Board Exam (Accountancy)", "trait_tag": "Finance-Acct"},
            {"option_id": 353, "option_text": "Engineering Board Exam (Civil/ME/EE)", "trait_tag": "Civil-Build"},
            {"option_id": 354, "option_text": "Criminology Board Exam", "trait_tag": "Law-Enforce"},
            {"option_id": 355, "option_text": "Medical Technologist Board Exam", "trait_tag": "Medical-Lab"},
            {"option_id": 356, "option_text": "Licensure Exam for Teachers (LET)", "trait_tag": "Teaching-Ed"},
            {"option_id": 357, "option_text": "Pharmacy Board Exam", "trait_tag": "Medical-Lab"},
            {"option_id": 358, "option_text": "Physical/Occupational Therapy Board", "trait_tag": "Rehab-Therapy"},
            {"option_id": 359, "option_text": "Architecture Board Exam", "trait_tag": "Spatial-Design"},
            {"option_id": 360, "option_text": "I prefer careers without board exams", "trait_tag": "Software-Dev"}
        ]
    },

    # ==================== RIASEC-STYLE QUESTIONS ====================
    {
        "question_id": 37,
        "question_text": "Which activity would you choose on a free Saturday?",
        "category": "Interest Type",
        "options": [
            {"option_id": 361, "option_text": "Fixing or building something", "trait_tag": "Technical-Skill"},
            {"option_id": 362, "option_text": "Reading about science or doing experiments", "trait_tag": "Lab-Research"},
            {"option_id": 363, "option_text": "Creating art, music, or writing", "trait_tag": "Visual-Design"},
            {"option_id": 364, "option_text": "Volunteering to help others", "trait_tag": "Community-Serve"},
            {"option_id": 365, "option_text": "Working on a business idea", "trait_tag": "Startup-Venture"},
            {"option_id": 366, "option_text": "Organizing my room or files", "trait_tag": "Admin-Skill"},
            {"option_id": 367, "option_text": "Coding a personal project", "trait_tag": "Software-Dev"},
            {"option_id": 368, "option_text": "Playing sports or exercising", "trait_tag": "Physical-Skill"},
            {"option_id": 369, "option_text": "Cooking or trying new recipes", "trait_tag": "Hospitality-Svc"},
            {"option_id": 370, "option_text": "Watching true crime or mystery shows", "trait_tag": "Law-Enforce"}
        ]
    },
    {
        "question_id": 38,
        "question_text": "In a zombie apocalypse, what role would you take?",
        "category": "Fun - Role",
        "options": [
            {"option_id": 371, "option_text": "The medic - healing and caring for survivors", "trait_tag": "Patient-Care"},
            {"option_id": 372, "option_text": "The scientist - finding a cure", "trait_tag": "Lab-Research"},
            {"option_id": 373, "option_text": "The engineer - building fortifications", "trait_tag": "Civil-Build"},
            {"option_id": 374, "option_text": "The leader - organizing the group", "trait_tag": "Startup-Venture"},
            {"option_id": 375, "option_text": "The strategist - planning survival", "trait_tag": "Data-Analytics"},
            {"option_id": 376, "option_text": "The fighter - protecting everyone", "trait_tag": "Law-Enforce"},
            {"option_id": 377, "option_text": "The tech expert - communications and hacking", "trait_tag": "Software-Dev"},
            {"option_id": 378, "option_text": "The scout - exploring and gathering intel", "trait_tag": "Field-Research"},
            {"option_id": 379, "option_text": "The farmer - growing food supplies", "trait_tag": "Agri-Nature"},
            {"option_id": 380, "option_text": "The cook - keeping everyone fed and happy", "trait_tag": "Hospitality-Svc"}
        ]
    },
    {
        "question_id": 39,
        "question_text": "Which superpower would be most useful for your ideal career?",
        "category": "Fun - Superpower",
        "options": [
            {"option_id": 381, "option_text": "Healing touch - save patients instantly", "trait_tag": "Patient-Care"},
            {"option_id": 382, "option_text": "Super intelligence - solve any problem", "trait_tag": "Data-Analytics"},
            {"option_id": 383, "option_text": "Mind reading - understand everyone perfectly", "trait_tag": "People-Skill"},
            {"option_id": 384, "option_text": "Super strength - build anything easily", "trait_tag": "Civil-Build"},
            {"option_id": 385, "option_text": "Time manipulation - meet all deadlines", "trait_tag": "Finance-Acct"},
            {"option_id": 386, "option_text": "Truth detection - solve any crime", "trait_tag": "Law-Enforce"},
            {"option_id": 387, "option_text": "Teleportation - travel anywhere instantly", "trait_tag": "Maritime-Sea"},
            {"option_id": 388, "option_text": "Creativity burst - create amazing art", "trait_tag": "Visual-Design"},
            {"option_id": 389, "option_text": "Tech control - command any computer", "trait_tag": "Software-Dev"},
            {"option_id": 390, "option_text": "Plant growth - perfect farming", "trait_tag": "Agri-Nature"}
        ]
    },
    {
        "question_id": 40,
        "question_text": "What would your ideal Monday morning look like?",
        "category": "Work Lifestyle",
        "options": [
            {"option_id": 391, "option_text": "Arriving at the hospital for patient rounds", "trait_tag": "Patient-Care"},
            {"option_id": 392, "option_text": "Setting up experiments in a lab", "trait_tag": "Lab-Research"},
            {"option_id": 393, "option_text": "Opening my laptop to code at a tech company", "trait_tag": "Software-Dev"},
            {"option_id": 394, "option_text": "Reviewing blueprints at a construction site", "trait_tag": "Civil-Build"},
            {"option_id": 395, "option_text": "Preparing financial reports at my desk", "trait_tag": "Finance-Acct"},
            {"option_id": 396, "option_text": "Greeting students at a classroom", "trait_tag": "Teaching-Ed"},
            {"option_id": 397, "option_text": "Starting my shift at the police station", "trait_tag": "Law-Enforce"},
            {"option_id": 398, "option_text": "Working on designs at my creative studio", "trait_tag": "Visual-Design"},
            {"option_id": 399, "option_text": "Checking systems aboard a ship at sea", "trait_tag": "Maritime-Sea"},
            {"option_id": 400, "option_text": "Walking through my farm checking crops", "trait_tag": "Agri-Nature"}
        ]
    },

    # ==================== SECTION 2: EXPANDED CAREER SCENARIOS ====================
    {
        "question_id": 41,
        "question_text": "SCENARIO: Your barangay needs help. Which role would you volunteer for?",
        "category": "Community Scenario",
        "options": [
            {"option_id": 401, "option_text": "Medical mission - taking blood pressure, first aid", "trait_tag": "Patient-Care"},
            {"option_id": 402, "option_text": "Free tutoring for students", "trait_tag": "Teaching-Ed"},
            {"option_id": 403, "option_text": "Setting up computer systems for the barangay hall", "trait_tag": "Software-Dev"},
            {"option_id": 404, "option_text": "Organizing feeding programs and events", "trait_tag": "Hospitality-Svc"},
            {"option_id": 405, "option_text": "Helping with infrastructure repairs", "trait_tag": "Civil-Build"},
            {"option_id": 406, "option_text": "Assisting in crime prevention programs", "trait_tag": "Law-Enforce"},
            {"option_id": 407, "option_text": "Creating posters and promotional materials", "trait_tag": "Visual-Design"},
            {"option_id": 408, "option_text": "Managing donations and financial records", "trait_tag": "Finance-Acct"},
            {"option_id": 409, "option_text": "Environmental cleanup and tree planting", "trait_tag": "Agri-Nature"},
            {"option_id": 410, "option_text": "Counseling families in need", "trait_tag": "Community-Serve"}
        ]
    },
    {
        "question_id": 42,
        "question_text": "SCENARIO: You're stranded on an island with your classmates. What's your role?",
        "category": "Survival Scenario",
        "options": [
            {"option_id": 411, "option_text": "The medic - treating injuries and illnesses", "trait_tag": "Patient-Care"},
            {"option_id": 412, "option_text": "The engineer - building shelter and tools", "trait_tag": "Civil-Build"},
            {"option_id": 413, "option_text": "The leader - organizing the group and making decisions", "trait_tag": "Startup-Venture"},
            {"option_id": 414, "option_text": "The hunter/gatherer - finding food", "trait_tag": "Agri-Nature"},
            {"option_id": 415, "option_text": "The navigator - figuring out how to get rescued", "trait_tag": "Maritime-Sea"},
            {"option_id": 416, "option_text": "The peacekeeper - resolving conflicts", "trait_tag": "Community-Serve"},
            {"option_id": 417, "option_text": "The strategist - planning long-term survival", "trait_tag": "Data-Analytics"},
            {"option_id": 418, "option_text": "The teacher - training others in survival skills", "trait_tag": "Teaching-Ed"},
            {"option_id": 419, "option_text": "The communicator - boosting morale and keeping spirits up", "trait_tag": "People-Skill"},
            {"option_id": 420, "option_text": "The inventor - creating solutions from limited resources", "trait_tag": "Technical-Skill"}
        ]
    },
    {
        "question_id": 43,
        "question_text": "SCENARIO: A typhoon hit your town. How would you help?",
        "category": "Disaster Response",
        "options": [
            {"option_id": 421, "option_text": "Medical response - treating injured victims", "trait_tag": "Patient-Care"},
            {"option_id": 422, "option_text": "Search and rescue operations", "trait_tag": "Law-Enforce"},
            {"option_id": 423, "option_text": "Distributing relief goods fairly", "trait_tag": "Admin-Skill"},
            {"option_id": 424, "option_text": "Repairing damaged electrical lines", "trait_tag": "Electrical-Power"},
            {"option_id": 425, "option_text": "Clearing roads and debris", "trait_tag": "Civil-Build"},
            {"option_id": 426, "option_text": "Setting up communication systems", "trait_tag": "Hardware-Systems"},
            {"option_id": 427, "option_text": "Cooking and preparing food for evacuees", "trait_tag": "Hospitality-Svc"},
            {"option_id": 428, "option_text": "Counseling traumatized victims", "trait_tag": "People-Skill"},
            {"option_id": 429, "option_text": "Documenting damage for insurance/aid", "trait_tag": "Finance-Acct"},
            {"option_id": 430, "option_text": "Coordinating volunteer efforts", "trait_tag": "Community-Serve"}
        ]
    },
    {
        "question_id": 44,
        "question_text": "SCENARIO: Your school is planning a foundation day. What committee would you join?",
        "category": "Event Planning",
        "options": [
            {"option_id": 431, "option_text": "First aid and medical committee", "trait_tag": "Patient-Care"},
            {"option_id": 432, "option_text": "Stage design and decorations", "trait_tag": "Visual-Design"},
            {"option_id": 433, "option_text": "Sound and lights technical team", "trait_tag": "Hardware-Systems"},
            {"option_id": 434, "option_text": "Budget and finance committee", "trait_tag": "Finance-Acct"},
            {"option_id": 435, "option_text": "Food and catering committee", "trait_tag": "Hospitality-Svc"},
            {"option_id": 436, "option_text": "Security and crowd control", "trait_tag": "Law-Enforce"},
            {"option_id": 437, "option_text": "Program and hosting", "trait_tag": "Creative-Skill"},
            {"option_id": 438, "option_text": "Documentation and photography", "trait_tag": "Digital-Media"},
            {"option_id": 439, "option_text": "Logistics and venue setup", "trait_tag": "Industrial-Ops"},
            {"option_id": 440, "option_text": "Registration and guest relations", "trait_tag": "Admin-Skill"}
        ]
    },
    {
        "question_id": 45,
        "question_text": "SCENARIO: Your friend is crying about a failed exam. What do you do?",
        "category": "Emotional Intelligence",
        "options": [
            {"option_id": 441, "option_text": "Listen and comfort them emotionally", "trait_tag": "People-Skill"},
            {"option_id": 442, "option_text": "Offer to tutor them for the next exam", "trait_tag": "Teaching-Ed"},
            {"option_id": 443, "option_text": "Help them analyze what went wrong", "trait_tag": "Data-Analytics"},
            {"option_id": 444, "option_text": "Buy them food to cheer them up", "trait_tag": "Hospitality-Svc"},
            {"option_id": 445, "option_text": "Create a study schedule/plan for them", "trait_tag": "Admin-Skill"},
            {"option_id": 446, "option_text": "Distract them with fun activities", "trait_tag": "Creative-Skill"},
            {"option_id": 447, "option_text": "Share your own failure stories to relate", "trait_tag": "Community-Serve"},
            {"option_id": 448, "option_text": "Encourage them to talk to the teacher", "trait_tag": "Law-Enforce"},
            {"option_id": 449, "option_text": "Help them find online resources", "trait_tag": "Software-Dev"},
            {"option_id": 450, "option_text": "Give practical tips for better memorization", "trait_tag": "Medical-Lab"}
        ]
    },


        # ==================== SECTION 4: PHILIPPINE-SPECIFIC QUESTIONS ====================
    {
        "question_id": 51,
        "question_text": "Which Philippine industry would you like to work in?",
        "category": "PH Industry",
        "options": [
            {"option_id": 501, "option_text": "BPO/Call center industry", "trait_tag": "People-Skill"},
            {"option_id": 502, "option_text": "OFW - work abroad (healthcare)", "trait_tag": "Patient-Care"},
            {"option_id": 503, "option_text": "OFW - work abroad (maritime/seaman)", "trait_tag": "Maritime-Sea"},
            {"option_id": 504, "option_text": "OFW - work abroad (engineering)", "trait_tag": "Civil-Build"},
            {"option_id": 505, "option_text": "Government service (LGU, national agencies)", "trait_tag": "Community-Serve"},
            {"option_id": 506, "option_text": "Banking and finance sector", "trait_tag": "Finance-Acct"},
            {"option_id": 507, "option_text": "Tech startup/IT industry", "trait_tag": "Software-Dev"},
            {"option_id": 508, "option_text": "Tourism and hospitality", "trait_tag": "Hospitality-Svc"},
            {"option_id": 509, "option_text": "Manufacturing/factory industry", "trait_tag": "Industrial-Ops"},
            {"option_id": 510, "option_text": "Agriculture and farming", "trait_tag": "Agri-Nature"}
        ]
    },
    {
        "question_id": 52,
        "question_text": "Which board exam would you be most willing to study hard for?",
        "category": "Board Exam Preference",
        "options": [
            {"option_id": 511, "option_text": "Nursing Licensure Exam (NLE)", "trait_tag": "Patient-Care"},
            {"option_id": 512, "option_text": "CPA Board Exam", "trait_tag": "Finance-Acct"},
            {"option_id": 513, "option_text": "Civil Engineering Board Exam", "trait_tag": "Civil-Build"},
            {"option_id": 514, "option_text": "Electrical Engineering Board Exam", "trait_tag": "Electrical-Power"},
            {"option_id": 515, "option_text": "Mechanical Engineering Board Exam", "trait_tag": "Mechanical-Design"},
            {"option_id": 516, "option_text": "Criminology Board Exam", "trait_tag": "Law-Enforce"},
            {"option_id": 517, "option_text": "Licensure Exam for Teachers (LET)", "trait_tag": "Teaching-Ed"},
            {"option_id": 518, "option_text": "Medical Technologist Board Exam", "trait_tag": "Medical-Lab"},
            {"option_id": 519, "option_text": "Pharmacy Board Exam", "trait_tag": "Medical-Lab"},
            {"option_id": 520, "option_text": "I prefer careers without board exams", "trait_tag": "Software-Dev"}
        ]
    },
    {
        "question_id": 53,
        "question_text": "Where in the Philippines would you prefer to work?",
        "category": "Work Location",
        "options": [
            {"option_id": 521, "option_text": "Metro Manila - BGC, Makati, Ortigas", "trait_tag": "Finance-Acct"},
            {"option_id": 522, "option_text": "Clark/Subic - growing industrial zone", "trait_tag": "Industrial-Ops"},
            {"option_id": 523, "option_text": "Cebu - IT and BPO hub", "trait_tag": "Software-Dev"},
            {"option_id": 524, "option_text": "Davao - agribusiness center", "trait_tag": "Agri-Nature"},
            {"option_id": 525, "option_text": "Baguio - education and tourism", "trait_tag": "Teaching-Ed"},
            {"option_id": 526, "option_text": "Boracay/Palawan - tourism hotspots", "trait_tag": "Hospitality-Svc"},
            {"option_id": 527, "option_text": "My home province", "trait_tag": "Community-Serve"},
            {"option_id": 528, "option_text": "Anywhere with good hospitals", "trait_tag": "Patient-Care"},
            {"option_id": 529, "option_text": "Near ports - Batangas, Subic", "trait_tag": "Maritime-Sea"},
            {"option_id": 530, "option_text": "Abroad - international career", "trait_tag": "Marketing-Sales"}
        ]
    },
    {
        "question_id": 54,
        "question_text": "Which Filipino company/organization would you want to work for?",
        "category": "Dream Employer",
        "options": [
            {"option_id": 531, "option_text": "SM, Ayala, or San Miguel Corporation", "trait_tag": "Finance-Acct"},
            {"option_id": 532, "option_text": "PLDT, Globe, or Smart", "trait_tag": "Hardware-Systems"},
            {"option_id": 533, "option_text": "Jollibee, Max's, or Goldilocks", "trait_tag": "Hospitality-Svc"},
            {"option_id": 534, "option_text": "St. Luke's, Makati Med, or Philippine Heart Center", "trait_tag": "Patient-Care"},
            {"option_id": 535, "option_text": "DMCI, Megawide, or Ayala Land", "trait_tag": "Civil-Build"},
            {"option_id": 536, "option_text": "Accenture, IBM Philippines, or tech startups", "trait_tag": "Software-Dev"},
            {"option_id": 537, "option_text": "PNP, AFP, or NBI", "trait_tag": "Law-Enforce"},
            {"option_id": 538, "option_text": "DepEd, CHED, or universities", "trait_tag": "Teaching-Ed"},
            {"option_id": 539, "option_text": "DOH, PhilHealth, or health agencies", "trait_tag": "Community-Serve"},
            {"option_id": 540, "option_text": "Start my own business", "trait_tag": "Startup-Venture"}
        ]
    },

    # ==================== SECTION 5: SKILLS SELF-ASSESSMENT ====================
    {
        "question_id": 55,
        "question_text": "Rate your ENGLISH proficiency:",
        "category": "Language Skill",
        "options": [
            {"option_id": 541, "option_text": "Excellent - can debate, write essays fluently", "trait_tag": "Teaching-Ed"},
            {"option_id": 542, "option_text": "Very Good - comfortable in English conversations", "trait_tag": "Marketing-Sales"},
            {"option_id": 543, "option_text": "Good - can communicate clearly", "trait_tag": "People-Skill"},
            {"option_id": 544, "option_text": "Average - understand but struggle speaking", "trait_tag": "Technical-Skill"},
            {"option_id": 545, "option_text": "Below Average - prefer Filipino", "trait_tag": "Agri-Nature"},
            {"option_id": 546, "option_text": "I'm better at technical English (IT/Science)", "trait_tag": "Software-Dev"},
            {"option_id": 547, "option_text": "I'm better at medical/scientific terms", "trait_tag": "Medical-Lab"},
            {"option_id": 548, "option_text": "I'm better at business English", "trait_tag": "Finance-Acct"},
            {"option_id": 549, "option_text": "I'm better at legal/formal English", "trait_tag": "Law-Enforce"},
            {"option_id": 550, "option_text": "I'm better at creative writing", "trait_tag": "Visual-Design"}
        ]
    },
    {
        "question_id": 56,
        "question_text": "What technology activity are you most comfortable with?",
        "category": "Tech Skill",
        "options": [
            {"option_id": 551, "option_text": "Coding or building programs and websites", "trait_tags": ["Software-Dev", "Web-Dev"]},
            {"option_id": 552, "option_text": "Gaming - I know my way around PC specs, mods, and setups", "trait_tags": ["Game-Dev", "Hardware-Systems"]},
            {"option_id": 553, "option_text": "Working with spreadsheets and organizing data", "trait_tags": ["Data-Analytics", "Finance-Acct"]},
            {"option_id": 554, "option_text": "Editing photos, videos, or creating digital content", "trait_tags": ["Digital-Media", "Visual-Design"]},
            {"option_id": 555, "option_text": "Troubleshooting hardware or setting up networks", "trait_tags": ["Hardware-Systems", "Cloud-Systems"]},
            {"option_id": 556, "option_text": "Browsing social media and online communication", "trait_tags": ["Marketing-Sales", "People-Skill"]},
            {"option_id": 557, "option_text": "Using apps for design - Canva, Photoshop, Figma", "trait_tags": ["Visual-Design", "Animation-3D"]},
            {"option_id": 558, "option_text": "Exploring AI tools, chatbots, or automation", "trait_tags": ["AI-ML", "Software-Dev"]},
            {"option_id": 559, "option_text": "Managing files, records, or hospital/office systems", "trait_tags": ["Admin-Skill", "Health-Admin"]},
            {"option_id": 560, "option_text": "I mostly use my phone/computer for basic tasks only", "trait_tags": ["Agri-Nature", "Physical-Skill"]}
        ]
    },
    {
        "question_id": 57,
        "question_text": "Rate your LEADERSHIP ability:",
        "category": "Leadership Skill",
        "options": [
            {"option_id": 561, "option_text": "Natural leader - always take charge", "trait_tag": "Startup-Venture"},
            {"option_id": 562, "option_text": "Good leader when needed", "trait_tag": "Admin-Skill"},
            {"option_id": 563, "option_text": "Prefer to support the leader", "trait_tag": "People-Skill"},
            {"option_id": 564, "option_text": "Work best independently", "trait_tag": "Lab-Research"},
            {"option_id": 565, "option_text": "Lead through teaching/mentoring", "trait_tag": "Teaching-Ed"},
            {"option_id": 566, "option_text": "Lead through expertise/knowledge", "trait_tag": "Medical-Lab"},
            {"option_id": 567, "option_text": "Lead through organization/planning", "trait_tag": "Finance-Acct"},
            {"option_id": 568, "option_text": "Lead through inspiration/creativity", "trait_tag": "Visual-Design"},
            {"option_id": 569, "option_text": "Lead through authority/discipline", "trait_tag": "Law-Enforce"},
            {"option_id": 570, "option_text": "Lead through service/example", "trait_tag": "Community-Serve"}
        ]
    },
    {
        "question_id": 58,
        "question_text": "How do you handle PRESSURE and DEADLINES?",
        "category": "Stress Management",
        "options": [
            {"option_id": 571, "option_text": "Thrive under pressure - work better with urgency", "trait_tag": "Patient-Care"},
            {"option_id": 572, "option_text": "Handle it well - stay calm and focused", "trait_tag": "Law-Enforce"},
            {"option_id": 573, "option_text": "Manageable - can deal with reasonable deadlines", "trait_tag": "Software-Dev"},
            {"option_id": 574, "option_text": "Prefer steady pace - avoid high-pressure situations", "trait_tag": "Teaching-Ed"},
            {"option_id": 575, "option_text": "Struggle with pressure - need calm environments", "trait_tag": "Lab-Research"},
            {"option_id": 576, "option_text": "Good with financial deadlines", "trait_tag": "Finance-Acct"},
            {"option_id": 577, "option_text": "Good with project deadlines", "trait_tag": "Civil-Build"},
            {"option_id": 578, "option_text": "Good with creative deadlines", "trait_tag": "Visual-Design"},
            {"option_id": 579, "option_text": "Good with people-related pressure", "trait_tag": "Hospitality-Svc"},
            {"option_id": 580, "option_text": "Work best with flexible timelines", "trait_tag": "Agri-Nature"}
        ]
    },
    {
        "question_id": 59,
        "question_text": "How would you rate your MATHEMATICAL ability?",
        "category": "Math Skill",
        "options": [
            {"option_id": 581, "option_text": "Excellent - love calculus, physics, advanced math", "trait_tag": "Data-Analytics"},
            {"option_id": 582, "option_text": "Very Good - comfortable with algebra, statistics", "trait_tag": "Civil-Build"},
            {"option_id": 583, "option_text": "Good - can handle accounting math", "trait_tag": "Finance-Acct"},
            {"option_id": 584, "option_text": "Average - basic math is fine", "trait_tag": "Teaching-Ed"},
            {"option_id": 585, "option_text": "Below Average - struggle with math", "trait_tag": "Visual-Design"},
            {"option_id": 586, "option_text": "Good at programming math/logic", "trait_tag": "Software-Dev"},
            {"option_id": 587, "option_text": "Good at medical calculations (dosages)", "trait_tag": "Patient-Care"},
            {"option_id": 588, "option_text": "Good at engineering calculations", "trait_tag": "Mechanical-Design"},
            {"option_id": 589, "option_text": "Good at measurement/spatial math", "trait_tag": "Spatial-Design"},
            {"option_id": 590, "option_text": "Math isn't my strength", "trait_tag": "Creative-Skill"}
        ]
    },
    {
        "question_id": 60,
        "question_text": "How would you rate your SCIENCE ability?",
        "category": "Science Skill",
        "options": [
            {"option_id": 591, "option_text": "Excellent - love biology, chemistry, physics", "trait_tag": "Lab-Research"},
            {"option_id": 592, "option_text": "Very Good - enjoy science experiments", "trait_tag": "Medical-Lab"},
            {"option_id": 593, "option_text": "Good at biology/life sciences", "trait_tag": "Patient-Care"},
            {"option_id": 594, "option_text": "Good at chemistry", "trait_tag": "Medical-Lab"},
            {"option_id": 595, "option_text": "Good at physics/engineering science", "trait_tag": "Electrical-Power"},
            {"option_id": 596, "option_text": "Good at earth/environmental science", "trait_tag": "Agri-Nature"},
            {"option_id": 597, "option_text": "Good at computer science", "trait_tag": "Software-Dev"},
            {"option_id": 598, "option_text": "Average - science is okay", "trait_tag": "Teaching-Ed"},
            {"option_id": 599, "option_text": "Below Average - not my favorite", "trait_tag": "Finance-Acct"},
            {"option_id": 600, "option_text": "Science isn't my strength", "trait_tag": "Visual-Design"}
        ]
    },

    # ==================== SECTION 6: VALUES AND PRIORITIES ====================
    {
        "question_id": 61,
        "question_text": "What's MOST important to you in a career?",
        "category": "Career Priority",
        "options": [
            {"option_id": 601, "option_text": "High salary and financial security", "trait_tag": "Finance-Acct"},
            {"option_id": 602, "option_text": "Helping others and making a difference", "trait_tag": "Patient-Care"},
            {"option_id": 603, "option_text": "Job security and stability", "trait_tag": "Teaching-Ed"},
            {"option_id": 604, "option_text": "Creativity and self-expression", "trait_tag": "Visual-Design"},
            {"option_id": 605, "option_text": "Work-life balance", "trait_tag": "Admin-Skill"},
            {"option_id": 606, "option_text": "Prestige and respect", "trait_tag": "Law-Enforce"},
            {"option_id": 607, "option_text": "Adventure and travel", "trait_tag": "Maritime-Sea"},
            {"option_id": 608, "option_text": "Independence and being my own boss", "trait_tag": "Startup-Venture"},
            {"option_id": 609, "option_text": "Intellectual challenge", "trait_tag": "Software-Dev"},
            {"option_id": 610, "option_text": "Contributing to community/nation", "trait_tag": "Community-Serve"}
        ]
    },
    {
        "question_id": 62,
        "question_text": "How important is SALARY to you?",
        "category": "Salary Importance",
        "options": [
            {"option_id": 611, "option_text": "Very important - want high-paying career", "trait_tag": "Finance-Acct"},
            {"option_id": 612, "option_text": "Important - need good income for family", "trait_tag": "Maritime-Sea"},
            {"option_id": 613, "option_text": "Moderate - balance of pay and passion", "trait_tag": "Software-Dev"},
            {"option_id": 614, "option_text": "Less important - passion over pay", "trait_tag": "Teaching-Ed"},
            {"option_id": 615, "option_text": "Want to earn abroad (OFW)", "trait_tag": "Patient-Care"},
            {"option_id": 616, "option_text": "Want steady government salary", "trait_tag": "Community-Serve"},
            {"option_id": 617, "option_text": "Want entrepreneurial income", "trait_tag": "Startup-Venture"},
            {"option_id": 618, "option_text": "Want project-based freelance income", "trait_tag": "Visual-Design"},
            {"option_id": 619, "option_text": "Want commission-based income", "trait_tag": "Marketing-Sales"},
            {"option_id": 620, "option_text": "Money isn't my main motivation", "trait_tag": "Agri-Nature"}
        ]
    },
    {
        "question_id": 63,
        "question_text": "How do you feel about WORKING ABROAD?",
        "category": "International Work",
        "options": [
            {"option_id": 621, "option_text": "Dream of it - want to be an OFW", "trait_tag": "Maritime-Sea"},
            {"option_id": 622, "option_text": "Open to it for nursing/healthcare", "trait_tag": "Patient-Care"},
            {"option_id": 623, "option_text": "Open to it for engineering/construction", "trait_tag": "Civil-Build"},
            {"option_id": 624, "option_text": "Open to it for IT/tech work", "trait_tag": "Software-Dev"},
            {"option_id": 625, "option_text": "Open to it for hospitality/cruise ships", "trait_tag": "Hospitality-Svc"},
            {"option_id": 626, "option_text": "Prefer to stay in Philippines", "trait_tag": "Community-Serve"},
            {"option_id": 627, "option_text": "Want to work locally for family", "trait_tag": "Teaching-Ed"},
            {"option_id": 628, "option_text": "Want to build business here", "trait_tag": "Startup-Venture"},
            {"option_id": 629, "option_text": "Want government career here", "trait_tag": "Law-Enforce"},
            {"option_id": 630, "option_text": "Undecided about working abroad", "trait_tag": "Admin-Skill"}
        ]
    },
    {
        "question_id": 64,
        "question_text": "What type of WORK SCHEDULE do you prefer?",
        "category": "Work Schedule",
        "options": [
            {"option_id": 631, "option_text": "Regular 9-5 office hours", "trait_tag": "Finance-Acct"},
            {"option_id": 632, "option_text": "Flexible hours / work from home", "trait_tag": "Software-Dev"},
            {"option_id": 633, "option_text": "Shift work (morning/afternoon/night)", "trait_tag": "Patient-Care"},
            {"option_id": 634, "option_text": "School schedule (with summers off)", "trait_tag": "Teaching-Ed"},
            {"option_id": 635, "option_text": "On-call / emergency response", "trait_tag": "Law-Enforce"},
            {"option_id": 636, "option_text": "Contract-based / project work", "trait_tag": "Maritime-Sea"},
            {"option_id": 637, "option_text": "Seasonal work (planting/harvest)", "trait_tag": "Agri-Nature"},
            {"option_id": 638, "option_text": "Self-determined (entrepreneur)", "trait_tag": "Startup-Venture"},
            {"option_id": 639, "option_text": "Creative hours (deadlines-based)", "trait_tag": "Visual-Design"},
            {"option_id": 640, "option_text": "Hospitality hours (weekends/holidays)", "trait_tag": "Hospitality-Svc"}
        ]
    },

    # ==================== SECTION 7: PERSONALITY & INTERESTS ====================
    {
        "question_id": 65,
        "question_text": "How would your friends describe you?",
        "category": "Personality",
        "options": [
            {"option_id": 641, "option_text": "Caring and nurturing - always helping others", "trait_tag": "Patient-Care"},
            {"option_id": 642, "option_text": "Smart and analytical - the problem solver", "trait_tag": "Data-Analytics"},
            {"option_id": 643, "option_text": "Creative and artistic - the imaginative one", "trait_tag": "Visual-Design"},
            {"option_id": 644, "option_text": "Outgoing and persuasive - the social butterfly", "trait_tag": "Marketing-Sales"},
            {"option_id": 645, "option_text": "Organized and reliable - the planner", "trait_tag": "Finance-Acct"},
            {"option_id": 646, "option_text": "Patient and understanding - the teacher type", "trait_tag": "Teaching-Ed"},
            {"option_id": 647, "option_text": "Brave and protective - the defender", "trait_tag": "Law-Enforce"},
            {"option_id": 648, "option_text": "Adventurous and daring - the explorer", "trait_tag": "Maritime-Sea"},
            {"option_id": 649, "option_text": "Practical and hands-on - the builder", "trait_tag": "Civil-Build"},
            {"option_id": 650, "option_text": "Ambitious and driven - the entrepreneur", "trait_tag": "Startup-Venture"}
        ]
    },
    {
        "question_id": 66,
        "question_text": "What do you do in your FREE TIME?",
        "category": "Hobbies",
        "options": [
            {"option_id": 651, "option_text": "Draw, paint, or do arts and crafts", "trait_tag": "Visual-Design"},
            {"option_id": 652, "option_text": "Play video games or use computers", "trait_tag": "Software-Dev"},
            {"option_id": 653, "option_text": "Read books or watch documentaries", "trait_tag": "Lab-Research"},
            {"option_id": 654, "option_text": "Play sports or exercise", "trait_tag": "Physical-Skill"},
            {"option_id": 655, "option_text": "Volunteer or help in community", "trait_tag": "Community-Serve"},
            {"option_id": 656, "option_text": "Cook or try new recipes", "trait_tag": "Hospitality-Svc"},
            {"option_id": 657, "option_text": "Build or fix things", "trait_tag": "Technical-Skill"},
            {"option_id": 658, "option_text": "Care for plants or pets", "trait_tag": "Agri-Nature"},
            {"option_id": 659, "option_text": "Watch crime/mystery shows", "trait_tag": "Law-Enforce"},
            {"option_id": 660, "option_text": "Plan and organize events", "trait_tag": "Admin-Skill"}
        ]
    },
    {
        "question_id": 67,
        "question_text": "What type of TV show/movie do you enjoy most?",
        "category": "Entertainment Preference",
        "options": [
            {"option_id": 661, "option_text": "Medical dramas (Grey's Anatomy, House)", "trait_tag": "Patient-Care"},
            {"option_id": 662, "option_text": "Crime/detective shows (CSI, NCIS)", "trait_tag": "Law-Enforce"},
            {"option_id": 663, "option_text": "Tech/sci-fi (Black Mirror, Silicon Valley)", "trait_tag": "Software-Dev"},
            {"option_id": 664, "option_text": "Business/finance (Suits, Wolf of Wall Street)", "trait_tag": "Finance-Acct"},
            {"option_id": 665, "option_text": "Cooking shows (MasterChef, Kitchen Nightmares)", "trait_tag": "Hospitality-Svc"},
            {"option_id": 666, "option_text": "Design/makeover shows (home/fashion)", "trait_tag": "Spatial-Design"},
            {"option_id": 667, "option_text": "Nature/animal documentaries", "trait_tag": "Agri-Nature"},
            {"option_id": 668, "option_text": "Teacher/school stories", "trait_tag": "Teaching-Ed"},
            {"option_id": 669, "option_text": "Engineering/building shows (Grand Designs)", "trait_tag": "Civil-Build"},
            {"option_id": 670, "option_text": "Social issues/community stories", "trait_tag": "Community-Serve"}
        ]
    },
    {
        "question_id": 68,
        "question_text": "If you could meet any professional, who would it be?",
        "category": "Role Model",
        "options": [
            {"option_id": 671, "option_text": "A famous doctor or surgeon", "trait_tag": "Patient-Care"},
            {"option_id": 672, "option_text": "A tech CEO (Elon Musk, Mark Zuckerberg)", "trait_tag": "Software-Dev"},
            {"option_id": 673, "option_text": "A business tycoon (Henry Sy, Manny Pangilinan)", "trait_tag": "Finance-Acct"},
            {"option_id": 674, "option_text": "A famous artist or designer", "trait_tag": "Visual-Design"},
            {"option_id": 675, "option_text": "A renowned teacher or educator", "trait_tag": "Teaching-Ed"},
            {"option_id": 676, "option_text": "A successful chef (Gordon Ramsay)", "trait_tag": "Hospitality-Svc"},
            {"option_id": 677, "option_text": "A famous architect or engineer", "trait_tag": "Civil-Build"},
            {"option_id": 678, "option_text": "A high-ranking police/military officer", "trait_tag": "Law-Enforce"},
            {"option_id": 679, "option_text": "A scientist or researcher", "trait_tag": "Lab-Research"},
            {"option_id": 680, "option_text": "A social worker or humanitarian", "trait_tag": "Community-Serve"}
        ]
    },

    # ==================== SECTION 8: ACADEMIC & SCHOOL-RELATED ====================
    {
        "question_id": 69,
        "question_text": "Which school club/organization would you join?",
        "category": "School Involvement",
        "options": [
            {"option_id": 681, "option_text": "Red Cross Youth / First Aid Club", "trait_tag": "Patient-Care"},
            {"option_id": 682, "option_text": "Computer Club / Robotics Club", "trait_tag": "Software-Dev"},
            {"option_id": 683, "option_text": "Math Club / Science Club", "trait_tag": "Data-Analytics"},
            {"option_id": 684, "option_text": "Business Club / Junior Achievement", "trait_tag": "Startup-Venture"},
            {"option_id": 685, "option_text": "Art Club / Photography Club", "trait_tag": "Visual-Design"},
            {"option_id": 686, "option_text": "Drama Club / Glee Club", "trait_tag": "Creative-Skill"},
            {"option_id": 687, "option_text": "Student Council / Leadership", "trait_tag": "Admin-Skill"},
            {"option_id": 688, "option_text": "Environmental Club", "trait_tag": "Agri-Nature"},
            {"option_id": 689, "option_text": "CAT / Citizenship Advancement Training", "trait_tag": "Law-Enforce"},
            {"option_id": 690, "option_text": "Peer Tutoring / Academic Mentoring", "trait_tag": "Teaching-Ed"}
        ]
    },
    {
        "question_id": 70,
        "question_text": "Which school project do you enjoy most?",
        "category": "Project Preference",
        "options": [
            {"option_id": 691, "option_text": "Science investigatory project", "trait_tag": "Lab-Research"},
            {"option_id": 692, "option_text": "Programming/website project", "trait_tag": "Software-Dev"},
            {"option_id": 693, "option_text": "Business plan/feasibility study", "trait_tag": "Finance-Acct"},
            {"option_id": 694, "option_text": "Art project (painting, sculpture)", "trait_tag": "Visual-Design"},
            {"option_id": 695, "option_text": "Community service/outreach", "trait_tag": "Community-Serve"},
            {"option_id": 696, "option_text": "Video documentary/film project", "trait_tag": "Digital-Media"},
            {"option_id": 697, "option_text": "Research paper/case study", "trait_tag": "Teaching-Ed"},
            {"option_id": 698, "option_text": "Engineering/robotics project", "trait_tag": "Hardware-Systems"},
            {"option_id": 699, "option_text": "Health/nutrition project", "trait_tag": "Patient-Care"},
            {"option_id": 700, "option_text": "Mock trial/debate", "trait_tag": "Law-Enforce"}
        ]
    },
    {
        "question_id": 71,
        "question_text": "What's your FAVORITE subject in school?",
        "category": "Favorite Subject",
        "options": [
            {"option_id": 701, "option_text": "Math", "trait_tag": "Data-Analytics"},
            {"option_id": 702, "option_text": "Science", "trait_tag": "Lab-Research"},
            {"option_id": 703, "option_text": "English", "trait_tag": "Teaching-Ed"},
            {"option_id": 704, "option_text": "Filipino", "trait_tag": "Teaching-Ed"},
            {"option_id": 705, "option_text": "Social Studies", "trait_tag": "Community-Serve"},
            {"option_id": 706, "option_text": "Computer/ICT/TLE", "trait_tag": "Software-Dev"},
            {"option_id": 707, "option_text": "Arts", "trait_tag": "Visual-Design"},
            {"option_id": 708, "option_text": "PE", "trait_tag": "Physical-Skill"},
            {"option_id": 709, "option_text": "Accounting/Business subjects", "trait_tag": "Finance-Acct"},
            {"option_id": 710, "option_text": "Research/Practical Research", "trait_tag": "Lab-Research"}
        ]
    },
    {
        "question_id": 72,
        "question_text": "What's your LEAST favorite or most challenging subject?",
        "category": "Challenging Subject",
        "options": [
            {"option_id": 711, "option_text": "Math - too many formulas", "trait_tag": "Visual-Design"},
            {"option_id": 712, "option_text": "Science - hard to memorize", "trait_tag": "Finance-Acct"},
            {"option_id": 713, "option_text": "English - grammar is confusing", "trait_tag": "Technical-Skill"},
            {"option_id": 714, "option_text": "Filipino - prefer English", "trait_tag": "Software-Dev"},
            {"option_id": 715, "option_text": "History - too many dates", "trait_tag": "Data-Analytics"},
            {"option_id": 716, "option_text": "PE - not athletic", "trait_tag": "Lab-Research"},
            {"option_id": 717, "option_text": "Arts - not creative", "trait_tag": "Finance-Acct"},
            {"option_id": 718, "option_text": "Computer - technology confuses me", "trait_tag": "Patient-Care"},
            {"option_id": 719, "option_text": "None - I do well in all subjects", "trait_tag": "Teaching-Ed"},
            {"option_id": 720, "option_text": "All are equally challenging", "trait_tag": "Admin-Skill"}
        ]
    },

    # ==================== SECTION 9: FUTURE VISION ====================
    {
        "question_id": 73,
        "question_text": "Where do you see yourself in 10 YEARS?",
        "category": "Future Vision",
        "options": [
            {"option_id": 721, "option_text": "Working in a hospital saving lives", "trait_tag": "Patient-Care"},
            {"option_id": 722, "option_text": "Running my own successful business", "trait_tag": "Startup-Venture"},
            {"option_id": 723, "option_text": "Working as a professional in a corporate office", "trait_tag": "Finance-Acct"},
            {"option_id": 724, "option_text": "Teaching and inspiring students", "trait_tag": "Teaching-Ed"},
            {"option_id": 725, "option_text": "Working abroad earning dollars", "trait_tag": "Maritime-Sea"},
            {"option_id": 726, "option_text": "In uniform serving the country", "trait_tag": "Law-Enforce"},
            {"option_id": 727, "option_text": "Creating art or designs that people admire", "trait_tag": "Visual-Design"},
            {"option_id": 728, "option_text": "Building structures that last generations", "trait_tag": "Civil-Build"},
            {"option_id": 729, "option_text": "Developing technology that changes lives", "trait_tag": "Software-Dev"},
            {"option_id": 730, "option_text": "Serving my community/helping the poor", "trait_tag": "Community-Serve"}
        ]
    },
    {
        "question_id": 74,
        "question_text": "What LEGACY do you want to leave?",
        "category": "Life Legacy",
        "options": [
            {"option_id": 731, "option_text": "Saved many lives as a healthcare worker", "trait_tag": "Patient-Care"},
            {"option_id": 732, "option_text": "Built a successful company that employs many", "trait_tag": "Startup-Venture"},
            {"option_id": 733, "option_text": "Inspired thousands of students as a teacher", "trait_tag": "Teaching-Ed"},
            {"option_id": 734, "option_text": "Created art/designs that people remember", "trait_tag": "Visual-Design"},
            {"option_id": 735, "option_text": "Built structures that stand for centuries", "trait_tag": "Civil-Build"},
            {"option_id": 736, "option_text": "Developed technology used by millions", "trait_tag": "Software-Dev"},
            {"option_id": 737, "option_text": "Protected the community from crime", "trait_tag": "Law-Enforce"},
            {"option_id": 738, "option_text": "Managed finances that grew wealth", "trait_tag": "Finance-Acct"},
            {"option_id": 739, "option_text": "Helped lift families out of poverty", "trait_tag": "Community-Serve"},
            {"option_id": 740, "option_text": "Preserved nature for future generations", "trait_tag": "Agri-Nature"}
        ]
    },
    {
        "question_id": 75,
        "question_text": "What's your BIGGEST career fear?",
        "category": "Career Fear",
        "options": [
            {"option_id": 741, "option_text": "Not passing the board exam", "trait_tag": "Patient-Care"},
            {"option_id": 742, "option_text": "Being stuck in a boring/repetitive job", "trait_tag": "Creative-Skill"},
            {"option_id": 743, "option_text": "Not earning enough money", "trait_tag": "Finance-Acct"},
            {"option_id": 744, "option_text": "Making a mistake that harms someone", "trait_tag": "Medical-Lab"},
            {"option_id": 745, "option_text": "Not being creative enough", "trait_tag": "Visual-Design"},
            {"option_id": 746, "option_text": "Technology becoming obsolete", "trait_tag": "Software-Dev"},
            {"option_id": 747, "option_text": "Not finding a job in my field", "trait_tag": "Teaching-Ed"},
            {"option_id": 748, "option_text": "Physical danger in the job", "trait_tag": "Law-Enforce"},
            {"option_id": 749, "option_text": "Being away from family (OFW)", "trait_tag": "Maritime-Sea"},
            {"option_id": 750, "option_text": "Not making a meaningful impact", "trait_tag": "Community-Serve"}
        ]
    },

    # ==================== SECTION 10: PROBLEM-SOLVING STYLE ====================
    {
        "question_id": 76,
        "question_text": "How do you typically SOLVE PROBLEMS?",
        "category": "Problem Solving",
        "options": [
            {"option_id": 751, "option_text": "Analyze data and use logic", "trait_tag": "Data-Analytics"},
            {"option_id": 752, "option_text": "Research and gather information", "trait_tag": "Lab-Research"},
            {"option_id": 753, "option_text": "Ask experts or people with experience", "trait_tag": "People-Skill"},
            {"option_id": 754, "option_text": "Trial and error until it works", "trait_tag": "Technical-Skill"},
            {"option_id": 755, "option_text": "Think creatively, outside the box", "trait_tag": "Visual-Design"},
            {"option_id": 756, "option_text": "Follow established procedures", "trait_tag": "Admin-Skill"},
            {"option_id": 757, "option_text": "Break it down into smaller steps", "trait_tag": "Software-Dev"},
            {"option_id": 758, "option_text": "Use past experience", "trait_tag": "Teaching-Ed"},
            {"option_id": 759, "option_text": "Calculate and compute solutions", "trait_tag": "Finance-Acct"},
            {"option_id": 760, "option_text": "Take immediate action", "trait_tag": "Patient-Care"}
        ]
    },
    {
        "question_id": 77,
        "question_text": "When making DECISIONS, you tend to:",
        "category": "Decision Making",
        "options": [
            {"option_id": 761, "option_text": "Analyze all the facts and data", "trait_tag": "Data-Analytics"},
            {"option_id": 762, "option_text": "Consider how it affects others", "trait_tag": "Patient-Care"},
            {"option_id": 763, "option_text": "Think about the financial impact", "trait_tag": "Finance-Acct"},
            {"option_id": 764, "option_text": "Go with your gut feeling", "trait_tag": "Creative-Skill"},
            {"option_id": 765, "option_text": "Consult with others first", "trait_tag": "People-Skill"},
            {"option_id": 766, "option_text": "Follow rules and regulations", "trait_tag": "Law-Enforce"},
            {"option_id": 767, "option_text": "Think about long-term effects", "trait_tag": "Civil-Build"},
            {"option_id": 768, "option_text": "Consider the ethical implications", "trait_tag": "Community-Serve"},
            {"option_id": 769, "option_text": "Test with a small experiment first", "trait_tag": "Lab-Research"},
            {"option_id": 770, "option_text": "Decide quickly and adapt", "trait_tag": "Startup-Venture"}
        ]
    },
    {
        "question_id": 78,
        "question_text": "How do you prefer to LEARN new things?",
        "category": "Learning Style",
        "options": [
            {"option_id": 771, "option_text": "Reading books and articles", "trait_tag": "Teaching-Ed"},
            {"option_id": 772, "option_text": "Watching videos and tutorials", "trait_tag": "Digital-Media"},
            {"option_id": 773, "option_text": "Hands-on practice and doing", "trait_tag": "Technical-Skill"},
            {"option_id": 774, "option_text": "Classroom lectures", "trait_tag": "Lab-Research"},
            {"option_id": 775, "option_text": "Group discussions", "trait_tag": "People-Skill"},
            {"option_id": 776, "option_text": "Online courses and apps", "trait_tag": "Software-Dev"},
            {"option_id": 777, "option_text": "Mentorship from experts", "trait_tag": "Patient-Care"},
            {"option_id": 778, "option_text": "Trial and error", "trait_tag": "Startup-Venture"},
            {"option_id": 779, "option_text": "Visual diagrams and maps", "trait_tag": "Visual-Design"},
            {"option_id": 780, "option_text": "Structured step-by-step guides", "trait_tag": "Finance-Acct"}
        ]
    },
    {
        "question_id": 79,
        "question_text": "How do you handle DISAGREEMENTS with others?",
        "category": "Conflict Resolution",
        "options": [
            {"option_id": 781, "option_text": "Present facts and logic to convince them", "trait_tag": "Data-Analytics"},
            {"option_id": 782, "option_text": "Listen to their side first", "trait_tag": "People-Skill"},
            {"option_id": 783, "option_text": "Find a compromise", "trait_tag": "Community-Serve"},
            {"option_id": 784, "option_text": "Stand firm on my position", "trait_tag": "Law-Enforce"},
            {"option_id": 785, "option_text": "Avoid confrontation", "trait_tag": "Lab-Research"},
            {"option_id": 786, "option_text": "Use humor to diffuse tension", "trait_tag": "Hospitality-Svc"},
            {"option_id": 787, "option_text": "Seek a mediator", "trait_tag": "Admin-Skill"},
            {"option_id": 788, "option_text": "Give them time to cool down", "trait_tag": "Patient-Care"},
            {"option_id": 789, "option_text": "Focus on common goals", "trait_tag": "Teaching-Ed"},
            {"option_id": 790, "option_text": "Propose a creative alternative", "trait_tag": "Visual-Design"}
        ]
    },
    {
        "question_id": 80,
        "question_text": "What type of TEAM ROLE do you naturally take?",
        "category": "Team Role",
        "options": [
            {"option_id": 791, "option_text": "The Leader - directing the team", "trait_tag": "Startup-Venture"},
            {"option_id": 792, "option_text": "The Analyzer - studying the problem", "trait_tag": "Data-Analytics"},
            {"option_id": 793, "option_text": "The Creative - generating ideas", "trait_tag": "Visual-Design"},
            {"option_id": 794, "option_text": "The Executor - getting things done", "trait_tag": "Technical-Skill"},
            {"option_id": 795, "option_text": "The Mediator - keeping peace", "trait_tag": "People-Skill"},
            {"option_id": 796, "option_text": "The Organizer - planning and scheduling", "trait_tag": "Admin-Skill"},
            {"option_id": 797, "option_text": "The Expert - providing knowledge", "trait_tag": "Lab-Research"},
            {"option_id": 798, "option_text": "The Supporter - helping wherever needed", "trait_tag": "Patient-Care"},
            {"option_id": 799, "option_text": "The Quality Checker - ensuring accuracy", "trait_tag": "Finance-Acct"},
            {"option_id": 800, "option_text": "The Motivator - boosting morale", "trait_tag": "Teaching-Ed"}
        ]
    },
    
    # ==================== SITUATIONAL QUESTIONS ====================
    # Scenario-based questions that assess how students would react in real-life situations
    # Each option aligns with different career traits and courses
    
    {
        "question_id": 81,
        "question_text": "Your classmate suddenly collapses during PE class. What would you do first?",
        "category": "Situational - Emergency",
        "options": [
            {"option_id": 801, "option_text": "Rush to check their pulse and breathing, then perform first aid", "trait_tag": "Patient-Care"},
            {"option_id": 802, "option_text": "Stay calm, take charge and direct others to call for help", "trait_tag": "Startup-Venture"},
            {"option_id": 803, "option_text": "Quickly analyze what might have caused this (heat, dehydration, etc.)", "trait_tag": "Medical-Lab"},
            {"option_id": 804, "option_text": "Document the incident and time for the school clinic records", "trait_tag": "Admin-Skill"},
            {"option_id": 805, "option_text": "Comfort and reassure other classmates who are panicking", "trait_tag": "Teaching-Ed"},
            {"option_id": 806, "option_text": "Run to get the school nurse or security guard immediately", "trait_tag": "Law-Enforce"},
            {"option_id": 807, "option_text": "Think of ways to prevent this from happening again", "trait_tag": "Industrial-Ops"},
            {"option_id": 808, "option_text": "Help create shade or find a cool area for the student", "trait_tag": "Civil-Build"}
        ]
    },
    {
        "question_id": 82,
        "question_text": "Your barangay is planning a community project. Which role would you volunteer for?",
        "category": "Situational - Community",
        "options": [
            {"option_id": 809, "option_text": "Organize a free health checkup and first aid station", "trait_tag": "Patient-Care"},
            {"option_id": 810, "option_text": "Design posters and promotional materials for the event", "trait_tag": "Visual-Design"},
            {"option_id": 811, "option_text": "Create a website or social media page to promote it", "trait_tag": "Software-Dev"},
            {"option_id": 812, "option_text": "Handle the budget, collect donations, and track expenses", "trait_tag": "Finance-Acct"},
            {"option_id": 813, "option_text": "Lead and coordinate all the volunteer teams", "trait_tag": "Startup-Venture"},
            {"option_id": 814, "option_text": "Teach livelihood skills or conduct tutorials for youth", "trait_tag": "Teaching-Ed"},
            {"option_id": 815, "option_text": "Set up security and crowd control measures", "trait_tag": "Law-Enforce"},
            {"option_id": 816, "option_text": "Plan the venue layout and structural setup", "trait_tag": "Civil-Build"},
            {"option_id": 817, "option_text": "Organize a tree planting or clean-up drive", "trait_tag": "Agri-Nature"},
            {"option_id": 818, "option_text": "Prepare food and refreshments for volunteers", "trait_tag": "Hospitality-Svc"}
        ]
    },
    {
        "question_id": 83,
        "question_text": "You're assigned to lead a group project with unmotivated members. How do you handle it?",
        "category": "Situational - Leadership",
        "options": [
            {"option_id": 819, "option_text": "Create a detailed project plan with clear deadlines for everyone", "trait_tag": "Admin-Skill"},
            {"option_id": 820, "option_text": "Talk to each member personally to understand their concerns", "trait_tag": "People-Skill"},
            {"option_id": 821, "option_text": "Take charge and assign tasks based on each person's strengths", "trait_tag": "Startup-Venture"},
            {"option_id": 822, "option_text": "Use creative approaches to make the project more interesting", "trait_tag": "Visual-Design"},
            {"option_id": 823, "option_text": "Research the topic thoroughly and share knowledge to help them", "trait_tag": "Lab-Research"},
            {"option_id": 824, "option_text": "Create a rewards system or gamify the tasks", "trait_tag": "Teaching-Ed"},
            {"option_id": 825, "option_text": "Build a shared online document or app to track progress", "trait_tag": "Software-Dev"},
            {"option_id": 826, "option_text": "Focus on the practical, hands-on parts to keep them engaged", "trait_tag": "Technical-Skill"}
        ]
    },
    {
        "question_id": 84,
        "question_text": "A typhoon damaged several houses in your area. How would you want to help?",
        "category": "Situational - Disaster Response",
        "options": [
            {"option_id": 827, "option_text": "Join medical missions to treat injured victims", "trait_tag": "Patient-Care"},
            {"option_id": 828, "option_text": "Help rebuild or repair damaged structures", "trait_tag": "Civil-Build"},
            {"option_id": 829, "option_text": "Organize relief goods distribution and logistics", "trait_tag": "Admin-Skill"},
            {"option_id": 830, "option_text": "Set up communication systems for rescue coordination", "trait_tag": "Hardware-Systems"},
            {"option_id": 831, "option_text": "Document damage and help families with insurance claims", "trait_tag": "Finance-Acct"},
            {"option_id": 832, "option_text": "Counsel traumatized victims, especially children", "trait_tag": "Rehab-Therapy"},
            {"option_id": 833, "option_text": "Help in rescue operations and maintain order", "trait_tag": "Law-Enforce"},
            {"option_id": 834, "option_text": "Cook meals and manage temporary shelters", "trait_tag": "Hospitality-Svc"},
            {"option_id": 835, "option_text": "Assess environmental damage and clean-up needs", "trait_tag": "Field-Research"},
            {"option_id": 836, "option_text": "Use social media to spread awareness and call for donations", "trait_tag": "Digital-Media"}
        ]
    },
    {
        "question_id": 85,
        "question_text": "Your school is organizing a career fair. What booth would you want to manage?",
        "category": "Situational - School Event",
        "options": [
            {"option_id": 837, "option_text": "Healthcare booth with blood pressure and BMI checks", "trait_tag": "Patient-Care"},
            {"option_id": 838, "option_text": "Tech booth showcasing apps and coding demos", "trait_tag": "Software-Dev"},
            {"option_id": 839, "option_text": "Engineering booth with building models and robots", "trait_tag": "Mechanical-Design"},
            {"option_id": 840, "option_text": "Business booth with entrepreneurship tips and mock stocks", "trait_tag": "Startup-Venture"},
            {"option_id": 841, "option_text": "Arts booth with live sketching and design demos", "trait_tag": "Visual-Design"},
            {"option_id": 842, "option_text": "Criminology booth with forensic science activities", "trait_tag": "Law-Enforce"},
            {"option_id": 843, "option_text": "Maritime booth with ship models and navigation demos", "trait_tag": "Maritime-Sea"},
            {"option_id": 844, "option_text": "Hospitality booth serving sample dishes and drinks", "trait_tag": "Hospitality-Svc"},
            {"option_id": 845, "option_text": "Science booth with experiments and lab demonstrations", "trait_tag": "Lab-Research"},
            {"option_id": 846, "option_text": "Agriculture booth with plant propagation activities", "trait_tag": "Agri-Nature"}
        ]
    },
    {
        "question_id": 86,
        "question_text": "You found a lost wallet with cash and IDs near your school. What do you do?",
        "category": "Situational - Ethics",
        "options": [
            {"option_id": 847, "option_text": "Turn it in to the school security or police station", "trait_tag": "Law-Enforce"},
            {"option_id": 848, "option_text": "Try to contact the owner using the ID information", "trait_tag": "People-Skill"},
            {"option_id": 849, "option_text": "Post about it on social media to find the owner", "trait_tag": "Digital-Media"},
            {"option_id": 850, "option_text": "Keep it safe and make an organized list of contents", "trait_tag": "Admin-Skill"},
            {"option_id": 851, "option_text": "Announce it in school and ask teachers for help", "trait_tag": "Teaching-Ed"},
            {"option_id": 852, "option_text": "Think about how the owner must be feeling and act quickly", "trait_tag": "Patient-Care"},
            {"option_id": 853, "option_text": "Research the name to find social media accounts", "trait_tag": "Data-Analytics"},
            {"option_id": 854, "option_text": "Document everything with photos before returning", "trait_tag": "Finance-Acct"}
        ]
    },
    {
        "question_id": 87,
        "question_text": "Your family is starting a small business. How would you contribute?",
        "category": "Situational - Family Business",
        "options": [
            {"option_id": 855, "option_text": "Handle the accounting, pricing, and financial records", "trait_tag": "Finance-Acct"},
            {"option_id": 856, "option_text": "Create the logo, packaging, and visual branding", "trait_tag": "Visual-Design"},
            {"option_id": 857, "option_text": "Build a website and manage online sales", "trait_tag": "Software-Dev"},
            {"option_id": 858, "option_text": "Develop marketing strategies and social media content", "trait_tag": "Marketing-Sales"},
            {"option_id": 859, "option_text": "Manage inventory, suppliers, and daily operations", "trait_tag": "Admin-Skill"},
            {"option_id": 860, "option_text": "Come up with new product ideas and business strategies", "trait_tag": "Startup-Venture"},
            {"option_id": 861, "option_text": "Handle customer service and build client relationships", "trait_tag": "People-Skill"},
            {"option_id": 862, "option_text": "Set up equipment, fixtures, and technical systems", "trait_tag": "Technical-Skill"},
            {"option_id": 863, "option_text": "If it's food, focus on recipes and food preparation", "trait_tag": "Hospitality-Svc"},
            {"option_id": 864, "option_text": "Ensure legal compliance and business registration", "trait_tag": "Law-Enforce"}
        ]
    },
    {
        "question_id": 88,
        "question_text": "You notice a classmate seems depressed and withdrawn lately. How do you approach this?",
        "category": "Situational - Mental Health",
        "options": [
            {"option_id": 865, "option_text": "Talk to them privately and listen without judgment", "trait_tag": "Rehab-Therapy"},
            {"option_id": 866, "option_text": "Inform a trusted teacher or guidance counselor", "trait_tag": "Teaching-Ed"},
            {"option_id": 867, "option_text": "Research about mental health to understand what they might be going through", "trait_tag": "Lab-Research"},
            {"option_id": 868, "option_text": "Invite them to activities to help them feel included", "trait_tag": "People-Skill"},
            {"option_id": 869, "option_text": "Create something artistic or a playlist to cheer them up", "trait_tag": "Creative-Skill"},
            {"option_id": 870, "option_text": "Organize a support group among trusted friends", "trait_tag": "Community-Serve"},
            {"option_id": 871, "option_text": "Monitor the situation and document any concerning changes", "trait_tag": "Patient-Care"},
            {"option_id": 872, "option_text": "Help them with schoolwork to reduce their stress", "trait_tag": "Admin-Skill"}
        ]
    },
    {
        "question_id": 89,
        "question_text": "Your school's computer lab has been hacked and files are encrypted. What's your reaction?",
        "category": "Situational - Technology Crisis",
        "options": [
            {"option_id": 873, "option_text": "Try to analyze the malware and find a solution", "trait_tag": "Cyber-Defense"},
            {"option_id": 874, "option_text": "Document everything and report to IT authorities", "trait_tag": "Admin-Skill"},
            {"option_id": 875, "option_text": "Help restore data from backup systems", "trait_tag": "Software-Dev"},
            {"option_id": 876, "option_text": "Investigate who might be responsible", "trait_tag": "Law-Enforce"},
            {"option_id": 877, "option_text": "Calm down panicking students and teachers", "trait_tag": "Teaching-Ed"},
            {"option_id": 878, "option_text": "Calculate the financial impact and insurance claims", "trait_tag": "Finance-Acct"},
            {"option_id": 879, "option_text": "Set up alternative systems so classes can continue", "trait_tag": "Hardware-Systems"},
            {"option_id": 880, "option_text": "Create awareness materials about cybersecurity", "trait_tag": "Digital-Media"}
        ]
    },
    {
        "question_id": 90,
        "question_text": "You're stranded on an island with your friends for a survival challenge. What role do you take?",
        "category": "Situational - Survival",
        "options": [
            {"option_id": 881, "option_text": "Build shelter and secure the campsite", "trait_tag": "Civil-Build"},
            {"option_id": 882, "option_text": "Find and purify water, identify safe plants to eat", "trait_tag": "Field-Research"},
            {"option_id": 883, "option_text": "Take care of anyone who gets injured or sick", "trait_tag": "Patient-Care"},
            {"option_id": 884, "option_text": "Lead the group and make strategic decisions", "trait_tag": "Startup-Venture"},
            {"option_id": 885, "option_text": "Create tools and repair equipment", "trait_tag": "Mechanical-Design"},
            {"option_id": 886, "option_text": "Keep everyone's spirits up and resolve conflicts", "trait_tag": "People-Skill"},
            {"option_id": 887, "option_text": "Figure out navigation and plan an escape route", "trait_tag": "Maritime-Sea"},
            {"option_id": 888, "option_text": "Hunt, fish, or forage for food", "trait_tag": "Agri-Nature"},
            {"option_id": 889, "option_text": "Document the experience and keep a survival log", "trait_tag": "Creative-Skill"},
            {"option_id": 890, "option_text": "Create signals or devices to call for rescue", "trait_tag": "Hardware-Systems"}
        ]
    },
    {
        "question_id": 91,
        "question_text": "A local store owner asks for advice to compete with online shopping. What do you suggest?",
        "category": "Situational - Business",
        "options": [
            {"option_id": 891, "option_text": "Build them an e-commerce website and app", "trait_tag": "Software-Dev"},
            {"option_id": 892, "option_text": "Help them with digital marketing and social media", "trait_tag": "Marketing-Sales"},
            {"option_id": 893, "option_text": "Redesign their store layout and visual branding", "trait_tag": "Visual-Design"},
            {"option_id": 894, "option_text": "Analyze their finances and suggest cost-cutting", "trait_tag": "Finance-Acct"},
            {"option_id": 895, "option_text": "Create a loyalty program and customer database", "trait_tag": "Data-Analytics"},
            {"option_id": 896, "option_text": "Train their staff on customer service", "trait_tag": "Teaching-Ed"},
            {"option_id": 897, "option_text": "Focus on personalized service that online can't match", "trait_tag": "Hospitality-Svc"},
            {"option_id": 898, "option_text": "Develop a unique business strategy to stand out", "trait_tag": "Startup-Venture"}
        ]
    },
    {
        "question_id": 92,
        "question_text": "Your town is debating whether to build a factory that will create jobs but may cause pollution. Your stance?",
        "category": "Situational - Environmental",
        "options": [
            {"option_id": 899, "option_text": "Conduct environmental impact studies first", "trait_tag": "Field-Research"},
            {"option_id": 900, "option_text": "Propose engineering solutions to minimize pollution", "trait_tag": "Industrial-Ops"},
            {"option_id": 901, "option_text": "Focus on the economic benefits and job creation", "trait_tag": "Finance-Acct"},
            {"option_id": 902, "option_text": "Advocate for renewable and sustainable alternatives", "trait_tag": "Agri-Nature"},
            {"option_id": 903, "option_text": "Analyze health risks for the community", "trait_tag": "Patient-Care"},
            {"option_id": 904, "option_text": "Research legal requirements and compliance", "trait_tag": "Law-Enforce"},
            {"option_id": 905, "option_text": "Organize community forums for discussion", "trait_tag": "Community-Serve"},
            {"option_id": 906, "option_text": "Create awareness campaigns about both sides", "trait_tag": "Digital-Media"}
        ]
    },
    {
        "question_id": 93,
        "question_text": "You're asked to help organize your school's foundation anniversary. What task do you prefer?",
        "category": "Situational - Event Planning",
        "options": [
            {"option_id": 907, "option_text": "Handle the budget and collect contributions", "trait_tag": "Finance-Acct"},
            {"option_id": 908, "option_text": "Design invitations, banners, and stage backdrop", "trait_tag": "Visual-Design"},
            {"option_id": 909, "option_text": "Direct the program and coordinate performances", "trait_tag": "Creative-Skill"},
            {"option_id": 910, "option_text": "Set up sound systems, lights, and technical equipment", "trait_tag": "Hardware-Systems"},
            {"option_id": 911, "option_text": "Manage food catering and hospitality for guests", "trait_tag": "Hospitality-Svc"},
            {"option_id": 912, "option_text": "Lead the overall organizing committee", "trait_tag": "Startup-Venture"},
            {"option_id": 913, "option_text": "Handle security and crowd management", "trait_tag": "Law-Enforce"},
            {"option_id": 914, "option_text": "Document and livestream the event online", "trait_tag": "Digital-Media"},
            {"option_id": 915, "option_text": "Prepare first aid station in case of emergencies", "trait_tag": "Patient-Care"},
            {"option_id": 916, "option_text": "Coordinate with teachers and handle logistics", "trait_tag": "Admin-Skill"}
        ]
    },
    {
        "question_id": 94,
        "question_text": "A friend confides that they're being bullied online. How do you help?",
        "category": "Situational - Cyberbullying",
        "options": [
            {"option_id": 917, "option_text": "Listen to them and provide emotional support", "trait_tag": "Rehab-Therapy"},
            {"option_id": 918, "option_text": "Document the evidence and report to authorities", "trait_tag": "Law-Enforce"},
            {"option_id": 919, "option_text": "Help them adjust privacy settings and block the bully", "trait_tag": "Software-Dev"},
            {"option_id": 920, "option_text": "Inform a teacher or guidance counselor", "trait_tag": "Teaching-Ed"},
            {"option_id": 921, "option_text": "Research laws about cyberbullying", "trait_tag": "Community-Serve"},
            {"option_id": 922, "option_text": "Create a support group with other friends", "trait_tag": "People-Skill"},
            {"option_id": 923, "option_text": "Help them build confidence through activities", "trait_tag": "Creative-Skill"},
            {"option_id": 924, "option_text": "Track down who the bully is using digital clues", "trait_tag": "Cyber-Defense"}
        ]
    },
    {
        "question_id": 95,
        "question_text": "Your family member is diagnosed with a chronic illness. How do you cope and help?",
        "category": "Situational - Family Health",
        "options": [
            {"option_id": 925, "option_text": "Learn about the illness and help with their care", "trait_tag": "Patient-Care"},
            {"option_id": 926, "option_text": "Research the best doctors and treatment options", "trait_tag": "Medical-Lab"},
            {"option_id": 927, "option_text": "Manage medical expenses and insurance paperwork", "trait_tag": "Finance-Acct"},
            {"option_id": 928, "option_text": "Provide emotional support and stay positive", "trait_tag": "Rehab-Therapy"},
            {"option_id": 929, "option_text": "Help with physical therapy exercises at home", "trait_tag": "Rehab-Therapy"},
            {"option_id": 930, "option_text": "Prepare nutritious meals for their diet", "trait_tag": "Hospitality-Svc"},
            {"option_id": 931, "option_text": "Organize family schedules to share caregiving duties", "trait_tag": "Admin-Skill"},
            {"option_id": 932, "option_text": "Find support groups and community resources", "trait_tag": "Community-Serve"}
        ]
    },
    {
        "question_id": 96,
        "question_text": "You witness someone shoplifting at a mall. What's your reaction?",
        "category": "Situational - Ethics",
        "options": [
            {"option_id": 933, "option_text": "Immediately report to security guards", "trait_tag": "Law-Enforce"},
            {"option_id": 934, "option_text": "Discreetly take photos/video as evidence", "trait_tag": "Digital-Media"},
            {"option_id": 935, "option_text": "Think about why someone might resort to stealing", "trait_tag": "Community-Serve"},
            {"option_id": 936, "option_text": "Alert the store staff calmly and privately", "trait_tag": "Admin-Skill"},
            {"option_id": 937, "option_text": "Consider if it's safe to confront them directly", "trait_tag": "People-Skill"},
            {"option_id": 938, "option_text": "Think about the store's loss prevention measures", "trait_tag": "Finance-Acct"},
            {"option_id": 939, "option_text": "Wonder about the psychological factors involved", "trait_tag": "Rehab-Therapy"},
            {"option_id": 940, "option_text": "Think of technical solutions like better security systems", "trait_tag": "Hardware-Systems"}
        ]
    },
    {
        "question_id": 97,
        "question_text": "Your school wants to create a mobile app for students. What feature do you want to develop?",
        "category": "Situational - Technology",
        "options": [
            {"option_id": 941, "option_text": "Grade tracking and academic performance analytics", "trait_tag": "Data-Analytics"},
            {"option_id": 942, "option_text": "The overall user interface and visual design", "trait_tag": "Visual-Design"},
            {"option_id": 943, "option_text": "The backend programming and database", "trait_tag": "Software-Dev"},
            {"option_id": 944, "option_text": "Security features to protect student data", "trait_tag": "Cyber-Defense"},
            {"option_id": 945, "option_text": "Communication features for student-teacher interaction", "trait_tag": "Teaching-Ed"},
            {"option_id": 946, "option_text": "Financial modules for tracking fees and payments", "trait_tag": "Finance-Acct"},
            {"option_id": 947, "option_text": "Health and wellness tracking features", "trait_tag": "Patient-Care"},
            {"option_id": 948, "option_text": "Event planning and school activity calendar", "trait_tag": "Admin-Skill"}
        ]
    },
    {
        "question_id": 98,
        "question_text": "You're tasked to create a documentary about your local community. What topic would you choose?",
        "category": "Situational - Media",
        "options": [
            {"option_id": 949, "option_text": "Local healthcare heroes and medical workers", "trait_tag": "Patient-Care"},
            {"option_id": 950, "option_text": "Small businesses and entrepreneurial success stories", "trait_tag": "Startup-Venture"},
            {"option_id": 951, "option_text": "Environmental issues and conservation efforts", "trait_tag": "Field-Research"},
            {"option_id": 952, "option_text": "Local artists, musicians, and creative talents", "trait_tag": "Creative-Skill"},
            {"option_id": 953, "option_text": "Education and inspiring teacher stories", "trait_tag": "Teaching-Ed"},
            {"option_id": 954, "option_text": "Crime prevention and community safety", "trait_tag": "Law-Enforce"},
            {"option_id": 955, "option_text": "Farmers and agricultural practices", "trait_tag": "Agri-Nature"},
            {"option_id": 956, "option_text": "Infrastructure development and urban planning", "trait_tag": "Civil-Build"},
            {"option_id": 957, "option_text": "Technology adoption and digital transformation", "trait_tag": "Software-Dev"},
            {"option_id": 958, "option_text": "Local food culture and culinary traditions", "trait_tag": "Hospitality-Svc"}
        ]
    },
    {
        "question_id": 99,
        "question_text": "A classmate copied your homework and submitted it as their own. How do you handle it?",
        "category": "Situational - Academic Integrity",
        "options": [
            {"option_id": 959, "option_text": "Report it to the teacher with evidence", "trait_tag": "Law-Enforce"},
            {"option_id": 960, "option_text": "Confront them privately and ask why they did it", "trait_tag": "People-Skill"},
            {"option_id": 961, "option_text": "Offer to tutor them so they don't need to copy again", "trait_tag": "Teaching-Ed"},
            {"option_id": 962, "option_text": "Keep records and document future incidents", "trait_tag": "Admin-Skill"},
            {"option_id": 963, "option_text": "Think about their circumstances - maybe they needed help", "trait_tag": "Rehab-Therapy"},
            {"option_id": 964, "option_text": "Create a study group to help struggling classmates", "trait_tag": "Community-Serve"},
            {"option_id": 965, "option_text": "Develop a system to prevent copying in the future", "trait_tag": "Software-Dev"},
            {"option_id": 966, "option_text": "Let it go this time but protect your work better", "trait_tag": "Cyber-Defense"}
        ]
    },
    {
        "question_id": 100,
        "question_text": "You won a significant amount in a school raffle. How would you spend it?",
        "category": "Situational - Financial Decision",
        "options": [
            {"option_id": 967, "option_text": "Save it and invest for future education", "trait_tag": "Finance-Acct"},
            {"option_id": 968, "option_text": "Buy equipment for a skill I want to develop", "trait_tag": "Technical-Skill"},
            {"option_id": 969, "option_text": "Donate part of it to charity or community causes", "trait_tag": "Community-Serve"},
            {"option_id": 970, "option_text": "Start a small business or side hustle", "trait_tag": "Startup-Venture"},
            {"option_id": 971, "option_text": "Buy art supplies or creative tools", "trait_tag": "Visual-Design"},
            {"option_id": 972, "option_text": "Get a new computer or tech gadgets", "trait_tag": "Software-Dev"},
            {"option_id": 973, "option_text": "Help my family with household expenses", "trait_tag": "Patient-Care"},
            {"option_id": 974, "option_text": "Take a course or workshop to learn something new", "trait_tag": "Teaching-Ed"},
            {"option_id": 975, "option_text": "Travel and explore new places", "trait_tag": "Hospitality-Svc"},
            {"option_id": 976, "option_text": "Buy books and study materials", "trait_tag": "Lab-Research"}
        ]
    },
    
    # ==================== NEW SITUATIONAL QUESTIONS (101-120) ====================
    {
        "question_id": 101,
        "question_text": "Your school is organizing a career fair. Which booth would you volunteer to manage?",
        "category": "Situational - Career Fair",
        "options": [
            {"option_id": 1001, "option_text": "Healthcare booth - explaining nursing and medical careers", "trait_tag": "Patient-Care"},
            {"option_id": 1002, "option_text": "Technology booth - demonstrating apps and coding projects", "trait_tag": "Software-Dev"},
            {"option_id": 1003, "option_text": "Engineering booth - showing building models and designs", "trait_tag": "Civil-Build"},
            {"option_id": 1004, "option_text": "Business booth - presenting entrepreneurship success stories", "trait_tag": "Startup-Venture"},
            {"option_id": 1005, "option_text": "Arts booth - displaying creative works and portfolios", "trait_tag": "Visual-Design"},
            {"option_id": 1006, "option_text": "Education booth - helping students explore teaching careers", "trait_tag": "Teaching-Ed"},
            {"option_id": 1007, "option_text": "Law & Security booth - discussing criminology and justice", "trait_tag": "Law-Enforce"},
            {"option_id": 1008, "option_text": "Maritime booth - explaining ship careers and navigation", "trait_tag": "Maritime-Sea"},
            {"option_id": 1009, "option_text": "Agriculture booth - showcasing farming innovations", "trait_tag": "Agri-Nature"},
            {"option_id": 1010, "option_text": "Hospitality booth - promoting tourism and hotel management", "trait_tag": "Hospitality-Svc"}
        ]
    },
    {
        "question_id": 102,
        "question_text": "A local barangay asks for help solving a community problem. What role would you take?",
        "category": "Situational - Community Problem",
        "options": [
            {"option_id": 1011, "option_text": "Organize a health screening for residents", "trait_tag": "Patient-Care"},
            {"option_id": 1012, "option_text": "Set up a computer literacy program for youth", "trait_tag": "Software-Dev"},
            {"option_id": 1013, "option_text": "Help design safer roads and walkways", "trait_tag": "Civil-Build"},
            {"option_id": 1014, "option_text": "Start a livelihood program for unemployed residents", "trait_tag": "Startup-Venture"},
            {"option_id": 1015, "option_text": "Create murals and beautify public spaces", "trait_tag": "Visual-Design"},
            {"option_id": 1016, "option_text": "Tutor children who are struggling in school", "trait_tag": "Teaching-Ed"},
            {"option_id": 1017, "option_text": "Help establish a neighborhood watch program", "trait_tag": "Law-Enforce"},
            {"option_id": 1018, "option_text": "Advocate for government services and social welfare", "trait_tag": "Community-Serve"},
            {"option_id": 1019, "option_text": "Set up an urban garden for food security", "trait_tag": "Agri-Nature"},
            {"option_id": 1020, "option_text": "Organize community events and festivals", "trait_tag": "Hospitality-Svc"}
        ]
    },
    {
        "question_id": 103,
        "question_text": "You discover your friend is making unhealthy life choices. How do you help?",
        "category": "Situational - Friend Support",
        "options": [
            {"option_id": 1021, "option_text": "Research health information and share it with them", "trait_tag": "Patient-Care"},
            {"option_id": 1022, "option_text": "Find apps or tools that could help them track their habits", "trait_tag": "Software-Dev"},
            {"option_id": 1023, "option_text": "Create a structured plan with goals and timelines", "trait_tag": "Industrial-Ops"},
            {"option_id": 1024, "option_text": "Connect them with a counselor or therapist", "trait_tag": "Rehab-Therapy"},
            {"option_id": 1025, "option_text": "Express your feelings through creative activities together", "trait_tag": "Creative-Skill"},
            {"option_id": 1026, "option_text": "Teach them about self-care and wellness techniques", "trait_tag": "Teaching-Ed"},
            {"option_id": 1027, "option_text": "Investigate what triggered their behavior changes", "trait_tag": "Lab-Research"},
            {"option_id": 1028, "option_text": "Organize group activities to keep them engaged socially", "trait_tag": "People-Skill"},
            {"option_id": 1029, "option_text": "Encourage physical activities like sports or exercise", "trait_tag": "Physical-Skill"},
            {"option_id": 1030, "option_text": "Help them manage their time and finances better", "trait_tag": "Finance-Acct"}
        ]
    },
    {
        "question_id": 104,
        "question_text": "Your family is planning to start a small business. What role would you take?",
        "category": "Situational - Family Business",
        "options": [
            {"option_id": 1031, "option_text": "Handle the bookkeeping and financial records", "trait_tag": "Finance-Acct"},
            {"option_id": 1032, "option_text": "Build a website and manage online presence", "trait_tag": "Software-Dev"},
            {"option_id": 1033, "option_text": "Design the store layout and physical setup", "trait_tag": "Spatial-Design"},
            {"option_id": 1034, "option_text": "Create the business plan and growth strategy", "trait_tag": "Startup-Venture"},
            {"option_id": 1035, "option_text": "Design logos, packaging, and marketing materials", "trait_tag": "Visual-Design"},
            {"option_id": 1036, "option_text": "Train employees and create procedures", "trait_tag": "Teaching-Ed"},
            {"option_id": 1037, "option_text": "Handle customer relations and sales", "trait_tag": "Marketing-Sales"},
            {"option_id": 1038, "option_text": "Manage inventory and supply chain logistics", "trait_tag": "Admin-Skill"},
            {"option_id": 1039, "option_text": "Research market trends and competition", "trait_tag": "Data-Analytics"},
            {"option_id": 1040, "option_text": "Ensure safety and security measures are in place", "trait_tag": "Law-Enforce"}
        ]
    },
    {
        "question_id": 105,
        "question_text": "There's a power outage in your area for several hours. How do you spend your time?",
        "category": "Situational - Power Outage",
        "options": [
            {"option_id": 1041, "option_text": "Check on elderly neighbors and offer assistance", "trait_tag": "Patient-Care"},
            {"option_id": 1042, "option_text": "Think about how to prevent this with better infrastructure", "trait_tag": "Electrical-Power"},
            {"option_id": 1043, "option_text": "Plan a backup power solution like solar panels", "trait_tag": "Mechanical-Design"},
            {"option_id": 1044, "option_text": "Calculate how much money was lost due to the outage", "trait_tag": "Finance-Acct"},
            {"option_id": 1045, "option_text": "Draw, paint, or work on creative projects by candlelight", "trait_tag": "Visual-Design"},
            {"option_id": 1046, "option_text": "Read books and study without distractions", "trait_tag": "Lab-Research"},
            {"option_id": 1047, "option_text": "Play games and tell stories with family", "trait_tag": "People-Skill"},
            {"option_id": 1048, "option_text": "Help organize the neighborhood response", "trait_tag": "Community-Serve"},
            {"option_id": 1049, "option_text": "Go outside and explore nature", "trait_tag": "Field-Research"},
            {"option_id": 1050, "option_text": "Cook and prepare food using alternative methods", "trait_tag": "Hospitality-Svc"}
        ]
    },
    {
        "question_id": 106,
        "question_text": "Your school needs help preparing for an accreditation visit. What would you volunteer to do?",
        "category": "Situational - Accreditation",
        "options": [
            {"option_id": 1051, "option_text": "Organize health records and first aid stations", "trait_tag": "Health-Admin"},
            {"option_id": 1052, "option_text": "Set up computer systems and presentations", "trait_tag": "Software-Dev"},
            {"option_id": 1053, "option_text": "Help with building maintenance and repairs", "trait_tag": "Civil-Build"},
            {"option_id": 1054, "option_text": "Prepare financial reports and budget documents", "trait_tag": "Finance-Acct"},
            {"option_id": 1055, "option_text": "Create visual displays and decorations", "trait_tag": "Visual-Design"},
            {"option_id": 1056, "option_text": "Prepare lesson plans and teaching demonstrations", "trait_tag": "Teaching-Ed"},
            {"option_id": 1057, "option_text": "Manage security and visitor flow", "trait_tag": "Law-Enforce"},
            {"option_id": 1058, "option_text": "Organize documents and administrative files", "trait_tag": "Admin-Skill"},
            {"option_id": 1059, "option_text": "Prepare scientific lab demonstrations", "trait_tag": "Lab-Research"},
            {"option_id": 1060, "option_text": "Coordinate food and hospitality for guests", "trait_tag": "Hospitality-Svc"}
        ]
    },
    {
        "question_id": 107,
        "question_text": "You witness someone collapse on the street. What is your immediate response?",
        "category": "Situational - Medical Emergency",
        "options": [
            {"option_id": 1061, "option_text": "Rush to help and check their vital signs", "trait_tag": "Patient-Care"},
            {"option_id": 1062, "option_text": "Call emergency services immediately", "trait_tag": "Technical-Skill"},
            {"option_id": 1063, "option_text": "Look for a safe space to move them away from traffic", "trait_tag": "Civil-Build"},
            {"option_id": 1064, "option_text": "Start CPR if they're unresponsive", "trait_tag": "Rehab-Therapy"},
            {"option_id": 1065, "option_text": "Document what happened in case it's needed", "trait_tag": "Law-Enforce"},
            {"option_id": 1066, "option_text": "Calm down bystanders and explain what to do", "trait_tag": "Teaching-Ed"},
            {"option_id": 1067, "option_text": "Direct traffic to prevent accidents", "trait_tag": "Community-Serve"},
            {"option_id": 1068, "option_text": "Search their belongings for medical information", "trait_tag": "Medical-Lab"},
            {"option_id": 1069, "option_text": "Stay with them and provide emotional support", "trait_tag": "People-Skill"},
            {"option_id": 1070, "option_text": "Think about how hospitals could respond faster", "trait_tag": "Health-Admin"}
        ]
    },
    {
        "question_id": 108,
        "question_text": "Your group is assigned a research project. What role do you naturally take?",
        "category": "Situational - Group Research",
        "options": [
            {"option_id": 1071, "option_text": "Conduct interviews and gather primary data", "trait_tag": "People-Skill"},
            {"option_id": 1072, "option_text": "Analyze data and create statistical reports", "trait_tag": "Data-Analytics"},
            {"option_id": 1073, "option_text": "Write the research paper and documentation", "trait_tag": "Lab-Research"},
            {"option_id": 1074, "option_text": "Design the presentation and visual aids", "trait_tag": "Visual-Design"},
            {"option_id": 1075, "option_text": "Present the findings to the class", "trait_tag": "Teaching-Ed"},
            {"option_id": 1076, "option_text": "Manage the timeline and task assignments", "trait_tag": "Admin-Skill"},
            {"option_id": 1077, "option_text": "Create digital tools or apps for data collection", "trait_tag": "Software-Dev"},
            {"option_id": 1078, "option_text": "Conduct experiments and lab work", "trait_tag": "Medical-Lab"},
            {"option_id": 1079, "option_text": "Do field research and site visits", "trait_tag": "Field-Research"},
            {"option_id": 1080, "option_text": "Handle the budget and resource allocation", "trait_tag": "Finance-Acct"}
        ]
    },
    {
        "question_id": 109,
        "question_text": "A typhoon warning is issued for your area. How do you prepare?",
        "category": "Situational - Typhoon Preparation",
        "options": [
            {"option_id": 1081, "option_text": "Prepare first aid kit and medical supplies", "trait_tag": "Patient-Care"},
            {"option_id": 1082, "option_text": "Charge devices and backup important files", "trait_tag": "Software-Dev"},
            {"option_id": 1083, "option_text": "Secure the house structure and check for weak points", "trait_tag": "Civil-Build"},
            {"option_id": 1084, "option_text": "Stock up on food and essential supplies", "trait_tag": "Hospitality-Svc"},
            {"option_id": 1085, "option_text": "Create evacuation plans and routes", "trait_tag": "Community-Serve"},
            {"option_id": 1086, "option_text": "Teach family members about safety protocols", "trait_tag": "Teaching-Ed"},
            {"option_id": 1087, "option_text": "Check emergency hotlines and communication plans", "trait_tag": "Technical-Skill"},
            {"option_id": 1088, "option_text": "Prepare flashlights and alternative power sources", "trait_tag": "Electrical-Power"},
            {"option_id": 1089, "option_text": "Protect plants and agricultural materials", "trait_tag": "Agri-Nature"},
            {"option_id": 1090, "option_text": "Calculate potential damage costs for insurance", "trait_tag": "Finance-Acct"}
        ]
    },
    {
        "question_id": 110,
        "question_text": "You're given the chance to shadow a professional for a day. Who would you choose?",
        "category": "Situational - Job Shadow",
        "options": [
            {"option_id": 1091, "option_text": "A doctor or nurse in a busy hospital", "trait_tag": "Patient-Care"},
            {"option_id": 1092, "option_text": "A software engineer at a tech company", "trait_tag": "Software-Dev"},
            {"option_id": 1093, "option_text": "An architect designing a new building", "trait_tag": "Spatial-Design"},
            {"option_id": 1094, "option_text": "A CEO running a successful company", "trait_tag": "Startup-Venture"},
            {"option_id": 1095, "option_text": "A film director or artist in a studio", "trait_tag": "Digital-Media"},
            {"option_id": 1096, "option_text": "A university professor teaching students", "trait_tag": "Teaching-Ed"},
            {"option_id": 1097, "option_text": "A detective solving criminal cases", "trait_tag": "Law-Enforce"},
            {"option_id": 1098, "option_text": "A marine biologist researching ocean life", "trait_tag": "Field-Research"},
            {"option_id": 1099, "option_text": "A ship captain on an international voyage", "trait_tag": "Maritime-Sea"},
            {"option_id": 1100, "option_text": "A physical therapist helping patients recover", "trait_tag": "Rehab-Therapy"}
        ]
    },
    {
        "question_id": 111,
        "question_text": "Your school website has been hacked. How would you help?",
        "category": "Situational - Cyber Attack",
        "options": [
            {"option_id": 1101, "option_text": "Identify the vulnerability and fix the security breach", "trait_tag": "Cyber-Defense"},
            {"option_id": 1102, "option_text": "Restore the website from backup systems", "trait_tag": "Software-Dev"},
            {"option_id": 1103, "option_text": "Investigate who was responsible and gather evidence", "trait_tag": "Law-Enforce"},
            {"option_id": 1104, "option_text": "Communicate with students about what happened", "trait_tag": "Teaching-Ed"},
            {"option_id": 1105, "option_text": "Calculate the damage and costs to fix it", "trait_tag": "Finance-Acct"},
            {"option_id": 1106, "option_text": "Redesign the website with better security", "trait_tag": "Visual-Design"},
            {"option_id": 1107, "option_text": "Create a report documenting the incident", "trait_tag": "Admin-Skill"},
            {"option_id": 1108, "option_text": "Train others on cybersecurity best practices", "trait_tag": "Technical-Skill"},
            {"option_id": 1109, "option_text": "Analyze data logs to understand the attack pattern", "trait_tag": "Data-Analytics"},
            {"option_id": 1110, "option_text": "Coordinate with the IT team on the response", "trait_tag": "Hardware-Systems"}
        ]
    },
    {
        "question_id": 112,
        "question_text": "A new shopping mall is opening in your town. What job would interest you there?",
        "category": "Situational - Mall Jobs",
        "options": [
            {"option_id": 1111, "option_text": "Clinic staff in the mall's medical center", "trait_tag": "Patient-Care"},
            {"option_id": 1112, "option_text": "IT support for the mall's technology systems", "trait_tag": "Software-Dev"},
            {"option_id": 1113, "option_text": "Facilities manager overseeing building operations", "trait_tag": "Civil-Build"},
            {"option_id": 1114, "option_text": "Store owner running my own business there", "trait_tag": "Startup-Venture"},
            {"option_id": 1115, "option_text": "Interior designer for store layouts", "trait_tag": "Spatial-Design"},
            {"option_id": 1116, "option_text": "Customer service training manager", "trait_tag": "Teaching-Ed"},
            {"option_id": 1117, "option_text": "Security officer ensuring safety", "trait_tag": "Law-Enforce"},
            {"option_id": 1118, "option_text": "Marketing staff promoting mall events", "trait_tag": "Marketing-Sales"},
            {"option_id": 1119, "option_text": "Restaurant manager in the food court", "trait_tag": "Hospitality-Svc"},
            {"option_id": 1120, "option_text": "Accountant managing finances for stores", "trait_tag": "Finance-Acct"}
        ]
    },
    {
        "question_id": 113,
        "question_text": "Your neighbor's pet is acting strangely and seems sick. What do you do?",
        "category": "Situational - Sick Pet",
        "options": [
            {"option_id": 1121, "option_text": "Check the pet's symptoms and suggest going to a vet", "trait_tag": "Patient-Care"},
            {"option_id": 1122, "option_text": "Search online for possible causes and treatments", "trait_tag": "Software-Dev"},
            {"option_id": 1123, "option_text": "Think about what in their environment could be causing it", "trait_tag": "Field-Research"},
            {"option_id": 1124, "option_text": "Offer to help pay for veterinary care", "trait_tag": "Finance-Acct"},
            {"option_id": 1125, "option_text": "Make the pet comfortable and provide comfort", "trait_tag": "Rehab-Therapy"},
            {"option_id": 1126, "option_text": "Explain to the neighbor about pet health care", "trait_tag": "Teaching-Ed"},
            {"option_id": 1127, "option_text": "Investigate if other neighborhood pets are affected", "trait_tag": "Lab-Research"},
            {"option_id": 1128, "option_text": "Contact animal rescue organizations for help", "trait_tag": "Community-Serve"},
            {"option_id": 1129, "option_text": "Prepare special food or medicine if needed", "trait_tag": "Hospitality-Svc"},
            {"option_id": 1130, "option_text": "Check if it might be something agricultural-related", "trait_tag": "Agri-Nature"}
        ]
    },
    {
        "question_id": 114,
        "question_text": "Your school wants to reduce its environmental impact. What initiative would you lead?",
        "category": "Situational - Environmental Initiative",
        "options": [
            {"option_id": 1131, "option_text": "Health education about environmental pollution effects", "trait_tag": "Patient-Care"},
            {"option_id": 1132, "option_text": "Develop an app to track the school's carbon footprint", "trait_tag": "Software-Dev"},
            {"option_id": 1133, "option_text": "Design eco-friendly building modifications", "trait_tag": "Civil-Build"},
            {"option_id": 1134, "option_text": "Create a recycling business that generates funds", "trait_tag": "Startup-Venture"},
            {"option_id": 1135, "option_text": "Design posters and campaigns for awareness", "trait_tag": "Visual-Design"},
            {"option_id": 1136, "option_text": "Teach students about sustainability and conservation", "trait_tag": "Teaching-Ed"},
            {"option_id": 1137, "option_text": "Conduct scientific research on local environmental issues", "trait_tag": "Field-Research"},
            {"option_id": 1138, "option_text": "Advocate for policy changes with school administration", "trait_tag": "Community-Serve"},
            {"option_id": 1139, "option_text": "Start a school garden and composting program", "trait_tag": "Agri-Nature"},
            {"option_id": 1140, "option_text": "Install solar panels or energy-efficient systems", "trait_tag": "Electrical-Power"}
        ]
    },
    {
        "question_id": 115,
        "question_text": "You find a wallet with a large amount of cash and no ID. What do you do?",
        "category": "Situational - Found Wallet",
        "options": [
            {"option_id": 1141, "option_text": "Turn it in to the nearest authority or police station", "trait_tag": "Law-Enforce"},
            {"option_id": 1142, "option_text": "Post about it on social media to find the owner", "trait_tag": "Digital-Media"},
            {"option_id": 1143, "option_text": "Count the money and document everything carefully", "trait_tag": "Finance-Acct"},
            {"option_id": 1144, "option_text": "Look for any clues inside about who owns it", "trait_tag": "Lab-Research"},
            {"option_id": 1145, "option_text": "Ask people in the area if they lost a wallet", "trait_tag": "People-Skill"},
            {"option_id": 1146, "option_text": "Teach others about honesty and integrity through this", "trait_tag": "Teaching-Ed"},
            {"option_id": 1147, "option_text": "Leave your contact info in case the owner returns", "trait_tag": "Admin-Skill"},
            {"option_id": 1148, "option_text": "Think about creating a lost-and-found system", "trait_tag": "Community-Serve"},
            {"option_id": 1149, "option_text": "Consider the emotional impact on the person who lost it", "trait_tag": "Rehab-Therapy"},
            {"option_id": 1150, "option_text": "Give it to the nearest establishment for safekeeping", "trait_tag": "Hospitality-Svc"}
        ]
    },
    {
        "question_id": 116,
        "question_text": "A factory near your town is causing pollution. How would you address this?",
        "category": "Situational - Factory Pollution",
        "options": [
            {"option_id": 1151, "option_text": "Study the health effects on nearby residents", "trait_tag": "Patient-Care"},
            {"option_id": 1152, "option_text": "Develop sensors to monitor pollution levels", "trait_tag": "Hardware-Systems"},
            {"option_id": 1153, "option_text": "Design better waste management systems for the factory", "trait_tag": "Industrial-Ops"},
            {"option_id": 1154, "option_text": "Calculate the economic impact of the pollution", "trait_tag": "Finance-Acct"},
            {"option_id": 1155, "option_text": "Create documentary or media content about the issue", "trait_tag": "Digital-Media"},
            {"option_id": 1156, "option_text": "Educate the community about their rights", "trait_tag": "Teaching-Ed"},
            {"option_id": 1157, "option_text": "File legal complaints and gather evidence", "trait_tag": "Law-Enforce"},
            {"option_id": 1158, "option_text": "Conduct scientific tests on water and air quality", "trait_tag": "Lab-Research"},
            {"option_id": 1159, "option_text": "Organize community protests and advocacy", "trait_tag": "Community-Serve"},
            {"option_id": 1160, "option_text": "Study the environmental damage to local ecosystems", "trait_tag": "Field-Research"}
        ]
    },
    {
        "question_id": 117,
        "question_text": "Your classmate is struggling financially and can't afford school supplies. How do you help?",
        "category": "Situational - Helping Classmate",
        "options": [
            {"option_id": 1161, "option_text": "Share your supplies and offer emotional support", "trait_tag": "Patient-Care"},
            {"option_id": 1162, "option_text": "Help them find online resources and free materials", "trait_tag": "Software-Dev"},
            {"option_id": 1163, "option_text": "Organize a donation drive at school", "trait_tag": "Community-Serve"},
            {"option_id": 1164, "option_text": "Help them budget and manage their money better", "trait_tag": "Finance-Acct"},
            {"option_id": 1165, "option_text": "Create study materials they can use for free", "trait_tag": "Visual-Design"},
            {"option_id": 1166, "option_text": "Tutor them so they can succeed without expensive materials", "trait_tag": "Teaching-Ed"},
            {"option_id": 1167, "option_text": "Connect them with school assistance programs", "trait_tag": "Admin-Skill"},
            {"option_id": 1168, "option_text": "Help them find a part-time job opportunity", "trait_tag": "Startup-Venture"},
            {"option_id": 1169, "option_text": "Advocate to school for more student financial aid", "trait_tag": "People-Skill"},
            {"option_id": 1170, "option_text": "Research scholarship opportunities for them", "trait_tag": "Lab-Research"}
        ]
    },
    {
        "question_id": 118,
        "question_text": "You're asked to plan your family reunion. What aspect would you focus on?",
        "category": "Situational - Family Reunion",
        "options": [
            {"option_id": 1171, "option_text": "Ensure everyone's health needs are accommodated", "trait_tag": "Patient-Care"},
            {"option_id": 1172, "option_text": "Create a digital invitation and photo slideshow", "trait_tag": "Digital-Media"},
            {"option_id": 1173, "option_text": "Choose and set up the perfect venue", "trait_tag": "Spatial-Design"},
            {"option_id": 1174, "option_text": "Manage the budget and collect contributions", "trait_tag": "Finance-Acct"},
            {"option_id": 1175, "option_text": "Design decorations and create a festive atmosphere", "trait_tag": "Visual-Design"},
            {"option_id": 1176, "option_text": "Plan educational activities and games for kids", "trait_tag": "Teaching-Ed"},
            {"option_id": 1177, "option_text": "Organize the program flow and event timeline", "trait_tag": "Admin-Skill"},
            {"option_id": 1178, "option_text": "Plan the food menu and catering", "trait_tag": "Hospitality-Svc"},
            {"option_id": 1179, "option_text": "Document family history and create a family tree", "trait_tag": "Lab-Research"},
            {"option_id": 1180, "option_text": "Handle transportation and logistics", "trait_tag": "Industrial-Ops"}
        ]
    },
    {
        "question_id": 119,
        "question_text": "Your town is experiencing a water shortage. What solution would you propose?",
        "category": "Situational - Water Shortage",
        "options": [
            {"option_id": 1181, "option_text": "Ensure clean drinking water reaches vulnerable people first", "trait_tag": "Patient-Care"},
            {"option_id": 1182, "option_text": "Develop a water tracking and distribution app", "trait_tag": "Software-Dev"},
            {"option_id": 1183, "option_text": "Design rainwater collection and storage systems", "trait_tag": "Civil-Build"},
            {"option_id": 1184, "option_text": "Calculate costs of different water solutions", "trait_tag": "Finance-Acct"},
            {"option_id": 1185, "option_text": "Create awareness campaigns about water conservation", "trait_tag": "Visual-Design"},
            {"option_id": 1186, "option_text": "Teach people how to conserve and recycle water", "trait_tag": "Teaching-Ed"},
            {"option_id": 1187, "option_text": "Research new water purification technologies", "trait_tag": "Lab-Research"},
            {"option_id": 1188, "option_text": "Coordinate with government for emergency water supply", "trait_tag": "Community-Serve"},
            {"option_id": 1189, "option_text": "Study sustainable agricultural water practices", "trait_tag": "Agri-Nature"},
            {"option_id": 1190, "option_text": "Design efficient water pumping systems", "trait_tag": "Mechanical-Design"}
        ]
    },
    {
        "question_id": 120,
        "question_text": "You have the opportunity to intern anywhere for a month. Where would you go?",
        "category": "Situational - Dream Internship",
        "options": [
            {"option_id": 1191, "option_text": "A major hospital or healthcare facility", "trait_tag": "Patient-Care"},
            {"option_id": 1192, "option_text": "A tech startup or software company", "trait_tag": "Software-Dev"},
            {"option_id": 1193, "option_text": "A construction company or architecture firm", "trait_tag": "Spatial-Design"},
            {"option_id": 1194, "option_text": "An investment bank or financial institution", "trait_tag": "Finance-Acct"},
            {"option_id": 1195, "option_text": "A film studio or creative agency", "trait_tag": "Digital-Media"},
            {"option_id": 1196, "option_text": "A school or educational organization", "trait_tag": "Teaching-Ed"},
            {"option_id": 1197, "option_text": "A law firm or government agency", "trait_tag": "Law-Enforce"},
            {"option_id": 1198, "option_text": "A research laboratory or university", "trait_tag": "Lab-Research"},
            {"option_id": 1199, "option_text": "A shipping company or port authority", "trait_tag": "Maritime-Sea"},
            {"option_id": 1200, "option_text": "A resort, hotel, or travel company", "trait_tag": "Hospitality-Svc"}
        ]
    },

    # ==================== DOMAIN-SPECIFIC ENTRY QUESTIONS (Q121-Q133) ====================
    # Each domain gets a UNIQUE opener that directly relates to that field
    # These replace the generic Q1/Q4 as entry points

    # --- TECHNOLOGY ENTRY ---
    {
        "question_id": 121,
        "question_text": "When you use your computer or phone, what do you enjoy doing the most?",
        "category": "Domain Entry - Technology",
        "options": [
            {"option_id": 1201, "option_text": "Building websites or coding small programs", "trait_tags": ["Web-Dev", "Software-Dev"]},
            {"option_id": 1202, "option_text": "Playing and analyzing video games", "trait_tags": ["Game-Dev", "Digital-Media"]},
            {"option_id": 1203, "option_text": "Setting up networks or fixing hardware issues", "trait_tags": ["Cloud-Systems", "Hardware-Systems"]},
            {"option_id": 1204, "option_text": "Analyzing data or making spreadsheets", "trait_tags": ["Data-Analytics", "AI-ML"]},
            {"option_id": 1205, "option_text": "Creating digital art or editing videos", "trait_tags": ["Digital-Media", "Animation-3D"]},
            {"option_id": 1206, "option_text": "Learning about hacking and online security", "trait_tags": ["Cyber-Defense", "Software-Dev"]},
            {"option_id": 1207, "option_text": "Developing mobile apps or chatbots", "trait_tags": ["Mobile-Dev", "AI-ML"]},
            {"option_id": 1208, "option_text": "Managing cloud servers or databases", "trait_tags": ["Cloud-Systems", "Data-Analytics"]},
            {"option_id": 1209, "option_text": "Automating tasks with scripts", "trait_tags": ["Software-Dev", "Data-Analytics"]},
            {"option_id": 1210, "option_text": "None of these interest me", "trait_tags": []}
        ]
    },
    # --- HEALTHCARE ENTRY ---
    {
        "question_id": 122,
        "question_text": "In a hospital setting, what would you most want to do?",
        "category": "Domain Entry - Healthcare",
        "options": [
            {"option_id": 1211, "option_text": "Directly care for patients at their bedside", "trait_tags": ["Patient-Care", "People-Skill"]},
            {"option_id": 1212, "option_text": "Analyze blood and tissue samples in the lab", "trait_tags": ["Medical-Lab", "Lab-Research"]},
            {"option_id": 1213, "option_text": "Help patients recover through physical exercises", "trait_tags": ["Rehab-Therapy", "Physical-Skill"]},
            {"option_id": 1214, "option_text": "Prepare and dispense medications", "trait_tags": ["Pharmacy", "Medical-Lab"]},
            {"option_id": 1215, "option_text": "Manage hospital records and health data", "trait_tags": ["Health-Admin", "Admin-Skill"]},
            {"option_id": 1216, "option_text": "Promote health programs for communities", "trait_tags": ["Public-Health", "Community-Serve"]},
            {"option_id": 1217, "option_text": "Plan nutritious diets for patients", "trait_tags": ["Nutrition-Diet", "Patient-Care"]},
            {"option_id": 1218, "option_text": "Help people with speech or mental health issues", "trait_tags": ["Rehab-Therapy", "Counseling"]},
            {"option_id": 1219, "option_text": "Operate medical imaging equipment (X-ray, MRI)", "trait_tags": ["Medical-Lab", "Technical-Skill"]},
            {"option_id": 1220, "option_text": "None of these interest me", "trait_tags": []}
        ]
    },
    # --- ENGINEERING ENTRY ---
    {
        "question_id": 123,
        "question_text": "When you see a construction site or factory, what interests you most?",
        "category": "Domain Entry - Engineering",
        "options": [
            {"option_id": 1221, "option_text": "How buildings and bridges are designed to be strong", "trait_tags": ["Civil-Build", "Spatial-Design"]},
            {"option_id": 1222, "option_text": "The machines and engines that power everything", "trait_tags": ["Mechanical-Design", "Industrial-Ops"]},
            {"option_id": 1223, "option_text": "The electrical systems and power grids", "trait_tags": ["Electrical-Power", "Hardware-Systems"]},
            {"option_id": 1224, "option_text": "How factories optimize their production process", "trait_tags": ["Industrial-Ops", "Mechanical-Design"]},
            {"option_id": 1225, "option_text": "The environmental impact and sustainability", "trait_tags": ["Environmental-Eng", "Environmental-Sci"]},
            {"option_id": 1226, "option_text": "The mapping and surveying of the land", "trait_tags": ["Civil-Build", "Field-Research"]},
            {"option_id": 1227, "option_text": "The architecture and visual design of the buildings", "trait_tags": ["Spatial-Design", "Visual-Design"]},
            {"option_id": 1228, "option_text": "How aircraft and vehicles are engineered", "trait_tags": ["Mechanical-Design", "Hardware-Systems"]},
            {"option_id": 1229, "option_text": "The electronics and embedded computer systems", "trait_tags": ["Hardware-Systems", "Software-Dev"]},
            {"option_id": 1230, "option_text": "None of these interest me", "trait_tags": []}
        ]
    },
    # --- BUSINESS ENTRY ---
    {
        "question_id": 124,
        "question_text": "When you think about money and business, what excites you most?",
        "category": "Domain Entry - Business",
        "options": [
            {"option_id": 1231, "option_text": "Managing budgets and analyzing financial reports", "trait_tags": ["Finance-Acct", "Analytical-Skill"]},
            {"option_id": 1232, "option_text": "Creating ads and marketing campaigns", "trait_tags": ["Marketing-Sales", "Creative-Skill"]},
            {"option_id": 1233, "option_text": "Starting my own business from scratch", "trait_tags": ["Startup-Venture", "Marketing-Sales"]},
            {"option_id": 1234, "option_text": "Hiring and managing employees", "trait_tags": ["HR-Management", "People-Skill"]},
            {"option_id": 1235, "option_text": "Trading stocks and making investments", "trait_tags": ["Finance-Acct", "Startup-Venture"]},
            {"option_id": 1236, "option_text": "Selling products and negotiating deals", "trait_tags": ["Marketing-Sales", "People-Skill"]},
            {"option_id": 1237, "option_text": "Managing real estate properties", "trait_tags": ["Marketing-Sales", "Admin-Skill"]},
            {"option_id": 1238, "option_text": "Running logistics and supply chains", "trait_tags": ["Industrial-Ops", "Admin-Skill"]},
            {"option_id": 1239, "option_text": "Analyzing economic trends and policies", "trait_tags": ["Finance-Acct", "Analytical-Skill"]},
            {"option_id": 1240, "option_text": "None of these interest me", "trait_tags": []}
        ]
    },
    # --- CREATIVE ENTRY ---
    {
        "question_id": 125,
        "question_text": "Which form of creative expression speaks to you the most?",
        "category": "Domain Entry - Creative",
        "options": [
            {"option_id": 1241, "option_text": "Drawing, painting, or graphic design", "trait_tags": ["Visual-Design", "Creative-Skill"]},
            {"option_id": 1242, "option_text": "3D modeling and animation", "trait_tags": ["Animation-3D", "Digital-Media"]},
            {"option_id": 1243, "option_text": "Making short films or video content", "trait_tags": ["Film-Broadcast", "Digital-Media"]},
            {"option_id": 1244, "option_text": "Acting, dancing, or performing on stage", "trait_tags": ["Performing-Arts", "People-Skill"]},
            {"option_id": 1245, "option_text": "Music production and sound design", "trait_tags": ["Performing-Arts", "Digital-Media"]},
            {"option_id": 1246, "option_text": "Interior decorating or space design", "trait_tags": ["Spatial-Design", "Creative-Skill"]},
            {"option_id": 1247, "option_text": "Fashion design and clothing", "trait_tags": ["Spatial-Design", "Visual-Design"]},
            {"option_id": 1248, "option_text": "Photography and visual storytelling", "trait_tags": ["Visual-Design", "Film-Broadcast"]},
            {"option_id": 1249, "option_text": "Game design and interactive media", "trait_tags": ["Game-Dev", "Animation-3D"]},
            {"option_id": 1250, "option_text": "None of these interest me", "trait_tags": []}
        ]
    },
    # --- EDUCATION ENTRY ---
    {
        "question_id": 126,
        "question_text": "What draws you most to sharing knowledge with others?",
        "category": "Domain Entry - Education",
        "options": [
            {"option_id": 1251, "option_text": "Teaching young children how to read and write", "trait_tags": ["Teaching-Ed", "People-Skill"]},
            {"option_id": 1252, "option_text": "Coaching students through difficult subjects", "trait_tags": ["Teaching-Ed", "Analytical-Skill"]},
            {"option_id": 1253, "option_text": "Guiding students with personal and career problems", "trait_tags": ["Counseling", "People-Skill"]},
            {"option_id": 1254, "option_text": "Training athletes and coaching sports teams", "trait_tags": ["Sports-Ed", "Physical-Skill"]},
            {"option_id": 1255, "option_text": "Teaching technical and vocational skills", "trait_tags": ["Teaching-Ed", "Technical-Skill"]},
            {"option_id": 1256, "option_text": "Helping special needs children learn", "trait_tags": ["Teaching-Ed", "Counseling"]},
            {"option_id": 1257, "option_text": "Organizing library resources and research tools", "trait_tags": ["Teaching-Ed", "Admin-Skill"]},
            {"option_id": 1258, "option_text": "Developing educational programs and curricula", "trait_tags": ["Teaching-Ed", "Creative-Skill"]},
            {"option_id": 1259, "option_text": "Mentoring youth in the community", "trait_tags": ["Community-Serve", "People-Skill"]},
            {"option_id": 1260, "option_text": "None of these interest me", "trait_tags": []}
        ]
    },
    # --- PUBLIC SERVICE ENTRY ---
    {
        "question_id": 127,
        "question_text": "How would you most like to serve your community?",
        "category": "Domain Entry - Public Service",
        "options": [
            {"option_id": 1261, "option_text": "Protecting people as a police officer or detective", "trait_tags": ["Law-Enforce", "Physical-Skill"]},
            {"option_id": 1262, "option_text": "Fighting for justice as a lawyer", "trait_tags": ["Legal-Practice", "Analytical-Skill"]},
            {"option_id": 1263, "option_text": "Analyzing forensic evidence at crime scenes", "trait_tags": ["Forensic-Sci", "Lab-Research"]},
            {"option_id": 1264, "option_text": "Helping families through social work", "trait_tags": ["Social-Work", "People-Skill"]},
            {"option_id": 1265, "option_text": "Working in government to create public policy", "trait_tags": ["Community-Serve", "Admin-Skill"]},
            {"option_id": 1266, "option_text": "Organizing community development programs", "trait_tags": ["Community-Serve", "Social-Work"]},
            {"option_id": 1267, "option_text": "Advocating for human rights and social justice", "trait_tags": ["Legal-Practice", "Community-Serve"]},
            {"option_id": 1268, "option_text": "Serving as a diplomat or in international relations", "trait_tags": ["Community-Serve", "People-Skill"]},
            {"option_id": 1269, "option_text": "Managing disaster relief and emergency response", "trait_tags": ["Community-Serve", "Physical-Skill"]},
            {"option_id": 1270, "option_text": "None of these interest me", "trait_tags": []}
        ]
    },
    # --- SCIENCE ENTRY ---
    {
        "question_id": 128,
        "question_text": "What kind of scientific discovery excites you the most?",
        "category": "Domain Entry - Science",
        "options": [
            {"option_id": 1271, "option_text": "Finding a cure for diseases in a laboratory", "trait_tags": ["Lab-Research", "Medical-Lab"]},
            {"option_id": 1272, "option_text": "Discovering new species in the wild", "trait_tags": ["Field-Research", "Environmental-Sci"]},
            {"option_id": 1273, "option_text": "Developing new food products and preserving food safely", "trait_tags": ["Food-Science", "Lab-Research"]},
            {"option_id": 1274, "option_text": "Analyzing crime scene evidence in a lab", "trait_tags": ["Forensic-Sci", "Analytical-Skill"]},
            {"option_id": 1275, "option_text": "Studying climate change and protecting the environment", "trait_tags": ["Environmental-Sci", "Field-Research"]},
            {"option_id": 1276, "option_text": "Exploring the ocean floor and marine life", "trait_tags": ["Field-Research", "Physical-Skill"]},
            {"option_id": 1277, "option_text": "Inventing new materials through chemistry", "trait_tags": ["Lab-Research", "Analytical-Skill"]},
            {"option_id": 1278, "option_text": "Understanding the universe through physics", "trait_tags": ["Lab-Research", "Analytical-Skill"]},
            {"option_id": 1279, "option_text": "Using statistics and math to solve real-world problems", "trait_tags": ["Data-Analytics", "Analytical-Skill"]},
            {"option_id": 1280, "option_text": "None of these interest me", "trait_tags": []}
        ]
    },
    # --- AGRICULTURE ENTRY ---
    {
        "question_id": 129,
        "question_text": "What aspect of nature and farming interests you most?",
        "category": "Domain Entry - Agriculture",
        "options": [
            {"option_id": 1281, "option_text": "Growing crops and managing farmland", "trait_tags": ["Agri-Nature", "Physical-Skill"]},
            {"option_id": 1282, "option_text": "Raising animals and livestock", "trait_tags": ["Agri-Nature", "Field-Research"]},
            {"option_id": 1283, "option_text": "Protecting forests and natural resources", "trait_tags": ["Agri-Nature", "Environmental-Sci"]},
            {"option_id": 1284, "option_text": "Fish farming and aquaculture", "trait_tags": ["Agri-Nature", "Maritime-Sea"]},
            {"option_id": 1285, "option_text": "Developing agricultural technology", "trait_tags": ["Agri-Nature", "Technical-Skill"]},
            {"option_id": 1286, "option_text": "Soil science and land management", "trait_tags": ["Agri-Nature", "Lab-Research"]},
            {"option_id": 1287, "option_text": "Agricultural business and farm marketing", "trait_tags": ["Agri-Nature", "Startup-Venture"]},
            {"option_id": 1288, "option_text": "Studying plant genetics and breeding", "trait_tags": ["Agri-Nature", "Lab-Research"]},
            {"option_id": 1289, "option_text": "None of these interest me", "trait_tags": []}
        ]
    },
    # --- MARITIME ENTRY ---
    {
        "question_id": 130,
        "question_text": "What draws you to the sea and maritime industry?",
        "category": "Domain Entry - Maritime",
        "options": [
            {"option_id": 1291, "option_text": "Navigating ships across the ocean", "trait_tags": ["Maritime-Sea", "Physical-Skill"]},
            {"option_id": 1292, "option_text": "Maintaining and repairing ship engines", "trait_tags": ["Maritime-Sea", "Mechanical-Design"]},
            {"option_id": 1293, "option_text": "Working at a seaport managing cargo", "trait_tags": ["Maritime-Sea", "Admin-Skill"]},
            {"option_id": 1294, "option_text": "Studying marine ecosystems and biology", "trait_tags": ["Field-Research", "Environmental-Sci"]},
            {"option_id": 1295, "option_text": "Building and designing ships or boats", "trait_tags": ["Maritime-Sea", "Mechanical-Design"]},
            {"option_id": 1296, "option_text": "The adventure of traveling to different countries", "trait_tags": ["Maritime-Sea", "Tourism-Travel"]},
            {"option_id": 1297, "option_text": "Fishing industry and aquatic resources", "trait_tags": ["Maritime-Sea", "Agri-Nature"]},
            {"option_id": 1298, "option_text": "None of these interest me", "trait_tags": []}
        ]
    },
    # --- HOSPITALITY ENTRY ---
    {
        "question_id": 131,
        "question_text": "What do you enjoy most about serving and hosting people?",
        "category": "Domain Entry - Hospitality",
        "options": [
            {"option_id": 1301, "option_text": "Managing a hotel and making guests feel welcome", "trait_tags": ["Hospitality-Svc", "People-Skill"]},
            {"option_id": 1302, "option_text": "Planning travel itineraries and tour packages", "trait_tags": ["Tourism-Travel", "Marketing-Sales"]},
            {"option_id": 1303, "option_text": "Cooking and creating new dishes", "trait_tags": ["Culinary-Arts", "Creative-Skill"]},
            {"option_id": 1304, "option_text": "Organizing events and conferences", "trait_tags": ["Hospitality-Svc", "Admin-Skill"]},
            {"option_id": 1305, "option_text": "Running a restaurant or food business", "trait_tags": ["Culinary-Arts", "Startup-Venture"]},
            {"option_id": 1306, "option_text": "Being a tour guide and sharing culture", "trait_tags": ["Tourism-Travel", "People-Skill"]},
            {"option_id": 1307, "option_text": "Managing a resort or spa", "trait_tags": ["Hospitality-Svc", "Admin-Skill"]},
            {"option_id": 1308, "option_text": "Food photography and culinary content creation", "trait_tags": ["Culinary-Arts", "Digital-Media"]},
            {"option_id": 1309, "option_text": "None of these interest me", "trait_tags": []}
        ]
    },
    # --- PHYSICAL/SPORTS ENTRY ---
    {
        "question_id": 132,
        "question_text": "What physical activity or career excites you most?",
        "category": "Domain Entry - Physical",
        "options": [
            {"option_id": 1311, "option_text": "Coaching athletes and training sports teams", "trait_tags": ["Sports-Ed", "Teaching-Ed"]},
            {"option_id": 1312, "option_text": "Helping injured athletes recover", "trait_tags": ["Rehab-Therapy", "Sports-Ed"]},
            {"option_id": 1313, "option_text": "Working as a fitness trainer", "trait_tags": ["Physical-Skill", "Sports-Ed"]},
            {"option_id": 1314, "option_text": "Becoming a professional athlete", "trait_tags": ["Physical-Skill", "Sports-Ed"]},
            {"option_id": 1315, "option_text": "Sports management and event organizing", "trait_tags": ["Sports-Ed", "Admin-Skill"]},
            {"option_id": 1316, "option_text": "Outdoor adventure sports and recreation", "trait_tags": ["Physical-Skill", "Tourism-Travel"]},
            {"option_id": 1317, "option_text": "Military or law enforcement fitness", "trait_tags": ["Physical-Skill", "Law-Enforce"]},
            {"option_id": 1318, "option_text": "None of these interest me", "trait_tags": []}
        ]
    },
    # --- SOCIAL/HUMANITIES ENTRY ---
    {
        "question_id": 133,
        "question_text": "How do you most enjoy connecting with and understanding people?",
        "category": "Domain Entry - Social",
        "options": [
            {"option_id": 1321, "option_text": "Counseling people through emotional problems", "trait_tags": ["Counseling", "People-Skill"]},
            {"option_id": 1322, "option_text": "Writing stories and creative content", "trait_tags": ["Creative-Skill", "Film-Broadcast"]},
            {"option_id": 1323, "option_text": "Studying how societies and cultures work", "trait_tags": ["Community-Serve", "Analytical-Skill"]},
            {"option_id": 1324, "option_text": "Helping underprivileged communities", "trait_tags": ["Social-Work", "Community-Serve"]},
            {"option_id": 1325, "option_text": "Researching psychology and human behavior", "trait_tags": ["Counseling", "Analytical-Skill"]},
            {"option_id": 1326, "option_text": "News reporting and investigative journalism", "trait_tags": ["Film-Broadcast", "Analytical-Skill"]},
            {"option_id": 1327, "option_text": "Understanding languages and communication", "trait_tags": ["Teaching-Ed", "People-Skill"]},
            {"option_id": 1328, "option_text": "Political activism and civic engagement", "trait_tags": ["Community-Serve", "Legal-Practice"]},
            {"option_id": 1329, "option_text": "None of these interest me", "trait_tags": []}
        ]
    },

    # ==================== EXPANDED SITUATIONAL QUESTIONS (Q134-Q200+) ====================
    # Multi-trait options, deeper domain coverage, Philippine context

    # --- TECHNOLOGY SITUATIONAL (Q134-Q148) ---
    {
        "question_id": 134,
        "question_text": "Your school asks you to build their new website. What excites you most about the project?",
        "category": "Situational - Web Development",
        "options": [
            {"option_id": 1341, "option_text": "Designing the visual layout and user interface", "trait_tags": ["Web-Dev", "Visual-Design"]},
            {"option_id": 1342, "option_text": "Writing the backend code and database", "trait_tags": ["Web-Dev", "Software-Dev"]},
            {"option_id": 1343, "option_text": "Setting up the server and hosting", "trait_tags": ["Cloud-Systems", "Web-Dev"]},
            {"option_id": 1344, "option_text": "Making sure it's secure from hackers", "trait_tags": ["Cyber-Defense", "Web-Dev"]},
            {"option_id": 1345, "option_text": "Adding interactive features and animations", "trait_tags": ["Web-Dev", "Animation-3D"]},
            {"option_id": 1346, "option_text": "Testing it on different devices and browsers", "trait_tags": ["Mobile-Dev", "Web-Dev"]},
            {"option_id": 1347, "option_text": "Analyzing user data to improve the site", "trait_tags": ["Data-Analytics", "Web-Dev"]},
            {"option_id": 1348, "option_text": "Managing the project team and timeline", "trait_tags": ["Admin-Skill", "Software-Dev"]}
        ]
    },
    {
        "question_id": 135,
        "question_text": "You're part of a hackathon team. Which project would you choose?",
        "category": "Situational - Tech Competition",
        "options": [
            {"option_id": 1351, "option_text": "An AI chatbot that helps students study", "trait_tags": ["AI-ML", "Software-Dev"]},
            {"option_id": 1352, "option_text": "A mobile app for local businesses", "trait_tags": ["Mobile-Dev", "Startup-Venture"]},
            {"option_id": 1353, "option_text": "A cybersecurity tool to detect phishing", "trait_tags": ["Cyber-Defense", "Software-Dev"]},
            {"option_id": 1354, "option_text": "A data dashboard tracking COVID cases", "trait_tags": ["Data-Analytics", "Public-Health"]},
            {"option_id": 1355, "option_text": "A VR game set in Philippine history", "trait_tags": ["Game-Dev", "Animation-3D"]},
            {"option_id": 1356, "option_text": "An IoT system for smart farming", "trait_tags": ["Hardware-Systems", "Agri-Nature"]},
            {"option_id": 1357, "option_text": "A cloud platform for school management", "trait_tags": ["Cloud-Systems", "Admin-Skill"]},
            {"option_id": 1358, "option_text": "A machine learning model to predict floods", "trait_tags": ["AI-ML", "Environmental-Sci"]}
        ]
    },
    {
        "question_id": 136,
        "question_text": "If you could create any app, what would it do?",
        "category": "Situational - App Development",
        "options": [
            {"option_id": 1361, "option_text": "Help people find the best doctors nearby", "trait_tags": ["Mobile-Dev", "Patient-Care"]},
            {"option_id": 1362, "option_text": "Track personal finances and budgets", "trait_tags": ["Mobile-Dev", "Finance-Acct"]},
            {"option_id": 1363, "option_text": "Connect local farmers to buyers directly", "trait_tags": ["Mobile-Dev", "Agri-Nature"]},
            {"option_id": 1364, "option_text": "An AI tutor that adapts to student learning", "trait_tags": ["AI-ML", "Teaching-Ed"]},
            {"option_id": 1365, "option_text": "A social platform for Filipino artists", "trait_tags": ["Mobile-Dev", "Visual-Design"]},
            {"option_id": 1366, "option_text": "A fitness tracker with workout plans", "trait_tags": ["Mobile-Dev", "Sports-Ed"]},
            {"option_id": 1367, "option_text": "A disaster alert system using real-time data", "trait_tags": ["Mobile-Dev", "Environmental-Sci"]},
            {"option_id": 1368, "option_text": "A game that teaches children about science", "trait_tags": ["Game-Dev", "Teaching-Ed"]}
        ]
    },
    {
        "question_id": 137,
        "question_text": "Your company is hit by a ransomware attack. What's your role in the response?",
        "category": "Situational - Cybersecurity",
        "options": [
            {"option_id": 1371, "option_text": "Leading the technical incident response team", "trait_tags": ["Cyber-Defense", "Cloud-Systems"]},
            {"option_id": 1372, "option_text": "Analyzing the malware to find its source", "trait_tags": ["Cyber-Defense", "Forensic-Sci"]},
            {"option_id": 1373, "option_text": "Restoring systems from backup servers", "trait_tags": ["Cloud-Systems", "Software-Dev"]},
            {"option_id": 1374, "option_text": "Communicating with stakeholders about the breach", "trait_tags": ["Admin-Skill", "People-Skill"]},
            {"option_id": 1375, "option_text": "Working with law enforcement to catch the hackers", "trait_tags": ["Cyber-Defense", "Law-Enforce"]},
            {"option_id": 1376, "option_text": "Training employees to prevent future attacks", "trait_tags": ["Teaching-Ed", "Cyber-Defense"]},
            {"option_id": 1377, "option_text": "Developing better security protocols", "trait_tags": ["Cyber-Defense", "Software-Dev"]},
            {"option_id": 1378, "option_text": "Assessing the financial damage and filing insurance", "trait_tags": ["Finance-Acct", "Admin-Skill"]}
        ]
    },
    {
        "question_id": 138,
        "question_text": "You're asked to create an AI system for your school. What would it do?",
        "category": "Situational - AI/ML",
        "options": [
            {"option_id": 1381, "option_text": "Predict which students need extra tutoring", "trait_tags": ["AI-ML", "Teaching-Ed"]},
            {"option_id": 1382, "option_text": "Automate grading of essays and exams", "trait_tags": ["AI-ML", "Data-Analytics"]},
            {"option_id": 1383, "option_text": "Detect cheating in online exams", "trait_tags": ["AI-ML", "Cyber-Defense"]},
            {"option_id": 1384, "option_text": "Generate personalized study materials", "trait_tags": ["AI-ML", "Teaching-Ed"]},
            {"option_id": 1385, "option_text": "Analyze campus safety through security cameras", "trait_tags": ["AI-ML", "Law-Enforce"]},
            {"option_id": 1386, "option_text": "Optimize class schedules and room assignments", "trait_tags": ["AI-ML", "Admin-Skill"]},
            {"option_id": 1387, "option_text": "Create a virtual campus tour using AR", "trait_tags": ["AI-ML", "Animation-3D"]},
            {"option_id": 1388, "option_text": "Monitor campus energy usage to save electricity", "trait_tags": ["AI-ML", "Environmental-Eng"]}
        ]
    },
    {
        "question_id": 139,
        "question_text": "A friend asks you to help make their indie video game. What role do you want?",
        "category": "Situational - Game Development",
        "options": [
            {"option_id": 1391, "option_text": "Programming the game mechanics and physics", "trait_tags": ["Game-Dev", "Software-Dev"]},
            {"option_id": 1392, "option_text": "Creating the 3D character models and environments", "trait_tags": ["Animation-3D", "Visual-Design"]},
            {"option_id": 1393, "option_text": "Writing the storyline and dialogue", "trait_tags": ["Creative-Skill", "Game-Dev"]},
            {"option_id": 1394, "option_text": "Composing the music and sound effects", "trait_tags": ["Performing-Arts", "Digital-Media"]},
            {"option_id": 1395, "option_text": "Testing and finding bugs", "trait_tags": ["Software-Dev", "Analytical-Skill"]},
            {"option_id": 1396, "option_text": "Marketing and publishing the game online", "trait_tags": ["Marketing-Sales", "Digital-Media"]},
            {"option_id": 1397, "option_text": "Designing the UI and menu systems", "trait_tags": ["Web-Dev", "Visual-Design"]},
            {"option_id": 1398, "option_text": "Managing the project schedule and budget", "trait_tags": ["Admin-Skill", "Startup-Venture"]}
        ]
    },
    {
        "question_id": 140,
        "question_text": "Your barangay wants a tech solution for a local problem. What would you build?",
        "category": "Situational - Community Tech",
        "options": [
            {"option_id": 1401, "option_text": "A database to track residents and health records", "trait_tags": ["Software-Dev", "Public-Health"]},
            {"option_id": 1402, "option_text": "A CCTV monitoring system with smart alerts", "trait_tags": ["Hardware-Systems", "Law-Enforce"]},
            {"option_id": 1403, "option_text": "A Wi-Fi hotspot for students without internet", "trait_tags": ["Cloud-Systems", "Community-Serve"]},
            {"option_id": 1404, "option_text": "An app for reporting emergencies and crimes", "trait_tags": ["Mobile-Dev", "Law-Enforce"]},
            {"option_id": 1405, "option_text": "A system to track garbage collection schedules", "trait_tags": ["Software-Dev", "Environmental-Eng"]},
            {"option_id": 1406, "option_text": "A digital marketplace for local vendors", "trait_tags": ["Web-Dev", "Marketing-Sales"]},
            {"option_id": 1407, "option_text": "An SMS alert system for typhoon warnings", "trait_tags": ["Mobile-Dev", "Environmental-Sci"]},
            {"option_id": 1408, "option_text": "None — I'd focus on non-tech solutions", "trait_tags": ["Community-Serve", "People-Skill"]}
        ]
    },

    # --- HEALTHCARE SITUATIONAL (Q141-Q152) ---
    {
        "question_id": 141,
        "question_text": "A typhoon hits your province. As a healthcare worker, what's your priority?",
        "category": "Situational - Disaster Healthcare",
        "options": [
            {"option_id": 1411, "option_text": "Treating injured victims at the evacuation center", "trait_tags": ["Patient-Care", "Physical-Skill"]},
            {"option_id": 1412, "option_text": "Setting up a temporary pharmacy for medicine distribution", "trait_tags": ["Pharmacy", "Public-Health"]},
            {"option_id": 1413, "option_text": "Running water and food quality tests", "trait_tags": ["Medical-Lab", "Food-Science"]},
            {"option_id": 1414, "option_text": "Organizing mental health support for survivors", "trait_tags": ["Counseling", "Rehab-Therapy"]},
            {"option_id": 1415, "option_text": "Coordinating health teams and supply logistics", "trait_tags": ["Health-Admin", "Admin-Skill"]},
            {"option_id": 1416, "option_text": "Providing nutritional support and meal planning", "trait_tags": ["Nutrition-Diet", "Public-Health"]},
            {"option_id": 1417, "option_text": "Helping injured people with physical rehabilitation", "trait_tags": ["Rehab-Therapy", "Physical-Skill"]},
            {"option_id": 1418, "option_text": "Preventing disease outbreaks through sanitation", "trait_tags": ["Public-Health", "Environmental-Sci"]}
        ]
    },
    {
        "question_id": 142,
        "question_text": "A patient comes in with an unknown illness. What would you want to do?",
        "category": "Situational - Medical Mystery",
        "options": [
            {"option_id": 1421, "option_text": "Take their vital signs and comfort them", "trait_tags": ["Patient-Care", "People-Skill"]},
            {"option_id": 1422, "option_text": "Run lab tests on their blood and tissue samples", "trait_tags": ["Medical-Lab", "Lab-Research"]},
            {"option_id": 1423, "option_text": "Research the symptoms and possible diseases", "trait_tags": ["Lab-Research", "Analytical-Skill"]},
            {"option_id": 1424, "option_text": "Check if the right medications are available", "trait_tags": ["Pharmacy", "Medical-Lab"]},
            {"option_id": 1425, "option_text": "Operate the imaging machines for diagnosis", "trait_tags": ["Medical-Lab", "Technical-Skill"]},
            {"option_id": 1426, "option_text": "Track if others in the community have the same illness", "trait_tags": ["Public-Health", "Data-Analytics"]},
            {"option_id": 1427, "option_text": "Update the patient's medical records accurately", "trait_tags": ["Health-Admin", "Admin-Skill"]},
            {"option_id": 1428, "option_text": "Call a team meeting to discuss the case", "trait_tags": ["People-Skill", "Analytical-Skill"]}
        ]
    },
    {
        "question_id": 143,
        "question_text": "Your barangay health center needs improvements. What would you focus on?",
        "category": "Situational - Community Health",
        "options": [
            {"option_id": 1431, "option_text": "Training midwives for safer childbirth", "trait_tags": ["Patient-Care", "Teaching-Ed"]},
            {"option_id": 1432, "option_text": "Adding a small lab for basic diagnostics", "trait_tags": ["Medical-Lab", "Lab-Research"]},
            {"option_id": 1433, "option_text": "Starting a vaccination and immunization drive", "trait_tags": ["Public-Health", "Community-Serve"]},
            {"option_id": 1434, "option_text": "Setting up a rehabilitation room for PT", "trait_tags": ["Rehab-Therapy", "Physical-Skill"]},
            {"option_id": 1435, "option_text": "Creating a nutrition program for malnourished children", "trait_tags": ["Nutrition-Diet", "Public-Health"]},
            {"option_id": 1436, "option_text": "Digitalizing patient records for better tracking", "trait_tags": ["Health-Admin", "Software-Dev"]},
            {"option_id": 1437, "option_text": "Adding mental health counseling services", "trait_tags": ["Counseling", "People-Skill"]},
            {"option_id": 1438, "option_text": "Stocking essential medicines properly", "trait_tags": ["Pharmacy", "Admin-Skill"]}
        ]
    },
    {
        "question_id": 144,
        "question_text": "At a health fair, which booth would you volunteer at?",
        "category": "Situational - Health Fair",
        "options": [
            {"option_id": 1441, "option_text": "Free blood pressure and sugar level testing", "trait_tags": ["Patient-Care", "Medical-Lab"]},
            {"option_id": 1442, "option_text": "Nutrition advice and healthy cooking demos", "trait_tags": ["Nutrition-Diet", "Culinary-Arts"]},
            {"option_id": 1443, "option_text": "Physical fitness testing and exercise tips", "trait_tags": ["Sports-Ed", "Rehab-Therapy"]},
            {"option_id": 1444, "option_text": "Mental health awareness and stress management", "trait_tags": ["Counseling", "People-Skill"]},
            {"option_id": 1445, "option_text": "Free eye exams and vision screening", "trait_tags": ["Medical-Lab", "Patient-Care"]},
            {"option_id": 1446, "option_text": "First aid training demonstrations", "trait_tags": ["Patient-Care", "Teaching-Ed"]},
            {"option_id": 1447, "option_text": "Distributing medicine and explaining dosages", "trait_tags": ["Pharmacy", "People-Skill"]},
            {"option_id": 1448, "option_text": "Organizing the event logistics and schedule", "trait_tags": ["Admin-Skill", "Health-Admin"]}
        ]
    },

    # --- ENGINEERING SITUATIONAL (Q145-Q155) ---
    {
        "question_id": 145,
        "question_text": "Your city needs a new bridge. What aspect of the project would you handle?",
        "category": "Situational - Bridge Project",
        "options": [
            {"option_id": 1451, "option_text": "Designing the structural framework", "trait_tags": ["Civil-Build", "Analytical-Skill"]},
            {"option_id": 1452, "option_text": "Planning the electrical and lighting systems", "trait_tags": ["Electrical-Power", "Civil-Build"]},
            {"option_id": 1453, "option_text": "Setting up the construction machinery", "trait_tags": ["Mechanical-Design", "Physical-Skill"]},
            {"option_id": 1454, "option_text": "Assessing environmental impact of the bridge", "trait_tags": ["Environmental-Eng", "Environmental-Sci"]},
            {"option_id": 1455, "option_text": "Surveying and mapping the terrain", "trait_tags": ["Civil-Build", "Field-Research"]},
            {"option_id": 1456, "option_text": "Making the bridge aesthetically beautiful", "trait_tags": ["Spatial-Design", "Visual-Design"]},
            {"option_id": 1457, "option_text": "Managing the construction timeline and budget", "trait_tags": ["Industrial-Ops", "Admin-Skill"]},
            {"option_id": 1458, "option_text": "Installing smart sensors for structural monitoring", "trait_tags": ["Hardware-Systems", "Civil-Build"]}
        ]
    },
    {
        "question_id": 146,
        "question_text": "A factory manager asks you to improve production efficiency. What's your approach?",
        "category": "Situational - Factory Optimization",
        "options": [
            {"option_id": 1461, "option_text": "Redesigning the assembly line layout", "trait_tags": ["Industrial-Ops", "Mechanical-Design"]},
            {"option_id": 1462, "option_text": "Automating processes with robotics", "trait_tags": ["Mechanical-Design", "Software-Dev"]},
            {"option_id": 1463, "option_text": "Upgrading the electrical power systems", "trait_tags": ["Electrical-Power", "Technical-Skill"]},
            {"option_id": 1464, "option_text": "Analyzing data to find bottlenecks", "trait_tags": ["Industrial-Ops", "Data-Analytics"]},
            {"option_id": 1465, "option_text": "Reducing waste and environmental impact", "trait_tags": ["Environmental-Eng", "Industrial-Ops"]},
            {"option_id": 1466, "option_text": "Training workers on new equipment", "trait_tags": ["Teaching-Ed", "Industrial-Ops"]},
            {"option_id": 1467, "option_text": "Building custom machines for specific tasks", "trait_tags": ["Mechanical-Design", "Hardware-Systems"]},
            {"option_id": 1468, "option_text": "Implementing quality control systems", "trait_tags": ["Industrial-Ops", "Analytical-Skill"]}
        ]
    },
    {
        "question_id": 147,
        "question_text": "An earthquake damaged several buildings in your area. What would you inspect first?",
        "category": "Situational - Structural Assessment",
        "options": [
            {"option_id": 1471, "option_text": "The structural integrity of the foundations", "trait_tags": ["Civil-Build", "Analytical-Skill"]},
            {"option_id": 1472, "option_text": "The electrical wiring and fire hazards", "trait_tags": ["Electrical-Power", "Technical-Skill"]},
            {"option_id": 1473, "option_text": "The water and plumbing systems", "trait_tags": ["Mechanical-Design", "Civil-Build"]},
            {"option_id": 1474, "option_text": "Environmental contamination from damaged facilities", "trait_tags": ["Environmental-Eng", "Lab-Research"]},
            {"option_id": 1475, "option_text": "Whether the building design followed earthquake codes", "trait_tags": ["Spatial-Design", "Civil-Build"]},
            {"option_id": 1476, "option_text": "The seismic data to predict aftershocks", "trait_tags": ["Data-Analytics", "Field-Research"]},
            {"option_id": 1477, "option_text": "Whether machinery and elevators are safe", "trait_tags": ["Mechanical-Design", "Industrial-Ops"]},
            {"option_id": 1478, "option_text": "I'd focus on helping rescue trapped people", "trait_tags": ["Physical-Skill", "Community-Serve"]}
        ]
    },

    # --- BUSINESS SITUATIONAL (Q148-Q157) ---
    {
        "question_id": 148,
        "question_text": "You're launching a food business in your town. What's your first priority?",
        "category": "Situational - Food Business",
        "options": [
            {"option_id": 1481, "option_text": "Creating a unique menu and recipes", "trait_tags": ["Culinary-Arts", "Creative-Skill"]},
            {"option_id": 1482, "option_text": "Managing the budget and financial projections", "trait_tags": ["Finance-Acct", "Startup-Venture"]},
            {"option_id": 1483, "option_text": "Marketing on social media to attract customers", "trait_tags": ["Marketing-Sales", "Digital-Media"]},
            {"option_id": 1484, "option_text": "Hiring and training the right staff", "trait_tags": ["HR-Management", "People-Skill"]},
            {"option_id": 1485, "option_text": "Ensuring food safety and proper storage", "trait_tags": ["Food-Science", "Nutrition-Diet"]},
            {"option_id": 1486, "option_text": "Designing the restaurant layout and ambiance", "trait_tags": ["Spatial-Design", "Visual-Design"]},
            {"option_id": 1487, "option_text": "Negotiating with suppliers for best prices", "trait_tags": ["Startup-Venture", "Finance-Acct"]},
            {"option_id": 1488, "option_text": "Building a delivery app or online ordering system", "trait_tags": ["Web-Dev", "Startup-Venture"]}
        ]
    },
    {
        "question_id": 149,
        "question_text": "Your friend's sari-sari store is struggling. How would you help?",
        "category": "Situational - Small Business",
        "options": [
            {"option_id": 1491, "option_text": "Analyze their sales data to find what sells best", "trait_tags": ["Data-Analytics", "Finance-Acct"]},
            {"option_id": 1492, "option_text": "Create a Facebook page and promote online", "trait_tags": ["Marketing-Sales", "Digital-Media"]},
            {"option_id": 1493, "option_text": "Redesign the store layout to attract customers", "trait_tags": ["Spatial-Design", "Marketing-Sales"]},
            {"option_id": 1494, "option_text": "Help them manage inventory and expenses", "trait_tags": ["Admin-Skill", "Finance-Acct"]},
            {"option_id": 1495, "option_text": "Introduce new products based on neighborhood needs", "trait_tags": ["Startup-Venture", "Community-Serve"]},
            {"option_id": 1496, "option_text": "Train them on customer service skills", "trait_tags": ["HR-Management", "People-Skill"]},
            {"option_id": 1497, "option_text": "Set up a simple POS or accounting system", "trait_tags": ["Software-Dev", "Finance-Acct"]},
            {"option_id": 1498, "option_text": "Look into franchise or cooperative options", "trait_tags": ["Startup-Venture", "Admin-Skill"]}
        ]
    },
    {
        "question_id": 150,
        "question_text": "You're managing a company's HR department. What task do you enjoy most?",
        "category": "Situational - Human Resources",
        "options": [
            {"option_id": 1501, "option_text": "Interviewing and selecting the best candidates", "trait_tags": ["HR-Management", "People-Skill"]},
            {"option_id": 1502, "option_text": "Designing training programs for new employees", "trait_tags": ["HR-Management", "Teaching-Ed"]},
            {"option_id": 1503, "option_text": "Resolving workplace conflicts between team members", "trait_tags": ["HR-Management", "Counseling"]},
            {"option_id": 1504, "option_text": "Managing payroll and employee benefits", "trait_tags": ["Finance-Acct", "Admin-Skill"]},
            {"option_id": 1505, "option_text": "Creating team-building activities and events", "trait_tags": ["HR-Management", "Creative-Skill"]},
            {"option_id": 1506, "option_text": "Ensuring the company follows labor laws", "trait_tags": ["Legal-Practice", "Admin-Skill"]},
            {"option_id": 1507, "option_text": "Analyzing employee performance data", "trait_tags": ["Data-Analytics", "HR-Management"]},
            {"option_id": 1508, "option_text": "Building the company culture and values", "trait_tags": ["HR-Management", "Community-Serve"]}
        ]
    },

    # --- CREATIVE SITUATIONAL (Q151-Q158) ---
    {
        "question_id": 151,
        "question_text": "Your school is putting on a big cultural show. What role would you take?",
        "category": "Situational - Cultural Event",
        "options": [
            {"option_id": 1511, "option_text": "Directing the play or dance performance", "trait_tags": ["Performing-Arts", "People-Skill"]},
            {"option_id": 1512, "option_text": "Designing the stage set and costumes", "trait_tags": ["Visual-Design", "Spatial-Design"]},
            {"option_id": 1513, "option_text": "Filming and editing the event highlights", "trait_tags": ["Film-Broadcast", "Digital-Media"]},
            {"option_id": 1514, "option_text": "Composing or selecting the music", "trait_tags": ["Performing-Arts", "Creative-Skill"]},
            {"option_id": 1515, "option_text": "Creating promotional posters and social media content", "trait_tags": ["Visual-Design", "Marketing-Sales"]},
            {"option_id": 1516, "option_text": "Managing the budget and sponsorships", "trait_tags": ["Finance-Acct", "Admin-Skill"]},
            {"option_id": 1517, "option_text": "Operating the lights, sound, and tech equipment", "trait_tags": ["Technical-Skill", "Hardware-Systems"]},
            {"option_id": 1518, "option_text": "Acting or performing on stage", "trait_tags": ["Performing-Arts", "Creative-Skill"]}
        ]
    },
    {
        "question_id": 152,
        "question_text": "A local museum asks you to create a digital exhibit. What would you make?",
        "category": "Situational - Digital Art",
        "options": [
            {"option_id": 1521, "option_text": "A 3D virtual tour of Philippine heritage sites", "trait_tags": ["Animation-3D", "Tourism-Travel"]},
            {"option_id": 1522, "option_text": "Interactive animations of historical events", "trait_tags": ["Animation-3D", "Film-Broadcast"]},
            {"option_id": 1523, "option_text": "A documentary film about local traditions", "trait_tags": ["Film-Broadcast", "Community-Serve"]},
            {"option_id": 1524, "option_text": "Digital paintings and visual art installations", "trait_tags": ["Visual-Design", "Creative-Skill"]},
            {"option_id": 1525, "option_text": "An interactive game that teaches Philippine history", "trait_tags": ["Game-Dev", "Teaching-Ed"]},
            {"option_id": 1526, "option_text": "A music and sound experience of Philippine instruments", "trait_tags": ["Performing-Arts", "Digital-Media"]},
            {"option_id": 1527, "option_text": "A mobile app as a museum guide", "trait_tags": ["Mobile-Dev", "Tourism-Travel"]},
            {"option_id": 1528, "option_text": "Fashion display of traditional Filipino clothing", "trait_tags": ["Spatial-Design", "Creative-Skill"]}
        ]
    },
    {
        "question_id": 153,
        "question_text": "You're hired to redesign a local park. What's most important to you?",
        "category": "Situational - Design Project",
        "options": [
            {"option_id": 1531, "option_text": "The landscape architecture and garden layout", "trait_tags": ["Spatial-Design", "Environmental-Sci"]},
            {"option_id": 1532, "option_text": "Installing public art and sculptures", "trait_tags": ["Visual-Design", "Creative-Skill"]},
            {"option_id": 1533, "option_text": "Making it eco-friendly with solar lighting", "trait_tags": ["Environmental-Eng", "Electrical-Power"]},
            {"option_id": 1534, "option_text": "Adding a sports area and fitness equipment", "trait_tags": ["Sports-Ed", "Physical-Skill"]},
            {"option_id": 1535, "option_text": "Creating a children's playground with interactive features", "trait_tags": ["Creative-Skill", "Teaching-Ed"]},
            {"option_id": 1536, "option_text": "Designing accessible pathways for disabled visitors", "trait_tags": ["Civil-Build", "Community-Serve"]},
            {"option_id": 1537, "option_text": "Adding a food stall area and gathering space", "trait_tags": ["Hospitality-Svc", "Culinary-Arts"]},
            {"option_id": 1538, "option_text": "Installing security cameras and lighting", "trait_tags": ["Hardware-Systems", "Law-Enforce"]}
        ]
    },

    # --- SCIENCE SITUATIONAL (Q154-Q161) ---
    {
        "question_id": 154,
        "question_text": "A river in your town is getting polluted. How would you help as a scientist?",
        "category": "Situational - Environmental Crisis",
        "options": [
            {"option_id": 1541, "option_text": "Collect and analyze water samples in the lab", "trait_tags": ["Lab-Research", "Environmental-Sci"]},
            {"option_id": 1542, "option_text": "Track the pollution source using field surveys", "trait_tags": ["Field-Research", "Environmental-Sci"]},
            {"option_id": 1543, "option_text": "Study the impact on fish and aquatic life", "trait_tags": ["Field-Research", "Agri-Nature"]},
            {"option_id": 1544, "option_text": "Test food safety in crops irrigated by the river", "trait_tags": ["Food-Science", "Lab-Research"]},
            {"option_id": 1545, "option_text": "Use data modeling to predict pollution spread", "trait_tags": ["Data-Analytics", "Environmental-Sci"]},
            {"option_id": 1546, "option_text": "Design a water filtration system", "trait_tags": ["Environmental-Eng", "Mechanical-Design"]},
            {"option_id": 1547, "option_text": "Organize a community cleanup and awareness campaign", "trait_tags": ["Community-Serve", "Public-Health"]},
            {"option_id": 1548, "option_text": "Work with the government to enforce pollution laws", "trait_tags": ["Legal-Practice", "Environmental-Sci"]}
        ]
    },
    {
        "question_id": 155,
        "question_text": "A new food product needs testing before it goes to market. What's your job?",
        "category": "Situational - Food Science",
        "options": [
            {"option_id": 1551, "option_text": "Testing for bacteria and contaminants in the lab", "trait_tags": ["Food-Science", "Lab-Research"]},
            {"option_id": 1552, "option_text": "Analyzing the nutritional content and labeling", "trait_tags": ["Nutrition-Diet", "Food-Science"]},
            {"option_id": 1553, "option_text": "Improving the taste and texture through experiments", "trait_tags": ["Food-Science", "Culinary-Arts"]},
            {"option_id": 1554, "option_text": "Designing the packaging and branding", "trait_tags": ["Visual-Design", "Marketing-Sales"]},
            {"option_id": 1555, "option_text": "Calculating the cost and setting the price", "trait_tags": ["Finance-Acct", "Industrial-Ops"]},
            {"option_id": 1556, "option_text": "Checking if it meets government food safety rules", "trait_tags": ["Food-Science", "Legal-Practice"]},
            {"option_id": 1557, "option_text": "Running consumer taste tests and focus groups", "trait_tags": ["Marketing-Sales", "People-Skill"]},
            {"option_id": 1558, "option_text": "Developing the production process for mass manufacturing", "trait_tags": ["Industrial-Ops", "Food-Science"]}
        ]
    },
    {
        "question_id": 156,
        "question_text": "You're working at a forensic science lab. What's your favorite task?",
        "category": "Situational - Forensics",
        "options": [
            {"option_id": 1561, "option_text": "Analyzing DNA evidence from crime scenes", "trait_tags": ["Forensic-Sci", "Lab-Research"]},
            {"option_id": 1562, "option_text": "Examining fingerprints and trace evidence", "trait_tags": ["Forensic-Sci", "Analytical-Skill"]},
            {"option_id": 1563, "option_text": "Performing toxicology tests for poison detection", "trait_tags": ["Forensic-Sci", "Medical-Lab"]},
            {"option_id": 1564, "option_text": "Using digital forensics to analyze computer evidence", "trait_tags": ["Forensic-Sci", "Cyber-Defense"]},
            {"option_id": 1565, "option_text": "Testifying as an expert witness in court", "trait_tags": ["Forensic-Sci", "Legal-Practice"]},
            {"option_id": 1566, "option_text": "Reconstructing how a crime happened", "trait_tags": ["Forensic-Sci", "Law-Enforce"]},
            {"option_id": 1567, "option_text": "Taking photographs and documenting evidence", "trait_tags": ["Visual-Design", "Law-Enforce"]},
            {"option_id": 1568, "option_text": "Processing evidence at the actual crime scene", "trait_tags": ["Forensic-Sci", "Physical-Skill"]}
        ]
    },

    # --- EDUCATION SITUATIONAL (Q157-Q162) ---
    {
        "question_id": 157,
        "question_text": "A struggling student asks for your help. How would you assist them?",
        "category": "Situational - Student Support",
        "options": [
            {"option_id": 1571, "option_text": "Tutor them one-on-one in their weak subject", "trait_tags": ["Teaching-Ed", "People-Skill"]},
            {"option_id": 1572, "option_text": "Talk to them about their personal problems first", "trait_tags": ["Counseling", "People-Skill"]},
            {"option_id": 1573, "option_text": "Create fun study materials and visual aids", "trait_tags": ["Teaching-Ed", "Creative-Skill"]},
            {"option_id": 1574, "option_text": "Organize a study group for peer support", "trait_tags": ["Teaching-Ed", "Community-Serve"]},
            {"option_id": 1575, "option_text": "Use sports or games as motivation", "trait_tags": ["Sports-Ed", "Teaching-Ed"]},
            {"option_id": 1576, "option_text": "Recommend an online tutorial or learning app", "trait_tags": ["Teaching-Ed", "Software-Dev"]},
            {"option_id": 1577, "option_text": "Talk to their parents about the issue", "trait_tags": ["Counseling", "Social-Work"]},
            {"option_id": 1578, "option_text": "Create a structured study plan and schedule", "trait_tags": ["Teaching-Ed", "Admin-Skill"]}
        ]
    },
    {
        "question_id": 158,
        "question_text": "You're a guidance counselor and a student is being bullied. What do you do first?",
        "category": "Situational - School Counseling",
        "options": [
            {"option_id": 1581, "option_text": "Listen to the student's feelings and give emotional support", "trait_tags": ["Counseling", "People-Skill"]},
            {"option_id": 1582, "option_text": "Investigate the bullying situation thoroughly", "trait_tags": ["Law-Enforce", "Analytical-Skill"]},
            {"option_id": 1583, "option_text": "Mediate between the bully and the victim", "trait_tags": ["Counseling", "People-Skill"]},
            {"option_id": 1584, "option_text": "Inform the school administration and parents", "trait_tags": ["Admin-Skill", "Community-Serve"]},
            {"option_id": 1585, "option_text": "Start an anti-bullying awareness program", "trait_tags": ["Teaching-Ed", "Community-Serve"]},
            {"option_id": 1586, "option_text": "Refer them to a professional therapist", "trait_tags": ["Counseling", "Rehab-Therapy"]},
            {"option_id": 1587, "option_text": "Teach the student coping and self-defense strategies", "trait_tags": ["Sports-Ed", "Counseling"]},
            {"option_id": 1588, "option_text": "Document everything for potential legal action", "trait_tags": ["Legal-Practice", "Admin-Skill"]}
        ]
    },

    # --- PUBLIC SERVICE SITUATIONAL (Q159-Q164) ---
    {
        "question_id": 159,
        "question_text": "You discover illegal dumping in a local river. What action do you take?",
        "category": "Situational - Environmental Law",
        "options": [
            {"option_id": 1591, "option_text": "Gather evidence and file a case with the DENR", "trait_tags": ["Legal-Practice", "Environmental-Sci"]},
            {"option_id": 1592, "option_text": "Organize a community protest and cleanup", "trait_tags": ["Community-Serve", "Social-Work"]},
            {"option_id": 1593, "option_text": "Interview witnesses and investigate the source", "trait_tags": ["Law-Enforce", "Analytical-Skill"]},
            {"option_id": 1594, "option_text": "Write a news report to bring public attention", "trait_tags": ["Film-Broadcast", "Community-Serve"]},
            {"option_id": 1595, "option_text": "Test water samples to document contamination", "trait_tags": ["Lab-Research", "Environmental-Sci"]},
            {"option_id": 1596, "option_text": "Lobby the barangay council for stricter enforcement", "trait_tags": ["Community-Serve", "Legal-Practice"]},
            {"option_id": 1597, "option_text": "Design a monitoring system using cameras and sensors", "trait_tags": ["Hardware-Systems", "Environmental-Eng"]},
            {"option_id": 1598, "option_text": "Educate the community about proper waste disposal", "trait_tags": ["Teaching-Ed", "Public-Health"]}
        ]
    },
    {
        "question_id": 160,
        "question_text": "You work at a social welfare office. A family lost their home to a fire. What's your role?",
        "category": "Situational - Social Welfare",
        "options": [
            {"option_id": 1601, "option_text": "Process their emergency assistance paperwork", "trait_tags": ["Social-Work", "Admin-Skill"]},
            {"option_id": 1602, "option_text": "Provide counseling for the traumatized family", "trait_tags": ["Counseling", "Social-Work"]},
            {"option_id": 1603, "option_text": "Coordinate temporary housing and donations", "trait_tags": ["Community-Serve", "Admin-Skill"]},
            {"option_id": 1604, "option_text": "Assess the fire's cause for legal investigation", "trait_tags": ["Forensic-Sci", "Law-Enforce"]},
            {"option_id": 1605, "option_text": "Enroll their children in a nearby school", "trait_tags": ["Teaching-Ed", "Social-Work"]},
            {"option_id": 1606, "option_text": "Help them find new jobs or livelihood programs", "trait_tags": ["HR-Management", "Social-Work"]},
            {"option_id": 1607, "option_text": "Ensure they get proper medical checkups", "trait_tags": ["Public-Health", "Patient-Care"]},
            {"option_id": 1608, "option_text": "Raise funds through the community or online", "trait_tags": ["Marketing-Sales", "Community-Serve"]}
        ]
    },

    # --- AGRICULTURE/MARITIME/HOSPITALITY SITUATIONAL (Q161-Q170) ---
    {
        "question_id": 161,
        "question_text": "A farmer in your province wants to modernize their farm. How would you help?",
        "category": "Situational - Modern Farming",
        "options": [
            {"option_id": 1611, "option_text": "Introduce drone technology for crop monitoring", "trait_tags": ["Agri-Nature", "Hardware-Systems"]},
            {"option_id": 1612, "option_text": "Set up an irrigation system for better water use", "trait_tags": ["Agri-Nature", "Mechanical-Design"]},
            {"option_id": 1613, "option_text": "Test soil quality to recommend the right fertilizer", "trait_tags": ["Agri-Nature", "Lab-Research"]},
            {"option_id": 1614, "option_text": "Help them sell products online or in markets", "trait_tags": ["Agri-Nature", "Marketing-Sales"]},
            {"option_id": 1615, "option_text": "Teach organic farming techniques", "trait_tags": ["Agri-Nature", "Environmental-Sci"]},
            {"option_id": 1616, "option_text": "Process and package their harvest for retail", "trait_tags": ["Food-Science", "Industrial-Ops"]},
            {"option_id": 1617, "option_text": "Set up a fishpond alongside the farmland", "trait_tags": ["Agri-Nature", "Field-Research"]},
            {"option_id": 1618, "option_text": "Build a simple app to track planting schedules", "trait_tags": ["Mobile-Dev", "Agri-Nature"]}
        ]
    },
    {
        "question_id": 162,
        "question_text": "You're on a cargo ship and the engine breaks down at sea. What's your role?",
        "category": "Situational - Maritime Emergency",
        "options": [
            {"option_id": 1621, "option_text": "Diagnose and repair the engine problem", "trait_tags": ["Maritime-Sea", "Mechanical-Design"]},
            {"option_id": 1622, "option_text": "Navigate to the nearest port for repairs", "trait_tags": ["Maritime-Sea", "Physical-Skill"]},
            {"option_id": 1623, "option_text": "Radio for help and coordinate with coast guard", "trait_tags": ["Maritime-Sea", "Community-Serve"]},
            {"option_id": 1624, "option_text": "Check the electrical systems for faults", "trait_tags": ["Electrical-Power", "Maritime-Sea"]},
            {"option_id": 1625, "option_text": "Manage the crew to keep calm and organized", "trait_tags": ["People-Skill", "Admin-Skill"]},
            {"option_id": 1626, "option_text": "Assess cargo damage and safety protocols", "trait_tags": ["Industrial-Ops", "Maritime-Sea"]},
            {"option_id": 1627, "option_text": "Document the incident for insurance and legal records", "trait_tags": ["Legal-Practice", "Admin-Skill"]},
            {"option_id": 1628, "option_text": "Provide first aid to any injured crew members", "trait_tags": ["Patient-Care", "Physical-Skill"]}
        ]
    },
    {
        "question_id": 163,
        "question_text": "A Boracay resort asks you to improve their guest experience. What do you focus on?",
        "category": "Situational - Resort Management",
        "options": [
            {"option_id": 1631, "option_text": "Revamp the menu with local Filipino cuisine", "trait_tags": ["Culinary-Arts", "Hospitality-Svc"]},
            {"option_id": 1632, "option_text": "Create exciting tour packages and activities", "trait_tags": ["Tourism-Travel", "Hospitality-Svc"]},
            {"option_id": 1633, "option_text": "Train staff for world-class customer service", "trait_tags": ["HR-Management", "Hospitality-Svc"]},
            {"option_id": 1634, "option_text": "Design a beautiful website for online bookings", "trait_tags": ["Web-Dev", "Marketing-Sales"]},
            {"option_id": 1635, "option_text": "Manage the resort's finances and operations", "trait_tags": ["Admin-Skill", "Finance-Acct"]},
            {"option_id": 1636, "option_text": "Ensure environmental sustainability of the resort", "trait_tags": ["Environmental-Sci", "Hospitality-Svc"]},
            {"option_id": 1637, "option_text": "Create Instagram-worthy interiors and spaces", "trait_tags": ["Spatial-Design", "Visual-Design"]},
            {"option_id": 1638, "option_text": "Set up a spa and wellness program", "trait_tags": ["Rehab-Therapy", "Hospitality-Svc"]}
        ]
    },
    {
        "question_id": 164,
        "question_text": "You're organizing a Philippine food festival. What's your main responsibility?",
        "category": "Situational - Festival Planning",
        "options": [
            {"option_id": 1641, "option_text": "Curating the food stalls and menu selection", "trait_tags": ["Culinary-Arts", "Hospitality-Svc"]},
            {"option_id": 1642, "option_text": "Marketing the event through flyers and social media", "trait_tags": ["Marketing-Sales", "Film-Broadcast"]},
            {"option_id": 1643, "option_text": "Managing the event budget and vendor payments", "trait_tags": ["Finance-Acct", "Admin-Skill"]},
            {"option_id": 1644, "option_text": "Coordinating live entertainment and performances", "trait_tags": ["Performing-Arts", "Admin-Skill"]},
            {"option_id": 1645, "option_text": "Setting up the venue layout and decorations", "trait_tags": ["Spatial-Design", "Creative-Skill"]},
            {"option_id": 1646, "option_text": "Ensuring food safety and hygiene standards", "trait_tags": ["Food-Science", "Public-Health"]},
            {"option_id": 1647, "option_text": "Selling tickets and managing the entrance", "trait_tags": ["Admin-Skill", "Marketing-Sales"]},
            {"option_id": 1648, "option_text": "Filming and live-streaming the event", "trait_tags": ["Film-Broadcast", "Digital-Media"]}
        ]
    },

    # --- CROSS-DOMAIN & PERSONALITY QUESTIONS (Q165-Q185) ---
    {
        "question_id": 165,
        "question_text": "If you could start any online business tomorrow, what would it be?",
        "category": "Entrepreneurship Vision",
        "options": [
            {"option_id": 1651, "option_text": "An e-commerce store selling Filipino products", "trait_tags": ["Startup-Venture", "Web-Dev"]},
            {"option_id": 1652, "option_text": "A freelance graphic design service", "trait_tags": ["Visual-Design", "Startup-Venture"]},
            {"option_id": 1653, "option_text": "An online tutoring platform", "trait_tags": ["Teaching-Ed", "Web-Dev"]},
            {"option_id": 1654, "option_text": "A food delivery service for home-cooked meals", "trait_tags": ["Culinary-Arts", "Startup-Venture"]},
            {"option_id": 1655, "option_text": "A tech consulting company", "trait_tags": ["Software-Dev", "Startup-Venture"]},
            {"option_id": 1656, "option_text": "A travel vlog and tourism promotion channel", "trait_tags": ["Tourism-Travel", "Film-Broadcast"]},
            {"option_id": 1657, "option_text": "A fitness coaching and workout plan service", "trait_tags": ["Sports-Ed", "Startup-Venture"]},
            {"option_id": 1658, "option_text": "A virtual mental health counseling platform", "trait_tags": ["Counseling", "Web-Dev"]}
        ]
    },
    {
        "question_id": 166,
        "question_text": "What kind of volunteer work appeals to you the most?",
        "category": "Values - Volunteering",
        "options": [
            {"option_id": 1661, "option_text": "Teaching in remote areas with no schools", "trait_tags": ["Teaching-Ed", "Community-Serve"]},
            {"option_id": 1662, "option_text": "Medical missions in underserved communities", "trait_tags": ["Patient-Care", "Public-Health"]},
            {"option_id": 1663, "option_text": "Building houses through Habitat for Humanity", "trait_tags": ["Civil-Build", "Community-Serve"]},
            {"option_id": 1664, "option_text": "Environmental cleanup and tree planting", "trait_tags": ["Environmental-Sci", "Agri-Nature"]},
            {"option_id": 1665, "option_text": "Feeding programs for malnourished children", "trait_tags": ["Nutrition-Diet", "Social-Work"]},
            {"option_id": 1666, "option_text": "Teaching computer literacy to senior citizens", "trait_tags": ["Software-Dev", "Teaching-Ed"]},
            {"option_id": 1667, "option_text": "Legal aid for those who can't afford lawyers", "trait_tags": ["Legal-Practice", "Social-Work"]},
            {"option_id": 1668, "option_text": "Organizing sports clinics for youth", "trait_tags": ["Sports-Ed", "Community-Serve"]}
        ]
    },
    {
        "question_id": 167,
        "question_text": "What would you study about the Philippines if you could do research?",
        "category": "Research Interest",
        "options": [
            {"option_id": 1671, "option_text": "How to make Filipino agriculture more productive", "trait_tags": ["Agri-Nature", "Lab-Research"]},
            {"option_id": 1672, "option_text": "How social media affects Filipino youth mental health", "trait_tags": ["Counseling", "Data-Analytics"]},
            {"option_id": 1673, "option_text": "How to combat plastic pollution in Philippine seas", "trait_tags": ["Environmental-Sci", "Field-Research"]},
            {"option_id": 1674, "option_text": "How AI can improve healthcare access in rural areas", "trait_tags": ["AI-ML", "Public-Health"]},
            {"option_id": 1675, "option_text": "How to make Philippine businesses globally competitive", "trait_tags": ["Startup-Venture", "Marketing-Sales"]},
            {"option_id": 1676, "option_text": "The history and preservation of Filipino indigenous cultures", "trait_tags": ["Community-Serve", "Field-Research"]},
            {"option_id": 1677, "option_text": "How to reduce traffic congestion in Metro Manila", "trait_tags": ["Civil-Build", "Data-Analytics"]},
            {"option_id": 1678, "option_text": "Developing Filipino language technology and NLP", "trait_tags": ["AI-ML", "Teaching-Ed"]}
        ]
    },
    {
        "question_id": 168,
        "question_text": "Your group project is about climate change. Which part do you want to handle?",
        "category": "Situational - Group Research",
        "options": [
            {"option_id": 1681, "option_text": "Collecting data and running statistical analysis", "trait_tags": ["Data-Analytics", "Environmental-Sci"]},
            {"option_id": 1682, "option_text": "Doing field research and environmental surveys", "trait_tags": ["Field-Research", "Environmental-Sci"]},
            {"option_id": 1683, "option_text": "Creating the visual presentation and infographics", "trait_tags": ["Visual-Design", "Digital-Media"]},
            {"option_id": 1684, "option_text": "Writing the research paper and conclusions", "trait_tags": ["Analytical-Skill", "Teaching-Ed"]},
            {"option_id": 1685, "option_text": "Presenting and defending the findings", "trait_tags": ["People-Skill", "Performing-Arts"]},
            {"option_id": 1686, "option_text": "Building a working prototype solution", "trait_tags": ["Environmental-Eng", "Hardware-Systems"]},
            {"option_id": 1687, "option_text": "Recording a documentary video about the topic", "trait_tags": ["Film-Broadcast", "Environmental-Sci"]},
            {"option_id": 1688, "option_text": "Organizing the group tasks and deadlines", "trait_tags": ["Admin-Skill", "People-Skill"]}
        ]
    },
    {
        "question_id": 169,
        "question_text": "If your LGU gave you a budget to improve your barangay, what would you prioritize?",
        "category": "Situational - Community Development",
        "options": [
            {"option_id": 1691, "option_text": "Build a community health center", "trait_tags": ["Public-Health", "Civil-Build"]},
            {"option_id": 1692, "option_text": "Set up free Wi-Fi and a computer lab", "trait_tags": ["Cloud-Systems", "Teaching-Ed"]},
            {"option_id": 1693, "option_text": "Create a livelihood training center", "trait_tags": ["Startup-Venture", "Teaching-Ed"]},
            {"option_id": 1694, "option_text": "Improve the roads and drainage system", "trait_tags": ["Civil-Build", "Environmental-Eng"]},
            {"option_id": 1695, "option_text": "Build a basketball court and sports facilities", "trait_tags": ["Sports-Ed", "Physical-Skill"]},
            {"option_id": 1696, "option_text": "Create a daycare and after-school program", "trait_tags": ["Teaching-Ed", "Social-Work"]},
            {"option_id": 1697, "option_text": "Install streetlights and CCTV for safety", "trait_tags": ["Electrical-Power", "Law-Enforce"]},
            {"option_id": 1698, "option_text": "Start a community garden and food program", "trait_tags": ["Agri-Nature", "Nutrition-Diet"]}
        ]
    },
    {
        "question_id": 170,
        "question_text": "What kind of YouTube channel would you create?",
        "category": "Content Creation Interest",
        "options": [
            {"option_id": 1701, "option_text": "Coding tutorials and tech reviews", "trait_tags": ["Software-Dev", "Film-Broadcast"]},
            {"option_id": 1702, "option_text": "Cooking shows featuring Filipino recipes", "trait_tags": ["Culinary-Arts", "Film-Broadcast"]},
            {"option_id": 1703, "option_text": "Science experiments and educational content", "trait_tags": ["Lab-Research", "Teaching-Ed"]},
            {"option_id": 1704, "option_text": "True crime and forensic analysis", "trait_tags": ["Forensic-Sci", "Film-Broadcast"]},
            {"option_id": 1705, "option_text": "Travel vlogs of Philippine destinations", "trait_tags": ["Tourism-Travel", "Film-Broadcast"]},
            {"option_id": 1706, "option_text": "Fitness workouts and health tips", "trait_tags": ["Sports-Ed", "Film-Broadcast"]},
            {"option_id": 1707, "option_text": "Art tutorials and design process videos", "trait_tags": ["Visual-Design", "Film-Broadcast"]},
            {"option_id": 1708, "option_text": "Business advice and entrepreneurship tips", "trait_tags": ["Startup-Venture", "Film-Broadcast"]}
        ]
    },
    {
        "question_id": 171,
        "question_text": "What makes you feel most accomplished at the end of a day?",
        "category": "Values - Accomplishment",
        "options": [
            {"option_id": 1711, "option_text": "Solving a difficult technical problem", "trait_tags": ["Software-Dev", "Analytical-Skill"]},
            {"option_id": 1712, "option_text": "Helping someone feel better emotionally or physically", "trait_tags": ["Patient-Care", "Counseling"]},
            {"option_id": 1713, "option_text": "Creating something beautiful or artistic", "trait_tags": ["Visual-Design", "Creative-Skill"]},
            {"option_id": 1714, "option_text": "Closing a deal or making a sale", "trait_tags": ["Marketing-Sales", "Startup-Venture"]},
            {"option_id": 1715, "option_text": "Teaching someone something they finally understand", "trait_tags": ["Teaching-Ed", "People-Skill"]},
            {"option_id": 1716, "option_text": "Discovering new facts through research", "trait_tags": ["Lab-Research", "Field-Research"]},
            {"option_id": 1717, "option_text": "Completing a physical challenge or workout", "trait_tags": ["Physical-Skill", "Sports-Ed"]},
            {"option_id": 1718, "option_text": "Organizing a messy situation into order", "trait_tags": ["Admin-Skill", "Industrial-Ops"]}
        ]
    },
    {
        "question_id": 172,
        "question_text": "Which school subject combination do you enjoy the most?",
        "category": "Academic Interest",
        "options": [
            {"option_id": 1721, "option_text": "Biology and Chemistry", "trait_tags": ["Lab-Research", "Medical-Lab"]},
            {"option_id": 1722, "option_text": "Mathematics and Physics", "trait_tags": ["Data-Analytics", "Mechanical-Design"]},
            {"option_id": 1723, "option_text": "Computer Science and Math", "trait_tags": ["Software-Dev", "AI-ML"]},
            {"option_id": 1724, "option_text": "History and Social Studies", "trait_tags": ["Community-Serve", "Teaching-Ed"]},
            {"option_id": 1725, "option_text": "Art and Music", "trait_tags": ["Visual-Design", "Performing-Arts"]},
            {"option_id": 1726, "option_text": "English and Filipino Literature", "trait_tags": ["Creative-Skill", "Teaching-Ed"]},
            {"option_id": 1727, "option_text": "Physical Education and Health", "trait_tags": ["Sports-Ed", "Public-Health"]},
            {"option_id": 1728, "option_text": "Business and Economics", "trait_tags": ["Finance-Acct", "Startup-Venture"]}
        ]
    },
    {
        "question_id": 173,
        "question_text": "What kind of leader are you in a group project?",
        "category": "Leadership Style",
        "options": [
            {"option_id": 1731, "option_text": "The organizer who makes checklists and timelines", "trait_tags": ["Admin-Skill", "Industrial-Ops"]},
            {"option_id": 1732, "option_text": "The creative one with all the ideas", "trait_tags": ["Creative-Skill", "Startup-Venture"]},
            {"option_id": 1733, "option_text": "The researcher who digs deep into the topic", "trait_tags": ["Lab-Research", "Analytical-Skill"]},
            {"option_id": 1734, "option_text": "The tech person handling presentations and tools", "trait_tags": ["Software-Dev", "Digital-Media"]},
            {"option_id": 1735, "option_text": "The motivator who keeps everyone going", "trait_tags": ["People-Skill", "Teaching-Ed"]},
            {"option_id": 1736, "option_text": "The negotiator who deals with disagreements", "trait_tags": ["HR-Management", "Counseling"]},
            {"option_id": 1737, "option_text": "The presenter who speaks in front of the class", "trait_tags": ["People-Skill", "Performing-Arts"]},
            {"option_id": 1738, "option_text": "The hands-on builder who makes the prototype", "trait_tags": ["Hardware-Systems", "Mechanical-Design"]}
        ]
    },
    {
        "question_id": 174,
        "question_text": "What career do you imagine yourself in 10 years from now?",
        "category": "Future Vision",
        "options": [
            {"option_id": 1741, "option_text": "Running my own tech startup", "trait_tags": ["Startup-Venture", "Software-Dev"]},
            {"option_id": 1742, "option_text": "A doctor or specialist in a hospital", "trait_tags": ["Patient-Care", "Medical-Lab"]},
            {"option_id": 1743, "option_text": "A licensed engineer on major projects", "trait_tags": ["Civil-Build", "Mechanical-Design"]},
            {"option_id": 1744, "option_text": "A teacher or professor at a university", "trait_tags": ["Teaching-Ed", "Lab-Research"]},
            {"option_id": 1745, "option_text": "A famous artist or content creator", "trait_tags": ["Visual-Design", "Film-Broadcast"]},
            {"option_id": 1746, "option_text": "A lawyer or judge fighting for justice", "trait_tags": ["Legal-Practice", "Law-Enforce"]},
            {"option_id": 1747, "option_text": "A scientist making groundbreaking discoveries", "trait_tags": ["Lab-Research", "Environmental-Sci"]},
            {"option_id": 1748, "option_text": "A successful business executive or CEO", "trait_tags": ["Finance-Acct", "Startup-Venture"]},
            {"option_id": 1749, "option_text": "A chef or restaurant owner", "trait_tags": ["Culinary-Arts", "Startup-Venture"]},
            {"option_id": 1750, "option_text": "A sports coach or fitness expert", "trait_tags": ["Sports-Ed", "Teaching-Ed"]}
        ]
    },
    {
        "question_id": 175,
        "question_text": "What problem in the Philippines do you most want to help solve?",
        "category": "Philippine Issues",
        "options": [
            {"option_id": 1751, "option_text": "Poverty and unemployment", "trait_tags": ["Social-Work", "Startup-Venture"]},
            {"option_id": 1752, "option_text": "Climate change and typhoon damage", "trait_tags": ["Environmental-Sci", "Environmental-Eng"]},
            {"option_id": 1753, "option_text": "Poor access to quality education", "trait_tags": ["Teaching-Ed", "Software-Dev"]},
            {"option_id": 1754, "option_text": "Corruption and poor governance", "trait_tags": ["Legal-Practice", "Community-Serve"]},
            {"option_id": 1755, "option_text": "Food insecurity and hunger", "trait_tags": ["Agri-Nature", "Nutrition-Diet"]},
            {"option_id": 1756, "option_text": "Lack of access to healthcare in rural areas", "trait_tags": ["Public-Health", "Patient-Care"]},
            {"option_id": 1757, "option_text": "Traffic and poor transportation systems", "trait_tags": ["Civil-Build", "Industrial-Ops"]},
            {"option_id": 1758, "option_text": "Cybercrime and online fraud", "trait_tags": ["Cyber-Defense", "Law-Enforce"]},
            {"option_id": 1759, "option_text": "Drug abuse and addiction", "trait_tags": ["Counseling", "Public-Health"]},
            {"option_id": 1760, "option_text": "Environmental destruction and deforestation", "trait_tags": ["Environmental-Sci", "Agri-Nature"]}
        ]
    },
    {
        "question_id": 176,
        "question_text": "If you receive a scholarship abroad, what would you study?",
        "category": "Study Abroad Interest",
        "options": [
            {"option_id": 1761, "option_text": "Computer science or artificial intelligence", "trait_tags": ["AI-ML", "Software-Dev"]},
            {"option_id": 1762, "option_text": "Medicine or public health", "trait_tags": ["Patient-Care", "Public-Health"]},
            {"option_id": 1763, "option_text": "Engineering or architecture", "trait_tags": ["Civil-Build", "Spatial-Design"]},
            {"option_id": 1764, "option_text": "Business administration or finance", "trait_tags": ["Finance-Acct", "Startup-Venture"]},
            {"option_id": 1765, "option_text": "Film, animation, or digital arts", "trait_tags": ["Film-Broadcast", "Animation-3D"]},
            {"option_id": 1766, "option_text": "Law or political science", "trait_tags": ["Legal-Practice", "Community-Serve"]},
            {"option_id": 1767, "option_text": "Environmental science or marine biology", "trait_tags": ["Environmental-Sci", "Field-Research"]},
            {"option_id": 1768, "option_text": "Culinary arts or hospitality management", "trait_tags": ["Culinary-Arts", "Tourism-Travel"]},
            {"option_id": 1769, "option_text": "Psychology or counseling", "trait_tags": ["Counseling", "Rehab-Therapy"]},
            {"option_id": 1770, "option_text": "Sports science or physical therapy", "trait_tags": ["Sports-Ed", "Rehab-Therapy"]}
        ]
    },
    {
        "question_id": 177,
        "question_text": "What's your favorite way to learn something new?",
        "category": "Learning Style",
        "options": [
            {"option_id": 1771, "option_text": "Building something hands-on and experimenting", "trait_tags": ["Hardware-Systems", "Mechanical-Design"]},
            {"option_id": 1772, "option_text": "Reading books and articles about the topic", "trait_tags": ["Lab-Research", "Analytical-Skill"]},
            {"option_id": 1773, "option_text": "Watching YouTube tutorials and demo videos", "trait_tags": ["Film-Broadcast", "Digital-Media"]},
            {"option_id": 1774, "option_text": "Asking an expert and learning through conversation", "trait_tags": ["People-Skill", "Teaching-Ed"]},
            {"option_id": 1775, "option_text": "Practicing by coding or creating projects", "trait_tags": ["Software-Dev", "Web-Dev"]},
            {"option_id": 1776, "option_text": "Drawing diagrams and visual notes", "trait_tags": ["Visual-Design", "Spatial-Design"]},
            {"option_id": 1777, "option_text": "Going outdoors and experiencing firsthand", "trait_tags": ["Field-Research", "Physical-Skill"]},
            {"option_id": 1778, "option_text": "Taking online courses and quizzes", "trait_tags": ["Teaching-Ed", "Software-Dev"]}
        ]
    },
    {
        "question_id": 178,
        "question_text": "What type of news story catches your attention most?",
        "category": "News Interest",
        "options": [
            {"option_id": 1781, "option_text": "New technology and gadget launches", "trait_tags": ["Hardware-Systems", "Software-Dev"]},
            {"option_id": 1782, "option_text": "Medical breakthroughs and health news", "trait_tags": ["Patient-Care", "Lab-Research"]},
            {"option_id": 1783, "option_text": "Stock market and business news", "trait_tags": ["Finance-Acct", "Marketing-Sales"]},
            {"option_id": 1784, "option_text": "Crime investigations and court cases", "trait_tags": ["Law-Enforce", "Forensic-Sci"]},
            {"option_id": 1785, "option_text": "Environmental issues and climate reports", "trait_tags": ["Environmental-Sci", "Field-Research"]},
            {"option_id": 1786, "option_text": "Sports results and athlete interviews", "trait_tags": ["Sports-Ed", "Physical-Skill"]},
            {"option_id": 1787, "option_text": "Celebrity and entertainment news", "trait_tags": ["Performing-Arts", "Film-Broadcast"]},
            {"option_id": 1788, "option_text": "Political news and government policies", "trait_tags": ["Community-Serve", "Legal-Practice"]}
        ]
    },
    {
        "question_id": 179,
        "question_text": "What's your biggest strength in a team?",
        "category": "Team Strength",
        "options": [
            {"option_id": 1791, "option_text": "I fix technical problems quickly", "trait_tags": ["Software-Dev", "Technical-Skill"]},
            {"option_id": 1792, "option_text": "I support my teammates emotionally", "trait_tags": ["Counseling", "People-Skill"]},
            {"option_id": 1793, "option_text": "I come up with creative solutions", "trait_tags": ["Creative-Skill", "Startup-Venture"]},
            {"option_id": 1794, "option_text": "I keep everything organized and on schedule", "trait_tags": ["Admin-Skill", "Industrial-Ops"]},
            {"option_id": 1795, "option_text": "I do thorough research and fact-checking", "trait_tags": ["Lab-Research", "Analytical-Skill"]},
            {"option_id": 1796, "option_text": "I persuade others and build consensus", "trait_tags": ["Marketing-Sales", "People-Skill"]},
            {"option_id": 1797, "option_text": "I do the physical work and hands-on tasks", "trait_tags": ["Physical-Skill", "Mechanical-Design"]},
            {"option_id": 1798, "option_text": "I present our work confidently to others", "trait_tags": ["Performing-Arts", "People-Skill"]}
        ]
    },
    {
        "question_id": 180,
        "question_text": "What would you invent if you had unlimited resources?",
        "category": "Innovation Vision",
        "options": [
            {"option_id": 1801, "option_text": "A robot nurse that helps hospital patients", "trait_tags": ["AI-ML", "Patient-Care"]},
            {"option_id": 1802, "option_text": "A machine that converts ocean plastic to fuel", "trait_tags": ["Environmental-Eng", "Mechanical-Design"]},
            {"option_id": 1803, "option_text": "A virtual reality classroom for any subject", "trait_tags": ["Game-Dev", "Teaching-Ed"]},
            {"option_id": 1804, "option_text": "A bulletproof emergency shelter for typhoons", "trait_tags": ["Civil-Build", "Community-Serve"]},
            {"option_id": 1805, "option_text": "An app that translates all Filipino dialects", "trait_tags": ["AI-ML", "Mobile-Dev"]},
            {"option_id": 1806, "option_text": "Vertical farms in cities to end hunger", "trait_tags": ["Agri-Nature", "Environmental-Eng"]},
            {"option_id": 1807, "option_text": "A drone system for delivering medicine to remote areas", "trait_tags": ["Hardware-Systems", "Public-Health"]},
            {"option_id": 1808, "option_text": "Smart clothes that monitor your health", "trait_tags": ["Hardware-Systems", "Patient-Care"]}
        ]
    },
    {
        "question_id": 181,
        "question_text": "What type of work environment makes you most productive?",
        "category": "Work Style",
        "options": [
            {"option_id": 1811, "option_text": "A quiet laboratory or research room", "trait_tags": ["Lab-Research", "Analytical-Skill"]},
            {"option_id": 1812, "option_text": "A busy hospital or clinic", "trait_tags": ["Patient-Care", "People-Skill"]},
            {"option_id": 1813, "option_text": "An open-plan tech office", "trait_tags": ["Software-Dev", "Web-Dev"]},
            {"option_id": 1814, "option_text": "An outdoor construction or field site", "trait_tags": ["Civil-Build", "Physical-Skill"]},
            {"option_id": 1815, "option_text": "A creative studio with art supplies", "trait_tags": ["Visual-Design", "Creative-Skill"]},
            {"option_id": 1816, "option_text": "A classroom full of students", "trait_tags": ["Teaching-Ed", "People-Skill"]},
            {"option_id": 1817, "option_text": "A corporate office with meetings", "trait_tags": ["Finance-Acct", "Admin-Skill"]},
            {"option_id": 1818, "option_text": "A kitchen or food production area", "trait_tags": ["Culinary-Arts", "Food-Science"]}
        ]
    },
    {
        "question_id": 182,
        "question_text": "What motivates you most to work hard?",
        "category": "Values - Motivation",
        "options": [
            {"option_id": 1821, "option_text": "Discovering something new or innovative", "trait_tags": ["Lab-Research", "AI-ML"]},
            {"option_id": 1822, "option_text": "Helping people who are suffering", "trait_tags": ["Patient-Care", "Social-Work"]},
            {"option_id": 1823, "option_text": "Earning money and financial success", "trait_tags": ["Finance-Acct", "Startup-Venture"]},
            {"option_id": 1824, "option_text": "Creating something beautiful", "trait_tags": ["Visual-Design", "Performing-Arts"]},
            {"option_id": 1825, "option_text": "Teaching the next generation", "trait_tags": ["Teaching-Ed", "Community-Serve"]},
            {"option_id": 1826, "option_text": "Protecting the environment", "trait_tags": ["Environmental-Sci", "Agri-Nature"]},
            {"option_id": 1827, "option_text": "Being respected as an expert", "trait_tags": ["Lab-Research", "Legal-Practice"]},
            {"option_id": 1828, "option_text": "The thrill of competition and winning", "trait_tags": ["Sports-Ed", "Marketing-Sales"]}
        ]
    },
    {
        "question_id": 183,
        "question_text": "How do you handle stress and pressure?",
        "category": "Stress Management",
        "options": [
            {"option_id": 1831, "option_text": "Exercise, play sports, or go to the gym", "trait_tags": ["Sports-Ed", "Physical-Skill"]},
            {"option_id": 1832, "option_text": "Draw, paint, or work on creative projects", "trait_tags": ["Visual-Design", "Creative-Skill"]},
            {"option_id": 1833, "option_text": "Talk to friends or family about my feelings", "trait_tags": ["People-Skill", "Counseling"]},
            {"option_id": 1834, "option_text": "Organize and plan to feel in control", "trait_tags": ["Admin-Skill", "Industrial-Ops"]},
            {"option_id": 1835, "option_text": "Code, tinker, or work on a tech project", "trait_tags": ["Software-Dev", "Hardware-Systems"]},
            {"option_id": 1836, "option_text": "Cook or bake something delicious", "trait_tags": ["Culinary-Arts", "Creative-Skill"]},
            {"option_id": 1837, "option_text": "Go outdoors and be in nature", "trait_tags": ["Field-Research", "Agri-Nature"]},
            {"option_id": 1838, "option_text": "Watch documentaries or read educational content", "trait_tags": ["Lab-Research", "Film-Broadcast"]}
        ]
    },
    {
        "question_id": 184,
        "question_text": "Which after-school club would you join or start?",
        "category": "Extracurricular Interest",
        "options": [
            {"option_id": 1841, "option_text": "Robotics or computer science club", "trait_tags": ["Hardware-Systems", "Software-Dev"]},
            {"option_id": 1842, "option_text": "Red Cross or medical volunteer club", "trait_tags": ["Patient-Care", "Community-Serve"]},
            {"option_id": 1843, "option_text": "Business and entrepreneurship club", "trait_tags": ["Startup-Venture", "Finance-Acct"]},
            {"option_id": 1844, "option_text": "Art, photography, or film club", "trait_tags": ["Visual-Design", "Film-Broadcast"]},
            {"option_id": 1845, "option_text": "Debate and public speaking club", "trait_tags": ["Legal-Practice", "People-Skill"]},
            {"option_id": 1846, "option_text": "Environmental or science club", "trait_tags": ["Environmental-Sci", "Lab-Research"]},
            {"option_id": 1847, "option_text": "Theater or dance troupe", "trait_tags": ["Performing-Arts", "Creative-Skill"]},
            {"option_id": 1848, "option_text": "Student government or community service", "trait_tags": ["Community-Serve", "Legal-Practice"]},
            {"option_id": 1849, "option_text": "Sports team or fitness club", "trait_tags": ["Sports-Ed", "Physical-Skill"]},
            {"option_id": 1850, "option_text": "Cooking or food appreciation club", "trait_tags": ["Culinary-Arts", "Nutrition-Diet"]}
        ]
    },
    {
        "question_id": 185,
        "question_text": "What kind of problem do you most enjoy solving?",
        "category": "Problem-Solving Style",
        "options": [
            {"option_id": 1851, "option_text": "Debugging code or fixing software errors", "trait_tags": ["Software-Dev", "Web-Dev"]},
            {"option_id": 1852, "option_text": "Diagnosing a medical condition", "trait_tags": ["Patient-Care", "Medical-Lab"]},
            {"option_id": 1853, "option_text": "Calculating the best financial strategy", "trait_tags": ["Finance-Acct", "Data-Analytics"]},
            {"option_id": 1854, "option_text": "Figuring out how a machine broke down", "trait_tags": ["Mechanical-Design", "Hardware-Systems"]},
            {"option_id": 1855, "option_text": "Understanding why someone is upset", "trait_tags": ["Counseling", "People-Skill"]},
            {"option_id": 1856, "option_text": "Designing a better layout or structure", "trait_tags": ["Spatial-Design", "Civil-Build"]},
            {"option_id": 1857, "option_text": "Solving a scientific mystery through experiments", "trait_tags": ["Lab-Research", "Forensic-Sci"]},
            {"option_id": 1858, "option_text": "Finding the right ingredients for a perfect recipe", "trait_tags": ["Culinary-Arts", "Food-Science"]}
        ]
    },

    # --- MORE SITUATIONAL - DEEPER EXPLORATION (Q186-Q200) ---
    {
        "question_id": 186,
        "question_text": "A local NGO needs a social media campaign. What's your contribution?",
        "category": "Situational - Digital Marketing",
        "options": [
            {"option_id": 1861, "option_text": "Writing compelling stories about their cause", "trait_tags": ["Creative-Skill", "Community-Serve"]},
            {"option_id": 1862, "option_text": "Designing graphics and posters", "trait_tags": ["Visual-Design", "Digital-Media"]},
            {"option_id": 1863, "option_text": "Filming and editing a short documentary", "trait_tags": ["Film-Broadcast", "Digital-Media"]},
            {"option_id": 1864, "option_text": "Analyzing which posts get the most engagement", "trait_tags": ["Data-Analytics", "Marketing-Sales"]},
            {"option_id": 1865, "option_text": "Managing the social media accounts daily", "trait_tags": ["Marketing-Sales", "Admin-Skill"]},
            {"option_id": 1866, "option_text": "Reaching out to corporate sponsors", "trait_tags": ["Startup-Venture", "People-Skill"]},
            {"option_id": 1867, "option_text": "Building a fundraising website", "trait_tags": ["Web-Dev", "Community-Serve"]},
            {"option_id": 1868, "option_text": "Organizing real-world events to complement the campaign", "trait_tags": ["Admin-Skill", "Community-Serve"]}
        ]
    },
    {
        "question_id": 187,
        "question_text": "Your school's science fair is coming up. What's your project?",
        "category": "Situational - Science Fair",
        "options": [
            {"option_id": 1871, "option_text": "Testing which fertilizer helps plants grow fastest", "trait_tags": ["Agri-Nature", "Lab-Research"]},
            {"option_id": 1872, "option_text": "Building a simple robot that follows a line", "trait_tags": ["Hardware-Systems", "Software-Dev"]},
            {"option_id": 1873, "option_text": "Studying bacteria levels in local water sources", "trait_tags": ["Lab-Research", "Environmental-Sci"]},
            {"option_id": 1874, "option_text": "Creating a solar-powered phone charger", "trait_tags": ["Electrical-Power", "Environmental-Eng"]},
            {"option_id": 1875, "option_text": "Analyzing the nutritional value of local street food", "trait_tags": ["Nutrition-Diet", "Food-Science"]},
            {"option_id": 1876, "option_text": "Building a bridge model that holds the most weight", "trait_tags": ["Civil-Build", "Mechanical-Design"]},
            {"option_id": 1877, "option_text": "An AI program that recognizes Filipino sign language", "trait_tags": ["AI-ML", "Counseling"]},
            {"option_id": 1878, "option_text": "A survey of mental health among SHS students", "trait_tags": ["Counseling", "Data-Analytics"]}
        ]
    },
    {
        "question_id": 188,
        "question_text": "You're assigned to a rural health unit for immersion. What task do you choose?",
        "category": "Situational - Rural Health",
        "options": [
            {"option_id": 1881, "option_text": "Assisting the nurse with check-ups and injections", "trait_tags": ["Patient-Care", "Public-Health"]},
            {"option_id": 1882, "option_text": "Helping the pharmacy sort and distribute medicines", "trait_tags": ["Pharmacy", "Admin-Skill"]},
            {"option_id": 1883, "option_text": "Teaching mothers about proper child nutrition", "trait_tags": ["Nutrition-Diet", "Teaching-Ed"]},
            {"option_id": 1884, "option_text": "Recording patient data in their health information system", "trait_tags": ["Health-Admin", "Software-Dev"]},
            {"option_id": 1885, "option_text": "Running a mini fitness and exercise activity", "trait_tags": ["Sports-Ed", "Rehab-Therapy"]},
            {"option_id": 1886, "option_text": "Conducting a dengue awareness campaign", "trait_tags": ["Public-Health", "Community-Serve"]},
            {"option_id": 1887, "option_text": "Collecting and organizing health survey data", "trait_tags": ["Data-Analytics", "Health-Admin"]},
            {"option_id": 1888, "option_text": "Helping with physical therapy for elderly patients", "trait_tags": ["Rehab-Therapy", "People-Skill"]}
        ]
    },
    {
        "question_id": 189,
        "question_text": "Your professor asks you to lead a capstone project. What topic do you pick?",
        "category": "Situational - Capstone Project",
        "options": [
            {"option_id": 1891, "option_text": "An automated grading system using machine learning", "trait_tags": ["AI-ML", "Software-Dev"]},
            {"option_id": 1892, "option_text": "A mobile health app for rural barangays", "trait_tags": ["Mobile-Dev", "Public-Health"]},
            {"option_id": 1893, "option_text": "A sustainable building design using local materials", "trait_tags": ["Civil-Build", "Environmental-Eng"]},
            {"option_id": 1894, "option_text": "A marketing plan for a local cooperative", "trait_tags": ["Marketing-Sales", "Agri-Nature"]},
            {"option_id": 1895, "option_text": "A documentary about endangered Philippine species", "trait_tags": ["Film-Broadcast", "Environmental-Sci"]},
            {"option_id": 1896, "option_text": "A counseling intervention program for at-risk youth", "trait_tags": ["Counseling", "Social-Work"]},
            {"option_id": 1897, "option_text": "A water quality monitoring system using IoT sensors", "trait_tags": ["Hardware-Systems", "Environmental-Eng"]},
            {"option_id": 1898, "option_text": "A food processing facility plan for local farmers", "trait_tags": ["Food-Science", "Industrial-Ops"]}
        ]
    },
    {
        "question_id": 190,
        "question_text": "If a company hired you right now, which department would you want to work in?",
        "category": "Department Preference",
        "options": [
            {"option_id": 1901, "option_text": "IT / Software Engineering", "trait_tags": ["Software-Dev", "Cloud-Systems"]},
            {"option_id": 1902, "option_text": "Marketing and Communications", "trait_tags": ["Marketing-Sales", "Film-Broadcast"]},
            {"option_id": 1903, "option_text": "Finance and Accounting", "trait_tags": ["Finance-Acct", "Analytical-Skill"]},
            {"option_id": 1904, "option_text": "Human Resources", "trait_tags": ["HR-Management", "People-Skill"]},
            {"option_id": 1905, "option_text": "Research and Development", "trait_tags": ["Lab-Research", "AI-ML"]},
            {"option_id": 1906, "option_text": "Operations and Logistics", "trait_tags": ["Industrial-Ops", "Admin-Skill"]},
            {"option_id": 1907, "option_text": "Legal and Compliance", "trait_tags": ["Legal-Practice", "Admin-Skill"]},
            {"option_id": 1908, "option_text": "Creative / Design", "trait_tags": ["Visual-Design", "Digital-Media"]},
            {"option_id": 1909, "option_text": "Customer Service", "trait_tags": ["People-Skill", "Hospitality-Svc"]},
            {"option_id": 1910, "option_text": "Health and Safety", "trait_tags": ["Public-Health", "Physical-Skill"]}
        ]
    },
    {
        "question_id": 191,
        "question_text": "Your city is planning a new public transportation system. What's your role?",
        "category": "Situational - Urban Planning",
        "options": [
            {"option_id": 1911, "option_text": "Designing the routes and schedules", "trait_tags": ["Civil-Build", "Data-Analytics"]},
            {"option_id": 1912, "option_text": "Building the stations and infrastructure", "trait_tags": ["Civil-Build", "Spatial-Design"]},
            {"option_id": 1913, "option_text": "Developing a mobile app for commuters", "trait_tags": ["Mobile-Dev", "Web-Dev"]},
            {"option_id": 1914, "option_text": "Ensuring it's environmentally sustainable", "trait_tags": ["Environmental-Eng", "Environmental-Sci"]},
            {"option_id": 1915, "option_text": "Managing the PR and public communication", "trait_tags": ["Marketing-Sales", "Community-Serve"]},
            {"option_id": 1916, "option_text": "Handling the budget and financial projections", "trait_tags": ["Finance-Acct", "Admin-Skill"]},
            {"option_id": 1917, "option_text": "Engineering the actual vehicles and systems", "trait_tags": ["Mechanical-Design", "Electrical-Power"]},
            {"option_id": 1918, "option_text": "Studying the traffic data to optimize flow", "trait_tags": ["Data-Analytics", "Industrial-Ops"]}
        ]
    },
    {
        "question_id": 192,
        "question_text": "A classmate faints during PE class. What do you instinctively do?",
        "category": "Situational - Emergency Response",
        "options": [
            {"option_id": 1921, "option_text": "Check their pulse and do CPR if needed", "trait_tags": ["Patient-Care", "Physical-Skill"]},
            {"option_id": 1922, "option_text": "Run and get the school nurse immediately", "trait_tags": ["People-Skill", "Physical-Skill"]},
            {"option_id": 1923, "option_text": "Stay calm and keep the crowd back", "trait_tags": ["Admin-Skill", "People-Skill"]},
            {"option_id": 1924, "option_text": "Document the incident for the school report", "trait_tags": ["Admin-Skill", "Legal-Practice"]},
            {"option_id": 1925, "option_text": "Provide emotional support and reassurance", "trait_tags": ["Counseling", "People-Skill"]},
            {"option_id": 1926, "option_text": "Think about what medical condition might cause this", "trait_tags": ["Medical-Lab", "Analytical-Skill"]},
            {"option_id": 1927, "option_text": "Call 911 and provide location details", "trait_tags": ["Community-Serve", "Admin-Skill"]},
            {"option_id": 1928, "option_text": "Check if it's heat-related and move them to shade", "trait_tags": ["Sports-Ed", "Patient-Care"]}
        ]
    },
    {
        "question_id": 193,
        "question_text": "Which internship opportunity would you grab immediately?",
        "category": "Internship Preference",
        "options": [
            {"option_id": 1931, "option_text": "A tech startup developing new apps", "trait_tags": ["Software-Dev", "Startup-Venture"]},
            {"option_id": 1932, "option_text": "A hospital's research and clinical department", "trait_tags": ["Medical-Lab", "Patient-Care"]},
            {"option_id": 1933, "option_text": "A construction company for a major project", "trait_tags": ["Civil-Build", "Mechanical-Design"]},
            {"option_id": 1934, "option_text": "A bank's financial analysis department", "trait_tags": ["Finance-Acct", "Data-Analytics"]},
            {"option_id": 1935, "option_text": "A TV or film production company", "trait_tags": ["Film-Broadcast", "Digital-Media"]},
            {"option_id": 1936, "option_text": "A government environmental agency", "trait_tags": ["Environmental-Sci", "Community-Serve"]},
            {"option_id": 1937, "option_text": "A hotel or resort chain", "trait_tags": ["Hospitality-Svc", "Tourism-Travel"]},
            {"option_id": 1938, "option_text": "An NGO helping underprivileged communities", "trait_tags": ["Social-Work", "Community-Serve"]},
            {"option_id": 1939, "option_text": "A law firm or legal aid organization", "trait_tags": ["Legal-Practice", "Law-Enforce"]},
            {"option_id": 1940, "option_text": "A sports training facility", "trait_tags": ["Sports-Ed", "Rehab-Therapy"]}
        ]
    },
    {
        "question_id": 194,
        "question_text": "Rate your confidence: 'I can explain complex science topics to anyone.'",
        "category": "Scale - Communication",
        "options": [
            {"option_id": 1941, "option_text": "Strongly Agree - I love teaching and explaining", "trait_tags": ["Teaching-Ed", "Lab-Research"]},
            {"option_id": 1942, "option_text": "Agree - I'm good at simplifying things", "trait_tags": ["Teaching-Ed", "People-Skill"]},
            {"option_id": 1943, "option_text": "Neutral - I prefer doing rather than explaining", "trait_tags": ["Technical-Skill", "Analytical-Skill"]},
            {"option_id": 1944, "option_text": "Disagree - I understand but can't explain well", "trait_tags": ["Lab-Research", "Analytical-Skill"]},
            {"option_id": 1945, "option_text": "Strongly Disagree - Science isn't my area", "trait_tags": ["Creative-Skill", "People-Skill"]}
        ]
    },
    {
        "question_id": 195,
        "question_text": "How comfortable are you working with numbers and calculations?",
        "category": "Scale - Math Comfort",
        "options": [
            {"option_id": 1951, "option_text": "Very comfortable - I love math and statistics", "trait_tags": ["Data-Analytics", "Finance-Acct"]},
            {"option_id": 1952, "option_text": "Comfortable - I use them for practical purposes", "trait_tags": ["Analytical-Skill", "Industrial-Ops"]},
            {"option_id": 1953, "option_text": "Neutral - I can do them when needed", "trait_tags": ["Technical-Skill", "Admin-Skill"]},
            {"option_id": 1954, "option_text": "Uncomfortable - I prefer words over numbers", "trait_tags": ["Creative-Skill", "Teaching-Ed"]},
            {"option_id": 1955, "option_text": "Very uncomfortable - I avoid math whenever possible", "trait_tags": ["Performing-Arts", "People-Skill"]}
        ]
    },
    {
        "question_id": 196,
        "question_text": "How do you feel about working outdoors in the sun and rain?",
        "category": "Scale - Outdoor Work",
        "options": [
            {"option_id": 1961, "option_text": "Love it - I thrive outdoors", "trait_tags": ["Agri-Nature", "Field-Research"]},
            {"option_id": 1962, "option_text": "I'm fine with it when needed", "trait_tags": ["Civil-Build", "Physical-Skill"]},
            {"option_id": 1963, "option_text": "I prefer a mix of indoor and outdoor", "trait_tags": ["Maritime-Sea", "Environmental-Sci"]},
            {"option_id": 1964, "option_text": "I'd rather stay indoors most of the time", "trait_tags": ["Software-Dev", "Lab-Research"]},
            {"option_id": 1965, "option_text": "I strongly prefer air-conditioned office work", "trait_tags": ["Finance-Acct", "Admin-Skill"]}
        ]
    },
    {
        "question_id": 197,
        "question_text": "How important is it for you to help other people in your career?",
        "category": "Scale - Helping Others",
        "options": [
            {"option_id": 1971, "option_text": "Essential — my career should directly help people", "trait_tags": ["Patient-Care", "Social-Work"]},
            {"option_id": 1972, "option_text": "Very important — I want to serve communities", "trait_tags": ["Community-Serve", "Teaching-Ed"]},
            {"option_id": 1973, "option_text": "Somewhat important — I help through my work indirectly", "trait_tags": ["Lab-Research", "Environmental-Sci"]},
            {"option_id": 1974, "option_text": "Not very important — I focus on the work itself", "trait_tags": ["Software-Dev", "Mechanical-Design"]},
            {"option_id": 1975, "option_text": "Not really — I prefer working on things, not people", "trait_tags": ["Hardware-Systems", "Data-Analytics"]}
        ]
    },
    {
        "question_id": 198,
        "question_text": "If your school had a hackathon for social good, what would your team create?",
        "category": "Situational - Social Innovation",
        "options": [
            {"option_id": 1981, "option_text": "A telemedicine app for rural doctors", "trait_tags": ["Mobile-Dev", "Public-Health"]},
            {"option_id": 1982, "option_text": "A disaster early warning system", "trait_tags": ["Hardware-Systems", "Environmental-Sci"]},
            {"option_id": 1983, "option_text": "A crowdsourcing platform for community cleanup", "trait_tags": ["Web-Dev", "Environmental-Eng"]},
            {"option_id": 1984, "option_text": "An AI tutor in Filipino for underprivileged students", "trait_tags": ["AI-ML", "Teaching-Ed"]},
            {"option_id": 1985, "option_text": "A financial literacy game for young Filipinos", "trait_tags": ["Game-Dev", "Finance-Acct"]},
            {"option_id": 1986, "option_text": "A GIS map tracking illegal logging", "trait_tags": ["Data-Analytics", "Agri-Nature"]},
            {"option_id": 1987, "option_text": "A mental health chatbot for students", "trait_tags": ["AI-ML", "Counseling"]},
            {"option_id": 1988, "option_text": "A platform connecting small farmers to buyers", "trait_tags": ["Web-Dev", "Agri-Nature"]}
        ]
    },
    {
        "question_id": 199,
        "question_text": "Which TV show genre do you enjoy most?",
        "category": "Media Preference",
        "options": [
            {"option_id": 1991, "option_text": "Sci-fi and technology (Black Mirror, Westworld)", "trait_tags": ["Software-Dev", "AI-ML"]},
            {"option_id": 1992, "option_text": "Medical dramas (Grey's Anatomy, The Good Doctor)", "trait_tags": ["Patient-Care", "Medical-Lab"]},
            {"option_id": 1993, "option_text": "Crime and legal (CSI, Suits)", "trait_tags": ["Forensic-Sci", "Legal-Practice"]},
            {"option_id": 1994, "option_text": "Business and finance (Shark Tank, The Profit)", "trait_tags": ["Startup-Venture", "Finance-Acct"]},
            {"option_id": 1995, "option_text": "Nature and wildlife (Planet Earth, Our Planet)", "trait_tags": ["Environmental-Sci", "Field-Research"]},
            {"option_id": 1996, "option_text": "Reality competition (MasterChef, Amazing Race)", "trait_tags": ["Culinary-Arts", "Tourism-Travel"]},
            {"option_id": 1997, "option_text": "Creative arts (Project Runway, Abstract)", "trait_tags": ["Visual-Design", "Performing-Arts"]},
            {"option_id": 1998, "option_text": "Sports (ESPN, UFC)", "trait_tags": ["Sports-Ed", "Physical-Skill"]}
        ]
    },
    {
        "question_id": 200,
        "question_text": "What section of a bookstore do you visit first?",
        "category": "Reading Interest",
        "options": [
            {"option_id": 2001, "option_text": "Technology and programming books", "trait_tags": ["Software-Dev", "Web-Dev"]},
            {"option_id": 2002, "option_text": "Medical and health references", "trait_tags": ["Patient-Care", "Pharmacy"]},
            {"option_id": 2003, "option_text": "Engineering and science textbooks", "trait_tags": ["Mechanical-Design", "Lab-Research"]},
            {"option_id": 2004, "option_text": "Business and self-improvement", "trait_tags": ["Startup-Venture", "Marketing-Sales"]},
            {"option_id": 2005, "option_text": "Art, photography, and design books", "trait_tags": ["Visual-Design", "Film-Broadcast"]},
            {"option_id": 2006, "option_text": "Cooking and recipe books", "trait_tags": ["Culinary-Arts", "Nutrition-Diet"]},
            {"option_id": 2007, "option_text": "True crime and mystery novels", "trait_tags": ["Forensic-Sci", "Law-Enforce"]},
            {"option_id": 2008, "option_text": "Psychology and social science", "trait_tags": ["Counseling", "Social-Work"]},
            {"option_id": 2009, "option_text": "Travel and adventure books", "trait_tags": ["Tourism-Travel", "Field-Research"]},
            {"option_id": 2010, "option_text": "Education and teaching guides", "trait_tags": ["Teaching-Ed", "Counseling"]}
        ]
    },
    # ═══════ MARITIME DEDICATED QUESTIONS ═══════
    {
        "question_id": 201,
        "question_text": "You're assigned to a merchant vessel for your first voyage. What department do you want to join?",
        "category": "Situational - Maritime Career Path",
        "options": [
            {"option_id": 2011, "option_text": "Deck department - navigation and watchkeeping", "trait_tags": ["Maritime-Sea", "Physical-Skill"]},
            {"option_id": 2012, "option_text": "Engine department - maintaining propulsion systems", "trait_tags": ["Maritime-Sea", "Mechanical-Design"]},
            {"option_id": 2013, "option_text": "Electrical officer - managing ship electronics", "trait_tags": ["Maritime-Sea", "Electrical-Power"]},
            {"option_id": 2014, "option_text": "Radio officer - communications and safety signals", "trait_tags": ["Maritime-Sea", "Hardware-Systems"]},
            {"option_id": 2015, "option_text": "Steward department - hospitality on cruise ships", "trait_tags": ["Maritime-Sea", "Hospitality-Svc"]},
            {"option_id": 2016, "option_text": "Port operations - managing cargo loading/unloading", "trait_tags": ["Maritime-Sea", "Industrial-Ops"]},
            {"option_id": 2017, "option_text": "Safety officer - emergency procedures and drills", "trait_tags": ["Maritime-Sea", "Community-Serve"]},
            {"option_id": 2018, "option_text": "None of these appeal to me", "trait_tags": []}
        ]
    },
    {
        "question_id": 202,
        "question_text": "What aspect of maritime studies interests you most?",
        "category": "Interest - Maritime Studies",
        "options": [
            {"option_id": 2021, "option_text": "Celestial and electronic navigation", "trait_tags": ["Maritime-Sea", "Physical-Skill"]},
            {"option_id": 2022, "option_text": "Marine diesel engines and ship machinery", "trait_tags": ["Maritime-Sea", "Mechanical-Design"]},
            {"option_id": 2023, "option_text": "International maritime law and regulations", "trait_tags": ["Maritime-Sea", "Legal-Practice"]},
            {"option_id": 2024, "option_text": "Ship stability, construction, and naval architecture", "trait_tags": ["Maritime-Sea", "Civil-Build"]},
            {"option_id": 2025, "option_text": "Cargo handling and logistics management", "trait_tags": ["Maritime-Sea", "Industrial-Ops"]},
            {"option_id": 2026, "option_text": "Marine environmental protection", "trait_tags": ["Maritime-Sea", "Environmental-Sci"]},
            {"option_id": 2027, "option_text": "Meteorology and weather routing at sea", "trait_tags": ["Maritime-Sea", "Field-Research"]},
            {"option_id": 2028, "option_text": "Seamanship and survival at sea", "trait_tags": ["Maritime-Sea", "Physical-Skill"]}
        ]
    },
    {
        "question_id": 203,
        "question_text": "A typhoon is approaching while your ship is in Philippine waters. What do you focus on?",
        "category": "Situational - Maritime Safety",
        "options": [
            {"option_id": 2031, "option_text": "Plot an alternative course to avoid the typhoon", "trait_tags": ["Maritime-Sea", "Physical-Skill"]},
            {"option_id": 2032, "option_text": "Secure the engine room and check all machinery", "trait_tags": ["Maritime-Sea", "Mechanical-Design"]},
            {"option_id": 2033, "option_text": "Coordinate with MARINA and coast guard for updates", "trait_tags": ["Maritime-Sea", "Community-Serve"]},
            {"option_id": 2034, "option_text": "Organize the crew for emergency procedures", "trait_tags": ["Maritime-Sea", "People-Skill"]},
            {"option_id": 2035, "option_text": "Check all safety equipment - lifeboats, life jackets", "trait_tags": ["Maritime-Sea", "Physical-Skill"]},
            {"option_id": 2036, "option_text": "Monitor weather radar and satellite data", "trait_tags": ["Maritime-Sea", "Data-Analytics"]},
            {"option_id": 2037, "option_text": "Secure all cargo to prevent shifting", "trait_tags": ["Maritime-Sea", "Industrial-Ops"]},
            {"option_id": 2038, "option_text": "Prepare medical supplies for potential injuries", "trait_tags": ["Patient-Care", "Maritime-Sea"]}
        ]
    },
    {
        "question_id": 204,
        "question_text": "Why does a career at sea appeal to you?",
        "category": "Motivation - Maritime",
        "options": [
            {"option_id": 2041, "option_text": "Traveling to different countries and seeing the world", "trait_tags": ["Maritime-Sea", "Tourism-Travel"]},
            {"option_id": 2042, "option_text": "High salary potential especially working abroad", "trait_tags": ["Maritime-Sea", "Physical-Skill"]},
            {"option_id": 2043, "option_text": "Challenging work that tests my physical and mental limits", "trait_tags": ["Maritime-Sea", "Physical-Skill"]},
            {"option_id": 2044, "option_text": "Following a family tradition of seafaring", "trait_tags": ["Maritime-Sea", "Community-Serve"]},
            {"option_id": 2045, "option_text": "Working with advanced ship technology and systems", "trait_tags": ["Maritime-Sea", "Hardware-Systems"]},
            {"option_id": 2046, "option_text": "Being part of global trade and shipping industry", "trait_tags": ["Maritime-Sea", "Industrial-Ops"]},
            {"option_id": 2047, "option_text": "The discipline and structured life on a ship", "trait_tags": ["Maritime-Sea", "Admin-Skill"]},
            {"option_id": 2048, "option_text": "A career at sea doesn't really appeal to me", "trait_tags": []}
        ]
    },
    {
        "question_id": 205,
        "question_text": "You're choosing between two maritime academies. Which program feature matters most?",
        "category": "Preference - Maritime Training",
        "options": [
            {"option_id": 2051, "option_text": "More time on training ships with real sea experience", "trait_tags": ["Maritime-Sea", "Physical-Skill"]},
            {"option_id": 2052, "option_text": "Strong engine room simulation and workshop facilities", "trait_tags": ["Maritime-Sea", "Mechanical-Design"]},
            {"option_id": 2053, "option_text": "Modern bridge simulator for navigation training", "trait_tags": ["Maritime-Sea", "Hardware-Systems"]},
            {"option_id": 2054, "option_text": "Good connections with international shipping companies", "trait_tags": ["Maritime-Sea", "Marketing-Sales"]},
            {"option_id": 2055, "option_text": "Strong MARINA board exam pass rate", "trait_tags": ["Maritime-Sea", "Analytical-Skill"]},
            {"option_id": 2056, "option_text": "Additional certifications like GMDSS, STCW", "trait_tags": ["Maritime-Sea", "Technical-Skill"]},
            {"option_id": 2057, "option_text": "Focus on marine environmental protection", "trait_tags": ["Maritime-Sea", "Environmental-Sci"]},
            {"option_id": 2058, "option_text": "Dual degree option with business or management", "trait_tags": ["Maritime-Sea", "Admin-Skill"]}
        ]
    }
]

# ==================== MULTI-TRAIT WEIGHT ENRICHMENT ====================
# Each option maps to multiple traits with weights so recommendations
# aren't limited to a single dimension. Primary trait = 1.0, secondary
# traits have lower weights reflecting partial relevance.

TRAIT_SECONDARY_MAP = {
    "Patient-Care":      [("People-Skill", 0.4), ("Rehab-Therapy", 0.2)],
    "Medical-Lab":       [("Lab-Research", 0.4), ("Patient-Care", 0.2)],
    "Rehab-Therapy":     [("Patient-Care", 0.4), ("People-Skill", 0.2)],
    "Health-Admin":      [("Admin-Skill", 0.4), ("Patient-Care", 0.2)],
    "Software-Dev":      [("Data-Analytics", 0.3), ("Hardware-Systems", 0.2)],
    "Hardware-Systems":  [("Software-Dev", 0.3), ("Electrical-Power", 0.2)],
    "Data-Analytics":    [("Software-Dev", 0.3), ("Lab-Research", 0.2)],
    "Cyber-Defense":     [("Software-Dev", 0.3), ("Law-Enforce", 0.2)],
    "Digital-Media":     [("Visual-Design", 0.4), ("Software-Dev", 0.2)],
    "Civil-Build":       [("Spatial-Design", 0.3), ("Mechanical-Design", 0.2)],
    "Mechanical-Design": [("Civil-Build", 0.3), ("Industrial-Ops", 0.2)],
    "Electrical-Power":  [("Hardware-Systems", 0.3), ("Mechanical-Design", 0.2)],
    "Industrial-Ops":    [("Mechanical-Design", 0.3), ("Admin-Skill", 0.2)],
    "Spatial-Design":    [("Visual-Design", 0.3), ("Civil-Build", 0.2)],
    "Finance-Acct":      [("Admin-Skill", 0.3), ("Data-Analytics", 0.2)],
    "Marketing-Sales":   [("Startup-Venture", 0.3), ("People-Skill", 0.2)],
    "Startup-Venture":   [("Marketing-Sales", 0.3), ("Finance-Acct", 0.2)],
    "Admin-Skill":       [("Finance-Acct", 0.3), ("People-Skill", 0.2)],
    "Teaching-Ed":       [("People-Skill", 0.4), ("Community-Serve", 0.2)],
    "Visual-Design":     [("Digital-Media", 0.3), ("Creative-Skill", 0.2)],
    "Creative-Skill":    [("Visual-Design", 0.3), ("Digital-Media", 0.2)],
    "Law-Enforce":       [("Community-Serve", 0.3), ("Physical-Skill", 0.2)],
    "Community-Serve":   [("People-Skill", 0.3), ("Teaching-Ed", 0.2)],
    "Maritime-Sea":      [("Mechanical-Design", 0.3), ("Physical-Skill", 0.2)],
    "Agri-Nature":       [("Field-Research", 0.3), ("Lab-Research", 0.2)],
    "Hospitality-Svc":   [("People-Skill", 0.3), ("Admin-Skill", 0.2)],
    "Lab-Research":      [("Data-Analytics", 0.3), ("Medical-Lab", 0.2)],
    "Field-Research":    [("Lab-Research", 0.3), ("Agri-Nature", 0.2)],
    "People-Skill":      [("Teaching-Ed", 0.3), ("Community-Serve", 0.2)],
    "Technical-Skill":   [("Hardware-Systems", 0.3), ("Mechanical-Design", 0.2)],
    "Physical-Skill":    [("Law-Enforce", 0.3), ("Maritime-Sea", 0.2)],
    "Analytical-Skill":  [("Data-Analytics", 0.3), ("Lab-Research", 0.2)],
    # --- New expanded traits ---
    "Web-Dev":           [("Software-Dev", 0.4), ("Digital-Media", 0.2)],
    "Mobile-Dev":        [("Software-Dev", 0.4), ("Web-Dev", 0.2)],
    "Game-Dev":          [("Software-Dev", 0.3), ("Animation-3D", 0.3)],
    "AI-ML":             [("Software-Dev", 0.3), ("Data-Analytics", 0.3)],
    "Cloud-Systems":     [("Software-Dev", 0.3), ("Cyber-Defense", 0.2)],
    "Pharmacy":          [("Medical-Lab", 0.4), ("Patient-Care", 0.2)],
    "Public-Health":     [("Community-Serve", 0.3), ("Patient-Care", 0.2)],
    "Nutrition-Diet":    [("Food-Science", 0.3), ("Patient-Care", 0.2)],
    "Environmental-Eng": [("Environmental-Sci", 0.4), ("Civil-Build", 0.2)],
    "HR-Management":     [("People-Skill", 0.4), ("Admin-Skill", 0.2)],
    "Counseling":        [("People-Skill", 0.4), ("Rehab-Therapy", 0.2)],
    "Sports-Ed":         [("Physical-Skill", 0.4), ("Teaching-Ed", 0.2)],
    "Performing-Arts":   [("Creative-Skill", 0.4), ("Visual-Design", 0.2)],
    "Film-Broadcast":    [("Digital-Media", 0.4), ("Creative-Skill", 0.2)],
    "Animation-3D":      [("Digital-Media", 0.3), ("Visual-Design", 0.3)],
    "Environmental-Sci": [("Field-Research", 0.3), ("Lab-Research", 0.2)],
    "Food-Science":      [("Lab-Research", 0.3), ("Nutrition-Diet", 0.2)],
    "Forensic-Sci":      [("Lab-Research", 0.3), ("Law-Enforce", 0.3)],
    "Legal-Practice":    [("Law-Enforce", 0.3), ("Community-Serve", 0.2)],
    "Social-Work":       [("Community-Serve", 0.3), ("Counseling", 0.3)],
    "Tourism-Travel":    [("Hospitality-Svc", 0.4), ("People-Skill", 0.2)],
    "Culinary-Arts":     [("Hospitality-Svc", 0.3), ("Food-Science", 0.2)],
}


def _enrich_options_with_traits():
    """Add weighted multi-trait 'traits' dict to every option in the pool.
    Handles both old format (trait_tag: str) and new format (trait_tags: list)."""
    for question in QUESTIONS_POOL_ENHANCED:
        for option in question.get("options", []):
            # New format: trait_tags list
            trait_tags = option.get("trait_tags", [])
            if trait_tags:
                traits = {}
                for i, tag in enumerate(trait_tags):
                    traits[tag] = 1.0 if i == 0 else 0.6
                    # Also add secondary traits from the map
                    for secondary_tag, weight in TRAIT_SECONDARY_MAP.get(tag, []):
                        if secondary_tag not in traits:
                            sec_weight = weight if i == 0 else weight * 0.5
                            traits[secondary_tag] = sec_weight
                option["traits"] = traits
                # Set trait_tag to first tag for backward compatibility
                if "trait_tag" not in option and trait_tags:
                    option["trait_tag"] = trait_tags[0]
                continue

            # Old format: single trait_tag
            primary = option.get("trait_tag")
            if not primary:
                continue
            traits = {primary: 1.0}
            for secondary_tag, weight in TRAIT_SECONDARY_MAP.get(primary, []):
                traits[secondary_tag] = weight
            option["traits"] = traits


_enrich_options_with_traits()


# Verify trait coverage
if __name__ == "__main__":
    trait_counts = {}
    for q in QUESTIONS_POOL_ENHANCED:
        for opt in q.get("options", []):
            trait = opt.get("trait_tag")
            if trait:
                trait_counts[trait] = trait_counts.get(trait, 0) + 1
    
    print("=" * 60)
    print("ENHANCED QUESTIONS - TRAIT COVERAGE (8-10 options each)")
    print("=" * 60)
    for trait, count in sorted(trait_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"{trait}: {count} options")
    print(f"\nTotal: {len(trait_counts)} unique traits across {len(QUESTIONS_POOL_ENHANCED)} questions")
    print(f"Average options per question: {sum(len(q['options']) for q in QUESTIONS_POOL_ENHANCED) / len(QUESTIONS_POOL_ENHANCED):.1f}")
    
    # Show multi-trait example
    example = QUESTIONS_POOL_ENHANCED[0]["options"][0]
    print(f"\nExample multi-trait option: {example.get('option_text')}")
    print(f"  traits: {example.get('traits')}")
