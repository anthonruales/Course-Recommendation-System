# courses_specialized.py - Courses with UNIQUE Specialized Traits
"""
================================================================================
NEW SPECIALIZED TRAIT SYSTEM - Unique Traits Per Career Path
================================================================================

Each course now has 3 traits:
1. RIASEC Interest Type (6 types) - General personality fit
2. SPECIALIZED PATH TRAIT (unique per field) - Distinguishes career paths
3. SKILL/ENVIRONMENT TRAIT - Work style preference

This prevents overlap and makes matching more accurate!

SPECIALIZED PATH TRAITS (22 unique traits):
├── Healthcare Path
│   ├── Patient-Care      → Direct patient interaction (Nursing, Midwifery)
│   ├── Medical-Lab       → Laboratory diagnostics (MedTech, Pharmacy)
│   ├── Rehab-Therapy     → Rehabilitation services (PT, OT, Speech)
│   └── Health-Admin      → Healthcare management (Health Info)
│
├── Technology Path
│   ├── Software-Dev      → Programming, apps (CS, IT)
│   ├── Hardware-Systems  → Electronics, circuits (CompEng, Electronics)
│   ├── Data-Analytics    → Data science, ML (Data Science)
│   └── Cyber-Defense     → Security (Cybersecurity)
│
├── Engineering Path
│   ├── Civil-Build       → Infrastructure (Civil Eng)
│   ├── Electrical-Power  → Power systems (EE)
│   ├── Mechanical-Design → Machines (ME)
│   └── Industrial-Ops    → Process optimization (IE)
│
├── Business Path
│   ├── Finance-Acct      → Accounting, finance
│   ├── Marketing-Sales   → Sales, advertising
│   └── Startup-Venture   → Entrepreneurship
│
├── Education Path
│   └── Teaching-Ed       → All education courses
│
├── Arts & Design Path
│   ├── Visual-Design     → Graphics, fine arts
│   ├── Digital-Media     → Animation, multimedia
│   └── Spatial-Design    → Architecture, interior
│
├── Science Path
│   ├── Lab-Research      → Laboratory science
│   └── Field-Research    → Environmental, marine
│
├── Public Service Path
│   ├── Law-Enforce       → Criminology, forensics
│   └── Community-Serve   → Social work, public admin
│
├── Maritime Path
│   └── Maritime-Sea      → Marine transportation & engineering
│
├── Agriculture Path
│   └── Agri-Nature       → Agriculture, forestry, fisheries
│
└── Hospitality Path
    └── Hospitality-Svc   → Hotels, tourism, culinary

SKILL TRAITS (6):
├── Technical-Skill   → Requires technical proficiency
├── People-Skill      → Requires interpersonal abilities
├── Creative-Skill    → Requires creativity/design
├── Analytical-Skill  → Requires analysis/research
├── Physical-Skill    → Requires physical activity
└── Admin-Skill       → Requires organization/management

================================================================================
"""

# 22 Specialized Path Traits + 6 RIASEC + 6 Skill Traits = 34 unique traits
TRAIT_DEFINITIONS_V2 = {
    # RIASEC Interest Types
    "Realistic": "Practical, hands-on work with tools, machines, or nature",
    "Investigative": "Research, analysis, and intellectual problem-solving",
    "Artistic": "Creative expression, design, and aesthetics",
    "Social": "Helping, teaching, and working with people",
    "Enterprising": "Leading, persuading, and business ventures",
    "Conventional": "Organizing, data management, and systematic work",
    
    # Healthcare Specializations
    "Patient-Care": "Direct patient interaction and bedside care",
    "Medical-Lab": "Laboratory diagnostics and pharmaceutical work",
    "Rehab-Therapy": "Rehabilitation and therapeutic services",
    "Health-Admin": "Healthcare information and administration",
    
    # Technology Specializations
    "Software-Dev": "Software development and programming",
    "Hardware-Systems": "Electronics, circuits, and hardware",
    "Data-Analytics": "Data science, statistics, and machine learning",
    "Cyber-Defense": "Cybersecurity and information protection",
    
    # Engineering Specializations
    "Civil-Build": "Infrastructure, construction, and structural design",
    "Electrical-Power": "Power systems and electrical circuits",
    "Mechanical-Design": "Machines, mechanics, and thermal systems",
    "Industrial-Ops": "Process optimization and industrial management",
    
    # Business Specializations
    "Finance-Acct": "Accounting, finance, and fiscal management",
    "Marketing-Sales": "Marketing, sales, and advertising",
    "Startup-Venture": "Entrepreneurship and business creation",
    
    # Education
    "Teaching-Ed": "Teaching and educational instruction",
    
    # Arts & Design
    "Visual-Design": "Visual arts, graphics, and illustration",
    "Digital-Media": "Animation, multimedia, and digital content",
    "Spatial-Design": "Architecture, interior, and spatial planning",
    
    # Science
    "Lab-Research": "Laboratory-based scientific research",
    "Field-Research": "Field-based environmental research",
    
    # Public Service
    "Law-Enforce": "Law enforcement and criminal justice",
    "Community-Serve": "Community service and public administration",
    
    # Maritime
    "Maritime-Sea": "Maritime navigation and marine engineering",
    
    # Agriculture
    "Agri-Nature": "Agriculture, forestry, and natural resources",
    
    # Hospitality
    "Hospitality-Svc": "Hospitality, tourism, and food service",
    
    # Skill Traits
    "Technical-Skill": "Requires technical and technological proficiency",
    "People-Skill": "Requires strong interpersonal abilities",
    "Creative-Skill": "Requires creativity and design thinking",
    "Analytical-Skill": "Requires analysis and research abilities",
    "Physical-Skill": "Requires physical activity and stamina",
    "Admin-Skill": "Requires organization and management skills"
}


