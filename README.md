# CoursePro: College Course Recommendation System

## 📋 Project Overview

CoursePro is a web-based **College Course Recommendation System** designed to help Senior High School (SHS) students in the Philippines identify suitable college courses based on their personality traits, academic performance, and career interests.

The system uses a **Hybrid Recommendation Algorithm** combining **Rule-Based Logic** and **Decision Tree Classification** to provide accurate, explainable recommendations.

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           COURSEPRO SYSTEM                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   ┌──────────────┐         ┌──────────────┐         ┌──────────────┐       │
│   │   FRONTEND   │ ◄─────► │   BACKEND    │ ◄─────► │   DATABASE   │       │
│   │   (React)    │  REST   │  (FastAPI)   │   SQL   │ (PostgreSQL) │       │
│   │   Port 3000  │  API    │   Port 8000  │         │   Port 5432  │       │
│   └──────────────┘         └──────────────┘         └──────────────┘       │
│                                   │                                         │
│                                   ▼                                         │
│                    ┌──────────────────────────────┐                        │
│                    │  RECOMMENDATION ENGINE       │                        │
│                    │  • Rule-Based Filtering      │                        │
│                    │  • Decision Tree Classifier  │                        │
│                    └──────────────────────────────┘                        │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Technology Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| Frontend | React.js | User interface |
| Backend | FastAPI (Python) | REST API server |
| Database | PostgreSQL | Data persistence |
| Algorithm | Custom Python | Recommendation engine |

---

## 📁 Project Structure

```
Course-Recommendation-System/
├── frontend/                    # React Frontend Application
│   ├── src/
│   │   ├── App.js              # Main application component
│   │   ├── Login.js            # User login page
│   │   ├── Signup.js           # User registration page
│   │   ├── Dashboard.js        # User dashboard
│   │   ├── ProfileForm.js      # Academic profile form (GWA, Strand)
│   │   ├── AssessmentForm.js   # Career assessment questionnaire
│   │   ├── ResultsView.js      # Recommendation results display
│   │   └── admin/              # Admin panel components
│   │       ├── Admin.js
│   │       ├── ManageCourse.js
│   │       ├── ManageQuestion.js
│   │       ├── ViewReport.js
│   │       └── ViewUser.js
│   └── package.json
│
├── backend/                     # FastAPI Backend Application
│   ├── main.py                 # API endpoints & recommendation logic
│   ├── models.py               # SQLAlchemy database models
│   ├── database.py             # Database connection
│   ├── schema.py               # Pydantic schemas
│   ├── security.py             # Password hashing
│   ├── seed_data.py            # Course & question data (193 questions, 99 courses)
│   ├── recommendation_engine.py # Hybrid algorithm implementation
│   ├── trait_mapping.py        # Trait standardization
│   ├── assessment_service.py   # Assessment tier management
│   └── requirements.txt        # Python dependencies
│
└── README.md                    # This documentation
```

---

## 🔄 Data Flow Diagram (DFD)

The system follows a structured data flow based on the thesis DFD:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          DATA FLOW DIAGRAM                                   │
└─────────────────────────────────────────────────────────────────────────────┘

    [User]
       │
       ▼
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Process 1:   │────►│ Process 2:   │────►│ Process 3:   │
│ User Login   │     │ Fill Profile │     │ View Profile │
└──────────────┘     └──────────────┘     └──────────────┘
       │                    │                    │
       ▼                    ▼                    │
   D1: User            D4: Personal &            │
   Accounts            Academic DB               │
                                                 ▼
                      ┌──────────────┐     ┌──────────────┐
                      │ Process 5:   │◄────│ Process 4:   │
                      │ Take Test    │     │ View Questions│
                      └──────────────┘     └──────────────┘
                             │                    ▲
                             │                    │
                             ▼                D2: Question
                      D5: Test Attempt           Pool
                             │
                             ▼
                      ┌──────────────┐
                      │ Process 6:   │
                      │ Rule-Based   │◄─── PHASE 1: IF-THEN Filtering
                      │ Logic        │
                      └──────────────┘
                             │
                             ▼
                      ┌──────────────┐
                      │ Process 7:   │
                      │ Decision     │◄─── PHASE 2: Tree Classification
                      │ Tree         │
                      └──────────────┘
                             │
                             ▼
                      D6: Course DB
                             │
                             ▼
                      ┌──────────────┐
                      │ Process 8:   │
                      │ Generate     │
                      │ Recommend    │
                      └──────────────┘
                             │
                             ▼
                      D7: Recommendation
                          Results
                             │
                             ▼
                         [User]
