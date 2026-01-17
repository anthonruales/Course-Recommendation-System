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
    },
    {
        "question": "Your group project deadline is tomorrow, but a teammate just quit. What do you do?",
        "category": "Crisis Management",
        "options": [
            {"text": "Take charge and reorganize the work to ensure completion", "tag": "Leading-teams"},
            {"text": "Help redistribute tasks fairly among remaining members", "tag": "Collaborative"},
            {"text": "Focus on completing your own portion excellently", "tag": "Independent"},
            {"text": "Support whoever is most stressed by the situation", "tag": "Empathetic"}
        ]
    },
    {
        "question": "You discover a cheaper and more efficient way to solve a workplace problem. Do you:",
        "category": "Innovation Initiative",
        "options": [
            {"text": "Immediately propose it to management with detailed analysis", "tag": "Problem-solving"},
            {"text": "Test it thoroughly before presenting", "tag": "Methodical"},
            {"text": "Share the idea with your team first for feedback", "tag": "Collaborative"},
            {"text": "Implement it quietly if it doesn't break any rules", "tag": "Innovative"}
        ]
    },
    {
        "question": "A client is unhappy with your work. How do you respond?",
        "category": "Client Conflict",
        "options": [
            {"text": "Listen carefully, understand their concerns, and apologize sincerely", "tag": "Empathetic"},
            {"text": "Analyze what went wrong and propose concrete solutions", "tag": "Problem-solving"},
            {"text": "Ask for specific feedback to improve your work", "tag": "Detail-focused"},
            {"text": "Involve your supervisor to mediate and resolve", "tag": "Collaborative"}
        ]
    },
    {
        "question": "You're offered a promotion that requires relocating far from family. Do you:",
        "category": "Life Decision",
        "options": [
            {"text": "Accept immediately - career advancement is top priority", "tag": "Ambitious"},
            {"text": "Decline - family and relationships come first", "tag": "Contemplative"},
            {"text": "Negotiate for remote work or delayed start", "tag": "Strategic"},
            {"text": "Ask family for their input before deciding", "tag": "Collaborative"}
        ]
    },
    {
        "question": "You notice a coworker struggling with their mental health. What do you do?",
        "category": "Workplace Compassion",
        "options": [
            {"text": "Reach out privately and offer to listen or help", "tag": "Empathetic"},
            {"text": "Connect them with HR or counseling resources", "tag": "Helping-others"},
            {"text": "Give them space but show you're available", "tag": "Respectful"},
            {"text": "Mind my business; it's not my responsibility", "tag": "Independent"}
        ]
    },
    {
        "question": "You're working on a complex project and hit a major obstacle. Do you:",
        "category": "Problem Resolution",
        "options": [
            {"text": "Break it down into smaller parts and tackle systematically", "tag": "Analytical"},
            {"text": "Brainstorm creative workarounds", "tag": "Innovative"},
            {"text": "Research solutions and study similar cases", "tag": "Research-oriented"},
            {"text": "Ask for help from colleagues or experts", "tag": "Collaborative"}
        ]
    },
    {
        "question": "You're asked to work on a project outside your expertise. Do you:",
        "category": "Skill Development",
        "options": [
            {"text": "Enthusiastically accept and learn as you go", "tag": "Adventurous"},
            {"text": "Ask for training or mentoring first", "tag": "Mentoring"},
            {"text": "Decline politely and stick to your strengths", "tag": "Practical"},
            {"text": "Accept but set a realistic timeline for learning", "tag": "Methodical"}
        ]
    },
    {
        "question": "During a meeting, you realize the proposed plan has a flaw. Do you:",
        "category": "Speaking Up",
        "options": [
            {"text": "Raise your hand immediately and point out the issue", "tag": "Confident"},
            {"text": "Wait until after to discuss with the leader privately", "tag": "Diplomatic"},
            {"text": "Speak up if asked directly; otherwise stay quiet", "tag": "Introverted"},
            {"text": "Suggest a constructive alternative politely", "tag": "Collaborative"}
        ]
    },
    {
        "question": "A project requires you to work nights and weekends. Do you:",
        "category": "Work Commitment",
        "options": [
            {"text": "Agree willingly - I love being absorbed in work", "tag": "Ambitious"},
            {"text": "Negotiate for flexible hours or additional support", "tag": "Practical"},
            {"text": "Do it if it's temporary and important", "tag": "Resilient"},
            {"text": "Decline - I need work-life balance", "tag": "Health-conscious"}
        ]
    },
    {
        "question": "You receive critical feedback that stings. How do you handle it?",
        "category": "Feedback Response",
        "options": [
            {"text": "Thank them and immediately implement improvements", "tag": "Growth-minded"},
            {"text": "Ask clarifying questions to understand fully", "tag": "Inquisitive"},
            {"text": "Feel hurt initially but eventually see the value", "tag": "Resilient"},
            {"text": "Defend my position if I believe I was right", "tag": "Confident"}
        ]
    },
    {
        "question": "You're in a team where people constantly conflict. Do you:",
        "category": "Team Dynamics",
        "options": [
            {"text": "Try to mediate and find common ground", "tag": "Empathetic"},
            {"text": "Address the issues directly with the team", "tag": "Leading-teams"},
            {"text": "Focus on my work and stay neutral", "tag": "Independent"},
            {"text": "Suggest team-building activities to improve relationships", "tag": "Collaborative"}
        ]
    },
    {
        "question": "You have an ethical concern about a company practice. Do you:",
        "category": "Ethics in Action",
        "options": [
            {"text": "Report it to the appropriate authority immediately", "tag": "Ethical"},
            {"text": "Discuss it with leadership to understand the rationale", "tag": "Analytical"},
            {"text": "Speak with colleagues to see if others share concerns", "tag": "Collaborative"},
            {"text": "Leave the company if it conflicts with my values", "tag": "Principled"}
        ]
    },
    {
        "question": "You're offered a high-paying job with unethical practices vs. lower-paying ethical job. You choose:",
        "category": "Values Priority",
        "options": [
            {"text": "The ethical job - my values are more important than money", "tag": "Ethical"},
            {"text": "The high-paying job - I'll influence change from within", "tag": "Strategic"},
            {"text": "Negotiate with the ethical company for better pay", "tag": "Practical"},
            {"text": "The ethical job - I'd struggle mentally with dishonesty", "tag": "Contemplative"}
        ]
    },
    {
        "question": "A team member takes credit for your work. Do you:",
        "category": "Professional Boundaries",
        "options": [
            {"text": "Confront them directly and clearly set boundaries", "tag": "Confident"},
            {"text": "Talk to my supervisor about the situation", "tag": "Professional"},
            {"text": "Gather evidence and present facts calmly", "tag": "Analytical"},
            {"text": "Document everything and prepare for future disputes", "tag": "Methodical"}
        ]
    },
    {
        "question": "How do you typically spend your free time?",
        "category": "Leisure Preference",
        "options": [
            {"text": "Pursuing hobbies that challenge my creativity", "tag": "Creative-expression"},
            {"text": "Learning new skills or diving into research", "tag": "Research-oriented"},
            {"text": "Engaging in physical activities or sports", "tag": "Active"},
            {"text": "Socializing with friends and attending events", "tag": "Extroverted"}
        ]
    },
    {
        "question": "When faced with failure, you typically:",
        "category": "Resilience",
        "options": [
            {"text": "Analyze what went wrong and try again with improvements", "tag": "Analytical"},
            {"text": "Feel discouraged but eventually bounce back", "tag": "Resilient"},
            {"text": "View it as a learning opportunity immediately", "tag": "Growth-minded"},
            {"text": "Seek support from others to move forward", "tag": "Collaborative"}
        ]
    },
    {
        "question": "What kind of people do you enjoy being around most?",
        "category": "Social Preference",
        "options": [
            {"text": "Ambitious, driven people with clear goals", "tag": "Ambitious"},
            {"text": "Empathetic, understanding people who listen well", "tag": "Empathetic"},
            {"text": "Creative, innovative people with unique perspectives", "tag": "Innovative"},
            {"text": "Intelligent, analytical people who debate ideas", "tag": "Logical"}
        ]
    },
    {
        "question": "How do you prefer to receive recognition for your work?",
        "category": "Recognition Style",
        "options": [
            {"text": "Public acknowledgment in front of colleagues", "tag": "Confident"},
            {"text": "Private praise from my supervisor", "tag": "Introverted"},
            {"text": "Tangible rewards like bonuses or promotions", "tag": "Ambitious"},
            {"text": "Knowing that I made a meaningful impact", "tag": "Purpose-driven"}
        ]
    },
    {
        "question": "When learning something new, you prefer:",
        "category": "Learning Approach",
        "options": [
            {"text": "Hands-on practice and real-world application", "tag": "Hands-on"},
            {"text": "Structured lessons and clear instructions", "tag": "Methodical"},
            {"text": "Exploring independently at your own pace", "tag": "Independent"},
            {"text": "Group discussions and collaborative learning", "tag": "Collaborative"}
        ]
    },
    {
        "question": "How comfortable are you with ambiguity and uncertainty?",
        "category": "Certainty Tolerance",
        "options": [
            {"text": "Very comfortable - I enjoy navigating uncertainty", "tag": "Adventurous"},
            {"text": "I prefer clarity but can adapt when needed", "tag": "Adaptive"},
            {"text": "I need clear guidelines and expectations", "tag": "Methodical"},
            {"text": "I struggle without structure and clear direction", "tag": "Detail-focused"}
        ]
    },
    {
        "question": "What motivates you to excel in your work?",
        "category": "Motivation Source",
        "options": [
            {"text": "The desire to make a positive impact on others", "tag": "Purpose-driven"},
            {"text": "Financial rewards and career advancement", "tag": "Ambitious"},
            {"text": "The satisfaction of solving difficult problems", "tag": "Problem-solving"},
            {"text": "Recognition and respect from peers", "tag": "Confident"}
        ]
    },
    {
        "question": "How do you feel about competition?",
        "category": "Competitiveness",
        "options": [
            {"text": "I thrive on competition and love to win", "tag": "Competitive"},
            {"text": "I prefer collaboration over competition", "tag": "Collaborative"},
            {"text": "I'm competitive but maintain integrity", "tag": "Ethical"},
            {"text": "I avoid overly competitive environments", "tag": "Introverted"}
        ]
    },
    {
        "question": "How important is job satisfaction vs. job security to you?",
        "category": "Career Priority",
        "options": [
            {"text": "Satisfaction is paramount; I need meaningful work", "tag": "Purpose-driven"},
            {"text": "Security is more important; I need stability", "tag": "Practical"},
            {"text": "Both are equally important", "tag": "Balanced"},
            {"text": "Financial compensation is the priority", "tag": "Ambitious"}
        ]
    },
    {
        "question": "When working on a long-term project, do you:",
        "category": "Project Commitment",
        "options": [
            {"text": "Maintain enthusiasm from start to finish", "tag": "Resilient"},
            {"text": "Need regular motivation and check-ins", "tag": "Social"},
            {"text": "Break it into milestones to stay on track", "tag": "Systematic"},
            {"text": "Work intensely in bursts", "tag": "Adaptive"}
        ]
    },
    {
        "question": "How do you typically handle stress?",
        "category": "Stress Management",
        "options": [
            {"text": "Exercise, sports, or physical activity", "tag": "Active"},
            {"text": "Talk it through with friends or family", "tag": "Social"},
            {"text": "Focus on the problem and work through it", "tag": "Problem-solving"},
            {"text": "Creative outlets like art, music, or writing", "tag": "Creative-expression"}
        ]
    },
    {
        "question": "What does success mean to you?",
        "category": "Success Definition",
        "options": [
            {"text": "Achieving financial wealth and security", "tag": "Ambitious"},
            {"text": "Making a positive difference in others' lives", "tag": "Compassionate"},
            {"text": "Mastering my field and gaining expertise", "tag": "Expert-focused"},
            {"text": "Finding balance and enjoying life", "tag": "Health-conscious"}
        ]
    },
    {
        "question": "How do you approach continuous learning?",
        "category": "Learning Commitment",
        "options": [
            {"text": "I actively seek courses and certifications", "tag": "Growth-minded"},
            {"text": "I learn on the job as needed", "tag": "Practical"},
            {"text": "I prefer deep expertise in one area", "tag": "Detail-focused"},
            {"text": "I explore diverse topics out of curiosity", "tag": "Inquisitive"}
        ]
    },
    {
        "question": "In a disagreement with a colleague, you typically:",
        "category": "Conflict Resolution",
        "options": [
            {"text": "Stand firm on your position with evidence", "tag": "Confident"},
            {"text": "Listen to their perspective and find compromise", "tag": "Empathetic"},
            {"text": "Analyze both sides logically", "tag": "Analytical"},
            {"text": "Avoid confrontation if possible", "tag": "Introverted"}
        ]
    },
    {
        "question": "How important is work variety to you?",
        "category": "Task Variety",
        "options": [
            {"text": "Very important - I need diverse tasks", "tag": "Adaptive"},
            {"text": "I prefer mastering one skill deeply", "tag": "Expert-focused"},
            {"text": "Some variety but with consistency", "tag": "Balanced"},
            {"text": "Routine tasks help me focus", "tag": "Methodical"}
        ]
    },
    {
        "question": "How do you feel about taking responsibility?",
        "category": "Accountability",
        "options": [
            {"text": "I welcome it and take ownership gladly", "tag": "Confident"},
            {"text": "I'm willing but prefer shared responsibility", "tag": "Collaborative"},
            {"text": "I accept it when necessary", "tag": "Responsible"},
            {"text": "I prefer others to take the lead", "tag": "Introverted"}
        ]
    },
    {
        "question": "What role do you prefer in social situations?",
        "category": "Social Role",
        "options": [
            {"text": "The center of attention - I like being noticed", "tag": "Extroverted"},
            {"text": "An active participant but not leading", "tag": "Collaborative"},
            {"text": "An observer; I prefer listening to talking", "tag": "Introverted"},
            {"text": "It depends on the group and topic", "tag": "Adaptive"}
        ]
    },
    {
        "question": "How organized do you naturally tend to be?",
        "category": "Organization Level",
        "options": [
            {"text": "Very organized - systems and order are essential", "tag": "Organized"},
            {"text": "Moderately organized but flexible", "tag": "Systematic"},
            {"text": "Somewhat chaotic but functional", "tag": "Adaptive"},
            {"text": "I work best in creative chaos", "tag": "Innovative"}
        ]
    },
    {
        "question": "Which academic subject have you consistently excelled in?",
        "category": "Academic Strength",
        "options": [
            {"text": "Math, Physics, or Computer Science", "tag": "Logical"},
            {"text": "Chemistry, Biology, or Earth Sciences", "tag": "Scientific-thinking"},
            {"text": "English, Literature, or Languages", "tag": "Articulate"},
            {"text": "Social Sciences, History, or Humanities", "tag": "Analytical"}
        ]
    },
    {
        "question": "How do you typically prepare for major exams?",
        "category": "Exam Preparation",
        "options": [
            {"text": "Create detailed study guides and review regularly", "tag": "Methodical"},
            {"text": "Form study groups and teach others", "tag": "Collaborative"},
            {"text": "Do practice problems repeatedly", "tag": "Hands-on"},
            {"text": "Read extensively and understand concepts deeply", "tag": "Theoretical"}
        ]
    },
    {
        "question": "When reading assigned textbooks, you prefer:",
        "category": "Reading Style",
        "options": [
            {"text": "Taking detailed notes of key points", "tag": "Detail-focused"},
            {"text": "Skimming for main ideas and themes", "tag": "Big-picture"},
            {"text": "Highlighting and annotating as you read", "tag": "Visual-learner"},
            {"text": "Reading once thoroughly and remembering", "tag": "Focused"}
        ]
    },
    {
        "question": "Which type of assignment do you find most engaging?",
        "category": "Assignment Preference",
        "options": [
            {"text": "Research papers requiring investigation", "tag": "Research-oriented"},
            {"text": "Creative projects like presentations or art", "tag": "Creative-expression"},
            {"text": "Problem sets and calculations", "tag": "Logical"},
            {"text": "Group projects and discussions", "tag": "Collaborative"}
        ]
    },
    {
        "question": "How do you feel about class presentations?",
        "category": "Public Speaking Comfort",
        "options": [
            {"text": "I enjoy them and present confidently", "tag": "Extroverted"},
            {"text": "I'm nervous but manage well with preparation", "tag": "Methodical"},
            {"text": "I dislike them but do what's required", "tag": "Introverted"},
            {"text": "I excel at engaging audiences", "tag": "Articulate"}
        ]
    },
    {
        "question": "In lab or practical classes, you typically:",
        "category": "Practical Class Performance",
        "options": [
            {"text": "Follow procedures precisely and carefully", "tag": "Detail-focused"},
            {"text": "Experiment and adapt procedures creatively", "tag": "Innovative"},
            {"text": "Work methodically step by step", "tag": "Methodical"},
            {"text": "Collaborate with partners to solve problems", "tag": "Collaborative"}
        ]
    },
    {
        "question": "When confused about course material, you:",
        "category": "Academic Help Seeking",
        "options": [
            {"text": "Ask the teacher for clarification immediately", "tag": "Proactive"},
            {"text": "Research and figure it out independently", "tag": "Independent"},
            {"text": "Ask classmates or form study groups", "tag": "Collaborative"},
            {"text": "Review the textbook and lecture notes again", "tag": "Methodical"}
        ]
    },
    {
        "question": "How important are good grades to you?",
        "category": "Academic Motivation",
        "options": [
            {"text": "Very important - I aim for top marks", "tag": "Ambitious"},
            {"text": "Important but not at the cost of wellbeing", "tag": "Balanced"},
            {"text": "Somewhat important but I value learning more", "tag": "Learning-focused"},
            {"text": "I'm satisfied with passing grades", "tag": "Practical"}
        ]
    },
    {
        "question": "Which teaching style helps you learn best?",
        "category": "Teacher Preference",
        "options": [
            {"text": "Lectures with clear structure and examples", "tag": "Methodical"},
            {"text": "Interactive discussions and Q&A sessions", "tag": "Collaborative"},
            {"text": "Hands-on demonstrations and practical work", "tag": "Hands-on"},
            {"text": "Independent study with resources provided", "tag": "Independent"}
        ]
    },
    {
        "question": "How do you organize your schoolwork and assignments?",
        "category": "Academic Organization",
        "options": [
            {"text": "Detailed color-coded planner with all deadlines", "tag": "Organized"},
            {"text": "A simple system that works for me", "tag": "Practical"},
            {"text": "Rely on remembering and last-minute work", "tag": "Adaptive"},
            {"text": "Digital calendar with reminders", "tag": "Tech-savvy"}
        ]
    },
    {
        "question": "Which elective or optional subjects have you chosen or would choose?",
        "category": "Academic Interest",
        "options": [
            {"text": "Advanced STEM courses", "tag": "Logical"},
            {"text": "Arts, music, or creative subjects", "tag": "Creative-expression"},
            {"text": "Social sciences and humanities", "tag": "Analytical"},
            {"text": "Vocational or practical skills", "tag": "Hands-on"}
        ]
    },
    {
        "question": "How do you handle group academic projects?",
        "category": "Group Project Role",
        "options": [
            {"text": "Lead the group and coordinate efforts", "tag": "Leading-teams"},
            {"text": "Contribute equally to all parts", "tag": "Collaborative"},
            {"text": "Focus on my assigned portion", "tag": "Independent"},
            {"text": "Support whoever needs help", "tag": "Empathetic"}
        ]
    },
    {
        "question": "What's your approach to feedback from teachers?",
        "category": "Academic Feedback",
        "options": [
            {"text": "I actively seek feedback to improve", "tag": "Growth-minded"},
            {"text": "I listen and implement suggestions", "tag": "Responsible"},
            {"text": "I consider it but maintain my approach", "tag": "Confident"},
            {"text": "I sometimes feel discouraged by criticism", "tag": "Sensitive"}
        ]
    },
    {
        "question": "How do you choose which subjects to study in college?",
        "category": "Subject Selection",
        "options": [
            {"text": "Based on career prospects and earning potential", "tag": "Practical"},
            {"text": "Based on personal passion and interest", "tag": "Purpose-driven"},
            {"text": "Based on my natural talents and strengths", "tag": "Expert-focused"},
            {"text": "Based on social impact and helping others", "tag": "Compassionate"}
        ]
    },
    {
        "question": "When reading a complex academic article, you:",
        "category": "Complex Text Processing",
        "options": [
            {"text": "Break it into sections and analyze systematically", "tag": "Analytical"},
            {"text": "Read multiple sources to understand context", "tag": "Research-oriented"},
            {"text": "Focus on key findings and conclusions first", "tag": "Big-picture"},
            {"text": "Take detailed notes and reread as needed", "tag": "Detail-focused"}
        ]
    },
    {
        "question": "How do you handle tight deadlines?",
        "category": "Work Style",
        "options": [
            {"text": "I thrive under pressure and work efficiently", "tag": "Resilient"},
            {"text": "I manage well but prefer more time for quality", "tag": "Methodical"},
            {"text": "I feel stressed and need support", "tag": "Sensitive"},
            {"text": "I plan ahead to avoid tight deadlines", "tag": "Organized"}
        ]
    },
    {
        "question": "What's your approach to making important decisions?",
        "category": "Decision Making",
        "options": [
            {"text": "I analyze all available data thoroughly", "tag": "Analytical"},
            {"text": "I follow my instincts and intuition", "tag": "Intuitive"},
            {"text": "I consult with others for input", "tag": "Collaborative"},
            {"text": "I research and learn from past experiences", "tag": "Methodical"}
        ]
    },
    {
        "question": "How do you prefer to receive feedback?",
        "category": "Feedback Style",
        "options": [
            {"text": "Direct and honest, with no sugarcoating", "tag": "Confident"},
            {"text": "Constructive criticism with suggestions for improvement", "tag": "Growth-minded"},
            {"text": "Encouragement first, then areas to improve", "tag": "Sensitive"},
            {"text": "In writing so I can review and reflect", "tag": "Analytical"}
        ]
    },
    {
        "question": "What role do you play in social situations?",
        "category": "Social Behavior",
        "options": [
            {"text": "The energizer who gets people excited", "tag": "Extroverted"},
            {"text": "The listener who understands others", "tag": "Empathetic"},
            {"text": "The thinker who asks deeper questions", "tag": "Analytical"},
            {"text": "The observer who prefers watching", "tag": "Introverted"}
        ]
    },
    {
        "question": "How important is stability in your life?",
        "category": "Life Stability",
        "options": [
            {"text": "Very important - I need predictability", "tag": "Practical"},
            {"text": "Important but I can adapt to change", "tag": "Balanced"},
            {"text": "I actually prefer change and variety", "tag": "Adventurous"},
            {"text": "It depends on the circumstances", "tag": "Adaptive"}
        ]
    },
    {
        "question": "What motivates you most in daily life?",
        "category": "Daily Motivation",
        "options": [
            {"text": "Achievement and reaching my goals", "tag": "Ambitious"},
            {"text": "Helping others and making a difference", "tag": "Compassionate"},
            {"text": "Learning new things and growing", "tag": "Growth-minded"},
            {"text": "Enjoying life and having fun", "tag": "Adventurous"}
        ]
    },
    {
        "question": "How do you approach a completely new situation?",
        "category": "Adaptability",
        "options": [
            {"text": "Jump in and learn as I go", "tag": "Adventurous"},
            {"text": "Observe and study first before acting", "tag": "Methodical"},
            {"text": "Ask for guidance and support", "tag": "Collaborative"},
            {"text": "Research and prepare thoroughly", "tag": "Detail-focused"}
        ]
    },
    {
        "question": "What's your relationship with perfectionism?",
        "category": "Standards",
        "options": [
            {"text": "I strive for excellence in everything", "tag": "Meticulous"},
            {"text": "I aim for quality but accept good enough", "tag": "Balanced"},
            {"text": "I focus on what matters most", "tag": "Practical"},
            {"text": "I don't worry much about perfection", "tag": "Relaxed"}
        ]
    },
    {
        "question": "How do you handle conflict with others?",
        "category": "Conflict Management",
        "options": [
            {"text": "Face it head-on and resolve it directly", "tag": "Confident"},
            {"text": "Try to find a compromise that works for everyone", "tag": "Diplomatic"},
            {"text": "Avoid it and hope it goes away", "tag": "Avoidant"},
            {"text": "Involve a neutral third party if needed", "tag": "Collaborative"}
        ]
    },
    {
        "question": "What kind of environment do you work best in?",
        "category": "Work Environment",
        "options": [
            {"text": "Bustling and energetic with lots of activity", "tag": "Extroverted"},
            {"text": "Quiet and focused with minimal distractions", "tag": "Introverted"},
            {"text": "Collaborative with teamwork and interaction", "tag": "Collaborative"},
            {"text": "Flexible so I can adjust as needed", "tag": "Adaptive"}
        ]
    },
    {
        "question": "How do you view failure?",
        "category": "Failure Perspective",
        "options": [
            {"text": "A valuable learning opportunity", "tag": "Growth-minded"},
            {"text": "Unfortunate but manageable", "tag": "Resilient"},
            {"text": "Something to avoid at all costs", "tag": "Perfectionist"},
            {"text": "A normal part of progress", "tag": "Pragmatic"}
        ]
    },
    {
        "question": "What draws you to different career paths?",
        "category": "Career Interest",
        "options": [
            {"text": "The ability to help people directly", "tag": "Compassionate"},
            {"text": "Creative expression and innovation", "tag": "Creative-expression"},
            {"text": "Solving complex problems analytically", "tag": "Problem-solving"},
            {"text": "Building and leading teams", "tag": "Leading-teams"}
        ]
    },
    {
        "question": "How do you spend your weekends ideally?",
        "category": "Leisure Preference",
        "options": [
            {"text": "With friends and family doing social activities", "tag": "Social"},
            {"text": "Pursuing personal hobbies and interests", "tag": "Independent"},
            {"text": "Volunteering or helping others", "tag": "Compassionate"},
            {"text": "Learning something new", "tag": "Learning-focused"}
        ]
    },
    {
        "question": "How important are work-life balance and personal time?",
        "category": "Work-Life Balance",
        "options": [
            {"text": "Absolutely critical - my well-being comes first", "tag": "Health-conscious"},
            {"text": "Very important but I can flex when needed", "tag": "Balanced"},
            {"text": "Somewhat important but career is priority", "tag": "Ambitious"},
            {"text": "Not my main concern", "tag": "Work-focused"}
        ]
    },
    
    # ==================== SCALE-BASED QUESTIONS (1-5 RATING) ====================
    # These questions use a scale format with weighted trait scoring
    {
        "question": "How confident are you in solving mathematical problems?",
        "category": "Scale Assessment",
        "question_type": "scale",
        "options": [
            {"text": "1 - Not confident at all", "tag": "Math-Low", "weight": 1},
            {"text": "2 - Slightly confident", "tag": "Math-Low", "weight": 2},
            {"text": "3 - Moderately confident", "tag": "Math-Medium", "weight": 3},
            {"text": "4 - Very confident", "tag": "Math-High", "weight": 4},
            {"text": "5 - Extremely confident", "tag": "Math-High", "weight": 5}
        ],
        "trait_mapping": {
            "high": ["Logical", "Analytical", "Problem-solving", "Quantitative"],
            "medium": ["Methodical", "Detail-focused"],
            "low": ["Creative-expression", "Social"]
        },
        "course_boost": {
            "high": ["BS Computer Science", "BS Mathematics", "BS Statistics", "BS Data Science", "BS Accountancy", "BS Civil Engineering", "BS Electrical Engineering"],
            "medium": ["BS Business Administration major in Financial Management", "BS Economics", "BS Architecture"],
            "low": []
        }
    },
    {
        "question": "Rate your interest in technology and computer-related activities.",
        "category": "Scale Assessment",
        "question_type": "scale",
        "options": [
            {"text": "1 - Not interested at all", "tag": "Tech-Low", "weight": 1},
            {"text": "2 - Slightly interested", "tag": "Tech-Low", "weight": 2},
            {"text": "3 - Moderately interested", "tag": "Tech-Medium", "weight": 3},
            {"text": "4 - Very interested", "tag": "Tech-High", "weight": 4},
            {"text": "5 - Extremely interested", "tag": "Tech-High", "weight": 5}
        ],
        "trait_mapping": {
            "high": ["Tech-savvy", "Algorithm-focused", "Innovative", "Problem-solving"],
            "medium": ["Analytical", "Logical"],
            "low": ["Hands-on", "Field-work", "Social"]
        },
        "course_boost": {
            "high": ["BS Computer Science", "BS Information Technology", "BS Computer Engineering", "BS Data Science", "BS Cybersecurity", "BS Entertainment and Multimedia Computing"],
            "medium": ["BS Accounting Information Systems", "BS Health Information Management"],
            "low": []
        }
    },
    {
        "question": "Rate your comfort level with public speaking and presentations.",
        "category": "Scale Assessment",
        "question_type": "scale",
        "options": [
            {"text": "1 - Very uncomfortable", "tag": "Speaking-Low", "weight": 1},
            {"text": "2 - Somewhat uncomfortable", "tag": "Speaking-Low", "weight": 2},
            {"text": "3 - Neutral", "tag": "Speaking-Medium", "weight": 3},
            {"text": "4 - Comfortable", "tag": "Speaking-High", "weight": 4},
            {"text": "5 - Very comfortable", "tag": "Speaking-High", "weight": 5}
        ],
        "trait_mapping": {
            "high": ["Extroverted", "Articulate", "Leading-teams", "Confident"],
            "medium": ["Collaborative", "Social"],
            "low": ["Introverted", "Independent", "Detail-focused"]
        },
        "course_boost": {
            "high": ["BA in Communication", "Bachelor of Secondary Education", "BA in Political Science", "BS Tourism Management", "BA in Theater Arts", "BA in Journalism"],
            "medium": ["BS Business Administration major in Marketing Management", "Bachelor of Public Administration"],
            "low": []
        }
    },
    {
        "question": "How interested are you in understanding how the human body works?",
        "category": "Scale Assessment",
        "question_type": "scale",
        "options": [
            {"text": "1 - Not interested at all", "tag": "Health-Low", "weight": 1},
            {"text": "2 - Slightly interested", "tag": "Health-Low", "weight": 2},
            {"text": "3 - Moderately interested", "tag": "Health-Medium", "weight": 3},
            {"text": "4 - Very interested", "tag": "Health-High", "weight": 4},
            {"text": "5 - Extremely interested", "tag": "Health-High", "weight": 5}
        ],
        "trait_mapping": {
            "high": ["Helping-others", "Patient-focused", "Scientific-thinking", "Empathetic"],
            "medium": ["Analytical", "Research-oriented"],
            "low": ["Tech-savvy", "Business-minded"]
        },
        "course_boost": {
            "high": ["BS Nursing", "BS Medical Technology", "BS Physical Therapy", "BS Pharmacy", "Doctor of Veterinary Medicine", "BS Biology", "BS Psychology"],
            "medium": ["BS Nutrition and Dietetics", "BS Exercise and Sports Science"],
            "low": []
        }
    },
    {
        "question": "Rate your creativity and artistic abilities.",
        "category": "Scale Assessment",
        "question_type": "scale",
        "options": [
            {"text": "1 - Not creative at all", "tag": "Creative-Low", "weight": 1},
            {"text": "2 - Slightly creative", "tag": "Creative-Low", "weight": 2},
            {"text": "3 - Moderately creative", "tag": "Creative-Medium", "weight": 3},
            {"text": "4 - Very creative", "tag": "Creative-High", "weight": 4},
            {"text": "5 - Extremely creative", "tag": "Creative-High", "weight": 5}
        ],
        "trait_mapping": {
            "high": ["Creative-expression", "Artistic-passion", "Innovative", "Visual-learner"],
            "medium": ["Aesthetic-sense", "Hands-on"],
            "low": ["Logical", "Analytical", "Methodical"]
        },
        "course_boost": {
            "high": ["Bachelor of Fine Arts", "BS Architecture", "BS Multimedia Arts", "BA in Animation", "BA in Fashion Design and Merchandising", "BS Interior Design"],
            "medium": ["BA in Communication", "BA in Advertising Arts"],
            "low": []
        }
    },
    {
        "question": "How comfortable are you with leadership and taking charge?",
        "category": "Scale Assessment",
        "question_type": "scale",
        "options": [
            {"text": "1 - Not comfortable at all", "tag": "Leadership-Low", "weight": 1},
            {"text": "2 - Slightly comfortable", "tag": "Leadership-Low", "weight": 2},
            {"text": "3 - Moderately comfortable", "tag": "Leadership-Medium", "weight": 3},
            {"text": "4 - Very comfortable", "tag": "Leadership-High", "weight": 4},
            {"text": "5 - Extremely comfortable", "tag": "Leadership-High", "weight": 5}
        ],
        "trait_mapping": {
            "high": ["Leading-teams", "Ambitious", "Strategic", "Big-picture"],
            "medium": ["Collaborative", "Team-centric"],
            "low": ["Independent", "Detail-focused", "Introverted"]
        },
        "course_boost": {
            "high": ["BS Business Administration major in Operations Management", "BS Entrepreneurship", "Bachelor of Public Administration", "BS Industrial Engineering"],
            "medium": ["BS Business Administration major in Marketing Management", "BS Business Administration major in Human Resource Management"],
            "low": []
        }
    },
    {
        "question": "Rate your interest in helping and caring for others.",
        "category": "Scale Assessment",
        "question_type": "scale",
        "options": [
            {"text": "1 - Not interested", "tag": "Helping-Low", "weight": 1},
            {"text": "2 - Slightly interested", "tag": "Helping-Low", "weight": 2},
            {"text": "3 - Moderately interested", "tag": "Helping-Medium", "weight": 3},
            {"text": "4 - Very interested", "tag": "Helping-High", "weight": 4},
            {"text": "5 - Extremely interested", "tag": "Helping-High", "weight": 5}
        ],
        "trait_mapping": {
            "high": ["Helping-others", "Empathetic", "Compassionate", "Patient-focused"],
            "medium": ["Collaborative", "Social", "Service-oriented"],
            "low": ["Independent", "Analytical", "Problem-solving"]
        },
        "course_boost": {
            "high": ["BS Nursing", "BS Social Work", "Bachelor of Elementary Education", "Bachelor of Special Needs Education", "BS Physical Therapy", "BS Psychology"],
            "medium": ["BS Hospitality Management", "BS Tourism Management"],
            "low": []
        }
    },
    {
        "question": "How interested are you in business, finance, and entrepreneurship?",
        "category": "Scale Assessment",
        "question_type": "scale",
        "options": [
            {"text": "1 - Not interested at all", "tag": "Business-Low", "weight": 1},
            {"text": "2 - Slightly interested", "tag": "Business-Low", "weight": 2},
            {"text": "3 - Moderately interested", "tag": "Business-Medium", "weight": 3},
            {"text": "4 - Very interested", "tag": "Business-High", "weight": 4},
            {"text": "5 - Extremely interested", "tag": "Business-High", "weight": 5}
        ],
        "trait_mapping": {
            "high": ["Business-minded", "Ambitious", "Strategic", "Investment-minded"],
            "medium": ["Analytical", "Practical", "Organized"],
            "low": ["Creative-expression", "Research-oriented"]
        },
        "course_boost": {
            "high": ["BS Accountancy", "BS Entrepreneurship", "BS Business Administration major in Financial Management", "BS Business Administration major in Marketing Management", "BS Real Estate Management"],
            "medium": ["BS Business Economics", "BS Management Accounting"],
            "low": []
        }
    },
    {
        "question": "Rate your interest in scientific research and laboratory work.",
        "category": "Scale Assessment",
        "question_type": "scale",
        "options": [
            {"text": "1 - Not interested at all", "tag": "Research-Low", "weight": 1},
            {"text": "2 - Slightly interested", "tag": "Research-Low", "weight": 2},
            {"text": "3 - Moderately interested", "tag": "Research-Medium", "weight": 3},
            {"text": "4 - Very interested", "tag": "Research-High", "weight": 4},
            {"text": "5 - Extremely interested", "tag": "Research-High", "weight": 5}
        ],
        "trait_mapping": {
            "high": ["Research-oriented", "Laboratory", "Scientific-thinking", "Analytical"],
            "medium": ["Detail-focused", "Methodical"],
            "low": ["Hands-on", "Social", "Field-work"]
        },
        "course_boost": {
            "high": ["BS Biology", "BS Chemistry", "BS Biotechnology", "BS Medical Technology", "BS Forensic Science", "BS Physics"],
            "medium": ["BS Environmental Science", "BS Food Technology"],
            "low": []
        }
    },
    {
        "question": "How much do you enjoy outdoor activities and fieldwork?",
        "category": "Scale Assessment",
        "question_type": "scale",
        "options": [
            {"text": "1 - Strongly prefer indoors", "tag": "Outdoor-Low", "weight": 1},
            {"text": "2 - Prefer indoors", "tag": "Outdoor-Low", "weight": 2},
            {"text": "3 - No preference", "tag": "Outdoor-Medium", "weight": 3},
            {"text": "4 - Prefer outdoors", "tag": "Outdoor-High", "weight": 4},
            {"text": "5 - Strongly prefer outdoors", "tag": "Outdoor-High", "weight": 5}
        ],
        "trait_mapping": {
            "high": ["Field-work", "Outdoor-enthusiast", "Nature-connected", "Adventurous"],
            "medium": ["Hands-on", "Active"],
            "low": ["Office-based", "Laboratory", "Studio-work"]
        },
        "course_boost": {
            "high": ["BS Agriculture", "BS Forestry", "BS Marine Biology", "BS Geology", "BS Environmental Science", "BS Marine Transportation"],
            "medium": ["BS Civil Engineering", "BS Geodetic Engineering"],
            "low": []
        }
    },
    
    # ==================== CAREER PATH PREFERENCE QUESTIONS ====================
    # Direct mapping to course categories
    {
        "question": "Which career path appeals to you the most?",
        "category": "Career Preference",
        "question_type": "career_path",
        "options": [
            {"text": "Engineering - Building, designing, and solving technical problems", "tag": "Engineering-Path", 
             "course_tags": ["Problem-solving", "Technical", "Analytical", "Hands-on"],
             "recommended_courses": ["BS Civil Engineering", "BS Computer Engineering", "BS Electrical Engineering", "BS Mechanical Engineering", "BS Industrial Engineering"]},
            {"text": "Education - Teaching, mentoring, and developing others", "tag": "Education-Path",
             "course_tags": ["Helping-others", "Mentoring", "Patient", "Leading-teams"],
             "recommended_courses": ["Bachelor of Elementary Education", "Bachelor of Secondary Education", "Bachelor of Special Needs Education", "Bachelor of Physical Education"]},
            {"text": "Medicine & Healthcare - Caring for patients and promoting health", "tag": "Healthcare-Path",
             "course_tags": ["Helping-others", "Patient-focused", "Clinical-setting", "Empathetic"],
             "recommended_courses": ["BS Nursing", "BS Medical Technology", "BS Pharmacy", "BS Physical Therapy", "Doctor of Veterinary Medicine"]},
            {"text": "Business & Finance - Managing organizations and financial resources", "tag": "Business-Path",
             "course_tags": ["Business-minded", "Strategic", "Analytical", "Leading-teams"],
             "recommended_courses": ["BS Accountancy", "BS Business Administration major in Financial Management", "BS Entrepreneurship", "BS Business Economics"]},
            {"text": "Arts & Design - Creating visual content and artistic works", "tag": "Arts-Path",
             "course_tags": ["Creative-expression", "Visual-learner", "Artistic-passion", "Innovative"],
             "recommended_courses": ["Bachelor of Fine Arts", "BS Architecture", "BS Multimedia Arts", "BA in Animation", "BS Interior Design"]},
            {"text": "Law & Public Service - Advocating justice and serving communities", "tag": "Law-Path",
             "course_tags": ["Analytical", "Advocacy", "Leadership", "Critical-thinking"],
             "recommended_courses": ["BA in Political Science", "BS Legal Management", "Bachelor of Public Administration", "BS Criminology"]}
        ]
    },
    {
        "question": "Which secondary career area interests you?",
        "category": "Career Preference",
        "question_type": "career_path",
        "options": [
            {"text": "Technology & Computing - Software, data, and digital systems", "tag": "Tech-Path",
             "course_tags": ["Tech-savvy", "Algorithm-focused", "Logical", "Problem-solving"],
             "recommended_courses": ["BS Computer Science", "BS Information Technology", "BS Data Science", "BS Cybersecurity"]},
            {"text": "Science & Research - Discovering new knowledge through research", "tag": "Science-Path",
             "course_tags": ["Research-oriented", "Scientific-thinking", "Analytical", "Laboratory"],
             "recommended_courses": ["BS Biology", "BS Chemistry", "BS Physics", "BS Biotechnology", "BS Environmental Science"]},
            {"text": "Communication & Media - Creating content and connecting with audiences", "tag": "Media-Path",
             "course_tags": ["Creative-expression", "Articulate", "Media-savvy", "Extroverted"],
             "recommended_courses": ["BA in Communication", "BA in Journalism", "BA in Digital Filmmaking", "BS Development Communication"]},
            {"text": "Hospitality & Tourism - Serving guests and promoting travel", "tag": "Hospitality-Path",
             "course_tags": ["Service-oriented", "Social", "Cultural-awareness", "Extroverted"],
             "recommended_courses": ["BS Hospitality Management", "BS Tourism Management", "BS Culinary Management"]},
            {"text": "Agriculture & Environment - Working with nature and sustainability", "tag": "Agriculture-Path",
             "course_tags": ["Nature-connected", "Field-work", "Outdoor-enthusiast", "Practical"],
             "recommended_courses": ["BS Agriculture", "BS Forestry", "BS Environmental Science", "BS Marine Biology"]},
            {"text": "Maritime & Aviation - Working at sea or in the skies", "tag": "Maritime-Path",
             "course_tags": ["Adventurous", "Disciplined", "Technical", "Field-work"],
             "recommended_courses": ["BS Marine Transportation", "BS Marine Engineering", "BS Aeronautical Engineering", "BS Aircraft Maintenance Technology"]}
        ]
    },
    
    # ==================== EXTRACURRICULAR PREFERENCE QUESTIONS ====================
    {
        "question": "Which extracurricular activity do you prefer or would enjoy most?",
        "category": "Extracurricular Preference",
        "question_type": "extracurricular",
        "options": [
            {"text": "Debating / Public Speaking Club", "tag": "Debating-Club",
             "trait_tags": ["Articulate", "Critical-thinking", "Confident", "Analytical"],
             "recommended_courses": ["BA in Political Science", "BA in Communication", "BS Legal Management", "BA in Philosophy"]},
            {"text": "Programming / Robotics / Tech Club", "tag": "Programming-Club",
             "trait_tags": ["Tech-savvy", "Algorithm-focused", "Logical", "Problem-solving"],
             "recommended_courses": ["BS Computer Science", "BS Information Technology", "BS Computer Engineering", "BS Data Science"]},
            {"text": "Arts / Music / Drama Club", "tag": "Arts-Club",
             "trait_tags": ["Creative-expression", "Artistic-passion", "Expressive", "Visual-learner"],
             "recommended_courses": ["Bachelor of Fine Arts", "BA in Theater Arts", "BA in Music Production", "BS Multimedia Arts"]},
            {"text": "Science / Math Olympiad", "tag": "Science-Club",
             "trait_tags": ["Analytical", "Problem-solving", "Logical", "Research-oriented"],
             "recommended_courses": ["BS Mathematics", "BS Physics", "BS Chemistry", "BS Statistics"]},
            {"text": "Student Government / Leadership", "tag": "Leadership-Club",
             "trait_tags": ["Leading-teams", "Strategic", "Civic-minded", "Ambitious"],
             "recommended_courses": ["Bachelor of Public Administration", "BS Business Administration major in Operations Management", "BS Entrepreneurship"]},
            {"text": "Community Service / Volunteering", "tag": "Service-Club",
             "trait_tags": ["Helping-others", "Empathetic", "Community-focused", "Compassionate"],
             "recommended_courses": ["BS Social Work", "BS Nursing", "Bachelor of Elementary Education", "BS Community Development"]},
            {"text": "Sports / Athletic Teams", "tag": "Sports-Club",
             "trait_tags": ["Active", "Athletic-passion", "Team-centric", "Physical-fitness"],
             "recommended_courses": ["Bachelor of Physical Education", "BS Exercise and Sports Science", "BS Criminology"]},
            {"text": "School Publication / Writing", "tag": "Publication-Club",
             "trait_tags": ["Articulate", "Creative-expression", "Inquisitive", "Investigative"],
             "recommended_courses": ["BA in Journalism", "BA in Communication", "Bachelor of Library and Information Science"]}
        ]
    },
    {
        "question": "What type of school project do you enjoy working on most?",
        "category": "Extracurricular Preference",
        "question_type": "extracurricular",
        "options": [
            {"text": "Building models, prototypes, or experiments", "tag": "Prototype-Projects",
             "trait_tags": ["Hands-on", "Technical", "Problem-solving", "Practical"],
             "recommended_courses": ["BS Civil Engineering", "BS Mechanical Engineering", "BS Architecture", "BS Industrial Design"]},
            {"text": "Research papers and case studies", "tag": "Research-Projects",
             "trait_tags": ["Research-oriented", "Analytical", "Detail-focused", "Methodical"],
             "recommended_courses": ["BS Psychology", "BS Biology", "BA in Sociology", "BS Chemistry"]},
            {"text": "Creative presentations and multimedia", "tag": "Creative-Projects",
             "trait_tags": ["Creative-expression", "Visual-learner", "Tech-savvy", "Innovative"],
             "recommended_courses": ["BS Multimedia Arts", "BA in Communication", "BA in Advertising Arts", "BS Entertainment and Multimedia Computing"]},
            {"text": "Business plans and financial analysis", "tag": "Business-Projects",
             "trait_tags": ["Business-minded", "Strategic", "Analytical", "Ambitious"],
             "recommended_courses": ["BS Entrepreneurship", "BS Business Administration major in Financial Management", "BS Accountancy"]},
            {"text": "Community outreach and social programs", "tag": "Community-Projects",
             "trait_tags": ["Helping-others", "Community-focused", "Advocacy", "Collaborative"],
             "recommended_courses": ["BS Social Work", "BS Development Communication", "BS Community Development"]},
            {"text": "Science experiments and laboratory work", "tag": "Lab-Projects",
             "trait_tags": ["Laboratory", "Scientific-thinking", "Research-oriented", "Detail-focused"],
             "recommended_courses": ["BS Medical Technology", "BS Chemistry", "BS Biology", "BS Food Technology"]}
        ]
    },
    
    # ==================== ENHANCED SITUATIONAL QUESTIONS WITH COURSE MAPPING ====================
    {
        "question": "You're given a group project. What role do you prefer to take?",
        "category": "Situational - Role Preference",
        "question_type": "situational_mapped",
        "options": [
            {"text": "Leader / Organizer - Coordinating the team and delegating tasks", "tag": "Leader-Role",
             "trait_tags": ["Leading-teams", "Strategic", "Organized", "Big-picture"],
             "course_categories": ["Business Administration", "Education", "Political Science", "Management courses"],
             "recommended_courses": ["BS Business Administration major in Operations Management", "Bachelor of Secondary Education", "BA in Political Science", "BS Entrepreneurship", "Bachelor of Public Administration"]},
            {"text": "Researcher / Analyst - Gathering data and analyzing information", "tag": "Researcher-Role",
             "trait_tags": ["Research-oriented", "Analytical", "Detail-focused", "Methodical"],
             "course_categories": ["Engineering", "Science Related courses", "Information Technology"],
             "recommended_courses": ["BS Civil Engineering", "BS Computer Science", "BS Data Science", "BS Chemistry", "BS Statistics"]},
            {"text": "Designer / Creative contributor - Creating visuals and innovative ideas", "tag": "Designer-Role",
             "trait_tags": ["Creative-expression", "Visual-learner", "Innovative", "Artistic-passion"],
             "course_categories": ["Architecture", "Multimedia Arts", "Graphic Design", "Communication Arts"],
             "recommended_courses": ["BS Architecture", "BS Multimedia Arts", "BA in Animation", "BA in Advertising Arts", "BS Interior Design"]},
            {"text": "Presenter / Communicator - Explaining ideas and presenting to others", "tag": "Presenter-Role",
             "trait_tags": ["Articulate", "Extroverted", "Confident", "Communication-skills"],
             "course_categories": ["Mass Communication", "Education", "Law", "Tourism Management"],
             "recommended_courses": ["BA in Communication", "Bachelor of Secondary Education", "BS Legal Management", "BS Tourism Management", "BA in Journalism"]}
        ]
    },
    {
        "question": "Your school needs to raise funds for charity. What would you volunteer to do?",
        "category": "Situational - Role Preference",
        "question_type": "situational_mapped",
        "options": [
            {"text": "Plan the event logistics and coordinate volunteers", "tag": "Event-Planner",
             "trait_tags": ["Leading-teams", "Organized", "Strategic", "Collaborative"],
             "recommended_courses": ["BS Hospitality Management", "BS Business Administration major in Operations Management", "BS Tourism Management", "Bachelor of Public Administration"]},
            {"text": "Handle the finances, budgeting, and accounting", "tag": "Finance-Handler",
             "trait_tags": ["Analytical", "Detail-focused", "Numerical-thinking", "Methodical"],
             "recommended_courses": ["BS Accountancy", "BS Business Administration major in Financial Management", "BS Management Accounting"]},
            {"text": "Create promotional materials and social media content", "tag": "Promo-Creator",
             "trait_tags": ["Creative-expression", "Media-savvy", "Visual-learner", "Innovative"],
             "recommended_courses": ["BA in Communication", "BA in Advertising Arts", "BS Multimedia Arts", "BA in Digital Filmmaking"]},
            {"text": "Directly engage with donors and explain the cause", "tag": "Donor-Engager",
             "trait_tags": ["Extroverted", "Persuasive", "Helping-others", "Social"],
             "recommended_courses": ["BS Business Administration major in Marketing Management", "BS Social Work", "BS Real Estate Management", "Bachelor of Elementary Education"]}
        ]
    },
    {
        "question": "A friend is struggling with personal problems. How do you help?",
        "category": "Situational - Helping Style",
        "question_type": "situational_mapped",
        "options": [
            {"text": "Listen carefully and offer emotional support", "tag": "Emotional-Support",
             "trait_tags": ["Empathetic", "Compassionate", "Patient", "Helping-others"],
             "recommended_courses": ["BS Psychology", "BS Social Work", "BS Nursing", "Bachelor of Special Needs Education"]},
            {"text": "Analyze the situation and suggest practical solutions", "tag": "Solution-Provider",
             "trait_tags": ["Analytical", "Problem-solving", "Logical", "Practical"],
             "recommended_courses": ["BS Computer Science", "BS Industrial Engineering", "BS Business Administration major in Operations Management"]},
            {"text": "Help them research resources and options", "tag": "Resource-Researcher",
             "trait_tags": ["Research-oriented", "Helpful", "Detail-focused", "Methodical"],
             "recommended_courses": ["Bachelor of Library and Information Science", "BS Health Information Management", "BA in Sociology"]},
            {"text": "Distract them with fun activities to lift their spirits", "tag": "Mood-Lifter",
             "trait_tags": ["Extroverted", "Social", "Active", "Creative-expression"],
             "recommended_courses": ["BS Hospitality Management", "BS Entertainment and Multimedia Computing", "Bachelor of Physical Education"]}
        ]
    },
    {
        "question": "You notice a technical problem with the school's computer system. What do you do?",
        "category": "Situational - Problem Response",
        "question_type": "situational_mapped",
        "options": [
            {"text": "Try to diagnose and fix it yourself", "tag": "Self-Fixer",
             "trait_tags": ["Problem-solving", "Tech-savvy", "Independent", "Hands-on"],
             "recommended_courses": ["BS Computer Science", "BS Information Technology", "BS Computer Engineering", "BS Cybersecurity"]},
            {"text": "Report it to the IT department with detailed documentation", "tag": "Detail-Reporter",
             "trait_tags": ["Detail-focused", "Organized", "Systematic", "Methodical"],
             "recommended_courses": ["BS Health Information Management", "BS Office Administration", "BS Accounting Information Systems"]},
            {"text": "Alert others and help coordinate a workaround", "tag": "Coordinator",
             "trait_tags": ["Leading-teams", "Collaborative", "Communication-skills", "Helpful"],
             "recommended_courses": ["BS Business Administration major in Operations Management", "BA in Communication", "BS Industrial Engineering"]},
            {"text": "Let someone else handle it - tech isn't my thing", "tag": "Non-Tech",
             "trait_tags": ["Social", "Creative-expression", "Field-work", "Hands-on"],
             "recommended_courses": ["Bachelor of Fine Arts", "BS Agriculture", "BS Nursing", "BS Hospitality Management"]}
        ]
    },
    {
        "question": "You're asked to present your ideas to a panel of judges. How do you feel?",
        "category": "Situational - Presentation",
        "question_type": "situational_mapped",
        "options": [
            {"text": "Excited! I love presenting and persuading others", "tag": "Presentation-Lover",
             "trait_tags": ["Extroverted", "Confident", "Articulate", "Persuasive"],
             "recommended_courses": ["BA in Communication", "BS Business Administration major in Marketing Management", "BA in Journalism", "BS Legal Management"]},
            {"text": "Nervous, but I can do it if I prepare well", "tag": "Prepared-Presenter",
             "trait_tags": ["Methodical", "Detail-focused", "Resilient", "Analytical"],
             "recommended_courses": ["BS Accountancy", "BS Statistics", "BS Architecture", "BS Civil Engineering"]},
            {"text": "I'd rather someone else present while I prepare the content", "tag": "Content-Creator",
             "trait_tags": ["Research-oriented", "Detail-focused", "Independent", "Analytical"],
             "recommended_courses": ["BS Data Science", "BS Chemistry", "BS Biotechnology", "BS Medical Technology"]},
            {"text": "I prefer visual presentations - let my work speak for itself", "tag": "Visual-Presenter",
             "trait_tags": ["Visual-learner", "Creative-expression", "Artistic-passion", "Independent"],
             "recommended_courses": ["BS Architecture", "BS Multimedia Arts", "BA in Animation", "BA in Photography"]}
        ]
    },
    {
        "question": "There's an emergency situation at school. What's your instinct?",
        "category": "Situational - Crisis Response",
        "question_type": "situational_mapped",
        "options": [
            {"text": "Take charge and help organize the response", "tag": "Crisis-Leader",
             "trait_tags": ["Leading-teams", "Crisis-management", "Confident", "Decisive"],
             "recommended_courses": ["BS Criminology", "Bachelor of Public Administration", "BS Business Administration major in Operations Management", "BS Marine Transportation"]},
            {"text": "Help those who are injured or in distress", "tag": "Crisis-Helper",
             "trait_tags": ["Helping-others", "Empathetic", "Compassionate", "Patient-focused"],
             "recommended_courses": ["BS Nursing", "BS Medical Technology", "BS Physical Therapy", "BS Respiratory Therapy"]},
            {"text": "Stay calm and follow established protocols", "tag": "Protocol-Follower",
             "trait_tags": ["Methodical", "Disciplined", "Systematic", "Detail-focused"],
             "recommended_courses": ["BS Accountancy", "BS Customs Administration", "BS Office Administration"]},
            {"text": "Document the situation and communicate information", "tag": "Situation-Documenter",
             "trait_tags": ["Analytical", "Detail-focused", "Communication-skills", "Observational"],
             "recommended_courses": ["BA in Journalism", "BS Forensic Science", "BA in Communication", "BS Health Information Management"]}
        ]
    },
    {
        "question": "Your teacher assigns a research topic you know nothing about. How do you approach it?",
        "category": "Situational - Learning Approach",
        "question_type": "situational_mapped",
        "options": [
            {"text": "Dive deep into books, journals, and online resources", "tag": "Deep-Researcher",
             "trait_tags": ["Research-oriented", "Independent", "Detail-focused", "Methodical"],
             "recommended_courses": ["BS Biology", "BS Chemistry", "BA in Philosophy", "BS Psychology", "BS Statistics"]},
            {"text": "Find experts or knowledgeable people to interview", "tag": "Network-Learner",
             "trait_tags": ["Extroverted", "Social", "Collaborative", "Inquisitive"],
             "recommended_courses": ["BA in Journalism", "BA in Communication", "BS Social Work", "BS Tourism Management"]},
            {"text": "Try hands-on experiments to understand through doing", "tag": "Hands-On-Learner",
             "trait_tags": ["Hands-on", "Practical", "Active", "Experiential"],
             "recommended_courses": ["BS Civil Engineering", "BS Mechanical Engineering", "BS Agriculture", "BS Food Technology"]},
            {"text": "Watch videos and look for visual explanations", "tag": "Visual-Learner",
             "trait_tags": ["Visual-learner", "Tech-savvy", "Creative-expression", "Digital-art"],
             "recommended_courses": ["BS Multimedia Arts", "BA in Digital Filmmaking", "BS Entertainment and Multimedia Computing", "BA in Animation"]}
        ]
    },
    {
        "question": "You have free time after school. How do you spend it?",
        "category": "Situational - Free Time",
        "question_type": "situational_mapped",
        "options": [
            {"text": "Working on personal coding projects or tech experiments", "tag": "Tech-Hobbyist",
             "trait_tags": ["Tech-savvy", "Algorithm-focused", "Independent", "Innovative"],
             "recommended_courses": ["BS Computer Science", "BS Information Technology", "BS Data Science", "BS Entertainment and Multimedia Computing"]},
            {"text": "Volunteering or helping in community activities", "tag": "Community-Helper",
             "trait_tags": ["Helping-others", "Community-focused", "Compassionate", "Social"],
             "recommended_courses": ["BS Social Work", "BS Nursing", "Bachelor of Elementary Education", "BS Community Development"]},
            {"text": "Creating art, music, or working on creative projects", "tag": "Creative-Hobbyist",
             "trait_tags": ["Creative-expression", "Artistic-passion", "Innovative", "Visual-learner"],
             "recommended_courses": ["Bachelor of Fine Arts", "BA in Music Production", "BS Multimedia Arts", "BA in Animation"]},
            {"text": "Playing sports or engaging in physical activities", "tag": "Sports-Enthusiast",
             "trait_tags": ["Active", "Athletic-passion", "Physical-fitness", "Team-centric"],
             "recommended_courses": ["Bachelor of Physical Education", "BS Exercise and Sports Science", "BS Hospitality Management"]},
            {"text": "Reading books or learning something new online", "tag": "Self-Learner",
             "trait_tags": ["Research-oriented", "Independent", "Inquisitive", "Contemplative"],
             "recommended_courses": ["BA in Philosophy", "Bachelor of Library and Information Science", "BS Psychology", "BA in Linguistics"]}
        ]
    },
    {
        "question": "A classmate asks you to help them understand a difficult concept. How do you explain?",
        "category": "Situational - Teaching Style",
        "question_type": "situational_mapped",
        "options": [
            {"text": "Break it down step-by-step with clear explanations", "tag": "Step-By-Step-Teacher",
             "trait_tags": ["Methodical", "Patient", "Mentoring", "Helping-others"],
             "recommended_courses": ["Bachelor of Elementary Education", "Bachelor of Secondary Education", "Bachelor of Special Needs Education"]},
            {"text": "Use diagrams, drawings, and visual aids", "tag": "Visual-Teacher",
             "trait_tags": ["Visual-learner", "Creative-expression", "Hands-on", "Practical"],
             "recommended_courses": ["BS Architecture", "BS Interior Design", "BS Multimedia Arts", "BA in Animation"]},
            {"text": "Give real-world examples and practical applications", "tag": "Practical-Teacher",
             "trait_tags": ["Practical", "Hands-on", "Problem-solving", "Business-minded"],
             "recommended_courses": ["BS Business Administration major in Operations Management", "BS Industrial Engineering", "BS Civil Engineering"]},
            {"text": "Encourage them to discover the answer themselves with guidance", "tag": "Discovery-Teacher",
             "trait_tags": ["Mentoring", "Analytical", "Independent", "Research-oriented"],
             "recommended_courses": ["BS Psychology", "Bachelor of Secondary Education", "BA in Philosophy"]}
        ]
    },
    {
        "question": "You're planning a dream vacation. What type of trip appeals most?",
        "category": "Situational - Preferences",
        "question_type": "situational_mapped",
        "options": [
            {"text": "Adventure trip - hiking, diving, exploring nature", "tag": "Adventure-Trip",
             "trait_tags": ["Adventurous", "Outdoor-enthusiast", "Active", "Field-work"],
             "recommended_courses": ["BS Marine Biology", "BS Forestry", "BS Environmental Science", "BS Geology"]},
            {"text": "Cultural trip - museums, historical sites, local experiences", "tag": "Cultural-Trip",
             "trait_tags": ["Cultural-awareness", "Inquisitive", "Research-oriented", "Global-minded"],
             "recommended_courses": ["BS Tourism Management", "BA in International Studies", "BA in Sociology", "BA in Philosophy"]},
            {"text": "Relaxation trip - resorts, spas, and leisure activities", "tag": "Relaxation-Trip",
             "trait_tags": ["Service-oriented", "Health-conscious", "Social", "Practical"],
             "recommended_courses": ["BS Hospitality Management", "BS Nutrition and Dietetics", "BS Tourism Management"]},
            {"text": "City exploration - shopping, restaurants, nightlife", "tag": "Urban-Trip",
             "trait_tags": ["Social", "Extroverted", "Urban-focus", "Business-minded"],
             "recommended_courses": ["BS Business Administration major in Marketing Management", "BS Real Estate Management", "BS Environmental Planning"]}
        ]
    },
    
    # ==================== PHILIPPINE PUBLIC UNIVERSITY FOCUSED QUESTIONS ====================
    # These questions specifically target popular and affordable courses in SUCs (State Universities and Colleges)
    
    # --- PUBLIC SERVICE & GOVERNMENT CAREER QUESTIONS ---
    {
        "question": "Would you consider working for the government or public sector after graduation?",
        "category": "Public Service Interest",
        "question_type": "career_path",
        "options": [
            {"text": "Yes, I want to serve the Filipino people through government work", "tag": "Public-Service-Path",
             "course_tags": ["Civic-minded", "Public-service", "Leadership", "Helping-others"],
             "recommended_courses": ["Bachelor of Public Administration", "BS Criminology", "BS Social Work", "Bachelor of Secondary Education", "BA in Political Science"]},
            {"text": "Yes, particularly in law enforcement or peace and order", "tag": "Law-Enforcement-Path",
             "course_tags": ["Disciplined", "Protective", "Justice-minded", "Physical-fitness"],
             "recommended_courses": ["BS Criminology", "Bachelor of Public Administration", "BS Forensic Science"]},
            {"text": "Yes, I want to help with rural development and agriculture", "tag": "Rural-Development-Path",
             "course_tags": ["Field-work", "Nature-connected", "Community-focused", "Practical"],
             "recommended_courses": ["BS Agriculture", "BS Forestry", "BS Fisheries", "BS Community Development", "BS Agribusiness"]},
            {"text": "I prefer working in private companies or starting my own business", "tag": "Private-Sector-Path",
             "course_tags": ["Business-minded", "Independent", "Ambitious", "Entrepreneurial"],
             "recommended_courses": ["BS Entrepreneurship", "BS Business Administration major in Marketing Management", "BS Information Technology"]}
        ]
    },
    {
        "question": "If you could help your community, which way would you prefer?",
        "category": "Community Service Preference",
        "question_type": "situational_mapped",
        "options": [
            {"text": "Teaching children and youth in our barangay", "tag": "Community-Teacher",
             "trait_tags": ["Mentoring", "Helping-others", "Patient", "Child-focused"],
             "recommended_courses": ["Bachelor of Elementary Education", "Bachelor of Secondary Education", "Bachelor of Early Childhood Education", "Bachelor of Special Needs Education"]},
            {"text": "Organizing community programs and outreach activities", "tag": "Community-Organizer",
             "trait_tags": ["Leadership", "Community-focused", "Collaborative", "Advocacy"],
             "recommended_courses": ["BS Community Development", "BS Social Work", "BS Development Communication", "Bachelor of Public Administration"]},
            {"text": "Helping farmers and fisherfolk improve their livelihood", "tag": "Agricultural-Helper",
             "trait_tags": ["Practical", "Nature-connected", "Field-work", "Helping-others"],
             "recommended_courses": ["BS Agriculture", "BS Fisheries", "BS Agribusiness", "BS Forestry"]},
            {"text": "Providing healthcare and first aid services", "tag": "Community-Health-Worker",
             "trait_tags": ["Helping-others", "Clinical-setting", "Empathetic", "Patient-focused"],
             "recommended_courses": ["BS Nursing", "BS Midwifery", "BS Medical Technology", "BS Physical Therapy"]}
        ]
    },
    
    # --- EDUCATION PATH QUESTIONS (Very Popular in Public Schools) ---
    {
        "question": "What age group would you most enjoy teaching or working with?",
        "category": "Teaching Preference",
        "question_type": "situational_mapped",
        "options": [
            {"text": "Young children (kindergarten to elementary)", "tag": "Early-Childhood-Teacher",
             "trait_tags": ["Nurturing", "Patient", "Child-focused", "Playful"],
             "recommended_courses": ["Bachelor of Elementary Education", "Bachelor of Early Childhood Education"]},
            {"text": "Teenagers (high school students)", "tag": "High-School-Teacher",
             "trait_tags": ["Mentoring", "Subject-expertise", "Leadership", "Patient"],
             "recommended_courses": ["Bachelor of Secondary Education", "Bachelor of Physical Education"]},
            {"text": "Students with special learning needs", "tag": "Special-Education-Teacher",
             "trait_tags": ["Empathetic", "Adaptive", "Compassionate", "Patient"],
             "recommended_courses": ["Bachelor of Special Needs Education", "BS Psychology"]},
            {"text": "Adults learning vocational/technical skills", "tag": "Vocational-Teacher",
             "trait_tags": ["Practical-skills", "Hands-on", "Technical", "Mentoring"],
             "recommended_courses": ["Bachelor of Technical-Vocational Teacher Education", "BS Information Technology"]}
        ]
    },
    {
        "question": "If you become a teacher, what subject would you want to specialize in?",
        "category": "Teaching Specialization",
        "question_type": "situational_mapped",
        "options": [
            {"text": "Mathematics or Science subjects", "tag": "STEM-Teacher",
             "trait_tags": ["Logical", "Analytical", "Problem-solving", "Methodical"],
             "recommended_courses": ["Bachelor of Secondary Education", "BS Mathematics", "BS Biology", "BS Chemistry"]},
            {"text": "English, Filipino, or Literature", "tag": "Language-Teacher",
             "trait_tags": ["Articulate", "Creative-expression", "Language-passion", "Communication-skills"],
             "recommended_courses": ["Bachelor of Secondary Education", "BA in Linguistics", "BA in Communication"]},
            {"text": "Physical Education and Sports", "tag": "PE-Teacher",
             "trait_tags": ["Athletic-passion", "Active", "Coaching", "Motivational"],
             "recommended_courses": ["Bachelor of Physical Education", "BS Exercise and Sports Science"]},
            {"text": "Social Studies, History, or Values Education", "tag": "Social-Studies-Teacher",
             "trait_tags": ["Cultural-awareness", "Civic-minded", "Research-oriented", "Ethical"],
             "recommended_courses": ["Bachelor of Secondary Education", "BA in Political Science", "BA in Sociology", "BA in Philosophy"]}
        ]
    },
    
    # --- CRIMINOLOGY & LAW ENFORCEMENT (Very Popular in Philippines) ---
    {
        "question": "How do you feel about maintaining peace and order in your community?",
        "category": "Law Enforcement Interest",
        "question_type": "situational_mapped",
        "options": [
            {"text": "I would enjoy being directly involved in law enforcement", "tag": "Direct-Law-Enforcement",
             "trait_tags": ["Disciplined", "Protective", "Physical-fitness", "Justice-minded"],
             "recommended_courses": ["BS Criminology"]},
            {"text": "I prefer investigating crimes and collecting evidence", "tag": "Crime-Investigation",
             "trait_tags": ["Investigative", "Analytical", "Detail-focused", "Methodical"],
             "recommended_courses": ["BS Criminology", "BS Forensic Science"]},
            {"text": "I want to help rehabilitate offenders and prevent crimes", "tag": "Crime-Prevention",
             "trait_tags": ["Helping-others", "Empathetic", "Community-focused", "Advocacy"],
             "recommended_courses": ["BS Criminology", "BS Social Work", "BS Psychology"]},
            {"text": "I'm more interested in legal procedures and court processes", "tag": "Legal-Process",
             "trait_tags": ["Analytical", "Law-oriented", "Detail-focused", "Critical-thinking"],
             "recommended_courses": ["BS Legal Management", "BA in Political Science", "Bachelor of Public Administration"]}
        ]
    },
    
    # --- AGRICULTURE, FISHERIES & FORESTRY (Common in Provincial SUCs) ---
    {
        "question": "How do you feel about working in farms, forests, or fishing communities?",
        "category": "Agriculture Interest",
        "question_type": "situational_mapped",
        "options": [
            {"text": "I love the idea of growing crops and working with plants", "tag": "Crop-Farming",
             "trait_tags": ["Nature-connected", "Hands-on", "Outdoor-enthusiast", "Practical"],
             "recommended_courses": ["BS Agriculture", "BS Agribusiness", "BS Forestry"]},
            {"text": "I'm interested in fishing, aquaculture, or marine resources", "tag": "Aquatic-Resources",
             "trait_tags": ["Aquatic-passion", "Field-work", "Nature-connected", "Resourceful"],
             "recommended_courses": ["BS Fisheries", "BS Marine Biology", "BS Marine Transportation"]},
            {"text": "I want to protect forests and wildlife", "tag": "Forest-Conservation",
             "trait_tags": ["Conservation-minded", "Environmental-passion", "Nature-focused", "Advocacy"],
             "recommended_courses": ["BS Forestry", "BS Environmental Science", "BS Biology"]},
            {"text": "I want to help farmers and fisherfolk sell their products better", "tag": "Agri-Business",
             "trait_tags": ["Business-minded", "Practical", "Community-focused", "Entrepreneurial"],
             "recommended_courses": ["BS Agribusiness", "BS Agriculture", "BS Entrepreneurship"]}
        ]
    },
    {
        "question": "Would you be willing to work in rural or provincial areas after graduation?",
        "category": "Work Location Preference",
        "question_type": "career_path",
        "options": [
            {"text": "Yes, I want to help develop rural communities", "tag": "Rural-Work-Path",
             "course_tags": ["Community-focused", "Field-work", "Nature-connected", "Helping-others"],
             "recommended_courses": ["BS Agriculture", "BS Community Development", "Bachelor of Elementary Education", "BS Social Work", "BS Forestry"]},
            {"text": "Yes, especially in coastal or fishing communities", "tag": "Coastal-Work-Path",
             "course_tags": ["Aquatic-passion", "Field-work", "Nature-connected", "Adventurous"],
             "recommended_courses": ["BS Fisheries", "BS Marine Biology", "BS Marine Transportation", "BS Tourism Management"]},
            {"text": "I prefer working in cities but willing to do fieldwork", "tag": "Urban-Field-Path",
             "course_tags": ["Office-based", "Field-work", "Analytical", "Practical"],
             "recommended_courses": ["BS Civil Engineering", "BS Environmental Planning", "BS Geology", "BS Social Work"]},
            {"text": "I prefer working in urban areas or office settings", "tag": "Urban-Office-Path",
             "course_tags": ["Office-based", "Tech-savvy", "Business-minded", "Independent"],
             "recommended_courses": ["BS Information Technology", "BS Computer Science", "BS Accountancy", "BS Business Administration major in Financial Management"]}
        ]
    },
    
    # --- HEALTHCARE PATHS (Affordable in Public Medical Schools) ---
    {
        "question": "What aspect of healthcare interests you the most?",
        "category": "Healthcare Interest",
        "question_type": "situational_mapped",
        "options": [
            {"text": "Direct patient care and nursing", "tag": "Nursing-Care",
             "trait_tags": ["Helping-others", "Empathetic", "Patient-focused", "Compassionate"],
             "recommended_courses": ["BS Nursing", "BS Midwifery", "BS Physical Therapy"]},
            {"text": "Laboratory work and medical testing", "tag": "Medical-Lab",
             "trait_tags": ["Laboratory", "Analytical", "Detail-focused", "Methodical"],
             "recommended_courses": ["BS Medical Technology", "BS Chemistry", "BS Biology"]},
            {"text": "Nutrition and helping people eat healthier", "tag": "Nutrition-Focus",
             "trait_tags": ["Health-conscious", "Helping-others", "Scientific-thinking", "Empathetic"],
             "recommended_courses": ["BS Nutrition and Dietetics", "BS Food Technology"]},
            {"text": "Community health education and disease prevention", "tag": "Community-Health",
             "trait_tags": ["Community-focused", "Advocacy", "Helping-others", "Extroverted"],
             "recommended_courses": ["BS Nursing", "BS Midwifery", "BS Community Development", "BS Social Work"]}
        ]
    },
    
    # --- PRACTICAL/TECHNICAL SKILLS (TVL Track & Tech-Voc Programs) ---
    {
        "question": "Do you prefer learning practical, hands-on skills that you can use immediately?",
        "category": "Practical Skills Interest",
        "question_type": "situational_mapped",
        "options": [
            {"text": "Yes, I want to learn computer and IT skills", "tag": "IT-Skills",
             "trait_tags": ["Tech-savvy", "Problem-solving", "Practical", "Independent"],
             "recommended_courses": ["BS Information Technology", "BS Computer Science", "BS Entertainment and Multimedia Computing"]},
            {"text": "Yes, I want to learn about cooking and food service", "tag": "Culinary-Skills",
             "trait_tags": ["Culinary-passion", "Hands-on", "Service-oriented", "Creative-expression"],
             "recommended_courses": ["BS Culinary Management", "BS Hospitality Management", "BS Food Technology"]},
            {"text": "Yes, I want to learn technical/mechanical skills", "tag": "Technical-Skills",
             "trait_tags": ["Mechanical-minded", "Hands-on", "Technical", "Practical"],
             "recommended_courses": ["Bachelor of Technical-Vocational Teacher Education", "BS Industrial Engineering", "BS Mechanical Engineering"]},
            {"text": "Yes, I want to learn about tourism and hospitality", "tag": "Hospitality-Skills",
             "trait_tags": ["Service-oriented", "Social", "Cultural-awareness", "Guest-focused"],
             "recommended_courses": ["BS Tourism Management", "BS Hospitality Management", "BS Office Administration"]}
        ]
    },
    
    # --- BUDGET/SCHOLARSHIP CONSIDERATIONS ---
    {
        "question": "What is your primary consideration when choosing a college course?",
        "category": "Course Selection Priority",
        "question_type": "career_path",
        "options": [
            {"text": "Affordability - I need a course I can afford or get a scholarship for", "tag": "Budget-Conscious-Path",
             "course_tags": ["Practical", "Accessible", "Public-service", "Community-focused"],
             "recommended_courses": ["Bachelor of Elementary Education", "Bachelor of Secondary Education", "BS Agriculture", "BS Criminology", "BS Information Technology"]},
            {"text": "Job availability - I want a course with many job opportunities", "tag": "Employment-Path",
             "course_tags": ["Practical", "In-demand", "Versatile", "Tech-savvy"],
             "recommended_courses": ["BS Nursing", "BS Information Technology", "BS Accountancy", "BS Civil Engineering", "BS Criminology"]},
            {"text": "Passion - I want to study what I truly love regardless of job prospects", "tag": "Passion-Path",
             "course_tags": ["Creative-expression", "Artistic-passion", "Independent", "Authentic"],
             "recommended_courses": ["Bachelor of Fine Arts", "BA in Music Production", "BA in Theater Arts", "BA in Philosophy"]},
            {"text": "Family or community impact - I want to help my family or community", "tag": "Family-Impact-Path",
             "course_tags": ["Helping-others", "Community-focused", "Practical", "Service-oriented"],
             "recommended_courses": ["BS Nursing", "Bachelor of Elementary Education", "BS Agriculture", "BS Social Work", "BS Midwifery"]}
        ]
    },
    {
        "question": "Are you planning to apply for government scholarships like CHED or DOST?",
        "category": "Scholarship Interest",
        "question_type": "career_path",
        "options": [
            {"text": "Yes, DOST scholarship (Science and Technology courses)", "tag": "DOST-Scholar-Path",
             "course_tags": ["Scientific-thinking", "Research-oriented", "Technical", "Analytical"],
             "recommended_courses": ["BS Computer Science", "BS Information Technology", "BS Biology", "BS Chemistry", "BS Civil Engineering", "BS Agriculture"]},
            {"text": "Yes, CHED scholarship (various courses in SUCs)", "tag": "CHED-Scholar-Path",
             "course_tags": ["Practical", "Accessible", "Public-service", "Versatile"],
             "recommended_courses": ["Bachelor of Elementary Education", "Bachelor of Secondary Education", "BS Criminology", "BS Nursing", "Bachelor of Public Administration"]},
            {"text": "Yes, Teacher Education scholarship (DepEd programs)", "tag": "Teacher-Scholar-Path",
             "course_tags": ["Mentoring", "Helping-others", "Patient", "Public-service"],
             "recommended_courses": ["Bachelor of Elementary Education", "Bachelor of Secondary Education", "Bachelor of Special Needs Education", "Bachelor of Early Childhood Education"]},
            {"text": "No, I will self-fund or look for private scholarships", "tag": "Private-Fund-Path",
             "course_tags": ["Independent", "Ambitious", "Flexible", "Self-directed"],
             "recommended_courses": ["BS Business Administration major in Marketing Management", "BS Entrepreneurship", "BS Architecture", "BS Accountancy"]}
        ]
    },
    
    # --- SCALE QUESTIONS FOR POPULAR SUC COURSES ---
    {
        "question": "Rate your interest in becoming a teacher and educating future generations.",
        "category": "Scale Assessment - Teaching",
        "question_type": "scale",
        "options": [
            {"text": "1 - Not interested at all", "tag": "Teaching-Low", "weight": 1},
            {"text": "2 - Slightly interested", "tag": "Teaching-Low", "weight": 2},
            {"text": "3 - Moderately interested", "tag": "Teaching-Medium", "weight": 3},
            {"text": "4 - Very interested", "tag": "Teaching-High", "weight": 4},
            {"text": "5 - Extremely interested, teaching is my calling", "tag": "Teaching-High", "weight": 5}
        ],
        "trait_mapping": {
            "high": ["Mentoring", "Patient", "Helping-others", "Child-focused"],
            "medium": ["Collaborative", "Social", "Communicative"],
            "low": ["Independent", "Technical", "Office-based"]
        },
        "course_boost": {
            "high": ["Bachelor of Elementary Education", "Bachelor of Secondary Education", "Bachelor of Early Childhood Education", "Bachelor of Special Needs Education", "Bachelor of Physical Education"],
            "medium": ["Bachelor of Technical-Vocational Teacher Education", "BS Psychology"],
            "low": []
        }
    },
    {
        "question": "Rate your interest in law enforcement, crime prevention, and maintaining peace and order.",
        "category": "Scale Assessment - Criminology",
        "question_type": "scale",
        "options": [
            {"text": "1 - Not interested at all", "tag": "Criminology-Low", "weight": 1},
            {"text": "2 - Slightly interested", "tag": "Criminology-Low", "weight": 2},
            {"text": "3 - Moderately interested", "tag": "Criminology-Medium", "weight": 3},
            {"text": "4 - Very interested", "tag": "Criminology-High", "weight": 4},
            {"text": "5 - Extremely interested, I want to serve in law enforcement", "tag": "Criminology-High", "weight": 5}
        ],
        "trait_mapping": {
            "high": ["Disciplined", "Protective", "Justice-minded", "Physical-fitness"],
            "medium": ["Analytical", "Investigative", "Detail-focused"],
            "low": ["Creative-expression", "Artistic-passion", "Introverted"]
        },
        "course_boost": {
            "high": ["BS Criminology", "BS Forensic Science"],
            "medium": ["BA in Political Science", "Bachelor of Public Administration", "BS Legal Management"],
            "low": []
        }
    },
    {
        "question": "Rate your interest in farming, fishing, or working with natural resources.",
        "category": "Scale Assessment - Agriculture",
        "question_type": "scale",
        "options": [
            {"text": "1 - Not interested at all", "tag": "Agriculture-Low", "weight": 1},
            {"text": "2 - Slightly interested", "tag": "Agriculture-Low", "weight": 2},
            {"text": "3 - Moderately interested", "tag": "Agriculture-Medium", "weight": 3},
            {"text": "4 - Very interested", "tag": "Agriculture-High", "weight": 4},
            {"text": "5 - Extremely interested, I love working with nature", "tag": "Agriculture-High", "weight": 5}
        ],
        "trait_mapping": {
            "high": ["Nature-connected", "Outdoor-enthusiast", "Practical", "Field-work"],
            "medium": ["Hands-on", "Resourceful", "Independent"],
            "low": ["Office-based", "Tech-savvy", "Urban-focus"]
        },
        "course_boost": {
            "high": ["BS Agriculture", "BS Fisheries", "BS Forestry", "BS Agribusiness", "BS Marine Biology"],
            "medium": ["BS Environmental Science", "Doctor of Veterinary Medicine", "BS Geology"],
            "low": []
        }
    },
    {
        "question": "Rate your interest in helping sick people recover and providing healthcare services.",
        "category": "Scale Assessment - Healthcare",
        "question_type": "scale",
        "options": [
            {"text": "1 - Not interested at all", "tag": "Healthcare-Low", "weight": 1},
            {"text": "2 - Slightly interested", "tag": "Healthcare-Low", "weight": 2},
            {"text": "3 - Moderately interested", "tag": "Healthcare-Medium", "weight": 3},
            {"text": "4 - Very interested", "tag": "Healthcare-High", "weight": 4},
            {"text": "5 - Extremely interested, I want to save lives", "tag": "Healthcare-High", "weight": 5}
        ],
        "trait_mapping": {
            "high": ["Helping-others", "Empathetic", "Patient-focused", "Compassionate"],
            "medium": ["Clinical-setting", "Detail-focused", "Methodical"],
            "low": ["Independent", "Office-based", "Tech-savvy"]
        },
        "course_boost": {
            "high": ["BS Nursing", "BS Midwifery", "BS Physical Therapy", "BS Medical Technology", "BS Pharmacy"],
            "medium": ["BS Nutrition and Dietetics", "BS Respiratory Therapy", "BS Psychology"],
            "low": []
        }
    },
    {
        "question": "Rate your interest in serving the government or working for public institutions.",
        "category": "Scale Assessment - Public Service",
        "question_type": "scale",
        "options": [
            {"text": "1 - Not interested at all", "tag": "PublicService-Low", "weight": 1},
            {"text": "2 - Slightly interested", "tag": "PublicService-Low", "weight": 2},
            {"text": "3 - Moderately interested", "tag": "PublicService-Medium", "weight": 3},
            {"text": "4 - Very interested", "tag": "PublicService-High", "weight": 4},
            {"text": "5 - Extremely interested, I want to serve the Filipino people", "tag": "PublicService-High", "weight": 5}
        ],
        "trait_mapping": {
            "high": ["Civic-minded", "Public-service", "Leadership", "Community-focused"],
            "medium": ["Collaborative", "Helping-others", "Organized"],
            "low": ["Independent", "Entrepreneurial", "Risk-taking"]
        },
        "course_boost": {
            "high": ["Bachelor of Public Administration", "BA in Political Science", "BS Criminology", "BS Social Work", "Bachelor of Elementary Education"],
            "medium": ["Bachelor of Secondary Education", "BS Community Development", "BS Development Communication"],
            "low": []
        }
    },
    {
        "question": "Rate your interest in tourism, hospitality, and serving guests or tourists.",
        "category": "Scale Assessment - Hospitality",
        "question_type": "scale",
        "options": [
            {"text": "1 - Not interested at all", "tag": "Hospitality-Low", "weight": 1},
            {"text": "2 - Slightly interested", "tag": "Hospitality-Low", "weight": 2},
            {"text": "3 - Moderately interested", "tag": "Hospitality-Medium", "weight": 3},
            {"text": "4 - Very interested", "tag": "Hospitality-High", "weight": 4},
            {"text": "5 - Extremely interested, I love serving and interacting with people", "tag": "Hospitality-High", "weight": 5}
        ],
        "trait_mapping": {
            "high": ["Service-oriented", "Social", "Cultural-awareness", "Guest-focused"],
            "medium": ["Extroverted", "Collaborative", "Organized"],
            "low": ["Introverted", "Independent", "Technical"]
        },
        "course_boost": {
            "high": ["BS Tourism Management", "BS Hospitality Management", "BS Culinary Management"],
            "medium": ["BS Office Administration", "BA in Communication", "BS Business Administration major in Marketing Management"],
            "low": []
        }
    },
    
    # --- OFW/ABROAD WORK OPPORTUNITIES ---
    {
        "question": "Are you considering working abroad (OFW) after graduation?",
        "category": "Career Location",
        "question_type": "career_path",
        "options": [
            {"text": "Yes, I want to work as a nurse or healthcare worker abroad", "tag": "OFW-Healthcare-Path",
             "course_tags": ["Helping-others", "Clinical-setting", "Patient-focused", "Global-opportunity"],
             "recommended_courses": ["BS Nursing", "BS Physical Therapy", "BS Medical Technology", "BS Respiratory Therapy"]},
            {"text": "Yes, I want to work in the maritime or shipping industry", "tag": "OFW-Maritime-Path",
             "course_tags": ["Sea-passion", "Disciplined", "Technical", "Adventurous"],
             "recommended_courses": ["BS Marine Transportation", "BS Marine Engineering"]},
            {"text": "Yes, I want to work in hotels or cruise ships abroad", "tag": "OFW-Hospitality-Path",
             "course_tags": ["Service-oriented", "Social", "Cultural-awareness", "Guest-focused"],
             "recommended_courses": ["BS Hospitality Management", "BS Tourism Management", "BS Culinary Management"]},
            {"text": "I prefer to work and serve in the Philippines", "tag": "Local-Career-Path",
             "course_tags": ["Community-focused", "Civic-minded", "Local-service", "Helping-others"],
             "recommended_courses": ["Bachelor of Elementary Education", "Bachelor of Secondary Education", "BS Criminology", "Bachelor of Public Administration", "BS Social Work"]}
        ]
    },
    
    # --- FAMILY BUSINESS/LIVELIHOOD ---
    {
        "question": "Does your family have a business or livelihood you might continue or support?",
        "category": "Family Business Interest",
        "question_type": "situational_mapped",
        "options": [
            {"text": "Yes, we have a farm or agricultural business", "tag": "Family-Farm",
             "trait_tags": ["Nature-connected", "Business-minded", "Practical", "Family-oriented"],
             "recommended_courses": ["BS Agriculture", "BS Agribusiness", "BS Fisheries", "BS Forestry"]},
            {"text": "Yes, we have a small retail or service business (sari-sari store, eatery, etc.)", "tag": "Family-Retail",
             "trait_tags": ["Business-minded", "Service-oriented", "Practical", "Entrepreneurial"],
             "recommended_courses": ["BS Entrepreneurship", "BS Business Administration major in Marketing Management", "BS Accountancy", "BS Hospitality Management"]},
            {"text": "No, but I want to start a business to help my family", "tag": "Future-Entrepreneur",
             "trait_tags": ["Ambitious", "Entrepreneurial", "Independent", "Risk-taking"],
             "recommended_courses": ["BS Entrepreneurship", "BS Business Administration major in Financial Management", "BS Information Technology"]},
            {"text": "No, I want to pursue a professional career", "tag": "Professional-Career",
             "trait_tags": ["Ambitious", "Independent", "Career-focused", "Professional"],
             "recommended_courses": ["BS Computer Science", "BS Civil Engineering", "BS Accountancy", "BS Nursing", "BS Architecture"]}
        ]
    }
]

