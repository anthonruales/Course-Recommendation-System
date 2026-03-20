"""Add missing options to DB-only questions (Q1002-Q1910) to bring each to 6 options."""
from database import SessionLocal
from models import Option

# New options to add for each question that has < 6
# Format: {question_id: [(option_text, trait_tag), ...]}
NEW_OPTIONS = {
    # TECHNOLOGY DOMAIN
    1002: [  # Software - needs 1 more (has 5)
        ("Cloud and DevOps tools that keep systems running smoothly", "Cloud-Systems"),
    ],
    1003: [  # Hardware - needs 1 more (has 5)
        ("Cybersecurity hardware — firewalls, intrusion detection devices", "Cyber-Defense"),
    ],
    1004: [  # Creative Digital - needs 1 more (has 5)
        ("Digital photography and photo editing for creative campaigns", "Digital-Media"),
    ],
    1005: [  # Data - needs 2 more (has 4)
        ("Clean and organize messy data for better decision-making", "Data-Analytics"),
        ("Use data storytelling to communicate insights to non-technical teams", "Data-Analytics"),
    ],
    1006: [  # Security - needs 2 more (has 4)
        ("Cryptography and secure communications design", "Cyber-Defense"),
        ("Incident response — containing and recovering from breaches", "Cyber-Defense"),
    ],
    1007: [  # Software Depth - needs 1 more (has 5)
        ("Making it accessible and inclusive for all users", "Software-Dev"),
    ],
    1008: [  # Games - needs 2 more (has 4)
        ("Game testing, QA, and player experience research", "Game-Dev"),
        ("Multiplayer networking and online game infrastructure", "Game-Dev"),
    ],
    1009: [  # AI - needs 2 more (has 4)
        ("AI ethics and responsible AI development", "AI-ML"),
        ("Reinforcement learning — training agents through trial and reward", "AI-ML"),
    ],
    1010: [  # (needs 1 more, has 5) — check what this is
        ("Building interactive data-driven web dashboards", "Web-Dev"),
    ],

    # HEALTHCARE DOMAIN
    1102: [  # Patient Care - needs 1 more (has 5)
        ("Geriatric care — supporting elderly patients with compassion", "Patient-Care"),
    ],
    1103: [  # Lab - needs 2 more (has 4)
        ("Clinical chemistry — analyzing body fluids for disease markers", "Medical-Lab"),
        ("Histopathology — examining tissue samples under microscopes", "Medical-Lab"),
    ],
    1104: [  # Therapy - needs 1 more (has 5)
        ("Art or music therapy — using creative expression for healing", "Rehab-Therapy"),
    ],
    1105: [  # Management - needs 2 more (has 4)
        ("Healthcare quality improvement — patient safety and outcomes", "Health-Admin"),
        ("Health economics — analyzing costs and resource allocation", "Health-Admin"),
    ],
    1106: [  # Pharmacy - needs 2 more (has 4)
        ("Regulatory affairs — ensuring drug safety and compliance", "Pharmacy"),
        ("Compounding pharmacy — creating custom medication formulations", "Pharmacy"),
    ],

    # ENGINEERING DOMAIN
    1201: [  # Exploration - needs 1 more (has 5)
        ("Environmental engineering — designing eco-friendly solutions", "Environmental-Eng"),
    ],
    1202: [  # Civil - needs 2 more (has 4)
        ("Construction management — overseeing building projects on-site", "Civil-Build"),
        ("Earthquake and disaster-resistant structural engineering", "Civil-Build"),
    ],
    1203: [  # Mechanical - needs 2 more (has 4)
        ("Robotics and mechatronics — combining mechanics with electronics", "Mechanical-Design"),
        ("Marine engineering — ship engines, propulsion, and hull design", "Mechanical-Design"),
    ],
    1204: [  # Electrical - needs 2 more (has 4)
        ("Renewable energy — solar, wind, and sustainable power systems", "Electrical-Power"),
        ("Biomedical electronics — medical devices and diagnostic equipment", "Electrical-Power"),
    ],
    1205: [  # Industrial - needs 2 more (has 4)
        ("Ergonomics and workplace design — making work safer and efficient", "Industrial-Ops"),
        ("Lean manufacturing and Six Sigma process improvement", "Industrial-Ops"),
    ],
    1206: [  # Spatial - needs 2 more (has 4)
        ("Sustainable and green building design", "Spatial-Design"),
        ("Heritage conservation — restoring historical buildings and sites", "Spatial-Design"),
    ],

    # BUSINESS DOMAIN
    1301: [  # Exploration - needs 1 more (has 5)
        ("International business and global trade", "Marketing-Sales"),
    ],
    1302: [  # Finance - needs 2 more (has 4)
        ("Insurance and risk management — protecting assets and businesses", "Finance-Acct"),
        ("Tax consulting and compliance — navigating tax laws for clients", "Finance-Acct"),
    ],
    1303: [  # Marketing - needs 2 more (has 4)
        ("Public relations — managing company image and media", "Marketing-Sales"),
        ("Event marketing and experiential campaigns", "Marketing-Sales"),
    ],
    1304: [  # Entrepreneurship - needs 2 more (has 4)
        ("Tech startup — building an app or platform that disrupts an industry", "Startup-Venture"),
        ("E-commerce — selling products and services online", "Startup-Venture"),
    ],
    1305: [  # Management - needs 2 more (has 4)
        ("Strategic planning and business consulting", "Admin-Skill"),
        ("Customer service management — ensuring client satisfaction", "Admin-Skill"),
    ],

    # ARTS DOMAIN
    1401: [  # Exploration - needs 1 more (has 5)
        ("Creative writing and publishing — books, scripts, and poetry", "Creative-Skill"),
    ],
    1402: [  # Visual - needs 1 more (has 5)
        ("Industrial design — creating functional and aesthetic product prototypes", "Visual-Design"),
    ],
    1403: [  # Digital - needs 1 more (has 5)
        ("Web design and interactive digital storytelling", "Web-Dev"),
    ],
    1404: [  # Performing - needs 2 more (has 4)
        ("Comedy, improv, and stand-up performance", "Performing-Arts"),
        ("Live event production — concerts, festivals, and shows", "Performing-Arts"),
    ],
    1405: [  # Spatial - needs 2 more (has 4)
        ("Theme park and attraction design — immersive environments", "Spatial-Design"),
        ("Retail and commercial space design — stores and malls", "Spatial-Design"),
    ],

    # EDUCATION DOMAIN
    1501: [  # Exploration - needs 1 more (has 5)
        ("Educational technology — creating digital tools for learning", "Teaching-Ed"),
    ],
    1502: [  # Age Group - needs 3 more (has 3)
        ("Middle school (ages 13-15)", "Teaching-Ed"),
        ("High school (ages 16-18)", "Teaching-Ed"),
        ("College/university students (ages 18+)", "Teaching-Ed"),
    ],
    1503: [  # Subject - needs 1 more (has 5)
        ("Arts and Music Education", "Teaching-Ed"),
    ],

    # SCIENCE DOMAIN
    1601: [  # Exploration - needs 2 more (has 4)
        ("Space science and astronomy — planets, stars, and the cosmos", "Lab-Research"),
        ("Biomedical research — developing cures and medical breakthroughs", "Lab-Research"),
    ],
    1602: [  # Lab - needs 2 more (has 4)
        ("Pharmacology — studying drug effects on the body", "Lab-Research"),
        ("Clinical pathology — diagnosing diseases through lab tests", "Lab-Research"),
    ],
    1603: [  # Field - needs 2 more (has 4)
        ("Wildlife biology and animal behavior studies", "Field-Research"),
        ("Volcanology and natural hazard assessment", "Field-Research"),
    ],
    1604: [  # Applied - needs 2 more (has 4)
        ("Nanotechnology — engineering at the atomic scale", "Lab-Research"),
        ("Agricultural science and crop improvement technology", "Agri-Nature"),
    ],

    # PUBLIC SERVICE DOMAIN
    1701: [  # Exploration - needs 1 more (has 5)
        ("Disaster management and emergency response coordination", "Community-Serve"),
    ],
    1702: [  # Law - needs 2 more (has 4)
        ("Traffic management and road safety enforcement", "Law-Enforce"),
        ("Drug enforcement and narcotics investigation", "Law-Enforce"),
    ],
    1703: [  # Community - needs 2 more (has 4)
        ("Youth development and mentorship programs", "Community-Serve"),
        ("Disaster relief and humanitarian aid coordination", "Community-Serve"),
    ],

    # MARITIME DOMAIN
    1801: [  # Exploration - needs 2 more (has 4)
        ("Maritime safety and coast guard operations", "Maritime-Sea"),
        ("Marine biology and ocean conservation research", "Maritime-Sea"),
    ],

    # AGRICULTURE DOMAIN
    1802: [  # Exploration - needs 1 more (has 5)
        ("Agricultural technology and precision farming innovations", "Agri-Nature"),
    ],

    # HOSPITALITY DOMAIN
    1803: [  # Exploration - needs 2 more (has 4)
        ("Food and beverage management — restaurants and catering services", "Hospitality-Svc"),
        ("Resort and spa management — wellness and leisure operations", "Hospitality-Svc"),
    ],

    # VALIDATION QUESTIONS
    1902: [  # Problem Solving - needs 1 more (has 5)
        ("Follow established procedures and proven methods", "Conventional"),
    ],
    1903: [  # Motivation - needs 1 more (has 5)
        ("Leading teams and managing important projects", "Enterprising"),
    ],
    1905: [  # Teamwork - needs 2 more (has 4)
        ("Mentor and guide less experienced team members", "Teaching-Ed"),
        ("Bridge between different teams as a liaison or coordinator", "People-Skill"),
    ],
    1908: [  # Coping - needs 2 more (has 4)
        ("Organizing and making detailed plans to feel in control", "Conventional"),
        ("Seeking mentorship or professional guidance", "Teaching-Ed"),
    ],
    1910: [  # Values - needs 1 more (has 5)
        ("Creativity and freedom to express ideas in my work", "Creative-Skill"),
    ],
}


def main():
    db = SessionLocal()
    
    next_id = 20501  # Start after previous batch (20001-20314)
    added = 0
    
    for qid, options in NEW_OPTIONS.items():
        for opt_text, trait_tag in options:
            new_opt = Option(
                option_id=next_id,
                question_id=qid,
                option_text=opt_text,
                trait_tag=trait_tag
            )
            db.add(new_opt)
            next_id += 1
            added += 1
    
    db.commit()
    print(f"Added {added} options (IDs {20501}-{next_id-1})")
    
    # Verify all questions now have >= 6 options (except Q194-Q197 scale questions)
    from models import Question
    still_low = []
    for q in db.query(Question).all():
        n = db.query(Option).filter(Option.question_id == q.question_id).count()
        if n < 6 and q.question_id not in (194, 195, 196, 197):
            still_low.append((q.question_id, n))
    
    if still_low:
        print(f"Still under 6 options: {still_low}")
    else:
        print("All questions (except scale Q194-197) now have 6+ options!")
    
    db.close()


if __name__ == "__main__":
    main()
