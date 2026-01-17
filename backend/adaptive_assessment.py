# adaptive_assessment.py - Akinator-Style Adaptive Question System
"""
================================================================================
ADAPTIVE ASSESSMENT ENGINE - Like Akinator but for Course Recommendations
================================================================================

This system asks questions ONE AT A TIME and intelligently selects the next 
question based on the student's previous answers to maximize information gain.

Key Concepts:
1. INFORMATION GAIN - Pick questions that best discriminate between courses
2. COURSE NARROWING - Each answer eliminates some courses, strengthens others
3. EARLY STOPPING - Can stop when confident enough about top recommendations
4. TRAIT ACCUMULATION - Build student profile incrementally

Algorithm:
1. Start with all 99 courses as candidates
2. For each round:
   a. Calculate which traits would most discriminate remaining courses
   b. Pick question that tests the most discriminating trait
   c. Update course scores based on answer
   d. Eliminate courses that fall too far behind
3. Stop when top 5 courses are significantly ahead OR max questions reached

================================================================================
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
    """Stores the state of an adaptive assessment session"""
    session_id: str
    user_id: int
    
    # User's SHS strand (for question prioritization)
    user_strand: str = None
    
    # Student's accumulated traits with strengths
    trait_scores: Dict[str, float] = field(default_factory=dict)
    
    # Course scores (higher = better match)
    course_scores: Dict[str, float] = field(default_factory=dict)
    
    # Questions already asked (question_id -> chosen_option)
    answered_questions: Dict[int, int] = field(default_factory=dict)
    
    # Questions to avoid (already asked or similar)
    excluded_question_ids: Set[int] = field(default_factory=set)
    
    # Current round number
    round_number: int = 0
    
    # Courses still in consideration (not eliminated)
    active_courses: Set[str] = field(default_factory=set)
    
    # Confidence level (0-1)
    confidence: float = 0.0
    
    # Is session complete?
    is_complete: bool = False
    
    # Final recommendations when complete
    final_recommendations: List[dict] = field(default_factory=list)


# Strand to prioritized traits mapping for question selection
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
    Akinator-style question selector for course recommendations.
    
    Instead of asking ALL questions upfront, it:
    1. Asks one question at a time
    2. Picks the BEST next question based on previous answers
    3. Narrows down courses dynamically
    4. Stops when confident enough
    """
    
    # Configuration
    MAX_QUESTIONS = 25  # Maximum questions to ask
    MIN_QUESTIONS = 10  # Minimum before allowing early stop
    CONFIDENCE_THRESHOLD = 0.75  # Stop when top courses are this far ahead
    TOP_N_RECOMMENDATIONS = 5  # Number of courses to recommend
    
    def __init__(self, courses: List[dict], questions: List[dict]):
        """
        Initialize with available courses and questions.
        
        Args:
            courses: List of course dicts with trait_tag field
            questions: List of question dicts with options and their trait_tags
        """
        self.courses = {c['course_name']: c for c in courses}
        self.questions = {q['question_id']: q for q in questions}
        self.sessions: Dict[str, AdaptiveSession] = {}
        
        # Pre-compute trait -> courses mapping for faster lookups
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
        
        print(f"🧠 Adaptive Engine initialized with {len(self.courses)} courses and {len(self.questions)} questions")
    
    def _parse_traits(self, trait_tag) -> Set[str]:
        """Parse trait_tag field into set of traits"""
        if not trait_tag:
            return set()
        if isinstance(trait_tag, list):
            return set(trait_tag)
        return set(t.strip() for t in str(trait_tag).split(',') if t.strip())
    
    def create_session(self, user_id: int, user_gwa: float = None, user_strand: str = None) -> str:
        """
        Start a new adaptive assessment session.
        
        Returns session_id for tracking.
        """
        import uuid
        session_id = str(uuid.uuid4())[:8]
        
        # Normalize strand
        normalized_strand = user_strand.upper() if user_strand else "GAS"
        if normalized_strand not in STRAND_PRIORITY_TRAITS:
            normalized_strand = "GAS"
        
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
        
        session = AdaptiveSession(
            session_id=session_id,
            user_id=user_id,
            user_strand=normalized_strand,  # Store strand for question selection
            course_scores=course_scores,
            active_courses=set(self.courses.keys())
        )
        
        self.sessions[session_id] = session
        print(f"📋 Created adaptive session {session_id} for user {user_id} (strand: {normalized_strand})")
        return session_id
    
    def get_next_question(self, session_id: str) -> Optional[dict]:
        """
        Select the BEST next question to ask based on current state.
        
        Uses information gain to pick the question that will most
        discriminate between the remaining courses.
        """
        session = self.sessions.get(session_id)
        if not session or session.is_complete:
            return None
        
        # Check if we should stop
        if self._should_stop(session):
            self._finalize_session(session)
            return None
        
        # Calculate which traits would give us most information
        trait_scores = self._calculate_trait_information_gain(session)
        
        # Find questions that test the highest-value traits
        best_question = None
        best_score = -1
        
        # Shuffle questions for variety when scores are similar
        question_ids = list(self.questions.keys())
        random.shuffle(question_ids)
        
        for qid in question_ids:
            if qid in session.excluded_question_ids:
                continue
            
            question = self.questions[qid]
            question_score = self._score_question(question, trait_scores, session)
            
            if question_score > best_score:
                best_score = question_score
                best_question = question
        
        if best_question:
            session.round_number += 1
            return {
                "session_id": session_id,
                "round": session.round_number,
                "total_max_rounds": self.MAX_QUESTIONS,
                "question": best_question,
                "courses_remaining": len(session.active_courses),
                "confidence": round(session.confidence * 100, 1),
                "can_finish_early": session.round_number >= self.MIN_QUESTIONS
            }
        
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
        """Score how valuable a question would be, with strand-based prioritization"""
        score = 0
        options = question.get('options', [])
        
        # Get strand priority traits
        strand_priority_traits = set(STRAND_PRIORITY_TRAITS.get(session.user_strand, []))
        
        for opt in options:
            trait = opt.get('trait_tag')
            if trait:
                # Direct trait value
                score += trait_values.get(trait, 0)
                
                # STRAND BONUS: Prioritize questions relevant to user's strand
                if trait in strand_priority_traits:
                    score += 0.5  # Significant bonus for strand-relevant traits
                
                # Also consider mapped traits from our trait system
                mapped_traits = EXPANDED_TRAIT_MAPPING.get(trait, [])
                for mapped_trait in mapped_traits:
                    score += trait_values.get(mapped_trait, 0) * 0.5
                    # Strand bonus for mapped traits too
                    if mapped_trait in strand_priority_traits:
                        score += 0.25
        
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
        """
        Process a student's answer and update course scores.
        
        Returns current state including narrowed courses.
        """
        session = self.sessions.get(session_id)
        if not session:
            return {"error": "Session not found"}
        
        if session.is_complete:
            return {
                "status": "complete",
                "recommendations": session.final_recommendations
            }
        
        question = self.questions.get(question_id)
        if not question:
            return {"error": "Question not found"}
        
        # Find the chosen option
        chosen_option = None
        for opt in question.get('options', []):
            if opt.get('option_id') == chosen_option_id:
                chosen_option = opt
                break
        
        if not chosen_option:
            return {"error": "Option not found"}
        
        # Record the answer
        session.answered_questions[question_id] = chosen_option_id
        session.excluded_question_ids.add(question_id)
        
        # Extract trait from chosen option
        chosen_trait = chosen_option.get('trait_tag')
        
        if chosen_trait:
            # Increase student's affinity for this trait
            current = session.trait_scores.get(chosen_trait, 0)
            session.trait_scores[chosen_trait] = current + 1.0
            
            # Also add mapped traits (from our enhanced trait system)
            mapped_traits = EXPANDED_TRAIT_MAPPING.get(chosen_trait, [])
            for mapped_trait in mapped_traits:
                current = session.trait_scores.get(mapped_trait, 0)
                session.trait_scores[mapped_trait] = current + 0.5
        
        # Update course scores based on this answer
        self._update_course_scores(session, chosen_trait)
        
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
        """Get similarity between two traits using SPECIALIZED relationships"""
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
        """Update course scores based on the chosen trait (using SPECIALIZED traits)"""
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
                
                # Apply boosts based on similarity level
                if best_similarity > 0.7:
                    session.course_scores[course_name] += 4.0  # Strong similarity
                elif best_similarity > 0.4:
                    session.course_scores[course_name] += 2.0  # Moderate similarity
                elif best_similarity > 0.2:
                    session.course_scores[course_name] += 0.5  # Slight similarity
                # NO PENALTY for non-matching traits - just don't boost
                # This prevents courses from being eliminated too quickly
        
        # REMOVED: Aggressive course elimination
        # We no longer remove courses that fall behind - let them compete naturally
        # The top courses will still rise to the top based on accumulated scores
    
    def _calculate_confidence(self, session: AdaptiveSession) -> float:
        """
        Calculate confidence that we have a good recommendation.
        
        High confidence when top courses are significantly ahead.
        """
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
        question_factor = min(session.round_number / self.MIN_QUESTIONS, 1.0)
        
        confidence = gap_ratio * 0.7 + question_factor * 0.3
        return min(max(confidence, 0), 1)
    
    def _should_stop(self, session: AdaptiveSession) -> bool:
        """Determine if we should stop asking questions"""
        # Must ask minimum questions
        if session.round_number < self.MIN_QUESTIONS:
            return False
        
        # Stop at max questions
        if session.round_number >= self.MAX_QUESTIONS:
            return True
        
        # Stop if confidence is high enough
        if session.confidence >= self.CONFIDENCE_THRESHOLD:
            return True
        
        # REMOVED: Stop if very few courses left
        # We no longer eliminate courses, so this check is not needed
        
        return False
    
    def _finalize_session(self, session: AdaptiveSession):
        """Create final recommendations when assessment is complete"""
        session.is_complete = True
        
        # Sort courses by score
        sorted_courses = sorted(
            session.course_scores.items(),
            key=lambda x: x[1],
            reverse=True
        )
        
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
            
            recommendations.append({
                "rank": i + 1,
                "course_name": course_name,
                "description": course.get('description', ''),
                "match_percentage": round(float(percentage), 1),
                "matched_traits": matched_traits[:5],  # Top 5 traits
                "minimum_gwa": course.get('minimum_gwa'),
                "recommended_strand": course.get('required_strand')
            })
        
        session.final_recommendations = recommendations
        print(f"✅ Session {session.session_id} complete after {session.round_number} questions")
    
    def get_final_results(self, session_id: str) -> dict:
        """Get final recommendations for a completed session"""
        session = self.sessions.get(session_id)
        if not session:
            return {"error": "Session not found"}
        
        if not session.is_complete:
            # Force finalize
            self._finalize_session(session)
        
        return {
            "session_id": session_id,
            "is_complete": True,
            "total_questions_asked": session.round_number,
            "traits_discovered": dict(session.trait_scores),
            "confidence": round(session.confidence * 100, 1),
            "recommendations": session.final_recommendations
        }
    
    def finish_early(self, session_id: str) -> dict:
        """Allow user to finish early and get current recommendations"""
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
