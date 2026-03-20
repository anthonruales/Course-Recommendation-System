"""
Patch script: 
1. Cross-reference existing questions into TRAIT_FOLLOWUP_MAP to fill gaps
2. Add new questions for paths that still fall short of 30
3. Update DOMAIN_ENTRY_QUESTIONS
"""
import json, re, os

# --- Load current data ---
from questions_enhanced import QUESTIONS_POOL_ENHANCED
from adaptive_assessment import TRAIT_FOLLOWUP_MAP, DOMAIN_ENTRY_QUESTIONS, QUESTION_TREE_NODES

# ============================================================
# STEP 1: Build cross-reference map from existing questions
# ============================================================
trait_to_scored = {}
for q in QUESTIONS_POOL_ENHANCED:
    qid = q['question_id']
    for opt in q['options']:
        for trait, score in opt['trait_tags'].items():
            if score >= 0.5:
                if trait not in trait_to_scored:
                    trait_to_scored[trait] = {}
                trait_to_scored[trait][qid] = max(trait_to_scored[trait].get(qid, 0), score)

# Build the new TRAIT_FOLLOWUP_MAP: keep existing order, add best missing questions
new_followup_map = {}
for trait in sorted(TRAIT_FOLLOWUP_MAP.keys()):
    current = list(TRAIT_FOLLOWUP_MAP[trait])
    current_set = set(current)
    need = 30 - len(current)
    if need <= 0:
        new_followup_map[trait] = current[:30]
        continue
    
    available = trait_to_scored.get(trait, {})
    missing = {qid: score for qid, score in available.items() if qid not in current_set}
    # Sort by score descending, pick top `need`
    best = sorted(missing.items(), key=lambda x: -x[1])[:need]
    new_followup_map[trait] = current + [qid for qid, _ in best]

# ============================================================
# STEP 2: Define new questions for paths still under 30
# ============================================================
# After cross-ref, these paths are still short:
# Culinary-Arts: 29 (need 1), Environmental-Eng: 29 (need 1), 
# HR-Management: 27 (need 3), Health-Admin: 27 (need 3),
# Mobile-Dev: 28 (need 2), Pharmacy: 26 (need 4), Tourism-Travel: 25 (need 5)
# Total: 19 new questions

