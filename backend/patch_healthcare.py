#!/usr/bin/env python3
"""
Phase 2: Add dedicated Healthcare questions.
Covers: Public-Health, Pharmacy, Medical-Lab, Rehab-Therapy,
        Nutrition-Diet, Health-Admin, Counseling, Patient-Care
"""
import re, sys, os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Starting IDs: Q457+, options 4065+
QID = 457
OID = 4065

def nq(text, weight, qtags, options):
    """Helper to build a question dict."""
    global QID, OID
    opts = []
    for (otext, otags) in options:
        opts.append({"option_id": OID, "option_text": otext, "trait_tags": otags})
        OID += 1
    q = {"question_id": QID, "question_text": text, "weight": weight,
         "trait_tags": qtags, "options": opts}
    QID += 1
    return q

HEALTHCARE_QUESTIONS = []

# ===== PUBLIC-HEALTH (currently 2 on-topic, need ~23 more) =====
for text, qtags, opts in [
    ("What public health initiative would you most want to lead?",
     {"Public-Health": 0.9},
     [("Vaccination and immunization campaigns", {"Public-Health": 1.0, "Community-Serve": 0.5, "Patient-Care": 0.3}),
      ("Disease surveillance and outbreak response", {"Public-Health": 1.0, "Data-Analytics": 0.5, "Lab-Research": 0.3}),
      ("Health education and awareness programs", {"Public-Health": 0.9, "Teaching-Ed": 0.5, "Community-Serve": 0.4}),
      ("Water quality and sanitation improvement", {"Public-Health": 0.9, "Environmental-Eng": 0.5, "Field-Research": 0.3}),
      ("Maternal and child health services", {"Public-Health": 0.9, "Patient-Care": 0.5, "Counseling": 0.3}),
      ("Nutrition programs for underserved communities", {"Public-Health": 0.8, "Nutrition-Diet": 0.6, "Community-Serve": 0.4})]),
    ("Which epidemiology topic interests you most?",
     {"Public-Health": 0.9, "Data-Analytics": 0.3},
     [("Tracking infectious disease spread patterns", {"Public-Health": 1.0, "Data-Analytics": 0.5, "Lab-Research": 0.3}),
      ("Chronic disease risk factor analysis", {"Public-Health": 0.9, "Data-Analytics": 0.5, "Analytical-Skill": 0.4}),
      ("Environmental health hazard assessment", {"Public-Health": 0.9, "Environmental-Sci": 0.5, "Field-Research": 0.3}),
      ("Occupational health and workplace safety", {"Public-Health": 0.9, "Industrial-Ops": 0.4, "Admin-Skill": 0.3}),
      ("Mental health prevalence studies", {"Public-Health": 0.9, "Counseling": 0.5, "Data-Analytics": 0.3}),
      ("Vaccine efficacy and population impact", {"Public-Health": 1.0, "Lab-Research": 0.5, "Data-Analytics": 0.3})]),
    ("What health promotion strategy appeals to you most?",
     {"Public-Health": 0.9, "Community-Serve": 0.3},
     [("Community health worker training programs", {"Public-Health": 1.0, "Teaching-Ed": 0.5, "Community-Serve": 0.4}),
      ("Social media health awareness campaigns", {"Public-Health": 0.9, "Digital-Media": 0.5, "Marketing-Sales": 0.3}),
      ("School-based health education curricula", {"Public-Health": 0.9, "Teaching-Ed": 0.5, "Nutrition-Diet": 0.3}),
      ("Barangay health center capacity building", {"Public-Health": 0.9, "Community-Serve": 0.5, "Admin-Skill": 0.3}),
      ("Policy advocacy for health legislation", {"Public-Health": 0.9, "Legal-Practice": 0.4, "People-Skill": 0.4}),
      ("Research-based intervention design", {"Public-Health": 0.8, "Lab-Research": 0.5, "Data-Analytics": 0.4})]),
    ("Which public health emergency response role suits you?",
     {"Public-Health": 0.9, "People-Skill": 0.3},
     [("Epidemiological investigation team lead", {"Public-Health": 1.0, "Analytical-Skill": 0.5, "Field-Research": 0.3}),
      ("Contact tracing and quarantine coordinator", {"Public-Health": 0.9, "People-Skill": 0.5, "Admin-Skill": 0.4}),
      ("Laboratory testing and sample management", {"Public-Health": 0.8, "Medical-Lab": 0.6, "Lab-Research": 0.4}),
      ("Risk communication and media briefing", {"Public-Health": 0.9, "People-Skill": 0.5, "Digital-Media": 0.3}),
      ("Logistics for medical supply distribution", {"Public-Health": 0.9, "Industrial-Ops": 0.5, "Admin-Skill": 0.3}),
      ("Community health volunteer coordination", {"Public-Health": 0.9, "Community-Serve": 0.5, "People-Skill": 0.4})]),
    ("What aspect of healthcare policy would you want to shape?",
     {"Public-Health": 0.9, "Legal-Practice": 0.3},
     [("Universal health coverage implementation", {"Public-Health": 1.0, "Admin-Skill": 0.4, "Community-Serve": 0.3}),
      ("Disease prevention funding allocation", {"Public-Health": 0.9, "Finance-Acct": 0.4, "Analytical-Skill": 0.3}),
      ("Healthcare worker deployment policies", {"Public-Health": 0.9, "HR-Management": 0.5, "Admin-Skill": 0.3}),
      ("Pharmaceutical regulation and access", {"Public-Health": 0.8, "Pharmacy": 0.5, "Legal-Practice": 0.4}),
      ("Environmental health standards enforcement", {"Public-Health": 0.9, "Environmental-Sci": 0.4, "Law-Enforce": 0.3}),
      ("Mental health legislation and programs", {"Public-Health": 0.9, "Counseling": 0.5, "Legal-Practice": 0.3})]),
    ("Which global health concern motivates you most?",
     {"Public-Health": 0.9},
     [("Pandemic preparedness and response systems", {"Public-Health": 1.0, "Data-Analytics": 0.4, "Lab-Research": 0.3}),
      ("Antimicrobial resistance prevention", {"Public-Health": 0.9, "Pharmacy": 0.5, "Lab-Research": 0.4}),
      ("Climate change effects on health", {"Public-Health": 0.9, "Environmental-Sci": 0.5, "Field-Research": 0.3}),
      ("Health equity and access in rural areas", {"Public-Health": 0.9, "Community-Serve": 0.5, "Social-Work": 0.4}),
      ("Non-communicable disease prevention", {"Public-Health": 1.0, "Nutrition-Diet": 0.4, "Counseling": 0.3}),
      ("Digital health and telemedicine expansion", {"Public-Health": 0.8, "Software-Dev": 0.5, "Technical-Skill": 0.4})]),
    ("What public health data analysis task excites you?",
     {"Public-Health": 0.9, "Data-Analytics": 0.4},
     [("Mapping disease hotspots with GIS", {"Public-Health": 1.0, "Data-Analytics": 0.6, "Software-Dev": 0.3}),
      ("Analyzing hospital admission trends", {"Public-Health": 0.9, "Data-Analytics": 0.5, "Health-Admin": 0.3}),
      ("Monitoring vaccination coverage rates", {"Public-Health": 1.0, "Data-Analytics": 0.5, "Community-Serve": 0.3}),
      ("Studying demographic health survey results", {"Public-Health": 0.9, "Analytical-Skill": 0.5, "Data-Analytics": 0.4}),
      ("Evaluating health program effectiveness", {"Public-Health": 0.9, "Analytical-Skill": 0.5, "Admin-Skill": 0.3}),
      ("Forecasting disease burden for budget planning", {"Public-Health": 0.9, "Data-Analytics": 0.5, "Finance-Acct": 0.3})]),
    ("Where would you most want to practice public health?",
     {"Public-Health": 0.9},
     [("DOH regional epidemiology office", {"Public-Health": 1.0, "Data-Analytics": 0.4, "Admin-Skill": 0.3}),
      ("WHO or UNICEF international programs", {"Public-Health": 1.0, "Community-Serve": 0.4, "People-Skill": 0.3}),
      ("Municipal or barangay health unit", {"Public-Health": 0.9, "Community-Serve": 0.5, "People-Skill": 0.4}),
      ("University public health research center", {"Public-Health": 0.9, "Lab-Research": 0.5, "Teaching-Ed": 0.3}),
      ("NGO running health outreach programs", {"Public-Health": 0.9, "Community-Serve": 0.5, "Social-Work": 0.4}),
      ("Hospital infection prevention department", {"Public-Health": 0.8, "Patient-Care": 0.5, "Medical-Lab": 0.3})]),
]:
    HEALTHCARE_QUESTIONS.append(nq(text, 1.5, qtags, opts))