# ==================== COURSE DIRECT MAPPING ====================
# Maps specific traits to recommended courses with weights
COURSE_DIRECT_MAPPING = {
    # Engineering Courses
    "Engineering-Path": {
        "courses": ["BS Civil Engineering", "BS Computer Engineering", "BS Electrical Engineering", "BS Mechanical Engineering", "BS Industrial Engineering", "BS Electronics Engineering"],
        "required_traits": ["Problem-solving", "Analytical", "Technical"],
        "boost_weight": 15
    },
    # Technology Courses
    "Tech-Path": {
        "courses": ["BS Computer Science", "BS Information Technology", "BS Data Science", "BS Cybersecurity", "BS Entertainment and Multimedia Computing"],
        "required_traits": ["Tech-savvy", "Algorithm-focused", "Logical"],
        "boost_weight": 15
    },
    # Healthcare Courses
    "Healthcare-Path": {
        "courses": ["BS Nursing", "BS Medical Technology", "BS Pharmacy", "BS Physical Therapy", "Doctor of Veterinary Medicine", "BS Respiratory Therapy"],
        "required_traits": ["Helping-others", "Patient-focused", "Empathetic"],
        "boost_weight": 15
    },
    # Business Courses
    "Business-Path": {
        "courses": ["BS Accountancy", "BS Business Administration major in Financial Management", "BS Entrepreneurship", "BS Business Economics", "BS Management Accounting"],
        "required_traits": ["Business-minded", "Strategic", "Analytical"],
        "boost_weight": 15
    },
    # Arts & Design Courses
    "Arts-Path": {
        "courses": ["Bachelor of Fine Arts", "BS Architecture", "BS Multimedia Arts", "BA in Animation", "BS Interior Design", "BA in Fashion Design and Merchandising"],
        "required_traits": ["Creative-expression", "Visual-learner", "Artistic-passion"],
        "boost_weight": 15
    },
    # Education Courses
    "Education-Path": {
        "courses": ["Bachelor of Elementary Education", "Bachelor of Secondary Education", "Bachelor of Special Needs Education", "Bachelor of Physical Education"],
        "required_traits": ["Helping-others", "Mentoring", "Patient"],
        "boost_weight": 15
    },
    # Science & Research Courses
    "Science-Path": {
        "courses": ["BS Biology", "BS Chemistry", "BS Physics", "BS Biotechnology", "BS Environmental Science", "BS Mathematics"],
        "required_traits": ["Research-oriented", "Scientific-thinking", "Analytical"],
        "boost_weight": 15
    },
    
    # ========== PHILIPPINE PUBLIC UNIVERSITY POPULAR COURSES ==========
    # Criminology Path (Very popular in SUCs)
    "Criminology-Path": {
        "courses": ["BS Criminology", "BS Forensic Science"],
        "required_traits": ["Disciplined", "Protective", "Justice-minded", "Physical-fitness"],
        "boost_weight": 15
    },
    # Agriculture & Fisheries Path (Provincial SUCs)
    "Agriculture-Path": {
        "courses": ["BS Agriculture", "BS Fisheries", "BS Forestry", "BS Agribusiness", "Doctor of Veterinary Medicine"],
        "required_traits": ["Nature-connected", "Field-work", "Outdoor-enthusiast", "Practical"],
        "boost_weight": 15
    },
    # Public Administration Path (Government careers)
    "PublicAdmin-Path": {
        "courses": ["Bachelor of Public Administration", "BA in Political Science", "BS Community Development", "BS Social Work"],
        "required_traits": ["Civic-minded", "Public-service", "Leadership", "Community-focused"],
        "boost_weight": 15
    },
    # Teacher Education Path (Very common in SUCs)
    "Teacher-Path": {
        "courses": ["Bachelor of Elementary Education", "Bachelor of Secondary Education", "Bachelor of Early Childhood Education", "Bachelor of Special Needs Education", "Bachelor of Physical Education", "Bachelor of Technical-Vocational Teacher Education"],
        "required_traits": ["Mentoring", "Patient", "Helping-others", "Child-focused"],
        "boost_weight": 18
    },
    # Nursing & Allied Health Path (High demand)
    "Nursing-Path": {
        "courses": ["BS Nursing", "BS Midwifery", "BS Medical Technology", "BS Physical Therapy", "BS Respiratory Therapy"],
        "required_traits": ["Helping-others", "Empathetic", "Patient-focused", "Clinical-setting"],
        "boost_weight": 15
    },
    # Maritime Path (OFW opportunities)
    "Maritime-Path": {
        "courses": ["BS Marine Transportation", "BS Marine Engineering"],
        "required_traits": ["Sea-passion", "Disciplined", "Technical", "Adventurous"],
        "boost_weight": 15
    },
    # Hospitality & Tourism Path (Common in SUCs)
    "Hospitality-Path": {
        "courses": ["BS Hospitality Management", "BS Tourism Management", "BS Culinary Management", "BS Office Administration"],
        "required_traits": ["Service-oriented", "Social", "Cultural-awareness", "Guest-focused"],
        "boost_weight": 15
    },
    # IT Path (Widely available in public schools)
    "IT-Path": {
        "courses": ["BS Information Technology", "BS Computer Science", "BS Entertainment and Multimedia Computing"],
        "required_traits": ["Tech-savvy", "Problem-solving", "Logical", "Independent"],
        "boost_weight": 15
    }
}