NEW_QUESTIONS = [
    # --- CULINARY-ARTS (need 1) ---
    {
        "question_id": 424,
        "question_text": "Which culinary specialization appeals to you most?",
        "category": "Culinary - Specialization",
        "options": [
            {"option_id": 3867, "option_text": "Pastry arts and dessert innovation", "trait_tags": {"Culinary-Arts": 1.0, "Creative-Skill": 0.7, "Food-Science": 0.4}},
            {"option_id": 3868, "option_text": "International cuisine and fusion cooking", "trait_tags": {"Culinary-Arts": 0.9, "Tourism-Travel": 0.5, "Creative-Skill": 0.5}},
            {"option_id": 3869, "option_text": "Farm-to-table and sustainable gastronomy", "trait_tags": {"Culinary-Arts": 0.9, "Agri-Nature": 0.5, "Environmental-Sci": 0.4}},
            {"option_id": 3870, "option_text": "Food styling, photography, and media", "trait_tags": {"Culinary-Arts": 0.7, "Digital-Media": 0.6, "Visual-Design": 0.5}},
            {"option_id": 3871, "option_text": "Restaurant management and kitchen leadership", "trait_tags": {"Culinary-Arts": 0.8, "Hospitality-Svc": 0.6, "Admin-Skill": 0.5}},
            {"option_id": 3872, "option_text": "Food science research and recipe development", "trait_tags": {"Food-Science": 0.8, "Culinary-Arts": 0.7, "Lab-Research": 0.4}}
        ]
    },
    # --- ENVIRONMENTAL-ENG (need 1) ---
    {
        "question_id": 425,
        "question_text": "Which environmental engineering project excites you most?",
        "category": "Environmental Engineering - Project",
        "options": [
            {"option_id": 3873, "option_text": "Designing wastewater treatment systems for communities", "trait_tags": {"Environmental-Eng": 1.0, "Civil-Build": 0.5, "Community-Serve": 0.4}},
            {"option_id": 3874, "option_text": "Developing air quality monitoring and pollution control", "trait_tags": {"Environmental-Eng": 0.9, "Lab-Research": 0.5, "Environmental-Sci": 0.5}},
            {"option_id": 3875, "option_text": "Building renewable energy systems for rural areas", "trait_tags": {"Environmental-Eng": 0.8, "Electrical-Power": 0.6, "Community-Serve": 0.4}},
            {"option_id": 3876, "option_text": "Creating sustainable waste management solutions", "trait_tags": {"Environmental-Eng": 0.9, "Industrial-Ops": 0.5, "Agri-Nature": 0.3}},
            {"option_id": 3877, "option_text": "Remediation of contaminated soil and groundwater", "trait_tags": {"Environmental-Eng": 0.9, "Environmental-Sci": 0.6, "Field-Research": 0.4}},
            {"option_id": 3878, "option_text": "Green building design and energy-efficient infrastructure", "trait_tags": {"Environmental-Eng": 0.8, "Civil-Build": 0.6, "Spatial-Design": 0.4}}
        ]
    },
    # --- HR-MANAGEMENT (need 3) ---
    {
        "question_id": 426,
        "question_text": "Which HR function do you find most rewarding?",
        "category": "HR - Function",
        "options": [
            {"option_id": 3879, "option_text": "Talent acquisition and recruitment strategy", "trait_tags": {"HR-Management": 1.0, "People-Skill": 0.7, "Admin-Skill": 0.4}},
            {"option_id": 3880, "option_text": "Employee training and professional development", "trait_tags": {"HR-Management": 0.9, "Teaching-Ed": 0.7, "People-Skill": 0.5}},
            {"option_id": 3881, "option_text": "Compensation, benefits, and payroll management", "trait_tags": {"HR-Management": 0.8, "Finance-Acct": 0.6, "Admin-Skill": 0.5}},
            {"option_id": 3882, "option_text": "Organizational development and change management", "trait_tags": {"HR-Management": 0.9, "Admin-Skill": 0.6, "Analytical-Skill": 0.4}},
            {"option_id": 3883, "option_text": "Employee relations and workplace conflict mediation", "trait_tags": {"HR-Management": 0.8, "Counseling": 0.5, "People-Skill": 0.6}},
            {"option_id": 3884, "option_text": "Workforce analytics and data-driven HR decisions", "trait_tags": {"HR-Management": 0.8, "Data-Analytics": 0.6, "Analytical-Skill": 0.5}}
        ]
    },
    {
        "question_id": 427,
        "question_text": "How do you handle a workplace culture issue?",
        "category": "HR - Culture",
        "options": [
            {"option_id": 3885, "option_text": "Conduct employee surveys and listen to feedback", "trait_tags": {"HR-Management": 0.9, "People-Skill": 0.7, "Analytical-Skill": 0.4}},
            {"option_id": 3886, "option_text": "Run team-building workshops and engagement programs", "trait_tags": {"HR-Management": 0.8, "Teaching-Ed": 0.5, "Community-Serve": 0.4}},
            {"option_id": 3887, "option_text": "Review policies and update the employee handbook", "trait_tags": {"HR-Management": 0.8, "Legal-Practice": 0.4, "Admin-Skill": 0.5}},
            {"option_id": 3888, "option_text": "Coach leaders on effective management practices", "trait_tags": {"HR-Management": 0.9, "Counseling": 0.5, "Teaching-Ed": 0.5}},
            {"option_id": 3889, "option_text": "Use data to identify trends and root causes", "trait_tags": {"HR-Management": 0.7, "Data-Analytics": 0.6, "Analytical-Skill": 0.5}},
            {"option_id": 3890, "option_text": "Implement diversity, equity, and inclusion initiatives", "trait_tags": {"HR-Management": 0.8, "Community-Serve": 0.5, "Social-Work": 0.4}}
        ]
    },
    {
        "question_id": 428,
        "question_text": "Which aspect of employee development interests you most?",
        "category": "HR - Development",
        "options": [
            {"option_id": 3891, "option_text": "Leadership pipeline and succession planning", "trait_tags": {"HR-Management": 0.9, "Admin-Skill": 0.6, "Analytical-Skill": 0.4}},
            {"option_id": 3892, "option_text": "Skills assessment and competency mapping", "trait_tags": {"HR-Management": 0.8, "Analytical-Skill": 0.6, "Teaching-Ed": 0.4}},
            {"option_id": 3893, "option_text": "Mentoring programs and career coaching", "trait_tags": {"HR-Management": 0.8, "Counseling": 0.6, "People-Skill": 0.5}},
            {"option_id": 3894, "option_text": "Digital learning platforms and e-training tools", "trait_tags": {"HR-Management": 0.7, "Technical-Skill": 0.5, "Teaching-Ed": 0.5}},
            {"option_id": 3895, "option_text": "Performance review systems and goal tracking", "trait_tags": {"HR-Management": 0.8, "Admin-Skill": 0.6, "Data-Analytics": 0.4}},
            {"option_id": 3896, "option_text": "Employee wellness and mental health support programs", "trait_tags": {"HR-Management": 0.7, "Social-Work": 0.5, "Counseling": 0.5}}
        ]
    },
    # --- HEALTH-ADMIN (need 3) ---
    {
        "question_id": 429,
        "question_text": "Which healthcare management area interests you most?",
        "category": "Health Admin - Area",
        "options": [
            {"option_id": 3897, "option_text": "Hospital operations and clinical workflow management", "trait_tags": {"Health-Admin": 1.0, "Admin-Skill": 0.6, "Patient-Care": 0.4}},
            {"option_id": 3898, "option_text": "Health information systems and electronic medical records", "trait_tags": {"Health-Admin": 0.9, "Technical-Skill": 0.5, "Data-Analytics": 0.4}},
            {"option_id": 3899, "option_text": "Healthcare policy and government health programs", "trait_tags": {"Health-Admin": 0.8, "Community-Serve": 0.6, "Legal-Practice": 0.3}},
            {"option_id": 3900, "option_text": "Medical supply chain and procurement", "trait_tags": {"Health-Admin": 0.8, "Industrial-Ops": 0.5, "Admin-Skill": 0.5}},
            {"option_id": 3901, "option_text": "Quality improvement and patient safety programs", "trait_tags": {"Health-Admin": 0.9, "Patient-Care": 0.5, "Analytical-Skill": 0.4}},
            {"option_id": 3902, "option_text": "Healthcare finance, billing, and insurance management", "trait_tags": {"Health-Admin": 0.8, "Finance-Acct": 0.7, "Admin-Skill": 0.4}}
        ]
    },
    {
        "question_id": 430,
        "question_text": "How would you improve a hospital's efficiency?",
        "category": "Health Admin - Efficiency",
        "options": [
            {"option_id": 3903, "option_text": "Implement digital scheduling and patient flow systems", "trait_tags": {"Health-Admin": 0.9, "Technical-Skill": 0.5, "Admin-Skill": 0.5}},
            {"option_id": 3904, "option_text": "Optimize staffing patterns based on patient demand data", "trait_tags": {"Health-Admin": 0.9, "Data-Analytics": 0.6, "Analytical-Skill": 0.4}},
            {"option_id": 3905, "option_text": "Streamline procurement and reduce waste in supplies", "trait_tags": {"Health-Admin": 0.8, "Industrial-Ops": 0.5, "Finance-Acct": 0.4}},
            {"option_id": 3906, "option_text": "Improve interdepartmental communication and teamwork", "trait_tags": {"Health-Admin": 0.7, "People-Skill": 0.6, "Admin-Skill": 0.5}},
            {"option_id": 3907, "option_text": "Train staff on lean healthcare management practices", "trait_tags": {"Health-Admin": 0.8, "Teaching-Ed": 0.5, "Industrial-Ops": 0.4}},
            {"option_id": 3908, "option_text": "Audit processes and implement evidence-based protocols", "trait_tags": {"Health-Admin": 0.8, "Analytical-Skill": 0.6, "Lab-Research": 0.3}}
        ]
    },
    {
        "question_id": 431,
        "question_text": "Which healthcare leadership role appeals to you?",
        "category": "Health Admin - Leadership",
        "options": [
            {"option_id": 3909, "option_text": "Medical center director or hospital administrator", "trait_tags": {"Health-Admin": 1.0, "Admin-Skill": 0.7, "People-Skill": 0.4}},
            {"option_id": 3910, "option_text": "Public health program manager", "trait_tags": {"Health-Admin": 0.8, "Public-Health": 0.7, "Community-Serve": 0.4}},
            {"option_id": 3911, "option_text": "Health informatics and technology officer", "trait_tags": {"Health-Admin": 0.8, "Technical-Skill": 0.6, "Data-Analytics": 0.4}},
            {"option_id": 3912, "option_text": "Clinical research coordinator", "trait_tags": {"Health-Admin": 0.7, "Lab-Research": 0.6, "Analytical-Skill": 0.5}},
            {"option_id": 3913, "option_text": "Healthcare compliance and regulatory officer", "trait_tags": {"Health-Admin": 0.8, "Legal-Practice": 0.5, "Admin-Skill": 0.5}},
            {"option_id": 3914, "option_text": "Community health center manager", "trait_tags": {"Health-Admin": 0.8, "Community-Serve": 0.6, "Patient-Care": 0.4}}
        ]
    },
    # --- MOBILE-DEV (need 2) ---
    {
        "question_id": 432,
        "question_text": "Which mobile app category would you most enjoy building?",
        "category": "Mobile Dev - Category",
        "options": [
            {"option_id": 3915, "option_text": "Health and fitness tracking applications", "trait_tags": {"Mobile-Dev": 0.9, "Physical-Skill": 0.4, "Patient-Care": 0.3}},
            {"option_id": 3916, "option_text": "E-commerce and fintech payment platforms", "trait_tags": {"Mobile-Dev": 0.9, "Finance-Acct": 0.5, "Startup-Venture": 0.4}},
            {"option_id": 3917, "option_text": "Social networking and communication tools", "trait_tags": {"Mobile-Dev": 0.8, "People-Skill": 0.4, "Creative-Skill": 0.4}},
            {"option_id": 3918, "option_text": "Educational and e-learning platforms", "trait_tags": {"Mobile-Dev": 0.8, "Teaching-Ed": 0.6, "Creative-Skill": 0.4}},
            {"option_id": 3919, "option_text": "Gaming and interactive entertainment apps", "trait_tags": {"Mobile-Dev": 0.8, "Game-Dev": 0.7, "Creative-Skill": 0.4}},
            {"option_id": 3920, "option_text": "IoT and smart device controller applications", "trait_tags": {"Mobile-Dev": 0.8, "Hardware-Systems": 0.5, "Technical-Skill": 0.5}}
        ]
    },
    {
        "question_id": 433,
        "question_text": "Which mobile development skill do you want to master?",
        "category": "Mobile Dev - Skill",
        "options": [
            {"option_id": 3921, "option_text": "Cross-platform development (React Native, Flutter)", "trait_tags": {"Mobile-Dev": 1.0, "Software-Dev": 0.6, "Web-Dev": 0.4}},
            {"option_id": 3922, "option_text": "Native iOS or Android development", "trait_tags": {"Mobile-Dev": 1.0, "Software-Dev": 0.7, "Technical-Skill": 0.4}},
            {"option_id": 3923, "option_text": "Mobile UI/UX design and user research", "trait_tags": {"Mobile-Dev": 0.8, "Visual-Design": 0.6, "Creative-Skill": 0.5}},
            {"option_id": 3924, "option_text": "Mobile security and secure coding practices", "trait_tags": {"Mobile-Dev": 0.8, "Cyber-Defense": 0.7, "Software-Dev": 0.4}},
            {"option_id": 3925, "option_text": "Backend APIs and cloud integration for mobile", "trait_tags": {"Mobile-Dev": 0.8, "Cloud-Systems": 0.6, "Software-Dev": 0.5}},
            {"option_id": 3926, "option_text": "Mobile analytics, performance tuning, and testing", "trait_tags": {"Mobile-Dev": 0.8, "Data-Analytics": 0.5, "Analytical-Skill": 0.4}}
        ]
    },
    # --- PHARMACY (need 4) ---
    {
        "question_id": 434,
        "question_text": "Which pharmacy practice setting appeals to you most?",
        "category": "Pharmacy - Setting",
        "options": [
            {"option_id": 3927, "option_text": "Hospital clinical pharmacy and patient rounds", "trait_tags": {"Pharmacy": 1.0, "Patient-Care": 0.7, "Medical-Lab": 0.3}},
            {"option_id": 3928, "option_text": "Community retail pharmacy and patient counseling", "trait_tags": {"Pharmacy": 0.9, "People-Skill": 0.6, "Community-Serve": 0.4}},
            {"option_id": 3929, "option_text": "Pharmaceutical industry and drug manufacturing", "trait_tags": {"Pharmacy": 0.8, "Industrial-Ops": 0.6, "Lab-Research": 0.4}},
            {"option_id": 3930, "option_text": "Research pharmacy and clinical drug trials", "trait_tags": {"Pharmacy": 0.8, "Lab-Research": 0.7, "Analytical-Skill": 0.4}},
            {"option_id": 3931, "option_text": "Government regulatory and drug approval roles", "trait_tags": {"Pharmacy": 0.7, "Legal-Practice": 0.5, "Admin-Skill": 0.5}},
            {"option_id": 3932, "option_text": "Specialty pharmacy for complex medications", "trait_tags": {"Pharmacy": 0.9, "Patient-Care": 0.5, "Analytical-Skill": 0.5}}
        ]
    },
    {
        "question_id": 435,
        "question_text": "Which pharmacology topic fascinates you most?",
        "category": "Pharmacy - Pharmacology",
        "options": [
            {"option_id": 3933, "option_text": "Drug interactions and adverse effect management", "trait_tags": {"Pharmacy": 1.0, "Analytical-Skill": 0.6, "Patient-Care": 0.4}},
            {"option_id": 3934, "option_text": "Herbal medicine and natural product pharmacology", "trait_tags": {"Pharmacy": 0.8, "Agri-Nature": 0.4, "Food-Science": 0.4}},
            {"option_id": 3935, "option_text": "Pharmacogenomics and personalized medicine", "trait_tags": {"Pharmacy": 0.9, "Lab-Research": 0.6, "Medical-Lab": 0.5}},
            {"option_id": 3936, "option_text": "Antibiotic resistance and infectious disease drugs", "trait_tags": {"Pharmacy": 0.9, "Lab-Research": 0.5, "Public-Health": 0.4}},
            {"option_id": 3937, "option_text": "Toxicology and poison control pharmacotherapy", "trait_tags": {"Pharmacy": 0.8, "Forensic-Sci": 0.4, "Medical-Lab": 0.4}},
            {"option_id": 3938, "option_text": "Pediatric and geriatric dosing and care", "trait_tags": {"Pharmacy": 0.9, "Patient-Care": 0.6, "People-Skill": 0.3}}
        ]
    },
    {
        "question_id": 436,
        "question_text": "How do you feel about patient counseling as a pharmacist?",
        "category": "Pharmacy - Counseling",
        "options": [
            {"option_id": 3939, "option_text": "Love it — educating patients is my priority", "trait_tags": {"Pharmacy": 0.9, "People-Skill": 0.7, "Teaching-Ed": 0.5}},
            {"option_id": 3940, "option_text": "Enjoy it when combined with clinical decision-making", "trait_tags": {"Pharmacy": 0.9, "Analytical-Skill": 0.5, "Patient-Care": 0.5}},
            {"option_id": 3941, "option_text": "Prefer behind-the-scenes compounding and dispensing", "trait_tags": {"Pharmacy": 0.8, "Lab-Research": 0.5, "Medical-Lab": 0.4}},
            {"option_id": 3942, "option_text": "I focus on accuracy and medication safety systems", "trait_tags": {"Pharmacy": 0.8, "Admin-Skill": 0.5, "Analytical-Skill": 0.5}},
            {"option_id": 3943, "option_text": "Prefer drug research over direct patient interaction", "trait_tags": {"Pharmacy": 0.7, "Lab-Research": 0.7, "Analytical-Skill": 0.4}},
            {"option_id": 3944, "option_text": "Enjoy public health campaigns on medication awareness", "trait_tags": {"Pharmacy": 0.7, "Public-Health": 0.6, "Community-Serve": 0.5}}
        ]
    },
    {
        "question_id": 437,
        "question_text": "Which pharmaceutical innovation excites you most?",
        "category": "Pharmacy - Innovation",
        "options": [
            {"option_id": 3945, "option_text": "New drug delivery systems and nanotechnology", "trait_tags": {"Pharmacy": 0.9, "Lab-Research": 0.6, "Technical-Skill": 0.4}},
            {"option_id": 3946, "option_text": "Digital health and telepharmacy services", "trait_tags": {"Pharmacy": 0.7, "Technical-Skill": 0.5, "Community-Serve": 0.5}},
            {"option_id": 3947, "option_text": "Vaccine development and immunotherapy", "trait_tags": {"Pharmacy": 0.8, "Lab-Research": 0.7, "Public-Health": 0.4}},
            {"option_id": 3948, "option_text": "Compounding custom medications for special needs", "trait_tags": {"Pharmacy": 0.9, "Patient-Care": 0.5, "Creative-Skill": 0.3}},
            {"option_id": 3949, "option_text": "AI-powered drug discovery and molecular design", "trait_tags": {"Pharmacy": 0.7, "AI-ML": 0.5, "Lab-Research": 0.5}},
            {"option_id": 3950, "option_text": "Pharmacovigilance and post-market drug surveillance", "trait_tags": {"Pharmacy": 0.8, "Analytical-Skill": 0.5, "Admin-Skill": 0.4}}
        ]
    },
    # --- TOURISM-TRAVEL (need 5) ---
    {
        "question_id": 438,
        "question_text": "Which tourism sector excites you most?",
        "category": "Tourism - Sector",
        "options": [
            {"option_id": 3951, "option_text": "Eco-tourism and nature-based travel experiences", "trait_tags": {"Tourism-Travel": 1.0, "Environmental-Sci": 0.5, "Agri-Nature": 0.4}},
            {"option_id": 3952, "option_text": "Luxury hospitality and resort management", "trait_tags": {"Tourism-Travel": 0.9, "Hospitality-Svc": 0.7, "Admin-Skill": 0.4}},
            {"option_id": 3953, "option_text": "Cultural heritage tourism and museum curation", "trait_tags": {"Tourism-Travel": 0.9, "Creative-Skill": 0.5, "Teaching-Ed": 0.4}},
            {"option_id": 3954, "option_text": "Adventure tourism and outdoor expedition guiding", "trait_tags": {"Tourism-Travel": 0.9, "Physical-Skill": 0.6, "Field-Research": 0.3}},
            {"option_id": 3955, "option_text": "Event tourism and convention management", "trait_tags": {"Tourism-Travel": 0.8, "Admin-Skill": 0.6, "Marketing-Sales": 0.4}},
            {"option_id": 3956, "option_text": "Medical and wellness tourism coordination", "trait_tags": {"Tourism-Travel": 0.7, "Patient-Care": 0.4, "Hospitality-Svc": 0.5}}
        ]
    },
    {
        "question_id": 439,
        "question_text": "How would you promote a travel destination?",
        "category": "Tourism - Marketing",
        "options": [
            {"option_id": 3957, "option_text": "Social media campaigns and influencer partnerships", "trait_tags": {"Tourism-Travel": 0.8, "Digital-Media": 0.7, "Marketing-Sales": 0.6}},
            {"option_id": 3958, "option_text": "Documentary-style video content and storytelling", "trait_tags": {"Tourism-Travel": 0.8, "Film-Broadcast": 0.6, "Creative-Skill": 0.5}},
            {"option_id": 3959, "option_text": "Data-driven targeting and travel analytics", "trait_tags": {"Tourism-Travel": 0.7, "Data-Analytics": 0.6, "Marketing-Sales": 0.5}},
            {"option_id": 3960, "option_text": "Community-based tourism and local partnerships", "trait_tags": {"Tourism-Travel": 0.8, "Community-Serve": 0.6, "People-Skill": 0.5}},
            {"option_id": 3961, "option_text": "Print brochures, travel expos, and trade shows", "trait_tags": {"Tourism-Travel": 0.8, "Admin-Skill": 0.4, "Marketing-Sales": 0.5}},
            {"option_id": 3962, "option_text": "Creating immersive virtual tours and online experiences", "trait_tags": {"Tourism-Travel": 0.7, "Technical-Skill": 0.5, "Digital-Media": 0.5}}
        ]
    },
    {
        "question_id": 440,
        "question_text": "What aspect of travel operations interests you most?",
        "category": "Tourism - Operations",
        "options": [
            {"option_id": 3963, "option_text": "Tour package design and itinerary planning", "trait_tags": {"Tourism-Travel": 1.0, "Admin-Skill": 0.5, "Creative-Skill": 0.4}},
            {"option_id": 3964, "option_text": "Airline and transportation logistics management", "trait_tags": {"Tourism-Travel": 0.8, "Industrial-Ops": 0.5, "Admin-Skill": 0.5}},
            {"option_id": 3965, "option_text": "Hotel and accommodation management", "trait_tags": {"Tourism-Travel": 0.8, "Hospitality-Svc": 0.7, "Admin-Skill": 0.4}},
            {"option_id": 3966, "option_text": "Tourist safety, insurance, and risk management", "trait_tags": {"Tourism-Travel": 0.8, "Law-Enforce": 0.3, "Admin-Skill": 0.5}},
            {"option_id": 3967, "option_text": "Sustainable tourism policy and environmental impact", "trait_tags": {"Tourism-Travel": 0.8, "Environmental-Sci": 0.6, "Community-Serve": 0.4}},
            {"option_id": 3968, "option_text": "Tour guiding and cross-cultural guest engagement", "trait_tags": {"Tourism-Travel": 0.9, "People-Skill": 0.7, "Teaching-Ed": 0.4}}
        ]
    },
    {
        "question_id": 441,
        "question_text": "Which type of tourist experience would you create?",
        "category": "Tourism - Experience Design",
        "options": [
            {"option_id": 3969, "option_text": "Food and culinary tourism trails", "trait_tags": {"Tourism-Travel": 0.8, "Culinary-Arts": 0.7, "Creative-Skill": 0.4}},
            {"option_id": 3970, "option_text": "Wildlife safari and nature photography tours", "trait_tags": {"Tourism-Travel": 0.8, "Agri-Nature": 0.5, "Field-Research": 0.4}},
            {"option_id": 3971, "option_text": "Historical walking tours and architectural excursions", "trait_tags": {"Tourism-Travel": 0.8, "Teaching-Ed": 0.5, "Spatial-Design": 0.3}},
            {"option_id": 3972, "option_text": "Extreme sports and adrenaline-fueled adventures", "trait_tags": {"Tourism-Travel": 0.7, "Physical-Skill": 0.7, "Sports-Ed": 0.3}},
            {"option_id": 3973, "option_text": "Wellness retreats and spa tourism packages", "trait_tags": {"Tourism-Travel": 0.8, "Patient-Care": 0.3, "Hospitality-Svc": 0.5}},
            {"option_id": 3974, "option_text": "Festival tourism and live entertainment events", "trait_tags": {"Tourism-Travel": 0.8, "Performing-Arts": 0.5, "People-Skill": 0.4}}
        ]
    },
    {
        "question_id": 442,
        "question_text": "What is your view on technology in the tourism industry?",
        "category": "Tourism - Technology",
        "options": [
            {"option_id": 3975, "option_text": "Essential — online booking platforms drive tourism", "trait_tags": {"Tourism-Travel": 0.8, "Web-Dev": 0.5, "Technical-Skill": 0.4}},
            {"option_id": 3976, "option_text": "VR and AR enhance destination previews", "trait_tags": {"Tourism-Travel": 0.7, "Technical-Skill": 0.5, "Digital-Media": 0.5}},
            {"option_id": 3977, "option_text": "Big data helps personalize travel recommendations", "trait_tags": {"Tourism-Travel": 0.7, "Data-Analytics": 0.6, "AI-ML": 0.3}},
            {"option_id": 3978, "option_text": "Mobile apps are key for on-the-go traveler support", "trait_tags": {"Tourism-Travel": 0.7, "Mobile-Dev": 0.5, "Technical-Skill": 0.4}},
            {"option_id": 3979, "option_text": "Technology supplements but personal touch matters most", "trait_tags": {"Tourism-Travel": 0.8, "People-Skill": 0.6, "Hospitality-Svc": 0.4}},
            {"option_id": 3980, "option_text": "Social media and content creation attract modern travelers", "trait_tags": {"Tourism-Travel": 0.7, "Digital-Media": 0.6, "Marketing-Sales": 0.5}}
        ]
    },
]

