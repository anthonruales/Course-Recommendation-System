# courses_focused.py - Optimized Traits for Better Accuracy
"""
================================================================================
IMPROVED TRAIT SYSTEM BASED ON HOLLAND'S RIASEC + PRACTICAL DIMENSIONS
================================================================================

WHY THIS IS BETTER:
- Based on scientifically-validated career assessment model (RIASEC)
- Each trait is clearly distinct (no overlap like "Logical" vs "Analytical")
- Easy to measure through questions
- Direct connection to career success prediction

CORE TRAIT TYPES:

HOLLAND'S RIASEC (6 interest types):
├── Realistic (R)     → Hands-on, practical, building/fixing things
├── Investigative (I) → Research, analysis, understanding systems
├── Artistic (A)      → Creative, expressive, original ideas
├── Social (S)        → Helping, teaching, caring for others
├── Enterprising (E)  → Leading, persuading, taking charge
└── Conventional (C)  → Organizing, detailed work, procedures

SKILL/DOMAIN (6 types):
├── Technical         → Technology, machines, equipment
├── Scientific        → Lab work, research, experimentation
├── Numbers           → Math, statistics, financial data
├── Words             → Writing, speaking, languages
├── Visual            → Design, images, spatial thinking
└── Physical          → Active, movement, sports

ENVIRONMENT (3 types):
├── Outdoor           → Nature, fieldwork, outside
├── Healthcare        → Clinical settings, patient care
└── Business          → Corporate, commerce, trade

BONUS (2 types):
├── Problem-solving   → Tackling challenges, finding solutions
└── Creative          → Original ideas, thinking outside box

================================================================================
"""

