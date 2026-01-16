import os
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from dotenv import load_dotenv
import models, database
from security import hash_password, verify_password
from seed_data import COURSES_POOL, QUESTIONS_POOL, ASSESSMENT_TIERS
from sqlalchemy import func
from sqlalchemy.orm import Session, joinedload
from trait_mapping import apply_trait_mapping
from assessment_service import AssessmentService

load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🛠️ Synchronizing database schema...")
    models.Base.metadata.create_all(bind=database.engine)
    seed_database()
    yield

app = FastAPI(lifespan=lifespan)
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

def seed_database():
    db = database.SessionLocal()
    try:
        print("🧹 Cleaning out old data...")
        db.query(models.Recommendation).delete()
        db.query(models.StudentAnswer).delete()
        db.query(models.TestAttempt).delete()
        db.query(models.Option).delete()
        db.query(models.Question).delete()
        db.query(models.Test).delete()
        db.query(models.Course).delete()
        db.commit()

        # Create default test
        default_test = models.Test(
            test_name="Career Assessment",
            test_type="assessment",
            description="Comprehensive career interest and aptitude assessment to recommend college courses"
        )
        db.add(default_test)
        db.flush()
        print(f"🌱 Created default test with ID: {default_test.test_id}")

        if COURSES_POOL:
            print(f"🌱 Seeding {len(COURSES_POOL)} courses...")
            for c in COURSES_POOL:
                tags = c.get("trait_tag", [])
                tag_str = ", ".join(tags) if isinstance(tags, list) else str(tags)
                db.add(models.Course(
                    course_name=c.get("course_name"), 
                    description=c.get("description"), 
                    minimum_gwa=c.get("minimum_gwa"), 
                    required_strand=c.get("recommended_strand"),  # Map from recommended_strand to required_strand
                    trait_tag=tag_str
                ))

        if QUESTIONS_POOL:
            print(f"🌱 Seeding {len(QUESTIONS_POOL)} questions...")
            for q in QUESTIONS_POOL:
                new_q = models.Question(
                    test_id=default_test.test_id,
                    question_text=q.get("question"), 
                    category=q.get("category")
                )
                db.add(new_q)
                db.flush()
                options_list = q.get("options", [])
                if options_list:
                    for opt in options_list:
                        db.add(models.Option(question_id=new_q.question_id, option_text=opt.get("text"), trait_tag=opt.get("tag")))
                else:
                    db.add(models.Option(question_id=new_q.question_id, option_text="Yes", trait_tag=q.get("tag")))
                    db.add(models.Option(question_id=new_q.question_id, option_text="No", trait_tag="None"))
        db.commit()
        print("✅ DATABASE SUCCESSFULLY REBUILT AND SEEDED!")
    except Exception as e:
        print(f"❌ DATABASE ERROR: {e}"); db.rollback()
    finally:
        db.close()

def get_db():
    db = database.SessionLocal()
    try: yield db
    finally: db.close()

class UserCreate(BaseModel): fullname: str; email: str; password: str
class UserLogin(BaseModel): email: str; password: str
class AssessmentAnswer(BaseModel):
    questionId: int
    chosenOptionId: int

class AssessmentSubmit(BaseModel):
    userId: int
    answers: List[AssessmentAnswer]
class OptionSchema(BaseModel):
    option_id: int; option_text: str; trait_tag: Optional[str]
    class Config: from_attributes = True
class QuestionSchema(BaseModel):
    question_id: int
    question_text: str
    category: str
    options: List[OptionSchema]

    class Config:
        from_attributes = True


class AcademicInfoUpdate(BaseModel):
    gwa: float
    strand: str
    fullname: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    interests: Optional[str] = None
    skills: Optional[str] = None

class CourseCreate(BaseModel):
    course_name: str
    description: str
    trait_tag: str
    required_strand: Optional[str] = None
    minimum_gwa: Optional[float] = None

class CourseUpdate(BaseModel):
    course_name: Optional[str] = None
    description: Optional[str] = None
    trait_tag: Optional[str] = None
    required_strand: Optional[str] = None
    minimum_gwa: Optional[float] = None

class QuestionCreate(BaseModel):
    question_text: str
    category: str
    options: List[dict]  # [{text: str, trait_tag: str}]

class QuestionUpdate(BaseModel):
    question_text: Optional[str] = None
    category: Optional[str] = None

class OptionCreate(BaseModel):
    option_text: str
    trait_tag: str

class OptionUpdate(BaseModel):
    option_text: Optional[str] = None
    trait_tag: Optional[str] = None


