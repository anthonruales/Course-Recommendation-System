const courseDNA = [
  { 
    name: "BS Computer Science", 
    traits: { analytical: 0.9, technical: 0.9, creative: 0.3 },
    preferredStrand: "STEM",
    reqSubject: "math",
    minGrade: 85 
  },
  { 
    name: "BS Accountancy", 
    traits: { analytical: 0.8, organized: 0.9, technical: 0.2 },
    preferredStrand: "ABM",
    reqSubject: "math",
    minGrade: 85 
  },
  { 
    name: "BS Civil Engineering", 
    traits: { analytical: 0.9, technical: 0.8, organized: 0.5 },
    preferredStrand: "STEM",
    reqSubject: "math",
    minGrade: 88 
  },
  { 
    name: "BS Psychology", 
    traits: { social: 0.9, analytical: 0.6, persuasive: 0.4 },
    preferredStrand: "HUMSS",
    reqSubject: "science",
    minGrade: 83 
  },
  { 
    name: "BS Marketing", 
    traits: { persuasive: 0.9, creative: 0.7, social: 0.6 },
    preferredStrand: "ABM",
    reqSubject: "math",
    minGrade: 80 
  }
];

export const calculateRecommendation = (profile, answers) => {
  let studentTraits = {
    analytical: 0,
    technical: 0,
    creative: 0,
    social: 0,
    persuasive: 0,
    organized: 0
  };

  if (answers.q1 === 'yes') { 
    studentTraits.analytical += 15;
    studentTraits.organized += 5; 
  }
  if (answers.q2 === 'yes') { 
    studentTraits.technical += 15;
    studentTraits.analytical += 5;
  }
  if (answers.q3 === 'yes') { 
    studentTraits.persuasive += 12;
    studentTraits.social += 8;
    studentTraits.organized += 4;
  }

  const studentStrand = profile?.shsStrand || "";

  const results = courseDNA.map(course => {
    let matchScore = 0;
    
    for (let trait in course.traits) {
      matchScore += (studentTraits[trait] || 0) * course.traits[trait];
    }

    if (studentStrand === course.preferredStrand) {
      matchScore *= 1.1; 
    }

    return {
      course: course.name,
      rawScore: matchScore,
      config: course 
    };
  });

  const topTrait = getTopTrait(studentTraits);

  const topMatches = results
    .sort((a, b) => b.rawScore - a.rawScore)
    .slice(0, 5)
    .map(match => {
      let status = "Qualified";
      let analysis = `Reflects your strong ${topTrait} affinity. `;

      const studentGrades = profile?.grades || {};
      const requiredSubject = match.config.reqSubject;
      const passingGrade = match.config.minGrade;

      const gradeKey = Object.keys(studentGrades).find(key => 
        key.toLowerCase().includes(requiredSubject.toLowerCase())
      );
      
      const studentGradeValue = parseInt(studentGrades[gradeKey] || 0);

      if (studentGradeValue > 0 && studentGradeValue < passingGrade) {
        status = "Bridging Required";
        analysis = `Your ${requiredSubject} grade (${studentGradeValue}) is below the university threshold of ${passingGrade}.`;
      } else if (studentGradeValue === 0) {
        status = "Incomplete Profile";
        analysis = `Academic history for ${requiredSubject} is missing. Results may vary.`;
      }

      return {
        course: match.course,
        status: status,
        analysis: analysis,
        score: Math.round(match.rawScore)
      };
    });

  return {
    courses: topMatches,
    traitProfile: studentTraits 
  };
};

function getTopTrait(traits) {
  const top = Object.keys(traits).reduce((a, b) => traits[a] > traits[b] ? a : b);
  return top.charAt(0).toUpperCase() + top.slice(1);
}