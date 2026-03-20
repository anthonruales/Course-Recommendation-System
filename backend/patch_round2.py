#!/usr/bin/env python3
"""Round 2: Focused questions for all traits still under 10 on-topic."""
import re, sys, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

QID = 649; OID = 5217  # 102 questions * 6 options = 612, 4605+612=5217
def nq(text, qtags, opts, branches):
    global QID, OID
    options = []
    for (otext, otags) in opts:
        options.append({"option_id": OID, "option_text": otext, "trait_tags": otags})
        OID += 1
    q = {"question_id": QID, "question_text": text, "weight": 1.5, "trait_tags": qtags, "options": options}
    QID += 1
    return q, branches

ALL = []

# Admin-Skill (was 4 — need ~21 more) - 7 questions
adm = [
("What office process would you improve?", {"Admin-Skill": 0.9}, [
("Filing and document management system", {"Admin-Skill": 1.0, "Technical-Skill": 0.4}),
("Meeting minutes and correspondence tracking", {"Admin-Skill": 1.0, "People-Skill": 0.3}),
("Purchase order and procurement workflow", {"Admin-Skill": 0.9, "Finance-Acct": 0.4}),
("Employee attendance and leave tracking", {"Admin-Skill": 0.9, "HR-Management": 0.4}),
("Mail and courier handling procedures", {"Admin-Skill": 0.9, "Physical-Skill": 0.3}),
("Visitor log and access management", {"Admin-Skill": 1.0, "Law-Enforce": 0.3})], ["business"]),
("What administrative challenge motivates you?", {"Admin-Skill": 0.9}, [
("Reducing paperwork and going digital", {"Admin-Skill": 1.0, "Technical-Skill": 0.4}),
("Coordinating between multiple departments", {"Admin-Skill": 0.9, "People-Skill": 0.4}),
("Maintaining accurate records and databases", {"Admin-Skill": 1.0, "Data-Analytics": 0.3}),
("Organizing company events and functions", {"Admin-Skill": 0.9, "Hospitality-Svc": 0.4}),
("Managing office supplies and inventory", {"Admin-Skill": 0.9, "Industrial-Ops": 0.3}),
("Handling confidential documents securely", {"Admin-Skill": 1.0, "Cyber-Defense": 0.3})], ["business"]),
("What type of administrative project interests you?", {"Admin-Skill": 0.9}, [
("Implementing a new filing classification system", {"Admin-Skill": 1.0, "Analytical-Skill": 0.4}),
("Setting up a new office from scratch", {"Admin-Skill": 0.9, "Spatial-Design": 0.3}),
("Creating an employee onboarding handbook", {"Admin-Skill": 0.9, "HR-Management": 0.4}),
("Organizing a company-wide town hall meeting", {"Admin-Skill": 0.9, "People-Skill": 0.4}),
("Cleaning up and archiving old records", {"Admin-Skill": 1.0, "Analytical-Skill": 0.3}),
("Building a shared knowledge base wiki", {"Admin-Skill": 0.9, "Technical-Skill": 0.4})], ["business"]),
("What administrative support role appeals to you?", {"Admin-Skill": 0.9}, [
("Legal secretary handling court documents", {"Admin-Skill": 0.9, "Legal-Practice": 0.5}),
("Medical office receptionist managing patients", {"Admin-Skill": 0.9, "Patient-Care": 0.4}),
("School registrar handling student records", {"Admin-Skill": 0.9, "Teaching-Ed": 0.4}),
("Bank teller processing transactions", {"Admin-Skill": 0.9, "Finance-Acct": 0.4}),
("Hotel concierge coordinating guest services", {"Admin-Skill": 0.9, "Hospitality-Svc": 0.5}),
("Government clerk processing permits", {"Admin-Skill": 1.0, "Community-Serve": 0.3})], ["business"]),
("What daily admin task do you enjoy most?", {"Admin-Skill": 0.9}, [
("Sorting and prioritizing incoming requests", {"Admin-Skill": 1.0, "Analytical-Skill": 0.3}),
("Drafting professional emails and letters", {"Admin-Skill": 0.9, "Creative-Skill": 0.3}),
("Creating organized spreadsheets and reports", {"Admin-Skill": 1.0, "Data-Analytics": 0.3}),
("Answering phone calls and directing inquiries", {"Admin-Skill": 0.9, "People-Skill": 0.4}),
("Scheduling appointments and managing calendars", {"Admin-Skill": 0.9, "Technical-Skill": 0.3}),
("Filing expense reports and receipts", {"Admin-Skill": 0.9, "Finance-Acct": 0.3})], ["business"]),
("What office management certification would you pursue?", {"Admin-Skill": 0.9}, [
("Certified Administrative Professional (CAP)", {"Admin-Skill": 1.0, "People-Skill": 0.3}),
("Microsoft Office Specialist (MOS)", {"Admin-Skill": 0.9, "Technical-Skill": 0.5}),
("Project Management Professional (PMP)", {"Admin-Skill": 0.9, "Industrial-Ops": 0.4}),
("Certified Records Manager (CRM)", {"Admin-Skill": 1.0, "Analytical-Skill": 0.3}),
("Business Communication certificate", {"Admin-Skill": 0.9, "People-Skill": 0.5}),
("Office Safety and Health certification", {"Admin-Skill": 0.9, "Physical-Skill": 0.3})], ["business"]),
("What excites you about office administration?", {"Admin-Skill": 0.9}, [
("Everything running smoothly and on time", {"Admin-Skill": 1.0, "Industrial-Ops": 0.3}),
("Being the person everyone comes to for help", {"Admin-Skill": 0.9, "People-Skill": 0.5}),
("Organizing chaos into structured systems", {"Admin-Skill": 1.0, "Analytical-Skill": 0.4}),
("Making a great first impression for the company", {"Admin-Skill": 0.9, "Marketing-Sales": 0.3}),
("Keeping accurate and reliable records", {"Admin-Skill": 0.9, "Analytical-Skill": 0.3}),
("Supporting leaders and helping them succeed", {"Admin-Skill": 0.9, "People-Skill": 0.4})], ["business"]),
]
for t, qt, o, br in adm: ALL.append(nq(t, qt, o, br))

# Analytical-Skill (was 1 — need ~24 more) - 8 questions
ana = [
("What analytical problem-solving approach suits you?", {"Analytical-Skill": 0.9}, [
("Breaking complex problems into smaller parts", {"Analytical-Skill": 1.0, "Technical-Skill": 0.3}),
("Finding patterns in large datasets", {"Analytical-Skill": 0.9, "Data-Analytics": 0.4}),
("Creating logical flowcharts and diagrams", {"Analytical-Skill": 1.0, "Software-Dev": 0.3}),
("Testing hypotheses with controlled experiments", {"Analytical-Skill": 0.9, "Lab-Research": 0.4}),
("Comparing options with pros and cons analysis", {"Analytical-Skill": 0.9, "Finance-Acct": 0.3}),
("Using mathematical models to predict outcomes", {"Analytical-Skill": 1.0, "Data-Analytics": 0.4})], ["science", "technology"]),
("What type of puzzles or challenges do you enjoy?", {"Analytical-Skill": 0.9}, [
("Logic puzzles and brain teasers", {"Analytical-Skill": 1.0, "Creative-Skill": 0.3}),
("Sudoku and number pattern games", {"Analytical-Skill": 0.9, "Data-Analytics": 0.3}),
("Strategy games requiring planning ahead", {"Analytical-Skill": 0.9, "Game-Dev": 0.3}),
("Debug a system by tracing errors step by step", {"Analytical-Skill": 1.0, "Software-Dev": 0.4}),
("Crossword puzzles and word association", {"Analytical-Skill": 0.9, "Creative-Skill": 0.3}),
("Mechanical puzzles and 3D assembly challenges", {"Analytical-Skill": 0.9, "Mechanical-Design": 0.3})], ["science"]),
("What critical thinking skill would you develop?", {"Analytical-Skill": 0.9}, [
("Evaluating evidence and sources for credibility", {"Analytical-Skill": 1.0, "Lab-Research": 0.3}),
("Identifying logical fallacies in arguments", {"Analytical-Skill": 0.9, "Legal-Practice": 0.4}),
("Root cause analysis using the 5 Whys method", {"Analytical-Skill": 1.0, "Industrial-Ops": 0.3}),
("Statistical reasoning and probability assessment", {"Analytical-Skill": 0.9, "Data-Analytics": 0.5}),
("Systems thinking — seeing the big picture", {"Analytical-Skill": 0.9, "Environmental-Eng": 0.3}),
("Decision matrices for multi-criteria evaluation", {"Analytical-Skill": 1.0, "Admin-Skill": 0.3})], ["science"]),
("Where would you apply analytical skills?", {"Analytical-Skill": 0.9}, [
("Financial audit examining company books", {"Analytical-Skill": 0.9, "Finance-Acct": 0.5}),
("Quality testing in a manufacturing lab", {"Analytical-Skill": 0.9, "Industrial-Ops": 0.5}),
("Data science for business intelligence", {"Analytical-Skill": 0.9, "Data-Analytics": 0.5}),
("Research methodology and experimental design", {"Analytical-Skill": 1.0, "Lab-Research": 0.4}),
("Strategic consulting for organizations", {"Analytical-Skill": 0.9, "Startup-Venture": 0.3}),
("Policy analysis for government agencies", {"Analytical-Skill": 0.9, "Legal-Practice": 0.4})], ["science", "business"]),
("What data interpretation task interests you?", {"Analytical-Skill": 0.9, "Data-Analytics": 0.3}, [
("Reading financial statements and ratios", {"Analytical-Skill": 1.0, "Finance-Acct": 0.5}),
("Interpreting scientific research results", {"Analytical-Skill": 0.9, "Lab-Research": 0.4}),
("Analyzing survey responses for trends", {"Analytical-Skill": 0.9, "Data-Analytics": 0.4}),
("Evaluating engineering test measurements", {"Analytical-Skill": 1.0, "Mechanical-Design": 0.3}),
("Reviewing medical diagnostic reports", {"Analytical-Skill": 0.9, "Medical-Lab": 0.4}),
("Comparing market research data", {"Analytical-Skill": 0.9, "Marketing-Sales": 0.4})], ["science"]),
("What systematic approach appeals to you?", {"Analytical-Skill": 0.9}, [
("Scientific method for testing ideas", {"Analytical-Skill": 1.0, "Lab-Research": 0.4}),
("SWOT analysis for strategy planning", {"Analytical-Skill": 0.9, "Marketing-Sales": 0.3}),
("Fishbone diagram for cause-effect analysis", {"Analytical-Skill": 1.0, "Industrial-Ops": 0.3}),
("Risk assessment and mitigation planning", {"Analytical-Skill": 0.9, "Finance-Acct": 0.3}),
("Process mapping and workflow optimization", {"Analytical-Skill": 0.9, "Industrial-Ops": 0.4}),
("Benchmarking and competitive comparison", {"Analytical-Skill": 0.9, "Marketing-Sales": 0.3})], ["science", "business"]),
("What analytical tool would you learn?", {"Analytical-Skill": 0.9, "Technical-Skill": 0.3}, [
("Spreadsheet formulas and pivot tables", {"Analytical-Skill": 1.0, "Data-Analytics": 0.4}),
("SPSS or R for statistical analysis", {"Analytical-Skill": 0.9, "Data-Analytics": 0.5}),
("Mind mapping software for organizing ideas", {"Analytical-Skill": 0.9, "Creative-Skill": 0.3}),
("Flowchart tools like Visio or Lucidchart", {"Analytical-Skill": 1.0, "Software-Dev": 0.3}),
("Financial analysis calculators and models", {"Analytical-Skill": 0.9, "Finance-Acct": 0.4}),
("SQL for querying and examining databases", {"Analytical-Skill": 0.9, "Software-Dev": 0.4})], ["science", "technology"]),
("What reasoning challenge would you tackle?", {"Analytical-Skill": 0.9}, [
("Solving a mystery using clues and evidence", {"Analytical-Skill": 1.0, "Forensic-Sci": 0.3}),
("Optimizing a route or schedule for efficiency", {"Analytical-Skill": 0.9, "Industrial-Ops": 0.4}),
("Detecting inconsistencies in data or reports", {"Analytical-Skill": 1.0, "Finance-Acct": 0.3}),
("Predicting outcomes from historical trends", {"Analytical-Skill": 0.9, "Data-Analytics": 0.5}),
("Designing a fair scoring or ranking system", {"Analytical-Skill": 0.9, "Data-Analytics": 0.3}),
("Finding the root cause of a recurring problem", {"Analytical-Skill": 1.0, "Industrial-Ops": 0.3})], ["science"]),
]
for t, qt, o, br in ana: ALL.append(nq(t, qt, o, br))