# ===== MEDICAL-LAB (currently 2 on-topic, need ~23 more) =====
for text, qtags, opts in [
    ("Which medical laboratory specialization excites you most?",
     {"Medical-Lab": 0.9},
     [("Clinical chemistry and blood analysis", {"Medical-Lab": 1.0, "Lab-Research": 0.5, "Analytical-Skill": 0.3}),
      ("Hematology and blood cell examination", {"Medical-Lab": 1.0, "Lab-Research": 0.4, "Patient-Care": 0.3}),
      ("Microbiology and culture identification", {"Medical-Lab": 0.9, "Lab-Research": 0.6, "Environmental-Sci": 0.3}),
      ("Histopathology and tissue analysis", {"Medical-Lab": 0.9, "Lab-Research": 0.5, "Analytical-Skill": 0.3}),
      ("Immunology and serology testing", {"Medical-Lab": 0.9, "Lab-Research": 0.5, "Pharmacy": 0.3}),
      ("Blood banking and transfusion services", {"Medical-Lab": 1.0, "Patient-Care": 0.4, "Admin-Skill": 0.3})]),
    ("What lab equipment would you most want to master?",
     {"Medical-Lab": 0.9, "Technical-Skill": 0.3},
     [("Automated chemistry analyzer", {"Medical-Lab": 1.0, "Technical-Skill": 0.5, "Data-Analytics": 0.3}),
      ("Microscope for cell morphology studies", {"Medical-Lab": 0.9, "Lab-Research": 0.5, "Analytical-Skill": 0.4}),
      ("Flow cytometry cell counter", {"Medical-Lab": 0.9, "Technical-Skill": 0.5, "Data-Analytics": 0.4}),
      ("PCR machine for molecular diagnostics", {"Medical-Lab": 0.9, "Lab-Research": 0.6, "Technical-Skill": 0.4}),
      ("Blood gas analyzer for critical care", {"Medical-Lab": 1.0, "Patient-Care": 0.4, "Technical-Skill": 0.3}),
      ("Culture incubator and identification system", {"Medical-Lab": 0.9, "Lab-Research": 0.5, "Technical-Skill": 0.3})]),
    ("What role would you play in a diagnostic laboratory?",
     {"Medical-Lab": 0.9},
     [("Running routine patient sample tests", {"Medical-Lab": 1.0, "Patient-Care": 0.4, "Technical-Skill": 0.3}),
      ("Quality control and instrument calibration", {"Medical-Lab": 0.9, "Analytical-Skill": 0.5, "Technical-Skill": 0.4}),
      ("Interpreting abnormal results and flagging", {"Medical-Lab": 0.9, "Analytical-Skill": 0.5, "Patient-Care": 0.4}),
      ("Research and method development", {"Medical-Lab": 0.8, "Lab-Research": 0.6, "Analytical-Skill": 0.4}),
      ("Lab safety and biohazard management", {"Medical-Lab": 0.9, "Admin-Skill": 0.4, "Environmental-Sci": 0.3}),
      ("Supervising and training lab technicians", {"Medical-Lab": 0.8, "Teaching-Ed": 0.5, "People-Skill": 0.4})]),
    ("Which sample type would you prefer working with?",
     {"Medical-Lab": 0.9, "Lab-Research": 0.3},
     [("Blood specimens for hematology profiles", {"Medical-Lab": 1.0, "Lab-Research": 0.4, "Patient-Care": 0.3}),
      ("Urine for chemical and microscopic analysis", {"Medical-Lab": 0.9, "Lab-Research": 0.5, "Analytical-Skill": 0.3}),
      ("Tissue biopsies for pathology review", {"Medical-Lab": 0.9, "Lab-Research": 0.5, "Analytical-Skill": 0.4}),
      ("Bacterial cultures from wound or throat swabs", {"Medical-Lab": 0.9, "Lab-Research": 0.5, "Environmental-Sci": 0.3}),
      ("Cerebrospinal fluid for neurological tests", {"Medical-Lab": 1.0, "Lab-Research": 0.5, "Patient-Care": 0.3}),
      ("Genetic samples for molecular analysis", {"Medical-Lab": 0.8, "Lab-Research": 0.6, "Data-Analytics": 0.3})]),
    ("What motivates you most about medical lab work?",
     {"Medical-Lab": 0.9},
     [("Helping doctors diagnose diseases accurately", {"Medical-Lab": 1.0, "Patient-Care": 0.5, "Analytical-Skill": 0.3}),
      ("Working with precision instruments and technology", {"Medical-Lab": 0.9, "Technical-Skill": 0.5, "Hardware-Systems": 0.3}),
      ("Discovering new pathogens or biomarkers", {"Medical-Lab": 0.9, "Lab-Research": 0.6, "Field-Research": 0.3}),
      ("Ensuring blood supply safety through screening", {"Medical-Lab": 1.0, "Patient-Care": 0.4, "Admin-Skill": 0.3}),
      ("Performing quality assurance on test results", {"Medical-Lab": 0.9, "Analytical-Skill": 0.5, "Admin-Skill": 0.3}),
      ("Training the next generation of med techs", {"Medical-Lab": 0.8, "Teaching-Ed": 0.5, "People-Skill": 0.4})]),
    ("Where would you most want to work as a medical technologist?",
     {"Medical-Lab": 0.9},
     [("Hospital clinical laboratory", {"Medical-Lab": 1.0, "Patient-Care": 0.4, "Technical-Skill": 0.3}),
      ("Research university laboratory", {"Medical-Lab": 0.9, "Lab-Research": 0.5, "Teaching-Ed": 0.3}),
      ("Public health reference laboratory", {"Medical-Lab": 0.9, "Public-Health": 0.5, "Data-Analytics": 0.3}),
      ("Forensic and crime laboratory", {"Medical-Lab": 0.8, "Forensic-Sci": 0.6, "Law-Enforce": 0.3}),
      ("Pharmaceutical testing laboratory", {"Medical-Lab": 0.9, "Pharmacy": 0.5, "Lab-Research": 0.3}),
      ("Veterinary diagnostic laboratory", {"Medical-Lab": 0.8, "Agri-Nature": 0.4, "Lab-Research": 0.4})]),
    ("What lab quality practice matters most to you?",
     {"Medical-Lab": 0.9, "Analytical-Skill": 0.3},
     [("Daily calibration of analyzers", {"Medical-Lab": 1.0, "Technical-Skill": 0.5, "Analytical-Skill": 0.3}),
      ("Proficiency testing and external QA", {"Medical-Lab": 0.9, "Analytical-Skill": 0.5, "Admin-Skill": 0.3}),
      ("Standard operating procedure compliance", {"Medical-Lab": 0.9, "Admin-Skill": 0.5, "Legal-Practice": 0.3}),
      ("Specimen collection and handling protocols", {"Medical-Lab": 1.0, "Patient-Care": 0.4, "Physical-Skill": 0.3}),
      ("Result verification and validation", {"Medical-Lab": 0.9, "Analytical-Skill": 0.5, "Data-Analytics": 0.3}),
      ("Inventory and reagent management", {"Medical-Lab": 0.8, "Admin-Skill": 0.5, "Industrial-Ops": 0.3})]),
    ("Which emerging lab technology fascinates you?",
     {"Medical-Lab": 0.9, "Technical-Skill": 0.4},
     [("Point-of-care rapid testing devices", {"Medical-Lab": 1.0, "Technical-Skill": 0.5, "Patient-Care": 0.3}),
      ("Next-generation DNA sequencing platforms", {"Medical-Lab": 0.9, "Lab-Research": 0.6, "Data-Analytics": 0.3}),
      ("Mass spectrometry for clinical diagnostics", {"Medical-Lab": 0.9, "Technical-Skill": 0.5, "Lab-Research": 0.4}),
      ("Digital pathology and AI-assisted analysis", {"Medical-Lab": 0.8, "AI-ML": 0.5, "Data-Analytics": 0.4}),
      ("Automated liquid handling robots", {"Medical-Lab": 0.9, "Technical-Skill": 0.5, "Industrial-Ops": 0.3}),
      ("Lab information management systems", {"Medical-Lab": 0.9, "Software-Dev": 0.4, "Admin-Skill": 0.4})]),
]:
    HEALTHCARE_QUESTIONS.append(nq(text, 1.5, qtags, opts))

