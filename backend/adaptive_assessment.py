# adaptive_assessment.py
"""
Adaptive Assessment Engine using Decision Tree Principles (Information Gain)

================================================================================
ALGORITHM FOUNDATION: Decision Tree Classification with Information Gain
Based on: Quinlan, J.R. (1986). Induction of Decision Trees. Machine Learning.
================================================================================

This module implements an adaptive question selection system using the same
Information Gain calculation that powers Decision Tree algorithms (ID3/C4.5).

The Decision Tree Approach:
- Uses Information Gain (Shannon Entropy) to select optimal splitting questions
- Each question acts as a decision node that splits the candidate course set
- Answers traverse the implicit decision tree towards leaf nodes (recommendations)
- The tree is dynamically constructed based on real-time user responses

Key Decision Tree Concepts Applied:
1. INFORMATION GAIN: Measures how well a question discriminates between courses
   (same formula used in ID3/C4.5 Decision Tree construction)
2. ENTROPY CALCULATION: Shannon entropy to find questions that best split candidates
3. ATTRIBUTE SELECTION: Choosing the most informative trait-based question
4. PRUNING: Excluding already-answered questions and rejected topics

The algorithm:
- Start with all courses as candidates (root of implicit tree)
- Calculate Information Gain for each potential question (finding best split)
- Select question with highest gain (optimal decision node)
- User's answer updates trait scores (traversing the tree)
- Repeat until confident or max questions reached (reaching leaf nodes)
- Final recommendations are the courses at the terminal leaf nodes

This approach is MORE ADAPTIVE than a pre-built static Decision Tree because:
- The tree structure adapts to each user's unique responses
- No training data required - uses trait-course relationships directly
- Handles new questions/courses without retraining
"""

import math
from collections import defaultdict
from typing import Dict, List, Optional, Tuple, Set
import random
from dataclasses import dataclass, field
from trait_system import (
    EXPANDED_TRAIT_MAPPING, 
    TRAIT_CATEGORIES, 
    TRAIT_RELATIONSHIPS,
    SPECIALIZED_TRAIT_RELATIONSHIPS,  # NEW: Specialized trait relationships
    calculate_trait_match_score,
    get_trait_similarity
)


@dataclass
class AdaptiveSession:
    """State for a single assessment session"""
    session_id: str
    user_id: int
    
    user_strand: str = None
    user_interests: str = None
    user_skills: str = None
    
    max_questions: int = 30
    min_questions: int = 15
    
    trait_scores: Dict[str, float] = field(default_factory=dict)
    course_scores: Dict[str, float] = field(default_factory=dict)
    answered_questions: Dict[int, int] = field(default_factory=dict)
    excluded_question_ids: Set[int] = field(default_factory=set)
    rejected_topics: Set[str] = field(default_factory=set)
    question_history: List[int] = field(default_factory=list)  # Track order of answered questions for "Previous"
    answer_trait_changes: Dict[int, Dict[str, float]] = field(default_factory=dict)  # Track trait changes per question for reversal
    
    round_number: int = 0
    active_courses: Set[str] = field(default_factory=set)
    confidence: float = 0.0
    is_complete: bool = False
    final_recommendations: List[dict] = field(default_factory=list)


# Maps SHS strand to prioritized traits for question selection
STRAND_PRIORITY_TRAITS = {
    "STEM": ["Software-Dev", "Hardware-Systems", "Lab-Research", "Analytical", "Investigative", 
             "Scientific", "Math-Logic", "Realistic", "Data-Analytics"],
    "ABM": ["Finance-Acct", "Marketing-Sales", "Startup-Venture", "Enterprising", "Conventional",
            "Business-Ops", "Corporate-Mgmt", "Communication"],
    "HUMSS": ["Teaching-Ed", "Community-Serve", "Law-Enforce", "Social", "Artistic",
              "Media-Journalism", "Linguistic-Cultural", "Public-Admin"],
    "TVL": ["Software-Dev", "Hospitality-Svc", "Mechanical-Design", "Realistic", "Conventional",
            "Practical", "Manual-Technical", "Agriculture-Env"],
    "GAS": ["Investigative", "Social", "Enterprising", "Analytical", "Communication",
            "Creative", "Leadership", "Critical-Think"],
    "SPORTS": ["Sports-Fitness", "Coaching-Training", "Realistic", "Social",
               "Practical", "Wellness-Health", "Leadership"],
    "ARTS": ["Creative-Design", "Media-Production", "Artistic", "Creative",
             "Visual-Arts", "Performing-Arts", "Communication"]
}