# ============================================================
# STEP 3: Add new questions to questions_enhanced.py
# ============================================================
with open('questions_enhanced.py', 'r', encoding='utf-8') as f:
    qfile = f.read()

# Find the insert point: just before TRAIT_SECONDARY_MAP
insert_marker = "TRAIT_SECONDARY_MAP = {"
insert_pos = qfile.find(insert_marker)
if insert_pos == -1:
    print("ERROR: Could not find TRAIT_SECONDARY_MAP marker")
    exit(1)

# Build question text
new_q_lines = []
for q in NEW_QUESTIONS:
    lines = []
    lines.append("    {")
    lines.append(f'        "question_id": {q["question_id"]},')
    lines.append(f'        "question_text": "{q["question_text"]}",')
    lines.append(f'        "category": "{q["category"]}",')
    lines.append('        "options": [')
    for i, opt in enumerate(q["options"]):
        tag_str = ", ".join(f'"{k}": {v}' for k, v in opt["trait_tags"].items())
        comma = "," if i < len(q["options"]) - 1 else ""
        lines.append(f'            {{"option_id": {opt["option_id"]}, "option_text": "{opt["option_text"]}", "trait_tags": {{{tag_str}}}}}{comma}')
    lines.append("        ]")
    lines.append("    },")
    new_q_lines.append("\n".join(lines))

