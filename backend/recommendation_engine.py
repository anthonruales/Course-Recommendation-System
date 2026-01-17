# recommendation_engine.py
# ================================================================================
# COLLEGE COURSE RECOMMENDATION SYSTEM
# Using Rule-Based Logic and Decision Tree Algorithm
# ================================================================================
# 
# This module implements the hybrid recommendation system as described in the thesis:
# 
# PHASE 1: RULE-BASED FILTERING
# - Uses explicit IF-THEN rules to filter out courses that don't meet student's
#   qualifications or stated preferences
# - Based on Rule-Based Expert Systems Theory (Giarratano & Riley, 2005)
# 
# PHASE 2: DECISION TREE CLASSIFICATION
# - Ranks and prioritizes courses based on identified patterns from student data
# - Based on Decision Tree Algorithm Theory (Quinlan, 1986)
# 
# ================================================================================

from typing import List, Dict, Any, Optional, Tuple, Set
from dataclasses import dataclass, field
from enum import Enum
import json


# ================================================================================
# PHASE 1: RULE-BASED FILTERING SYSTEM
# ================================================================================

class RuleType(Enum):
    """Types of rules in the rule-based system"""
    ELIGIBILITY = "eligibility"      # Hard rules - must pass to be eligible
    PREFERENCE = "preference"        # Soft rules - preferences that boost/reduce score
    EXCLUSION = "exclusion"          # Rules that exclude courses entirely


@dataclass
class Rule:
    """
    Represents a single IF-THEN rule in the rule-based system
    
    Structure:
    IF [conditions] THEN [action]
    
    Example:
    IF user_strand != required_strand AND required_strand != 'GAS' 
    THEN exclude_course OR penalize_score
    """
    rule_id: str
    rule_name: str
    rule_type: RuleType
    conditions: Dict[str, Any]
    action: str
    penalty_points: int = 0
    boost_points: int = 0
    explanation_template: str = ""
    priority: int = 1  # Higher priority rules are evaluated first


@dataclass
class RuleEvaluationResult:
    """Result of evaluating a single rule"""
    rule_id: str
    rule_name: str
    passed: bool
    action_taken: str
    explanation: str
    points_applied: int = 0


@dataclass
class FilteredCourse:
    """A course that passed the rule-based filtering phase"""
    course: Any  # Course model
    eligibility_score: float
    passed_rules: List[str]
    failed_rules: List[str]
    warnings: List[str]
    rule_explanations: List[str]
    is_eligible: bool
    penalty_total: int = 0
    boost_total: int = 0