# Creative-Skill (was 1) - 7 questions
crs = [
("What creative activity do you enjoy most?", {"Creative-Skill": 0.9}, [
("Drawing, painting, or sketching", {"Creative-Skill": 1.0, "Visual-Design": 0.5}),
("Writing stories, poems, or scripts", {"Creative-Skill": 0.9, "Film-Broadcast": 0.3}),
("Composing music or writing songs", {"Creative-Skill": 0.9, "Performing-Arts": 0.4}),
("Crafting handmade items and DIY projects", {"Creative-Skill": 0.9, "Physical-Skill": 0.3}),
("Photography and visual storytelling", {"Creative-Skill": 0.9, "Digital-Media": 0.4}),
("Brainstorming unique solutions to problems", {"Creative-Skill": 1.0, "Analytical-Skill": 0.3})], ["creative"]),
("How do you express creativity at work?", {"Creative-Skill": 0.9}, [
("Designing visually appealing presentations", {"Creative-Skill": 1.0, "Visual-Design": 0.4}),
("Thinking of innovative marketing campaigns", {"Creative-Skill": 0.9, "Marketing-Sales": 0.4}),
("Finding unconventional solutions to challenges", {"Creative-Skill": 1.0, "Analytical-Skill": 0.3}),
("Decorating and arranging spaces beautifully", {"Creative-Skill": 0.9, "Spatial-Design": 0.4}),
("Creating engaging social media content", {"Creative-Skill": 0.9, "Digital-Media": 0.4}),
("Developing new recipes or food presentations", {"Creative-Skill": 0.9, "Culinary-Arts": 0.5})], ["creative"]),
("What creative skill would you develop?", {"Creative-Skill": 0.9}, [
("Digital illustration and graphic design", {"Creative-Skill": 1.0, "Visual-Design": 0.5}),
("Video production and filmmaking", {"Creative-Skill": 0.9, "Film-Broadcast": 0.4}),
("Creative writing and storytelling", {"Creative-Skill": 0.9, "Digital-Media": 0.3}),
("Improvisation and thinking on your feet", {"Creative-Skill": 0.9, "Performing-Arts": 0.4}),
("3D modeling and character creation", {"Creative-Skill": 0.9, "Animation-3D": 0.5}),
("Innovation and design thinking methodology", {"Creative-Skill": 1.0, "Startup-Venture": 0.3})], ["creative"]),
("What inspires your creativity?", {"Creative-Skill": 0.9}, [
("Philippine culture and indigenous art forms", {"Creative-Skill": 1.0, "Visual-Design": 0.3}),
("Nature and the environment around you", {"Creative-Skill": 0.9, "Environmental-Sci": 0.3}),
("Technology and what's possible with new tools", {"Creative-Skill": 0.9, "Technical-Skill": 0.4}),
("Music, film, and contemporary media", {"Creative-Skill": 0.9, "Performing-Arts": 0.4}),
("Social issues and the desire for change", {"Creative-Skill": 0.9, "Community-Serve": 0.3}),
("Travel experiences and different cultures", {"Creative-Skill": 1.0, "Tourism-Travel": 0.3})], ["creative"]),
("Where would you apply creativity professionally?", {"Creative-Skill": 0.9}, [
("Advertising and creative agency", {"Creative-Skill": 1.0, "Marketing-Sales": 0.4}),
("Game design and entertainment studio", {"Creative-Skill": 0.9, "Game-Dev": 0.5}),
("Architectural and interior design firm", {"Creative-Skill": 0.9, "Spatial-Design": 0.4}),
("Fashion and textile design", {"Creative-Skill": 0.9, "Visual-Design": 0.4}),
("Film production and broadcasting", {"Creative-Skill": 0.9, "Film-Broadcast": 0.4}),
("Product innovation and R&D department", {"Creative-Skill": 1.0, "Startup-Venture": 0.3})], ["creative"]),
("What design thinking phase excites you most?", {"Creative-Skill": 0.9}, [
("Empathize: understanding users and their needs", {"Creative-Skill": 0.9, "People-Skill": 0.5}),
("Define: framing the right problem to solve", {"Creative-Skill": 0.9, "Analytical-Skill": 0.4}),
("Ideate: generating tons of wild ideas", {"Creative-Skill": 1.0, "Analytical-Skill": 0.3}),
("Prototype: building quick mockups to test", {"Creative-Skill": 0.9, "Technical-Skill": 0.4}),
("Test: getting feedback and iterating", {"Creative-Skill": 1.0, "People-Skill": 0.3}),
("Storytelling: presenting the final concept", {"Creative-Skill": 0.9, "Performing-Arts": 0.3})], ["creative"]),
("What creative challenge would you tackle?", {"Creative-Skill": 0.9}, [
("Rebranding a local Filipino product for export", {"Creative-Skill": 1.0, "Marketing-Sales": 0.4}),
("Creating art installations for public spaces", {"Creative-Skill": 0.9, "Spatial-Design": 0.4}),
("Designing educational games for children", {"Creative-Skill": 0.9, "Teaching-Ed": 0.4}),
("Illustrating a children's book", {"Creative-Skill": 1.0, "Visual-Design": 0.4}),
("Creating an animated series pilot episode", {"Creative-Skill": 0.9, "Animation-3D": 0.4}),
("Designing a mobile app user experience", {"Creative-Skill": 0.9, "Mobile-Dev": 0.3})], ["creative"]),
]
for t, qt, o, br in crs: ALL.append(nq(t, qt, o, br))

# Technical-Skill (was 3) - 7 questions
tec = [
("What technical equipment do you prefer working with?", {"Technical-Skill": 0.9}, [
("Computers and IT hardware setup", {"Technical-Skill": 1.0, "Hardware-Systems": 0.4}),
("Electronic instruments and multimeters", {"Technical-Skill": 0.9, "Electrical-Power": 0.4}),
("Power tools and workshop equipment", {"Technical-Skill": 0.9, "Mechanical-Design": 0.3}),
("Medical devices and diagnostic equipment", {"Technical-Skill": 0.9, "Medical-Lab": 0.4}),
("Audio-visual and broadcast equipment", {"Technical-Skill": 0.9, "Film-Broadcast": 0.3}),
("Survey instruments and GPS devices", {"Technical-Skill": 1.0, "Field-Research": 0.4})], ["technology", "engineering"]),
("What hands-on technical skill would you learn?", {"Technical-Skill": 0.9}, [
("Computer assembly and troubleshooting", {"Technical-Skill": 1.0, "Hardware-Systems": 0.5}),
("Electrical wiring and panel installation", {"Technical-Skill": 0.9, "Electrical-Power": 0.4}),
("Soldering electronic components on boards", {"Technical-Skill": 0.9, "Hardware-Systems": 0.4}),
("Operating CNC and precision machinery", {"Technical-Skill": 0.9, "Mechanical-Design": 0.4}),
("Network cabling and infrastructure setup", {"Technical-Skill": 1.0, "Cloud-Systems": 0.3}),
("Calibrating laboratory instruments", {"Technical-Skill": 0.9, "Lab-Research": 0.4})], ["technology"]),
("What technical problem do you enjoy solving?", {"Technical-Skill": 0.9}, [
("Fixing devices and equipment that stopped working", {"Technical-Skill": 1.0, "Hardware-Systems": 0.4}),
("Debugging software or system errors", {"Technical-Skill": 0.9, "Software-Dev": 0.4}),
("Installing and configuring new systems", {"Technical-Skill": 0.9, "Cloud-Systems": 0.3}),
("Maintaining and servicing machinery", {"Technical-Skill": 0.9, "Mechanical-Design": 0.3}),
("Connecting and setting up AV equipment", {"Technical-Skill": 1.0, "Film-Broadcast": 0.3}),
("Troubleshooting network connectivity issues", {"Technical-Skill": 0.9, "Cloud-Systems": 0.4})], ["technology"]),
("What TESDA technical-vocational course interests you?", {"Technical-Skill": 0.9}, [
("Computer hardware servicing (CHS)", {"Technical-Skill": 1.0, "Hardware-Systems": 0.5}),
("Electrical installation and maintenance", {"Technical-Skill": 0.9, "Electrical-Power": 0.5}),
("Automotive servicing and repair", {"Technical-Skill": 0.9, "Mechanical-Design": 0.4}),
("Welding technology (SMAW/GMAW)", {"Technical-Skill": 0.9, "Mechanical-Design": 0.3}),
("Electronics product assembly and servicing", {"Technical-Skill": 1.0, "Hardware-Systems": 0.4}),
("Plumbing installation and maintenance", {"Technical-Skill": 0.9, "Civil-Build": 0.4})], ["technology", "engineering"]),
("What technical certification would you earn?", {"Technical-Skill": 0.9}, [
("CompTIA A+ for IT technician", {"Technical-Skill": 1.0, "Hardware-Systems": 0.5}),
("Cisco CCNA for networking", {"Technical-Skill": 0.9, "Cloud-Systems": 0.4}),
("AWS or Azure cloud certifications", {"Technical-Skill": 0.9, "Cloud-Systems": 0.5}),
("PLC programming certification", {"Technical-Skill": 0.9, "Electrical-Power": 0.4}),
("AutoCAD certified user", {"Technical-Skill": 0.9, "Civil-Build": 0.3}),
("TESDA National Certificate in electronics", {"Technical-Skill": 1.0, "Hardware-Systems": 0.4})], ["technology"]),
("What motivates you about technical work?", {"Technical-Skill": 0.9}, [
("Seeing something you built actually work", {"Technical-Skill": 1.0, "Creative-Skill": 0.3}),
("Understanding how systems and machines operate", {"Technical-Skill": 0.9, "Mechanical-Design": 0.3}),
("The satisfaction of fixing what was broken", {"Technical-Skill": 1.0, "Analytical-Skill": 0.3}),
("Staying current with the latest technologies", {"Technical-Skill": 0.9, "Software-Dev": 0.3}),
("Teaching others how to use tools and equipment", {"Technical-Skill": 0.9, "Teaching-Ed": 0.4}),
("Earning practical skills that are always in demand", {"Technical-Skill": 0.9, "Physical-Skill": 0.3})], ["technology"]),
("Where would you apply your technical skills?", {"Technical-Skill": 0.9}, [
("IT support department of a company", {"Technical-Skill": 1.0, "Admin-Skill": 0.3}),
("BPO technical support center", {"Technical-Skill": 0.9, "People-Skill": 0.4}),
("Industrial plant maintenance team", {"Technical-Skill": 0.9, "Industrial-Ops": 0.4}),
("Telecommunications company field technician", {"Technical-Skill": 0.9, "Electrical-Power": 0.3}),
("Hospital biomedical equipment department", {"Technical-Skill": 0.9, "Medical-Lab": 0.3}),
("Self-employed technical repair shop", {"Technical-Skill": 1.0, "Startup-Venture": 0.3})], ["technology"]),
]
for t, qt, o, br in tec: ALL.append(nq(t, qt, o, br))

# People-Skill (was 7) - 5 questions
peo = [
("What interpersonal situation do you handle best?", {"People-Skill": 0.9}, [
("Mediating a disagreement between teammates", {"People-Skill": 1.0, "Counseling": 0.4}),
("Motivating a group toward a shared goal", {"People-Skill": 0.9, "Admin-Skill": 0.3}),
("Explaining complex ideas in simple terms", {"People-Skill": 0.9, "Teaching-Ed": 0.4}),
("Building rapport with new acquaintances quickly", {"People-Skill": 1.0, "Marketing-Sales": 0.3}),
("Listening deeply to someone who needs support", {"People-Skill": 0.9, "Counseling": 0.5}),
("Networking and making professional connections", {"People-Skill": 0.9, "Startup-Venture": 0.3})], ["social"]),
("What team leadership style suits you?", {"People-Skill": 0.9}, [
("Democratic: getting everyone's input before deciding", {"People-Skill": 1.0, "Admin-Skill": 0.3}),
("Coaching: developing each team member's strengths", {"People-Skill": 0.9, "Teaching-Ed": 0.5}),
("Servant: putting team needs ahead of your own", {"People-Skill": 0.9, "Community-Serve": 0.4}),
("Collaborative: working alongside the team as equals", {"People-Skill": 1.0, "Creative-Skill": 0.3}),
("Visionary: inspiring others with a compelling goal", {"People-Skill": 0.9, "Startup-Venture": 0.3}),
("Mentoring: guiding through experience and wisdom", {"People-Skill": 0.9, "Counseling": 0.4})], ["social", "business"]),
("What communication skill would you strengthen?", {"People-Skill": 0.9}, [
("Public speaking and presentation delivery", {"People-Skill": 1.0, "Performing-Arts": 0.3}),
("Active listening and empathetic responses", {"People-Skill": 0.9, "Counseling": 0.5}),
("Persuasion and influential negotiation", {"People-Skill": 0.9, "Marketing-Sales": 0.4}),
("Written communication and professional emails", {"People-Skill": 0.9, "Admin-Skill": 0.3}),
("Cross-cultural communication and sensitivity", {"People-Skill": 1.0, "Tourism-Travel": 0.3}),
("Conflict resolution and peace-building", {"People-Skill": 0.9, "Social-Work": 0.4})], ["social"]),
("Who would you most enjoy helping?", {"People-Skill": 0.9}, [
("Customers with product questions and concerns", {"People-Skill": 1.0, "Marketing-Sales": 0.3}),
("Students struggling to understand lessons", {"People-Skill": 0.9, "Teaching-Ed": 0.5}),
("Patients recovering from illness or injury", {"People-Skill": 0.9, "Patient-Care": 0.4}),
("Colleagues dealing with workplace stress", {"People-Skill": 0.9, "Counseling": 0.4}),
("Community members facing social challenges", {"People-Skill": 1.0, "Social-Work": 0.4}),
("Tourists navigating an unfamiliar place", {"People-Skill": 0.9, "Tourism-Travel": 0.4})], ["social"]),
("What group activity do you enjoy facilitating?", {"People-Skill": 0.9}, [
("Team-building games and icebreakers", {"People-Skill": 1.0, "Sports-Ed": 0.3}),
("Brainstorming sessions for new ideas", {"People-Skill": 0.9, "Creative-Skill": 0.4}),
("Group discussions and roundtable forums", {"People-Skill": 0.9, "Teaching-Ed": 0.3}),
("Community organizing and town hall meetings", {"People-Skill": 0.9, "Community-Serve": 0.5}),
("Mentoring circles and peer support groups", {"People-Skill": 1.0, "Counseling": 0.4}),
("Training workshops and skills seminars", {"People-Skill": 0.9, "Teaching-Ed": 0.4})], ["social", "education"]),
]
for t, qt, o, br in peo: ALL.append(nq(t, qt, o, br))