# Find the last ] before TRAIT_SECONDARY_MAP (end of QUESTIONS_POOL_ENHANCED)
bracket_pos = qfile.rfind("]", 0, insert_pos)
# Go back to find the last }, before ]
last_entry_end = qfile.rfind("}", 0, bracket_pos)

# Insert after the last } of the last question entry but before ]
new_questions_text = "\n" + "\n".join(new_q_lines) + "\n"
# We need to add after the closing } of last entry with a comma
# Check if there's already a comma after the last }
after_last = qfile[last_entry_end+1:bracket_pos].strip()
if not after_last.startswith(","):
    # The last entry might need a comma
    pass

# Simpler approach: insert before the closing ]
insert_text = "\n    # ==================== GAP-FILL QUESTIONS (424-442) ====================\n" + "\n".join(new_q_lines) + "\n"
qfile = qfile[:bracket_pos] + insert_text + qfile[bracket_pos:]

with open('questions_enhanced.py', 'w', encoding='utf-8') as f:
    f.write(qfile)
print(f"Added {len(NEW_QUESTIONS)} new questions (Q424-Q442) to questions_enhanced.py")

# ============================================================
# STEP 4: Update TRAIT_FOLLOWUP_MAP in adaptive_assessment.py
# ============================================================

# Reload with new questions
import importlib
import questions_enhanced
importlib.reload(questions_enhanced)
from questions_enhanced import QUESTIONS_POOL_ENHANCED as QP