# ===== NUTRITION-DIET (currently 2 on-topic, need ~23 more) =====
for text, qtags, opts in [
    ("What area of nutrition science interests you most?",
     {"Nutrition-Diet": 0.9},
     [("Clinical nutrition and therapeutic diets", {"Nutrition-Diet": 1.0, "Patient-Care": 0.5, "Analytical-Skill": 0.3}),
      ("Sports nutrition and athletic performance", {"Nutrition-Diet": 0.9, "Sports-Ed": 0.5, "Physical-Skill": 0.4}),
      ("Community nutrition and public feeding programs", {"Nutrition-Diet": 0.9, "Community-Serve": 0.5, "Public-Health": 0.4}),
      ("Food science and product development", {"Nutrition-Diet": 0.8, "Food-Science": 0.6, "Lab-Research": 0.3}),
      ("Pediatric nutrition and child growth", {"Nutrition-Diet": 1.0, "Patient-Care": 0.4, "Teaching-Ed": 0.3}),
      ("Nutrition research and dietary studies", {"Nutrition-Diet": 0.9, "Lab-Research": 0.5, "Data-Analytics": 0.3})]),
    ("Which nutrition counseling scenario excites you?",
     {"Nutrition-Diet": 0.9, "Counseling": 0.3},
     [("Helping a diabetic patient plan their meals", {"Nutrition-Diet": 1.0, "Patient-Care": 0.5, "Counseling": 0.4}),
      ("Designing a meal plan for an athlete", {"Nutrition-Diet": 0.9, "Sports-Ed": 0.5, "Physical-Skill": 0.3}),
      ("Guiding pregnant women on prenatal nutrition", {"Nutrition-Diet": 1.0, "Patient-Care": 0.5, "Counseling": 0.3}),
      ("Planning menus for school feeding programs", {"Nutrition-Diet": 0.9, "Community-Serve": 0.5, "Admin-Skill": 0.3}),
      ("Teaching children about healthy food choices", {"Nutrition-Diet": 0.9, "Teaching-Ed": 0.5, "Community-Serve": 0.3}),
      ("Advising elderly patients on bone-health diets", {"Nutrition-Diet": 1.0, "Patient-Care": 0.5, "Counseling": 0.3})]),
    ("What nutrition-related research would you pursue?",
     {"Nutrition-Diet": 0.9, "Lab-Research": 0.3},
     [("Impact of Filipino diet on chronic disease", {"Nutrition-Diet": 1.0, "Public-Health": 0.5, "Data-Analytics": 0.3}),
      ("Micronutrient deficiency in rural communities", {"Nutrition-Diet": 0.9, "Community-Serve": 0.5, "Field-Research": 0.3}),
      ("Food fortification effectiveness studies", {"Nutrition-Diet": 0.9, "Food-Science": 0.5, "Lab-Research": 0.4}),
      ("Gut microbiome and nutritional health links", {"Nutrition-Diet": 0.8, "Lab-Research": 0.6, "Medical-Lab": 0.3}),
      ("Herbal and traditional food nutrient analysis", {"Nutrition-Diet": 0.9, "Lab-Research": 0.5, "Agri-Nature": 0.3}),
      ("Obesity prevention program evaluation", {"Nutrition-Diet": 1.0, "Public-Health": 0.5, "Data-Analytics": 0.3})]),
    ("Where would you most want to practice nutrition?",
     {"Nutrition-Diet": 0.9},
     [("Hospital dietetics department", {"Nutrition-Diet": 1.0, "Patient-Care": 0.5, "Health-Admin": 0.3}),
      ("Sports team nutritionist", {"Nutrition-Diet": 0.9, "Sports-Ed": 0.5, "Physical-Skill": 0.3}),
      ("Community health center", {"Nutrition-Diet": 0.9, "Community-Serve": 0.5, "Public-Health": 0.4}),
      ("Food manufacturing quality lab", {"Nutrition-Diet": 0.8, "Food-Science": 0.6, "Lab-Research": 0.3}),
      ("School nutrition program coordinator", {"Nutrition-Diet": 0.9, "Teaching-Ed": 0.5, "Admin-Skill": 0.3}),
      ("Private wellness and diet clinic", {"Nutrition-Diet": 0.9, "Counseling": 0.5, "Startup-Venture": 0.3})]),
    ("What aspect of meal planning do you find most rewarding?",
     {"Nutrition-Diet": 0.9},
     [("Calculating exact macro and micro nutrients", {"Nutrition-Diet": 1.0, "Analytical-Skill": 0.5, "Data-Analytics": 0.3}),
      ("Creating delicious yet therapeutic recipes", {"Nutrition-Diet": 0.9, "Culinary-Arts": 0.5, "Creative-Skill": 0.3}),
      ("Accommodating food allergies and restrictions", {"Nutrition-Diet": 1.0, "Patient-Care": 0.4, "Analytical-Skill": 0.3}),
      ("Planning cost-effective community meals", {"Nutrition-Diet": 0.9, "Community-Serve": 0.5, "Finance-Acct": 0.3}),
      ("Adapting local Filipino ingredients for health", {"Nutrition-Diet": 0.9, "Culinary-Arts": 0.5, "Agri-Nature": 0.3}),
      ("Tracking patient dietary compliance", {"Nutrition-Diet": 0.9, "Counseling": 0.4, "Data-Analytics": 0.3})]),
    ("Which nutrition assessment method interests you most?",
     {"Nutrition-Diet": 0.9, "Analytical-Skill": 0.3},
     [("Anthropometric measurements and growth charts", {"Nutrition-Diet": 1.0, "Analytical-Skill": 0.5, "Patient-Care": 0.3}),
      ("Dietary recall and food diary analysis", {"Nutrition-Diet": 0.9, "Data-Analytics": 0.5, "Counseling": 0.3}),
      ("Biochemical nutrient level testing", {"Nutrition-Diet": 0.8, "Medical-Lab": 0.6, "Lab-Research": 0.3}),
      ("Body composition analysis technology", {"Nutrition-Diet": 0.9, "Technical-Skill": 0.5, "Physical-Skill": 0.3}),
      ("Clinical nutrition physical examination", {"Nutrition-Diet": 1.0, "Patient-Care": 0.5, "Analytical-Skill": 0.3}),
      ("Community nutrition survey methods", {"Nutrition-Diet": 0.9, "Public-Health": 0.5, "Data-Analytics": 0.3})]),
    ("What nutrition challenge would you most want to solve?",
     {"Nutrition-Diet": 0.9, "Community-Serve": 0.3},
     [("Child malnutrition in underserved areas", {"Nutrition-Diet": 1.0, "Community-Serve": 0.5, "Public-Health": 0.4}),
      ("Rising diabetes rates from poor diet", {"Nutrition-Diet": 1.0, "Patient-Care": 0.4, "Public-Health": 0.3}),
      ("Food insecurity in disaster-prone regions", {"Nutrition-Diet": 0.9, "Community-Serve": 0.5, "Social-Work": 0.3}),
      ("Iron deficiency anemia in Filipino women", {"Nutrition-Diet": 0.9, "Public-Health": 0.5, "Medical-Lab": 0.3}),
      ("Promoting breastfeeding in working mothers", {"Nutrition-Diet": 0.9, "Counseling": 0.5, "People-Skill": 0.3}),
      ("Junk food and obesity in Filipino youth", {"Nutrition-Diet": 1.0, "Teaching-Ed": 0.4, "Public-Health": 0.3})]),
]:
    HEALTHCARE_QUESTIONS.append(nq(text, 1.5, qtags, opts))