# ==================== SCALE QUESTION PROCESSING CONFIG ====================
SCALE_WEIGHTS = {
    5: {"multiplier": 2.0, "confidence_boost": 20},   # Extremely/Very strong
    4: {"multiplier": 1.5, "confidence_boost": 10},   # Very/Strong
    3: {"multiplier": 1.0, "confidence_boost": 0},    # Moderate/Neutral
    2: {"multiplier": 0.5, "confidence_boost": -5},   # Slight/Low
    1: {"multiplier": 0.25, "confidence_boost": -10}  # Not at all/Very low
}

# ==================== ENHANCED ALGORITHM CONFIGURATIONS ====================

# === LEARNING STYLE MAPPING ===
# Maps trait tags to learning style categories
LEARNING_STYLE_MAPPING = {
    "visual": ["Visual-learner", "Creative-expression", "Artistic-passion", "Aesthetic-sense", "Cinematic-vision", "Digital-art"],
    "hands_on": ["Hands-on", "Practical", "Field-work", "Laboratory", "Active", "Technical"],
    "theoretical": ["Theoretical", "Research-oriented", "Analytical", "Abstract-thinking", "Contemplative", "Scientific-thinking"],
    "social": ["Collaborative", "Extroverted", "Team-centric", "Social", "Helping-others", "Mentoring"],
    "independent": ["Independent", "Introverted", "Detail-focused", "Methodical", "Systematic", "Office-based"]
}

