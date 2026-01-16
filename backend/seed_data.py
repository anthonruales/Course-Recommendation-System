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

SITUATIONAL_QUESTIONS_POOL = [
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
    },
    {
        "text": "You have an opportunity to start your own business. What aspect excites you most?",
        "category": "Situational",
        "options": [
            {"text": "Creating a unique product or service idea.", "tag": "Innovative"},
            {"text": "Building and managing a strong team.", "tag": "Leadership"},
            {"text": "Understanding the market and customer needs.", "tag": "Strategic"},
            {"text": "Managing finances and tracking profitability.", "tag": "Fiscal"}
        ]
    },
    {
        "text": "A creative project needs visual representation. What is your contribution?",
        "category": "Situational",
        "options": [
            {"text": "Create eye-catching graphics or illustrations.", "tag": "Visual-focused"},
            {"text": "Design the overall layout and user interface.", "tag": "Design-heavy"},
            {"text": "Develop an animated or interactive presentation.", "tag": "Digital-creative"},
            {"text": "Choose colors, fonts, and aesthetic elements.", "tag": "Aesthetic"}
        ]
    },
    {
        "text": "You are part of a team addressing climate change. What role appeals to you?",
        "category": "Situational",
        "options": [
            {"text": "Research environmental data and solutions.", "tag": "Conservation-minded"},
            {"text": "Advocate for policy changes with government officials.", "tag": "Governance-focused"},
            {"text": "Educate the public through media campaigns.", "tag": "Media-literate"},
            {"text": "Develop eco-friendly technology or products.", "tag": "Innovative"}
        ]
    },
    {
        "text": "Your company needs to improve its software system. What is your approach?",
        "category": "Situational",
        "options": [
            {"text": "Write efficient code and improve system architecture.", "tag": "Technical"},
            {"text": "Ensure the system is secure and protects data.", "tag": "Defensive"},
            {"text": "Make the interface user-friendly and intuitive.", "tag": "Design-heavy"},
            {"text": "Test extensively to find and fix bugs.", "tag": "Methodical"}
        ]
    },
    {
        "text": "You are designing a new public park for your community. What is your main focus?",
        "category": "Situational",
        "options": [
            {"text": "Create sustainable green spaces and protect ecosystems.", "tag": "Ecological"},
            {"text": "Design aesthetically beautiful walking trails and features.", "tag": "Aesthetic"},
            {"text": "Plan facilities that serve the elderly and disabled.", "tag": "Inclusive"},
            {"text": "Calculate budget and manage construction logistics.", "tag": "Methodical"}
        ]
    },
    {
        "text": "A medical emergency occurs in your workplace. What do you do first?",
        "category": "Situational",
        "options": [
            {"text": "Assess the situation and call emergency services immediately.", "tag": "Medical"},
            {"text": "Comfort the affected person and offer emotional support.", "tag": "Empathetic"},
            {"text": "Document details for the medical report.", "tag": "Detail-oriented"},
            {"text": "Organize coworkers to help and manage the situation.", "tag": "Leadership"}
        ]
    },
    {
    "text": "You are tasked to organize a fundraising event. What is your first step?",
    "category": "Situational",
    "options": [
        {"text": "Plan the event logistics and schedule.", "tag": "Methodical"},
        {"text": "Design creative promotional materials.", "tag": "Creative"},
        {"text": "Reach out to potential sponsors and donors.", "tag": "Interpersonal"},
        {"text": "Manage the event budget and finances.", "tag": "Fiscal"}
    ]
},
{
    "text": "A friend is struggling with a difficult subject. How do you help?",
    "category": "Situational",
    "options": [
        {"text": "Break down the topic into simple steps.", "tag": "Analytical"},
        {"text": "Encourage and motivate them.", "tag": "Empathetic"},
        {"text": "Find online resources or tutorials.", "tag": "Resourceful"},
        {"text": "Organize a group study session.", "tag": "Collaborative"}
    ]
},
{
    "text": "You are leading a team with conflicting ideas. What do you do?",
    "category": "Situational",
    "options": [
        {"text": "Facilitate a discussion to reach consensus.", "tag": "Leadership"},
        {"text": "Analyze each idea for pros and cons.", "tag": "Analytical"},
        {"text": "Encourage creative brainstorming.", "tag": "Creative"},
        {"text": "Assign roles based on strengths.", "tag": "Organized"}
    ]
},
{
    "text": "You are given a tight deadline for a project. How do you proceed?",
    "category": "Situational",
    "options": [
        {"text": "Prioritize tasks and create a timeline.", "tag": "Methodical"},
        {"text": "Work extra hours to finish on time.", "tag": "Resilient"},
        {"text": "Delegate tasks to team members.", "tag": "Leadership"},
        {"text": "Find shortcuts to speed up the process.", "tag": "Practical"}
    ]
},
{
    "text": "A new technology is introduced at work. What is your reaction?",
    "category": "Situational",
    "options": [
        {"text": "Learn how it works and teach others.", "tag": "Technical"},
        {"text": "Find ways to integrate it into current processes.", "tag": "Innovative"},
        {"text": "Ask questions to understand its benefits.", "tag": "Analytical"},
        {"text": "Wait for others to try it first.", "tag": "Cautious"}
    ]
},
{
    "text": "You are asked to mediate a conflict between two colleagues.",
    "category": "Situational",
    "options": [
        {"text": "Listen to both sides and find common ground.", "tag": "Empathetic"},
        {"text": "Suggest a compromise solution.", "tag": "Practical"},
        {"text": "Refer the issue to a supervisor.", "tag": "Administrative"},
        {"text": "Encourage open communication.", "tag": "Interpersonal"}
    ]
},
{
    "text": "You are responsible for a group presentation. What is your focus?",
    "category": "Situational",
    "options": [
        {"text": "Ensure the content is accurate and well-researched.", "tag": "Analytical"},
        {"text": "Make the slides visually appealing.", "tag": "Aesthetic"},
        {"text": "Practice public speaking for a confident delivery.", "tag": "Articulate"},
        {"text": "Coordinate team members' contributions.", "tag": "Organized"}
    ]
},
{
    "text": "You are asked to design a new product. What is your approach?",
    "category": "Situational",
    "options": [
        {"text": "Research market needs and trends.", "tag": "Strategic"},
        {"text": "Sketch creative design concepts.", "tag": "Creative"},
        {"text": "Test prototypes for functionality.", "tag": "Technical"},
        {"text": "Gather feedback from potential users.", "tag": "Interpersonal"}
    ]
},
{
    "text": "You are assigned to write a report on a complex issue.",
    "category": "Situational",
    "options": [
        {"text": "Gather and analyze all relevant data.", "tag": "Analytical"},
        {"text": "Summarize findings in a clear, concise way.", "tag": "Communication-focused"},
        {"text": "Use visuals to support your points.", "tag": "Visual-focused"},
        {"text": "Organize the report into logical sections.", "tag": "Methodical"}
    ]
},
{
    "text": "You are asked to help with a community outreach program.",
    "category": "Situational",
    "options": [
        {"text": "Plan activities that engage participants.", "tag": "Creative"},
        {"text": "Promote the event on social media.", "tag": "Media-literate"},
        {"text": "Coordinate volunteers and resources.", "tag": "Organized"},
        {"text": "Evaluate the program's impact.", "tag": "Analytical"}
    ]
},
{
    "text": "You are given a leadership role in a volunteer project.",
    "category": "Situational",
    "options": [
        {"text": "Motivate and inspire your team.", "tag": "Leadership"},
        {"text": "Set clear goals and expectations.", "tag": "Methodical"},
        {"text": "Solve problems as they arise.", "tag": "Practical"},
        {"text": "Celebrate team achievements.", "tag": "Empathetic"}
    ]
},
{
    "text": "You are asked to create a budget for a school event.",
    "category": "Situational",
    "options": [
        {"text": "List all possible expenses and income.", "tag": "Detail-oriented"},
        {"text": "Negotiate discounts with suppliers.", "tag": "Negotiation-focused"},
        {"text": "Allocate funds based on priorities.", "tag": "Strategic"},
        {"text": "Track spending to stay within budget.", "tag": "Methodical"}
    ]
},
{
    "text": "You are part of a team developing a new app.",
    "category": "Situational",
    "options": [
        {"text": "Write and test the code.", "tag": "Technical"},
        {"text": "Design the user interface.", "tag": "Aesthetic"},
        {"text": "Conduct user testing and gather feedback.", "tag": "Interpersonal"},
        {"text": "Market the app to potential users.", "tag": "Media-literate"}
    ]
},
{
    "text": "You are asked to solve a sudden technical problem.",
    "category": "Situational",
    "options": [
        {"text": "Diagnose the issue step by step.", "tag": "Analytical"},
        {"text": "Consult documentation or experts.", "tag": "Resourceful"},
        {"text": "Try creative solutions to fix it.", "tag": "Innovative"},
        {"text": "Document the solution for future reference.", "tag": "Methodical"}
    ]
},
]

