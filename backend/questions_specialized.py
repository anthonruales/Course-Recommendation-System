# questions_specialized.py - Questions for SPECIALIZED Trait System
"""
================================================================================
SPECIALIZED QUESTIONS - Match the New Unique Traits
================================================================================

These questions are designed to identify the 34 unique traits:
- 6 RIASEC Interest Types
- 22 Specialized Path Traits (unique per career field)
- 6 Skill Traits

Each question has options that map to DIFFERENT specialized traits,
ensuring clear differentiation between career paths.

================================================================================
"""

QUESTIONS_POOL_SPECIALIZED = [
    # ==================== SECTION 1: INTEREST TYPE (RIASEC) ====================
    {
        "question_id": 1,
        "question_text": "What type of activities do you enjoy most?",
        "category": "Interest Type",
        "options": [
            {"option_id": 1, "option_text": "Building, fixing, or working with tools and machines", "trait_tag": "Realistic"},
            {"option_id": 2, "option_text": "Researching, analyzing data, and solving complex problems", "trait_tag": "Investigative"},
            {"option_id": 3, "option_text": "Creating art, designing, or expressing myself creatively", "trait_tag": "Artistic"},
            {"option_id": 4, "option_text": "Helping people, teaching, or providing care", "trait_tag": "Social"},
            {"option_id": 5, "option_text": "Leading teams, starting projects, or making deals", "trait_tag": "Enterprising"},
            {"option_id": 6, "option_text": "Organizing information, following procedures, and managing details", "trait_tag": "Conventional"}
        ]
    },
    {
        "question_id": 2,
        "question_text": "In a group project, what role do you naturally take?",
        "category": "Interest Type",
        "options": [
            {"option_id": 7, "option_text": "The one who builds or creates the physical output", "trait_tag": "Realistic"},
            {"option_id": 8, "option_text": "The researcher who gathers and analyzes information", "trait_tag": "Investigative"},
            {"option_id": 9, "option_text": "The creative who designs the presentation or visuals", "trait_tag": "Artistic"},
            {"option_id": 10, "option_text": "The one who coordinates and helps team members", "trait_tag": "Social"},
            {"option_id": 11, "option_text": "The leader who directs and motivates the team", "trait_tag": "Enterprising"},
            {"option_id": 12, "option_text": "The organizer who tracks tasks and deadlines", "trait_tag": "Conventional"}
        ]
    },
    {
        "question_id": 3,
        "question_text": "What kind of problems do you enjoy solving?",
        "category": "Interest Type",
        "options": [
            {"option_id": 13, "option_text": "Mechanical or technical problems with equipment", "trait_tag": "Realistic"},
            {"option_id": 14, "option_text": "Scientific or mathematical puzzles", "trait_tag": "Investigative"},
            {"option_id": 15, "option_text": "Design challenges that need creative solutions", "trait_tag": "Artistic"},
            {"option_id": 16, "option_text": "Personal problems - helping friends or family", "trait_tag": "Social"},
            {"option_id": 17, "option_text": "Business challenges like making something profitable", "trait_tag": "Enterprising"},
            {"option_id": 18, "option_text": "Organizational problems like improving processes", "trait_tag": "Conventional"}
        ]
    },
    
    # ==================== SECTION 2: HEALTHCARE SPECIALIZATIONS ====================
    {
        "question_id": 4,
        "question_text": "If you were to work in healthcare, which appeals to you most?",
        "category": "Healthcare Interest",
        "options": [
            {"option_id": 19, "option_text": "Caring for patients directly - checking vitals, giving medications, providing comfort", "trait_tag": "Patient-Care"},
            {"option_id": 20, "option_text": "Working in a laboratory - analyzing blood samples, running tests", "trait_tag": "Medical-Lab"},
            {"option_id": 21, "option_text": "Helping patients recover - physical exercises, therapy sessions", "trait_tag": "Rehab-Therapy"},
            {"option_id": 22, "option_text": "Managing health records and hospital information systems", "trait_tag": "Health-Admin"},
            {"option_id": 23, "option_text": "I'm not interested in healthcare careers", "trait_tag": "Realistic"}
        ]
    },
    {
        "question_id": 5,
        "question_text": "What healthcare scenario sounds most fulfilling to you?",
        "category": "Healthcare Interest",
        "options": [
            {"option_id": 24, "option_text": "Being at a patient's bedside, monitoring their recovery", "trait_tag": "Patient-Care"},
            {"option_id": 25, "option_text": "Discovering what illness someone has by analyzing their samples", "trait_tag": "Medical-Lab"},
            {"option_id": 26, "option_text": "Guiding someone through exercises to walk again after injury", "trait_tag": "Rehab-Therapy"},
            {"option_id": 27, "option_text": "Ensuring patient records are accurate and accessible", "trait_tag": "Health-Admin"},
            {"option_id": 28, "option_text": "None of these - I prefer non-healthcare work", "trait_tag": "Enterprising"}
        ]
    },
    
    # ==================== SECTION 3: TECHNOLOGY SPECIALIZATIONS ====================
    {
        "question_id": 6,
        "question_text": "Which technology work interests you the most?",
        "category": "Technology Interest",
        "options": [
            {"option_id": 29, "option_text": "Writing code, building apps, or creating software", "trait_tag": "Software-Dev"},
            {"option_id": 30, "option_text": "Working with computer hardware, circuits, or electronics", "trait_tag": "Hardware-Systems"},
            {"option_id": 31, "option_text": "Analyzing big data, creating AI models, or machine learning", "trait_tag": "Data-Analytics"},
            {"option_id": 32, "option_text": "Protecting systems from hackers, cybersecurity", "trait_tag": "Cyber-Defense"},
            {"option_id": 33, "option_text": "I'm not interested in technology careers", "trait_tag": "Artistic"}
        ]
    },
    {
        "question_id": 7,
        "question_text": "What tech project would you enjoy most?",
        "category": "Technology Interest",
        "options": [
            {"option_id": 34, "option_text": "Building a mobile app or website from scratch", "trait_tag": "Software-Dev"},
            {"option_id": 35, "option_text": "Designing and assembling a custom computer or robot", "trait_tag": "Hardware-Systems"},
            {"option_id": 36, "option_text": "Creating a model that predicts stock prices or trends", "trait_tag": "Data-Analytics"},
            {"option_id": 37, "option_text": "Finding vulnerabilities in a system to make it more secure", "trait_tag": "Cyber-Defense"},
            {"option_id": 38, "option_text": "Creating visual effects or animations for games", "trait_tag": "Digital-Media"}
        ]
    },
    
    # ==================== SECTION 4: ENGINEERING SPECIALIZATIONS ====================
    {
        "question_id": 8,
        "question_text": "Which engineering field fascinates you?",
        "category": "Engineering Interest",
        "options": [
            {"option_id": 39, "option_text": "Designing buildings, bridges, and infrastructure", "trait_tag": "Civil-Build"},
            {"option_id": 40, "option_text": "Working with power systems and electrical networks", "trait_tag": "Electrical-Power"},
            {"option_id": 41, "option_text": "Creating machines, engines, and mechanical systems", "trait_tag": "Mechanical-Design"},
            {"option_id": 42, "option_text": "Improving factory processes and manufacturing efficiency", "trait_tag": "Industrial-Ops"},
            {"option_id": 43, "option_text": "I'm not interested in engineering", "trait_tag": "Social"}
        ]
    },
    {
        "question_id": 9,
        "question_text": "What engineering project appeals to you?",
        "category": "Engineering Interest",
        "options": [
            {"option_id": 44, "option_text": "Designing a new highway or skyscraper", "trait_tag": "Civil-Build"},
            {"option_id": 45, "option_text": "Setting up a solar power system for a community", "trait_tag": "Electrical-Power"},
            {"option_id": 46, "option_text": "Building a new type of engine or vehicle", "trait_tag": "Mechanical-Design"},
            {"option_id": 47, "option_text": "Streamlining a production line to reduce waste", "trait_tag": "Industrial-Ops"},
            {"option_id": 48, "option_text": "I prefer creative or people-focused work", "trait_tag": "Artistic"}
        ]
    },
    
    # ==================== SECTION 5: BUSINESS SPECIALIZATIONS ====================
    {
        "question_id": 10,
        "question_text": "Which business role sounds most appealing?",
        "category": "Business Interest",
        "options": [
            {"option_id": 49, "option_text": "Managing budgets, analyzing financial statements, doing audits", "trait_tag": "Finance-Acct"},
            {"option_id": 50, "option_text": "Creating marketing campaigns, managing brands, selling products", "trait_tag": "Marketing-Sales"},
            {"option_id": 51, "option_text": "Starting my own business or creating new ventures", "trait_tag": "Startup-Venture"},
            {"option_id": 52, "option_text": "I prefer non-business careers", "trait_tag": "Investigative"}
        ]
    },
    {
        "question_id": 11,
        "question_text": "What business activity excites you?",
        "category": "Business Interest",
        "options": [
            {"option_id": 53, "option_text": "Preparing tax returns or financial reports", "trait_tag": "Finance-Acct"},
            {"option_id": 54, "option_text": "Pitching products to customers or creating ads", "trait_tag": "Marketing-Sales"},
            {"option_id": 55, "option_text": "Developing a business plan for a new startup idea", "trait_tag": "Startup-Venture"},
            {"option_id": 56, "option_text": "Improving how a factory or warehouse operates", "trait_tag": "Industrial-Ops"}
        ]
    },
    
    # ==================== SECTION 6: ARTS & DESIGN SPECIALIZATIONS ====================
    {
        "question_id": 12,
        "question_text": "Which creative work interests you most?",
        "category": "Arts & Design",
        "options": [
            {"option_id": 57, "option_text": "Drawing, painting, graphic design, or photography", "trait_tag": "Visual-Design"},
            {"option_id": 58, "option_text": "Animation, video production, or game design", "trait_tag": "Digital-Media"},
            {"option_id": 59, "option_text": "Architecture, interior design, or product design", "trait_tag": "Spatial-Design"},
            {"option_id": 60, "option_text": "I'm not very interested in arts/design", "trait_tag": "Conventional"}
        ]
    },
    {
        "question_id": 13,
        "question_text": "Which project would you enjoy creating?",
        "category": "Arts & Design",
        "options": [
            {"option_id": 61, "option_text": "A poster, logo, or visual artwork", "trait_tag": "Visual-Design"},
            {"option_id": 62, "option_text": "An animated short film or video game character", "trait_tag": "Digital-Media"},
            {"option_id": 63, "option_text": "A floor plan for a house or an interior room design", "trait_tag": "Spatial-Design"},
            {"option_id": 64, "option_text": "A business presentation or report", "trait_tag": "Admin-Skill"}
        ]
    },
    
    # ==================== SECTION 7: EDUCATION & TEACHING ====================
    {
        "question_id": 14,
        "question_text": "How do you feel about teaching?",
        "category": "Education",
        "options": [
            {"option_id": 65, "option_text": "I love explaining concepts and helping students learn", "trait_tag": "Teaching-Ed"},
            {"option_id": 66, "option_text": "I prefer working independently, not teaching others", "trait_tag": "Investigative"},
            {"option_id": 67, "option_text": "I'd rather create things than teach", "trait_tag": "Artistic"},
            {"option_id": 68, "option_text": "I prefer leading business teams rather than teaching", "trait_tag": "Enterprising"}
        ]
    },
    {
        "question_id": 15,
        "question_text": "If you had to teach, what age group would you prefer?",
        "category": "Education",
        "options": [
            {"option_id": 69, "option_text": "Young children (elementary or preschool)", "trait_tag": "Teaching-Ed"},
            {"option_id": 70, "option_text": "Teenagers (high school)", "trait_tag": "Teaching-Ed"},
            {"option_id": 71, "option_text": "Adults (vocational or professional training)", "trait_tag": "Teaching-Ed"},
            {"option_id": 72, "option_text": "I don't want to teach at all", "trait_tag": "Realistic"}
        ]
    },
    
    # ==================== SECTION 8: SCIENCE & RESEARCH ====================
    {
        "question_id": 16,
        "question_text": "What type of research interests you?",
        "category": "Science",
        "options": [
            {"option_id": 73, "option_text": "Laboratory experiments - chemistry, biology, physics", "trait_tag": "Lab-Research"},
            {"option_id": 74, "option_text": "Field work - outdoors studying environment, geology, marine life", "trait_tag": "Field-Research"},
            {"option_id": 75, "option_text": "Data analysis - statistics, patterns, predictions", "trait_tag": "Data-Analytics"},
            {"option_id": 76, "option_text": "I'm not interested in research careers", "trait_tag": "Social"}
        ]
    },
    {
        "question_id": 17,
        "question_text": "Which scientific project appeals to you?",
        "category": "Science",
        "options": [
            {"option_id": 77, "option_text": "Testing new medicines or analyzing chemicals in a lab", "trait_tag": "Lab-Research"},
            {"option_id": 78, "option_text": "Studying coral reefs or monitoring forest ecosystems", "trait_tag": "Field-Research"},
            {"option_id": 79, "option_text": "Building machine learning models from large datasets", "trait_tag": "Data-Analytics"},
            {"option_id": 80, "option_text": "Medical lab testing - blood analysis, diagnostics", "trait_tag": "Medical-Lab"}
        ]
    },
    
    # ==================== SECTION 9: PUBLIC SERVICE ====================
    {
        "question_id": 18,
        "question_text": "Which public service career appeals to you?",
        "category": "Public Service",
        "options": [
            {"option_id": 81, "option_text": "Police officer, detective, or forensic investigator", "trait_tag": "Law-Enforce"},
            {"option_id": 82, "option_text": "Social worker, community organizer, or counselor", "trait_tag": "Community-Serve"},
            {"option_id": 83, "option_text": "Government administrator or policy analyst", "trait_tag": "Community-Serve"},
            {"option_id": 84, "option_text": "I prefer private sector jobs", "trait_tag": "Enterprising"}
        ]
    },
    {
        "question_id": 19,
        "question_text": "What public service activity interests you?",
        "category": "Public Service",
        "options": [
            {"option_id": 85, "option_text": "Investigating crimes and catching criminals", "trait_tag": "Law-Enforce"},
            {"option_id": 86, "option_text": "Helping underprivileged families access resources", "trait_tag": "Community-Serve"},
            {"option_id": 87, "option_text": "Analyzing evidence in a forensic laboratory", "trait_tag": "Law-Enforce"},
            {"option_id": 88, "option_text": "Developing policies to improve communities", "trait_tag": "Community-Serve"}
        ]
    },
    
    # ==================== SECTION 10: MARITIME & OUTDOOR ====================
    {
        "question_id": 20,
        "question_text": "How do you feel about working at sea?",
        "category": "Maritime",
        "options": [
            {"option_id": 89, "option_text": "I'd love to work on ships, traveling the oceans", "trait_tag": "Maritime-Sea"},
            {"option_id": 90, "option_text": "I prefer outdoor work on land (farms, forests)", "trait_tag": "Agri-Nature"},
            {"option_id": 91, "option_text": "I prefer indoor/office work", "trait_tag": "Conventional"},
            {"option_id": 92, "option_text": "I'd like outdoor field research (environmental, geology)", "trait_tag": "Field-Research"}
        ]
    },
    {
        "question_id": 21,
        "question_text": "Which maritime/outdoor role appeals to you?",
        "category": "Maritime & Agriculture",
        "options": [
            {"option_id": 93, "option_text": "Ship captain or marine officer navigating vessels", "trait_tag": "Maritime-Sea"},
            {"option_id": 94, "option_text": "Ship engineer maintaining engines and machinery", "trait_tag": "Maritime-Sea"},
            {"option_id": 95, "option_text": "Farmer or agricultural technician growing crops", "trait_tag": "Agri-Nature"},
            {"option_id": 96, "option_text": "Forest ranger or environmental conservationist", "trait_tag": "Agri-Nature"}
        ]
    },
    
    # ==================== SECTION 11: HOSPITALITY ====================
    {
        "question_id": 22,
        "question_text": "Which hospitality career interests you?",
        "category": "Hospitality",
        "options": [
            {"option_id": 97, "option_text": "Hotel manager or event coordinator", "trait_tag": "Hospitality-Svc"},
            {"option_id": 98, "option_text": "Tour guide or travel agent", "trait_tag": "Hospitality-Svc"},
            {"option_id": 99, "option_text": "Chef or restaurant owner", "trait_tag": "Hospitality-Svc"},
            {"option_id": 100, "option_text": "I'm not interested in hospitality careers", "trait_tag": "Investigative"}
        ]
    },
    
    # ==================== SECTION 12: SKILL TRAITS ====================
    {
        "question_id": 23,
        "question_text": "What is your strongest skill?",
        "category": "Skills",
        "options": [
            {"option_id": 101, "option_text": "Technical skills - computers, machines, equipment", "trait_tag": "Technical-Skill"},
            {"option_id": 102, "option_text": "People skills - communication, empathy, teamwork", "trait_tag": "People-Skill"},
            {"option_id": 103, "option_text": "Creative skills - design, art, innovation", "trait_tag": "Creative-Skill"},
            {"option_id": 104, "option_text": "Analytical skills - math, logic, research", "trait_tag": "Analytical-Skill"},
            {"option_id": 105, "option_text": "Physical skills - sports, hands-on work, stamina", "trait_tag": "Physical-Skill"},
            {"option_id": 106, "option_text": "Administrative skills - organization, planning, details", "trait_tag": "Admin-Skill"}
        ]
    },
    {
        "question_id": 24,
        "question_text": "Which skill do you want to develop most?",
        "category": "Skills",
        "options": [
            {"option_id": 107, "option_text": "Programming, engineering, or technical expertise", "trait_tag": "Technical-Skill"},
            {"option_id": 108, "option_text": "Leadership, communication, or counseling abilities", "trait_tag": "People-Skill"},
            {"option_id": 109, "option_text": "Design thinking, artistic expression, or creativity", "trait_tag": "Creative-Skill"},
            {"option_id": 110, "option_text": "Data analysis, problem-solving, or research methods", "trait_tag": "Analytical-Skill"},
            {"option_id": 111, "option_text": "Physical fitness, sports, or hands-on trade skills", "trait_tag": "Physical-Skill"},
            {"option_id": 112, "option_text": "Project management, organization, or administration", "trait_tag": "Admin-Skill"}
        ]
    },
    {
        "question_id": 25,
        "question_text": "In your free time, what do you enjoy most?",
        "category": "Skills",
        "options": [
            {"option_id": 113, "option_text": "Tinkering with gadgets, coding, or fixing things", "trait_tag": "Technical-Skill"},
            {"option_id": 114, "option_text": "Hanging out with friends, volunteering, helping others", "trait_tag": "People-Skill"},
            {"option_id": 115, "option_text": "Drawing, designing, creating art or music", "trait_tag": "Creative-Skill"},
            {"option_id": 116, "option_text": "Reading, solving puzzles, or learning new things", "trait_tag": "Analytical-Skill"},
            {"option_id": 117, "option_text": "Sports, exercise, outdoor activities", "trait_tag": "Physical-Skill"},
            {"option_id": 118, "option_text": "Organizing, planning events, managing schedules", "trait_tag": "Admin-Skill"}
        ]
    },
    
    # ==================== SECTION 13: CAREER SCENARIO QUESTIONS ====================
    {
        "question_id": 26,
        "question_text": "Imagine your ideal workday. Where are you?",
        "category": "Work Environment",
        "options": [
            {"option_id": 119, "option_text": "In a hospital or clinic caring for patients", "trait_tag": "Patient-Care"},
            {"option_id": 120, "option_text": "In a laboratory running experiments or tests", "trait_tag": "Lab-Research"},
            {"option_id": 121, "option_text": "At a computer coding or analyzing data", "trait_tag": "Software-Dev"},
            {"option_id": 122, "option_text": "On a construction site or factory floor", "trait_tag": "Civil-Build"},
            {"option_id": 123, "option_text": "In a classroom teaching students", "trait_tag": "Teaching-Ed"},
            {"option_id": 124, "option_text": "In an office meeting with clients or managing business", "trait_tag": "Marketing-Sales"}
        ]
    },
    {
        "question_id": 27,
        "question_text": "What would make you proud at the end of your career?",
        "category": "Career Vision",
        "options": [
            {"option_id": 125, "option_text": "Saving lives and helping patients heal", "trait_tag": "Patient-Care"},
            {"option_id": 126, "option_text": "Discovering something new in science or technology", "trait_tag": "Lab-Research"},
            {"option_id": 127, "option_text": "Building structures or systems that last for generations", "trait_tag": "Civil-Build"},
            {"option_id": 128, "option_text": "Inspiring and educating thousands of students", "trait_tag": "Teaching-Ed"},
            {"option_id": 129, "option_text": "Running a successful business or company", "trait_tag": "Startup-Venture"},
            {"option_id": 130, "option_text": "Creating art or designs that people admire", "trait_tag": "Visual-Design"}
        ]
    },
    {
        "question_id": 28,
        "question_text": "Which job title appeals to you most?",
        "category": "Career Goals",
        "options": [
            {"option_id": 131, "option_text": "Registered Nurse or Physical Therapist", "trait_tag": "Patient-Care"},
            {"option_id": 132, "option_text": "Medical Technologist or Pharmacist", "trait_tag": "Medical-Lab"},
            {"option_id": 133, "option_text": "Software Engineer or Data Scientist", "trait_tag": "Software-Dev"},
            {"option_id": 134, "option_text": "Civil Engineer or Architect", "trait_tag": "Civil-Build"},
            {"option_id": 135, "option_text": "Teacher or Professor", "trait_tag": "Teaching-Ed"},
            {"option_id": 136, "option_text": "Accountant or Financial Analyst", "trait_tag": "Finance-Acct"}
        ]
    },
    {
        "question_id": 29,
        "question_text": "Which job title appeals to you most? (Part 2)",
        "category": "Career Goals",
        "options": [
            {"option_id": 137, "option_text": "Graphic Designer or Animator", "trait_tag": "Visual-Design"},
            {"option_id": 138, "option_text": "Police Officer or Criminal Investigator", "trait_tag": "Law-Enforce"},
            {"option_id": 139, "option_text": "Social Worker or Community Organizer", "trait_tag": "Community-Serve"},
            {"option_id": 140, "option_text": "Ship Captain or Marine Engineer", "trait_tag": "Maritime-Sea"},
            {"option_id": 141, "option_text": "Hotel Manager or Travel Consultant", "trait_tag": "Hospitality-Svc"},
            {"option_id": 142, "option_text": "Farmer or Environmental Scientist", "trait_tag": "Agri-Nature"}
        ]
    },
    {
        "question_id": 30,
        "question_text": "What subject did you enjoy most in school?",
        "category": "Academic Interest",
        "options": [
            {"option_id": 143, "option_text": "Biology, Chemistry, or Health Science", "trait_tag": "Medical-Lab"},
            {"option_id": 144, "option_text": "Physics, Math, or Computer Science", "trait_tag": "Software-Dev"},
            {"option_id": 145, "option_text": "Art, Music, or Creative Writing", "trait_tag": "Visual-Design"},
            {"option_id": 146, "option_text": "History, Social Studies, or Filipino", "trait_tag": "Teaching-Ed"},
            {"option_id": 147, "option_text": "Business, Economics, or Accounting", "trait_tag": "Finance-Acct"},
            {"option_id": 148, "option_text": "Physical Education or Sports", "trait_tag": "Physical-Skill"}
        ]
    },
    
    # ==================== SECTION 14: ADDITIONAL DIFFERENTIATING QUESTIONS ====================
    {
        "question_id": 31,
        "question_text": "How do you prefer to help others?",
        "category": "Helping Style",
        "options": [
            {"option_id": 149, "option_text": "Physically - treating injuries, providing care", "trait_tag": "Patient-Care"},
            {"option_id": 150, "option_text": "Emotionally - counseling, listening, supporting", "trait_tag": "Community-Serve"},
            {"option_id": 151, "option_text": "Intellectually - teaching, explaining, mentoring", "trait_tag": "Teaching-Ed"},
            {"option_id": 152, "option_text": "Practically - fixing things, solving problems", "trait_tag": "Technical-Skill"}
        ]
    },
    {
        "question_id": 32,
        "question_text": "What type of work environment do you prefer?",
        "category": "Work Environment",
        "options": [
            {"option_id": 153, "option_text": "Hospital or healthcare facility", "trait_tag": "Patient-Care"},
            {"option_id": 154, "option_text": "Laboratory or research center", "trait_tag": "Lab-Research"},
            {"option_id": 155, "option_text": "Office with computers", "trait_tag": "Software-Dev"},
            {"option_id": 156, "option_text": "Outdoors - construction sites, farms, nature", "trait_tag": "Agri-Nature"},
            {"option_id": 157, "option_text": "Creative studio - design agency, film set", "trait_tag": "Digital-Media"},
            {"option_id": 158, "option_text": "Classroom or training center", "trait_tag": "Teaching-Ed"}
        ]
    },
    {
        "question_id": 33,
        "question_text": "Which problem would you most want to solve?",
        "category": "Impact",
        "options": [
            {"option_id": 159, "option_text": "Finding cures for diseases", "trait_tag": "Medical-Lab"},
            {"option_id": 160, "option_text": "Making technology accessible to everyone", "trait_tag": "Software-Dev"},
            {"option_id": 161, "option_text": "Protecting the environment from pollution", "trait_tag": "Field-Research"},
            {"option_id": 162, "option_text": "Reducing crime and keeping communities safe", "trait_tag": "Law-Enforce"},
            {"option_id": 163, "option_text": "Helping poor families escape poverty", "trait_tag": "Community-Serve"},
            {"option_id": 164, "option_text": "Building sustainable infrastructure", "trait_tag": "Civil-Build"}
        ]
    },
    {
        "question_id": 34,
        "question_text": "What motivates you most at work?",
        "category": "Motivation",
        "options": [
            {"option_id": 165, "option_text": "Making a direct difference in people's lives", "trait_tag": "Patient-Care"},
            {"option_id": 166, "option_text": "Discovering new knowledge or innovations", "trait_tag": "Lab-Research"},
            {"option_id": 167, "option_text": "Building something tangible and lasting", "trait_tag": "Civil-Build"},
            {"option_id": 168, "option_text": "Financial success and business growth", "trait_tag": "Startup-Venture"},
            {"option_id": 169, "option_text": "Creative expression and recognition", "trait_tag": "Visual-Design"},
            {"option_id": 170, "option_text": "Stability, order, and systematic processes", "trait_tag": "Admin-Skill"}
        ]
    },
    {
        "question_id": 35,
        "question_text": "How do you feel about working with blood, needles, or sick patients?",
        "category": "Healthcare Tolerance",
        "options": [
            {"option_id": 171, "option_text": "I'm completely comfortable - I want to help patients directly", "trait_tag": "Patient-Care"},
            {"option_id": 172, "option_text": "I'm okay with lab work (blood samples) but not direct patient care", "trait_tag": "Medical-Lab"},
            {"option_id": 173, "option_text": "I'd prefer therapy/rehab work rather than medical procedures", "trait_tag": "Rehab-Therapy"},
            {"option_id": 174, "option_text": "I'd rather avoid healthcare altogether", "trait_tag": "Software-Dev"}
        ]
    },
    {
        "question_id": 36,
        "question_text": "What's your ideal work schedule?",
        "category": "Work Style",
        "options": [
            {"option_id": 175, "option_text": "Shift work (hospitals, 24/7 operations)", "trait_tag": "Patient-Care"},
            {"option_id": 176, "option_text": "Regular office hours (9-5)", "trait_tag": "Finance-Acct"},
            {"option_id": 177, "option_text": "Flexible/project-based (creative, tech)", "trait_tag": "Software-Dev"},
            {"option_id": 178, "option_text": "Seasonal/outdoor work (farming, tourism)", "trait_tag": "Agri-Nature"},
            {"option_id": 179, "option_text": "Extended deployments at sea", "trait_tag": "Maritime-Sea"}
        ]
    },
    {
        "question_id": 37,
        "question_text": "Do you want to work abroad (OFW)?",
        "category": "Career Goals",
        "options": [
            {"option_id": 180, "option_text": "Yes, in healthcare (USA, UK, Middle East)", "trait_tag": "Patient-Care"},
            {"option_id": 181, "option_text": "Yes, as a seafarer on international ships", "trait_tag": "Maritime-Sea"},
            {"option_id": 182, "option_text": "Yes, in hotels/tourism abroad", "trait_tag": "Hospitality-Svc"},
            {"option_id": 183, "option_text": "Yes, in tech/IT companies abroad", "trait_tag": "Software-Dev"},
            {"option_id": 184, "option_text": "No, I prefer to work locally", "trait_tag": "Community-Serve"}
        ]
    },
    {
        "question_id": 38,
        "question_text": "What kind of challenge excites you?",
        "category": "Challenge Type",
        "options": [
            {"option_id": 185, "option_text": "Diagnosing what's wrong and finding solutions", "trait_tag": "Medical-Lab"},
            {"option_id": 186, "option_text": "Building something from blueprints or designs", "trait_tag": "Civil-Build"},
            {"option_id": 187, "option_text": "Debugging code or fixing technical issues", "trait_tag": "Software-Dev"},
            {"option_id": 188, "option_text": "Convincing people and closing deals", "trait_tag": "Marketing-Sales"},
            {"option_id": 189, "option_text": "Creating something visually stunning", "trait_tag": "Visual-Design"},
            {"option_id": 190, "option_text": "Helping someone through a difficult time", "trait_tag": "Community-Serve"}
        ]
    },
    {
        "question_id": 39,
        "question_text": "What tools would you prefer to work with?",
        "category": "Tools",
        "options": [
            {"option_id": 191, "option_text": "Medical equipment (stethoscope, IV, monitors)", "trait_tag": "Patient-Care"},
            {"option_id": 192, "option_text": "Lab equipment (microscope, test tubes, centrifuge)", "trait_tag": "Medical-Lab"},
            {"option_id": 193, "option_text": "Computers and software", "trait_tag": "Software-Dev"},
            {"option_id": 194, "option_text": "Construction tools and machinery", "trait_tag": "Civil-Build"},
            {"option_id": 195, "option_text": "Art supplies or design software", "trait_tag": "Visual-Design"},
            {"option_id": 196, "option_text": "Teaching materials (books, whiteboards, projectors)", "trait_tag": "Teaching-Ed"}
        ]
    },
    {
        "question_id": 40,
        "question_text": "Which Filipino career path resonates with you?",
        "category": "Career Path",
        "options": [
            {"option_id": 197, "option_text": "Healthcare professional working abroad (nurse, PT)", "trait_tag": "Patient-Care"},
            {"option_id": 198, "option_text": "Seafarer earning high salary on ships", "trait_tag": "Maritime-Sea"},
            {"option_id": 199, "option_text": "Government employee serving the community", "trait_tag": "Community-Serve"},
            {"option_id": 200, "option_text": "Teacher shaping the next generation", "trait_tag": "Teaching-Ed"},
            {"option_id": 201, "option_text": "Tech professional in BPO or startup", "trait_tag": "Software-Dev"},
            {"option_id": 202, "option_text": "Entrepreneur running my own business", "trait_tag": "Startup-Venture"}
        ]
    },
    
    # ==================== SECTION 15: ADDITIONAL QUESTIONS (30 MORE) ====================
    {
        "question_id": 41,
        "question_text": "When facing a problem, what's your first instinct?",
        "category": "Problem Solving Style",
        "options": [
            {"option_id": 203, "option_text": "Take it apart and see how it works", "trait_tag": "Mechanical-Design"},
            {"option_id": 204, "option_text": "Research and gather more information first", "trait_tag": "Lab-Research"},
            {"option_id": 205, "option_text": "Ask others for their input and collaborate", "trait_tag": "People-Skill"},
            {"option_id": 206, "option_text": "Think of creative, unconventional solutions", "trait_tag": "Creative-Skill"},
            {"option_id": 207, "option_text": "Follow a systematic step-by-step approach", "trait_tag": "Admin-Skill"}
        ]
    },
    {
        "question_id": 42,
        "question_text": "What type of books, videos, or content do you enjoy?",
        "category": "Content Interest",
        "options": [
            {"option_id": 208, "option_text": "Medical dramas or documentaries about doctors/nurses", "trait_tag": "Patient-Care"},
            {"option_id": 209, "option_text": "Tech videos, coding tutorials, or gadget reviews", "trait_tag": "Software-Dev"},
            {"option_id": 210, "option_text": "True crime, detective stories, or forensic shows", "trait_tag": "Law-Enforce"},
            {"option_id": 211, "option_text": "Business news, entrepreneurship stories, or finance tips", "trait_tag": "Finance-Acct"},
            {"option_id": 212, "option_text": "Art tutorials, design inspiration, or creative content", "trait_tag": "Visual-Design"},
            {"option_id": 213, "option_text": "Nature documentaries or agricultural shows", "trait_tag": "Agri-Nature"}
        ]
    },
    {
        "question_id": 43,
        "question_text": "How do you prefer to spend your weekends?",
        "category": "Leisure Preference",
        "options": [
            {"option_id": 214, "option_text": "Volunteering or helping in community activities", "trait_tag": "Community-Serve"},
            {"option_id": 215, "option_text": "Building projects, DIY, or fixing things at home", "trait_tag": "Technical-Skill"},
            {"option_id": 216, "option_text": "Creating art, music, or working on creative hobbies", "trait_tag": "Creative-Skill"},
            {"option_id": 217, "option_text": "Playing sports or outdoor physical activities", "trait_tag": "Physical-Skill"},
            {"option_id": 218, "option_text": "Reading, studying, or learning something new online", "trait_tag": "Analytical-Skill"},
            {"option_id": 219, "option_text": "Spending quality time with family and friends", "trait_tag": "People-Skill"}
        ]
    },
    {
        "question_id": 44,
        "question_text": "What achievement would make you most proud?",
        "category": "Achievement Values",
        "options": [
            {"option_id": 220, "option_text": "Saving someone's life or helping them recover from illness", "trait_tag": "Patient-Care"},
            {"option_id": 221, "option_text": "Building an app or software used by millions", "trait_tag": "Software-Dev"},
            {"option_id": 222, "option_text": "Designing a building that becomes a landmark", "trait_tag": "Spatial-Design"},
            {"option_id": 223, "option_text": "Starting a successful business from scratch", "trait_tag": "Startup-Venture"},
            {"option_id": 224, "option_text": "Teaching students who later become successful", "trait_tag": "Teaching-Ed"},
            {"option_id": 225, "option_text": "Solving a major crime or bringing justice", "trait_tag": "Law-Enforce"}
        ]
    },
    {
        "question_id": 45,
        "question_text": "What sounds like the most interesting work meeting?",
        "category": "Work Style",
        "options": [
            {"option_id": 226, "option_text": "Medical case discussion with doctors and nurses", "trait_tag": "Medical-Lab"},
            {"option_id": 227, "option_text": "Code review and technical architecture planning", "trait_tag": "Software-Dev"},
            {"option_id": 228, "option_text": "Creative brainstorming for a new campaign or design", "trait_tag": "Digital-Media"},
            {"option_id": 229, "option_text": "Financial planning and budget review", "trait_tag": "Finance-Acct"},
            {"option_id": 230, "option_text": "Team building and staff development session", "trait_tag": "People-Skill"},
            {"option_id": 231, "option_text": "Safety and operations planning for construction", "trait_tag": "Civil-Build"}
        ]
    },
    {
        "question_id": 46,
        "question_text": "If you could instantly master one skill, which would it be?",
        "category": "Skill Aspiration",
        "options": [
            {"option_id": 232, "option_text": "Surgery or advanced medical procedures", "trait_tag": "Patient-Care"},
            {"option_id": 233, "option_text": "Programming in any language perfectly", "trait_tag": "Software-Dev"},
            {"option_id": 234, "option_text": "Speaking multiple languages fluently", "trait_tag": "Teaching-Ed"},
            {"option_id": 235, "option_text": "Creating stunning artwork or designs", "trait_tag": "Visual-Design"},
            {"option_id": 236, "option_text": "Understanding complex financial markets", "trait_tag": "Finance-Acct"},
            {"option_id": 237, "option_text": "Building or engineering anything mechanical", "trait_tag": "Mechanical-Design"}
        ]
    },
    {
        "question_id": 47,
        "question_text": "What kind of TV show character would you be?",
        "category": "Personality Match",
        "options": [
            {"option_id": 238, "option_text": "The doctor or nurse who saves lives", "trait_tag": "Patient-Care"},
            {"option_id": 239, "option_text": "The tech genius who hacks systems", "trait_tag": "Cyber-Defense"},
            {"option_id": 240, "option_text": "The detective solving mysteries", "trait_tag": "Law-Enforce"},
            {"option_id": 241, "option_text": "The creative artist or designer", "trait_tag": "Visual-Design"},
            {"option_id": 242, "option_text": "The business mogul making deals", "trait_tag": "Marketing-Sales"},
            {"option_id": 243, "option_text": "The teacher inspiring students", "trait_tag": "Teaching-Ed"}
        ]
    },
    {
        "question_id": 48,
        "question_text": "What frustrates you the most?",
        "category": "Work Frustration",
        "options": [
            {"option_id": 244, "option_text": "Seeing people suffer when I could help", "trait_tag": "Patient-Care"},
            {"option_id": 245, "option_text": "Inefficient systems that could be automated", "trait_tag": "Software-Dev"},
            {"option_id": 246, "option_text": "Poor design or ugly visual presentations", "trait_tag": "Visual-Design"},
            {"option_id": 247, "option_text": "Disorganized finances or wasted money", "trait_tag": "Finance-Acct"},
            {"option_id": 248, "option_text": "Environmental destruction or pollution", "trait_tag": "Field-Research"},
            {"option_id": 249, "option_text": "Injustice or criminals getting away", "trait_tag": "Law-Enforce"}
        ]
    },
    {
        "question_id": 49,
        "question_text": "What's your ideal lunch break activity?",
        "category": "Daily Preference",
        "options": [
            {"option_id": 250, "option_text": "Quick meal then back to patients or clients", "trait_tag": "Patient-Care"},
            {"option_id": 251, "option_text": "Eating while watching tech news or tutorials", "trait_tag": "Technical-Skill"},
            {"option_id": 252, "option_text": "Socializing and chatting with coworkers", "trait_tag": "People-Skill"},
            {"option_id": 253, "option_text": "Taking a walk outside in nature", "trait_tag": "Agri-Nature"},
            {"option_id": 254, "option_text": "Quick workout or physical activity", "trait_tag": "Physical-Skill"},
            {"option_id": 255, "option_text": "Sketching, doodling, or creative activities", "trait_tag": "Creative-Skill"}
        ]
    },
    {
        "question_id": 50,
        "question_text": "Which school subject combination did you enjoy most?",
        "category": "Academic Preference",
        "options": [
            {"option_id": 256, "option_text": "Biology + Chemistry (life sciences)", "trait_tag": "Medical-Lab"},
            {"option_id": 257, "option_text": "Math + Physics (exact sciences)", "trait_tag": "Electrical-Power"},
            {"option_id": 258, "option_text": "English + Filipino (languages/communication)", "trait_tag": "Teaching-Ed"},
            {"option_id": 259, "option_text": "Arts + TLE (creative/practical)", "trait_tag": "Visual-Design"},
            {"option_id": 260, "option_text": "MAPEH + PE (physical/performance)", "trait_tag": "Physical-Skill"},
            {"option_id": 261, "option_text": "Social Studies + Economics (society/business)", "trait_tag": "Community-Serve"}
        ]
    },
    {
        "question_id": 51,
        "question_text": "How do you handle stress?",
        "category": "Stress Response",
        "options": [
            {"option_id": 262, "option_text": "I stay calm and methodical under pressure", "trait_tag": "Patient-Care"},
            {"option_id": 263, "option_text": "I analyze the problem logically and break it down", "trait_tag": "Analytical-Skill"},
            {"option_id": 264, "option_text": "I talk to others and seek support", "trait_tag": "People-Skill"},
            {"option_id": 265, "option_text": "I exercise or do physical activities", "trait_tag": "Physical-Skill"},
            {"option_id": 266, "option_text": "I express myself through creative outlets", "trait_tag": "Creative-Skill"},
            {"option_id": 267, "option_text": "I organize and make lists to regain control", "trait_tag": "Admin-Skill"}
        ]
    },
    {
        "question_id": 52,
        "question_text": "What type of workplace sounds best?",
        "category": "Work Environment",
        "options": [
            {"option_id": 268, "option_text": "Hospital or medical clinic", "trait_tag": "Patient-Care"},
            {"option_id": 269, "option_text": "Tech startup or IT company", "trait_tag": "Software-Dev"},
            {"option_id": 270, "option_text": "School or university campus", "trait_tag": "Teaching-Ed"},
            {"option_id": 271, "option_text": "Design studio or creative agency", "trait_tag": "Digital-Media"},
            {"option_id": 272, "option_text": "Bank or corporate office", "trait_tag": "Finance-Acct"},
            {"option_id": 273, "option_text": "Ship or maritime vessel", "trait_tag": "Maritime-Sea"}
        ]
    },
    {
        "question_id": 53,
        "question_text": "What's your attitude toward uniforms?",
        "category": "Work Style",
        "options": [
            {"option_id": 274, "option_text": "I'd proudly wear scrubs or medical uniform", "trait_tag": "Patient-Care"},
            {"option_id": 275, "option_text": "I prefer casual dress code (tech/startup)", "trait_tag": "Software-Dev"},
            {"option_id": 276, "option_text": "I like professional business attire", "trait_tag": "Finance-Acct"},
            {"option_id": 277, "option_text": "I'd wear a police or military uniform proudly", "trait_tag": "Law-Enforce"},
            {"option_id": 278, "option_text": "I prefer seafarer or maritime uniform", "trait_tag": "Maritime-Sea"},
            {"option_id": 279, "option_text": "I like creative, self-expressive clothing", "trait_tag": "Visual-Design"}
        ]
    },
    {
        "question_id": 54,
        "question_text": "How important is salary vs. job satisfaction to you?",
        "category": "Career Priority",
        "options": [
            {"option_id": 280, "option_text": "I want high salary even if work is tough (maritime, nursing abroad)", "trait_tag": "Maritime-Sea"},
            {"option_id": 281, "option_text": "I want good balance of both (tech, business)", "trait_tag": "Software-Dev"},
            {"option_id": 282, "option_text": "I prioritize helping others over money (teaching, social work)", "trait_tag": "Community-Serve"},
            {"option_id": 283, "option_text": "I want creative fulfillment even if pay is moderate", "trait_tag": "Visual-Design"},
            {"option_id": 284, "option_text": "I want stable government job with benefits", "trait_tag": "Admin-Skill"},
            {"option_id": 285, "option_text": "I want to build my own wealth (entrepreneurship)", "trait_tag": "Startup-Venture"}
        ]
    },
    {
        "question_id": 55,
        "question_text": "Which emergency situation would you handle best?",
        "category": "Crisis Response",
        "options": [
            {"option_id": 286, "option_text": "Medical emergency - performing first aid or CPR", "trait_tag": "Patient-Care"},
            {"option_id": 287, "option_text": "Technical failure - fixing systems or equipment", "trait_tag": "Technical-Skill"},
            {"option_id": 288, "option_text": "Fire or natural disaster - organizing evacuation", "trait_tag": "Law-Enforce"},
            {"option_id": 289, "option_text": "Financial crisis - managing budget and resources", "trait_tag": "Finance-Acct"},
            {"option_id": 290, "option_text": "Social conflict - mediating between people", "trait_tag": "People-Skill"},
            {"option_id": 291, "option_text": "Ship emergency - maritime crisis management", "trait_tag": "Maritime-Sea"}
        ]
    },
    {
        "question_id": 56,
        "question_text": "What would you study if you had unlimited time?",
        "category": "Learning Interest",
        "options": [
            {"option_id": 292, "option_text": "Human anatomy and medicine", "trait_tag": "Medical-Lab"},
            {"option_id": 293, "option_text": "Artificial intelligence and machine learning", "trait_tag": "Data-Analytics"},
            {"option_id": 294, "option_text": "History, culture, and languages", "trait_tag": "Teaching-Ed"},
            {"option_id": 295, "option_text": "Art history and design principles", "trait_tag": "Visual-Design"},
            {"option_id": 296, "option_text": "Economics and global markets", "trait_tag": "Finance-Acct"},
            {"option_id": 297, "option_text": "Environmental science and sustainability", "trait_tag": "Field-Research"}
        ]
    },
    {
        "question_id": 57,
        "question_text": "How do you prefer to learn new things?",
        "category": "Learning Style",
        "options": [
            {"option_id": 298, "option_text": "Hands-on practice and real-world application", "trait_tag": "Technical-Skill"},
            {"option_id": 299, "option_text": "Reading books and research papers", "trait_tag": "Lab-Research"},
            {"option_id": 300, "option_text": "Watching videos and visual demonstrations", "trait_tag": "Digital-Media"},
            {"option_id": 301, "option_text": "Discussing with others and group learning", "trait_tag": "People-Skill"},
            {"option_id": 302, "option_text": "Step-by-step structured courses", "trait_tag": "Admin-Skill"},
            {"option_id": 303, "option_text": "Trial and error experimentation", "trait_tag": "Creative-Skill"}
        ]
    },
    {
        "question_id": 58,
        "question_text": "What's your dream project?",
        "category": "Dream Project",
        "options": [
            {"option_id": 304, "option_text": "Open a clinic or hospital in my hometown", "trait_tag": "Patient-Care"},
            {"option_id": 305, "option_text": "Create an app that changes how people live", "trait_tag": "Software-Dev"},
            {"option_id": 306, "option_text": "Design a building that becomes an icon", "trait_tag": "Spatial-Design"},
            {"option_id": 307, "option_text": "Start a business empire", "trait_tag": "Startup-Venture"},
            {"option_id": 308, "option_text": "Establish a school or educational foundation", "trait_tag": "Teaching-Ed"},
            {"option_id": 309, "option_text": "Lead a research team making discoveries", "trait_tag": "Lab-Research"}
        ]
    },
    {
        "question_id": 59,
        "question_text": "Which news headline would excite you most?",
        "category": "Interest Indicator",
        "options": [
            {"option_id": 310, "option_text": "'New treatment cures previously incurable disease'", "trait_tag": "Medical-Lab"},
            {"option_id": 311, "option_text": "'Revolutionary AI breakthrough changes everything'", "trait_tag": "Data-Analytics"},
            {"option_id": 312, "option_text": "'New sustainable building wins architecture award'", "trait_tag": "Spatial-Design"},
            {"option_id": 313, "option_text": "'Local startup becomes billion-dollar company'", "trait_tag": "Startup-Venture"},
            {"option_id": 314, "option_text": "'Crime rate drops thanks to new police program'", "trait_tag": "Law-Enforce"},
            {"option_id": 315, "option_text": "'Education reform improves student outcomes'", "trait_tag": "Teaching-Ed"}
        ]
    },
    {
        "question_id": 60,
        "question_text": "What's your ideal team size at work?",
        "category": "Team Preference",
        "options": [
            {"option_id": 316, "option_text": "Large team (hospital, corporation)", "trait_tag": "Patient-Care"},
            {"option_id": 317, "option_text": "Small team (startup, design studio)", "trait_tag": "Software-Dev"},
            {"option_id": 318, "option_text": "Working mostly alone (research, writing)", "trait_tag": "Lab-Research"},
            {"option_id": 319, "option_text": "Classroom setting (teacher + students)", "trait_tag": "Teaching-Ed"},
            {"option_id": 320, "option_text": "Ship crew (maritime)", "trait_tag": "Maritime-Sea"},
            {"option_id": 321, "option_text": "Field team (construction, agriculture)", "trait_tag": "Civil-Build"}
        ]
    },
    {
        "question_id": 61,
        "question_text": "What's your relationship with technology?",
        "category": "Tech Attitude",
        "options": [
            {"option_id": 322, "option_text": "I love it - I want to create new technology", "trait_tag": "Software-Dev"},
            {"option_id": 323, "option_text": "I use it as a tool for my work", "trait_tag": "Technical-Skill"},
            {"option_id": 324, "option_text": "I prefer minimal technology, more human interaction", "trait_tag": "Patient-Care"},
            {"option_id": 325, "option_text": "I want to protect people from tech dangers", "trait_tag": "Cyber-Defense"},
            {"option_id": 326, "option_text": "I use it creatively for design and media", "trait_tag": "Digital-Media"},
            {"option_id": 327, "option_text": "I prefer traditional, hands-on methods", "trait_tag": "Agri-Nature"}
        ]
    },
    {
        "question_id": 62,
        "question_text": "How do you feel about working night shifts?",
        "category": "Work Schedule",
        "options": [
            {"option_id": 328, "option_text": "Fine - hospitals and patients need 24/7 care", "trait_tag": "Patient-Care"},
            {"option_id": 329, "option_text": "Fine - I'm a night owl, good for tech work", "trait_tag": "Software-Dev"},
            {"option_id": 330, "option_text": "Prefer daytime - normal school/office hours", "trait_tag": "Teaching-Ed"},
            {"option_id": 331, "option_text": "I'll work any shift for good pay (BPO, maritime)", "trait_tag": "Maritime-Sea"},
            {"option_id": 332, "option_text": "Prefer flexible hours (creative, freelance)", "trait_tag": "Visual-Design"},
            {"option_id": 333, "option_text": "I prefer structured 9-5 schedule", "trait_tag": "Finance-Acct"}
        ]
    },
    {
        "question_id": 63,
        "question_text": "What's your attitude toward paperwork and documentation?",
        "category": "Admin Preference",
        "options": [
            {"option_id": 334, "option_text": "It's essential - medical records save lives", "trait_tag": "Health-Admin"},
            {"option_id": 335, "option_text": "I prefer to automate it with software", "trait_tag": "Software-Dev"},
            {"option_id": 336, "option_text": "It's important for financial accuracy", "trait_tag": "Finance-Acct"},
            {"option_id": 337, "option_text": "I enjoy organizing and keeping records", "trait_tag": "Admin-Skill"},
            {"option_id": 338, "option_text": "I prefer hands-on work over paperwork", "trait_tag": "Physical-Skill"},
            {"option_id": 339, "option_text": "Documentation is crucial for legal cases", "trait_tag": "Law-Enforce"}
        ]
    },
    {
        "question_id": 64,
        "question_text": "What kind of recognition matters most to you?",
        "category": "Recognition",
        "options": [
            {"option_id": 340, "option_text": "Patient gratitude and lives saved", "trait_tag": "Patient-Care"},
            {"option_id": 341, "option_text": "Technical respect from peers", "trait_tag": "Software-Dev"},
            {"option_id": 342, "option_text": "Student success and appreciation", "trait_tag": "Teaching-Ed"},
            {"option_id": 343, "option_text": "Creative awards and portfolio", "trait_tag": "Visual-Design"},
            {"option_id": 344, "option_text": "Financial success and wealth", "trait_tag": "Startup-Venture"},
            {"option_id": 345, "option_text": "Community respect and civic awards", "trait_tag": "Community-Serve"}
        ]
    },
    {
        "question_id": 65,
        "question_text": "How do you feel about physical labor?",
        "category": "Physical Work",
        "options": [
            {"option_id": 346, "option_text": "I enjoy it - construction, farming, or maritime work", "trait_tag": "Physical-Skill"},
            {"option_id": 347, "option_text": "Some is fine - like in healthcare or rehab", "trait_tag": "Rehab-Therapy"},
            {"option_id": 348, "option_text": "I prefer mental work over physical", "trait_tag": "Analytical-Skill"},
            {"option_id": 349, "option_text": "I like a mix of desk and active work", "trait_tag": "Technical-Skill"},
            {"option_id": 350, "option_text": "I prefer purely desk-based work", "trait_tag": "Software-Dev"},
            {"option_id": 351, "option_text": "I enjoy physical work in sports/PE", "trait_tag": "Teaching-Ed"}
        ]
    },
    {
        "question_id": 66,
        "question_text": "What's your comfort level with blood and medical situations?",
        "category": "Medical Tolerance",
        "options": [
            {"option_id": 352, "option_text": "Very comfortable - I want direct patient care", "trait_tag": "Patient-Care"},
            {"option_id": 353, "option_text": "Comfortable with lab samples, not direct wounds", "trait_tag": "Medical-Lab"},
            {"option_id": 354, "option_text": "I prefer therapy and rehab, less medical", "trait_tag": "Rehab-Therapy"},
            {"option_id": 355, "option_text": "I'd rather work in health administration", "trait_tag": "Health-Admin"},
            {"option_id": 356, "option_text": "Not comfortable - I prefer non-medical careers", "trait_tag": "Software-Dev"},
            {"option_id": 357, "option_text": "I can handle it for forensic/crime work", "trait_tag": "Law-Enforce"}
        ]
    },
    {
        "question_id": 67,
        "question_text": "What's your ideal level of job stability?",
        "category": "Stability Preference",
        "options": [
            {"option_id": 358, "option_text": "Very stable - government or hospital job", "trait_tag": "Community-Serve"},
            {"option_id": 359, "option_text": "Stable with growth - corporate or banking", "trait_tag": "Finance-Acct"},
            {"option_id": 360, "option_text": "Dynamic - tech startup environment", "trait_tag": "Software-Dev"},
            {"option_id": 361, "option_text": "Contract-based - maritime or project work", "trait_tag": "Maritime-Sea"},
            {"option_id": 362, "option_text": "Freelance - creative and flexible", "trait_tag": "Visual-Design"},
            {"option_id": 363, "option_text": "Self-employed - entrepreneurship", "trait_tag": "Startup-Venture"}
        ]
    },
    {
        "question_id": 68,
        "question_text": "What role do you play in your friend group?",
        "category": "Social Role",
        "options": [
            {"option_id": 364, "option_text": "The caregiver - always checking on everyone", "trait_tag": "Patient-Care"},
            {"option_id": 365, "option_text": "The problem solver - fixes tech or practical issues", "trait_tag": "Technical-Skill"},
            {"option_id": 366, "option_text": "The planner - organizes events and activities", "trait_tag": "Admin-Skill"},
            {"option_id": 367, "option_text": "The creative - comes up with fun ideas", "trait_tag": "Creative-Skill"},
            {"option_id": 368, "option_text": "The counselor - friends come to me for advice", "trait_tag": "People-Skill"},
            {"option_id": 369, "option_text": "The achiever - motivates others to succeed", "trait_tag": "Marketing-Sales"}
        ]
    },
    {
        "question_id": 69,
        "question_text": "What industry trend excites you most?",
        "category": "Industry Interest",
        "options": [
            {"option_id": 370, "option_text": "Telemedicine and healthcare technology", "trait_tag": "Patient-Care"},
            {"option_id": 371, "option_text": "AI, blockchain, and emerging tech", "trait_tag": "Data-Analytics"},
            {"option_id": 372, "option_text": "Green energy and sustainable engineering", "trait_tag": "Electrical-Power"},
            {"option_id": 373, "option_text": "E-commerce and digital marketing", "trait_tag": "Marketing-Sales"},
            {"option_id": 374, "option_text": "EdTech and online learning", "trait_tag": "Teaching-Ed"},
            {"option_id": 375, "option_text": "Sustainable agriculture and food tech", "trait_tag": "Agri-Nature"}
        ]
    },
    {
        "question_id": 70,
        "question_text": "If you could shadow someone for a day, who would it be?",
        "category": "Role Model",
        "options": [
            {"option_id": 376, "option_text": "A surgeon in the operating room", "trait_tag": "Patient-Care"},
            {"option_id": 377, "option_text": "A software engineer at Google or Meta", "trait_tag": "Software-Dev"},
            {"option_id": 378, "option_text": "An architect designing skyscrapers", "trait_tag": "Spatial-Design"},
            {"option_id": 379, "option_text": "A CEO running a major company", "trait_tag": "Startup-Venture"},
            {"option_id": 380, "option_text": "A detective solving a major case", "trait_tag": "Law-Enforce"},
            {"option_id": 381, "option_text": "A ship captain navigating the ocean", "trait_tag": "Maritime-Sea"}
        ]
    }
]

# Verify trait coverage
if __name__ == "__main__":
    trait_counts = {}
    for q in QUESTIONS_POOL_SPECIALIZED:
        for opt in q.get("options", []):
            trait = opt.get("trait_tag")
            if trait:
                trait_counts[trait] = trait_counts.get(trait, 0) + 1
    
    print("=" * 60)
    print("SPECIALIZED QUESTIONS - TRAIT COVERAGE")
    print("=" * 60)
    for trait, count in sorted(trait_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"{trait}: {count} options")
    print(f"\nTotal: {len(trait_counts)} unique traits across {len(QUESTIONS_POOL_SPECIALIZED)} questions")