# Rebuild trait_to_scored with new questions
trait_to_scored = {}
for q in QP:
    qid = q['question_id']
    for opt in q['options']:
        for trait, score in opt['trait_tags'].items():
            if score >= 0.5:
                if trait not in trait_to_scored:
                    trait_to_scored[trait] = {}
                trait_to_scored[trait][qid] = max(trait_to_scored[trait].get(qid, 0), score)

# Build new map
new_followup_map = {}
for trait in sorted(TRAIT_FOLLOWUP_MAP.keys()):
    current = list(TRAIT_FOLLOWUP_MAP[trait])
    current_set = set(current)
    need = 30 - len(current)
    if need <= 0:
        new_followup_map[trait] = current[:30]
        continue
    
    available = trait_to_scored.get(trait, {})
    missing = {qid: score for qid, score in available.items() if qid not in current_set}
    best = sorted(missing.items(), key=lambda x: -x[1])[:need]
    new_followup_map[trait] = current + [qid for qid, _ in best]

# Verify all traits hit 30
short = {t: len(v) for t, v in new_followup_map.items() if len(v) < 30}
if short:
    print(f"WARNING: These traits still under 30: {short}")
else:
    print("All 52 traits have 30 questions!")

# Also update DOMAIN_ENTRY_QUESTIONS: fill each to 30 using domain-tagged questions
# Build domain mapping from QUESTION_TREE_NODES
domain_to_questions = {}
for qid, node in QUESTION_TREE_NODES.items():
    for branch in node.get("branches", []):
        domain_to_questions.setdefault(branch, set()).add(qid)

