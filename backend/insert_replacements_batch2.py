"""
Insert 15 replacement questions (Batch 2) into questions_enhanced.py to replace
deleted duplicates.  Each question covers the SAME topic area as the one it
replaces but uses a completely different angle / question text / option wording.

Using IDs 8-22 (free gap in static pool, below all expansion ranges):
  8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
  18, 19, 20, 21, 22

Option IDs:
  151–216  (free gap between batch-1 replacements and static pool)
  26839–26862  (above current max option_id)
"""

import sys, os, re, json

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# ═══════════════════════════════════════════════════════════════
# 15 REPLACEMENT QUESTIONS — BATCH 2
# ═══════════════════════════════════════════════════════════════

NEW_QUESTIONS = [

    # ── 1. Replace Q104 (Situational - Family Business dup) ──
    # Existing Q87 asks "How would you contribute?" (role-based).
    # Removed Q104 was "What role would you take?" (same angle).
    # NEW ANGLE: turnaround STRATEGY — what approach would you try?
    {
        "question_id": 8,
        "question_text": "Your family's small business is losing customers. What strategy would you suggest to turn things around?",
        "category": "Situational - Business Strategy",
        "options": [
            {"option_id": 151, "option_text": "Revamp the branding and create eye-catching social media campaigns",
             "trait_tags": {"Marketing-Sales": 1.0, "Visual-Design": 0.5, "Digital-Media": 0.4, "Creative-Skill": 0.35, "Enterprising": 0.25}},
            {"option_id": 152, "option_text": "Analyze the finances and cut unnecessary costs to stay afloat",
             "trait_tags": {"Finance-Acct": 1.0, "Analytical-Skill": 0.5, "Admin-Skill": 0.4, "Conventional": 0.35, "Investigative": 0.2}},
            {"option_id": 153, "option_text": "Talk to customers directly and find out what they really need",
             "trait_tags": {"People-Skill": 1.0, "Social": 0.5, "Community-Serve": 0.4, "Counseling": 0.3, "Marketing-Sales": 0.25}},
            {"option_id": 154, "option_text": "Build a website and set up online ordering or delivery services",
             "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.5, "Digital-Media": 0.4, "Startup-Venture": 0.3, "Enterprising": 0.25}},
            {"option_id": 155, "option_text": "Improve the product quality and introduce something new to the menu or lineup",
             "trait_tags": {"Startup-Venture": 1.0, "Creative-Skill": 0.5, "Culinary-Arts": 0.35, "Enterprising": 0.3, "Investigative": 0.25}},
            {"option_id": 156, "option_text": "Streamline operations — fix the inventory, scheduling, and workflow",
             "trait_tags": {"Admin-Skill": 1.0, "Industrial-Ops": 0.5, "Conventional": 0.45, "Analytical-Skill": 0.35, "Finance-Acct": 0.2}},
        ],
    },

    # ── 2. Replace Q465 (Medical Laboratory dup) ──
    # Existing questions ask about sample types, motivation, workplace, quality, tech.
    # Removed Q465 was "Which medical laboratory specialization excites you most?"
    # NEW ANGLE: critical-thinking SCENARIO about inconsistent lab results.
    {
        "question_id": 9,
        "question_text": "SCENARIO: A lab test result doesn't match a patient's symptoms. What's your first move?",
        "category": "Academic Interest - Medical Technology & Lab Science",
        "options": [
            {"option_id": 157, "option_text": "Rerun the test with a fresh sample to rule out contamination",
             "trait_tags": {"Medical-Lab": 1.0, "Analytical-Skill": 0.5, "Lab-Research": 0.45, "Investigative": 0.35, "Conventional": 0.2}},
            {"option_id": 158, "option_text": "Check the equipment calibration logs for any recent anomalies",
             "trait_tags": {"Technical-Skill": 1.0, "Medical-Lab": 0.5, "Analytical-Skill": 0.45, "Hardware-Systems": 0.3, "Investigative": 0.25}},
            {"option_id": 159, "option_text": "Review the patient's medication list — drugs can skew test results",
             "trait_tags": {"Patient-Care": 1.0, "Medical-Lab": 0.5, "Investigative": 0.45, "Analytical-Skill": 0.3, "Counseling": 0.2}},
            {"option_id": 160, "option_text": "Consult the pathologist and discuss whether additional tests are needed",
             "trait_tags": {"People-Skill": 1.0, "Medical-Lab": 0.5, "Lab-Research": 0.4, "Social": 0.3, "Community-Serve": 0.2}},
            {"option_id": 161, "option_text": "Cross-reference the result with related biomarkers for a fuller picture",
             "trait_tags": {"Data-Analytics": 1.0, "Medical-Lab": 0.5, "Analytical-Skill": 0.45, "Lab-Research": 0.35, "Investigative": 0.25}},
            {"option_id": 162, "option_text": "Document everything carefully and flag it in the lab information system",
             "trait_tags": {"Admin-Skill": 1.0, "Conventional": 0.5, "Medical-Lab": 0.45, "Technical-Skill": 0.3, "Analytical-Skill": 0.2}},
        ],
    },

    # ── 3. Replace Q599 (Performing Arts dup) ──
    # Existing Q931 asks "What draws you to music and performance?"
    # Replacement Q7 asks "What production would you create?"
    # Removed Q599 was "What performing arts discipline appeals to you?"
    # NEW ANGLE: What CHALLENGE in Philippine performing arts would you address?
    {
        "question_id": 10,
        "question_text": "What challenge facing Philippine performing arts would you most want to address?",
        "category": "Academic Interest - Theater & Performing Arts",
        "options": [
            {"option_id": 163, "option_text": "Making theater affordable so more Filipinos can experience live shows",
             "trait_tags": {"Performing-Arts": 1.0, "Community-Serve": 0.5, "People-Skill": 0.4, "Social": 0.35, "Enterprising": 0.2}},
            {"option_id": 164, "option_text": "Preserving traditional Filipino dances and folk music for future generations",
             "trait_tags": {"Performing-Arts": 1.0, "Teaching-Ed": 0.5, "Community-Serve": 0.45, "Creative-Skill": 0.3, "Writing-Comm": 0.2}},
            {"option_id": 165, "option_text": "Creating original Filipino musicals that can compete on the world stage",
             "trait_tags": {"Creative-Skill": 1.0, "Performing-Arts": 0.5, "Music-Audio": 0.45, "Writing-Comm": 0.35, "Artistic": 0.25}},
            {"option_id": 166, "option_text": "Training young performers who can't afford formal arts education",
             "trait_tags": {"Teaching-Ed": 1.0, "Community-Serve": 0.5, "Performing-Arts": 0.45, "People-Skill": 0.35, "Social": 0.25}},
            {"option_id": 167, "option_text": "Using digital platforms to stream and promote local productions online",
             "trait_tags": {"Digital-Media": 1.0, "Performing-Arts": 0.5, "Software-Dev": 0.4, "Marketing-Sales": 0.35, "Technical-Skill": 0.25}},
            {"option_id": 168, "option_text": "Building better performance venues and improving stage technology",
             "trait_tags": {"Spatial-Design": 1.0, "Technical-Skill": 0.5, "Performing-Arts": 0.45, "Mechanical-Design": 0.3, "Admin-Skill": 0.25}},
        ],
    },

    # ── 4. Replace Q774 (Nutrition & Dietetics dup) ──
    # Existing questions cover interest, counseling, research, workplace, meal planning, challenges.
    # Removed Q774 was "Where would you work as a nutritionist?"
    # NEW ANGLE: SCENARIO about designing a nutrition program for a specific population.
    {
        "question_id": 11,
        "question_text": "SCENARIO: You're assigned to design a nutrition program for a Filipino community. Who would you focus on?",
        "category": "Academic Interest - Nutrition & Dietetics",
        "options": [
            {"option_id": 169, "option_text": "Malnourished children in low-income barangays",
             "trait_tags": {"Nutrition-Diet": 1.0, "Community-Serve": 0.5, "Patient-Care": 0.4, "Social": 0.35, "People-Skill": 0.25}},
            {"option_id": 170, "option_text": "Student athletes who need performance-based meal plans",
             "trait_tags": {"Nutrition-Diet": 1.0, "Sports-Ed": 0.5, "Physical-Skill": 0.4, "Analytical-Skill": 0.3, "Lab-Research": 0.2}},
            {"option_id": 171, "option_text": "Senior citizens managing diabetes and hypertension through diet",
             "trait_tags": {"Nutrition-Diet": 1.0, "Patient-Care": 0.5, "Counseling": 0.4, "People-Skill": 0.35, "Medical-Lab": 0.2}},
            {"option_id": 172, "option_text": "Pregnant and breastfeeding mothers in rural clinics",
             "trait_tags": {"Nutrition-Diet": 1.0, "Midwifery": 0.5, "Patient-Care": 0.45, "Community-Serve": 0.35, "People-Skill": 0.2}},
            {"option_id": 173, "option_text": "Factory workers who need affordable, balanced packed lunches",
             "trait_tags": {"Nutrition-Diet": 1.0, "Food-Science": 0.5, "Industrial-Ops": 0.35, "Culinary-Arts": 0.3, "Admin-Skill": 0.25}},
            {"option_id": 174, "option_text": "Overweight teens who need guidance on healthy eating habits",
             "trait_tags": {"Nutrition-Diet": 1.0, "Counseling": 0.5, "Teaching-Ed": 0.4, "People-Skill": 0.35, "Social": 0.25}},
        ],
    },

    # ── 5. Replace Q1116 (Veterinary & Animal Science dup) ──
    # Existing questions cover vet interests, animal care specialties.
    # Removed Q1116 was "What animal science research area excites you?"
    # NEW ANGLE: What would your ideal day working with animals look like?
    {
        "question_id": 12,
        "question_text": "What would your ideal day working with animals look like?",
        "category": "Academic Interest - Veterinary & Animal Science",
        "options": [
            {"option_id": 175, "option_text": "Treating sick pets in a veterinary clinic — dogs, cats, and rabbits",
             "trait_tags": {"Veterinary": 1.0, "Patient-Care": 0.5, "People-Skill": 0.4, "Lab-Research": 0.3, "Community-Serve": 0.2}},
            {"option_id": 176, "option_text": "Visiting farms to check on livestock health and prevent disease outbreaks",
             "trait_tags": {"Veterinary": 1.0, "Agri-Nature": 0.5, "Field-Research": 0.45, "Community-Serve": 0.3, "Realistic": 0.25}},
            {"option_id": 177, "option_text": "Researching animal genetics in a laboratory to improve breeding programs",
             "trait_tags": {"Lab-Research": 1.0, "Veterinary": 0.5, "Data-Analytics": 0.4, "Investigative": 0.35, "Analytical-Skill": 0.25}},
            {"option_id": 178, "option_text": "Working at a wildlife sanctuary rehabilitating injured or endangered species",
             "trait_tags": {"Environmental-Sci": 1.0, "Veterinary": 0.5, "Field-Research": 0.45, "Community-Serve": 0.3, "Physical-Skill": 0.25}},
            {"option_id": 179, "option_text": "Inspecting meat and dairy processing plants to ensure food safety",
             "trait_tags": {"Food-Science": 1.0, "Veterinary": 0.5, "Admin-Skill": 0.4, "Analytical-Skill": 0.35, "Conventional": 0.25}},
            {"option_id": 180, "option_text": "Training animals for therapy programs in hospitals and schools",
             "trait_tags": {"Veterinary": 1.0, "Counseling": 0.5, "Teaching-Ed": 0.4, "People-Skill": 0.35, "Rehab-Therapy": 0.3}},
        ],
    },

    # ── 6. Replace Q1401 (Weather & Atmospheric Science dup) ──
    # Existing questions cover atmospheric interest areas, tools, research.
    # Removed Q1401 was "Which part of weather and atmosphere science interests you most?"
    # NEW ANGLE: SCENARIO about applying weather science to a Philippine climate crisis.
    {
        "question_id": 13,
        "question_text": "SCENARIO: Super typhoon season is approaching the Philippines. How would you contribute as a weather scientist?",
        "category": "Academic Interest - Weather & Atmospheric Science",
        "options": [
            {"option_id": 181, "option_text": "Improve forecast models so communities get earlier and more accurate warnings",
             "trait_tags": {"Data-Analytics": 1.0, "Analytical-Skill": 0.5, "Software-Dev": 0.4, "Investigative": 0.3, "Technical-Skill": 0.25}},
            {"option_id": 182, "option_text": "Deploy weather stations in remote provinces that currently have no coverage",
             "trait_tags": {"Hardware-Systems": 1.0, "Field-Research": 0.5, "Technical-Skill": 0.45, "Community-Serve": 0.35, "Realistic": 0.2}},
            {"option_id": 183, "option_text": "Conduct research on how climate change is making Philippine typhoons stronger",
             "trait_tags": {"Lab-Research": 1.0, "Environmental-Sci": 0.5, "Investigative": 0.45, "Analytical-Skill": 0.35, "Field-Research": 0.25}},
            {"option_id": 184, "option_text": "Train local disaster risk reduction officers to interpret weather data",
             "trait_tags": {"Teaching-Ed": 1.0, "Community-Serve": 0.5, "People-Skill": 0.45, "Social": 0.3, "Data-Analytics": 0.2}},
            {"option_id": 185, "option_text": "Build a real-time weather dashboard app that fishermen and farmers can use",
             "trait_tags": {"Software-Dev": 1.0, "Digital-Media": 0.5, "Technical-Skill": 0.4, "Data-Analytics": 0.35, "Agri-Nature": 0.2}},
            {"option_id": 186, "option_text": "Fly into storms with aircraft instruments to gather data nobody else can get",
             "trait_tags": {"Field-Research": 1.0, "Aeronautical-Eng": 0.5, "Physical-Skill": 0.4, "Investigative": 0.35, "Realistic": 0.25}},
        ],
    },

    # ── 7. Replace Q2331 (Economics dup) ──
    # Existing questions cover economic interest areas and academic topics.
    # Removed Q2331 was "Which part of economics interests you most?"
    # NEW ANGLE: If you could change one economic policy in the Philippines.
    {
        "question_id": 14,
        "question_text": "If you could change one economic policy in the Philippines, what would it address?",
        "category": "Academic Interest - Economics",
        "options": [
            {"option_id": 187, "option_text": "Raising minimum wage so workers can afford basic needs",
             "trait_tags": {"Finance-Acct": 1.0, "Community-Serve": 0.5, "Social": 0.45, "People-Skill": 0.3, "Enterprising": 0.2}},
            {"option_id": 188, "option_text": "Making it easier for small businesses and startups to get funding",
             "trait_tags": {"Startup-Venture": 1.0, "Enterprising": 0.5, "Finance-Acct": 0.45, "Admin-Skill": 0.3, "Marketing-Sales": 0.2}},
            {"option_id": 189, "option_text": "Reducing income tax to leave more money in people's pockets",
             "trait_tags": {"Finance-Acct": 1.0, "Analytical-Skill": 0.5, "Conventional": 0.4, "Admin-Skill": 0.3, "Investigative": 0.2}},
            {"option_id": 190, "option_text": "Investing more in public education and scholarship programs",
             "trait_tags": {"Teaching-Ed": 1.0, "Community-Serve": 0.5, "Social": 0.4, "People-Skill": 0.35, "Conventional": 0.2}},
            {"option_id": 191, "option_text": "Developing agricultural subsidies so farmers earn a fair income",
             "trait_tags": {"Agri-Nature": 1.0, "Community-Serve": 0.5, "Finance-Acct": 0.4, "Environmental-Sci": 0.3, "Social": 0.25}},
            {"option_id": 192, "option_text": "Attracting foreign tech companies to create high-skilled jobs",
             "trait_tags": {"Software-Dev": 1.0, "Enterprising": 0.5, "Technical-Skill": 0.4, "Data-Analytics": 0.3, "Admin-Skill": 0.25}},
        ],
    },

    # ── 8. Replace Q2576 (Fine Arts & Painting dup) ──
    # Existing questions cover fine arts interest, visual design, disciplines.
    # Removed Q2576 was "Which area of fine arts interests you most?"
    # NEW ANGLE: What INSPIRES your creative process when making art?
    {
        "question_id": 15,
        "question_text": "When creating art, what inspires you the most?",
        "category": "Academic Interest - Fine Arts & Painting",
        "options": [
            {"option_id": 193, "option_text": "Nature — landscapes, oceans, and the beauty of the natural world",
             "trait_tags": {"Artistic": 1.0, "Visual-Design": 0.5, "Environmental-Sci": 0.35, "Field-Research": 0.3, "Creative-Skill": 0.25}},
            {"option_id": 194, "option_text": "Human emotions — capturing feelings like joy, grief, and longing on canvas",
             "trait_tags": {"Artistic": 1.0, "Creative-Skill": 0.5, "People-Skill": 0.4, "Counseling": 0.3, "Performing-Arts": 0.2}},
            {"option_id": 195, "option_text": "Filipino culture — weaving indigenous patterns, festivals, and traditions into art",
             "trait_tags": {"Artistic": 1.0, "Community-Serve": 0.5, "Creative-Skill": 0.45, "Teaching-Ed": 0.3, "Social": 0.2}},
            {"option_id": 196, "option_text": "Social issues — using art as protest or commentary on injustice",
             "trait_tags": {"Artistic": 1.0, "Community-Serve": 0.5, "Social": 0.45, "Writing-Comm": 0.35, "People-Skill": 0.2}},
            {"option_id": 197, "option_text": "Technology — experimenting with digital tools, AI, or mixed media",
             "trait_tags": {"Digital-Media": 1.0, "Artistic": 0.5, "Software-Dev": 0.4, "Creative-Skill": 0.35, "Technical-Skill": 0.25}},
            {"option_id": 198, "option_text": "Architecture and urban spaces — the shapes, light, and geometry of buildings",
             "trait_tags": {"Spatial-Design": 1.0, "Artistic": 0.5, "Visual-Design": 0.45, "Civil-Build": 0.3, "Creative-Skill": 0.25}},
        ],
    },

    # ── 9. Replace Q2841 (Writing & Literature dup) ──
    # Existing questions cover writing interest, career, genres.
    # Removed Q2841 was "What excites you most about pursuing a career in writing and literature?"
    # NEW ANGLE: If you could write any type of book, what would it be about?
    {
        "question_id": 16,
        "question_text": "If you could write any type of book, what would it be about?",
        "category": "Academic Interest - Writing & Literature",
        "options": [
            {"option_id": 199, "option_text": "A novel exploring the lives of Filipinos working abroad",
             "trait_tags": {"Writing-Comm": 1.0, "Creative-Skill": 0.5, "Social": 0.4, "People-Skill": 0.35, "Community-Serve": 0.2}},
            {"option_id": 200, "option_text": "A self-help book about building good habits and mental resilience",
             "trait_tags": {"Writing-Comm": 1.0, "Counseling": 0.5, "Teaching-Ed": 0.4, "People-Skill": 0.35, "Social": 0.25}},
            {"option_id": 201, "option_text": "A science fiction story about technology transforming the future",
             "trait_tags": {"Writing-Comm": 1.0, "Creative-Skill": 0.5, "Software-Dev": 0.35, "Investigative": 0.3, "Technical-Skill": 0.2}},
            {"option_id": 202, "option_text": "An investigative journalism book uncovering corruption",
             "trait_tags": {"Writing-Comm": 1.0, "Investigative": 0.5, "Law-Enforce": 0.4, "Community-Serve": 0.35, "Social": 0.25}},
            {"option_id": 203, "option_text": "A children's book with colorful illustrations teaching Filipino values",
             "trait_tags": {"Writing-Comm": 1.0, "Artistic": 0.5, "Teaching-Ed": 0.45, "Visual-Design": 0.3, "Creative-Skill": 0.25}},
            {"option_id": 204, "option_text": "A business guide for aspiring Filipino entrepreneurs",
             "trait_tags": {"Writing-Comm": 1.0, "Startup-Venture": 0.5, "Enterprising": 0.45, "Finance-Acct": 0.3, "Marketing-Sales": 0.25}},
        ],
    },

    # ── 10. Replace Q2901 (Clothing & Textile Technology dup) ──
    # Existing questions cover fashion interest, textile career paths.
    # Removed Q2901 was "What excites you most about clothing and textile technology?"
    # NEW ANGLE: What fashion or textile INNOVATION would you develop?
    {
        "question_id": 17,
        "question_text": "What fashion or textile innovation would you most like to develop?",
        "category": "Academic Interest - Clothing & Textile Technology",
        "options": [
            {"option_id": 205, "option_text": "Sustainable fabrics made from Philippine natural fibers like abaca and piña",
             "trait_tags": {"Creative-Skill": 1.0, "Environmental-Sci": 0.5, "Agri-Nature": 0.4, "Artistic": 0.35, "Lab-Research": 0.2}},
            {"option_id": 206, "option_text": "Smart clothing with embedded sensors that monitor health or fitness",
             "trait_tags": {"Technical-Skill": 1.0, "Hardware-Systems": 0.5, "Software-Dev": 0.4, "Medical-Lab": 0.3, "Data-Analytics": 0.25}},
            {"option_id": 207, "option_text": "A Filipino fashion brand that blends traditional weaving with modern streetwear",
             "trait_tags": {"Artistic": 1.0, "Creative-Skill": 0.5, "Marketing-Sales": 0.45, "Startup-Venture": 0.35, "Enterprising": 0.25}},
            {"option_id": 208, "option_text": "Durable, affordable school and work uniforms for mass production",
             "trait_tags": {"Industrial-Ops": 1.0, "Admin-Skill": 0.5, "Conventional": 0.4, "Analytical-Skill": 0.3, "Mechanical-Design": 0.2}},
            {"option_id": 209, "option_text": "Adaptive clothing designed for persons with disabilities",
             "trait_tags": {"Creative-Skill": 1.0, "Community-Serve": 0.5, "People-Skill": 0.45, "Patient-Care": 0.3, "Rehab-Therapy": 0.25}},
            {"option_id": 210, "option_text": "High-performance athletic wear using cutting-edge textile engineering",
             "trait_tags": {"Lab-Research": 1.0, "Physical-Skill": 0.5, "Technical-Skill": 0.45, "Sports-Ed": 0.35, "Mechanical-Design": 0.2}},
        ],
    },

    # ── 11. Replace Q3206 (Respiratory Therapy dup) ──
    # Existing questions cover respiratory therapy interest, career, patient types.
    # Removed Q3206 was "Which respiratory therapy specialty or practice area interests you most?"
    # NEW ANGLE: SCENARIO about a respiratory emergency — what would you handle?
    {
        "question_id": 18,
        "question_text": "SCENARIO: A patient in the ICU is struggling to breathe after surgery. What aspect of their care would you want to handle?",
        "category": "Academic Interest - Respiratory Therapy",
        "options": [
            {"option_id": 211, "option_text": "Setting up and adjusting the mechanical ventilator to stabilize their breathing",
             "trait_tags": {"Rehab-Therapy": 1.0, "Technical-Skill": 0.5, "Patient-Care": 0.45, "Medical-Lab": 0.3, "Analytical-Skill": 0.25}},
            {"option_id": 212, "option_text": "Monitoring their blood oxygen levels and interpreting arterial blood gas results",
             "trait_tags": {"Medical-Lab": 1.0, "Analytical-Skill": 0.5, "Rehab-Therapy": 0.45, "Data-Analytics": 0.3, "Investigative": 0.2}},
            {"option_id": 213, "option_text": "Coaching the patient through breathing exercises once they're stable",
             "trait_tags": {"Patient-Care": 1.0, "People-Skill": 0.5, "Rehab-Therapy": 0.45, "Teaching-Ed": 0.35, "Counseling": 0.25}},
            {"option_id": 214, "option_text": "Coordinating with the doctor and nurses to adjust the treatment plan",
             "trait_tags": {"People-Skill": 1.0, "Admin-Skill": 0.5, "Patient-Care": 0.4, "Community-Serve": 0.3, "Social": 0.25}},
            {"option_id": 215, "option_text": "Performing chest physiotherapy to help clear mucus from their airways",
             "trait_tags": {"Physical-Skill": 1.0, "Rehab-Therapy": 0.5, "Patient-Care": 0.45, "Realistic": 0.3, "Medical-Lab": 0.2}},
            {"option_id": 216, "option_text": "Documenting the patient's progress and respiratory data for the medical team",
             "trait_tags": {"Conventional": 1.0, "Admin-Skill": 0.5, "Data-Analytics": 0.4, "Medical-Lab": 0.35, "Analytical-Skill": 0.25}},
        ],
    },

    # ── 12. Replace Q3266 (Dentistry & Oral Health dup) ──
    # Existing questions cover dental interest, specialties, career.
    # Removed Q3266 was "Which dental specialty or oral health area interests you most?"
    # NEW ANGLE: What oral health initiative would you bring to an underserved area?
    {
        "question_id": 19,
        "question_text": "What oral health initiative would you bring to a community with limited access to dental care?",
        "category": "Academic Interest - Dentistry & Oral Health",
        "options": [
            {"option_id": 26839, "option_text": "A mobile dental clinic that visits remote barangays for free checkups",
             "trait_tags": {"Patient-Care": 1.0, "Community-Serve": 0.5, "People-Skill": 0.4, "Social": 0.35, "Realistic": 0.2}},
            {"option_id": 26840, "option_text": "A school program teaching children proper brushing and oral hygiene habits",
             "trait_tags": {"Teaching-Ed": 1.0, "Community-Serve": 0.5, "People-Skill": 0.45, "Patient-Care": 0.3, "Social": 0.25}},
            {"option_id": 26841, "option_text": "Affordable prosthetic dentures for senior citizens who can't afford them",
             "trait_tags": {"Spatial-Design": 1.0, "Patient-Care": 0.5, "Technical-Skill": 0.4, "Community-Serve": 0.35, "Creative-Skill": 0.2}},
            {"option_id": 26842, "option_text": "Training community health workers to do basic dental screenings",
             "trait_tags": {"Teaching-Ed": 1.0, "Community-Serve": 0.5, "Admin-Skill": 0.4, "People-Skill": 0.35, "Social": 0.25}},
            {"option_id": 26843, "option_text": "Using teledentistry so patients can consult a dentist through video calls",
             "trait_tags": {"Software-Dev": 1.0, "Digital-Media": 0.5, "Technical-Skill": 0.4, "Patient-Care": 0.35, "Data-Analytics": 0.2}},
            {"option_id": 26844, "option_text": "Researching low-cost dental materials that work well in tropical climates",
             "trait_tags": {"Lab-Research": 1.0, "Investigative": 0.5, "Analytical-Skill": 0.45, "Technical-Skill": 0.3, "Environmental-Sci": 0.2}},
        ],
    },

    # ── 13. Replace Q3541 (Politics & Government dup) ──
    # Existing questions cover political interest areas, government careers.
    # Removed Q3541 was "What part of politics and government work would you enjoy most?"
    # Existing Q1011 covers "elected mayor" scenario; Q891 covers "business department".
    # NEW ANGLE: What part of GOVERNANCE excites you — unique phrasing to avoid overlap.
    {
        "question_id": 20,
        "question_text": "What role in Philippine governance would you find most meaningful?",
        "category": "Academic Interest - Politics & Government",
        "options": [
            {"option_id": 26845, "option_text": "Crafting national health policies at the Department of Health",
             "trait_tags": {"Community-Serve": 1.0, "Patient-Care": 0.5, "Admin-Skill": 0.4, "Social": 0.35, "People-Skill": 0.25}},
            {"option_id": 26846, "option_text": "Auditing government spending to fight corruption and waste",
             "trait_tags": {"Finance-Acct": 1.0, "Analytical-Skill": 0.5, "Conventional": 0.45, "Admin-Skill": 0.35, "Investigative": 0.25}},
            {"option_id": 26847, "option_text": "Leading the country's digital transformation at DICT",
             "trait_tags": {"Software-Dev": 1.0, "Technical-Skill": 0.5, "Data-Analytics": 0.4, "Admin-Skill": 0.35, "Digital-Media": 0.2}},
            {"option_id": 26848, "option_text": "Planning nationwide infrastructure projects at DPWH",
             "trait_tags": {"Civil-Build": 1.0, "Spatial-Design": 0.5, "Technical-Skill": 0.4, "Mechanical-Design": 0.3, "Realistic": 0.25}},
            {"option_id": 26849, "option_text": "Running social welfare programs for vulnerable families at DSWD",
             "trait_tags": {"Social": 1.0, "Community-Serve": 0.5, "People-Skill": 0.45, "Counseling": 0.35, "Teaching-Ed": 0.2}},
            {"option_id": 26850, "option_text": "Protecting forests, wildlife, and natural resources at DENR",
             "trait_tags": {"Environmental-Sci": 1.0, "Agri-Nature": 0.5, "Field-Research": 0.45, "Community-Serve": 0.3, "Investigative": 0.25}},
        ],
    },

    # ── 14. Replace Q3801 (Special Needs Education dup) ──
    # Existing questions cover special education interests, scenarios.
    # Removed Q3801 was "What excites you most about studying special needs education?"
    # NEW ANGLE: What inclusive learning activity would you design?
    {
        "question_id": 21,
        "question_text": "What type of inclusive learning activity would you design for students with special needs?",
        "category": "Academic Interest - Special Needs Education",
        "options": [
            {"option_id": 26851, "option_text": "Sensory play stations that help children with autism develop motor skills",
             "trait_tags": {"Teaching-Ed": 1.0, "Rehab-Therapy": 0.5, "Creative-Skill": 0.4, "Patient-Care": 0.35, "People-Skill": 0.25}},
            {"option_id": 26852, "option_text": "Picture-based communication boards for non-verbal students",
             "trait_tags": {"Teaching-Ed": 1.0, "Visual-Design": 0.5, "Creative-Skill": 0.4, "Counseling": 0.35, "People-Skill": 0.25}},
            {"option_id": 26853, "option_text": "Adaptive physical education games that every ability level can enjoy",
             "trait_tags": {"Sports-Ed": 1.0, "Teaching-Ed": 0.5, "Physical-Skill": 0.45, "People-Skill": 0.35, "Community-Serve": 0.2}},
            {"option_id": 26854, "option_text": "A buddy system pairing mainstream students with special needs classmates",
             "trait_tags": {"Social": 1.0, "Teaching-Ed": 0.5, "Community-Serve": 0.45, "People-Skill": 0.4, "Counseling": 0.25}},
            {"option_id": 26855, "option_text": "Interactive tablet apps that adjust difficulty based on the learner's pace",
             "trait_tags": {"Software-Dev": 1.0, "Teaching-Ed": 0.5, "Digital-Media": 0.4, "Technical-Skill": 0.35, "Data-Analytics": 0.25}},
            {"option_id": 26856, "option_text": "Music and art therapy sessions that build confidence and self-expression",
             "trait_tags": {"Creative-Skill": 1.0, "Performing-Arts": 0.5, "Counseling": 0.45, "Teaching-Ed": 0.35, "Artistic": 0.25}},
        ],
    },

    # ── 15. Replace Q3921 (Sports & Fitness dup) ──
    # Existing questions cover sports interest, fitness careers.
    # Removed Q3921 was "What excites you most about studying sports and fitness?"
    # NEW ANGLE: If you could coach or train a team, what would your focus be?
    {
        "question_id": 22,
        "question_text": "If you could coach or train a sports team, what would be your main focus?",
        "category": "Academic Interest - Sports & Fitness",
        "options": [
            {"option_id": 26857, "option_text": "Strength and conditioning programs to prevent injuries and boost performance",
             "trait_tags": {"Physical-Skill": 1.0, "Sports-Ed": 0.5, "Rehab-Therapy": 0.4, "Analytical-Skill": 0.3, "Realistic": 0.25}},
            {"option_id": 26858, "option_text": "Game strategy and film analysis to outsmart opponents",
             "trait_tags": {"Analytical-Skill": 1.0, "Sports-Ed": 0.5, "Data-Analytics": 0.45, "Investigative": 0.3, "Technical-Skill": 0.2}},
            {"option_id": 26859, "option_text": "Mental toughness — helping athletes handle pressure and stay motivated",
             "trait_tags": {"Counseling": 1.0, "People-Skill": 0.5, "Sports-Ed": 0.45, "Social": 0.35, "Teaching-Ed": 0.2}},
            {"option_id": 26860, "option_text": "Nutrition and recovery plans tailored to each athlete's needs",
             "trait_tags": {"Nutrition-Diet": 1.0, "Sports-Ed": 0.5, "Patient-Care": 0.4, "Analytical-Skill": 0.3, "Lab-Research": 0.2}},
            {"option_id": 26861, "option_text": "Using wearable tech and data analytics to track player performance",
             "trait_tags": {"Data-Analytics": 1.0, "Software-Dev": 0.5, "Sports-Ed": 0.4, "Technical-Skill": 0.35, "Hardware-Systems": 0.25}},
            {"option_id": 26862, "option_text": "Building teamwork and discipline through character development activities",
             "trait_tags": {"Teaching-Ed": 1.0, "People-Skill": 0.5, "Social": 0.45, "Community-Serve": 0.3, "Sports-Ed": 0.25}},
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

    # 2. Check for near-duplicate question texts (basic similarity check)
    new_texts = [nq["question_text"].lower() for nq in NEW_QUESTIONS]
    existing_texts = [q["question_text"].lower() for q in QUESTIONS_POOL_ENHANCED]
    
    for i, nt in enumerate(new_texts):
        for et in existing_texts:
            # Check if >60% of words overlap
            nw = set(nt.split())
            ew = set(et.split())
            if len(nw & ew) > 0.6 * min(len(nw), len(ew)):
                print(f"  WARNING: Possible text overlap:")
                print(f"    NEW:      {NEW_QUESTIONS[i]['question_text']}")
                print(f"    EXISTING: {et}")

    # 3. Convert to Python source code
    import json as _json

    def dict_to_source(d, indent=4):
        """Convert a question dict to Python source code string."""
        lines = []
        sp = " " * indent
        lines.append(f"{sp}{{")
        lines.append(f'{sp}    "question_id": {d["question_id"]},')
        lines.append(f'{sp}    "question_text": {_json.dumps(d["question_text"])},')
        lines.append(f'{sp}    "category": {_json.dumps(d["category"])},')
        lines.append(f'{sp}    "options": [')
        for opt in d["options"]:
            trait_str = _json.dumps(opt["trait_tags"])
            lines.append(
                f'{sp}        {{"option_id": {opt["option_id"]}, '
                f'"option_text": {_json.dumps(opt["option_text"])}, '
                f'"trait_tags": {trait_str}}},'
            )
        lines.append(f"{sp}    ]")
        lines.append(f"{sp}}},")
        return "\n".join(lines)

    source_blocks = []
    for nq in NEW_QUESTIONS:
        source_blocks.append(dict_to_source(nq))

    insert_code = "\n".join(source_blocks) + "\n"

    # 4. Insert before the expansion functions
    filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "data", "questions_enhanced.py")
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    marker = "\ndef _build_science_interest_expansion"
    marker_pos = content.find(marker)
    if marker_pos == -1:
        print("ERROR: Could not find expansion marker in file!")
        return

    bracket_pos = content.rfind("]", 0, marker_pos)
    if bracket_pos == -1:
        print("ERROR: Could not find list closing bracket!")
        return

    new_content = content[:bracket_pos] + insert_code + content[bracket_pos:]

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"  Inserted {len(NEW_QUESTIONS)} new questions into file.")

    # 5. Verify by reimporting
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
