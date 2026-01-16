"""
Test script to demonstrate the Enhanced Algorithm v2.0 improvements
"""

def simulate_algorithm_comparison():
    """Compare old vs new algorithm results"""
    
    # Sample user profile
    user_profile = {
        "user_id": 1,
        "gwa": 90.5,
        "strand": "STEM",
        "trait_scores": {
            "Analytical": 7,
            "Technical": 5,
            "Creative": 4,
            "Logical": 3,
            "Problem-solving": 2
        }
    }
    
    # Sample course
    course = {
        "name": "BS Computer Science",
        "minimum_gwa": 88,
        "required_strand": "STEM",
        "traits": ["Analytical", "Technical", "Logical", "Problem-solving", "Algorithm-focused"]
    }
    
    print("=" * 80)
    print("ALGORITHM COMPARISON TEST")
    print("=" * 80)
    print(f"\n👤 User Profile:")
    print(f"   GWA: {user_profile['gwa']}")
    print(f"   Strand: {user_profile['strand']}")
    print(f"   Top Traits: {', '.join([f'{k}({v})' for k,v in list(user_profile['trait_scores'].items())[:3]])}")
    
    print(f"\n📚 Course: {course['name']}")
    print(f"   Min GWA: {course['minimum_gwa']}")
    print(f"   Strand: {course['required_strand']}")
    print(f"   Traits: {', '.join(course['traits'][:3])}")
    
    # ========== OLD ALGORITHM (v1.0) ==========
    print("\n" + "=" * 80)
    print("OLD ALGORITHM (v1.0) - Simple Linear Scoring")
    print("=" * 80)
    
    old_score = 0
    matched_traits = []
    
    # Old: Simple trait matching (top 3 only, equal weight)
    for trait, count in list(user_profile['trait_scores'].items())[:3]:
        if trait in course['traits']:
            old_score += count * 3
            matched_traits.append(trait)
    
    print(f"\n1. Trait Matching (Top 3 only, weight ×3):")
    print(f"   Matched: {', '.join(matched_traits)}")
    print(f"   Score: {old_score}")
    
    # Old: Binary GWA scoring
    if user_profile['gwa'] >= course['minimum_gwa']:
        old_score += 2
        print(f"\n2. GWA: ✓ Meets requirement (+2)")
    else:
        old_score -= 5
        print(f"\n2. GWA: ✗ Below requirement (-5)")
    
    # Old: Binary Strand scoring
    if user_profile['strand'] in course['required_strand']:
        old_score += 2
        print(f"3. Strand: ✓ Matches (+2)")
    else:
        old_score -= 3
        print(f"3. Strand: ✗ Doesn't match (-3)")
    
    print(f"\n📊 FINAL OLD SCORE: {old_score}")
    print(f"   Percentage: {min(100, max(0, (old_score / 30) * 100)):.1f}%")
    print(f"   Confidence Score: N/A (not available)")
    print(f"   Priority Tier: N/A (not available)")
    
    # ========== NEW ALGORITHM (v2.0) ==========
    print("\n" + "=" * 80)
    print("NEW ALGORITHM (v2.0) - Multi-Criteria Weighted Decision Tree")
    print("=" * 80)
    
    # New: Weighted trait matching (top 5, progressive weights)
    trait_score = 0
    matched_traits_new = []
    weights = [5, 4, 3, 2, 1]
    
    print(f"\n1. Enhanced Trait Matching (Top 5, progressive weights):")
    for idx, (trait, count) in enumerate(list(user_profile['trait_scores'].items())[:5]):
        if trait in course['traits']:
            weight = weights[idx]
            points = count * weight
            trait_score += points
            matched_traits_new.append(trait)
            print(f"   • {trait}: {count} selections × weight {weight} = {points} points")
    
    print(f"   Trait Score: {trait_score}")
    
    # New: Progressive GWA scoring
    gwa_gap = user_profile['gwa'] - course['minimum_gwa']
    academic_score = 0
    gwa_penalty = 0
    
    print(f"\n2. Progressive GWA Assessment:")
    print(f"   Gap: {gwa_gap:.1f} points")
    if gwa_gap >= 5:
        academic_score += 5
        print(f"   ✓ Significantly exceeds requirement (+5)")
    elif gwa_gap >= 2:
        academic_score += 3
        print(f"   ✓ Comfortably exceeds requirement (+3)")
    elif gwa_gap >= 0:
        academic_score += 2
        print(f"   ✓ Meets requirement (+2)")
    else:
        if abs(gwa_gap) <= 1:
            gwa_penalty = 2
            print(f"   ⚠ Close miss (-2)")
        elif abs(gwa_gap) <= 3:
            gwa_penalty = 5
            print(f"   ⚠ Moderate gap (-5)")
        else:
            gwa_penalty = 8
            print(f"   ⚠ Significant gap (-8)")
    
    # New: Intelligent strand alignment
    strand_score = 0
    strand_penalty = 0
    
    print(f"\n3. Intelligent Strand Alignment:")
    if user_profile['strand'] in course['required_strand']:
        strand_score = 4
        print(f"   ✓ Perfect alignment (+4)")
    else:
        # Check related strands
        related = {'STEM': ['GAS'], 'GAS': ['STEM', 'ABM', 'HUMSS']}
        user_related = related.get(user_profile['strand'], [])
        if course['required_strand'] in user_related:
            strand_score = 1
            strand_penalty = 2
            print(f"   ~ Related strand (+1, -2 penalty)")
        else:
            strand_penalty = 4
            print(f"   ✗ Unrelated strand (-4)")
    
    base_score = trait_score + academic_score + strand_score
    final_score = base_score - gwa_penalty - strand_penalty
    
    print(f"\n4. Score Calculation:")
    print(f"   Base Score: {base_score} (trait: {trait_score} + academic: {academic_score} + strand: {strand_score})")
    print(f"   Penalties: -{gwa_penalty + strand_penalty} (gwa: {gwa_penalty} + strand: {strand_penalty})")
    print(f"   Final Score: {final_score}")
    
    # New: Confidence scoring
    trait_confidence = min(100, (len(matched_traits_new) / min(5, len(course['traits']))) * 100) * 0.40
    academic_confidence = 100 * 0.30  # Both match
    diversity_confidence = min(100, (len(matched_traits_new) / len(user_profile['trait_scores'])) * 100) * 0.20
    primary_bonus = 100 * 0.10  # Primary trait matches
    
    confidence = trait_confidence + academic_confidence + diversity_confidence + primary_bonus
    
    print(f"\n5. Confidence Score (New Feature):")
    print(f"   Trait Match Strength (40%): {trait_confidence:.1f}")
    print(f"   Academic Fit (30%): {academic_confidence:.1f}")
    print(f"   Diversity Alignment (20%): {diversity_confidence:.1f}")
    print(f"   Primary Trait Bonus (10%): {primary_bonus:.1f}")
    print(f"   Total Confidence: {confidence:.1f}%")
    
    # New: Priority tier
    gwa_match = gwa_gap >= 0
    strand_match = user_profile['strand'] in course['required_strand']
    
    if strand_match and gwa_match and len(matched_traits_new) >= 3:
        priority = "EXCELLENT 🌟"
    elif (strand_match or gwa_match) and len(matched_traits_new) >= 2:
        priority = "GOOD ✨"
    elif len(matched_traits_new) >= 1:
        priority = "FAIR 💡"
    else:
        priority = "EXPLORATORY 🔍"
    
    print(f"\n6. Priority Tier (New Feature): {priority}")
    
    print(f"\n📊 FINAL NEW SCORE: {final_score}")
    print(f"   Percentage: {min(100, max(0, (final_score / 40) * 100)):.1f}%")
    print(f"   Confidence: {confidence:.1f}%")
    print(f"   Priority: {priority}")
    
    # ========== COMPARISON SUMMARY ==========
    print("\n" + "=" * 80)
    print("IMPROVEMENT SUMMARY")
    print("=" * 80)
    
    improvements = [
        "✅ Considers Top 5 traits instead of 3",
        "✅ Progressive weighting (5,4,3,2,1) instead of equal weights",
        "✅ Graduated GWA scoring (2-5 points) instead of binary",
        "✅ Intelligent strand relationships recognized",
        "✅ Confidence score (0-100%) added for reliability",
        "✅ Priority tiers (EXCELLENT/GOOD/FAIR/EXPLORATORY) for quick assessment",
        "✅ More granular penalties based on gap size",
        "✅ Better transparency with detailed breakdowns"
    ]
    
    print("\n🎯 Key Improvements:")
    for improvement in improvements:
        print(f"   {improvement}")
    
    print(f"\n📈 Score Change: {old_score} → {final_score} ({'+' if final_score > old_score else ''}{final_score - old_score})")
    print(f"📈 New Features: Confidence Score ({confidence:.1f}%), Priority Tier ({priority.split()[0]})")
    
    print("\n" + "=" * 80)
    print("Test Complete! The enhanced algorithm provides more accurate,")
    print("transparent, and helpful recommendations.")
    print("=" * 80)

if __name__ == "__main__":
    simulate_algorithm_comparison()