COURSES_POOL_SPECIALIZED = [
    # ============== TECHNOLOGY & COMPUTING ==============
    {"course_name": "BS Computer Science", 
     "description": "Study of algorithms, programming, AI, and software development.", 
     "minimum_gwa": 85, "required_strand": "STEM",
     "trait_tag": ["Investigative", "Software-Dev", "Technical-Skill"]},
    
    {"course_name": "BS Information Technology", 
     "description": "IT infrastructure, networking, systems administration, and web development.", 
     "minimum_gwa": 82, "required_strand": "STEM",
     "trait_tag": ["Realistic", "Software-Dev", "Technical-Skill"]},
    
    {"course_name": "BS Computer Engineering", 
     "description": "Hardware-software integration, embedded systems, and computer architecture.", 
     "minimum_gwa": 85, "required_strand": "STEM",
     "trait_tag": ["Investigative", "Hardware-Systems", "Technical-Skill"]},
    
    {"course_name": "BS Electronics Engineering", 
     "description": "Electronic circuits, communications systems, and signal processing.", 
     "minimum_gwa": 85, "required_strand": "STEM",
     "trait_tag": ["Investigative", "Hardware-Systems", "Technical-Skill"]},
    
    {"course_name": "BS Data Science", 
     "description": "Big data analytics, machine learning, and statistical modeling.", 
     "minimum_gwa": 85, "required_strand": "STEM",
     "trait_tag": ["Investigative", "Data-Analytics", "Analytical-Skill"]},
    
    {"course_name": "BS Cybersecurity", 
     "description": "Information security, ethical hacking, and network defense.", 
     "minimum_gwa": 85, "required_strand": "STEM",
     "trait_tag": ["Investigative", "Cyber-Defense", "Technical-Skill"]},
    
    {"course_name": "BS Entertainment and Multimedia Computing", 
     "description": "Game development, interactive media, and digital entertainment.", 
     "minimum_gwa": 82, "required_strand": "STEM",
     "trait_tag": ["Artistic", "Digital-Media", "Creative-Skill"]},
    
    # ============== ENGINEERING ==============
    {"course_name": "BS Civil Engineering", 
     "description": "Design and construction of infrastructure like bridges, roads, and buildings.", 
     "minimum_gwa": 85, "required_strand": "STEM",
     "trait_tag": ["Realistic", "Civil-Build", "Technical-Skill"]},
    
    {"course_name": "BS Mechanical Engineering", 
     "description": "Design of mechanical systems, thermodynamics, and manufacturing.", 
     "minimum_gwa": 85, "required_strand": "STEM",
     "trait_tag": ["Realistic", "Mechanical-Design", "Technical-Skill"]},
    
    {"course_name": "BS Electrical Engineering", 
     "description": "Power generation, electrical systems, and electronics.", 
     "minimum_gwa": 85, "required_strand": "STEM",
     "trait_tag": ["Investigative", "Electrical-Power", "Technical-Skill"]},
    
    {"course_name": "BS Industrial Engineering", 
     "description": "Process optimization, operations management, and quality control.", 
     "minimum_gwa": 85, "required_strand": "STEM",
     "trait_tag": ["Enterprising", "Industrial-Ops", "Analytical-Skill"]},
    
    {"course_name": "BS Geodetic Engineering", 
     "description": "Land surveying, mapping, and geographic information systems.", 
     "minimum_gwa": 83, "required_strand": "STEM",
     "trait_tag": ["Realistic", "Civil-Build", "Technical-Skill"]},
    
    {"course_name": "BS Aeronautical Engineering", 
     "description": "Design and maintenance of aircraft and aerospace systems.", 
     "minimum_gwa": 88, "required_strand": "STEM",
     "trait_tag": ["Investigative", "Mechanical-Design", "Technical-Skill"]},
    
    # ============== HEALTHCARE - PATIENT CARE ==============
    {"course_name": "BS Nursing", 
     "description": "Professional training in patient care, health promotion, and community health nursing.", 
     "minimum_gwa": 85, "required_strand": "STEM",
     "trait_tag": ["Social", "Patient-Care", "People-Skill"]},
    
    {"course_name": "BS Midwifery", 
     "description": "Primary healthcare for women during pregnancy, childbirth, and the postpartum period.", 
     "minimum_gwa": 82, "required_strand": "STEM",
     "trait_tag": ["Social", "Patient-Care", "People-Skill"]},
    
    # ============== HEALTHCARE - MEDICAL LAB ==============
    {"course_name": "BS Medical Technology", 
     "description": "Laboratory analysis of blood, tissues, and other specimens for diagnosis.", 
     "minimum_gwa": 85, "required_strand": "STEM",
     "trait_tag": ["Investigative", "Medical-Lab", "Analytical-Skill"]},
    
    {"course_name": "BS Pharmacy", 
     "description": "Drug formulation, dispensing, and pharmaceutical care.", 
     "minimum_gwa": 85, "required_strand": "STEM",
     "trait_tag": ["Investigative", "Medical-Lab", "Analytical-Skill"]},
    
    {"course_name": "BS Radiologic Technology", 
     "description": "Operating medical imaging equipment like X-rays, CT scans, and MRI.", 
     "minimum_gwa": 83, "required_strand": "STEM",
     "trait_tag": ["Realistic", "Medical-Lab", "Technical-Skill"]},
    
    # ============== HEALTHCARE - REHABILITATION ==============
    {"course_name": "BS Physical Therapy", 
     "description": "Rehabilitation through physical exercises and therapeutic techniques.", 
     "minimum_gwa": 85, "required_strand": "STEM",
     "trait_tag": ["Social", "Rehab-Therapy", "Physical-Skill"]},
    
    {"course_name": "BS Occupational Therapy", 
     "description": "Helping patients develop or recover daily living and work skills.", 
     "minimum_gwa": 85, "required_strand": "STEM",
     "trait_tag": ["Social", "Rehab-Therapy", "People-Skill"]},
    
    {"course_name": "BS Speech-Language Pathology", 
     "description": "Diagnosis and treatment of communication and swallowing disorders.", 
     "minimum_gwa": 85, "required_strand": "STEM",
     "trait_tag": ["Social", "Rehab-Therapy", "People-Skill"]},
    
    {"course_name": "BS Respiratory Therapy", 
     "description": "Treatment of patients with breathing or cardiopulmonary disorders.", 
     "minimum_gwa": 83, "required_strand": "STEM",
     "trait_tag": ["Realistic", "Rehab-Therapy", "Technical-Skill"]},
    
    # ============== HEALTHCARE - OTHER ==============
    {"course_name": "BS Nutrition and Dietetics", 
     "description": "Study of food science and the role of nutrition in health and disease management.", 
     "minimum_gwa": 83, "required_strand": "STEM",
     "trait_tag": ["Social", "Patient-Care", "Analytical-Skill"]},
    
    {"course_name": "BS Optometry", 
     "description": "Examining eyes for defects and prescribing corrective lenses.", 
     "minimum_gwa": 85, "required_strand": "STEM",
     "trait_tag": ["Investigative", "Medical-Lab", "Technical-Skill"]},
    
    {"course_name": "BS Health Information Management", 
     "description": "Managing patient health records and healthcare data systems.", 
     "minimum_gwa": 82, "required_strand": "STEM",
     "trait_tag": ["Conventional", "Health-Admin", "Admin-Skill"]},
    
    {"course_name": "Doctor of Veterinary Medicine", 
     "description": "Medical care for animals including diagnosis, treatment, and surgery.", 
     "minimum_gwa": 85, "required_strand": "STEM",
     "trait_tag": ["Investigative", "Patient-Care", "Analytical-Skill"]},
    
    # ============== BUSINESS - FINANCE ==============
    {"course_name": "BS Accountancy", 
     "description": "Financial reporting, auditing, and tax accounting.", 
     "minimum_gwa": 85, "required_strand": "ABM",
     "trait_tag": ["Conventional", "Finance-Acct", "Analytical-Skill"]},
    
    {"course_name": "BS Business Administration major in Financial Management", 
     "description": "Corporate finance, investment analysis, and financial planning.", 
     "minimum_gwa": 82, "required_strand": "ABM",
     "trait_tag": ["Enterprising", "Finance-Acct", "Analytical-Skill"]},
    
    {"course_name": "BS Management Accounting", 
     "description": "Cost accounting, budgeting, and management financial analysis.", 
     "minimum_gwa": 83, "required_strand": "ABM",
     "trait_tag": ["Conventional", "Finance-Acct", "Analytical-Skill"]},
    
    {"course_name": "BS Accounting Information Systems", 
     "description": "Integration of accounting with information technology systems.", 
     "minimum_gwa": 83, "required_strand": "ABM",
     "trait_tag": ["Conventional", "Finance-Acct", "Technical-Skill"]},
    
    {"course_name": "BS Business Economics", 
     "description": "Economic analysis for business decision-making.", 
     "minimum_gwa": 85, "required_strand": "ABM",
     "trait_tag": ["Investigative", "Finance-Acct", "Analytical-Skill"]},
    
    {"course_name": "BS Customs Administration", 
     "description": "Customs procedures, international trade, and tariff management.", 
     "minimum_gwa": 82, "required_strand": "ABM",
     "trait_tag": ["Conventional", "Finance-Acct", "Admin-Skill"]},
    
    # ============== BUSINESS - MARKETING ==============
    {"course_name": "BS Business Administration major in Marketing Management", 
     "description": "Marketing strategies, consumer behavior, and brand management.", 
     "minimum_gwa": 82, "required_strand": "ABM",
     "trait_tag": ["Enterprising", "Marketing-Sales", "People-Skill"]},
    
    {"course_name": "BS Business Administration major in Human Resource Management", 
     "description": "Recruitment, training, and employee relations.", 
     "minimum_gwa": 82, "required_strand": "ABM",
     "trait_tag": ["Social", "Marketing-Sales", "People-Skill"]},
    
    {"course_name": "BS Real Estate Management", 
     "description": "Property development, sales, and real estate investments.", 
     "minimum_gwa": 82, "required_strand": "ABM",
     "trait_tag": ["Enterprising", "Marketing-Sales", "People-Skill"]},
    
    # ============== BUSINESS - ENTREPRENEURSHIP ==============
    {"course_name": "BS Entrepreneurship", 
     "description": "Starting and managing new business ventures.", 
     "minimum_gwa": 80, "required_strand": "ABM",
     "trait_tag": ["Enterprising", "Startup-Venture", "Creative-Skill"]},
    
    {"course_name": "BS Business Administration major in Operations Management", 
     "description": "Supply chain, logistics, and operations optimization.", 
     "minimum_gwa": 82, "required_strand": "ABM",
     "trait_tag": ["Enterprising", "Industrial-Ops", "Admin-Skill"]},
    
    {"course_name": "BS Agribusiness", 
     "description": "Business management in agriculture and food industries.", 
     "minimum_gwa": 80, "required_strand": "ABM",
     "trait_tag": ["Enterprising", "Agri-Nature", "Admin-Skill"]},
    
    # ============== EDUCATION ==============
    {"course_name": "Bachelor of Elementary Education", 
     "description": "Teaching in elementary school (Grades 1-6).", 
     "minimum_gwa": 80, "required_strand": "GAS",
     "trait_tag": ["Social", "Teaching-Ed", "People-Skill"]},
    
    {"course_name": "Bachelor of Secondary Education", 
     "description": "Teaching in junior and senior high school.", 
     "minimum_gwa": 80, "required_strand": "GAS",
     "trait_tag": ["Social", "Teaching-Ed", "People-Skill"]},
    
    {"course_name": "Bachelor of Early Childhood Education", 
     "description": "Teaching preschool and kindergarten children.", 
     "minimum_gwa": 80, "required_strand": "GAS",
     "trait_tag": ["Social", "Teaching-Ed", "Creative-Skill"]},
    
    {"course_name": "Bachelor of Special Needs Education", 
     "description": "Teaching students with disabilities and special learning needs.", 
     "minimum_gwa": 80, "required_strand": "GAS",
     "trait_tag": ["Social", "Teaching-Ed", "People-Skill"]},
    
    {"course_name": "Bachelor of Physical Education", 
     "description": "Physical fitness instruction and sports coaching.", 
     "minimum_gwa": 80, "required_strand": "GAS",
     "trait_tag": ["Social", "Teaching-Ed", "Physical-Skill"]},
    
    {"course_name": "Bachelor of Technical-Vocational Teacher Education", 
     "description": "Training for teachers in technical and vocational fields.", 
     "minimum_gwa": 80, "required_strand": "TVL",
     "trait_tag": ["Realistic", "Teaching-Ed", "Technical-Skill"]},
    
    {"course_name": "Bachelor of Library and Information Science", 
     "description": "Library management, information organization, and research services.", 
     "minimum_gwa": 80, "required_strand": "GAS",
     "trait_tag": ["Conventional", "Teaching-Ed", "Admin-Skill"]},
    
    # ============== ARTS & DESIGN - VISUAL ==============
    {"course_name": "Bachelor of Fine Arts", 
     "description": "Studio art, painting, sculpture, and visual arts.", 
     "minimum_gwa": 80, "required_strand": "HUMSS",
     "trait_tag": ["Artistic", "Visual-Design", "Creative-Skill"]},
    
    {"course_name": "BS Multimedia Arts", 
     "description": "Digital design, graphics, and multimedia production.", 
     "minimum_gwa": 80, "required_strand": "HUMSS",
     "trait_tag": ["Artistic", "Visual-Design", "Creative-Skill"]},
    
    {"course_name": "BA in Advertising Arts", 
     "description": "Visual communication for advertising and branding.", 
     "minimum_gwa": 80, "required_strand": "HUMSS",
     "trait_tag": ["Artistic", "Visual-Design", "Creative-Skill"]},
    
    {"course_name": "BA in Photography", 
     "description": "Photography techniques, editing, and visual storytelling.", 
     "minimum_gwa": 80, "required_strand": "HUMSS",
     "trait_tag": ["Artistic", "Visual-Design", "Creative-Skill"]},
    
    # ============== ARTS & DESIGN - DIGITAL MEDIA ==============
    {"course_name": "BA in Animation", 
     "description": "2D/3D animation, motion graphics, and visual effects.", 
     "minimum_gwa": 80, "required_strand": "HUMSS",
     "trait_tag": ["Artistic", "Digital-Media", "Technical-Skill"]},
    
    {"course_name": "BA in Game Art and Design", 
     "description": "Game graphics, character design, and interactive media.", 
     "minimum_gwa": 80, "required_strand": "HUMSS",
     "trait_tag": ["Artistic", "Digital-Media", "Technical-Skill"]},
    
    {"course_name": "BA in Digital Filmmaking", 
     "description": "Video production, cinematography, and film editing.", 
     "minimum_gwa": 80, "required_strand": "HUMSS",
     "trait_tag": ["Artistic", "Digital-Media", "Technical-Skill"]},
    
    {"course_name": "BA in Music Production", 
     "description": "Audio engineering, music composition, and sound design.", 
     "minimum_gwa": 80, "required_strand": "HUMSS",
     "trait_tag": ["Artistic", "Digital-Media", "Creative-Skill"]},
    
    # ============== ARTS & DESIGN - SPATIAL ==============
    {"course_name": "BS Architecture", 
     "description": "Building design, urban planning, and structural aesthetics.", 
     "minimum_gwa": 85, "required_strand": "STEM",
     "trait_tag": ["Artistic", "Spatial-Design", "Technical-Skill"]},
    
    {"course_name": "BS Interior Design", 
     "description": "Interior space planning, decoration, and functional design.", 
     "minimum_gwa": 80, "required_strand": "HUMSS",
     "trait_tag": ["Artistic", "Spatial-Design", "Creative-Skill"]},
    
    {"course_name": "BS Landscape Architecture", 
     "description": "Outdoor space design, parks, and environmental planning.", 
     "minimum_gwa": 83, "required_strand": "STEM",
     "trait_tag": ["Artistic", "Spatial-Design", "Creative-Skill"]},
    
    {"course_name": "BS Industrial Design", 
     "description": "Product design, manufacturing aesthetics, and ergonomics.", 
     "minimum_gwa": 82, "required_strand": "STEM",
     "trait_tag": ["Artistic", "Spatial-Design", "Creative-Skill"]},
    
    {"course_name": "BA in Fashion Design and Merchandising", 
     "description": "Clothing design, fashion trends, and retail management.", 
     "minimum_gwa": 80, "required_strand": "HUMSS",
     "trait_tag": ["Artistic", "Spatial-Design", "Creative-Skill"]},
    
    {"course_name": "BS Clothing Technology", 
     "description": "Garment production, textile science, and apparel manufacturing.", 
     "minimum_gwa": 80, "required_strand": "TVL",
     "trait_tag": ["Realistic", "Spatial-Design", "Technical-Skill"]},
    
    # ============== SCIENCE - LAB RESEARCH ==============
    {"course_name": "BS Biology", 
     "description": "Study of living organisms, genetics, and ecosystems.", 
     "minimum_gwa": 85, "required_strand": "STEM",
     "trait_tag": ["Investigative", "Lab-Research", "Analytical-Skill"]},
    
    {"course_name": "BS Chemistry", 
     "description": "Chemical compounds, reactions, and materials science.", 
     "minimum_gwa": 85, "required_strand": "STEM",
     "trait_tag": ["Investigative", "Lab-Research", "Analytical-Skill"]},
    
    {"course_name": "BS Physics", 
     "description": "Fundamental laws of nature, matter, and energy.", 
     "minimum_gwa": 88, "required_strand": "STEM",
     "trait_tag": ["Investigative", "Lab-Research", "Analytical-Skill"]},
    
    {"course_name": "BS Biotechnology", 
     "description": "Application of biology in medicine, agriculture, and industry.", 
     "minimum_gwa": 85, "required_strand": "STEM",
     "trait_tag": ["Investigative", "Lab-Research", "Technical-Skill"]},
    
    {"course_name": "BS Mathematics", 
     "description": "Pure and applied mathematics, statistics, and computation.", 
     "minimum_gwa": 85, "required_strand": "STEM",
     "trait_tag": ["Investigative", "Lab-Research", "Analytical-Skill"]},
    
    {"course_name": "BS Statistics", 
     "description": "Statistical analysis, probability, and data interpretation.", 
     "minimum_gwa": 85, "required_strand": "STEM",
     "trait_tag": ["Investigative", "Data-Analytics", "Analytical-Skill"]},
    
    {"course_name": "BS Food Technology", 
     "description": "Food processing, preservation, and quality control.", 
     "minimum_gwa": 83, "required_strand": "STEM",
     "trait_tag": ["Investigative", "Lab-Research", "Technical-Skill"]},
    
    # ============== SCIENCE - FIELD RESEARCH ==============
    {"course_name": "BS Environmental Science", 
     "description": "Environmental conservation, pollution control, and sustainability.", 
     "minimum_gwa": 83, "required_strand": "STEM",
     "trait_tag": ["Investigative", "Field-Research", "Analytical-Skill"]},
    
    {"course_name": "BS Marine Biology", 
     "description": "Study of marine organisms and ocean ecosystems.", 
     "minimum_gwa": 83, "required_strand": "STEM",
     "trait_tag": ["Investigative", "Field-Research", "Physical-Skill"]},
    
    {"course_name": "BS Geology", 
     "description": "Study of Earth's structure, minerals, and geological processes.", 
     "minimum_gwa": 83, "required_strand": "STEM",
     "trait_tag": ["Investigative", "Field-Research", "Physical-Skill"]},
    
    {"course_name": "BS Meteorology", 
     "description": "Weather patterns, climate science, and atmospheric phenomena.", 
     "minimum_gwa": 83, "required_strand": "STEM",
     "trait_tag": ["Investigative", "Field-Research", "Analytical-Skill"]},
    
    {"course_name": "BS Environmental Planning", 
     "description": "Land use planning, urban development, and environmental policy.", 
     "minimum_gwa": 83, "required_strand": "STEM",
     "trait_tag": ["Investigative", "Field-Research", "Admin-Skill"]},
    
    # ============== PUBLIC SERVICE - LAW ENFORCEMENT ==============
    {"course_name": "BS Criminology", 
     "description": "Criminal justice, law enforcement, and forensic investigation.", 
     "minimum_gwa": 80, "required_strand": "GAS",
     "trait_tag": ["Realistic", "Law-Enforce", "Physical-Skill"]},
    
    {"course_name": "BS Forensic Science", 
     "description": "Scientific analysis of evidence for criminal investigations.", 
     "minimum_gwa": 85, "required_strand": "STEM",
     "trait_tag": ["Investigative", "Law-Enforce", "Analytical-Skill"]},
    
    {"course_name": "BS Legal Management", 
     "description": "Legal procedures, paralegal work, and law office management.", 
     "minimum_gwa": 83, "required_strand": "ABM",
     "trait_tag": ["Conventional", "Law-Enforce", "Admin-Skill"]},
    
    # ============== PUBLIC SERVICE - COMMUNITY ==============
    {"course_name": "Bachelor of Public Administration", 
     "description": "Government operations, public policy, and civil service.", 
     "minimum_gwa": 80, "required_strand": "GAS",
     "trait_tag": ["Enterprising", "Community-Serve", "Admin-Skill"]},
    
    {"course_name": "BS Social Work", 
     "description": "Community welfare, counseling, and social services.", 
     "minimum_gwa": 80, "required_strand": "HUMSS",
     "trait_tag": ["Social", "Community-Serve", "People-Skill"]},
    
    {"course_name": "BS Community Development", 
     "description": "Community organizing, development programs, and social change.", 
     "minimum_gwa": 80, "required_strand": "HUMSS",
     "trait_tag": ["Social", "Community-Serve", "People-Skill"]},
    
    {"course_name": "BA in Political Science", 
     "description": "Political systems, governance, and public policy analysis.", 
     "minimum_gwa": 83, "required_strand": "HUMSS",
     "trait_tag": ["Investigative", "Community-Serve", "Analytical-Skill"]},
    
    {"course_name": "BA in International Studies", 
     "description": "International relations, diplomacy, and global affairs.", 
     "minimum_gwa": 83, "required_strand": "HUMSS",
     "trait_tag": ["Investigative", "Community-Serve", "Analytical-Skill"]},
    
    # ============== MARITIME ==============
    {"course_name": "BS Marine Transportation", 
     "description": "Ship navigation, maritime law, and vessel operations.", 
     "minimum_gwa": 80, "required_strand": "STEM",
     "trait_tag": ["Realistic", "Maritime-Sea", "Physical-Skill"]},
    
    {"course_name": "BS Marine Engineering", 
     "description": "Ship engine systems, maintenance, and marine machinery.", 
     "minimum_gwa": 83, "required_strand": "STEM",
     "trait_tag": ["Realistic", "Maritime-Sea", "Technical-Skill"]},
    
    # ============== AGRICULTURE ==============
    {"course_name": "BS Agriculture", 
     "description": "Crop production, soil management, and agricultural technology.", 
     "minimum_gwa": 80, "required_strand": "STEM",
     "trait_tag": ["Realistic", "Agri-Nature", "Physical-Skill"]},
    
    {"course_name": "BS Forestry", 
     "description": "Forest management, conservation, and natural resources.", 
     "minimum_gwa": 80, "required_strand": "STEM",
     "trait_tag": ["Realistic", "Agri-Nature", "Physical-Skill"]},
    
    {"course_name": "BS Fisheries", 
     "description": "Aquaculture, fish production, and marine resource management.", 
     "minimum_gwa": 80, "required_strand": "STEM",
     "trait_tag": ["Realistic", "Agri-Nature", "Physical-Skill"]},
    
    # ============== HOSPITALITY & TOURISM ==============
    {"course_name": "BS Hospitality Management", 
     "description": "Hotel operations, event management, and guest services.", 
     "minimum_gwa": 80, "required_strand": "TVL",
     "trait_tag": ["Enterprising", "Hospitality-Svc", "People-Skill"]},
    
    {"course_name": "BS Tourism Management", 
     "description": "Travel planning, tour operations, and destination management.", 
     "minimum_gwa": 80, "required_strand": "TVL",
     "trait_tag": ["Enterprising", "Hospitality-Svc", "People-Skill"]},
    
    {"course_name": "BS Culinary Management", 
     "description": "Culinary arts, restaurant management, and food service.", 
     "minimum_gwa": 80, "required_strand": "TVL",
     "trait_tag": ["Artistic", "Hospitality-Svc", "Creative-Skill"]},
    
    {"course_name": "BS Office Administration", 
     "description": "Office management, administrative support, and business communication.", 
     "minimum_gwa": 80, "required_strand": "ABM",
     "trait_tag": ["Conventional", "Hospitality-Svc", "Admin-Skill"]},
    
    # ============== COMMUNICATION & MEDIA ==============
    {"course_name": "BA in Communication", 
     "description": "Mass media, public relations, and corporate communication.", 
     "minimum_gwa": 82, "required_strand": "HUMSS",
     "trait_tag": ["Social", "Marketing-Sales", "People-Skill"]},
    
    {"course_name": "BA in Journalism", 
     "description": "News writing, investigative reporting, and broadcast journalism.", 
     "minimum_gwa": 82, "required_strand": "HUMSS",
     "trait_tag": ["Investigative", "Marketing-Sales", "Analytical-Skill"]},
    
    {"course_name": "BS Development Communication", 
     "description": "Communication for social development and community engagement.", 
     "minimum_gwa": 82, "required_strand": "HUMSS",
     "trait_tag": ["Social", "Community-Serve", "People-Skill"]},
    
    # ============== PSYCHOLOGY & SOCIAL SCIENCES ==============
    {"course_name": "BS Psychology", 
     "description": "Human behavior, mental processes, and psychological assessment.", 
     "minimum_gwa": 85, "required_strand": "HUMSS",
     "trait_tag": ["Investigative", "Rehab-Therapy", "Analytical-Skill"]},
    
    {"course_name": "BA in Sociology", 
     "description": "Social structures, human interactions, and societal patterns.", 
     "minimum_gwa": 82, "required_strand": "HUMSS",
     "trait_tag": ["Investigative", "Community-Serve", "Analytical-Skill"]},
    
    {"course_name": "BA in Philosophy", 
     "description": "Critical thinking, ethics, and fundamental questions of existence.", 
     "minimum_gwa": 82, "required_strand": "HUMSS",
     "trait_tag": ["Investigative", "Lab-Research", "Analytical-Skill"]},
    
    {"course_name": "BA in Linguistics", 
     "description": "Language structure, communication patterns, and linguistic analysis.", 
     "minimum_gwa": 82, "required_strand": "HUMSS",
     "trait_tag": ["Investigative", "Teaching-Ed", "Analytical-Skill"]},
    
    # ============== PERFORMING ARTS ==============
    {"course_name": "BA in Theater Arts", 
     "description": "Acting, stage production, and dramatic arts.", 
     "minimum_gwa": 80, "required_strand": "HUMSS",
     "trait_tag": ["Artistic", "Visual-Design", "Creative-Skill"]},
    
    # ============== EXERCISE & SPORTS ==============
    {"course_name": "BS Exercise and Sports Science", 
     "description": "Exercise physiology, sports training, and athletic performance.", 
     "minimum_gwa": 82, "required_strand": "STEM",
     "trait_tag": ["Investigative", "Rehab-Therapy", "Physical-Skill"]},
    
    # ============== AVIATION ==============
    {"course_name": "BS Aircraft Maintenance Technology", 
     "description": "Aircraft repair, maintenance, and aviation safety.", 
     "minimum_gwa": 83, "required_strand": "STEM",
     "trait_tag": ["Realistic", "Hardware-Systems", "Technical-Skill"]},
    
    {"course_name": "BS Aviation Electronics Technology", 
     "description": "Aircraft electronic systems and avionics maintenance.", 
     "minimum_gwa": 83, "required_strand": "STEM",
     "trait_tag": ["Realistic", "Hardware-Systems", "Technical-Skill"]},
]

# Verify trait coverage
if __name__ == "__main__":
    trait_counts = {}
    for course in COURSES_POOL_SPECIALIZED:
        for trait in course.get("trait_tag", []):
            trait_counts[trait] = trait_counts.get(trait, 0) + 1
    
    print("=" * 60)
    print("SPECIALIZED TRAIT SYSTEM - COURSE COVERAGE")
    print("=" * 60)
    for trait, count in sorted(trait_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"{trait}: {count} courses")
    print(f"\nTotal: {len(trait_counts)} unique traits across {len(COURSES_POOL_SPECIALIZED)} courses")
