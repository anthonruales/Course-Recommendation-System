# DFD Implementation Mapping Document

## System Overview
This document maps the Data Flow Diagram (DFD) to the actual implementation in the Course Recommendation System. It demonstrates how each process, data store, and external entity in the DFD is realized in the code.

---

## EXTERNAL ENTITIES

### 1. Student
**DFD Role:** Primary user providing input and receiving recommendations
**Implementation:**
- **Frontend:** `Login.js`, `Signup.js`, `Dashboard.js`, `ProfileForm.js`, `AssessmentForm.js`
- **Backend:** `models.User` - User authentication and profile storage
- **Key Endpoints:**
  - `POST /signup` - Student creates account
  - `POST /login` - Student authenticates
  - `PUT /user/{user_id}/academic-info` - Student updates academic profile

### 2. Admin
**DFD Role:** Manages system parameters, courses, and questions
**Implementation:**
- **Frontend:** `admin/Admin.js`, `admin/ManageCourse.js`, `admin/ManageQuestion.js`
- **Backend:** Admin endpoints for CRUD operations on courses and questions
- **Key Endpoints:**
  - `POST /admin/courses` - Create course
  - `PUT /admin/courses/{course_id}` - Update course
  - `DELETE /admin/courses/{course_id}` - Delete course
  - `POST /admin/questions` - Create question
  - `PUT /admin/questions/{question_id}` - Update question
  - `DELETE /admin/questions/{question_id}` - Delete question

---

## DATA STORES

### D1: User Database
**DFD Role:** Stores user account and authentication data
**Implementation:**
- **Model:** `models.User`
- **Columns:**
  - `user_id` (PK) - Primary key
  - `fullname` - User's full name
  - `email` (UNIQUE) - Email for login
  - `password_hash` - Encrypted password
  - `academic_info` (JSON) - Stores GWA and strand
  - `created_at` - Account creation timestamp
- **Seeding:** `seed_database()` in main.py
- **Table Name:** `users`

### D2: Course Database
**DFD Role:** Stores course information and requirements
**Implementation:**
- **Model:** `models.Course`
- **Columns:**
  - `course_id` (PK) - Primary key
  - `course_name` - Name of course (e.g., "BS Computer Science")
  - `description` - Course description
  - `minimum_gwa` - GWA requirement (80-100 scale)
  - `recommended_strand` - Recommended SHS strand
  - `trait_tag` - Comma-separated trait tags (e.g., "Analytical, Technical, Logical")
- **Data Source:** `COURSES_POOL` in seed_data.py (111 courses)
- **Table Name:** `courses`

### D3: Question Database
**DFD Role:** Stores assessment questions and options
**Implementation:**
- **Models:** 
  - `models.Question` - Question text and category
  - `models.Option` - Answer options with trait tags
- **Columns (Question):**
  - `question_id` (PK)
  - `question_text` - The question prompt
  - `category` - "Situational", "Assessment", or "Academic"
  - `options` - Relationship to Option records
- **Columns (Option):**
  - `option_id` (PK)
  - `question_id` (FK) - Reference to Question
  - `option_text` - The answer option text
  - `trait_tag` - Associated personality trait (e.g., "Leadership", "Analytical")
- **Data Source:** 
  - `SITUATIONAL_QUESTIONS_POOL` (30 questions)
  - `ASSESSMENT_QUESTIONS_POOL` (30 questions)
  - `ACADEMIC_QUESTIONS_POOL` (30 questions)
- **Total:** 90 questions, 360 options
- **Table Names:** `questions`, `options`

### D4: Personal & Academic Database
**DFD Role:** Stores student's personal info and academic profile
**Implementation:**
- **Model:** `models.User.academic_info` (JSON field)
- **Structure:**
  ```json
  {
    "gwa": 88.5,
    "strand": "STEM"
  }
  ```
- **Related Storage:**
  - `models.StudentAnswer` - Records each assessment response
  - `models.Recommendation` - Stores recommendation results
- **Table Names:** `users` (academic_info column), `student_answers`, `recommendations`

---

## PROCESSES

### P0: Feedback (System Loop)
**DFD Role:** Overall system feedback mechanism
**Implementation:** Continuous cycle through Dashboard where users can:
1. View recommendations → P2
2. Update profile → P1
3. Retake assessment → P5

