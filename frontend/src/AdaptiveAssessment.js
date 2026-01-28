import React, { useState, useEffect } from 'react';

/**
 * SMART CAREER ASSESSMENT
 * 
 * This component provides an intelligent assessment experience:
 * - Questions appear ONE AT A TIME
 * - Each question is intelligently selected based on your previous answers
 * - You can see courses narrowing down in real-time
 * - User selects 30, 50, or 60 questions
 */
function AdaptiveAssessment({ onBack, onShowResults, maxQuestions = 30 }) {
  // Session state
  const [sessionId, setSessionId] = useState(null);
  const [currentQuestion, setCurrentQuestion] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [isStarting, setIsStarting] = useState(false);
  const [error, setError] = useState(null);
  
  // Progress tracking
  const [currentRound, setCurrentRound] = useState(0);
  const [maxRounds, setMaxRounds] = useState(maxQuestions);
  const [minRounds, setMinRounds] = useState(Math.floor(maxQuestions * 0.5));
  const [confidence, setConfidence] = useState(0);
  const [coursesRemaining, setCoursesRemaining] = useState(99);
  const [traitsDiscovered, setTraitsDiscovered] = useState(0);
  const [canFinishEarly, setCanFinishEarly] = useState(false);
  
  // Preview of top courses (updates after each answer)
  const [topCoursesPreview, setTopCoursesPreview] = useState([]);
  const [lastTraitRecorded, setLastTraitRecorded] = useState(null);
  
  // Animation state
  const [isTransitioning, setIsTransitioning] = useState(false);
  
  // Results
  const [isComplete, setIsComplete] = useState(false);
  const [results, setResults] = useState(null);

  // Check academic profile on mount
  useEffect(() => {
    const userId = localStorage.getItem('userId');
    if (userId) {
      fetch(`http://localhost:8000/user/${userId}/academic-info`)
        .then(res => res.json())
        .then(data => {
          if (!data.has_academic_info) {
            alert('⚠️ Please complete your Academic Profile first!\n\nYou need to fill in your GWA and SHS Strand before taking the assessment.');
            onBack();
          }
        })
        .catch(err => {
          console.error('Error checking academic info:', err);
        });
    } else {
      alert('User ID not found. Please log in again.');
      onBack();
    }
  }, [onBack]);

  // Start the adaptive assessment
  const startAssessment = async () => {
    const userId = localStorage.getItem('userId');
    if (!userId) {
      alert('User ID not found. Please log in again.');
      return;
    }

    setIsStarting(true);
    setError(null);

    try {
      const response = await fetch('http://localhost:8000/adaptive/start', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 
          userId: parseInt(userId),
          maxQuestions: maxQuestions
        })
      });

      const data = await response.json();

      if (response.ok && data.success) {
        setSessionId(data.session_id);
        setMaxRounds(data.max_questions);
        setMinRounds(data.min_questions);
        setCurrentQuestion(data.first_question.question);
        setCurrentRound(data.first_question.round);
        setCoursesRemaining(data.first_question.courses_remaining);
        setConfidence(data.first_question.confidence);
      } else {
        setError(data.detail || 'Failed to start assessment');
      }
    } catch (err) {
      console.error('Start error:', err);
      setError('Connection error. Please check if the server is running.');
    } finally {
      setIsStarting(false);
    }
  };

  // Submit answer and get next question
  const submitAnswer = async (optionId) => {
    if (!sessionId || !currentQuestion || isLoading) return;

    setIsLoading(true);
    setIsTransitioning(true);

    try {
      const response = await fetch('http://localhost:8000/adaptive/answer', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          sessionId: sessionId,
          questionId: currentQuestion.question_id,
          chosenOptionId: optionId
        })
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || 'Failed to submit answer');
      }

      if (data.is_complete) {
        // Assessment finished
        setIsComplete(true);
        setResults(data.recommendations);
      } else {
        // Update state with new info
        setLastTraitRecorded(data.trait_recorded);
        setCurrentRound(data.current_round);
        setCoursesRemaining(data.courses_remaining);
        setConfidence(data.confidence);
        setTraitsDiscovered(data.traits_discovered);
        setTopCoursesPreview(data.top_courses_preview || []);
        setCanFinishEarly(data.can_finish_early);
        
        // Brief delay for transition effect
        setTimeout(() => {
          setCurrentQuestion(data.next_question.question);
          setIsTransitioning(false);
        }, 300);
      }
    } catch (err) {
      console.error('Submit error:', err);
      setError(err.message);
      setIsTransitioning(false);
    } finally {
      setIsLoading(false);
    }
  };

  // Finish early
  const finishEarly = async () => {
    if (!sessionId) return;

    setIsLoading(true);

    try {
      const response = await fetch('http://localhost:8000/adaptive/finish', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ sessionId })
      });

      const data = await response.json();

      if (response.ok && data.success) {
        setIsComplete(true);
        setResults(data.recommendations);
      } else {
        alert(data.detail || 'Cannot finish early yet');
      }
    } catch (err) {
      console.error('Finish error:', err);
      alert('Failed to finish assessment');
    } finally {
      setIsLoading(false);
    }
  };

  // Show results
  const handleShowResults = () => {
    if (results) {
      // Format for ResultsView - must match what standard assessment returns
      const formattedResults = {
        // This format triggers history save in App.js
        courses: results.map(rec => ({
          course: rec.course_name,
          score: typeof rec.match_percentage === 'number' && !isNaN(rec.match_percentage) ? rec.match_percentage : 75
        })),
        student_traits: results.flatMap(r => r.matched_traits || []).filter((v, i, a) => a.indexOf(v) === i),
        detected_traits: results.flatMap(r => r.matched_traits || []).map(t => [t, 1]).slice(0, 5),
        recommendations: results.map(rec => {
          const matchPercent = typeof rec.match_percentage === 'number' && !isNaN(rec.match_percentage) ? rec.match_percentage : 75;
          return {
            course_name: rec.course_name,
            description: rec.description,
            compatibility_score: matchPercent,  // This is what ResultsView expects!
            matched_traits: rec.matched_traits || [],
            minimum_gwa: rec.minimum_gwa,
            recommended_strand: rec.recommended_strand,
            reasoning: `Based on your ${(rec.matched_traits || []).slice(0, 3).join(', ')} traits from the adaptive assessment.`
          };
        })
      };
      onShowResults(formattedResults);
    }
  };

  // RENDER: Start Screen
  if (!sessionId) {
    return (
      <div style={styles.container}>
        <aside style={styles.sidebar}>
          <div style={styles.brand}>
            <img src="/logo.svg" alt="CoursePro" style={styles.logo} />
            <h2 style={styles.brandName}>CoursePro</h2>
          </div>
          <div style={styles.nav}>
            <div style={styles.navActive}>🧠 Smart Assessment</div>
            <div style={styles.navLink} onClick={onBack}>⬅ Exit</div>
          </div>
        </aside>

        <main style={styles.main}>
          <div style={styles.startScreen}>
            <div style={styles.genieIcon}>🎓</div>
            <h1 style={styles.title}>AI-Powered Career Assessment</h1>
            <p style={styles.subtitle}>
              Experience an intelligent assessment that adapts to YOUR answers!
            </p>

            <div style={styles.featureGrid}>
              <div style={styles.featureCard}>
                <span style={styles.featureIcon}>🎯</span>
                <h3>Adaptive Intelligence</h3>
                <p>Each question is dynamically selected based on your responses</p>
              </div>
              <div style={styles.featureCard}>
                <span style={styles.featureIcon}>⚡</span>
                <h3>Efficient Analysis</h3>
                <p>Get precise recommendations with only 10-25 targeted questions</p>
              </div>
              <div style={styles.featureCard}>
                <span style={styles.featureIcon}>📊</span>
                <h3>Real-Time Matching</h3>
                <p>Watch your career matches refine as you progress</p>
              </div>
              <div style={styles.featureCard}>
                <span style={styles.featureIcon}>💼</span>
                <h3>Personalized Guidance</h3>
                <p>One-on-one style consultation powered by AI</p>
              </div>
            </div>

            <button 
              onClick={startAssessment} 
              disabled={isStarting}
              style={styles.startButton}
            >
              {isStarting ? '🔄 Preparing...' : '🚀 Begin Assessment'}
            </button>

            {error && <p style={styles.error}>{error}</p>}
          </div>
        </main>
      </div>
    );
  }

  // RENDER: Results Screen
  if (isComplete && results) {
    return (
      <div style={styles.container}>
        <aside style={styles.sidebar}>
          <div style={styles.brand}>
            <img src="/logo.svg" alt="CoursePro" style={styles.logo} />
            <h2 style={styles.brandName}>CoursePro</h2>
          </div>
          <div style={styles.nav}>
            <div style={styles.navActive}>✅ Complete</div>
            <div style={styles.navLink} onClick={onBack}>⬅ Dashboard</div>
          </div>
        </aside>

        <main style={styles.main}>
          <div style={styles.resultsHeader}>
            <h1 style={styles.title}>🎉 Assessment Complete!</h1>
            <p style={styles.subtitle}>
              Based on {currentRound} questions, here are your personalized recommendations
            </p>
            <div style={styles.statsRow}>
              <div style={styles.stat}>
                <span style={styles.statValue}>{currentRound}</span>
                <span style={styles.statLabel}>Questions</span>
              </div>
              <div style={styles.stat}>
                <span style={styles.statValue}>{traitsDiscovered}</span>
                <span style={styles.statLabel}>Traits Found</span>
              </div>
              <div style={styles.stat}>
                <span style={styles.statValue}>{confidence}%</span>
                <span style={styles.statLabel}>Confidence</span>
              </div>
            </div>
          </div>

          <div style={styles.resultsGrid}>
            {results.slice(0, 5).map((course, index) => {
              // Ensure match_percentage is a valid number
              const matchPercent = typeof course.match_percentage === 'number' && !isNaN(course.match_percentage) 
                ? course.match_percentage 
                : 75;
              
              return (
              <div key={index} style={{
                ...styles.resultCard,
                borderColor: index === 0 ? '#10b981' : index < 3 ? '#6366f1' : 'rgba(255,255,255,0.1)'
              }}>
                <div style={styles.resultRank}>#{course.rank}</div>
                <h3 style={styles.resultName}>{course.course_name}</h3>
                <div style={styles.resultMatch}>
                  <div style={styles.matchBar}>
                    <div style={{
                      ...styles.matchFill,
                      width: `${matchPercent}%`,
                      background: index === 0 ? 'linear-gradient(90deg, #10b981, #34d399)' : 
                                 index < 3 ? 'linear-gradient(90deg, #6366f1, #818cf8)' : '#64748b'
                    }} />
                  </div>
                  <span style={styles.matchPercent}>{matchPercent}%</span>
                </div>
                <p style={styles.resultDesc}>{course.description}</p>
                {course.matched_traits && course.matched_traits.length > 0 && (
                  <div style={styles.traitTags}>
                    {course.matched_traits.slice(0, 3).map((trait, i) => (
                      <span key={i} style={styles.traitTag}>{trait}</span>
                    ))}
                  </div>
                )}
              </div>
            )})}
          </div>

          <button onClick={handleShowResults} style={styles.viewFullButton}>
            View Full Results & Analysis →
          </button>
        </main>
      </div>
    );
  }

  // RENDER: Question Screen
  return (
    <div style={styles.container}>
      <aside style={styles.sidebar}>
        <div style={styles.brand}>
          <img src="/logo.svg" alt="CoursePro" style={styles.logo} />
          <h2 style={styles.brandName}>CoursePro</h2>
        </div>
        
        {/* Progress Section */}
        <div style={styles.progressSection}>
          <h3 style={styles.progressTitle}>Progress</h3>
          
          <div style={styles.progressBar}>
            <div style={{
              ...styles.progressFill,
              width: `${(currentRound / maxRounds) * 100}%`
            }} />
          </div>
          <p style={styles.progressText}>Question {currentRound} of {maxRounds}</p>
          
          <div style={styles.confidenceMeter}>
            <span>Confidence</span>
            <div style={styles.confidenceBar}>
              <div style={{
                ...styles.confidenceFill,
                width: `${confidence}%`,
                background: confidence > 70 ? '#10b981' : confidence > 40 ? '#f59e0b' : '#6366f1'
              }} />
            </div>
            <span style={styles.confidenceValue}>{confidence}%</span>
          </div>
          
          <div style={styles.statsSmall}>
            <div>📚 {coursesRemaining} courses in consideration</div>
            <div>🏷️ {traitsDiscovered} traits discovered</div>
          </div>
        </div>

        {/* Top Courses Preview */}
        {topCoursesPreview.length > 0 && (
          <div style={styles.previewSection}>
            <h3 style={styles.previewTitle}>🔥 Top Matches</h3>
            {topCoursesPreview.slice(0, 3).map((course, index) => (
              <div key={index} style={styles.previewCard}>
                <div style={styles.previewRank}>#{index + 1}</div>
                <div style={styles.previewName}>{course.course_name}</div>
              </div>
            ))}
          </div>
        )}

        <div style={styles.nav}>
          {canFinishEarly && (
            <div style={styles.finishButton} onClick={finishEarly}>
              ✅ Finish & See Results
            </div>
          )}
          <div style={styles.navLink} onClick={onBack}>⬅ Exit</div>
        </div>
      </aside>

      <main style={styles.mainQuestion}>
        {/* Last trait indicator */}
        {lastTraitRecorded && (
          <div style={styles.traitIndicator}>
            ✨ Trait recorded: <strong>{lastTraitRecorded}</strong>
          </div>
        )}

        <div style={{
          ...styles.questionCard,
          opacity: isTransitioning ? 0.5 : 1,
          transform: isTransitioning ? 'translateX(20px)' : 'translateX(0)'
        }}>
          <div style={styles.questionHeader}>
            <span style={styles.questionNumber}>Question {currentRound}</span>
            <span style={styles.questionCategory}>{currentQuestion?.category}</span>
          </div>

          <h2 style={styles.questionText}>{currentQuestion?.question_text}</h2>

          <div style={styles.optionsContainer}>
            {currentQuestion?.options?.map((option) => (
              <button
                key={option.option_id}
                onClick={() => submitAnswer(option.option_id)}
                disabled={isLoading}
                style={styles.optionButton}
                onMouseEnter={(e) => {
                  e.target.style.background = 'rgba(99, 102, 241, 0.2)';
                  e.target.style.borderColor = '#6366f1';
                  e.target.style.transform = 'translateX(8px)';
                }}
                onMouseLeave={(e) => {
                  e.target.style.background = 'rgba(255,255,255,0.03)';
                  e.target.style.borderColor = 'rgba(255,255,255,0.1)';
                  e.target.style.transform = 'translateX(0)';
                }}
              >
                {option.option_text}
              </button>
            ))}
          </div>

          {isLoading && (
            <div style={styles.loadingOverlay}>
              <div style={styles.loadingSpinner}>🔄</div>
              <p>Analyzing your response...</p>
            </div>
          )}
        </div>

        {error && <p style={styles.error}>{error}</p>}
      </main>
    </div>
  );
}