COURSES_POOL_FOCUSED = [
    # ============== TECHNICAL & ANALYTICAL ==============
    {"course_name": "BS Computer Science", 
     "description": "Study of computation, complexity, and advanced software design.", 
     "minimum_gwa": 88, "recommended_strand": "STEM", 
     "trait_tag": ["Investigative", "Technical", "Problem-solving"]},
    
    {"course_name": "BS Information Technology", 
     "description": "Focuses on the practical application of computing technology to business processes.", 
     "minimum_gwa": 85, "recommended_strand": "STEM", 
     "trait_tag": ["Realistic", "Technical", "Social"]},
    
    {"course_name": "BS Civil Engineering", 
     "description": "Design and supervision of infrastructure projects like roads, bridges, and buildings.", 
     "minimum_gwa": 90, "recommended_strand": "STEM", 
     "trait_tag": ["Realistic", "Investigative", "Visual"]},
    
    {"course_name": "BS Computer Engineering", 
     "description": "Combines electronics engineering and computer science to develop computer hardware and software systems.", 
     "minimum_gwa": 88, "recommended_strand": "STEM", 
     "trait_tag": ["Realistic", "Investigative", "Technical"]},
    
    {"course_name": "BS Electronics Engineering", 
     "description": "Design and development of electronic circuits, communication systems, and automated devices.", 
     "minimum_gwa": 88, "recommended_strand": "STEM", 
     "trait_tag": ["Realistic", "Investigative", "Technical"]},
    
    {"course_name": "BS Mechanical Engineering", 
     "description": "Focuses on the design, analysis, and manufacturing of mechanical systems and machinery.", 
     "minimum_gwa": 88, "recommended_strand": "STEM", 
     "trait_tag": ["Realistic", "Investigative", "Visual"]},
    
    {"course_name": "BS Electrical Engineering", 
     "description": "Study of electricity, electronics, and electromagnetism for power generation and distribution.", 
     "minimum_gwa": 88, "recommended_strand": "STEM", 
     "trait_tag": ["Investigative", "Technical", "Problem-solving"]},
    
    {"course_name": "BS Data Science", 
     "description": "Uses scientific methods, algorithms, and systems to extract knowledge and insights from structured and unstructured data.", 
     "minimum_gwa": 89, "recommended_strand": "STEM", 
     "trait_tag": ["Investigative", "Numbers", "Technical"]},
    
    {"course_name": "BS Mathematics", 
     "description": "Advanced study of mathematical structures, logic, and numerical analysis for various industries.", 
     "minimum_gwa": 87, "recommended_strand": "STEM", 
     "trait_tag": ["Investigative", "Numbers", "Problem-solving"]},
    
    {"course_name": "BS Statistics", 
     "description": "Focuses on the collection, analysis, interpretation, and presentation of quantitative data.", 
     "minimum_gwa": 86, "recommended_strand": "STEM", 
     "trait_tag": ["Investigative", "Numbers", "Conventional"]},
    
    {"course_name": "BS Geodetic Engineering", 
     "description": "Professional study of surveying, mapping, and global positioning systems (GPS).", 
     "minimum_gwa": 86, "recommended_strand": "STEM", 
     "trait_tag": ["Realistic", "Outdoor", "Technical"]},
    
    {"course_name": "BS Industrial Engineering", 
     "description": "Focuses on optimizing complex processes, systems, and organizations to reduce waste.", 
     "minimum_gwa": 86, "recommended_strand": "STEM", 
     "trait_tag": ["Investigative", "Enterprising", "Problem-solving"]},
    
    {"course_name": "BS Cybersecurity", 
     "description": "Specialized training in protecting networks, devices, and data from digital attacks.", 
     "minimum_gwa": 87, "recommended_strand": "STEM", 
     "trait_tag": ["Investigative", "Technical", "Problem-solving"]},

    # ============== BUSINESS & LEADERSHIP ==============
    {"course_name": "BS Accountancy", 
     "description": "Detailed study of financial reporting, auditing, and taxation.", 
     "minimum_gwa": 92, "recommended_strand": "ABM", 
     "trait_tag": ["Conventional", "Numbers", "Business"]},
    
    {"course_name": "BS Business Administration major in Marketing Management", 
     "description": "Focuses on market research, consumer behavior, and strategic brand positioning.", 
     "minimum_gwa": 85, "recommended_strand": "ABM", 
     "trait_tag": ["Enterprising", "Artistic", "Social"]},
    
    {"course_name": "BS Business Administration major in Financial Management", 
     "description": "Deals with investment decisions, capital markets, and corporate financial planning.", 
     "minimum_gwa": 86, "recommended_strand": "ABM", 
     "trait_tag": ["Enterprising", "Numbers", "Business"]},
    
    {"course_name": "BS Business Administration major in Human Resource Management", 
     "description": "Studies organizational behavior, employee relations, and talent development.", 
     "minimum_gwa": 84, "recommended_strand": "ABM", 
     "trait_tag": ["Social", "Enterprising", "Business"]},
    
    {"course_name": "BS Entrepreneurship", 
     "description": "Develops skills in identifying business opportunities and managing new ventures.", 
     "minimum_gwa": 83, "recommended_strand": "ABM", 
     "trait_tag": ["Enterprising", "Artistic", "Business"]},
    
    {"course_name": "BS Customs Administration", 
     "description": "Focuses on tariff and customs laws, international trade, and logistics.", 
     "minimum_gwa": 85, "recommended_strand": "ABM", 
     "trait_tag": ["Conventional", "Business", "Numbers"]},
    
    {"course_name": "BS Real Estate Management", 
     "description": "Deals with property appraisal, brokerage, and real estate development laws.", 
     "minimum_gwa": 84, "recommended_strand": "ABM", 
     "trait_tag": ["Enterprising", "Social", "Business"]},
    
    {"course_name": "BS Accounting Information Systems", 
     "description": "Combines accounting principles with information technology to manage business financial data.", 
     "minimum_gwa": 88, "recommended_strand": "ABM", 
     "trait_tag": ["Conventional", "Technical", "Numbers"]},
    
    {"course_name": "BS Management Accounting", 
     "description": "Focuses on providing internal financial information for business decision-making and strategic planning.", 
     "minimum_gwa": 88, "recommended_strand": "ABM", 
     "trait_tag": ["Conventional", "Numbers", "Business"]},
    
    {"course_name": "BS Business Administration major in Operations Management", 
     "description": "Focuses on the production and delivery of goods and services, logistics, and supply chain.", 
     "minimum_gwa": 84, "recommended_strand": "ABM", 
     "trait_tag": ["Enterprising", "Conventional", "Business"]},
    
    {"course_name": "BS Business Economics", 
     "description": "Study of economic theories and their practical application in business environments.", 
     "minimum_gwa": 86, "recommended_strand": "ABM", 
     "trait_tag": ["Investigative", "Numbers", "Business"]},
    
    {"course_name": "BS Agribusiness", 
     "description": "Management and operations of agricultural businesses and the food supply chain.", 
     "minimum_gwa": 83, "recommended_strand": "ABM", 
     "trait_tag": ["Enterprising", "Outdoor", "Business"]},
    
    {"course_name": "BS Legal Management", 
     "description": "Study of business administration combined with essential legal principles and procedures.", 
     "minimum_gwa": 87, "recommended_strand": "ABM", 
     "trait_tag": ["Investigative", "Conventional", "Words"]},
    
    {"course_name": "Bachelor of Public Administration", 
     "description": "Preparation for leadership roles in government, non-profits, and public service organizations.", 
     "minimum_gwa": 85, "recommended_strand": "HUMSS", 
     "trait_tag": ["Enterprising", "Social", "Conventional"]},

    # ============== SCIENCE & HEALTHCARE ==============
    {"course_name": "BS Medical Technology", 
     "description": "Focuses on laboratory analysis of blood, tissues, and fluids for disease diagnosis.", 
     "minimum_gwa": 90, "recommended_strand": "STEM", 
     "trait_tag": ["Investigative", "Scientific", "Healthcare"]},
    
    {"course_name": "BS Pharmacy", 
     "description": "Study of drug preparation, therapeutic uses, and pharmaceutical chemistry.", 
     "minimum_gwa": 88, "recommended_strand": "STEM", 
     "trait_tag": ["Investigative", "Scientific", "Healthcare"]},
    
    {"course_name": "BS Physical Therapy", 
     "description": "Rehabilitation science focusing on improving patient mobility and physical function.", 
     "minimum_gwa": 89, "recommended_strand": "STEM", 
     "trait_tag": ["Social", "Healthcare", "Physical"]},
    
    {"course_name": "BS Occupational Therapy", 
     "description": "Helping patients develop skills for daily living and working through therapeutic activities.", 
     "minimum_gwa": 88, "recommended_strand": "STEM", 
     "trait_tag": ["Social", "Healthcare", "Artistic"]},
    
    {"course_name": "BS Biology", 
     "description": "Scientific study of living organisms, from molecular levels to entire ecosystems.", 
     "minimum_gwa": 86, "recommended_strand": "STEM", 
     "trait_tag": ["Investigative", "Scientific", "Outdoor"]},
    
    {"course_name": "BS Radiologic Technology", 
     "description": "Operating medical imaging equipment like X-rays, CT scans, and MRI.", 
     "minimum_gwa": 85, "recommended_strand": "STEM", 
     "trait_tag": ["Realistic", "Technical", "Healthcare"]},
    
    {"course_name": "BS Nutrition and Dietetics", 
     "description": "Study of food science and the role of nutrition in health and disease management.", 
     "minimum_gwa": 85, "recommended_strand": "STEM", 
     "trait_tag": ["Social", "Scientific", "Healthcare"]},
    
    {"course_name": "BS Midwifery", 
     "description": "Primary healthcare for women during pregnancy, childbirth, and the postpartum period.", 
     "minimum_gwa": 83, "recommended_strand": "STEM", 
     "trait_tag": ["Social", "Healthcare", "Realistic"]},
    
    {"course_name": "BS Nursing", 
     "description": "Professional training in patient care, health promotion, and community health nursing.", 
     "minimum_gwa": 89, "recommended_strand": "STEM", 
     "trait_tag": ["Social", "Healthcare", "Realistic"]},
    
    {"course_name": "BS Speech-Language Pathology", 
     "description": "Specialized study in treating communication and swallowing disorders in patients.", 
     "minimum_gwa": 90, "recommended_strand": "STEM", 
     "trait_tag": ["Social", "Healthcare", "Words"]},
    
    {"course_name": "BS Respiratory Therapy", 
     "description": "Focuses on the treatment and care of patients with cardiopulmonary and breathing disorders.", 
     "minimum_gwa": 86, "recommended_strand": "STEM", 
     "trait_tag": ["Realistic", "Healthcare", "Technical"]},
    
    {"course_name": "BS Chemistry", 
     "description": "The study of matter, its properties, and how it changes during chemical reactions.", 
     "minimum_gwa": 87, "recommended_strand": "STEM", 
     "trait_tag": ["Investigative", "Scientific", "Problem-solving"]},
    
    {"course_name": "BS Marine Biology", 
     "description": "Study of marine organisms and their behaviors and interactions with the environment.", 
     "minimum_gwa": 85, "recommended_strand": "STEM", 
     "trait_tag": ["Investigative", "Scientific", "Outdoor"]},
    
    {"course_name": "BS Environmental Science", 
     "description": "Interdisciplinary study of environmental problems and human impact on the ecosystem.", 
     "minimum_gwa": 84, "recommended_strand": "STEM", 
     "trait_tag": ["Investigative", "Outdoor", "Scientific"]},
    
    {"course_name": "BS Optometry", 
     "description": "Specialized healthcare profession involving examining the eyes for defects or abnormalities.", 
     "minimum_gwa": 88, "recommended_strand": "STEM", 
     "trait_tag": ["Social", "Healthcare", "Scientific"]},
    
    {"course_name": "BS Health Information Management", 
     "description": "Combines medical science and IT to manage patient data and healthcare records.", 
     "minimum_gwa": 83, "recommended_strand": "STEM", 
     "trait_tag": ["Conventional", "Technical", "Healthcare"]},
    
    {"course_name": "BS Biotechnology", 
     "description": "Using biological systems or living organisms to develop or create different products.", 
     "minimum_gwa": 88, "recommended_strand": "STEM", 
     "trait_tag": ["Investigative", "Scientific", "Technical"]},
    
    {"course_name": "BS Exercise and Sports Science", 
     "description": "Scientific study of human movement and how the body responds to physical activity.", 
     "minimum_gwa": 82, "recommended_strand": "STEM", 
     "trait_tag": ["Investigative", "Physical", "Social"]},
    
    {"course_name": "BS Psychology", 
     "description": "Scientific study of human behavior and mental processes.", 
     "minimum_gwa": 87, "recommended_strand": "HUMSS", 
     "trait_tag": ["Investigative", "Social", "Scientific"]},

    # ============== CREATIVE & DESIGN ==============
    {"course_name": "BS Interior Design", 
     "description": "Planning and design of interior spaces to improve function and aesthetic quality of life.", 
     "minimum_gwa": 85, "recommended_strand": "STEM", 
     "trait_tag": ["Artistic", "Visual", "Realistic"]},
    
    {"course_name": "Bachelor of Fine Arts", 
     "description": "Advanced study in traditional arts like painting, sculpture, and visual theory.", 
     "minimum_gwa": 80, "recommended_strand": "HUMSS", 
     "trait_tag": ["Artistic", "Visual", "Creative"]},
    
    {"course_name": "BA in Communication", 
     "description": "Study of media production, public relations, broadcasting, and digital journalism.", 
     "minimum_gwa": 85, "recommended_strand": "HUMSS", 
     "trait_tag": ["Artistic", "Social", "Words"]},
    
    {"course_name": "BS Entertainment and Multimedia Computing", 
     "description": "Specialized study in game development, digital animation, and interactive software.", 
     "minimum_gwa": 86, "recommended_strand": "STEM", 
     "trait_tag": ["Artistic", "Technical", "Visual"]},
    
    {"course_name": "BA in Fashion Design and Merchandising", 
     "description": "Study of apparel design, textile science, and the business of the fashion industry.", 
     "minimum_gwa": 82, "recommended_strand": "HUMSS", 
     "trait_tag": ["Artistic", "Visual", "Business"]},
    
    {"course_name": "BS Industrial Design", 
     "description": "Designing mass-produced products focusing on user experience, form, and industrial function.", 
     "minimum_gwa": 85, "recommended_strand": "STEM", 
     "trait_tag": ["Artistic", "Realistic", "Visual"]},
    
    {"course_name": "BA in Digital Filmmaking", 
     "description": "Comprehensive training in cinematography, scriptwriting, and post-production editing.", 
     "minimum_gwa": 84, "recommended_strand": "HUMSS", 
     "trait_tag": ["Artistic", "Technical", "Visual"]},
    
    {"course_name": "BS Clothing Technology", 
     "description": "The technical side of garment production, quality control, and clothing manufacturing systems.", 
     "minimum_gwa": 84, "recommended_strand": "STEM", 
     "trait_tag": ["Realistic", "Conventional", "Visual"]},
    
    {"course_name": "BS Architecture", 
     "description": "Integration of art and science in designing buildings and structures with focus on aesthetics and safety.", 
     "minimum_gwa": 88, "recommended_strand": "STEM", 
     "trait_tag": ["Artistic", "Investigative", "Visual"]},
    
    {"course_name": "BS Multimedia Arts", 
     "description": "Multidisciplinary program combining graphic design, 2D/3D animation, and video production.", 
     "minimum_gwa": 83, "recommended_strand": "HUMSS", 
     "trait_tag": ["Artistic", "Technical", "Visual"]},
    
    {"course_name": "BA in Advertising Arts", 
     "description": "Focuses on visual communication, branding, and creative strategies for marketing campaigns.", 
     "minimum_gwa": 84, "recommended_strand": "HUMSS", 
     "trait_tag": ["Artistic", "Enterprising", "Visual"]},
    
    {"course_name": "BA in Animation", 
     "description": "Technical and artistic study of creating movement and storytelling through digital and traditional animation.", 
     "minimum_gwa": 82, "recommended_strand": "HUMSS", 
     "trait_tag": ["Artistic", "Technical", "Visual"]},
    
    {"course_name": "BA in Game Art and Design", 
     "description": "Focuses on the visual elements of games, including character design, environment art, and UI/UX.", 
     "minimum_gwa": 84, "recommended_strand": "STEM", 
     "trait_tag": ["Artistic", "Technical", "Visual"]},
    
    {"course_name": "BA in Photography", 
     "description": "Professional study of digital and analog photography, lighting, and visual composition.", 
     "minimum_gwa": 80, "recommended_strand": "HUMSS", 
     "trait_tag": ["Artistic", "Visual", "Technical"]},
    
    {"course_name": "BA in Music Production", 
     "description": "Study of sound design, music theory, and digital tools for audio recording and engineering.", 
     "minimum_gwa": 82, "recommended_strand": "HUMSS", 
     "trait_tag": ["Artistic", "Technical", "Creative"]},
    
    {"course_name": "BA in Theater Arts", 
     "description": "The art of performance, stage management, scriptwriting, and theatrical production.", 
     "minimum_gwa": 80, "recommended_strand": "HUMSS", 
     "trait_tag": ["Artistic", "Social", "Creative"]},
    
    {"course_name": "BS Landscape Architecture", 
     "description": "Designing outdoor public areas, parks, and gardens to harmonize with the environment.", 
     "minimum_gwa": 85, "recommended_strand": "STEM", 
     "trait_tag": ["Artistic", "Outdoor", "Visual"]},
    
    {"course_name": "BA in Journalism", 
     "description": "Specialized training in news gathering, ethics, and writing for print, broadcast, and digital media.", 
     "minimum_gwa": 85, "recommended_strand": "HUMSS", 
     "trait_tag": ["Investigative", "Words", "Social"]},

    # ============== SOCIAL, EDUCATION & SERVICE ==============
    {"course_name": "BS Criminology", 
     "description": "Study of crime prevention, law enforcement, and criminal justice.", 
     "minimum_gwa": 83, "recommended_strand": "HUMSS", 
     "trait_tag": ["Realistic", "Investigative", "Physical"]},
    
    {"course_name": "BS Hospitality Management", 
     "description": "Management of hotels, restaurants, and tourism-related businesses.", 
     "minimum_gwa": 82, "recommended_strand": "ABM", 
     "trait_tag": ["Social", "Enterprising", "Business"]},
    
    {"course_name": "Bachelor of Secondary Education", 
     "description": "Preparing teachers for high school levels with specialization in specific subject areas like Math, English, or Science.", 
     "minimum_gwa": 85, "recommended_strand": "HUMSS", 
     "trait_tag": ["Social", "Enterprising", "Words"]},
    
    {"course_name": "BS Tourism Management", 
     "description": "Focuses on travel industry operations, sustainable tourism, and heritage management.", 
     "minimum_gwa": 82, "recommended_strand": "ABM", 
     "trait_tag": ["Social", "Enterprising", "Outdoor"]},
    
    {"course_name": "BS Office Administration", 
     "description": "Training in office management, secretarial duties, and corporate records handling.", 
     "minimum_gwa": 80, "recommended_strand": "ABM", 
     "trait_tag": ["Conventional", "Social", "Business"]},
    
    {"course_name": "Bachelor of Elementary Education", 
     "description": "Training for teachers specializing in primary school education and child development.", 
     "minimum_gwa": 85, "recommended_strand": "HUMSS", 
     "trait_tag": ["Social", "Artistic", "Words"]},
    
    {"course_name": "BA in Political Science", 
     "description": "Study of government systems, political activities, and political behavior.", 
     "minimum_gwa": 86, "recommended_strand": "HUMSS", 
     "trait_tag": ["Investigative", "Enterprising", "Words"]},
    
    {"course_name": "BS Social Work", 
     "description": "Focuses on social welfare, community organizing, and helping marginalized individuals.", 
     "minimum_gwa": 84, "recommended_strand": "HUMSS", 
     "trait_tag": ["Social", "Enterprising", "Outdoor"]},
    
    {"course_name": "BS Development Communication", 
     "description": "Using communication to promote social change and community development.", 
     "minimum_gwa": 85, "recommended_strand": "HUMSS", 
     "trait_tag": ["Social", "Artistic", "Words"]},
    
    {"course_name": "Bachelor of Library and Information Science", 
     "description": "Management of information resources in libraries, archives, and digital databases.", 
     "minimum_gwa": 82, "recommended_strand": "HUMSS", 
     "trait_tag": ["Conventional", "Investigative", "Words"]},
    
    {"course_name": "BS Community Development", 
     "description": "Planning and implementing programs for community empowerment and poverty alleviation.", 
     "minimum_gwa": 84, "recommended_strand": "HUMSS", 
     "trait_tag": ["Social", "Enterprising", "Outdoor"]},
    
    {"course_name": "BS Forensic Science", 
     "description": "Application of scientific principles to criminal investigation and legal evidence.", 
     "minimum_gwa": 87, "recommended_strand": "STEM", 
     "trait_tag": ["Investigative", "Scientific", "Realistic"]},
    
    {"course_name": "Bachelor of Special Needs Education", 
     "description": "Specialized training for teaching students with diverse learning needs and disabilities.", 
     "minimum_gwa": 86, "recommended_strand": "HUMSS", 
     "trait_tag": ["Social", "Artistic", "Healthcare"]},
    
    {"course_name": "BA in International Studies", 
     "description": "Study of global issues, diplomacy, foreign languages, and international relations.", 
     "minimum_gwa": 87, "recommended_strand": "HUMSS", 
     "trait_tag": ["Investigative", "Social", "Words"]},
    
    {"course_name": "BA in Sociology", 
     "description": "Systematic study of social institutions, collective behavior, and social development.", 
     "minimum_gwa": 84, "recommended_strand": "HUMSS", 
     "trait_tag": ["Investigative", "Social", "Scientific"]},
    
    {"course_name": "BA in Philosophy", 
     "description": "Critical study of fundamental questions regarding existence, knowledge, values, and reason.", 
     "minimum_gwa": 85, "recommended_strand": "HUMSS", 
     "trait_tag": ["Investigative", "Words", "Problem-solving"]},
    
    {"course_name": "Bachelor of Early Childhood Education", 
     "description": "Focuses on the holistic development and education of children from birth to age eight.", 
     "minimum_gwa": 84, "recommended_strand": "HUMSS", 
     "trait_tag": ["Social", "Artistic", "Healthcare"]},
    
    {"course_name": "Bachelor of Physical Education", 
     "description": "Training for educators in sports, fitness, and health-related school programs.", 
     "minimum_gwa": 82, "recommended_strand": "HUMSS", 
     "trait_tag": ["Social", "Physical", "Realistic"]},
    
    {"course_name": "BA in Linguistics", 
     "description": "Scientific study of language structure, evolution, and its role in human communication.", 
     "minimum_gwa": 85, "recommended_strand": "HUMSS", 
     "trait_tag": ["Investigative", "Words", "Scientific"]},
    
    {"course_name": "BS Environmental Planning", 
     "description": "Interdisciplinary study of urban development, resource management, and sustainable land use.", 
     "minimum_gwa": 86, "recommended_strand": "STEM", 
     "trait_tag": ["Investigative", "Outdoor", "Visual"]},

    # ============== MARITIME, AVIATION & AGRICULTURE ==============
    {"course_name": "BS Marine Transportation", 
     "description": "Professional training for deck officers, focusing on navigation and ship management.", 
     "minimum_gwa": 85, "recommended_strand": "STEM", 
     "trait_tag": ["Realistic", "Outdoor", "Enterprising"]},
    
    {"course_name": "BS Marine Engineering", 
     "description": "Technical study of marine propulsion, power plants, and ship machinery maintenance.", 
     "minimum_gwa": 85, "recommended_strand": "STEM", 
     "trait_tag": ["Realistic", "Technical", "Outdoor"]},
    
    {"course_name": "BS Agriculture", 
     "description": "Scientific study of crop production, livestock raising, and soil management.", 
     "minimum_gwa": 82, "recommended_strand": "STEM", 
     "trait_tag": ["Realistic", "Outdoor", "Scientific"]},
    
    {"course_name": "BS Forestry", 
     "description": "Management and protection of forest resources, ecosystems, and wildlife conservation.", 
     "minimum_gwa": 82, "recommended_strand": "STEM", 
     "trait_tag": ["Realistic", "Outdoor", "Scientific"]},
    
    {"course_name": "BS Fisheries", 
     "description": "Study of aquaculture, fish processing, and sustainable aquatic resource management.", 
     "minimum_gwa": 82, "recommended_strand": "STEM", 
     "trait_tag": ["Realistic", "Outdoor", "Scientific"]},
    
    {"course_name": "Doctor of Veterinary Medicine", 
     "description": "Six-year program focused on the prevention, diagnosis, and treatment of animal diseases.", 
     "minimum_gwa": 88, "recommended_strand": "STEM", 
     "trait_tag": ["Investigative", "Social", "Scientific"]},
    
    {"course_name": "BS Aeronautical Engineering", 
     "description": "Design, construction, and maintenance of aircraft and spacecraft structures.", 
     "minimum_gwa": 88, "recommended_strand": "STEM", 
     "trait_tag": ["Investigative", "Technical", "Visual"]},
    
    {"course_name": "BS Aircraft Maintenance Technology", 
     "description": "Specialized training in the inspection, repair, and overhaul of aircraft engines and systems.", 
     "minimum_gwa": 85, "recommended_strand": "STEM", 
     "trait_tag": ["Realistic", "Technical", "Conventional"]},
    
    {"course_name": "BS Aviation Electronics Technology", 
     "description": "Focuses on the electronic systems (avionics) used on aircraft and satellites.", 
     "minimum_gwa": 85, "recommended_strand": "STEM", 
     "trait_tag": ["Realistic", "Technical", "Investigative"]},
    
    {"course_name": "BS Geology", 
     "description": "Study of the solid Earth, its rocks, and the processes by which they change.", 
     "minimum_gwa": 85, "recommended_strand": "STEM", 
     "trait_tag": ["Investigative", "Outdoor", "Scientific"]},
    
    {"course_name": "BS Physics", 
     "description": "Fundamental study of matter, energy, and the laws of the universe.", 
     "minimum_gwa": 87, "recommended_strand": "STEM", 
     "trait_tag": ["Investigative", "Numbers", "Scientific"]},
    
    {"course_name": "BS Meteorology", 
     "description": "Scientific study of the atmosphere and weather patterns for forecasting.", 
     "minimum_gwa": 85, "recommended_strand": "STEM", 
     "trait_tag": ["Investigative", "Scientific", "Outdoor"]},
    
    {"course_name": "BS Food Technology", 
     "description": "The application of food science to the selection, preservation, and packaging of food.", 
     "minimum_gwa": 84, "recommended_strand": "STEM", 
     "trait_tag": ["Investigative", "Scientific", "Realistic"]},
    
    {"course_name": "BS Culinary Management", 
     "description": "Combines culinary arts with business management for professional kitchen operations.", 
     "minimum_gwa": 82, "recommended_strand": "ABM", 
     "trait_tag": ["Artistic", "Realistic", "Enterprising"]},
    
    {"course_name": "Bachelor of Technical-Vocational Teacher Education", 
     "description": "Training for teachers in technical and vocational fields like welding, automotive, and electronics.", 
     "minimum_gwa": 83, "recommended_strand": "TVL", 
     "trait_tag": ["Social", "Realistic", "Technical"]},
]


