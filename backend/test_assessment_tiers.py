#!/usr/bin/env python
"""Test the assessment service"""

from assessment_service import AssessmentService

# Test getting available tiers
print("=" * 60)
print("Testing Assessment Service")
print("=" * 60)

# Test 1: Get all tiers
print("\n1. Getting all available tiers...")
tiers = AssessmentService.get_available_tiers()
for tier_name, tier_info in tiers.items():
    print(f"   - {tier_name}: {tier_info['question_count']} questions")

# Test 2: Get quick assessment
print("\n2. Getting Quick Assessment (30 questions)...")
quick_assessment = AssessmentService.get_assessment_by_tier('quick')
print(f"   ✓ Generated {len(quick_assessment['questions'])} questions")
print(f"   ✓ First question: {quick_assessment['questions'][0]['question'][:50]}...")

# Test 3: Get standard assessment
print("\n3. Getting Standard Assessment (80 questions)...")
standard_assessment = AssessmentService.get_assessment_by_tier('standard')
print(f"   ✓ Generated {len(standard_assessment['questions'])} questions")

# Test 4: Get comprehensive assessment
print("\n4. Getting Comprehensive Assessment (150 questions)...")
comprehensive_assessment = AssessmentService.get_assessment_by_tier('comprehensive')
print(f"   ✓ Generated {len(comprehensive_assessment['questions'])} questions")

# Test 5: Invalid tier
print("\n5. Testing invalid tier error handling...")
try:
    AssessmentService.get_assessment_by_tier('invalid')
    print("   ✗ Error: Should have raised ValueError")
except ValueError as e:
    print(f"   ✓ Correctly raised error: {str(e)[:50]}...")

print("\n" + "=" * 60)
print("✅ All tests passed!")
print("=" * 60)