ASSESSMENT_QUESTIONS_POOL = [
    {
        "text": "What type of work environment brings out your best performance?",
        "category": "Assessment",
        "options": [
            {"text": "Independent workspace where I can focus deeply.", "tag": "Analytical"},
            {"text": "Collaborative team environment with constant interaction.", "tag": "Social"},
            {"text": "Flexible environment where I can work creatively.", "tag": "Creative"},
            {"text": "Structured environment with clear rules and procedures.", "tag": "Methodical"}
        ]
    },
    {
        "text": "How do you typically respond to challenges or obstacles?",
        "category": "Assessment",
        "options": [
            {"text": "Analyze the problem logically to find solutions.", "tag": "Logical"},
            {"text": "Think outside the box and try unconventional approaches.", "tag": "Innovative"},
            {"text": "Ask others for input and collaborate on solutions.", "tag": "Interpersonal"},
            {"text": "Persist and work methodically until resolved.", "tag": "Resilient"}
        ]
    },
    {
        "text": "Which activity energizes you the most?",
        "category": "Assessment",
        "options": [
            {"text": "Learning new technical skills or technologies.", "tag": "Technical"},
            {"text": "Helping others achieve their goals.", "tag": "Service"},
            {"text": "Creating something visible and tangible.", "tag": "Practical"},
            {"text": "Exploring abstract concepts and theories.", "tag": "Theoretical"}
        ]
    },
    {
        "text": "How do you prefer to learn new information?",
        "category": "Assessment",
        "options": [
            {"text": "Through hands-on practice and experimentation.", "tag": "Practical"},
            {"text": "By reading and studying theory-based materials.", "tag": "Theoretical"},
            {"text": "By listening to explanations and discussions.", "tag": "Communication-focused"},
            {"text": "By visual diagrams, charts, and demonstrations.", "tag": "Visual-focused"}
        ]
    },
    {
        "text": "What motivates you most in your career?",
        "category": "Assessment",
        "options": [
            {"text": "Making a positive impact on society.", "tag": "Altruistic"},
            {"text": "Achieving recognition and professional success.", "tag": "Leadership"},
            {"text": "Solving complex problems and puzzles.", "tag": "Logical"},
            {"text": "Creating beautiful or meaningful work.", "tag": "Creative"}
        ]
    },
    {
        "text": "How do you prefer to spend your free time?",
        "category": "Assessment",
        "options": [
            {"text": "Reading books or exploring online resources.", "tag": "Theoretical"},
            {"text": "Engaging in sports or outdoor activities.", "tag": "Active"},
            {"text": "Creating art, music, or other creative projects.", "tag": "Creative"},
            {"text": "Spending time with friends and family.", "tag": "Social"}
        ]
    },
    {
        "text": "When facing a difficult decision, what do you rely on?",
        "category": "Assessment",
        "options": [
            {"text": "Data and logical analysis.", "tag": "Logical"},
            {"text": "My intuition and gut feeling.", "tag": "Intuitive"},
            {"text": "Advice from trusted people.", "tag": "Interpersonal"},
            {"text": "Past experience and patterns.", "tag": "Analytical"}
        ]
    },
    {
        "text": "How important is financial security to you?",
        "category": "Assessment",
        "options": [
            {"text": "Very important - I prioritize stable income.", "tag": "Practical"},
            {"text": "Important but not my only concern.", "tag": "Balanced"},
            {"text": "Less important than doing work I love.", "tag": "Passionate"},
            {"text": "I pursue wealth and entrepreneurial success.", "tag": "Ambitious"}
        ]
    },
    {
        "text": "Do you prefer working independently or in teams?",
        "category": "Assessment",
        "options": [
            {"text": "Strongly prefer working alone.", "tag": "Analytical"},
            {"text": "Prefer working independently with occasional collaboration.", "tag": "Self-reliant"},
            {"text": "Enjoy balanced mix of both.", "tag": "Flexible"},
            {"text": "Strongly prefer team-based work.", "tag": "Social"}
        ]
    },
    {
        "text": "How do you handle criticism or negative feedback?",
        "category": "Assessment",
        "options": [
            {"text": "I see it as valuable input for improvement.", "tag": "Resilient"},
            {"text": "I need time to process it before responding.", "tag": "Reflective"},
            {"text": "I get defensive and feel hurt.", "tag": "Sensitive"},
            {"text": "I analyze it objectively and extract useful points.", "tag": "Logical"}
        ]
    },
    {
        "text": "What kind of people do you work best with?",
        "category": "Assessment",
        "options": [
            {"text": "Detail-oriented and organized people.", "tag": "Methodical"},
            {"text": "Creative and innovative thinkers.", "tag": "Creative"},
            {"text": "Compassionate and empathetic individuals.", "tag": "Empathetic"},
            {"text": "Ambitious and driven professionals.", "tag": "Leadership"}
        ]
    },
    {
        "text": "How comfortable are you with taking risks?",
        "category": "Assessment",
        "options": [
            {"text": "I prefer to play it safe and minimize risk.", "tag": "Cautious"},
            {"text": "I take calculated risks when warranted.", "tag": "Balanced"},
            {"text": "I enjoy risk-taking and new ventures.", "tag": "Innovative"},
            {"text": "I actively seek high-risk, high-reward situations.", "tag": "Ambitious"}
        ]
    },
    {
        "text": "What role do ethics and values play in your decisions?",
        "category": "Assessment",
        "options": [
            {"text": "They are my primary guide in all decisions.", "tag": "Ethical"},
            {"text": "They are important but balanced with practicality.", "tag": "Principled"},
            {"text": "They matter but financial concerns come first.", "tag": "Practical"},
            {"text": "I follow rules and regulations strictly.", "tag": "Methodical"}
        ]
    },
    {
        "text": "How do you define success?",
        "category": "Assessment",
        "options": [
            {"text": "Making a positive difference in the world.", "tag": "Altruistic"},
            {"text": "Achieving high income and status.", "tag": "Ambitious"},
            {"text": "Having work-life balance and personal fulfillment.", "tag": "Balanced"},
            {"text": "Mastering my craft and continuous improvement.", "tag": "Perfectionist"}
        ]
    },
    {
        "text": "What aspect of work frustrates you most?",
        "category": "Assessment",
        "options": [
            {"text": "Lack of clarity or poorly defined goals.", "tag": "Analytical"},
            {"text": "Repetitive or routine tasks.", "tag": "Creative"},
            {"text": "Interpersonal conflicts or difficult people.", "tag": "Empathetic"},
            {"text": "Inefficiency or disorganization.", "tag": "Methodical"}
        ]
    },
    {
        "text": "How important is recognition and appreciation to you?",
        "category": "Assessment",
        "options": [
            {"text": "Very important - I need constant validation.", "tag": "Ambitious"},
            {"text": "Important but not essential.", "tag": "Balanced"},
            {"text": "Not very important - I work for intrinsic reasons.", "tag": "Principled"},
            {"text": "I appreciate it but don't seek it.", "tag": "Humble"}
        ]
    },
    {
        "text": "How do you approach learning new skills?",
        "category": "Assessment",
        "options": [
            {"text": "I prefer formal education and structured courses.", "tag": "Theoretical"},
            {"text": "I learn best by doing and making mistakes.", "tag": "Practical"},
            {"text": "I prefer to teach myself at my own pace.", "tag": "Self-reliant"},
            {"text": "I learn by observing and copying others.", "tag": "Observational"}
        ]
    },
    {
        "text": "What inspires you to pursue a career?",
        "category": "Assessment",
        "options": [
            {"text": "Passion for the subject matter.", "tag": "Passionate"},
            {"text": "Potential for helping others.", "tag": "Altruistic"},
            {"text": "Financial rewards and stability.", "tag": "Practical"},
            {"text": "Personal growth and development.", "tag": "Ambitious"}
        ]
    },
    {
        "text": "How do you manage stress and pressure?",
        "category": "Assessment",
        "options": [
            {"text": "I stay calm and break problems into smaller tasks.", "tag": "Methodical"},
            {"text": "I talk it through with others for support.", "tag": "Social"},
            {"text": "I take breaks and do activities I enjoy.", "tag": "Balanced"},
            {"text": "I channel it into productive work.", "tag": "Resilient"}
        ]
    },
    {
        "text": "How do you view authority and rules?",
        "category": "Assessment",
        "options": [
            {"text": "I respect them and follow them carefully.", "tag": "Methodical"},
            {"text": "I follow them but question if they make sense.", "tag": "Analytical"},
            {"text": "I see them as guidelines, not restrictions.", "tag": "Innovative"},
            {"text": "I challenge them when I disagree.", "tag": "Independent"}
        ]
    },
    {
        "text": "What kind of projects excite you most?",
        "category": "Assessment",
        "options": [
            {"text": "Projects with clear, measurable outcomes.", "tag": "Analytical"},
            {"text": "Projects that involve creating something new.", "tag": "Creative"},
            {"text": "Projects that help people or communities.", "tag": "Altruistic"},
            {"text": "Projects that push my technical skills.", "tag": "Technical"}
        ]
    },
    {
        "text": "How do you prefer to communicate?",
        "category": "Assessment",
        "options": [
            {"text": "Face-to-face conversations.", "tag": "Social"},
            {"text": "Written communication for clarity.", "tag": "Detail-oriented"},
            {"text": "Visual presentations and demonstrations.", "tag": "Visual-focused"},
            {"text": "Data and reports.", "tag": "Analytical"}
        ]
    },
    {
        "text": "What level of competition do you enjoy?",
        "category": "Assessment",
        "options": [
            {"text": "I thrive on competition and winning.", "tag": "Ambitious"},
            {"text": "Moderate competition motivates me.", "tag": "Balanced"},
            {"text": "I prefer collaboration over competition.", "tag": "Social"},
            {"text": "Competition stresses me out.", "tag": "Sensitive"}
        ]
    },
    {
    "text": "How do you handle multitasking?",
    "category": "Assessment",
    "options": [
        {"text": "I prefer focusing on one task at a time.", "tag": "Methodical"},
        {"text": "I can juggle multiple tasks easily.", "tag": "Flexible"},
        {"text": "I prioritize tasks by urgency.", "tag": "Organized"},
        {"text": "I delegate when possible.", "tag": "Leadership"}
    ]
},
{
    "text": "What motivates you to keep learning?",
    "category": "Assessment",
    "options": [
        {"text": "Curiosity about new things.", "tag": "Passionate"},
        {"text": "Desire for career advancement.", "tag": "Ambitious"},
        {"text": "Need to solve real-world problems.", "tag": "Practical"},
        {"text": "Enjoyment of academic challenges.", "tag": "Theoretical"}
    ]
},
{
    "text": "How do you approach teamwork?",
    "category": "Assessment",
    "options": [
        {"text": "I take the lead and organize.", "tag": "Leadership"},
        {"text": "I support others and fill gaps.", "tag": "Supportive"},
        {"text": "I contribute ideas and solutions.", "tag": "Creative"},
        {"text": "I prefer to work independently.", "tag": "Self-reliant"}
    ]
},
{
    "text": "How do you respond to failure?",
    "category": "Assessment",
    "options": [
        {"text": "I analyze what went wrong and try again.", "tag": "Resilient"},
        {"text": "I seek feedback to improve.", "tag": "Growth-oriented"},
        {"text": "I move on to new challenges.", "tag": "Flexible"},
        {"text": "I feel discouraged but recover quickly.", "tag": "Sensitive"}
    ]
},
{
    "text": "What is your preferred way to celebrate success?",
    "category": "Assessment",
    "options": [
        {"text": "Share achievements with others.", "tag": "Social"},
        {"text": "Reflect privately on accomplishments.", "tag": "Introspective"},
        {"text": "Set new goals right away.", "tag": "Ambitious"},
        {"text": "Reward myself with a treat.", "tag": "Practical"}
    ]
},
]

