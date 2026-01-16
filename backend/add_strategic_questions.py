"""
Add 18 strategic questions to cover missing traits and improve accuracy
Targets the most frequently used traits in courses that aren't detected by current questions
"""

from database import SessionLocal
from models import Question, Option

def add_strategic_questions():
    db = SessionLocal()
    
    try:
        # Starting IDs
        question_id = 2472
        option_id = 9837
        
        strategic_questions = [
            {
                "category": "Team Dynamics",
                "text": "In group projects, what role do you naturally take?",
                "options": [
                    {"text": "Coordinating everyone's efforts and ensuring smooth collaboration", "trait": "Team-centric"},
                    {"text": "Leading the strategy and making key decisions", "trait": "Leadership"},
                    {"text": "Working independently on my assigned tasks", "trait": "Independent"},
                    {"text": "Supporting others and helping where needed", "trait": "Collaborative"}
                ]
            },
            {
                "category": "Patience Level",
                "text": "How do you feel about tasks that require long-term dedication?",
                "options": [
                    {"text": "I thrive on projects that take months or years to complete", "trait": "Patient"},
                    {"text": "I prefer quick results and fast-paced work", "trait": "Active"},
                    {"text": "I can handle both depending on the importance", "trait": "Adaptive"},
                    {"text": "I like steady progress with clear milestones", "trait": "Methodical"}
                ]
            },
            {
                "category": "Compassion Expression",
                "text": "When someone is struggling, what's your first instinct?",
                "options": [
                    {"text": "Offer emotional support and understanding", "trait": "Compassionate"},
                    {"text": "Help solve their practical problems", "trait": "Helping-others"},
                    {"text": "Listen actively without judgment", "trait": "Empathetic"},
                    {"text": "Give advice based on logic", "trait": "Logical"}
                ]
            },
            {
                "category": "Observation Skills",
                "text": "What do you notice most about your surroundings?",
                "options": [
                    {"text": "Small details and patterns that others miss", "trait": "Observational"},
                    {"text": "How things work and their functions", "trait": "Analytical"},
                    {"text": "The overall aesthetic and atmosphere", "trait": "Aesthetic-sense"},
                    {"text": "People's emotions and social dynamics", "trait": "Empathetic"}
                ]
            },
            {
                "category": "Nature Connection",
                "text": "How do you feel about spending time in natural environments?",
                "options": [
                    {"text": "It's essential for my wellbeing - I feel most alive outdoors", "trait": "Nature-connected"},
                    {"text": "I enjoy outdoor activities and adventure", "trait": "Outdoor-enthusiast"},
                    {"text": "I appreciate nature but prefer urban settings", "trait": "Office-based"},
                    {"text": "I'm more focused on indoor hobbies", "trait": "Introverted"}
                ]
            },
            {
                "category": "Persuasion Style",
                "text": "When you need to convince someone of your idea, you:",
                "options": [
                    {"text": "Use compelling arguments and influence their perspective", "trait": "Persuasive"},
                    {"text": "Present data and logical evidence", "trait": "Analytical"},
                    {"text": "Build relationships and find common ground", "trait": "Collaborative"},
                    {"text": "Demonstrate through actions and results", "trait": "Practical"}
                ]
            },
            {
                "category": "Pattern Recognition",
                "text": "Do you easily spot patterns in data, behavior, or systems?",
                "options": [
                    {"text": "Yes, I naturally see connections and recurring themes", "trait": "Pattern-recognition"},
                    {"text": "I'm good at analyzing structured data", "trait": "Quantitative"},
                    {"text": "I focus more on individual details than patterns", "trait": "Detail-focused"},
                    {"text": "I see the big picture rather than specific patterns", "trait": "Big-picture"}
                ]
            },
            {
                "category": "Community Engagement",
                "text": "How important is contributing to your community?",
                "options": [
                    {"text": "It's central to my life - I want to make a local impact", "trait": "Community-focused"},
                    {"text": "I prefer helping people through my professional work", "trait": "Service-oriented"},
                    {"text": "I care about broader social causes", "trait": "Advocacy"},
                    {"text": "I focus on personal and family wellbeing first", "trait": "Independent"}
                ]
            },
            {
                "category": "Cultural Sensitivity",
                "text": "How do you approach people from different cultural backgrounds?",
                "options": [
                    {"text": "I actively learn about and respect diverse perspectives", "trait": "Cultural-awareness"},
                    {"text": "I adapt my communication to different audiences", "trait": "Adaptive"},
                    {"text": "I treat everyone the same regardless of background", "trait": "Ethical"},
                    {"text": "I'm curious and ask questions to understand", "trait": "Inquisitive"}
                ]
            },
            {
                "category": "Resourcefulness",
                "text": "When faced with limited resources, you:",
                "options": [
                    {"text": "Find creative solutions and make the most of what's available", "trait": "Resourceful"},
                    {"text": "Innovate new approaches", "trait": "Innovative"},
                    {"text": "Plan carefully to optimize efficiency", "trait": "Strategic"},
                    {"text": "Work harder with what you have", "trait": "Resilient"}
                ]
            },
            {
                "category": "Discipline Assessment",
                "text": "How would you describe your work habits?",
                "options": [
                    {"text": "Highly structured with strict routines and self-control", "trait": "Disciplined"},
                    {"text": "Organized with clear systems", "trait": "Organized"},
                    {"text": "Methodical but flexible", "trait": "Methodical"},
                    {"text": "Adaptable to changing needs", "trait": "Adaptive"}
                ]
            },
            {
                "category": "Nurturing Tendency",
                "text": "How do you feel about helping others grow and develop?",
                "options": [
                    {"text": "I love guiding and caring for others' development", "trait": "Nurturing"},
                    {"text": "I enjoy mentoring and teaching", "trait": "Mentoring"},
                    {"text": "I prefer coaching toward specific goals", "trait": "Coaching"},
                    {"text": "I support others but focus on my own growth", "trait": "Independent"}
                ]
            },
            {
                "category": "Critical Analysis",
                "text": "When evaluating information, you:",
                "options": [
                    {"text": "Question assumptions and examine evidence critically", "trait": "Critical-thinking"},
                    {"text": "Break down complex ideas systematically", "trait": "Analytical"},
                    {"text": "Look for logical inconsistencies", "trait": "Logical"},
                    {"text": "Investigate thoroughly before forming opinions", "trait": "Investigative"}
                ]
            },
            {
                "category": "Exploration Mindset",
                "text": "What's your approach to new experiences?",
                "options": [
                    {"text": "I actively seek out novel experiences and discoveries", "trait": "Exploratory"},
                    {"text": "I'm curious but prefer structured learning", "trait": "Inquisitive"},
                    {"text": "I take calculated risks", "trait": "Risk-taking"},
                    {"text": "I prefer familiar and proven approaches", "trait": "Methodical"}
                ]
            },
            {
                "category": "Healthcare Interaction",
                "text": "If working in healthcare, what aspect appeals most?",
                "options": [
                    {"text": "Direct interaction and care with patients", "trait": "Patient-interaction"},
                    {"text": "Focus on patient wellbeing and recovery", "trait": "Patient-focused"},
                    {"text": "Medical research and laboratory work", "trait": "Laboratory"},
                    {"text": "Health policy and system improvement", "trait": "Governance-focus"}
                ]
            },
            {
                "category": "Data Orientation",
                "text": "How do you make important decisions?",
                "options": [
                    {"text": "Based on data analysis and evidence", "trait": "Data-driven"},
                    {"text": "Using numbers and statistical reasoning", "trait": "Quantitative"},
                    {"text": "Through logical reasoning", "trait": "Logical"},
                    {"text": "Combining data with intuition", "trait": "Strategic"}
                ]
            },
            {
                "category": "Client Relations",
                "text": "How comfortable are you working directly with clients?",
                "options": [
                    {"text": "I thrive on building client relationships", "trait": "Client-interaction"},
                    {"text": "I enjoy social interaction in professional settings", "trait": "Extroverted"},
                    {"text": "I prefer collaborative team environments", "trait": "Collaborative"},
                    {"text": "I work better behind the scenes", "trait": "Independent"}
                ]
            },
            {
                "category": "Physical Wellness",
                "text": "How important is physical fitness to you?",
                "options": [
                    {"text": "It's a core part of my lifestyle and identity", "trait": "Physical-fitness"},
                    {"text": "I'm active and enjoy sports", "trait": "Athletic-passion"},
                    {"text": "I maintain basic health but it's not a focus", "trait": "Health-conscious"},
                    {"text": "I prioritize mental over physical activities", "trait": "Contemplative"}
                ]
            }
        ]
        
        print(f"📝 Adding {len(strategic_questions)} strategic questions...\n")
        
        for q_data in strategic_questions:
            # Create question
            question = Question(
                question_id=question_id,
                category=q_data["category"],
                question_text=q_data["text"]
            )
            db.add(question)
            print(f"✅ Q{question_id}: {q_data['category']}")
            
            # Create options
            for opt_data in q_data["options"]:
                option = Option(
                    option_id=option_id,
                    question_id=question_id,
                    option_text=opt_data["text"],
                    trait_tag=opt_data["trait"]
                )
                db.add(option)
                print(f"   └─ {opt_data['trait']}")
                option_id += 1
            
            question_id += 1
            print()
        
        db.commit()
        print(f"\n✅ Successfully added {len(strategic_questions)} questions with {len(strategic_questions) * 4} options!")
        print(f"📊 New totals: {question_id - 2472} questions added")
        
        # Verify new traits
        all_options = db.query(Option).all()
        all_traits = set([o.trait_tag.strip() for o in all_options if o.trait_tag and o.trait_tag.strip().lower() not in ['none', '']])
        print(f"🎯 Total unique traits now: {len(all_traits)}")
        
    except Exception as e:
        db.rollback()
        print(f"❌ Error: {e}")
        raise
    finally:
        db.close()

if __name__ == "__main__":
    add_strategic_questions()