# Physical-Skill (was 8) - 4 questions
phy = [
("What physical skill interests you most?", {"Physical-Skill": 0.9}, [
("Strength training and weight lifting", {"Physical-Skill": 1.0, "Sports-Ed": 0.4}),
("Swimming and water sports", {"Physical-Skill": 0.9, "Maritime-Sea": 0.3}),
("Outdoor hiking and mountaineering", {"Physical-Skill": 0.9, "Field-Research": 0.3}),
("Construction and hands-on building", {"Physical-Skill": 0.9, "Civil-Build": 0.4}),
("Martial arts discipline and self-defense", {"Physical-Skill": 1.0, "Sports-Ed": 0.3}),
("Dance movement and body coordination", {"Physical-Skill": 0.9, "Performing-Arts": 0.4})], ["physical"]),
("Where would you apply physical fitness?", {"Physical-Skill": 0.9}, [
("Military or ROTC officer training", {"Physical-Skill": 1.0, "Law-Enforce": 0.4}),
("Construction site operations and labor", {"Physical-Skill": 0.9, "Civil-Build": 0.5}),
("Athletic coaching for competitive sports", {"Physical-Skill": 0.9, "Sports-Ed": 0.5}),
("Farm work and agricultural operations", {"Physical-Skill": 0.9, "Agri-Nature": 0.5}),
("Rescue and disaster emergency response", {"Physical-Skill": 0.9, "Community-Serve": 0.4}),
("Fitness instructor and personal trainer", {"Physical-Skill": 1.0, "Sports-Ed": 0.4})], ["physical"]),
("What physically demanding job appeals to you?", {"Physical-Skill": 0.9}, [
("Firefighter combating blazes and rescuing people", {"Physical-Skill": 1.0, "Community-Serve": 0.4}),
("Maritime crew working on ships", {"Physical-Skill": 0.9, "Maritime-Sea": 0.5}),
("Lineman maintaining power lines", {"Physical-Skill": 0.9, "Electrical-Power": 0.4}),
("Park ranger protecting natural reserves", {"Physical-Skill": 0.9, "Environmental-Sci": 0.4}),
("Professional athlete competing nationally", {"Physical-Skill": 0.9, "Sports-Ed": 0.5}),
("Underwater diver for inspection or research", {"Physical-Skill": 1.0, "Maritime-Sea": 0.4})], ["physical"]),
("What physical endurance challenge would you take on?", {"Physical-Skill": 0.9}, [
("Marathon or long-distance running event", {"Physical-Skill": 1.0, "Sports-Ed": 0.3}),
("Mountain climbing expedition (Mt. Apo, Mt. Pulag)", {"Physical-Skill": 0.9, "Field-Research": 0.3}),
("Ocean swimming or open water competition", {"Physical-Skill": 0.9, "Maritime-Sea": 0.3}),
("Military-style obstacle course challenge", {"Physical-Skill": 1.0, "Law-Enforce": 0.3}),
("Multi-sport triathlon or adventure race", {"Physical-Skill": 0.9, "Sports-Ed": 0.4}),
("Week-long wilderness survival experience", {"Physical-Skill": 0.9, "Field-Research": 0.4})], ["physical"]),
]
for t, qt, o, br in phy: ALL.append(nq(t, qt, o, br))

# Cloud-Systems (was 7) - 5 questions
cld = [
("What cloud computing task interests you?", {"Cloud-Systems": 0.9}, [
("Setting up virtual servers and infrastructure", {"Cloud-Systems": 1.0, "Technical-Skill": 0.4}),
("Container orchestration with Kubernetes", {"Cloud-Systems": 0.9, "Software-Dev": 0.4}),
("Cloud database management and optimization", {"Cloud-Systems": 0.9, "Data-Analytics": 0.3}),
("CDN and load balancer configuration", {"Cloud-Systems": 1.0, "Web-Dev": 0.3}),
("Serverless function development (AWS Lambda)", {"Cloud-Systems": 0.9, "Software-Dev": 0.4}),
("Cloud cost optimization and billing management", {"Cloud-Systems": 0.9, "Finance-Acct": 0.3})], ["technology"]),
("What cloud platform would you specialize in?", {"Cloud-Systems": 0.9, "Technical-Skill": 0.3}, [
("Amazon Web Services (AWS) ecosystem", {"Cloud-Systems": 1.0, "Software-Dev": 0.3}),
("Microsoft Azure cloud services", {"Cloud-Systems": 0.9, "Software-Dev": 0.3}),
("Google Cloud Platform (GCP)", {"Cloud-Systems": 0.9, "Data-Analytics": 0.4}),
("DigitalOcean for simple deployments", {"Cloud-Systems": 0.9, "Web-Dev": 0.3}),
("Hybrid cloud with on-premise integration", {"Cloud-Systems": 1.0, "Hardware-Systems": 0.3}),
("Multi-cloud strategy and management", {"Cloud-Systems": 0.9, "Admin-Skill": 0.3})], ["technology"]),
("What DevOps practice excites you?", {"Cloud-Systems": 0.9, "Software-Dev": 0.3}, [
("CI/CD pipelines for automated deployment", {"Cloud-Systems": 1.0, "Software-Dev": 0.4}),
("Infrastructure as Code using Terraform", {"Cloud-Systems": 0.9, "Software-Dev": 0.4}),
("Monitoring and alerting with Prometheus/Grafana", {"Cloud-Systems": 0.9, "Data-Analytics": 0.3}),
("Log management and analysis (ELK stack)", {"Cloud-Systems": 0.9, "Data-Analytics": 0.4}),
("Automated testing and deployment validation", {"Cloud-Systems": 1.0, "Software-Dev": 0.4}),
("Site reliability engineering (SRE) practices", {"Cloud-Systems": 0.9, "Analytical-Skill": 0.3})], ["technology"]),
("What cloud architecture challenge would you solve?", {"Cloud-Systems": 0.9}, [
("Scaling a Filipino app to millions of users", {"Cloud-Systems": 1.0, "Mobile-Dev": 0.3}),
("Ensuring 99.99% uptime for critical systems", {"Cloud-Systems": 0.9, "Analytical-Skill": 0.3}),
("Designing disaster recovery across regions", {"Cloud-Systems": 0.9, "Cyber-Defense": 0.3}),
("Migrating legacy systems to the cloud", {"Cloud-Systems": 1.0, "Software-Dev": 0.3}),
("Optimizing cloud spending for a startup", {"Cloud-Systems": 0.9, "Finance-Acct": 0.3}),
("Building microservices architecture", {"Cloud-Systems": 0.9, "Software-Dev": 0.5})], ["technology"]),
("What cloud security concern interests you most?", {"Cloud-Systems": 0.9, "Cyber-Defense": 0.3}, [
("Identity and access management (IAM)", {"Cloud-Systems": 1.0, "Cyber-Defense": 0.4}),
("Data encryption at rest and in transit", {"Cloud-Systems": 0.9, "Cyber-Defense": 0.5}),
("Network security groups and firewalls", {"Cloud-Systems": 0.9, "Cyber-Defense": 0.4}),
("Compliance and regulatory requirements", {"Cloud-Systems": 0.9, "Legal-Practice": 0.3}),
("Container security scanning", {"Cloud-Systems": 1.0, "Software-Dev": 0.3}),
("Secrets management and key rotation", {"Cloud-Systems": 0.9, "Cyber-Defense": 0.4})], ["technology"]),
]
for t, qt, o, br in cld: ALL.append(nq(t, qt, o, br))

# Software-Dev (was 9) - 3 questions
swd = [
("What software development methodology interests you?", {"Software-Dev": 0.9}, [
("Agile Scrum with sprints and stand-ups", {"Software-Dev": 1.0, "Admin-Skill": 0.3}),
("Test-driven development writing tests first", {"Software-Dev": 0.9, "Analytical-Skill": 0.4}),
("Pair programming and code review culture", {"Software-Dev": 0.9, "People-Skill": 0.3}),
("DevOps continuous integration and delivery", {"Software-Dev": 0.9, "Cloud-Systems": 0.4}),
("Open source contribution and community", {"Software-Dev": 1.0, "Community-Serve": 0.3}),
("Clean code and refactoring practices", {"Software-Dev": 0.9, "Analytical-Skill": 0.3})], ["technology"]),
("What type of software would you build?", {"Software-Dev": 0.9}, [
("Enterprise management system for companies", {"Software-Dev": 1.0, "Admin-Skill": 0.3}),
("Healthcare information system for hospitals", {"Software-Dev": 0.9, "Health-Admin": 0.4}),
("Educational platform for Filipino students", {"Software-Dev": 0.9, "Teaching-Ed": 0.3}),
("Financial transaction processing system", {"Software-Dev": 0.9, "Finance-Acct": 0.4}),
("Social media or communication app", {"Software-Dev": 0.9, "Digital-Media": 0.3}),
("Automation tools to reduce manual work", {"Software-Dev": 1.0, "Industrial-Ops": 0.3})], ["technology"]),
("What programming challenge excites you?", {"Software-Dev": 0.9}, [
("Algorithm optimization for speed", {"Software-Dev": 1.0, "Analytical-Skill": 0.5}),
("Integrating multiple APIs into one platform", {"Software-Dev": 0.9, "Web-Dev": 0.4}),
("Building real-time collaborative features", {"Software-Dev": 0.9, "Web-Dev": 0.3}),
("Database design and query optimisation", {"Software-Dev": 0.9, "Data-Analytics": 0.3}),
("Version control and branching strategies", {"Software-Dev": 1.0, "Cloud-Systems": 0.3}),
("Debugging and fixing complex legacy code", {"Software-Dev": 0.9, "Analytical-Skill": 0.4})], ["technology"]),
]
for t, qt, o, br in swd: ALL.append(nq(t, qt, o, br))

# Hardware-Systems (was 7) - 5 questions
hws = [
("What hardware project would you build?", {"Hardware-Systems": 0.9}, [
("Custom PC build for gaming or work", {"Hardware-Systems": 1.0, "Technical-Skill": 0.4}),
("IoT sensor network for monitoring", {"Hardware-Systems": 0.9, "Software-Dev": 0.3}),
("Arduino or Raspberry Pi automation project", {"Hardware-Systems": 0.9, "Software-Dev": 0.4}),
("Home server and network attached storage", {"Hardware-Systems": 0.9, "Cloud-Systems": 0.3}),
("RC drone or robot assembly", {"Hardware-Systems": 1.0, "Mechanical-Design": 0.3}),
("Solar-powered charging station", {"Hardware-Systems": 0.9, "Electrical-Power": 0.4})], ["technology"]),
("What computer hardware component interests you most?", {"Hardware-Systems": 0.9}, [
("CPU architecture and processor design", {"Hardware-Systems": 1.0, "Analytical-Skill": 0.3}),
("GPU and graphics card technology", {"Hardware-Systems": 0.9, "Game-Dev": 0.3}),
("SSD and storage technology advancement", {"Hardware-Systems": 0.9, "Data-Analytics": 0.3}),
("Network switches and router configuration", {"Hardware-Systems": 0.9, "Cloud-Systems": 0.4}),
("RAM and memory management hardware", {"Hardware-Systems": 1.0, "Technical-Skill": 0.3}),
("Motherboard and chipset compatibility", {"Hardware-Systems": 0.9, "Technical-Skill": 0.4})], ["technology"]),
("What hardware troubleshooting do you enjoy?", {"Hardware-Systems": 0.9}, [
("Diagnosing boot failures and blue screens", {"Hardware-Systems": 1.0, "Analytical-Skill": 0.4}),
("Replacing laptop screens and keyboards", {"Hardware-Systems": 0.9, "Physical-Skill": 0.3}),
("Resolving overheating and cooling issues", {"Hardware-Systems": 0.9, "Mechanical-Design": 0.3}),
("Recovering data from damaged drives", {"Hardware-Systems": 0.9, "Data-Analytics": 0.3}),
("Cable management and signal integrity", {"Hardware-Systems": 1.0, "Electrical-Power": 0.3}),
("Network latency and connectivity debugging", {"Hardware-Systems": 0.9, "Cloud-Systems": 0.4})], ["technology"]),
("What embedded systems application interests you?", {"Hardware-Systems": 0.9, "Software-Dev": 0.3}, [
("Smart agriculture sensors and controllers", {"Hardware-Systems": 0.9, "Agri-Nature": 0.4}),
("Medical device embedded firmware", {"Hardware-Systems": 0.9, "Medical-Lab": 0.3}),
("Automotive electronics and ECU programming", {"Hardware-Systems": 1.0, "Mechanical-Design": 0.3}),
("Wearable fitness tracker design", {"Hardware-Systems": 0.9, "Sports-Ed": 0.3}),
("Home automation and smart lighting", {"Hardware-Systems": 0.9, "Electrical-Power": 0.4}),
("Security camera and alarm system module", {"Hardware-Systems": 1.0, "Cyber-Defense": 0.3})], ["technology", "engineering"]),
("What hardware certification would you pursue?", {"Hardware-Systems": 0.9}, [
("CompTIA A+ hardware and troubleshooting", {"Hardware-Systems": 1.0, "Technical-Skill": 0.5}),
("Cisco CCNA for network hardware", {"Hardware-Systems": 0.9, "Cloud-Systems": 0.4}),
("CompTIA Server+ for server administration", {"Hardware-Systems": 0.9, "Cloud-Systems": 0.3}),
("AWS IoT certification", {"Hardware-Systems": 0.9, "Software-Dev": 0.3}),
("BICSI cabling and infrastructure", {"Hardware-Systems": 1.0, "Electrical-Power": 0.3}),
("Certified Electronics Technician (CET)", {"Hardware-Systems": 0.9, "Electrical-Power": 0.4})], ["technology"]),
]
for t, qt, o, br in hws: ALL.append(nq(t, qt, o, br))