ACADEMIC_QUESTIONS_POOL = [
    {
        "text": "Which subject has always come naturally to you in school?",
        "category": "Academic",
        "options": [
            {"text": "Mathematics and quantitative subjects.", "tag": "Logical"},
            {"text": "Science and laboratory work.", "tag": "Scientific"},
            {"text": "Languages and literature.", "tag": "Communication-focused"},
            {"text": "Arts and creative subjects.", "tag": "Creative"}
        ]
    },
    {
        "text": "In science class, what type of experiments interest you most?",
        "category": "Academic",
        "options": [
            {"text": "Biology experiments with living organisms.", "tag": "Biological"},
            {"text": "Chemistry experiments involving reactions and compounds.", "tag": "Molecular-focused"},
            {"text": "Physics experiments about motion and energy.", "tag": "Mathematical-logic"},
            {"text": "Environmental science field studies.", "tag": "Ecological"}
        ]
    },
    {
        "text": "How do you perform best on assignments and projects?",
        "category": "Academic",
        "options": [
            {"text": "Individual work where I control every detail.", "tag": "Detail-oriented"},
            {"text": "Group work where I can collaborate and share ideas.", "tag": "Collaborative"},
            {"text": "Open-ended projects where I can be creative.", "tag": "Creative"},
            {"text": "Structured assignments with clear requirements.", "tag": "Methodical"}
        ]
    },
    {
        "text": "Which academic skill is your strongest?",
        "category": "Academic",
        "options": [
            {"text": "Written communication and essays.", "tag": "Writing-heavy"},
            {"text": "Mathematical problem-solving.", "tag": "Logical"},
            {"text": "Oral presentations and public speaking.", "tag": "Articulate"},
            {"text": "Research and data analysis.", "tag": "Analytical"}
        ]
    },
    {
        "text": "What type of academic subject excites your curiosity?",
        "category": "Academic",
        "options": [
            {"text": "How things are built and how systems work.", "tag": "Technical"},
            {"text": "How people behave and think.", "tag": "Behavioral-analytical"},
            {"text": "How society and cultures develop.", "tag": "Societal-analytical"},
            {"text": "How technology can solve real-world problems.", "tag": "Innovative"}
        ]
    },
    {
        "text": "When studying for exams, what is your approach?",
        "category": "Academic",
        "options": [
            {"text": "I create detailed notes and study guides.", "tag": "Methodical"},
            {"text": "I form study groups and discuss with others.", "tag": "Social"},
            {"text": "I use flashcards and memory techniques.", "tag": "Logical"},
            {"text": "I review past exams and practice problems.", "tag": "Practical"}
        ]
    },
    {
        "text": "How do you handle difficult or complex topics?",
        "category": "Academic",
        "options": [
            {"text": "I break them down into smaller parts.", "tag": "Analytical"},
            {"text": "I seek help from teachers or tutors.", "tag": "Help-seeking"},
            {"text": "I persist and figure it out myself.", "tag": "Resilient"},
            {"text": "I visualize or create analogies to understand.", "tag": "Visual-focused"}
        ]
    },
    {
        "text": "What type of grading system motivates you?",
        "category": "Academic",
        "options": [
            {"text": "Letter grades and comparative ranking.", "tag": "Competitive"},
            {"text": "Detailed feedback on my work.", "tag": "Growth-oriented"},
            {"text": "Pass/fail or completion-based grades.", "tag": "Practical"},
            {"text": "Mastery-based assessment.", "tag": "Perfectionist"}
        ]
    },
    {
        "text": "How important is extracurricular involvement to you?",
        "category": "Academic",
        "options": [
            {"text": "Very important - clubs and activities are essential.", "tag": "Social"},
            {"text": "Somewhat important - I participate selectively.", "tag": "Balanced"},
            {"text": "Not important - I focus on academics.", "tag": "Focused"},
            {"text": "I lead clubs and take leadership roles.", "tag": "Leadership"}
        ]
    },
    {
        "text": "Which type of reading do you prefer?",
        "category": "Academic",
        "options": [
            {"text": "Technical manuals and instructional texts.", "tag": "Technical"},
            {"text": "Fiction and imaginative literature.", "tag": "Creative"},
            {"text": "News and current events.", "tag": "Analytical"},
            {"text": "Historical and biographical accounts.", "tag": "Theoretical"}
        ]
    },
    {
        "text": "How do you feel about memorization in academics?",
        "category": "Academic",
        "options": [
            {"text": "I'm good at it and find it useful.", "tag": "Methodical"},
            {"text": "I prefer understanding over memorization.", "tag": "Analytical"},
            {"text": "I struggle with memorization.", "tag": "Creative"},
            {"text": "I use memory aids and techniques.", "tag": "Practical"}
        ]
    },
    {
        "text": "What academic environment do you thrive in?",
        "category": "Academic",
        "options": [
            {"text": "Large universities with diverse opportunities.", "tag": "Social"},
            {"text": "Smaller institutions with close faculty relationships.", "tag": "Interpersonal"},
            {"text": "Specialized or technical schools.", "tag": "Technical"},
            {"text": "Flexible or online learning environments.", "tag": "Independent"}
        ]
    },
    {
        "text": "How do you approach research papers and projects?",
        "category": "Academic",
        "options": [
            {"text": "I start early and plan thoroughly.", "tag": "Methodical"},
            {"text": "I research deeply and create comprehensive work.", "tag": "Analytical"},
            {"text": "I add creative elements to make it interesting.", "tag": "Creative"},
            {"text": "I focus on meeting the requirements efficiently.", "tag": "Practical"}
        ]
    },
    {
        "text": "What type of teacher/professor helps you learn best?",
        "category": "Academic",
        "options": [
            {"text": "Engaging storytellers who make topics interesting.", "tag": "Communication-focused"},
            {"text": "Experts who provide deep technical knowledge.", "tag": "Technical"},
            {"text": "Mentors who provide personalized feedback.", "tag": "Supportive"},
            {"text": "Organized instructors with clear expectations.", "tag": "Methodical"}
        ]
    },
    {
        "text": "How do you view collaboration on academic work?",
        "category": "Academic",
        "options": [
            {"text": "It's essential for learning and motivation.", "tag": "Social"},
            {"text": "It's helpful but I prefer individual work.", "tag": "Independent"},
            {"text": "It's necessary but can be challenging.", "tag": "Realistic"},
            {"text": "I excel at bringing team strengths together.", "tag": "Leadership"}
        ]
    },
    {
        "text": "Which type of writing assignment appeals to you most?",
        "category": "Academic",
        "options": [
            {"text": "Creative writing and storytelling.", "tag": "Creative"},
            {"text": "Analytical and argumentative essays.", "tag": "Analytical"},
            {"text": "Technical and instructional writing.", "tag": "Technical"},
            {"text": "Reflective and personal narratives.", "tag": "Introspective"}
        ]
    },
    {
        "text": "How do you handle time management for schoolwork?",
        "category": "Academic",
        "options": [
            {"text": "I plan ahead and work consistently.", "tag": "Methodical"},
            {"text": "I work best under deadline pressure.", "tag": "Practical"},
            {"text": "I struggle with procrastination.", "tag": "Realistic"},
            {"text": "I balance work with other priorities well.", "tag": "Organized"}
        ]
    },
    {
        "text": "What motivates you to do well academically?",
        "category": "Academic",
        "options": [
            {"text": "Getting good grades and high rankings.", "tag": "Ambitious"},
            {"text": "Mastering the subject matter.", "tag": "Perfectionist"},
            {"text": "Meeting expectations of parents or mentors.", "tag": "Dutiful"},
            {"text": "Personal curiosity and love of learning.", "tag": "Passionate"}
        ]
    },
    {
        "text": "How comfortable are you with public speaking in class?",
        "category": "Academic",
        "options": [
            {"text": "Very comfortable - I enjoy presentations.", "tag": "Articulate"},
            {"text": "Somewhat comfortable with preparation.", "tag": "Practical"},
            {"text": "Uncomfortable but I can do it.", "tag": "Resilient"},
            {"text": "Very uncomfortable - I avoid it.", "tag": "Shy"}
        ]
    },
    {
        "text": "Which academic discipline interests you most?",
        "category": "Academic",
        "options": [
            {"text": "Engineering and applied sciences.", "tag": "Technical"},
            {"text": "Humanities and social sciences.", "tag": "Societal-analytical"},
            {"text": "Business and economics.", "tag": "Strategic"},
            {"text": "Health sciences and medicine.", "tag": "Medical"}
        ]
    },
    {
        "text": "How do you respond when you get a low grade?",
        "category": "Academic",
        "options": [
            {"text": "I analyze what went wrong and improve.", "tag": "Growth-oriented"},
            {"text": "I feel discouraged and lose motivation.", "tag": "Sensitive"},
            {"text": "I question the grading fairness.", "tag": "Analytical"},
            {"text": "I work harder to prove myself.", "tag": "Ambitious"}
        ]
    },
    {
    "text": "Which science subject do you find most interesting?",
    "category": "Academic",
    "options": [
        {"text": "Biology", "tag": "Biological"},
        {"text": "Chemistry", "tag": "Molecular-focused"},
        {"text": "Physics", "tag": "Mathematical-logic"},
        {"text": "Earth Science", "tag": "Ecological"}
    ]
},
{
    "text": "How do you approach group projects in school?",
    "category": "Academic",
    "options": [
        {"text": "Take the lead and assign tasks.", "tag": "Leadership"},
        {"text": "Focus on my assigned part.", "tag": "Detail-oriented"},
        {"text": "Help coordinate and communicate.", "tag": "Collaborative"},
        {"text": "Ensure deadlines are met.", "tag": "Methodical"}
    ]
},
{
    "text": "What type of math problems do you enjoy?",
    "category": "Academic",
    "options": [
        {"text": "Solving equations and logic puzzles.", "tag": "Logical"},
        {"text": "Applying math to real-life situations.", "tag": "Practical"},
        {"text": "Exploring abstract concepts.", "tag": "Theoretical"},
        {"text": "Working with statistics and data.", "tag": "Analytical"}
    ]
},
{
    "text": "How do you prepare for oral presentations?",
    "category": "Academic",
    "options": [
        {"text": "Practice speaking in front of others.", "tag": "Articulate"},
        {"text": "Create detailed notes and outlines.", "tag": "Methodical"},
        {"text": "Use visuals to support my talk.", "tag": "Visual-focused"},
        {"text": "Rehearse until I feel confident.", "tag": "Resilient"}
    ]
},
{
    "text": "Which academic competition would you join?",
    "category": "Academic",
    "options": [
        {"text": "Math Olympiad", "tag": "Logical"},
        {"text": "Science Fair", "tag": "Scientific"},
        {"text": "Debate Tournament", "tag": "Articulate"},
        {"text": "Art Contest", "tag": "Creative"}
    ]
},
]