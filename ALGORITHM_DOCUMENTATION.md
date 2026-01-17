# Course Recommendation System - Algorithm Documentation

## Overview

This document describes the **Hybrid Recommendation System** implemented in the CoursePro College Course Recommendation System. The algorithm follows a **two-phase approach** combining **Rule-Based Logic** and **Decision Tree Classification** as specified in the thesis proposal.

---

## Theoretical Framework

### 1. Rule-Based Expert Systems Theory (Giarratano & Riley, 2005)
The Rule-Based Filtering component applies a set of predefined IF-THEN rules to initially filter suitable courses based on the student's qualifications and stated preferences.

### 2. Decision Tree Algorithm Theory (Quinlan, 1986)
The Decision Tree component classifies students into career categories and ranks courses based on identified patterns from assessment data.

### 3. Hybrid Recommender Systems Theory (Burke, 2002)
The system combines content-based filtering (matching user traits to course requirements) with knowledge-based recommendations (using explicit rules about course eligibility).

### 4. Holland's Theory (RIASEC)
The assessment questions and trait mapping align with Holland's vocational personality types to identify career interests.

---

## Algorithm Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    COURSE RECOMMENDATION SYSTEM                               │
│                     Two-Phase Hybrid Approach                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                               │
│   INPUT                                                                       │
│   ├── User Profile (GWA, Strand, Personal Info)                              │
│   ├── Assessment Answers (193 questions)                                      │
│   └── Trait Scores (derived from answers)                                    │
│                                                                               │
│   ┌───────────────────────────────────────────────────────────────────────┐  │
│   │         PHASE 1: RULE-BASED FILTERING                                  │  │
│   │         (Giarratano & Riley, 2005)                                     │  │
│   │                                                                         │  │
│   │   Apply IF-THEN rules to eliminate ineligible courses:                 │  │
│   │                                                                         │  │
│   │   ELIGIBILITY RULES (Hard Constraints):                                │  │
│   │   ├── E1: GWA Minimum Requirement                                      │  │
│   │   │       IF user_gwa < course_min_gwa - 5 THEN INELIGIBLE            │  │
│   │   └── E2: Strand Alignment                                             │  │
│   │           IF strand_incompatible THEN APPLY PENALTY                    │  │
│   │                                                                         │  │
│   │   PREFERENCE RULES (Soft Constraints with Scoring):                    │  │
│   │   ├── P1: Primary Trait Match → +15 points                            │  │
│   │   ├── P2: Trait Synergy (≥3 matches) → +10 points                     │  │
│   │   ├── P3: Career Path Direct Match → +20 points                       │  │
│   │   ├── P4: GWA Excellence (exceeds by ≥5) → +8 points                  │  │
│   │   ├── P5: Strand Perfect Match → +12 points                           │  │
│   │   ├── P6: Work Environment Match → +6 points                          │  │
│   │   └── P7: Learning Style Match → +5 points                            │  │
│   │                                                                         │  │
│   │   PENALTY RULES:                                                        │  │
│   │   ├── N1: GWA Shortfall → -5 × gap points                             │  │
│   │   ├── N2: Strand Mismatch → -10 points                                │  │
│   │   └── N3: No Trait Match → -15 points                                 │  │
│   │                                                                         │  │
│   │   OUTPUT: Eligibility Score + Rule Explanations                        │  │
│   └───────────────────────────────────────────────────────────────────────┘  │
│                                     │                                         │
│                                     ▼                                         │
│   ┌───────────────────────────────────────────────────────────────────────┐  │
│   │         PHASE 2: DECISION TREE CLASSIFICATION                          │  │
│   │         (Quinlan, 1986)                                                 │  │
│   │                                                                         │  │
│   │   Hierarchical classification based on user attributes:                │  │
│   │                                                                         │  │
│   │                    [trait_category]                                     │  │
│   │                           │                                             │  │
│   │          ┌────────────────┼────────────────┐                           │  │
│   │          │                │                │                           │  │
│   │      [helping]      [problem_solving]  [creative]    [leading]         │  │
│   │          │                │                │             │              │  │
│   │     [work_setting]  [analytical_type] [creative_type] [domain]         │  │
│   │          │                │                │             │              │  │
│   │    ┌─────┼─────┐    ┌─────┼─────┐    ┌────┼────┐    ┌───┼───┐         │  │
│   │    │     │     │    │     │     │    │    │    │    │   │   │          │  │
│   │ clinical office field tech business research visual perf writing       │  │
│   │    │                │                │                                  │  │
│   │ [gwa_level]    [gwa_level]      [tech_affinity]                        │  │
│   │    │                │                │                                  │  │
│   │ high→healthcare_prof  high→engineering_cs  high→digital_media          │  │
│   │ med→healthcare_allied med→it_technology    med→design_arts             │  │
│   │ low→healthcare_support low→tech_vocational low→fine_arts               │  │
│   │                                                                         │  │
│   │   LEAF NODE OUTPUTS:                                                   │  │
│   │   ├── Classification (e.g., "healthcare_professional")                 │  │
│   │   ├── Confidence Score (0-100%)                                        │  │
│   │   └── Score Modifier (+15 to +25 points for matching courses)         │  │
│   │                                                                         │  │
│   │   OUTPUT: Career Classification + Decision Path                        │  │
│   └───────────────────────────────────────────────────────────────────────┘  │
│                                     │                                         │
│                                     ▼                                         │
│   ┌───────────────────────────────────────────────────────────────────────┐  │
│   │         SCORE COMBINATION & RANKING                                    │  │
│   │                                                                         │  │
│   │   Final Score = Rule-Based Score + Decision Tree Boost                 │  │
│   │                                                                         │  │
│   │   Priority Tiers:                                                       │  │
│   │   ├── EXCELLENT: ≥3 traits + academic match + in predicted category   │  │
│   │   ├── GOOD: Strong trait OR academic match                            │  │
│   │   ├── FAIR: Some alignment, room for growth                           │  │
│   │   └── EXPLORATORY: Consider for horizon expansion                     │  │
│   │                                                                         │  │
│   │   Diversity Filtering: Max 2 courses per strand                        │  │
│   └───────────────────────────────────────────────────────────────────────┘  │
│                                     │                                         │
│   OUTPUT                            ▼                                         │
│   ├── Top 5 Recommendations with:                                            │
│   │   ├── Course Name & Description                                          │
│   │   ├── Matched Traits                                                     │
│   │   ├── Compatibility Score                                                │
│   │   ├── Confidence Score (0-100%)                                         │
│   │   ├── Priority Tier                                                      │  
│   │   └── Transparent Reasoning (rule explanations)                         │
│   │                                                                           │
│   └── Algorithm Details:                                                      │
│       ├── Phase 1: Rules applied, eligible/ineligible counts                │
│       └── Phase 2: Classification, decision path, confidence                │
│                                                                               │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Phase 1: Rule-Based Filtering

