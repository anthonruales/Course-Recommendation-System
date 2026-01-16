"""
Export new strategic questions to add to seed_data.py
"""
from database import SessionLocal
from models import Question, Option

db = SessionLocal()

# Get questions from 2472 onwards (if they exist after seed wipe)
questions = db.query(Question).filter(Question.question_id >= 2472).all()

if not questions:
    print("No new questions found (they were wiped by seed). Using hardcoded data...")
    # Use the data from add_strategic_questions.py
    strategic_questions = [
        ("Team Dynamics", "In group projects, what role do you naturally take?", [
            ("Coordinating everyone's efforts and ensuring smooth collaboration", "Team-centric"),
            ("Leading the strategy and making key decisions", "Leadership"),
            ("Working independently on my assigned tasks", "Independent"),
            ("Supporting others and helping where needed", "Collaborative")
        ]),
        ("Patience Level", "How do you feel about tasks that require long-term dedication?", [
            ("I thrive on projects that take months or years to complete", "Patient"),
            ("I prefer quick results and fast-paced work", "Active"),
            ("I can handle both depending on the importance", "Adaptive"),
            ("I like steady progress with clear milestones", "Methodical")
        ]),
        ("Compassion Expression", "When someone is struggling, what's your first instinct?", [
            ("Offer emotional support and understanding", "Compassionate"),
            ("Help solve their practical problems", "Helping-others"),
            ("Listen actively without judgment", "Empathetic"),
            ("Give advice based on logic", "Logical")
        ]),
        ("Observation Skills", "What do you notice most about your surroundings?", [
            ("Small details and patterns that others miss", "Observational"),
            ("How things work and their functions", "Analytical"),
            ("The overall aesthetic and atmosphere", "Aesthetic-sense"),
            ("People's emotions and social dynamics", "Empathetic")
        ]),
        ("Nature Connection", "How do you feel about spending time in natural environments?", [
            ("It's essential for my wellbeing - I feel most alive outdoors", "Nature-connected"),
            ("I enjoy outdoor activities and adventure", "Outdoor-enthusiast"),
            ("I appreciate nature but prefer urban settings", "Office-based"),
            ("I'm more focused on indoor hobbies", "Introverted")
        ]),
        ("Persuasion Style", "When you need to convince someone of your idea, you:", [
            ("Use compelling arguments and influence their perspective", "Persuasive"),
            ("Present data and logical evidence", "Analytical"),
            ("Build relationships and find common ground", "Collaborative"),
            ("Demonstrate through actions and results", "Practical")
        ]),
        ("Pattern Recognition", "Do you easily spot patterns in data, behavior, or systems?", [
            ("Yes, I naturally see connections and recurring themes", "Pattern-recognition"),
            ("I'm good at analyzing structured data", "Quantitative"),
            ("I focus more on individual details than patterns", "Detail-focused"),
            ("I see the big picture rather than specific patterns", "Big-picture")
        ]),
        ("Community Engagement", "How important is contributing to your community?", [
            ("It's central to my life - I want to make a local impact", "Community-focused"),
            ("I prefer helping people through my professional work", "Service-oriented"),
            ("I care about broader social causes", "Advocacy"),
            ("I focus on personal and family wellbeing first", "Independent")
        ]),
        ("Cultural Sensitivity", "How do you approach people from different cultural backgrounds?", [
            ("I actively learn about and respect diverse perspectives", "Cultural-awareness"),
            ("I adapt my communication to different audiences", "Adaptive"),
            ("I treat everyone the same regardless of background", "Ethical"),
            ("I'm curious and ask questions to understand", "Inquisitive")
        ]),
        ("Resourcefulness", "When faced with limited resources, you:", [
            ("Find creative solutions and make the most of what's available", "Resourceful"),
            ("Innovate new approaches", "Innovative"),
            ("Plan carefully to optimize efficiency", "Strategic"),
            ("Work harder with what you have", "Resilient")
        ]),
        ("Discipline Assessment", "How would you describe your work habits?", [
            ("Highly structured with strict routines and self-control", "Disciplined"),
            ("Organized with clear systems", "Organized"),
            ("Methodical but flexible", "Methodical"),
            ("Adaptable to changing needs", "Adaptive")
        ]),
        ("Nurturing Tendency", "How do you feel about helping others grow and develop?", [
            ("I love guiding and caring for others' development", "Nurturing"),
            ("I enjoy mentoring and teaching", "Mentoring"),
            ("I prefer coaching toward specific goals", "Coaching"),
            ("I support others but focus on my own growth", "Independent")
        ]),
        ("Critical Analysis", "When evaluating information, you:", [
            ("Question assumptions and examine evidence critically", "Critical-thinking"),
            ("Break down complex ideas systematically", "Analytical"),
            ("Look for logical inconsistencies", "Logical"),
            ("Investigate thoroughly before forming opinions", "Investigative")
        ]),
        ("Exploration Mindset", "What's your approach to new experiences?", [
            ("I actively seek out novel experiences and discoveries", "Exploratory"),
            ("I'm curious but prefer structured learning", "Inquisitive"),
            ("I take calculated risks", "Risk-taking"),
            ("I prefer familiar and proven approaches", "Methodical")
        ]),
        ("Healthcare Interaction", "If working in healthcare, what aspect appeals most?", [
            ("Direct interaction and care with patients", "Patient-interaction"),
            ("Focus on patient wellbeing and recovery", "Patient-focused"),
            ("Medical research and laboratory work", "Laboratory"),
            ("Health policy and system improvement", "Governance-focus")
        ]),
        ("Data Orientation", "How do you make important decisions?", [
            ("Based on data analysis and evidence", "Data-driven"),
            ("Using numbers and statistical reasoning", "Quantitative"),
            ("Through logical reasoning", "Logical"),
            ("Combining data with intuition", "Strategic")
        ]),
        ("Client Relations", "How comfortable are you working directly with clients?", [
            ("I thrive on building client relationships", "Client-interaction"),
            ("I enjoy social interaction in professional settings", "Extroverted"),
            ("I prefer collaborative team environments", "Collaborative"),
            ("I work better behind the scenes", "Independent")
        ]),
        ("Physical Wellness", "How important is physical fitness to you?", [
            ("It's a core part of my lifestyle and identity", "Physical-fitness"),
            ("I'm active and enjoy sports", "Athletic-passion"),
            ("I maintain basic health but it's not a focus", "Health-conscious"),
            ("I prioritize mental over physical activities", "Contemplative")
        ])
    ]
    
    print("\n# ADD THESE TO seed_data.py QUESTIONS_POOL list:\n")
    for category, question_text, options in strategic_questions:
        print(f'    {{')
        print(f'        "category": "{category}",')
        print(f'        "question_text": "{question_text}",')
        print(f'        "options": [')
        for opt_text, trait_tag in options:
            print(f'            {{"option_text": "{opt_text}", "trait_tag": "{trait_tag}"}},')
        print(f'        ]')
        print(f'    }},')

db.close()
