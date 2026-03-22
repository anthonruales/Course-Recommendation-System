"""
Generate multi-trait enrichments for DB-only questions that are NOT in 
QUESTIONS_POOL_ENHANCED. Each option gets contextually relevant secondary 
traits based on its primary trait and domain.

Rules:
- Every option gets 4-6 traits total (1 primary at 1.0 + 3-5 secondaries)
- Secondary traits must be domain-relevant (same domain or universal)
- No cross-domain contamination
"""

# Domain-specific secondary trait mappings
# For each primary trait, define which secondary traits are contextually appropriate
# Only include traits from the same domain or universal (Holland/skill) traits
CURATED_SECONDARIES = {
    # === HEALTHCARE ===
    "Patient-Care": [
        ("People-Skill", 0.45), ("Social", 0.4), ("Rehab-Therapy", 0.3),
        ("Community-Serve", 0.25), ("Medical-Lab", 0.2)
    ],
    "Medical-Lab": [
        ("Analytical-Skill", 0.45), ("Investigative", 0.4), ("Lab-Research", 0.35),
        ("Patient-Care", 0.2), ("Technical-Skill", 0.2)
    ],
    "Rehab-Therapy": [
        ("Physical-Skill", 0.4), ("Social", 0.35), ("People-Skill", 0.35),
        ("Patient-Care", 0.3), ("Teaching-Ed", 0.2)
    ],
    "Health-Admin": [
        ("Admin-Skill", 0.45), ("Conventional", 0.35), ("People-Skill", 0.3),
        ("Patient-Care", 0.2), ("Data-Analytics", 0.15)
    ],
    "Pharmacy": [
        ("Medical-Lab", 0.45), ("Analytical-Skill", 0.4), ("Lab-Research", 0.35),
        ("Patient-Care", 0.25), ("Investigative", 0.2)
    ],
    "Nutrition-Diet": [
        ("Patient-Care", 0.45), ("People-Skill", 0.36), ("Food-Science", 0.35),
        ("Social", 0.32), ("Analytical-Skill", 0.3)
    ],
    "Public-Health": [
        ("Community-Serve", 0.45), ("Social", 0.4), ("People-Skill", 0.35),
        ("Patient-Care", 0.25), ("Teaching-Ed", 0.2)
    ],

    # === TECHNOLOGY ===
    "Software-Dev": [
        ("Technical-Skill", 0.45), ("Investigative", 0.4), ("Data-Analytics", 0.3),
        ("Cyber-Defense", 0.25), ("Analytical-Skill", 0.2)
    ],
    "Web-Dev": [
        ("Software-Dev", 0.45), ("Technical-Skill", 0.4), ("Digital-Media", 0.3),
        ("Creative-Skill", 0.2), ("Investigative", 0.15)
    ],
    "Mobile-Dev": [
        ("Software-Dev", 0.45), ("Technical-Skill", 0.4), ("Investigative", 0.3),
        ("Data-Analytics", 0.25), ("Creative-Skill", 0.2)
    ],
    "Game-Dev": [
        ("Software-Dev", 0.4), ("Creative-Skill", 0.35), ("Animation-3D", 0.35),
        ("Technical-Skill", 0.3), ("Digital-Media", 0.25)
    ],
    "AI-ML": [
        ("Software-Dev", 0.45), ("Investigative", 0.4), ("Analytical-Skill", 0.4),
        ("Data-Analytics", 0.35), ("Technical-Skill", 0.3)
    ],
    "Data-Analytics": [
        ("Investigative", 0.45), ("Analytical-Skill", 0.45), ("Software-Dev", 0.3),
        ("Technical-Skill", 0.25), ("Conventional", 0.2)
    ],
    "Cloud-Systems": [
        ("Technical-Skill", 0.45), ("Software-Dev", 0.35), ("Cyber-Defense", 0.3),
        ("Hardware-Systems", 0.25), ("Investigative", 0.2)
    ],
    "Cyber-Defense": [
        ("Technical-Skill", 0.45), ("Investigative", 0.4), ("Software-Dev", 0.3),
        ("Analytical-Skill", 0.25), ("Hardware-Systems", 0.2)
    ],
    "Hardware-Systems": [
        ("Technical-Skill", 0.45), ("Realistic", 0.4), ("Electrical-Power", 0.3),
        ("Software-Dev", 0.2), ("Investigative", 0.15)
    ],
    "Electronics-Dev": [
        ("Hardware-Systems", 0.45), ("Technical-Skill", 0.4), ("Realistic", 0.35),
        ("Electrical-Power", 0.3), ("Investigative", 0.2)
    ],
    "Digital-Media": [
        ("Creative-Skill", 0.45), ("Artistic", 0.4), ("Visual-Design", 0.3),
        ("Software-Dev", 0.2), ("Technical-Skill", 0.15)
    ],

    # === ENGINEERING ===
    "Mechanical-Design": [
        ("Realistic", 0.45), ("Technical-Skill", 0.4), ("Industrial-Ops", 0.3),
        ("Analytical-Skill", 0.25), ("Investigative", 0.2)
    ],
    "Civil-Build": [
        ("Realistic", 0.45), ("Technical-Skill", 0.4), ("Spatial-Design", 0.25),
        ("Mechanical-Design", 0.2), ("Analytical-Skill", 0.15)
    ],
    "Industrial-Ops": [
        ("Analytical-Skill", 0.45), ("Realistic", 0.35), ("Technical-Skill", 0.3),
        ("Mechanical-Design", 0.25), ("Enterprising", 0.2)
    ],
    "Electrical-Power": [
        ("Technical-Skill", 0.45), ("Realistic", 0.4), ("Hardware-Systems", 0.3),
        ("Mechanical-Design", 0.2), ("Analytical-Skill", 0.15)
    ],
    "Aeronautical-Eng": [
        ("Mechanical-Design", 0.45), ("Realistic", 0.36), ("Technical-Skill", 0.32),
        ("Investigative", 0.25), ("Industrial-Ops", 0.2)
    ],
    "Spatial-Design": [
        ("Artistic", 0.45), ("Creative-Skill", 0.4), ("Visual-Design", 0.3),
        ("Civil-Build", 0.25), ("Realistic", 0.2)
    ],

    # === BUSINESS ===
    "Finance-Acct": [
        ("Conventional", 0.45), ("Analytical-Skill", 0.4), ("Admin-Skill", 0.3),
        ("Investigative", 0.25), ("Data-Analytics", 0.2)
    ],
    "Marketing-Sales": [
        ("Enterprising", 0.45), ("People-Skill", 0.4), ("Creative-Skill", 0.3),
        ("Startup-Venture", 0.25), ("Social", 0.2)
    ],
    "Startup-Venture": [
        ("Enterprising", 0.45), ("People-Skill", 0.3), ("Marketing-Sales", 0.3),
        ("Finance-Acct", 0.2), ("Creative-Skill", 0.2)
    ],
    "Admin-Skill": [
        ("Conventional", 0.45), ("People-Skill", 0.35), ("Enterprising", 0.3),
        ("Finance-Acct", 0.2), ("Data-Analytics", 0.15)
    ],
    "HR-Management": [
        ("People-Skill", 0.45), ("Social", 0.4), ("Admin-Skill", 0.35),
        ("Enterprising", 0.25), ("Teaching-Ed", 0.2)
    ],

    # === EDUCATION ===
    "Teaching-Ed": [
        ("Social", 0.45), ("People-Skill", 0.45), ("Community-Serve", 0.25),
        ("Patient-Care", 0.15), ("Rehab-Therapy", 0.15)
    ],
    "Counseling": [
        ("People-Skill", 0.45), ("Social", 0.4), ("Community-Serve", 0.3),
        ("Teaching-Ed", 0.25), ("Rehab-Therapy", 0.2)
    ],

    # === ARTS ===
    "Visual-Design": [
        ("Artistic", 0.45), ("Creative-Skill", 0.45), ("Digital-Media", 0.3),
        ("Spatial-Design", 0.25), ("Investigative", 0.15)
    ],
    "Artistic": [
        ("Visual-Design", 0.45), ("Creative-Skill", 0.45), ("Spatial-Design", 0.3),
        ("Digital-Media", 0.2), ("Performing-Arts", 0.15)
    ],
    "Performing-Arts": [
        ("Creative-Skill", 0.45), ("Artistic", 0.4), ("People-Skill", 0.35),
        ("Social", 0.25), ("Film-Broadcast", 0.2)
    ],
    "Animation-3D": [
        ("Digital-Media", 0.45), ("Creative-Skill", 0.4), ("Software-Dev", 0.3),
        ("Artistic", 0.25), ("Visual-Design", 0.2)
    ],
    "Film-Broadcast": [
        ("Digital-Media", 0.45), ("Creative-Skill", 0.4), ("Artistic", 0.3),
        ("Visual-Design", 0.25), ("People-Skill", 0.2)
    ],
    "Creative-Skill": [
        ("Artistic", 0.45), ("Visual-Design", 0.35), ("Performing-Arts", 0.3),
        ("Digital-Media", 0.25), ("Social", 0.2)
    ],

    # === PUBLIC SERVICE ===
    "Law-Enforce": [
        ("Realistic", 0.35), ("Physical-Skill", 0.35), ("Investigative", 0.3),
        ("Community-Serve", 0.2), ("People-Skill", 0.15)
    ],
    "Legal-Practice": [
        ("Analytical-Skill", 0.45), ("Investigative", 0.4), ("People-Skill", 0.3),
        ("Admin-Skill", 0.25), ("Conventional", 0.2)
    ],
    "Forensic-Sci": [
        ("Lab-Research", 0.45), ("Investigative", 0.45), ("Analytical-Skill", 0.35),
        ("Law-Enforce", 0.25), ("Medical-Lab", 0.2)
    ],
    "Community-Serve": [
        ("Social", 0.45), ("People-Skill", 0.4), ("Teaching-Ed", 0.25),
        ("Enterprising", 0.2), ("Law-Enforce", 0.15)
    ],
    "Social-Work": [
        ("Social", 0.45), ("People-Skill", 0.45), ("Community-Serve", 0.35),
        ("Counseling", 0.25), ("Teaching-Ed", 0.2)
    ],

    # === MARITIME ===
    "Maritime-Sea": [
        ("Realistic", 0.45), ("Physical-Skill", 0.4), ("Technical-Skill", 0.25),
        ("Mechanical-Design", 0.15), ("Investigative", 0.1)
    ],

    # === AGRICULTURE ===
    "Agri-Nature": [
        ("Realistic", 0.45), ("Physical-Skill", 0.35), ("Field-Research", 0.25),
        ("Environmental-Sci", 0.2), ("Investigative", 0.15)
    ],
    "Environmental-Sci": [
        ("Field-Research", 0.45), ("Investigative", 0.4), ("Agri-Nature", 0.3),
        ("Lab-Research", 0.25), ("Analytical-Skill", 0.2)
    ],
    "Environmental-Eng": [
        ("Field-Research", 0.45), ("Investigative", 0.35), ("Civil-Build", 0.3),
        ("Technical-Skill", 0.25), ("Agri-Nature", 0.2)
    ],

    # === HOSPITALITY ===
    "Hospitality-Svc": [
        ("People-Skill", 0.45), ("Tourism-Travel", 0.4), ("Enterprising", 0.35),
        ("Culinary-Arts", 0.3), ("Social", 0.2)
    ],
    "Tourism-Travel": [
        ("Hospitality-Svc", 0.45), ("People-Skill", 0.4), ("Enterprising", 0.3),
        ("Social", 0.25), ("Creative-Skill", 0.2)
    ],
    "Culinary-Arts": [
        ("Hospitality-Svc", 0.45), ("Creative-Skill", 0.35), ("Artistic", 0.3),
        ("People-Skill", 0.2), ("Realistic", 0.15)
    ],

    # === SCIENCE ===
    "Lab-Research": [
        ("Investigative", 0.45), ("Analytical-Skill", 0.45), ("Medical-Lab", 0.3),
        ("Field-Research", 0.25), ("Technical-Skill", 0.2)
    ],
    "Field-Research": [
        ("Investigative", 0.4), ("Realistic", 0.35), ("Analytical-Skill", 0.3),
        ("Physical-Skill", 0.25), ("Lab-Research", 0.2)
    ],
    "Food-Science": [
        ("Lab-Research", 0.45), ("Analytical-Skill", 0.4), ("Investigative", 0.35),
        ("Nutrition-Diet", 0.25), ("Culinary-Arts", 0.2)
    ],

    # === UNIVERSAL/Holland codes as primary (unlikely but just in case) ===
    "Realistic": [
        ("Physical-Skill", 0.4), ("Technical-Skill", 0.35), ("Investigative", 0.2),
        ("Mechanical-Design", 0.15), ("Civil-Build", 0.1)
    ],
    "Investigative": [
        ("Analytical-Skill", 0.45), ("Lab-Research", 0.35), ("Data-Analytics", 0.3),
        ("Technical-Skill", 0.25), ("Realistic", 0.15)
    ],
    "Social": [
        ("People-Skill", 0.45), ("Community-Serve", 0.35), ("Teaching-Ed", 0.3),
        ("Enterprising", 0.2), ("Patient-Care", 0.15)
    ],
    "Enterprising": [
        ("People-Skill", 0.4), ("Startup-Venture", 0.35), ("Marketing-Sales", 0.3),
        ("Social", 0.25), ("Admin-Skill", 0.2)
    ],
    "Conventional": [
        ("Admin-Skill", 0.45), ("Finance-Acct", 0.35), ("Analytical-Skill", 0.3),
        ("Data-Analytics", 0.2), ("People-Skill", 0.15)
    ],
    "People-Skill": [
        ("Social", 0.45), ("Teaching-Ed", 0.35), ("Community-Serve", 0.3),
        ("Enterprising", 0.2), ("People-Skill", 0.15)
    ],
    "Technical-Skill": [
        ("Realistic", 0.4), ("Investigative", 0.35), ("Analytical-Skill", 0.3),
        ("Software-Dev", 0.2), ("Hardware-Systems", 0.15)
    ],
    "Analytical-Skill": [
        ("Investigative", 0.45), ("Data-Analytics", 0.35), ("Lab-Research", 0.3),
        ("Technical-Skill", 0.2), ("Conventional", 0.15)
    ],
    "Physical-Skill": [
        ("Realistic", 0.4), ("Sports-Ed", 0.35), ("Physical-Skill", 0.3),
        ("Field-Research", 0.2), ("Law-Enforce", 0.15)
    ],
    "Sports-Ed": [
        ("Physical-Skill", 0.45), ("Realistic", 0.4), ("Teaching-Ed", 0.3),
        ("People-Skill", 0.25), ("Social", 0.2)
    ],
}


def build_multi_trait(primary_tag):
    """Build a multi-trait dict from a primary trait using curated secondaries"""
    if not primary_tag:
        return {}
    
    trait_tags = {primary_tag: 1.0}
    secondaries = CURATED_SECONDARIES.get(primary_tag, [])
    
    for secondary, weight in secondaries:
        if secondary != primary_tag and secondary not in trait_tags:
            trait_tags[secondary] = weight
    
    return trait_tags


if __name__ == "__main__":
    # Test a few
    tests = ["Patient-Care", "Software-Dev", "Agri-Nature", "Maritime-Sea", 
             "Finance-Acct", "Visual-Design", "Law-Enforce", "Teaching-Ed",
             "Hardware-Systems", "Data-Analytics"]
    
    for primary in tests:
        result = build_multi_trait(primary)
        print(f"{primary}: {sorted(result.items(), key=lambda x: -x[1])}")
        print(f"  Count: {len(result)} traits")
        print()
