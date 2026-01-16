# Course Recommendation System - API Documentation

## Base URL
`http://localhost:8000`

---

## 🔐 Authentication Endpoints

### 1. User Signup
**POST** `/signup`

Create a new user account.

**Request Body:**
```json
{
  "fullname": "John Doe",
  "email": "john@example.com",
  "password": "password123"
}
```

**Response:**
```json
{
  "message": "Success"
}
```

---

### 2. User Login
**POST** `/login`

Authenticate user and get user details.

**Request Body:**
```json
{
  "email": "john@example.com",
  "password": "password123"
}
```

**Response:**
```json
{
  "user": "John Doe",
  "user_id": 1
}
```

---

## 👤 User Endpoints

### 3. Update Academic Info
**PUT** `/user/{user_id}/academic-info`

Update user's GWA and strand for better recommendations.

**Request Body:**
```json
{
  "gwa": 1.75,
  "strand": "STEM"
}
```

**Response:**
```json
{
  "message": "Academic info updated successfully",
  "user_id": 1,
  "academic_info": {
    "gwa": 1.75,
    "strand": "STEM"
  }
}
```

---

### 4. Get User Recommendations
**GET** `/user/{user_id}/recommendations`

Retrieve user's saved course recommendations.

**Response:**
```json
{
  "user_id": 1,
  "recommendations": [
    {
      "course_name": "Bachelor of Science in Computer Science",
      "description": "Study of algorithms, programming, and computing systems",
      "top_trait": "Analytical",
      "reasoning": "This course aligns with your interests in Analytical, Logical...",
      "minimum_gwa": 2.0,
      "recommended_strand": "STEM"
    }
  ]
}
```

---

### 5. Get Assessment History
**GET** `/user/{user_id}/assessment-history`

View user's assessment history and statistics.

**Response:**
```json
{
  "user_id": 1,
  "total_answers": 20,
  "assessments_taken": 1,
  "last_assessment": "2026-01-16T10:30:00"
}
```

---

## 📝 Assessment Endpoints

### 6. Get Questions
**GET** `/questions`

Retrieve 20 random questions with options for assessment.

**Response:**
```json
[
  {
    "question_id": 1,
    "question_text": "When planning a group project, I prefer to:",
    "category": "Leadership",
    "options": [
      {
        "option_id": 1,
        "option_text": "Take charge and delegate tasks",
        "trait_tag": "Leadership"
      },
      {
        "option_id": 2,
        "option_text": "Support others and follow instructions",
        "trait_tag": "Collaborative"
      }
    ]
  }
]
```

---

### 7. Submit Assessment & Get Recommendations
**POST** `/recommend`

Submit assessment answers and receive course recommendations.

**Request Body:**
```json
{
  "userId": 1,
  "answers": [
    {
      "questionId": 1,
      "chosenOptionId": 1
    },
    {
      "questionId": 2,
      "chosenOptionId": 4
    }
  ]
}
```

**Response:**
```json
{
  "user_id": 1,
  "user_gwa": 1.75,
  "user_strand": "STEM",
  "detected_traits": [
    ["Analytical", 8],
    ["Leadership", 5],
    ["Strategic", 3]
  ],
  "recommendations": [
    {
      "course_name": "Bachelor of Science in Computer Science",
      "description": "Study of algorithms and computing systems",
      "matched_traits": ["Analytical", "Logical"],
      "minimum_gwa": 2.0,
      "recommended_strand": "STEM",
      "reasoning": "This course aligns with your interests in Analytical, Logical. Your GWA (1.75) meets the requirement (2.0). Your strand (STEM) matches perfectly!",
      "compatibility_score": 15
    }
  ]
}
```

---

## 🔧 Admin - Course Management

### 8. Get All Courses
**GET** `/admin/courses`

Retrieve all courses in the system.

**Response:**
```json
{
  "courses": [
    {
      "course_id": 1,
      "course_name": "BS Computer Science",
      "description": "Study of computing",
      "trait_tag": "Analytical, Logical",
      "minimum_gwa": 2.0,
      "recommended_strand": "STEM"
    }
  ]
}
```

---

### 9. Get Course by ID
**GET** `/admin/courses/{course_id}`

Get specific course details.

---

### 10. Create Course
**POST** `/admin/courses`

Add a new course to the system.

**Request Body:**
```json
{
  "course_name": "BS Nursing",
  "description": "Healthcare and patient care",
  "trait_tag": "Compassionate, Caring",
  "recommended_strand": "STEM",
  "minimum_gwa": 2.0
}
```

**Response:**
```json
{
  "message": "Course created successfully",
  "course": {
    "course_id": 50,
    "course_name": "BS Nursing",
    "description": "Healthcare and patient care",
    "trait_tag": "Compassionate, Caring",
    "minimum_gwa": 2.0,
    "recommended_strand": "STEM"
  }
}
```

---

### 11. Update Course
**PUT** `/admin/courses/{course_id}`

Update course information.

**Request Body:**
```json
{
  "course_name": "BS Nursing (Updated)",
  "description": "Updated description",
  "minimum_gwa": 1.75
}
```

---

### 12. Delete Course
**DELETE** `/admin/courses/{course_id}`

Remove course from system.

**Response:**
```json
{
  "message": "Course 'BS Nursing' deleted successfully"
}
```

