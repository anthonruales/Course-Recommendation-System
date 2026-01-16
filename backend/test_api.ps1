# Test Script for New Endpoints
# Run this in PowerShell to test the new API features

Write-Host "=== Testing Course Recommendation System API ===" -ForegroundColor Cyan

# 1. Health Check
Write-Host "`n1. Testing Health Check..." -ForegroundColor Yellow
curl http://localhost:8000/ | ConvertFrom-Json | ConvertTo-Json

# 2. System Overview
Write-Host "`n2. Testing Admin Reports - System Overview..." -ForegroundColor Yellow
curl http://localhost:8000/admin/reports/overview | ConvertFrom-Json | ConvertTo-Json

# 3. Get All Courses
Write-Host "`n3. Testing Get All Courses..." -ForegroundColor Yellow
$courses = curl http://localhost:8000/admin/courses | ConvertFrom-Json
Write-Host "Total Courses: $($courses.courses.Count)" -ForegroundColor Green

# 4. Get All Questions
Write-Host "`n4. Testing Get All Questions..." -ForegroundColor Yellow
$questions = curl http://localhost:8000/admin/questions | ConvertFrom-Json
Write-Host "Total Questions: $($questions.questions.Count)" -ForegroundColor Green

# 5. Create a Test User
Write-Host "`n5. Testing User Signup..." -ForegroundColor Yellow
$signupData = @{
    fullname = "Test Admin"
    email = "admin@test.com"
    password = "admin123"
} | ConvertTo-Json

try {
    $result = Invoke-RestMethod -Uri "http://localhost:8000/signup" -Method Post -Body $signupData -ContentType "application/json"
    Write-Host "Signup Result: $($result.message)" -ForegroundColor Green
} catch {
    Write-Host "User might already exist" -ForegroundColor Yellow
}

# 6. Login
Write-Host "`n6. Testing User Login..." -ForegroundColor Yellow
$loginData = @{
    email = "admin@test.com"
    password = "admin123"
} | ConvertTo-Json

try {
    $loginResult = Invoke-RestMethod -Uri "http://localhost:8000/login" -Method Post -Body $loginData -ContentType "application/json"
    Write-Host "Login successful! User: $($loginResult.user), ID: $($loginResult.user_id)" -ForegroundColor Green
    $userId = $loginResult.user_id
} catch {
    Write-Host "Login failed" -ForegroundColor Red
    $userId = 1  # Fallback
}

# 7. Update Academic Info
Write-Host "`n7. Testing Update Academic Info..." -ForegroundColor Yellow
$academicData = @{
    gwa = 1.75
    strand = "STEM"
} | ConvertTo-Json

try {
    $academicResult = Invoke-RestMethod -Uri "http://localhost:8000/user/$userId/academic-info" -Method Put -Body $academicData -ContentType "application/json"
    Write-Host "Academic info updated! GWA: $($academicResult.academic_info.gwa), Strand: $($academicResult.academic_info.strand)" -ForegroundColor Green
} catch {
    Write-Host "Failed to update academic info" -ForegroundColor Red
}

# 8. Get Random Questions
Write-Host "`n8. Testing Get Questions for Assessment..." -ForegroundColor Yellow
$assessmentQuestions = curl http://localhost:8000/questions | ConvertFrom-Json
Write-Host "Retrieved $($assessmentQuestions.Count) random questions for assessment" -ForegroundColor Green

# 9. Test Popular Courses Report
Write-Host "`n9. Testing Popular Courses Report..." -ForegroundColor Yellow
try {
    $popularCourses = curl http://localhost:8000/admin/reports/popular-courses | ConvertFrom-Json
    Write-Host "Popular courses data retrieved" -ForegroundColor Green
} catch {
    Write-Host "No recommendations yet (expected for fresh database)" -ForegroundColor Yellow
}

# 10. Get All Users
Write-Host "`n10. Testing Get All Users (Admin)..." -ForegroundColor Yellow
$users = curl http://localhost:8000/admin/users | ConvertFrom-Json
Write-Host "Total Users: $($users.users.Count)" -ForegroundColor Green

Write-Host "`n=== All Tests Complete! ===" -ForegroundColor Cyan
Write-Host "`nAPI is running at: http://localhost:8000" -ForegroundColor Green
Write-Host "Swagger Docs: http://localhost:8000/docs" -ForegroundColor Green
Write-Host "ReDoc: http://localhost:8000/redoc" -ForegroundColor Green