```

### Data Stores

| Store | Name | Contents |
|-------|------|----------|
| D1 | User Accounts | Login credentials, user profiles |
| D2 | Question Pool | 193 assessment questions |
| D3 | Course Database | 99 Philippine college courses |
| D4 | Personal & Academic DB | GWA, strand, interests |
| D5 | Test Attempt DB | User assessment responses |
| D6 | Trait Scores | Calculated personality traits |
| D7 | Recommendations | Final course recommendations |

---

## 🧠 Recommendation Algorithm

### Theoretical Framework

The algorithm is based on established theories from the thesis:

1. **Rule-Based Expert Systems Theory** (Giarratano & Riley, 2005)
2. **Decision Tree Algorithm Theory** (Quinlan, 1986)
3. **Hybrid Recommender Systems Theory** (Burke, 2002)
4. **Holland's Theory (RIASEC)** for career interest mapping

### Two-Phase Hybrid Approach

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    HYBRID RECOMMENDATION ALGORITHM                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   INPUT: User Profile + Assessment Answers + Trait Scores                   │
│                                                                              │
│   ═══════════════════════════════════════════════════════════════════════   │
│   ║                  PHASE 1: RULE-BASED FILTERING                      ║   │
│   ║                  (Giarratano & Riley, 2005)                         ║   │
│   ═══════════════════════════════════════════════════════════════════════   │
│                                                                              │
│   Applies IF-THEN rules to filter and score courses:                        │
│                                                                              │
│   ELIGIBILITY RULES (Hard Constraints):                                     │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │ E1: IF user_gwa < course_minimum_gwa - 5 THEN mark INELIGIBLE       │  │
│   │ E2: IF strand completely incompatible THEN apply heavy penalty      │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│                                                                              │
│   PREFERENCE RULES (Soft Constraints - Add Points):                         │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │ P1: IF primary_trait IN course_traits THEN +15 points               │  │
│   │ P2: IF trait_matches >= 3 THEN +10 points (synergy bonus)           │  │
│   │ P3: IF course IN user's career_path THEN +20 points                 │  │
│   │ P4: IF user_gwa exceeds requirement by 5+ THEN +8 points            │  │
│   │ P5: IF strand perfectly matches THEN +12 points                     │  │
│   │ P6: IF work environment preference matches THEN +6 points           │  │
│   │ P7: IF learning style matches THEN +5 points                        │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│                                                                              │
│   PENALTY RULES (Subtract Points):                                          │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │ N1: IF user_gwa < course_min THEN -(gap × 5) points                 │  │
│   │ N2: IF strand_mismatch THEN -10 points                              │  │
│   │ N3: IF no_trait_matches THEN -15 points                             │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│                                                                              │
│   OUTPUT: Eligibility Score + Rule Explanations for each course             │
│                                                                              │
│   ═══════════════════════════════════════════════════════════════════════   │
│   ║                PHASE 2: DECISION TREE CLASSIFICATION                ║   │
│   ║                (Quinlan, 1986)                                      ║   │
│   ═══════════════════════════════════════════════════════════════════════   │
│                                                                              │
│   Hierarchical classification tree:                                          │
│                                                                              │
│                        [ROOT: trait_category]                               │
│                               │                                              │
│          ┌───────────────────┼───────────────────┐                          │
│          │                   │                   │                          │
│      [helping]        [problem_solving]     [creative]      [leading]       │
│          │                   │                   │              │           │
│     [work_setting]    [analytical_type]   [creative_type]  [domain]        │
│          │                   │                   │              │           │
│    ┌─────┼─────┐      ┌─────┼─────┐       ┌─────┼─────┐    ┌───┼───┐       │
│ clinical office field  tech  business    visual perf write bus pub tech    │
│    │                    │                   │                              │
│ [gwa_level]        [gwa_level]        [tech_affinity]                      │
│    │                    │                   │                              │
│ high→healthcare_prof  high→engineering_cs   high→digital_media             │
│ med→healthcare_allied  med→it_technology    med→design_arts                │
│ low→healthcare_support low→tech_vocational  low→fine_arts                  │
│                                                                              │
│   LEAF NODES OUTPUT:                                                        │
│   • Classification (e.g., "healthcare_professional")                        │
│   • Confidence Score (0-100%)                                               │
│   • Score Boost (+15 to +25 for matching courses)                           │
│                                                                              │
│   ═══════════════════════════════════════════════════════════════════════   │
│   ║                    SCORE COMBINATION & RANKING                      ║   │
│   ═══════════════════════════════════════════════════════════════════════   │
│                                                                              │
│   Final Score = Phase 1 (Rule Score) + Phase 2 (Tree Boost)                 │
│                                                                              │
│   Priority Tiers:                                                           │
│   🌟 EXCELLENT: ≥3 traits + academic match + in predicted category          │
│   ✨ GOOD: Strong trait OR academic match                                   │
│   💡 FAIR: Some alignment, room for growth                                  │
│   🔍 EXPLORATORY: Consider for horizon expansion                            │
│                                                                              │
│   OUTPUT: Top 5 Recommendations with transparent reasoning                   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Trait Categories and Mappings

| Category | Associated Traits | Example Courses |
|----------|-------------------|-----------------|
| **Helping** | Helping-others, Empathetic, Compassionate, Service-oriented | BS Nursing, BS Social Work, Education |
| **Problem-Solving** | Analytical, Logical, Research-oriented, Methodical | BS Computer Science, Engineering |
| **Creative** | Creative-expression, Artistic-passion, Innovative | BS Multimedia Arts, Architecture |
| **Leading** | Leadership, Strategic, Big-picture, Ambitious | BS Business Administration, Public Admin |

### Strand Compatibility Matrix

```python
STRAND_COMPATIBILITY = {
    'STEM':   ['STEM', 'GAS'],
    'ABM':    ['ABM', 'GAS', 'HUMSS'],
    'HUMSS':  ['HUMSS', 'GAS', 'ABM'],
    'GAS':    ['STEM', 'ABM', 'HUMSS', 'GAS', 'TVL', 'Sports'],  # Most flexible
    'TVL':    ['TVL', 'GAS', 'STEM'],
    'Sports': ['Sports', 'GAS', 'HUMSS'],
}
```

---

## 📊 Assessment System

### Question Types

The system has **193 questions** across 7 different types:

| Type | Count | Description | Scoring |
|------|-------|-------------|---------|
| `standard` | ~150 | Yes/No personality questions | +1 per trait match |
| `scale` | ~15 | 1-5 Likert scale questions | Weighted multiplier |
| `career_path` | ~10 | Direct career preference | +2 weight + course boost |
| `extracurricular` | ~8 | Activity preferences | Multiple trait tags |
| `situational_mapped` | ~10 | Scenario-based questions | Trait + course mapping |

### Assessment Tiers

| Tier | Questions | Duration | Purpose |
|------|-----------|----------|---------|
| Quick | 20 | 5-10 min | Fast screening |
| Standard | 50 | 15-20 min | Balanced assessment |
| Comprehensive | 100 | 30-45 min | Full personality profile |
| Expert | 150 | 45-60 min | Maximum accuracy |

### Question Categories

1. **Academic Interests** - Subject preferences and learning styles
2. **Personality Traits** - Introvert/extrovert, analytical/creative
3. **Career Goals** - Work environment, salary expectations
4. **Skills Assessment** - Technical, communication, creative abilities
5. **Values & Priorities** - What matters most in a career

---

## 📚 Course Database

The system contains **99 Philippine college courses** covering:

### Course Categories

| Category | Example Courses |
|----------|-----------------|
| **Healthcare** | BS Nursing, BS Medical Technology, BS Pharmacy, BS Physical Therapy |
| **Engineering** | BS Civil Engineering, BS Computer Engineering, BS Mechanical Engineering |
| **IT & Computing** | BS Computer Science, BS Information Technology, BS Cybersecurity |
| **Business** | BS Accountancy, BS Business Administration, BS Entrepreneurship |
| **Education** | Bachelor of Elementary Education, Bachelor of Secondary Education |
| **Arts & Design** | BS Architecture, BS Multimedia Arts, BA in Fine Arts |
| **Sciences** | BS Biology, BS Chemistry, BS Marine Biology, BS Environmental Science |
| **Social Sciences** | BS Psychology, BA in Political Science, BS Social Work |
| **Agriculture** | BS Agriculture, BS Forestry, BS Fisheries |
| **Hospitality** | BS Hotel and Restaurant Management, BS Tourism Management |

### Course Data Structure

Each course includes:
- **Course Name** - Official program title
- **Description** - What the course is about
- **Trait Tags** - Personality traits that align (e.g., "Analytical, Problem-solving, Logical")
- **Minimum GWA** - Academic requirement (75-90)
- **Recommended Strand** - SHS track compatibility (STEM, ABM, HUMSS, GAS, TVL, Sports)

---

## 🔌 API Endpoints

### Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/signup` | Register new user |
| POST | `/login` | User login |
| POST | `/google-login` | Google OAuth login |