### P1: User Authentication
**DFD Role:** Verify user credentials
**Implementation:**
- **Endpoint:** `POST /login`
- **Function:** `login()` in main.py
- **Logic:**
  1. Query User table by email
  2. Verify password hash using `verify_password()`
  3. Return user_id and fullname
- **Security:** bcrypt password hashing via `security.py`

### P2: Input Personal & Academic Data
**DFD Role:** Capture student profile information
**Implementation:**
- **Endpoint:** `PUT /user/{user_id}/academic-info`
- **Function:** `update_academic_info()` in main.py
- **Frontend:** `ProfileForm.js`
- **Captures:**
  - Full name, age, gender
  - SHS strand (STEM, ABM, HUMSS, GAS, TVL)
  - GWA (80-100 scale)
  - Academic interests
  - Technical skills
- **Storage:** User.academic_info JSON field

### P3: Input Personal & Academic Data (Alternative)
**DFD Role:** Manual profile data entry (admin override)
**Implementation:** Same as P2, used when students create account
- **Frontend:** `ProfileForm.js` during signup
- **Validation:** Validates strand and GWA range

### P4: Fetch Personal & Academic Data
**DFD Role:** Retrieve student profile for recommendation
**Implementation:**
- **Endpoint:** `GET /user/{user_id}` (implicit in /recommend)
- **Function:** `recommend()` in main.py (lines 168-365)
- **Logic:**
  ```python
  user = db.query(models.User).filter(models.User.user_id == data.userId).first()
  user_gwa = user.academic_info.get("gwa")
  user_strand = user.academic_info.get("strand")
  ```
- **Used For:** Filtering courses and generating recommendations

### P5: Fetch Q&A
**DFD Role:** Retrieve questions for assessment
**Implementation:**
- **Endpoint:** `GET /questions?user_id={user_id}`
- **Function:** `fetch_questions()` or `@app.get("/questions")` in main.py
- **Logic:**
  1. Fetch user's academic profile (P4)
  2. Find suitable courses for user's strand/GWA
  3. Extract trait tags from suitable courses
  4. Fetch 10 random questions per category (Situational, Assessment, Academic)
  5. Prioritize questions with traits matching suitable courses
- **Returns:** 30 questions total (10 per category)

### P6: Take a Test
**DFD Role:** Student completes assessment
**Implementation:**
- **Frontend:** `AssessmentForm.js`
- **Endpoint:** Submits answers via `POST /recommend`
- **Process:**
  1. Display 30 questions (from P5)
  2. Student selects one option per question
  3. Record each selection with trait tag
  4. Submit all answers as `AssessmentSubmit` object

### P7: Record Test Attempt (Test Attempt Database)
**DFD Role:** Store assessment responses
**Implementation:**
- **Model:** `models.StudentAnswer`
- **Columns:**
  - `answer_id` (PK)
  - `user_id` (FK)
  - `question_id` (FK)
  - `chosen_option_id` (FK)
  - `taken_at` - Timestamp of submission
- **Storage:** All answers saved in `/recommend` endpoint (lines 338-342)
  ```python
  for ans in data.answers:
    db.add(models.StudentAnswer(
      user_id=data.userId,
      question_id=ans.questionId,
      chosen_option_id=ans.chosenOptionId
    ))
  ```

### P8: Rule-Based Logic & Decision Tree
**DFD Role:** Generate ranked course recommendations
**Implementation:**
- **Endpoint:** `POST /recommend`
- **Function:** `recommend()` in main.py (lines 162-365)
- **Algorithm:**
  
  **Step 1: Count Trait Scores**
  ```python
  trait_scores = {}
  for ans in data.answers:
    option = db.query(models.Option).filter(...)
    if option.trait_tag:
      trait_scores[tag] += 1
  ```
  
  **Step 2: Filter & Score Courses**
  ```python
  for course in all_courses:
    score = 0
    
    # Match traits (top 3 user traits)
    for trait, count in top_3_traits:
      if trait in course.trait_tag:
        score += count * 3  # Weight by frequency
    
    # GWA match
    if user_gwa >= course.minimum_gwa:
      score += 2  # Bonus
    else:
      score -= 5  # Penalty
    
    # Strand match
    if user_strand in course.recommended_strand:
      score += 2  # Bonus
    else:
      score -= 3  # Penalty
  ```
  
  **Step 3: Rank & Select**
  ```python
  scored_courses.sort(key=lambda x: x["score"], reverse=True)
  top_recommendations = scored_courses[:5]
  ```