# ===== REHAB-THERAPY (currently 4 on-topic, need ~21 more) =====
for text, qtags, opts in [
    ("What type of rehabilitation patient would you most want to help?",
     {"Rehab-Therapy": 0.9},
     [("Stroke survivors regaining motor function", {"Rehab-Therapy": 1.0, "Patient-Care": 0.5, "Physical-Skill": 0.3}),
      ("Athletes recovering from sports injuries", {"Rehab-Therapy": 0.9, "Sports-Ed": 0.5, "Physical-Skill": 0.4}),
      ("Children with developmental delays", {"Rehab-Therapy": 0.9, "Patient-Care": 0.5, "Teaching-Ed": 0.3}),
      ("Workers with repetitive strain injuries", {"Rehab-Therapy": 0.9, "Industrial-Ops": 0.4, "Physical-Skill": 0.3}),
      ("Elderly patients maintaining independence", {"Rehab-Therapy": 1.0, "Patient-Care": 0.5, "Counseling": 0.3}),
      ("Amputees learning to use prosthetics", {"Rehab-Therapy": 0.9, "Technical-Skill": 0.4, "Patient-Care": 0.4})]),
    ("Which rehabilitation therapy technique interests you?",
     {"Rehab-Therapy": 0.9, "Physical-Skill": 0.3},
     [("Therapeutic exercise and strength training", {"Rehab-Therapy": 1.0, "Physical-Skill": 0.6, "Sports-Ed": 0.3}),
      ("Electrotherapy and ultrasound treatment", {"Rehab-Therapy": 0.9, "Technical-Skill": 0.5, "Hardware-Systems": 0.3}),
      ("Hydrotherapy and aquatic rehabilitation", {"Rehab-Therapy": 0.9, "Physical-Skill": 0.5, "Maritime-Sea": 0.2}),
      ("Manual therapy and joint mobilization", {"Rehab-Therapy": 1.0, "Physical-Skill": 0.5, "Patient-Care": 0.3}),
      ("Cognitive rehabilitation exercises", {"Rehab-Therapy": 0.9, "Counseling": 0.5, "Teaching-Ed": 0.3}),
      ("Assistive device and orthotics fitting", {"Rehab-Therapy": 0.9, "Mechanical-Design": 0.4, "Technical-Skill": 0.4})]),
    ("Where would you most want to practice rehabilitation?",
     {"Rehab-Therapy": 0.9},
     [("Hospital rehabilitation department", {"Rehab-Therapy": 1.0, "Patient-Care": 0.5, "Health-Admin": 0.3}),
      ("Sports medicine and athletic clinic", {"Rehab-Therapy": 0.9, "Sports-Ed": 0.5, "Physical-Skill": 0.4}),
      ("Pediatric developmental therapy center", {"Rehab-Therapy": 0.9, "Patient-Care": 0.5, "Teaching-Ed": 0.3}),
      ("Community-based rehabilitation program", {"Rehab-Therapy": 0.9, "Community-Serve": 0.5, "Social-Work": 0.3}),
      ("Private physical therapy clinic", {"Rehab-Therapy": 1.0, "Startup-Venture": 0.4, "Patient-Care": 0.3}),
      ("Home health rehabilitation services", {"Rehab-Therapy": 0.9, "Patient-Care": 0.5, "People-Skill": 0.4})]),
    ("What rehabilitation outcome is most rewarding to you?",
     {"Rehab-Therapy": 0.9, "Patient-Care": 0.3},
     [("Patient walking again after surgery", {"Rehab-Therapy": 1.0, "Patient-Care": 0.5, "Physical-Skill": 0.3}),
      ("Athlete returning to competitive play", {"Rehab-Therapy": 0.9, "Sports-Ed": 0.5, "Physical-Skill": 0.4}),
      ("Child reaching developmental milestones", {"Rehab-Therapy": 1.0, "Teaching-Ed": 0.4, "Patient-Care": 0.4}),
      ("Elderly patient regaining daily independence", {"Rehab-Therapy": 0.9, "Patient-Care": 0.5, "Counseling": 0.3}),
      ("Worker returning safely to their job", {"Rehab-Therapy": 0.9, "Industrial-Ops": 0.4, "People-Skill": 0.3}),
      ("Speech patient communicating clearly again", {"Rehab-Therapy": 0.9, "Patient-Care": 0.5, "People-Skill": 0.4})]),
    ("Which rehabilitation assessment skill would you master first?",
     {"Rehab-Therapy": 0.9, "Analytical-Skill": 0.3},
     [("Range of motion and flexibility testing", {"Rehab-Therapy": 1.0, "Physical-Skill": 0.5, "Analytical-Skill": 0.3}),
      ("Muscle strength grading and evaluation", {"Rehab-Therapy": 1.0, "Physical-Skill": 0.5, "Patient-Care": 0.3}),
      ("Gait analysis and walking pattern assessment", {"Rehab-Therapy": 0.9, "Analytical-Skill": 0.5, "Technical-Skill": 0.3}),
      ("Pain assessment and management planning", {"Rehab-Therapy": 0.9, "Patient-Care": 0.5, "Counseling": 0.3}),
      ("Functional capacity evaluation for work", {"Rehab-Therapy": 0.9, "Analytical-Skill": 0.5, "Industrial-Ops": 0.3}),
      ("Balance and coordination testing", {"Rehab-Therapy": 1.0, "Physical-Skill": 0.5, "Sports-Ed": 0.3})]),
    ("What aspect of rehabilitation science excites you?",
     {"Rehab-Therapy": 0.9, "Lab-Research": 0.3},
     [("Exercise physiology and tissue healing", {"Rehab-Therapy": 0.9, "Lab-Research": 0.5, "Physical-Skill": 0.4}),
      ("Biomechanics of human movement", {"Rehab-Therapy": 0.9, "Mechanical-Design": 0.4, "Analytical-Skill": 0.4}),
      ("Neuroplasticity and brain recovery", {"Rehab-Therapy": 1.0, "Lab-Research": 0.5, "Patient-Care": 0.3}),
      ("Ergonomics and injury prevention design", {"Rehab-Therapy": 0.8, "Industrial-Ops": 0.5, "Spatial-Design": 0.3}),
      ("Prosthetic and orthotic technology advances", {"Rehab-Therapy": 0.9, "Mechanical-Design": 0.5, "Technical-Skill": 0.4}),
      ("Pain science and chronic pain management", {"Rehab-Therapy": 1.0, "Patient-Care": 0.5, "Counseling": 0.3})]),
    ("Which rehabilitation team role suits you best?",
     {"Rehab-Therapy": 0.9, "People-Skill": 0.3},
     [("Physical therapist doing hands-on treatment", {"Rehab-Therapy": 1.0, "Physical-Skill": 0.5, "Patient-Care": 0.4}),
      ("Occupational therapist improving daily living", {"Rehab-Therapy": 1.0, "Patient-Care": 0.5, "Creative-Skill": 0.3}),
      ("Speech-language pathologist restoring communication", {"Rehab-Therapy": 0.9, "People-Skill": 0.5, "Teaching-Ed": 0.3}),
      ("Rehab program coordinator and scheduler", {"Rehab-Therapy": 0.8, "Admin-Skill": 0.5, "People-Skill": 0.4}),
      ("Rehab research assistant conducting studies", {"Rehab-Therapy": 0.9, "Lab-Research": 0.5, "Data-Analytics": 0.3}),
      ("Rehab equipment specialist and advisor", {"Rehab-Therapy": 0.9, "Technical-Skill": 0.5, "Mechanical-Design": 0.3})]),
]:
    HEALTHCARE_QUESTIONS.append(nq(text, 1.5, qtags, opts))