# === WORK ENVIRONMENT MAPPING ===
# Maps courses to their primary work environments
WORK_ENVIRONMENT_MAPPING = {
    "office": ["Office-based", "Remote-friendly", "Systematic", "Administrative-skills"],
    "field": ["Field-work", "Outdoor-enthusiast", "Nature-connected", "Adventurous"],
    "clinical": ["Clinical-setting", "Patient-focused", "Healthcare", "Empathetic"],
    "laboratory": ["Laboratory", "Research-oriented", "Scientific-thinking", "Detail-focused"],
    "creative_studio": ["Studio-work", "Creative-expression", "Artistic-passion", "Visual-learner"],
    "active_physical": ["Active", "Athletic-passion", "Physical-fitness", "Hands-on"]
}

# === COURSE EMPLOYABILITY & DEMAND SCORES ===
# Based on CHED, DOLE, and job market data for Philippines (1-10 scale)
COURSE_EMPLOYABILITY = {
    # Very High Demand (9-10)
    "BS Nursing": {"demand_score": 10, "ofw_opportunity": True, "gov_opportunity": True, "salary_potential": "high"},
    "BS Information Technology": {"demand_score": 9, "ofw_opportunity": True, "gov_opportunity": True, "salary_potential": "high"},
    "BS Computer Science": {"demand_score": 9, "ofw_opportunity": True, "gov_opportunity": True, "salary_potential": "very_high"},
    "BS Accountancy": {"demand_score": 9, "ofw_opportunity": True, "gov_opportunity": True, "salary_potential": "high"},
    "BS Civil Engineering": {"demand_score": 9, "ofw_opportunity": True, "gov_opportunity": True, "salary_potential": "high"},
    "BS Medical Technology": {"demand_score": 9, "ofw_opportunity": True, "gov_opportunity": True, "salary_potential": "high"},
    "BS Pharmacy": {"demand_score": 8, "ofw_opportunity": True, "gov_opportunity": True, "salary_potential": "high"},
    
    # High Demand (7-8)
    "Bachelor of Elementary Education": {"demand_score": 8, "ofw_opportunity": False, "gov_opportunity": True, "salary_potential": "moderate"},
    "Bachelor of Secondary Education": {"demand_score": 8, "ofw_opportunity": False, "gov_opportunity": True, "salary_potential": "moderate"},
    "BS Criminology": {"demand_score": 8, "ofw_opportunity": False, "gov_opportunity": True, "salary_potential": "moderate"},
    "BS Electrical Engineering": {"demand_score": 8, "ofw_opportunity": True, "gov_opportunity": True, "salary_potential": "high"},
    "BS Mechanical Engineering": {"demand_score": 8, "ofw_opportunity": True, "gov_opportunity": True, "salary_potential": "high"},
    "BS Marine Transportation": {"demand_score": 8, "ofw_opportunity": True, "gov_opportunity": False, "salary_potential": "very_high"},
    "BS Marine Engineering": {"demand_score": 8, "ofw_opportunity": True, "gov_opportunity": False, "salary_potential": "very_high"},
    "BS Physical Therapy": {"demand_score": 8, "ofw_opportunity": True, "gov_opportunity": True, "salary_potential": "high"},
    "BS Hospitality Management": {"demand_score": 7, "ofw_opportunity": True, "gov_opportunity": False, "salary_potential": "moderate"},
    "BS Tourism Management": {"demand_score": 7, "ofw_opportunity": True, "gov_opportunity": False, "salary_potential": "moderate"},
    "BS Agriculture": {"demand_score": 7, "ofw_opportunity": False, "gov_opportunity": True, "salary_potential": "moderate"},
    "BS Midwifery": {"demand_score": 7, "ofw_opportunity": True, "gov_opportunity": True, "salary_potential": "moderate"},
    "Bachelor of Public Administration": {"demand_score": 7, "ofw_opportunity": False, "gov_opportunity": True, "salary_potential": "moderate"},
    "BS Social Work": {"demand_score": 7, "ofw_opportunity": False, "gov_opportunity": True, "salary_potential": "moderate"},
    
    # Moderate Demand (5-6)
    "BS Psychology": {"demand_score": 6, "ofw_opportunity": False, "gov_opportunity": True, "salary_potential": "moderate"},
    "BS Architecture": {"demand_score": 6, "ofw_opportunity": True, "gov_opportunity": True, "salary_potential": "high"},
    "BS Business Administration major in Marketing Management": {"demand_score": 6, "ofw_opportunity": False, "gov_opportunity": False, "salary_potential": "moderate"},
    "BS Business Administration major in Financial Management": {"demand_score": 6, "ofw_opportunity": False, "gov_opportunity": True, "salary_potential": "moderate"},
    "BS Entrepreneurship": {"demand_score": 5, "ofw_opportunity": False, "gov_opportunity": False, "salary_potential": "variable"},
    "BS Culinary Management": {"demand_score": 6, "ofw_opportunity": True, "gov_opportunity": False, "salary_potential": "moderate"},
    "BS Multimedia Arts": {"demand_score": 6, "ofw_opportunity": False, "gov_opportunity": False, "salary_potential": "moderate"},
    "BA in Communication": {"demand_score": 5, "ofw_opportunity": False, "gov_opportunity": True, "salary_potential": "moderate"},
    "BS Fisheries": {"demand_score": 5, "ofw_opportunity": False, "gov_opportunity": True, "salary_potential": "low"},
    "BS Forestry": {"demand_score": 5, "ofw_opportunity": False, "gov_opportunity": True, "salary_potential": "low"}
}

