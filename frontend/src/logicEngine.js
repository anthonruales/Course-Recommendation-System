export const calculateRecommendation = (profile, answers) => {
  let recommendations = [];

  // --- LAYER 1: RULE-BASED FILTERING (Academic Profile) ---
  // This narrows down what the student is "eligible" for based on SHS Strand
  let candidatePool = [];

  if (profile.shsStrand === 'STEM') {
    candidatePool = ['Computer Science', 'Civil Engineering', 'Biology', 'Data Science'];
  } else if (profile.shsStrand === 'ABM') {
    candidatePool = ['Accountancy', 'Business Administration', 'Marketing'];
  } else if (profile.shsStrand === 'HUMSS') {
    candidatePool = ['Psychology', 'Communication Arts', 'Political Science'];
  } else {
    candidatePool = ['General Studies', 'Entrepreneurship'];
  }

  // --- LAYER 2: DECISION TREE (Interest Questionnaire) ---
  // We use the answers (q1, q2, q3) to branch down to a specific result
  
  if (answers.q1 === 'yes') { 
    // Branch: Technical/Problem Solving
    if (answers.q2 === 'yes') {
      // Branch: Analytical/Data
      if (candidatePool.includes('Computer Science')) recommendations.push('BS Computer Science');
      if (candidatePool.includes('Data Science')) recommendations.push('BS Data Science');
    } else {
      // Branch: Physical/Hands-on
      if (candidatePool.includes('Civil Engineering')) recommendations.push('BS Civil Engineering');
    }
  } else {
    // Branch: Social/Leadership/Creative
    if (answers.q3 === 'yes') {
      // Branch: Business/Lead
      if (candidatePool.includes('Accountancy')) recommendations.push('BS Accountancy');
      if (candidatePool.includes('Business Administration')) recommendations.push('BS Business Administration');
    } else {
      // Branch: Human-Centric/Social
      if (candidatePool.includes('Psychology')) recommendations.push('BS Psychology');
      if (candidatePool.includes('Communication Arts')) recommendations.push('BA Communication Arts');
    }
  }

  // Fallback if no specific matches found in the tree
  if (recommendations.length === 0) {
    recommendations.push(candidatePool[0]); 
  }

  return recommendations;
};