# seed_data.py

COURSES_POOL = [
    # --- TECHNICAL & ANALYTICAL ---
    {"course_name": "BS Computer Science", "description": "Study of computation, complexity, and advanced software design.", "minimum_gwa": 88, "recommended_strand": "STEM", "trait_tag": ["Analytical", "Technical", "Logical", "Algorithm-focused", "Innovative"]},
    {"course_name": "BS Information Technology", "description": "Focuses on the practical application of computing technology to business processes.", "minimum_gwa": 85, "recommended_strand": "STEM / TVL", "trait_tag": ["Technical", "Practical", "Support-oriented", "Systematic", "Service"]},
    {"course_name": "BS Civil Engineering", "description": "Design and supervision of infrastructure projects like roads, bridges, and buildings.", "minimum_gwa": 90, "recommended_strand": "STEM", "trait_tag": ["Structural", "Methodical", "Technical", "Practical", "Leadership"]},
    {"course_name": "BS Computer Engineering", "description": "Combines electronics engineering and computer science to develop computer hardware and software systems.", "minimum_gwa": 88, "recommended_strand": "STEM", "trait_tag": ["Hardware-oriented", "Analytical", "Practical", "Logical", "Technical"]},
    {"course_name": "BS Electronics Engineering", "description": "Design and development of electronic circuits, communication systems, and automated devices.", "minimum_gwa": 88, "recommended_strand": "STEM", "trait_tag": ["Circuit-focused", "Methodical", "Precision-oriented", "Practical", "Technical"]},
    {"course_name": "BS Mechanical Engineering", "description": "Focuses on the design, analysis, and manufacturing of mechanical systems and machinery.", "minimum_gwa": 88, "recommended_strand": "STEM", "trait_tag": ["Structural", "Tangible", "Analytical", "Practical", "Technical"]},
    {"course_name": "BS Electrical Engineering", "description": "Study of electricity, electronics, and electromagnetism for power generation and distribution.", "minimum_gwa": 88, "recommended_strand": "STEM", "trait_tag": ["Systemic", "Complex", "Methodical", "Logical", "Technical"]},     
    {"course_name": "BS Data Science", "description": "Uses scientific methods, algorithms, and systems to extract knowledge and insights from structured and unstructured data.", "minimum_gwa": 89, "recommended_strand": "STEM", "trait_tag": ["Analytical", "Statistical", "Logical", "Insightful", "Technical"]},
    {"course_name": "BS Mathematics", "description": "Advanced study of mathematical structures, logic, and numerical analysis for various industries.", "minimum_gwa": 87, "recommended_strand": "STEM", "trait_tag": ["Abstract", "Logical", "Methodical", "Theoretical", "Analytical"]},
    {"course_name": "BS Statistics", "description": "Focuses on the collection, analysis, interpretation, and presentation of quantitative data.", "minimum_gwa": 86, "recommended_strand": "STEM", "trait_tag": ["Quantitative", "Logical", "Data-driven", "Technical", "Analytical"]},
    {"course_name": "BS Geodetic Engineering", "description": "Professional study of surveying, mapping, and global positioning systems (GPS).", "minimum_gwa": 86, "recommended_strand": "STEM", "trait_tag": ["Mapping-oriented", "Precision-oriented", "Outdoor-leaning", "Practical", "Technical"]},
    {"course_name": "BS Industrial Engineering", "description": "Focuses on optimizing complex processes, systems, and organizations to reduce waste.", "minimum_gwa": 86, "recommended_strand": "STEM", "trait_tag": ["Process-oriented", "Efficiency-driven", "Leadership", "Business-minded", "Analytical"]},
    {"course_name": "BS Cybersecurity", "description": "Specialized training in protecting networks, devices, and data from digital attacks.", "minimum_gwa": 87, "recommended_strand": "STEM / TVL", "trait_tag": ["Defensive", "Methodical", "Vigilant", "Logical", "Technical"]},

    # --- BUSINESS & LEADERSHIP ---
    {"course_name": "BS Accountancy", "description": "Detailed study of financial reporting, auditing, and taxation.", "minimum_gwa": 92, "recommended_strand": "ABM", "trait_tag": ["Detail-oriented", "Methodical", "Analytical", "Fiscal", "Business"]},
    {"course_name": "BS Business Administration major in Marketing Management", "description": "Focuses on market research, consumer behavior, and strategic brand positioning.", "minimum_gwa": 85, "recommended_strand": "ABM", "trait_tag": ["Persuasive", "Creative", "Social", "Strategic", "Business"]},
    {"course_name": "BS Business Administration major in Financial Management", "description": "Deals with investment decisions, capital markets, and corporate financial planning.", "minimum_gwa": 86, "recommended_strand": "ABM", "trait_tag": ["Investment-oriented", "Analytical", "Risk-evaluative", "Strategic", "Business"]},
    {"course_name": "BS Business Administration major in Human Resource Management", "description": "Studies organizational behavior, employee relations, and talent development.", "minimum_gwa": 84, "recommended_strand": "ABM", "trait_tag": ["People-oriented", "Social", "Empathetic", "Administrative", "Leadership"]},
    {"course_name": "BS Entrepreneurship", "description": "Develops skills in identifying business opportunities and managing new ventures.", "minimum_gwa": 83, "recommended_strand": "ABM", "trait_tag": ["Risk-taking", "Innovative", "Business-minded", "Practical", "Leadership"]},
    {"course_name": "BS Customs Administration", "description": "Focuses on tariff and customs laws, international trade, and logistics.", "minimum_gwa": 85, "recommended_strand": "ABM", "trait_tag": ["Regulatory", "Administrative", "Methodical", "Trade-oriented", "Business"]},
    {"course_name": "BS Real Estate Management", "description": "Deals with property appraisal, brokerage, and real estate development laws.", "minimum_gwa": 84, "recommended_strand": "ABM", "trait_tag": ["Negotiation-focused", "Social", "Interpersonal", "Sales-oriented", "Business"]},
    {"course_name": "BS Accounting Information Systems", "description": "Combines accounting principles with information technology to manage business financial data.", "minimum_gwa": 88, "recommended_strand": "ABM", "trait_tag": ["Hybrid-skilled", "Business", "Logical", "Software-heavy", "Technical"]},
    {"course_name": "BS Management Accounting", "description": "Focuses on providing internal financial information for business decision-making and strategic planning.", "minimum_gwa": 88, "recommended_strand": "ABM", "trait_tag": ["Decision-support", "Analytical", "Strategic", "Internal-audit", "Business"]},
    {"course_name": "BS Business Administration major in Operations Management", "description": "Focuses on the production and delivery of goods and services, logistics, and supply chain.", "minimum_gwa": 84, "recommended_strand": "ABM", "trait_tag": ["Logistics-oriented", "Methodical", "Supervisory", "Practical", "Business"]},
    {"course_name": "BS Business Economics", "description": "Study of economic theories and their practical application in business environments.", "minimum_gwa": 86, "recommended_strand": "ABM / STEM", "trait_tag": ["Theoretical", "Logical", "Market-analytical", "Strategic", "Business"]},
    {"course_name": "BS Agribusiness", "description": "Management and operations of agricultural businesses and the food supply chain.", "minimum_gwa": 83, "recommended_strand": "ABM / GAS", "trait_tag": ["Agricultural", "Practical", "Resource-management", "Nature-connected", "Business"]},
    {"course_name": "BS Legal Management", "description": "Study of business administration combined with essential legal principles and procedures.", "minimum_gwa": 87, "recommended_strand": "ABM / HUMSS", "trait_tag": ["Law-oriented", "Analytical", "Logical", "Compliance-focused", "Administrative"]},
    {"course_name": "Bachelor of Public Administration", "description": "Preparation for leadership roles in government, non-profits, and public service organizations.", "minimum_gwa": 85, "recommended_strand": "HUMSS / ABM", "trait_tag": ["Civic-minded", "Social", "Administrative", "Policy-oriented", "Leadership"]},

    # --- SCIENCE & HEALTHCARE ---
    {"course_name": "BS Medical Technology", "description": "Focuses on laboratory analysis of blood, tissues, and fluids for disease diagnosis.", "minimum_gwa": 90, "recommended_strand": "STEM", "trait_tag": ["Laboratory-oriented", "Methodical", "Technical", "Clinical", "Science"]},
    {"course_name": "BS Pharmacy", "description": "Study of drug preparation, therapeutic uses, and pharmaceutical chemistry.", "minimum_gwa": 88, "recommended_strand": "STEM", "trait_tag": ["Pharmacological", "Methodical", "Analytical", "Precision-oriented", "Science"]},
    {"course_name": "BS Physical Therapy", "description": "Rehabilitation science focusing on improving patient mobility and physical function.", "minimum_gwa": 89, "recommended_strand": "STEM", "trait_tag": ["Rehabilitative", "Social", "Patient-focused", "Practical", "Science"]},
    {"course_name": "BS Occupational Therapy", "description": "Helping patients develop skills for daily living and working through therapeutic activities.", "minimum_gwa": 88, "recommended_strand": "STEM", "trait_tag": ["Holistic", "Patient-focused", "Interpersonal", "Adaptive", "Science"]},
    {"course_name": "BS Biology", "description": "Scientific study of living organisms, from molecular levels to entire ecosystems.", "minimum_gwa": 86, "recommended_strand": "STEM", "trait_tag": ["Biological", "Analytical", "Nature-focused", "Theoretical", "Science"]},
    {"course_name": "BS Radiologic Technology", "description": "Operating medical imaging equipment like X-rays, CT scans, and MRI.", "minimum_gwa": 85, "recommended_strand": "STEM", "trait_tag": ["Imaging-focused", "Practical", "Safety-conscious", "Technical", "Clinical"]},
    {"course_name": "BS Nutrition and Dietetics", "description": "Study of food science and the role of nutrition in health and disease management.", "minimum_gwa": 85, "recommended_strand": "STEM", "trait_tag": ["Health-conscious", "Dietary-expert", "Service", "Methodical", "Science"]},
    {"course_name": "BS Midwifery", "description": "Primary healthcare for women during pregnancy, childbirth, and the postpartum period.", "minimum_gwa": 83, "recommended_strand": "STEM / GAS", "trait_tag": ["Maternal-care", "Social", "Empathetic", "Practical", "Medical"]},
    {"course_name": "BS Nursing", "description": "Professional training in patient care, health promotion, and community health nursing.", "minimum_gwa": 89, "recommended_strand": "STEM", "trait_tag": ["Care-oriented", "Resilient", "Interpersonal", "Practical", "Medical"]},
    {"course_name": "BS Speech-Language Pathology", "description": "Specialized study in treating communication and swallowing disorders in patients.", "minimum_gwa": 90, "recommended_strand": "STEM", "trait_tag": ["Communication-focused", "Diagnostic", "Interpersonal", "Clinical", "Social"]},
    {"course_name": "BS Respiratory Therapy", "description": "Focuses on the treatment and care of patients with cardiopulmonary and breathing disorders.", "minimum_gwa": 86, "recommended_strand": "STEM", "trait_tag": ["Pulmonary-focused", "Crisis-management", "Practical", "Technical", "Clinical"]},
    {"course_name": "BS Chemistry", "description": "The study of matter, its properties, and how it changes during chemical reactions.", "minimum_gwa": 87, "recommended_strand": "STEM", "trait_tag": ["Molecular-focused", "Analytical", "Methodical", "Logical", "Science"]},
    {"course_name": "BS Marine Biology", "description": "Study of marine organisms and their behaviors and interactions with the environment.", "minimum_gwa": 85, "recommended_strand": "STEM", "trait_tag": ["Aquatic-focused", "Analytical", "Exploratory", "Field-oriented", "Science"]},
    {"course_name": "BS Environmental Science", "description": "Interdisciplinary study of environmental problems and human impact on the ecosystem.", "minimum_gwa": 84, "recommended_strand": "STEM", "trait_tag": ["Ecological", "Analytical", "Conservation-minded", "Logical", "Science"]},
    {"course_name": "BS Optometry", "description": "Specialized healthcare profession involving examining the eyes for defects or abnormalities.", "minimum_gwa": 88, "recommended_strand": "STEM", "trait_tag": ["Vision-focused", "Clinical", "Methodical", "Practical", "Technical"]},
    {"course_name": "BS Health Information Management", "description": "Combines medical science and IT to manage patient data and healthcare records.", "minimum_gwa": 83, "recommended_strand": "STEM / TVL", "trait_tag": ["Data-focused", "Technical", "Organized", "Logical", "Administrative"]},
    {"course_name": "BS Biotechnology", "description": "Using biological systems or living organisms to develop or create different products.", "minimum_gwa": 88, "recommended_strand": "STEM", "trait_tag": ["Bio-innovative", "Research-oriented", "Analytical", "Technical", "Science"]},
    {"course_name": "BS Exercise and Sports Science", "description": "Scientific study of human movement and how the body responds to physical activity.", "minimum_gwa": 82, "recommended_strand": "STEM / Sports", "trait_tag": ["Athletic-minded", "Kinesiology-focused", "Active", "Interpersonal", "Science"]},
    {"course_name": "BS Psychology", "description": "Scientific study of human behavior and mental processes.", "minimum_gwa": 87, "recommended_strand": "STEM / HUMSS", "trait_tag": ["Behavioral-analytical", "Empathetic", "Observational", "Social", "Theoretical"]},
    
    # --- CREATIVE & DESIGN ---
    {"course_name": "BS Interior Design", "description": "Planning and design of interior spaces to improve function and aesthetic quality of life.", "minimum_gwa": 85, "recommended_strand": "STEM / HUMSS", "trait_tag": ["Spatial-creative", "Aesthetic", "Methodical", "Detail-oriented", "Practical"]},
    {"course_name": "Bachelor of Fine Arts", "description": "Advanced study in traditional arts like painting, sculpture, and visual theory.", "minimum_gwa": 80, "recommended_strand": "HUMSS / GAS", "trait_tag": ["Artistic", "Expressive", "Creative", "Visual-focused", "Theoretical"]},
    {"course_name": "BA in Communication", "description": "Study of media production, public relations, broadcasting, and digital journalism.", "minimum_gwa": 85, "recommended_strand": "HUMSS", "trait_tag": ["Media-literate", "Articulate", "Interpersonal", "Strategic", "Social"]},
    {"course_name": "BS Entertainment and Multimedia Computing", "description": "Specialized study in game development, digital animation, and interactive software.", "minimum_gwa": 86, "recommended_strand": "STEM / TVL", "trait_tag": ["Digital-creative", "Coding-heavy", "Innovative", "Logical", "Technical"]},
    {"course_name": "BA in Fashion Design and Merchandising", "description": "Study of apparel design, textile science, and the business of the fashion industry.", "minimum_gwa": 82, "recommended_strand": "HUMSS / ABM", "trait_tag": ["Style-conscious", "Textile-oriented", "Creative", "Innovative", "Business"]},
    {"course_name": "BS Industrial Design", "description": "Designing mass-produced products focusing on user experience, form, and industrial function.", "minimum_gwa": 85, "recommended_strand": "STEM", "trait_tag": ["Product-focused", "Technical-creative", "Ergonomic-minded", "Practical", "Innovative"]},
    {"course_name": "BA in Digital Filmmaking", "description": "Comprehensive training in cinematography, scriptwriting, and post-production editing.", "minimum_gwa": 84, "recommended_strand": "HUMSS / TVL", "trait_tag": ["Cinematic", "Storytelling", "Creative", "Technical", "Collaborative"]},
    {"course_name": "BS Clothing Technology", "description": "The technical side of garment production, quality control, and clothing manufacturing systems.", "minimum_gwa": 84, "recommended_strand": "STEM / TVL", "trait_tag": ["Manufacturing-oriented", "Methodical", "Technical", "Textile-expert", "Business"]},
    {"course_name": "BS Architecture", "description": "Integration of art and science in designing buildings and structures with focus on aesthetics and safety.", "minimum_gwa": 88, "recommended_strand": "STEM", "trait_tag": ["Design-heavy", "Analytical-creative", "Technical", "Architectural", "Structural"]},
    {"course_name": "BS Multimedia Arts", "description": "Multidisciplinary program combining graphic design, 2D/3D animation, and video production.", "minimum_gwa": 83, "recommended_strand": "HUMSS / TVL", "trait_tag": ["Versatile-creative", "Digital-artist", "Visual-communicator", "Practical", "Innovative"]},
    {"course_name": "BA in Advertising Arts", "description": "Focuses on visual communication, branding, and creative strategies for marketing campaigns.", "minimum_gwa": 84, "recommended_strand": "HUMSS / GAS", "trait_tag": ["Promotional", "Brand-strategic", "Creative", "Persuasive", "Visual-focused"]},
    {"course_name": "BA in Animation", "description": "Technical and artistic study of creating movement and storytelling through digital and traditional animation.", "minimum_gwa": 82, "recommended_strand": "TVL / HUMSS", "trait_tag": ["Illustration-focused", "Creative-technical", "Motion-oriented", "Patient", "Methodical"]},
    {"course_name": "BA in Game Art and Design", "description": "Focuses on the visual elements of games, including character design, environment art, and UI/UX.", "minimum_gwa": 84, "recommended_strand": "TVL / STEM", "trait_tag": ["Game-centric", "World-building", "Digital-artist", "Innovative", "Logical"]},
    {"course_name": "BA in Photography", "description": "Professional study of digital and analog photography, lighting, and visual composition.", "minimum_gwa": 80, "recommended_strand": "HUMSS / GAS", "trait_tag": ["Observational-creative", "Technical-camera", "Visual-composition", "Practical", "Social"]},
    {"course_name": "BA in Music Production", "description": "Study of sound design, music theory, and digital tools for audio recording and engineering.", "minimum_gwa": 82, "recommended_strand": "HUMSS / TVL", "trait_tag": ["Auditory-creative", "Acoustic-technical", "Melodic", "Software-proficient", "Methodical"]},
    {"course_name": "BA in Theater Arts", "description": "The art of performance, stage management, scriptwriting, and theatrical production.", "minimum_gwa": 80, "recommended_strand": "HUMSS", "trait_tag": ["Performative", "Expressive", "Interpersonal", "Creative", "Collaborative"]},
    {"course_name": "BS Landscape Architecture", "description": "Designing outdoor public areas, parks, and gardens to harmonize with the environment.", "minimum_gwa": 85, "recommended_strand": "STEM", "trait_tag": ["Environmental-design", "Botanical-minded", "Aesthetic", "Technical", "Structural"]},
    {"course_name": "BA in Journalism", "description": "Specialized training in news gathering, ethics, and writing for print, broadcast, and digital media.", "minimum_gwa": 85, "recommended_strand": "HUMSS", "trait_tag": ["Inquisitive", "Objective", "Ethical", "Writing-heavy", "Analytical"]},

    # --- SOCIAL, EDUCATION & SERVICE ---
    {"course_name": "BS Criminology", "description": "Study of crime prevention, law enforcement, and criminal justice.", "minimum_gwa": 83, "recommended_strand": "HUMSS", "trait_tag": ["Disciplined", "Enforcement-oriented", "Methodical", "Protective", "Law-focused"]},
    {"course_name": "BS Hospitality Management", "description": "Management of hotels, restaurants, and tourism-related businesses.", "minimum_gwa": 82, "recommended_strand": "ABM / TVL", "trait_tag": ["Hospitality-oriented", "Service-driven", "Interpersonal", "Organized", "Practical"]},
    {"course_name": "Bachelor of Secondary Education", "description": "Preparing teachers for high school levels with specialization in specific subject areas like Math, English, or Science.", "minimum_gwa": 85, "recommended_strand": "HUMSS", "trait_tag": ["Instructive", "Mentoring-focused", "Social", "Subject-expert", "Service"]},
    {"course_name": "BS Tourism Management", "description": "Focuses on travel industry operations, sustainable tourism, and heritage management.", "minimum_gwa": 82, "recommended_strand": "ABM / HUMSS", "trait_tag": ["Global-minded", "Cultural-sensitive", "Social", "Service-oriented", "Business"]},
    {"course_name": "BS Office Administration", "description": "Training in office management, secretarial duties, and corporate records handling.", "minimum_gwa": 80, "recommended_strand": "ABM / TVL", "trait_tag": ["Clerical-expert", "Organized", "Methodical", "Supportive", "Administrative"]},
    {"course_name": "Bachelor of Elementary Education", "description": "Training for teachers specializing in primary school education and child development.", "minimum_gwa": 85, "recommended_strand": "HUMSS", "trait_tag": ["Child-centric", "Patient", "Interpersonal", "Creative-educator", "Social"]},
    {"course_name": "BA in Political Science", "description": "Study of government systems, political activities, and political behavior.", "minimum_gwa": 86, "recommended_strand": "HUMSS", "trait_tag": ["Governance-focused", "Societal-analytical", "Theoretical", "Logical", "Leadership"]},
    {"course_name": "BS Social Work", "description": "Focuses on social welfare, community organizing, and helping marginalized individuals.", "minimum_gwa": 84, "recommended_strand": "HUMSS", "trait_tag": ["Advocacy-driven", "Community-focused", "Empathetic", "Resilient", "Social"]},
    {"course_name": "BS Development Communication", "description": "Using communication to promote social change and community development.", "minimum_gwa": 85, "recommended_strand": "HUMSS / STEM", "trait_tag": ["Change-agent", "Media-literate", "Community-focused", "Social", "Interpersonal"]},
    {"course_name": "Bachelor of Library and Information Science", "description": "Management of information resources in libraries, archives, and digital databases.", "minimum_gwa": 82, "recommended_strand": "HUMSS / ABM", "trait_tag": ["Archival-focused", "Informational-logical", "Organized", "Service-oriented", "Technical"]},
    {"course_name": "BS Community Development", "description": "Planning and implementing programs for community empowerment and poverty alleviation.", "minimum_gwa": 84, "recommended_strand": "HUMSS", "trait_tag": ["Grassroots-oriented", "Altruistic", "Leadership", "Practical", "Social"]},
    {"course_name": "BS Forensic Science", "description": "Application of scientific principles to criminal investigation and legal evidence.", "minimum_gwa": 87, "recommended_strand": "STEM", "trait_tag": ["Investigative", "Clinical-analytical", "Methodical", "Scientific-logical", "Technical"]},
    {"course_name": "Bachelor of Special Needs Education", "description": "Specialized training for teaching students with diverse learning needs and disabilities.", "minimum_gwa": 86, "recommended_strand": "HUMSS", "trait_tag": ["Adaptive-educator", "Patient", "Compassionate", "Creative", "Social"]},
    {"course_name": "BA in International Studies", "description": "Study of global issues, diplomacy, foreign languages, and international relations.", "minimum_gwa": 87, "recommended_strand": "HUMSS", "trait_tag": ["Diplomatic", "Global-analytical", "Linguistic-interested", "Strategic", "Theoretical"]},
    {"course_name": "BA in Sociology", "description": "Systematic study of social institutions, collective behavior, and social development.", "minimum_gwa": 84, "recommended_strand": "HUMSS", "trait_tag": ["Societal-analytical", "Cultural-focused", "Theoretical", "Logical", "Observational"]},
    {"course_name": "BA in Philosophy", "description": "Critical study of fundamental questions regarding existence, knowledge, values, and reason.", "minimum_gwa": 85, "recommended_strand": "HUMSS", "trait_tag": ["Contemplative", "Argumentative-logical", "Theoretical", "Critical-thinking", "Existential"]},
    {"course_name": "Bachelor of Early Childhood Education", "description": "Focuses on the holistic development and education of children from birth to age eight.", "minimum_gwa": 84, "recommended_strand": "HUMSS", "trait_tag": ["Nurturing", "Playful-creative", "Patient", "Interpersonal", "Social"]},
    {"course_name": "Bachelor of Physical Education", "description": "Training for educators in sports, fitness, and health-related school programs.", "minimum_gwa": 82, "recommended_strand": "HUMSS / Sports", "trait_tag": ["Kinetically-skilled", "Coach-minded", "Active", "Motivational", "Social"]},
    {"course_name": "BA in Linguistics", "description": "Scientific study of language structure, evolution, and its role in human communication.", "minimum_gwa": 85, "recommended_strand": "HUMSS", "trait_tag": ["Linguistic-analytical", "Structural-logic", "Theoretical", "Methodical", "Communication-focused"]},
    {"course_name": "BS Environmental Planning", "description": "Interdisciplinary study of urban development, resource management, and sustainable land use.", "minimum_gwa": 86, "recommended_strand": "STEM / HUMSS", "trait_tag": ["Urban-analytical", "Strategic-spatial", "Sustainability-minded", "Logical", "Structural"]},

    # --- MARITIME, AVIATION & AGRICULTURE ---
    {"course_name": "BS Marine Transportation", "description": "Professional training for deck officers, focusing on navigation and ship management.", "minimum_gwa": 85, "recommended_strand": "STEM / TVL", "trait_tag": ["Nautical-focused", "Navigational", "Disciplined", "Leadership", "Practical"]},
    {"course_name": "BS Marine Engineering", "description": "Technical study of marine propulsion, power plants, and ship machinery maintenance.", "minimum_gwa": 85, "recommended_strand": "STEM / TVL", "trait_tag": ["Maritime-technical", "Engine-oriented", "Mechanical-practical", "Analytical", "Methodical"]},
    {"course_name": "BS Agriculture", "description": "Scientific study of crop production, livestock raising, and soil management.", "minimum_gwa": 82, "recommended_strand": "STEM / GAS", "trait_tag": ["Agronomical", "Practical", "Nature-connected", "Resourceful", "Scientific"]},
    {"course_name": "BS Forestry", "description": "Management and protection of forest resources, ecosystems, and wildlife conservation.", "minimum_gwa": 82, "recommended_strand": "STEM", "trait_tag": ["Silvicultural", "Outdoor-focused", "Conservationist", "Analytical", "Practical"]},
    {"course_name": "BS Fisheries", "description": "Study of aquaculture, fish processing, and sustainable aquatic resource management.", "minimum_gwa": 82, "recommended_strand": "STEM", "trait_tag": ["Aquacultural", "Practical", "Technical-water", "Science", "Resourceful"]},
    {"course_name": "Doctor of Veterinary Medicine", "description": "Six-year program focused on the prevention, diagnosis, and treatment of animal diseases.", "minimum_gwa": 88, "recommended_strand": "STEM", "trait_tag": ["Animal-care", "Clinical-precision", "Methodical", "Scientific", "Medical"]},
    {"course_name": "BS Aeronautical Engineering", "description": "Design, construction, and maintenance of aircraft and spacecraft structures.", "minimum_gwa": 88, "recommended_strand": "STEM", "trait_tag": ["Aerodynamic-focused", "Precision-technical", "Analytical", "Methodical", "Structural"]},
    {"course_name": "BS Aircraft Maintenance Technology", "description": "Specialized training in the inspection, repair, and overhaul of aircraft engines and systems.", "minimum_gwa": 85, "recommended_strand": "STEM / TVL", "trait_tag": ["Avionics-practical", "Safety-driven", "Methodical", "Technical", "Manual-precision"]},
    {"course_name": "BS Aviation Electronics Technology", "description": "Focuses on the electronic systems (avionics) used on aircraft and satellites.", "minimum_gwa": 85, "recommended_strand": "STEM / TVL", "trait_tag": ["Circuit-focused", "Aviation-technical", "Analytical", "Precise", "Practical"]},
    {"course_name": "BS Geology", "description": "Study of the solid Earth, its rocks, and the processes by which they change.", "minimum_gwa": 85, "recommended_strand": "STEM", "trait_tag": ["Earth-science", "Field-analytical", "Observational", "Theoretical", "Methodical"]},
    {"course_name": "BS Physics", "description": "Fundamental study of matter, energy, and the laws of the universe.", "minimum_gwa": 87, "recommended_strand": "STEM", "trait_tag": ["Mathematical-logic", "Theoretical-abstract", "Fundamental-science", "Logical", "Analytical"]},
    {"course_name": "BS Meteorology", "description": "Scientific study of the atmosphere and weather patterns for forecasting.", "minimum_gwa": 85, "recommended_strand": "STEM", "trait_tag": ["Atmospheric-science", "Predictive-analytical", "Data-centric", "Logical", "Technical"]},
    {"course_name": "BS Food Technology", "description": "The application of food science to the selection, preservation, and packaging of food.", "minimum_gwa": 84, "recommended_strand": "STEM / TVL", "trait_tag": ["Food-chemistry", "Quality-control", "Methodical", "Practical", "Science"]},
    {"course_name": "BS Culinary Management", "description": "Combines culinary arts with business management for professional kitchen operations.", "minimum_gwa": 82, "recommended_strand": "TVL / ABM", "trait_tag": ["Gastronomic-creative", "Gastronomic-service", "Practical-skill", "Business-minded", "Leadership"]},
    {"course_name": "Bachelor of Technical-Vocational Teacher Education", "description": "Training for teachers in technical and vocational fields like welding, automotive, and electronics.", "minimum_gwa": 83, "recommended_strand": "TVL", "trait_tag": ["Vocational-skilled", "Mentoring-focused", "Practical-expert", "Social", "Service"]},
]