### User Profile

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/user/{id}/academic-info` | Get user's academic profile |
| PUT | `/user/{id}/academic-info` | Update GWA, strand, personal info |

### Assessment

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/questions` | Get 20 random questions |
| GET | `/assessment/tiers` | Get available assessment tiers |
| GET | `/assessment/start/{tier}` | Start tiered assessment |
| POST | `/recommend` | Submit answers & get recommendations |

### Recommendations

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/user/{id}/recommendations` | Get user's recommendation history |
| GET | `/user/{id}/recommendations/{attempt_id}` | Get specific attempt results |

### Admin

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/courses` | List all courses |
| POST | `/courses` | Add new course |
| PUT | `/courses/{id}` | Update course |
| DELETE | `/courses/{id}` | Delete course |
| GET | `/admin/questions` | List all questions |
| POST | `/admin/questions` | Add new question |
| PUT | `/admin/questions/{id}` | Update question |
| DELETE | `/admin/questions/{id}` | Delete question |
| GET | `/admin/reports` | View system reports |

---

## 📤 API Response Format

### Recommendation Response

```json
{
  "user_id": 1,
  "user_gwa": 90,
  "user_strand": "STEM",
  "detected_traits": [["Problem-solving", 8], ["Analytical", 6], ["Tech-savvy", 5]],
  "trait_analysis": {
    "primary_trait": "Problem-solving",
    "top_traits": ["Problem-solving", "Analytical", "Tech-savvy", "Logical"],
    "predicted_career_category": "Engineering Cs",
    "work_environments": ["office", "laboratory"],
    "total_traits_detected": 15
  },
  "recommendations": [
    {
      "rank": 1,
      "course_name": "BS Computer Science",
      "description": "Study of algorithms, programming, and computing systems",
      "matched_traits": ["Problem-solving", "Analytical", "Tech-savvy"],
      "minimum_gwa": 85.0,
      "recommended_strand": "STEM",
      "reasoning": "✓ Personality alignment: Problem-solving, Analytical, Tech-savvy | ✓ Matches your predicted career path: Engineering Cs | ✓ Meets all academic requirements | 🌟 Highly Recommended",
      "compatibility_score": 85,
      "confidence_score": 92.5,
      "priority_tier": "EXCELLENT",
      "match_details": {
        "trait_matches": 3,
        "rule_based_score": 60,
        "decision_tree_boost": 25,
        "in_predicted_category": true,
        "rule_explanations": [
          "✓ Primary Trait Alignment: Primary trait matches course requirements",
          "✓ Trait Synergy Bonus: 3 traits match",
          "✓ GWA Excellence: Exceeds requirement by 5.0 points"
        ]
      }
    }
  ],
  "algorithm_details": {
    "phase1_rule_based": {
      "description": "Rule-Based Filtering using IF-THEN logic (Giarratano & Riley, 2005)",
      "rules_applied": 12,
      "eligible_courses": 75,
      "ineligible_courses": 22
    },
    "phase2_decision_tree": {
      "description": "Decision Tree Classification (Quinlan, 1986)",
      "classification": "engineering_cs",
      "confidence": 0.9,
      "decision_path": ["trait_category=problem_solving", "analytical_type=technical", "gwa_level=high"]
    }
  },
  "algorithm_metrics": {
    "average_confidence": 87.5,
    "priority_distribution": {"excellent": 2, "good": 2, "fair": 1, "exploratory": 0},
    "total_courses_analyzed": 99,
    "matching_algorithm_version": "3.0-RuleBased-DecisionTree"
  }
}
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- Node.js 16+
- PostgreSQL 13+

### Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Configure database (create .env file)
echo "DATABASE_URL=postgresql://username:password@localhost:5432/coursepro_db" > .env

# Run server
uvicorn main:app --reload --port 8000
```

### Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Run development server
npm start
```

### Database Setup

The database is automatically seeded on first run with:
- 99 courses
- 193 questions
- Default assessment test

---

## 🔐 Security Features

- Password hashing using bcrypt
- Google OAuth integration
- CORS middleware configured
- SQL injection protection via SQLAlchemy ORM

---

## 📈 Algorithm Performance

### Scoring Metrics

| Metric | Description |
|--------|-------------|
| **Compatibility Score** | 0-100+ based on rule evaluations |
| **Confidence Score** | 0-100% certainty of recommendation |
| **Priority Tier** | EXCELLENT, GOOD, FAIR, EXPLORATORY |

### Transparency Features

Every recommendation includes:
1. **Matched Traits** - Which personality traits aligned
2. **Rule Explanations** - Why each rule passed/failed
3. **Decision Path** - How the decision tree classified the user
4. **Academic Fit** - GWA and strand compatibility

---

## 📚 References

1. Giarratano, J. C., & Riley, G. D. (2005). *Expert Systems: Principles and Programming*. Thomson Course Technology.

2. Quinlan, J. R. (1986). Induction of decision trees. *Machine Learning*, 1(1), 81-106.

3. Burke, R. (2002). Hybrid recommender systems: Survey and experiments. *User Modeling and User-Adapted Interaction*, 12(4), 331-370.

4. Holland, J. L. (1997). *Making Vocational Choices: A Theory of Vocational Personalities and Work Environments*. Psychological Assessment Resources.

---

## 👥 Contributors

- Thesis Authors: [Your Names Here]
- Course: [Your Course]
- University: [Your University]
- Academic Year: 2025-2026

---

## 📄 License

This project was developed as an academic thesis project.