class RuleBasedFilter:
    """
    PHASE 1: Rule-Based Filtering System
    
    Implements IF-THEN logic to filter courses based on:
    - Academic eligibility (GWA requirements)
    - Strand alignment (SHS track compatibility)
    - Trait matching (personality/interest alignment)
    - Career path preferences (direct course preferences)
    
    Reference: Rule-Based Expert Systems Theory (Giarratano & Riley, 2005)
    """
    
    def __init__(self):
        self.rules: List[Rule] = []
        self._initialize_rules()
    
    def _initialize_rules(self):
        """Initialize the rule base with predefined IF-THEN rules"""
        
        # ==================== ACADEMIC BONUS RULES (Soft Constraints - Bonus Points Only) ====================
        # NOTE: Academic info (GWA, Strand) are BONUS POINTS only, NOT hard constraints
        # All courses remain eligible regardless of user's strand or GWA
        # The PRIMARY focus is on TRAIT MATCHING from assessment answers
        
        # Rule A1: GWA Bonus/Penalty (Soft Constraint)
        self.rules.append(Rule(
            rule_id="A1",
            rule_name="GWA Academic Bonus",
            rule_type=RuleType.PREFERENCE,
            conditions={"check": "gwa_bonus"},
            action="adjust_score",
            boost_points=10,  # Bonus for meeting GWA
            penalty_points=5,  # Small penalty per point below (not disqualifying)
            explanation_template="IF user_gwa ({user_gwa}) meets course_minimum_gwa ({min_gwa}) THEN BONUS, else small penalty",
            priority=5  # Lower priority than trait matching
        ))
        
        # Rule A2: Strand Alignment Bonus (Soft Constraint)
        self.rules.append(Rule(
            rule_id="A2",
            rule_name="Strand Alignment Bonus",
            rule_type=RuleType.PREFERENCE,
            conditions={"check": "strand_bonus"},
            action="adjust_score",
            boost_points=8,  # Bonus for matching strand
            penalty_points=0,  # NO penalty for mismatch - all courses available
            explanation_template="IF user_strand ({user_strand}) matches required_strand ({req_strand}) THEN BONUS (no penalty for mismatch)",
            priority=4  # Lower priority than trait matching
        ))
        
        # ==================== TRAIT-BASED PREFERENCE RULES (PRIMARY FOCUS) ====================
        # These have HIGHEST PRIORITY - assessment answers determine recommendations
        
        # Rule P1: Primary Trait Match (HIGHEST PRIORITY)
        self.rules.append(Rule(
            rule_id="P1",
            rule_name="Primary Trait Alignment",
            rule_type=RuleType.PREFERENCE,
            conditions={"check": "primary_trait_match"},
            action="boost_score",
            boost_points=20,  # Increased - primary focus
            explanation_template="IF user_primary_trait ({primary_trait}) IN course_traits THEN BOOST +20 points",
            priority=10  # Highest priority
        ))
        
        # Rule P2: Multiple Trait Match (Synergy)
        self.rules.append(Rule(
            rule_id="P2",
            rule_name="Trait Synergy Bonus",
            rule_type=RuleType.PREFERENCE,
            conditions={"check": "trait_synergy", "min_matches": 3},
            action="boost_score",
            boost_points=15,  # Increased - trait matching is primary
            explanation_template="IF trait_matches >= 3 THEN BOOST +15 points (synergy bonus)",
            priority=9
        ))
        
        # Rule P3: Career Path Direct Match
        self.rules.append(Rule(
            rule_id="P3",
            rule_name="Career Path Preference",
            rule_type=RuleType.PREFERENCE,
            conditions={"check": "career_path_match"},
            action="boost_score",
            boost_points=25,  # High - user expressed interest
            explanation_template="IF user selected career path that maps to this course THEN BOOST +25 points",
            priority=10
        ))
        
        # Rule P6: Work Environment Preference
        self.rules.append(Rule(
            rule_id="P6",
            rule_name="Work Environment Match",
            rule_type=RuleType.PREFERENCE,
            conditions={"check": "work_environment_match"},
            action="boost_score",
            boost_points=8,
            explanation_template="IF user preferred work environment matches course setting THEN BOOST +8 points",
            priority=7
        ))
        
        # Rule P7: Learning Style Compatibility
        self.rules.append(Rule(
            rule_id="P7",
            rule_name="Learning Style Match",
            rule_type=RuleType.PREFERENCE,
            conditions={"check": "learning_style_match"},
            action="boost_score",
            boost_points=6,
            explanation_template="IF user learning style matches course teaching method THEN BOOST +6 points",
            priority=6
        ))
        
        # ==================== PENALTY RULES ====================
        
        # Rule N3: No Trait Match Penalty
        self.rules.append(Rule(
            rule_id="N3",
            rule_name="No Trait Match Penalty",
            rule_type=RuleType.PREFERENCE,
            conditions={"check": "no_trait_match"},
            action="penalize_score",
            penalty_points=15,
            explanation_template="IF no user traits match course traits THEN PENALIZE -15 points",
            priority=7
        ))
        
        # Sort rules by priority (higher priority first)
        self.rules.sort(key=lambda r: r.priority, reverse=True)
    
    def evaluate_rule(self, rule: Rule, context: Dict[str, Any]) -> RuleEvaluationResult:
        """
        Evaluate a single rule against the given context
        
        Args:
            rule: The rule to evaluate
            context: Dictionary containing user profile, course info, and derived data
        
        Returns:
            RuleEvaluationResult with pass/fail status and explanation
        """
        check_type = rule.conditions.get("check")
        
        # Extract context data
        user_gwa = context.get("user_gwa")
        user_strand = context.get("user_strand")
        course = context.get("course")
        user_traits = context.get("user_traits", [])
        primary_trait = context.get("primary_trait")
        career_path_courses = context.get("career_path_courses", [])
        user_work_env = context.get("user_work_environment", set())
        user_learning_style = context.get("user_learning_style", set())
        matched_traits = context.get("matched_traits", [])
        
        course_min_gwa = float(course.minimum_gwa) if course.minimum_gwa else 0
        course_strand = course.required_strand or ""
        course_traits = [t.strip() for t in (course.trait_tag or "").split(",")]
        
        passed = True
        action_taken = "none"
        points = 0
        explanation = ""
        
        # ==================== RULE EVALUATION LOGIC ====================
        
        if check_type == "gwa_bonus":
            # A1: GWA Bonus/Penalty (SOFT CONSTRAINT - NEVER MARKS INELIGIBLE)
            # All courses remain eligible regardless of GWA
            if user_gwa is not None and course_min_gwa > 0:
                if user_gwa >= course_min_gwa:
                    # User meets or exceeds requirement - give bonus
                    passed = True
                    action_taken = "boost_applied"
                    points = rule.boost_points
                    explanation = f"GWA Bonus: Your GWA ({user_gwa}) meets the course requirement ({course_min_gwa}) +{points} points"
                else:
                    # User below requirement - apply small penalty but STILL ELIGIBLE
                    gap = course_min_gwa - user_gwa
                    passed = True  # ALWAYS ELIGIBLE
                    action_taken = "penalty_applied"
                    points = -min(int(gap * rule.penalty_points), 15)  # Cap penalty at -15 points
                    explanation = f"GWA Note: Your GWA ({user_gwa}) is below requirement ({course_min_gwa}), but you can still pursue this course with extra effort. ({points} points)"
            else:
                passed = True
                action_taken = "skipped"
                explanation = "GWA check skipped (no requirement or user data)"
        
        elif check_type == "strand_bonus":
            # A2: Strand Alignment Bonus (SOFT CONSTRAINT - NEVER MARKS INELIGIBLE)
            # All courses remain eligible regardless of strand
            if user_strand and course_strand:
                # Define strand compatibility matrix for BONUS only (not restriction)
                best_strands = {
                    'STEM': ['STEM'],
                    'ABM': ['ABM'],
                    'HUMSS': ['HUMSS'],
                    'GAS': ['GAS'],
                    'TVL': ['TVL'],
                    'Sports': ['Sports'],
                }
                compatible_strands = {
                    'STEM': ['GAS', 'TVL'],
                    'ABM': ['GAS', 'HUMSS'],
                    'HUMSS': ['GAS', 'ABM'],
                    'GAS': ['STEM', 'ABM', 'HUMSS', 'TVL', 'Sports'],
                    'TVL': ['GAS', 'STEM'],
                    'Sports': ['GAS', 'HUMSS'],
                }
                
                user_best = best_strands.get(user_strand, [user_strand])
                user_compatible = compatible_strands.get(user_strand, [])
                
                if course_strand in user_best or user_strand == course_strand:
                    # Perfect match - give full bonus
                    passed = True
                    action_taken = "boost_applied"
                    points = rule.boost_points
                    explanation = f"Strand Bonus: Your strand ({user_strand}) perfectly matches the course +{points} points"
                elif course_strand in user_compatible:
                    # Compatible - give partial bonus
                    passed = True
                    action_taken = "boost_applied"
                    points = rule.boost_points // 2
                    explanation = f"Strand Bonus: Your strand ({user_strand}) is compatible with {course_strand} courses +{points} points"
                else:
                    # Different strand - NO PENALTY, just no bonus
                    # User can still take ANY course regardless of strand!
                    passed = True
                    action_taken = "no_penalty"
                    points = 0
                    explanation = f"Your strand ({user_strand}) differs from {course_strand}, but you can still pursue this course based on your interests!"
            else:
                passed = True
                action_taken = "skipped"
                explanation = "Strand check skipped (no requirement or user data)"
        
        elif check_type == "gwa_requirement":
            # DEPRECATED - Redirect to gwa_bonus for backward compatibility
            passed = True
            action_taken = "skipped"
            explanation = "GWA is now a bonus factor only"
        
        elif check_type == "strand_alignment":
            # DEPRECATED - Redirect to strand_bonus for backward compatibility
            passed = True
            action_taken = "skipped"
            explanation = "Strand is now a bonus factor only"
        
        elif check_type == "primary_trait_match":
            # P1: Check if primary trait matches
            if primary_trait and primary_trait in course_traits:
                passed = True
                action_taken = "boost_applied"
                points = rule.boost_points
                explanation = f"Primary trait '{primary_trait}' matches course requirements"
            else:
                passed = True
                action_taken = "no_boost"
                explanation = f"Primary trait '{primary_trait}' not in course traits"
        
        elif check_type == "trait_synergy":
            # P2: Check for multiple trait matches
            min_matches = rule.conditions.get("min_matches", 3)
            if len(matched_traits) >= min_matches:
                passed = True
                action_taken = "boost_applied"
                points = rule.boost_points
                explanation = f"Trait synergy: {len(matched_traits)} traits match ({', '.join(matched_traits[:3])}...)"
            else:
                passed = True
                action_taken = "no_boost"
                explanation = f"Trait synergy not met: only {len(matched_traits)} matches (need {min_matches})"
        
        elif check_type == "career_path_match":
            # P3: Check if course is in user's career path preference
            if course.course_name in career_path_courses:
                passed = True
                action_taken = "boost_applied"
                points = rule.boost_points
                explanation = f"Course matches user's stated career path preference"
            else:
                passed = True
                action_taken = "no_boost"
                explanation = "Course not in user's career path preferences"
        
        elif check_type == "gwa_excellence":
            # DEPRECATED - GWA bonus handled by A1 rule now
            passed = True
            action_taken = "skipped"
            explanation = "GWA excellence now handled by GWA Academic Bonus rule"
        
        elif check_type == "strand_perfect_match":
            # DEPRECATED - Strand bonus handled by A2 rule now
            passed = True
            action_taken = "skipped"
            explanation = "Strand matching now handled by Strand Alignment Bonus rule"
        
        elif check_type == "work_environment_match":
            # P6: Work environment preference
            work_env_traits = {
                'office': ['Office-based', 'Remote-friendly'],
                'field': ['Field-work', 'Outdoor-enthusiast'],
                'clinical': ['Clinical-setting', 'Patient-focused'],
                'laboratory': ['Laboratory', 'Research-oriented'],
                'studio': ['Studio-work', 'Creative-expression'],
            }
            
            env_match = False
            for env in user_work_env:
                env_traits = work_env_traits.get(env, [])
                if any(t in course_traits for t in env_traits):
                    env_match = True
                    break
            
            if env_match:
                passed = True
                action_taken = "boost_applied"
                points = rule.boost_points
                explanation = "Work environment preference matches course setting"
            else:
                passed = True
                action_taken = "no_boost"
                explanation = "Work environment preference not matched"
        
        elif check_type == "learning_style_match":
            # P7: Learning style compatibility
            learning_traits = {
                'visual': ['Visual-learner', 'Aesthetic-sense', 'Digital-art'],
                'hands_on': ['Hands-on', 'Practical', 'Field-work'],
                'theoretical': ['Theoretical', 'Research-oriented', 'Abstract-thinking'],
                'social': ['Collaborative', 'Team-centric', 'Extroverted'],
                'independent': ['Independent', 'Introverted', 'Self-directed'],
            }
            
            style_match = False
            for style in user_learning_style:
                style_traits = learning_traits.get(style, [])
                if any(t in course_traits for t in style_traits):
                    style_match = True
                    break
            
            if style_match:
                passed = True
                action_taken = "boost_applied"
                points = rule.boost_points
                explanation = "Learning style compatible with course teaching approach"
            else:
                passed = True
                action_taken = "no_boost"
                explanation = "Learning style preference not matched"
        
        elif check_type == "gwa_shortfall":
            # DEPRECATED - GWA penalty now handled by A1 rule
            passed = True
            action_taken = "skipped"
            explanation = "GWA shortfall now handled by GWA Academic Bonus rule"
        
        elif check_type == "strand_mismatch":
            # DEPRECATED - No strand penalties anymore - all courses available
            passed = True
            action_taken = "skipped"
            explanation = "Strand mismatch removed - all courses available regardless of strand"
        
        elif check_type == "no_trait_match":
            # N3: Penalty for no trait matches
            if len(matched_traits) == 0:
                passed = True
                action_taken = "penalty_applied"
                points = -rule.penalty_points
                explanation = f"No trait match penalty: -{rule.penalty_points} points"
            else:
                passed = True
                action_taken = "no_penalty"
                explanation = f"Has {len(matched_traits)} trait matches"
        
        else:
            passed = True
            action_taken = "unknown_rule"
            explanation = f"Unknown rule check: {check_type}"
        
        return RuleEvaluationResult(
            rule_id=rule.rule_id,
            rule_name=rule.rule_name,
            passed=passed,
            action_taken=action_taken,
            explanation=explanation,
            points_applied=points
        )
    
    def filter_courses(
        self,
        courses: List[Any],
        user_profile: Dict[str, Any],
        trait_scores: Dict[str, float],
        career_path_courses: List[str] = None
    ) -> List[FilteredCourse]:
        """
        PHASE 1: Apply rule-based filtering to all courses
        
        Args:
            courses: List of all courses from database
            user_profile: Dictionary with user's academic info (gwa, strand, etc.)
            trait_scores: Dictionary of trait -> score from assessment
            career_path_courses: List of course names from career path selections
        
        Returns:
            List of FilteredCourse objects that passed filtering
        """
        filtered_courses = []
        
        # Prepare user context
        user_gwa = user_profile.get("gwa")
        user_strand = user_profile.get("strand")
        
        # Get top traits for matching
        sorted_traits = sorted(trait_scores.items(), key=lambda x: x[1], reverse=True)
        top_traits = [t for t, _ in sorted_traits[:7]]
        primary_trait = sorted_traits[0][0] if sorted_traits else None
        
        # Determine user's learning style and work environment preferences from traits
        user_learning_style = self._determine_learning_style(top_traits)
        user_work_env = self._determine_work_environment(top_traits)
        
        for course in courses:
            # Calculate matched traits for this course
            course_traits = [t.strip() for t in (course.trait_tag or "").split(",")]
            matched_traits = [t for t in top_traits if t in course_traits]
            
            # Build context for rule evaluation
            context = {
                "user_gwa": user_gwa,
                "user_strand": user_strand,
                "course": course,
                "user_traits": top_traits,
                "primary_trait": primary_trait,
                "career_path_courses": career_path_courses or [],
                "user_work_environment": user_work_env,
                "user_learning_style": user_learning_style,
                "matched_traits": matched_traits,
            }
            
            # Evaluate all rules
            passed_rules = []
            failed_rules = []
            warnings = []
            explanations = []
            total_boost = 0
            total_penalty = 0
            is_eligible = True
            
            for rule in self.rules:
                result = self.evaluate_rule(rule, context)
                
                if result.passed:
                    if result.action_taken == "boost_applied":
                        total_boost += result.points_applied
                        passed_rules.append(f"{rule.rule_id}: {rule.rule_name}")
                        explanations.append(f"✓ {rule.rule_name}: {result.explanation}")
                    elif result.action_taken == "penalty_applied":
                        total_penalty += abs(result.points_applied)
                        warnings.append(f"{rule.rule_id}: {result.explanation}")
                        explanations.append(f"⚠ {rule.rule_name}: {result.explanation}")
                    elif result.action_taken in ["passed", "no_boost", "no_penalty"]:
                        pass  # Normal processing
                    elif result.action_taken == "eligible_with_warning":
                        warnings.append(result.explanation)
                        explanations.append(f"⚠ {rule.rule_name}: {result.explanation}")
                    elif result.action_taken == "eligible_with_penalty":
                        warnings.append(result.explanation)
                        explanations.append(f"⚠ {rule.rule_name}: {result.explanation}")
                else:
                    # Rule failed - check if it's an eligibility rule
                    if rule.rule_type == RuleType.ELIGIBILITY:
                        is_eligible = False
                        failed_rules.append(f"{rule.rule_id}: {rule.rule_name}")
                        explanations.append(f"✗ {rule.rule_name}: {result.explanation}")
                    else:
                        failed_rules.append(f"{rule.rule_id}: {rule.rule_name}")
                        explanations.append(f"⚠ {rule.rule_name}: {result.explanation}")
            
            # Calculate eligibility score
            base_score = len(matched_traits) * 10  # 10 points per matched trait
            eligibility_score = base_score + total_boost - total_penalty
            
            filtered_courses.append(FilteredCourse(
                course=course,
                eligibility_score=eligibility_score,
                passed_rules=passed_rules,
                failed_rules=failed_rules,
                warnings=warnings,
                rule_explanations=explanations,
                is_eligible=is_eligible,
                penalty_total=total_penalty,
                boost_total=total_boost
            ))
        
        # Sort by eligibility score (descending)
        filtered_courses.sort(key=lambda x: (x.is_eligible, x.eligibility_score), reverse=True)
        
        return filtered_courses
    
    def _determine_learning_style(self, traits: List[str]) -> Set[str]:
        """Determine user's learning style from their traits"""
        learning_styles = set()
        
        style_mapping = {
            'visual': ['Visual-learner', 'Aesthetic-sense', 'Digital-art', 'Spatial-thinking'],
            'hands_on': ['Hands-on', 'Practical', 'Field-work', 'Active', 'Laboratory'],
            'theoretical': ['Theoretical', 'Research-oriented', 'Abstract-thinking', 'Analytical'],
            'social': ['Collaborative', 'Team-centric', 'Extroverted', 'Social'],
            'independent': ['Independent', 'Introverted', 'Contemplative', 'Self-directed'],
        }
        
        for style, style_traits in style_mapping.items():
            matches = [t for t in traits if t in style_traits]
            if len(matches) >= 2:
                learning_styles.add(style)
            elif len(matches) >= 1:
                learning_styles.add(style)  # Partial match still counts
        
        return learning_styles
    
    def _determine_work_environment(self, traits: List[str]) -> Set[str]:
        """Determine user's preferred work environment from their traits"""
        work_envs = set()
        
        env_mapping = {
            'office': ['Office-based', 'Remote-friendly', 'Organized'],
            'field': ['Field-work', 'Outdoor-enthusiast', 'Adventurous', 'Active'],
            'clinical': ['Clinical-setting', 'Patient-focused', 'Helping-others', 'Empathetic'],
            'laboratory': ['Laboratory', 'Research-oriented', 'Detail-focused', 'Scientific-thinking'],
            'studio': ['Studio-work', 'Creative-expression', 'Artistic-passion', 'Visual-learner'],
        }
        
        for env, env_traits in env_mapping.items():
            matches = [t for t in traits if t in env_traits]
            if len(matches) >= 2:
                work_envs.add(env)
        
        return work_envs


