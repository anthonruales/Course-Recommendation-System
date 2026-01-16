# Enhanced Recommendation Reasoning System

## Overview
The recommendation system now provides detailed reasoning for each recommended course, showing exactly how four key factors influenced the recommendation.

## Response Structure

When a user submits an assessment, the `/recommend` endpoint returns recommendations with detailed reasoning:

```json
{
  "user_id": 1,
  "user_gwa": 87.5,
  "user_strand": "STEM",
  "detected_traits": [
    ["Analytical", 5],
    ["Technical", 4],
    ["Logical", 3]
  ],
  "recommendations": [
    {
      "course_name": "BS Computer Science",
      "description": "Study of computation, complexity, and advanced software design.",
      "matched_traits": ["Analytical", "Technical", "Logical"],
      "minimum_gwa": 88,
      "recommended_strand": "STEM",
      "compatibility_score": 15,
      "reasoning": "Matches your personality traits: Analytical, Technical, Logical. ✓ Your strand (STEM) perfectly aligns with the recommended strand (STEM) ✓ Your GWA (87.5) exceeds the minimum requirement (88) by -0.50 points. Your assessment revealed interests in: Analytical, Technical, Logical",
      "reasoning_details": {
        "trait_alignment": "Matches your personality traits: Analytical, Technical, Logical",
        "strand_influence": "✓ Your strand (STEM) perfectly aligns with the recommended strand (STEM)",
        "gwa_assessment": "⚠ Your GWA (87.5) is 0.50 points below the minimum requirement (88). You may need improvement.",
        "academic_interest": "Your assessment revealed interests in: Analytical, Technical, Logical",
        "summary": "Full summary of all factors combined"
      }
    }
  ]
}
```

## Reasoning Factors Explained

### 1. **Trait Alignment**
- **Purpose**: Shows which personality traits from the assessment match the course
- **Example**: "Matches your personality traits: Analytical, Technical, Logical"
- **Impact**: Questions with selected options tagged with these traits are counted during assessment
- **How it works**: Each question option has a trait tag. When the user selects an option, that trait is counted. Traits appearing most frequently are matched against the course's trait_tag list.

### 2. **Strand Influence**
- **Purpose**: Indicates whether the user's SHS strand (STEM, ABM, HUMSS, GAS, TVL, Sports) matches the course's recommended strand
- **Example with match**: "✓ Your strand (STEM) perfectly aligns with the recommended strand (STEM)"
- **Example with mismatch**: "⚠ Your strand (ABM) differs from recommended (STEM), but alternative path is available"
- **Impact**: Strand matching provides a +2 score bonus to recommendations
- **Why it matters**: Some courses are designed for specific strands and students in those strands have prerequisites or foundational knowledge

### 3. **GWA Assessment**
- **Purpose**: Shows how the user's General Weighted Average (GWA) compares to the course's minimum GWA requirement
- **Example with qualification**: "✓ Your GWA (87.5) exceeds the minimum requirement (88) by 0.5 points"
- **Example without qualification**: "⚠ Your GWA (87.5) is 0.5 points below the minimum requirement (88). You may need improvement."
- **Impact**: 
  - GWA match provides a +2 score bonus
  - GWA mismatch applies a -5 penalty
- **Why it matters**: GWA reflects academic performance; higher GWA requirements indicate more demanding courses

### 4. **Academic Interest**
- **Purpose**: Displays the top 3 traits detected from the user's assessment answers
- **Example**: "Your assessment revealed interests in: Analytical, Technical, Logical"
- **How it works**: All selected options' traits are counted. The system identifies the top 3 most-selected traits, indicating areas of interest
- **Impact**: These interests are used to find matching courses and weight the recommendations

## Scoring Algorithm

Each course receives a compatibility score based on:

```
Score = 0

For each matched trait (from top 3 user traits):
  Score += count * 3  (count = how many times user selected this trait)

If GWA meets minimum:
  Score += 2

If Strand matches:
  Score += 2

Final Score = Score - GWA_penalty - Strand_penalty
```

### Penalties Applied:
- **GWA Mismatch**: -5 points
- **Strand Mismatch**: -3 points

Courses are ranked by final score, and the top 5 are returned as recommendations.

## Example Scenario

**Student Profile:**
- Name: Maria Santos
- Strand: STEM
- GWA: 89.5
- Assessment Results: Frequently selected options tagged with "Analytical", "Technical", "Problem-solving"

**Top Recommendation: BS Computer Science**

Reasoning breakdown:
- **Trait Alignment**: ✓ Matches your personality traits: Analytical, Technical
- **Strand Influence**: ✓ Your strand (STEM) perfectly aligns with the recommended strand (STEM)
- **GWA Assessment**: ✓ Your GWA (89.5) exceeds the minimum requirement (88) by 1.5 points
- **Academic Interest**: Your assessment revealed interests in: Analytical, Technical, Problem-solving

**Why this recommendation?**
1. Maria's trait selection shows she's analytical and technical
2. Her STEM strand is perfect for this program
3. Her GWA of 89.5 is above the minimum requirement of 88
4. The combination of factors gives this course a high compatibility score

## Benefits of This Approach

1. **Transparency**: Students understand exactly why they're being recommended a course
2. **Actionable Feedback**: Clear indicators of what needs improvement (e.g., GWA targets)
3. **Multiple Perspectives**: Considers traits, academics, and strand simultaneously
4. **Personalization**: Recommendations change based on individual assessment responses
5. **Alternative Pathways**: System acknowledges mismatches but suggests alternatives

## Usage for Students

When reviewing recommendations, students should:
1. Check the **Trait Alignment** to see if the course matches their interests
2. Review the **Strand Influence** to understand their path compatibility
3. Note the **GWA Assessment** to see if they need to improve academically
4. Consider the **Academic Interest** section to understand their revealed preferences
5. Use the **Compatibility Score** to understand ranking among recommendations

## API Endpoint

**POST** `/recommend`

**Request Body:**
```json
{
  "userId": 1,
  "answers": [
    {
      "questionId": 1,
      "chosenOptionId": 2
    }
  ]
}
```

**Response Includes:**
- User's GWA and Strand
- Top 3 detected traits from assessment
- 5 recommended courses with detailed reasoning