# Add new Q424-442 to QUESTION_TREE_NODES mapping
new_q_branches = {
    424: ["hospitality", "creative"],
    425: ["engineering", "science"],
    426: ["business", "public_service"],
    427: ["business", "public_service"],
    428: ["business", "education"],
    429: ["healthcare", "public_service"],
    430: ["healthcare", "business"],
    431: ["healthcare", "public_service"],
    432: ["technology", "creative"],
    433: ["technology", "engineering"],
    434: ["healthcare", "science"],
    435: ["healthcare", "science"],
    436: ["healthcare", "public_service"],
    437: ["healthcare", "science", "technology"],
    438: ["hospitality", "business"],
    439: ["hospitality", "business", "creative"],
    440: ["hospitality", "business"],
    441: ["hospitality", "creative"],
    442: ["hospitality", "technology"],
}

for qid, branches in new_q_branches.items():
    for b in branches:
        domain_to_questions.setdefault(b, set()).add(qid)

new_domain_entry = {}
for domain in sorted(DOMAIN_ENTRY_QUESTIONS.keys()):
    current = list(DOMAIN_ENTRY_QUESTIONS[domain])
    current_set = set(current)
    need = 30 - len(current)
    if need <= 0:
        new_domain_entry[domain] = current[:30]
        continue
    
    available = domain_to_questions.get(domain, set()) - current_set
    extra = sorted(available)[:need]
    new_domain_entry[domain] = current + extra