# seed_data.py (Continued)

QUESTIONS_POOL = [
    {
        "text": "When working on a group project, which task do you naturally gravitate toward?",
        "category": "Situational",
        "options": [
            {"text": "Organizing the timeline and leading the meetings.", "tag": "Leadership"},
            {"text": "Diving into the data and researching the facts.", "tag": "Analytical"},
            {"text": "Designing the layout, visuals, or the final presentation.", "tag": "Design-heavy"},
            {"text": "Writing the report and explaining it to the class.", "tag": "Communication-focused"}
        ]
    },
    {
        "text": "Your community is facing a serious problem with plastic waste. How do you decide to help?",
        "category": "Situational",
        "options": [
            {"text": "Create a viral video or social media campaign to raise awareness.", "tag": "Media-literate"},
            {"text": "Research local laws and present a new policy to the Barangay captain.", "tag": "Governance-focused"},
            {"text": "Start a non-profit group to help those most affected by the pollution.", "tag": "Advocacy-driven"},
            {"text": "Study how the language and signs used in the area affect people's habits.", "tag": "Linguistic-analytical"}
        ]
    },
    {
        "text": "You are given a piece of empty land in a beautiful location. What is the first thing you want to do with it?",
        "category": "Situational",
        "options": [
            {"text": "Design a strong, safe building that fits the landscape.", "tag": "Structural"},
            {"text": "Measure the land accurately and create a detailed map of its borders.", "tag": "Mapping-oriented"},
            {"text": "Focus on the interior look, colors, and how the rooms feel inside.", "tag": "Aesthetic"},
            {"text": "Study the local plants and animals to ensure they are protected.", "tag": "Ecological"}
        ]
    },
    {
        "text": "You are in a high-tech laboratory and discovered an unknown substance. What is your first approach to studying it?",
        "category": "Situational",
        "options": [
            {"text": "Try to modify its genetic structure to see if it can benefit humans.", "tag": "Bio-innovative"},
            {"text": "Break it down into its smallest molecules to understand its chemical makeup.", "tag": "Molecular-focused"},
            {"text": "Investigate its origin like a detective using forensic tools.", "tag": "Investigative"},
            {"text": "Test its reaction to electrical currents and circuits.", "tag": "Circuit-focused"}
        ]
    },
    {
        "text": "A ship is navigating through a difficult storm. What is your priority?",
        "category": "Situational",
        "options": [
            {"text": "Using nautical instruments to plot the safest path.", "tag": "Nautical-focused"},
            {"text": "Maintaining the engine and mechanical systems.", "tag": "Maritime-technical"},
            {"text": "Organizing the crew to ensure passenger safety.", "tag": "Leadership"},
            {"text": "Calculating the fuel efficiency and resources left.", "tag": "Resourceful"}
        ]
    },
    {
        "text": "An aircraft engine shows an unusual vibration before takeoff. What do you do?",
        "category": "Situational",
        "options": [
            {"text": "Study the aerodynamic forces acting on the wing.", "tag": "Aerodynamic-focused"},
            {"text": "Perform a manual inspection of the engine's hardware.", "tag": "Avionics-practical"},
            {"text": "Analyze the electronic sensors in the cockpit.", "tag": "Aviation-technical"},
            {"text": "Re-check the structural integrity of the fuselage.", "tag": "Structural"}
        ]
    },
    {
        "text": "You see a patient struggling with a physical injury. What is your first instinct?",
        "category": "Situational",
        "options": [
            {"text": "Design a long-term exercise plan for their recovery.", "tag": "Rehabilitative"},
            {"text": "Check their vital signs and provide immediate medical care.", "tag": "Medical"},
            {"text": "Listen to their concerns and offer emotional support.", "tag": "Empathetic"},
            {"text": "Analyze the chemistry of the medicine they need.", "tag": "Pharmacological"}
        ]
    },
    {
        "text": "A local business is losing money and needs a new plan. How do you help?",
        "category": "Situational",
        "options": [
            {"text": "Analyze their financial statements for errors.", "tag": "Fiscal"},
            {"text": "Create a new brand identity and marketing strategy.", "tag": "Strategic"},
            {"text": "Improve the way employees work together.", "tag": "People-oriented"},
            {"text": "Find ways to make their production more efficient.", "tag": "Efficiency-driven"}
        ]
    },
    {
        "text": "You are asked to teach a group of children a new skill. How do you approach it?",
        "category": "Situational",
        "options": [
            {"text": "Prepare a structured lesson plan with clear goals.", "tag": "Instructive"},
            {"text": "Use games and creative activities to make it fun.", "tag": "Creative-educator"},
            {"text": "Focus on the children who are struggling the most.", "tag": "Patient"},
            {"text": "Observe how they interact to understand their behavior.", "tag": "Behavioral-analytical"}
        ]
    }
]