class AdaptiveAssessmentEngine:
    """
    Selects questions adaptively based on previous answers.
    Prioritizes questions that best discriminate between remaining course candidates.
    """
    
    # Configuration
    MAX_QUESTIONS = 25  # Maximum questions to ask
    MIN_QUESTIONS = 10  # Minimum before allowing early stop
    CONFIDENCE_THRESHOLD = 0.75  # Stop when top courses are this far ahead
    TOP_N_RECOMMENDATIONS = 5  # Number of courses to recommend
    
    def __init__(self, courses: List[dict], questions: List[dict]):
        """Initialize with course and question data."""
        self.courses = {c['course_name']: c for c in courses}
        self.questions = {q['question_id']: q for q in questions}
        self.sessions: Dict[str, AdaptiveSession] = {}
        
        # Build lookup tables
        self.trait_to_courses: Dict[str, Set[str]] = defaultdict(set)
        self.course_traits: Dict[str, Set[str]] = {}
        
        for course_name, course in self.courses.items():
            traits = self._parse_traits(course.get('trait_tag', ''))
            self.course_traits[course_name] = traits
            for trait in traits:
                self.trait_to_courses[trait].add(course_name)
        
        # Pre-compute trait -> questions mapping
        self.trait_to_questions: Dict[str, List[int]] = defaultdict(list)
        for qid, question in self.questions.items():
            for opt in question.get('options', []):
                trait = opt.get('trait_tag')
                if trait:
                    self.trait_to_questions[trait].append(qid)
        
        print(f"[ENGINE] Adaptive Engine initialized with {len(self.courses)} courses and {len(self.questions)} questions")
    
    def _parse_traits(self, trait_tag) -> Set[str]:
        """Parse trait_tag field into set of traits"""
        if not trait_tag:
            return set()
        if isinstance(trait_tag, list):
            return set(trait_tag)
        return set(t.strip() for t in str(trait_tag).split(',') if t.strip())
    
    def _calculate_profile_bonus(self, interests: str, skills: str, course_traits: Set[str]) -> float:
        """Calculate bonus points (0-15) for courses matching user's profile interests/skills."""
        if not interests and not skills:
            return 0.0
        
        # Profile keyword to trait mapping - MUST use actual trait names from courses
        PROFILE_TO_TRAITS = {
            "science": ["Scientific", "Lab-Research", "Medical-Lab"],
            "biology": ["Medical-Lab", "Lab-Research", "Patient-Care"],
            "chemistry": ["Medical-Lab", "Lab-Research", "Scientific"],
            "physics": ["Mechanical-Design", "Electrical-Power", "Civil-Build"],
            "environment": ["Field-Research", "Agri-Nature"],
            "programming": ["Software-Dev", "Data-Analytics", "Cyber-Defense"],
            "computer": ["Software-Dev", "Hardware-Systems", "Data-Analytics"],
            "data": ["Data-Analytics", "Software-Dev"],
            "ai": ["Software-Dev", "Data-Analytics"],
            "cybersecurity": ["Cyber-Defense", "Software-Dev"],
            "engineering": ["Civil-Build", "Mechanical-Design", "Electrical-Power", "Industrial-Ops"],
            "mechanical": ["Mechanical-Design", "Industrial-Ops"],
            "electrical": ["Electrical-Power", "Hardware-Systems"],
            "civil": ["Civil-Build", "Spatial-Design"],
            "business": ["Startup-Venture", "Marketing-Sales", "Finance-Acct", "Admin-Skill"],
            "finance": ["Finance-Acct", "Startup-Venture"],
            "marketing": ["Marketing-Sales", "Startup-Venture"],
            "accounting": ["Finance-Acct", "Admin-Skill"],
            "economics": ["Finance-Acct"],
            "art": ["Visual-Design", "Creative-Skill", "Digital-Media"],
            "music": ["Creative-Skill"],
            "film": ["Digital-Media", "Creative-Skill"],
            "writing": ["Creative-Skill"],
            "photography": ["Visual-Design", "Digital-Media"],
            "medical": ["Patient-Care", "Medical-Lab", "Rehab-Therapy"],
            "nursing": ["Patient-Care"],
            "psychology": ["Rehab-Therapy", "Community-Serve"],
            "education": ["Teaching-Ed"],
            "law": ["Law-Enforce"],
            "politics": ["Community-Serve"],
            "social": ["Community-Serve", "Rehab-Therapy"],
            "history": ["Community-Serve"],
            # Sports & Fitness - CORRECT trait names
            "sports": ["Physical-Skill", "Rehab-Therapy", "Teaching-Ed"],
            "fitness": ["Physical-Skill", "Rehab-Therapy"],
            "sports & fitness": ["Physical-Skill", "Rehab-Therapy", "Teaching-Ed"],
            "sports and fitness": ["Physical-Skill", "Rehab-Therapy", "Teaching-Ed"],
            "athletic": ["Physical-Skill"],
            "physical education": ["Physical-Skill", "Teaching-Ed"],
            "tourism": ["Hospitality-Svc"],
            "food": ["Hospitality-Svc"],
            "agriculture": ["Agri-Nature", "Field-Research"],
            
            # Skills - CORRECT trait names
            "programming_skill": ["Software-Dev", "Data-Analytics"],
            "data_analysis": ["Data-Analytics", "Software-Dev"],
            "web_development": ["Software-Dev", "Digital-Media"],
            "graphic_design": ["Visual-Design", "Digital-Media"],
            "video_editing": ["Digital-Media", "Creative-Skill"],
            "math_skills": ["Data-Analytics", "Finance-Acct"],
            "laboratory": ["Lab-Research", "Medical-Lab"],
            "technical_writing": ["Admin-Skill", "Software-Dev"],
            "public_speaking": ["Teaching-Ed", "Marketing-Sales"],
            "writing_skill": ["Creative-Skill", "Admin-Skill"],
            "presentation": ["Marketing-Sales", "Teaching-Ed"],
            "negotiation": ["Marketing-Sales", "Startup-Venture"],
            "foreign_language": ["Teaching-Ed", "Hospitality-Svc"],
            "leadership": ["Startup-Venture", "Admin-Skill"],
            "project_management": ["Admin-Skill", "Industrial-Ops"],
            "team_management": ["Admin-Skill", "People-Skill"],
            "decision_making": ["Startup-Venture", "Admin-Skill"],
            "planning": ["Admin-Skill", "Industrial-Ops"],
            "teamwork": ["People-Skill", "Industrial-Ops"],
            "empathy": ["Patient-Care", "Rehab-Therapy"],
            "customer_service": ["Hospitality-Svc", "People-Skill"],
            "mentoring": ["Teaching-Ed"],
            "conflict_resolution": ["People-Skill", "Community-Serve"],
            # Musical Ability - CORRECT trait names
            "musical": ["Creative-Skill"],
            "musical ability": ["Creative-Skill"],
            "singing": ["Creative-Skill"],
            "instrument": ["Creative-Skill"],
            # Additional analytical skills
            "critical_thinking": ["Data-Analytics", "Lab-Research"],
            "problem_solving": ["Software-Dev", "Mechanical-Design", "Data-Analytics"],
            "research": ["Lab-Research", "Field-Research"],
            "attention_detail": ["Admin-Skill", "Finance-Acct"],
            "logical_reasoning": ["Data-Analytics", "Software-Dev"],
            "creativity": ["Creative-Skill", "Visual-Design", "Digital-Media"],
            "artistic": ["Visual-Design", "Creative-Skill"],
            "music_skill": ["Creative-Skill"],
            "storytelling": ["Creative-Skill", "Digital-Media"],
            "design_thinking": ["Visual-Design", "Creative-Skill"],
        }
        
        # Parse user's selections
        interest_list = [i.strip().lower() for i in (interests or "").split(",") if i.strip()]
        skill_list = [s.strip().lower() for s in (skills or "").split(",") if s.strip()]
        user_selections = set(interest_list + skill_list)
        
        # Normalize course traits for matching
        course_traits_lower = {t.lower() for t in course_traits}
        
        bonus = 0.0
        matched_count = 0
        
        for selection in user_selections:
            # Get related traits for this selection
            related_traits = PROFILE_TO_TRAITS.get(selection, [])
            
            for trait in related_traits:
                trait_lower = trait.lower()
                # Check if any course trait matches
                for course_trait in course_traits_lower:
                    if trait_lower in course_trait or course_trait in trait_lower:
                        matched_count += 1
                        bonus += 3.0  # 3 points per match
                        break
        
        # Cap bonus at 15 points (5 strong matches)
        return min(bonus, 15.0)
    
    def _determine_rejected_topic(self, question: dict, chosen_option: dict) -> Optional[str]:
        """Figure out which topic the user rejected when they selected 'none'."""
        option_text = chosen_option.get('option_text', '').lower()
        
        # Keyword to topic mapping
        REJECTION_KEYWORDS = {
            "healthcare": "Patient-Care",
            "nursing": "Patient-Care",
            "medical": "Medical-Lab",
            "technology": "Software-Dev",
            "programming": "Software-Dev",
            "coding": "Software-Dev",
            "engineering": "Civil-Build",
            "business": "Finance-Acct",
            "accounting": "Finance-Acct",
            "finance": "Finance-Acct",
            "teaching": "Teaching-Ed",
            "education": "Teaching-Ed",
            "teach": "Teaching-Ed",
            "creative": "Visual-Design",
            "arts": "Visual-Design",
            "design": "Visual-Design",
            "maritime": "Maritime-Sea",
            "sea": "Maritime-Sea",
            "ship": "Maritime-Sea",
            "agriculture": "Agri-Nature",
            "farming": "Agri-Nature",
            "urban": "Agri-Nature",
            "land-based": "Maritime-Sea",
            "hospitality": "Hospitality-Svc",
            "hotel": "Hospitality-Svc",
            "tourism": "Hospitality-Svc",
            "law": "Law-Enforce",
            "police": "Law-Enforce",
            "criminology": "Law-Enforce",
            "private sector": "Community-Serve",
            "public": "Community-Serve",
        }
        
        # Check for direct keyword matches in the rejection text
        for keyword, topic in REJECTION_KEYWORDS.items():
            if keyword in option_text:
                return topic
        
        # If no direct match, analyze the question's other options
        # The rejected topic is likely what most other options are about
        question_category = question.get('category', '').lower()
        
        # Category-based rejection
        CATEGORY_TO_TOPIC = {
            "healthcare": "Patient-Care",
            "nursing": "Patient-Care",
            "medical": "Medical-Lab",
            "technology": "Software-Dev",
            "tech": "Software-Dev",
            "engineering": "Civil-Build",
            "business": "Finance-Acct",
            "finance": "Finance-Acct",
            "education": "Teaching-Ed",
            "creative": "Visual-Design",
            "arts": "Visual-Design",
            "maritime": "Maritime-Sea",
            "agriculture": "Agri-Nature",
            "hospitality": "Hospitality-Svc",
            "public service": "Community-Serve",
            "law": "Law-Enforce",
        }
        
        for category_keyword, topic in CATEGORY_TO_TOPIC.items():
            if category_keyword in question_category:
                return topic
        
        # Count traits from other options to determine majority topic
        trait_counts: Dict[str, int] = {}
        for opt in question.get('options', []):
            if opt.get('option_id') != chosen_option.get('option_id'):
                trait = opt.get('trait_tag')
                if trait:
                    trait_counts[trait] = trait_counts.get(trait, 0) + 1
        
        # Return the most common trait from other options (what user rejected)
        if trait_counts:
            most_common = max(trait_counts.items(), key=lambda x: x[1])
            if most_common[1] >= 2:  # At least 2 options had this trait
                return most_common[0]
        
        return None
    
    def _get_profile_priority_traits(self, session: AdaptiveSession) -> Set[str]:
        """Get traits that should be prioritized based on user's profile interests/skills.
        
        When user selects many interests/skills, we prioritize traits that appear
        most frequently across their selections (shows stronger preference).
        We limit to top 6 traits to ensure focused early questions.
        """
        if not session.user_interests and not session.user_skills:
            return set()
        
        # Reuse the PROFILE_TO_TRAITS mapping
        PROFILE_TO_TRAITS = {
            "science": ["Scientific", "Lab-Research", "Medical-Lab"],
            "biology": ["Medical-Lab", "Lab-Research", "Patient-Care"],
            "chemistry": ["Medical-Lab", "Lab-Research"],
            "physics": ["Mechanical-Design", "Electrical-Power", "Civil-Build"],
            "environment": ["Agri-Nature", "Field-Research"],
            "programming": ["Software-Dev", "Data-Analytics", "Cyber-Defense"],
            "computer": ["Software-Dev", "Hardware-Systems", "Data-Analytics"],
            "data": ["Data-Analytics", "Software-Dev"],
            "ai": ["Software-Dev", "Data-Analytics"],
            "cybersecurity": ["Cyber-Defense", "Software-Dev"],
            "engineering": ["Civil-Build", "Mechanical-Design", "Electrical-Power", "Industrial-Ops"],
            "mechanical": ["Mechanical-Design", "Industrial-Ops"],
            "electrical": ["Electrical-Power", "Hardware-Systems"],
            "civil": ["Civil-Build", "Spatial-Design"],
            "business": ["Startup-Venture", "Marketing-Sales", "Finance-Acct"],
            "finance": ["Finance-Acct", "Startup-Venture"],
            "marketing": ["Marketing-Sales", "Startup-Venture"],
            "accounting": ["Finance-Acct", "Admin-Skill"],
            "economics": ["Finance-Acct"],
            "art": ["Visual-Design", "Creative-Skill", "Digital-Media"],
            "music": ["Creative-Skill"],
            "film": ["Digital-Media", "Creative-Skill"],
            "writing": ["Creative-Skill"],
            "photography": ["Visual-Design", "Digital-Media"],
            "medical": ["Patient-Care", "Medical-Lab", "Rehab-Therapy"],
            "nursing": ["Patient-Care"],
            "psychology": ["Rehab-Therapy", "Community-Serve"],
            "education": ["Teaching-Ed"],
            "law": ["Law-Enforce"],
            "politics": ["Community-Serve"],
            "social": ["Community-Serve", "Rehab-Therapy"],
            "tourism": ["Hospitality-Svc"],
            "food": ["Hospitality-Svc"],
            "agriculture": ["Agri-Nature"],
            # Skills mapping
            "programming_skill": ["Software-Dev", "Data-Analytics"],
            "data_analysis": ["Data-Analytics", "Software-Dev"],
            "web_development": ["Software-Dev", "Digital-Media"],
            "graphic_design": ["Visual-Design", "Digital-Media"],
            "video_editing": ["Digital-Media"],
            "laboratory": ["Lab-Research", "Medical-Lab"],
            "leadership": ["Startup-Venture", "Admin-Skill"],
            "project_management": ["Admin-Skill", "Industrial-Ops"],
            "empathy": ["Patient-Care", "Rehab-Therapy"],
            "customer_service": ["Hospitality-Svc"],
            "mentoring": ["Teaching-Ed"],
            "research": ["Lab-Research", "Field-Research"],
            "creativity": ["Visual-Design", "Creative-Skill", "Digital-Media"],
            "artistic": ["Visual-Design", "Creative-Skill"],
            # Additional common terms
            "public_speaking": ["Teaching-Ed", "Marketing-Sales"],
            "communication": ["Marketing-Sales", "Teaching-Ed", "Admin-Skill"],
            "problem_solving": ["Software-Dev", "Mechanical-Design", "Data-Analytics"],
            "critical_thinking": ["Scientific", "Lab-Research", "Data-Analytics"],
            "teamwork": ["Industrial-Ops", "Admin-Skill", "Community-Serve"],
            "writing_skill": ["Creative-Skill", "Admin-Skill"],
            # Sports & Fitness
            "sports": ["Physical-Skill", "Rehab-Therapy"],
            "fitness": ["Physical-Skill", "Rehab-Therapy"],
            "sports & fitness": ["Physical-Skill", "Rehab-Therapy"],
            "sports and fitness": ["Physical-Skill", "Rehab-Therapy"],
            "athletic": ["Physical-Skill"],
            "physical education": ["Physical-Skill", "Teaching-Ed"],
            # Musical Ability
            "musical": ["Creative-Skill"],
            "musical ability": ["Creative-Skill"],
            "music": ["Creative-Skill"],
            "singing": ["Creative-Skill"],
            "instrument": ["Creative-Skill"],
        }
        
        # Count how often each trait appears across all selected interests/skills
        trait_counts = {}
        
        # Parse interests
        if session.user_interests:
            for interest in session.user_interests.split(','):
                interest = interest.strip().lower()
                traits = PROFILE_TO_TRAITS.get(interest, [])
                for trait in traits:
                    trait_counts[trait] = trait_counts.get(trait, 0) + 1
        
        # Parse skills
        if session.user_skills:
            for skill in session.user_skills.split(','):
                skill = skill.strip().lower()
                traits = PROFILE_TO_TRAITS.get(skill, [])
                for trait in traits:
                    trait_counts[trait] = trait_counts.get(trait, 0) + 1
        
        if not trait_counts:
            return set()
        
        # Sort traits by frequency (most common first) and take top 6
        # This ensures early questions focus on the user's STRONGEST interests
        sorted_traits = sorted(trait_counts.items(), key=lambda x: x[1], reverse=True)
        top_traits = [trait for trait, count in sorted_traits[:6]]
        
        print(f"[STATS] User profile traits (top 6 of {len(trait_counts)}): {top_traits}")
        
        return set(top_traits)
    
    def _get_strand_priority_traits(self, strand: str) -> Set[str]:
        """Get traits prioritized by user's SHS strand."""
        return set(STRAND_PRIORITY_TRAITS.get(strand, []))

    def create_session(self, user_id: int, user_gwa: float = None, user_strand: str = None, max_questions: int = 30, user_interests: str = None, user_skills: str = None) -> str:
        """Start a new assessment session. Returns session_id."""
        import uuid
        session_id = str(uuid.uuid4())[:8]
        
        # Normalize strand
        normalized_strand = user_strand.upper() if user_strand else "GAS"
        if normalized_strand not in STRAND_PRIORITY_TRAITS:
            normalized_strand = "GAS"
        
        # Calculate min questions (50% of max)
        min_questions = int(max_questions * 0.5)
        
        # Initialize all courses with base score
        course_scores = {name: 50.0 for name in self.courses}
        
        # Apply initial GWA/Strand bonuses (not exclusions!)
        for course_name, course in self.courses.items():
            # GWA bonus (preference, not requirement)
            if user_gwa and course.get('minimum_gwa'):
                if user_gwa >= course['minimum_gwa']:
                    course_scores[course_name] += 5  # Bonus for meeting GWA
                elif user_gwa >= course['minimum_gwa'] - 5:
                    course_scores[course_name] += 2  # Small bonus for close
            
            # Strand bonus (preference, not requirement)
            if user_strand and course.get('required_strand'):
                if user_strand.upper() == course['required_strand'].upper():
                    course_scores[course_name] += 5  # Bonus for matching strand
            
            # Add profile bonus from interests/skills
            if user_interests or user_skills:
                course_traits = self.course_traits.get(course_name, set())
                profile_bonus = self._calculate_profile_bonus(user_interests, user_skills, course_traits)
                course_scores[course_name] += profile_bonus
        
        session = AdaptiveSession(
            session_id=session_id,
            user_id=user_id,
            user_strand=normalized_strand,  # Store strand for question selection
            user_interests=user_interests,  # Store for later use
            user_skills=user_skills,  # Store for later use
            max_questions=max_questions,
            min_questions=min_questions,
            course_scores=course_scores,
            active_courses=set(self.courses.keys())
        )
        
        self.sessions[session_id] = session
        print(f"[SESSION] Created adaptive session {session_id} for user {user_id} (strand: {normalized_strand}, questions: {max_questions}, interests: {bool(user_interests)}, skills: {bool(user_skills)})")
        return session_id
    
    def get_next_question(self, session_id: str) -> Optional[dict]:
        """Select question based on profile relevance (early) and information gain (later)."""
        session = self.sessions.get(session_id)
        if not session or session.is_complete:
            return None
        
        if self._should_stop(session):
            self._finalize_session(session)
            return None
        
        # Get user's profile traits (from interests, skills, strand)
        profile_traits = self._get_profile_priority_traits(session)
        strand_traits = self._get_strand_priority_traits(session.user_strand)
        all_priority_traits = profile_traits | strand_traits
        
        # Calculate information gain for adaptive selection
        trait_info_scores = self._calculate_trait_information_gain(session)
        
        best_question = None
        best_score = -1
        
        question_ids = list(self.questions.keys())
        random.shuffle(question_ids)
        
        for qid in question_ids:
            if qid in session.excluded_question_ids:
                continue
            
            question = self.questions[qid]
            options = question.get('options', [])
            
            # Check how many options are about rejected topics
            rejected_count = 0
            profile_match_count = 0
            
            for opt in options:
                trait = opt.get('trait_tag')
                if trait:
                    if trait in session.rejected_topics:
                        rejected_count += 1
                    if trait in all_priority_traits:
                        profile_match_count += 1
            
            # Skip questions where most options are about rejected topics
            if len(options) > 0 and rejected_count / len(options) > 0.5:
                continue
            
            # Calculate base score
            question_score = self._score_question(question, trait_info_scores, session)
            
            # FIRST 5 QUESTIONS: Focus on profile-relevant questions
            if session.round_number < 5:
                # Strong bonus for questions matching user's profile
                if profile_match_count >= 3:
                    question_score += 3.0
                elif profile_match_count >= 2:
                    question_score += 2.0
                elif profile_match_count >= 1:
                    question_score += 1.0
                
                # Penalty for rejected topic presence (even partial)
                if rejected_count > 0:
                    question_score *= (1 - rejected_count / len(options) * 0.8)
            
            if question_score > best_score:
                best_score = question_score
                best_question = question
        
        if best_question:
            session.round_number += 1
            print(f"[TARGET] Round {session.round_number}: Q{best_question.get('question_id')} (score: {best_score:.2f})")
            return {
                "session_id": session_id,
                "round": session.round_number,
                "total_max_rounds": session.max_questions,
                "question": best_question,
                "courses_remaining": len(session.active_courses),
                "confidence": round(session.confidence * 100, 1),
                "can_finish_early": session.round_number >= session.min_questions
            }
        
        self._finalize_session(session)
        return None
    
    def _calculate_profile_question_bonus(self, question: dict, profile_traits: Set[str], bonus_multiplier: float) -> float:
        """Calculate bonus score for questions matching user's profile interests/skills."""
        if not profile_traits:
            return 0
        
        options = question.get('options', [])
        matching_options = 0
        
        for opt in options:
            trait = opt.get('trait_tag')
            if trait and trait in profile_traits:
                matching_options += 1
        
        # Bonus based on how many options match profile traits
        if matching_options >= 3:
            return bonus_multiplier * 1.5  # Strong match
        elif matching_options >= 2:
            return bonus_multiplier * 1.0
        elif matching_options >= 1:
            return bonus_multiplier * 0.5
        
        return 0
        
        # No more questions available
        self._finalize_session(session)
        return None
    
    def _calculate_trait_information_gain(self, session: AdaptiveSession) -> Dict[str, float]:
        """
        Calculate how valuable each trait would be to ask about.
        
        Traits that appear in roughly half the active courses are most valuable
        (they split the candidate set best).
        
        Traits we already know about are less valuable.
        """
        trait_value = {}
        total_active = len(session.active_courses)
        
        if total_active == 0:
            return trait_value
        
        for trait, courses_with_trait in self.trait_to_courses.items():
            # How many active courses have this trait?
            active_with_trait = len(courses_with_trait & session.active_courses)
            
            if active_with_trait == 0 or active_with_trait == total_active:
                # This trait doesn't discriminate at all
                trait_value[trait] = 0
                continue
            
            # Information gain is highest when trait splits courses 50/50
            # Entropy: -p*log(p) - (1-p)*log(1-p)
            p = active_with_trait / total_active
            entropy = -p * math.log2(p) - (1-p) * math.log2(1-p) if 0 < p < 1 else 0
            
            # Reduce value if we already have strong info about this trait
            existing_knowledge = abs(session.trait_scores.get(trait, 0))
            knowledge_penalty = 1 / (1 + existing_knowledge * 0.5)
            
            trait_value[trait] = entropy * knowledge_penalty
        
        return trait_value
    
    def _score_question(self, question: dict, trait_values: Dict[str, float], 
                       session: AdaptiveSession) -> float:
        """Score question value based on trait info gain and strand relevance."""
        score = 0
        options = question.get('options', [])
        
        # Get strand priority traits
        strand_priority_traits = set(STRAND_PRIORITY_TRAITS.get(session.user_strand, []))
        
        # Track if this question is primarily about a rejected topic
        rejected_option_count = 0
        total_options = len(options)
        
        for opt in options:
            trait = opt.get('trait_tag')
            if trait:
                # Check if this option's trait is in rejected topics
                if trait in session.rejected_topics:
                    rejected_option_count += 1
                
                # Direct trait value
                score += trait_values.get(trait, 0)
                
                # Strand relevance bonus
                if trait in strand_priority_traits:
                    score += 0.5
                
                # Also consider mapped traits from our trait system
                mapped_traits = EXPANDED_TRAIT_MAPPING.get(trait, [])
                for mapped_trait in mapped_traits:
                    score += trait_values.get(mapped_trait, 0) * 0.5
                    if mapped_trait in strand_priority_traits:
                        score += 0.25
                    # Check mapped traits for rejection too
                    if mapped_trait in session.rejected_topics:
                        rejected_option_count += 0.5
        
        # Penalize questions about rejected topics
        if total_options > 0:
            rejection_ratio = rejected_option_count / total_options
            if rejection_ratio > 0.5:
                score *= 0.1
            elif rejection_ratio > 0.3:
                score *= 0.4
            elif rejection_ratio > 0.1:
                score *= 0.7
        
        # Bonus for questions with more options (more information)
        option_bonus = min(len(options) / 4, 1.5)
        score *= option_bonus
        
        # Category diversity bonus (prefer different categories)
        category = question.get('category', '')
        category_count = sum(1 for qid in session.answered_questions 
                           if self.questions.get(qid, {}).get('category') == category)
        diversity_bonus = 1 / (1 + category_count * 0.2)
        score *= diversity_bonus
        
        return score
    
    def process_answer(self, session_id: str, question_id: int, 
                      chosen_option_id: int) -> dict:
        """Process answer and update trait/course scores."""
        session = self.sessions.get(session_id)
        if not session:
            print(f"[WARN] process_answer: Session {session_id} not found!")
            return {"error": "Session not found"}
        
        if session.is_complete:
            print(f"[WARN] process_answer: Session {session_id} already complete, answer NOT recorded for q{question_id}")
            return {
                "status": "complete",
                "recommendations": session.final_recommendations
            }
        
        question = self.questions.get(question_id)
        if not question:
            print(f"[WARN] process_answer: Question {question_id} not found in engine questions!")
            return {"error": "Question not found"}
        
        # Find the chosen option
        chosen_option = None
        for opt in question.get('options', []):
            if opt.get('option_id') == chosen_option_id:
                chosen_option = opt
                break
        
        if not chosen_option:
            print(f"[WARN] process_answer: Option {chosen_option_id} not found for question {question_id}!")
            return {"error": "Option not found"}
        
        # Check if this question was already answered (prevent duplicate answers)
        if question_id in session.answered_questions:
            print(f"[WARN] process_answer: Question {question_id} already answered! Skipping duplicate.")
            # Still return success to not break the flow, but don't overwrite
            return {
                "status": "duplicate",
                "message": "Question already answered",
                "session_id": session_id,
                "round": session.round_number,
                "confidence": round(session.confidence * 100, 1),
                "courses_remaining": len(self.courses),
                "traits_discovered": len(session.trait_scores)
            }
        
        # Record the answer
        session.answered_questions[question_id] = chosen_option_id
        session.excluded_question_ids.add(question_id)
        session.question_history.append(question_id)  # Track for "Previous" button
        print(f"[ANSWER] Q{question_id} answered. Total answers={len(session.answered_questions)}, round={session.round_number}, excluded={len(session.excluded_question_ids)}")
        
        # Check if user rejected this topic (e.g., "none", "not interested")
        option_text = chosen_option.get('option_text', '').lower()
        is_rejection = any(phrase in option_text for phrase in [
            "none", "not interested", "don't want", "prefer not", 
            "i'm not", "im not", "prefer non-", "prefer other",
            "i don't want to", "not for me"
        ])
        
        # Also check for specific topic rejections in the option text
        EXPLICIT_REJECTIONS = {
            "don't want to teach": "Teaching-Ed",
            "not teach": "Teaching-Ed",
            "don't want to be a teacher": "Teaching-Ed",
            "not in education": "Teaching-Ed",
            "don't want healthcare": "Patient-Care",
            "not medical": "Patient-Care",
            "don't want engineering": "Civil-Build",
            "not engineering": "Civil-Build",
            "don't want business": "Finance-Acct",
            "not business": "Finance-Acct",
            "don't want technology": "Software-Dev",
            "not tech": "Software-Dev",
            "don't want maritime": "Maritime-Sea",
            "not maritime": "Maritime-Sea",
        }
        
        for phrase, topic in EXPLICIT_REJECTIONS.items():
            if phrase in option_text:
                session.rejected_topics.add(topic)
                print(f"[REJECT] Explicit rejection detected: {topic}")
        
        if is_rejection:
            # Determine what topic was rejected based on the question category and other options
            rejected_topic = self._determine_rejected_topic(question, chosen_option)
            if rejected_topic:
                session.rejected_topics.add(rejected_topic)
                print(f"[REJECT] User rejected topic: {rejected_topic}")
                
                # Penalize courses associated with this rejected topic
                for course_name, course_traits in self.course_traits.items():
                    if rejected_topic in course_traits:
                        session.course_scores[course_name] -= 8  # Penalty for rejected topic
        
        # Extract trait from chosen option
        chosen_trait = chosen_option.get('trait_tag')
        option_text = chosen_option.get('option_text', '').lower()
        
        # Track all trait changes for this question (for reversal with "Previous" button)
        trait_changes = {}
        
        # Check if this is a "None" or "Not interested" option
        is_none_option = any(phrase in option_text for phrase in [
            'none', 'not interested', "don't want", 'prefer not',
            'none of these', 'not for me', "i don't"
        ])
        
        # Track which traits to update course scores for
        traits_to_boost = []
        
        if is_none_option:
            # For "None" options, don't add any traits - the user is rejecting this topic
            # The rejection penalty was already applied above
            # This prevents arbitrary traits from being added
            print(f"[NONE_OPTION] No traits added - user rejected this topic")
            chosen_trait = None
        elif chosen_trait:
            # Normal option - use the trait tag
            # Increase student's affinity for this trait
            current = session.trait_scores.get(chosen_trait, 0)
            session.trait_scores[chosen_trait] = current + 1.0
            trait_changes[chosen_trait] = 1.0
            traits_to_boost.append(chosen_trait)
            
            # Also add mapped traits (from our enhanced trait system)
            mapped_traits = EXPANDED_TRAIT_MAPPING.get(chosen_trait, [])
            for mapped_trait in mapped_traits:
                current = session.trait_scores.get(mapped_trait, 0)
                session.trait_scores[mapped_trait] = current + 0.5
                trait_changes[mapped_trait] = trait_changes.get(mapped_trait, 0) + 0.5
                traits_to_boost.append(mapped_trait)
        
        # Store the trait changes for this question (for reversal)
        session.answer_trait_changes[question_id] = trait_changes
        
        # Update course scores based on this answer - for all traits boosted
        for trait in traits_to_boost:
            self._update_course_scores(session, trait)
        
        # Calculate confidence
        session.confidence = self._calculate_confidence(session)
        
        # Get current top courses for preview (from ALL courses, not just active)
        sorted_courses = sorted(
            session.course_scores.items(),
            key=lambda x: x[1],
            reverse=True
        )
        
        # Show top 5 courses with their matched trait count
        top_courses = [
            {
                "course_name": name,
                "current_score": round(score, 1),
                "traits_matched": len(self.course_traits.get(name, set()) & 
                                    set(session.trait_scores.keys()))
            }
            for name, score in sorted_courses[:5]
        ]
        
        return {
            "status": "continue",
            "session_id": session_id,
            "round": session.round_number,
            "trait_recorded": chosen_trait,
            "courses_remaining": len(self.courses),  # All courses remain in consideration
            "confidence": round(session.confidence * 100, 1),
            "top_courses_preview": top_courses,
            "traits_discovered": len(session.trait_scores)
        }
    
    def _get_specialized_similarity(self, trait1: str, trait2: str) -> float:
        """Get similarity score between two traits (0-1)."""
        # Exact match
        if trait1 == trait2:
            return 1.0
        
        # Check specialized trait relationships first (more accurate for new system)
        if trait1 in SPECIALIZED_TRAIT_RELATIONSHIPS:
            if trait2 in SPECIALIZED_TRAIT_RELATIONSHIPS[trait1]:
                return SPECIALIZED_TRAIT_RELATIONSHIPS[trait1][trait2]
        
        if trait2 in SPECIALIZED_TRAIT_RELATIONSHIPS:
            if trait1 in SPECIALIZED_TRAIT_RELATIONSHIPS[trait2]:
                return SPECIALIZED_TRAIT_RELATIONSHIPS[trait2][trait1]
        
        # Fall back to old trait system for backward compatibility
        return get_trait_similarity(trait1, trait2)
    
    def _update_course_scores(self, session: AdaptiveSession, chosen_trait: str):
        """Boost course scores based on trait matches."""
        if not chosen_trait:
            return
        
        for course_name in list(session.active_courses):
            course_traits = self.course_traits.get(course_name, set())
            
            # Direct trait match - BIG BOOST (matches unique specialized trait)
            if chosen_trait in course_traits:
                session.course_scores[course_name] += 8.0  # Increased for specialized traits
            else:
                # Check for similar traits using our SPECIALIZED trait system
                best_similarity = 0
                for course_trait in course_traits:
                    sim = self._get_specialized_similarity(chosen_trait, course_trait)
                    best_similarity = max(best_similarity, sim)
                
                # Similarity-based score boost
                if best_similarity > 0.7:
                    session.course_scores[course_name] += 4.0
                elif best_similarity > 0.4:
                    session.course_scores[course_name] += 2.0
                elif best_similarity > 0.2:
                    session.course_scores[course_name] += 0.5
    
    def _calculate_confidence(self, session: AdaptiveSession) -> float:
        """Calculate recommendation confidence based on score separation."""
        if len(session.active_courses) == 0:
            return 1.0
        
        sorted_scores = sorted(session.course_scores.values(), reverse=True)
        
        if len(sorted_scores) < 2:
            return 0.5
        
        # Compare top 5 to the rest
        top_5_avg = sum(sorted_scores[:5]) / 5
        rest_avg = sum(sorted_scores[5:15]) / 10 if len(sorted_scores) > 5 else top_5_avg * 0.8
        
        if rest_avg == 0:
            return 1.0
        
        # Confidence based on gap between top and rest
        gap_ratio = (top_5_avg - rest_avg) / top_5_avg
        
        # Also factor in number of questions answered
        question_factor = min(session.round_number / session.min_questions, 1.0)
        
        confidence = gap_ratio * 0.7 + question_factor * 0.3
        return min(max(confidence, 0), 1)
    
    def _should_stop(self, session: AdaptiveSession) -> bool:
        """Determine if we should stop asking questions"""
        # Must ask minimum questions (use session's min_questions)
        if session.round_number < session.min_questions:
            return False
        
        # Stop at max questions (use session's max_questions)
        if session.round_number >= session.max_questions:
            return True
        
        # Stop if confidence is high enough
        if session.confidence >= self.CONFIDENCE_THRESHOLD:
            return True
        
        return False
    
    def _finalize_session(self, session: AdaptiveSession):
        """Build final course recommendations."""
        print(f"[OK_GREEN] FINALIZE SESSION CALLED - session_id: {session.session_id}")
        session.is_complete = True
        
        # Sort courses by score
        sorted_courses = sorted(
            session.course_scores.items(),
            key=lambda x: x[1],
            reverse=True
        )
        
        print(f"[OK_GREEN] Total courses scored: {len(sorted_courses)}")
        if sorted_courses:
            print(f"[OK_GREEN] Top 5 courses: {sorted_courses[:5]}")
        
        # Normalize scores to percentages
        top_score = sorted_courses[0][1] if sorted_courses else 1
        min_score = sorted_courses[-1][1] if sorted_courses else 0
        score_range = max(top_score - min_score, 0.001)  # Prevent division by zero
        
        recommendations = []
        for i, (course_name, raw_score) in enumerate(sorted_courses[:self.TOP_N_RECOMMENDATIONS]):
            course = self.courses.get(course_name, {})
            course_traits = self.course_traits.get(course_name, set())
            
            # Calculate match percentage (curved for realism)
            normalized = (raw_score - min_score) / score_range
            # Ensure normalized is a valid number
            if not isinstance(normalized, (int, float)) or normalized != normalized:  # NaN check
                normalized = 0.5
            normalized = max(0, min(1, normalized))  # Clamp to 0-1
            # Apply curve: 97% max, 55% min for top 5
            percentage = 55 + (normalized * 42)
            
            # Final safety check for percentage
            if not isinstance(percentage, (int, float)) or percentage != percentage:  # NaN check
                percentage = 75.0  # Default reasonable value
            percentage = max(55, min(97, percentage))  # Clamp to valid range
            
            # Find which traits matched
            matched_traits = list(course_traits & set(session.trait_scores.keys()))
            
            # Calculate profile bonus for display (shows if user's interests/skills helped)
            profile_bonus = 0
            if session.user_interests or session.user_skills:
                profile_bonus = self._calculate_profile_bonus(
                    session.user_interests, 
                    session.user_skills, 
                    course_traits
                )
            
            reasoning = self._generate_recommendation_reasoning(
                session, course_name, course, course_traits, 
                matched_traits, profile_bonus, raw_score
            )
            
            recommendations.append({
                "rank": i + 1,
                "course_name": course_name,
                "description": course.get('description', ''),
                "match_percentage": round(float(percentage), 1),
                "matched_traits": matched_traits[:5],  # Top 5 traits
                "minimum_gwa": course.get('minimum_gwa'),
                "recommended_strand": course.get('required_strand'),
                "profile_bonus_applied": profile_bonus > 0,
                "reasoning": reasoning  # Detailed explanation
            })
        
        session.final_recommendations = recommendations
        print(f"[OK_GREEN] Generated {len(recommendations)} recommendations")
        print(f"[OK_GREEN] Recommendation course names: {[r['course_name'] for r in recommendations]}")
        print(f"[OK] Session {session.session_id} complete after {session.round_number} questions")
    
    def _generate_recommendation_reasoning(self, session: AdaptiveSession, course_name: str,
                                           course: dict, course_traits: Set[str],
                                           matched_traits: List[str], profile_bonus: float,
                                           raw_score: float) -> str:
        """Generate explanation for why this course was recommended."""
        reasons = []
        
        # Trait matches from responses
        if matched_traits:
            trait_labels = self._get_trait_labels(matched_traits[:3])
            if len(matched_traits) >= 3:
                reasons.append(f"Your responses showed strong alignment with {trait_labels}")
            elif len(matched_traits) >= 1:
                reasons.append(f"You demonstrated interest in {trait_labels}")
        
        # Profile interests match
        profile_matches = []
        if session.user_interests:
            interests = [i.strip().lower() for i in session.user_interests.split(',') if i.strip()]
            course_name_lower = course_name.lower()
            course_desc_lower = course.get('description', '').lower()
            
            for interest in interests:
                interest_label = self._get_interest_label(interest)
                if interest_label and (interest in course_name_lower or 
                    any(t.lower() in course_desc_lower for t in self._get_interest_traits(interest))):
                    profile_matches.append(interest_label)
        
        if profile_matches:
            reasons.append(f"This aligns with your stated interests: {', '.join(profile_matches[:2])}")
        
        # Skills match
        skill_matches = []
        if session.user_skills:
            skills = [s.strip().lower() for s in session.user_skills.split(',') if s.strip()]
            for skill in skills:
                skill_label = self._get_skill_label(skill)
                if skill_label and profile_bonus > 0:
                    skill_matches.append(skill_label)
        
        if skill_matches and len(skill_matches) <= 2:
            reasons.append(f"Your skills in {', '.join(skill_matches[:2])} are valuable for this field")
        
        # Strand match
        required_strand = course.get('required_strand', '')
        if session.user_strand and required_strand:
            if session.user_strand.upper() == required_strand.upper():
                reasons.append(f"This is a natural progression from your {session.user_strand} strand")
            elif required_strand.upper() == "GAS":
                reasons.append("This course welcomes students from any strand background")
        
        # Career category bonus
        career_reason = self._get_career_reasoning(course_name, course_traits)
        if career_reason:
            reasons.append(career_reason)
        
        # Strong answer patterns
        strong_traits = [t for t, score in session.trait_scores.items() if score >= 2.0]
        strong_matching = [t for t in strong_traits if t in course_traits]
        if strong_matching:
            trait_label = self._get_trait_labels([strong_matching[0]])
            reasons.append(f"You consistently showed preference for {trait_label}-related activities")
        
        # Combine reasons into a coherent paragraph
        if not reasons:
            # Fallback reasoning
            return f"Based on your assessment responses, {course_name} appears to be a good match for your interests and aptitudes."
        
        # Join first 3 reasons
        reasoning_text = ". ".join(reasons[:3])
        if not reasoning_text.endswith('.'):
            reasoning_text += '.'
        
        return reasoning_text
    
    def _get_trait_labels(self, traits: List[str]) -> str:
        """Convert trait tags to readable labels."""
        TRAIT_LABELS = {
            "Patient-Care": "patient care and healthcare",
            "Medical-Lab": "medical laboratory and diagnostics",
            "Rehab-Therapy": "therapy and rehabilitation",
            "Software-Dev": "software development and programming",
            "Hardware-Systems": "computer hardware and systems",
            "Data-Analytics": "data analysis and statistics",
            "Cyber-Defense": "cybersecurity",
            "Digital-Media": "digital media and multimedia",
            "Civil-Build": "construction and infrastructure",
            "Mechanical-Design": "mechanical systems and design",
            "Electrical-Power": "electrical systems",
            "Industrial-Ops": "industrial operations",
            "Spatial-Design": "spatial design and architecture",
            "Finance-Acct": "finance and accounting",
            "Marketing-Sales": "marketing and sales",
            "Startup-Venture": "entrepreneurship and business",
            "Admin-Skill": "administration and organization",
            "Teaching-Ed": "teaching and education",
            "Visual-Design": "visual arts and design",
            "Creative-Skill": "creative and artistic expression",
            "Law-Enforce": "law enforcement and justice",
            "Community-Serve": "public service and community",
            "Maritime-Sea": "maritime and ocean industries",
            "Agri-Nature": "agriculture and environmental science",
            "Hospitality-Svc": "hospitality and tourism",
            "Lab-Research": "scientific research",
            "Field-Research": "field research and exploration",
            "People-Skill": "interpersonal communication",
            "Technical-Skill": "technical problem-solving",
        }
        labels = [TRAIT_LABELS.get(t, t.replace('-', ' ').lower()) for t in traits]
        if len(labels) == 1:
            return labels[0]
        elif len(labels) == 2:
            return f"{labels[0]} and {labels[1]}"
        else:
            return f"{', '.join(labels[:-1])}, and {labels[-1]}"
    
    def _get_interest_label(self, interest: str) -> str:
        """Map interest ID to display name."""
        INTEREST_LABELS = {
            "science": "Science & Research",
            "biology": "Biology",
            "chemistry": "Chemistry",
            "physics": "Physics",
            "environment": "Environmental Science",
            "programming": "Programming",
            "computer": "Computers & IT",
            "data": "Data Analytics",
            "ai": "AI & Machine Learning",
            "cybersecurity": "Cybersecurity",
            "engineering": "Engineering",
            "mechanical": "Mechanical Systems",
            "electrical": "Electronics",
            "civil": "Civil Engineering",
            "business": "Business",
            "finance": "Finance",
            "marketing": "Marketing",
            "accounting": "Accounting",
            "economics": "Economics",
            "art": "Arts & Design",
            "music": "Music",
            "film": "Film & Media",
            "writing": "Writing",
            "photography": "Photography",
            "medical": "Medicine",
            "nursing": "Nursing",
            "psychology": "Psychology",
            "education": "Education",
            "law": "Law",
            "politics": "Political Science",
            "social": "Social Work",
            "history": "History",
            "sports": "Sports",
            "tourism": "Tourism",
            "food": "Culinary Arts",
            "agriculture": "Agriculture",
        }
        return INTEREST_LABELS.get(interest.lower(), "")
    
    def _get_interest_traits(self, interest: str) -> List[str]:
        """Get keywords associated with an interest."""
        INTEREST_TRAITS = {
            "science": ["scientific", "research", "laboratory"],
            "programming": ["software", "coding", "development", "tech"],
            "business": ["business", "entrepreneurship", "management"],
            "medical": ["medical", "healthcare", "patient"],
            "nursing": ["nursing", "patient care", "healthcare"],
            "engineering": ["engineering", "technical", "mechanical"],
            "education": ["education", "teaching", "pedagogy"],
            "art": ["art", "design", "creative"],
        }
        return INTEREST_TRAITS.get(interest.lower(), [interest])
    
    def _get_skill_label(self, skill: str) -> str:
        """Map skill ID to display name."""
        SKILL_LABELS = {
            "programming_skill": "Programming",
            "data_analysis": "Data Analysis",
            "web_development": "Web Development",
            "graphic_design": "Graphic Design",
            "video_editing": "Video Editing",
            "math_skills": "Mathematics",
            "laboratory": "Laboratory Work",
            "technical_writing": "Technical Writing",
            "public_speaking": "Public Speaking",
            "writing_skill": "Writing",
            "presentation": "Presentation",
            "negotiation": "Negotiation",
            "foreign_language": "Foreign Languages",
            "leadership": "Leadership",
            "project_management": "Project Management",
            "team_management": "Team Management",
            "decision_making": "Decision Making",
            "planning": "Planning & Organization",
            "teamwork": "Teamwork",
            "empathy": "Empathy",
            "customer_service": "Customer Service",
            "mentoring": "Mentoring",
            "conflict_resolution": "Conflict Resolution",
            "critical_thinking": "Critical Thinking",
            "problem_solving": "Problem Solving",
            "research": "Research",
            "attention_detail": "Attention to Detail",
            "logical_reasoning": "Logical Reasoning",
            "creativity": "Creativity",
            "artistic": "Artistic Ability",
            "music_skill": "Musical Ability",
            "storytelling": "Storytelling",
            "design_thinking": "Design Thinking",
        }
        return SKILL_LABELS.get(skill.lower(), "")
    
    def _get_career_reasoning(self, course_name: str, course_traits: Set[str]) -> str:
        """Get career-focused blurb based on course traits."""
        course_lower = course_name.lower()
        
        if any(t in course_traits for t in ["Patient-Care", "Medical-Lab", "Rehab-Therapy"]):
            return "This career path offers opportunities to help others and make a direct impact on people's health and wellbeing"
        
        if any(t in course_traits for t in ["Software-Dev", "Hardware-Systems", "Data-Analytics"]):
            return "The tech industry offers excellent career growth, competitive salaries, and opportunities for innovation"
        
        if any(t in course_traits for t in ["Civil-Build", "Mechanical-Design", "Electrical-Power"]):
            return "Engineering careers are in high demand and offer the chance to build and create tangible solutions"
        
        if any(t in course_traits for t in ["Finance-Acct", "Marketing-Sales", "Startup-Venture"]):
            return "Business careers offer diverse paths from corporate roles to entrepreneurship opportunities"
        
        if any(t in course_traits for t in ["Teaching-Ed"]):
            return "Education careers allow you to shape future generations and make a lasting societal impact"
        
        if any(t in course_traits for t in ["Visual-Design", "Creative-Skill", "Digital-Media"]):
            return "Creative careers let you express yourself while building practical skills valued in many industries"
        
        if any(t in course_traits for t in ["Law-Enforce", "Community-Serve"]):
            return "Public service careers offer the satisfaction of serving your community and upholding justice"
        
        if any(t in course_traits for t in ["Maritime-Sea"]):
            return "Maritime careers offer unique opportunities for travel and are essential to global trade"
        
        if any(t in course_traits for t in ["Hospitality-Svc"]):
            return "Hospitality careers combine service excellence with opportunities in tourism and culinary arts"
        
        if any(t in course_traits for t in ["Agri-Nature", "Field-Research"]):
            return "Careers in agriculture and environmental science address crucial sustainability challenges"
        
        return ""
    
    def get_final_results(self, session_id: str) -> dict:
        """Retrieve final recommendations."""
        print(f"[BLUE] get_final_results called for session: {session_id}")
        session = self.sessions.get(session_id)
        if not session:
            print(f"[RED] Session not found: {session_id}")
            return {"error": "Session not found"}
        
        if not session.is_complete:
            print(f"[YELLOW] Session not complete, forcing finalize...")
            # Force finalize
            self._finalize_session(session)
        
        print(f"[BLUE] Returning {len(session.final_recommendations)} recommendations")
        return {
            "session_id": session_id,
            "is_complete": True,
            "total_questions_asked": session.round_number,
            "traits_discovered": len(session.trait_scores),
            "confidence": round(session.confidence * 100, 1),
            "recommendations": session.final_recommendations
        }
    
    def finish_early(self, session_id: str) -> dict:
        """End session early and return current recommendations."""
        session = self.sessions.get(session_id)
        if not session:
            return {"error": "Session not found"}
        
        if session.round_number < self.MIN_QUESTIONS:
            return {
                "error": f"Please answer at least {self.MIN_QUESTIONS} questions",
                "current_round": session.round_number,
                "minimum_required": self.MIN_QUESTIONS
            }
        
        self._finalize_session(session)
        return self.get_final_results(session_id)
    
    def go_to_previous_question(self, session_id: str) -> dict:
        """Go back to previous question and allow user to change answer."""
        session = self.sessions.get(session_id)
        if not session:
            return {"error": "Session not found"}
        
        if len(session.question_history) == 0:
            return {"error": "No previous questions"}
        
        # Get the last answered question
        previous_question_id = session.question_history.pop()
        
        # Remove from answered and excluded
        if previous_question_id in session.answered_questions:
            del session.answered_questions[previous_question_id]
        session.excluded_question_ids.discard(previous_question_id)
        
        # PROPERLY reverse all trait score changes from this answer
        if previous_question_id in session.answer_trait_changes:
            trait_changes = session.answer_trait_changes[previous_question_id]
            for trait, amount in trait_changes.items():
                if trait in session.trait_scores:
                    session.trait_scores[trait] -= amount
                    # Remove trait if score is 0 or negative
                    if session.trait_scores[trait] <= 0:
                        del session.trait_scores[trait]
            # Remove the stored changes
            del session.answer_trait_changes[previous_question_id]
            print(f"[PREVIOUS] Reversed trait changes: {trait_changes}")
        
        # Get the question to show again
        question = self.questions.get(previous_question_id)
        
        # Decrement round
        session.round_number -= 1
        
        # Recalculate course scores based on current trait scores
        self._recalculate_all_course_scores(session)
        
        # Recalculate confidence
        session.confidence = self._calculate_confidence(session)
        
        # Get top courses preview - only if there are traits discovered
        top_courses = []
        if len(session.trait_scores) > 0:
            sorted_courses = sorted(
                session.course_scores.items(),
                key=lambda x: x[1],
                reverse=True
            )
            top_courses = [
                {
                    "course_name": name,
                    "current_score": round(score, 1),
                    "traits_matched": len(self.course_traits.get(name, set()) & 
                                        set(session.trait_scores.keys()))
                }
                for name, score in sorted_courses[:5]
            ]
        
        print(f"[PREVIOUS] Went back to Q{previous_question_id}. Round: {session.round_number}, answers: {len(session.answered_questions)}, traits: {len(session.trait_scores)}")
        
        return {
            "status": "continue",
            "session_id": session_id,
            "round": session.round_number,
            "question": question,
            "confidence": round(session.confidence * 100, 1),
            "courses_remaining": len(self.courses),
            "traits_discovered": len(session.trait_scores),
            "top_courses_preview": top_courses,
            "message": "Go back to previous question. Select a different answer."
        }
    
    def _recalculate_all_course_scores(self, session: AdaptiveSession):
        """Recalculate all course scores from scratch based on current trait scores."""
        # Reset to base scores
        session.course_scores = {name: 50.0 for name in self.courses}
        
        # Apply trait-based scoring
        for trait, score in session.trait_scores.items():
            if trait in self.trait_to_courses:
                for course_name in self.trait_to_courses[trait]:
                    session.course_scores[course_name] = session.course_scores.get(course_name, 50.0) + (score * 2)


# Singleton instance (will be initialized by FastAPI)
adaptive_engine: Optional[AdaptiveAssessmentEngine] = None


def initialize_adaptive_engine(courses: List[dict], questions: List[dict]):
    """Initialize the global adaptive engine"""
    global adaptive_engine
    adaptive_engine = AdaptiveAssessmentEngine(courses, questions)
    return adaptive_engine


def get_adaptive_engine() -> Optional[AdaptiveAssessmentEngine]:
    """Get the global adaptive engine instance"""
    return adaptive_engine