# ================================================================================
# PHASE 2: DECISION TREE CLASSIFICATION
# ================================================================================

class DecisionNodeType(Enum):
    """Types of nodes in the decision tree"""
    ROOT = "root"
    INTERNAL = "internal"
    LEAF = "leaf"


@dataclass
class DecisionNode:
    """
    A node in the decision tree
    
    Based on Decision Tree Algorithm Theory (Quinlan, 1986)
    Each node represents a decision point based on an attribute
    """
    node_id: str
    node_type: DecisionNodeType
    attribute: str  # The attribute being tested (e.g., "primary_trait", "gwa_level")
    threshold: Any = None  # For numerical attributes
    children: Dict[str, 'DecisionNode'] = field(default_factory=dict)
    classification: str = None  # For leaf nodes - the course category/recommendation
    confidence: float = 0.0  # Confidence of this classification
    score_modifier: int = 0  # Additional points to add/subtract


class DecisionTreeClassifier:
    """
    PHASE 2: Decision Tree Classification System
    
    Analyzes filtered courses and ranks them based on hierarchical decision paths.
    The tree structure represents learned patterns from student data.
    
    Reference: Decision Tree Algorithm Theory (Quinlan, 1986)
    """
    
    def __init__(self):
        self.root = None
        self._build_decision_tree()
    
    def _build_decision_tree(self):
        """
        Build the decision tree structure
        
        The tree makes decisions based on:
        1. Primary trait category (Helping, Problem-solving, Creative, Leading)
        2. Academic strength (High, Medium, Low GWA)
        3. Work preference (Office, Field, Clinical, etc.)
        4. Social orientation (Extrovert vs Introvert)
        """
        
        # ROOT NODE: Split by primary trait category
        self.root = DecisionNode(
            node_id="root",
            node_type=DecisionNodeType.ROOT,
            attribute="trait_category"
        )
        
        # ==================== HELPING-OTHERS BRANCH ====================
        helping_node = DecisionNode(
            node_id="helping",
            node_type=DecisionNodeType.INTERNAL,
            attribute="work_setting"
        )
        
        # Helping + Clinical Setting
        helping_clinical = DecisionNode(
            node_id="helping_clinical",
            node_type=DecisionNodeType.INTERNAL,
            attribute="gwa_level"
        )
        helping_clinical.children["high"] = DecisionNode(
            node_id="helping_clinical_high",
            node_type=DecisionNodeType.LEAF,
            attribute=None,
            classification="healthcare_professional",
            confidence=0.9,
            score_modifier=25
        )
        helping_clinical.children["medium"] = DecisionNode(
            node_id="helping_clinical_medium",
            node_type=DecisionNodeType.LEAF,
            attribute=None,
            classification="healthcare_allied",
            confidence=0.85,
            score_modifier=20
        )
        helping_clinical.children["low"] = DecisionNode(
            node_id="helping_clinical_low",
            node_type=DecisionNodeType.LEAF,
            attribute=None,
            classification="healthcare_support",
            confidence=0.75,
            score_modifier=15
        )
        
        # Helping + Office Setting
        helping_office = DecisionNode(
            node_id="helping_office",
            node_type=DecisionNodeType.INTERNAL,
            attribute="social_orientation"
        )
        helping_office.children["extrovert"] = DecisionNode(
            node_id="helping_office_extrovert",
            node_type=DecisionNodeType.LEAF,
            attribute=None,
            classification="education_social",
            confidence=0.85,
            score_modifier=20
        )
        helping_office.children["introvert"] = DecisionNode(
            node_id="helping_office_introvert",
            node_type=DecisionNodeType.LEAF,
            attribute=None,
            classification="counseling_support",
            confidence=0.8,
            score_modifier=18
        )
        helping_office.children["balanced"] = DecisionNode(
            node_id="helping_office_balanced",
            node_type=DecisionNodeType.LEAF,
            attribute=None,
            classification="public_service",
            confidence=0.8,
            score_modifier=18
        )
        
        # Helping + Field Setting
        helping_field = DecisionNode(
            node_id="helping_field",
            node_type=DecisionNodeType.LEAF,
            attribute=None,
            classification="community_service",
            confidence=0.85,
            score_modifier=20
        )
        
        helping_node.children["clinical"] = helping_clinical
        helping_node.children["office"] = helping_office
        helping_node.children["field"] = helping_field
        helping_node.children["default"] = helping_office
        
        # ==================== PROBLEM-SOLVING BRANCH ====================
        problem_node = DecisionNode(
            node_id="problem_solving",
            node_type=DecisionNodeType.INTERNAL,
            attribute="analytical_type"
        )
        
        # Problem-solving + Technical
        problem_technical = DecisionNode(
            node_id="problem_technical",
            node_type=DecisionNodeType.INTERNAL,
            attribute="gwa_level"
        )
        problem_technical.children["high"] = DecisionNode(
            node_id="problem_technical_high",
            node_type=DecisionNodeType.LEAF,
            attribute=None,
            classification="engineering_cs",
            confidence=0.9,
            score_modifier=25
        )
        problem_technical.children["medium"] = DecisionNode(
            node_id="problem_technical_medium",
            node_type=DecisionNodeType.LEAF,
            attribute=None,
            classification="it_technology",
            confidence=0.85,
            score_modifier=20
        )
        problem_technical.children["low"] = DecisionNode(
            node_id="problem_technical_low",
            node_type=DecisionNodeType.LEAF,
            attribute=None,
            classification="tech_vocational",
            confidence=0.75,
            score_modifier=15
        )
        
        # Problem-solving + Business
        problem_business = DecisionNode(
            node_id="problem_business",
            node_type=DecisionNodeType.INTERNAL,
            attribute="leadership_tendency"
        )
        problem_business.children["high"] = DecisionNode(
            node_id="problem_business_leader",
            node_type=DecisionNodeType.LEAF,
            attribute=None,
            classification="business_management",
            confidence=0.85,
            score_modifier=22
        )
        problem_business.children["low"] = DecisionNode(
            node_id="problem_business_analyst",
            node_type=DecisionNodeType.LEAF,
            attribute=None,
            classification="business_analytics",
            confidence=0.85,
            score_modifier=20
        )
        problem_business.children["medium"] = DecisionNode(
            node_id="problem_business_medium",
            node_type=DecisionNodeType.LEAF,
            attribute=None,
            classification="business_general",
            confidence=0.8,
            score_modifier=18
        )
        
        # Problem-solving + Research
        problem_research = DecisionNode(
            node_id="problem_research",
            node_type=DecisionNodeType.LEAF,
            attribute=None,
            classification="science_research",
            confidence=0.85,
            score_modifier=22
        )
        
        problem_node.children["technical"] = problem_technical
        problem_node.children["business"] = problem_business
        problem_node.children["research"] = problem_research
        problem_node.children["default"] = problem_technical
        
        # ==================== CREATIVE BRANCH ====================
        creative_node = DecisionNode(
            node_id="creative",
            node_type=DecisionNodeType.INTERNAL,
            attribute="creative_type"
        )
        
        # Creative + Visual
        creative_visual = DecisionNode(
            node_id="creative_visual",
            node_type=DecisionNodeType.INTERNAL,
            attribute="tech_affinity"
        )
        creative_visual.children["high"] = DecisionNode(
            node_id="creative_visual_tech",
            node_type=DecisionNodeType.LEAF,
            attribute=None,
            classification="digital_media",
            confidence=0.9,
            score_modifier=25
        )
        creative_visual.children["low"] = DecisionNode(
            node_id="creative_visual_traditional",
            node_type=DecisionNodeType.LEAF,
            attribute=None,
            classification="fine_arts",
            confidence=0.85,
            score_modifier=20
        )
        creative_visual.children["medium"] = DecisionNode(
            node_id="creative_visual_mixed",
            node_type=DecisionNodeType.LEAF,
            attribute=None,
            classification="design_arts",
            confidence=0.85,
            score_modifier=22
        )
        
        # Creative + Performing
        creative_performing = DecisionNode(
            node_id="creative_performing",
            node_type=DecisionNodeType.LEAF,
            attribute=None,
            classification="performing_arts",
            confidence=0.85,
            score_modifier=20
        )
        
        # Creative + Writing/Communication
        creative_writing = DecisionNode(
            node_id="creative_writing",
            node_type=DecisionNodeType.LEAF,
            attribute=None,
            classification="communication_media",
            confidence=0.85,
            score_modifier=20
        )
        
        creative_node.children["visual"] = creative_visual
        creative_node.children["performing"] = creative_performing
        creative_node.children["writing"] = creative_writing
        creative_node.children["default"] = creative_visual
        
        # ==================== LEADING BRANCH ====================
        leading_node = DecisionNode(
            node_id="leading",
            node_type=DecisionNodeType.INTERNAL,
            attribute="domain_interest"
        )
        
        # Leading + Business
        leading_business = DecisionNode(
            node_id="leading_business",
            node_type=DecisionNodeType.LEAF,
            attribute=None,
            classification="business_leadership",
            confidence=0.85,
            score_modifier=22
        )
        
        # Leading + Public Service
        leading_public = DecisionNode(
            node_id="leading_public",
            node_type=DecisionNodeType.LEAF,
            attribute=None,
            classification="public_administration",
            confidence=0.85,
            score_modifier=20
        )
        
        # Leading + Technical
        leading_technical = DecisionNode(
            node_id="leading_technical",
            node_type=DecisionNodeType.LEAF,
            attribute=None,
            classification="engineering_management",
            confidence=0.85,
            score_modifier=22
        )
        
        leading_node.children["business"] = leading_business
        leading_node.children["public"] = leading_public
        leading_node.children["technical"] = leading_technical
        leading_node.children["default"] = leading_business
        
        # Attach branches to root
        self.root.children["helping"] = helping_node
        self.root.children["problem_solving"] = problem_node
        self.root.children["creative"] = creative_node
        self.root.children["leading"] = leading_node
        self.root.children["default"] = problem_node  # Default to problem-solving
    
    def classify(self, user_profile: Dict[str, Any]) -> Tuple[str, float, int, List[str]]:
        """
        Traverse the decision tree to classify the user
        
        Args:
            user_profile: Dictionary with user attributes
        
        Returns:
            Tuple of (classification, confidence, score_modifier, decision_path)
        """
        current_node = self.root
        decision_path = []
        
        while current_node.node_type != DecisionNodeType.LEAF:
            attribute = current_node.attribute
            value = self._get_attribute_value(attribute, user_profile)
            decision_path.append(f"{attribute}={value}")
            
            if value in current_node.children:
                current_node = current_node.children[value]
            elif "default" in current_node.children:
                current_node = current_node.children["default"]
            else:
                # If no matching child, return the first child
                current_node = list(current_node.children.values())[0]
        
        return (
            current_node.classification,
            current_node.confidence,
            current_node.score_modifier,
            decision_path
        )
    
    def _get_attribute_value(self, attribute: str, user_profile: Dict[str, Any]) -> str:
        """Get the value of an attribute for decision making"""
        
        if attribute == "trait_category":
            primary_trait = user_profile.get("primary_trait", "")
            return self._categorize_trait(primary_trait)
        
        elif attribute == "work_setting":
            work_envs = user_profile.get("work_environments", set())
            if "clinical" in work_envs:
                return "clinical"
            elif "field" in work_envs:
                return "field"
            else:
                return "office"
        
        elif attribute == "gwa_level":
            gwa = user_profile.get("gwa", 85)
            if gwa >= 90:
                return "high"
            elif gwa >= 85:
                return "medium"
            else:
                return "low"
        
        elif attribute == "social_orientation":
            traits = user_profile.get("top_traits", [])
            extrovert_traits = ["Extroverted", "Social", "Collaborative", "Team-centric"]
            introvert_traits = ["Introverted", "Independent", "Contemplative"]
            
            ext_count = sum(1 for t in traits if t in extrovert_traits)
            int_count = sum(1 for t in traits if t in introvert_traits)
            
            if ext_count > int_count:
                return "extrovert"
            elif int_count > ext_count:
                return "introvert"
            else:
                return "balanced"
        
        elif attribute == "analytical_type":
            traits = user_profile.get("top_traits", [])
            tech_traits = ["Logical", "Tech-savvy", "Algorithm-focused", "Hands-on"]
            business_traits = ["Strategic", "Business-minded", "Leadership"]
            research_traits = ["Research-oriented", "Theoretical", "Scientific-thinking"]
            
            tech_count = sum(1 for t in traits if t in tech_traits)
            bus_count = sum(1 for t in traits if t in business_traits)
            res_count = sum(1 for t in traits if t in research_traits)
            
            if tech_count >= bus_count and tech_count >= res_count:
                return "technical"
            elif bus_count >= res_count:
                return "business"
            else:
                return "research"
        
        elif attribute == "creative_type":
            traits = user_profile.get("top_traits", [])
            visual_traits = ["Visual-learner", "Digital-art", "Aesthetic-sense"]
            performing_traits = ["Performative", "Expressive", "Storytelling"]
            writing_traits = ["Articulate", "Media-savvy", "Investigative"]
            
            vis_count = sum(1 for t in traits if t in visual_traits)
            perf_count = sum(1 for t in traits if t in performing_traits)
            writ_count = sum(1 for t in traits if t in writing_traits)
            
            if vis_count >= perf_count and vis_count >= writ_count:
                return "visual"
            elif perf_count >= writ_count:
                return "performing"
            else:
                return "writing"
        
        elif attribute == "tech_affinity":
            traits = user_profile.get("top_traits", [])
            tech_traits = ["Tech-savvy", "Digital-art", "Remote-friendly", "Innovative"]
            tech_count = sum(1 for t in traits if t in tech_traits)
            
            if tech_count >= 2:
                return "high"
            elif tech_count >= 1:
                return "medium"
            else:
                return "low"
        
        elif attribute == "leadership_tendency":
            traits = user_profile.get("top_traits", [])
            leader_traits = ["Leading-teams", "Leadership", "Big-picture", "Strategic"]
            leader_count = sum(1 for t in traits if t in leader_traits)
            
            if leader_count >= 2:
                return "high"
            elif leader_count >= 1:
                return "medium"
            else:
                return "low"
        
        elif attribute == "domain_interest":
            traits = user_profile.get("top_traits", [])
            business_traits = ["Business-minded", "Strategic", "Entrepreneurial"]
            public_traits = ["Civic-minded", "Public-service", "Advocacy"]
            tech_traits = ["Technical", "Engineering", "Problem-solving"]
            
            bus_count = sum(1 for t in traits if t in business_traits)
            pub_count = sum(1 for t in traits if t in public_traits)
            tech_count = sum(1 for t in traits if t in tech_traits)
            
            if bus_count >= pub_count and bus_count >= tech_count:
                return "business"
            elif pub_count >= tech_count:
                return "public"
            else:
                return "technical"
        
        return "default"
    
    def _categorize_trait(self, trait: str) -> str:
        """Categorize a trait into one of the main categories"""
        
        helping_traits = [
            "Helping-others", "Empathetic", "Compassionate", "Patient-focused",
            "Service-oriented", "Nurturing", "Mentoring", "Collaborative"
        ]
        
        problem_traits = [
            "Problem-solving", "Analytical", "Logical", "Research-oriented",
            "Detail-focused", "Methodical", "Systematic", "Investigative"
        ]
        
        creative_traits = [
            "Creative-expression", "Innovative", "Artistic-passion", "Visual-learner",
            "Aesthetic-sense", "Expressive", "Storytelling", "Digital-art"
        ]
        
        leading_traits = [
            "Leading-teams", "Leadership", "Big-picture", "Strategic",
            "Ambitious", "Confident", "Extroverted", "Persuasive"
        ]
        
        if trait in helping_traits:
            return "helping"
        elif trait in problem_traits:
            return "problem_solving"
        elif trait in creative_traits:
            return "creative"
        elif trait in leading_traits:
            return "leading"
        else:
            return "problem_solving"  # Default


