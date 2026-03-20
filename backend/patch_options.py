"""
One-time patch script: expand questions 381 and 384-423 from 4 to 6 options.
Safe to re-run: skips any question already at 6+ options.
"""

with open('questions_enhanced.py', 'r', encoding='utf-8') as f:
    content = f.read()


def fmt_opt(oid, text, tags):
    tag_str = ', '.join('"' + k + '": ' + str(v) for k, v in tags.items())
    return '            {"option_id": ' + str(oid) + ', "option_text": "' + text + '", "trait_tags": {' + tag_str + '}}'


def add_options(src, qid, new_opts):
    q_marker = '"question_id": ' + str(qid) + ','
    q_start = src.find(q_marker)
    if q_start == -1:
        return src, False

    opts_start = src.find('"options": [', q_start)
    if opts_start == -1:
        return src, False

    scan_start = opts_start + len('"options": [')
    depth = 0
    opts_end = -1
    for i in range(scan_start, len(src)):
        c = src[i]
        if c == '[':
            depth += 1
        elif c == ']':
            if depth == 0:
                opts_end = i
                break
            depth -= 1

    if opts_end == -1:
        return src, False

    # Count existing options (safety check)
    current_count = src[scan_start:opts_end].count('"option_id"')
    if current_count >= 6:
        return src, 'skip'

    last_close = src.rfind('}', scan_start, opts_end)
    if last_close == -1:
        return src, False

    insertion = ',\n' + ',\n'.join(fmt_opt(*opt) for opt in new_opts)
    new_src = src[:last_close + 1] + insertion + src[last_close + 1:]
    return new_src, True