# Remaining under-10 traits need 3-5 questions each
# Animation-3D (was 6) - 4
anim = [
("What animation production pipeline stage interests you?", {"Animation-3D": 0.9}, [
("Storyboarding and pre-visualization", {"Animation-3D": 1.0, "Film-Broadcast": 0.3}),
("3D modeling and texturing assets", {"Animation-3D": 0.9, "Visual-Design": 0.4}),
("Character rigging and joint setup", {"Animation-3D": 1.0, "Technical-Skill": 0.4}),
("Animation timing and movement polish", {"Animation-3D": 0.9, "Creative-Skill": 0.4}),
("Lighting and rendering the final scene", {"Animation-3D": 0.9, "Visual-Design": 0.3}),
("Compositing and post-production effects", {"Animation-3D": 0.9, "Film-Broadcast": 0.4})], ["creative"]),
("What Philippine animation opportunity excites you?", {"Animation-3D": 0.9}, [
("Working in Manila's growing animation studios", {"Animation-3D": 1.0, "Film-Broadcast": 0.3}),
("Outsourced animation for Hollywood projects", {"Animation-3D": 0.9, "Film-Broadcast": 0.4}),
("Creating Filipino animated characters/shows", {"Animation-3D": 0.9, "Creative-Skill": 0.5}),
("Game asset creation for international studios", {"Animation-3D": 0.9, "Game-Dev": 0.5}),
("AR/VR content creation for tech companies", {"Animation-3D": 1.0, "Software-Dev": 0.3}),
("Freelance motion graphics for ads", {"Animation-3D": 0.9, "Marketing-Sales": 0.3})], ["creative"]),
("What animation technique would you perfect?", {"Animation-3D": 0.9}, [
("Walk cycle and character locomotion", {"Animation-3D": 1.0, "Creative-Skill": 0.3}),
("Facial animation and lip sync", {"Animation-3D": 0.9, "Performing-Arts": 0.3}),
("Particle effects: fire, water, smoke", {"Animation-3D": 1.0, "Technical-Skill": 0.3}),
("Camera animation and cinematic shots", {"Animation-3D": 0.9, "Film-Broadcast": 0.4}),
("Cloth and hair simulation physics", {"Animation-3D": 0.9, "Technical-Skill": 0.4}),
("Procedural animation and scripting", {"Animation-3D": 0.9, "Software-Dev": 0.4})], ["creative"]),
("What animated content do you watch and admire?", {"Animation-3D": 0.9}, [
("Pixar and Disney feature film quality", {"Animation-3D": 1.0, "Film-Broadcast": 0.4}),
("Japanese anime art style and storytelling", {"Animation-3D": 0.9, "Creative-Skill": 0.4}),
("Motion graphics in commercials and explainers", {"Animation-3D": 0.9, "Marketing-Sales": 0.3}),
("Game cinematics and real-time cutscenes", {"Animation-3D": 0.9, "Game-Dev": 0.5}),
("Independent and experimental animation", {"Animation-3D": 0.9, "Creative-Skill": 0.5}),
("Architectural and product visualization", {"Animation-3D": 1.0, "Spatial-Design": 0.3})], ["creative"]),
]
for t, qt, o, br in anim: ALL.append(nq(t, qt, o, br))

# Community-Serve (was 5) - 4
com = [
("What Filipino community issue would you address?", {"Community-Serve": 0.9}, [
("Poverty and hunger in urban poor areas", {"Community-Serve": 1.0, "Social-Work": 0.5}),
("Lack of access to quality education", {"Community-Serve": 0.9, "Teaching-Ed": 0.5}),
("Environmental pollution in waterways", {"Community-Serve": 0.9, "Environmental-Sci": 0.4}),
("Drug abuse prevention programs for youth", {"Community-Serve": 0.9, "Counseling": 0.4}),
("Senior citizen welfare and care programs", {"Community-Serve": 0.9, "Patient-Care": 0.3}),
("Disaster preparedness in typhoon-prone areas", {"Community-Serve": 1.0, "Environmental-Eng": 0.3})], ["public_service"]),
("What volunteer role would you take?", {"Community-Serve": 0.9}, [
("Teaching computer literacy to barangay residents", {"Community-Serve": 1.0, "Teaching-Ed": 0.4}),
("Organizing feeding programs for malnourished kids", {"Community-Serve": 0.9, "Nutrition-Diet": 0.4}),
("Medical mission volunteer in remote areas", {"Community-Serve": 0.9, "Patient-Care": 0.5}),
("Tree planting and mangrove restoration", {"Community-Serve": 0.9, "Environmental-Sci": 0.5}),
("Habitat building for families in need", {"Community-Serve": 0.9, "Civil-Build": 0.3}),
("Legal aid for indigent community members", {"Community-Serve": 1.0, "Legal-Practice": 0.4})], ["public_service", "social"]),
("What community empowerment approach would you use?", {"Community-Serve": 0.9}, [
("Skills training for livelihood generation", {"Community-Serve": 1.0, "Teaching-Ed": 0.4}),
("Cooperative formation for economic growth", {"Community-Serve": 0.9, "Finance-Acct": 0.3}),
("Youth leadership and civic engagement", {"Community-Serve": 0.9, "People-Skill": 0.5}),
("Health education and disease prevention", {"Community-Serve": 0.9, "Public-Health": 0.4}),
("Cultural preservation and heritage programs", {"Community-Serve": 0.9, "Tourism-Travel": 0.3}),
("Technology access and digital literacy", {"Community-Serve": 1.0, "Technical-Skill": 0.3})], ["public_service"]),
("What community organizing strategy would you lead?", {"Community-Serve": 0.9}, [
("Door-to-door outreach and needs assessment", {"Community-Serve": 1.0, "People-Skill": 0.5}),
("Social media campaigns for local causes", {"Community-Serve": 0.9, "Digital-Media": 0.3}),
("Barangay assembly and community meetings", {"Community-Serve": 0.9, "People-Skill": 0.4}),
("Partnership with local government units", {"Community-Serve": 0.9, "Legal-Practice": 0.3}),
("Fundraising events and donation drives", {"Community-Serve": 1.0, "Marketing-Sales": 0.3}),
("Mentoring and coaching community leaders", {"Community-Serve": 0.9, "Teaching-Ed": 0.4})], ["public_service", "social"]),
]
for t, qt, o, br in com: ALL.append(nq(t, qt, o, br))

# Digital-Media (was 5) - 4
dm = [
("What digital content creation process excites you?", {"Digital-Media": 0.9}, [
("Filming and editing vlogs and tutorials", {"Digital-Media": 1.0, "Film-Broadcast": 0.4}),
("Designing social media graphics and carousels", {"Digital-Media": 0.9, "Visual-Design": 0.5}),
("Writing scripts and captions for posts", {"Digital-Media": 0.9, "Creative-Skill": 0.4}),
("Recording and editing podcast episodes", {"Digital-Media": 1.0, "Performing-Arts": 0.3}),
("Creating reels and short-form video content", {"Digital-Media": 0.9, "Film-Broadcast": 0.3}),
("Managing and growing online communities", {"Digital-Media": 0.9, "People-Skill": 0.4})], ["creative"]),
("What digital media metric matters most to you?", {"Digital-Media": 0.9, "Data-Analytics": 0.3}, [
("Follower growth and audience building", {"Digital-Media": 1.0, "Marketing-Sales": 0.4}),
("Engagement rate and comments quality", {"Digital-Media": 0.9, "People-Skill": 0.3}),
("Video views and watch time", {"Digital-Media": 0.9, "Film-Broadcast": 0.3}),
("Click-through rate and traffic to website", {"Digital-Media": 0.9, "Web-Dev": 0.3}),
("Revenue and monetization from content", {"Digital-Media": 0.9, "Finance-Acct": 0.3}),
("Social impact and awareness created", {"Digital-Media": 1.0, "Community-Serve": 0.3})], ["creative"]),
("What content niche would you build?", {"Digital-Media": 0.9}, [
("Tech reviews and gadget unboxing", {"Digital-Media": 1.0, "Hardware-Systems": 0.3}),
("Travel and food vlogging across Philippines", {"Digital-Media": 0.9, "Tourism-Travel": 0.4}),
("Educational content and study tips", {"Digital-Media": 0.9, "Teaching-Ed": 0.4}),
("Fitness and wellness lifestyle content", {"Digital-Media": 0.9, "Sports-Ed": 0.3}),
("Art and creative process behind-the-scenes", {"Digital-Media": 0.9, "Visual-Design": 0.4}),
("Comedy sketches and entertainment", {"Digital-Media": 1.0, "Performing-Arts": 0.4})], ["creative"]),
("What digital media business model appeals to you?", {"Digital-Media": 0.9, "Startup-Venture": 0.3}, [
("YouTube ad revenue and brand sponsorships", {"Digital-Media": 1.0, "Finance-Acct": 0.3}),
("Freelance content creation agency", {"Digital-Media": 0.9, "Startup-Venture": 0.4}),
("Online course and membership platform", {"Digital-Media": 0.9, "Teaching-Ed": 0.4}),
("Print-on-demand and merchandise sales", {"Digital-Media": 0.9, "Marketing-Sales": 0.3}),
("Newsletter and premium content subscription", {"Digital-Media": 0.9, "Creative-Skill": 0.3}),
("Social media management for brands", {"Digital-Media": 1.0, "Marketing-Sales": 0.4})], ["creative", "business"]),
]
for t, qt, o, br in dm: ALL.append(nq(t, qt, o, br))

# Electrical-Power (was 6) - 4
elp = [
("What electrical system would you design?", {"Electrical-Power": 0.9}, [
("Solar farm power generation system", {"Electrical-Power": 1.0, "Environmental-Eng": 0.4}),
("Industrial factory power distribution", {"Electrical-Power": 0.9, "Industrial-Ops": 0.4}),
("Hospital emergency backup power system", {"Electrical-Power": 0.9, "Health-Admin": 0.3}),
("Data center uninterruptible power supply", {"Electrical-Power": 0.9, "Cloud-Systems": 0.3}),
("Residential electrical panel and circuitry", {"Electrical-Power": 1.0, "Civil-Build": 0.3}),
("Streetlight and public lighting automation", {"Electrical-Power": 0.9, "Community-Serve": 0.3})], ["engineering"]),
("What electrical safety practice interests you?", {"Electrical-Power": 0.9}, [
("Lockout/tagout procedures for maintenance", {"Electrical-Power": 1.0, "Industrial-Ops": 0.3}),
("Grounding and earthing system design", {"Electrical-Power": 0.9, "Civil-Build": 0.3}),
("Arc flash hazard analysis and prevention", {"Electrical-Power": 1.0, "Analytical-Skill": 0.3}),
("Philippine Electrical Code compliance", {"Electrical-Power": 0.9, "Legal-Practice": 0.3}),
("Surge protection and lightning design", {"Electrical-Power": 0.9, "Environmental-Sci": 0.3}),
("Electrical fire investigation and prevention", {"Electrical-Power": 0.9, "Forensic-Sci": 0.3})], ["engineering"]),
("What electrical innovation excites you?", {"Electrical-Power": 0.9}, [
("Wireless power transfer technology", {"Electrical-Power": 1.0, "Technical-Skill": 0.4}),
("Microgrids for island communities", {"Electrical-Power": 0.9, "Community-Serve": 0.4}),
("Smart meters and IoT energy monitoring", {"Electrical-Power": 0.9, "Hardware-Systems": 0.4}),
("High-voltage direct current (HVDC) transmission", {"Electrical-Power": 1.0, "Analytical-Skill": 0.3}),
("Battery management systems for EVs", {"Electrical-Power": 0.9, "Mechanical-Design": 0.3}),
("Power electronics and inverter design", {"Electrical-Power": 0.9, "Hardware-Systems": 0.3})], ["engineering", "technology"]),
("What power engineering role would you pursue?", {"Electrical-Power": 0.9}, [
("Licensed Professional Electrical Engineer", {"Electrical-Power": 1.0, "Technical-Skill": 0.3}),
("Substation and transmission line engineer", {"Electrical-Power": 0.9, "Civil-Build": 0.3}),
("Control systems engineer in a power plant", {"Electrical-Power": 0.9, "Industrial-Ops": 0.4}),
("Energy auditor for buildings and factories", {"Electrical-Power": 0.9, "Environmental-Eng": 0.3}),
("Renewable energy project manager", {"Electrical-Power": 0.9, "Admin-Skill": 0.3}),
("Electrical estimator and project bidder", {"Electrical-Power": 1.0, "Finance-Acct": 0.3})], ["engineering"]),
]
for t, qt, o, br in elp: ALL.append(nq(t, qt, o, br))

