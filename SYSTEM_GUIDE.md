# 🎓 Course Recommendation System - Complete Guide

> **A Hybrid Recommendation System for Senior High School Students**  
> Using Rule-Based Logic + Decision Tree Algorithm

---

## 📋 Table of Contents

1. [System Overview](#1-system-overview)
2. [How It Works (User Flow)](#2-how-it-works-user-flow)
3. [The Algorithm Explained](#3-the-algorithm-explained)
4. [Trait System](#4-trait-system)
5. [Database Structure](#5-database-structure)
6. [Frontend Components](#6-frontend-components)
7. [Backend API Endpoints](#7-backend-api-endpoints)
8. [For Your Thesis Defense](#8-for-your-thesis-defense)

---

## 1. System Overview

### What Does This System Do?
This system helps **Senior High School (SHS) students** find the best **college courses** for them by analyzing:
- Their **personality traits** (from assessment questions)
- Their **academic profile** (GWA, SHS strand)
- Their **interests and skills**

### Technology Stack
| Component | Technology |
|-----------|------------|
| Frontend | ReactJS |
| Backend | Python + FastAPI |
| Database | SQLite (dev) / PostgreSQL (production) |
| Algorithm | Rule-Based Logic + Decision Tree |

### Theoretical Foundations
| Theory | Author | Used For |
|--------|--------|----------|
| Rule-Based Expert Systems | Giarratano & Riley (2005) | Filtering courses with IF-THEN rules |
| Decision Tree Algorithm | Quinlan (1986) | Ranking and classifying courses |
| Hybrid Recommender Systems | Burke (2002) | Combining multiple recommendation approaches |
| RIASEC Career Theory | Holland | Personality-based career matching |

---

## 2. How It Works (User Flow)

### Step-by-Step Journey

```
┌─────────────────────────────────────────────────────────────────────┐
│                         USER JOURNEY                                │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  1. SIGNUP/LOGIN                                                    │
│     └── User creates account with email/username                    │
│         └── Can login with username OR email                        │
│                                                                     │
│  2. COMPLETE PROFILE                                                │
│     └── Enter academic info:                                        │
│         • GWA (General Weighted Average)                            │
│         • SHS Strand (STEM, ABM, HUMSS, TVL, GAS, etc.)            │
│         • Age, Gender                                               │
│         • Academic Interests (select from categories)               │
│         • Skills (select from categories)                           │
│                                                                     │
│  3. TAKE ASSESSMENT                                                 │
│     └── Choose quiz length: 30, 50, or 60 questions                │
│     └── Answer situational questions ONE AT A TIME                  │
│     └── Each answer assigns TRAIT TAGS to your profile             │
│     └── System uses INFORMATION GAIN to pick next question         │
│         (This is the Decision Tree principle!)                      │
│                                                                     │
│  4. GET RECOMMENDATIONS                                             │
│     └── System calculates scores for all courses:                   │
│         • Phase 1: Rule-Based Filtering (IF-THEN rules)            │
│         • Phase 2: Decision Tree Classification (ranking)           │
│     └── Top 5 courses displayed with match percentages             │
│                                                                     │
│  5. PROVIDE FEEDBACK                                                │
│     └── Rate each recommendation (1-5 stars)                        │
│     └── Leave optional comments                                     │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 3. The Algorithm Explained

### Two-Phase Hybrid Approach

The system uses a **hybrid approach** combining two algorithms:

```
┌──────────────────────────────────────────────────────────────────┐
│                    RECOMMENDATION ALGORITHM                       │
├──────────────────────────────────────────────────────────────────┤
│                                                                   │
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │ PHASE 1: RULE-BASED FILTERING                               │ │
│  │ (Giarratano & Riley, 2005)                                  │ │
│  │                                                              │ │
│  │ Applies IF-THEN rules to calculate eligibility scores:      │ │
│  │                                                              │ │
│  │  Rule A1: GWA Bonus                                         │ │
│  │  IF user_gwa >= course_minimum_gwa                          │ │
│  │  THEN add +10 bonus points                                  │ │
│  │                                                              │ │
│  │  Rule A2: Strand Alignment                                  │ │
│  │  IF user_strand matches course_required_strand              │ │
│  │  THEN add +8 bonus points                                   │ │
│  │                                                              │ │
│  │  Rule P1: Primary Trait Match (HIGHEST PRIORITY)            │ │
│  │  IF user_primary_trait IN course_traits                     │ │
│  │  THEN add +20 bonus points                                  │ │
│  │                                                              │ │
│  │  Rule P2: Trait Synergy                                     │ │
│  │  IF trait_matches >= 3                                      │ │
│  │  THEN add +15 bonus points                                  │ │
│  │                                                              │ │
│  │  Rule P3: Career Path Match                                 │ │
│  │  IF user_selected_career_path maps to course                │ │
│  │  THEN add +25 bonus points                                  │ │
│  │                                                              │ │
│  │  Rule P8: Interests/Skills Bonus                            │ │
│  │  IF user_interests/skills keywords match course traits      │ │
│  │  THEN add up to +25 bonus points                            │ │
│  │                                                              │ │
│  │  Rule N3: No Trait Match Penalty                            │ │
│  │  IF no user_traits match course_traits                      │ │
│  │  THEN subtract -15 points                                   │ │
│  │                                                              │ │
│  └─────────────────────────────────────────────────────────────┘ │
│                              ↓                                    │
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │ PHASE 2: DECISION TREE CLASSIFICATION                       │ │
│  │ (Quinlan, 1986)                                             │ │
│  │                                                              │ │
│  │ Traverses a decision tree to add final score modifiers:     │ │
│  │                                                              │ │
│  │                    [ROOT: trait_category]                   │ │
│  │                    /         |         \                    │ │
│  │           Helping     Problem-Solving   Creative            │ │
│  │             /                |              \               │ │
│  │    [work_setting]    [analytical_type]   [expression]       │ │
│  │    /     |    \        /     |     \       /    \           │ │
│  │ clinical office field tech business  visual performance     │ │
│  │    |       |     |     |       |       |        |           │ │
│  │ [gwa_level] ...      [gwa_level]   [LEAF: arts_visual]     │ │
│  │  /   |   \            /   |   \                             │ │
│  │ high med low        high med low                            │ │
│  │  |    |    |          |    |    |                           │ │
│  │ LEAF LEAF LEAF      LEAF LEAF LEAF                          │ │
│  │                                                              │ │
│  │ Each LEAF node has:                                         │ │
│  │ - classification (e.g., "healthcare_professional")          │ │
│  │ - confidence (0.0 - 1.0)                                    │ │
│  │ - score_modifier (+15 to +25 points)                        │ │
│  │                                                              │ │
│  └─────────────────────────────────────────────────────────────┘ │
│                              ↓                                    │
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │ FINAL SCORE = Rule Score + Decision Tree Score              │ │
│  │ Top 5 courses with highest scores are recommended           │ │
│  └─────────────────────────────────────────────────────────────┘ │
│                                                                   │
└──────────────────────────────────────────────────────────────────┘
```

### Adaptive Assessment (Information Gain)

The assessment uses **Information Gain** (the same formula used in Decision Tree construction) to select questions:

```
┌─────────────────────────────────────────────────────────────────┐
│                ADAPTIVE QUESTION SELECTION                       │
│                (Decision Tree Principles)                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  For each unanswered question, calculate INFORMATION GAIN:       │
│                                                                  │
│  Information Gain = Entropy(before) - Entropy(after)             │
│                                                                  │
│  Where Entropy = -Σ p(x) * log2(p(x))                           │
│                                                                  │
│  The question with HIGHEST information gain is selected next!    │
│                                                                  │
│  Why? Because it best discriminates between remaining courses.   │
│                                                                  │
│  Example:                                                        │
│  - 50 courses remain as candidates                               │
│  - Question A: would split into 25/25 (high info gain)           │
│  - Question B: would split into 48/2 (low info gain)             │
│  - System picks Question A (better discrimination)               │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 4. Trait System

### What Are Traits?

Traits are personality/interest markers assigned when users answer questions. Each answer option has a `trait_tag` that gets added to the user's profile.

### Trait Categories

```
┌─────────────────────────────────────────────────────────────────┐
│                      TRAIT SYSTEM                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  RIASEC TYPES (Holland's Theory):                                │
│  ├── Realistic      (hands-on, practical)                        │
│  ├── Investigative  (analytical, research-oriented)              │
│  ├── Artistic       (creative, expressive)                       │
│  ├── Social         (helping, teaching)                          │
│  ├── Enterprising   (leading, persuading)                        │
│  └── Conventional   (organizing, data-focused)                   │
│                                                                  │
│  CAREER PATH TRAITS (22 unique paths):                           │
│  ├── Healthcare: Patient-Care, Medical-Lab, Rehab-Therapy        │
│  ├── Technology: Software-Dev, Hardware-Systems, Data-Analytics  │
│  ├── Engineering: Civil-Build, Electrical-Power, Mechanical      │
│  ├── Business: Finance-Acct, Marketing-Sales, Startup-Venture    │
│  ├── Education: Teaching-Ed                                      │
│  ├── Arts: Visual-Design, Digital-Media, Spatial-Design          │
│  ├── Science: Lab-Research, Field-Research                       │
│  ├── Public Service: Law-Enforce, Community-Serve                │
│  └── Others: Maritime-Sea, Agri-Nature, Hospitality-Svc          │
│                                                                  │
│  SKILL TRAITS:                                                   │
│  ├── Technical-Skill                                             │
│  ├── People-Skill                                                │
│  ├── Creative-Skill                                              │
│  ├── Analytical-Skill                                            │
│  ├── Physical-Skill                                              │
│  └── Admin-Skill                                                 │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### How Traits Are Matched to Courses

Each course in the database has a `trait_tag` field with comma-separated traits:

```
Example Course: BS Computer Science
trait_tag: "Software-Dev, Technical-Skill, Investigative, Data-Analytics"

Example Course: BS Nursing
trait_tag: "Patient-Care, Social, People-Skill, Healthcare"
```

When calculating recommendations:
1. User's accumulated traits are compared to each course's traits
2. More matches = higher score
3. Trait relationships are also considered (e.g., Software-Dev is related to Data-Analytics)

### Trait Relationships

Traits have relationships with similarity scores (0.0 - 1.0):

```python
"Software-Dev": {
    "Investigative": 0.8,      # Strong relationship
    "Technical-Skill": 0.9,    # Very strong
    "Data-Analytics": 0.6,     # Moderate
    "Hardware-Systems": 0.4,   # Weak but present
}
```

This allows **partial matching** - if a user has "Software-Dev" trait, they get partial credit for courses requiring "Data-Analytics".

---

## 5. Database Structure

### Entity Relationship Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                    DATABASE SCHEMA                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────────┐       ┌──────────────┐                        │
│  │    USERS     │       │    TESTS     │                        │
│  ├──────────────┤       ├──────────────┤                        │
│  │ user_id (PK) │       │ test_id (PK) │                        │
│  │ username     │       │ test_name    │                        │
│  │ email        │       │ test_type    │                        │
│  │ password_hash│       │ description  │                        │
│  │ first_name   │       └──────┬───────┘                        │
│  │ last_name    │              │                                │
│  │ academic_info│  (JSON: GWA, strand, age, gender, etc.)       │
│  │ created_at   │              │                                │
│  │ last_active  │              │                                │
│  └──────┬───────┘              │                                │
│         │                      │                                │
│         │         ┌────────────┴────────────┐                   │
│         │         │                         │                   │
│         │         ▼                         ▼                   │
│         │  ┌──────────────┐         ┌──────────────┐            │
│         │  │  QUESTIONS   │         │ TEST_ATTEMPTS│            │
│         │  ├──────────────┤         ├──────────────┤            │
│         │  │ question_id  │         │ attempt_id   │◄───────┐   │
│         │  │ test_id (FK) │         │ user_id (FK) │        │   │
│         │  │ question_text│         │ test_id (FK) │        │   │
│         │  │ category     │         │ taken_at     │        │   │
│         │  │ question_type│         │ max_questions│        │   │
│         │  └──────┬───────┘         │ confidence   │        │   │
│         │         │                 └──────┬───────┘        │   │
│         │         │                        │                │   │
│         │         ▼                        │                │   │
│         │  ┌──────────────┐                │                │   │
│         │  │   OPTIONS    │                │                │   │
│         │  ├──────────────┤                │                │   │
│         │  │ option_id    │                │                │   │
│         │  │ question_id  │                │                │   │
│         │  │ option_text  │                │                │   │
│         │  │ trait_tag    │◄── This is where traits come from   │
│         │  │ weight       │                │                │   │
│         │  └──────────────┘                │                │   │
│         │                                  │                │   │
│         │                                  ▼                │   │
│         │                         ┌──────────────────┐      │   │
│         │                         │ STUDENT_ANSWERS  │      │   │
│         │                         ├──────────────────┤      │   │
│         │                         │ answer_id        │      │   │
│         │                         │ attempt_id (FK)  │──────┘   │
│         │                         │ question_id (FK) │          │
│         │                         │ chosen_option_id │          │
│         │                         └──────────────────┘          │
│         │                                                       │
│         │         ┌──────────────┐                              │
│         │         │   COURSES    │                              │
│         │         ├──────────────┤                              │
│         │         │ course_id    │                              │
│         │         │ course_name  │                              │
│         │         │ description  │                              │
│         │         │ trait_tag    │◄── Comma-separated traits    │
│         │         │ required_strand│                            │
│         │         │ minimum_gwa  │                              │
│         │         └──────┬───────┘                              │
│         │                │                                      │
│         │                │                                      │
│         ▼                ▼                                      │
│  ┌────────────────────────────┐                                 │
│  │     RECOMMENDATIONS        │                                 │
│  ├────────────────────────────┤                                 │
│  │ recommendation_id          │                                 │
│  │ attempt_id (FK)            │                                 │
│  │ user_id (FK)               │                                 │
│  │ course_id (FK)             │                                 │
│  │ reasoning                  │                                 │
│  │ recommended_at             │                                 │
│  └────────────┬───────────────┘                                 │
│               │                                                 │
│               ▼                                                 │
│  ┌────────────────────────────┐                                 │
│  │ RECOMMENDATION_FEEDBACK    │                                 │
│  ├────────────────────────────┤                                 │
│  │ feedback_id                │                                 │
│  │ recommendation_id (FK)     │                                 │
│  │ user_id (FK)               │                                 │
│  │ rating (1-5 stars)         │                                 │
│  │ feedback_text              │                                 │
│  │ created_at                 │                                 │
│  └────────────────────────────┘                                 │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 6. Frontend Components

### Component Structure

```
frontend/src/
├── App.js                 # Main app with routing logic
├── LandingPage.js         # Welcome page
├── Login.js               # Login (username OR email)
├── Signup.js              # User registration
├── Dashboard.js           # Main user dashboard
├── ProfileForm.js         # Academic profile editor
├── AdaptiveAssessment.js  # The assessment quiz
├── ResultsView.js         # Shows recommendations
├── FeedbackForm.js        # Collect user feedback
├── MyActivity.js          # User's history
└── admin/
    ├── Admin.js           # Admin dashboard
    ├── ManageCourse.js    # CRUD for courses
    ├── ManageQuestion.js  # CRUD for questions
    ├── ViewUser.js        # View all users
    ├── ViewFeedback.js    # View all feedback
    └── ViewReport.js      # Analytics/reports
```

### Key Components Explained

| Component | Purpose |
|-----------|---------|
| **AdaptiveAssessment.js** | Handles the quiz - shows one question at a time, sends answers to backend, receives next question based on Information Gain |
| **ResultsView.js** | Displays the top 5 recommended courses with match percentages and reasoning |
| **ProfileForm.js** | Collects GWA, strand, age, gender, interests, and skills |
| **Dashboard.js** | Central hub - shows profile summary, start assessment button, view history |

---

## 7. Backend API Endpoints

### Authentication

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/signup` | POST | Create new user account |
| `/login` | POST | Login with username OR email |
| `/google-login` | POST | Login via Google OAuth |
| `/google-register` | POST | Complete Google registration |

### User Profile

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/user/{id}/academic-info` | GET | Get user's academic profile |
| `/user/{id}/academic-info` | PUT | Update academic profile |

### Assessment

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/adaptive/start` | POST | Start new assessment session |
| `/adaptive/answer` | POST | Submit answer, get next question |
| `/adaptive/previous` | POST | Go back to previous question |
| `/adaptive/finish` | POST | End early and get recommendations |

### Recommendations

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/recommendations/{user_id}` | GET | Get user's past recommendations |

### Feedback

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/feedback/submit` | POST | Submit feedback for recommendation |

### Admin

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/admin/courses` | GET/POST | List/create courses |
| `/admin/courses/{id}` | PUT/DELETE | Update/delete course |
| `/admin/questions` | GET/POST | List/create questions |
| `/admin/users` | GET | List all users |
| `/admin/feedback` | GET | List all feedback |

---

## 8. For Your Thesis Defense

### Key Points to Explain

1. **Why Hybrid Approach?**
   - Rule-Based alone is too rigid (binary yes/no)
   - Decision Tree alone needs training data
   - Hybrid combines structured rules with intelligent ranking

2. **Why Information Gain for Question Selection?**
   - Same formula used in Decision Tree construction (ID3/C4.5)
   - Maximizes discrimination between candidate courses
   - Makes the assessment adaptive and efficient

3. **How Do Traits Connect Everything?**
   - Questions → Options → trait_tags → User Profile
   - Courses → trait_tags
   - Matching = comparing user traits to course traits

4. **What Makes This System "Intelligent"?**
   - Adaptive question selection (not random)
   - Considers relationships between traits
   - Weighs multiple factors (academic + personality + interests)

### Algorithm Flow Summary

```
User answers question
        ↓
trait_tag added to user profile
        ↓
Information Gain calculated for remaining questions
        ↓
Next best question selected
        ↓
... (repeat until done) ...
        ↓
Phase 1: Rule-Based Filter calculates base scores
        ↓
Phase 2: Decision Tree adds classification bonuses
        ↓
Final scores sorted → Top 5 recommendations displayed
```

### Theoretical References

| Concept | Citation |
|---------|----------|
| Rule-Based Expert Systems | Giarratano, J.C. & Riley, G.D. (2005). Expert Systems: Principles and Programming |
| Decision Tree Algorithm | Quinlan, J.R. (1986). Induction of Decision Trees. Machine Learning, 1(1), 81-106 |
| Hybrid Recommender Systems | Burke, R. (2002). Hybrid Recommender Systems: Survey and Experiments |
| Information Gain | Shannon, C.E. (1948). A Mathematical Theory of Communication |
| RIASEC Career Theory | Holland, J.L. (1997). Making Vocational Choices |

---

## Quick Reference

### Files You Need to Know

| File | Purpose |
|------|---------|
| `backend/recommendation_engine.py` | The main algorithm (Rule-Based + Decision Tree) |
| `backend/adaptive_assessment.py` | Information Gain-based question selection |
| `backend/trait_system.py` | Trait definitions and relationships |
| `backend/models.py` | Database table definitions |
| `backend/main.py` | All API endpoints |
| `frontend/src/AdaptiveAssessment.js` | Quiz UI |
| `frontend/src/ResultsView.js` | Results display |

### How to Run

**Backend:**
```bash
cd backend
pip install -r requirements.txt
python main.py
# Runs on http://localhost:8000
```

**Frontend:**
```bash
cd frontend
npm install
npm start
# Runs on http://localhost:3000
```

---

*This documentation was created to provide a complete understanding of the Course Recommendation System for thesis defense and future maintenance.*