# ===== COUNSELING (currently 9 on-topic, need ~16 more) =====
for text, qtags, opts in [
    ("What type of counseling practice appeals to you most?",
     {"Counseling": 0.9},
     [("Individual therapy for anxiety and depression", {"Counseling": 1.0, "Patient-Care": 0.4, "Analytical-Skill": 0.3}),
      ("Marriage and family relationship counseling", {"Counseling": 1.0, "People-Skill": 0.5, "Social-Work": 0.3}),
      ("School guidance and student career advising", {"Counseling": 0.9, "Teaching-Ed": 0.5, "People-Skill": 0.4}),
      ("Substance abuse and addiction recovery", {"Counseling": 0.9, "Patient-Care": 0.5, "Community-Serve": 0.3}),
      ("Trauma and crisis intervention", {"Counseling": 1.0, "People-Skill": 0.4, "Social-Work": 0.4}),
      ("Workplace employee assistance programs", {"Counseling": 0.9, "HR-Management": 0.5, "People-Skill": 0.3})]),
    ("Which counseling approach resonates with you?",
     {"Counseling": 0.9, "Analytical-Skill": 0.3},
     [("Cognitive-behavioral therapy (CBT) techniques", {"Counseling": 1.0, "Analytical-Skill": 0.5, "Patient-Care": 0.3}),
      ("Person-centered humanistic approach", {"Counseling": 0.9, "People-Skill": 0.5, "Patient-Care": 0.4}),
      ("Play therapy for children and adolescents", {"Counseling": 0.9, "Creative-Skill": 0.5, "Teaching-Ed": 0.3}),
      ("Group therapy and support facilitation", {"Counseling": 1.0, "People-Skill": 0.5, "Community-Serve": 0.3}),
      ("Art and music therapy integration", {"Counseling": 0.9, "Performing-Arts": 0.5, "Creative-Skill": 0.4}),
      ("Solution-focused brief counseling", {"Counseling": 0.9, "Analytical-Skill": 0.5, "People-Skill": 0.3})]),
    ("What counseling population would you focus on?",
     {"Counseling": 0.9, "People-Skill": 0.3},
     [("Children and adolescents in schools", {"Counseling": 1.0, "Teaching-Ed": 0.5, "People-Skill": 0.3}),
      ("College students navigating transitions", {"Counseling": 0.9, "Teaching-Ed": 0.4, "People-Skill": 0.4}),
      ("Adults facing workplace stress and burnout", {"Counseling": 0.9, "HR-Management": 0.4, "People-Skill": 0.4}),
      ("Families in conflict or crisis situations", {"Counseling": 1.0, "Social-Work": 0.5, "People-Skill": 0.4}),
      ("Disaster survivors and trauma victims", {"Counseling": 0.9, "Social-Work": 0.5, "Community-Serve": 0.3}),
      ("Senior citizens coping with loss or isolation", {"Counseling": 0.9, "Patient-Care": 0.4, "People-Skill": 0.4})]),
    ("Which mental health assessment tool would you want to learn?",
     {"Counseling": 0.9, "Analytical-Skill": 0.3},
     [("Standardized psychological testing instruments", {"Counseling": 1.0, "Analytical-Skill": 0.5, "Data-Analytics": 0.3}),
      ("Clinical interview and intake assessment", {"Counseling": 0.9, "People-Skill": 0.5, "Patient-Care": 0.4}),
      ("Behavioral observation and rating scales", {"Counseling": 0.9, "Analytical-Skill": 0.5, "Teaching-Ed": 0.3}),
      ("Personality and career interest inventories", {"Counseling": 1.0, "Analytical-Skill": 0.5, "People-Skill": 0.3}),
      ("Risk and suicide assessment protocols", {"Counseling": 1.0, "Patient-Care": 0.5, "People-Skill": 0.3}),
      ("Child developmental screening tools", {"Counseling": 0.9, "Patient-Care": 0.5, "Teaching-Ed": 0.3})]),
    ("Where would you most want to practice counseling?",
     {"Counseling": 0.9},
     [("School or university guidance office", {"Counseling": 1.0, "Teaching-Ed": 0.5, "People-Skill": 0.3}),
      ("Hospital psychiatric or behavioral health unit", {"Counseling": 0.9, "Patient-Care": 0.5, "Medical-Lab": 0.2}),
      ("Community mental health center", {"Counseling": 0.9, "Community-Serve": 0.5, "Social-Work": 0.3}),
      ("Private counseling or therapy practice", {"Counseling": 1.0, "Startup-Venture": 0.4, "People-Skill": 0.3}),
      ("Rehabilitation or addiction recovery center", {"Counseling": 0.9, "Rehab-Therapy": 0.5, "Patient-Care": 0.3}),
      ("Corporate wellness and EAP provider", {"Counseling": 0.9, "HR-Management": 0.5, "Admin-Skill": 0.3})]),
    ("What counseling skill do you most want to develop?",
     {"Counseling": 0.9, "People-Skill": 0.4},
     [("Active listening and reflective questioning", {"Counseling": 1.0, "People-Skill": 0.6, "Analytical-Skill": 0.3}),
      ("Crisis de-escalation techniques", {"Counseling": 1.0, "People-Skill": 0.5, "Patient-Care": 0.3}),
      ("Cultural sensitivity and diversity competence", {"Counseling": 0.9, "People-Skill": 0.5, "Community-Serve": 0.3}),
      ("Psychometric test administration", {"Counseling": 0.9, "Analytical-Skill": 0.5, "Data-Analytics": 0.3}),
      ("Case documentation and treatment planning", {"Counseling": 0.9, "Admin-Skill": 0.5, "Analytical-Skill": 0.3}),
      ("Referral networking with other professionals", {"Counseling": 0.8, "People-Skill": 0.5, "Health-Admin": 0.4})]),
]:
    HEALTHCARE_QUESTIONS.append(nq(text, 1.5, qtags, opts))