# Environmental-Eng (was 6), Env-Sci (was 4), Field-Research (was 5), Film-Broadcast (was 4)
# Combine small adds
misc1 = [
# Environmental-Eng +4
("What pollution control technology interests you?", {"Environmental-Eng": 0.9}, [
("Activated sludge process for sewage treatment", {"Environmental-Eng": 1.0, "Lab-Research": 0.3}),
("Electrostatic precipitators for factory emissions", {"Environmental-Eng": 0.9, "Electrical-Power": 0.3}),
("Reverse osmosis desalination plants", {"Environmental-Eng": 0.9, "Technical-Skill": 0.4}),
("Biogas capture from organic waste", {"Environmental-Eng": 1.0, "Agri-Nature": 0.3}),
("Noise pollution barriers and engineering", {"Environmental-Eng": 0.9, "Civil-Build": 0.4}),
("Hazardous waste containment and disposal", {"Environmental-Eng": 0.9, "Lab-Research": 0.4})], ["engineering"]),
("What environmental compliance task appeals to you?", {"Environmental-Eng": 0.9}, [
("Writing environmental management plans", {"Environmental-Eng": 1.0, "Admin-Skill": 0.3}),
("Conducting environmental monitoring sampling", {"Environmental-Eng": 0.9, "Field-Research": 0.4}),
("Calculating carbon emissions and offsets", {"Environmental-Eng": 0.9, "Data-Analytics": 0.4}),
("Reviewing EIA documents for DENR submission", {"Environmental-Eng": 1.0, "Legal-Practice": 0.3}),
("Designing stormwater management systems", {"Environmental-Eng": 0.9, "Civil-Build": 0.4}),
("Implementing ISO 14001 environmental standards", {"Environmental-Eng": 0.9, "Industrial-Ops": 0.3})], ["engineering"]),
("What environmental engineering innovation interests you?", {"Environmental-Eng": 0.9}, [
("Plastic-to-fuel pyrolysis technology", {"Environmental-Eng": 1.0, "Lab-Research": 0.3}),
("Vertical farming and controlled environment agriculture", {"Environmental-Eng": 0.9, "Agri-Nature": 0.4}),
("Atmospheric water generators for arid areas", {"Environmental-Eng": 0.9, "Mechanical-Design": 0.3}),
("Ocean plastic cleanup technology", {"Environmental-Eng": 1.0, "Maritime-Sea": 0.3}),
("Carbon capture and storage systems", {"Environmental-Eng": 0.9, "Lab-Research": 0.3}),
("Smart waste sorting using AI vision", {"Environmental-Eng": 0.9, "AI-ML": 0.4})], ["engineering", "technology"]),
("What environmental project would you manage?", {"Environmental-Eng": 0.9}, [
("Municipal sewage treatment plant upgrade", {"Environmental-Eng": 1.0, "Civil-Build": 0.4}),
("Factory air quality improvement project", {"Environmental-Eng": 0.9, "Industrial-Ops": 0.4}),
("River rehabilitation and cleanup program", {"Environmental-Eng": 0.9, "Community-Serve": 0.3}),
("Green building certification project", {"Environmental-Eng": 0.9, "Spatial-Design": 0.3}),
("Renewable energy feasibility study", {"Environmental-Eng": 1.0, "Electrical-Power": 0.3}),
("Solid waste reduction plan for a city", {"Environmental-Eng": 0.9, "Admin-Skill": 0.3})], ["engineering"]),
# Environmental-Sci +4
("What Philippine ecosystem would you study?", {"Environmental-Sci": 0.9}, [
("Coral reef systems of Tubbataha", {"Environmental-Sci": 1.0, "Maritime-Sea": 0.4}),
("Mangrove forests along coastlines", {"Environmental-Sci": 0.9, "Maritime-Sea": 0.3}),
("Rainforest canopy in Sierra Madre", {"Environmental-Sci": 0.9, "Field-Research": 0.5}),
("Freshwater lake ecosystems like Laguna de Bay", {"Environmental-Sci": 1.0, "Field-Research": 0.3}),
("Volcanic soil ecosystems near Mt. Pinatubo", {"Environmental-Sci": 0.9, "Field-Research": 0.4}),
("Urban ecosystems in Metro Manila", {"Environmental-Sci": 0.9, "Community-Serve": 0.3})], ["science"]),
("What environmental data would you collect?", {"Environmental-Sci": 0.9, "Data-Analytics": 0.3}, [
("Air quality index measurements", {"Environmental-Sci": 1.0, "Lab-Research": 0.3}),
("Water pH and dissolved oxygen levels", {"Environmental-Sci": 0.9, "Lab-Research": 0.4}),
("Species population and biodiversity counts", {"Environmental-Sci": 0.9, "Field-Research": 0.5}),
("Soil composition and contaminant levels", {"Environmental-Sci": 1.0, "Lab-Research": 0.4}),
("Weather patterns and climate trends", {"Environmental-Sci": 0.9, "Data-Analytics": 0.4}),
("Noise and light pollution measurements", {"Environmental-Sci": 0.9, "Technical-Skill": 0.3})], ["science"]),
("What environmental policy issue concerns you?", {"Environmental-Sci": 0.9}, [
("Deforestation and illegal logging", {"Environmental-Sci": 1.0, "Law-Enforce": 0.3}),
("Plastic pollution in Philippine oceans", {"Environmental-Sci": 0.9, "Maritime-Sea": 0.3}),
("Air pollution from vehicles and factories", {"Environmental-Sci": 0.9, "Environmental-Eng": 0.3}),
("Loss of endemic Philippine species", {"Environmental-Sci": 1.0, "Field-Research": 0.3}),
("Mining damage to mountain ecosystems", {"Environmental-Sci": 0.9, "Legal-Practice": 0.3}),
("Sea level rise threatening coastal communities", {"Environmental-Sci": 0.9, "Community-Serve": 0.3})], ["science"]),
("What environmental conservation method would you support?", {"Environmental-Sci": 0.9}, [
("Marine protected areas and no-take zones", {"Environmental-Sci": 1.0, "Maritime-Sea": 0.3}),
("Reforestation and native tree planting", {"Environmental-Sci": 0.9, "Agri-Nature": 0.3}),
("Wildlife rescue and rehabilitation centers", {"Environmental-Sci": 0.9, "Patient-Care": 0.2}),
("Community-based ecosystem management", {"Environmental-Sci": 0.9, "Community-Serve": 0.5}),
("Ecotourism as conservation incentive", {"Environmental-Sci": 0.9, "Tourism-Travel": 0.4}),
("Scientific breeding programs for rare species", {"Environmental-Sci": 1.0, "Lab-Research": 0.4})], ["science"]),
# Field-Research +4
("What field data collection technology would you use?", {"Field-Research": 0.9}, [
("GIS mapping with ArcGIS or QGIS software", {"Field-Research": 1.0, "Data-Analytics": 0.4}),
("Drone photography for terrain mapping", {"Field-Research": 0.9, "Technical-Skill": 0.5}),
("GPS tracking collars for wildlife", {"Field-Research": 0.9, "Environmental-Sci": 0.4}),
("Mobile data collection apps (KoBoToolbox)", {"Field-Research": 0.9, "Software-Dev": 0.3}),
("Camera traps for nocturnal wildlife", {"Field-Research": 1.0, "Environmental-Sci": 0.3}),
("Underwater acoustic monitoring devices", {"Field-Research": 0.9, "Maritime-Sea": 0.4})], ["science"]),
("What type of field survey would you conduct?", {"Field-Research": 0.9}, [
("Forest plot inventory and tree measurement", {"Field-Research": 1.0, "Environmental-Sci": 0.4}),
("Bird counting and migration tracking", {"Field-Research": 0.9, "Environmental-Sci": 0.5}),
("Community health baseline survey", {"Field-Research": 0.9, "Public-Health": 0.5}),
("Soil erosion and land degradation assessment", {"Field-Research": 0.9, "Environmental-Eng": 0.3}),
("Archaeological site excavation", {"Field-Research": 1.0, "Creative-Skill": 0.2}),
("Marine invertebrate diversity transect", {"Field-Research": 0.9, "Maritime-Sea": 0.4})], ["science"]),
("What motivates you about field work?", {"Field-Research": 0.9}, [
("Working outdoors instead of in an office", {"Field-Research": 1.0, "Physical-Skill": 0.4}),
("Discovering new species or habitats", {"Field-Research": 0.9, "Environmental-Sci": 0.5}),
("Interacting with local and indigenous communities", {"Field-Research": 0.9, "People-Skill": 0.4}),
("The adventure and unpredictability of fieldwork", {"Field-Research": 0.9, "Physical-Skill": 0.3}),
("Collecting data that directly helps conservation", {"Field-Research": 1.0, "Environmental-Sci": 0.3}),
("Training local volunteers in research methods", {"Field-Research": 0.9, "Teaching-Ed": 0.4})], ["science"]),
("What field research challenge would you overcome?", {"Field-Research": 0.9}, [
("Working in extreme weather conditions", {"Field-Research": 1.0, "Physical-Skill": 0.5}),
("Reaching very remote and inaccessible areas", {"Field-Research": 0.9, "Physical-Skill": 0.4}),
("Getting community permission and cooperation", {"Field-Research": 0.9, "People-Skill": 0.5}),
("Maintaining equipment in harsh environments", {"Field-Research": 0.9, "Technical-Skill": 0.4}),
("Processing large volumes of field data quickly", {"Field-Research": 1.0, "Data-Analytics": 0.4}),
("Working safely with dangerous wildlife", {"Field-Research": 0.9, "Environmental-Sci": 0.3})], ["science"]),
# Film-Broadcast +4
("What film production stage excites you most?", {"Film-Broadcast": 0.9}, [
("Pre-production: scripting and location scouting", {"Film-Broadcast": 1.0, "Creative-Skill": 0.4}),
("Production: directing actors on set", {"Film-Broadcast": 0.9, "People-Skill": 0.4}),
("Post-production: editing and color grading", {"Film-Broadcast": 0.9, "Digital-Media": 0.4}),
("Sound design and music scoring", {"Film-Broadcast": 0.9, "Performing-Arts": 0.4}),
("Distribution and film festival submission", {"Film-Broadcast": 1.0, "Marketing-Sales": 0.3}),
("VFX and CGI integration", {"Film-Broadcast": 0.9, "Animation-3D": 0.5})], ["creative"]),
("What broadcast technology would you operate?", {"Film-Broadcast": 0.9, "Technical-Skill": 0.3}, [
("Professional cinema cameras (RED, ARRI)", {"Film-Broadcast": 1.0, "Technical-Skill": 0.4}),
("Live broadcast switchers and control rooms", {"Film-Broadcast": 0.9, "Technical-Skill": 0.5}),
("Studio lighting rigs and grip equipment", {"Film-Broadcast": 0.9, "Physical-Skill": 0.3}),
("Teleprompter and live feed management", {"Film-Broadcast": 0.9, "Admin-Skill": 0.3}),
("Drone cameras for aerial cinematography", {"Film-Broadcast": 1.0, "Technical-Skill": 0.4}),
("Live streaming encoder and setup", {"Film-Broadcast": 0.9, "Digital-Media": 0.4})], ["creative", "technology"]),
("What kind of Filipino story would you tell through film?", {"Film-Broadcast": 0.9}, [
("OFW experience and family sacrifice", {"Film-Broadcast": 1.0, "Social-Work": 0.3}),
("Filipino heroism and historical events", {"Film-Broadcast": 0.9, "Teaching-Ed": 0.3}),
("Urban poverty and social inequality", {"Film-Broadcast": 0.9, "Community-Serve": 0.3}),
("Philippine natural beauty and travel", {"Film-Broadcast": 0.9, "Tourism-Travel": 0.4}),
("Coming-of-age story of a Filipino youth", {"Film-Broadcast": 1.0, "Community-Serve": 0.3}),
("Science fiction set in future Philippines", {"Film-Broadcast": 0.9, "Creative-Skill": 0.5})], ["creative"]),
("What film/media industry role would you take?", {"Film-Broadcast": 0.9}, [
("TV or film production assistant", {"Film-Broadcast": 1.0, "Admin-Skill": 0.3}),
("Freelance videographer for events and weddings", {"Film-Broadcast": 0.9, "Hospitality-Svc": 0.3}),
("News cameraman covering current events", {"Film-Broadcast": 0.9, "Community-Serve": 0.3}),
("Music video director", {"Film-Broadcast": 0.9, "Performing-Arts": 0.4}),
("Documentary filmmaker for social causes", {"Film-Broadcast": 1.0, "Social-Work": 0.3}),
("Film editor for a post-production house", {"Film-Broadcast": 0.9, "Technical-Skill": 0.4})], ["creative"]),
]
for t, qt, o, br in misc1: ALL.append(nq(t, qt, o, br))