- **Decision Factors:**
  1. **Trait Alignment** - How well student's interests match course traits
  2. **GWA Compatibility** - Student's GWA vs. course minimum requirement
  3. **Strand Alignment** - Student's strand vs. recommended strand
  4. **Weighting:** Traits (highest impact) > GWA (medium) > Strand (lower impact with penalty)

### P9: Filtered Courses
**DFD Role:** Return final recommendations with reasoning
**Implementation:**
- **Endpoint:** Response from `POST /recommend`
- **Response Structure:**
  ```json
  {
    "user_id": 1,
    "user_gwa": 88.5,
    "user_strand": "STEM",
    "detected_traits": [["Analytical", 5], ["Technical", 4], ["Logical", 3]],
    "recommendations": [
      {
        "course_name": "BS Computer Science",
        "description": "...",
        "matched_traits": ["Analytical", "Technical", "Logical"],
        "minimum_gwa": 88,
        "recommended_strand": "STEM",
        "compatibility_score": 15,
        "reasoning": "Full explanation...",
        "reasoning_details": {
          "trait_alignment": "Matches your personality traits: Analytical, Technical, Logical",
          "strand_influence": "✓ Your strand (STEM) perfectly aligns...",
          "gwa_assessment": "✓ Your GWA (88.5) exceeds the minimum requirement (88)...",
          "academic_interest": "Your assessment revealed interests in: Analytical, Technical, Logical",
          "summary": "Combined explanation"
        }
      }
    ]
  }
  ```

---

## DATA FLOWS

### Flow 1: Signup/Login → Dashboard
```
External: Student
  ↓ Provides credentials
P1: User Authentication
  ↓ Validates against D1
D1: User Database
  ↓ Returns user_id
P2: Input Personal & Academic Data
  ↓ Stores profile
D4: Personal & Academic Database
  ↓ Redirects to Dashboard
External: Student
```

### Flow 2: Assessment & Recommendation
```
External: Student (Dashboard)
  ↓ Requests assessment
P5: Fetch Q&A
  ↓ Queries D4 for profile
D4: Personal & Academic Database
  ↓ Filters by strand/GWA
D2: Course Database
  ↓ Extracts trait tags
D3: Question Database
  ↓ Selects 30 relevant questions
External: Student (Takes Assessment)
  ↓ Submits 30 answers
P6: Take a Test
  ↓ Records responses
P7: Record Test Attempt (D3)
  ↓ Stores in Student Answers
D4: Test Attempt Database
  ↓ Sends answers to recommendation
P8: Rule-Based Logic & Decision Tree
  ↓ Counts traits, filters courses
D2: Course Database
  ↓ Scores based on rules
P9: Filtered Courses
  ↓ Returns top 5 with reasoning
External: Student (Results View)
```

### Flow 3: Admin Management
```
External: Admin (Admin Interface)
  ↓ Creates/updates course
P1 (Admin): Manage Courses
  ↓ Writes to
D2: Course Database
  ↓ Affects future recommendations
P8: Rule-Based Logic & Decision Tree
  ↓ Uses updated courses
External: Student (Sees new options)
```

---

## IMPLEMENTATION COMPLETENESS CHECKLIST