# ================================================================================
# COURSE CATEGORY MAPPING
# ================================================================================

# Maps decision tree classifications to course categories
CLASSIFICATION_TO_COURSES = {
    "healthcare_professional": [
        "BS Nursing", "BS Medical Technology", "BS Pharmacy", "Doctor of Veterinary Medicine",
        "BS Physical Therapy", "BS Occupational Therapy", "BS Optometry"
    ],
    "healthcare_allied": [
        "BS Radiologic Technology", "BS Respiratory Therapy", "BS Medical Technology",
        "BS Nutrition and Dietetics", "BS Midwifery", "BS Speech-Language Pathology"
    ],
    "healthcare_support": [
        "BS Health Information Management", "BS Midwifery", "BS Nutrition and Dietetics"
    ],
    "education_social": [
        "Bachelor of Elementary Education", "Bachelor of Secondary Education",
        "Bachelor of Early Childhood Education", "Bachelor of Physical Education",
        "Bachelor of Special Needs Education"
    ],
    "counseling_support": [
        "BS Psychology", "BS Social Work", "Bachelor of Library and Information Science"
    ],
    "public_service": [
        "Bachelor of Public Administration", "BS Community Development",
        "BS Development Communication", "BA in Political Science"
    ],
    "community_service": [
        "BS Social Work", "BS Community Development", "BS Criminology"
    ],
    "engineering_cs": [
        "BS Computer Science", "BS Computer Engineering", "BS Civil Engineering",
        "BS Electrical Engineering", "BS Electronics Engineering", "BS Mechanical Engineering",
        "BS Aeronautical Engineering", "BS Data Science"
    ],
    "it_technology": [
        "BS Information Technology", "BS Cybersecurity", "BS Data Science",
        "BS Entertainment and Multimedia Computing", "BS Health Information Management"
    ],
    "tech_vocational": [
        "Bachelor of Technical-Vocational Teacher Education", "BS Aircraft Maintenance Technology",
        "BS Aviation Electronics Technology"
    ],
    "business_management": [
        "BS Entrepreneurship", "BS Business Administration major in Marketing Management",
        "BS Business Administration major in Human Resource Management",
        "BS Business Administration major in Operations Management"
    ],
    "business_analytics": [
        "BS Accountancy", "BS Business Administration major in Financial Management",
        "BS Management Accounting", "BS Accounting Information Systems", "BS Business Economics"
    ],
    "business_general": [
        "BS Customs Administration", "BS Real Estate Management", "BS Legal Management",
        "BS Agribusiness"
    ],
    "science_research": [
        "BS Biology", "BS Chemistry", "BS Physics", "BS Marine Biology",
        "BS Environmental Science", "BS Biotechnology", "BS Forensic Science",
        "BS Mathematics", "BS Statistics", "BS Geology", "BS Meteorology"
    ],
    "digital_media": [
        "BS Entertainment and Multimedia Computing", "BS Multimedia Arts",
        "BA in Animation", "BA in Game Art and Design", "BA in Digital Filmmaking"
    ],
    "fine_arts": [
        "Bachelor of Fine Arts", "BA in Photography", "BA in Fashion Design and Merchandising"
    ],
    "design_arts": [
        "BS Architecture", "BS Interior Design", "BS Landscape Architecture",
        "BS Industrial Design", "BA in Advertising Arts"
    ],
    "performing_arts": [
        "BA in Theater Arts", "BA in Music Production"
    ],
    "communication_media": [
        "BA in Communication", "BA in Journalism", "BS Development Communication"
    ],
    "business_leadership": [
        "BS Entrepreneurship", "BS Business Administration major in Marketing Management",
        "BS Business Administration major in Human Resource Management"
    ],
    "public_administration": [
        "Bachelor of Public Administration", "BA in Political Science",
        "BA in International Studies"
    ],
    "engineering_management": [
        "BS Industrial Engineering", "BS Civil Engineering",
        "BS Business Administration major in Operations Management"
    ],
}


