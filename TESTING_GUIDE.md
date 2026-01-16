# Testing Guide - Course Recommendation System

## ✅ Complete Testing Workflow

### Step 1: Set Up Academic Profile
1. **Login** to the system (not as admin)
2. Navigate to **"Academic Profile"** from the sidebar
3. Fill in the following information:
   - Full Name
   - Age
   - Gender
   - **SHS Strand** (STEM, ABM, HUMSS, GAS, or TVL)
   - **GWA** (General Weighted Average, e.g., 1.75)
   - Academic Interests
   - Technical & Soft Skills
4. Click **"Update Profile Configuration"**
5. Return to Dashboard

### Step 2: Take Assessment
1. From Dashboard, click **"Start New Assessment"**
2. You will see **20 randomized questions**
3. Each question has 4 options with different personality trait associations:
   - **Analytical** (Blue) - Logical thinking, problem-solving
   - **Creative** (Purple) - Artistic, innovative
   - **Interpersonal** (Pink) - Social skills, teamwork
   - **Practical** (Green) - Hands-on, application-focused
4. **Answer ALL 20 questions** (validation will prevent submission if incomplete)
5. Click **"Submit Assessment"**

### Step 3: View Recommendations
After submission, you should see:

#### User Profile Summary
- Your detected personality traits with counts (e.g., "Analytical (7)")
- Your strand (if provided)
- Your GWA (if provided)

#### Top 5 Course Recommendations
Each course card displays:
- **Course Name** (e.g., "Bachelor of Science in Computer Science")
- **Course Description**
- **Compatibility Score** (as percentage, 0-100%)
- **"Why this fits you"** section with personalized reasoning
- **Matched Traits** badges showing which of your traits align
- **Minimum GWA** required (if applicable)
- **Recommended Strand** (if applicable)

### Step 4: Test Different Scenarios

#### Scenario A: STEM Student with High GWA
- Set Strand: **STEM**
- Set GWA: **1.50**
- Take assessment, answer with mostly **Analytical** options
- Expected: Engineering, Computer Science, Mathematics courses

#### Scenario B: HUMSS Student
- Set Strand: **HUMSS**
- Set GWA: **2.00**
- Take assessment, answer with mostly **Interpersonal** options
- Expected: Psychology, Communication, Social Work courses

#### Scenario C: Creative Profile
- Set Strand: **GAS** or **HUMSS**
- Take assessment, answer with mostly **Creative** options
- Expected: Design, Fine Arts, Multimedia courses

#### Scenario D: Mixed Profile
- Answer questions with variety of trait options
- Expected: Courses that match your dominant traits with balanced reasoning

### Step 5: Verify Results
Check that each recommendation includes:
- ✅ Course name displays correctly
- ✅ Description is clear and relevant
- ✅ Compatibility percentage is realistic (usually 60-95%)
- ✅ Reasoning explains why course matches your profile
- ✅ Matched traits correspond to your answers
- ✅ GWA requirements shown (if course has minimum GWA)
- ✅ Recommended strand shown (if course prefers specific strand)

### Step 6: Retake Assessment
1. Click **"Retake Assessment"** button
2. Answer differently to see how recommendations change
3. Verify that history updates on Dashboard

---

## 🔧 Troubleshooting

### No Recommendations Showing
- **Check Console**: Open browser DevTools (F12) → Console tab
- **Verify Backend**: Ensure server is running on http://localhost:8000
- **Check Response**: Look for errors in network tab

### Wrong Course Recommendations
- **Update Profile**: Make sure GWA and Strand are filled in ProfileForm
- **Answer Consistently**: Select options that match your intended personality
- **Check Trait Distribution**: Your top 3 traits determine recommendations

### Database Issues
- **Verify PostgreSQL**: Ensure service is running
- **Check Connection**: Backend should show "✅ Database connection successful!"
- **Seed Data**: Run `python backend/seed_data.py` if courses/questions are missing

---

## 📊 Behind the Scenes

### Recommendation Algorithm
1. **Trait Detection**: Counts your trait responses (Analytical, Creative, Interpersonal, Practical)
2. **Top 3 Identification**: Selects your 3 most dominant traits
3. **Course Matching**: Finds courses with matching traits
4. **Scoring**: Calculates compatibility (trait matches × 10 points)
5. **Filtering**: Removes courses incompatible with your GWA or strand
6. **Ranking**: Sorts by score, returns top 5
7. **Reasoning**: Generates personalized explanation for each match

### Database Structure
- **99 Courses**: Diverse programs across all fields
- **9 Questions**: 20 randomly selected per assessment
- **Traits Stored**: Each course has 2-4 associated traits
- **GWA Ranges**: Some courses have minimum GWA requirements
- **Strand Preferences**: Some courses prefer specific SHS strands

---

## 🎯 Expected Behavior

### Valid Assessment
- All 20 questions answered → Submit works
- Backend generates recommendations
- Frontend displays results with all components

### Incomplete Assessment
- Missing answers → Alert: "Please answer all questions!"
- Submit blocked until complete

### No Profile Data
- GWA/Strand optional → Algorithm still works
- Recommendations based purely on personality traits

### With Profile Data
- GWA/Strand provided → Filters out incompatible courses
- More personalized recommendations

---

## 📝 Notes
- **User ID**: Currently hardcoded to 1 (suitable for single-user testing)
- **Storage**: Profile data stored in browser localStorage
- **History**: Assessment history tracked per user in localStorage
- **Backend**: FastAPI server must be running on port 8000
- **Database**: PostgreSQL on localhost:5432 (coursepro_db)