# === COURSE ACCESSIBILITY IN PUBLIC SCHOOLS ===
# Availability in SUCs (State Universities and Colleges) - affects affordability
COURSE_PUBLIC_AVAILABILITY = {
    # Widely Available (most SUCs offer these)
    "Bachelor of Elementary Education": {"availability": "very_high", "typical_tuition": "free_in_suc", "scholarship_available": True},
    "Bachelor of Secondary Education": {"availability": "very_high", "typical_tuition": "free_in_suc", "scholarship_available": True},
    "BS Criminology": {"availability": "very_high", "typical_tuition": "free_in_suc", "scholarship_available": True},
    "BS Information Technology": {"availability": "very_high", "typical_tuition": "free_in_suc", "scholarship_available": True},
    "BS Agriculture": {"availability": "very_high", "typical_tuition": "free_in_suc", "scholarship_available": True},
    "BS Fisheries": {"availability": "high", "typical_tuition": "free_in_suc", "scholarship_available": True},
    "BS Forestry": {"availability": "high", "typical_tuition": "free_in_suc", "scholarship_available": True},
    "Bachelor of Public Administration": {"availability": "high", "typical_tuition": "free_in_suc", "scholarship_available": True},
    "BS Social Work": {"availability": "high", "typical_tuition": "free_in_suc", "scholarship_available": True},
    "BS Hospitality Management": {"availability": "high", "typical_tuition": "free_in_suc", "scholarship_available": True},
    "BS Tourism Management": {"availability": "high", "typical_tuition": "free_in_suc", "scholarship_available": True},
    
    # Available in Many SUCs
    "BS Nursing": {"availability": "moderate", "typical_tuition": "subsidized", "scholarship_available": True},
    "BS Civil Engineering": {"availability": "moderate", "typical_tuition": "subsidized", "scholarship_available": True},
    "BS Computer Science": {"availability": "moderate", "typical_tuition": "free_in_suc", "scholarship_available": True},
    "BS Accountancy": {"availability": "moderate", "typical_tuition": "subsidized", "scholarship_available": True},
    "BS Biology": {"availability": "moderate", "typical_tuition": "free_in_suc", "scholarship_available": True},
    "BS Chemistry": {"availability": "moderate", "typical_tuition": "free_in_suc", "scholarship_available": True},
    "BS Mathematics": {"availability": "moderate", "typical_tuition": "free_in_suc", "scholarship_available": True},
    "BS Midwifery": {"availability": "moderate", "typical_tuition": "free_in_suc", "scholarship_available": True},
    
    # Limited Availability (select SUCs only)
    "BS Medical Technology": {"availability": "limited", "typical_tuition": "subsidized", "scholarship_available": True},
    "BS Pharmacy": {"availability": "limited", "typical_tuition": "subsidized", "scholarship_available": True},
    "BS Architecture": {"availability": "limited", "typical_tuition": "subsidized", "scholarship_available": True},
    "BS Marine Transportation": {"availability": "limited", "typical_tuition": "subsidized", "scholarship_available": True},
    "BS Marine Engineering": {"availability": "limited", "typical_tuition": "subsidized", "scholarship_available": True},
    
    # Primarily Private Schools
    "BS Multimedia Arts": {"availability": "low", "typical_tuition": "private_rate", "scholarship_available": False},
    "BA in Animation": {"availability": "low", "typical_tuition": "private_rate", "scholarship_available": False},
    "BS Entertainment and Multimedia Computing": {"availability": "low", "typical_tuition": "private_rate", "scholarship_available": False}
}

