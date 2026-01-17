# Course Recommendation System - Complete Documentation

## Table of Contents
1. [System Overview](#system-overview)
2. [Architecture](#architecture)
3. [Algorithm Flow](#algorithm-flow)
4. [Trait System](#trait-system)
5. [Database Schema](#database-schema)
6. [API Endpoints](#api-endpoints)
7. [Frontend Components](#frontend-components)
8. [Assessment Types](#assessment-types)

---

## System Overview

### What is this system?
A **Course Recommendation System** designed for Filipino Senior High School students to discover their ideal college courses based on personality traits, interests, and skills.

### Key Features
- ✅ **Standard Assessment** - Tiered questionnaire (15/30/50 questions)
- ✅ **Adaptive Assessment** - Akinator-style intelligent questioning
- ✅ **User Authentication** - Signup, login, session management
- ✅ **Admin Dashboard** - Manage courses, questions, view reports
- ✅ **Assessment History** - Track past attempts and recommendations
- ✅ **Question Randomization** - Different questions each attempt
- ✅ **Strand-Based Personalization** - Questions prioritized by SHS strand

### Technology Stack
| Layer | Technology |
|-------|------------|
| Frontend | React.js |
| Backend | FastAPI (Python) |
| Database | PostgreSQL |
| Auth | JWT Tokens |

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        FRONTEND (React)                      │
│  ┌─────────┐ ┌──────────────┐ ┌──────────┐ ┌─────────────┐  │
│  │  Login  │ │  Assessment  │ │ Results  │ │   Admin     │  │
│  │  Signup │ │     Form     │ │   View   │ │  Dashboard  │  │
│  └────┬────┘ └──────┬───────┘ └────┬─────┘ └──────┬──────┘  │
└───────┼─────────────┼──────────────┼──────────────┼─────────┘
        │             │              │              │
        ▼             ▼              ▼              ▼
┌─────────────────────────────────────────────────────────────┐
│                     BACKEND (FastAPI)                        │
│  ┌────────────────┐  ┌─────────────────┐  ┌──────────────┐  │
│  │  Auth Service  │  │ Assessment      │  │   Admin      │  │
│  │  - JWT tokens  │  │ Service         │  │   APIs       │  │
│  │  - Password    │  │ - Standard      │  │   - CRUD     │  │
│  │    hashing     │  │ - Adaptive      │  │   - Reports  │  │
│  └────────────────┘  └─────────────────┘  └──────────────┘  │
│                              │                               │
│  ┌───────────────────────────▼───────────────────────────┐  │
│  │              RECOMMENDATION ENGINE                     │  │
│  │  ┌─────────────┐  ┌─────────────┐  ┌───────────────┐  │  │
│  │  │   Trait     │  │   Course    │  │   Adaptive    │  │  │
│  │  │   Matcher   │  │   Scorer    │  │   Engine      │  │  │
│  │  └─────────────┘  └─────────────┘  └───────────────┘  │  │
│  └───────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    DATABASE (PostgreSQL)                     │
│  ┌─────────┐ ┌──────────┐ ┌─────────┐ ┌──────────────────┐  │
│  │  Users  │ │  Courses │ │Questions│ │  Test Attempts   │  │
│  │         │ │  (99)    │ │  (70)   │ │  & History       │  │
│  └─────────┘ └──────────┘ └─────────┘ └──────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

---

## Algorithm Flow

### Standard Assessment Flow

```
START
  │
  ▼
┌─────────────────────────┐
│ 1. User selects tier    │
│    (Quick/Standard/     │
│     Comprehensive)      │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│ 2. Random questions     │
│    selected from pool   │
│    (15/30/50 questions) │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│ 3. User answers each    │
│    question, selecting  │
│    one option           │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│ 4. TRAIT ACCUMULATION   │
│    Each answer adds     │
│    its trait to user's  │
│    trait profile        │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│ 5. COURSE MATCHING      │
│    Compare user traits  │
│    vs course traits     │
│    Calculate % match    │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│ 6. RANKING & RESULTS    │
│    Sort by match score  │
│    Return top 5 courses │
└───────────┬─────────────┘
            │
            ▼
          END
```

### Adaptive Assessment Flow (Akinator-Style)

```
START
  │
  ▼
┌─────────────────────────────┐
│ 1. Initialize session       │
│    - All 99 courses active  │
│    - Empty trait profile    │
└───────────┬─────────────────┘
            │
            ▼
┌─────────────────────────────┐
│ 2. CALCULATE INFORMATION    │
│    GAIN for each trait      │
│    - Which trait best       │
│      splits remaining       │
│      courses 50/50?         │
└───────────┬─────────────────┘
            │
            ▼
┌─────────────────────────────┐
│ 3. SELECT BEST QUESTION     │
│    Pick question that       │
│    tests highest-value      │
│    discriminating trait     │
└───────────┬─────────────────┘
            │
            ▼
┌─────────────────────────────┐
│ 4. User answers question    │
└───────────┬─────────────────┘
            │
            ▼
┌─────────────────────────────┐
│ 5. UPDATE COURSE SCORES     │
│    - Direct match: +8 pts   │
│    - Similar (>70%): +4 pts │
│    - Moderate (>40%): +2 pts│
│    - Slight (>20%): +0.5 pts│
│    - No penalty for others  │
└───────────┬─────────────────┘
            │
            ▼
┌─────────────────────────────┐
│ 6. CHECK CONFIDENCE         │
│    Are top 5 courses        │
│    significantly ahead?     │
└───────────┬─────────────────┘
            │
      ┌─────┴─────┐
      │           │
     YES          NO
      │           │
      ▼           ▼
┌──────────┐ ┌────────────────┐
│ FINISH   │ │ More questions │
│ Show top │ │ needed?        │
│ 5 courses│ │ (max 25)       │
└──────────┘ └───────┬────────┘
                     │
               Loop back to step 2
```

### Strand-Based Question Filtering

Questions are personalized based on the user's SHS strand to provide more relevant assessments.

#### How It Works
1. **User enters their SHS strand** in their academic profile (STEM, ABM, HUMSS, TVL, GAS, SPORTS, or ARTS)
2. **System maps strand to priority traits** - each strand has traits that are most relevant to its career paths
3. **Questions are selected proportionally**:
   - **50%** from strand-priority traits
   - **30%** from secondary/related traits  
   - **20%** from general traits (ensures variety)

#### Strand to Trait Mapping

| Strand | Priority Traits | Career Direction |
|--------|-----------------|------------------|
| **STEM** | Software-Dev, Hardware-Systems, Lab-Research, Data-Analytics | Tech, Science, Engineering |
| **ABM** | Finance-Acct, Marketing-Sales, Startup-Venture, Corporate-Mgmt | Business, Finance |
| **HUMSS** | Teaching-Ed, Community-Serve, Law-Enforce, Public-Admin | Education, Social Sciences |
| **TVL** | Software-Dev, Hospitality-Svc, Mechanical-Design, Agriculture-Env | Technical-Vocational |
| **GAS** | Balanced mix across all traits | General exploration |
| **SPORTS** | Sports-Fitness, Coaching-Training, Wellness-Health | Athletic careers |
| **ARTS** | Creative-Design, Media-Production, Visual-Arts | Creative industries |

#### Example: STEM Student vs ABM Student

**STEM Student's Assessment:**
- More questions about coding, scientific research, mathematical thinking
- Questions explore Hardware vs Software vs Data Science paths
- Still includes some business/creative questions for variety

**ABM Student's Assessment:**
- More questions about finance, marketing, entrepreneurship
- Questions explore Accounting vs Marketing vs Management paths
- Still includes some tech/creative questions for variety

This ensures each student gets questions **relevant to their educational background** while still exploring all possible career paths.

### Trait Matching Algorithm

```python
# Simplified matching logic
def calculate_course_score(user_traits, course):
    score = 0
    course_traits = course.trait_tag  # e.g., ["Social", "Patient-Care", "People-Skill"]
    
    for user_trait in user_traits:
        if user_trait in course_traits:
            # DIRECT MATCH - highest boost
            score += 8
        else:
            # Check similarity using SPECIALIZED_TRAIT_RELATIONSHIPS
            best_similarity = get_best_similarity(user_trait, course_traits)
            if best_similarity > 0.7:
                score += 4
            elif best_similarity > 0.4:
                score += 2
            elif best_similarity > 0.2:
                score += 0.5
            # No penalty - courses just don't get boosted
    
    return score
```

---

## Trait System

### Overview
The system uses **34 unique traits** organized into 3 categories:

### 1. RIASEC Interest Types (6 traits)
Based on Holland's career theory:
| Trait | Description | Example Careers |
|-------|-------------|-----------------|
| Realistic | Hands-on, practical | Engineering, Maritime |
| Investigative | Research, analysis | Science, Technology |
| Artistic | Creative, expressive | Arts, Design |
| Social | Helping others | Healthcare, Teaching |
| Enterprising | Leadership, business | Business, Marketing |
| Conventional | Organization, data | Accounting, Admin |

### 2. Specialized Path Traits (22 unique traits)
Each career field has **unique traits that don't overlap**:

| Career Field | Unique Trait | Courses |
|--------------|--------------|---------|
| Healthcare - Patient | `Patient-Care` | Nursing, Midwifery |
| Healthcare - Lab | `Medical-Lab` | Medical Technology, Pharmacy |
| Healthcare - Rehab | `Rehab-Therapy` | Physical Therapy, OT |
| Healthcare - Admin | `Health-Admin` | Health Info Management |
| Technology - Software | `Software-Dev` | Computer Science, IT |
| Technology - Hardware | `Hardware-Systems` | Computer Engineering |
| Technology - Data | `Data-Analytics` | Data Science, Statistics |
| Technology - Security | `Cyber-Defense` | Cybersecurity |
| Engineering - Civil | `Civil-Build` | Civil Engineering |
| Engineering - Electrical | `Electrical-Power` | Electrical Engineering |
| Engineering - Mechanical | `Mechanical-Design` | Mechanical Engineering |
| Engineering - Industrial | `Industrial-Ops` | Industrial Engineering |
| Business - Finance | `Finance-Acct` | Accountancy, Finance |
| Business - Marketing | `Marketing-Sales` | Marketing, Advertising |
| Business - Startup | `Startup-Venture` | Entrepreneurship |
| Education | `Teaching-Ed` | Education courses |
| Arts - Visual | `Visual-Design` | Fine Arts, Photography |
| Arts - Digital | `Digital-Media` | Animation, Multimedia |
| Arts - Spatial | `Spatial-Design` | Architecture, Interior Design |
| Science - Lab | `Lab-Research` | Biology, Chemistry |
| Science - Field | `Field-Research` | Environmental Science |
| Public Service - Law | `Law-Enforce` | Criminology |
| Public Service - Community | `Community-Serve` | Social Work |
| Maritime | `Maritime-Sea` | Marine Transportation |
| Agriculture | `Agri-Nature` | Agriculture, Fisheries |
| Hospitality | `Hospitality-Svc` | Hotel Management, Tourism |

### 3. Skill Traits (6 traits)
| Trait | Description |
|-------|-------------|
| Technical-Skill | Computers, machines, equipment |
| People-Skill | Communication, empathy, teamwork |
| Creative-Skill | Design, art, innovation |
| Analytical-Skill | Math, logic, research |
| Physical-Skill | Sports, hands-on work |
| Admin-Skill | Organization, planning |

### How Courses Use Traits
Each course has exactly **3 traits**:
```python
{
    "course_name": "BS Nursing",
    "trait_tag": ["Social", "Patient-Care", "People-Skill"]
    #              ^RIASEC   ^Specialized    ^Skill
}
```

### Trait Similarity Relationships
Related traits have defined similarity scores for partial matching:
```python
SPECIALIZED_TRAIT_RELATIONSHIPS = {
    "Patient-Care": {
        "Social": 0.8,          # Strong relationship
        "People-Skill": 0.9,    # Very strong
        "Rehab-Therapy": 0.6,   # Moderate
        "Medical-Lab": 0.4,     # Weak
    },
    # ... more relationships
}
```

---

## Database Schema

```
┌──────────────────┐     ┌──────────────────┐
│      users       │     │      tests       │
├──────────────────┤     ├──────────────────┤
│ user_id (PK)     │     │ test_id (PK)     │
│ fullname         │     │ name             │
│ email (unique)   │     │ description      │
│ hashed_password  │     └────────┬─────────┘
│ role             │              │
│ created_at       │              │
└────────┬─────────┘              │
         │                        │
         │     ┌──────────────────┴───────────────┐
         │     │                                   │
         ▼     ▼                                   ▼
┌──────────────────────┐              ┌──────────────────┐
│    test_attempts     │              │    questions     │
├──────────────────────┤              ├──────────────────┤
│ attempt_id (PK)      │              │ question_id (PK) │
│ user_id (FK)         │              │ test_id (FK)     │
│ test_id (FK)         │              │ question_text    │
│ started_at           │              │ category         │
│ completed_at         │              │ question_type    │
│ recommendation_json  │              └────────┬─────────┘
└──────────┬───────────┘                       │
           │                                   │
           ▼                                   ▼
┌──────────────────────┐              ┌──────────────────┐
│   student_answers    │              │     options      │
├──────────────────────┤              ├──────────────────┤
│ answer_id (PK)       │              │ option_id (PK)   │
│ attempt_id (FK)      │◄─────────────│ question_id (FK) │
│ question_id (FK)     │              │ option_text      │
│ option_id (FK)       │              │ trait_tag        │
│ answered_at          │              │ weight           │
└──────────────────────┘              └──────────────────┘

┌──────────────────┐
│     courses      │
├──────────────────┤
│ course_id (PK)   │
│ course_name      │
│ description      │
│ trait_tag        │  ← Comma-separated or JSON array
│ required_strand  │
│ minimum_gwa      │
└──────────────────┘
```

---

## API Endpoints

### Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/signup` | Register new user |
| POST | `/login` | Authenticate user |

### Assessment
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/assessment/tiers` | Get available tiers |
| GET | `/assessment/{tier}` | Get questions for tier |
| POST | `/submit-assessment` | Submit answers, get results |
| GET | `/questions` | Get random questions (legacy) |

### Adaptive Assessment
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/adaptive/start` | Start adaptive session |
| GET | `/adaptive/question/{session_id}` | Get next question |
| POST | `/adaptive/answer` | Submit answer |
| POST | `/adaptive/finish` | End early, get results |

### User Data
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/user/{user_id}/history` | Get test history |
| PUT | `/user/{user_id}/profile` | Update profile |

### Admin
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/admin/courses` | List all courses |
| POST | `/admin/courses` | Create course |
| PUT | `/admin/courses/{id}` | Update course |
| DELETE | `/admin/courses/{id}` | Delete course |
| GET | `/admin/questions` | List all questions |
| POST | `/admin/questions` | Create question |
| GET | `/admin/reports` | View reports |

---

## Frontend Components

### Pages
| Component | Path | Description |
|-----------|------|-------------|
| Login | `/login` | User authentication |
| Signup | `/signup` | User registration |
| Dashboard | `/dashboard` | Main user dashboard |
| AssessmentForm | `/assessment` | Take assessment |
| AdaptiveAssessment | `/adaptive` | Akinator-style assessment |
| ResultsView | `/results` | View recommendations |
| ProfileForm | `/profile` | Edit user profile |

### Admin Pages
| Component | Path | Description |
|-----------|------|-------------|
| Admin | `/admin` | Admin dashboard |
| ManageCourse | `/admin/courses` | CRUD courses |
| ManageQuestion | `/admin/questions` | CRUD questions |
| ViewUser | `/admin/users` | View users |
| ViewReport | `/admin/reports` | View reports |

---

## Assessment Types

### 1. Standard Assessment (Tiered)
| Tier | Questions | Time | Use Case |
|------|-----------|------|----------|
| Quick | 15 | 5-8 min | Quick exploration |
| Standard | 30 | 10-15 min | Recommended |
| Comprehensive | 50 | 20-25 min | Most accurate |

**Features:**
- Questions randomly selected from pool of 70
- Different questions each attempt
- All questions shown upfront

### 2. Adaptive Assessment (Akinator-Style)
| Setting | Value |
|---------|-------|
| Min Questions | 10 |
| Max Questions | 25 |
| Confidence Threshold | 75% |
| Top Recommendations | 5 |

**Features:**
- Questions selected based on information gain
- Dynamically picks best next question
- Can finish early when confident
- Shows real-time course narrowing

---

## Data Summary

| Data Type | Count |
|-----------|-------|
| Courses | 99 |
| Questions | 70 |
| Unique Traits | 38 |
| Assessment Tiers | 3 |

---

## File Structure

```
Course-Recommendation-System/
├── backend/
│   ├── main.py                    # FastAPI app, all endpoints
│   ├── models.py                  # SQLAlchemy models
│   ├── database.py                # DB connection
│   ├── schema.py                  # Pydantic schemas
│   ├── security.py                # JWT, password hashing
│   ├── seed_data.py               # Data imports, tier config
│   ├── courses_specialized.py     # 99 courses with traits
│   ├── questions_specialized.py   # 70 questions with traits
│   ├── adaptive_assessment.py     # Adaptive engine
│   ├── assessment_service.py      # Tier-based assessment
│   ├── trait_system.py            # Trait relationships
│   └── requirements.txt           # Python dependencies
│
├── frontend/
│   ├── src/
│   │   ├── App.js                 # Main router
│   │   ├── Login.js               # Login page
│   │   ├── Signup.js              # Registration
│   │   ├── Dashboard.js           # User dashboard
│   │   ├── AssessmentForm.js      # Standard assessment
│   │   ├── AdaptiveAssessment.js  # Adaptive assessment
│   │   ├── ResultsView.js         # Show recommendations
│   │   ├── ProfileForm.js         # User profile
│   │   └── admin/                 # Admin components
│   │       ├── Admin.js
│   │       ├── ManageCourse.js
│   │       ├── ManageQuestion.js
│   │       ├── ViewUser.js
│   │       └── ViewReport.js
│   └── package.json
│
└── SYSTEM_DOCUMENTATION.md        # This file
```

---

## Progress Assessment

### ✅ Completed Features (90%)

| Feature | Status | Notes |
|---------|--------|-------|
| User Authentication | ✅ 100% | Login, signup, JWT |
| User Dashboard | ✅ 100% | View history, profile |
| Standard Assessment | ✅ 100% | 3 tiers, randomization |
| Adaptive Assessment | ✅ 100% | Akinator-style |
| Course Database | ✅ 100% | 99 courses |
| Question Database | ✅ 100% | 70 questions |
| Trait System | ✅ 100% | 38 unique traits |
| Recommendation Engine | ✅ 100% | Matching algorithm |
| Results Display | ✅ 100% | Top 5 with reasoning |
| Assessment History | ✅ 100% | Track all attempts |
| Admin - Courses | ✅ 100% | CRUD operations |
| Admin - Questions | ✅ 100% | CRUD operations |
| Admin - Users | ✅ 100% | View users |
| Admin - Reports | ✅ 90% | Basic reports |
| Question Randomization | ✅ 100% | Different each time |

### 🔄 Potential Improvements (10%)

| Feature | Status | Priority |
|---------|--------|----------|
| Email Verification | ❌ Not started | Low |
| Password Reset | ❌ Not started | Medium |
| Export Results (PDF) | ❌ Not started | Low |
| More Detailed Reports | 🔄 Partial | Low |
| Mobile Responsive Polish | 🔄 Partial | Medium |
| Unit Tests | ❌ Not started | Low |

### Overall Progress: **~90% Complete**

The system is **fully functional** with all core features working:
- Users can register, login, take assessments
- Both standard and adaptive assessments work
- Recommendations are accurate with the new trait system
- Admin can manage all data
- History is tracked properly

The remaining 10% consists of nice-to-have features that aren't critical for the core functionality.