### Rule Structure

Each rule follows the IF-THEN structure of expert systems:

```python
Rule(
    rule_id="E1",
    rule_name="GWA Minimum Requirement",
    rule_type=RuleType.ELIGIBILITY,
    conditions={"check": "gwa_requirement"},
    action="check_eligibility",
    explanation_template="IF user_gwa ({user_gwa}) < course_minimum_gwa ({min_gwa}) THEN course is INELIGIBLE"
)
```

### Rule Categories

#### 1. Eligibility Rules (Hard Constraints)
These rules determine if a course is even possible for the student:

| Rule ID | Rule Name | Condition | Action |
|---------|-----------|-----------|--------|
| E1 | GWA Minimum Requirement | user_gwa < min_gwa - 5 | Mark INELIGIBLE |
| E2 | Strand Alignment | strand_incompatible | Apply penalty or mark INELIGIBLE |

#### 2. Preference Rules (Soft Constraints)
These rules add boost points to compatible courses:

| Rule ID | Rule Name | Condition | Boost |
|---------|-----------|-----------|-------|
| P1 | Primary Trait Alignment | primary_trait IN course_traits | +15 |
| P2 | Trait Synergy Bonus | trait_matches ≥ 3 | +10 |
| P3 | Career Path Preference | course IN career_path_selection | +20 |
| P4 | GWA Excellence | user_gwa > min_gwa + 5 | +8 |
| P5 | Strand Perfect Match | user_strand == required_strand | +12 |
| P6 | Work Environment Match | env_preference matches | +6 |
| P7 | Learning Style Match | learning_style matches | +5 |

#### 3. Penalty Rules
These rules subtract points for mismatches:

| Rule ID | Rule Name | Condition | Penalty |
|---------|-----------|-----------|---------|
| N1 | GWA Shortfall Penalty | user_gwa < min_gwa | gap × 5 |
| N2 | Strand Mismatch Penalty | strand_incompatible | 10 |
| N3 | No Trait Match Penalty | trait_matches = 0 | 15 |

### Strand Compatibility Matrix

```python
STRAND_COMPATIBILITY = {
    'STEM': ['STEM', 'GAS'],
    'ABM': ['ABM', 'GAS', 'HUMSS'],
    'HUMSS': ['HUMSS', 'GAS', 'ABM'],
    'GAS': ['STEM', 'ABM', 'HUMSS', 'GAS', 'TVL', 'Sports'],
    'TVL': ['TVL', 'GAS', 'STEM'],
    'Sports': ['Sports', 'GAS', 'HUMSS'],
}
```

---

## Phase 2: Decision Tree Classification

### Tree Structure

The decision tree classifies users based on:
1. **Primary Trait Category** (Root node)
2. **Work Setting Preference** (Internal nodes)
3. **Academic Strength** (Internal nodes)
4. **Specialization** (Leaf nodes → Course categories)

### Trait Categories

| Category | Associated Traits |
|----------|-------------------|
| Helping | Helping-others, Empathetic, Compassionate, Service-oriented |
| Problem-Solving | Problem-solving, Analytical, Logical, Research-oriented |
| Creative | Creative-expression, Innovative, Artistic-passion, Visual-learner |
| Leading | Leading-teams, Leadership, Big-picture, Strategic |