# === SKILL REQUIREMENT MAPPING ===
# Maps courses to required skill levels (for self-assessment matching)
COURSE_SKILL_REQUIREMENTS = {
    # Math-Heavy Courses
    "BS Computer Science": {"math": "high", "communication": "moderate", "physical": "low", "creativity": "moderate"},
    "BS Civil Engineering": {"math": "very_high", "communication": "moderate", "physical": "moderate", "creativity": "moderate"},
    "BS Accountancy": {"math": "high", "communication": "moderate", "physical": "low", "creativity": "low"},
    "BS Mathematics": {"math": "very_high", "communication": "low", "physical": "low", "creativity": "moderate"},
    "BS Statistics": {"math": "very_high", "communication": "moderate", "physical": "low", "creativity": "low"},
    "BS Physics": {"math": "very_high", "communication": "low", "physical": "low", "creativity": "moderate"},
    "BS Data Science": {"math": "high", "communication": "moderate", "physical": "low", "creativity": "moderate"},
    
    # Communication-Heavy Courses
    "Bachelor of Elementary Education": {"math": "moderate", "communication": "high", "physical": "moderate", "creativity": "high"},
    "Bachelor of Secondary Education": {"math": "moderate", "communication": "high", "physical": "low", "creativity": "moderate"},
    "BA in Communication": {"math": "low", "communication": "very_high", "physical": "low", "creativity": "high"},
    "BA in Journalism": {"math": "low", "communication": "very_high", "physical": "moderate", "creativity": "high"},
    "BS Social Work": {"math": "low", "communication": "high", "physical": "moderate", "creativity": "moderate"},
    "Bachelor of Public Administration": {"math": "moderate", "communication": "high", "physical": "low", "creativity": "low"},
    
    # Physical/Active Courses
    "BS Criminology": {"math": "low", "communication": "moderate", "physical": "high", "creativity": "low"},
    "Bachelor of Physical Education": {"math": "low", "communication": "moderate", "physical": "very_high", "creativity": "moderate"},
    "BS Marine Transportation": {"math": "moderate", "communication": "moderate", "physical": "high", "creativity": "low"},
    "BS Agriculture": {"math": "moderate", "communication": "low", "physical": "high", "creativity": "moderate"},
    "BS Nursing": {"math": "moderate", "communication": "high", "physical": "high", "creativity": "low"},
    
    # Creative Courses
    "Bachelor of Fine Arts": {"math": "low", "communication": "moderate", "physical": "moderate", "creativity": "very_high"},
    "BS Architecture": {"math": "high", "communication": "moderate", "physical": "low", "creativity": "very_high"},
    "BS Multimedia Arts": {"math": "low", "communication": "moderate", "physical": "low", "creativity": "very_high"},
    "BA in Animation": {"math": "low", "communication": "low", "physical": "low", "creativity": "very_high"},
    "BS Interior Design": {"math": "moderate", "communication": "moderate", "physical": "low", "creativity": "very_high"},
    
    # Balanced Courses
    "BS Information Technology": {"math": "moderate", "communication": "moderate", "physical": "low", "creativity": "moderate"},
    "BS Hospitality Management": {"math": "low", "communication": "high", "physical": "moderate", "creativity": "moderate"},
    "BS Tourism Management": {"math": "low", "communication": "high", "physical": "moderate", "creativity": "moderate"},
    "BS Psychology": {"math": "moderate", "communication": "high", "physical": "low", "creativity": "moderate"}
}