# ==================== TRAIT DEFINITIONS ====================
# Use these to generate assessment questions

TRAIT_DEFINITIONS = {
    # HOLLAND'S RIASEC (6 core interest types)
    "Realistic": {
        "description": "You like working with your hands, tools, machines, or being physically active.",
        "sample_questions": [
            "Do you enjoy building or fixing things?",
            "Would you rather work with tools than sit at a desk?",
            "Do you prefer learning by doing rather than reading?"
        ]
    },
    "Investigative": {
        "description": "You enjoy researching, analyzing, and solving complex problems.",
        "sample_questions": [
            "Do you enjoy understanding how things work?",
            "Do you like solving puzzles or brain teasers?",
            "Are you curious about science and research?"
        ]
    },
    "Artistic": {
        "description": "You are creative and enjoy expressing yourself through art, design, or writing.",
        "sample_questions": [
            "Do you enjoy creating art, music, or writing?",
            "Do you prefer work that lets you be creative?",
            "Are you drawn to beautiful or unique designs?"
        ]
    },
    "Social": {
        "description": "You enjoy helping, teaching, and caring for others.",
        "sample_questions": [
            "Do you enjoy helping others with their problems?",
            "Would you like a job where you work closely with people?",
            "Do friends often come to you for advice?"
        ]
    },
    "Enterprising": {
        "description": "You like leading, persuading, and taking charge of situations.",
        "sample_questions": [
            "Do you enjoy leading a team or group?",
            "Are you comfortable convincing others of your ideas?",
            "Do you see yourself starting your own business someday?"
        ]
    },
    "Conventional": {
        "description": "You prefer organized, structured work with clear rules and procedures.",
        "sample_questions": [
            "Do you like organizing things and keeping them neat?",
            "Do you prefer following clear instructions over improvising?",
            "Are you good at detailed, careful work?"
        ]
    },
    
    # SKILL/DOMAIN TRAITS (6 types)
    "Technical": {
        "description": "You enjoy working with technology, computers, or machines.",
        "sample_questions": [
            "Do you enjoy learning new technologies?",
            "Are you comfortable troubleshooting tech problems?",
            "Do computers and gadgets fascinate you?"
        ]
    },
    "Scientific": {
        "description": "You like lab work, experiments, and the scientific method.",
        "sample_questions": [
            "Do you enjoy conducting experiments?",
            "Would you like working in a laboratory?",
            "Are you interested in how the natural world works?"
        ]
    },
    "Numbers": {
        "description": "You enjoy math, statistics, and working with numerical data.",
        "sample_questions": [
            "Do you enjoy working with numbers and data?",
            "Are you comfortable with math and calculations?",
            "Do you like finding patterns in data?"
        ]
    },
    "Words": {
        "description": "You enjoy reading, writing, and working with language.",
        "sample_questions": [
            "Do you enjoy reading and writing?",
            "Are you good at expressing ideas in words?",
            "Do you enjoy learning languages?"
        ]
    },
    "Visual": {
        "description": "You think in images and enjoy design and spatial thinking.",
        "sample_questions": [
            "Do you think in pictures more than words?",
            "Are you good at visualizing objects in 3D?",
            "Do you notice design and aesthetics in everyday things?"
        ]
    },
    "Physical": {
        "description": "You enjoy sports, movement, and being physically active.",
        "sample_questions": [
            "Do you enjoy sports and physical activities?",
            "Would you prefer a job that keeps you moving?",
            "Do you feel restless sitting still for long periods?"
        ]
    },
    
    # ENVIRONMENT TRAITS (3 types)
    "Outdoor": {
        "description": "You prefer working outside, in nature, or doing fieldwork.",
        "sample_questions": [
            "Do you prefer being outdoors over being inside?",
            "Would you enjoy a job in nature or the environment?",
            "Do you feel energized by being outside?"
        ]
    },
    "Healthcare": {
        "description": "You are interested in medical settings and patient care.",
        "sample_questions": [
            "Are you interested in medicine and healthcare?",
            "Would you feel comfortable working in a hospital?",
            "Do you want to help people with their health?"
        ]
    },
    "Business": {
        "description": "You are interested in commerce, trade, and corporate work.",
        "sample_questions": [
            "Are you interested in how businesses work?",
            "Would you enjoy working in a corporate environment?",
            "Do you follow business news and markets?"
        ]
    },
    
    # BONUS TRAITS (2 types)
    "Problem-solving": {
        "description": "You enjoy tackling challenges and finding solutions.",
        "sample_questions": [
            "Do you enjoy solving difficult problems?",
            "Do challenges motivate rather than frustrate you?",
            "Are you persistent when facing obstacles?"
        ]
    },
    "Creative": {
        "description": "You like generating original ideas and thinking outside the box.",
        "sample_questions": [
            "Do you often come up with unique ideas?",
            "Do you prefer innovative over traditional approaches?",
            "Do people describe you as creative?"
        ]
    },
}


# Export for backward compatibility
def get_all_traits():
    """Returns a flat list of all trait names"""
    return list(TRAIT_DEFINITIONS.keys())


def get_trait_questions(trait_name):
    """Returns sample questions for a specific trait"""
    if trait_name in TRAIT_DEFINITIONS:
        return TRAIT_DEFINITIONS[trait_name].get("sample_questions", [])
    return []
