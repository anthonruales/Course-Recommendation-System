// --- EXPERT KNOWLEDGE BASE ---
const strandRequirements = {
  "STEM": ["Computer Science", "Civil Engineering", "Biology", "Data Science"],
  "ABM": ["Accountancy", "Business Administration", "Marketing"],
  "HUMSS": ["Psychology", "Communication Arts", "Political Science"],
  "GAS": ["General Studies", "Entrepreneurship", "Education"],
  "TVL": ["Information Technology", "Hospitality Management"]
};

const gradeThresholds = {
  "BS Computer Science": { keyword: "math", min: 85 },
  "BS Civil Engineering": { keyword: "math", min: 88 },
  "BS Accountancy": { keyword: "math", min: 85 },
  "BS Data Science": { keyword: "math", min: 85 },
  "BS Psychology": { keyword: "science", min: 83 },
  "BS Biology": { keyword: "science", min: 85 }
};

export const calculateRecommendation = (profile, answers) => {
  // DEBUGGER: This helps you see exactly what data is arriving in the engine
  console.log("DEBUG: Received Profile:", profile);
  console.log("DEBUG: Received Answers:", answers);

  let recommendations = [];
  let candidatePool = [];

  const currentStrand = profile?.shsStrand || 'GAS';
  candidatePool = strandRequirements[currentStrand] || strandRequirements["GAS"];

  // 1. DECISION TREE (INTEREST QUESTIONNAIRE)
  if (answers?.q1 === 'yes') { 
    if (answers?.q2 === 'yes') {
      if (candidatePool.includes('Computer Science')) recommendations.push('BS Computer Science');
      if (candidatePool.includes('Data Science')) recommendations.push('BS Data Science');
    } else {
      if (candidatePool.includes('Civil Engineering')) recommendations.push('BS Civil Engineering');
    }
  } else {
    if (answers?.q3 === 'yes') {
      if (candidatePool.includes('Accountancy')) recommendations.push('BS Accountancy');
      if (candidatePool.includes('Business Administration')) recommendations.push('BS Business Administration');
    } else {
      if (candidatePool.includes('Psychology')) recommendations.push('BS Psychology');
      if (candidatePool.includes('Communication Arts')) recommendations.push('BA Communication Arts');
    }
  }

  if (recommendations.length === 0) {
    recommendations.push(candidatePool[0] === 'General Studies' ? 'General Studies' : `BS ${candidatePool[0]}`); 
  }

  const primaryCourse = recommendations[0];

  // 2. EXPERT VALIDATION
  const isAligned = (strandRequirements[currentStrand] || []).some(course => 
    primaryCourse.includes(course)
  );

  let status = "Qualified";
  let analysis = "";
  const requirement = gradeThresholds[primaryCourse];

  if (requirement) {
    let studentGrade = 0;
    let foundSubjectName = "";

    // Aggressive Search Logic
    // We check both profile.grades AND profile.profileData.grades in case of nesting
    const gradeSource = profile?.grades || profile?.profileData?.grades;

    if (gradeSource) {
      const keys = Object.keys(gradeSource);
      const targetKey = keys.find(k => 
        k.toLowerCase().includes(requirement.keyword.toLowerCase())
      );
      
      if (targetKey) {
        studentGrade = parseInt(gradeSource[targetKey]);
        foundSubjectName = targetKey;
      }
    }
    
    if (!gradeSource || studentGrade === 0) {
      status = "Profile Incomplete";
      analysis = `We couldn't find a grade for "${requirement.keyword}". Current data: ${JSON.stringify(gradeSource || 'Missing')}`;
    } else if (studentGrade < requirement.min) {
      status = "Bridging Required";
      analysis = `Your interest matches ${primaryCourse}, but your ${foundSubjectName} grade (${studentGrade}) is below the recommended ${requirement.min}%. You may need bridging classes.`;
    }
  }

  if (status === "Qualified") {
    analysis = isAligned 
      ? `This course is highly recommended! It perfectly aligns with your ${currentStrand} strand and your academic performance.` 
      : `Based on your interests, ${primaryCourse} is a strong match, though it differs from your ${currentStrand} track.`;
  }

  return {
    courses: [primaryCourse],
    isAligned: isAligned,
    status: status,
    analysis: analysis
  };
};