### Decision Paths Example

```
User with traits: [Helping-others, Empathetic, Clinical-setting] + High GWA

DECISION PATH:
1. trait_category = "helping"        → Branch to helping node
2. work_setting = "clinical"         → Branch to clinical setting
3. gwa_level = "high"               → Leaf: healthcare_professional

RESULT: Classification = "healthcare_professional"
        Confidence = 90%
        Boost = +25 points for: BS Nursing, BS Medical Technology, etc.
```

### Course Category Mappings

| Classification | Example Courses |
|---------------|-----------------|
| healthcare_professional | BS Nursing, BS Medical Technology, BS Pharmacy |
| healthcare_allied | BS Radiologic Technology, BS Nutrition and Dietetics |
| engineering_cs | BS Computer Science, BS Civil Engineering |
| it_technology | BS Information Technology, BS Cybersecurity |
| digital_media | BS Multimedia Arts, BA in Animation |
| business_management | BS Entrepreneurship, BS Business Administration |
| education_social | Bachelor of Elementary Education, BS Psychology |

---

## Output Format

### Recommendation Response

```json
{
    "user_id": 1,
    "user_gwa": 90,
    "user_strand": "STEM",
    "detected_traits": [["Problem-solving", 8], ["Analytical", 6], ["Tech-savvy", 5]],
    "trait_analysis": {
        "primary_trait": "Problem-solving",
        "predicted_career_category": "Engineering Cs",
        "total_traits_detected": 15
    },
    "recommendations": [
        {
            "rank": 1,
            "course_name": "BS Computer Science",
            "description": "Study of algorithms, programming, and computing systems",
            "matched_traits": ["Problem-solving", "Analytical", "Tech-savvy"],
            "minimum_gwa": 85.0,
            "recommended_strand": "STEM",
            "reasoning": "✓ Personality alignment: Problem-solving, Analytical, Tech-savvy | ✓ Matches your predicted career path: Engineering Cs | ✓ Meets all academic requirements | 🌟 Highly Recommended - Excellent match for your profile",
            "compatibility_score": 85,
            "confidence_score": 92.5,
            "priority_tier": "EXCELLENT",
            "match_details": {
                "trait_matches": 3,
                "rule_based_score": 60,
                "decision_tree_boost": 25,
                "in_predicted_category": true,
                "rule_explanations": [
                    "✓ Primary Trait Alignment: Primary trait 'Problem-solving' matches course requirements",
                    "✓ Trait Synergy Bonus: Trait synergy: 3 traits match",
                    "✓ GWA Excellence: GWA excellence: exceeds requirement by 5.0 points"
                ]
            }
        }
    ],
    "algorithm_details": {
        "phase1_rule_based": {
            "description": "Rule-Based Filtering using IF-THEN logic (Giarratano & Riley, 2005)",
            "rules_applied": 10,
            "eligible_courses": 75,
            "ineligible_courses": 22
        },
        "phase2_decision_tree": {
            "description": "Decision Tree Classification (Quinlan, 1986)",
            "classification": "engineering_cs",
            "confidence": 0.9,
            "decision_path": ["trait_category=problem_solving", "analytical_type=technical", "gwa_level=high"]
        }
    },
    "algorithm_metrics": {
        "matching_algorithm_version": "3.0-RuleBased-DecisionTree"
    }
}
```

---

## Transparency & Explainability

### Rule Explanations

Each recommendation includes transparent explanations of why it was selected:

1. **Trait-Based Reasoning**: "✓ Personality alignment: Problem-solving, Analytical, Tech-savvy"
2. **Decision Tree Reasoning**: "✓ Matches your predicted career path: Engineering Cs"
3. **Academic Reasoning**: "✓ Meets all academic requirements" or "⚠ GWA slightly below requirement"
4. **Priority Explanation**: "🌟 Highly Recommended - Excellent match for your profile"

### Decision Path Transparency

The algorithm provides the exact decision path taken:
```
decision_path: ["trait_category=problem_solving", "analytical_type=technical", "gwa_level=high"]
```

This allows users and panelists to understand exactly how the recommendation was generated.

---

## Algorithm Version History

| Version | Description | Date |
|---------|-------------|------|
| 1.0 | Basic trait matching | Initial |
| 2.0 | 10-algorithm weighted scoring (deprecated) | Previous |
| 3.0-RuleBased-DecisionTree | Thesis-compliant hybrid approach | Current |

---

## References

1. Giarratano, J. C., & Riley, G. D. (2005). *Expert Systems: Principles and Programming*. Thomson Course Technology.

2. Quinlan, J. R. (1986). Induction of decision trees. *Machine Learning*, 1(1), 81-106.

3. Burke, R. (2002). Hybrid recommender systems: Survey and experiments. *User Modeling and User-Adapted Interaction*, 12(4), 331-370.

4. Holland, J. L. (1997). *Making Vocational Choices: A Theory of Vocational Personalities and Work Environments*. Psychological Assessment Resources.