# ===== HEALTH-ADMIN (currently 8 on-topic, need ~17 more) =====
for text, qtags, opts in [
    ("Which healthcare administration function interests you most?",
     {"Health-Admin": 0.9},
     [("Hospital operations and department management", {"Health-Admin": 1.0, "Admin-Skill": 0.5, "Industrial-Ops": 0.3}),
      ("Healthcare budget and financial planning", {"Health-Admin": 0.9, "Finance-Acct": 0.6, "Analytical-Skill": 0.3}),
      ("Patient records and health information systems", {"Health-Admin": 0.9, "Data-Analytics": 0.5, "Technical-Skill": 0.3}),
      ("Healthcare quality accreditation standards", {"Health-Admin": 0.9, "Analytical-Skill": 0.5, "Legal-Practice": 0.3}),
      ("Human resources and medical staff recruitment", {"Health-Admin": 0.9, "HR-Management": 0.6, "People-Skill": 0.3}),
      ("Healthcare policy and regulatory compliance", {"Health-Admin": 1.0, "Legal-Practice": 0.4, "Admin-Skill": 0.3})]),
    ("What type of healthcare facility would you manage?",
     {"Health-Admin": 0.9},
     [("Large tertiary hospital", {"Health-Admin": 1.0, "Admin-Skill": 0.5, "People-Skill": 0.3}),
      ("Community health center or rural clinic", {"Health-Admin": 0.9, "Community-Serve": 0.5, "Public-Health": 0.3}),
      ("Specialty outpatient surgical center", {"Health-Admin": 0.9, "Patient-Care": 0.4, "Finance-Acct": 0.3}),
      ("Long-term care or nursing facility", {"Health-Admin": 0.9, "Patient-Care": 0.5, "People-Skill": 0.3}),
      ("Health maintenance organization (HMO)", {"Health-Admin": 1.0, "Finance-Acct": 0.5, "Admin-Skill": 0.3}),
      ("Rehabilitation and wellness center", {"Health-Admin": 0.9, "Rehab-Therapy": 0.4, "Admin-Skill": 0.4})]),
    ("What healthcare quality metric would you prioritize?",
     {"Health-Admin": 0.9, "Analytical-Skill": 0.3},
     [("Patient satisfaction and experience scores", {"Health-Admin": 1.0, "People-Skill": 0.5, "Data-Analytics": 0.3}),
      ("Clinical outcome and recovery rate tracking", {"Health-Admin": 0.9, "Data-Analytics": 0.5, "Patient-Care": 0.3}),
      ("Wait time reduction and scheduling efficiency", {"Health-Admin": 0.9, "Industrial-Ops": 0.5, "Analytical-Skill": 0.3}),
      ("Infection prevention and control rates", {"Health-Admin": 0.9, "Public-Health": 0.5, "Medical-Lab": 0.3}),
      ("Staff competency and continuing education", {"Health-Admin": 0.9, "Teaching-Ed": 0.4, "HR-Management": 0.4}),
      ("Billing accuracy and insurance claim processing", {"Health-Admin": 0.9, "Finance-Acct": 0.5, "Admin-Skill": 0.3})]),
    ("Which healthcare information system challenge interests you?",
     {"Health-Admin": 0.9, "Technical-Skill": 0.3},
     [("Electronic medical records implementation", {"Health-Admin": 1.0, "Software-Dev": 0.4, "Data-Analytics": 0.3}),
      ("Patient data privacy and security", {"Health-Admin": 0.9, "Cyber-Defense": 0.5, "Legal-Practice": 0.3}),
      ("Telemedicine platform management", {"Health-Admin": 0.9, "Software-Dev": 0.4, "Technical-Skill": 0.4}),
      ("Health analytics and reporting dashboards", {"Health-Admin": 0.9, "Data-Analytics": 0.6, "Software-Dev": 0.3}),
      ("Insurance and PhilHealth claims integration", {"Health-Admin": 0.9, "Finance-Acct": 0.5, "Admin-Skill": 0.3}),
      ("Hospital supply chain management system", {"Health-Admin": 1.0, "Industrial-Ops": 0.5, "Admin-Skill": 0.3})]),
    ("What healthcare leadership challenge would you tackle?",
     {"Health-Admin": 0.9, "People-Skill": 0.3},
     [("Retaining skilled healthcare workers", {"Health-Admin": 1.0, "HR-Management": 0.5, "People-Skill": 0.4}),
      ("Expanding PhilHealth coverage and access", {"Health-Admin": 0.9, "Public-Health": 0.5, "Legal-Practice": 0.3}),
      ("Managing hospital during disaster response", {"Health-Admin": 0.9, "People-Skill": 0.5, "Industrial-Ops": 0.3}),
      ("Improving rural healthcare delivery", {"Health-Admin": 0.9, "Community-Serve": 0.5, "Public-Health": 0.3}),
      ("Balancing budget while improving patient care", {"Health-Admin": 1.0, "Finance-Acct": 0.5, "Analytical-Skill": 0.3}),
      ("Building partnerships with medical schools", {"Health-Admin": 0.9, "Teaching-Ed": 0.4, "People-Skill": 0.4})]),
    ("Which PhilHealth or HMO administrative area interests you?",
     {"Health-Admin": 0.9, "Finance-Acct": 0.3},
     [("Claims processing and benefit management", {"Health-Admin": 1.0, "Finance-Acct": 0.5, "Admin-Skill": 0.4}),
      ("Provider network and hospital accreditation", {"Health-Admin": 0.9, "Analytical-Skill": 0.5, "Legal-Practice": 0.3}),
      ("Member enrollment and outreach", {"Health-Admin": 0.9, "Marketing-Sales": 0.4, "People-Skill": 0.4}),
      ("Fraud detection and compliance auditing", {"Health-Admin": 0.9, "Law-Enforce": 0.4, "Analytical-Skill": 0.4}),
      ("Cost analysis and rate setting", {"Health-Admin": 0.9, "Finance-Acct": 0.6, "Data-Analytics": 0.3}),
      ("Policy development and program design", {"Health-Admin": 1.0, "Legal-Practice": 0.4, "Admin-Skill": 0.3})]),
]:
    HEALTHCARE_QUESTIONS.append(nq(text, 1.5, qtags, opts))

