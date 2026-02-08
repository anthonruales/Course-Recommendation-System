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

    # ==================== HEALTHCARE SPECIALIZATION ====================
    {
        "question_id": 6,
        "question_text": "In HEALTHCARE, which specific role appeals to you most?",
        "category": "Healthcare Career",
        "options": [
            {"option_id": 51, "option_text": "Registered Nurse - bedside care, medication, patient monitoring", "trait_tag": "Patient-Care"},
            {"option_id": 52, "option_text": "Midwife - assisting mothers during pregnancy and childbirth", "trait_tag": "Patient-Care"},
            {"option_id": 53, "option_text": "Medical Technologist - lab tests, blood analysis, diagnostics", "trait_tag": "Medical-Lab"},
            {"option_id": 54, "option_text": "Pharmacist - preparing medicines and advising on drugs", "trait_tag": "Medical-Lab"},
            {"option_id": 55, "option_text": "Physical Therapist - rehabilitation exercises for recovery", "trait_tag": "Rehab-Therapy"},
            {"option_id": 56, "option_text": "Occupational Therapist - helping with daily living skills", "trait_tag": "Rehab-Therapy"},
            {"option_id": 57, "option_text": "Radiologic Technologist - X-rays and medical imaging", "trait_tag": "Medical-Lab"},
            {"option_id": 58, "option_text": "Nutritionist/Dietitian - meal planning and nutrition", "trait_tag": "Patient-Care"},
            {"option_id": 59, "option_text": "Health Information Manager - medical records systems", "trait_tag": "Health-Admin"},
            {"option_id": 60, "option_text": "None - I'm not interested in healthcare", "trait_tag": "Software-Dev"}
        ]
    },
    {
        "question_id": 7,
        "question_text": "Which healthcare scenario sounds most rewarding to you?",
        "category": "Healthcare Scenario",
        "options": [
            {"option_id": 61, "option_text": "Holding a patient's hand and monitoring their recovery", "trait_tag": "Patient-Care"},
            {"option_id": 62, "option_text": "Analyzing a blood sample to diagnose an illness", "trait_tag": "Medical-Lab"},
            {"option_id": 63, "option_text": "Helping an accident victim walk again through therapy", "trait_tag": "Rehab-Therapy"},
            {"option_id": 64, "option_text": "Delivering a baby and supporting the new mother", "trait_tag": "Patient-Care"},
            {"option_id": 65, "option_text": "Operating an X-ray machine to detect fractures", "trait_tag": "Medical-Lab"},
            {"option_id": 66, "option_text": "Creating a diet plan for a diabetic patient", "trait_tag": "Patient-Care"},
            {"option_id": 67, "option_text": "Managing a hospital's electronic records system", "trait_tag": "Health-Admin"},
            {"option_id": 68, "option_text": "Dispensing the right medication at a pharmacy", "trait_tag": "Medical-Lab"},
            {"option_id": 69, "option_text": "Teaching a stroke patient to use utensils again", "trait_tag": "Rehab-Therapy"},
            {"option_id": 70, "option_text": "None of these interest me", "trait_tag": "Finance-Acct"}
        ]
    },

    # ==================== TECHNOLOGY SPECIALIZATION ====================
    {
        "question_id": 8,
        "question_text": "In TECHNOLOGY, which specific role appeals to you most?",
        "category": "Technology Career",
        "options": [
            {"option_id": 71, "option_text": "Software Developer - building apps, websites, systems", "trait_tag": "Software-Dev"},
            {"option_id": 72, "option_text": "Web Developer - creating and maintaining websites", "trait_tag": "Software-Dev"},
            {"option_id": 73, "option_text": "Computer Engineer - designing computer hardware", "trait_tag": "Hardware-Systems"},
            {"option_id": 74, "option_text": "Network Administrator - managing IT infrastructure", "trait_tag": "Hardware-Systems"},
            {"option_id": 75, "option_text": "Data Scientist - analyzing big data and AI", "trait_tag": "Data-Analytics"},
            {"option_id": 76, "option_text": "Cybersecurity Analyst - protecting against hackers", "trait_tag": "Cyber-Defense"},
            {"option_id": 77, "option_text": "Game Developer - creating video games", "trait_tag": "Digital-Media"},
            {"option_id": 78, "option_text": "UI/UX Designer - designing user interfaces", "trait_tag": "Digital-Media"},
            {"option_id": 79, "option_text": "Database Administrator - managing data systems", "trait_tag": "Data-Analytics"},
            {"option_id": 80, "option_text": "None - I prefer non-technology careers", "trait_tag": "Patient-Care"}
        ]
    },
    {
        "question_id": 9,
        "question_text": "Which tech project would you most enjoy working on?",
        "category": "Technology Project",
        "options": [
            {"option_id": 81, "option_text": "Building a mobile app from scratch", "trait_tag": "Software-Dev"},
            {"option_id": 82, "option_text": "Creating an e-commerce website", "trait_tag": "Software-Dev"},
            {"option_id": 83, "option_text": "Assembling and configuring a server system", "trait_tag": "Hardware-Systems"},
            {"option_id": 84, "option_text": "Designing a circuit board or robot", "trait_tag": "Hardware-Systems"},
            {"option_id": 85, "option_text": "Creating an AI model that predicts trends", "trait_tag": "Data-Analytics"},
            {"option_id": 86, "option_text": "Penetration testing to find security vulnerabilities", "trait_tag": "Cyber-Defense"},
            {"option_id": 87, "option_text": "Developing a 3D video game", "trait_tag": "Digital-Media"},
            {"option_id": 88, "option_text": "Creating animated videos or visual effects", "trait_tag": "Digital-Media"},
            {"option_id": 89, "option_text": "Building a dashboard to visualize data", "trait_tag": "Data-Analytics"},
            {"option_id": 90, "option_text": "None of these interest me", "trait_tag": "Teaching-Ed"}
        ]
    },

    # ==================== ENGINEERING SPECIALIZATION ====================
    {
        "question_id": 10,
        "question_text": "In ENGINEERING, which specific field appeals to you most?",
        "category": "Engineering Career",
        "options": [
            {"option_id": 91, "option_text": "Civil Engineer - bridges, roads, buildings", "trait_tag": "Civil-Build"},
            {"option_id": 92, "option_text": "Structural Engineer - building foundations and frames", "trait_tag": "Civil-Build"},
            {"option_id": 93, "option_text": "Mechanical Engineer - machines and systems", "trait_tag": "Mechanical-Design"},
            {"option_id": 94, "option_text": "Automotive Engineer - vehicles and transportation", "trait_tag": "Mechanical-Design"},
            {"option_id": 95, "option_text": "Electrical Engineer - power systems", "trait_tag": "Electrical-Power"},
            {"option_id": 96, "option_text": "Electronics Engineer - circuits and devices", "trait_tag": "Electrical-Power"},
            {"option_id": 97, "option_text": "Industrial Engineer - optimizing processes", "trait_tag": "Industrial-Ops"},
            {"option_id": 98, "option_text": "Chemical Engineer - chemical processes", "trait_tag": "Lab-Research"},
            {"option_id": 99, "option_text": "Architect - designing buildings and spaces", "trait_tag": "Spatial-Design"},
            {"option_id": 100, "option_text": "None - I prefer non-engineering careers", "trait_tag": "Teaching-Ed"}
        ]
    },
    {
        "question_id": 11,
        "question_text": "Which engineering project would excite you the most?",
        "category": "Engineering Project",
        "options": [
            {"option_id": 101, "option_text": "Designing a new highway or bridge", "trait_tag": "Civil-Build"},
            {"option_id": 102, "option_text": "Building a new shopping mall or office tower", "trait_tag": "Civil-Build"},
            {"option_id": 103, "option_text": "Creating a new engine design for vehicles", "trait_tag": "Mechanical-Design"},
            {"option_id": 104, "option_text": "Developing an HVAC system for a building", "trait_tag": "Mechanical-Design"},
            {"option_id": 105, "option_text": "Setting up a solar power plant", "trait_tag": "Electrical-Power"},
            {"option_id": 106, "option_text": "Designing the electrical system for a factory", "trait_tag": "Electrical-Power"},
            {"option_id": 107, "option_text": "Optimizing a manufacturing production line", "trait_tag": "Industrial-Ops"},
            {"option_id": 108, "option_text": "Designing the interior of a luxury home", "trait_tag": "Spatial-Design"},
            {"option_id": 109, "option_text": "Creating floor plans for a resort", "trait_tag": "Spatial-Design"},
            {"option_id": 110, "option_text": "None of these interest me", "trait_tag": "Patient-Care"}
        ]
    },

    # ==================== BUSINESS SPECIALIZATION ====================
    {
        "question_id": 12,
        "question_text": "In BUSINESS, which specific role appeals to you most?",
        "category": "Business Career",
        "options": [
            {"option_id": 111, "option_text": "Accountant - financial statements, auditing, taxes", "trait_tag": "Finance-Acct"},
            {"option_id": 112, "option_text": "Financial Analyst - investment analysis", "trait_tag": "Finance-Acct"},
            {"option_id": 113, "option_text": "Bank Manager - banking operations", "trait_tag": "Finance-Acct"},
            {"option_id": 114, "option_text": "Marketing Manager - advertising campaigns", "trait_tag": "Marketing-Sales"},
            {"option_id": 115, "option_text": "Sales Manager - selling products/services", "trait_tag": "Marketing-Sales"},
            {"option_id": 116, "option_text": "Entrepreneur - starting my own business", "trait_tag": "Startup-Venture"},
            {"option_id": 117, "option_text": "Operations Manager - managing workflows", "trait_tag": "Industrial-Ops"},
            {"option_id": 118, "option_text": "HR Manager - hiring and employee relations", "trait_tag": "People-Skill"},
            {"option_id": 119, "option_text": "Real Estate Agent - buying/selling properties", "trait_tag": "Marketing-Sales"},
            {"option_id": 120, "option_text": "None - I prefer non-business careers", "trait_tag": "Patient-Care"}
        ]
    },
    {
        "question_id": 13,
        "question_text": "Which business activity would you enjoy most?",
        "category": "Business Activity",
        "options": [
            {"option_id": 121, "option_text": "Preparing monthly financial reports", "trait_tag": "Finance-Acct"},
            {"option_id": 122, "option_text": "Auditing a company's financial records", "trait_tag": "Finance-Acct"},
            {"option_id": 123, "option_text": "Creating a viral marketing campaign", "trait_tag": "Marketing-Sales"},
            {"option_id": 124, "option_text": "Closing a big sales deal with a client", "trait_tag": "Marketing-Sales"},
            {"option_id": 125, "option_text": "Pitching a startup idea to investors", "trait_tag": "Startup-Venture"},
            {"option_id": 126, "option_text": "Building a business plan from scratch", "trait_tag": "Startup-Venture"},
            {"option_id": 127, "option_text": "Improving factory efficiency by 30%", "trait_tag": "Industrial-Ops"},
            {"option_id": 128, "option_text": "Negotiating a property sale", "trait_tag": "Marketing-Sales"},
            {"option_id": 129, "option_text": "Conducting job interviews", "trait_tag": "People-Skill"},
            {"option_id": 130, "option_text": "None of these interest me", "trait_tag": "Visual-Design"}
        ]
    },

    # ==================== PUBLIC SERVICE SPECIALIZATION ====================
    {
        "question_id": 14,
        "question_text": "In PUBLIC SERVICE, which specific role appeals to you most?",
        "category": "Public Service Career",
        "options": [
            {"option_id": 131, "option_text": "Police Officer - patrolling, maintaining peace", "trait_tag": "Law-Enforce"},
            {"option_id": 132, "option_text": "Detective - investigating crimes", "trait_tag": "Law-Enforce"},
            {"option_id": 133, "option_text": "Forensic Scientist - analyzing crime evidence", "trait_tag": "Law-Enforce"},
            {"option_id": 134, "option_text": "Lawyer - representing clients in court", "trait_tag": "Admin-Skill"},
            {"option_id": 135, "option_text": "Social Worker - helping families in need", "trait_tag": "Community-Serve"},
            {"option_id": 136, "option_text": "Government Employee - public administration", "trait_tag": "Community-Serve"},
            {"option_id": 137, "option_text": "Politician - creating policies and laws", "trait_tag": "Community-Serve"},
            {"option_id": 138, "option_text": "NGO Worker - humanitarian assistance", "trait_tag": "Community-Serve"},
            {"option_id": 139, "option_text": "Military Officer - national defense", "trait_tag": "Law-Enforce"},
            {"option_id": 140, "option_text": "None - I prefer private sector careers", "trait_tag": "Finance-Acct"}
        ]
    },
    {
        "question_id": 15,
        "question_text": "Which public service scenario appeals to you most?",
        "category": "Public Service Scenario",
        "options": [
            {"option_id": 141, "option_text": "Arresting a criminal and protecting victims", "trait_tag": "Law-Enforce"},
            {"option_id": 142, "option_text": "Solving a murder case through investigation", "trait_tag": "Law-Enforce"},
            {"option_id": 143, "option_text": "Analyzing DNA evidence in a crime lab", "trait_tag": "Law-Enforce"},
            {"option_id": 144, "option_text": "Helping a poor family get housing assistance", "trait_tag": "Community-Serve"},
            {"option_id": 145, "option_text": "Developing a government program for farmers", "trait_tag": "Community-Serve"},
            {"option_id": 146, "option_text": "Representing a client in a court trial", "trait_tag": "Admin-Skill"},
            {"option_id": 147, "option_text": "Providing disaster relief to typhoon victims", "trait_tag": "Community-Serve"},
            {"option_id": 148, "option_text": "Training new police recruits", "trait_tag": "Law-Enforce"},
            {"option_id": 149, "option_text": "Counseling a troubled teenager", "trait_tag": "People-Skill"},
            {"option_id": 150, "option_text": "None of these interest me", "trait_tag": "Software-Dev"}
        ]
    },

    # ==================== EDUCATION SPECIALIZATION ====================
    {
        "question_id": 16,
        "question_text": "In EDUCATION, which teaching role appeals to you most?",
        "category": "Education Career",
        "options": [
            {"option_id": 151, "option_text": "Elementary Teacher - teaching young children", "trait_tag": "Teaching-Ed"},
            {"option_id": 152, "option_text": "High School Teacher - teaching teenagers", "trait_tag": "Teaching-Ed"},
            {"option_id": 153, "option_text": "College Professor - teaching adults", "trait_tag": "Teaching-Ed"},
            {"option_id": 154, "option_text": "Special Education Teacher - students with disabilities", "trait_tag": "Teaching-Ed"},
            {"option_id": 155, "option_text": "Preschool Teacher - early childhood education", "trait_tag": "Teaching-Ed"},
            {"option_id": 156, "option_text": "Vocational Trainer - teaching technical skills", "trait_tag": "Technical-Skill"},
            {"option_id": 157, "option_text": "School Guidance Counselor - student counseling", "trait_tag": "People-Skill"},
            {"option_id": 158, "option_text": "School Administrator - managing schools", "trait_tag": "Admin-Skill"},
            {"option_id": 159, "option_text": "Corporate Trainer - training employees", "trait_tag": "Teaching-Ed"},
            {"option_id": 160, "option_text": "None - I don't want to teach", "trait_tag": "Software-Dev"}
        ]
    },
    {
        "question_id": 17,
        "question_text": "Which subject would you most enjoy teaching?",
        "category": "Teaching Subject",
        "options": [
            {"option_id": 161, "option_text": "Mathematics - algebra, calculus, geometry", "trait_tag": "Data-Analytics"},
            {"option_id": 162, "option_text": "Science - biology, chemistry, physics", "trait_tag": "Lab-Research"},
            {"option_id": 163, "option_text": "English - grammar, literature, writing", "trait_tag": "Teaching-Ed"},
            {"option_id": 164, "option_text": "Filipino - language and literature", "trait_tag": "Teaching-Ed"},
            {"option_id": 165, "option_text": "Social Studies - history, economics", "trait_tag": "Community-Serve"},
            {"option_id": 166, "option_text": "Computer/Technology - IT skills", "trait_tag": "Software-Dev"},
            {"option_id": 167, "option_text": "Arts - visual arts, music, drama", "trait_tag": "Visual-Design"},
            {"option_id": 168, "option_text": "Physical Education - sports, fitness", "trait_tag": "Physical-Skill"},
            {"option_id": 169, "option_text": "TLE - technical/vocational skills", "trait_tag": "Technical-Skill"},
            {"option_id": 170, "option_text": "I don't want to teach any subject", "trait_tag": "Finance-Acct"}
        ]
    },

    # ==================== ARTS & DESIGN SPECIALIZATION ====================
    {
        "question_id": 18,
        "question_text": "In ARTS & DESIGN, which specific role appeals to you most?",
        "category": "Arts Career",
        "options": [
            {"option_id": 171, "option_text": "Graphic Designer - logos, posters, branding", "trait_tag": "Visual-Design"},
            {"option_id": 172, "option_text": "Fine Artist - paintings, sculptures", "trait_tag": "Visual-Design"},
            {"option_id": 173, "option_text": "Animator - 2D/3D animation", "trait_tag": "Digital-Media"},
            {"option_id": 174, "option_text": "Video Editor - film and video production", "trait_tag": "Digital-Media"},
            {"option_id": 175, "option_text": "Interior Designer - room and space design", "trait_tag": "Spatial-Design"},
            {"option_id": 176, "option_text": "Fashion Designer - clothing and accessories", "trait_tag": "Visual-Design"},
            {"option_id": 177, "option_text": "Musician - performing or composing music", "trait_tag": "Creative-Skill"},
            {"option_id": 178, "option_text": "Actor/Performer - theater, film, TV", "trait_tag": "Creative-Skill"},
            {"option_id": 179, "option_text": "Photographer - capturing images", "trait_tag": "Visual-Design"},
            {"option_id": 180, "option_text": "None - I prefer non-creative careers", "trait_tag": "Finance-Acct"}
        ]
    },
    {
        "question_id": 19,
        "question_text": "Which creative project would you most enjoy working on?",
        "category": "Creative Project",
        "options": [
            {"option_id": 181, "option_text": "Designing a company logo and brand identity", "trait_tag": "Visual-Design"},
            {"option_id": 182, "option_text": "Creating a painting for an art gallery", "trait_tag": "Visual-Design"},
            {"option_id": 183, "option_text": "Making an animated short film", "trait_tag": "Digital-Media"},
            {"option_id": 184, "option_text": "Editing a music video", "trait_tag": "Digital-Media"},
            {"option_id": 185, "option_text": "Redesigning a living room interior", "trait_tag": "Spatial-Design"},
            {"option_id": 186, "option_text": "Designing a fashion collection", "trait_tag": "Visual-Design"},
            {"option_id": 187, "option_text": "Composing music for a film", "trait_tag": "Creative-Skill"},
            {"option_id": 188, "option_text": "Acting in a theater production", "trait_tag": "Creative-Skill"},
            {"option_id": 189, "option_text": "Shooting a wedding photography session", "trait_tag": "Visual-Design"},
            {"option_id": 190, "option_text": "None of these interest me", "trait_tag": "Civil-Build"}
        ]
    },

    # ==================== MARITIME SPECIALIZATION ====================
    {
        "question_id": 20,
        "question_text": "In MARITIME careers, which role appeals to you most?",
        "category": "Maritime Career",
        "options": [
            {"option_id": 191, "option_text": "Ship Captain - navigating vessels across oceans", "trait_tag": "Maritime-Sea"},
            {"option_id": 192, "option_text": "Deck Officer - ship operations and safety", "trait_tag": "Maritime-Sea"},
            {"option_id": 193, "option_text": "Marine Engineer - ship engine and machinery", "trait_tag": "Maritime-Sea"},
            {"option_id": 194, "option_text": "Port Manager - harbor and dock operations", "trait_tag": "Maritime-Sea"},
            {"option_id": 195, "option_text": "Ship Electrician - maritime electrical systems", "trait_tag": "Electrical-Power"},
            {"option_id": 196, "option_text": "Cruise Ship Staff - hospitality at sea", "trait_tag": "Hospitality-Svc"},
            {"option_id": 197, "option_text": "Coast Guard Officer - maritime safety and rescue", "trait_tag": "Law-Enforce"},
            {"option_id": 198, "option_text": "Marine Biologist - ocean life research", "trait_tag": "Field-Research"},
            {"option_id": 199, "option_text": "Fisheries Manager - fishing operations", "trait_tag": "Agri-Nature"},
            {"option_id": 200, "option_text": "None - I prefer land-based careers", "trait_tag": "Software-Dev"}
        ]
    },

    # ==================== AGRICULTURE SPECIALIZATION ====================
    {
        "question_id": 21,
        "question_text": "In AGRICULTURE, which role appeals to you most?",
        "category": "Agriculture Career",
        "options": [
            {"option_id": 201, "option_text": "Farm Manager - crop and livestock management", "trait_tag": "Agri-Nature"},
            {"option_id": 202, "option_text": "Agronomist - soil and crop science", "trait_tag": "Agri-Nature"},
            {"option_id": 203, "option_text": "Veterinarian - animal healthcare", "trait_tag": "Patient-Care"},
            {"option_id": 204, "option_text": "Forester - forest conservation and management", "trait_tag": "Agri-Nature"},
            {"option_id": 205, "option_text": "Agricultural Engineer - farm machinery", "trait_tag": "Mechanical-Design"},
            {"option_id": 206, "option_text": "Food Technologist - food processing", "trait_tag": "Lab-Research"},
            {"option_id": 207, "option_text": "Environmental Scientist - ecology research", "trait_tag": "Field-Research"},
            {"option_id": 208, "option_text": "Aquaculturist - fish farming", "trait_tag": "Agri-Nature"},
            {"option_id": 209, "option_text": "Agricultural Extension Worker - farmer training", "trait_tag": "Teaching-Ed"},
            {"option_id": 210, "option_text": "None - I prefer urban careers", "trait_tag": "Software-Dev"}
        ]
    },

    # ==================== HOSPITALITY SPECIALIZATION ====================
    {
        "question_id": 22,
        "question_text": "In HOSPITALITY & TOURISM, which role appeals to you most?",
        "category": "Hospitality Career",
        "options": [
            {"option_id": 211, "option_text": "Hotel Manager - hotel operations", "trait_tag": "Hospitality-Svc"},
            {"option_id": 212, "option_text": "Tour Guide - showing tourists around", "trait_tag": "Hospitality-Svc"},
            {"option_id": 213, "option_text": "Event Planner - organizing events and weddings", "trait_tag": "Hospitality-Svc"},
            {"option_id": 214, "option_text": "Chef - cooking in restaurants", "trait_tag": "Hospitality-Svc"},
            {"option_id": 215, "option_text": "Restaurant Manager - food service management", "trait_tag": "Hospitality-Svc"},
            {"option_id": 216, "option_text": "Travel Agent - booking trips and vacations", "trait_tag": "Hospitality-Svc"},
            {"option_id": 217, "option_text": "Flight Attendant - airline cabin crew", "trait_tag": "Hospitality-Svc"},
            {"option_id": 218, "option_text": "Resort Activities Coordinator - guest entertainment", "trait_tag": "Hospitality-Svc"},
            {"option_id": 219, "option_text": "Bartender/Barista - beverage service", "trait_tag": "Hospitality-Svc"},
            {"option_id": 220, "option_text": "None - I prefer other industries", "trait_tag": "Software-Dev"}
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
            {"option_id": 258, "option_text": "I prefer applied math (like accounting)", "trait_tag": "Finance-Acct"},
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
            {"option_id": 301, "option_text": "Science (Biology, Chemistry, Physics)", "trait_tag": "Lab-Research"},
            {"option_id": 302, "option_text": "Mathematics (Algebra, Calculus, Statistics)", "trait_tag": "Data-Analytics"},
            {"option_id": 303, "option_text": "English (Literature, Writing, Grammar)", "trait_tag": "Teaching-Ed"},
            {"option_id": 304, "option_text": "Filipino (Panitikan, Wika)", "trait_tag": "Teaching-Ed"},
            {"option_id": 305, "option_text": "Social Studies (History, Economics, Politics)", "trait_tag": "Community-Serve"},
            {"option_id": 306, "option_text": "Computer/TLE (Technology, Programming)", "trait_tag": "Software-Dev"},
            {"option_id": 307, "option_text": "Arts (Drawing, Music, Theater)", "trait_tag": "Visual-Design"},
            {"option_id": 308, "option_text": "PE (Sports, Physical Activities)", "trait_tag": "Physical-Skill"},
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
            {"option_id": 331, "option_text": "Willing to work long shifts if meaningful (healthcare)", "trait_tag": "Patient-Care"},
            {"option_id": 332, "option_text": "Willing to be away for months (maritime)", "trait_tag": "Maritime-Sea"},
            {"option_id": 333, "option_text": "Flexible hours, can work from home (tech)", "trait_tag": "Software-Dev"},
            {"option_id": 334, "option_text": "Regular 9-5 office hours (corporate)", "trait_tag": "Finance-Acct"},
            {"option_id": 335, "option_text": "School schedule with holidays (education)", "trait_tag": "Teaching-Ed"},
            {"option_id": 336, "option_text": "Shift work including nights (police/hospital)", "trait_tag": "Law-Enforce"},
            {"option_id": 337, "option_text": "Freelance - choose my own hours", "trait_tag": "Visual-Design"},
            {"option_id": 338, "option_text": "Outdoor work following seasons (agriculture)", "trait_tag": "Agri-Nature"},
            {"option_id": 339, "option_text": "Hospitality hours including weekends", "trait_tag": "Hospitality-Svc"},
            {"option_id": 340, "option_text": "Project-based with varying schedules", "trait_tag": "Civil-Build"}
        ]
    },
    {
        "question_id": 35,
        "question_text": "What salary priority do you have?",
        "category": "Career Values",
        "options": [
            {"option_id": 341, "option_text": "High salary is most important (accounting/engineering)", "trait_tag": "Finance-Acct"},
            {"option_id": 342, "option_text": "High salary abroad (maritime/nursing)", "trait_tag": "Maritime-Sea"},
            {"option_id": 343, "option_text": "Stable salary with benefits (government)", "trait_tag": "Community-Serve"},
            {"option_id": 344, "option_text": "Job satisfaction over salary (teaching/social work)", "trait_tag": "Teaching-Ed"},
            {"option_id": 345, "option_text": "Growth potential more than starting salary", "trait_tag": "Software-Dev"},
            {"option_id": 346, "option_text": "Entrepreneurship - unlimited potential", "trait_tag": "Startup-Venture"},
            {"option_id": 347, "option_text": "Balanced salary and work-life", "trait_tag": "Admin-Skill"},
            {"option_id": 348, "option_text": "Tips and commissions (sales/hospitality)", "trait_tag": "Hospitality-Svc"},
            {"option_id": 349, "option_text": "Hazard pay for risky work (police)", "trait_tag": "Law-Enforce"},
            {"option_id": 350, "option_text": "Project-based high fees (freelance)", "trait_tag": "Visual-Design"}
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
            {"option_id": 360, "option_text": "I prefer careers without board exams (IT/Business)", "trait_tag": "Software-Dev"}
        ]
    },

    # ==================== RIASEC-STYLE QUESTIONS ====================
    {
        "question_id": 37,
        "question_text": "Which activity would you choose on a free Saturday?",
        "category": "Interest Type",
        "options": [
            {"option_id": 361, "option_text": "Fixing or building something (Realistic)", "trait_tag": "Technical-Skill"},
            {"option_id": 362, "option_text": "Reading about science or doing experiments (Investigative)", "trait_tag": "Lab-Research"},
            {"option_id": 363, "option_text": "Creating art, music, or writing (Artistic)", "trait_tag": "Visual-Design"},
            {"option_id": 364, "option_text": "Volunteering to help others (Social)", "trait_tag": "Community-Serve"},
            {"option_id": 365, "option_text": "Working on a business idea (Enterprising)", "trait_tag": "Startup-Venture"},
            {"option_id": 366, "option_text": "Organizing my room or files (Conventional)", "trait_tag": "Admin-Skill"},
            {"option_id": 367, "option_text": "Coding a personal project (Tech)", "trait_tag": "Software-Dev"},
            {"option_id": 368, "option_text": "Playing sports or exercising (Physical)", "trait_tag": "Physical-Skill"},
            {"option_id": 369, "option_text": "Cooking or trying new recipes (Hospitality)", "trait_tag": "Hospitality-Svc"},
            {"option_id": 370, "option_text": "Watching true crime or mystery shows (Investigative)", "trait_tag": "Law-Enforce"}
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

    # ==================== SECTION 3: DEEP CAREER SPECIALIZATION ====================
    {
        "question_id": 46,
        "question_text": "In NURSING specifically, which area interests you most?",
        "category": "Nursing Specialization",
        "options": [
            {"option_id": 451, "option_text": "Emergency Room (ER) - fast-paced trauma care", "trait_tag": "Patient-Care"},
            {"option_id": 452, "option_text": "Operating Room (OR) - surgical assistance", "trait_tag": "Patient-Care"},
            {"option_id": 453, "option_text": "Pediatrics - caring for children", "trait_tag": "Patient-Care"},
            {"option_id": 454, "option_text": "Geriatrics - caring for elderly patients", "trait_tag": "Patient-Care"},
            {"option_id": 455, "option_text": "Psychiatric nursing - mental health care", "trait_tag": "People-Skill"},
            {"option_id": 456, "option_text": "Community health nursing - public health", "trait_tag": "Community-Serve"},
            {"option_id": 457, "option_text": "ICU/Critical care - intensive monitoring", "trait_tag": "Patient-Care"},
            {"option_id": 458, "option_text": "OB-GYN - maternal and newborn care", "trait_tag": "Patient-Care"},
            {"option_id": 459, "option_text": "Oncology - cancer patient care", "trait_tag": "Patient-Care"},
            {"option_id": 460, "option_text": "I'm not interested in nursing", "trait_tag": "Software-Dev"}
        ]
    },
    {
        "question_id": 47,
        "question_text": "In PROGRAMMING specifically, which area interests you most?",
        "category": "Programming Specialization",
        "options": [
            {"option_id": 461, "option_text": "Web development - websites and web apps", "trait_tag": "Software-Dev"},
            {"option_id": 462, "option_text": "Mobile development - Android/iOS apps", "trait_tag": "Software-Dev"},
            {"option_id": 463, "option_text": "Game development - video games", "trait_tag": "Digital-Media"},
            {"option_id": 464, "option_text": "AI/Machine Learning - intelligent systems", "trait_tag": "Data-Analytics"},
            {"option_id": 465, "option_text": "Cybersecurity - ethical hacking, security", "trait_tag": "Cyber-Defense"},
            {"option_id": 466, "option_text": "DevOps - infrastructure and deployment", "trait_tag": "Hardware-Systems"},
            {"option_id": 467, "option_text": "Data engineering - big data pipelines", "trait_tag": "Data-Analytics"},
            {"option_id": 468, "option_text": "Embedded systems - IoT and hardware programming", "trait_tag": "Hardware-Systems"},
            {"option_id": 469, "option_text": "Backend development - servers and APIs", "trait_tag": "Software-Dev"},
            {"option_id": 470, "option_text": "I'm not interested in programming", "trait_tag": "Patient-Care"}
        ]
    },
    {
        "question_id": 48,
        "question_text": "In ACCOUNTING specifically, which area interests you most?",
        "category": "Accounting Specialization",
        "options": [
            {"option_id": 471, "option_text": "Auditing - examining financial records", "trait_tag": "Finance-Acct"},
            {"option_id": 472, "option_text": "Tax accounting - preparing tax returns", "trait_tag": "Finance-Acct"},
            {"option_id": 473, "option_text": "Management accounting - internal company finance", "trait_tag": "Finance-Acct"},
            {"option_id": 474, "option_text": "Forensic accounting - investigating fraud", "trait_tag": "Law-Enforce"},
            {"option_id": 475, "option_text": "Government accounting - public sector", "trait_tag": "Community-Serve"},
            {"option_id": 476, "option_text": "Cost accounting - manufacturing costs", "trait_tag": "Industrial-Ops"},
            {"option_id": 477, "option_text": "Financial planning - wealth management", "trait_tag": "Finance-Acct"},
            {"option_id": 478, "option_text": "Bookkeeping - day-to-day transactions", "trait_tag": "Admin-Skill"},
            {"option_id": 479, "option_text": "Investment analysis - stocks and bonds", "trait_tag": "Data-Analytics"},
            {"option_id": 480, "option_text": "I'm not interested in accounting", "trait_tag": "Visual-Design"}
        ]
    },
    {
        "question_id": 49,
        "question_text": "In CRIMINOLOGY specifically, which area interests you most?",
        "category": "Criminology Specialization",
        "options": [
            {"option_id": 481, "option_text": "Law enforcement - police officer, SWAT", "trait_tag": "Law-Enforce"},
            {"option_id": 482, "option_text": "Criminal investigation - detective work", "trait_tag": "Law-Enforce"},
            {"option_id": 483, "option_text": "Forensic science - crime scene analysis", "trait_tag": "Lab-Research"},
            {"option_id": 484, "option_text": "Corrections - prison/jail management", "trait_tag": "Law-Enforce"},
            {"option_id": 485, "option_text": "Cybercrime investigation - digital forensics", "trait_tag": "Cyber-Defense"},
            {"option_id": 486, "option_text": "Traffic management - road safety", "trait_tag": "Law-Enforce"},
            {"option_id": 487, "option_text": "Intelligence - NBI, NICA type work", "trait_tag": "Law-Enforce"},
            {"option_id": 488, "option_text": "Crime prevention - community programs", "trait_tag": "Community-Serve"},
            {"option_id": 489, "option_text": "Private security - bodyguard, VIP protection", "trait_tag": "Physical-Skill"},
            {"option_id": 490, "option_text": "I'm not interested in criminology", "trait_tag": "Teaching-Ed"}
        ]
    },
    {
        "question_id": 50,
        "question_text": "In EDUCATION specifically, which level/type interests you most?",
        "category": "Education Specialization",
        "options": [
            {"option_id": 491, "option_text": "Kindergarten/Preschool teacher", "trait_tag": "Teaching-Ed"},
            {"option_id": 492, "option_text": "Elementary school teacher", "trait_tag": "Teaching-Ed"},
            {"option_id": 493, "option_text": "High school teacher", "trait_tag": "Teaching-Ed"},
            {"option_id": 494, "option_text": "College professor", "trait_tag": "Lab-Research"},
            {"option_id": 495, "option_text": "Special education (SPED) teacher", "trait_tag": "People-Skill"},
            {"option_id": 496, "option_text": "School administrator/principal", "trait_tag": "Admin-Skill"},
            {"option_id": 497, "option_text": "Guidance counselor", "trait_tag": "People-Skill"},
            {"option_id": 498, "option_text": "Corporate trainer", "trait_tag": "Startup-Venture"},
            {"option_id": 499, "option_text": "Online educator/content creator", "trait_tag": "Digital-Media"},
            {"option_id": 500, "option_text": "I'm not interested in education", "trait_tag": "Finance-Acct"}
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
        "question_text": "Rate your COMPUTER/TECHNOLOGY skills:",
        "category": "Tech Skill",
        "options": [
            {"option_id": 551, "option_text": "Expert - can code, build systems", "trait_tag": "Software-Dev"},
            {"option_id": 552, "option_text": "Advanced - comfortable with most software", "trait_tag": "Data-Analytics"},
            {"option_id": 553, "option_text": "Intermediate - know MS Office, can learn new tools", "trait_tag": "Admin-Skill"},
            {"option_id": 554, "option_text": "Basic - can browse, email, social media", "trait_tag": "Marketing-Sales"},
            {"option_id": 555, "option_text": "Minimal - prefer manual/hands-on work", "trait_tag": "Agri-Nature"},
            {"option_id": 556, "option_text": "Good at hardware - fixing computers", "trait_tag": "Hardware-Systems"},
            {"option_id": 557, "option_text": "Good at design software - Photoshop, Canva", "trait_tag": "Visual-Design"},
            {"option_id": 558, "option_text": "Good at spreadsheets - Excel, Google Sheets", "trait_tag": "Finance-Acct"},
            {"option_id": 559, "option_text": "Good at video editing - Premiere, CapCut", "trait_tag": "Digital-Media"},
            {"option_id": 560, "option_text": "Good at medical software - hospital systems", "trait_tag": "Health-Admin"}
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
            {"option_id": 701, "option_text": "Math (Algebra, Calculus, Statistics)", "trait_tag": "Data-Analytics"},
            {"option_id": 702, "option_text": "Science (Biology, Chemistry, Physics)", "trait_tag": "Lab-Research"},
            {"option_id": 703, "option_text": "English (Literature, Writing)", "trait_tag": "Teaching-Ed"},
            {"option_id": 704, "option_text": "Filipino (Panitikan, Wika)", "trait_tag": "Teaching-Ed"},
            {"option_id": 705, "option_text": "Social Studies (History, Economics)", "trait_tag": "Community-Serve"},
            {"option_id": 706, "option_text": "Computer/ICT/TLE", "trait_tag": "Software-Dev"},
            {"option_id": 707, "option_text": "Arts (Drawing, Music)", "trait_tag": "Visual-Design"},
            {"option_id": 708, "option_text": "PE (Sports, Physical Education)", "trait_tag": "Physical-Skill"},
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
    }
]

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