# Food-Science (was 8) - 4
fs = [
("What food testing method interests you?", {"Food-Science": 0.9}, [
("Microbiological testing for pathogens", {"Food-Science": 1.0, "Lab-Research": 0.5}),
("Proximate analysis for nutrient content", {"Food-Science": 0.9, "Nutrition-Diet": 0.4}),
("Shelf-life stability testing", {"Food-Science": 0.9, "Analytical-Skill": 0.3}),
("Food allergen detection and labeling", {"Food-Science": 0.9, "Lab-Research": 0.4}),
("Water activity and moisture measurement", {"Food-Science": 1.0, "Technical-Skill": 0.3}),
("Pesticide residue analysis in produce", {"Food-Science": 0.9, "Environmental-Sci": 0.3})], ["science"]),
("What food processing technology fascinates you?", {"Food-Science": 0.9}, [
("High-pressure processing for fresh foods", {"Food-Science": 1.0, "Technical-Skill": 0.4}),
("Freeze-drying for space and emergency food", {"Food-Science": 0.9, "Technical-Skill": 0.3}),
("Fermentation science for yogurt and tempeh", {"Food-Science": 0.9, "Lab-Research": 0.4}),
("Extrusion technology for snack production", {"Food-Science": 0.9, "Industrial-Ops": 0.4}),
("Pasteurization and sterilization methods", {"Food-Science": 1.0, "Lab-Research": 0.3}),
("Encapsulation of vitamins and probiotics", {"Food-Science": 0.9, "Pharmacy": 0.3})], ["science"]),
("What food quality challenge would you tackle?", {"Food-Science": 0.9, "Industrial-Ops": 0.3}, [
("Reducing food waste in supply chains", {"Food-Science": 1.0, "Industrial-Ops": 0.4}),
("Ensuring halal and organic food certification", {"Food-Science": 0.9, "Legal-Practice": 0.3}),
("Detecting food adulteration and fake products", {"Food-Science": 0.9, "Forensic-Sci": 0.3}),
("Extending shelf life of tropical fruits", {"Food-Science": 1.0, "Agri-Nature": 0.3}),
("Improving taste while reducing sugar and salt", {"Food-Science": 0.9, "Nutrition-Diet": 0.4}),
("Scaling artisanal food for mass production", {"Food-Science": 0.9, "Industrial-Ops": 0.4})], ["science"]),
("What food industry career appeals to you?", {"Food-Science": 0.9}, [
("Food researcher in a tech company lab", {"Food-Science": 1.0, "Lab-Research": 0.4}),
("Quality assurance manager in a food factory", {"Food-Science": 0.9, "Industrial-Ops": 0.5}),
("Food safety inspector for government (FDA)", {"Food-Science": 0.9, "Law-Enforce": 0.3}),
("Product developer for a snack company", {"Food-Science": 0.9, "Creative-Skill": 0.3}),
("Nutritionist consultant for food brands", {"Food-Science": 0.9, "Nutrition-Diet": 0.5}),
("Food technology professor and researcher", {"Food-Science": 1.0, "Teaching-Ed": 0.4})], ["science"]),
]
for t, qt, o, br in fs: ALL.append(nq(t, qt, o, br))

