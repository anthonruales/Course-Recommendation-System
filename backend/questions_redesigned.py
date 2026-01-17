# questions_redesigned.py - Clear Questions That Map to RIASEC Traits
"""
================================================================================
REDESIGNED QUESTION SYSTEM FOR ACCURATE COURSE MATCHING
================================================================================

These questions are designed to:
1. Use the SAME traits as courses (Investigative, Realistic, Artistic, etc.)
2. Be clear and easy to answer
3. Directly lead to expected course recommendations

The 17 traits used:
- RIASEC: Realistic, Investigative, Artistic, Social, Enterprising, Conventional
- Skills: Technical, Scientific, Numbers, Words, Visual, Physical
- Environment: Outdoor, Healthcare, Business
- Bonus: Problem-solving, Creative

================================================================================
"""

QUESTIONS_POOL = [
    # ============================================================
    # SECTION 1: WHAT DO YOU LIKE TO DO? (Core Interest)
    # ============================================================
    {
        "question": "On a free weekend, what would you MOST enjoy doing?",
        "category": "Core Interest",
        "options": [
            {"text": "Building, fixing, or working on something with my hands", "tag": "Realistic"},
            {"text": "Reading about science or researching something interesting", "tag": "Investigative"},
            {"text": "Creating art, music, or designing something", "tag": "Artistic"},
            {"text": "Hanging out with friends or helping someone", "tag": "Social"}
        ]
    },
    {
        "question": "What type of YouTube videos do you watch most?",
        "category": "Content Interest",
        "options": [
            {"text": "DIY tutorials, car/tech repairs, how to build things", "tag": "Realistic"},
            {"text": "Science explainers, documentaries, educational content", "tag": "Investigative"},
            {"text": "Art tutorials, music, films, design content", "tag": "Artistic"},
            {"text": "Vlogs, lifestyle, travel, or motivational speakers", "tag": "Social"}
        ]
    },
    {
        "question": "Which school subject makes you excited to attend class?",
        "category": "Subject Passion",
        "options": [
            {"text": "TLE/Shop class - making things, cooking, technical skills", "tag": "Realistic"},
            {"text": "Science - experiments, discoveries, understanding nature", "tag": "Investigative"},
            {"text": "Arts/Music - creating, performing, expressing myself", "tag": "Artistic"},
            {"text": "Filipino/English/MAPEH - discussions, presentations, group work", "tag": "Social"}
        ]
    },
    {
        "question": "If someone gave you ₱10,000 to spend on a hobby, what would you buy?",
        "category": "Hobby Investment",
        "options": [
            {"text": "Tools, equipment, or gadgets to build/fix things", "tag": "Realistic"},
            {"text": "Books, online courses, or a microscope/telescope", "tag": "Investigative"},
            {"text": "Art supplies, musical instrument, or camera", "tag": "Artistic"},
            {"text": "Experiences with friends, event tickets, or gifts for others", "tag": "Social"}
        ]
    },

    # ============================================================
    # SECTION 2: WORK STYLE (Enterprising vs Conventional)
    # ============================================================
    {
        "question": "In a group project, which role fits you best?",
        "category": "Group Role",
        "options": [
            {"text": "The leader - I organize everyone and make decisions", "tag": "Enterprising"},
            {"text": "The organizer - I keep track of tasks and deadlines", "tag": "Conventional"},
            {"text": "The doer - I focus on my assigned work quietly", "tag": "Realistic"},
            {"text": "The supporter - I help whoever needs it most", "tag": "Social"}
        ]
    },
    {
        "question": "When you imagine your future career, you see yourself:",
        "category": "Career Vision",
        "options": [
            {"text": "Running my own business or leading a company", "tag": "Enterprising"},
            {"text": "Working in a stable job with clear responsibilities", "tag": "Conventional"},
            {"text": "Discovering something new or solving big problems", "tag": "Investigative"},
            {"text": "Creating something that people will remember", "tag": "Artistic"}
        ]
    },
    {
        "question": "How do you feel about taking risks?",
        "category": "Risk Attitude",
        "options": [
            {"text": "I love taking risks - high risk, high reward!", "tag": "Enterprising"},
            {"text": "I prefer safe, predictable paths with steady progress", "tag": "Conventional"},
            {"text": "I'll take risks if I've analyzed all the data first", "tag": "Investigative"},
            {"text": "Depends on who else is affected by my decision", "tag": "Social"}
        ]
    },
    {
        "question": "Which statement describes you better?",
        "category": "Work Preference",
        "options": [
            {"text": "I like convincing people and selling ideas", "tag": "Enterprising"},
            {"text": "I like organizing files, data, and keeping things in order", "tag": "Conventional"},
            {"text": "I like figuring out how things work and why", "tag": "Investigative"},
            {"text": "I like making things look beautiful and creative", "tag": "Artistic"}
        ]
    },

    # ============================================================
    # SECTION 3: SKILLS YOU ENJOY (Technical, Numbers, Words, Visual, Physical)
    # ============================================================
    {
        "question": "Which of these tasks would you enjoy doing for hours?",
        "category": "Skill Enjoyment",
        "options": [
            {"text": "Coding, troubleshooting computers, or using software", "tag": "Technical"},
            {"text": "Solving math problems or analyzing data/statistics", "tag": "Numbers"},
            {"text": "Writing essays, reading books, or learning languages", "tag": "Words"},
            {"text": "Drawing, designing layouts, or editing photos/videos", "tag": "Visual"}
        ]
    },
    {
        "question": "What's your relationship with Mathematics?",
        "category": "Math Comfort",
        "options": [
            {"text": "I love it! Numbers and formulas are fun", "tag": "Numbers"},
            {"text": "I like math when it's applied to real problems", "tag": "Problem-solving"},
            {"text": "It's okay, but I prefer other subjects", "tag": "Words"},
            {"text": "I struggle with it and prefer creative subjects", "tag": "Artistic"}
        ]
    },
    {
        "question": "How do you prefer to express your ideas?",
        "category": "Expression Style",
        "options": [
            {"text": "Through diagrams, sketches, or visual presentations", "tag": "Visual"},
            {"text": "Through writing - essays, stories, or reports", "tag": "Words"},
            {"text": "Through numbers - charts, graphs, or calculations", "tag": "Numbers"},
            {"text": "Through building prototypes or demonstrations", "tag": "Technical"}
        ]
    },
    {
        "question": "Which computer activity do you enjoy most?",
        "category": "Digital Skills",
        "options": [
            {"text": "Coding, programming, or building websites/apps", "tag": "Technical"},
            {"text": "Using Excel, analyzing data, or creating formulas", "tag": "Numbers"},
            {"text": "Graphic design, video editing, or digital art", "tag": "Visual"},
            {"text": "Writing documents, blogging, or social media content", "tag": "Words"}
        ]
    },

    # ============================================================
    # SECTION 4: WORK ENVIRONMENT (Outdoor, Healthcare, Business, Scientific)
    # ============================================================
    {
        "question": "Where would you love to work?",
        "category": "Work Location",
        "options": [
            {"text": "Outdoors - farms, forests, construction sites, or the sea", "tag": "Outdoor"},
            {"text": "Hospitals, clinics, or healthcare facilities", "tag": "Healthcare"},
            {"text": "Corporate offices, banks, or business centers", "tag": "Business"},
            {"text": "Laboratories, research centers, or universities", "tag": "Scientific"}
        ]
    },
    {
        "question": "Which work setting sounds most appealing?",
        "category": "Setting Preference",
        "options": [
            {"text": "Being outside in nature, even in sun or rain", "tag": "Outdoor"},
            {"text": "A clean, organized office with a desk and computer", "tag": "Business"},
            {"text": "A creative studio with art supplies or equipment", "tag": "Artistic"},
            {"text": "A lab with equipment for experiments and research", "tag": "Scientific"}
        ]
    },
    {
        "question": "How do you feel about working in a hospital or clinic?",
        "category": "Healthcare Interest",
        "options": [
            {"text": "I'd love it! I want to help sick people get better", "tag": "Healthcare"},
            {"text": "Maybe, but I prefer the research/science side of medicine", "tag": "Scientific"},
            {"text": "I'd rather work in wellness, fitness, or nutrition", "tag": "Physical"},
            {"text": "Not for me - I prefer other environments", "tag": "Business"}
        ]
    },
    {
        "question": "Would you enjoy a job that keeps you physically active?",
        "category": "Activity Level",
        "options": [
            {"text": "Yes! I hate sitting all day - I need to move", "tag": "Physical"},
            {"text": "Yes, especially if it's outdoors in nature", "tag": "Outdoor"},
            {"text": "I prefer a mix of active and desk work", "tag": "Realistic"},
            {"text": "No, I prefer working at a desk or computer", "tag": "Technical"}
        ]
    },

    # ============================================================
    # SECTION 5: HELPING OTHERS (Social, Healthcare)
    # ============================================================
    {
        "question": "What motivates you most in a career?",
        "category": "Career Motivation",
        "options": [
            {"text": "Helping people directly - teaching, healing, counseling", "tag": "Social"},
            {"text": "Discovering new knowledge or solutions", "tag": "Investigative"},
            {"text": "Building wealth and achieving financial success", "tag": "Enterprising"},
            {"text": "Creating something beautiful or meaningful", "tag": "Artistic"}
        ]
    },
    {
        "question": "A friend is stressed about a problem. What do you do?",
        "category": "Helping Style",
        "options": [
            {"text": "Listen patiently and offer emotional support", "tag": "Social"},
            {"text": "Analyze the problem and suggest logical solutions", "tag": "Investigative"},
            {"text": "Take charge and help them make a decision", "tag": "Enterprising"},
            {"text": "Distract them with fun activities or creative ideas", "tag": "Artistic"}
        ]
    },
    {
        "question": "Which career impact would make you proudest?",
        "category": "Impact Preference",
        "options": [
            {"text": "I helped hundreds of patients recover their health", "tag": "Healthcare"},
            {"text": "I taught students who became successful professionals", "tag": "Social"},
            {"text": "I built a successful company that employs many people", "tag": "Enterprising"},
            {"text": "I discovered something that advanced human knowledge", "tag": "Investigative"}
        ]
    },
    {
        "question": "Would you enjoy teaching or training others?",
        "category": "Teaching Interest",
        "options": [
            {"text": "Yes! I love explaining things and helping people learn", "tag": "Social"},
            {"text": "Maybe, if it's about a technical topic I'm expert in", "tag": "Technical"},
            {"text": "I prefer working independently on my own projects", "tag": "Investigative"},
            {"text": "I'd rather lead and manage than teach", "tag": "Enterprising"}
        ]
    },

    # ============================================================
    # SECTION 6: PROBLEM-SOLVING STYLE
    # ============================================================
    {
        "question": "When faced with a difficult problem, you:",
        "category": "Problem Approach",
        "options": [
            {"text": "Break it into pieces and solve it step by step", "tag": "Problem-solving"},
            {"text": "Research similar problems and learn from others", "tag": "Investigative"},
            {"text": "Ask others for help and collaborate on solutions", "tag": "Social"},
            {"text": "Try creative or unconventional approaches", "tag": "Creative"}
        ]
    },
    {
        "question": "Which type of puzzle do you enjoy most?",
        "category": "Puzzle Type",
        "options": [
            {"text": "Logic puzzles - Sudoku, brain teasers, riddles", "tag": "Problem-solving"},
            {"text": "Building puzzles - Lego, models, assembly challenges", "tag": "Realistic"},
            {"text": "Word puzzles - crosswords, word games, trivia", "tag": "Words"},
            {"text": "Visual puzzles - spot the difference, mazes, patterns", "tag": "Visual"}
        ]
    },
    {
        "question": "How do you react when something breaks?",
        "category": "Fix-It Attitude",
        "options": [
            {"text": "I try to fix it myself - I enjoy troubleshooting", "tag": "Realistic"},
            {"text": "I research the problem and find the best solution", "tag": "Investigative"},
            {"text": "I call someone who knows how to fix it", "tag": "Social"},
            {"text": "I see if I can improve or redesign it while fixing", "tag": "Creative"}
        ]
    },

    # ============================================================
    # SECTION 7: CREATIVITY (Artistic, Creative, Visual)
    # ============================================================
    {
        "question": "How creative do you consider yourself?",
        "category": "Creativity Self-Assessment",
        "options": [
            {"text": "Very creative - I'm always thinking of new ideas", "tag": "Creative"},
            {"text": "Somewhat creative - I like design and aesthetics", "tag": "Visual"},
            {"text": "Practical creative - I find creative solutions to problems", "tag": "Problem-solving"},
            {"text": "Not very creative - I prefer following proven methods", "tag": "Conventional"}
        ]
    },
    {
        "question": "Which creative activity appeals to you most?",
        "category": "Creative Activity",
        "options": [
            {"text": "Drawing, painting, or digital art", "tag": "Visual"},
            {"text": "Writing stories, poetry, or scripts", "tag": "Words"},
            {"text": "Making music, singing, or performing", "tag": "Artistic"},
            {"text": "Designing products, buildings, or interiors", "tag": "Creative"}
        ]
    },
    {
        "question": "Do you notice details in design and aesthetics?",
        "category": "Design Awareness",
        "options": [
            {"text": "Yes! I notice fonts, colors, layouts everywhere", "tag": "Visual"},
            {"text": "I notice when things look good but can't explain why", "tag": "Artistic"},
            {"text": "I care more about function than appearance", "tag": "Realistic"},
            {"text": "I notice efficiency and organization more than beauty", "tag": "Conventional"}
        ]
    },

    # ============================================================
    # SECTION 8: SPECIFIC CAREER INTERESTS
    # ============================================================
    {
        "question": "Are you interested in computers and technology?",
        "category": "Tech Interest",
        "options": [
            {"text": "Yes! I love coding, building apps, or IT work", "tag": "Technical"},
            {"text": "Yes, but I prefer using tech for design/creative work", "tag": "Visual"},
            {"text": "I use tech as a tool but it's not my passion", "tag": "Business"},
            {"text": "Not really - I prefer working with people or nature", "tag": "Outdoor"}
        ]
    },
    {
        "question": "How do you feel about business and entrepreneurship?",
        "category": "Business Interest",
        "options": [
            {"text": "I dream of starting my own business someday", "tag": "Enterprising"},
            {"text": "I'd like a stable corporate career with good pay", "tag": "Business"},
            {"text": "Business is okay but I prefer technical/creative work", "tag": "Investigative"},
            {"text": "I'm more interested in helping people than making money", "tag": "Social"}
        ]
    },
    {
        "question": "Would you enjoy working with scientific research and experiments?",
        "category": "Science Interest",
        "options": [
            {"text": "Yes! I love lab work and discovering new things", "tag": "Scientific"},
            {"text": "Yes, especially if it helps solve health problems", "tag": "Healthcare"},
            {"text": "I prefer applying science practically, not research", "tag": "Realistic"},
            {"text": "Not really - I prefer people or creative work", "tag": "Artistic"}
        ]
    },
    {
        "question": "Are you interested in law, government, or public service?",
        "category": "Public Service Interest",
        "options": [
            {"text": "Yes, I want to serve the public or work in government", "tag": "Social"},
            {"text": "Yes, I'm interested in business law or management", "tag": "Enterprising"},
            {"text": "I prefer working in private sector", "tag": "Business"},
            {"text": "I'm more interested in science or creative fields", "tag": "Investigative"}
        ]
    },

    # ============================================================
    # SECTION 9: WORK VALUES
    # ============================================================
    {
        "question": "What's most important to you in a job?",
        "category": "Job Priority",
        "options": [
            {"text": "High salary and financial rewards", "tag": "Enterprising"},
            {"text": "Job security and work-life balance", "tag": "Conventional"},
            {"text": "Meaningful work that helps others", "tag": "Social"},
            {"text": "Freedom to be creative and innovate", "tag": "Artistic"}
        ]
    },
    {
        "question": "How do you handle routine, repetitive tasks?",
        "category": "Routine Tolerance",
        "options": [
            {"text": "I like them - they're calming and predictable", "tag": "Conventional"},
            {"text": "I can do them if they're part of a bigger goal", "tag": "Realistic"},
            {"text": "I try to automate or optimize them", "tag": "Technical"},
            {"text": "I get bored quickly - I need variety", "tag": "Creative"}
        ]
    },
    {
        "question": "How important is it that your work helps society?",
        "category": "Social Impact",
        "options": [
            {"text": "Very important - I want to make a difference", "tag": "Social"},
            {"text": "Important, but I also need good compensation", "tag": "Enterprising"},
            {"text": "Nice to have, but not my main priority", "tag": "Realistic"},
            {"text": "I'd rather focus on interesting work than social impact", "tag": "Investigative"}
        ]
    },

    # ============================================================
    # SECTION 10: SCENARIO-BASED QUESTIONS
    # ============================================================
    {
        "question": "Your school needs help with a project. Which do you choose?",
        "category": "Project Choice",
        "options": [
            {"text": "Build or repair something physical (stage, furniture)", "tag": "Realistic"},
            {"text": "Create promotional materials (posters, videos)", "tag": "Visual"},
            {"text": "Organize the logistics and manage the team", "tag": "Enterprising"},
            {"text": "Tutor students or help with counseling", "tag": "Social"}
        ]
    },
    {
        "question": "A new app idea pops into your head. What excites you most?",
        "category": "App Development",
        "options": [
            {"text": "Writing the code and building the backend", "tag": "Technical"},
            {"text": "Designing the user interface and visuals", "tag": "Visual"},
            {"text": "Planning the business model and marketing", "tag": "Enterprising"},
            {"text": "How it could help people solve a problem", "tag": "Social"}
        ]
    },
    {
        "question": "You're watching a nature documentary. What interests you most?",
        "category": "Nature Interest",
        "options": [
            {"text": "The animals and ecosystems - I want to protect them", "tag": "Outdoor"},
            {"text": "The science - how things evolved and work", "tag": "Scientific"},
            {"text": "The cinematography - beautiful shots and editing", "tag": "Visual"},
            {"text": "The story of the people trying to help", "tag": "Social"}
        ]
    },
    {
        "question": "At a career fair, which booth would you visit first?",
        "category": "Career Fair",
        "options": [
            {"text": "Engineering/Tech companies", "tag": "Technical"},
            {"text": "Hospitals/Healthcare organizations", "tag": "Healthcare"},
            {"text": "Banks/Business corporations", "tag": "Business"},
            {"text": "Design studios/Creative agencies", "tag": "Artistic"}
        ]
    },
    {
        "question": "If you could shadow someone for a day, who would it be?",
        "category": "Role Model",
        "options": [
            {"text": "A scientist working in a lab", "tag": "Scientific"},
            {"text": "A doctor or nurse helping patients", "tag": "Healthcare"},
            {"text": "A CEO running a company", "tag": "Enterprising"},
            {"text": "An artist or designer creating work", "tag": "Artistic"}
        ]
    },
    {
        "question": "Which achievement would make your parents proudest?",
        "category": "Achievement Pride",
        "options": [
            {"text": "Becoming a successful engineer or scientist", "tag": "Investigative"},
            {"text": "Becoming a doctor, nurse, or healthcare professional", "tag": "Healthcare"},
            {"text": "Starting a successful business", "tag": "Enterprising"},
            {"text": "Becoming a recognized artist or creative professional", "tag": "Artistic"}
        ]
    },

    # ============================================================
    # SECTION 11: DIRECT CAREER PATH QUESTIONS
    # ============================================================
    {
        "question": "Which career path sounds most interesting to you?",
        "category": "Career Path A",
        "options": [
            {"text": "Software Developer, Data Scientist, or IT Specialist", "tag": "Technical"},
            {"text": "Doctor, Nurse, Physical Therapist, or Pharmacist", "tag": "Healthcare"},
            {"text": "Accountant, Financial Analyst, or Business Manager", "tag": "Business"},
            {"text": "Architect, Graphic Designer, or Animator", "tag": "Visual"}
        ]
    },
    {
        "question": "Which career path sounds most interesting to you?",
        "category": "Career Path B",
        "options": [
            {"text": "Civil Engineer, Mechanical Engineer, or Electrician", "tag": "Realistic"},
            {"text": "Teacher, Counselor, or Social Worker", "tag": "Social"},
            {"text": "Entrepreneur, Marketing Manager, or Sales Director", "tag": "Enterprising"},
            {"text": "Marine Biologist, Environmental Scientist, or Geologist", "tag": "Outdoor"}
        ]
    },
    {
        "question": "Which career path sounds most interesting to you?",
        "category": "Career Path C",
        "options": [
            {"text": "Researcher, Scientist, or Professor", "tag": "Scientific"},
            {"text": "Journalist, Writer, or Communications Specialist", "tag": "Words"},
            {"text": "Athlete, Fitness Trainer, or Physical Education Teacher", "tag": "Physical"},
            {"text": "Accountant, Auditor, or Administrative Manager", "tag": "Conventional"}
        ]
    },

    # ============================================================
    # SECTION 12: TIEBREAKER / CLARIFICATION QUESTIONS
    # ============================================================
    {
        "question": "When you think about your dream job, it involves:",
        "category": "Dream Job",
        "options": [
            {"text": "Working with my hands and seeing physical results", "tag": "Realistic"},
            {"text": "Thinking deeply and solving complex puzzles", "tag": "Investigative"},
            {"text": "Interacting with people and building relationships", "tag": "Social"},
            {"text": "Creating original work that expresses my vision", "tag": "Artistic"}
        ]
    },
    {
        "question": "If you had to choose, would you rather:",
        "category": "Either-Or",
        "options": [
            {"text": "Work with THINGS (machines, tools, systems)", "tag": "Realistic"},
            {"text": "Work with IDEAS (theories, research, concepts)", "tag": "Investigative"},
            {"text": "Work with PEOPLE (helping, teaching, leading)", "tag": "Social"},
            {"text": "Work with DATA (numbers, records, analysis)", "tag": "Numbers"}
        ]
    },
    {
        "question": "Your ideal work results in:",
        "category": "Work Output",
        "options": [
            {"text": "Something built or repaired that works well", "tag": "Realistic"},
            {"text": "New knowledge or discoveries published", "tag": "Scientific"},
            {"text": "People helped, healed, or educated", "tag": "Social"},
            {"text": "Beautiful designs or creative content", "tag": "Artistic"}
        ]
    },
    {
        "question": "Which skill do you most want to develop?",
        "category": "Skill Development",
        "options": [
            {"text": "Technical skills - coding, engineering, mechanics", "tag": "Technical"},
            {"text": "People skills - communication, empathy, leadership", "tag": "Social"},
            {"text": "Analytical skills - research, data analysis, logic", "tag": "Investigative"},
            {"text": "Creative skills - design, art, innovation", "tag": "Artistic"}
        ]
    },
    {
        "question": "In 10 years, you hope to be known as someone who:",
        "category": "Future Identity",
        "options": [
            {"text": "Built or created something impressive", "tag": "Realistic"},
            {"text": "Made important discoveries or innovations", "tag": "Investigative"},
            {"text": "Helped many people improve their lives", "tag": "Social"},
            {"text": "Led a successful organization or business", "tag": "Enterprising"}
        ]
    },

    # ============================================================
    # SECTION 13: ADDITIONAL COVERAGE QUESTIONS
    # ============================================================
    {
        "question": "Which after-school activity would you choose?",
        "category": "Extracurricular",
        "options": [
            {"text": "Robotics club or tech workshop", "tag": "Technical"},
            {"text": "Theater, art club, or school paper", "tag": "Artistic"},
            {"text": "Student council or community service", "tag": "Social"},
            {"text": "Sports team or outdoor adventure club", "tag": "Physical"}
        ]
    },
    {
        "question": "When watching news, which stories interest you most?",
        "category": "News Interest",
        "options": [
            {"text": "New technology, gadgets, and scientific discoveries", "tag": "Investigative"},
            {"text": "Business news, economy, and entrepreneurship", "tag": "Enterprising"},
            {"text": "Social issues, community stories, and human interest", "tag": "Social"},
            {"text": "Environmental news and nature documentaries", "tag": "Outdoor"}
        ]
    },
    {
        "question": "If you could have any superpower, what would it be?",
        "category": "Superpower",
        "options": [
            {"text": "Super intelligence - understand anything instantly", "tag": "Investigative"},
            {"text": "Healing powers - cure any illness", "tag": "Healthcare"},
            {"text": "Creativity - create anything I imagine", "tag": "Creative"},
            {"text": "Leadership - inspire anyone to follow me", "tag": "Enterprising"}
        ]
    },
    {
        "question": "What kind of books/content do you prefer?",
        "category": "Reading Preference",
        "options": [
            {"text": "Science, technology, or how-things-work", "tag": "Scientific"},
            {"text": "Business, success stories, or self-improvement", "tag": "Business"},
            {"text": "Fiction, poetry, or creative writing", "tag": "Words"},
            {"text": "Art books, design magazines, or visual content", "tag": "Visual"}
        ]
    },
    {
        "question": "Your friends would describe you as someone who:",
        "category": "Friend Perception",
        "options": [
            {"text": "Fixes things and solves practical problems", "tag": "Realistic"},
            {"text": "Always has creative ideas and artistic flair", "tag": "Artistic"},
            {"text": "Is always there to help and listen", "tag": "Social"},
            {"text": "Takes charge and organizes group activities", "tag": "Enterprising"}
        ]
    },
    {
        "question": "What frustrates you most?",
        "category": "Frustration",
        "options": [
            {"text": "Disorganization and chaos - I like things orderly", "tag": "Conventional"},
            {"text": "Boring, repetitive tasks - I need variety", "tag": "Creative"},
            {"text": "Working alone - I need human interaction", "tag": "Social"},
            {"text": "Sitting still - I need to be active", "tag": "Physical"}
        ]
    },
    {
        "question": "Which gift would you be most excited to receive?",
        "category": "Gift Preference",
        "options": [
            {"text": "High-end laptop or latest tech gadget", "tag": "Technical"},
            {"text": "Professional art supplies or camera", "tag": "Visual"},
            {"text": "Travel voucher for adventure trip", "tag": "Outdoor"},
            {"text": "Course or workshop to learn new skills", "tag": "Investigative"}
        ]
    },
    {
        "question": "In a team competition, you want to be responsible for:",
        "category": "Team Role",
        "options": [
            {"text": "The technical/practical execution", "tag": "Realistic"},
            {"text": "Research and strategy planning", "tag": "Investigative"},
            {"text": "Design and presentation", "tag": "Visual"},
            {"text": "Team coordination and morale", "tag": "Social"}
        ]
    },
    {
        "question": "Which workplace perk matters most to you?",
        "category": "Workplace Perk",
        "options": [
            {"text": "Access to latest technology and equipment", "tag": "Technical"},
            {"text": "Creative freedom and flexible hours", "tag": "Artistic"},
            {"text": "Great team and positive work culture", "tag": "Social"},
            {"text": "High salary and career advancement", "tag": "Enterprising"}
        ]
    },
    {
        "question": "How do you usually spend your allowance/savings?",
        "category": "Spending Habit",
        "options": [
            {"text": "Tech gadgets, games, or equipment", "tag": "Technical"},
            {"text": "Food, experiences with friends, or gifts", "tag": "Social"},
            {"text": "Art supplies, music, or creative hobbies", "tag": "Artistic"},
            {"text": "Save it or invest for the future", "tag": "Conventional"}
        ]
    },
    {
        "question": "What makes you feel most accomplished?",
        "category": "Accomplishment",
        "options": [
            {"text": "Completing a difficult technical challenge", "tag": "Problem-solving"},
            {"text": "Creating something beautiful or original", "tag": "Creative"},
            {"text": "Helping someone succeed or feel better", "tag": "Social"},
            {"text": "Achieving a goal or winning a competition", "tag": "Enterprising"}
        ]
    },
    {
        "question": "If you had to teach a class, what subject would you choose?",
        "category": "Teaching Subject",
        "options": [
            {"text": "Math, Science, or Computer class", "tag": "Numbers"},
            {"text": "Art, Music, or Creative writing", "tag": "Artistic"},
            {"text": "PE, Sports, or Health class", "tag": "Physical"},
            {"text": "Filipino, English, or Social Studies", "tag": "Words"}
        ]
    },
    {
        "question": "What's your ideal vacation?",
        "category": "Vacation Style",
        "options": [
            {"text": "Adventure trip - hiking, camping, exploring nature", "tag": "Outdoor"},
            {"text": "City trip - museums, restaurants, cultural sites", "tag": "Artistic"},
            {"text": "Beach resort - relaxing with friends and family", "tag": "Social"},
            {"text": "Staycation - working on personal projects at home", "tag": "Investigative"}
        ]
    },
]


# Trait mapping for reference (to verify questions cover all traits)
TRAIT_COVERAGE = {
    # RIASEC
    "Realistic": "Building, fixing, hands-on work",
    "Investigative": "Research, analysis, understanding",
    "Artistic": "Creative expression, design, performance",
    "Social": "Helping, teaching, caring for others",
    "Enterprising": "Leading, persuading, business",
    "Conventional": "Organizing, detailed work, procedures",
    
    # Skills
    "Technical": "Technology, computers, programming",
    "Scientific": "Lab work, experiments, research",
    "Numbers": "Math, statistics, data analysis",
    "Words": "Writing, speaking, languages",
    "Visual": "Design, images, spatial thinking",
    "Physical": "Sports, movement, active work",
    
    # Environment
    "Outdoor": "Nature, fieldwork, outside",
    "Healthcare": "Medical settings, patient care",
    "Business": "Corporate, commerce, trade",
    
    # Bonus
    "Problem-solving": "Tackling challenges, finding solutions",
    "Creative": "Original ideas, innovation",
}