# === CAREER GOAL MAPPING ===
# Maps career goals/aspirations to suitable courses
CAREER_GOAL_MAPPING = {
    "ofw_healthcare": ["BS Nursing", "BS Physical Therapy", "BS Medical Technology", "BS Midwifery", "BS Respiratory Therapy"],
    "ofw_maritime": ["BS Marine Transportation", "BS Marine Engineering"],
    "ofw_hospitality": ["BS Hospitality Management", "BS Tourism Management", "BS Culinary Management"],
    "ofw_tech": ["BS Computer Science", "BS Information Technology", "BS Data Science"],
    "government_service": ["Bachelor of Public Administration", "BS Criminology", "Bachelor of Elementary Education", "Bachelor of Secondary Education", "BS Social Work"],
    "teaching": ["Bachelor of Elementary Education", "Bachelor of Secondary Education", "Bachelor of Special Needs Education", "Bachelor of Physical Education", "Bachelor of Technical-Vocational Teacher Education"],
    "healthcare_local": ["BS Nursing", "BS Medical Technology", "BS Pharmacy", "BS Physical Therapy", "BS Midwifery"],
    "business_entrepreneur": ["BS Entrepreneurship", "BS Business Administration major in Marketing Management", "BS Accountancy", "BS Business Administration major in Financial Management"],
    "agriculture_rural": ["BS Agriculture", "BS Agribusiness", "BS Fisheries", "BS Forestry"],
    "tech_startup": ["BS Computer Science", "BS Information Technology", "BS Data Science", "BS Entertainment and Multimedia Computing"],
    "creative_arts": ["Bachelor of Fine Arts", "BS Multimedia Arts", "BA in Animation", "BA in Music Production", "BS Architecture"],
    "law_enforcement": ["BS Criminology", "BS Forensic Science"],
    "community_service": ["BS Social Work", "BS Community Development", "BS Development Communication"]
}