# Remaining traits: Hospitality-Svc(5), Industrial-Ops(7), Lab-Research(8), Marketing-Sales(5),
# Mechanical-Design(6), Nutrition-Diet(9), Performing-Arts(5), Spatial-Design(5),
# Startup-Venture(7), Teaching-Ed(5), Visual-Design(8)
misc2 = [
# Hospitality-Svc +4
("What guest experience would you create?", {"Hospitality-Svc": 0.9}, [
("Welcome package for first-time resort guests", {"Hospitality-Svc": 1.0, "Tourism-Travel": 0.3}),
("Personalized dining experience for anniversaries", {"Hospitality-Svc": 0.9, "Culinary-Arts": 0.4}),
("Guided city tour for corporate retreat groups", {"Hospitality-Svc": 0.9, "Tourism-Travel": 0.5}),
("Spa and wellness relaxation package", {"Hospitality-Svc": 0.9, "Rehab-Therapy": 0.3}),
("VIP lounge and priority service program", {"Hospitality-Svc": 1.0, "Admin-Skill": 0.3}),
("Cultural immersion program for foreign visitors", {"Hospitality-Svc": 0.9, "Community-Serve": 0.3})], ["hospitality"]),
("What hospitality management topic interests you?", {"Hospitality-Svc": 0.9, "Admin-Skill": 0.3}, [
("Hotel revenue management and yield pricing", {"Hospitality-Svc": 1.0, "Finance-Acct": 0.4}),
("Food and beverage cost control", {"Hospitality-Svc": 0.9, "Finance-Acct": 0.4}),
("Housekeeping operations and standards", {"Hospitality-Svc": 0.9, "Admin-Skill": 0.4}),
("Front desk operations and check-in systems", {"Hospitality-Svc": 1.0, "Technical-Skill": 0.3}),
("Guest satisfaction measurement and improvement", {"Hospitality-Svc": 0.9, "Data-Analytics": 0.3}),
("Sustainable hospitality and eco-friendly practices", {"Hospitality-Svc": 0.9, "Environmental-Sci": 0.3})], ["hospitality"]),
("What hospitality emergency would you handle well?", {"Hospitality-Svc": 0.9}, [
("Guest medical emergency at the hotel", {"Hospitality-Svc": 1.0, "Patient-Care": 0.3}),
("Overbooking situation during peak season", {"Hospitality-Svc": 0.9, "Analytical-Skill": 0.3}),
("VIP complaint about room or service quality", {"Hospitality-Svc": 0.9, "People-Skill": 0.5}),
("Natural disaster evacuation procedures", {"Hospitality-Svc": 0.9, "Community-Serve": 0.3}),
("Food safety incident in the restaurant", {"Hospitality-Svc": 0.9, "Food-Science": 0.4}),
("Security breach or theft in the property", {"Hospitality-Svc": 1.0, "Law-Enforce": 0.3})], ["hospitality"]),
("What hotel department would you manage?", {"Hospitality-Svc": 0.9}, [
("Rooms division and guest services", {"Hospitality-Svc": 1.0, "Admin-Skill": 0.4}),
("Food and beverage operations", {"Hospitality-Svc": 0.9, "Culinary-Arts": 0.4}),
("Sales and marketing department", {"Hospitality-Svc": 0.9, "Marketing-Sales": 0.4}),
("Engineering and facility maintenance", {"Hospitality-Svc": 0.9, "Technical-Skill": 0.3}),
("Human resources and employee training", {"Hospitality-Svc": 0.9, "HR-Management": 0.4}),
("Finance and accounting department", {"Hospitality-Svc": 1.0, "Finance-Acct": 0.3})], ["hospitality"]),
# Industrial-Ops +3
("What factory floor improvement would you make?", {"Industrial-Ops": 0.9}, [
("Reducing bottlenecks in the production line", {"Industrial-Ops": 1.0, "Analytical-Skill": 0.4}),
("Implementing automated quality checks", {"Industrial-Ops": 0.9, "Software-Dev": 0.3}),
("Optimizing raw material usage to reduce waste", {"Industrial-Ops": 0.9, "Environmental-Eng": 0.3}),
("Improving worker safety with better procedures", {"Industrial-Ops": 0.9, "Physical-Skill": 0.3}),
("Redesigning workflow for shorter cycle times", {"Industrial-Ops": 1.0, "Mechanical-Design": 0.3}),
("Installing IoT sensors for real-time monitoring", {"Industrial-Ops": 0.9, "Hardware-Systems": 0.3})], ["engineering"]),
("What industrial engineering tool would you apply?", {"Industrial-Ops": 0.9}, [
("Time and motion study for productivity", {"Industrial-Ops": 1.0, "Analytical-Skill": 0.5}),
("Pareto analysis for problem prioritization", {"Industrial-Ops": 0.9, "Data-Analytics": 0.4}),
("Kanban boards for workflow visualization", {"Industrial-Ops": 0.9, "Admin-Skill": 0.3}),
("Overall Equipment Effectiveness (OEE) tracking", {"Industrial-Ops": 1.0, "Data-Analytics": 0.3}),
("Failure Mode and Effects Analysis (FMEA)", {"Industrial-Ops": 0.9, "Analytical-Skill": 0.4}),
("Work sampling and ergonomic assessment", {"Industrial-Ops": 0.9, "Physical-Skill": 0.3})], ["engineering"]),
("What supply chain challenge would you solve?", {"Industrial-Ops": 0.9}, [
("Reducing delivery lead times for Philippine logistics", {"Industrial-Ops": 1.0, "Admin-Skill": 0.3}),
("Warehouse layout optimization for faster picking", {"Industrial-Ops": 0.9, "Spatial-Design": 0.3}),
("Inventory control to prevent stockouts", {"Industrial-Ops": 0.9, "Finance-Acct": 0.3}),
("Supplier quality evaluation and management", {"Industrial-Ops": 0.9, "Analytical-Skill": 0.4}),
("Cold chain management for perishable goods", {"Industrial-Ops": 1.0, "Food-Science": 0.3}),
("Last-mile delivery optimization with routing", {"Industrial-Ops": 0.9, "Data-Analytics": 0.4})], ["engineering", "business"]),
# Lab-Research +3
("What laboratory research breakthrough excites you?", {"Lab-Research": 0.9}, [
("CRISPR gene editing for disease treatment", {"Lab-Research": 1.0, "Medical-Lab": 0.4}),
("Novel drug discovery for tropical diseases", {"Lab-Research": 0.9, "Pharmacy": 0.5}),
("New materials with extraordinary properties", {"Lab-Research": 0.9, "Mechanical-Design": 0.3}),
("Stem cell research for regenerative medicine", {"Lab-Research": 1.0, "Patient-Care": 0.3}),
("Bioplastics and sustainable materials", {"Lab-Research": 0.9, "Environmental-Eng": 0.4}),
("Quantum computing hardware development", {"Lab-Research": 0.9, "Hardware-Systems": 0.3})], ["science"]),
("What lab research routine would you enjoy?", {"Lab-Research": 0.9}, [
("Preparing samples and running experiments daily", {"Lab-Research": 1.0, "Technical-Skill": 0.3}),
("Analyzing data and writing research papers", {"Lab-Research": 0.9, "Analytical-Skill": 0.5}),
("Calibrating and maintaining lab equipment", {"Lab-Research": 0.9, "Technical-Skill": 0.5}),
("Supervising lab assistants and interns", {"Lab-Research": 0.9, "People-Skill": 0.3}),
("Reading journals and planning new experiments", {"Lab-Research": 1.0, "Analytical-Skill": 0.3}),
("Presenting results at scientific conferences", {"Lab-Research": 0.9, "Performing-Arts": 0.2})], ["science"]),
("What lab safety practice is most important to you?", {"Lab-Research": 0.9}, [
("Proper chemical handling and storage", {"Lab-Research": 1.0, "Environmental-Eng": 0.3}),
("Wearing appropriate PPE at all times", {"Lab-Research": 0.9, "Physical-Skill": 0.3}),
("Managing biological hazard waste disposal", {"Lab-Research": 0.9, "Environmental-Eng": 0.3}),
("Fire safety and emergency shower locations", {"Lab-Research": 0.9, "Physical-Skill": 0.2}),
("Equipment lockout and electrical safety", {"Lab-Research": 1.0, "Electrical-Power": 0.3}),
("Accurate labeling and record keeping", {"Lab-Research": 0.9, "Admin-Skill": 0.4})], ["science"]),
# Marketing-Sales +4
("What marketing content would you create?", {"Marketing-Sales": 0.9}, [
("Compelling product descriptions and ad copy", {"Marketing-Sales": 1.0, "Creative-Skill": 0.4}),
("Marketing email campaigns and newsletters", {"Marketing-Sales": 0.9, "Digital-Media": 0.3}),
("Video advertisements for social media", {"Marketing-Sales": 0.9, "Film-Broadcast": 0.3}),
("Infographics and visual marketing materials", {"Marketing-Sales": 0.9, "Visual-Design": 0.4}),
("Case studies and testimonial content", {"Marketing-Sales": 1.0, "People-Skill": 0.3}),
("Market research reports and presentations", {"Marketing-Sales": 0.9, "Analytical-Skill": 0.4})], ["business"]),
("What consumer behavior concept interests you?", {"Marketing-Sales": 0.9, "Analytical-Skill": 0.3}, [
("Purchase decision psychology and triggers", {"Marketing-Sales": 1.0, "Counseling": 0.3}),
("Brand loyalty and repeat customer behavior", {"Marketing-Sales": 0.9, "People-Skill": 0.3}),
("Price sensitivity and value perception", {"Marketing-Sales": 0.9, "Finance-Acct": 0.3}),
("Social proof and peer influence on buying", {"Marketing-Sales": 1.0, "People-Skill": 0.3}),
("Digital shopping habits and cart abandonment", {"Marketing-Sales": 0.9, "Web-Dev": 0.3}),
("Cultural factors in Filipino consumer choices", {"Marketing-Sales": 0.9, "Community-Serve": 0.3})], ["business"]),
("What sales achievement would motivate you most?", {"Marketing-Sales": 0.9}, [
("Closing the biggest deal in company history", {"Marketing-Sales": 1.0, "Finance-Acct": 0.3}),
("Building a loyal customer base from scratch", {"Marketing-Sales": 0.9, "People-Skill": 0.5}),
("Launching a viral marketing campaign", {"Marketing-Sales": 0.9, "Digital-Media": 0.4}),
("Winning a national advertising award", {"Marketing-Sales": 0.9, "Creative-Skill": 0.4}),
("Growing market share against competitors", {"Marketing-Sales": 1.0, "Analytical-Skill": 0.3}),
("Training a top-performing sales team", {"Marketing-Sales": 0.9, "Teaching-Ed": 0.3})], ["business"]),
("What marketing channel would you specialize in?", {"Marketing-Sales": 0.9}, [
("Google Ads and search engine marketing", {"Marketing-Sales": 1.0, "Data-Analytics": 0.4}),
("Facebook and Instagram paid advertising", {"Marketing-Sales": 0.9, "Digital-Media": 0.4}),
("Shopee and Lazada marketplace optimization", {"Marketing-Sales": 0.9, "Web-Dev": 0.3}),
("Email marketing automation", {"Marketing-Sales": 0.9, "Software-Dev": 0.3}),
("Outdoor and traditional print advertising", {"Marketing-Sales": 0.9, "Visual-Design": 0.3}),
("Radio and TV commercial production", {"Marketing-Sales": 1.0, "Film-Broadcast": 0.3})], ["business"]),
# Mechanical-Design +4
("What machine would you design?", {"Mechanical-Design": 0.9}, [
("Agricultural harvesting machine for rice", {"Mechanical-Design": 1.0, "Agri-Nature": 0.4}),
("Automated packaging and filling machine", {"Mechanical-Design": 0.9, "Industrial-Ops": 0.4}),
("Solar-powered water pump for rural areas", {"Mechanical-Design": 0.9, "Environmental-Eng": 0.3}),
("Medical rehabilitation exercise device", {"Mechanical-Design": 0.9, "Rehab-Therapy": 0.3}),
("Electric tricycle for Philippine transport", {"Mechanical-Design": 1.0, "Environmental-Eng": 0.3}),
("CNC router for small-scale fabrication", {"Mechanical-Design": 0.9, "Technical-Skill": 0.4})], ["engineering"]),
("What mechanical engineering principle fascinates you?", {"Mechanical-Design": 0.9, "Analytical-Skill": 0.3}, [
("Thermodynamics and heat engine cycles", {"Mechanical-Design": 1.0, "Analytical-Skill": 0.4}),
("Fluid mechanics and hydraulic systems", {"Mechanical-Design": 0.9, "Civil-Build": 0.3}),
("Kinematics and mechanism linkage design", {"Mechanical-Design": 1.0, "Analytical-Skill": 0.4}),
("Strength of materials and stress analysis", {"Mechanical-Design": 0.9, "Civil-Build": 0.3}),
("Machine dynamics and vibration analysis", {"Mechanical-Design": 0.9, "Analytical-Skill": 0.5}),
("Tribology: friction, wear, and lubrication", {"Mechanical-Design": 0.9, "Lab-Research": 0.3})], ["engineering"]),
("What Philippine mechanical engineering need would you address?", {"Mechanical-Design": 0.9}, [
("Developing local automotive parts manufacturing", {"Mechanical-Design": 1.0, "Industrial-Ops": 0.4}),
("Designing flood-proof water pumping stations", {"Mechanical-Design": 0.9, "Civil-Build": 0.3}),
("Creating affordable farming equipment", {"Mechanical-Design": 0.9, "Agri-Nature": 0.4}),
("Improving public transportation vehicle design", {"Mechanical-Design": 0.9, "Community-Serve": 0.3}),
("Building industrial chillers for food storage", {"Mechanical-Design": 1.0, "Food-Science": 0.3}),
("Designing earthquake dampers for buildings", {"Mechanical-Design": 0.9, "Civil-Build": 0.4})], ["engineering"]),
("What mechanical testing method would you perform?", {"Mechanical-Design": 0.9, "Lab-Research": 0.3}, [
("Tensile and compression testing of metals", {"Mechanical-Design": 1.0, "Lab-Research": 0.4}),
("Hardness testing with Brinell and Rockwell", {"Mechanical-Design": 0.9, "Lab-Research": 0.4}),
("Fatigue testing for cyclic loading analysis", {"Mechanical-Design": 0.9, "Analytical-Skill": 0.3}),
("Impact testing for material toughness", {"Mechanical-Design": 1.0, "Lab-Research": 0.3}),
("Non-destructive testing (ultrasonic, X-ray)", {"Mechanical-Design": 0.9, "Technical-Skill": 0.4}),
("Vibration testing on rotating machinery", {"Mechanical-Design": 0.9, "Technical-Skill": 0.3})], ["engineering"]),
# Performing-Arts +4
("What performance venue would you prefer?", {"Performing-Arts": 0.9}, [
("CCP main theater stage", {"Performing-Arts": 1.0, "Creative-Skill": 0.3}),
("Open-air concert at an evening festival", {"Performing-Arts": 0.9, "Hospitality-Svc": 0.3}),
("Intimate acoustic cafe performance", {"Performing-Arts": 0.9, "People-Skill": 0.3}),
("Church or community hall for local shows", {"Performing-Arts": 0.9, "Community-Serve": 0.3}),
("Recording studio for professional production", {"Performing-Arts": 0.9, "Technical-Skill": 0.4}),
("Virtual livestream performance for global audience", {"Performing-Arts": 1.0, "Digital-Media": 0.4})], ["creative"]),
("What performing arts tradition interests you?", {"Performing-Arts": 0.9, "Creative-Skill": 0.3}, [
("Kundiman and Filipino operatic tradition", {"Performing-Arts": 1.0, "Creative-Skill": 0.3}),
("Tinikling and Filipino folk dance", {"Performing-Arts": 0.9, "Physical-Skill": 0.5}),
("Senakulo and religious dramatic presentations", {"Performing-Arts": 0.9, "Community-Serve": 0.3}),
("Rondalla ensemble music performance", {"Performing-Arts": 0.9, "Technical-Skill": 0.3}),
("Modern Filipino hip-hop dance culture", {"Performing-Arts": 1.0, "Physical-Skill": 0.4}),
("OPM rock and indie music scene", {"Performing-Arts": 0.9, "Startup-Venture": 0.3})], ["creative"]),
("What performance skill would you focus on?", {"Performing-Arts": 0.9}, [
("Breath control and vocal projection", {"Performing-Arts": 1.0, "Physical-Skill": 0.3}),
("Stage presence and audience connection", {"Performing-Arts": 0.9, "People-Skill": 0.5}),
("Musical ear training and pitch accuracy", {"Performing-Arts": 0.9, "Analytical-Skill": 0.3}),
("Memorization and quick script learning", {"Performing-Arts": 0.9, "Analytical-Skill": 0.3}),
("Physical conditioning for dance endurance", {"Performing-Arts": 0.9, "Physical-Skill": 0.5}),
("Emotional expression and character depth", {"Performing-Arts": 1.0, "Counseling": 0.3})], ["creative"]),
("What performing arts collaboration appeals to you?", {"Performing-Arts": 0.9}, [
("Joining a theater company ensemble", {"Performing-Arts": 1.0, "People-Skill": 0.4}),
("Forming a band and playing gigs", {"Performing-Arts": 0.9, "Startup-Venture": 0.3}),
("Dance crew competing in competitions", {"Performing-Arts": 0.9, "Physical-Skill": 0.4}),
("Choir and choral group harmonizing", {"Performing-Arts": 0.9, "People-Skill": 0.3}),
("Community theater teaching kids to perform", {"Performing-Arts": 0.9, "Teaching-Ed": 0.5}),
("Film scoring and composing for movies", {"Performing-Arts": 1.0, "Film-Broadcast": 0.4})], ["creative"]),
# Spatial-Design +4
("What space would you redesign?", {"Spatial-Design": 0.9}, [
("A cramped studio apartment into a functional home", {"Spatial-Design": 1.0, "Creative-Skill": 0.4}),
("A traditional Filipino bahay kubo with modern touches", {"Spatial-Design": 0.9, "Creative-Skill": 0.4}),
("An office space for maximum productivity", {"Spatial-Design": 0.9, "Admin-Skill": 0.3}),
("A school classroom for better learning", {"Spatial-Design": 0.9, "Teaching-Ed": 0.3}),
("A hospital wing for patient comfort", {"Spatial-Design": 0.9, "Health-Admin": 0.3}),
("A public park with inclusive play areas", {"Spatial-Design": 1.0, "Community-Serve": 0.3})], ["creative"]),
("What interior design element interests you most?", {"Spatial-Design": 0.9, "Creative-Skill": 0.3}, [
("Color theory and paint selection", {"Spatial-Design": 1.0, "Visual-Design": 0.4}),
("Furniture selection and space planning", {"Spatial-Design": 0.9, "Creative-Skill": 0.3}),
("Lighting design for mood and function", {"Spatial-Design": 0.9, "Electrical-Power": 0.3}),
("Material and texture combinations", {"Spatial-Design": 1.0, "Creative-Skill": 0.4}),
("Sustainable and eco-friendly design choices", {"Spatial-Design": 0.9, "Environmental-Eng": 0.3}),
("Space acoustics and sound management", {"Spatial-Design": 0.9, "Performing-Arts": 0.3})], ["creative"]),
("What architectural style inspires you?", {"Spatial-Design": 0.9}, [
("Minimalist modern with clean lines", {"Spatial-Design": 1.0, "Creative-Skill": 0.3}),
("Tropical contemporary suited for Philippines", {"Spatial-Design": 0.9, "Environmental-Eng": 0.3}),
("Heritage and colonial Filipino architecture", {"Spatial-Design": 0.9, "Tourism-Travel": 0.3}),
("Industrial loft with exposed materials", {"Spatial-Design": 0.9, "Mechanical-Design": 0.2}),
("Japanese-inspired zen and natural design", {"Spatial-Design": 1.0, "Creative-Skill": 0.3}),
("Biophilic design bringing nature indoors", {"Spatial-Design": 0.9, "Environmental-Sci": 0.3})], ["creative"]),
("What spatial design project management skill interests you?", {"Spatial-Design": 0.9}, [
("Client consultation and vision interpretation", {"Spatial-Design": 1.0, "People-Skill": 0.4}),
("Material sourcing and vendor negotiations", {"Spatial-Design": 0.9, "Finance-Acct": 0.3}),
("Construction supervision and site visits", {"Spatial-Design": 0.9, "Civil-Build": 0.3}),
("3D rendering presentations for clients", {"Spatial-Design": 0.9, "Animation-3D": 0.3}),
("Budget management and cost estimation", {"Spatial-Design": 0.9, "Finance-Acct": 0.4}),
("Building code compliance and permits", {"Spatial-Design": 1.0, "Legal-Practice": 0.3})], ["creative", "engineering"]),
# Startup-Venture +3
("What would your Filipino startup solve?", {"Startup-Venture": 0.9}, [
("Traffic congestion with ride-sharing innovation", {"Startup-Venture": 1.0, "Software-Dev": 0.3}),
("Access to affordable healthcare consultations", {"Startup-Venture": 0.9, "Patient-Care": 0.3}),
("Food delivery for underserved rural towns", {"Startup-Venture": 0.9, "Hospitality-Svc": 0.3}),
("Bank the unbanked with mobile wallet services", {"Startup-Venture": 0.9, "Finance-Acct": 0.4}),
("Connect farmers directly to consumers", {"Startup-Venture": 1.0, "Agri-Nature": 0.3}),
("Affordable online tutoring for DepEd students", {"Startup-Venture": 0.9, "Teaching-Ed": 0.3})], ["business"]),
("What startup funding strategy would you use?", {"Startup-Venture": 0.9, "Finance-Acct": 0.3}, [
("Bootstrapping: building with personal savings", {"Startup-Venture": 1.0, "Finance-Acct": 0.3}),
("Angel investors from Philippine business leaders", {"Startup-Venture": 0.9, "People-Skill": 0.4}),
("Venture capital from local and international VCs", {"Startup-Venture": 0.9, "Finance-Acct": 0.4}),
("Crowdfunding on Kickstarter or local platforms", {"Startup-Venture": 0.9, "Marketing-Sales": 0.4}),
("Government grants from DOST or DTI programs", {"Startup-Venture": 0.9, "Admin-Skill": 0.3}),
("Revenue-first model: earning before raising", {"Startup-Venture": 1.0, "Analytical-Skill": 0.3})], ["business"]),
("What startup metric would you track obsessively?", {"Startup-Venture": 0.9, "Data-Analytics": 0.3}, [
("Monthly recurring revenue (MRR)", {"Startup-Venture": 1.0, "Finance-Acct": 0.4}),
("Customer acquisition cost (CAC)", {"Startup-Venture": 0.9, "Marketing-Sales": 0.3}),
("User retention and churn rate", {"Startup-Venture": 0.9, "Data-Analytics": 0.4}),
("Net promoter score (NPS) from customers", {"Startup-Venture": 0.9, "People-Skill": 0.3}),
("Runway: months of cash remaining", {"Startup-Venture": 1.0, "Finance-Acct": 0.3}),
("Daily active users (DAU)", {"Startup-Venture": 0.9, "Software-Dev": 0.3})], ["business"]),
# Teaching-Ed +4
("What teaching technology would you adopt?", {"Teaching-Ed": 0.9}, [
("Interactive whiteboard and smart classroom", {"Teaching-Ed": 1.0, "Technical-Skill": 0.4}),
("Learning management system (Google Classroom)", {"Teaching-Ed": 0.9, "Software-Dev": 0.3}),
("Educational apps and gamified quizzes", {"Teaching-Ed": 0.9, "Game-Dev": 0.3}),
("Video lessons and flipped classroom model", {"Teaching-Ed": 0.9, "Digital-Media": 0.4}),
("AR/VR immersive educational experiences", {"Teaching-Ed": 0.9, "Software-Dev": 0.3}),
("Adaptive learning platforms using AI", {"Teaching-Ed": 1.0, "AI-ML": 0.3})], ["education"]),
("What makes a great teacher in your view?", {"Teaching-Ed": 0.9}, [
("Patience and understanding of each student", {"Teaching-Ed": 1.0, "Counseling": 0.4}),
("Passion for the subject that's contagious", {"Teaching-Ed": 0.9, "Creative-Skill": 0.3}),
("Clear communication and explanation skills", {"Teaching-Ed": 0.9, "People-Skill": 0.5}),
("Fairness and consistent discipline", {"Teaching-Ed": 0.9, "Analytical-Skill": 0.3}),
("Creativity in lesson planning and activities", {"Teaching-Ed": 1.0, "Creative-Skill": 0.4}),
("Dedication to continuous self-improvement", {"Teaching-Ed": 0.9, "Analytical-Skill": 0.3})], ["education"]),
("What student population would you serve?", {"Teaching-Ed": 0.9}, [
("Kindergarten and early childhood learners", {"Teaching-Ed": 1.0, "Creative-Skill": 0.3}),
("Elementary students building foundations", {"Teaching-Ed": 0.9, "People-Skill": 0.3}),
("High school students preparing for college", {"Teaching-Ed": 0.9, "Counseling": 0.3}),
("College students in specialized subjects", {"Teaching-Ed": 0.9, "Lab-Research": 0.3}),
("Adult learners and continuing education", {"Teaching-Ed": 0.9, "People-Skill": 0.4}),
("Out-of-school youth needing alternative learning", {"Teaching-Ed": 1.0, "Community-Serve": 0.4})], ["education"]),
("What education assessment method would you use?", {"Teaching-Ed": 0.9, "Analytical-Skill": 0.3}, [
("Portfolio-based assessment of student work", {"Teaching-Ed": 1.0, "Creative-Skill": 0.3}),
("Performance tasks and practical exams", {"Teaching-Ed": 0.9, "Physical-Skill": 0.3}),
("Rubric-based evaluation for projects", {"Teaching-Ed": 0.9, "Analytical-Skill": 0.4}),
("Formative quizzes for ongoing feedback", {"Teaching-Ed": 0.9, "Data-Analytics": 0.3}),
("Peer assessment and self-evaluation", {"Teaching-Ed": 1.0, "People-Skill": 0.3}),
("Standardized testing with data analytics", {"Teaching-Ed": 0.9, "Data-Analytics": 0.5})], ["education"]),
# Visual-Design +3
("What visual design project would you take on?", {"Visual-Design": 0.9}, [
("Complete brand identity for a local business", {"Visual-Design": 1.0, "Marketing-Sales": 0.4}),
("Magazine editorial layout and design", {"Visual-Design": 0.9, "Digital-Media": 0.3}),
("Website UI design with custom illustrations", {"Visual-Design": 0.9, "Web-Dev": 0.4}),
("Product packaging for Philippine exports", {"Visual-Design": 0.9, "Marketing-Sales": 0.3}),
("Environmental graphics and signage system", {"Visual-Design": 1.0, "Spatial-Design": 0.4}),
("Social media visual template library", {"Visual-Design": 0.9, "Digital-Media": 0.4})], ["creative"]),
("What color and design principle matters most to you?", {"Visual-Design": 0.9, "Creative-Skill": 0.3}, [
("Color harmony and effective palette selection", {"Visual-Design": 1.0, "Creative-Skill": 0.4}),
("Visual hierarchy guiding the viewer's eye", {"Visual-Design": 0.9, "Analytical-Skill": 0.3}),
("Whitespace and breathing room in layouts", {"Visual-Design": 0.9, "Spatial-Design": 0.3}),
("Grid systems for consistent proportions", {"Visual-Design": 1.0, "Analytical-Skill": 0.4}),
("Contrast and readability for accessibility", {"Visual-Design": 0.9, "Community-Serve": 0.2}),
("Consistency across a brand's visual materials", {"Visual-Design": 0.9, "Marketing-Sales": 0.3})], ["creative"]),
("What design movement inspires your style?", {"Visual-Design": 0.9}, [
("Minimalism: less is more clean design", {"Visual-Design": 1.0, "Creative-Skill": 0.3}),
("Bauhaus: form follows function", {"Visual-Design": 0.9, "Spatial-Design": 0.3}),
("Art Nouveau: organic and decorative", {"Visual-Design": 0.9, "Creative-Skill": 0.5}),
("Swiss Design: clear typography and grids", {"Visual-Design": 1.0, "Analytical-Skill": 0.3}),
("Retro/vintage Filipino poster style", {"Visual-Design": 0.9, "Creative-Skill": 0.4}),
("Contemporary flat and material design", {"Visual-Design": 0.9, "Web-Dev": 0.3})], ["creative"]),
# Nutrition-Diet +3
("What nutritional health program would you create?", {"Nutrition-Diet": 0.9}, [
("School feeding program with balanced meals", {"Nutrition-Diet": 1.0, "Teaching-Ed": 0.3}),
("Weight management plan for obese patients", {"Nutrition-Diet": 0.9, "Patient-Care": 0.4}),
("Senior citizen dietary guidance and counseling", {"Nutrition-Diet": 0.9, "Counseling": 0.3}),
("Prenatal nutrition plan for expecting mothers", {"Nutrition-Diet": 0.9, "Patient-Care": 0.4}),
("Diabetic meal planning and blood sugar control", {"Nutrition-Diet": 1.0, "Medical-Lab": 0.3}),
("Sports performance nutrition coaching", {"Nutrition-Diet": 0.9, "Sports-Ed": 0.4})], ["healthcare"]),
("What nutrition science topic interests you?", {"Nutrition-Diet": 0.9, "Lab-Research": 0.3}, [
("Macronutrient balance and metabolism", {"Nutrition-Diet": 1.0, "Lab-Research": 0.3}),
("Micronutrient deficiency in Filipino children", {"Nutrition-Diet": 0.9, "Public-Health": 0.5}),
("Gut microbiome and its effect on health", {"Nutrition-Diet": 0.9, "Lab-Research": 0.4}),
("Food allergies and intolerance management", {"Nutrition-Diet": 0.9, "Medical-Lab": 0.3}),
("Anti-inflammatory diet and chronic disease", {"Nutrition-Diet": 1.0, "Patient-Care": 0.3}),
("Nutrigenomics: nutrition based on genetics", {"Nutrition-Diet": 0.9, "Lab-Research": 0.4})], ["healthcare", "science"]),
("Where would you work as a nutritionist?", {"Nutrition-Diet": 0.9}, [
("Hospital dietary department", {"Nutrition-Diet": 1.0, "Health-Admin": 0.4}),
("Sports team nutritional support", {"Nutrition-Diet": 0.9, "Sports-Ed": 0.5}),
("Community health center nutrition clinic", {"Nutrition-Diet": 0.9, "Community-Serve": 0.4}),
("Food company product health claims team", {"Nutrition-Diet": 0.9, "Food-Science": 0.4}),
("Private nutrition consulting practice", {"Nutrition-Diet": 0.9, "Startup-Venture": 0.3}),
("School nutrition program coordinator", {"Nutrition-Diet": 1.0, "Teaching-Ed": 0.3})], ["healthcare"]),
]
for t, qt, o, br in misc2: ALL.append(nq(t, qt, o, br))