# ================================================================================
# HYBRID RECOMMENDATION ENGINE
# ================================================================================

class HybridRecommendationEngine:
    """
    Hybrid Recommendation System combining Rule-Based Logic and Decision Tree
    
    Based on Hybrid Recommender Systems Theory (Burke, 2002)
    
    Flow:
    1. PHASE 1: Rule-Based Filtering
       - Apply eligibility rules to filter out ineligible courses
       - Apply preference rules to score remaining courses
    
    2. PHASE 2: Decision Tree Classification
       - Classify user into a course category
       - Boost courses in the predicted category
    
    3. Final Ranking
       - Combine scores from both phases
       - Rank courses and select top recommendations
    """
    
    def __init__(self):
        self.rule_filter = RuleBasedFilter()
        self.decision_tree = DecisionTreeClassifier()
    
    def generate_recommendations(
        self,
        courses: List[Any],
        user_profile: Dict[str, Any],
        trait_scores: Dict[str, float],
        career_path_courses: List[str] = None,
        top_n: int = 5
    ) -> Dict[str, Any]:
        """
        Generate course recommendations using the hybrid approach
        
        Args:
            courses: List of all courses from database
            user_profile: Dictionary with user's academic info
            trait_scores: Dictionary of trait -> score from assessment
            career_path_courses: List of course names from career path selections
            top_n: Number of top recommendations to return
        
        Returns:
            Dictionary with recommendations and detailed explanations
        """
        
        # Prepare user data for decision tree
        sorted_traits = sorted(trait_scores.items(), key=lambda x: x[1], reverse=True)
        top_traits = [t for t, _ in sorted_traits[:7]]
        primary_trait = sorted_traits[0][0] if sorted_traits else None
        
        # Determine work environments from traits
        work_envs = self.rule_filter._determine_work_environment(top_traits)
        
        tree_profile = {
            "primary_trait": primary_trait,
            "top_traits": top_traits,
            "gwa": user_profile.get("gwa", 85),
            "strand": user_profile.get("strand"),
            "work_environments": work_envs
        }
        
        # ==================== PHASE 1: RULE-BASED FILTERING ====================
        print("📋 PHASE 1: Applying Rule-Based Filtering...")
        
        filtered_courses = self.rule_filter.filter_courses(
            courses=courses,
            user_profile=user_profile,
            trait_scores=trait_scores,
            career_path_courses=career_path_courses
        )
        
        eligible_courses = [fc for fc in filtered_courses if fc.is_eligible]
        ineligible_courses = [fc for fc in filtered_courses if not fc.is_eligible]
        
        print(f"   ✓ {len(eligible_courses)} eligible courses")
        print(f"   ✗ {len(ineligible_courses)} ineligible courses")
        
        # ==================== PHASE 2: DECISION TREE CLASSIFICATION ====================
        print("🌳 PHASE 2: Applying Decision Tree Classification...")
        
        classification, confidence, tree_modifier, decision_path = self.decision_tree.classify(tree_profile)
        
        print(f"   → Classification: {classification}")
        print(f"   → Confidence: {confidence:.0%}")
        print(f"   → Decision Path: {' → '.join(decision_path)}")
        
        # Get recommended course categories
        recommended_courses_in_category = CLASSIFICATION_TO_COURSES.get(classification, [])
        
        # ==================== COMBINE SCORES ====================
        print("🔢 Combining scores from both phases...")
        
        final_scored_courses = []
        
        for fc in eligible_courses:
            course = fc.course
            
            # Base score from rule-based filtering
            rule_score = fc.eligibility_score
            
            # Decision tree boost for courses in predicted category
            tree_boost = 0
            in_predicted_category = course.course_name in recommended_courses_in_category
            if in_predicted_category:
                tree_boost = tree_modifier
            
            # Calculate matched traits for this course
            course_traits = [t.strip() for t in (course.trait_tag or "").split(",")]
            matched_traits = [t for t in top_traits if t in course_traits]
            
            # Final combined score
            final_score = rule_score + tree_boost
            
            # Calculate confidence score
            trait_confidence = (len(matched_traits) / max(1, len(course_traits))) * 100
            academic_confidence = 100 if fc.boost_total > fc.penalty_total else 50
            tree_confidence = confidence * 100 if in_predicted_category else 50
            
            overall_confidence = (trait_confidence * 0.4 + academic_confidence * 0.3 + tree_confidence * 0.3)
            
            # Determine priority tier
            if len(matched_traits) >= 3 and fc.penalty_total == 0 and in_predicted_category:
                priority = "EXCELLENT"
            elif len(matched_traits) >= 2 and fc.penalty_total <= 5:
                priority = "GOOD"
            elif len(matched_traits) >= 1:
                priority = "FAIR"
            else:
                priority = "EXPLORATORY"
            
            final_scored_courses.append({
                "course": course,
                "final_score": final_score,
                "rule_score": rule_score,
                "tree_boost": tree_boost,
                "confidence": round(overall_confidence, 1),
                "priority": priority,
                "matched_traits": matched_traits,
                "in_predicted_category": in_predicted_category,
                "rule_explanations": fc.rule_explanations,
                "warnings": fc.warnings,
                "boost_total": fc.boost_total,
                "penalty_total": fc.penalty_total
            })
        
        # Sort by final score
        final_scored_courses.sort(key=lambda x: (x["final_score"], x["confidence"]), reverse=True)
        
        # Select top recommendations with diversity
        top_recommendations = self._select_diverse_recommendations(final_scored_courses, top_n)
        
        # ==================== BUILD RESPONSE ====================
        recommendations = []
        for rank, rec in enumerate(top_recommendations, 1):
            course = rec["course"]
            
            # Build comprehensive reasoning
            reasoning_parts = []
            
            # Rule-based explanations
            if rec["matched_traits"]:
                trait_str = ", ".join(rec["matched_traits"][:3])
                if len(rec["matched_traits"]) > 3:
                    trait_str += f" (+{len(rec['matched_traits'])-3} more)"
                reasoning_parts.append(f"✓ Personality alignment: {trait_str}")
            
            # Decision tree explanation
            if rec["in_predicted_category"]:
                reasoning_parts.append(f"✓ Matches your predicted career path: {classification.replace('_', ' ').title()}")
            
            # Academic fit
            if rec["penalty_total"] == 0:
                reasoning_parts.append("✓ Meets all academic requirements")
            elif rec["warnings"]:
                reasoning_parts.append(f"⚠ {rec['warnings'][0]}")
            
            # Priority explanation
            priority_explanations = {
                "EXCELLENT": "🌟 Highly Recommended - Excellent match for your profile",
                "GOOD": "✨ Good Match - Strong alignment with your interests",
                "FAIR": "💡 Worth Considering - Could be rewarding with dedication",
                "EXPLORATORY": "🔍 Explore Option - Expand your horizons"
            }
            reasoning_parts.append(priority_explanations.get(rec["priority"], ""))
            
            recommendations.append({
                "rank": rank,
                "course_name": course.course_name,
                "description": course.description,
                "matched_traits": rec["matched_traits"],
                "minimum_gwa": float(course.minimum_gwa) if course.minimum_gwa else None,
                "recommended_strand": course.required_strand,
                "reasoning": " | ".join(reasoning_parts),
                "compatibility_score": rec["final_score"],
                "confidence_score": rec["confidence"],
                "priority_tier": rec["priority"],
                "match_details": {
                    "trait_matches": len(rec["matched_traits"]),
                    "rule_based_score": rec["rule_score"],
                    "decision_tree_boost": rec["tree_boost"],
                    "in_predicted_category": rec["in_predicted_category"],
                    "rule_explanations": rec["rule_explanations"][:5],  # Top 5 rule explanations
                    "warnings": rec["warnings"]
                }
            })
        
        return {
            "recommendations": recommendations,
            "algorithm_details": {
                "phase1_rule_based": {
                    "total_courses_evaluated": len(courses),
                    "eligible_courses": len(eligible_courses),
                    "ineligible_courses": len(ineligible_courses),
                    "rules_applied": len(self.rule_filter.rules)
                },
                "phase2_decision_tree": {
                    "classification": classification,
                    "confidence": confidence,
                    "decision_path": decision_path,
                    "recommended_category_courses": len(recommended_courses_in_category)
                }
            },
            "user_analysis": {
                "primary_trait": primary_trait,
                "top_traits": top_traits,
                "work_environments": list(work_envs),
                "predicted_career_category": classification.replace("_", " ").title()
            }
        }
    
    def _select_diverse_recommendations(
        self,
        scored_courses: List[Dict],
        top_n: int
    ) -> List[Dict]:
        """Select top recommendations while ensuring diversity"""
        
        selected = []
        used_strands = {}
        max_per_strand = 2  # Allow max 2 courses per strand
        
        # First pass: prioritize EXCELLENT and GOOD courses
        for course_data in scored_courses:
            if len(selected) >= top_n:
                break
            
            course = course_data["course"]
            strand = course.required_strand or "General"
            
            if used_strands.get(strand, 0) < max_per_strand:
                if course_data["priority"] in ["EXCELLENT", "GOOD"]:
                    selected.append(course_data)
                    used_strands[strand] = used_strands.get(strand, 0) + 1
        
        # Second pass: fill remaining slots
        for course_data in scored_courses:
            if len(selected) >= top_n:
                break
            
            if course_data not in selected:
                course = course_data["course"]
                strand = course.required_strand or "General"
                
                if used_strands.get(strand, 0) < max_per_strand:
                    selected.append(course_data)
                    used_strands[strand] = used_strands.get(strand, 0) + 1
        
        return selected
