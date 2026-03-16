# CoursePro — Complete System Reviewer & Defense Guide

> **Purpose of this document:** This is a comprehensive reviewer of every part of the CoursePro College Course Recommendation System—from the database schema to the algorithms, from the backend API to the frontend pages. Use this to study before your thesis defense.

---

# TABLE OF CONTENTS

1. [Objectives Verification](#1-objectives-verification)
2. [System Architecture](#2-system-architecture)
3. [Database Schema (9 Tables)](#3-database-schema-9-tables)
4. [Backend File-By-File Walkthrough](#4-backend-file-by-file-walkthrough)
5. [Authentication System (Login / Signup / Google OAuth)](#5-authentication-system)
6. [Profile System](#6-profile-system)
7. [Adaptive Assessment Engine — Full Deep Dive](#7-adaptive-assessment-engine)
8. [Recommendation Engine — Full Deep Dive](#8-recommendation-engine)
9. [Trait System & Trait Mapping](#9-trait-system--trait-mapping)
10. [Frontend File-By-File Walkthrough](#10-frontend-file-by-file-walkthrough)
11. [Complete API Endpoint Reference](#11-complete-api-endpoint-reference)
12. [Admin System](#12-admin-system)
13. [Feedback System](#13-feedback-system)
14. [Security Implementation](#14-security-implementation)
15. [Technologies & Libraries](#15-technologies--libraries)
16. [Theories & References for Defense](#16-theories--references-for-defense)
17. [Complete Decision Tree Diagram](#17-complete-decision-tree-diagram)
18. [Complete Rule-Based System Table](#18-complete-rule-based-system-table)
19. [Trait Relationship Map](#19-trait-relationship-map)
20. [Score Calculation Walkthrough (Step by Step Example)](#20-score-calculation-walkthrough)
21. [Possible Panel Questions & Answers (30+)](#21-possible-panel-questions--answers)

---

# 1. OBJECTIVES VERIFICATION

| # | Objective (from Chapter 1) | Met? | Evidence in Code |
|---|---|---|---|
| **General** | Develop a College Course Recommendation System using Rule-Based Logic and Decision Tree | **YES** | `recommendation_engine.py` — `RuleBasedFilter` class (Phase 1) and `DecisionTreeClassifier` class (Phase 2) |
| **SO1** | Obtain a validated dataset of SHS student profiles (interests, skills, academic performance, learning styles) | **YES** | `ProfileForm.js` collects GWA, strand, age, gender, interests (36 options), skills (32 options). Stored in `users.academic_info` JSON column. 193 questions in `questions_enhanced.py` with 8-10 options each. |
| **SO2** | Produce a filtered shortlist of eligible courses using rule-based constraints | **YES** | `RuleBasedFilter.filter_courses()` applies 8 rules (A1, A2, P1, P2, P3, P6, P7, P8, N3) to all 99 courses. Returns scored `FilteredCourse` objects sorted by eligibility. |
| **SO3** | Deliver ranked recommendations through decision tree analysis | **YES** | `DecisionTreeClassifier.classify()` traverses a pre-built tree from ROOT → trait_category → sub-attributes → leaf node. Returns classification + score modifier (+15 to +25). Final score = Phase 1 + Phase 2. |
| **SO4** | Present recommendations with transparent rationale via user-friendly interface | **YES** | `ResultsView.js` shows: match %, tier labels (Excellent/Good/Fair/Exploratory), reasoning text explaining WHY each course was recommended, matched traits, GWA requirement, recommended strand. |
| **SO5** | Demonstrate effectiveness by measuring accuracy and usability | **PARTIAL** | System has built-in feedback (1-5 star ratings per course in `RecommendationFeedback` table). You need to add actual survey results from respondents. |
| **SO6** | Test using User Acceptance Testing | **YOU DO THIS** | System is fully functional and testable. You conduct the UAT with respondents. |

**VERDICT:** All technical objectives (SO1–SO4) are 100% implemented in code. SO5 and SO6 depend on your actual survey/testing data collection.

---

# 2. SYSTEM ARCHITECTURE

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           USER'S BROWSER                                    │
│                                                                             │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                    FRONTEND  (React.js)                             │   │
│   │   localhost:3000  or  https://coursepro.ildf.site                   │   │
│   │                                                                     │   │
│   │   Pages:                                                            │   │
│   │   ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐              │   │
│   │   │ Landing  │ │  Login   │ │  Signup  │ │Dashboard │              │   │
│   │   └──────────┘ └──────────┘ └──────────┘ └──────────┘              │   │
│   │   ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐              │   │
│   │   │ Profile  │ │Assessment│ │ Results  │ │ Activity │              │   │
│   │   └──────────┘ └──────────┘ └──────────┘ └──────────┘              │   │
│   │   ┌──────────┐                                                      │   │
│   │   │ Settings │                                                      │   │
│   │   └──────────┘                                                      │   │
│   │                                                                     │   │
│   │   Communication: Axios HTTP client → sends JSON requests            │   │
│   │   Auth: JWT token stored in localStorage, sent as Bearer header     │   │
│   └──────────────────────────────────┬──────────────────────────────────┘   │
│                                      │ HTTP / JSON                          │
└──────────────────────────────────────┼──────────────────────────────────────┘
                                       │
                                       ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│                         BACKEND  (FastAPI / Python)                          │
│                    localhost:8000  or  Railway deployment                    │
│                                                                              │
│   ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────────────┐  │
│   │   main.py         │  │  security.py      │  │  recommendation_engine  │  │
│   │   (API endpoints) │  │  (JWT + bcrypt)   │  │  .py (Phase 1 + 2)     │  │
│   └──────────────────┘  └──────────────────┘  └──────────────────────────┘  │
│   ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────────────┐  │
│   │  adaptive_        │  │  trait_system.py  │  │  trait_mapping.py       │  │
│   │  assessment.py    │  │  (28 traits)      │  │  (rare→common map)     │  │
│   └──────────────────┘  └──────────────────┘  └──────────────────────────┘  │
│   ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────────────┐  │
│   │  models.py        │  │  database.py      │  │  seed_data.py /        │  │
│   │  (9 ORM models)   │  │  (DB connection)  │  │  questions_enhanced.py │  │
│   └──────────────────┘  └──────────────────┘  └──────────────────────────┘  │
│                                                                              │
│   CORS: Only allows requests from coursepro.ildf.site and localhost:3000    │
└──────────────────────────────────────┬───────────────────────────────────────┘
                                       │ SQLAlchemy ORM
                                       ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│                         DATABASE  (PostgreSQL)                                │
│                         coursepro_db  or  SQLite fallback                    │
│                                                                              │
│   Tables: users, tests, test_attempts, questions, options,                  │
│           student_answers, courses, recommendations, recommendation_feedback │
│                                                                              │
│   Features: JSON columns, connection pooling (10 + 20 overflow),            │
│             auto-migration on startup, auto-seeding if empty                │
└──────────────────────────────────────────────────────────────────────────────┘
```

**Data Flow Summary:**
1. User opens browser → React frontend loads
2. User interacts (clicks, fills forms) → Frontend sends HTTP request via Axios
3. Axios attaches JWT token in `Authorization: Bearer <token>` header
4. FastAPI backend receives request → validates JWT → processes logic
5. Backend queries PostgreSQL via SQLAlchemy ORM
6. Backend returns JSON response → Frontend renders the result

---

# 3. DATABASE SCHEMA (9 Tables)

## 3.1 users

| Column | Type | Description |
|---|---|---|
| `user_id` | Integer (PK) | Auto-increment primary key |
| `username` | String(50) UNIQUE | Login username, must be unique |
| `password_hash` | String(255) | bcrypt hash of password (never plain text) |
| `first_name` | String(50) | First name (capitalized) |
| `last_name` | String(50) | Last name (capitalized) |
| `email` | String(100) UNIQUE | Email address (lowercase) |
| `academic_info` | JSON | `{gwa, strand, age, gender, interests, skills}` |
| `created_at` | DateTime | Account creation timestamp (auto) |
| `last_active` | DateTime | Last login timestamp |
| `is_online` | Integer | 1 = online, 0 = offline |
| `is_active` | Integer | 1 = active, 0 = deactivated by admin |
| `is_admin` | Integer | 1 = admin, 0 = regular user |

**Relationships:** Has many `test_attempts`, has many `recommendations`

**Computed property:** `fullname` → returns `first_name + last_name`

**academic_info JSON structure:**
```json
{
  "gwa": 92.5,
  "strand": "STEM",
  "age": 18,
  "gender": "Male",
  "interests": "programming,science,engineering",
  "skills": "problem_solving,data_analysis,leadership"
}
```

---

## 3.2 tests

| Column | Type | Description |
|---|---|---|
| `test_id` | Integer (PK) | Auto-increment |
| `test_name` | String(100) | Name of the test |
| `test_type` | String(50) | "assessment" or "adaptive" |
| `description` | Text | Description of the test |

**Seeded data:** One test: "Career Assessment" (type: "assessment"). An "adaptive" test is auto-created when the first adaptive session runs.

---

## 3.3 test_attempts

| Column | Type | Description |
|---|---|---|
| `attempt_id` | Integer (PK) | Auto-increment |
| `user_id` | Integer (FK → users) | Who took the assessment |
| `test_id` | Integer (FK → tests) | Which test type |
| `taken_at` | DateTime | When the attempt started (auto) |
| `max_questions` | Integer | Quiz length selected by student (30, 50, or 60) |
| `questions_presented` | Integer | How many questions were actually shown |
| `questions_answered` | Integer | How many questions were actually answered |
| `confidence_score` | Float | Final confidence % when assessment ended |
| `user_gwa` | Float | Snapshot of user's GWA at time of assessment |
| `user_strand` | String(50) | Snapshot of user's strand at time of assessment |

**Relationships:** Belongs to `user`, belongs to `test`, has many `student_answers`, has many `recommendations`

**Why snapshot GWA/strand?** A user can update their profile later. The snapshot preserves what their profile was when they took the assessment, so historical data stays accurate.

---

## 3.4 questions

| Column | Type | Description |
|---|---|---|
| `question_id` | Integer (PK) | Auto-increment |
| `test_id` | Integer (FK → tests) | Which test this belongs to |
| `question_text` | Text | The question text displayed to the user |
| `category` | String(50) | e.g., "Situational", "Assessment", "Academic", "Technology", "Healthcare" |
| `question_type` | String(30) | "standard", "scale", "career_path", "extracurricular", "situational_mapped" |

**Seeded data:** 193 questions from `questions_enhanced.py`, each with 8-10 options.

**Question types explained:**
- **standard** — Pick one option, adds +1 to that trait
- **scale** — Likert scale (1-5), multiplied by weight
- **career_path** — Options map to specific careers, adds +2 to primary trait and +1.5 to multiple trait tags
- **extracurricular** — About activities outside school, same scoring as career_path
- **situational_mapped** — "What would you do in this situation?", same scoring as career_path

---

## 3.5 options

| Column | Type | Description |
|---|---|---|
| `option_id` | Integer (PK) | Auto-increment |
| `question_id` | Integer (FK → questions) | Which question this belongs to |
| `option_text` | Text | The option text displayed |
| `trait_tag` | String(100) | Primary trait tag (e.g., "Software-Dev", "Patient-Care") |
| `weight` | Integer | For scale questions: 1-5 weight multiplier |
| `trait_tags_json` | JSON | Additional trait tags for career_path/extracurricular questions |
| `recommended_courses_json` | JSON | Direct course name recommendations for career_path questions |

**Example:** A question about career interest might have an option like:
```
option_text: "I'd love to develop software and build apps"
trait_tag: "Software-Dev"
trait_tags_json: ["Technical-Skill", "Data-Analytics"]
recommended_courses_json: ["BS Computer Science", "BS Information Technology"]
```

---

## 3.6 student_answers

| Column | Type | Description |
|---|---|---|
| `answer_id` | Integer (PK) | Auto-increment |
| `attempt_id` | Integer (FK → test_attempts) | Which attempt |
| `question_id` | Integer (FK → questions) | Which question |
| `chosen_option_id` | Integer (FK → options) | Which option the student selected |

---

## 3.7 courses

| Column | Type | Description |
|---|---|---|
| `course_id` | Integer (PK) | Auto-increment |
| `course_name` | String(100) | Full course name (e.g., "BS Computer Science") |
| `description` | Text | Course description |
| `trait_tag` | String | Comma-separated trait tags (e.g., "Software-Dev, Data-Analytics, Technical-Skill") |
| `required_strand` | String(50) | Recommended SHS strand (e.g., "STEM", "ABM") |
| `minimum_gwa` | Numeric(5,2) | Minimum GWA recommendation (soft constraint) |

**Seeded data:** 99 college courses from `courses_specialized.py`

---

## 3.8 recommendations

| Column | Type | Description |
|---|---|---|
| `recommendation_id` | Integer (PK) | Auto-increment |
| `attempt_id` | Integer (FK → test_attempts) | Which assessment attempt |
| `user_id` | Integer (FK → users) | Who received the recommendation |
| `course_id` | Integer (FK → courses) | Which course was recommended |
| `reasoning` | Text | Human-readable text explaining why |
| `score` | Float | Match percentage (0-100) |
| `recommended_at` | DateTime | Timestamp (auto) |

**Relationships:** Has many `recommendation_feedback`

---

## 3.9 recommendation_feedback

| Column | Type | Description |
|---|---|---|
| `feedback_id` | Integer (PK) | Auto-increment |
| `recommendation_id` | Integer (FK → recommendations, nullable) | Which recommendation (null for overall feedback) |
| `user_id` | Integer (FK → users, nullable) | Who gave feedback |
| `rating` | Integer | 1-5 stars |
| `feedback_text` | Text (nullable) | Optional comment |
| `created_at` | DateTime | Timestamp (auto) |

---

# 4. BACKEND FILE-BY-FILE WALKTHROUGH

## 4.1 `database.py` — Database Connection

**What it does:** Connects to PostgreSQL (or SQLite fallback).

**How it works:**
1. Reads `DATABASE_URL` from `.env` file
2. If not found → falls back to SQLite (`coursepro.db`)
3. For PostgreSQL: creates engine with connection pool (10 connections, 20 overflow)
4. For SQLite: creates engine with `check_same_thread=False`
5. Tests connection on startup
6. Exports: `engine`, `SessionLocal` (session factory), `Base` (declarative base for models)

---

## 4.2 `models.py` — Database Models (ORM)

**What it does:** Defines all 9 database tables as Python classes using SQLAlchemy.

**Every table is a class:**
- `User` → `users` table
- `Test` → `tests` table
- `TestAttempt` → `test_attempts` table
- `Question` → `questions` table
- `Option` → `options` table
- `StudentAnswer` → `student_answers` table
- `Course` → `courses` table
- `Recommendation` → `recommendations` table
- `RecommendationFeedback` → `recommendation_feedback` table

**Relationships defined:**
- User ← (one-to-many) → TestAttempt (cascade delete)
- User ← (one-to-many) → Recommendation (cascade delete)
- Test ← (one-to-many) → Question (cascade delete)
- Test ← (one-to-many) → TestAttempt (cascade delete)
- TestAttempt ← (one-to-many) → StudentAnswer (cascade delete)
- TestAttempt ← (one-to-many) → Recommendation (cascade delete)
- Question ← (one-to-many) → Option (cascade delete)
- Course ← (one-to-many) → Recommendation (cascade delete)
- Recommendation ← (one-to-many) → RecommendationFeedback (cascade delete)

---

## 4.3 `security.py` — Authentication & Authorization

**What it does:** Handles password hashing, JWT token creation/validation, and access control.

**Functions:**
| Function | What it does |
|---|---|
| `hash_password(password)` | Hashes a plaintext password using bcrypt |
| `verify_password(plain, hashed)` | Compares plaintext against bcrypt hash (returns True/False) |
| `create_access_token(data, expires_delta)` | Creates a signed JWT containing user_id, username, is_admin. Default expiry: 24 hours. Algorithm: HS256 |
| `decode_access_token(token)` | Decodes and verifies a JWT. Raises 401 if invalid/expired |
| `get_current_user(token, db)` | FastAPI dependency — extracts JWT from Authorization header, queries DB for user, checks if active. Returns User object or raises 401/403 |
| `require_admin(current_user)` | FastAPI dependency — checks `is_admin == 1`. Raises 403 if not admin |
| `require_self_or_admin(user_id, current_user)` | FastAPI dependency — ensures user is accessing their own data OR is admin |

**JWT payload structure:**
```json
{
  "user_id": 1,
  "username": "john_doe",
  "is_admin": false,
  "exp": 1710460800
}
```

---

## 4.4 `trait_system.py` — Personality Trait System

**What it does:** Defines the 28 personality traits and their relationships.

**The 28 traits:**

| Category | Traits | Count |
|---|---|---|
| RIASEC Types | Realistic, Investigative, Artistic, Social, Enterprising, Conventional | 6 |
| Healthcare | Patient-Care, Medical-Lab, Rehab-Therapy, Health-Admin | 4 |
| Technology | Software-Dev, Hardware-Systems, Data-Analytics, Cyber-Defense | 4 |
| Engineering | Civil-Build, Electrical-Power, Mechanical-Design, Industrial-Ops | 4 |
| Business | Finance-Acct, Marketing-Sales, Startup-Venture | 3 |
| Education | Teaching-Ed | 1 |
| Arts | Visual-Design, Digital-Media, Spatial-Design | 3 |
| Science | Lab-Research, Field-Research | 2 |
| Public Service | Law-Enforce, Community-Serve | 2 |
| Maritime | Maritime-Sea | 1 |
| Agriculture | Agri-Nature | 1 |
| Hospitality | Hospitality-Svc | 1 |
| Skills | Technical-Skill, People-Skill, Creative-Skill, Analytical-Skill, Physical-Skill, Admin-Skill | 6 |
| **TOTAL** | | **28 specialized + 6 skill = 34** |

**Trait relationships (similarity scores 0.0–1.0):**

Every specialized trait has defined relationships. Examples:
- `Software-Dev` → `Investigative: 0.8`, `Technical-Skill: 0.9`, `Data-Analytics: 0.6`, `Cyber-Defense: 0.5`
- `Patient-Care` → `Social: 0.8`, `People-Skill: 0.9`, `Rehab-Therapy: 0.6`, `Community-Serve: 0.5`
- `Finance-Acct` → `Conventional: 0.9`, `Analytical-Skill: 0.8`, `Admin-Skill: 0.6`

These relationships are used for:
1. **Partial matching** — if a student scores high on "Software-Dev" and a course needs "Data-Analytics", the 0.6 similarity gives partial credit
2. **Mapped trait boosting** — when a student answers a question tagged "Software-Dev", related traits like "Technical-Skill" also get +0.5

---

## 4.5 `trait_mapping.py` — Rare-to-Common Trait Consolidation

**What it does:** Maps 40+ rare/specific course traits to common question traits.

**Examples:**
```
"Data-driven"      → "Quantitative"
"Clinical-science"  → "Laboratory"
"Compassionate"     → "Empathetic"
"Civic-minded"      → "Governance-focus"
"World-building"    → "Creative-expression"
"Safety-conscious"  → "Methodical"
```

**Why?** Some courses have niche trait tags that don't directly appear in questions. This mapping ensures they still match when relevant questions are answered.

---

## 4.6 `seed_data.py` / `questions_enhanced.py` / `courses_specialized.py`

**seed_data.py:** Contains the original 99 courses (`COURSES_POOL`), assessment tier configs, scale weights, learning style mappings, work environment mappings, and career goal mappings.

**questions_enhanced.py:** Contains 193 assessment questions (`QUESTIONS_POOL_ENHANCED`), each with 8-10 options. Categories include: Technology, Healthcare, Engineering, Business, Education, Arts, Maritime, Agriculture, Hospitality, Criminology, Science, Public Service, General, Situational.

**courses_specialized.py:** Contains the 99 college courses with updated trait tags using the specialized trait system (e.g., "Software-Dev, Data-Analytics, Technical-Skill" for BS Computer Science).

---

## 4.7 `adaptive_assessment.py` — Adaptive Assessment Engine (MOST IMPORTANT)

Detailed in [Section 7](#7-adaptive-assessment-engine).

## 4.8 `recommendation_engine.py` — Hybrid Recommendation Engine

Detailed in [Section 8](#8-recommendation-engine).

## 4.9 `main.py` — API Endpoints & Application Logic

Detailed in [Section 11](#11-complete-api-endpoint-reference).

---

# 5. AUTHENTICATION SYSTEM

## 5.1 Regular Signup Flow

```
User fills: username, fullname, email, password
    │
    ▼
Frontend (Signup.js) validates:
  - Username: 3+ chars, alphanumeric + underscores only
  - Fullname: 2+ chars, letters/spaces/hyphens/apostrophes, no bad words
  - Email: must match regex ^[^\s@]+@[^\s@]+\.[^\s@]+$
  - Password: 6+ chars, must match confirm field
    │
    ▼
POST /signup {username, fullname, email, password}
    │
    ▼
Backend (main.py) validates:
  - Email format (regex)
  - Username not already taken (DB query)
  - Email not already taken (DB query)
  - Fullname not containing bad words (English + Filipino)
  - Fullname auto-capitalized
    │
    ▼
Backend creates User:
  - password → bcrypt hash (never stores plain text)
  - fullname → split into first_name + last_name
  - email → lowercased
    │
    ▼
Returns {"message": "Success"}
```

## 5.2 Regular Login Flow

```
User enters: username OR email + password
    │
    ▼
POST /login {username, password}
    │
    ▼
Backend:
  1. Detects if input is email (contains @) or username
  2. Queries DB for matching user
  3. Calls verify_password(plain, hashed) using bcrypt
  4. If wrong → 400 "Invalid username/email or password"
  5. Checks is_active → if 0 → 403 "Account is deactivated"
  6. Marks user as online (is_online = 1)
  7. Updates last_active timestamp
  8. Creates JWT with {user_id, username, is_admin}, expiry: 24 hours
    │
    ▼
Returns: {user, user_id, username, email, access_token, token_type: "bearer"}
    │
    ▼
Frontend stores in localStorage:
  - userName, userId, userEmail, accessToken
```

## 5.3 Google OAuth Login Flow

```
User clicks "Continue with Google"
    │
    ▼
Google OAuth popup → user signs in with Google account
    │
    ▼
Frontend receives Google credential (JWT from Google)
    │
    ▼
Frontend decodes Google JWT → gets email, name
    │
    ▼
POST /google-login {email, name}
    │
    ├── User EXISTS in DB:
    │     → Same login flow as regular (JWT created, user marked online)
    │     → Returns {needs_username: false, access_token, ...}
    │
    └── User DOES NOT EXIST:
          → Returns {needs_username: true, email, name}
          │
          ▼
        Frontend shows modal: "Choose a username"
          │
          ▼
        POST /google-register {email, name, username}
          │
          ▼
        Backend creates User with:
          - chosen username
          - dummy password hash (google_oauth_{email})
          - first_name + last_name from Google name
          - email from Google
          - marked as online
          │
          ▼
        Returns {access_token, ...}
```

## 5.4 JWT Token Lifecycle

```
1. Token CREATED on login (24-hour expiry)
2. Token STORED in localStorage as "accessToken"
3. Token ATTACHED to every API call via Axios interceptor:
     Authorization: Bearer <token>
4. Token VERIFIED on every protected endpoint by get_current_user():
     - Decodes JWT
     - Checks user exists in DB
     - Checks user is_active == 1
     - Returns User object
5. Token EXPIRES after 24 hours → 401 → frontend clears localStorage → redirect to login
```

## 5.5 Logout Flow

```
POST /logout {user_id}
  → Backend sets is_online = 0
  → Frontend clears all localStorage keys
  → Frontend redirects to landing page
```

---

# 6. PROFILE SYSTEM

## 6.1 What Data is Collected

| Field | Type | Options / Range |
|---|---|---|
| Full Name | String | Letters, spaces, hyphens, apostrophes. No bad words. |
| GWA | Float | 75.0 – 100.0 |
| SHS Strand | String | STEM, ABM, HUMSS, TVL, GAS, Sports, Arts |
| Age | Integer | Any valid age |
| Gender | String | Male, Female, Other |
| Interests | Comma-separated | 36 predefined options across 8 categories |
| Skills | Comma-separated | 32 predefined options across 6 categories |

## 6.2 Interest Options (36 total)

| Category | Options |
|---|---|
| Science & Research | Science, Biology, Chemistry, Physics, Environment |
| Technology | Programming, Computer, Data, AI, Cybersecurity |
| Engineering | Engineering, Mechanical, Electrical, Civil |
| Business & Finance | Business, Finance, Marketing, Accounting, Economics |
| Arts & Creative | Art, Music, Film, Writing, Photography |
| Healthcare | Medical, Nursing, Psychology |
| Social & Humanities | Education, Law, Politics, Social, History |
| Others | Sports, Tourism, Food, Agriculture |

## 6.3 Skill Options (32 total)

| Category | Options |
|---|---|
| Technical | Programming, Data Analysis, Web Development, Graphic Design, Video Editing, Math, Laboratory, Technical Writing |
| Communication | Public Speaking, Writing, Presentation, Negotiation, Foreign Language |
| Leadership | Leadership, Project Management, Team Management, Decision Making, Planning |
| Interpersonal | Teamwork, Empathy, Customer Service, Mentoring, Conflict Resolution |
| Analytical | Critical Thinking, Problem Solving, Research, Attention to Detail, Logical Reasoning |
| Creative | Creativity, Artistic, Music, Storytelling, Design Thinking |

## 6.4 How Profile Data Affects Recommendations

Profile data affects recommendations in THREE ways:

**1. During Adaptive Assessment — Initial Course Scores:**
- All 99 courses start at base score 50.0
- GWA bonus: +5 if meets course minimum, +2 if within 5 points
- Strand bonus: +5 if matches course's required strand
- Profile bonus: up to +15 per course based on interest/skill keyword matching

**2. During Adaptive Assessment — Question Selection:**
- First 5 questions are biased toward the student's profile interests/skills
- Strand-priority traits influence which questions are selected

**3. During Final Recommendation — Rule-Based Filtering:**
- Rule A1 (GWA): +10 for meeting minimum, penalty up to -15 for not meeting
- Rule A2 (Strand): +8 for exact match, +4 for compatible strand
- Rule P8 (Interests/Skills): up to +25 for keyword matches

---

# 7. ADAPTIVE ASSESSMENT ENGINE

**File:** `adaptive_assessment.py`
**Class:** `AdaptiveAssessmentEngine`
**Theory:** Decision Tree Algorithm with Information Gain (Quinlan, 1986; Shannon, 1948)

## 7.1 Configuration Constants

| Constant | Value | Meaning |
|---|---|---|
| `MAX_QUESTIONS` | 25 | Internal max (overridden by user's selection) |
| `MIN_QUESTIONS` | 10 | Internal min (overridden: 50% of user's selection) |
| `CONFIDENCE_THRESHOLD` | 0.75 | Stop if top courses are 75% ahead |
| `TOP_N_RECOMMENDATIONS` | 6 | Number of courses to recommend |

**User selects:** 30, 50, or 60 questions
- 30 → min 15, max 30
- 50 → min 25, max 50
- 60 → min 30, max 60

## 7.2 Session Initialization (`create_session()`)

When a student starts the assessment:

```
1. Generate unique session_id (8-char UUID)
2. Store user's GWA, strand, interests, skills
3. Calculate min_questions = max_questions × 0.5
4. Initialize ALL 99 courses with base score = 50.0
5. Apply initial bonuses per course:
   - GWA meets course minimum → +5
   - GWA within 5 points → +2
   - Strand matches → +5
   - Interest/skill keyword match → up to +15
6. Store initial_course_scores as a copy (used for recalculation on "Previous")
7. Initialize empty: trait_scores, answered_questions, rejected_topics, question_history
```

## 7.3 Question Selection Algorithm (`get_next_question()`)

This is the core adaptive algorithm. For every unanswered question:

### Step 1: Calculate Information Gain for each trait

```
For each trait in the dataset:
    active_with_trait = count of active courses that have this trait
    total_active = total active courses
    
    p = active_with_trait / total_active
    
    Entropy H = -p × log₂(p) - (1-p) × log₂(1-p)
    
    knowledge_penalty = 1 / (1 + |existing_trait_score| × 0.5)
    
    trait_value = H × knowledge_penalty
```

**In plain English:** A trait that appears in exactly 50% of courses has the highest entropy (most informative). A trait that appears in all or no courses has zero entropy (useless to ask about). Traits we already know about get penalized.

### Step 2: Score each candidate question

```
For each unanswered question:
    1. Skip if already answered (in excluded_question_ids)
    2. Skip if category matches a rejected topic
    3. Skip if >30% of options are about rejected topics
    
    4. Base score = sum of trait_values for each option's trait_tag
       + 0.5 bonus if option matches strand priority traits
       + 0.25 bonus for mapped traits matching strand
    
    5. Rejection penalty: if some options match rejected topics
       - >50% rejected → score × 0.1
       - >30% rejected → score × 0.4
       - >10% rejected → score × 0.7
    
    6. Option bonus: more options = more information
       bonus = min(len(options) / 4, 1.5)
    
    7. Category diversity: avoid asking same category repeatedly
       diversity = 1 / (1 + category_count × 0.2)
    
    8. FIRST 5 QUESTIONS: Profile relevance bonus
       - 3+ options match profile traits → +3.0
       - 2 options match → +2.0
       - 1 option matches → +1.0
```

### Step 3: Select the question with the highest score

The question with the highest combined score is selected as the next question.

## 7.4 Answer Processing (`process_answer()`)

When a student selects an answer:

```
1. Validate: session exists, not complete, question exists, option exists
2. Check for duplicate answer (prevent double-click)
3. Record answer: answered_questions[question_id] = option_id
4. Add question_id to excluded_question_ids
5. Append to question_history (for "Previous" button)

6. Check if answer is a rejection ("None", "Not interested", etc.):
   - Determine what topic was rejected
   - Add topic to rejected_topics set
   - Penalize courses with that topic: -8 points each
   - Store rejection data for reversal

7. If NOT a rejection:
   - Extract trait_tag from chosen option (e.g., "Software-Dev")
   - Add +1.0 to student's trait_score for that trait
   - Add +0.5 to related/mapped traits from EXPANDED_TRAIT_MAPPING
   - Store all trait changes for reversal

8. Update course scores for each boosted trait:
   - Direct match (trait in course): +12 × early_boost_multiplier
   - Similar (>70% similarity): +6 × early_boost_multiplier
   - Moderate (>40%): +3 × early_boost_multiplier
   - Weak (>20%): +1 × early_boost_multiplier

   Early boost multiplier:
   - Rounds 1-3: ×2.5 (first answers matter more)
   - Rounds 4-7: ×1.5
   - Rounds 8+:  ×1.0

9. Calculate new confidence score
10. Return: trait_recorded, confidence, top_courses_preview
```

## 7.5 Early Boost Multiplier — Why?

The first 3 answers get a `×2.5` multiplier because:
- Early answers reflect the student's strongest preferences
- They help the system quickly lock onto the right course direction
- Without this, the initial profile-based scores (max +15) would dominate too long

## 7.6 Rejection Handling

When a student picks "Not interested" or "None of the above":

```
1. Identify rejected topic via:
   a. Explicit keywords in option text (e.g., "don't want to teach" → Teaching-Ed)
   b. Category keywords mapping (e.g., "healthcare" category → Patient-Care)
   c. Most common trait among other options (majority vote)

2. Add rejected topic to session.rejected_topics

3. Penalize ALL courses that have this trait: -8 points each

4. Future questions: skip questions where the category matches rejection
   AND skip questions where >30% of options relate to rejected topics
```

**Rejection keyword examples:**
- "don't want to teach" → `Teaching-Ed`
- "not interested" in a healthcare question → `Patient-Care`
- "None" in a maritime question → `Maritime-Sea`

## 7.7 Previous Button — Answer Reversal (`go_to_previous_question()`)

```
1. Pop last question from question_history
2. Remove from answered_questions and excluded_question_ids
3. Reverse trait changes:
   - For each trait that was added, subtract the exact amount
   - If trait score becomes ≤ 0, delete it entirely
4. Reverse rejection data:
   - Remove rejected topics that were added by this question
   - Add back course penalties: +8 for each course that was penalized
5. Recalculate ALL course scores from scratch:
   - Reset to initial_course_scores (base 50 + GWA + strand + profile bonuses)
   - Re-apply all remaining trait-based scoring
6. Recalculate confidence
7. Decrement round_number
8. Return the previous question for re-answering
```

## 7.8 Confidence Calculation

```
sorted_scores = all course scores sorted descending

top_5_avg = average of top 5 course scores
rest_avg = average of courses ranked 6-15

gap_ratio = (top_5_avg - rest_avg) / top_5_avg

question_factor = min(round_number / min_questions, 1.0)

confidence = gap_ratio × 0.7 + question_factor × 0.3
             (clamped to 0.0 – 1.0)
```

**In plain English:** Confidence is high when the top 5 courses are far ahead of the rest AND we've asked enough questions.

## 7.9 Stopping Conditions

The assessment stops when ANY of these is true:
1. Student reached `max_questions` (30, 50, or 60) → forced stop
2. Student answered ≥ `min_questions` AND confidence ≥ 75% → early stop
3. No more valid questions available → forced stop

## 7.10 Session Finalization (`_finalize_session()`)

```
1. Mark session as complete
2. Sort all 99 courses by score (descending)
3. Take top 6 courses
4. Normalize scores to percentage:
   - normalized = (raw - min_score) / (max_score - min_score)
   - percentage = 55 + (normalized × 42)  → range: 55% to 97%
5. For each recommended course:
   - Find matched traits (intersection of student traits and course traits)
   - Calculate profile bonus for display
   - Generate recommendation reasoning text
6. Store as final_recommendations
```

## 7.11 Recommendation Reasoning Generation

For each recommended course, the system generates a human-readable paragraph:

```
1. Trait matches: "Your responses showed strong alignment with [trait labels]"
2. Profile interests: "This aligns with your stated interests: [matching interests]"
3. Skills: "Your skills in [matching skills] are valuable for this field"
4. Strand: "This is a natural progression from your [strand] strand"
5. Career reasoning: "The tech industry offers excellent career growth..." (based on course category)
6. Strong patterns: "You consistently showed preference for [strong trait]-related activities"
```

---

# 8. RECOMMENDATION ENGINE

**File:** `recommendation_engine.py`
**Class:** `HybridRecommendationEngine`
**Theory:** Rule-Based Expert Systems (Giarratano & Riley, 2005) + Decision Tree (Quinlan, 1986) + Hybrid Recommender Systems (Burke, 2002)

## 8.1 Two-Phase Architecture

```
    99 Courses
        │
        ▼
  ┌─────────────────────────────────────┐
  │  PHASE 1: RULE-BASED FILTERING     │
  │  (RuleBasedFilter class)            │
  │                                     │
  │  8 IF-THEN rules evaluated per      │
  │  course. Each adds/subtracts        │
  │  points. All courses stay eligible  │
  │  (soft constraints only).           │
  │                                     │
  │  Output: scored FilteredCourse list │
  └──────────────┬──────────────────────┘
                 │
                 ▼
  ┌─────────────────────────────────────┐
  │  PHASE 2: DECISION TREE             │
  │  (DecisionTreeClassifier class)     │
  │                                     │
  │  Traverses tree based on student's  │
  │  primary trait → sub-attributes.    │
  │  Classifies into career category.   │
  │  Adds +15 to +25 modifier to       │
  │  courses in that category.          │
  │                                     │
  │  Output: classification + modifier  │
  └──────────────┬──────────────────────┘
                 │
                 ▼
  ┌─────────────────────────────────────┐
  │  FINAL SCORE COMBINATION            │
  │                                     │
  │  Final = Phase1 Score + Phase2 Mod  │
  │  Sort descending → Top 6 courses    │
  │  Assign tier labels                 │
  │  Calculate match percentage         │
  └─────────────────────────────────────┘
```

## 8.2 Phase 1: Rule-Based Filtering — All 8 Rules in Detail

### Rule P1 — Primary Trait Alignment (Priority: 10)
```
IF student's #1 trait (highest score) matches ANY course trait:
  - Exact match → +20 points
  - Similar (≥70% similarity) → +14 to +19 points (scaled)
  - Moderate (≥50% similarity) → +10 points
ELSE → no boost (0 points, NOT a penalty)
```

### Rule P3 — Career Path Preference (Priority: 10)
```
IF course name is in the student's career_path_courses list
   (from career_path question options with recommended_courses_json):
THEN +25 points
ELSE → no boost
```

### Rule P2 — Trait Synergy Bonus (Priority: 9)
```
IF total meaningful trait matches ≥ 3
   (exact matches count as 1, similar matches count as 0.5):
THEN +15 points
ELSE → no boost
```

### Rule P8 — Interests & Skills Bonus (Priority: 8)
```
IF user's interests/skills keywords match course traits
   (using QUALITATIVE_KEYWORD_MAPPING — 100+ keywords mapped to traits):
THEN +5 per keyword match, capped at +25 points
ELSE → no boost
```

### Rule P6 — Work Environment Match (Priority: 7)
```
IF user's preferred work environment (determined from traits) matches course:
  - office traits: Office-based, Remote-friendly
  - field traits: Field-work, Outdoor-enthusiast
  - clinical traits: Clinical-setting, Patient-focused
  - laboratory traits: Laboratory, Research-oriented
  - studio traits: Studio-work, Creative-expression
THEN +8 points
ELSE → no boost
```

### Rule N3 — No Trait Match Penalty (Priority: 7)
```
IF zero user traits match ANY course trait:
THEN -15 points
ELSE → no penalty
```

### Rule P7 — Learning Style Match (Priority: 6)
```
IF user's learning style (determined from traits) matches course:
  - visual traits: Visual-learner, Aesthetic-sense, Digital-art
  - hands_on traits: Hands-on, Practical, Field-work
  - theoretical traits: Theoretical, Research-oriented
  - social traits: Collaborative, Team-centric
  - independent traits: Independent, Introverted
THEN +6 points
ELSE → no boost
```

### Rule A1 — GWA Academic Bonus (Priority: 5)
```
IF user_gwa ≥ course_minimum_gwa:
  → +10 points
ELSE IF user_gwa < course_minimum_gwa:
  → penalty = min(gap × 5, 15) points (capped at -15)
  → Course is STILL ELIGIBLE (never disqualified)
```

### Rule A2 — Strand Alignment Bonus (Priority: 4)
```
IF user_strand == course_required_strand:
  → +8 points (perfect match)
ELSE IF user_strand is in compatible_strands:
  → +4 points (partial match)
  Compatible: STEM↔GAS/TVL, ABM↔GAS/HUMSS, HUMSS↔GAS/ABM, etc.
ELSE:
  → 0 points (NO penalty — course is still available)
```

**CRITICAL:** GWA and strand are SOFT CONSTRAINTS ONLY. They add bonus/penalty points but NEVER remove a course from consideration. A STEM student can get recommended a HUMSS course if their trait scores are strong enough.

## 8.3 Phase 1: Enhanced Trait Matching

Before rules are applied, the system uses enhanced trait matching:

```
For each course:
  1. Get student's top 10 traits (sorted by score)
  2. Get course's trait tags (comma-separated)
  3. Calculate matches:
     - EXACT matches: trait appears in both lists → high score
     - SIMILAR matches: trait has >0.5 similarity (from trait_system.py) → partial score
     - CATEGORY matches: traits in same category → small bonus
  4. Return: trait_match_score, matched_traits list, match_details
  
  This trait_match_score becomes the BASE score for rule evaluation
```

## 8.4 Phase 1: Eligibility Score Calculation

```
eligibility_score = trait_match_score        (enhanced matching base)
                  + total_boost              (sum of all rule boosts)
                  - total_penalty            (sum of all penalties)
                  + synergy_bonus            (extra +5 or +10 for 3+ or 4+ exact matches)
```

## 8.5 Phase 2: Decision Tree — Complete Tree Structure

```
ROOT: What is the primary trait category?
│
├── "helping" (Helping-Others / Empathetic / Compassionate / Patient-focused)
│   │
│   ├── Work Setting = "clinical"
│   │   ├── GWA High (≥90) → healthcare_professional (+25, 90% conf)
│   │   ├── GWA Medium (≥85) → healthcare_allied (+20, 85% conf)
│   │   └── GWA Low (<85) → healthcare_support (+15, 75% conf)
│   │
│   ├── Work Setting = "office"
│   │   ├── Social Orientation = Extrovert → education_social (+20, 85% conf)
│   │   ├── Social Orientation = Introvert → counseling_support (+18, 80% conf)
│   │   └── Social Orientation = Balanced → public_service (+18, 80% conf)
│   │
│   ├── Work Setting = "field" → community_service (+20, 85% conf)
│   └── Default → office branch
│
├── "problem_solving" (Problem-solving / Analytical / Logical / Research-oriented)
│   │
│   ├── Analytical Type = "technical"
│   │   ├── GWA High → engineering_cs (+25, 90% conf)
│   │   ├── GWA Medium → it_technology (+20, 85% conf)
│   │   └── GWA Low → tech_vocational (+15, 75% conf)
│   │
│   ├── Analytical Type = "business"
│   │   ├── Leadership High → business_management (+22, 85% conf)
│   │   ├── Leadership Medium → business_general (+18, 80% conf)
│   │   └── Leadership Low → business_analytics (+20, 85% conf)
│   │
│   ├── Analytical Type = "research" → science_research (+22, 85% conf)
│   └── Default → technical branch
│
├── "creative" (Creative-expression / Innovative / Artistic-passion)
│   │
│   ├── Creative Type = "visual"
│   │   ├── Tech Affinity High → digital_media (+25, 90% conf)
│   │   ├── Tech Affinity Medium → design_arts (+22, 85% conf)
│   │   └── Tech Affinity Low → fine_arts (+20, 85% conf)
│   │
│   ├── Creative Type = "performing" → performing_arts (+20, 85% conf)
│   ├── Creative Type = "writing" → communication_media (+20, 85% conf)
│   └── Default → visual branch
│
├── "leading" (Leading-teams / Leadership / Strategic)
│   │
│   ├── Domain = "business" → business_leadership (+22, 85% conf)
│   ├── Domain = "public" → public_administration (+20, 85% conf)
│   ├── Domain = "technical" → engineering_management (+22, 85% conf)
│   └── Default → business branch
│
└── Default → problem_solving branch
```

## 8.6 Phase 2: How Attributes are Determined

| Attribute | How it's determined |
|---|---|
| `trait_category` | Primary trait is categorized: helping traits → "helping", analytical traits → "problem_solving", creative traits → "creative", leadership traits → "leading" |
| `work_setting` | From traits: clinical/patient traits → "clinical", field/outdoor traits → "field", else → "office" |
| `gwa_level` | ≥90 → "high", ≥85 → "medium", <85 → "low" |
| `social_orientation` | Count extrovert vs introvert traits in top traits |
| `analytical_type` | Count tech vs business vs research traits |
| `creative_type` | Count visual vs performing vs writing traits |
| `tech_affinity` | Count tech-savvy/digital/innovative traits: ≥2 = "high", 1 = "medium", 0 = "low" |
| `leadership_tendency` | Count leadership/strategic/big-picture traits |
| `domain_interest` | Count business vs public service vs technical traits |

## 8.7 Phase 2: Classification-to-Course Mapping

Each leaf node classifies the student into a category. Each category maps to specific courses:

| Classification | Example Courses |
|---|---|
| `healthcare_professional` | BS Nursing, BS Medical Technology, BS Pharmacy, BS Physical Therapy |
| `healthcare_allied` | BS Radiologic Technology, BS Respiratory Therapy, BS Nutrition and Dietetics |
| `engineering_cs` | BS Computer Science, BS Computer Engineering, BS Civil Engineering, BS Data Science |
| `it_technology` | BS Information Technology, BS Cybersecurity, BS Entertainment and Multimedia Computing |
| `business_management` | BS Entrepreneurship, BS Business Administration (Marketing, HR, Operations) |
| `business_analytics` | BS Accountancy, BS Management Accounting, BS Business Economics |
| `science_research` | BS Biology, BS Chemistry, BS Physics, BS Marine Biology, BS Environmental Science |
| `digital_media` | BS Multimedia Arts, BA in Animation, BA in Game Art and Design |
| `education_social` | Bachelor of Elementary/Secondary/Early Childhood/Physical Education |
| `public_administration` | Bachelor of Public Administration, BA in Political Science |
| ...and more | 20 total categories covering all 99 courses |

## 8.8 Final Score Combination

```
For each eligible course:
  rule_score = Phase 1 eligibility score
  tree_boost = Phase 2 modifier (0 if not in predicted category, +15 to +25 if matches)
  
  final_score = rule_score + tree_boost
```

## 8.9 Match Percentage Calculation

The raw `final_score` (which could be 0 to ~217) is converted to a 0-97% scale using a curve:

```
if final_score ≤ 40:    percentage = 25 + (score/40) × 20           → 25-45%
if final_score ≤ 70:    percentage = 45 + ((score-40)/30) × 20      → 45-65%
if final_score ≤ 100:   percentage = 65 + ((score-70)/30) × 15      → 65-80%
if final_score ≤ 130:   percentage = 80 + ((score-100)/30) × 10     → 80-90%
if final_score > 130:   percentage = 90 + min(7, ((score-130)/30)×7) → 90-97%

Clamped to range [25%, 97%]
```

## 8.10 Tier Assignment

| Tier | Condition |
|---|---|
| **EXCELLENT** | ≥3 exact trait matches AND no penalties AND in predicted category |
| **GOOD** | ≥2 exact matches OR (≥1 exact + ≥2 similar) |
| **FAIR** | ≥1 exact match OR ≥2 similar matches |
| **EXPLORATORY** | Everything else |

## 8.11 Diversity Selection

Top 6 courses are selected with diversity:
- Max 2 courses per strand (prevents all-STEM or all-ABM results)
- First pass: take EXCELLENT and GOOD courses
- Second pass: fill remaining slots from FAIR/EXPLORATORY

---

# 9. TRAIT SYSTEM & TRAIT MAPPING

## 9.1 Direct Trait Example: "Software-Dev"

When a student selects an option with `trait_tag: "Software-Dev"`:

```
1. trait_scores["Software-Dev"] += 1.0

2. Mapped traits from EXPANDED_TRAIT_MAPPING:
   trait_scores["Investigative"] += 0.5  (0.8 relationship)
   trait_scores["Technical-Skill"] += 0.5  (0.9 relationship)
   trait_scores["Data-Analytics"] += 0.5  (0.6 relationship)
   trait_scores["Cyber-Defense"] += 0.5  (0.5 relationship)

3. Course score updates (with early_boost at round 1 = ×2.5):
   "BS Computer Science" has trait_tag containing "Software-Dev"
   → Direct match: +12 × 2.5 = +30 points
   
   "BS Data Science" has "Data-Analytics" (similarity 0.6 to Software-Dev)
   → Similar (>40%): +3 × 2.5 = +7.5 points
   
   "BS Nursing" has "Patient-Care" (no similarity to Software-Dev)
   → No match: +0 points
```

## 9.2 Qualitative Keyword Mapping (100+ entries)

The `QUALITATIVE_KEYWORD_MAPPING` in `recommendation_engine.py` maps user interest/skill keywords to trait-related keywords. Examples:

```
"programming" → ["Technical", "Computational", "Software", "IT", "Analytical"]
"nursing"     → ["Healthcare", "Helping", "Medical", "Caregiving", "Clinical"]
"business"    → ["Business", "Entrepreneurial", "Fiscal", "Management", "Commercial"]
"art"         → ["Creative", "Artistic", "Visual", "Design", "Expressive"]
```

These are used in Rule P8 to give bonus points when a user's interests/skills keywords match course trait keywords.

## 9.3 Profile-to-Trait Mapping (for Question Selection)

The `PROFILE_TO_TRAITS` mapping in `adaptive_assessment.py` translates interests/skills to specialized traits:

```
"programming"    → ["Software-Dev", "Data-Analytics", "Cyber-Defense"]
"medical"        → ["Patient-Care", "Medical-Lab", "Rehab-Therapy"]
"business"       → ["Startup-Venture", "Marketing-Sales", "Finance-Acct"]
"graphic_design" → ["Visual-Design", "Digital-Media"]
"leadership"     → ["Startup-Venture", "Admin-Skill"]
"empathy"        → ["Patient-Care", "Rehab-Therapy"]
```

This is used to:
1. Give initial course score bonuses (up to +15)
2. Prioritize early questions to match the student's stated interests

---

# 10. FRONTEND FILE-BY-FILE WALKTHROUGH

## 10.1 `api.js` — API Client

**Purpose:** Pre-configured Axios instance with JWT interceptor.

- Creates Axios instance with `baseURL` from `REACT_APP_API_URL` environment variable
- **Request interceptor:** Automatically attaches `Authorization: Bearer {token}` from localStorage to every request
- **Response interceptor:** If any API returns 401, clears all auth data from localStorage and redirects to login
- Also exports: `authHeaders()` helper and `authFetch()` for native fetch calls

## 10.2 `App.js` — Root Component & Router

**Hash-based routing:**
| URL Fragment | Component | Auth Required |
|---|---|---|
| `#/landing` | `LandingPage` | No |
| `#/login` | `Login` | No |
| `#/signup` | `Signup` | No |
| `#/dashboard` | `Dashboard` | Yes |
| `#/profile` | `ProfileView` | Yes |
| `#/settings` | `Settings` (lazy) | Yes |
| `#/assessment` | `AdaptiveAssessment` (lazy) | Yes |
| `#/activity` | `MyActivity` (lazy) | Yes |
| `#/results` | `ResultsView` (lazy) | Yes |

**State managed:**
- `isLoggedIn` — based on localStorage `userName`
- `authView` — current auth page (landing/login/signup)
- `view` — current app page
- `recommendationData` — latest assessment results
- `selectedQuestionCount` — 30/50/60
- `profileData` — user's academic info
- `history` — activity log

**Lazy loading:** Settings, AdaptiveAssessment, MyActivity, ResultsView are loaded on-demand using `React.lazy()` for better initial page load time.

## 10.3 `LandingPage.js` — Public Homepage

**Sections:**
1. **Nav Bar** — Logo, Features link, How It Works link, Sign In button, Get Started button
2. **Hero** — "Find Your Perfect Career Path" headline, CTA buttons
3. **Features** — 4 cards: Smart Course Matching, Adaptive Assessment, College Course Database, Personalized Results
4. **How It Works** — 3 steps: Create Profile → Take Assessment → Get Recommendations
5. **CTA** — "Ready to find the right course?"
6. **Footer** — Logo, copyright

**Design:** Animated gradient background orbs, glass-morphism cards, smooth scroll

## 10.4 `Login.js` — Login Page

**Features:**
- Username OR email login
- Password with visibility toggle
- Google OAuth login (via `@react-oauth/google`)
- Username selection modal for new Google users
- Loading states, error messages
- Link to signup page

## 10.5 `Signup.js` — Registration Page

**Validation:**
- Username: 3+ chars, alphanumeric + underscores
- Full Name: 2+ chars, letters/spaces/hyphens/apostrophes, bad word filter (English + Filipino)
- Email: regex validation with `@domain.tld` format
- Password: 6+ chars, must match confirm
- Real-time email validation on blur
- Auto-capitalization of full name

## 10.6 `Dashboard.js` — Main Hub

**Layout (Bento Grid):**
- Main Assessment Card (large) — shows 30/50/60 question options, Start button
- Profile Card — link to edit profile, shows completion status
- Activity Card — shows assessment count badge
- Recent Activity Card — last 3 activities

**Behavior:**
- Checks if profile is complete (GWA + strand filled)
- Blocks assessment if profile incomplete
- Shows user menu dropdown (Profile, Settings, Help, Logout)
- Periodic activity ping every 5 minutes

## 10.7 `AdaptiveAssessment.js` — Assessment Page

**Three phases:**

1. **Start Screen** — Features overview, "Begin Assessment" button
2. **Question Loop:**
   - One question at a time
   - 8-10 options per question
   - Real-time stats: round/max, confidence %, traits found, courses remaining
   - Top courses preview (updates after each answer)
   - "Previous" button (go back)
   - "Finish Early" button (when allowed)
3. **Results Screen** — Shows top 6 courses with match %, tier badges, reasoning

**API calls:** `/adaptive/start`, `/adaptive/answer`, `/adaptive/previous`, `/adaptive/finish`

## 10.8 `ResultsView.js` — Recommendation Display

**Per course shows:**
- Rank (#1, #2, etc.)
- Course name
- Match percentage (visual bar + number)
- Description
- Matched traits (up to 3)
- GWA requirement
- Recommended strand
- Reasoning text (why recommended)
- Feedback button (1-5 star rating)

**Export options:**
- PDF download → `/export/pdf`
- Email export → `/export/email`

## 10.9 `ProfileForm.js` — Profile Edit Form

**Fields:** Full name, GWA (75-100), strand (dropdown), age, gender, interests (36 checkboxes), skills (32 checkboxes)

## 10.10 `ProfileView.js` — Profile Display

**Sections:** Avatar/name header, stats grid (assessments/GWA/interests/skills counts), about info, academic info, interests list, skills list

## 10.11 `MyActivity.js` — Assessment History

**Features:**
- List of past assessment attempts (cards)
- Expandable details: Summary, Courses, Traits, Stats tabs
- "Unseen" indicator for new activities
- Fetches from `/user/{userId}/assessment-history`

## 10.12 `Settings.js` — Account Settings

**Tabs:**
- Profile settings: name, GWA, strand, age, gender, photo, interests, skills
- Security settings: change email, change password

## 10.13 `FeedbackForm.js` — Star Rating Modal

- 5-star interactive rating
- Optional comment (500 chars max)
- Supports per-course or overall feedback
- Posts to `/feedback/submit`

## 10.14 `Toast.js` — Notification Component

- Auto-dismiss toast notifications
- Types: success (green), error (red), warning (orange), info (blue)

## 10.15 `NavBar.js` — Navigation Bar

- Brand: Logo + "CoursePro"
- Links: Home, Profile, Activity
- Right side: user menu / settings
- Sticky, semi-transparent with blur

## 10.16 `useIsMobile.js` — Mobile Detection Hook

- Returns `true` if window width ≤ 768px
- Used for responsive layout decisions

---

# 11. COMPLETE API ENDPOINT REFERENCE

## Authentication

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| POST | `/signup` | No | Register new user |
| POST | `/login` | No | Login with username/email + password |
| POST | `/google-login` | No | Login with Google OAuth |
| POST | `/google-register` | No | Complete Google registration with chosen username |
| POST | `/logout` | Yes | Mark user offline |
| GET | `/verify-session/{user_id}` | Yes | Check if session/account is still valid |

## User Profile

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| GET | `/user/{user_id}/academic-info` | Yes | Get user's profile data |
| PUT | `/user/{user_id}/academic-info` | Yes | Update profile (GWA, strand, interests, etc.) |
| PUT | `/user/{user_id}/change-password` | Yes | Change password (requires current password) |
| PUT | `/user/{user_id}/change-email` | Yes | Change email address |
| POST | `/user/{user_id}/update-activity` | Yes | Update online status |
| POST | `/refresh-user-activity/{user_id}` | Yes | Force refresh last_active timestamp |

## Adaptive Assessment

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| POST | `/adaptive/start` | Yes | Start session, get first question |
| POST | `/adaptive/answer` | Yes | Submit answer, get next question or results |
| POST | `/adaptive/previous` | Yes | Go back to previous question |
| POST | `/adaptive/finish` | Yes | End assessment early |
| GET | `/adaptive/status/{session_id}` | Yes | Get current session status |

## History & Recommendations

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| GET | `/user/{user_id}/recommendations` | Yes | Get saved recommendations |
| GET | `/user/{user_id}/assessment-history` | Yes | Get all past attempts with full details |

## Feedback

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| POST | `/feedback/submit` | Yes | Submit 1-5 star rating + optional comment |
| GET | `/feedback/recommendation/{id}` | Yes | Get feedback for specific recommendation |
| GET | `/user/{user_id}/feedback` | Yes | Get all feedback by user |

## Admin: Course Management

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| GET | `/admin/courses` | Admin | List all courses |
| GET | `/admin/courses/{id}` | Admin | Get course details |
| POST | `/admin/courses` | Admin | Create new course |
| PUT | `/admin/courses/{id}` | Admin | Update course |
| DELETE | `/admin/courses/{id}` | Admin | Delete course |

## Admin: Question Management

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| GET | `/admin/questions` | Admin | List all questions with options |
| GET | `/admin/questions/{id}` | Admin | Get question details |
| POST | `/admin/questions` | Admin | Create question with options |
| PUT | `/admin/questions/{id}` | Admin | Update question text/category |
| DELETE | `/admin/questions/{id}` | Admin | Delete question (cascades to options) |
| POST | `/admin/questions/{id}/options` | Admin | Add option to question |
| PUT | `/admin/options/{id}` | Admin | Update option |
| DELETE | `/admin/options/{id}` | Admin | Delete option |

## Admin: User Management

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| GET | `/admin/users` | Admin | List all users with status |
| GET | `/admin/users/{id}` | Admin | Get user details with history |
| PUT | `/admin/users/{id}/toggle-status` | Admin | Activate/deactivate user |
| DELETE | `/admin/users/{id}` | Admin | Delete user and all data |

## Admin: Reports

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| GET | `/admin/reports/overview` | Admin | System-wide statistics |
| GET | `/admin/reports/popular-courses` | Admin | Most recommended courses |
| GET | `/admin/reports/trait-distribution` | Admin | Trait frequency analysis |
| GET | `/admin/reports/user-activity` | Admin | Recent user activity |

## Admin: Feedback Management

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| GET | `/admin/feedback/stats` | Admin | Overall feedback statistics |
| GET | `/admin/feedback/courses/{id}` | Admin | Detailed feedback for a course |
| GET | `/admin/feedback/low-rated` | Admin | Recommendations rated below threshold |
| DELETE | `/admin/feedback/{id}` | Admin | Delete a feedback entry |

## Public

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| GET | `/` | No | Health check — returns `{status: "online"}` |
| GET | `/public/stats` | No | Public stats (courses, questions, assessments counts) |

---

# 12. ADMIN SYSTEM

## 12.1 How Admin Access Works

1. A user has `is_admin = 1` in the database
2. When they login, the JWT contains `is_admin: true`
3. Admin-only endpoints use the `require_admin` dependency:
   - Extracts JWT from request header
   - Validates user exists and is active
   - Checks `is_admin == 1`
   - Returns 403 "Admin access required" if not admin

## 12.2 Admin Capabilities

| Feature | What admin can do |
|---|---|
| **Course Management** | Create, edit, delete courses. Update trait tags, strand, GWA minimum |
| **Question Management** | Create, edit, delete questions and their options |
| **User Management** | View all users, see their profile/history, activate/deactivate accounts, delete users |
| **Reports** | View system overview stats, popular courses, trait distribution, user activity |
| **Feedback Management** | View feedback statistics, see feedback per course, find low-rated recommendations, delete feedback |

## 12.3 Account Deactivation

When an admin deactivates a user:
1. `is_active` is set to 0 in the database
2. On the user's next API call, `get_current_user()` checks `is_active`
3. If 0 → raises 403 "Account is deactivated"
4. User is effectively locked out until admin re-activates

---

# 13. FEEDBACK SYSTEM

## 13.1 How It Works

1. After receiving recommendations, user can rate each course
2. Star rating: 1 (Poor), 2 (Fair), 3 (Good), 4 (Very Good), 5 (Excellent)
3. Optional text comment (up to 500 characters)
4. Saved to `recommendation_feedback` table with timestamp

## 13.2 Feedback Types

- **Per-course feedback:** Linked to a specific `recommendation_id`
- **Overall feedback:** `recommendation_id` is null — general assessment satisfaction

## 13.3 Admin Analytics

Admins can view:
- Average rating across all feedback
- Rating distribution (how many 1s, 2s, 3s, etc.)
- Top courses by feedback count and average rating
- Low-rated recommendations (flagged for improvement)

---

# 14. SECURITY IMPLEMENTATION

## 14.1 Password Security

| Aspect | Implementation |
|---|---|
| Hashing | bcrypt (passlib library) — industry standard |
| Salt | Automatic (bcrypt generates unique salt per password) |
| Storage | Only the hash is stored (password_hash column) |
| Verification | `verify_password()` compares plaintext against hash without ever decrypting |

## 14.2 Authentication

| Aspect | Implementation |
|---|---|
| Method | JWT (JSON Web Tokens) via python-jose library |
| Algorithm | HS256 (HMAC-SHA256) |
| Secret | SECRET_KEY from environment variable |
| Expiry | 24 hours from creation |
| Storage | localStorage on frontend |
| Transmission | `Authorization: Bearer <token>` header on every request |

## 14.3 Authorization

| Level | Implementation |
|---|---|
| Authenticated | `get_current_user` dependency — validates JWT, checks user exists and is active |
| Admin Only | `require_admin` dependency — chains after get_current_user, checks is_admin |
| Self or Admin | `require_self_or_admin` — ensures user accesses only their own data unless admin |

## 14.4 Input Validation

| Validation | Where |
|---|---|
| Email format | Regex: `^[^\s@]+@[^\s@]+\.[^\s@]+$` (both frontend and backend) |
| Username | 3+ chars, alphanumeric + underscores (frontend) |
| Password | 6+ chars minimum (both frontend and backend) |
| Full name | Letters, spaces, hyphens, apostrophes only. Bad word filter (English + Filipino) |
| GWA | Range 75-100 (frontend validation) |
| Rating | 1-5 integer (backend validation) |

## 14.5 Bad Words Filter

The system filters inappropriate words in both English and Filipino:
- English: ~30 words including slurs and profanity
- Filipino: ~15 words including "puta", "gago", "tangina", "bobo", "tanga", etc.
- Applied to: fullname during signup and profile updates

## 14.6 CORS Policy

Only these origins are allowed:
- `https://coursepro.ildf.site` (production)
- `http://localhost:3000` (React dev)
- `http://localhost:5173` (Vite dev)

## 14.7 Database Safety

- Auto-migration on startup (adds missing columns without dropping data)
- Database seeding only when empty (preserves all existing data)
- Cascade deletes (deleting a user removes all their attempts, answers, recommendations, feedback)
- Connection pooling (10 connections, 20 overflow) to handle concurrent users
- `pool_pre_ping=True` to verify connections before use

---

# 15. TECHNOLOGIES & LIBRARIES

## 15.1 Backend

| Technology | Version | Purpose |
|---|---|---|
| **Python** | 3.x | Programming language |
| **FastAPI** | — | Web framework for building APIs |
| **Uvicorn** | — | ASGI server to run FastAPI |
| **SQLAlchemy** | — | ORM (Object-Relational Mapping) for database |
| **PostgreSQL** | — | Production relational database |
| **SQLite** | — | Development/fallback database |
| **python-jose** | — | JWT token creation and verification |
| **passlib + bcrypt** | — | Password hashing |
| **python-dotenv** | — | Environment variable management |
| **Pydantic** | — | Request/response validation (built into FastAPI) |

## 15.2 Frontend

| Technology | Version | Purpose |
|---|---|---|
| **React.js** | 18.x | Frontend UI framework |
| **Axios** | — | HTTP client for API communication |
| **@react-oauth/google** | — | Google OAuth 2.0 integration |
| **CSS3** | — | Styling (glass-morphism, animations, gradients) |
| **localStorage** | — | Client-side authentication state storage |

## 15.3 Deployment

| Service | Purpose |
|---|---|
| **Railway** | Backend hosting (FastAPI + PostgreSQL) |
| **Vercel / Custom Domain** | Frontend hosting (coursepro.ildf.site) |

---

# 16. THEORIES & REFERENCES FOR DEFENSE

| Theory | Author(s) | Year | How We Used It |
|---|---|---|---|
| **Rule-Based Expert Systems** | Giarratano & Riley | 2005 | Phase 1 of recommendation engine. 8 IF-THEN rules evaluate each course against the student's profile. Rules have priorities and evaluate conditions like trait matching, GWA, strand alignment. |
| **Decision Tree Algorithm (ID3/C4.5)** | Quinlan, J.R. | 1986 | Phase 2 of recommendation engine. Pre-built decision tree classifies students into career categories by traversing attribute nodes (trait_category → work_setting → gwa_level → leaf). Also, the adaptive assessment uses Information Gain (the same formula used in ID3) for question selection. |
| **Shannon Entropy / Information Gain** | Shannon, C.E. | 1948 | Adaptive question selection calculates entropy `H = -Σ p × log₂(p)` for each trait to determine which question would give the most new information. |
| **RIASEC Career Typology** | Holland, J.L. | 1997 | 6 base personality types (Realistic, Investigative, Artistic, Social, Enterprising, Conventional) form the foundation of our trait system. Extended with 22 specialized career traits. |
| **Hybrid Recommender Systems** | Burke, R. | 2002 | Our system combines two different algorithms (rule-based + decision tree) for better results than either alone. The final score is the sum of both phases. |

---

# 17. COMPLETE DECISION TREE DIAGRAM

```
                                    ┌──────────────┐
                                    │     ROOT     │
                                    │ trait_category│
                                    └───────┬──────┘
                    ┌───────────────────────┼───────────────────────┐───────────────────┐
                    ▼                       ▼                       ▼                   ▼
            ┌──────────────┐       ┌──────────────┐       ┌──────────────┐     ┌──────────────┐
            │   HELPING    │       │  PROBLEM-    │       │   CREATIVE   │     │   LEADING    │
            │ work_setting │       │  SOLVING     │       │ creative_type│     │domain_interest│
            └──────┬───────┘       │analytical_type│      └──────┬───────┘     └──────┬───────┘
        ┌──────┬───┴───┐           └──────┬───────┘     ┌───────┼───────┐    ┌───────┼───────┐
        ▼      ▼       ▼          ┌───────┼───────┐     ▼       ▼       ▼    ▼       ▼       ▼
    clinical  office   field   technical business research visual performing writing business public technical
    gwa_level social_   │      gwa_level leadership  │   tech_    │       │     │       │       │
       │     orient.    │         │      tendency    │   affinity │       │     │       │       │
    ┌──┼──┐ ┌──┼──┐    │      ┌──┼──┐  ┌──┼──┐     │  ┌──┼──┐   │       │     │       │       │
    H  M  L E  I  B    ▼      H  M  L  H  M  L     ▼  H  M  L   ▼       ▼     ▼       ▼       ▼
    │  │  │ │  │  │  com_svc  │  │  │  │  │  │  sci_res│  │  │ perf_art com_med bus_lead pub_adm eng_mgmt
    ▼  ▼  ▼ ▼  ▼  ▼          ▼  ▼  ▼  ▼  ▼  ▼       ▼  ▼  ▼
   +25+20+15+20+18+18        +25+20+15+22+18+20     +25+22+20
```

*H=High, M=Medium, L=Low, E=Extrovert, I=Introvert, B=Balanced*

---

# 18. COMPLETE RULE-BASED SYSTEM TABLE

| Rule ID | Name | Type | Priority | Condition (IF) | Action (THEN) | Points |
|---|---|---|---|---|---|---|
| **P1** | Primary Trait Alignment | Preference | 10 | User's #1 trait matches a course trait | Boost score | +20 (exact), +14-19 (similar ≥70%), +10 (≥50%) |
| **P3** | Career Path Preference | Preference | 10 | User selected career path mapping to this course | Boost score | +25 |
| **P2** | Trait Synergy Bonus | Preference | 9 | ≥3 meaningful trait matches (exact + similar×0.5) | Boost score | +15 |
| **P8** | Interests & Skills Bonus | Preference | 8 | User's profile keywords match course traits | Boost score | up to +25 (5 per keyword) |
| **P6** | Work Environment Match | Preference | 7 | User's work preference matches course setting | Boost score | +8 |
| **N3** | No Trait Match Penalty | Preference | 7 | Zero user traits match course traits | Penalize score | -15 |
| **P7** | Learning Style Match | Preference | 6 | User's learning style matches course approach | Boost score | +6 |
| **A1** | GWA Academic Bonus | Preference | 5 | GWA meets minimum → bonus; below → soft penalty | Adjust score | +10 bonus / -5 per point gap (max -15) |
| **A2** | Strand Alignment Bonus | Preference | 4 | Strand matches → bonus; compatible → partial | Adjust score | +8 match / +4 compatible / 0 mismatch |

**Rule Evaluation Order:** Sorted by priority (highest first). P1 and P3 (priority 10) are evaluated first, A2 (priority 4) is evaluated last.

---

# 19. TRAIT RELATIONSHIP MAP

## 19.1 Healthcare Traits

```
Patient-Care ──── 0.8 ──── Social
     │                        │
     ├── 0.9 ── People-Skill-─┤
     │                        │
     ├── 0.6 ── Rehab-Therapy │
     │              │         │
     ├── 0.4 ── Medical-Lab   │
     │              │         │
     └── 0.5 ── Community-Serve
                    │
Medical-Lab ── 0.8 ── Investigative
     │
     ├── 0.9 ── Analytical-Skill
     ├── 0.7 ── Lab-Research
     └── 0.5 ── Technical-Skill
```

## 19.2 Technology Traits

```
Software-Dev ── 0.8 ── Investigative
     │
     ├── 0.9 ── Technical-Skill
     ├── 0.6 ── Data-Analytics
     ├── 0.5 ── Cyber-Defense
     ├── 0.4 ── Hardware-Systems
     └── 0.3 ── Digital-Media

Hardware-Systems ── 0.8 ── Realistic
     │
     ├── 0.9 ── Technical-Skill
     ├── 0.6 ── Electrical-Power
     └── 0.5 ── Mechanical-Design
```

## 19.3 Engineering Traits

```
Civil-Build ── 0.9 ── Realistic
     │
     ├── 0.8 ── Technical-Skill
     ├── 0.5 ── Spatial-Design
     └── 0.4 ── Mechanical-Design

Mechanical-Design ── 0.9 ── Realistic
     │
     ├── 0.8 ── Technical-Skill
     ├── 0.5 ── Industrial-Ops
     └── 0.4 ── Civil-Build
```

## 19.4 Business Traits

```
Finance-Acct ── 0.9 ── Conventional
     │
     ├── 0.8 ── Analytical-Skill
     ├── 0.6 ── Admin-Skill
     └── 0.4 ── Startup-Venture

Marketing-Sales ── 0.9 ── Enterprising
     │
     ├── 0.8 ── People-Skill
     └── 0.6 ── Startup-Venture
```

---

# 20. SCORE CALCULATION WALKTHROUGH

## Example: STEM Student Interested in Programming

**Profile:**
- GWA: 92.5
- Strand: STEM
- Interests: programming, data, cybersecurity
- Skills: problem_solving, critical_thinking

**Assessment Answers (simplified):**
1. Chose option with `Software-Dev` trait (Round 1)
2. Chose option with `Data-Analytics` trait (Round 2)
3. Chose option with `Cyber-Defense` trait (Round 3)
4. Chose "Not interested" on a healthcare question → rejects `Patient-Care` (Round 4)
5. Chose option with `Analytical-Skill` trait (Round 5)

---

### Step-by-step for **BS Computer Science** (trait_tag: "Software-Dev, Data-Analytics, Technical-Skill"):

**Session Init:**
```
Base score: 50.0
GWA bonus (92.5 ≥ 85 minimum): +5 → 55.0
Strand bonus (STEM = STEM): +5 → 60.0
Profile bonus (programming→Software-Dev match, data→Data-Analytics match): +6 → 66.0
```

**Round 1 (Software-Dev chosen, ×2.5 multiplier):**
```
Direct match (Software-Dev in course traits): +12 × 2.5 = +30 → 96.0
```

**Round 2 (Data-Analytics chosen, ×2.5 multiplier):**
```
Direct match (Data-Analytics in course traits): +12 × 2.5 = +30 → 126.0
```

**Round 3 (Cyber-Defense chosen, ×2.5 multiplier):**
```
Similar match (Cyber-Defense → Software-Dev similarity 0.5, >40%): +3 × 2.5 = +7.5 → 133.5
```

**Round 4 (Patient-Care rejected):**
```
No impact on BS CS (doesn't have Patient-Care): +0 → 133.5
```

**Round 5 (Analytical-Skill chosen, ×1.5 multiplier):**
```
Similar match (Analytical-Skill → Data-Analytics similarity 0.8, >70%): +6 × 1.5 = +9 → 142.5
```

**After Adaptive Assessment: Course Score = 142.5**

---

### Phase 1: Rule-Based Filtering

```
Trait scores: {Software-Dev: 1.0, Data-Analytics: 1.0, Cyber-Defense: 1.0, Analytical-Skill: 1.0, ...mapped traits...}
Primary trait: Software-Dev (highest score)
Top 10 traits: [Software-Dev, Data-Analytics, Cyber-Defense, Analytical-Skill, Technical-Skill, Investigative, ...]

For BS Computer Science:
  Enhanced trait matching:
    Exact matches: Software-Dev, Data-Analytics, Technical-Skill = 3 exact
    Similar matches: Cyber-Defense (sim 0.5 with Software-Dev), Analytical-Skill (sim 0.9 with Data-Analytics)
    → trait_match_score ≈ 85 (high due to 3 exact + 2 similar)

  Rule evaluation:
    P1 (Primary Trait): Software-Dev in course → +20
    P3 (Career Path): if career_path_courses includes "BS Computer Science" → +25
    P2 (Synergy): 3 exact ≥ 3 → +15
    P8 (Interests): programming→Software, data→Analytical → +10
    P6 (Work Env): if office match → +8
    N3 (No Match): has matches → 0
    P7 (Learning): if theoretical match → +6
    A1 (GWA): 92.5 ≥ 85 → +10
    A2 (Strand): STEM = STEM → +8

  Synergy bonus: 3 exact matches → +5
  
  eligibility_score = 85 + 20 + 25 + 15 + 10 + 8 + 0 + 6 + 10 + 8 + 5 = 192
```

### Phase 2: Decision Tree

```
Traverse tree:
  ROOT → trait_category: primary trait "Software-Dev" → categorized as "problem_solving"
  problem_solving → analytical_type: has tech traits → "technical"
  technical → gwa_level: 92.5 → "high"
  LEAF: engineering_cs → score_modifier = +25

  BS Computer Science is in engineering_cs list → gets +25
```

### Final Score

```
Final = rule_score (192) + tree_boost (25) = 217

Match percentage: final_score > 130 → 90 + min(7, (217-130)/30 × 7) = 90 + 7 = 97%
Tier: 3 exact + no penalties + in predicted category → EXCELLENT
```

**Result:** BS Computer Science shows as #1 with 97% match, EXCELLENT tier

---

### What about **BS Nursing** (trait_tag: "Patient-Care, Medical-Lab, People-Skill")?

```
Session Init:
  Base: 50.0
  GWA bonus (92.5 ≥ 80): +5 → 55.0
  Strand: STEM ≠ required strand → no bonus → 55.0
  Profile: programming/data don't match Patient-Care → +0 → 55.0
  
Round 1-3: Software-Dev, Data-Analytics, Cyber-Defense → no match with Patient-Care → +0
Round 4: Patient-Care REJECTED → -8 → 47.0
Round 5: Analytical-Skill → weak similarity to Medical-Lab (0.6) → +1 × 1.5 = 1.5 → 48.5

Phase 1: 
  Exact matches: 0
  Similar: maybe Analytical-Skill → Medical-Lab
  trait_match_score ≈ 5
  N3: 0 matches → -15
  A2: STEM ≠ nursing strand → 0
  eligibility_score ≈ 5 + 0 - 15 + 10 = 0

Phase 2: engineering_cs → Patient-Care NOT in that category → tree_boost = 0

Final: 0 + 0 = 0 → percentage ≈ 25%
Tier: EXPLORATORY (or not shown at all since it wouldn't be in top 6)
```

---

# 21. POSSIBLE PANEL QUESTIONS & ANSWERS

## Algorithm Questions

**Q1: "How does the rule-based system work?"**
A: It uses 8 IF-THEN rules evaluated for each of the 99 courses. For example: IF the student's primary trait matches a course, THEN +20 points. IF GWA meets the minimum, THEN +10 points. IF no traits match at all, THEN -15 points. Rules have priority levels — trait matching (priority 10) is evaluated before academics (priority 4-5). The total boost minus penalties gives the Phase 1 eligibility score.

**Q2: "How does the decision tree work?"**
A: After Phase 1 gives each course a base score, the decision tree classifies the student into a career category. It starts at the root node asking "What is the primary trait category?" (helping, problem-solving, creative, or leading), then branches further based on work setting, GWA level, social orientation, etc. Each leaf node assigns a classification like "engineering_cs" or "healthcare_professional" with a modifier of +15 to +25. Courses in the predicted category get this bonus added to their Phase 1 score.

**Q3: "Why adaptive? Why not just give all questions at once?"**
A: Adaptive means each next question is selected based on Information Gain — the same formula used in ID3 decision trees. We calculate Shannon Entropy for each trait: traits that appear in roughly 50% of remaining courses give maximum information. The system picks the question whose options cover the most informative traits. This makes the assessment shorter (high confidence can be reached in 15-20 questions) and more accurate (no wasted questions about already-confirmed preferences).

**Q4: "What is Information Gain and how does it work here?"**
A: Information Gain measures how well a question discriminates between courses. We calculate it using Shannon Entropy: H = -p × log₂(p) - (1-p) × log₂(1-p), where p is the fraction of active courses that have a particular trait. If a trait appears in 50% of courses, entropy is maximum (1.0) — asking about it gives the most information. If it appears in all or no courses, entropy is 0 — it's useless to ask about. We also penalize traits we already know about, so we don't repeat questions on the same topic.

**Q5: "Can a STEM student get recommended a HUMSS course?"**
A: Yes. Strand and GWA are soft constraints — they only add bonus points but never disqualify. A STEM student whose assessment answers show strong Social, Teaching-Ed, and People-Skill traits will get education or social science courses recommended, because the trait match points (+20 primary, +15 synergy, etc.) far outweigh the strand mismatch (which is at most +8 bonus lost, never a penalty).

**Q6: "How is the match percentage calculated?"**
A: The raw final score (Phase 1 + Phase 2) is converted to a percentage using a piecewise curve. Scores ≤40 map to 25-45%, scores 40-70 map to 45-65%, and scores 130+ map to 90-97%. This is more realistic than a simple linear mapping because it ensures there's meaningful differentiation between good and great matches. The maximum possible is 97% (never 100% because no course is a perfect match for anyone).

**Q7: "What happens when a student says 'Not interested'?"**
A: The system identifies what topic was rejected (using keyword detection in the option text, question category mapping, or majority vote of other options' traits). Then: (1) the rejected topic is added to a set, (2) all courses with that trait are penalized -8 points, (3) future questions about that topic are skipped entirely (either by category match or if >30% of options relate to the rejected topic). This significantly reduces noise and speeds up convergence.

**Q8: "What if the student clicks 'Previous' — how do you reverse an answer?"**
A: Every answer records its exact changes: which traits were added, how many points, and any rejection data. When the student goes back, we reverse ALL changes — subtract the exact trait scores that were added, remove rejected topics, add back course penalties. Then we recalculate all course scores from scratch using the stored initial scores (which include profile bonuses). This ensures perfect reversal without accumulating errors.

## Technical Questions

**Q9: "What security measures does the system have?"**
A: Passwords are hashed with bcrypt (salted, one-way — we never store plaintext). Authentication uses JWT tokens (HS256 algorithm, 24-hour expiry) verified on every API call. Admin endpoints are protected with role-based access control. Deactivated accounts are blocked at every endpoint. CORS policy restricts API access to only our frontend domains. Input validation sanitizes names (bad word filter in English and Filipino), validates email format, enforces password length.

**Q10: "What database do you use and why?"**
A: PostgreSQL for production. It's a production-grade relational database that supports JSON columns (for flexible profile data storage), handles concurrent users with connection pooling, and is widely adopted in industry. We use SQLAlchemy ORM so we write Python classes instead of raw SQL — this prevents SQL injection and makes the code maintainable. SQLite is available as a development fallback.

**Q11: "How are courses stored? How do you match traits to courses?"**
A: Each course has a `trait_tag` column containing comma-separated trait names like "Software-Dev, Data-Analytics, Technical-Skill". When matching, we parse these into a set and compare against the student's trait_scores dictionary. We check for exact matches, then use the SPECIALIZED_TRAIT_RELATIONSHIPS dictionary for similarity scores (0.0-1.0) to give partial credit for related traits.

**Q12: "What is the trait system based on?"**
A: It's based on Holland's RIASEC model — 6 personality types (Realistic, Investigative, Artistic, Social, Enterprising, Conventional). We extended it with 22 specialized career path traits unique to each field: 4 for healthcare (Patient-Care, Medical-Lab, Rehab-Therapy, Health-Admin), 4 for technology (Software-Dev, Hardware-Systems, Data-Analytics, Cyber-Defense), 4 for engineering, 3 for business, and so on. Plus 6 skill traits (Technical-Skill, People-Skill, etc.). Total: 28 specialized + 6 RIASEC = 34 traits.

**Q13: "How many courses, questions, and traits?"**
A: 99 college courses (from various fields: IT, engineering, healthcare, business, education, arts, science, maritime, agriculture, hospitality, etc.), 193 assessment questions (each with 8-10 options), and 34 personality traits (6 RIASEC + 22 specialized career + 6 skill traits).

**Q14: "What is the early boost multiplier?"**
A: The first 3 answers get a ×2.5 score multiplier, answers 4-7 get ×1.5, and the rest get ×1.0. This ensures the student's initial strong preferences can override the profile-based starting scores. Without this, the initial GWA/strand/interests bonuses (max +15 per course) would dominate too long, making early answers feel meaningless.

## System Design Questions

**Q15: "How does Google Login work?"**
A: We use OAuth 2.0 via the @react-oauth/google library. When the user clicks "Continue with Google," Google handles authentication and returns a credential JWT. The frontend decodes this to get the email and name, then sends them to our /google-login endpoint. If the email exists in our database, the user is logged in immediately. If not, the frontend shows a modal asking them to choose a username, then calls /google-register to create their account.

**Q16: "Why did you choose FastAPI over Django or Flask?"**
A: FastAPI offers automatic validation with Pydantic models, built-in OpenAPI documentation, native async support, and dependency injection (which we use extensively for authentication). It's also faster than Flask and lighter than Django for our API-focused backend.

**Q17: "Why React instead of Vue or Angular?"**
A: React has the largest ecosystem, extensive community support, and component-based architecture that suited our multi-page application. We also used React.lazy() for code splitting to improve performance.

**Q18: "How do you handle concurrent users?"**
A: PostgreSQL connection pooling (10 connections, 20 overflow), FastAPI's async architecture, and stateless JWT authentication. Each user's assessment session is stored in-memory on the server in a dictionary (not in the database) for speed, and only saved to the database when the assessment is complete.

**Q19: "What happens if the server restarts during an assessment?"**
A: The adaptive session is stored in-memory, so it would be lost. The user would need to start a new assessment. Past completed assessments are permanently stored in the database and are not affected.

**Q20: "How do you deploy the system?"**
A: Backend on Railway (FastAPI + PostgreSQL), frontend on a custom domain (coursepro.ildf.site). Railway provides automatic SSL and PostgreSQL hosting. Environment variables (SECRET_KEY, DATABASE_URL) are configured in Railway's dashboard.

## Data & Validation Questions

**Q21: "How do you ensure data quality for the assessment?"**
A: Each question has 8-10 carefully crafted options with specific trait tags. Questions are categorized (Technology, Healthcare, etc.) for diversity. The adaptive engine ensures category diversity by penalizing questions from already-asked categories. Rejection detection prevents irrelevant questions from being asked.

**Q22: "What validation exists for user input?"**
A: Frontend: email regex, username format, password length, GWA range (75-100), name format with bad word filter, auto-capitalization. Backend: email format recheck, duplicate username/email check, password verification for changes, rating range (1-5) for feedback, name format with bad word filter.

**Q23: "How do you prevent duplicate assessments?"**
A: Each assessment creates a new `test_attempts` record with a unique `attempt_id`. Duplicate answer detection prevents double-counting if a user clicks too fast. The session tracks `excluded_question_ids` to never show the same question twice.

**Q24: "What is the confidence score?"**
A: Confidence measures how far ahead the top 5 courses are compared to courses ranked 6-15. Formula: confidence = (gap_ratio × 0.7) + (question_factor × 0.3). Gap ratio is (top5_avg - rest_avg) / top5_avg. Question factor is min(round_number / min_questions, 1.0). When confidence reaches 75% AND minimum questions are answered, the assessment can stop early.

## Theoretical Questions

**Q25: "What is the difference between your system and a collaborative filtering recommender?"**
A: Collaborative filtering recommends based on "users who liked X also liked Y" — it needs historical data from many users. Our system uses a content-based approach combined with knowledge-based rules. We match individual student traits against course attributes using expert rules and a decision tree. This works even with zero historical data (a new user gets recommendations immediately).

**Q26: "Why use a hybrid approach instead of just one algorithm?"**
A: Based on Burke (2002), hybrid systems outperform single-algorithm systems. Our rule-based phase handles explicit constraints (GWA, strand, stated interests) well, while the decision tree captures implicit patterns (a student who is analytical + technical + high GWA likely fits engineering). Combining them gives a more complete picture than either alone.

**Q27: "How is your decision tree different from a machine learning decision tree?"**
A: A traditional ML decision tree (like sklearn's DecisionTreeClassifier) is trained on labeled data. Our decision tree is expert-designed (knowledge-based) — we manually built the tree structure based on educational expertise about which traits map to which career paths. This approach doesn't need training data and is transparent (you can trace exactly why a classification was made).

**Q28: "How does the Information Gain in your assessment relate to ID3?"**
A: In ID3, Information Gain selects the best attribute to split a dataset at each node. In our assessment, we use the same formula to select the best question to ask. Each question is like a potential split attribute, and each trait is like a feature value. We calculate which trait would split the remaining courses most evenly (maximum entropy), then pick the question that covers that trait. It's the same mathematical concept applied dynamically.

## Edge Case Questions

**Q29: "What if a student answers all questions the same way?"**
A: If all answers have the same trait tag, that trait will dominate and courses matching it will score very high. The system still generates top 6 recommendations — they'll all be from the same field, which is correct behavior (a student consistently choosing healthcare options should get healthcare courses).

**Q30: "What if a student has no profile (no GWA/strand)?"**
A: The assessment still works. GWA and strand rules are skipped ("check skipped, no requirement or user data"). Recommendations are based purely on assessment answers. However, the Dashboard blocks starting an assessment until profile is complete (GWA + strand required).

**Q31: "What if there are fewer than 6 qualifying courses?"**
A: The system always has 99 courses in consideration (none are ever disqualified — soft constraints only). The diversity selector picks top 6 from the ranked list. In practice, there are always at least 6 courses with positive scores.

**Q32: "What if a student rejects many topics?"**
A: Each rejection penalizes related courses (-8) and excludes future questions on that topic. If many topics are rejected, the remaining courses with positive scores become the recommendations. The system naturally converges on whatever fields the student didn't reject.

---

# APPENDIX: CHAPTER IV FINAL DRAFT

### Chapter IV

### RESULTS AND DISCUSSIONS

The results and description are presented in accordance with the study's objectives and the respondents' responses to the suggested system.

---

**Presentation of Objective 1**

**1.1 Develop a College Course Recommendation System**

**1.1.1** Develop a web-based College Course Recommendation System that guides SHS students toward suitable college courses based on their individual profiles.

*(Insert screenshot of the Landing Page)*

**1.1.2** Users are required to register or log in before accessing the system to ensure personalized recommendations.

*(Insert screenshot of the Sign Up page)*

**1.1.3** Google Authentication login for users.

*(Insert screenshot of the Login page)*

**1.1.4** User registration through the sign-up form with username, email, and password.

*(Insert screenshot of the Sign Up page)*

---

**1.2 Obtain a Validated Dataset of SHS Student Profiles**

**1.2.1** Collect student information through a structured profile form that captures academic performance (GWA), SHS strand, personal interests, and skills.

*(Insert screenshot of the Profile Form)*

**1.2.2** Administer a structured questionnaire through an adaptive assessment that captures personality traits, situational responses, and preferred learning styles.

*(Insert screenshot of the Assessment screen)*

---

**1.3 Generate Course Recommendations**

**1.3.1** The system generates course recommendations through a two-phase process: Rule-Based Filtering to shortlist eligible courses, followed by Decision Tree Analysis to rank and prioritize the most suitable options. Each recommended course displays a match percentage and is assigned a priority tier — Excellent, Good, Fair, or Exploratory.

*(Insert screenshot of the Recommendation Results page showing courses with match percentages and tier labels)*

---

**1.4 Improve User Experience**

**1.4.1** Implementation of a dashboard and navigation for easy access to all features of the system.

*(Insert screenshot of the Dashboard)*

**1.4.2** Assessment history feature where users can view their past assessment attempts and recommendation results.

*(Insert screenshot of the My Activity page)*

**1.4.3** Account settings where users can update their profile information, password, and email.

*(Insert screenshot of the Settings page)*

---

**1.5 Develop an Admin System**

**1.5.1** Develop an admin interface to manage courses, questions, and user accounts.

*(Insert screenshot of the Admin Dashboard)*

---

**Presentation of Objective 2**

**To demonstrate the system's effectiveness, by measuring recommendation accuracy and user usability through testing with SHS students.**

*(Insert your survey results table here)*

---

**Presentation of Objective 3**

**To test the functionality of the system using User Acceptance Testing.**

**Table (?) Summary of User Acceptance Test**

| TEST CASE ID | DESCRIPTION | REMARKS |
|---|---|---|
| UAT-001 | User Registration | PASSED |
| UAT-002 | Google Login Functionality | PASSED |
| UAT-003 | Invalid/Canceled Login Handling | PASSED |
| UAT-004 | Logout Function | PASSED |
| UAT-005 | Navigation Menu and UI Flow | PASSED |
| UAT-006 | Profile Form Submission | PASSED |
| UAT-007a | Assessment – Question Display | PASSED |
| UAT-007b | Assessment – Answer Submission | PASSED |
| UAT-007c | Assessment – Previous Question | PASSED |
| UAT-008 | Course Recommendation Generation | PASSED |
| UAT-009 | Match Score and Tier Display | PASSED |
| UAT-010 | Assessment History Viewing | PASSED |
| UAT-011 | Feedback Submission | PASSED |
| UAT-012 | Account Settings Update | PASSED |
| UAT-013 | Admin – Course Management | PASSED |
| UAT-014 | Admin – Question Management | PASSED |
| UAT-015 | Admin – User Management | PASSED |
