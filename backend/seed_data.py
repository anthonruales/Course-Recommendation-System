# seed_data.py - Course Recommendation System Data

COURSES_POOL = [
    # --- TECHNICAL & ANALYTICAL ---
    {"course_name": "BS Computer Science", "description": "Study of computation, complexity, and advanced software design.", "minimum_gwa": 88, "recommended_strand": "STEM", "trait_tag": ["Problem-solving", "Logical", "Independent", "Algorithm-focused", "Abstract-thinking", "Innovative", "Office-based", "Remote-friendly", "Detail-focused"]},
    {"course_name": "BS Information Technology", "description": "Focuses on the practical application of computing technology to business processes.", "minimum_gwa": 85, "recommended_strand": "STEM", "trait_tag": ["Problem-solving", "Collaborative", "Helping-others", "Hands-on", "Office-based", "Team-centric", "Systematic", "Service-oriented", "Practical"]},
    {"course_name": "BS Civil Engineering", "description": "Design and supervision of infrastructure projects like roads, bridges, and buildings.", "minimum_gwa": 90, "recommended_strand": "STEM", "trait_tag": ["Problem-solving", "Big-picture", "Leading-teams", "Field-work", "Hands-on", "Visual-learner", "Structural-thinking", "Collaborative", "Practical"]},
    {"course_name": "BS Computer Engineering", "description": "Combines electronics engineering and computer science to develop computer hardware and software systems.", "minimum_gwa": 88, "recommended_strand": "STEM", "trait_tag": ["Problem-solving", "Logical", "Hands-on", "Hardware-focused", "Independent", "Detail-focused", "Laboratory", "Analytical", "Technical"]},
    {"course_name": "BS Electronics Engineering", "description": "Design and development of electronic circuits, communication systems, and automated devices.", "minimum_gwa": 88, "recommended_strand": "STEM", "trait_tag": ["Problem-solving", "Detail-focused", "Hands-on", "Precision-oriented", "Laboratory", "Circuit-design", "Independent", "Analytical", "Technical"]},
    {"course_name": "BS Mechanical Engineering", "description": "Focuses on the design, analysis, and manufacturing of mechanical systems and machinery.", "minimum_gwa": 88, "recommended_strand": "STEM", "trait_tag": ["Problem-solving", "Hands-on", "Visual-learner", "Tangible-design", "Field-work", "Collaborative", "Mechanical-minded", "Practical", "Analytical"]},
    {"course_name": "BS Electrical Engineering", "description": "Study of electricity, electronics, and electromagnetism for power generation and distribution.", "minimum_gwa": 88, "recommended_strand": "STEM", "trait_tag": ["Problem-solving", "Logical", "Big-picture", "Systemic-thinking", "Detail-focused", "Laboratory", "Theoretical", "Complex-systems", "Analytical"]},
    {"course_name": "BS Data Science", "description": "Uses scientific methods, algorithms, and systems to extract knowledge and insights from structured and unstructured data.", "minimum_gwa": 89, "recommended_strand": "STEM", "trait_tag": ["Problem-solving", "Analytical", "Independent", "Pattern-recognition", "Office-based", "Remote-friendly", "Data-driven", "Statistical-thinking", "Research-oriented"]},
    {"course_name": "BS Mathematics", "description": "Advanced study of mathematical structures, logic, and numerical analysis for various industries.", "minimum_gwa": 87, "recommended_strand": "STEM", "trait_tag": ["Problem-solving", "Logical", "Independent", "Abstract-thinking", "Theoretical", "Detail-focused", "Office-based", "Research-oriented", "Contemplative"]},
    {"course_name": "BS Statistics", "description": "Focuses on the collection, analysis, interpretation, and presentation of quantitative data.", "minimum_gwa": 86, "recommended_strand": "STEM", "trait_tag": ["Problem-solving", "Analytical", "Detail-focused", "Data-driven", "Office-based", "Research-oriented", "Pattern-recognition", "Quantitative", "Methodical"]},
    {"course_name": "BS Geodetic Engineering", "description": "Professional study of surveying, mapping, and global positioning systems (GPS).", "minimum_gwa": 86, "recommended_strand": "STEM", "trait_tag": ["Problem-solving", "Hands-on", "Field-work", "Outdoor-enthusiast", "Precision-oriented", "Independent", "Visual-learner", "Mapping-focused", "Exploratory"]},
    {"course_name": "BS Industrial Engineering", "description": "Focuses on optimizing complex processes, systems, and organizations to reduce waste.", "minimum_gwa": 86, "recommended_strand": "STEM", "trait_tag": ["Problem-solving", "Big-picture", "Leading-teams", "Efficiency-driven", "Office-based", "Collaborative", "Analytical", "Process-optimization", "Strategic"]},
    {"course_name": "BS Cybersecurity", "description": "Specialized training in protecting networks, devices, and data from digital attacks.", "minimum_gwa": 87, "recommended_strand": "STEM", "trait_tag": ["Problem-solving", "Logical", "Independent", "Detail-focused", "Vigilant", "Office-based", "Remote-friendly", "Defensive-thinking", "Methodical"]},

    # --- BUSINESS & LEADERSHIP ---
    {"course_name": "BS Accountancy", "description": "Detailed study of financial reporting, auditing, and taxation.", "minimum_gwa": 92, "recommended_strand": "ABM", "trait_tag": ["Detail-focused", "Analytical", "Independent", "Office-based", "Methodical", "Numerical-thinking", "Compliance-oriented", "Problem-solving", "Introverted"]},
    {"course_name": "BS Business Administration major in Marketing Management", "description": "Focuses on market research, consumer behavior, and strategic brand positioning.", "minimum_gwa": 85, "recommended_strand": "ABM", "trait_tag": ["Creative-expression", "Extroverted", "Collaborative", "Office-based", "Strategic", "Persuasive", "Team-centric", "Big-picture", "Social"]},
    {"course_name": "BS Business Administration major in Financial Management", "description": "Deals with investment decisions, capital markets, and corporate financial planning.", "minimum_gwa": 86, "recommended_strand": "ABM", "trait_tag": ["Problem-solving", "Analytical", "Independent", "Office-based", "Risk-assessment", "Strategic", "Detail-focused", "Logical", "Investment-minded"]},
    {"course_name": "BS Business Administration major in Human Resource Management", "description": "Studies organizational behavior, employee relations, and talent development.", "minimum_gwa": 84, "recommended_strand": "ABM", "trait_tag": ["Helping-others", "Extroverted", "Collaborative", "Office-based", "Empathetic", "Team-centric", "People-skills", "Leadership", "Social"]},
    {"course_name": "BS Entrepreneurship", "description": "Develops skills in identifying business opportunities and managing new ventures.", "minimum_gwa": 83, "recommended_strand": "ABM", "trait_tag": ["Problem-solving", "Independent", "Risk-taking", "Big-picture", "Innovative", "Leading-teams", "Creative-expression", "Hands-on", "Ambitious"]},
    {"course_name": "BS Customs Administration", "description": "Focuses on tariff and customs laws, international trade, and logistics.", "minimum_gwa": 85, "recommended_strand": "ABM", "trait_tag": ["Problem-solving", "Detail-focused", "Methodical", "Office-based", "Regulatory-compliance", "Analytical", "Trade-focused", "Independent", "Systematic"]},
    {"course_name": "BS Real Estate Management", "description": "Deals with property appraisal, brokerage, and real estate development laws.", "minimum_gwa": 84, "recommended_strand": "ABM", "trait_tag": ["Helping-others", "Extroverted", "Independent", "Field-work", "Negotiation-skills", "Social", "Visual-learner", "Sales-oriented", "Persuasive"]},
    {"course_name": "BS Accounting Information Systems", "description": "Combines accounting principles with information technology to manage business financial data.", "minimum_gwa": 88, "recommended_strand": "ABM", "trait_tag": ["Problem-solving", "Logical", "Detail-focused", "Office-based", "Tech-savvy", "Analytical", "Systematic", "Independent", "Hybrid-thinking"]},
    {"course_name": "BS Management Accounting", "description": "Focuses on providing internal financial information for business decision-making and strategic planning.", "minimum_gwa": 88, "recommended_strand": "ABM", "trait_tag": ["Problem-solving", "Analytical", "Detail-focused", "Office-based", "Strategic", "Decision-support", "Independent", "Business-minded", "Financial-analysis"]},
    {"course_name": "BS Business Administration major in Operations Management", "description": "Focuses on the production and delivery of goods and services, logistics, and supply chain.", "minimum_gwa": 84, "recommended_strand": "ABM", "trait_tag": ["Problem-solving", "Big-picture", "Leading-teams", "Office-based", "Process-optimization", "Collaborative", "Systematic", "Efficiency-driven", "Hands-on"]},
    {"course_name": "BS Business Economics", "description": "Study of economic theories and their practical application in business environments.", "minimum_gwa": 86, "recommended_strand": "ABM", "trait_tag": ["Problem-solving", "Analytical", "Theoretical", "Office-based", "Research-oriented", "Market-analysis", "Logical", "Strategic", "Independent"]},
    {"course_name": "BS Agribusiness", "description": "Management and operations of agricultural businesses and the food supply chain.", "minimum_gwa": 83, "recommended_strand": "ABM", "trait_tag": ["Problem-solving", "Hands-on", "Field-work", "Outdoor-enthusiast", "Nature-connected", "Business-minded", "Practical", "Independent", "Resourceful"]},
    {"course_name": "BS Legal Management", "description": "Study of business administration combined with essential legal principles and procedures.", "minimum_gwa": 87, "recommended_strand": "ABM", "trait_tag": ["Problem-solving", "Analytical", "Detail-focused", "Office-based", "Law-oriented", "Logical", "Compliance", "Independent", "Critical-thinking"]},
    {"course_name": "Bachelor of Public Administration", "description": "Preparation for leadership roles in government, non-profits, and public service organizations.", "minimum_gwa": 85, "recommended_strand": "HUMSS", "trait_tag": ["Helping-others", "Leading-teams", "Collaborative", "Office-based", "Civic-minded", "Policy-focused", "Big-picture", "Social", "Public-service"]},

    # --- SCIENCE & HEALTHCARE ---
    {"course_name": "BS Medical Technology", "description": "Focuses on laboratory analysis of blood, tissues, and fluids for disease diagnosis.", "minimum_gwa": 90, "recommended_strand": "STEM", "trait_tag": ["Problem-solving", "Detail-focused", "Laboratory", "Methodical", "Analytical", "Clinical-science", "Independent", "Precision-oriented", "Helping-others"]},
    {"course_name": "BS Pharmacy", "description": "Study of drug preparation, therapeutic uses, and pharmaceutical chemistry.", "minimum_gwa": 88, "recommended_strand": "STEM", "trait_tag": ["Helping-others", "Detail-focused", "Office-based", "Methodical", "Analytical", "Patient-interaction", "Precision-oriented", "Scientific-thinking", "Service-oriented"]},
    {"course_name": "BS Physical Therapy", "description": "Rehabilitation science focusing on improving patient mobility and physical function.", "minimum_gwa": 89, "recommended_strand": "STEM", "trait_tag": ["Helping-others", "Extroverted", "Hands-on", "Clinical-setting", "Empathetic", "Patient-focused", "Active", "Collaborative", "Encouraging"]},
    {"course_name": "BS Occupational Therapy", "description": "Helping patients develop skills for daily living and working through therapeutic activities.", "minimum_gwa": 88, "recommended_strand": "STEM", "trait_tag": ["Helping-others", "Extroverted", "Hands-on", "Clinical-setting", "Empathetic", "Patient-focused", "Creative-expression", "Adaptive", "Problem-solving"]},
    {"course_name": "BS Biology", "description": "Scientific study of living organisms, from molecular levels to entire ecosystems.", "minimum_gwa": 86, "recommended_strand": "STEM", "trait_tag": ["Research-oriented", "Analytical", "Laboratory", "Field-work", "Independent", "Nature-focused", "Theoretical", "Observational", "Scientific-thinking"]},
    {"course_name": "BS Radiologic Technology", "description": "Operating medical imaging equipment like X-rays, CT scans, and MRI.", "minimum_gwa": 85, "recommended_strand": "STEM", "trait_tag": ["Helping-others", "Hands-on", "Clinical-setting", "Detail-focused", "Tech-savvy", "Patient-interaction", "Safety-conscious", "Practical", "Collaborative"]},
    {"course_name": "BS Nutrition and Dietetics", "description": "Study of food science and the role of nutrition in health and disease management.", "minimum_gwa": 85, "recommended_strand": "STEM", "trait_tag": ["Helping-others", "Extroverted", "Office-based", "Clinical-setting", "Health-conscious", "Empathetic", "Analytical", "Service-oriented", "Scientific-thinking"]},
    {"course_name": "BS Midwifery", "description": "Primary healthcare for women during pregnancy, childbirth, and the postpartum period.", "minimum_gwa": 83, "recommended_strand": "STEM", "trait_tag": ["Helping-others", "Empathetic", "Hands-on", "Clinical-setting", "Maternal-care", "Patient-focused", "Extroverted", "Crisis-management", "Compassionate"]},
    {"course_name": "BS Nursing", "description": "Professional training in patient care, health promotion, and community health nursing.", "minimum_gwa": 89, "recommended_strand": "STEM", "trait_tag": ["Helping-others", "Empathetic", "Hands-on", "Clinical-setting", "Team-centric", "Patient-focused", "Resilient", "Collaborative", "Compassionate"]},
    {"course_name": "BS Speech-Language Pathology", "description": "Specialized study in treating communication and swallowing disorders in patients.", "minimum_gwa": 90, "recommended_strand": "STEM", "trait_tag": ["Helping-others", "Extroverted", "Clinical-setting", "Patient-focused", "Empathetic", "Communication-skills", "Detail-focused", "Collaborative", "Encouraging"]},
    {"course_name": "BS Respiratory Therapy", "description": "Focuses on the treatment and care of patients with cardiopulmonary and breathing disorders.", "minimum_gwa": 86, "recommended_strand": "STEM", "trait_tag": ["Helping-others", "Hands-on", "Clinical-setting", "Crisis-management", "Patient-focused", "Detail-focused", "Team-centric", "Resilient", "Technical"]},
    {"course_name": "BS Chemistry", "description": "The study of matter, its properties, and how it changes during chemical reactions.", "minimum_gwa": 87, "recommended_strand": "STEM", "trait_tag": ["Problem-solving", "Analytical", "Laboratory", "Detail-focused", "Research-oriented", "Methodical", "Scientific-thinking", "Independent", "Molecular-focus"]},
    {"course_name": "BS Marine Biology", "description": "Study of marine organisms and their behaviors and interactions with the environment.", "minimum_gwa": 85, "recommended_strand": "STEM", "trait_tag": ["Research-oriented", "Field-work", "Outdoor-enthusiast", "Exploratory", "Analytical", "Nature-focused", "Independent", "Aquatic-passion", "Adventurous"]},
    {"course_name": "BS Environmental Science", "description": "Interdisciplinary study of environmental problems and human impact on the ecosystem.", "minimum_gwa": 84, "recommended_strand": "STEM", "trait_tag": ["Problem-solving", "Field-work", "Outdoor-enthusiast", "Research-oriented", "Conservation-minded", "Analytical", "Big-picture", "Nature-focused", "Advocacy"]},
    {"course_name": "BS Optometry", "description": "Specialized healthcare profession involving examining the eyes for defects or abnormalities.", "minimum_gwa": 88, "recommended_strand": "STEM", "trait_tag": ["Helping-others", "Detail-focused", "Clinical-setting", "Patient-interaction", "Methodical", "Independent", "Vision-care", "Analytical", "Service-oriented"]},
    {"course_name": "BS Health Information Management", "description": "Combines medical science and IT to manage patient data and healthcare records.", "minimum_gwa": 83, "recommended_strand": "STEM", "trait_tag": ["Problem-solving", "Detail-focused", "Office-based", "Tech-savvy", "Organized", "Analytical", "Independent", "Systematic", "Data-management"]},
    {"course_name": "BS Biotechnology", "description": "Using biological systems or living organisms to develop or create different products.", "minimum_gwa": 88, "recommended_strand": "STEM", "trait_tag": ["Research-oriented", "Innovative", "Laboratory", "Problem-solving", "Analytical", "Bio-science", "Detail-focused", "Independent", "Scientific-thinking"]},
    {"course_name": "BS Exercise and Sports Science", "description": "Scientific study of human movement and how the body responds to physical activity.", "minimum_gwa": 82, "recommended_strand": "STEM", "trait_tag": ["Helping-others", "Active", "Hands-on", "Extroverted", "Athletic-passion", "Field-work", "Research-oriented", "Collaborative", "Health-conscious"]},
    {"course_name": "BS Psychology", "description": "Scientific study of human behavior and mental processes.", "minimum_gwa": 87, "recommended_strand": "HUMSS", "trait_tag": ["Helping-others", "Analytical", "Empathetic", "Research-oriented", "Observational", "Office-based", "Clinical-setting", "Theoretical", "Social"]},
    
    # --- CREATIVE & DESIGN ---
    {"course_name": "BS Interior Design", "description": "Planning and design of interior spaces to improve function and aesthetic quality of life.", "minimum_gwa": 85, "recommended_strand": "STEM", "trait_tag": ["Creative-expression", "Visual-learner", "Hands-on", "Office-based", "Client-interaction", "Aesthetic-sense", "Detail-focused", "Spatial-thinking", "Collaborative"]},
    {"course_name": "Bachelor of Fine Arts", "description": "Advanced study in traditional arts like painting, sculpture, and visual theory.", "minimum_gwa": 80, "recommended_strand": "HUMSS", "trait_tag": ["Creative-expression", "Independent", "Visual-learner", "Studio-work", "Artistic-passion", "Expressive", "Hands-on", "Experimental", "Contemplative"]},
    {"course_name": "BA in Communication", "description": "Study of media production, public relations, broadcasting, and digital journalism.", "minimum_gwa": 85, "recommended_strand": "HUMSS", "trait_tag": ["Creative-expression", "Extroverted", "Collaborative", "Office-based", "Media-savvy", "Articulate", "Team-centric", "Strategic", "Social"]},
    {"course_name": "BS Entertainment and Multimedia Computing", "description": "Specialized study in game development, digital animation, and interactive software.", "minimum_gwa": 86, "recommended_strand": "STEM", "trait_tag": ["Creative-expression", "Problem-solving", "Independent", "Office-based", "Tech-savvy", "Innovative", "Digital-art", "Logical", "Visual-learner"]},
    {"course_name": "BA in Fashion Design and Merchandising", "description": "Study of apparel design, textile science, and the business of the fashion industry.", "minimum_gwa": 82, "recommended_strand": "HUMSS", "trait_tag": ["Creative-expression", "Visual-learner", "Hands-on", "Studio-work", "Aesthetic-sense", "Trend-aware", "Innovative", "Business-minded", "Social"]},
    {"course_name": "BS Industrial Design", "description": "Designing mass-produced products focusing on user experience, form, and industrial function.", "minimum_gwa": 85, "recommended_strand": "STEM", "trait_tag": ["Creative-expression", "Problem-solving", "Hands-on", "Studio-work", "Visual-learner", "User-focused", "Innovative", "Technical", "Practical"]},
    {"course_name": "BA in Digital Filmmaking", "description": "Comprehensive training in cinematography, scriptwriting, and post-production editing.", "minimum_gwa": 84, "recommended_strand": "HUMSS", "trait_tag": ["Creative-expression", "Collaborative", "Visual-learner", "Studio-work", "Storytelling", "Tech-savvy", "Team-centric", "Cinematic-vision", "Artistic-passion"]},
    {"course_name": "BS Clothing Technology", "description": "The technical side of garment production, quality control, and clothing manufacturing systems.", "minimum_gwa": 84, "recommended_strand": "STEM", "trait_tag": ["Problem-solving", "Hands-on", "Detail-focused", "Office-based", "Methodical", "Technical", "Manufacturing-focus", "Practical", "Quality-oriented"]},
    {"course_name": "BS Architecture", "description": "Integration of art and science in designing buildings and structures with focus on aesthetics and safety.", "minimum_gwa": 88, "recommended_strand": "STEM", "trait_tag": ["Creative-expression", "Problem-solving", "Visual-learner", "Office-based", "Studio-work", "Analytical", "Big-picture", "Detail-focused", "Technical"]},
    {"course_name": "BS Multimedia Arts", "description": "Multidisciplinary program combining graphic design, 2D/3D animation, and video production.", "minimum_gwa": 83, "recommended_strand": "HUMSS", "trait_tag": ["Creative-expression", "Visual-learner", "Tech-savvy", "Office-based", "Studio-work", "Versatile", "Digital-art", "Innovative", "Independent"]},
    {"course_name": "BA in Advertising Arts", "description": "Focuses on visual communication, branding, and creative strategies for marketing campaigns.", "minimum_gwa": 84, "recommended_strand": "HUMSS", "trait_tag": ["Creative-expression", "Visual-learner", "Collaborative", "Office-based", "Strategic", "Persuasive", "Brand-thinking", "Innovative", "Social"]},
    {"course_name": "BA in Animation", "description": "Technical and artistic study of creating movement and storytelling through digital and traditional animation.", "minimum_gwa": 82, "recommended_strand": "HUMSS", "trait_tag": ["Creative-expression", "Visual-learner", "Independent", "Studio-work", "Detail-focused", "Patient", "Storytelling", "Tech-savvy", "Artistic-passion"]},
    {"course_name": "BA in Game Art and Design", "description": "Focuses on the visual elements of games, including character design, environment art, and UI/UX.", "minimum_gwa": 84, "recommended_strand": "STEM", "trait_tag": ["Creative-expression", "Visual-learner", "Independent", "Office-based", "Digital-art", "Innovative", "World-building", "Tech-savvy", "Detail-focused"]},
    {"course_name": "BA in Photography", "description": "Professional study of digital and analog photography, lighting, and visual composition.", "minimum_gwa": 80, "recommended_strand": "HUMSS", "trait_tag": ["Creative-expression", "Visual-learner", "Independent", "Field-work", "Studio-work", "Observational", "Artistic-passion", "Tech-savvy", "Client-interaction"]},
    {"course_name": "BA in Music Production", "description": "Study of sound design, music theory, and digital tools for audio recording and engineering.", "minimum_gwa": 82, "recommended_strand": "HUMSS", "trait_tag": ["Creative-expression", "Auditory-skills", "Independent", "Studio-work", "Tech-savvy", "Detail-focused", "Artistic-passion", "Methodical", "Patient"]},
    {"course_name": "BA in Theater Arts", "description": "The art of performance, stage management, scriptwriting, and theatrical production.", "minimum_gwa": 80, "recommended_strand": "HUMSS", "trait_tag": ["Creative-expression", "Extroverted", "Collaborative", "Studio-work", "Performative", "Expressive", "Team-centric", "Storytelling", "Confident"]},
    {"course_name": "BS Landscape Architecture", "description": "Designing outdoor public areas, parks, and gardens to harmonize with the environment.", "minimum_gwa": 85, "recommended_strand": "STEM", "trait_tag": ["Creative-expression", "Visual-learner", "Outdoor-enthusiast", "Field-work", "Environmental-design", "Nature-focused", "Big-picture", "Technical", "Aesthetic-sense"]},
    {"course_name": "BA in Journalism", "description": "Specialized training in news gathering, ethics, and writing for print, broadcast, and digital media.", "minimum_gwa": 85, "recommended_strand": "HUMSS", "trait_tag": ["Creative-expression", "Extroverted", "Independent", "Field-work", "Office-based", "Inquisitive", "Articulate", "Ethical", "Investigative"]},

    # --- SOCIAL, EDUCATION & SERVICE ---
    {"course_name": "BS Criminology", "description": "Study of crime prevention, law enforcement, and criminal justice.", "minimum_gwa": 83, "recommended_strand": "HUMSS", "trait_tag": ["Problem-solving", "Disciplined", "Field-work", "Law-enforcement", "Protective", "Physical-fitness", "Analytical", "Detail-focused", "Justice-minded"]},
    {"course_name": "BS Hospitality Management", "description": "Management of hotels, restaurants, and tourism-related businesses.", "minimum_gwa": 82, "recommended_strand": "ABM", "trait_tag": ["Helping-others", "Extroverted", "Hands-on", "Service-oriented", "Team-centric", "Collaborative", "Guest-focused", "Organized", "Social"]},
    {"course_name": "Bachelor of Secondary Education", "description": "Preparing teachers for high school levels with specialization in specific subject areas like Math, English, or Science.", "minimum_gwa": 85, "recommended_strand": "HUMSS", "trait_tag": ["Helping-others", "Extroverted", "Leading-teams", "Office-based", "Mentoring", "Patient", "Subject-expertise", "Collaborative", "Social"]},
    {"course_name": "BS Tourism Management", "description": "Focuses on travel industry operations, sustainable tourism, and heritage management.", "minimum_gwa": 82, "recommended_strand": "ABM", "trait_tag": ["Helping-others", "Extroverted", "Field-work", "Cultural-awareness", "Service-oriented", "Social", "Organized", "Global-minded", "Business"]},
    {"course_name": "BS Office Administration", "description": "Training in office management, secretarial duties, and corporate records handling.", "minimum_gwa": 80, "recommended_strand": "ABM", "trait_tag": ["Helping-others", "Detail-focused", "Office-based", "Organized", "Methodical", "Collaborative", "Administrative-skills", "Systematic", "Service-oriented"]},
    {"course_name": "Bachelor of Elementary Education", "description": "Training for teachers specializing in primary school education and child development.", "minimum_gwa": 85, "recommended_strand": "HUMSS", "trait_tag": ["Helping-others", "Extroverted", "Collaborative", "Office-based", "Patient", "Creative-expression", "Child-focused", "Nurturing", "Social"]},
    {"course_name": "BA in Political Science", "description": "Study of government systems, political activities, and political behavior.", "minimum_gwa": 86, "recommended_strand": "HUMSS", "trait_tag": ["Problem-solving", "Analytical", "Theoretical", "Office-based", "Leadership", "Critical-thinking", "Governance-focus", "Research-oriented", "Debating"]},
    {"course_name": "BS Social Work", "description": "Focuses on social welfare, community organizing, and helping marginalized individuals.", "minimum_gwa": 84, "recommended_strand": "HUMSS", "trait_tag": ["Helping-others", "Empathetic", "Field-work", "Advocacy", "Community-focused", "Resilient", "Collaborative", "Social", "Compassionate"]},
    {"course_name": "BS Development Communication", "description": "Using communication to promote social change and community development.", "minimum_gwa": 85, "recommended_strand": "HUMSS", "trait_tag": ["Helping-others", "Extroverted", "Field-work", "Media-savvy", "Advocacy", "Community-focused", "Collaborative", "Social", "Change-agent"]},
    {"course_name": "Bachelor of Library and Information Science", "description": "Management of information resources in libraries, archives, and digital databases.", "minimum_gwa": 82, "recommended_strand": "HUMSS", "trait_tag": ["Helping-others", "Organized", "Office-based", "Detail-focused", "Service-oriented", "Independent", "Systematic", "Information-management", "Introverted"]},
    {"course_name": "BS Community Development", "description": "Planning and implementing programs for community empowerment and poverty alleviation.", "minimum_gwa": 84, "recommended_strand": "HUMSS", "trait_tag": ["Helping-others", "Extroverted", "Field-work", "Community-focused", "Leadership", "Advocacy", "Practical", "Collaborative", "Grassroots"]},
    {"course_name": "BS Forensic Science", "description": "Application of scientific principles to criminal investigation and legal evidence.", "minimum_gwa": 87, "recommended_strand": "STEM", "trait_tag": ["Problem-solving", "Analytical", "Laboratory", "Detail-focused", "Investigative", "Methodical", "Independent", "Scientific-thinking", "Justice-minded"]},
    {"course_name": "Bachelor of Special Needs Education", "description": "Specialized training for teaching students with diverse learning needs and disabilities.", "minimum_gwa": 86, "recommended_strand": "HUMSS", "trait_tag": ["Helping-others", "Empathetic", "Patient", "Office-based", "Adaptive", "Creative-expression", "Collaborative", "Compassionate", "Nurturing"]},
    {"course_name": "BA in International Studies", "description": "Study of global issues, diplomacy, foreign languages, and international relations.", "minimum_gwa": 87, "recommended_strand": "HUMSS", "trait_tag": ["Problem-solving", "Analytical", "Theoretical", "Office-based", "Global-minded", "Cultural-awareness", "Research-oriented", "Strategic", "Diplomatic"]},
    {"course_name": "BA in Sociology", "description": "Systematic study of social institutions, collective behavior, and social development.", "minimum_gwa": 84, "recommended_strand": "HUMSS", "trait_tag": ["Problem-solving", "Analytical", "Research-oriented", "Office-based", "Field-work", "Observational", "Theoretical", "Cultural-awareness", "Social"]},
    {"course_name": "BA in Philosophy", "description": "Critical study of fundamental questions regarding existence, knowledge, values, and reason.", "minimum_gwa": 85, "recommended_strand": "HUMSS", "trait_tag": ["Problem-solving", "Logical", "Theoretical", "Independent", "Office-based", "Contemplative", "Critical-thinking", "Abstract-thinking", "Argumentative"]},
    {"course_name": "Bachelor of Early Childhood Education", "description": "Focuses on the holistic development and education of children from birth to age eight.", "minimum_gwa": 84, "recommended_strand": "HUMSS", "trait_tag": ["Helping-others", "Extroverted", "Patient", "Office-based", "Nurturing", "Creative-expression", "Playful", "Collaborative", "Child-focused"]},
    {"course_name": "Bachelor of Physical Education", "description": "Training for educators in sports, fitness, and health-related school programs.", "minimum_gwa": 82, "recommended_strand": "HUMSS", "trait_tag": ["Helping-others", "Extroverted", "Active", "Field-work", "Athletic-passion", "Coaching", "Motivational", "Collaborative", "Physical-fitness"]},
    {"course_name": "BA in Linguistics", "description": "Scientific study of language structure, evolution, and its role in human communication.", "minimum_gwa": 85, "recommended_strand": "HUMSS", "trait_tag": ["Problem-solving", "Analytical", "Theoretical", "Office-based", "Research-oriented", "Language-passion", "Detail-focused", "Independent", "Methodical"]},
    {"course_name": "BS Environmental Planning", "description": "Interdisciplinary study of urban development, resource management, and sustainable land use.", "minimum_gwa": 86, "recommended_strand": "STEM", "trait_tag": ["Problem-solving", "Big-picture", "Field-work", "Office-based", "Strategic", "Sustainability-minded", "Analytical", "Urban-focus", "Visual-learner"]},

    # --- MARITIME, AVIATION & AGRICULTURE ---
    {"course_name": "BS Marine Transportation", "description": "Professional training for deck officers, focusing on navigation and ship management.", "minimum_gwa": 85, "recommended_strand": "STEM", "trait_tag": ["Problem-solving", "Disciplined", "Field-work", "Outdoor-enthusiast", "Navigation", "Leadership", "Independent", "Adventurous", "Sea-passion"]},
    {"course_name": "BS Marine Engineering", "description": "Technical study of marine propulsion, power plants, and ship machinery maintenance.", "minimum_gwa": 85, "recommended_strand": "STEM", "trait_tag": ["Problem-solving", "Hands-on", "Field-work", "Mechanical-minded", "Technical", "Independent", "Methodical", "Disciplined", "Sea-passion"]},
    {"course_name": "BS Agriculture", "description": "Scientific study of crop production, livestock raising, and soil management.", "minimum_gwa": 82, "recommended_strand": "STEM", "trait_tag": ["Problem-solving", "Hands-on", "Field-work", "Outdoor-enthusiast", "Nature-connected", "Practical", "Independent", "Farming-passion", "Resourceful"]},
    {"course_name": "BS Forestry", "description": "Management and protection of forest resources, ecosystems, and wildlife conservation.", "minimum_gwa": 82, "recommended_strand": "STEM", "trait_tag": ["Problem-solving", "Hands-on", "Field-work", "Outdoor-enthusiast", "Nature-connected", "Conservation-minded", "Independent", "Adventurous", "Environmental-passion"]},
    {"course_name": "BS Fisheries", "description": "Study of aquaculture, fish processing, and sustainable aquatic resource management.", "minimum_gwa": 82, "recommended_strand": "STEM", "trait_tag": ["Problem-solving", "Hands-on", "Field-work", "Outdoor-enthusiast", "Aquatic-passion", "Nature-connected", "Practical", "Independent", "Resourceful"]},
    {"course_name": "Doctor of Veterinary Medicine", "description": "Six-year program focused on the prevention, diagnosis, and treatment of animal diseases.", "minimum_gwa": 88, "recommended_strand": "STEM", "trait_tag": ["Helping-others", "Empathetic", "Hands-on", "Clinical-setting", "Field-work", "Animal-care", "Detail-focused", "Patient-focused", "Compassionate"]},
    {"course_name": "BS Aeronautical Engineering", "description": "Design, construction, and maintenance of aircraft and spacecraft structures.", "minimum_gwa": 88, "recommended_strand": "STEM", "trait_tag": ["Problem-solving", "Analytical", "Detail-focused", "Office-based", "Laboratory", "Precision-oriented", "Aerospace-passion", "Technical", "Innovative"]},
    {"course_name": "BS Aircraft Maintenance Technology", "description": "Specialized training in the inspection, repair, and overhaul of aircraft engines and systems.", "minimum_gwa": 85, "recommended_strand": "STEM", "trait_tag": ["Problem-solving", "Hands-on", "Detail-focused", "Field-work", "Methodical", "Safety-conscious", "Technical", "Precision-oriented", "Aviation-passion"]},
    {"course_name": "BS Aviation Electronics Technology", "description": "Focuses on the electronic systems (avionics) used on aircraft and satellites.", "minimum_gwa": 85, "recommended_strand": "STEM", "trait_tag": ["Problem-solving", "Hands-on", "Detail-focused", "Laboratory", "Circuit-design", "Analytical", "Technical", "Precision-oriented", "Aviation-passion"]},
    {"course_name": "BS Geology", "description": "Study of the solid Earth, its rocks, and the processes by which they change.", "minimum_gwa": 85, "recommended_strand": "STEM", "trait_tag": ["Research-oriented", "Field-work", "Outdoor-enthusiast", "Analytical", "Observational", "Earth-science", "Independent", "Exploratory", "Nature-focused"]},
    {"course_name": "BS Physics", "description": "Fundamental study of matter, energy, and the laws of the universe.", "minimum_gwa": 87, "recommended_strand": "STEM", "trait_tag": ["Problem-solving", "Logical", "Theoretical", "Laboratory", "Research-oriented", "Abstract-thinking", "Mathematical", "Independent", "Scientific-thinking"]},
    {"course_name": "BS Meteorology", "description": "Scientific study of the atmosphere and weather patterns for forecasting.", "minimum_gwa": 85, "recommended_strand": "STEM", "trait_tag": ["Problem-solving", "Analytical", "Research-oriented", "Office-based", "Field-work", "Data-driven", "Pattern-recognition", "Weather-passion", "Scientific-thinking"]},
    {"course_name": "BS Food Technology", "description": "The application of food science to the selection, preservation, and packaging of food.", "minimum_gwa": 84, "recommended_strand": "STEM", "trait_tag": ["Problem-solving", "Hands-on", "Laboratory", "Detail-focused", "Methodical", "Quality-control", "Practical", "Scientific-thinking", "Food-science"]},
    {"course_name": "BS Culinary Management", "description": "Combines culinary arts with business management for professional kitchen operations.", "minimum_gwa": 82, "recommended_strand": "ABM", "trait_tag": ["Creative-expression", "Hands-on", "Leadership", "Active", "Culinary-passion", "Business-minded", "Team-centric", "Service-oriented", "Practical"]},
    {"course_name": "Bachelor of Technical-Vocational Teacher Education", "description": "Training for teachers in technical and vocational fields like welding, automotive, and electronics.", "minimum_gwa": 83, "recommended_strand": "TVL", "trait_tag": ["Helping-others", "Hands-on", "Leading-teams", "Field-work", "Mentoring", "Practical-skills", "Patient", "Collaborative", "Technical"]},
]