# ===== PHARMACY (currently 13 on-topic, need ~12 more) =====
for text, qtags, opts in [
    ("Which pharmacy practice area excites you most?",
     {"Pharmacy": 0.9},
     [("Community pharmacy patient consultations", {"Pharmacy": 1.0, "People-Skill": 0.5, "Patient-Care": 0.3}),
      ("Hospital clinical pharmacy rounds", {"Pharmacy": 0.9, "Patient-Care": 0.5, "Medical-Lab": 0.3}),
      ("Pharmaceutical manufacturing quality control", {"Pharmacy": 0.9, "Industrial-Ops": 0.5, "Lab-Research": 0.3}),
      ("Drug research and formulation development", {"Pharmacy": 0.9, "Lab-Research": 0.6, "Food-Science": 0.3}),
      ("Regulatory affairs and drug approval process", {"Pharmacy": 0.9, "Legal-Practice": 0.5, "Admin-Skill": 0.3}),
      ("Herbal and traditional medicine analysis", {"Pharmacy": 0.8, "Lab-Research": 0.5, "Agri-Nature": 0.4})]),
    ("What pharmaceutical science topic fascinates you?",
     {"Pharmacy": 0.9, "Lab-Research": 0.3},
     [("Pharmacokinetics \u2014 how drugs move in the body", {"Pharmacy": 1.0, "Lab-Research": 0.5, "Analytical-Skill": 0.3}),
      ("Drug interactions and safety monitoring", {"Pharmacy": 1.0, "Patient-Care": 0.4, "Analytical-Skill": 0.3}),
      ("Natural product chemistry from Philippine plants", {"Pharmacy": 0.9, "Lab-Research": 0.5, "Agri-Nature": 0.4}),
      ("Compounding and specialized formulations", {"Pharmacy": 0.9, "Lab-Research": 0.5, "Technical-Skill": 0.3}),
      ("Biopharmaceuticals and vaccine production", {"Pharmacy": 0.9, "Lab-Research": 0.5, "Public-Health": 0.3}),
      ("Toxicology and poison control", {"Pharmacy": 0.9, "Forensic-Sci": 0.5, "Lab-Research": 0.3})]),
    ("What pharmacy counseling scenario appeals to you?",
     {"Pharmacy": 0.9, "People-Skill": 0.3},
     [("Advising patients on proper medication use", {"Pharmacy": 1.0, "Patient-Care": 0.5, "People-Skill": 0.4}),
      ("Explaining drug side effects and precautions", {"Pharmacy": 1.0, "Patient-Care": 0.4, "Counseling": 0.3}),
      ("Helping doctors choose optimal drug therapy", {"Pharmacy": 0.9, "Analytical-Skill": 0.5, "Patient-Care": 0.4}),
      ("Guiding chronic disease medication management", {"Pharmacy": 0.9, "Patient-Care": 0.5, "Counseling": 0.3}),
      ("Counseling on over-the-counter product selection", {"Pharmacy": 1.0, "People-Skill": 0.5, "Marketing-Sales": 0.2}),
      ("Promoting medication adherence for elderly patients", {"Pharmacy": 0.9, "Counseling": 0.5, "Patient-Care": 0.4})]),
    ("Which pharmacy technology interests you?",
     {"Pharmacy": 0.9, "Technical-Skill": 0.3},
     [("Automated dispensing machines and robotics", {"Pharmacy": 0.9, "Technical-Skill": 0.5, "Industrial-Ops": 0.3}),
      ("Pharmacy information management systems", {"Pharmacy": 0.9, "Software-Dev": 0.4, "Admin-Skill": 0.4}),
      ("Drug dissolution and stability testing equipment", {"Pharmacy": 1.0, "Lab-Research": 0.5, "Technical-Skill": 0.3}),
      ("Electronic prescribing and verification", {"Pharmacy": 0.9, "Software-Dev": 0.4, "Cyber-Defense": 0.3}),
      ("Pharmaceutical production line automation", {"Pharmacy": 0.8, "Industrial-Ops": 0.6, "Technical-Skill": 0.4}),
      ("Drug database and interaction checking tools", {"Pharmacy": 1.0, "Data-Analytics": 0.4, "Software-Dev": 0.3})]),
    ("Where would you like to practice pharmacy in the Philippines?",
     {"Pharmacy": 0.9},
     [("Major hospital pharmacy department", {"Pharmacy": 1.0, "Patient-Care": 0.4, "Health-Admin": 0.3}),
      ("Community drugstore chain management", {"Pharmacy": 0.9, "Admin-Skill": 0.5, "Marketing-Sales": 0.3}),
      ("Pharmaceutical company R&D lab", {"Pharmacy": 0.9, "Lab-Research": 0.6, "Technical-Skill": 0.3}),
      ("FDA Philippines regulatory office", {"Pharmacy": 0.9, "Legal-Practice": 0.5, "Admin-Skill": 0.3}),
      ("University pharmacy teaching and research", {"Pharmacy": 0.8, "Teaching-Ed": 0.6, "Lab-Research": 0.4}),
      ("Cosmetics and personal care formulation lab", {"Pharmacy": 0.8, "Lab-Research": 0.5, "Creative-Skill": 0.3})]),
]:
    HEALTHCARE_QUESTIONS.append(nq(text, 1.5, qtags, opts))