---

## 🔧 Admin - Question Management

### 13. Get All Questions
**GET** `/admin/questions`

Retrieve all questions with options.

**Response:**
```json
{
  "questions": [
    {
      "question_id": 1,
      "question_text": "When solving problems, I prefer to:",
      "category": "Problem Solving",
      "options": [
        {
          "option_id": 1,
          "option_text": "Analyze data systematically",
          "trait_tag": "Analytical"
        }
      ]
    }
  ]
}
```

---

### 14. Get Question by ID
**GET** `/admin/questions/{question_id}`

Get specific question with all options.

---

### 15. Create Question
**POST** `/admin/questions`

Add new question with options.

**Request Body:**
```json
{
  "question_text": "In a team setting, I usually:",
  "category": "Teamwork",
  "options": [
    {
      "text": "Lead and organize",
      "trait_tag": "Leadership"
    },
    {
      "text": "Support and collaborate",
      "trait_tag": "Collaborative"
    }
  ]
}
```

**Response:**
```json
{
  "message": "Question created successfully",
  "question_id": 25
}
```

---

### 16. Update Question
**PUT** `/admin/questions/{question_id}`

Update question text or category.

**Request Body:**
```json
{
  "question_text": "Updated question text",
  "category": "New Category"
}
```

---

### 17. Delete Question
**DELETE** `/admin/questions/{question_id}`

Remove question (cascades to options).

---

## 🔧 Admin - Option Management

### 18. Add Option to Question
**POST** `/admin/questions/{question_id}/options`

Add new option to existing question.

**Request Body:**
```json
{
  "option_text": "Work independently",
  "trait_tag": "Independent"
}
```

---

### 19. Update Option
**PUT** `/admin/options/{option_id}`

Update option text or trait tag.

**Request Body:**
```json
{
  "option_text": "Updated option text",
  "trait_tag": "Updated-trait"
}
```

---

### 20. Delete Option
**DELETE** `/admin/options/{option_id}`

Remove option from question.

---

## 🔧 Admin - User Management

### 21. Get All Users
**GET** `/admin/users`

List all registered users.

**Response:**
```json
{
  "users": [
    {
      "user_id": 1,
      "fullname": "John Doe",
      "email": "john@example.com",
      "academic_info": {
        "gwa": 1.75,
        "strand": "STEM"
      },
      "created_at": "2026-01-15T10:00:00"
    }
  ]
}
```

---

### 22. Get User Details
**GET** `/admin/users/{user_id}`

Get detailed user information including assessment history.

**Response:**
```json
{
  "user_id": 1,
  "fullname": "John Doe",
  "email": "john@example.com",
  "academic_info": {
    "gwa": 1.75,
    "strand": "STEM"
  },
  "created_at": "2026-01-15T10:00:00",
  "total_assessments": 2,
  "recommendations_count": 5,
  "latest_recommendations": [
    {
      "course_id": 1,
      "top_trait": "Analytical",
      "reasoning": "This course aligns with..."
    }
  ]
}
```

---

### 23. Delete User
**DELETE** `/admin/users/{user_id}`

Remove user and all related data (answers, recommendations).

---

## 📊 Admin - Reports & Analytics

### 24. System Overview
**GET** `/admin/reports/overview`

Get system-wide statistics.

**Response:**
```json
{
  "total_users": 150,
  "total_courses": 45,
  "total_questions": 25,
  "total_assessments_taken": 120,
  "total_recommendations_generated": 600
}
```

---

### 25. Popular Courses
**GET** `/admin/reports/popular-courses`

Get most recommended courses.

**Response:**
```json
{
  "popular_courses": [
    {
      "course_name": "BS Computer Science",
      "course_id": 1,
      "times_recommended": 45
    },
    {
      "course_name": "BS Business Administration",
      "course_id": 2,
      "times_recommended": 38
    }
  ]
}
```

---

### 26. Trait Distribution
**GET** `/admin/reports/trait-distribution`

View personality trait distribution from all assessments.

**Response:**
```json
{
  "trait_distribution": [
    {
      "trait": "Analytical",
      "count": 234
    },
    {
      "trait": "Leadership",
      "count": 189
    },
    {
      "trait": "Creative",
      "count": 156
    }
  ]
}
```

---

### 27. User Activity
**GET** `/admin/reports/user-activity`

View recent user activity.

**Response:**
```json
{
  "recent_activity": [
    {
      "fullname": "John Doe",
      "email": "john@example.com",
      "last_assessment": "2026-01-16T10:30:00"
    }
  ]
}
```

---

## 🏠 System Endpoint

### 28. Health Check
**GET** `/`

Check if API is running.

**Response:**
```json
{
  "status": "online"
}
```

---

## Error Responses

All endpoints may return these error formats:

### 400 Bad Request
```json
{
  "detail": "Email already exists"
}
```

### 404 Not Found
```json
{
  "detail": "User not found"
}
```

### 500 Internal Server Error
```json
{
  "detail": "Internal server error"
}
```

---

## Notes

- All timestamps are in ISO 8601 format
- Authentication/Authorization should be implemented for production (JWT tokens recommended)
- Admin endpoints should be protected with admin-only access control
- CORS is currently set to allow all origins (`*`) - restrict this in production
- Database is automatically seeded on startup from `seed_data.py`