# ==================== ASSESSMENT QUESTIONS ====================

QUESTIONS_POOL = [
    # ===== CORE ACTIVITY PREFERENCES =====
    {
        "question": "What type of activities do you find most fulfilling?",
        "category": "Core Activities",
        "options": [
            {"text": "Solving complex problems and finding creative solutions", "tag": "Problem-solving"},
            {"text": "Helping others and making a positive impact on their lives", "tag": "Helping-others"},
            {"text": "Creating original content, art, or innovative designs", "tag": "Creative-expression"},
            {"text": "Leading and organizing teams to achieve goals", "tag": "Leading-teams"}
        ]
    },
    {
        "question": "In group projects, which role do you naturally gravitate towards?",
        "category": "Leadership Style",
        "options": [
            {"text": "The leader who coordinates everyone and delegates tasks", "tag": "Leading-teams"},
            {"text": "The problem solver who figures out technical solutions", "tag": "Problem-solving"},
            {"text": "The creative one who designs and adds innovative ideas", "tag": "Creative-expression"},
            {"text": "The supportive member who helps others complete their tasks", "tag": "Helping-others"}
        ]
    },
    {
        "question": "When faced with a community issue (like pollution in your barangay), what would you prefer to do?",
        "category": "Social Engagement",
        "options": [
            {"text": "Organize cleanup drives and mobilize volunteers", "tag": "Leading-teams"},
            {"text": "Research and propose technical solutions or innovations", "tag": "Problem-solving"},
            {"text": "Create awareness campaigns through art, videos, or posters", "tag": "Creative-expression"},
            {"text": "Go door-to-door educating residents and offering assistance", "tag": "Helping-others"}
        ]
    },

    # ===== PERSONALITY & WORK STYLE =====
    {
        "question": "How do you prefer to work on important tasks?",
        "category": "Work Style",
        "options": [
            {"text": "Working alone where I can focus deeply without distractions", "tag": "Independent"},
            {"text": "Working with a team, bouncing ideas off each other", "tag": "Collaborative"},
            {"text": "Leading a group and coordinating everyone's efforts", "tag": "Leading-teams"},
            {"text": "Working alongside one or two close collaborators", "tag": "Collaborative"}
        ]
    },
    {
        "question": "During your free time, you tend to:",
        "category": "Social Preference",
        "options": [
            {"text": "Hang out with groups of friends, attend gatherings or events", "tag": "Extroverted"},
            {"text": "Spend time with a few close friends in quiet settings", "tag": "Introverted"},
            {"text": "Work on personal hobbies and projects by yourself", "tag": "Independent"},
            {"text": "Join clubs or organizations for group activities", "tag": "Collaborative"}
        ]
    },
    {
        "question": "When starting a new project, do you prefer to:",
        "category": "Planning Style",
        "options": [
            {"text": "Plan every detail carefully before starting", "tag": "Detail-focused"},
            {"text": "Focus on the overall vision and adapt details as you go", "tag": "Big-picture"},
            {"text": "Jump in immediately and learn by doing", "tag": "Hands-on"},
            {"text": "Research thoroughly before taking action", "tag": "Research-oriented"}
        ]
    },
    {
        "question": "Which statement best describes your approach to tasks?",
        "category": "Task Approach",
        "options": [
            {"text": "I focus on accuracy and getting every detail right", "tag": "Detail-focused"},
            {"text": "I think about the overall impact and long-term goals", "tag": "Big-picture"},
            {"text": "I prefer systematic, methodical approaches", "tag": "Methodical"},
            {"text": "I like creative and flexible approaches", "tag": "Innovative"}
        ]
    },
    {
        "question": "In social situations, you usually:",
        "category": "Social Energy",
        "options": [
            {"text": "Feel energized and enjoy meeting new people", "tag": "Extroverted"},
            {"text": "Prefer listening and observing before contributing", "tag": "Introverted"},
            {"text": "Take charge and facilitate conversations", "tag": "Leading-teams"},
            {"text": "Feel comfortable but prefer smaller groups", "tag": "Collaborative"}
        ]
    },

    # ===== LEARNING STYLE PREFERENCES =====
    {
        "question": "How do you learn best?",
        "category": "Learning Style",
        "options": [
            {"text": "By doing experiments, building things, or practicing skills", "tag": "Hands-on"},
            {"text": "By reading, studying theories, and understanding concepts", "tag": "Theoretical"},
            {"text": "By watching demonstrations, videos, or looking at diagrams", "tag": "Visual-learner"},
            {"text": "By conducting research and analyzing information", "tag": "Research-oriented"}
        ]
    },
    {
        "question": "Which school activities do you enjoy most?",
        "category": "Activity Preference",
        "options": [
            {"text": "Laboratory experiments, workshops, or practical exercises", "tag": "Hands-on"},
            {"text": "Lectures, seminars, and theoretical discussions", "tag": "Theoretical"},
            {"text": "Art projects, presentations, or visual demonstrations", "tag": "Visual-learner"},
            {"text": "Research papers, case studies, and investigations", "tag": "Research-oriented"}
        ]
    },
    {
        "question": "When studying for an exam, you prefer to:",
        "category": "Study Method",
        "options": [
            {"text": "Practice problems repeatedly until mastery", "tag": "Hands-on"},
            {"text": "Read and understand the underlying principles", "tag": "Theoretical"},
            {"text": "Create diagrams, mind maps, or visual summaries", "tag": "Visual-learner"},
            {"text": "Look up multiple sources and synthesize information", "tag": "Research-oriented"}
        ]
    },

    # ===== WORK ENVIRONMENT PREFERENCES =====
    {
        "question": "What kind of work environment appeals to you most?",
        "category": "Work Environment",
        "options": [
            {"text": "Modern office with computers and technology", "tag": "Office-based"},
            {"text": "Outdoors - construction sites, farms, forests, or sea", "tag": "Field-work"},
            {"text": "Laboratory with scientific equipment and experiments", "tag": "Laboratory"},
            {"text": "Clinical settings like hospitals or health centers", "tag": "Clinical-setting"}
        ]
    },
    {
        "question": "For your ideal future job, you prefer working:",
        "category": "Location Preference",
        "options": [
            {"text": "In a comfortable office with air conditioning", "tag": "Office-based"},
            {"text": "In various locations, moving around frequently", "tag": "Field-work"},
            {"text": "From home or remotely using technology", "tag": "Remote-friendly"},
            {"text": "In specialized facilities like studios or labs", "tag": "Laboratory"}
        ]
    },
    {
        "question": "Would you enjoy a career that involves spending time outdoors?",
        "category": "Outdoor Preference",
        "options": [
            {"text": "Yes, I love being outdoors and would prefer it", "tag": "Outdoor-enthusiast"},
            {"text": "Sometimes, I enjoy a mix of indoor and outdoor work", "tag": "Field-work"},
            {"text": "No, I prefer working in controlled indoor environments", "tag": "Office-based"},
            {"text": "I prefer specialized indoor facilities like studios", "tag": "Studio-work"}
        ]
    },

    # ===== CAREER INTEREST & APTITUDE =====
    {
        "question": "Which field interests you the most?",
        "category": "Field Interest",
        "options": [
            {"text": "Technology, computers, and software development", "tag": "Tech-savvy"},
            {"text": "Healthcare, medicine, and helping patients", "tag": "Patient-focused"},
            {"text": "Business, finance, and entrepreneurship", "tag": "Business-minded"},
            {"text": "Arts, design, and creative production", "tag": "Creative-expression"}
        ]
    },
    {
        "question": "What type of problems do you enjoy solving?",
        "category": "Problem Type",
        "options": [
            {"text": "Mathematical equations and logical puzzles", "tag": "Logical"},
            {"text": "Technical issues with gadgets or systems", "tag": "Problem-solving"},
            {"text": "People's problems and conflicts", "tag": "Empathetic"},
            {"text": "Design challenges and aesthetic improvements", "tag": "Visual-learner"}
        ]
    },
    {
        "question": "Which of these activities sounds most appealing?",
        "category": "Activity Appeal",
        "options": [
            {"text": "Writing code or developing apps", "tag": "Algorithm-focused"},
            {"text": "Taking care of sick people or animals", "tag": "Patient-focused"},
            {"text": "Managing budgets and financial planning", "tag": "Analytical"},
            {"text": "Designing graphics or creating art", "tag": "Visual-learner"}
        ]
    },
    {
        "question": "Are you comfortable working with numbers and data?",
        "category": "Numerical Aptitude",
        "options": [
            {"text": "Yes, I love working with numbers and statistics", "tag": "Quantitative"},
            {"text": "I can handle it when needed", "tag": "Analytical"},
            {"text": "I prefer working with words and ideas", "tag": "Articulate"},
            {"text": "I prefer working with visuals and designs", "tag": "Visual-learner"}
        ]
    },

    # ===== SPECIFIC INTEREST AREAS =====
    {
        "question": "Which statement resonates with you most?",
        "category": "Career Vision",
        "options": [
            {"text": "I want to create innovative solutions using technology", "tag": "Innovative"},
            {"text": "I want to help people improve their health and wellbeing", "tag": "Helping-others"},
            {"text": "I want to start my own business or lead organizations", "tag": "Ambitious"},
            {"text": "I want to create beautiful and meaningful art or designs", "tag": "Artistic-passion"}
        ]
    },
    {
        "question": "What motivates you most in a potential career?",
        "category": "Career Motivation",
        "options": [
            {"text": "Solving challenging technical problems", "tag": "Problem-solving"},
            {"text": "Making a difference in people's lives", "tag": "Helping-others"},
            {"text": "Financial success and business growth", "tag": "Business-minded"},
            {"text": "Expressing creativity and originality", "tag": "Creative-expression"}
        ]
    },
    {
        "question": "Do you enjoy working with your hands and building things?",
        "category": "Manual Skills",
        "options": [
            {"text": "Yes, I love hands-on mechanical or construction work", "tag": "Hands-on"},
            {"text": "I prefer working with technology and digital tools", "tag": "Tech-savvy"},
            {"text": "I prefer working with my mind on abstract concepts", "tag": "Theoretical"},
            {"text": "I prefer creative hands-on work like art or crafts", "tag": "Creative-expression"}
        ]
    },

    # ===== SITUATIONAL QUESTIONS =====
    {
        "question": "Your school is organizing a science fair. What would you prefer to do?",
        "category": "Project Role",
        "options": [
            {"text": "Build a working prototype or conduct experiments", "tag": "Hands-on"},
            {"text": "Research and present theoretical findings", "tag": "Research-oriented"},
            {"text": "Design the booth display and create visual presentations", "tag": "Visual-learner"},
            {"text": "Coordinate the team and manage the project", "tag": "Leading-teams"}
        ]
    },
    {
        "question": "During intramurals, you would most likely:",
        "category": "Sports Event",
        "options": [
            {"text": "Participate actively in sports competitions", "tag": "Active"},
            {"text": "Help organize and manage the events", "tag": "Leading-teams"},
            {"text": "Design posters and document through photos/videos", "tag": "Creative-expression"},
            {"text": "Cheer and support classmates from the sidelines", "tag": "Collaborative"}
        ]
    },
    {
        "question": "If you see a classmate struggling with a subject, you would:",
        "category": "Helping Behavior",
        "options": [
            {"text": "Offer to tutor them and explain concepts patiently", "tag": "Helping-others"},
            {"text": "Share your notes and study materials with them", "tag": "Collaborative"},
            {"text": "Connect them with someone more knowledgeable", "tag": "Social"},
            {"text": "Focus on your own studies; they should ask the teacher", "tag": "Independent"}
        ]
    },
    {
        "question": "Your family is planning a vacation. How do you contribute?",
        "category": "Planning Role",
        "options": [
            {"text": "Research destinations, costs, and create detailed itineraries", "tag": "Detail-focused"},
            {"text": "Suggest the overall vision and key attractions to visit", "tag": "Big-picture"},
            {"text": "Take charge of booking and coordinating everything", "tag": "Leading-teams"},
            {"text": "Go with whatever the family decides", "tag": "Collaborative"}
        ]
    },
    {
        "question": "You discover a stray dog in your neighborhood. What would you do?",
        "category": "Compassion Test",
        "options": [
            {"text": "Take it to a vet and try to help it recover", "tag": "Animal-care"},
            {"text": "Organize neighbors to find its owner or a shelter", "tag": "Leading-teams"},
            {"text": "Feed it and provide temporary care", "tag": "Empathetic"},
            {"text": "Report it to local animal control", "tag": "Systematic"}
        ]
    },

    # ===== ACADEMIC SUBJECT PREFERENCES =====
    {
        "question": "Which subject do you find most interesting?",
        "category": "Subject Interest",
        "options": [
            {"text": "Mathematics and Physics", "tag": "Logical"},
            {"text": "Biology and Chemistry", "tag": "Scientific-thinking"},
            {"text": "Filipino, English, and Social Sciences", "tag": "Articulate"},
            {"text": "Arts, Music, and Creative subjects", "tag": "Creative-expression"}
        ]
    },
    {
        "question": "In Science class, which topics excite you most?",
        "category": "Science Interest",
        "options": [
            {"text": "How things work - mechanics, electricity, forces", "tag": "Technical"},
            {"text": "Living organisms - cells, genetics, ecosystems", "tag": "Biological"},
            {"text": "Chemical reactions and molecular structures", "tag": "Molecular-focus"},
            {"text": "Space, earth science, and natural phenomena", "tag": "Scientific-thinking"}
        ]
    },
    {
        "question": "What type of reading materials do you prefer?",
        "category": "Reading Preference",
        "options": [
            {"text": "Technical manuals, how-to guides, or tutorials", "tag": "Hands-on"},
            {"text": "Scientific journals and research articles", "tag": "Research-oriented"},
            {"text": "Stories, novels, and creative literature", "tag": "Creative-expression"},
            {"text": "News, current events, and opinion pieces", "tag": "Inquisitive"}
        ]
    },
    {
        "question": "Which extracurricular activity appeals to you?",
        "category": "Extracurricular",
        "options": [
            {"text": "Robotics club, computer club, or science club", "tag": "Tech-savvy"},
            {"text": "Theater, art club, or school publication", "tag": "Creative-expression"},
            {"text": "Student government or community service", "tag": "Leadership"},
            {"text": "Sports teams or dance troupe", "tag": "Active"}
        ]
    },

    # ===== WORK VALUES & PREFERENCES =====
    {
        "question": "What matters most to you in a future career?",
        "category": "Career Values",
        "options": [
            {"text": "Job security and stable income", "tag": "Practical"},
            {"text": "Making a positive impact on society", "tag": "Advocacy"},
            {"text": "Opportunities for creativity and innovation", "tag": "Innovative"},
            {"text": "Prestige and professional recognition", "tag": "Ambitious"}
        ]
    },
    {
        "question": "How do you feel about taking risks?",
        "category": "Risk Tolerance",
        "options": [
            {"text": "I'm comfortable taking calculated risks for rewards", "tag": "Risk-taking"},
            {"text": "I prefer safe, predictable paths", "tag": "Methodical"},
            {"text": "I'll take risks if I've researched thoroughly", "tag": "Analytical"},
            {"text": "I'm adventurous and embrace uncertainty", "tag": "Adventurous"}
        ]
    },
    {
        "question": "Would you enjoy a job that requires constant learning and adaptation?",
        "category": "Adaptability",
        "options": [
            {"text": "Yes, I love learning new things and facing new challenges", "tag": "Innovative"},
            {"text": "I prefer mastering one area deeply", "tag": "Detail-focused"},
            {"text": "I enjoy learning within my field of expertise", "tag": "Research-oriented"},
            {"text": "I prefer established routines and procedures", "tag": "Methodical"}
        ]
    },

    # ===== COMMUNICATION & INTERACTION =====
    {
        "question": "How comfortable are you speaking in front of large groups?",
        "category": "Public Speaking",
        "options": [
            {"text": "Very comfortable, I enjoy presenting to audiences", "tag": "Extroverted"},
            {"text": "I can do it but prefer smaller audiences", "tag": "Collaborative"},
            {"text": "I find it stressful and prefer written communication", "tag": "Introverted"},
            {"text": "I'm confident when presenting topics I'm passionate about", "tag": "Articulate"}
        ]
    },
    {
        "question": "In a debate or discussion, you tend to:",
        "category": "Discussion Style",
        "options": [
            {"text": "Actively argue your points with confidence", "tag": "Argumentative"},
            {"text": "Listen carefully and provide thoughtful input", "tag": "Analytical"},
            {"text": "Try to find middle ground and consensus", "tag": "Empathetic"},
            {"text": "Prefer observing unless you have strong expertise", "tag": "Contemplative"}
        ]
    },

    # ===== DECISION MAKING & ETHICS =====
    {
        "question": "When making important decisions, you rely most on:",
        "category": "Decision Making",
        "options": [
            {"text": "Logic, facts, and objective analysis", "tag": "Logical"},
            {"text": "How it will affect people emotionally", "tag": "Empathetic"},
            {"text": "Practical outcomes and real-world impact", "tag": "Practical"},
            {"text": "Your intuition and personal values", "tag": "Contemplative"}
        ]
    },
    {
        "question": "If you witness someone cheating on an exam, what would you do?",
        "category": "Ethics",
        "options": [
            {"text": "Report it immediately to maintain academic integrity", "tag": "Ethical"},
            {"text": "Talk to the person privately first", "tag": "Empathetic"},
            {"text": "Mind my own business; it's not my responsibility", "tag": "Independent"},
            {"text": "Discuss with classmates to decide collectively", "tag": "Collaborative"}
        ]
    },

    # ===== TECHNICAL & CREATIVE APTITUDE =====
    {
        "question": "How do you feel about coding or programming?",
        "category": "Coding Interest",
        "options": [
            {"text": "I love it or want to learn more about it", "tag": "Algorithm-focused"},
            {"text": "It's useful but not my primary interest", "tag": "Tech-savvy"},
            {"text": "I find it too technical; I prefer other skills", "tag": "Creative-expression"},
            {"text": "I've never tried it", "tag": "None"}
        ]
    },
    {
        "question": "Do you enjoy drawing, painting, or other visual arts?",
        "category": "Visual Arts",
        "options": [
            {"text": "Yes, it's one of my favorite activities", "tag": "Artistic-passion"},
            {"text": "I appreciate it but prefer digital design", "tag": "Digital-art"},
            {"text": "I'm more interested in technical drawing/drafting", "tag": "Technical"},
            {"text": "Not really, I prefer other activities", "tag": "None"}
        ]
    },
    {
        "question": "Are you interested in how the human body and health work?",
        "category": "Health Interest",
        "options": [
            {"text": "Yes, I'm fascinated by medicine and healthcare", "tag": "Patient-focused"},
            {"text": "Yes, from a scientific research perspective", "tag": "Research-oriented"},
            {"text": "Somewhat, but more interested in mental health", "tag": "Empathetic"},
            {"text": "Not particularly interested", "tag": "None"}
        ]
    },

    # ===== FUTURE CAREER SCENARIOS =====
    {
        "question": "Imagine your ideal workday. Which sounds most appealing?",
        "category": "Workday Vision",
        "options": [
            {"text": "Working on my computer solving technical challenges", "tag": "Tech-savvy"},
            {"text": "Interacting with clients, patients, or customers", "tag": "Service-oriented"},
            {"text": "Creating designs, content, or artistic works", "tag": "Creative-expression"},
            {"text": "Managing projects and leading team meetings", "tag": "Leading-teams"}
        ]
    },
    {
        "question": "If money wasn't an issue, which career path sounds most fulfilling?",
        "category": "True Calling",
        "options": [
            {"text": "Inventing new technology or scientific discoveries", "tag": "Innovative"},
            {"text": "Helping disadvantaged people or communities", "tag": "Advocacy"},
            {"text": "Creating art, music, films, or entertainment", "tag": "Artistic-passion"},
            {"text": "Building successful businesses or organizations", "tag": "Ambitious"}
        ]
    },
    {
        "question": "Which work schedule would you prefer?",
        "category": "Schedule Preference",
        "options": [
            {"text": "Regular 9-5 office hours with weekends off", "tag": "Office-based"},
            {"text": "Flexible hours working from anywhere", "tag": "Remote-friendly"},
            {"text": "Shift work in hospitals, emergencies, or operations", "tag": "Clinical-setting"},
            {"text": "Project-based with varying schedules", "tag": "Field-work"}
        ]
    },

    # ===== SOCIAL IMPACT & VALUES =====
    {
        "question": "Which cause are you most passionate about?",
        "category": "Social Cause",
        "options": [
            {"text": "Environmental conservation and sustainability", "tag": "Conservation-minded"},
            {"text": "Healthcare access and medical advancement", "tag": "Helping-others"},
            {"text": "Education and youth development", "tag": "Mentoring"},
            {"text": "Technology innovation for social good", "tag": "Innovative"}
        ]
    },
    {
        "question": "How important is work-life balance to you?",
        "category": "Life Balance",
        "options": [
            {"text": "Very important, I need clear boundaries", "tag": "Practical"},
            {"text": "Somewhat important, depends on the passion", "tag": "Ambitious"},
            {"text": "I'd dedicate myself fully to meaningful work", "tag": "Resilient"},
            {"text": "I prefer flexible arrangements", "tag": "Remote-friendly"}
        ]
    },

    # ===== SPECIALIZED CAREER INTERESTS =====
    {
        "question": "Are you interested in working directly with patients or people needing care?",
        "category": "Healthcare Interest",
        "options": [
            {"text": "Yes, I want to work directly with patients in healthcare", "tag": "Patient-focused"},
            {"text": "I prefer healthcare from a research/technical angle", "tag": "Clinical-setting"},
            {"text": "I'm interested in health but prefer wellness/nutrition", "tag": "Health-conscious"},
            {"text": "Not interested in healthcare fields", "tag": "None"}
        ]
    },
    {
        "question": "How do you feel about working with machines and mechanical systems?",
        "category": "Mechanical Interest",
        "options": [
            {"text": "I love understanding how machines work", "tag": "Mechanical-minded"},
            {"text": "I prefer designing structural systems", "tag": "Structural-thinking"},
            {"text": "I prefer electronic circuits and systems", "tag": "Circuit-design"},
            {"text": "I'm more interested in software than hardware", "tag": "Algorithm-focused"}
        ]
    },
    {
        "question": "Would you enjoy a career at sea or in maritime industries?",
        "category": "Maritime Interest",
        "options": [
            {"text": "Yes, I'm drawn to seafaring and navigation", "tag": "Sea-passion"},
            {"text": "I prefer land-based outdoor work", "tag": "Field-work"},
            {"text": "I prefer working indoors", "tag": "Office-based"},
            {"text": "Not interested in maritime work", "tag": "None"}
        ]
    },
    {
        "question": "Are you interested in agriculture, farming, or working with plants?",
        "category": "Agriculture Interest",
        "options": [
            {"text": "Yes, I'm interested in farming and crop production", "tag": "Farming-passion"},
            {"text": "I prefer forestry and environmental conservation", "tag": "Environmental-passion"},
            {"text": "I prefer studying plants from a scientific angle", "tag": "Nature-focused"},
            {"text": "Not interested in agriculture", "tag": "None"}
        ]
    },
    {
        "question": "Do you enjoy caring for animals?",
        "category": "Animal Interest",
        "options": [
            {"text": "Yes, I love animals and want to care for them", "tag": "Animal-care"},
            {"text": "I'm interested in marine life and aquatic animals", "tag": "Aquatic-passion"},
            {"text": "I prefer observing wildlife in nature", "tag": "Nature-focused"},
            {"text": "Not particularly interested in animals", "tag": "None"}
        ]
    },
    {
        "question": "Are you interested in aviation, aircraft, or aerospace?",
        "category": "Aviation Interest",
        "options": [
            {"text": "Yes, I'm fascinated by aircraft and flying", "tag": "Aviation-passion"},
            {"text": "I'm interested in space and aerospace engineering", "tag": "Aerospace-passion"},
            {"text": "I prefer ground transportation systems", "tag": "Technical"},
            {"text": "Not interested in aviation", "tag": "None"}
        ]
    },
    {
        "question": "How comfortable are you with abstract mathematical concepts?",
        "category": "Math Comfort",
        "options": [
            {"text": "Very comfortable, I enjoy theoretical mathematics", "tag": "Abstract-thinking"},
            {"text": "I prefer applied math with practical uses", "tag": "Quantitative"},
            {"text": "I can handle it but prefer other subjects", "tag": "Logical"},
            {"text": "I struggle with advanced mathematics", "tag": "None"}
        ]
    },
    {
        "question": "Are you interested in how societies, governments, and policies work?",
        "category": "Governance Interest",
        "options": [
            {"text": "Yes, I'm interested in politics and public service", "tag": "Governance-focus"},
            {"text": "I'm interested in law and legal systems", "tag": "Law-oriented"},
            {"text": "I'm interested in social change and advocacy", "tag": "Advocacy"},
            {"text": "Not particularly interested", "tag": "None"}
        ]
    },
    {
        "question": "Do you enjoy performing or being on stage?",
        "category": "Performance Interest",
        "options": [
            {"text": "Yes, I love performing in front of audiences", "tag": "Performative"},
            {"text": "I prefer behind-the-scenes creative work", "tag": "Creative-expression"},
            {"text": "I'm comfortable presenting but not performing", "tag": "Articulate"},
            {"text": "I prefer to avoid the spotlight", "tag": "Introverted"}
        ]
    },
    {
        "question": "Are you interested in creating music or working with sound?",
        "category": "Music Interest",
        "options": [
            {"text": "Yes, I'm passionate about music creation", "tag": "Auditory-skills"},
            {"text": "I appreciate music but prefer visual arts", "tag": "Visual-learner"},
            {"text": "I'm interested in music from a technical angle", "tag": "Tech-savvy"},
            {"text": "Not particularly interested in music", "tag": "None"}
        ]
    },
    {
        "question": "How do you feel about teaching or training others?",
        "category": "Teaching Interest",
        "options": [
            {"text": "I love helping others learn and grow", "tag": "Mentoring"},
            {"text": "I enjoy coaching in sports or physical activities", "tag": "Coaching"},
            {"text": "I prefer supporting roles rather than leading", "tag": "Collaborative"},
            {"text": "I prefer working independently", "tag": "Independent"}
        ]
    },
    {
        "question": "Are you interested in children and child development?",
        "category": "Child Interest",
        "options": [
            {"text": "Yes, I love working with young children", "tag": "Child-focused"},
            {"text": "I prefer working with teenagers", "tag": "Mentoring"},
            {"text": "I prefer working with adults", "tag": "Professional"},
            {"text": "Not particularly interested in education", "tag": "None"}
        ]
    },
    {
        "question": "Do you have an eye for aesthetics, design, and visual appeal?",
        "category": "Aesthetic Sense",
        "options": [
            {"text": "Yes, I'm very detail-oriented about visual design", "tag": "Aesthetic-sense"},
            {"text": "I appreciate good design but focus on function", "tag": "Practical"},
            {"text": "I prefer technical precision over aesthetics", "tag": "Precision-oriented"},
            {"text": "Not particularly concerned with visual appeal", "tag": "None"}
        ]
    },
    {
        "question": "Are you comfortable working in high-pressure or emergency situations?",
        "category": "Pressure Handling",
        "options": [
            {"text": "Yes, I thrive under pressure and in crises", "tag": "Crisis-management"},
            {"text": "I can handle it but prefer steady environments", "tag": "Resilient"},
            {"text": "I prefer calm, predictable work settings", "tag": "Methodical"},
            {"text": "I avoid high-stress situations", "tag": "None"}
        ]
    },
    {
        "question": "Are you interested in food science, nutrition, or culinary arts?",
        "category": "Food Interest",
        "options": [
            {"text": "Yes, I love cooking and culinary creativity", "tag": "Culinary-passion"},
            {"text": "I'm interested in nutrition and health", "tag": "Health-conscious"},
            {"text": "I'm interested in food from a scientific angle", "tag": "Food-science"},
            {"text": "Not particularly interested in food careers", "tag": "None"}
        ]
    },
    {
        "question": "How do you feel about detailed documentation and record-keeping?",
        "category": "Documentation",
        "options": [
            {"text": "I excel at maintaining detailed records", "tag": "Organized"},
            {"text": "I can do it but prefer other tasks", "tag": "Administrative-skills"},
            {"text": "I prefer big-picture work over details", "tag": "Big-picture"},
            {"text": "I find it tedious and prefer to avoid it", "tag": "None"}
        ]
    },
    {
        "question": "Are you interested in languages and how people communicate?",
        "category": "Language Interest",
        "options": [
            {"text": "Yes, I love learning languages and linguistics", "tag": "Language-passion"},
            {"text": "I'm interested in communication and media", "tag": "Communication-skills"},
            {"text": "I prefer non-verbal forms of expression", "tag": "Visual-learner"},
            {"text": "Not particularly interested in languages", "tag": "None"}
        ]
    },
    {
        "question": "Do you enjoy investigating mysteries or solving puzzles?",
        "category": "Investigation",
        "options": [
            {"text": "Yes, I love detective work and investigations", "tag": "Investigative"},
            {"text": "I enjoy research and uncovering facts", "tag": "Inquisitive"},
            {"text": "I prefer systematic problem-solving", "tag": "Analytical"},
            {"text": "Not particularly interested", "tag": "None"}
        ]
    },
    {
        "question": "Are you interested in earth sciences like geology or meteorology?",
        "category": "Earth Science",
        "options": [
            {"text": "Yes, I'm fascinated by earth's processes", "tag": "Earth-science"},
            {"text": "I'm interested in weather and climate", "tag": "Weather-passion"},
            {"text": "I prefer life sciences like biology", "tag": "Biological"},
            {"text": "Not particularly interested in earth sciences", "tag": "None"}
        ]
    },
    {
        "question": "How interested are you in business, entrepreneurship, and making money?",
        "category": "Business Acumen",
        "options": [
            {"text": "Very interested, I want to start my own business", "tag": "Ambitious"},
            {"text": "I'm interested in business management", "tag": "Business-minded"},
            {"text": "I prefer financial analysis and investment", "tag": "Investment-minded"},
            {"text": "Not interested in business careers", "tag": "None"}
        ]
    },
    {
        "question": "Do you enjoy sales, negotiation, and persuading others?",
        "category": "Sales Aptitude",
        "options": [
            {"text": "Yes, I'm good at persuading and negotiating", "tag": "Sales-oriented"},
            {"text": "I prefer marketing and strategy", "tag": "Strategic"},
            {"text": "I'm better at building relationships than selling", "tag": "Social"},
            {"text": "I prefer non-sales roles", "tag": "None"}
        ]
    },
    {
        "question": "Are you drawn to philosophy, ethics, and deep thinking?",
        "category": "Philosophical Interest",
        "options": [
            {"text": "Yes, I love contemplating life's big questions", "tag": "Contemplative"},
            {"text": "I'm interested in ethics and moral reasoning", "tag": "Ethical"},
            {"text": "I prefer practical over philosophical thinking", "tag": "Practical"},
            {"text": "Not particularly interested in philosophy", "tag": "None"}
        ]
    },
    {
        "question": "How do you feel about physical fitness and staying active?",
        "category": "Physical Activity",
        "options": [
            {"text": "Very important, I love sports and fitness", "tag": "Athletic-passion"},
            {"text": "I stay active but it's not my main focus", "tag": "Active"},
            {"text": "I prefer light activity", "tag": "Health-conscious"},
            {"text": "I'm not very physically active", "tag": "None"}
        ]
    },
    {
        "question": "Are you interested in digital media, game design, or entertainment?",
        "category": "Digital Entertainment",
        "options": [
            {"text": "Yes, I want to create games or digital entertainment", "tag": "World-building"},
            {"text": "I'm interested in digital art and animation", "tag": "Digital-art"},
            {"text": "I'm interested in storytelling and narratives", "tag": "Storytelling"},
            {"text": "Not interested in entertainment industry", "tag": "None"}
        ]
    },
    {
        "question": "How do you feel about routine, methodical work processes?",
        "category": "Routine Tolerance",
        "options": [
            {"text": "I thrive on routine and systematic approaches", "tag": "Systematic"},
            {"text": "I can handle routine but need some variety", "tag": "Adaptive"},
            {"text": "I prefer innovative and changing work", "tag": "Innovative"},
            {"text": "I dislike repetitive work", "tag": "Creative-expression"}
        ]
    },
    {
        "question": "Are you interested in sustainability and green technology?",
        "category": "Sustainability",
        "options": [
            {"text": "Yes, I'm passionate about environmental solutions", "tag": "Sustainability-minded"},
            {"text": "I'm interested in conservation", "tag": "Conservation-minded"},
            {"text": "Somewhat interested but not a priority", "tag": "Practical"},
            {"text": "Not particularly focused on environmental issues", "tag": "None"}
        ]
    },
    {
        "question": "In group projects, what role do you naturally take?",
        "category": "Team Dynamics",
        "options": [
            {"text": "Coordinating everyone's efforts and ensuring smooth collaboration", "tag": "Team-centric"},
            {"text": "Leading the strategy and making key decisions", "tag": "Leadership"},
            {"text": "Working independently on my assigned tasks", "tag": "Independent"},
            {"text": "Supporting others and helping where needed", "tag": "Collaborative"}
        ]
    },
    {
        "question": "How do you feel about tasks that require long-term dedication?",
        "category": "Patience Level",
        "options": [
            {"text": "I thrive on projects that take months or years to complete", "tag": "Patient"},
            {"text": "I prefer quick results and fast-paced work", "tag": "Active"},
            {"text": "I can handle both depending on the importance", "tag": "Adaptive"},
            {"text": "I like steady progress with clear milestones", "tag": "Methodical"}
        ]
    },
    {
        "question": "When someone is struggling, what's your first instinct?",
        "category": "Compassion Expression",
        "options": [
            {"text": "Offer emotional support and understanding", "tag": "Compassionate"},
            {"text": "Help solve their practical problems", "tag": "Helping-others"},
            {"text": "Listen actively without judgment", "tag": "Empathetic"},
            {"text": "Give advice based on logic", "tag": "Logical"}
        ]
    },
    {
        "question": "What do you notice most about your surroundings?",
        "category": "Observation Skills",
        "options": [
            {"text": "Small details and patterns that others miss", "tag": "Observational"},
            {"text": "How things work and their functions", "tag": "Analytical"},
            {"text": "The overall aesthetic and atmosphere", "tag": "Aesthetic-sense"},
            {"text": "People's emotions and social dynamics", "tag": "Empathetic"}
        ]
    },
    {
        "question": "How do you feel about spending time in natural environments?",
        "category": "Nature Connection",
        "options": [
            {"text": "It's essential for my wellbeing - I feel most alive outdoors", "tag": "Nature-connected"},
            {"text": "I enjoy outdoor activities and adventure", "tag": "Outdoor-enthusiast"},
            {"text": "I appreciate nature but prefer urban settings", "tag": "Office-based"},
            {"text": "I'm more focused on indoor hobbies", "tag": "Introverted"}
        ]
    },
    {
        "question": "When you need to convince someone of your idea, you:",
        "category": "Persuasion Style",
        "options": [
            {"text": "Use compelling arguments and influence their perspective", "tag": "Persuasive"},
            {"text": "Present data and logical evidence", "tag": "Analytical"},
            {"text": "Build relationships and find common ground", "tag": "Collaborative"},
            {"text": "Demonstrate through actions and results", "tag": "Practical"}
        ]
    },
    {
        "question": "Do you easily spot patterns in data, behavior, or systems?",
        "category": "Pattern Recognition",
        "options": [
            {"text": "Yes, I naturally see connections and recurring themes", "tag": "Pattern-recognition"},
            {"text": "I'm good at analyzing structured data", "tag": "Quantitative"},
            {"text": "I focus more on individual details than patterns", "tag": "Detail-focused"},
            {"text": "I see the big picture rather than specific patterns", "tag": "Big-picture"}
        ]
    },
    {
        "question": "How important is contributing to your community?",
        "category": "Community Engagement",
        "options": [
            {"text": "It's central to my life - I want to make a local impact", "tag": "Community-focused"},
            {"text": "I prefer helping people through my professional work", "tag": "Service-oriented"},
            {"text": "I care about broader social causes", "tag": "Advocacy"},
            {"text": "I focus on personal and family wellbeing first", "tag": "Independent"}
        ]
    },
    {
        "question": "How do you approach people from different cultural backgrounds?",
        "category": "Cultural Sensitivity",
        "options": [
            {"text": "I actively learn about and respect diverse perspectives", "tag": "Cultural-awareness"},
            {"text": "I adapt my communication to different audiences", "tag": "Adaptive"},
            {"text": "I treat everyone the same regardless of background", "tag": "Ethical"},
            {"text": "I'm curious and ask questions to understand", "tag": "Inquisitive"}
        ]
    },
    {
        "question": "When faced with limited resources, you:",
        "category": "Resourcefulness",
        "options": [
            {"text": "Find creative solutions and make the most of what's available", "tag": "Resourceful"},
            {"text": "Innovate new approaches", "tag": "Innovative"},
            {"text": "Plan carefully to optimize efficiency", "tag": "Strategic"},
            {"text": "Work harder with what you have", "tag": "Resilient"}
        ]
    },
    {
        "question": "How would you describe your work habits?",
        "category": "Discipline Assessment",
        "options": [
            {"text": "Highly structured with strict routines and self-control", "tag": "Disciplined"},
            {"text": "Organized with clear systems", "tag": "Organized"},
            {"text": "Methodical but flexible", "tag": "Methodical"},
            {"text": "Adaptable to changing needs", "tag": "Adaptive"}
        ]
    },
    {
        "question": "How do you feel about helping others grow and develop?",
        "category": "Nurturing Tendency",
        "options": [
            {"text": "I love guiding and caring for others' development", "tag": "Nurturing"},
            {"text": "I enjoy mentoring and teaching", "tag": "Mentoring"},
            {"text": "I prefer coaching toward specific goals", "tag": "Coaching"},
            {"text": "I support others but focus on my own growth", "tag": "Independent"}
        ]
    },
    {
        "question": "When evaluating information, you:",
        "category": "Critical Analysis",
        "options": [
            {"text": "Question assumptions and examine evidence critically", "tag": "Critical-thinking"},
            {"text": "Break down complex ideas systematically", "tag": "Analytical"},
            {"text": "Look for logical inconsistencies", "tag": "Logical"},
            {"text": "Investigate thoroughly before forming opinions", "tag": "Investigative"}
        ]
    },
    {
        "question": "What's your approach to new experiences?",
        "category": "Exploration Mindset",
        "options": [
            {"text": "I actively seek out novel experiences and discoveries", "tag": "Exploratory"},
            {"text": "I'm curious but prefer structured learning", "tag": "Inquisitive"},
            {"text": "I take calculated risks", "tag": "Risk-taking"},
            {"text": "I prefer familiar and proven approaches", "tag": "Methodical"}
        ]
    },
    {
        "question": "If working in healthcare, what aspect appeals most?",
        "category": "Healthcare Interaction",
        "options": [
            {"text": "Direct interaction and care with patients", "tag": "Patient-interaction"},
            {"text": "Focus on patient wellbeing and recovery", "tag": "Patient-focused"},
            {"text": "Medical research and laboratory work", "tag": "Laboratory"},
            {"text": "Health policy and system improvement", "tag": "Governance-focus"}
        ]
    },
    {
        "question": "How do you make important decisions?",
        "category": "Data Orientation",
        "options": [
            {"text": "Based on data analysis and evidence", "tag": "Data-driven"},
            {"text": "Using numbers and statistical reasoning", "tag": "Quantitative"},
            {"text": "Through logical reasoning", "tag": "Logical"},
            {"text": "Combining data with intuition", "tag": "Strategic"}
        ]
    },
    {
        "question": "How comfortable are you working directly with clients?",
        "category": "Client Relations",
        "options": [
            {"text": "I thrive on building client relationships", "tag": "Client-interaction"},
            {"text": "I enjoy social interaction in professional settings", "tag": "Extroverted"},
            {"text": "I prefer collaborative team environments", "tag": "Collaborative"},
            {"text": "I work better behind the scenes", "tag": "Independent"}
        ]
    },
    {
        "question": "How important is physical fitness to you?",
        "category": "Physical Wellness",
        "options": [
            {"text": "It's a core part of my lifestyle and identity", "tag": "Physical-fitness"},
            {"text": "I'm active and enjoy sports", "tag": "Athletic-passion"},
            {"text": "I maintain basic health but it's not a focus", "tag": "Health-conscious"},
            {"text": "I prioritize mental over physical activities", "tag": "Contemplative"}
        ]
    }
]