# QUESTION_TREE_NODES for healthcare questions
HEALTHCARE_TREE = {}
for q in HEALTHCARE_QUESTIONS:
    qid = q["question_id"]
    tags = q["trait_tags"]
    branches = ["healthcare"]
    if any(t in tags for t in ["Community-Serve", "Social-Work"]):
        branches.append("social")
    if any(t in tags for t in ["Lab-Research", "Environmental-Sci"]):
        branches.append("science")
    if any(t in tags for t in ["Data-Analytics", "Software-Dev"]):
        branches.append("technology")
    if any(t in tags for t in ["Teaching-Ed"]):
        branches.append("education")
    HEALTHCARE_TREE[qid] = {"level": 2, "weight": 1.5, "branches": branches}


def main():
    # ─── Guard: check if already applied ───
    with open("questions_enhanced.py", "r", encoding="utf-8") as f:
        qe = f.read()

    first_id = HEALTHCARE_QUESTIONS[0]["question_id"]
    if f'"question_id": {first_id}' in qe:
        print(f"Q{first_id} already exists — skipping insertion.")
    else:
        insert_point = qe.rfind("\n]\n\nTRAIT_SECONDARY_MAP")
        if insert_point == -1:
            print("ERROR: Cannot find insertion point")
            sys.exit(1)

        lines = []
        lines.append("    # ==================== HEALTHCARE DEDICATED QUESTIONS ====================")
        for q in HEALTHCARE_QUESTIONS:
            lines.append("    {")
            lines.append(f'        "question_id": {q["question_id"]},')
            lines.append(f'        "question_text": {repr(q["question_text"])},')
            lines.append(f'        "weight": {q["weight"]},')
            lines.append(f'        "trait_tags": {q["trait_tags"]},')
            lines.append('        "options": [')
            for opt in q["options"]:
                lines.append(f'            {{"option_id": {opt["option_id"]}, "option_text": {repr(opt["option_text"])}, "trait_tags": {opt["trait_tags"]}}},')
            lines.append("        ]")
            lines.append("    },")

        insert_text = "\n" + "\n".join(lines)
        new_content = qe[:insert_point] + insert_text + qe[insert_point:]
        with open("questions_enhanced.py", "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Added {len(HEALTHCARE_QUESTIONS)} healthcare questions (Q{HEALTHCARE_QUESTIONS[0]['question_id']}-Q{HEALTHCARE_QUESTIONS[-1]['question_id']})")

    # ─── Update adaptive_assessment.py ───
    import importlib
    for mod in ["questions_enhanced", "adaptive_assessment"]:
        if mod in sys.modules:
            del sys.modules[mod]

    from questions_enhanced import QUESTIONS_POOL_ENHANCED
    q_lookup = {q["question_id"]: q for q in QUESTIONS_POOL_ENHANCED}
    print(f"Total questions: {len(QUESTIONS_POOL_ENHANCED)}")

    with open("adaptive_assessment.py", "r", encoding="utf-8") as f:
        aa = f.read()

    # Add tree nodes
    new_ids = [q["question_id"] for q in HEALTHCARE_QUESTIONS]
    first_check = f"{new_ids[0]}:"
    if first_check not in aa.split("QUESTION_TREE_NODES")[1][:10000]:
        tree_marker = "QUESTION_TREE_NODES = {"
        tree_start = aa.find(tree_marker)
        brace_depth = 0
        pos = tree_start + len(tree_marker)
        while pos < len(aa):
            if aa[pos] == '{': brace_depth += 1
            elif aa[pos] == '}':
                if brace_depth == 0:
                    insert_lines = []
                    for qid, node in HEALTHCARE_TREE.items():
                        insert_lines.append(f'    {qid}: {{"level": {node["level"]}, "weight": {node["weight"]}, "branches": {node["branches"]}}},')
                    aa = aa[:pos] + "\n" + "\n".join(insert_lines) + "\n" + aa[pos:]
                    print(f"Added {len(HEALTHCARE_TREE)} tree nodes")
                    break
                brace_depth -= 1
            pos += 1
    else:
        print("Healthcare tree nodes already present")

    # Update TRAIT_FOLLOWUP_MAP with new questions + reorder
    tfm_match = re.search(r'TRAIT_FOLLOWUP_MAP\s*=\s*\{', aa)
    tfm_start = tfm_match.start()
    brace_depth = 0
    pos = tfm_match.end()
    while pos < len(aa):
        if aa[pos] == '{': brace_depth += 1
        elif aa[pos] == '}':
            if brace_depth == 0:
                tfm_end = pos + 1
                break
            brace_depth -= 1
        pos += 1

    local_ns = {}
    exec(aa[tfm_start:tfm_end], {}, local_ns)
    tfm = local_ns["TRAIT_FOLLOWUP_MAP"]

    # Add new questions to relevant traits
    for q in HEALTHCARE_QUESTIONS:
        qid = q["question_id"]
        all_traits = set(q["trait_tags"].keys())
        for opt in q["options"]:
            for t in opt.get("trait_tags", {}).keys():
                all_traits.add(t)
        for trait in all_traits:
            if trait in tfm and qid not in tfm[trait]:
                tfm[trait].append(qid)

    # Reorder: on-topic first (by average trait weight across options)
    def score(qid, trait):
        q = q_lookup.get(qid)
        if not q: return 0
        total = sum(o.get("trait_tags", {}).get(trait, 0) for o in q["options"])
        avg = total / max(len(q["options"]), 1)
        tmax = {}
        for o in q["options"]:
            for t, v in o.get("trait_tags", {}).items():
                if t not in tmax or v > tmax[t]: tmax[t] = v
        is_primary = tmax and max(tmax, key=tmax.get) == trait
        return avg + (10.0 if is_primary else 0)

    reordered = {}
    for trait, qids in sorted(tfm.items()):
        scored = [(qid, score(qid, trait)) for qid in qids]
        scored.sort(key=lambda x: -x[1])
        reordered[trait] = [qid for qid, _ in scored]

    # Build and replace
    tfm_lines = ["TRAIT_FOLLOWUP_MAP = {"]
    for trait in sorted(reordered.keys()):
        tfm_lines.append(f'    "{trait}": {reordered[trait]},')
    tfm_lines.append("}")
    aa = aa[:tfm_start] + "\n".join(tfm_lines) + aa[tfm_end:]

    with open("adaptive_assessment.py", "w", encoding="utf-8") as f:
        f.write(aa)
    print("Updated adaptive_assessment.py with healthcare questions + reordered TRAIT_FOLLOWUP_MAP")

    # Quick validation
    for mod in ["questions_enhanced", "adaptive_assessment"]:
        if mod in sys.modules: del sys.modules[mod]
    from adaptive_assessment import TRAIT_FOLLOWUP_MAP
    health_traits = ["Public-Health", "Medical-Lab", "Nutrition-Diet", "Rehab-Therapy",
                     "Counseling", "Health-Admin", "Pharmacy"]
    for t in health_traits:
        on = 0
        for qid in TRAIT_FOLLOWUP_MAP[t][:30]:
            q = q_lookup.get(qid)
            if not q: continue
            tmax = {}
            for o in q["options"]:
                for tr, v in o.get("trait_tags", {}).items():
                    if tr not in tmax or v > tmax[tr]: tmax[tr] = v
            if tmax and max(tmax, key=tmax.get) == t: on += 1
        print(f"  {t}: {on}/30 on-topic")


if __name__ == "__main__":
    main()