# === PERSONALITY-COURSE COMPATIBILITY ===
# Maps personality dimensions to course compatibility scores
PERSONALITY_COMPATIBILITY = {
    "introvert_friendly": ["BS Computer Science", "BS Mathematics", "BS Statistics", "BS Accountancy", "BA in Animation", 
                           "Bachelor of Library and Information Science", "BS Data Science", "BS Chemistry", "BS Physics",
                           "BS Biology", "BA in Philosophy"],
    "extrovert_friendly": ["BS Hospitality Management", "BS Tourism Management", "Bachelor of Elementary Education",
                           "BA in Communication", "BS Social Work", "BS Business Administration major in Marketing Management",
                           "Bachelor of Physical Education", "BA in Theater Arts", "BS Nursing"],
    "structured_preference": ["BS Accountancy", "BS Civil Engineering", "BS Criminology", "BS Nursing", 
                              "BS Medical Technology", "Bachelor of Public Administration"],
    "flexible_creative": ["BS Entrepreneurship", "Bachelor of Fine Arts", "BS Multimedia Arts", "BS Architecture",
                          "BA in Communication", "BA in Journalism", "BA in Fashion Design and Merchandising"]
}

# ==================== FILTERED QUESTION LISTS (For Algorithm Use) ====================
# Filter questions by type from the main pool for easy access
SCALE_QUESTIONS = [q for q in QUESTIONS_POOL if q.get("question_type") == "scale"]
CAREER_PATH_QUESTIONS = [q for q in QUESTIONS_POOL if q.get("question_type") == "career_path"]
EXTRACURRICULAR_QUESTIONS = [q for q in QUESTIONS_POOL if q.get("question_type") == "extracurricular"]
SITUATIONAL_MAPPED_QUESTIONS = [q for q in QUESTIONS_POOL if q.get("question_type") == "situational_mapped"]

# Standard questions (without explicit question_type)
STANDARD_QUESTIONS = [q for q in QUESTIONS_POOL if not q.get("question_type") or q.get("question_type") == "standard"]

# ==================== ASSESSMENT CONFIGURATION ====================
ASSESSMENT_TIERS = {
    "quick": {
        "name": "Quick Assessment",
        "description": "A brief 30-question assessment for quick recommendations",
        "question_count": 30,
        "estimated_time": "10-15 minutes",
        "accuracy": "Moderate - Good for initial exploration"
    },
    "standard": {
        "name": "Standard Assessment",
        "description": "A comprehensive 80-question assessment for reliable recommendations",
        "question_count": 80,
        "estimated_time": "25-35 minutes",
        "accuracy": "High - Recommended for most users"
    },
    "comprehensive": {
        "name": "Comprehensive Assessment",
        "description": "A thorough 150-question assessment for highly accurate recommendations",
        "question_count": 150,
        "estimated_time": "45-60 minutes",
        "accuracy": "Very High - Most accurate recommendations"
    }
}