ADDITIONS = {
    381: [
        (3781, "Professional boundaries \u2014 I balance deep care with healthy objectivity", {"Social-Work": 0.9, "Counseling": 0.6, "Admin-Skill": 0.4}),
        (3782, "Creativity \u2014 I find unexpected ways to reach and connect with people", {"Creative-Skill": 0.5, "People-Skill": 0.9, "Community-Serve": 0.5}),
    ],
    384: [
        (3787, "Strength and conditioning for competitive performance sports", {"Physical-Skill": 0.9, "Sports-Ed": 0.8, "Nutrition-Diet": 0.4}),
        (3788, "Outdoor and adventure education programs", {"Physical-Skill": 0.8, "Field-Research": 0.4, "Teaching-Ed": 0.7}),
    ],
    385: [
        (3789, "Speed, agility, and explosive power development", {"Physical-Skill": 0.9, "Sports-Ed": 0.7, "Teaching-Ed": 0.4}),
        (3790, "Game intelligence and tactical decision-making skills", {"Sports-Ed": 0.9, "Analytical-Skill": 0.5, "Teaching-Ed": 0.4}),
    ],
    386: [
        (3791, "Sports medicine and injury prevention assessment", {"Rehab-Therapy": 0.8, "Physical-Skill": 0.7, "Patient-Care": 0.4}),
        (3792, "Performance analytics and data-driven training methods", {"Data-Analytics": 0.7, "Sports-Ed": 0.8, "Physical-Skill": 0.4}),
    ],
    387: [
        (3793, "Corporate wellness and employee fitness programs", {"Physical-Skill": 0.8, "Admin-Skill": 0.5, "Teaching-Ed": 0.6}),
        (3794, "Adapted physical education for persons with disabilities", {"Rehab-Therapy": 0.8, "Teaching-Ed": 0.7, "Physical-Skill": 0.5}),
    ],
    388: [
        (3795, "Video analysis and movement review sessions", {"Sports-Ed": 0.8, "Technical-Skill": 0.5, "Physical-Skill": 0.5}),
        (3796, "Periodization logs and structured training journals", {"Analytical-Skill": 0.7, "Sports-Ed": 0.8, "Physical-Skill": 0.4}),
    ],
    389: [
        (3797, "Martial arts and combat sports tournaments", {"Physical-Skill": 0.9, "Sports-Ed": 0.6, "Teaching-Ed": 0.3}),
        (3798, "Health and wellness expos and community fitness events", {"Physical-Skill": 0.7, "Community-Serve": 0.6, "People-Skill": 0.5}),
    ],
    390: [
        (3799, "Coordinating the full rehabilitation team for the athlete", {"Admin-Skill": 0.6, "Sports-Ed": 0.7, "Rehab-Therapy": 0.6}),
        (3800, "Teaching injury prevention and safe movement habits", {"Teaching-Ed": 0.7, "Physical-Skill": 0.7, "Rehab-Therapy": 0.5}),
    ],
    391: [
        (3801, "University or national sports training complex", {"Physical-Skill": 0.9, "Sports-Ed": 0.7, "Teaching-Ed": 0.4}),
        (3802, "Open-water or beach sports environment", {"Physical-Skill": 0.8, "Maritime-Sea": 0.3, "Agri-Nature": 0.3}),
    ],
    392: [
        (3803, "Balance winning culture with athlete wellbeing and development", {"Sports-Ed": 0.8, "Teaching-Ed": 0.7, "Counseling": 0.4}),
        (3804, "Support underprivileged youth through sports programs", {"Community-Serve": 0.7, "Sports-Ed": 0.7, "Physical-Skill": 0.5}),
    ],
    393: [
        (3805, "Balance and coordination testing for sports performance", {"Physical-Skill": 0.9, "Sports-Ed": 0.7, "Analytical-Skill": 0.4}),
        (3806, "Biomechanical lab analysis using motion capture tools", {"Physical-Skill": 0.8, "Lab-Research": 0.6, "Mechanical-Design": 0.3}),
    ],
    394: [
        (3807, "Nutrition forms the foundation before training even begins", {"Nutrition-Diet": 0.9, "Physical-Skill": 0.5, "Sports-Ed": 0.5}),
        (3808, "A balance of training, rest, and nutrition drives real progress", {"Sports-Ed": 0.8, "Nutrition-Diet": 0.6, "Physical-Skill": 0.5}),
    ],
    395: [
        (3809, "Sport-for-development and cross-cultural programs", {"Community-Serve": 0.7, "People-Skill": 0.5, "Teaching-Ed": 0.5}),
        (3810, "National championships and high-performance competitions", {"Sports-Ed": 0.9, "Physical-Skill": 0.7, "Analytical-Skill": 0.3}),
    ],
    396: [
        (3811, "Interdisciplinary connections between PE and health science", {"Teaching-Ed": 0.8, "Nutrition-Diet": 0.5, "Physical-Skill": 0.5}),
        (3812, "Traditional and indigenous games as cultural heritage", {"Teaching-Ed": 0.7, "Physical-Skill": 0.7, "People-Skill": 0.4}),
    ],
    397: [
        (3813, "Beach volleyball and coastal recreational sports", {"Physical-Skill": 0.8, "Community-Serve": 0.4, "Field-Research": 0.3}),
        (3814, "Scuba diving and underwater sports activities", {"Physical-Skill": 0.8, "Field-Research": 0.4, "Maritime-Sea": 0.3}),
    ],
    398: [
        (3815, "Mental readiness is a core sports skill like any other", {"Counseling": 0.6, "Sports-Ed": 0.9, "People-Skill": 0.4}),
        (3816, "Mind and body training must be integrated for peak output", {"Physical-Skill": 0.8, "Sports-Ed": 0.8, "Counseling": 0.4}),
    ],
    399: [
        (3817, "Designing recreation and wellness policies for institutions", {"Admin-Skill": 0.8, "Teaching-Ed": 0.5, "Physical-Skill": 0.4}),
        (3818, "Expanding sports access for underserved communities", {"Community-Serve": 0.8, "Physical-Skill": 0.5, "Admin-Skill": 0.4}),
    ],
    400: [
        (3819, "Soil science and land resource conservation", {"Agri-Nature": 0.9, "Environmental-Sci": 0.7, "Lab-Research": 0.4}),
        (3820, "Food and nutrition security at the community level", {"Agri-Nature": 0.7, "Food-Science": 0.5, "Nutrition-Diet": 0.6}),
    ],
    401: [
        (3821, "Permaculture and regenerative land management", {"Agri-Nature": 0.9, "Environmental-Sci": 0.8, "Physical-Skill": 0.3}),
        (3822, "Aquaculture and integrated fish-farming systems", {"Agri-Nature": 0.8, "Maritime-Sea": 0.3, "Field-Research": 0.5}),
    ],
    402: [
        (3823, "Milk, egg, and fiber production efficiency", {"Agri-Nature": 0.9, "Industrial-Ops": 0.4, "Field-Research": 0.4}),
        (3824, "Small animal and companion animal production systems", {"Agri-Nature": 0.8, "Patient-Care": 0.4, "Field-Research": 0.4}),
    ],
    403: [
        (3825, "Consult local farmers and draw on indigenous knowledge", {"Agri-Nature": 0.8, "People-Skill": 0.5, "Community-Serve": 0.5}),
        (3826, "Design a crop rotation and intercropping system", {"Agri-Nature": 0.9, "Environmental-Sci": 0.6, "Analytical-Skill": 0.4}),
    ],
    404: [
        (3827, "Remote sensing and satellite crop monitoring systems", {"Agri-Nature": 0.7, "Data-Analytics": 0.6, "Technical-Skill": 0.5}),
        (3828, "AI and machine learning for crop yield prediction", {"Agri-Nature": 0.6, "AI-ML": 0.5, "Data-Analytics": 0.6}),
    ],
    405: [
        (3829, "Seasonal fieldwork is fulfilling despite the challenges", {"Agri-Nature": 0.9, "Physical-Skill": 0.5, "Field-Research": 0.4}),
        (3830, "Prefer managing teams and farming operations from an oversight role", {"Agri-Nature": 0.7, "Admin-Skill": 0.6, "People-Skill": 0.4}),
    ],
    406: [
        (3831, "Connecting smallholder farmers to premium markets", {"Agri-Nature": 0.7, "Marketing-Sales": 0.6, "Community-Serve": 0.5}),
        (3832, "Developing functional foods with health and wellness benefits", {"Food-Science": 0.8, "Nutrition-Diet": 0.6, "Lab-Research": 0.4}),
    ],
    407: [
        (3833, "Seed banking and heritage crop variety preservation", {"Agri-Nature": 0.9, "Field-Research": 0.5, "Lab-Research": 0.4}),
        (3834, "Integrating renewable energy and solar irrigation on farms", {"Agri-Nature": 0.7, "Environmental-Eng": 0.6, "Technical-Skill": 0.4}),
    ],
    408: [
        (3835, "Farmer cooperative development and rural organizations", {"Agri-Nature": 0.8, "Community-Serve": 0.6, "Admin-Skill": 0.4}),
        (3836, "Digital platforms connecting farmers directly to buyers", {"Agri-Nature": 0.7, "Marketing-Sales": 0.5, "Technical-Skill": 0.4}),
    ],
    409: [
        (3837, "Biochar and biostimulant application for soil health", {"Agri-Nature": 0.9, "Lab-Research": 0.5, "Environmental-Sci": 0.5}),
        (3838, "Erosion mapping and watershed restoration planning", {"Agri-Nature": 0.8, "Environmental-Sci": 0.7, "Field-Research": 0.4}),
    ],
    410: [
        (3839, "Zoo and wildlife management practices", {"Agri-Nature": 0.8, "Field-Research": 0.5, "Environmental-Sci": 0.4}),
        (3840, "Animal biosecurity, quarantine, and import protocols", {"Agri-Nature": 0.8, "Law-Enforce": 0.3, "Lab-Research": 0.4}),
    ],
    411: [
        (3841, "Soil microbiome research and beneficial bacteria studies", {"Agri-Nature": 0.8, "Lab-Research": 0.7, "Environmental-Sci": 0.4}),
        (3842, "Participatory research with smallholder farming communities", {"Agri-Nature": 0.8, "Community-Serve": 0.6, "Field-Research": 0.4}),
    ],
    412: [
        (3843, "Sustainable packaging and eco-friendly storage materials", {"Agri-Nature": 0.7, "Environmental-Sci": 0.6, "Industrial-Ops": 0.4}),
        (3844, "Crop insurance programs and post-harvest loss reduction", {"Agri-Nature": 0.7, "Admin-Skill": 0.5, "Analytical-Skill": 0.4}),
    ],
    413: [
        (3845, "Technology is most useful after mastering traditional farming", {"Agri-Nature": 0.9, "Field-Research": 0.5, "Physical-Skill": 0.3}),
        (3846, "Selective use of technology based on actual farm needs and data", {"Agri-Nature": 0.8, "Data-Analytics": 0.4, "Technical-Skill": 0.4}),
    ],
    414: [
        (3847, "Labor and employment law protecting workers rights", {"Legal-Practice": 0.9, "Community-Serve": 0.5, "Admin-Skill": 0.3}),
        (3848, "Environmental and natural resources law", {"Legal-Practice": 0.8, "Environmental-Sci": 0.5, "Community-Serve": 0.4}),
    ],
    415: [
        (3849, "Profiling suspect behavior through psychological analysis", {"Forensic-Sci": 0.8, "Counseling": 0.4, "Law-Enforce": 0.6}),
        (3850, "Conducting surveillance and monitoring operations", {"Law-Enforce": 0.9, "Technical-Skill": 0.4, "Admin-Skill": 0.3}),
    ],
    416: [
        (3851, "Contract drafting and transactional legal work", {"Legal-Practice": 0.9, "Admin-Skill": 0.5, "Finance-Acct": 0.4}),
        (3852, "Supreme Court appeals and constitutional interpretation", {"Legal-Practice": 1.0, "Analytical-Skill": 0.6, "Teaching-Ed": 0.3}),
    ],
    417: [
        (3853, "Prioritize the fundamental rights and dignity of all involved", {"Social-Work": 0.5, "Legal-Practice": 0.8, "Community-Serve": 0.5}),
        (3854, "Apply universal ethical principles that transcend local law", {"Legal-Practice": 0.9, "Community-Serve": 0.5, "Analytical-Skill": 0.4}),
    ],
    418: [
        (3855, "Human rights lawyer or non-profit legal advocate", {"Legal-Practice": 0.8, "Community-Serve": 0.7, "Social-Work": 0.4}),
        (3856, "Corporate counsel or legal compliance officer", {"Legal-Practice": 0.9, "Finance-Acct": 0.4, "Admin-Skill": 0.5}),
    ],
    419: [
        (3857, "Stronger support systems for crime victims and survivors", {"Social-Work": 0.7, "Counseling": 0.5, "Community-Serve": 0.7}),
        (3858, "Judicial independence, transparency, and anti-corruption measures", {"Legal-Practice": 0.8, "Community-Serve": 0.5, "Analytical-Skill": 0.4}),
    ],
    420: [
        (3859, "Legal technology and AI-assisted legal research", {"Legal-Practice": 0.8, "Data-Analytics": 0.5, "Technical-Skill": 0.4}),
        (3860, "Comparative law and international legal frameworks", {"Legal-Practice": 0.9, "Analytical-Skill": 0.5, "Teaching-Ed": 0.3}),
    ],
    421: [
        (3861, "Making the legal process accessible and easy to understand", {"Teaching-Ed": 0.5, "Legal-Practice": 0.8, "People-Skill": 0.6}),
        (3862, "Providing emotional reassurance throughout the legal process", {"Counseling": 0.5, "People-Skill": 0.8, "Legal-Practice": 0.5}),
    ],
    422: [
        (3863, "Ballistics evidence and firearms examination", {"Forensic-Sci": 0.9, "Mechanical-Design": 0.3, "Law-Enforce": 0.5}),
        (3864, "Questioned documents and handwriting analysis", {"Forensic-Sci": 0.9, "Analytical-Skill": 0.5, "Admin-Skill": 0.3}),
    ],
    423: [
        (3865, "Prefer community prevention and social crime programs", {"Community-Serve": 0.8, "Teaching-Ed": 0.5, "Social-Work": 0.5}),
        (3866, "Serve as a civilian researcher or policy consultant", {"Analytical-Skill": 0.7, "Legal-Practice": 0.5, "Forensic-Sci": 0.4}),
    ],
}

patched = 0
skipped = 0
failed = 0

for qid in sorted(ADDITIONS.keys()):
    content, result = add_options(content, qid, ADDITIONS[qid])
    if result is True:
        print(f"Q{qid}: patched OK")
        patched += 1
    elif result == 'skip':
        print(f"Q{qid}: already 6+ options, skipped")
        skipped += 1
    else:
        print(f"Q{qid}: FAILED to find question or options")
        failed += 1

print(f"\nSummary: {patched} patched, {skipped} skipped, {failed} failed")

if failed == 0:
    with open('questions_enhanced.py', 'w', encoding='utf-8') as f:
        f.write(content)
    print("File written successfully.")
else:
    print("File NOT written due to failures. Fix issues and retry.")
