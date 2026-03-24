"""
Insert 14 replacement questions into questions_enhanced.py to replace the
deleted duplicates.  Each question covers the SAME topic area as the one it
replaces but uses a completely different angle / question text / option wording.

Freed question IDs (from deleted dupes): 52, 71, 72, 414, 633, 634, 639, 642, 911, 915, 919, 920
Extra IDs needed for expansion-dup replacements: 6, 7  (both unused)

Uses freed option IDs starting at 51 (first large free block).
"""

import sys, os, re, json

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# ═══════════════════════════════════════════════════════════════
# 14 REPLACEMENT QUESTIONS
# ═══════════════════════════════════════════════════════════════

NEW_QUESTIONS = [
    # ── 1. Replace Q71 (Favorite Subject dup) ──
    # Original Q31 asks "Which subject do you enjoy MOST?" — this asks about
    # how they use their favorite subject OUTSIDE of class.
    {
        "question_id": 71,
        "question_text": "Outside of class, how do you use or explore what you learn in school?",
        "category": "Academic - Application",
        "options": [
            {"option_id": 51, "option_text": "I do science experiments or watch documentaries about discoveries",
             "trait_tags": {"Lab-Research": 1.0, "Investigative": 0.5, "Analytical-Skill": 0.4, "Field-Research": 0.35, "Data-Analytics": 0.2, "Medical-Lab": 0.15}},
            {"option_id": 52, "option_text": "I solve math puzzles, brainteasers, or play strategy games",
             "trait_tags": {"Data-Analytics": 1.0, "Analytical-Skill": 0.5, "Software-Dev": 0.35, "Finance-Acct": 0.3, "Investigative": 0.25, "Technical-Skill": 0.2}},
            {"option_id": 53, "option_text": "I read novels, write stories, or join speech contests",
             "trait_tags": {"Teaching-Ed": 1.0, "Writing-Comm": 0.5, "Social": 0.4, "People-Skill": 0.35, "Creative-Skill": 0.25, "Community-Serve": 0.2}},
            {"option_id": 54, "option_text": "I help younger students with homework or tutor classmates",
             "trait_tags": {"Teaching-Ed": 1.0, "People-Skill": 0.5, "Community-Serve": 0.45, "Social": 0.35, "Conventional": 0.25, "Counseling": 0.2}},
            {"option_id": 55, "option_text": "I tinker with computers, build apps, or edit videos",
             "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.5, "Digital-Media": 0.4, "Hardware-Systems": 0.3, "Creative-Skill": 0.25, "Data-Analytics": 0.2}},
            {"option_id": 56, "option_text": "I draw, paint, take photos, or create digital art",
             "trait_tags": {"Artistic": 1.0, "Visual-Design": 0.5, "Creative-Skill": 0.45, "Digital-Media": 0.35, "Spatial-Design": 0.25, "Performing-Arts": 0.15}},
            {"option_id": 57, "option_text": "I play sports, work out, or practice martial arts",
             "trait_tags": {"Physical-Skill": 1.0, "Realistic": 0.45, "Sports-Ed": 0.4, "Rehab-Therapy": 0.3, "Law-Enforce": 0.25, "Maritime-Sea": 0.2}},
            {"option_id": 58, "option_text": "I track my savings, sell things online, or plan small ventures",
             "trait_tags": {"Finance-Acct": 1.0, "Enterprising": 0.5, "Admin-Skill": 0.4, "Marketing-Sales": 0.35, "Startup-Venture": 0.3, "Conventional": 0.2}},
            {"option_id": 59, "option_text": "I grow plants, take care of animals, or explore outdoors",
             "trait_tags": {"Agri-Nature": 1.0, "Field-Research": 0.5, "Environmental-Sci": 0.4, "Physical-Skill": 0.3, "Realistic": 0.25, "Community-Serve": 0.2}},
            {"option_id": 60, "option_text": "I research current events, debate issues, or follow politics",
             "trait_tags": {"Community-Serve": 1.0, "Social": 0.5, "Legal-Practice": 0.35, "Law-Enforce": 0.3, "People-Skill": 0.25, "Investigative": 0.2}},
        ],
    },

    # ── 2. Replace Q72 (Challenging Subject dup) ──
    # Original Q32 asks "MOST CHALLENGING subject" — this asks about
    # how they REACT when a subject gets difficult.
    {
        "question_id": 72,
        "question_text": "When a school subject gets really difficult, what do you usually do?",
        "category": "Academic - Coping",
        "options": [
            {"option_id": 61, "option_text": "I search for YouTube tutorials or visual explanations",
             "trait_tags": {"Digital-Media": 1.0, "Software-Dev": 0.4, "Technical-Skill": 0.35, "Creative-Skill": 0.3, "Data-Analytics": 0.2, "Investigative": 0.15}},
            {"option_id": 62, "option_text": "I form a study group and we figure it out together",
             "trait_tags": {"People-Skill": 1.0, "Social": 0.5, "Teaching-Ed": 0.4, "Community-Serve": 0.3, "Counseling": 0.25, "Conventional": 0.2}},
            {"option_id": 63, "option_text": "I practice over and over until the formulas make sense",
             "trait_tags": {"Analytical-Skill": 1.0, "Data-Analytics": 0.45, "Investigative": 0.4, "Technical-Skill": 0.3, "Finance-Acct": 0.25, "Lab-Research": 0.2}},
            {"option_id": 64, "option_text": "I ask the teacher for extra help or attend remedial classes",
             "trait_tags": {"Conventional": 1.0, "Teaching-Ed": 0.4, "People-Skill": 0.35, "Admin-Skill": 0.35, "Community-Serve": 0.25, "Social": 0.2}},
            {"option_id": 65, "option_text": "I try to connect it to something real-world that I care about",
             "trait_tags": {"Creative-Skill": 1.0, "Artistic": 0.4, "Investigative": 0.35, "Field-Research": 0.3, "Environmental-Sci": 0.2, "Realistic": 0.15}},
            {"option_id": 66, "option_text": "I make flashcards, summaries, or organized review notes",
             "trait_tags": {"Admin-Skill": 1.0, "Conventional": 0.5, "Analytical-Skill": 0.4, "Teaching-Ed": 0.3, "Finance-Acct": 0.25, "Data-Analytics": 0.2}},
            {"option_id": 67, "option_text": "I try hands-on experiments or build models to understand it",
             "trait_tags": {"Lab-Research": 1.0, "Technical-Skill": 0.5, "Mechanical-Design": 0.4, "Hardware-Systems": 0.3, "Realistic": 0.25, "Civil-Build": 0.2}},
            {"option_id": 68, "option_text": "I look for the easier parts first and build confidence from there",
             "trait_tags": {"Enterprising": 1.0, "Startup-Venture": 0.35, "People-Skill": 0.3, "Marketing-Sales": 0.3, "Admin-Skill": 0.25, "Hospitality-Svc": 0.2}},
            {"option_id": 69, "option_text": "I push through with physical activity breaks to stay focused",
             "trait_tags": {"Physical-Skill": 1.0, "Realistic": 0.45, "Sports-Ed": 0.35, "Rehab-Therapy": 0.3, "Law-Enforce": 0.25, "Patient-Care": 0.2}},
            {"option_id": 70, "option_text": "Honestly, I just focus more on the subjects I'm already good at",
             "trait_tags": {"Artistic": 1.0, "Creative-Skill": 0.4, "Performing-Arts": 0.35, "Visual-Design": 0.3, "Digital-Media": 0.25, "Music-Audio": 0.2}},
        ],
    },

    # ── 3. Replace Q52 (Board Exam dup) ──
    # Original Q36 asks "Which board exam would you take?" — this asks about
    # their ATTITUDE toward professional certification & studying for it.
    {
        "question_id": 52,
        "question_text": "How do you feel about spending years studying for a professional licensure exam?",
        "category": "Professional Commitment",
        "options": [
            {"option_id": 75, "option_text": "I'd gladly do it if it means I'll save lives as a nurse or doctor",
             "trait_tags": {"Patient-Care": 1.0, "Medical-Lab": 0.45, "People-Skill": 0.4, "Rehab-Therapy": 0.35, "Social": 0.2, "Community-Serve": 0.2}},
            {"option_id": 76, "option_text": "I'd commit if it leads to a respected career in accounting or finance",
             "trait_tags": {"Finance-Acct": 1.0, "Conventional": 0.5, "Analytical-Skill": 0.45, "Admin-Skill": 0.35, "Enterprising": 0.2, "Investigative": 0.15}},
            {"option_id": 77, "option_text": "Studying for an engineering board exam sounds like a worthy challenge",
             "trait_tags": {"Civil-Build": 1.0, "Technical-Skill": 0.5, "Analytical-Skill": 0.4, "Mechanical-Design": 0.35, "Electrical-Power": 0.25, "Realistic": 0.2}},
            {"option_id": 78, "option_text": "I'd study hard to become a licensed teacher and shape young minds",
             "trait_tags": {"Teaching-Ed": 1.0, "Community-Serve": 0.45, "Social": 0.4, "People-Skill": 0.35, "Conventional": 0.25, "Counseling": 0.2}},
            {"option_id": 79, "option_text": "I'd train for a criminology exam if it meant serving justice",
             "trait_tags": {"Law-Enforce": 1.0, "Investigative": 0.5, "Community-Serve": 0.4, "Forensic-Sci": 0.3, "Physical-Skill": 0.25, "Realistic": 0.2}},
            {"option_id": 80, "option_text": "The pharmacy or med-tech board exam suits my love for lab work",
             "trait_tags": {"Medical-Lab": 1.0, "Lab-Research": 0.5, "Analytical-Skill": 0.45, "Investigative": 0.35, "Patient-Care": 0.25, "Technical-Skill": 0.2}},
            {"option_id": 81, "option_text": "I'd take the architecture board exam to bring designs to life",
             "trait_tags": {"Spatial-Design": 1.0, "Artistic": 0.45, "Creative-Skill": 0.4, "Civil-Build": 0.3, "Visual-Design": 0.25, "Technical-Skill": 0.2}},
            {"option_id": 82, "option_text": "I'd prepare for the PT/OT exam because I want to help people recover",
             "trait_tags": {"Rehab-Therapy": 1.0, "Physical-Skill": 0.5, "Patient-Care": 0.45, "People-Skill": 0.35, "Medical-Lab": 0.2, "Analytical-Skill": 0.15}},
            {"option_id": 83, "option_text": "I'd rather skip the board exam and go straight into tech or business",
             "trait_tags": {"Software-Dev": 1.0, "Enterprising": 0.45, "Technical-Skill": 0.4, "Startup-Venture": 0.35, "Digital-Media": 0.25, "Data-Analytics": 0.2}},
            {"option_id": 84, "option_text": "I haven't thought about it yet — I want to explore my options first",
             "trait_tags": {"Creative-Skill": 1.0, "Artistic": 0.35, "Investigative": 0.3, "Performing-Arts": 0.3, "Tourism-Travel": 0.25, "Hospitality-Svc": 0.2}},
        ],
    },

    # ── 4. Replace Q414 (Law - Area of Interest dup) ──
    # Original Q275 asks "What area of law interests you?" — this asks
    # what MOTIVATES them to consider a legal career.
    {
        "question_id": 414,
        "question_text": "What motivates you most about pursuing a career in law or criminal justice?",
        "category": "Law - Motivation",
        "options": [
            {"option_id": 85, "option_text": "Standing up in court and arguing for what's right",
             "trait_tags": {"Legal-Practice": 1.0, "People-Skill": 0.5, "Enterprising": 0.4, "Community-Serve": 0.3}},
            {"option_id": 86, "option_text": "Investigating crimes and piecing together evidence",
             "trait_tags": {"Law-Enforce": 1.0, "Forensic-Sci": 0.6, "Investigative": 0.5, "Analytical-Skill": 0.3}},
            {"option_id": 87, "option_text": "Helping everyday people understand and protect their rights",
             "trait_tags": {"Community-Serve": 1.0, "Legal-Practice": 0.6, "Social": 0.5, "People-Skill": 0.3}},
            {"option_id": 88, "option_text": "Drafting contracts and advising companies on compliance",
             "trait_tags": {"Legal-Practice": 0.9, "Finance-Acct": 0.6, "Admin-Skill": 0.5, "Conventional": 0.25}},
            {"option_id": 89, "option_text": "Fighting corruption and holding powerful people accountable",
             "trait_tags": {"Law-Enforce": 0.9, "Community-Serve": 0.7, "Investigative": 0.5, "Social": 0.25}},
            {"option_id": 90, "option_text": "Using technology to solve cybercrimes and protect digital privacy",
             "trait_tags": {"Cyber-Defense": 1.0, "Legal-Practice": 0.5, "Technical-Skill": 0.5, "Software-Dev": 0.3}},
        ],
    },

    # ── 5. Replace Q633 (Interest - Legal Practice dup) ──
    # Original Q275 asks "What area of law interests you?" — this asks
    # what TYPE OF LEGAL WORK ENVIRONMENT they prefer.
    {
        "question_id": 633,
        "question_text": "In what setting would you most want to practice law or justice work?",
        "category": "Career - Legal Setting",
        "options": [
            {"option_id": 91, "option_text": "A busy courtroom handling criminal or civil trials",
             "trait_tags": {"Legal-Practice": 1.0, "Law-Enforce": 0.5, "People-Skill": 0.5, "Enterprising": 0.25}},
            {"option_id": 92, "option_text": "A corporate office advising a major business on legal strategy",
             "trait_tags": {"Legal-Practice": 0.9, "Finance-Acct": 0.6, "Admin-Skill": 0.5, "Enterprising": 0.25}},
            {"option_id": 93, "option_text": "A forensic lab analyzing evidence from crime scenes",
             "trait_tags": {"Forensic-Sci": 1.0, "Lab-Research": 0.6, "Law-Enforce": 0.5, "Investigative": 0.3}},
            {"option_id": 94, "option_text": "A community legal aid office serving underprivileged clients",
             "trait_tags": {"Community-Serve": 1.0, "Legal-Practice": 0.6, "Social-Work": 0.5, "People-Skill": 0.3}},
            {"option_id": 95, "option_text": "A government agency creating policies and writing legislation",
             "trait_tags": {"Legal-Practice": 0.8, "Admin-Skill": 0.6, "Community-Serve": 0.5, "Writing-Comm": 0.3}},
            {"option_id": 96, "option_text": "In the field — conducting investigations or intelligence operations",
             "trait_tags": {"Law-Enforce": 1.0, "Physical-Skill": 0.5, "Investigative": 0.5, "Realistic": 0.25}},
        ],
    },

    # ── 6. Replace Q634 (Career - Legal Practice dup) ──
    # Original Q418 asks "Which legal career path?" — this asks
    # what SKILL they would develop first in a legal career.
    {
        "question_id": 634,
        "question_text": "If you were starting a legal career, which skill would you want to master first?",
        "category": "Law - Skill Development",
        "options": [
            {"option_id": 97, "option_text": "Public speaking and persuasive argumentation",
             "trait_tags": {"Legal-Practice": 1.0, "People-Skill": 0.6, "Enterprising": 0.4, "Writing-Comm": 0.3}},
            {"option_id": 98, "option_text": "Critical analysis of legal documents and case precedent",
             "trait_tags": {"Analytical-Skill": 1.0, "Legal-Practice": 0.6, "Investigative": 0.5, "Conventional": 0.25}},
            {"option_id": 99, "option_text": "Crime scene investigation and forensic evidence handling",
             "trait_tags": {"Forensic-Sci": 1.0, "Law-Enforce": 0.6, "Lab-Research": 0.4, "Investigative": 0.3}},
            {"option_id": 100, "option_text": "Negotiation and conflict mediation between disputing parties",
             "trait_tags": {"People-Skill": 1.0, "Legal-Practice": 0.6, "Counseling": 0.5, "Social": 0.25}},
            {"option_id": 101, "option_text": "Digital forensics and cybercrime investigation techniques",
             "trait_tags": {"Cyber-Defense": 1.0, "Software-Dev": 0.5, "Law-Enforce": 0.5, "Technical-Skill": 0.3}},
            {"option_id": 102, "option_text": "Legal writing — drafting briefs, contracts, and legislation",
             "trait_tags": {"Writing-Comm": 1.0, "Legal-Practice": 0.6, "Admin-Skill": 0.4, "Conventional": 0.3}},
        ],
    },

    # ── 7. Replace Q639 (Interest - Tourism & Travel dup) ──
    # Original Q438 asks "Which tourism sector?" — this asks about
    # what CHALLENGE in Philippine tourism they'd solve.
    {
        "question_id": 639,
        "question_text": "If you could improve one thing about the Philippine travel and tourism industry, what would it be?",
        "category": "Interest - Tourism Development",
        "options": [
            {"option_id": 103, "option_text": "Creating better eco-tourism programs that protect natural wonders",
             "trait_tags": {"Tourism-Travel": 1.0, "Environmental-Sci": 0.6, "Community-Serve": 0.4, "Agri-Nature": 0.3}},
            {"option_id": 104, "option_text": "Training more world-class Filipino chefs and hospitality professionals",
             "trait_tags": {"Hospitality-Svc": 1.0, "Culinary-Arts": 0.5, "Teaching-Ed": 0.4, "People-Skill": 0.3}},
            {"option_id": 105, "option_text": "Building a travel app that makes island-hopping easier for tourists",
             "trait_tags": {"Software-Dev": 1.0, "Tourism-Travel": 0.5, "Digital-Media": 0.4, "Technical-Skill": 0.3}},
            {"option_id": 106, "option_text": "Promoting local festivals and cultural heritage to international visitors",
             "trait_tags": {"Marketing-Sales": 1.0, "Tourism-Travel": 0.6, "Creative-Skill": 0.4, "Community-Serve": 0.3}},
            {"option_id": 107, "option_text": "Designing luxury resorts that blend modern comfort with nature",
             "trait_tags": {"Spatial-Design": 1.0, "Tourism-Travel": 0.5, "Hospitality-Svc": 0.5, "Creative-Skill": 0.3}},
            {"option_id": 108, "option_text": "Organizing adventure tours like diving, hiking, and surfing packages",
             "trait_tags": {"Tourism-Travel": 0.9, "Physical-Skill": 0.6, "Enterprising": 0.4, "People-Skill": 0.3}},
        ],
    },

    # ── 8. Replace Q642 (Interest - Culinary Arts dup) ──
    # Original Q424 asks "Which culinary specialization?" — this asks
    # about what FOOD EXPERIENCE they'd create.
    {
        "question_id": 642,
        "question_text": "If you could create any food-related experience, what would it be?",
        "category": "Interest - Food Innovation",
        "options": [
            {"option_id": 109, "option_text": "A pop-up restaurant showcasing modern Filipino cuisine",
             "trait_tags": {"Culinary-Arts": 1.0, "Creative-Skill": 0.5, "Startup-Venture": 0.4, "Hospitality-Svc": 0.3}},
            {"option_id": 110, "option_text": "A food science lab developing healthier versions of local snacks",
             "trait_tags": {"Food-Science": 1.0, "Lab-Research": 0.5, "Nutrition-Diet": 0.5, "Investigative": 0.25}},
            {"option_id": 111, "option_text": "A cooking show or food vlog reviewing street food across provinces",
             "trait_tags": {"Culinary-Arts": 0.8, "Digital-Media": 0.7, "Creative-Skill": 0.4, "Tourism-Travel": 0.3}},
            {"option_id": 112, "option_text": "A farm-to-table cooperative connecting local farmers to restaurants",
             "trait_tags": {"Agri-Nature": 1.0, "Culinary-Arts": 0.5, "Community-Serve": 0.5, "Enterprising": 0.25}},
            {"option_id": 113, "option_text": "A pastry shop famous for unique desserts and custom cakes",
             "trait_tags": {"Culinary-Arts": 1.0, "Artistic": 0.5, "Creative-Skill": 0.5, "Visual-Design": 0.3}},
            {"option_id": 114, "option_text": "A hotel kitchen where I manage a team preparing banquet menus",
             "trait_tags": {"Hospitality-Svc": 1.0, "Culinary-Arts": 0.6, "Admin-Skill": 0.5, "People-Skill": 0.25}},
        ],
    },

    # ── 9. Replace Q919 (Engineering General dup — "type of engineer") ──
    # Original Q861 asks "What type of engineer do you admire?" — this asks
    # what REAL-WORLD PROBLEM they'd solve with engineering.
    {
        "question_id": 919,
        "question_text": "If you were an engineer, what real-world problem would you want to solve first?",
        "category": "Academic Interest - Engineering Application",
        "options": [
            {"option_id": 115, "option_text": "Designing earthquake-resistant buildings for Philippine cities",
             "trait_tags": {"Civil-Build": 1.0, "Analytical-Skill": 0.5, "Technical-Skill": 0.4, "Spatial-Design": 0.3, "Realistic": 0.25}},
            {"option_id": 116, "option_text": "Developing renewable energy systems to reduce power costs",
             "trait_tags": {"Electrical-Power": 1.0, "Environmental-Eng": 0.5, "Technical-Skill": 0.45, "Investigative": 0.3, "Environmental-Sci": 0.25}},
            {"option_id": 117, "option_text": "Building affordable medical devices for rural health clinics",
             "trait_tags": {"Mechanical-Design": 1.0, "Medical-Lab": 0.5, "Patient-Care": 0.4, "Technical-Skill": 0.3, "Community-Serve": 0.25}},
            {"option_id": 118, "option_text": "Automating factory processes to make manufacturing more efficient",
             "trait_tags": {"Industrial-Ops": 1.0, "Hardware-Systems": 0.5, "Software-Dev": 0.4, "Mechanical-Design": 0.3, "Technical-Skill": 0.25}},
            {"option_id": 119, "option_text": "Cleaning polluted rivers and creating sustainable waste systems",
             "trait_tags": {"Environmental-Eng": 1.0, "Environmental-Sci": 0.5, "Community-Serve": 0.4, "Technical-Skill": 0.3, "Field-Research": 0.25}},
            {"option_id": 120, "option_text": "Programming drones or robots for disaster rescue operations",
             "trait_tags": {"Aeronautical-Eng": 1.0, "Software-Dev": 0.5, "Hardware-Systems": 0.4, "Technical-Skill": 0.35, "Mechanical-Design": 0.25}},
        ],
    },

    # ── 10. Replace Q920 (Engineering General dup — "engineering subject") ──
    # Original Q864 asks "Which engineering subject?" — this asks about
    # what HANDS-ON engineering project excites them.
    {
        "question_id": 920,
        "question_text": "Which hands-on engineering project would you sign up for first?",
        "category": "Academic Interest - Engineering Projects",
        "options": [
            {"option_id": 121, "option_text": "Building a small concrete bridge and testing how much weight it holds",
             "trait_tags": {"Civil-Build": 1.0, "Analytical-Skill": 0.5, "Technical-Skill": 0.4, "Mechanical-Design": 0.3, "Realistic": 0.25}},
            {"option_id": 122, "option_text": "Assembling and programming a robot to navigate a maze",
             "trait_tags": {"Hardware-Systems": 1.0, "Software-Dev": 0.5, "Mechanical-Design": 0.4, "Technical-Skill": 0.35, "Electronics-Dev": 0.25}},
            {"option_id": 123, "option_text": "Wiring a solar panel system to power a model house",
             "trait_tags": {"Electrical-Power": 1.0, "Electronics-Dev": 0.5, "Environmental-Eng": 0.4, "Technical-Skill": 0.35, "Analytical-Skill": 0.25}},
            {"option_id": 124, "option_text": "Designing and 3D-printing a prototype of a product you invented",
             "trait_tags": {"Mechanical-Design": 1.0, "Creative-Skill": 0.5, "Spatial-Design": 0.45, "Technical-Skill": 0.35, "Software-Dev": 0.25}},
            {"option_id": 125, "option_text": "Building a water filtration system from recycled materials",
             "trait_tags": {"Environmental-Eng": 1.0, "Environmental-Sci": 0.5, "Technical-Skill": 0.4, "Community-Serve": 0.3, "Investigative": 0.25}},
            {"option_id": 126, "option_text": "Disassembling a car engine and putting it back together",
             "trait_tags": {"Mechanical-Design": 1.0, "Technical-Skill": 0.5, "Realistic": 0.45, "Investigative": 0.3, "Industrial-Ops": 0.25}},
        ],
    },

    # ── 11. Replace Q911 (Geodetic & Surveying dup) ──
    # Original Q853 asks "What interests you about geodetic...?" — this asks
    # what CAREER OUTCOME in geodetic engineering appeals to them.
    {
        "question_id": 911,
        "question_text": "What career path in geodetic engineering and surveying appeals to you most?",
        "category": "Academic Interest - Geodetic Careers",
        "options": [
            {"option_id": 127, "option_text": "Leading survey teams for large infrastructure projects like highways",
             "trait_tags": {"Field-Research": 1.0, "Civil-Build": 0.5, "Admin-Skill": 0.4, "Realistic": 0.35, "Technical-Skill": 0.25}},
            {"option_id": 128, "option_text": "Operating satellite and drone systems for precision agriculture mapping",
             "trait_tags": {"Technical-Skill": 1.0, "Aeronautical-Eng": 0.5, "Agri-Nature": 0.4, "Data-Analytics": 0.35, "Field-Research": 0.25}},
            {"option_id": 129, "option_text": "Developing GIS software that city planners use for zoning decisions",
             "trait_tags": {"Software-Dev": 1.0, "Data-Analytics": 0.5, "Civil-Build": 0.4, "Field-Research": 0.3, "Technical-Skill": 0.25}},
            {"option_id": 130, "option_text": "Monitoring volcanic activity and earthquake fault lines",
             "trait_tags": {"Field-Research": 1.0, "Investigative": 0.5, "Environmental-Sci": 0.5, "Analytical-Skill": 0.3, "Technical-Skill": 0.25}},
            {"option_id": 131, "option_text": "Working as a licensed geodetic engineer resolving land boundary disputes",
             "trait_tags": {"Field-Research": 1.0, "Legal-Practice": 0.5, "People-Skill": 0.4, "Analytical-Skill": 0.35, "Civil-Build": 0.25}},
            {"option_id": 132, "option_text": "Creating detailed 3D terrain models from LIDAR and photogrammetry data",
             "trait_tags": {"Data-Analytics": 1.0, "Technical-Skill": 0.5, "Visual-Design": 0.4, "Field-Research": 0.35, "Software-Dev": 0.25}},
        ],
    },

    # ── 12. Replace Q915 (Aircraft Maintenance & Avionics dup) ──
    # Original Q857 asks "What interests you about aircraft...?" — this asks
    # what they'd PRIORITIZE in an aircraft maintenance career.
    {
        "question_id": 915,
        "question_text": "What would you focus on if you worked in the aircraft maintenance industry?",
        "category": "Academic Interest - Aviation Focus",
        "options": [
            {"option_id": 133, "option_text": "Becoming certified to sign off that an aircraft is safe to fly",
             "trait_tags": {"Aeronautical-Eng": 1.0, "Admin-Skill": 0.5, "Legal-Practice": 0.4, "Analytical-Skill": 0.35, "Technical-Skill": 0.25}},
            {"option_id": 134, "option_text": "Specializing in jet engine overhaul and performance tuning",
             "trait_tags": {"Mechanical-Design": 1.0, "Aeronautical-Eng": 0.5, "Technical-Skill": 0.5, "Realistic": 0.3, "Investigative": 0.25}},
            {"option_id": 135, "option_text": "Working on next-gen avionics like digital fly-by-wire systems",
             "trait_tags": {"Electronics-Dev": 1.0, "Software-Dev": 0.5, "Aeronautical-Eng": 0.45, "Technical-Skill": 0.3, "Data-Analytics": 0.25}},
            {"option_id": 136, "option_text": "Using predictive data to schedule maintenance before parts fail",
             "trait_tags": {"Data-Analytics": 1.0, "Aeronautical-Eng": 0.5, "Software-Dev": 0.4, "Analytical-Skill": 0.35, "Technical-Skill": 0.25}},
            {"option_id": 137, "option_text": "Training the next generation of aircraft maintenance technicians",
             "trait_tags": {"Teaching-Ed": 1.0, "Aeronautical-Eng": 0.5, "People-Skill": 0.45, "Technical-Skill": 0.35, "Community-Serve": 0.25}},
            {"option_id": 138, "option_text": "Investigating aircraft incidents and writing safety improvement reports",
             "trait_tags": {"Investigative": 1.0, "Aeronautical-Eng": 0.5, "Analytical-Skill": 0.5, "Writing-Comm": 0.3, "Admin-Skill": 0.25}},
        ],
    },

    # ── 13. Replace Q2031 (Aircraft Maintenance expansion dup) ──
    # This was an expansion duplicate of Q857. New angle: SCENARIO-based.
    {
        "question_id": 6,
        "question_text": "SCENARIO: A grounded aircraft needs to be cleared for its next flight by tomorrow morning. Which task would you volunteer for?",
        "category": "Academic Interest - Aircraft Maintenance & Avionics",
        "options": [
            {"option_id": 139, "option_text": "Running diagnostics on the engine control unit and turbine sensors",
             "trait_tags": {"Aeronautical-Eng": 1.0, "Mechanical-Design": 0.5, "Technical-Skill": 0.45, "Investigative": 0.3, "Analytical-Skill": 0.25}},
            {"option_id": 140, "option_text": "Checking all navigation and communication systems in the cockpit",
             "trait_tags": {"Electronics-Dev": 1.0, "Aeronautical-Eng": 0.5, "Hardware-Systems": 0.45, "Technical-Skill": 0.3, "Analytical-Skill": 0.25}},
            {"option_id": 141, "option_text": "Inspecting the airframe, landing gear, and hydraulic lines",
             "trait_tags": {"Mechanical-Design": 1.0, "Aeronautical-Eng": 0.5, "Realistic": 0.45, "Technical-Skill": 0.3, "Physical-Skill": 0.25}},
            {"option_id": 142, "option_text": "Reviewing the flight data logs for any anomalies to investigate",
             "trait_tags": {"Data-Analytics": 1.0, "Investigative": 0.5, "Aeronautical-Eng": 0.45, "Analytical-Skill": 0.35, "Software-Dev": 0.25}},
            {"option_id": 143, "option_text": "Coordinating the maintenance crew's tasks and signing off the work order",
             "trait_tags": {"Admin-Skill": 1.0, "Aeronautical-Eng": 0.5, "People-Skill": 0.45, "Legal-Practice": 0.3, "Conventional": 0.25}},
            {"option_id": 144, "option_text": "Testing and recalibrating the autopilot and weather radar systems",
             "trait_tags": {"Electronics-Dev": 1.0, "Software-Dev": 0.5, "Aeronautical-Eng": 0.45, "Data-Analytics": 0.3, "Technical-Skill": 0.25}},
        ],
    },

    # ── 14. Replace Q2781 (Theater & Performing Arts expansion dup) ──
    # This was an expansion duplicate of Q940. New angle: what they'd
    # CREATE or PRODUCE in performing arts.
    {
        "question_id": 7,
        "question_text": "If you had the resources to create any performing arts production, what would you choose?",
        "category": "Academic Interest - Theater & Performing Arts",
        "options": [
            {"option_id": 145, "option_text": "A musical that fuses traditional Filipino folk stories with modern music",
             "trait_tags": {"Performing-Arts": 1.0, "Music-Audio": 0.5, "Creative-Skill": 0.45, "Writing-Comm": 0.3, "Community-Serve": 0.25}},
            {"option_id": 146, "option_text": "A dance show combining hip-hop, contemporary, and cultural dance forms",
             "trait_tags": {"Performing-Arts": 1.0, "Physical-Skill": 0.5, "Creative-Skill": 0.45, "Artistic": 0.35, "People-Skill": 0.25}},
            {"option_id": 147, "option_text": "A drama series dealing with real social issues affecting Filipino youth",
             "trait_tags": {"Writing-Comm": 1.0, "Performing-Arts": 0.5, "Social": 0.45, "Community-Serve": 0.35, "People-Skill": 0.25}},
            {"option_id": 148, "option_text": "An immersive theater experience where the audience walks through the set",
             "trait_tags": {"Spatial-Design": 1.0, "Performing-Arts": 0.5, "Creative-Skill": 0.5, "Artistic": 0.3, "Technical-Skill": 0.25}},
            {"option_id": 149, "option_text": "A one-person comedy show that I write and perform myself",
             "trait_tags": {"Performing-Arts": 1.0, "Creative-Skill": 0.5, "People-Skill": 0.5, "Writing-Comm": 0.3, "Enterprising": 0.25}},
            {"option_id": 150, "option_text": "A large-scale production where I manage lights, sound, and stage crew",
             "trait_tags": {"Admin-Skill": 1.0, "Technical-Skill": 0.5, "Performing-Arts": 0.45, "Conventional": 0.3, "People-Skill": 0.25}},
        ],
    },
]


# ═══════════════════════════════════════════════════════════════
# VERIFICATION & INSERTION
# ═══════════════════════════════════════════════════════════════

def main():
    from data.questions_enhanced import QUESTIONS_POOL_ENHANCED

    # 1. Verify no ID collisions
    used_qids = {q["question_id"] for q in QUESTIONS_POOL_ENHANCED}
    used_oids = set()
    for q in QUESTIONS_POOL_ENHANCED:
        for o in q.get("options", []):
            used_oids.add(o["option_id"])

    print(f"Current pool: {len(QUESTIONS_POOL_ENHANCED)} questions")

    collisions = False
    for nq in NEW_QUESTIONS:
        if nq["question_id"] in used_qids:
            print(f"  COLLISION: question_id {nq['question_id']} already in use!")
            collisions = True
        for o in nq["options"]:
            if o["option_id"] in used_oids:
                print(f"  COLLISION: option_id {o['option_id']} already in use!")
                collisions = True

    if collisions:
        print("ABORTING — fix collisions before proceeding.")
        return

    print("  No ID collisions found.")

    # 2. Convert to Python source code
    def dict_to_source(d, indent=4):
        """Convert a question dict to Python source code string."""
        lines = []
        sp = " " * indent
        lines.append(f"{sp}{{")
        lines.append(f'{sp}    "question_id": {d["question_id"]},')
        lines.append(f'{sp}    "question_text": {json.dumps(d["question_text"])},')
        lines.append(f'{sp}    "category": {json.dumps(d["category"])},')
        lines.append(f'{sp}    "options": [')
        for opt in d["options"]:
            trait_str = json.dumps(opt["trait_tags"])
            # Make trait_tags use single quotes like existing code? No, double is fine.
            lines.append(
                f'{sp}        {{"option_id": {opt["option_id"]}, '
                f'"option_text": {json.dumps(opt["option_text"])}, '
                f'"trait_tags": {trait_str}}},'
            )
        lines.append(f"{sp}    ]")
        lines.append(f"{sp}}},")
        return "\n".join(lines)

    source_blocks = []
    for nq in NEW_QUESTIONS:
        source_blocks.append(dict_to_source(nq))

    insert_code = "\n".join(source_blocks) + "\n"

    # 3. Insert before the expansion functions
    filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "questions_enhanced.py")
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Find the closing bracket of the static QUESTIONS_POOL_ENHANCED list
    # It's the "]" right before the expansion code
    # Look for the pattern: end of last static question followed by ]
    # The expansion code starts with a function def or comment
    marker = "\n# ══════════════════════"
    # Actually, find the builder function
    marker = "\ndef _build_science_interest_expansion"
    marker_pos = content.find(marker)
    if marker_pos == -1:
        print("ERROR: Could not find expansion marker in file!")
        return

    # The list closing ']' should be just before this function
    # Find the last ']' before the marker
    bracket_pos = content.rfind("]", 0, marker_pos)
    if bracket_pos == -1:
        print("ERROR: Could not find list closing bracket!")
        return

    # Insert the new questions just before the closing bracket
    new_content = content[:bracket_pos] + insert_code + content[bracket_pos:]

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"  Inserted {len(NEW_QUESTIONS)} new questions into file.")

    # 4. Verify by reimporting
    import importlib
    for k in list(sys.modules.keys()):
        if "data" in k or "questions" in k:
            del sys.modules[k]

    from data.questions_enhanced import QUESTIONS_POOL_ENHANCED as UPDATED
    print(f"  New pool: {len(UPDATED)} questions")

    new_ids = {nq["question_id"] for nq in NEW_QUESTIONS}
    found = {q["question_id"] for q in UPDATED if q["question_id"] in new_ids}
    missing = new_ids - found
    if missing:
        print(f"  MISSING after insert: {missing}")
    else:
        print(f"  All {len(NEW_QUESTIONS)} new questions verified in pool!")


if __name__ == "__main__":
    main()