# ==================== PATCHING LOGIC ====================
def main():
    with open("questions_enhanced.py", "r", encoding="utf-8") as f:
        qe = f.read()
    questions = [q for q, _ in ALL]
    first_id = questions[0]["question_id"]
    if f'"question_id": {first_id}' in qe:
        print(f"Q{first_id} already exists — skipping."); return
    insert_point = qe.rfind("\n]\n\nTRAIT_SECONDARY_MAP")
    if insert_point == -1:
        print("ERROR: insertion point not found"); sys.exit(1)
    lines = ["    # ==================== ROUND 2: TARGETED QUESTIONS FOR UNDER-10 TRAITS ===================="]
    for q in questions:
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
    qe = qe[:insert_point] + "\n" + "\n".join(lines) + qe[insert_point:]
    with open("questions_enhanced.py", "w", encoding="utf-8") as f:
        f.write(qe)
    print(f"Added {len(questions)} questions (Q{questions[0]['question_id']}-Q{questions[-1]['question_id']})")

    import importlib
    for m in ["questions_enhanced", "adaptive_assessment"]:
        if m in sys.modules: del sys.modules[m]
    from questions_enhanced import QUESTIONS_POOL_ENHANCED
    q_lookup = {q["question_id"]: q for q in QUESTIONS_POOL_ENHANCED}
    print(f"Total questions: {len(QUESTIONS_POOL_ENHANCED)}")

    with open("adaptive_assessment.py", "r", encoding="utf-8") as f:
        aa = f.read()

    tree_data = {q["question_id"]: br for q, br in ALL}
    first_check = f"{questions[0]['question_id']}:"
    if first_check not in aa.split("QUESTION_TREE_NODES")[1][:50000]:
        ts = aa.find("QUESTION_TREE_NODES = {")
        bd = 0; p = ts + len("QUESTION_TREE_NODES = {")
        while p < len(aa):
            if aa[p] == '{': bd += 1
            elif aa[p] == '}':
                if bd == 0:
                    ins = [f'    {qid}: {{"level": 2, "weight": 1.5, "branches": {br}}},' for qid, br in tree_data.items()]
                    aa = aa[:p] + "\n" + "\n".join(ins) + "\n" + aa[p:]
                    print(f"Added {len(tree_data)} tree nodes"); break
                bd -= 1
            p += 1

    tfm_match = re.search(r'TRAIT_FOLLOWUP_MAP\s*=\s*\{', aa)
    tfm_start = tfm_match.start()
    bd = 0; p = tfm_match.end()
    while p < len(aa):
        if aa[p] == '{': bd += 1
        elif aa[p] == '}':
            if bd == 0: tfm_end = p + 1; break
            bd -= 1
        p += 1
    ns = {}; exec(aa[tfm_start:tfm_end], {}, ns)
    tfm = ns["TRAIT_FOLLOWUP_MAP"]

    for q in questions:
        qid = q["question_id"]
        all_traits = set(q["trait_tags"].keys())
        for opt in q["options"]:
            for t in opt.get("trait_tags", {}).keys(): all_traits.add(t)
        for trait in all_traits:
            if trait in tfm and qid not in tfm[trait]: tfm[trait].append(qid)

    def sc(qid, trait):
        q = q_lookup.get(qid)
        if not q: return 0
        total = sum(o.get("trait_tags",{}).get(trait,0) for o in q["options"])
        avg = total / max(len(q["options"]),1)
        tmax = {}
        for o in q["options"]:
            for t,v in o.get("trait_tags",{}).items():
                if t not in tmax or v > tmax[t]: tmax[t] = v
        return avg + (10.0 if tmax and max(tmax, key=tmax.get) == trait else 0)

    reordered = {}
    for trait, qids in sorted(tfm.items()):
        scored = [(qid, sc(qid, trait)) for qid in qids]
        scored.sort(key=lambda x: -x[1])
        reordered[trait] = [qid for qid, _ in scored]

    tlines = ["TRAIT_FOLLOWUP_MAP = {"]
    for trait in sorted(reordered.keys()):
        tlines.append(f'    "{trait}": {reordered[trait]},')
    tlines.append("}")
    aa = aa[:tfm_start] + "\n".join(tlines) + aa[tfm_end:]

    with open("adaptive_assessment.py", "w", encoding="utf-8") as f:
        f.write(aa)
    print("Updated adaptive_assessment.py")

    for m in ["questions_enhanced", "adaptive_assessment"]:
        if m in sys.modules: del sys.modules[m]
    from adaptive_assessment import TRAIT_FOLLOWUP_MAP
    under = {}
    for trait, qids in sorted(TRAIT_FOLLOWUP_MAP.items()):
        on = 0
        for qid in qids[:30]:
            q = q_lookup.get(qid)
            if not q: continue
            tmax = {}
            for o in q["options"]:
                for t,v in o.get("trait_tags",{}).items():
                    if t not in tmax or v > tmax[t]: tmax[t] = v
            if tmax and max(tmax, key=tmax.get) == trait: on += 1
        print(f"  {trait}: {on}/30 on-topic")
        if on < 20: under[trait] = on
    if under:
        print(f"\nStill under 20: {under}")

if __name__ == "__main__":
    main()
