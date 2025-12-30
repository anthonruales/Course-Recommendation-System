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
  const currentStrand = profile?.shsStrand || 'GAS';
  const candidatePool = strandRequirements[currentStrand] || strandRequirements["GAS"];
  
  let rankedPool = [...candidatePool];

  if (answers?.q1 === 'yes') {
    if (answers?.q2 === 'yes') {
      rankedPool.sort((a, b) => (a.includes('Science') ? -1 : 1));
    } else {
      rankedPool.sort((a, b) => (a.includes('Engineering') ? -1 : 1));
    }
  } else if (answers?.q3 === 'yes') {
    rankedPool.sort((a, b) => (a.includes('Accountancy') || a.includes('Business') ? -1 : 1));
  }

  const topRecommendations = rankedPool.slice(0, 5).map((courseName) => {
    const fullName = courseName.startsWith('BA') || courseName.includes('General') 
      ? courseName 
      : `BS ${courseName}`;

    const isAligned = (strandRequirements[currentStrand] || []).includes(courseName);

    let status = "Qualified";
    let analysis = isAligned 
      ? `Highly aligned with your ${currentStrand} background.` 
      : `A strong alternative path based on your interests.`;
    
    const requirement = gradeThresholds[fullName];
    const gradeSource = profile?.grades || profile?.profileData?.grades;

    if (requirement && gradeSource) {
      const targetKey = Object.keys(gradeSource).find(k => 
        k.toLowerCase().includes(requirement.keyword.toLowerCase())
      );
      const studentGrade = parseInt(gradeSource[targetKey] || 0);

      if (studentGrade === 0) {
        status = "Profile Incomplete";
        analysis = `Missing ${requirement.keyword} grade for validation.`;
      } else if (studentGrade < requirement.min) {
        status = "Bridging Required";
        analysis = `Your ${requirement.keyword} grade (${studentGrade}) is below the target ${requirement.min}%.`;
      }
    }

    return {
      course: fullName,
      status: status,
      isAligned: isAligned,
      analysis: analysis
    };
  });

  return {
    courses: topRecommendations,
    primaryStrand: currentStrand,
    overallAnalysis: `We've identified ${topRecommendations.length} potential pathways within the ${currentStrand} strand.`
  };
};