@app.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    if db.query(models.User).filter(models.User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already exists")
    
    # Parse fullname into first_name and last_name
    name_parts = user.fullname.strip().split(" ", 1)
    first_name = name_parts[0] if name_parts else user.fullname
    last_name = name_parts[1] if len(name_parts) > 1 else ""
    
    # Generate username from email
    username = user.email.split("@")[0]
    
    new_user = models.User(
        username=username,
        first_name=first_name,
        last_name=last_name,
        email=user.email,
        password_hash=hash_password(user.password)
    )
    db.add(new_user)
    db.commit()
    return {"message": "Success"}

@app.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if not db_user or not verify_password(user.password, db_user.password_hash):
        raise HTTPException(status_code=400, detail="Invalid email or password")
    return {"user": db_user.fullname, "user_id": db_user.user_id}

@app.post("/google-login")
def google_login(user: dict, db: Session = Depends(get_db)):
    """Handle Google OAuth login - creates user if doesn't exist, returns existing user if does"""
    email = user.get("email")
    name = user.get("name", "")
    
    if not email:
        raise HTTPException(status_code=400, detail="Email is required")
    
    # Check if user exists
    db_user = db.query(models.User).filter(models.User.email == email).first()
    
    if db_user:
        # User exists, return their info
        return {"user": db_user.fullname, "user_id": db_user.user_id}
    else:
        # Create new user with Google info
        name_parts = name.strip().split(" ", 1)
        first_name = name_parts[0] if name_parts else name
        last_name = name_parts[1] if len(name_parts) > 1 else ""
        
        new_user = models.User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password_hash=hash_password(f"google_oauth_{email}")  # Dummy password for Google users
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return {"user": new_user.fullname, "user_id": new_user.user_id}


@app.get("/user/{user_id}/academic-info")
def get_academic_info(user_id: int, db: Session = Depends(get_db)):
    """Get user's academic info including GWA, Strand, and personal info"""
    user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return {
        "user_id": user_id,
        "fullname": user.fullname,
        "academic_info": user.academic_info,
        "has_academic_info": user.academic_info is not None and user.academic_info.get("gwa") is not None and user.academic_info.get("strand") is not None
    }

@app.put("/user/{user_id}/academic-info")
def update_academic_info(user_id: int, info: AcademicInfoUpdate, db: Session = Depends(get_db)):
    """Update user's academic info (GWA, Strand, and personal info) for recommendation accuracy"""
    user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Update fullname if provided (parse into first_name and last_name)
    if info.fullname:
        name_parts = info.fullname.strip().split(" ", 1)
        user.first_name = name_parts[0] if name_parts else info.fullname
        user.last_name = name_parts[1] if len(name_parts) > 1 else ""
    
    # Update academic_info JSON with all fields (D4 - Personal & Academic Database)
    user.academic_info = {
        "gwa": info.gwa,
        "strand": info.strand,
        "age": info.age,
        "gender": info.gender,
        "interests": info.interests,
        "skills": info.skills
    }
    db.commit()
    return {
        "message": "Profile updated successfully",
        "user_id": user_id,
        "fullname": user.fullname,
        "academic_info": user.academic_info
    }

@app.post("/recommend")
def recommend(data: AssessmentSubmit, db: Session = Depends(get_db)):
    """
    DFD Process 5-7: Take a Test → Rule Based-Logic → Decision Tree
    ENHANCED recommendation system with:
    1. Multi-criteria weighted decision tree
    2. Confidence scoring & recommendation quality metrics
    3. Priority-based rule system with tiered matching
    4. Algorithm diversity using multiple scoring methods
    5. Comprehensive explanation generation
    """
    print(f"📝 Received recommendation request for user {data.userId} with {len(data.answers)} answers")
    
    # 1. Fetch user's academic info (D4 - Personal & Academic Database)
    user = db.query(models.User).filter(models.User.user_id == data.userId).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    user_gwa = None
    user_strand = None
    if user.academic_info:
        user_gwa = user.academic_info.get("gwa")
        user_strand = user.academic_info.get("strand")
    
    # Get the default test
    default_test = db.query(models.Test).filter(models.Test.test_type == "assessment").first()
    if not default_test:
        raise HTTPException(status_code=500, detail="No assessment test found in system")
    
    # Create a new test attempt (D5 - Test Attempt Database)
    test_attempt = models.TestAttempt(
        user_id=data.userId,
        test_id=default_test.test_id
    )
    db.add(test_attempt)
    db.flush()  # Get the attempt_id
    print(f"📋 Created test attempt ID: {test_attempt.attempt_id}")
    
    # 2. Process 6: Fetch Q&A - Count traits from the assessment answers
    trait_scores = {}
    category_distribution = {}
    trait_positions = {}  # NEW: Track which questions contributed to each trait
    trait_categories = {}  # NEW: Track which categories each trait appears in
    total_answers = len(data.answers)
    valid_answers = 0
    
    for idx, ans in enumerate(data.answers):
        option = db.query(models.Option).filter(
            models.Option.option_id == ans.chosenOptionId
        ).first()
        
        if option:
            # Save student answer linked to test attempt
            question = db.query(models.Question).filter(
                models.Question.question_id == ans.questionId
            ).first()
            
            db.add(models.StudentAnswer(
                attempt_id=test_attempt.attempt_id,
                question_id=ans.questionId,
                chosen_option_id=ans.chosenOptionId
            ))
            
            # Track category distribution for better insights
            if question and question.category:
                category_distribution[question.category] = category_distribution.get(question.category, 0) + 1
            
            if option.trait_tag and str(option.trait_tag).strip().lower() not in ["none", ""]:
                tag = option.trait_tag.strip()
                trait_scores[tag] = trait_scores.get(tag, 0) + 1
                
                # NEW: Track positions where trait appeared (for consistency analysis)
                if tag not in trait_positions:
                    trait_positions[tag] = []
                trait_positions[tag].append(idx)
                
                # NEW: Track which categories this trait appears in
                if question and question.category:
                    if tag not in trait_categories:
                        trait_categories[tag] = set()
                    trait_categories[tag].add(question.category)
                
                valid_answers += 1
        else:
            print(f"⚠️ Warning: Option ID {ans.chosenOptionId} not found in database")
    
    print(f"📊 Assessment Stats: {total_answers} answers, {valid_answers} with valid traits")
    print(f"📊 Trait Scores: {trait_scores}")
    print(f"📊 Category Distribution: {category_distribution}")
    print(f"🎯 Trait Consistency: {trait_positions}")
    
    if not trait_scores:
        db.rollback()
        raise HTTPException(
            status_code=400, 
            detail=f"Unable to generate recommendations. No personality traits were identified from your {total_answers} answers. Please ensure you've answered all questions."
        )
    
    # 3. IMPROVED Rule Based-Logic with Statistical Analysis
    # Normalize trait scores to percentages for better comparison
    total_trait_selections = sum(trait_scores.values())
    trait_percentages = {trait: (count / total_trait_selections) * 100 
                         for trait, count in trait_scores.items()}
    
    # NEW: Calculate trait consistency (are trait selections clustered or spread out?)
    trait_consistency_scores = {}
    for trait, positions in trait_positions.items():
        if len(positions) > 1:
            # Calculate average gap between selections
            gaps = [positions[i+1] - positions[i] for i in range(len(positions)-1)]
            avg_gap = sum(gaps) / len(gaps) if gaps else 0
            # Lower average gap = more clustered = higher consistency
            consistency = 1.0 / (1 + avg_gap / 5)  # Normalize to 0-1 scale
            trait_consistency_scores[trait] = consistency
        else:
            trait_consistency_scores[trait] = 0.5  # Neutral for single occurrence
    
    # NEW: Calculate category breadth (trait appearing in multiple categories = more versatile)
    trait_breadth_scores = {}
    for trait in trait_scores.keys():
        if trait in trait_categories:
            breadth = len(trait_categories[trait])  # Number of different categories
            trait_breadth_scores[trait] = breadth
        else:
            trait_breadth_scores[trait] = 1
    
    sorted_traits = sorted(trait_scores.items(), key=lambda x: x[1], reverse=True)
    
    # Adaptive trait selection: take more traits if answers are diverse, fewer if focused
    trait_diversity = len([t for t in trait_scores.values() if t >= 2])
    if trait_diversity >= 6:
        top_traits_count = 7  # Highly diverse - consider more traits
    elif trait_diversity >= 4:
        top_traits_count = 5  # Moderately diverse
    else:
        top_traits_count = 3  # Focused personality - fewer traits
    
    top_traits = sorted_traits[:top_traits_count]
    primary_trait = top_traits[0][0]
    trait_focus = trait_percentages.get(primary_trait, 0)
    
    print(f"🎯 Trait Consistency Scores: {trait_consistency_scores}")
    print(f"📚 Trait Breadth (category diversity): {trait_breadth_scores}")
    
    print(f"🎯 Primary Trait: {primary_trait} ({trait_focus:.1f}% focus)")
    print(f"🌈 Trait Diversity: {trait_diversity} distinct traits, using top {top_traits_count}")
    
    # 4. ENHANCED Decision Tree with Multi-Algorithm Scoring
    all_matching_courses = db.query(models.Course).all()
    
    scored_courses = []
    for course in all_matching_courses:
        # Initialize scoring components
        trait_score = 0
        academic_score = 0
        matched_traits = []
        match_quality = {}
        
        # === ALGORITHM 1: Improved Weighted Trait Matching ===
        if course.trait_tag:
            # Apply trait mapping to course tags for better matching
            course_tags = [apply_trait_mapping(tag.strip()) for tag in course.trait_tag.split(",")]
            
            # Calculate weights based on trait importance and user's trait strength
            for idx, (trait, count) in enumerate(top_traits):
                if trait in course_tags:
                    # Base weight decreases with rank
                    position_weight = top_traits_count - idx
                    
                    # Strength multiplier based on how often user selected this trait
                    strength_multiplier = min(2.0, count / 3)  # Cap at 2x for strong traits
                    
                    # NEW: Consistency bonus - reward traits that appeared consistently
                    consistency_bonus = trait_consistency_scores.get(trait, 0.5) * 2  # 0-2 points
                    
                    # NEW: Breadth bonus - reward versatile traits (appeared in multiple categories)
                    breadth_bonus = min(2.0, trait_breadth_scores.get(trait, 1) * 0.5)  # 0-2 points
                    
                    # Focus bonus: if user has high focus on few traits, reward exact matches more
                    if trait_focus > 40 and idx == 0:
                        focus_bonus = 3
                    else:
                        focus_bonus = 0
                    
                    # Enhanced scoring with consistency and breadth
                    trait_contribution = (count * position_weight * strength_multiplier) + focus_bonus + consistency_bonus + breadth_bonus
                    trait_score += trait_contribution
                    matched_traits.append(trait)
            
            # Bonus for courses matching multiple user traits (synergy bonus)
            if len(matched_traits) >= 3:
                trait_score += 5  # Strong synergy
            elif len(matched_traits) >= 2:
                trait_score += 2  # Good synergy
            
            # Calculate trait match quality (what % of course requirements user meets)
            trait_match_pct = (len(matched_traits) / len(course_tags)) * 100 if course_tags else 0
            match_quality['trait_alignment'] = trait_match_pct
            match_quality['trait_count'] = len(matched_traits)
        
        # === ALGORITHM 2: Improved Academic Compatibility ===
        gwa_match = True
        gwa_score = 0
        gwa_penalty = 0
        gwa_gap = 0
        
        if user_gwa and course.minimum_gwa:
            gwa_gap = user_gwa - float(course.minimum_gwa)
            
            if gwa_gap >= 0:
                # Graduated bonus system - rewards excellence without over-weighting it
                if gwa_gap >= 8:
                    gwa_score = 7  # Outstanding (95+)
                elif gwa_gap >= 5:
                    gwa_score = 5  # Excellent
                elif gwa_gap >= 3:
                    gwa_score = 4  # Very good
                elif gwa_gap >= 1:
                    gwa_score = 3  # Good
                else:
                    gwa_score = 2  # Just meets
                gwa_match = True
            else:
                # More forgiving penalty system - don't eliminate good trait matches
                gwa_match = False
                gap_size = abs(gwa_gap)
                if gap_size <= 0.5:
                    gwa_penalty = 1  # Very close miss
                elif gap_size <= 1.5:
                    gwa_penalty = 3  # Close miss
                elif gap_size <= 3:
                    gwa_penalty = 6  # Moderate gap
                elif gap_size <= 5:
                    gwa_penalty = 10  # Large gap
                else:
                    gwa_penalty = 15  # Very large gap
        
        academic_score += gwa_score
        match_quality['gwa_fit'] = gwa_match
        match_quality['gwa_gap'] = round(gwa_gap, 2)
        
        # === ALGORITHM 3: Improved Strand Alignment ===
        strand_match = True
        strand_score = 0
        strand_penalty = 0
        
        if user_strand and course.required_strand:
            if user_strand in course.required_strand:
                strand_score = 6  # Perfect match - increased importance
                strand_match = True
            else:
                # Enhanced strand compatibility matrix
                related_strands = {
                    'STEM': ['GAS'],  # GAS general education fits STEM
                    'ABM': ['GAS', 'HUMSS'],  # Business relates to social sciences
                    'HUMSS': ['GAS', 'ABM'],  # Social sciences overlap
                    'GAS': ['STEM', 'ABM', 'HUMSS', 'TVL', 'Sports'],  # GAS is versatile
                    'TVL': ['GAS', 'STEM'],  # Technical-vocational can fit some STEM
                    'Sports': ['GAS'],  # Sports can fit general programs
                }
                
                compatible_strands = related_strands.get(user_strand, [])
                
                if course.required_strand in compatible_strands:
                    strand_score = 2  # Compatible but not perfect
                    strand_penalty = 3  # Minor penalty
                    strand_match = True  # Still consider it a match
                else:
                    # Check reverse compatibility (course accepts diverse strands)
                    course_accepts_diverse = course.required_strand in ['GAS', 'Any']
                    if course_accepts_diverse:
                        strand_score = 1
                        strand_penalty = 4
                    else:
                        strand_match = False
                        strand_penalty = 7  # Significant mismatch
        
        academic_score += strand_score
        match_quality['strand_fit'] = strand_match
        
        # === Calculate Final Score with Balance ===
        # Balance trait importance with academic factors (60% trait, 40% academic)
        base_score = trait_score + academic_score
        final_score = max(0, base_score - gwa_penalty - strand_penalty)
        
        # NEW: Academic-Trait Synergy Bonus - reward courses where academic fit + trait fit align
        if gwa_match and strand_match and len(matched_traits) >= 2:
            synergy_strength = len(matched_traits) / top_traits_count  # 0.3-1.0 scale
            synergy_bonus = 5 + (synergy_strength * 5)  # 5-10 point bonus
            final_score += synergy_bonus
        elif (gwa_match or strand_match) and len(matched_traits) >= 3:
            # Strong trait match can compensate for partial academic match
            final_score += 4
        
        # === Calculate Confidence Score (0-100) with Enhanced Factors ===
        confidence_factors = []
        
        # Factor 1: Trait match strength (40% weight)
        if course.trait_tag:
            course_tags = [tag.strip() for tag in course.trait_tag.split(",")]
            expected_matches = min(top_traits_count, len(course_tags))
            trait_confidence = min(100, (len(matched_traits) / expected_matches) * 100)
        else:
            trait_confidence = 0
        confidence_factors.append(trait_confidence * 0.40)
        
        # Factor 2: Academic fit (30% weight)
        academic_confidence = 0
        if gwa_match:
            academic_confidence += 50
        if strand_match:
            academic_confidence += 50
        confidence_factors.append(academic_confidence * 0.30)
        
        # Factor 3: Primary trait alignment (20% weight)
        primary_match = 100 if primary_trait in matched_traits else 0
        confidence_factors.append(primary_match * 0.20)
        
        # NEW Factor 4: Trait consistency factor (10% weight)
        # Higher confidence if matched traits were consistently selected
        consistency_factor = 0
        if matched_traits:
            avg_consistency = sum(trait_consistency_scores.get(t, 0.5) for t in matched_traits) / len(matched_traits)
            consistency_factor = avg_consistency * 100
        confidence_factors.append(consistency_factor * 0.10)
        
        confidence_score = sum(confidence_factors)
        
        # === Determine Match Priority with Better Logic ===
        trait_quality = len(matched_traits) >= 3
        academic_quality = gwa_match and strand_match
        primary_present = primary_trait in matched_traits
        
        if academic_quality and trait_quality and primary_present:
            priority = "EXCELLENT"
        elif (gwa_match and strand_match) or (trait_quality and primary_present):
            priority = "GOOD"
        elif (gwa_match or strand_match) and len(matched_traits) >= 2:
            priority = "FAIR"
        else:
            priority = "EXPLORATORY"
        
        scored_courses.append({
            "course": course,
            "score": final_score,
            "base_score": base_score,
            "trait_score": trait_score,
            "academic_score": academic_score,
            "confidence": round(confidence_score, 1),
            "priority": priority,
            "matched_traits": matched_traits,
            "match_quality": match_quality,
            "gwa_match": gwa_match,
            "strand_match": strand_match,
            "gwa_gap": gwa_gap
        })
    
    print(f"📊 Scored {len(scored_courses)} courses")
    
    # 5. IMPROVED Sorting: Balanced multi-factor ranking
    # Primary: score (trait + academic fit)
    # Secondary: confidence (how certain we are)
    # Tertiary: priority tier
    priority_weights = {"EXCELLENT": 4, "GOOD": 3, "FAIR": 2, "EXPLORATORY": 1}
    
    # Composite ranking score for better sorting
    for course_data in scored_courses:
        # Normalized components (0-1 scale)
        score_norm = course_data["score"] / max(1, max([c["score"] for c in scored_courses]))
        confidence_norm = course_data["confidence"] / 100
        priority_norm = priority_weights.get(course_data["priority"], 0) / 4
        
        # Weighted composite: 60% score, 25% confidence, 15% priority
        course_data["composite_rank"] = (score_norm * 0.6) + (confidence_norm * 0.25) + (priority_norm * 0.15)
    
    scored_courses.sort(key=lambda x: x["composite_rank"], reverse=True)
    
    # Intelligent diversity: balance between best matches and variety
    diverse_recommendations = []
    used_strands = {}  # Track how many per strand
    MAX_PER_STRAND = 3  # Allow up to 3 courses per strand
    
    for course_data in scored_courses:
        course = course_data["course"]
        strand = course.required_strand or "General"
        
        # Accept if under strand limit or if it's really high scoring
        strand_count = used_strands.get(strand, 0)
        is_high_priority = course_data["priority"] in ["EXCELLENT", "GOOD"]
        
        if strand_count < MAX_PER_STRAND or (is_high_priority and len(diverse_recommendations) < 10):
            diverse_recommendations.append(course_data)
            used_strands[strand] = strand_count + 1
        
        if len(diverse_recommendations) >= 10:  # Get top 10 for final filtering
            break
    
    # Final selection: prioritize quality over quantity
    # Take best 5, but ensure at least 1 exploratory option if available
    excellent_good = [r for r in diverse_recommendations if r["priority"] in ["EXCELLENT", "GOOD"]]
    other = [r for r in diverse_recommendations if r["priority"] not in ["EXCELLENT", "GOOD"]]
    
    if len(excellent_good) >= 4 and other:
        top_recommendations = excellent_good[:4] + other[:1]  # 4 strong + 1 exploratory
    else:
        print(f"📊 Scored {len(scored_courses)} courses")
    
    # 5. ENHANCED Sorting: Multi-tier ranking
    # Primary: by score, Secondary: by confidence, Tertiary: by priority
    priority_weights = {"EXCELLENT": 4, "GOOD": 3, "FAIR": 2, "EXPLORATORY": 1}
    scored_courses.sort(
        key=lambda x: (x["score"], x["confidence"], priority_weights.get(x["priority"], 0)), 
        reverse=True
    )
    
    # Ensure diversity in recommendations (avoid recommending too many similar courses)
    diverse_recommendations = []
    used_strands = set()
    
    for course_data in scored_courses:
        course = course_data["course"]
        # Add course if we haven't filled quota OR if it's a different strand
        if len(diverse_recommendations) < 5 or course.required_strand not in used_strands:
            diverse_recommendations.append(course_data)
            if course.required_strand:
                used_strands.add(course.required_strand)
        if len(diverse_recommendations) >= 7:  # Get top 7 for final selection
            break
    
    # Select final top 5
    top_recommendations = diverse_recommendations[:5]
    
    # 6. ENHANCED Reasoning with Detailed Explanations
    recommendations = []
    for rank, rec in enumerate(top_recommendations, 1):
        course = rec["course"]
        
        # Build comprehensive reasoning
        reasoning_parts = []
        
        # Trait alignment explanation
        if rec['matched_traits']:
            trait_strength = "strong" if len(rec['matched_traits']) >= 3 else "moderate" if len(rec['matched_traits']) >= 2 else "some"
            reasoning_parts.append(
                f"✓ Shows {trait_strength} alignment with your personality: {', '.join(rec['matched_traits'][:3])}"
                + (f" (+{len(rec['matched_traits'])-3} more)" if len(rec['matched_traits']) > 3 else "")
            )
        else:
            reasoning_parts.append("• This course may expand your horizons into new areas")
        
        # GWA assessment
        if user_gwa and course.minimum_gwa:
            if rec["gwa_match"]:
                if rec["gwa_gap"] >= 5:
                    reasoning_parts.append(f"✓ Your GWA ({user_gwa}) significantly exceeds the requirement ({course.minimum_gwa})")
                elif rec["gwa_gap"] >= 2:
                    reasoning_parts.append(f"✓ Your GWA ({user_gwa}) comfortably meets the requirement ({course.minimum_gwa})")
                else:
                    reasoning_parts.append(f"✓ Your GWA ({user_gwa}) meets the minimum requirement ({course.minimum_gwa})")
            else:
                gap = abs(rec["gwa_gap"])
                if gap <= 1:
                    reasoning_parts.append(f"⚠ Your GWA ({user_gwa}) is slightly below requirement ({course.minimum_gwa}) - achievable with effort")
                else:
                    reasoning_parts.append(f"⚠ Your GWA ({user_gwa}) is {gap:.1f} points below requirement ({course.minimum_gwa}) - significant improvement needed")
        
        # Strand alignment
        if user_strand and course.required_strand:
            if rec["strand_match"]:
                reasoning_parts.append(f"✓ Perfect fit for your {user_strand} strand background")
            else:
                reasoning_parts.append(f"⚠ Recommended for {course.required_strand} strand (you're from {user_strand}) - consider prerequisites")
        
        # Priority tier explanation
        if rec["priority"] == "EXCELLENT":
            reasoning_parts.append("🌟 Highly recommended - excellent overall match")
        elif rec["priority"] == "GOOD":
            reasoning_parts.append("✨ Good match - solid foundation for success")
        elif rec["priority"] == "FAIR":
            reasoning_parts.append("💡 Fair match - could be rewarding with dedication")
        else:
            reasoning_parts.append("🔍 Exploratory option - consider your broader interests")
        
        full_reasoning = " | ".join(reasoning_parts)
        
        recommendations.append({
            "rank": rank,
            "course_name": course.course_name,
            "description": course.description,
            "matched_traits": rec["matched_traits"],
            "minimum_gwa": float(course.minimum_gwa) if course.minimum_gwa else None,
            "recommended_strand": course.required_strand,
            "reasoning": full_reasoning,
            "compatibility_score": rec["score"],
            "confidence_score": rec["confidence"],
            "priority_tier": rec["priority"],
            "match_details": {
                "trait_matches": len(rec["matched_traits"]),
                "gwa_compatible": rec["gwa_match"],
                "strand_compatible": rec["strand_match"],
                "overall_fit": rec["match_quality"]
            }
        })
    
    # Process 8: Decision Tree - Save recommendations to database
    try:
        # Save new recommendations linked to this test attempt
        for idx, rec in enumerate(top_recommendations):
            course = rec["course"]
            db.add(models.Recommendation(
                attempt_id=test_attempt.attempt_id,
                user_id=data.userId,
                course_id=course.course_id,
                reasoning=recommendations[idx]["reasoning"]
            ))
        
        db.commit()
        print(f"✅ Saved {len(top_recommendations)} recommendations for attempt {test_attempt.attempt_id}")
    except Exception as e:
        print(f"❌ Error saving recommendations: {e}")
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error saving recommendations: {str(e)}")
    
    # Generate algorithm performance metrics
    avg_confidence = sum(r["confidence_score"] for r in recommendations) / len(recommendations)
    priority_breakdown = {
        "excellent": len([r for r in recommendations if r["priority_tier"] == "EXCELLENT"]),
        "good": len([r for r in recommendations if r["priority_tier"] == "GOOD"]),
        "fair": len([r for r in recommendations if r["priority_tier"] == "FAIR"]),
        "exploratory": len([r for r in recommendations if r["priority_tier"] == "EXPLORATORY"])
    }
    
    return {
        "user_id": data.userId,
        "user_gwa": user_gwa,
        "user_strand": user_strand,
        "detected_traits": top_traits,
        "trait_analysis": {
            "primary_trait": primary_trait,
            "trait_focus_percentage": round(trait_focus, 1),
            "trait_diversity_score": trait_diversity,
            "total_traits_detected": len(trait_scores)
        },
        "recommendations": recommendations,
        "algorithm_metrics": {
            "average_confidence": round(avg_confidence, 1),
            "priority_distribution": priority_breakdown,
            "total_courses_analyzed": len(all_matching_courses),
            "matching_algorithm_version": "2.0-Enhanced"
        }
    }

@app.get("/questions", response_model=List[QuestionSchema])
def get_questions(db: Session = Depends(get_db)):
    # Using func.random() (for SQLite/Postgres) or func.rand() (for MySQL) 
    # to pull 20 random questions from the database
    questions = db.query(models.Question)\
        .options(joinedload(models.Question.options))\
        .order_by(func.random())\
        .limit(20)\
        .all()
    
    if not questions:
        raise HTTPException(status_code=404, detail="No questions found")
        
    return questions

# ==================== ASSESSMENT TIER ENDPOINTS ====================

@app.get("/assessment/tiers")
def get_assessment_tiers():
    """Get all available assessment tiers with their details"""
    try:
        tiers = AssessmentService.get_available_tiers()
        return {
            "success": True,
            "message": "Assessment tiers retrieved successfully",
            "tiers": tiers,
            "total_tiers": len(tiers)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/assessment/start/{tier}")
def start_assessment(tier: str, db: Session = Depends(get_db)):
    """Start an assessment with a specific tier and fetch questions from database"""
    try:
        # Validate tier
        tier_config = AssessmentService.get_available_tiers()
        if tier not in tier_config:
            raise ValueError(f"Invalid tier. Must be one of: {list(tier_config.keys())}")
        
        question_count = tier_config[tier]["question_count"]
        
        # Fetch random questions from database
        all_questions = db.query(models.Question)\
            .options(joinedload(models.Question.options))\
            .all()
        
        if not all_questions:
            raise ValueError("No questions found in database")
        
        # Randomly select the specified number of questions
        import random
        selected_questions = random.sample(all_questions, min(question_count, len(all_questions)))
        
        # Format questions with database IDs
        formatted_questions = []
        for q in selected_questions:
            formatted_questions.append({
                "question_id": q.question_id,
                "question_text": q.question_text,
                "category": q.category,
                "options": [
                    {
                        "option_id": opt.option_id,
                        "option_text": opt.option_text,
                        "trait_tag": opt.trait_tag
                    }
                    for opt in q.options
                ]
            })
        
        return {
            "success": True,
            "message": f"{tier_config[tier]['name']} started successfully",
            "tier": tier,
            "name": tier_config[tier]['name'],
            "description": tier_config[tier]['description'],
            "question_count": question_count,
            "estimated_time": tier_config[tier]['estimated_time'],
            "accuracy": tier_config[tier]['accuracy'],
            "questions": formatted_questions
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/assessment/questions/{tier}")
def get_assessment_questions(tier: str):
    """Get questions for a specific assessment tier without full assessment metadata"""
    try:
        questions = AssessmentService.get_specific_questions(tier)
        return {
            "success": True,
            "tier": tier,
            "question_count": len(questions),
            "questions": questions
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def home(): return {"status": "online"}

# ========== ADMIN: COURSE MANAGEMENT ==========

@app.get("/admin/courses")
def get_all_courses(db: Session = Depends(get_db)):
    """Admin: Get all courses with full details"""
    courses = db.query(models.Course).all()
    return {"courses": courses}

@app.get("/admin/courses/{course_id}")
def get_course(course_id: int, db: Session = Depends(get_db)):
    """Admin: Get specific course details"""
    course = db.query(models.Course).filter(models.Course.course_id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@app.post("/admin/courses")
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    """Admin: Create new course (D3 - Course Database)"""
    new_course = models.Course(
        course_name=course.course_name,
        description=course.description,
        trait_tag=course.trait_tag,
        required_strand=course.required_strand,
        minimum_gwa=course.minimum_gwa
    )
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return {"message": "Course created successfully", "course": new_course}

@app.put("/admin/courses/{course_id}")
def update_course(course_id: int, course: CourseUpdate, db: Session = Depends(get_db)):
    """Admin: Update existing course (D3 - Course Database)"""
    db_course = db.query(models.Course).filter(models.Course.course_id == course_id).first()
    if not db_course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    if course.course_name is not None:
        db_course.course_name = course.course_name
    if course.description is not None:
        db_course.description = course.description
    if course.trait_tag is not None:
        db_course.trait_tag = course.trait_tag
    if course.required_strand is not None:
        db_course.required_strand = course.required_strand
    if course.minimum_gwa is not None:
        db_course.minimum_gwa = course.minimum_gwa
    
    db.commit()
    db.refresh(db_course)
    return {"message": "Course updated successfully", "course": db_course}

@app.delete("/admin/courses/{course_id}")
def delete_course(course_id: int, db: Session = Depends(get_db)):
    """Admin: Delete course"""
    course = db.query(models.Course).filter(models.Course.course_id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    db.delete(course)
    db.commit()
    return {"message": f"Course '{course.course_name}' deleted successfully"}

# ========== ADMIN: QUESTION MANAGEMENT ==========

@app.get("/admin/questions")
def get_all_questions_admin(db: Session = Depends(get_db)):
    """Admin: Get all questions with options"""
    questions = db.query(models.Question).options(joinedload(models.Question.options)).all()
    return {"questions": questions}

@app.get("/admin/questions/{question_id}")
def get_question_admin(question_id: int, db: Session = Depends(get_db)):
    """Admin: Get specific question with options"""
    question = db.query(models.Question).options(joinedload(models.Question.options))\
        .filter(models.Question.question_id == question_id).first()
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    return question

@app.post("/admin/questions")
def create_question(question: QuestionCreate, db: Session = Depends(get_db)):
    """Admin: Create new question with options"""
    new_question = models.Question(
        question_text=question.question_text,
        category=question.category
    )
    db.add(new_question)
    db.flush()
    
    # Add options
    for opt in question.options:
        new_option = models.Option(
            question_id=new_question.question_id,
            option_text=opt.get("text"),
            trait_tag=opt.get("trait_tag")
        )
        db.add(new_option)
    
    db.commit()
    db.refresh(new_question)
    return {"message": "Question created successfully", "question_id": new_question.question_id}

@app.put("/admin/questions/{question_id}")
def update_question(question_id: int, question: QuestionUpdate, db: Session = Depends(get_db)):
    """Admin: Update question text/category"""
    db_question = db.query(models.Question).filter(models.Question.question_id == question_id).first()
    if not db_question:
        raise HTTPException(status_code=404, detail="Question not found")
    
    if question.question_text is not None:
        db_question.question_text = question.question_text
    if question.category is not None:
        db_question.category = question.category
    
    db.commit()
    return {"message": "Question updated successfully"}

@app.delete("/admin/questions/{question_id}")
def delete_question(question_id: int, db: Session = Depends(get_db)):
    """Admin: Delete question (cascades to options)"""
    question = db.query(models.Question).filter(models.Question.question_id == question_id).first()
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    
    db.delete(question)
    db.commit()
    return {"message": "Question deleted successfully"}

# ========== ADMIN: OPTION MANAGEMENT ==========

@app.post("/admin/questions/{question_id}/options")
def add_option(question_id: int, option: OptionCreate, db: Session = Depends(get_db)):
    """Admin: Add option to existing question"""
    question = db.query(models.Question).filter(models.Question.question_id == question_id).first()
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    
    new_option = models.Option(
        question_id=question_id,
        option_text=option.option_text,
        trait_tag=option.trait_tag
    )
    db.add(new_option)
    db.commit()
    db.refresh(new_option)
    return {"message": "Option added successfully", "option": new_option}

@app.put("/admin/options/{option_id}")
def update_option(option_id: int, option: OptionUpdate, db: Session = Depends(get_db)):
    """Admin: Update option"""
    db_option = db.query(models.Option).filter(models.Option.option_id == option_id).first()
    if not db_option:
        raise HTTPException(status_code=404, detail="Option not found")
    
    if option.option_text is not None:
        db_option.option_text = option.option_text
    if option.trait_tag is not None:
        db_option.trait_tag = option.trait_tag
    
    db.commit()
    return {"message": "Option updated successfully"}

@app.delete("/admin/options/{option_id}")
def delete_option(option_id: int, db: Session = Depends(get_db)):
    """Admin: Delete option"""
    option = db.query(models.Option).filter(models.Option.option_id == option_id).first()
    if not option:
        raise HTTPException(status_code=404, detail="Option not found")
    
    db.delete(option)
    db.commit()
    return {"message": "Option deleted successfully"}

# ========== ADMIN: USER MANAGEMENT ==========

@app.get("/admin/users")
def get_all_users(db: Session = Depends(get_db)):
    """Admin: Get all users with their info"""
    users = db.query(models.User).all()
    user_list = []
    for user in users:
        user_list.append({
            "user_id": user.user_id,
            "fullname": user.fullname,
            "email": user.email,
            "academic_info": user.academic_info,
            "created_at": user.created_at
        })
    return {"users": user_list}

@app.get("/admin/users/{user_id}")
def get_user_details(user_id: int, db: Session = Depends(get_db)):
    """Admin: Get specific user details with assessment history"""
    user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Get user's recommendations
    recommendations = db.query(models.Recommendation).filter(
        models.Recommendation.user_id == user_id
    ).all()
    
    # Get user's assessment answers count
    answers_count = db.query(models.StudentAnswer).filter(
        models.StudentAnswer.user_id == user_id
    ).count()
    
    return {
        "user_id": user.user_id,
        "fullname": user.fullname,
        "email": user.email,
        "academic_info": user.academic_info,
        "created_at": user.created_at,
        "total_assessments": db.query(models.TestAttempt).filter(models.TestAttempt.user_id == user_id).count(),
        "recommendations_count": len(recommendations),
        "latest_recommendations": [
            {
                "course_id": rec.course_id,
                "reasoning": rec.reasoning,
                "recommended_at": rec.recommended_at
            } for rec in recommendations
        ]
    }

@app.delete("/admin/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    """Admin: Delete user and all related data"""
    user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Delete related data (cascade will handle most)
    db.query(models.Recommendation).filter(models.Recommendation.user_id == user_id).delete()
    
    # Get all test attempts for user
    attempts = db.query(models.TestAttempt).filter(models.TestAttempt.user_id == user_id).all()
    for attempt in attempts:
        db.query(models.StudentAnswer).filter(models.StudentAnswer.attempt_id == attempt.attempt_id).delete()
    db.query(models.TestAttempt).filter(models.TestAttempt.user_id == user_id).delete()
    
    db.delete(user)
    db.commit()
    return {"message": f"User '{user.fullname}' and all related data deleted successfully"}

# ========== ADMIN: REPORTS & ANALYTICS ==========

@app.get("/admin/reports/overview")
def get_system_overview(db: Session = Depends(get_db)):
    """Admin: Get system-wide statistics"""
    total_users = db.query(models.User).count()
    total_courses = db.query(models.Course).count()
    total_questions = db.query(models.Question).count()
    total_test_attempts = db.query(models.TestAttempt).count()
    total_recommendations = db.query(models.Recommendation).count()
    total_tests = db.query(models.Test).count()
    
    return {
        "total_users": total_users,
        "total_courses": total_courses,
        "total_questions": total_questions,
        "total_tests": total_tests,
        "total_test_attempts": total_test_attempts,
        "total_recommendations_generated": total_recommendations
    }

@app.get("/admin/reports/popular-courses")
def get_popular_courses(db: Session = Depends(get_db)):
    """Admin: Get most recommended courses"""
    from sqlalchemy import func as sql_func
    
    popular_courses = db.query(
        models.Course.course_name,
        models.Course.course_id,
        sql_func.count(models.Recommendation.recommendation_id).label('recommendation_count')
    ).join(
        models.Recommendation,
        models.Course.course_id == models.Recommendation.course_id
    ).group_by(
        models.Course.course_id,
        models.Course.course_name
    ).order_by(
        sql_func.count(models.Recommendation.recommendation_id).desc()
    ).limit(10).all()
    
    return {
        "popular_courses": [
            {
                "course_name": course.course_name,
                "course_id": course.course_id,
                "times_recommended": course.recommendation_count
            } for course in popular_courses
        ]
    }

@app.get("/admin/reports/trait-distribution")
def get_trait_distribution(db: Session = Depends(get_db)):
    """Admin: Get distribution of personality traits from assessments"""
    from sqlalchemy import func as sql_func
    
    trait_counts = db.query(
        models.Option.trait_tag,
        sql_func.count(models.StudentAnswer.answer_id).label('count')
    ).join(
        models.StudentAnswer,
        models.Option.option_id == models.StudentAnswer.chosen_option_id
    ).filter(
        models.Option.trait_tag.isnot(None),
        models.Option.trait_tag != '',
        models.Option.trait_tag != 'None'
    ).group_by(
        models.Option.trait_tag
    ).order_by(
        sql_func.count(models.StudentAnswer.answer_id).desc()
    ).all()
    
    return {
        "trait_distribution": [
            {
                "trait": trait.trait_tag,
                "count": trait.count
            } for trait in trait_counts
        ]
    }

@app.get("/admin/reports/user-activity")
def get_user_activity(db: Session = Depends(get_db)):
    """Admin: Get recent user activity based on test attempts"""
    from sqlalchemy import func as sql_func
    
    recent_activity = db.query(
        models.User.first_name,
        models.User.last_name,
        models.User.email,
        sql_func.max(models.TestAttempt.taken_at).label('last_assessment')
    ).join(
        models.TestAttempt,
        models.User.user_id == models.TestAttempt.user_id
    ).group_by(
        models.User.user_id,
        models.User.first_name,
        models.User.last_name,
        models.User.email
    ).order_by(
        sql_func.max(models.TestAttempt.taken_at).desc()
    ).limit(20).all()
    
    return {
        "recent_activity": [
            {
                "fullname": f"{activity.first_name} {activity.last_name}".strip(),
                "email": activity.email,
                "last_assessment": activity.last_assessment
            } for activity in recent_activity
        ]
    }

# ========== USER: VIEW HISTORY ==========

@app.get("/user/{user_id}/recommendations")
def get_user_recommendations(user_id: int, db: Session = Depends(get_db)):
    """Get user's saved recommendations"""
    user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    recommendations = db.query(models.Recommendation).filter(
        models.Recommendation.user_id == user_id
    ).all()
    
    result = []
    for rec in recommendations:
        course = db.query(models.Course).filter(
            models.Course.course_id == rec.course_id
        ).first()
        
        if course:
            result.append({
                "course_name": course.course_name,
                "description": course.description,
                "reasoning": rec.reasoning,
                "minimum_gwa": float(course.minimum_gwa) if course.minimum_gwa else None,
                "required_strand": course.required_strand,
                "recommended_at": rec.recommended_at
            })
    
    return {"user_id": user_id, "recommendations": result}

@app.get("/user/{user_id}/assessment-history")
def get_assessment_history(user_id: int, db: Session = Depends(get_db)):
    """Get user's test attempts history (D5 - Test Attempt Database)"""
    user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Get all test attempts for this user
    attempts = db.query(models.TestAttempt).filter(
        models.TestAttempt.user_id == user_id
    ).order_by(models.TestAttempt.taken_at.desc()).all()
    
    history = []
    for attempt in attempts:
        # Count answers for this attempt
        answer_count = db.query(models.StudentAnswer).filter(
            models.StudentAnswer.attempt_id == attempt.attempt_id
        ).count()
        
        # Get test name
        test = db.query(models.Test).filter(
            models.Test.test_id == attempt.test_id
        ).first()
        
        history.append({
            "attempt_id": attempt.attempt_id,
            "test_name": test.test_name if test else "Assessment",
            "taken_at": attempt.taken_at,
            "questions_answered": answer_count
        })
    
    return {
        "user_id": user_id,
        "total_attempts": len(attempts),
        "history": history
    }

# ========== ADMIN: TEST MANAGEMENT ==========

@app.get("/admin/tests")
def get_all_tests(db: Session = Depends(get_db)):
    """Admin: Get all tests"""
    tests = db.query(models.Test).all()
    return {"tests": tests}

@app.get("/admin/test-attempts")
def get_all_test_attempts(db: Session = Depends(get_db)):
    """Admin: Get all test attempts with user info"""
    attempts = db.query(models.TestAttempt).order_by(models.TestAttempt.taken_at.desc()).limit(50).all()
    
    result = []
    for attempt in attempts:
        user = db.query(models.User).filter(models.User.user_id == attempt.user_id).first()
        test = db.query(models.Test).filter(models.Test.test_id == attempt.test_id).first()
        
        result.append({
            "attempt_id": attempt.attempt_id,
            "user_name": user.fullname if user else "Unknown",
            "user_email": user.email if user else "Unknown",
            "test_name": test.test_name if test else "Unknown",
            "taken_at": attempt.taken_at
        })
    
    return {"test_attempts": result}

# Run server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)