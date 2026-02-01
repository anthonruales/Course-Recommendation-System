# CoursePro: College Course Recommendation System
## Comprehensive Technical Documentation for Thesis Defense

---

## Table of Contents

1. [System Overview](#1-system-overview)
2. [System Architecture](#2-system-architecture)
3. [Technology Stack](#3-technology-stack)
4. [Database Design](#4-database-design)
5. [The Hybrid Recommendation Algorithm](#5-the-hybrid-recommendation-algorithm)
6. [Adaptive Assessment Engine](#6-adaptive-assessment-engine)
7. [Trait System](#7-trait-system)
8. [System Flow](#8-system-flow)
9. [API Endpoints](#9-api-endpoints)
10. [Frontend Components](#10-frontend-components)
11. [Security Implementation](#11-security-implementation)
12. [Algorithm Complexity & Performance](#12-algorithm-complexity--performance)
13. [Theoretical Foundation](#13-theoretical-foundation)
14. [Diagrams](#14-diagrams)

---

## 1. System Overview

### 1.1 What is CoursePro?

CoursePro is an intelligent **College Course Recommendation System** that helps Senior High School (SHS) students in the Philippines discover the best college courses suited to their:

- **Personality traits** (discovered through assessment)
- **Academic performance** (GWA)
- **SHS Strand** (STEM, ABM, HUMSS, TVL, GAS, etc.)
- **Personal interests and skills**

### 1.2 Problem Statement

Many SHS students struggle to choose the right college course because:
- They lack awareness of available courses
- They don't know which courses align with their personalities
- Traditional career counseling is time-consuming and subjective

### 1.3 Solution

CoursePro provides:
- An **adaptive, intelligent assessment** that asks questions one-at-a-time
- A **hybrid recommendation algorithm** combining Rule-Based Filtering and Decision Tree Classification
- **Personalized course recommendations** with detailed reasoning
- **Activity tracking and history** for students and administrators

---

## 2. System Architecture

### 2.1 High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        FRONTEND (React.js)                       │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────────┐  │
│  │  Dashboard  │  │  Assessment │  │  Results & Activity     │  │
│  │  Component  │  │  Component  │  │  Components             │  │
│  └─────────────┘  └─────────────┘  └─────────────────────────┘  │
└──────────────────────────┬──────────────────────────────────────┘
                           │ HTTP/REST API
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                     BACKEND (FastAPI - Python)                   │
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │                      API LAYER (main.py)                    │ │
│  │   • User Authentication    • Assessment Endpoints           │ │
│  │   • Admin Management       • Feedback System                │ │
│  └──────────────────────────────┬──────────────────────────────┘ │
│                                 │                                 │
│  ┌──────────────────────────────┴──────────────────────────────┐ │
│  │                    CORE ALGORITHM LAYER                      │ │
│  │  ┌─────────────────┐  ┌─────────────────┐  ┌──────────────┐ │ │
│  │  │    Adaptive     │  │  Recommendation │  │    Trait     │ │ │
│  │  │   Assessment    │  │     Engine      │  │    System    │ │ │
│  │  │     Engine      │  │  (Hybrid Algo)  │  │              │ │ │
│  │  └─────────────────┘  └─────────────────┘  └──────────────┘ │ │
│  └─────────────────────────────────────────────────────────────┘ │
│                                 │                                 │
│  ┌──────────────────────────────┴──────────────────────────────┐ │
│  │                      DATA ACCESS LAYER                       │ │
│  │              SQLAlchemy ORM + PostgreSQL/SQLite              │ │
│  └─────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                        DATABASE LAYER                            │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌───────────┐ │
│  │  Users  │ │ Courses │ │Questions│ │ Attempts│ │Recommend- │ │
│  │   D1    │ │   D3    │ │   D2    │ │   D5    │ │  ations   │ │
│  └─────────┘ └─────────┘ └─────────┘ └─────────┘ └───────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

### 2.2 Component Descriptions

| Component | File(s) | Purpose |
|-----------|---------|---------|
| **API Layer** | `main.py` | Handles HTTP requests, authentication, CRUD operations |
| **Adaptive Engine** | `adaptive_assessment.py` | Intelligent question selection algorithm |
| **Recommendation Engine** | `recommendation_engine.py` | Hybrid algorithm (Rule-Based + Decision Tree) |
| **Trait System** | `trait_system.py`, `trait_mapping.py` | Trait definitions, relationships, and matching |
| **Models** | `models.py` | SQLAlchemy database models |
| **Data Layer** | `database.py` | Database connection and session management |

---

## 3. Technology Stack

### 3.1 Backend Technologies

| Technology | Version | Purpose |
|------------|---------|---------|
| **Python** | 3.10+ | Primary programming language |
| **FastAPI** | Latest | High-performance web framework |
| **SQLAlchemy** | 2.0+ | ORM for database operations |
| **PostgreSQL** | 14+ | Production database |
| **SQLite** | 3+ | Development database |
| **Pydantic** | 2.0+ | Data validation and serialization |
| **Uvicorn** | Latest | ASGI server |

### 3.2 Frontend Technologies

| Technology | Version | Purpose |
|------------|---------|---------|
| **React.js** | 18+ | Frontend framework |
| **JavaScript (ES6+)** | - | Programming language |
| **CSS3** | - | Styling |
| **Google OAuth** | - | Social authentication |

### 3.3 Development Tools

- **VS Code** - IDE
- **Git/GitHub** - Version control
- **Postman** - API testing
- **npm** - Package management (frontend)
- **pip** - Package management (backend)

---

## 4. Database Design

### 4.1 Entity-Relationship Diagram (ERD)

```
┌──────────────────┐       ┌──────────────────┐
│      USERS       │       │      TESTS       │
│  (D1 - User DB)  │       │                  │
├──────────────────┤       ├──────────────────┤
│ user_id (PK)     │       │ test_id (PK)     │
│ username         │       │ test_name        │
│ password_hash    │       │ test_type        │
│ first_name       │       │ description      │
│ last_name        │       │                  │
│ email            │       └────────┬─────────┘
│ academic_info    │                │
│ created_at       │                │ 1:N
│ last_active      │                ▼
│ is_online        │       ┌──────────────────┐
└────────┬─────────┘       │    QUESTIONS     │
         │                 │  (D2 - Question) │
         │ 1:N             ├──────────────────┤
         ▼                 │ question_id (PK) │
┌──────────────────┐       │ test_id (FK)     │
│  TEST_ATTEMPTS   │       │ question_text    │
│ (D5 - Attempts)  │       │ category         │
├──────────────────┤       │ question_type    │
│ attempt_id (PK)  │       └────────┬─────────┘
│ user_id (FK)     │                │
│ test_id (FK)     │                │ 1:N
│ taken_at         │                ▼
│ max_questions    │       ┌──────────────────┐
│ questions_answered│      │     OPTIONS      │
│ confidence_score │       ├──────────────────┤
└────────┬─────────┘       │ option_id (PK)   │
         │                 │ question_id (FK) │
         │ 1:N             │ option_text      │
         ▼                 │ trait_tag        │
┌──────────────────┐       │ weight           │
│ STUDENT_ANSWERS  │       │ trait_tags_json  │
├──────────────────┤       │ recommended_     │
│ answer_id (PK)   │       │   courses_json   │
│ attempt_id (FK)  │       └──────────────────┘
│ question_id (FK) │
│ chosen_option_id │
└──────────────────┘

┌──────────────────┐       ┌──────────────────┐
│     COURSES      │◄──────│ RECOMMENDATIONS  │
│  (D3 - Course)   │ 1:N   ├──────────────────┤
├──────────────────┤       │ recommendation_id│
│ course_id (PK)   │       │ attempt_id (FK)  │
│ course_name      │       │ user_id (FK)     │
│ description      │       │ course_id (FK)   │
│ trait_tag        │       │ reasoning        │
│ required_strand  │       │ recommended_at   │
│ minimum_gwa      │       └────────┬─────────┘
└──────────────────┘                │
                                    │ 1:N
                                    ▼
                           ┌──────────────────┐
                           │    FEEDBACK      │
                           ├──────────────────┤
                           │ feedback_id (PK) │
                           │ recommendation_id│
                           │ user_id (FK)     │
                           │ rating (1-5)     │
                           │ feedback_text    │
                           │ created_at       │
                           └──────────────────┘
```

### 4.2 Table Descriptions

| Table | Code Name | Purpose |
|-------|-----------|---------|
| **users** | D1 | Stores user accounts and profiles |
| **questions** | D2 | Assessment questions bank |
| **courses** | D3 | Available college courses |
| **academic_info** | D4 | User's GWA, strand, interests (JSON in users) |
| **test_attempts** | D5 | Records of each assessment taken |
| **recommendations** | D7 | Generated course recommendations |
| **student_answers** | - | Individual question responses |
| **recommendation_feedback** | - | User ratings and comments |

---

## 5. The Hybrid Recommendation Algorithm

### 5.1 Algorithm Overview

The system uses a **Hybrid Recommendation Algorithm** that combines two phases:

```
┌─────────────────────────────────────────────────────────────────┐
│                    HYBRID RECOMMENDATION FLOW                    │
└─────────────────────────────────────────────────────────────────┘
                              │
              ┌───────────────┴───────────────┐
              ▼                               ▼
┌─────────────────────────┐     ┌─────────────────────────┐
│   PHASE 1: RULE-BASED   │     │  PHASE 2: DECISION TREE │
│       FILTERING         │     │     CLASSIFICATION      │
│                         │     │                         │
│  • Apply IF-THEN rules  │     │  • Traverse decision    │
│  • Calculate bonuses    │────▶│    tree nodes           │
│  • Score adjustments    │     │  • Apply score modifiers│
│  • Filter eligibility   │     │  • Rank final courses   │
└─────────────────────────┘     └─────────────────────────┘
                                          │
                                          ▼
                              ┌─────────────────────────┐
                              │   TOP 5 RECOMMENDED     │
                              │       COURSES           │
                              └─────────────────────────┘
```

### 5.2 Phase 1: Rule-Based Filtering

Based on **Rule-Based Expert Systems Theory** (Giarratano & Riley, 2005).

#### 5.2.1 How Rules Work

Each rule follows the IF-THEN pattern:

```python
IF [conditions are met] THEN [apply action]
```

#### 5.2.2 Rule Types

| Rule Type | Purpose | Example |
|-----------|---------|---------|
| **ELIGIBILITY** | Hard constraints (rarely used - system is inclusive) | GWA check |
| **PREFERENCE** | Soft constraints that boost/reduce scores | Strand match bonus |
| **EXCLUSION** | Rules that completely exclude courses | Not used (all courses available) |

#### 5.2.3 Implemented Rules

| Rule ID | Rule Name | Action | Points |
|---------|-----------|--------|--------|
| **A1** | GWA Academic Bonus | Boost if GWA meets requirement | +10 bonus |
| **A2** | Strand Alignment Bonus | Boost if strand matches | +8 bonus |
| **P1** | Primary Trait Alignment | Boost for primary trait match | +20 bonus |
| **P2** | Trait Synergy Bonus | Boost for 3+ trait matches | +15 bonus |
| **P3** | Career Path Preference | Boost for career path match | +25 bonus |
| **P6** | Work Environment Match | Boost for work environment fit | +8 bonus |
| **P7** | Learning Style Match | Boost for learning style fit | +6 bonus |
| **P8** | Interests & Skills Bonus | Boost from profile keywords | +25 max |
| **N3** | No Trait Match Penalty | Penalize if no traits match | -15 penalty |

#### 5.2.4 Rule Evaluation Code Flow

```python
def filter_courses(courses, user_profile, trait_scores):
    filtered_courses = []
    
    for course in courses:
        # Calculate trait match score
        trait_match_score, matched_traits, match_details = calculate_trait_match_score(
            user_traits, course_traits
        )
        
        # Evaluate all rules
        total_boost = 0
        total_penalty = 0
        
        for rule in self.rules:
            result = self.evaluate_rule(rule, context)
            if result.action_taken == "boost_applied":
                total_boost += result.points_applied
            elif result.action_taken == "penalty_applied":
                total_penalty += result.points_applied
        
        # Calculate final eligibility score
        eligibility_score = trait_match_score + total_boost - total_penalty
        
        filtered_courses.append(FilteredCourse(
            course=course,
            eligibility_score=eligibility_score,
            ...
        ))
    
    return sorted(filtered_courses, key=lambda x: x.eligibility_score, reverse=True)
```

### 5.3 Phase 2: Decision Tree Classification

Based on **Decision Tree Algorithm Theory** (Quinlan, 1986).

#### 5.3.1 Tree Structure

The decision tree makes hierarchical decisions based on:

1. **Root Node**: Split by primary trait category
2. **Internal Nodes**: Split by work setting, GWA level, social orientation
3. **Leaf Nodes**: Final classification with confidence score

```
                    ┌──────────────────────┐
                    │    ROOT NODE         │
                    │  (trait_category)    │
                    └──────────┬───────────┘
           ┌───────────────────┼───────────────────┐
           ▼                   ▼                   ▼
    ┌──────────────┐   ┌──────────────┐   ┌──────────────┐
    │   HELPING    │   │   CREATIVE   │   │  TECHNICAL   │
    │   OTHERS     │   │    ARTS      │   │  ANALYTICAL  │
    └──────┬───────┘   └──────┬───────┘   └──────┬───────┘
           │                  │                  │
     (work_setting)     (gwa_level)        (work_env)
           │                  │                  │
    ┌──────┴──────┐    ┌──────┴──────┐   ┌──────┴──────┐
    ▼             ▼    ▼             ▼   ▼             ▼
┌────────┐  ┌────────┐ ...         ... ┌────────┐  ┌────────┐
│Clinical│  │ Office │                 │  Lab   │  │ Field  │
└────────┘  └────────┘                 └────────┘  └────────┘
    │            │                          │           │
    ▼            ▼                          ▼           ▼
┌────────┐  ┌────────┐                 ┌────────┐  ┌────────┐
│NURSING │  │TEACHING│                 │CS/IT   │  │ENGINEER│
│BS MED  │  │BS EDUC │                 │DATA SCI│  │GEOLOGY │
└────────┘  └────────┘                 └────────┘  └────────┘
```

#### 5.3.2 Classification Categories

| Category | Score Modifier | Example Courses |
|----------|----------------|-----------------|
| healthcare_professional | +25 | BS Nursing, BS Medicine |
| healthcare_allied | +20 | BS Physical Therapy |
| education_social | +20 | BS Education |
| technology_software | +25 | BS Computer Science |
| technology_data | +22 | BS Data Science |
| engineering_structural | +25 | BS Civil Engineering |
| business_analytical | +22 | BS Accountancy |
| creative_visual | +20 | BS Fine Arts |

### 5.4 Final Score Calculation

```
FINAL_SCORE = PHASE1_SCORE + PHASE2_MODIFIER + TRAIT_MATCH_BONUS

Where:
- PHASE1_SCORE = base_trait_score + rule_boosts - rule_penalties
- PHASE2_MODIFIER = decision_tree_classification_score
- TRAIT_MATCH_BONUS = (exact_matches × 10) + (similar_matches × 5)
```

---

## 6. Adaptive Assessment Engine

### 6.1 Overview

The Adaptive Assessment Engine implements an **intelligent, question-by-question assessment** using **Decision Tree principles through Information Gain calculation**. This is the same mathematical foundation used in Decision Tree algorithms like ID3 and C4.5 (Quinlan, 1986).

**Connection to Decision Tree Algorithm:**
- Information Gain is the core metric used to BUILD Decision Trees
- Each question acts as a decision node that splits the candidate course set
- User answers traverse the implicit tree structure toward recommendations
- The system dynamically constructs the optimal decision path for each user

Instead of asking all questions at once, it:

1. Asks **one question at a time**
2. Analyzes the answer to **update trait scores**
3. Selects the **next best question** using **Information Gain** (Decision Tree splitting criterion)
4. Continues until **confident** or **max questions reached**

### 6.2 Key Configuration

```python
class AdaptiveAssessmentEngine:
    MAX_QUESTIONS = 25        # Maximum questions (can be 30, 50, or 60)
    MIN_QUESTIONS = 10        # Minimum before early stop
    CONFIDENCE_THRESHOLD = 0.75  # Stop when confident enough
    TOP_N_RECOMMENDATIONS = 5    # Number of courses to recommend
```

### 6.3 Session Data Structure

```python
@dataclass
class AdaptiveSession:
    session_id: str           # Unique session identifier
    user_id: int              # User taking the assessment
    user_strand: str          # User's SHS strand
    user_interests: str       # User's stated interests
    user_skills: str          # User's stated skills
    max_questions: int        # 30, 50, or 60
    min_questions: int        # 50% of max
    
    # Scoring
    trait_scores: Dict[str, float]      # Accumulated trait scores
    course_scores: Dict[str, float]     # Course match scores
    
    # Progress
    answered_questions: Dict[int, int]  # question_id -> option_id
    excluded_question_ids: Set[int]     # Already asked questions
    rejected_topics: Set[str]           # Topics user rejected
    
    round_number: int         # Current question number
    confidence: float         # 0.0 to 1.0
    is_complete: bool         # Assessment finished
    final_recommendations: List[dict]   # Top 5 courses
```

### 6.4 Question Selection Algorithm (Decision Tree Information Gain)

The algorithm calculates **Information Gain** for each potential question. This is the **same formula used in Decision Tree construction** (ID3/C4.5 algorithms):

```python
def _calculate_trait_information_gain(self, session):
    """
    Calculate Information Gain for each trait - the same metric used
    in Decision Tree algorithms (ID3, C4.5) for attribute selection.
    
    Based on: Quinlan, J.R. (1986). Induction of Decision Trees.
    
    Traits that appear in ~50% of courses are MOST valuable
    (they split the candidate set best - maximum entropy).
    """
    trait_value = {}
    total_active = len(session.active_courses)
    
    for trait, courses_with_trait in self.trait_to_courses.items():
        active_with_trait = len(courses_with_trait & session.active_courses)
        
        # Information gain is highest when trait splits courses 50/50
        # This is the classic Decision Tree splitting criterion
        p = active_with_trait / total_active
        entropy = -p * log2(p) - (1-p) * log2(1-p)  # Shannon Entropy
        
        # Reduce value if we already know about this trait
        existing_knowledge = abs(session.trait_scores.get(trait, 0))
        knowledge_penalty = 1 / (1 + existing_knowledge * 0.5)
        
        trait_value[trait] = entropy * knowledge_penalty
    
    return trait_value
```

### 6.5 Answer Processing

When a user answers a question:

```python
def process_answer(self, session_id, question_id, chosen_option_id):
    # 1. Record the answer
    session.answered_questions[question_id] = chosen_option_id
    session.excluded_question_ids.add(question_id)
    
    # 2. Check for rejection patterns ("none", "not interested")
    if is_rejection:
        rejected_topic = self._determine_rejected_topic(question, option)
        session.rejected_topics.add(rejected_topic)
    
    # 3. Update trait scores
    chosen_trait = option.get('trait_tag')
    session.trait_scores[chosen_trait] += 1.0
    
    # 4. Update course scores based on trait matches
    self._update_course_scores(session, chosen_trait)
    
    # 5. Calculate new confidence level
    session.confidence = self._calculate_confidence(session)
    
    return {
        "status": "continue",
        "confidence": session.confidence,
        "traits_discovered": len(session.trait_scores)
    }
```

### 6.6 Course Score Updates

```python
def _update_course_scores(self, session, chosen_trait):
    for course_name in session.active_courses:
        course_traits = self.course_traits[course_name]
        
        # Direct trait match - BIG BOOST
        if chosen_trait in course_traits:
            session.course_scores[course_name] += 8.0
        else:
            # Check for similar traits
            best_similarity = max(
                self._get_specialized_similarity(chosen_trait, ct)
                for ct in course_traits
            )
            
            if best_similarity > 0.7:
                session.course_scores[course_name] += 4.0
            elif best_similarity > 0.4:
                session.course_scores[course_name] += 2.0
            elif best_similarity > 0.2:
                session.course_scores[course_name] += 0.5
```

### 6.7 Confidence Calculation

```python
def _calculate_confidence(self, session):
    sorted_scores = sorted(session.course_scores.values(), reverse=True)
    
    # Compare top 5 courses to the rest
    top_5_avg = sum(sorted_scores[:5]) / 5
    rest_avg = sum(sorted_scores[5:15]) / 10
    
    # Confidence based on gap between top and rest
    gap_ratio = (top_5_avg - rest_avg) / top_5_avg
    
    # Also factor in question progress
    question_factor = min(session.round_number / session.min_questions, 1.0)
    
    confidence = gap_ratio * 0.7 + question_factor * 0.3
    return min(max(confidence, 0), 1)
```

### 6.8 Stopping Conditions

The assessment stops when:

1. **Minimum questions answered** AND **confidence ≥ 75%**
2. **Maximum questions reached** (30, 50, or 60)
3. **User requests early finish** (after minimum questions)

---

## 7. Trait System

### 7.1 Trait Categories

The system uses a comprehensive trait classification:

#### 7.1.1 RIASEC Interest Types

Based on Holland's Occupational Themes:

| Code | Type | Description |
|------|------|-------------|
| R | Realistic | Practical, hands-on work |
| I | Investigative | Analytical, research-oriented |
| A | Artistic | Creative, expressive |
| S | Social | Helping, teaching others |
| E | Enterprising | Leading, persuading |
| C | Conventional | Organizing, data management |

#### 7.1.2 Specialized Path Traits (22 unique traits)

| Category | Traits |
|----------|--------|
| **Healthcare** | Patient-Care, Medical-Lab, Rehab-Therapy, Health-Admin |
| **Technology** | Software-Dev, Hardware-Systems, Data-Analytics, Cyber-Defense |
| **Engineering** | Civil-Build, Electrical-Power, Mechanical-Design, Industrial-Ops |
| **Business** | Finance-Acct, Marketing-Sales, Startup-Venture |
| **Education** | Teaching-Ed |
| **Arts** | Visual-Design, Digital-Media, Spatial-Design |
| **Science** | Lab-Research, Field-Research |
| **Public Service** | Law-Enforce, Community-Serve |
| **Maritime** | Maritime-Sea |
| **Agriculture** | Agri-Nature |
| **Hospitality** | Hospitality-Svc |

#### 7.1.3 Skill Traits (6 traits)

- Technical-Skill
- People-Skill
- Creative-Skill
- Analytical-Skill
- Physical-Skill
- Admin-Skill

### 7.2 Trait Relationships

Traits have **similarity scores** (0.0 to 1.0) for partial matching:

```python
SPECIALIZED_TRAIT_RELATIONSHIPS = {
    "Patient-Care": {
        "Social": 0.8,           # Strong relationship
        "People-Skill": 0.9,     # Very strong
        "Rehab-Therapy": 0.6,    # Moderate
        "Medical-Lab": 0.4,      # Weak
    },
    "Software-Dev": {
        "Investigative": 0.8,
        "Technical-Skill": 0.9,
        "Data-Analytics": 0.6,
        "Digital-Media": 0.3,
    },
    # ... more relationships
}
```

### 7.3 Trait Matching Algorithm

```python
def calculate_trait_match_score(user_traits, course_traits):
    """
    Calculate match score between user traits and course traits.
    
    Returns:
        - total_score: Weighted score
        - matched_traits: List of matched trait names
        - match_details: Breakdown of exact/similar/category matches
    """
    exact_matches = []
    similar_matches = []
    
    for user_trait in user_traits:
        for course_trait in course_traits:
            if user_trait == course_trait:
                # Exact match - highest score
                exact_matches.append(user_trait)
            else:
                # Check similarity
                similarity = get_trait_similarity(user_trait, course_trait)
                if similarity >= 0.5:
                    similar_matches.append((user_trait, course_trait, similarity))
    
    # Calculate score
    score = (len(exact_matches) * 10) + sum(s[2] * 5 for s in similar_matches)
    
    return score, exact_matches + [s[0] for s in similar_matches], {
        "exact": exact_matches,
        "similar": similar_matches
    }
```

---

## 8. System Flow

### 8.1 Complete User Journey

```
┌─────────────────────────────────────────────────────────────────┐
│                       USER JOURNEY FLOW                          │
└─────────────────────────────────────────────────────────────────┘

     ┌──────────┐         ┌───────────────┐        ┌──────────────┐
     │  SIGNUP  │────────▶│ COMPLETE      │───────▶│  DASHBOARD   │
     │  /LOGIN  │         │ PROFILE       │        │              │
     └──────────┘         └───────────────┘        └──────┬───────┘
                                                          │
                                                          ▼
                                                 ┌──────────────┐
                                                 │ SELECT QUIZ  │
                                                 │ LENGTH       │
                                                 │ (30/50/60)   │
                                                 └──────┬───────┘
                                                        │
                    ┌───────────────────────────────────┘
                    ▼
           ┌──────────────────────────────────────────────────┐
           │            ADAPTIVE ASSESSMENT LOOP               │
           │  ┌─────────────────────────────────────────────┐ │
           │  │  1. Engine selects best next question       │ │
           │  │  2. User answers question                   │ │
           │  │  3. System updates trait/course scores      │ │
           │  │  4. Calculate confidence                    │ │
           │  │  5. Repeat until done                       │ │
           │  └─────────────────────────────────────────────┘ │
           └──────────────────────┬───────────────────────────┘
                                  │
                                  ▼
                         ┌──────────────┐
                         │ GENERATE     │
                         │ FINAL RECS   │
                         │ (Top 5)      │
                         └──────┬───────┘
                                │
            ┌───────────────────┼───────────────────┐
            ▼                   ▼                   ▼
    ┌──────────────┐   ┌──────────────┐   ┌──────────────┐
    │   RESULTS    │   │   FEEDBACK   │   │   HISTORY    │
    │   VIEW       │   │   FORM       │   │   SAVED      │
    └──────────────┘   └──────────────┘   └──────────────┘
```

### 8.2 API Request Flow

```
┌────────────────────────────────────────────────────────────────────────┐
│                      API REQUEST FLOW                                   │
└────────────────────────────────────────────────────────────────────────┘

1. START ASSESSMENT
   Frontend                         Backend
      │                                │
      │  POST /adaptive/start          │
      │  {userId, maxQuestions}        │
      │ ──────────────────────────────▶│
      │                                │
      │                                │  • Load user profile
      │                                │  • Initialize session
      │                                │  • Calculate initial scores
      │                                │  • Get first question
      │                                │
      │  {session_id, first_question}  │
      │ ◀──────────────────────────────│
      │                                │

2. ANSWER QUESTION (repeated)
      │                                │
      │  POST /adaptive/answer         │
      │  {sessionId, questionId,       │
      │   chosenOptionId}              │
      │ ──────────────────────────────▶│
      │                                │
      │                                │  • Record answer
      │                                │  • Update trait scores
      │                                │  • Update course scores
      │                                │  • Calculate confidence
      │                                │  • Select next question
      │                                │
      │  {status, next_question,       │
      │   confidence, traits}          │
      │ ◀──────────────────────────────│
      │                                │

3. COMPLETE (auto or manual)
      │                                │
      │  POST /adaptive/finish         │
      │  {sessionId}                   │
      │ ──────────────────────────────▶│
      │                                │
      │                                │  • Finalize recommendations
      │                                │  • Save to database
      │                                │  • Generate reasoning
      │                                │
      │  {recommendations: [...]}      │
      │ ◀──────────────────────────────│
```

### 8.3 Database Save Flow

```python
def save_adaptive_session_to_db(db, engine, session_id, recommendations):
    # 1. Get or create "adaptive" test type
    adaptive_test = db.query(Test).filter(Test.test_type == "adaptive").first()
    if not adaptive_test:
        adaptive_test = Test(
            test_name="Adaptive Career Assessment",
            test_type="adaptive",
            description="Intelligent question-by-question assessment"
        )
        db.add(adaptive_test)
        db.flush()
    
    # 2. Create test attempt record
    test_attempt = TestAttempt(
        user_id=session.user_id,
        test_id=adaptive_test.test_id,
        taken_at=datetime.now(),
        max_questions=session.max_questions,
        questions_answered=len(session.answered_questions),
        confidence_score=session.confidence * 100
    )
    db.add(test_attempt)
    db.flush()
    
    # 3. Save student answers
    for question_id, option_id in session.answered_questions.items():
        db.add(StudentAnswer(
            attempt_id=test_attempt.attempt_id,
            question_id=question_id,
            chosen_option_id=option_id
        ))
    
    # 4. Save recommendations
    for rec in recommendations:
        course = db.query(Course).filter(
            Course.course_name == rec['course_name']
        ).first()
        
        db.add(Recommendation(
            attempt_id=test_attempt.attempt_id,
            user_id=session.user_id,
            course_id=course.course_id,
            reasoning=rec['reasoning']
        ))
    
    db.commit()
```

---

## 9. API Endpoints

### 9.1 Authentication Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/signup` | Register new user |
| POST | `/login` | User login |
| POST | `/logout` | User logout (marks offline) |
| POST | `/google-login` | Google OAuth login |
| POST | `/google-register` | Complete Google registration |

### 9.2 User Profile Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/user/{user_id}/academic-info` | Get user's profile |
| POST | `/user/{user_id}/academic-info` | Save academic info |
| POST | `/user/{user_id}/update-activity` | Update online status |
| GET | `/user/{user_id}/recommendations` | Get saved recommendations |
| GET | `/user/{user_id}/assessment-history` | Get assessment history |

### 9.3 Adaptive Assessment Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/adaptive/start` | Start new assessment session |
| POST | `/adaptive/answer` | Submit answer, get next question |
| POST | `/adaptive/finish` | End assessment early |

### 9.4 Admin Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/admin/users` | List all users |
| GET | `/admin/courses` | List all courses |
| POST | `/admin/courses` | Create new course |
| PUT | `/admin/courses/{id}` | Update course |
| DELETE | `/admin/courses/{id}` | Delete course |
| GET | `/admin/questions` | List all questions |
| POST | `/admin/questions` | Create new question |
| GET | `/admin/feedback/all` | Get all feedback |
| GET | `/admin/feedback/stats` | Get feedback statistics |

### 9.5 Feedback Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/feedback/submit` | Submit recommendation feedback |
| GET | `/feedback/recommendation/{id}` | Get feedback for recommendation |
| GET | `/user/{user_id}/feedback` | Get user's feedback history |

---

## 10. Frontend Components

### 10.1 Component Hierarchy

```
App.js
├── LandingPage.js
├── Login.js
├── Signup.js
├── Dashboard.js
│   ├── Profile Section
│   ├── Quiz Length Selector (30/50/60)
│   └── Start Assessment Button
├── ProfileForm.js
│   ├── Academic Info (GWA, Strand)
│   ├── Personal Info (Age, Gender)
│   └── Interests & Skills Selection
├── AdaptiveAssessment.js
│   ├── Question Display
│   ├── Progress Bar
│   ├── Confidence Indicator
│   ├── Top Courses Preview
│   └── Early Finish Button
├── ResultsView.js
│   ├── Top 5 Courses
│   ├── Match Percentages
│   ├── Reasoning Display
│   └── Feedback Form
├── MyActivity.js
│   ├── Assessment History
│   ├── Past Recommendations
│   └── Traits Discovered
└── admin/
    ├── Admin.js
    ├── ManageCourse.js
    ├── ManageQuestion.js
    ├── ViewUser.js
    ├── ViewFeedback.js
    └── ViewReport.js
```

### 10.2 Key Component Descriptions

| Component | Purpose |
|-----------|---------|
| **Dashboard** | Main hub after login - shows profile status, start assessment |
| **AdaptiveAssessment** | Handles one-at-a-time question flow |
| **ProfileForm** | Collects GWA, strand, interests, skills |
| **ResultsView** | Displays top 5 recommendations with details |
| **MyActivity** | Shows assessment history and past results |
| **Admin** | Admin panel for managing system data |

### 10.3 State Management

The app uses React's `useState` and `useEffect` for state management:

```javascript
// App.js - Main state
const [user, setUser] = useState(null);
const [recommendationData, setRecommendationData] = useState(null);
const [profileData, setProfileData] = useState({});
const [history, setHistory] = useState([]);

// AdaptiveAssessment.js - Assessment state
const [sessionId, setSessionId] = useState(null);
const [currentQuestion, setCurrentQuestion] = useState(null);
const [currentRound, setCurrentRound] = useState(0);
const [confidence, setConfidence] = useState(0);
const [traitsDiscovered, setTraitsDiscovered] = useState(0);
const [topCoursesPreview, setTopCoursesPreview] = useState([]);
```

---

## 11. Security Implementation

### 11.1 Password Hashing

```python
# security.py
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """Hash password using bcrypt"""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify password against hash"""
    return pwd_context.verify(plain_password, hashed_password)
```

### 11.2 Input Validation

```python
# Name validation with bad words filter
BAD_WORDS = ['fuck', 'shit', ...]  # Profanity list

def validate_name(name: str) -> tuple:
    if len(name.strip()) < 2:
        return (False, "Name must be at least 2 characters", name)
    
    if contains_bad_words(name):
        return (False, "Please use an appropriate name", name)
    
    if not re.match(r"^[a-zA-Z\s'-]+$", name.strip()):
        return (False, "Name can only contain letters...", name)
    
    return (True, None, capitalize_name(name.strip()))
```

### 11.3 CORS Configuration

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
```

---

## 12. Algorithm Complexity & Performance

### 12.1 Time Complexity

| Operation | Complexity | Description |
|-----------|------------|-------------|
| Question Selection | O(Q × T) | Q=questions, T=traits |
| Answer Processing | O(C × T) | C=courses, T=traits |
| Trait Matching | O(U × C × R) | U=user traits, C=course traits, R=relationships |
| Confidence Calculation | O(C log C) | Sorting courses |
| Final Recommendations | O(C log C) | Sorting and selecting top 5 |

### 12.2 Space Complexity

| Structure | Complexity | Description |
|-----------|------------|-------------|
| Session Data | O(C + T + Q) | Courses, traits, questions |
| Trait Relationships | O(T²) | Relationship matrix |
| Answer History | O(Q) | One per answered question |

### 12.3 Performance Optimizations

1. **Pre-computed Lookups**: Trait-to-course and trait-to-question mappings built on engine initialization
2. **Session Caching**: Sessions stored in memory for fast access
3. **Early Stopping**: Assessment ends when confidence reaches threshold
4. **Excluded Questions**: Set-based O(1) lookup for already-asked questions

---

## 13. Theoretical Foundation

### 13.1 Rule-Based Expert Systems

**Reference**: Giarratano, J., & Riley, G. (2005). *Expert Systems: Principles and Programming*

The Rule-Based Filtering phase implements:
- **IF-THEN rules** for knowledge representation
- **Forward chaining** for rule evaluation
- **Conflict resolution** through priority ordering

### 13.2 Decision Trees

**Reference**: Quinlan, J.R. (1986). *Induction of Decision Trees*

The Decision Tree Classification phase implements:
- **Hierarchical classification** based on attributes
- **Node splitting** by trait category, GWA level, work setting
- **Leaf classification** with confidence scores

### 13.3 Information Theory

**Reference**: Shannon, C.E. (1948). *A Mathematical Theory of Communication*

Question selection uses:
- **Shannon Entropy** for information gain calculation
- **Maximum entropy principle** for optimal question selection
- **Knowledge penalty** for diminishing returns on repeated topics

### 13.4 Holland's RIASEC Theory

**Reference**: Holland, J.L. (1997). *Making Vocational Choices*

The trait system incorporates:
- **6 personality types** (Realistic, Investigative, Artistic, Social, Enterprising, Conventional)
- **Type relationships** for similarity matching
- **Career matching** based on personality-occupation fit

---

## 14. Diagrams

### 14.1 Data Flow Diagram (Level 0)

```
                    ┌─────────────────────────────┐
                    │          STUDENT            │
                    └──────────────┬──────────────┘
                                   │
              ┌────────────────────┼────────────────────┐
              │                    │                    │
              ▼                    ▼                    ▼
        ┌──────────┐        ┌──────────┐        ┌──────────┐
        │ Profile  │        │Assessment│        │ Feedback │
        │   Data   │        │ Answers  │        │  Ratings │
        └────┬─────┘        └────┬─────┘        └────┬─────┘
             │                   │                   │
             └───────────────────┼───────────────────┘
                                 │
                                 ▼
        ┌────────────────────────────────────────────────┐
        │                                                │
        │              CoursePro SYSTEM                  │
        │                                                │
        │  ┌──────────────────────────────────────────┐  │
        │  │        RECOMMENDATION ENGINE             │  │
        │  │                                          │  │
        │  │  1. Rule-Based Filtering                 │  │
        │  │  2. Decision Tree Classification         │  │
        │  │  3. Trait Matching                       │  │
        │  └──────────────────────────────────────────┘  │
        │                                                │
        └────────────────────────┬───────────────────────┘
                                 │
                                 ▼
        ┌────────────────────────────────────────────────┐
        │                                                │
        │              COURSE RECOMMENDATIONS            │
        │          (Top 5 with Reasoning)               │
        │                                                │
        └────────────────────────────────────────────────┘
```

### 14.2 Use Case Diagram

```
                    ┌─────────────────────────────────────┐
                    │         CoursePro SYSTEM            │
                    │                                     │
    ┌───────────┐   │   ┌─────────────────────────────┐   │
    │           │   │   │                             │   │
    │  STUDENT  │───┼──▶│  Register/Login             │   │
    │           │   │   │                             │   │
    └───────────┘   │   └─────────────────────────────┘   │
         │         │                                     │
         │         │   ┌─────────────────────────────┐   │
         ├─────────┼──▶│  Complete Profile           │   │
         │         │   │  (GWA, Strand, Interests)   │   │
         │         │   └─────────────────────────────┘   │
         │         │                                     │
         │         │   ┌─────────────────────────────┐   │
         ├─────────┼──▶│  Take Adaptive Assessment   │   │
         │         │   │  (Answer Questions)         │   │
         │         │   └─────────────────────────────┘   │
         │         │                                     │
         │         │   ┌─────────────────────────────┐   │
         ├─────────┼──▶│  View Recommendations       │   │
         │         │   │  (Top 5 Courses)            │   │
         │         │   └─────────────────────────────┘   │
         │         │                                     │
         │         │   ┌─────────────────────────────┐   │
         ├─────────┼──▶│  Submit Feedback            │   │
         │         │   │  (Rate Recommendations)     │   │
         │         │   └─────────────────────────────┘   │
         │         │                                     │
         │         │   ┌─────────────────────────────┐   │
         └─────────┼──▶│  View Activity History      │   │
                   │   │  (Past Assessments)         │   │
                   │   └─────────────────────────────┘   │
                   │                                     │
    ┌───────────┐  │   ┌─────────────────────────────┐   │
    │           │  │   │                             │   │
    │   ADMIN   │──┼──▶│  Manage Courses/Questions   │   │
    │           │  │   │                             │   │
    └───────────┘  │   └─────────────────────────────┘   │
         │        │                                     │
         │        │   ┌─────────────────────────────┐   │
         ├────────┼──▶│  View Users                  │   │
         │        │   │                             │   │
         │        │   └─────────────────────────────┘   │
         │        │                                     │
         │        │   ┌─────────────────────────────┐   │
         ├────────┼──▶│  View Feedback/Reports       │   │
         │        │   │                             │   │
         │        │   └─────────────────────────────┘   │
         │        │                                     │
                   └─────────────────────────────────────┘
```

### 14.3 Sequence Diagram - Assessment Flow

```
Student        Frontend       Backend          Engine         Database
   │               │              │               │               │
   │──Click Start──▶              │               │               │
   │               │──POST /start─▶               │               │
   │               │              │──getUser──────────────────────▶
   │               │              │◀──userData────────────────────│
   │               │              │──createSession▶               │
   │               │              │              │──initScores───▶│
   │               │              │◀──sessionId──│               │
   │               │              │──getNextQ───▶│               │
   │               │              │◀──question───│               │
   │               │◀──{session, question}───────│               │
   │◀──ShowQ───────│              │               │               │
   │               │              │               │               │
   │──SelectOption─▶              │               │               │
   │               │──POST /answer▶               │               │
   │               │              │──processAns──▶               │
   │               │              │              │──updateScores─▶│
   │               │              │              │──calcConfidence│
   │               │              │──getNextQ───▶│               │
   │               │              │◀──question───│               │
   │               │◀──{status, nextQ}───────────│               │
   │◀──ShowNextQ───│              │               │               │
   │               │              │               │               │
   │     ... (repeat until complete) ...         │               │
   │               │              │               │               │
   │               │              │──finalize────▶               │
   │               │              │              │──getTop5───────│
   │               │              │              │◀──courses──────│
   │               │              │──saveResults───────────────────▶
   │               │◀──{recommendations}─────────│               │
   │◀──ShowResults─│              │               │               │
```

---

## Summary

CoursePro is a sophisticated **College Course Recommendation System** that combines:

1. **Adaptive Assessment** - Intelligent question selection based on information gain
2. **Hybrid Algorithm** - Rule-Based Filtering + Decision Tree Classification
3. **Comprehensive Trait System** - 22+ specialized traits with similarity relationships
4. **Modern Tech Stack** - FastAPI backend, React frontend, PostgreSQL database

The system provides **personalized, explainable recommendations** that help SHS students make informed decisions about their college education.

---

*Document prepared for thesis defense presentation*
*CoursePro - College Course Recommendation System*
*Version 1.0*