| DFD Element | Implementation | Status | Code Location |
|---|---|---|---|
| **External Entities** | | | |
| Student | ✅ Frontend + Backend | Complete | Login.js, Signup.js, Dashboard.js |
| Admin | ✅ Frontend + Backend | Complete | admin/Admin.js, main.py |
| **Data Stores** | | | |
| D1: User Database | ✅ Implemented | Complete | models.User, SQLAlchemy |
| D2: Course Database | ✅ Implemented | Complete | models.Course, 111 courses seeded |
| D3: Question Database | ✅ Implemented | Complete | models.Question, models.Option, 90 questions |
| D4: Personal & Academic DB | ✅ Implemented | Complete | User.academic_info, StudentAnswer, Recommendation |
| **Processes** | | | |
| P0: Feedback Loop | ✅ Implemented | Complete | Dashboard navigation |
| P1: User Authentication | ✅ Implemented | Complete | /login endpoint, security.py |
| P2: Input Academic Data | ✅ Implemented | Complete | /user/{id}/academic-info, ProfileForm.js |
| P3: Store Academic Data | ✅ Implemented | Complete | User.academic_info JSON field |
| P4: Fetch Academic Data | ✅ Implemented | Complete | recommend() function, lines 168-180 |
| P5: Fetch Q&A | ✅ Implemented | Complete | /questions endpoint, trait-based selection |
| P6: Take a Test | ✅ Implemented | Complete | AssessmentForm.js, POST /recommend |
| P7: Record Test Attempt | ✅ Implemented | Complete | StudentAnswer model, lines 338-342 |
| P8: Rule-Based Logic | ✅ Implemented | Complete | recommend() function, lines 189-265 |
| P9: Filtered Courses | ✅ Implemented | Complete | recommend() response, lines 280-340 |
| **Data Flows** | | | |
| Signup → Login → Dashboard | ✅ Implemented | Complete | Full authentication flow |
| Assessment Flow | ✅ Implemented | Complete | /questions → /recommend → ResultsView |
| Admin Management Flow | ✅ Implemented | Complete | Admin CRUD endpoints |

---

## KEY ALGORITHM FLOWS

### Trait Scoring Algorithm
```
Input: Student answers (30 options selected)
Process:
  1. For each selected option:
     - Extract trait_tag from Option table
     - Increment count for that trait
  2. Sort traits by frequency (descending)
  3. Keep top 3 traits
Output: Top 3 traits with scores [("Analytical", 5), ("Technical", 4), ("Logical", 3)]
```

### Course Recommendation Algorithm
```
Input: 
  - trait_scores: {trait → count}
  - user_gwa: float (80-100)
  - user_strand: string
Process:
  For each course in database:
    score = 0
    
    # Factor 1: Trait Matching (Highest Weight)
    For each (trait, count) in top_3_traits:
      If trait in course.trait_tags:
        score += count * 3
    
    # Factor 2: GWA Compatibility (Medium Weight)
    If user_gwa >= course.minimum_gwa:
      score += 2
    Else:
      score -= 5
    
    # Factor 3: Strand Alignment (Lower Weight)
    If user_strand in course.recommended_strand:
      score += 2
    Else:
      score -= 3
    
    # Store: {course, score, matched_traits, gwa_match, strand_match}
  
  Sort courses by score (descending)
  Select top 5 courses
Output: Top 5 recommended courses with detailed reasoning
```

### Question Selection Algorithm
```
Input: 
  - user_id
  - user_gwa, user_strand
Process:
  1. Find suitable courses:
     courses = query where 
       minimum_gwa <= user_gwa AND 
       recommended_strand contains user_strand
  
  2. Extract relevant traits:
     traits = union of all trait_tags from suitable courses
  
  3. For each question category (Situational, Assessment, Academic):
     - Get all questions in category
     - Prioritize: questions with options matching traits
     - Select 10 random questions (biased toward matching traits)
  
  4. Return 30 questions (10 per category)
Output: Personalized question set relevant to student's academic path
```

---

## MISSING OR FUTURE ENHANCEMENTS

| Item | Status | Recommendation |
|---|---|---|
| Real-time progress tracking | ❌ Not implemented | Could add progress bars in assessment |
| Multiple assessment attempts comparison | ⚠️ Partial | Store but don't compare trends |
| Detailed career path guidance | ❌ Not implemented | Could add course prerequisites/sequences |
| Admin analytics dashboard | ❌ Not implemented | Could show user statistics, popular courses |
| Email notifications | ❌ Not implemented | Could send recommendations via email |
| Mobile app | ❌ Not implemented | React Native version possible |
| Machine learning refinement | ❌ Not implemented | Could improve scoring weights over time |

---

## CONCLUSION

The implemented system **successfully realizes all major DFD processes and data stores**. Every data flow in the DFD is mapped to actual code endpoints and functions. The system is production-ready for:

✅ Student registration and authentication
✅ Academic profile management
✅ Personalized assessment delivery
✅ Rule-based course recommendations with detailed reasoning
✅ Admin course and question management
✅ Complete audit trail of student responses

**Capstone Readiness:** All core DFD functionality is implemented and testable.