# Generate the code for adaptive_assessment.py
with open('adaptive_assessment.py', 'r', encoding='utf-8') as f:
    afile = f.read()

# --- Update QUESTION_TREE_NODES: add new entries ---
tree_insert_marker = "QUESTION_TREE_NODES = {"
tree_end = afile.find("}", afile.find(tree_insert_marker) + len(tree_insert_marker))
# Find proper end - need to handle nested {}
pos = afile.find(tree_insert_marker)
if pos == -1:
    print("ERROR: Can't find QUESTION_TREE_NODES")
    exit(1)

# Find the end of QUESTION_TREE_NODES dict by looking for the line starting with }
import re as regex
# Find the pattern: newline + } + newline that ends QUESTION_TREE_NODES
# Safer: find "DOMAIN_ENTRY_QUESTIONS" and go backwards to find the closing }
domain_entry_pos = afile.find("DOMAIN_ENTRY_QUESTIONS")
tree_end = afile.rfind("}", pos, domain_entry_pos)

# Insert new tree node entries before the closing }
new_tree_entries = []
for qid, branches in sorted(new_q_branches.items()):
    branches_str = str(branches)
    new_tree_entries.append(f'    {qid}: {{"branches": {branches_str}, "depth": 2}},')

tree_insert_text = "\n    # Gap-fill questions (424-442)\n" + "\n".join(new_tree_entries) + "\n"
afile = afile[:tree_end] + tree_insert_text + afile[tree_end:]