const styles = {
  container: {
    display: 'flex',
    width: '100vw',
    height: '100vh',
    background: '#020617',
    backgroundImage: 'radial-gradient(at 0% 0%, hsla(253,16%,7%,1) 0, transparent 50%), radial-gradient(at 50% 0%, hsla(225,39%,30%,1) 0, transparent 50%), radial-gradient(at 100% 0%, hsla(339,49%,30%,1) 0, transparent 50%)',
    color: 'white',
    overflow: 'hidden'
  },
  sidebar: {
    width: '280px',
    background: 'rgba(255, 255, 255, 0.02)',
    backdropFilter: 'blur(20px)',
    borderRight: '1px solid rgba(255, 255, 255, 0.08)',
    padding: '30px 20px',
    display: 'flex',
    flexDirection: 'column',
    overflowY: 'auto'
  },
  brand: { display: 'flex', alignItems: 'center', marginBottom: '30px' },
  logo: { width: '40px', height: '40px', borderRadius: '10px', marginRight: '10px', objectFit: 'contain' },
  brandName: { fontSize: '18px', fontWeight: 'bold' },
  nav: { marginTop: 'auto' },
  navActive: { padding: '12px', background: 'rgba(99, 102, 241, 0.1)', color: '#818cf8', borderRadius: '8px', fontWeight: '600', marginBottom: '10px' },
  navLink: { padding: '12px', color: '#94a3b8', cursor: 'pointer', borderRadius: '10px', transition: 'all 0.3s ease' },
  main: { flex: 1, padding: '40px 60px', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', overflowY: 'auto' },
  mainQuestion: { flex: 1, padding: '40px 60px', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center' },
  
  // Start Screen
  startScreen: { textAlign: 'center', maxWidth: '800px' },
  genieIcon: { fontSize: '80px', marginBottom: '20px' },
  title: { fontSize: '36px', fontWeight: '800', marginBottom: '15px' },
  subtitle: { fontSize: '18px', color: '#94a3b8', marginBottom: '40px' },
  featureGrid: { display: 'grid', gridTemplateColumns: 'repeat(2, 1fr)', gap: '20px', marginBottom: '40px' },
  featureCard: { background: 'rgba(255,255,255,0.03)', border: '1px solid rgba(255,255,255,0.08)', borderRadius: '16px', padding: '25px', textAlign: 'center' },
  featureIcon: { fontSize: '32px', marginBottom: '10px', display: 'block' },
  startButton: { padding: '18px 50px', background: 'linear-gradient(135deg, #6366f1, #8b5cf6)', border: 'none', borderRadius: '12px', color: 'white', fontSize: '18px', fontWeight: '700', cursor: 'pointer', transition: 'all 0.3s ease' },
  
  // Progress Section
  progressSection: { background: 'rgba(255,255,255,0.02)', borderRadius: '12px', padding: '20px', marginBottom: '20px' },
  progressTitle: { fontSize: '14px', color: '#94a3b8', marginBottom: '15px', textTransform: 'uppercase', letterSpacing: '1px' },
  progressBar: { height: '8px', background: 'rgba(255,255,255,0.1)', borderRadius: '4px', overflow: 'hidden', marginBottom: '8px' },
  progressFill: { height: '100%', background: 'linear-gradient(90deg, #6366f1, #8b5cf6)', transition: 'width 0.5s ease' },
  progressText: { fontSize: '13px', color: '#64748b' },
  confidenceMeter: { marginTop: '15px', display: 'flex', alignItems: 'center', gap: '10px', fontSize: '13px', color: '#94a3b8' },
  confidenceBar: { flex: 1, height: '6px', background: 'rgba(255,255,255,0.1)', borderRadius: '3px', overflow: 'hidden' },
  confidenceFill: { height: '100%', transition: 'all 0.5s ease' },
  confidenceValue: { fontWeight: '600', color: 'white', minWidth: '40px' },
  statsSmall: { marginTop: '15px', fontSize: '12px', color: '#64748b', display: 'flex', flexDirection: 'column', gap: '5px' },
  
  // Preview Section
  previewSection: { background: 'rgba(16, 185, 129, 0.1)', borderRadius: '12px', padding: '15px', marginBottom: '20px' },
  previewTitle: { fontSize: '14px', color: '#10b981', marginBottom: '12px' },
  previewCard: { display: 'flex', alignItems: 'center', gap: '10px', padding: '8px', background: 'rgba(255,255,255,0.05)', borderRadius: '8px', marginBottom: '6px' },
  previewRank: { width: '24px', height: '24px', background: '#10b981', borderRadius: '50%', display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: '12px', fontWeight: 'bold' },
  previewName: { fontSize: '12px', color: '#e2e8f0', flex: 1 },
  
  finishButton: { padding: '12px', background: 'rgba(16, 185, 129, 0.2)', color: '#10b981', borderRadius: '8px', cursor: 'pointer', textAlign: 'center', fontWeight: '600', marginBottom: '10px', transition: 'all 0.3s ease' },
  
  // Question Card
  traitIndicator: { padding: '10px 20px', background: 'rgba(99, 102, 241, 0.2)', borderRadius: '20px', marginBottom: '30px', fontSize: '14px', color: '#818cf8' },
  questionCard: { background: 'rgba(255,255,255,0.03)', border: '1px solid rgba(255,255,255,0.08)', borderRadius: '24px', padding: '50px', maxWidth: '700px', width: '100%', transition: 'all 0.3s ease', position: 'relative' },
  questionHeader: { display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '30px' },
  questionNumber: { fontSize: '14px', color: '#6366f1', fontWeight: '600', background: 'rgba(99, 102, 241, 0.1)', padding: '6px 14px', borderRadius: '20px' },
  questionCategory: { fontSize: '13px', color: '#64748b', textTransform: 'uppercase', letterSpacing: '1px' },
  questionText: { fontSize: '24px', fontWeight: '600', lineHeight: '1.5', marginBottom: '40px', color: 'white' },
  optionsContainer: { display: 'flex', flexDirection: 'column', gap: '15px' },
  optionButton: { width: '100%', padding: '18px 24px', background: 'rgba(255,255,255,0.03)', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '12px', color: '#e2e8f0', fontSize: '16px', textAlign: 'left', cursor: 'pointer', transition: 'all 0.3s ease' },
  loadingOverlay: { position: 'absolute', top: 0, left: 0, right: 0, bottom: 0, background: 'rgba(2, 6, 23, 0.9)', borderRadius: '24px', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center' },
  loadingSpinner: { fontSize: '40px', animation: 'spin 1s linear infinite' },
  
  // Results
  resultsHeader: { textAlign: 'center', marginBottom: '40px' },
  statsRow: { display: 'flex', justifyContent: 'center', gap: '40px', marginTop: '30px' },
  stat: { textAlign: 'center' },
  statValue: { fontSize: '32px', fontWeight: '700', color: '#6366f1', display: 'block' },
  statLabel: { fontSize: '14px', color: '#64748b' },
  resultsGrid: { display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '20px', width: '100%', maxWidth: '1200px' },
  resultCard: { background: 'rgba(255,255,255,0.03)', border: '2px solid', borderRadius: '16px', padding: '25px', position: 'relative' },
  resultRank: { position: 'absolute', top: '-12px', right: '20px', background: '#6366f1', padding: '4px 12px', borderRadius: '20px', fontSize: '14px', fontWeight: '600' },
  resultName: { fontSize: '18px', fontWeight: '600', marginBottom: '15px', paddingRight: '50px' },
  resultMatch: { display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '15px' },
  matchBar: { flex: 1, height: '8px', background: 'rgba(255,255,255,0.1)', borderRadius: '4px', overflow: 'hidden' },
  matchFill: { height: '100%', transition: 'width 0.5s ease' },
  matchPercent: { fontWeight: '600', color: '#10b981', minWidth: '45px' },
  resultDesc: { fontSize: '13px', color: '#94a3b8', lineHeight: '1.6', marginBottom: '15px' },
  traitTags: { display: 'flex', flexWrap: 'wrap', gap: '6px' },
  traitTag: { fontSize: '11px', background: 'rgba(99, 102, 241, 0.2)', color: '#818cf8', padding: '4px 10px', borderRadius: '20px' },
  viewFullButton: { marginTop: '30px', padding: '16px 40px', background: 'linear-gradient(135deg, #6366f1, #8b5cf6)', border: 'none', borderRadius: '12px', color: 'white', fontSize: '16px', fontWeight: '600', cursor: 'pointer' },
  
  error: { color: '#ef4444', marginTop: '20px', textAlign: 'center' }
};

export default AdaptiveAssessment;
