# Course Recommendation System - Complete Documentation

## Table of Contents
1. [System Overview](#system-overview)
2. [Architecture](#architecture)
3. [Trait System (RIASEC)](#trait-system-riasec)
4. [Assessment Types](#assessment-types)
5. [Adaptive Assessment Algorithm](#adaptive-assessment-algorithm)
6. [Course Matching Algorithm](#course-matching-algorithm)
7. [Database Schema](#database-schema)
8. [API Endpoints](#api-endpoints)
9. [Frontend Components](#frontend-components)
10. [Data Flow](#data-flow)

---

## System Overview

This is a **Course Recommendation System** designed for Filipino senior high school students to help them choose the right college course based on their interests, skills, and personality traits.

### Key Features:
- **Smart Assessment (Akinator-style)**: Asks one question at a time, adapting based on previous answers
- **Standard Assessment**: Traditional questionnaire with all questions
- **RIASEC-based Matching**: Uses scientifically-validated Holland's career assessment model
- **99 Courses**: Comprehensive database of Philippine college courses
- **60 Assessment Questions**: Carefully designed to measure 17 distinct traits

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         FRONTEND (React)                         │
│  ┌─────────────┐  ┌──────────────┐  ┌─────────────────────────┐ │
│  │   Login/    │  │   Dashboard  │  │   AdaptiveAssessment    │ │
│  │   Signup    │  │              │  │   (Smart Assessment)    │ │
│  └─────────────┘  └──────────────┘  └─────────────────────────┘ │
│  ┌─────────────┐  ┌──────────────┐  ┌─────────────────────────┐ │
│  │  Assessment │  │  ResultsView │  │      Admin Panel        │ │
│  │    Form     │  │              │  │                         │ │
│  └─────────────┘  └──────────────┘  └─────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ HTTP/REST API
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      BACKEND (FastAPI)                           │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │                      main.py (API Routes)                    ││
│  │  /auth/*  /assessment/*  /adaptive/*  /courses/*  /admin/*  ││
│  └─────────────────────────────────────────────────────────────┘│
│  ┌───────────────────┐  ┌───────────────────────────────────────┐│
│  │ adaptive_         │  │         seed_data.py                  ││
│  │ assessment.py     │  │  (Questions, Courses, Config)         ││
│  │ (Smart Algorithm) │  │                                       ││
│  └───────────────────┘  └───────────────────────────────────────┘│
│  ┌───────────────────┐  ┌───────────────────────────────────────┐│
│  │ courses_          │  │      questions_redesigned.py          ││
│  │ focused.py        │  │      (60 RIASEC Questions)            ││
│  │ (99 Courses)      │  │                                       ││
│  └───────────────────┘  └───────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ SQLAlchemy ORM
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                     DATABASE (PostgreSQL)                        │
│  ┌──────────┐  ┌──────────┐  ┌───────────┐  ┌────────────────┐  │
│  │  users   │  │ courses  │  │ questions │  │ assessment_    │  │
│  │          │  │          │  │           │  │ results        │  │
│  └──────────┘  └──────────┘  └───────────┘  └────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Trait System (RIASEC)

The system uses **17 traits** based on Holland's RIASEC model plus practical skill dimensions:

### Holland's RIASEC (6 Core Interest Types)

| Trait | Description | Example Careers |
|-------|-------------|-----------------|
| **Realistic (R)** | Hands-on, practical, building/fixing things | Engineers, Mechanics, Farmers |
| **Investigative (I)** | Research, analysis, understanding systems | Scientists, Researchers, Doctors |
| **Artistic (A)** | Creative, expressive, original ideas | Artists, Designers, Writers |
| **Social (S)** | Helping, teaching, caring for others | Teachers, Nurses, Counselors |
| **Enterprising (E)** | Leading, persuading, taking charge | Managers, Entrepreneurs, Lawyers |
| **Conventional (C)** | Organizing, detailed work, procedures | Accountants, Administrators |

### Skill/Domain Traits (6 Types)

| Trait | Description |
|-------|-------------|
| **Technical** | Technology, computers, programming |
| **Scientific** | Lab work, experiments, research |
| **Numbers** | Math, statistics, data analysis |
| **Words** | Writing, speaking, languages |
| **Visual** | Design, images, spatial thinking |
| **Physical** | Sports, movement, active work |

### Environment Traits (3 Types)

| Trait | Description |
|-------|-------------|
| **Outdoor** | Nature, fieldwork, outside work |
| **Healthcare** | Medical settings, patient care |
| **Business** | Corporate, commerce, trade |

### Bonus Traits (2 Types)

| Trait | Description |
|-------|-------------|
| **Problem-solving** | Tackling challenges, finding solutions |
| **Creative** | Original ideas, innovation |

---

## Assessment Types

### 1. Smart Assessment (Adaptive/Akinator-Style)

**How it works:**
- Asks **one question at a time**
- Selects the **next best question** based on previous answers
- Uses **information gain** to pick questions that best discriminate between courses
- Can stop early when confident enough (minimum 10, maximum 25 questions)

**Benefits:**
- Shorter assessment (10-25 questions vs 60)
- More engaging experience
- Adapts to the student's profile

### 2. Standard Assessment

**How it works:**
- Presents all 60 questions
- Student answers all questions
- Calculates trait scores from all answers
- Matches traits to courses

**Benefits:**
- More comprehensive
- Consistent experience for all users

---

## Adaptive Assessment Algorithm

The Smart Assessment uses an **Akinator-style algorithm** that intelligently selects questions:

### Algorithm Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                    START ASSESSMENT                              │
│                         │                                        │
│                         ▼                                        │
│         ┌───────────────────────────────┐                       │
│         │ Initialize Session            │                       │
│         │ - All 99 courses active       │                       │
│         │ - All traits at 0             │                       │
│         │ - Confidence = 0              │                       │
│         └───────────────────────────────┘                       │
│                         │                                        │
│                         ▼                                        │
│         ┌───────────────────────────────┐                       │
│         │ Calculate Information Gain    │◄─────────────────┐    │
│         │ for each unused question      │                  │    │
│         └───────────────────────────────┘                  │    │
│                         │                                  │    │
│                         ▼                                  │    │
│         ┌───────────────────────────────┐                  │    │
│         │ Select question with          │                  │    │
│         │ HIGHEST information gain      │                  │    │
│         └───────────────────────────────┘                  │    │
│                         │                                  │    │
│                         ▼                                  │    │
│         ┌───────────────────────────────┐                  │    │
│         │ Present question to user      │                  │    │
│         └───────────────────────────────┘                  │    │
│                         │                                  │    │
│                         ▼                                  │    │
│         ┌───────────────────────────────┐                  │    │
│         │ User selects an answer        │                  │    │
│         └───────────────────────────────┘                  │    │
│                         │                                  │    │
│                         ▼                                  │    │
│         ┌───────────────────────────────┐                  │    │
│         │ Process Answer:               │                  │    │
│         │ - Add trait to user profile   │                  │    │
│         │ - Update all course scores    │                  │    │
│         │ - Recalculate confidence      │                  │    │
│         └───────────────────────────────┘                  │    │
│                         │                                  │    │
│                         ▼                                  │    │
│         ┌───────────────────────────────┐                  │    │
│         │ Check stopping conditions:    │                  │    │
│         │ - Confidence > 75%? AND       │                  │    │
│         │ - Questions >= 10?            │                  │    │
│         │ OR                            │                  │    │
│         │ - Questions >= 25?            │                  │    │
│         └───────────────────────────────┘                  │    │
│                    │           │                           │    │
│               NO   │           │  YES                      │    │
│                    │           │                           │    │
│                    │           ▼                           │    │
│                    │  ┌─────────────────────┐              │    │
│                    │  │ Generate Final      │              │    │
│                    │  │ Recommendations     │              │    │
│                    │  │ (Top 10 courses)    │              │    │
│                    │  └─────────────────────┘              │    │
│                    │           │                           │    │
│                    │           ▼                           │    │
│                    │       END                             │    │
│                    │                                       │    │
│                    └───────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
```

### Information Gain Calculation

The algorithm selects questions using **entropy-based information gain**:

```python
def calculate_information_gain(trait, active_courses):
    """
    Calculates how well a trait splits the remaining courses.
    Higher gain = better discrimination between courses.
    """
    
    # Count courses WITH and WITHOUT this trait
    courses_with_trait = [c for c in active_courses if trait in c.traits]
    courses_without_trait = [c for c in active_courses if trait not in c.traits]
    
    # Calculate entropy (uncertainty)
    # Ideal split is 50/50 (maximum information gain)
    p_with = len(courses_with_trait) / len(active_courses)
    p_without = len(courses_without_trait) / len(active_courses)
    
    entropy = -p_with * log2(p_with) - p_without * log2(p_without)
    
    return entropy  # Higher = more discriminating
```

**Example:**
- If asking about "Healthcare" trait splits courses 15 with / 84 without
- But asking about "Investigative" splits courses 45 with / 54 without
- "Investigative" has higher information gain (closer to 50/50 split)
- So the algorithm asks about "Investigative" first

### Course Scoring

Each answer updates course scores:

```python
def update_course_scores(chosen_trait, courses):
    for course in courses:
        if chosen_trait in course.traits:
            # Boost score for courses with this trait
            course.score += TRAIT_MATCH_WEIGHT  # e.g., +10
        else:
            # Slight penalty for courses without
            course.score -= TRAIT_MISS_PENALTY  # e.g., -2
```

### Confidence Calculation

```python
def calculate_confidence(course_scores):
    """
    Confidence is high when top courses are far ahead of the rest.
    """
    sorted_scores = sorted(course_scores, reverse=True)
    
    top_5_avg = average(sorted_scores[:5])
    rest_avg = average(sorted_scores[5:])
    
    # Gap between top 5 and the rest
    gap = top_5_avg - rest_avg
    
    # Normalize to 0-1 range
    confidence = min(gap / MAX_GAP, 1.0)
    
    return confidence
```

---

## Course Matching Algorithm

### Standard Assessment Matching

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                  │
│  USER ANSWERS                    TRAIT PROFILE                  │
│  ┌─────────────────┐            ┌─────────────────────────────┐ │
│  │ Q1: "Building"  │            │ Realistic: 3                │ │
│  │ Q2: "Research"  │  ──────►   │ Investigative: 2            │ │
│  │ Q3: "Helping"   │            │ Social: 2                   │ │
│  │ Q4: "Technical" │            │ Technical: 2                │ │
│  │ ...             │            │ ...                         │ │
│  └─────────────────┘            └─────────────────────────────┘ │
│                                           │                      │
│                                           ▼                      │
│                              ┌─────────────────────────────────┐ │
│                              │     COURSE MATCHING             │ │
│                              │                                 │ │
│                              │  For each course:               │ │
│                              │    score = 0                    │ │
│                              │    for trait in course.traits:  │ │
│                              │      score += user[trait]       │ │
│                              │    match_% = score / max_score  │ │
│                              └─────────────────────────────────┘ │
│                                           │                      │
│                                           ▼                      │
│                              ┌─────────────────────────────────┐ │
│                              │     RECOMMENDATIONS             │ │
│                              │                                 │ │
│                              │  1. BS Computer Science (92%)   │ │
│                              │  2. BS IT (88%)                 │ │
│                              │  3. BS Civil Engineering (85%)  │ │
│                              │  ...                            │ │
│                              └─────────────────────────────────┘ │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Matching Formula

```python
def calculate_match_percentage(user_traits, course):
    """
    Calculate how well a user's traits match a course.
    """
    
    # Course traits (e.g., ["Investigative", "Technical", "Problem-solving"])
    course_traits = course.trait_tag
    
    # Count matching traits
    matches = 0
    for trait in course_traits:
        if trait in user_traits and user_traits[trait] > 0:
            matches += user_traits[trait]  # Weighted by frequency
    
    # Calculate percentage
    max_possible = len(course_traits) * MAX_TRAIT_SCORE
    match_percentage = (matches / max_possible) * 100
    
    return match_percentage
```

---

## Database Schema

```sql
-- Users table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(255),
    strand VARCHAR(50),  -- STEM, ABM, HUMSS, TVL, GAS
    gwa DECIMAL(4,2),
    created_at TIMESTAMP DEFAULT NOW(),
    is_admin BOOLEAN DEFAULT FALSE
);

-- Courses table
CREATE TABLE courses (
    id SERIAL PRIMARY KEY,
    course_name VARCHAR(255) UNIQUE NOT NULL,
    description TEXT,
    minimum_gwa DECIMAL(4,2),
    recommended_strand VARCHAR(50),
    trait_tag JSONB  -- ["Investigative", "Technical", "Problem-solving"]
);

-- Questions table
CREATE TABLE questions (
    id SERIAL PRIMARY KEY,
    question TEXT NOT NULL,
    category VARCHAR(100),
    options JSONB  -- [{"text": "...", "tag": "Realistic"}, ...]
);

-- Assessment Results table
CREATE TABLE assessment_results (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    assessment_type VARCHAR(50),  -- 'standard' or 'adaptive'
    trait_scores JSONB,  -- {"Realistic": 5, "Investigative": 3, ...}
    recommendations JSONB,  -- [{"course": "...", "score": 92}, ...]
    completed_at TIMESTAMP DEFAULT NOW()
);
```

---

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/signup` | Register new user |
| POST | `/auth/login` | Login and get JWT token |
| GET | `/auth/me` | Get current user info |

### Assessment

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/assessment/questions` | Get all questions |
| POST | `/assessment/submit` | Submit answers, get recommendations |
| GET | `/assessment/history` | Get user's past assessments |

### Adaptive Assessment

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/adaptive/start` | Start new adaptive session |
| POST | `/adaptive/answer` | Submit answer, get next question |
| POST | `/adaptive/finish` | End session early, get results |
| GET | `/adaptive/status/{id}` | Get session status |

### Courses

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/courses` | Get all courses |
| GET | `/courses/{id}` | Get specific course |
| GET | `/courses/strand/{strand}` | Get courses by strand |

### Admin

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/admin/users` | List all users |
| GET | `/admin/reports` | Get system reports |
| POST | `/admin/courses` | Add new course |
| PUT | `/admin/courses/{id}` | Update course |
| DELETE | `/admin/courses/{id}` | Delete course |

---

## Frontend Components

### Component Hierarchy

```
App.js
├── Login.js              # Login page
├── Signup.js             # Registration page
├── Dashboard.js          # Main dashboard
│   ├── Profile Section
│   ├── Assessment Buttons (Standard / Smart)
│   └── Activity History
├── AssessmentForm.js     # Standard assessment
├── AdaptiveAssessment.js # Smart assessment (Akinator-style)
│   ├── Start Screen
│   ├── Question Display
│   ├── Progress Meter
│   ├── Confidence Meter
│   └── Results Display
├── ResultsView.js        # View assessment results
└── admin/
    ├── Admin.js          # Admin dashboard
    ├── ManageCourse.js   # CRUD courses
    ├── ManageQuestion.js # CRUD questions
    ├── ViewUser.js       # User management
    └── ViewReport.js     # Reports
```

### Adaptive Assessment UI Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                     START SCREEN                                 │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │                    🧠 Smart Assessment                       ││
│  │                                                              ││
│  │   This assessment adapts to your answers!                   ││
│  │   • 10-25 questions (depends on your answers)               ││
│  │   • More accurate results                                   ││
│  │   • Takes about 5-10 minutes                                ││
│  │                                                              ││
│  │              [ Start Assessment ]                           ││
│  └─────────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    QUESTION SCREEN                               │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │  Question 5 of ~20                    Confidence: ████░ 72% ││
│  │  ═══════════════════░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ ││
│  └─────────────────────────────────────────────────────────────┘│
│                                                                  │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │        On a free weekend, what would you MOST enjoy?        ││
│  │                                                              ││
│  │   ┌─────────────────────────────────────────────────────┐   ││
│  │   │  Building, fixing, or working with my hands         │   ││
│  │   └─────────────────────────────────────────────────────┘   ││
│  │   ┌─────────────────────────────────────────────────────┐   ││
│  │   │  Reading about science or researching something     │   ││
│  │   └─────────────────────────────────────────────────────┘   ││
│  │   ┌─────────────────────────────────────────────────────┐   ││
│  │   │  Creating art, music, or designing something        │   ││
│  │   └─────────────────────────────────────────────────────┘   ││
│  │   ┌─────────────────────────────────────────────────────┐   ││
│  │   │  Hanging out with friends or helping someone        │   ││
│  │   └─────────────────────────────────────────────────────┘   ││
│  └─────────────────────────────────────────────────────────────┘│
│                                                                  │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │  Current Top Courses:                                       ││
│  │  🥇 BS Computer Science    🥈 BS IT    🥉 BS Civil Eng      ││
│  └─────────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    RESULTS SCREEN                                │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │                  🎉 Assessment Complete!                     ││
│  │                                                              ││
│  │  Your Top Course Recommendations:                           ││
│  │                                                              ││
│  │  1. BS Computer Science ........................... 94%     ││
│  │     Traits: Investigative, Technical, Problem-solving       ││
│  │                                                              ││
│  │  2. BS Information Technology .................... 89%      ││
│  │     Traits: Realistic, Technical, Social                    ││
│  │                                                              ││
│  │  3. BS Data Science .............................. 87%      ││
│  │     Traits: Investigative, Numbers, Technical               ││
│  │                                                              ││
│  │  ...                                                        ││
│  │                                                              ││
│  │  Your Trait Profile:                                        ││
│  │  ┌────────────────────────────────────────────────────┐    ││
│  │  │ Technical:     ████████████░░░░  75%               │    ││
│  │  │ Investigative: ██████████░░░░░░  65%               │    ││
│  │  │ Problem-solving:████████░░░░░░░  50%               │    ││
│  │  │ Realistic:     ██████░░░░░░░░░░  40%               │    ││
│  │  └────────────────────────────────────────────────────┘    ││
│  │                                                              ││
│  │         [ Back to Dashboard ]  [ Take Again ]               ││
│  └─────────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────┘
```

---

## Data Flow

### Complete Assessment Flow

```
┌──────────────────────────────────────────────────────────────────────────┐
│                         COMPLETE DATA FLOW                                │
│                                                                          │
│  ┌─────────────┐                                                         │
│  │   Student   │                                                         │
│  └─────────────┘                                                         │
│        │                                                                  │
│        │ 1. Login/Signup                                                 │
│        ▼                                                                  │
│  ┌─────────────┐     ┌──────────────┐     ┌─────────────────────────┐   │
│  │   Frontend  │────►│   Backend    │────►│   PostgreSQL            │   │
│  │   (React)   │     │   (FastAPI)  │     │   (User created)        │   │
│  └─────────────┘     └──────────────┘     └─────────────────────────┘   │
│        │                                                                  │
│        │ 2. Start Smart Assessment                                       │
│        ▼                                                                  │
│  ┌─────────────┐     ┌──────────────┐     ┌─────────────────────────┐   │
│  │  POST       │────►│  Adaptive    │────►│  Session Created        │   │
│  │  /adaptive/ │     │  Assessment  │     │  - 99 courses active    │   │
│  │  start      │     │  Engine      │     │  - Select 1st question  │   │
│  └─────────────┘     └──────────────┘     └─────────────────────────┘   │
│        │                                                                  │
│        │ 3. Answer Question (repeat 10-25 times)                         │
│        ▼                                                                  │
│  ┌─────────────┐     ┌──────────────┐     ┌─────────────────────────┐   │
│  │  POST       │────►│  Process:    │────►│  Update:                │   │
│  │  /adaptive/ │     │  - Add trait │     │  - Course scores        │   │
│  │  answer     │     │  - Calc gain │     │  - Confidence           │   │
│  │             │◄────│  - Next Q    │◄────│  - Next best question   │   │
│  └─────────────┘     └──────────────┘     └─────────────────────────┘   │
│        │                                                                  │
│        │ 4. Assessment Complete (confidence > 75% OR 25 questions)       │
│        ▼                                                                  │
│  ┌─────────────┐     ┌──────────────┐     ┌─────────────────────────┐   │
│  │  Receive    │◄────│  Generate:   │◄────│  Final Ranking:         │   │
│  │  Results    │     │  - Top 10    │     │  - Sort by score        │   │
│  │             │     │  - Match %   │     │  - Calculate %          │   │
│  └─────────────┘     └──────────────┘     └─────────────────────────┘   │
│        │                                                                  │
│        │ 5. Save to History                                              │
│        ▼                                                                  │
│  ┌─────────────┐     ┌──────────────┐     ┌─────────────────────────┐   │
│  │  POST       │────►│  Save        │────►│  assessment_results     │   │
│  │  /results   │     │  Result      │     │  table updated          │   │
│  └─────────────┘     └──────────────┘     └─────────────────────────┘   │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## File Structure

```
Course-Recommendation-System/
├── backend/
│   ├── main.py                    # FastAPI app, all routes
│   ├── database.py                # PostgreSQL connection
│   ├── models.py                  # SQLAlchemy models
│   ├── schema.py                  # Pydantic schemas
│   ├── security.py                # JWT authentication
│   ├── adaptive_assessment.py     # Smart assessment algorithm
│   ├── courses_focused.py         # 99 courses with RIASEC traits
│   ├── questions_redesigned.py    # 60 assessment questions
│   ├── seed_data.py               # Data imports & config
│   └── requirements.txt           # Python dependencies
│
├── frontend/
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── App.js                 # Main app component
│   │   ├── Login.js               # Login page
│   │   ├── Signup.js              # Registration page
│   │   ├── Dashboard.js           # Main dashboard
│   │   ├── AssessmentForm.js      # Standard assessment
│   │   ├── AdaptiveAssessment.js  # Smart assessment
│   │   ├── ResultsView.js         # Results display
│   │   └── admin/                 # Admin components
│   └── package.json
│
└── SYSTEM_DOCUMENTATION.md        # This file
```

---

## Configuration

### Adaptive Assessment Settings

```python
# In adaptive_assessment.py

MAX_QUESTIONS = 25      # Maximum questions to ask
MIN_QUESTIONS = 10      # Minimum before allowing early stop
CONFIDENCE_THRESHOLD = 0.75  # Stop when confidence reaches this
TOP_N_RECOMMENDATIONS = 10   # Number of courses to recommend

TRAIT_MATCH_WEIGHT = 10      # Points for matching trait
TRAIT_MISS_PENALTY = 2       # Penalty for non-matching trait
```

### Course Trait Assignment

Each course has 3-4 traits that define its best-fit student:

```python
# Example from courses_focused.py

{
    "course_name": "BS Computer Science",
    "trait_tag": ["Investigative", "Technical", "Problem-solving"]
}

{
    "course_name": "BS Nursing",
    "trait_tag": ["Social", "Healthcare", "Realistic"]
}

{
    "course_name": "BS Architecture",
    "trait_tag": ["Artistic", "Investigative", "Visual"]
}
```

---

## Summary

| Component | Count | Purpose |
|-----------|-------|---------|
| Courses | 99 | Philippine college courses |
| Questions | 60 | RIASEC-based assessment questions |
| Traits | 17 | Personality/interest dimensions |
| Assessment Types | 2 | Standard & Adaptive (Smart) |

The system provides accurate course recommendations by:
1. Using scientifically-validated RIASEC traits
2. Matching user responses to course requirements
3. Using adaptive algorithms to minimize questions while maximizing accuracy
4. Providing clear, actionable recommendations for Filipino students