# Now update DOMAIN_ENTRY_QUESTIONS
# Find and replace the entire DOMAIN_ENTRY_QUESTIONS dict
de_start = afile.find("DOMAIN_ENTRY_QUESTIONS = {")
if de_start == -1:
    print("ERROR: Can't find DOMAIN_ENTRY_QUESTIONS")
    exit(1)

# Find the closing }
depth = 0
de_content_start = afile.find("{", de_start)
for i in range(de_content_start, len(afile)):
    if afile[i] == '{':
        depth += 1
    elif afile[i] == '}':
        depth -= 1
        if depth == 0:
            de_end = i + 1
            break

de_new = "DOMAIN_ENTRY_QUESTIONS = {\n"
for domain in sorted(new_domain_entry.keys()):
    ids = new_domain_entry[domain]
    de_new += f'    "{domain}": {ids},\n'
de_new += "}"

afile = afile[:de_start] + de_new + afile[de_end:]

# Now update TRAIT_FOLLOWUP_MAP
tf_start = afile.find("TRAIT_FOLLOWUP_MAP = {")
if tf_start == -1:
    print("ERROR: Can't find TRAIT_FOLLOWUP_MAP")
    exit(1)

depth = 0
tf_content_start = afile.find("{", tf_start)
for i in range(tf_content_start, len(afile)):
    if afile[i] == '{':
        depth += 1
    elif afile[i] == '}':
        depth -= 1
        if depth == 0:
            tf_end = i + 1
            break

tf_new = "TRAIT_FOLLOWUP_MAP = {\n"
for trait in sorted(new_followup_map.keys()):
    ids = new_followup_map[trait]
    tf_new += f'    "{trait}": {ids},\n'
tf_new += "}"

afile = afile[:tf_start] + tf_new + afile[tf_end:]

with open('adaptive_assessment.py', 'w', encoding='utf-8') as f:
    f.write(afile)

print("Updated adaptive_assessment.py: QUESTION_TREE_NODES, DOMAIN_ENTRY_QUESTIONS, TRAIT_FOLLOWUP_MAP")
print("\nDone!")
