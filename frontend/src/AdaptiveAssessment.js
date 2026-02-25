import React, { useState, useEffect } from 'react';
import NavBar from './components/NavBar';

/**
 * SMART CAREER ASSESSMENT
 * 
 * This component provides an intelligent assessment experience:
 * - Questions appear ONE AT A TIME
 * - Each question is intelligently selected based on your previous answers
 * - You can see courses narrowing down in real-time
 * - User selects 30, 50, or 60 questions
 */
function AdaptiveAssessment({ onBack, onShowResults, maxQuestions = 30, onViewProfile, onViewActivity }) {
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
      fetch(`${process.env.REACT_APP_API_URL}/user/${userId}/academic-info`)
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
      const response = await fetch(`${process.env.REACT_APP_API_URL}/adaptive/start`, {
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
        setTopCoursesPreview(data.first_question.top_courses_preview || []);  // Show initial profile-based courses
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
      const response = await fetch(`${process.env.REACT_APP_API_URL}/adaptive/answer`, {
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
        // Assessment finished - update final values before showing results
        setTraitsDiscovered(data.traits_discovered);
        setConfidence(data.confidence);
        setIsComplete(true);
        setResults(data.recommendations);
        setIsLoading(false);  // Only set loading false after completion
      } else {
        // Update state with new info
        setLastTraitRecorded(data.trait_recorded);
        setCurrentRound(data.current_round);
        setCoursesRemaining(data.courses_remaining);
        setConfidence(data.confidence);
        setTraitsDiscovered(data.traits_discovered);
        setTopCoursesPreview(data.top_courses_preview || []);
        setCanFinishEarly(data.can_finish_early);
        
        // Brief delay for transition effect - IMPORTANT: Keep isLoading true until question is updated
        // to prevent user from clicking again with old question_id
        setTimeout(() => {
          setCurrentQuestion(data.next_question.question);
          setIsTransitioning(false);
          setIsLoading(false);  // Only allow new clicks after question is updated
        }, 300);
      }
    } catch (err) {
      console.error('Submit error:', err);
      setError(err.message);
      setIsTransitioning(false);
      setIsLoading(false);  // Allow retry on error
    }
  };

  // Go to previous question
  const goToPrevious = async () => {
    if (!sessionId || currentRound <= 1) return;

    setIsLoading(true);
    setIsTransitioning(true);

    try {
      const response = await fetch(`${process.env.REACT_APP_API_URL}/adaptive/previous`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ sessionId })
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || 'Failed to go to previous question');
      }

      // Update state with previous question
      setCurrentRound(data.current_round);
      setConfidence(data.confidence);
      setTraitsDiscovered(data.traits_discovered);
      setTopCoursesPreview(data.top_courses_preview || []);
      
      setTimeout(() => {
        setCurrentQuestion(data.next_question);
        setIsTransitioning(false);
        setIsLoading(false);
      }, 300);
    } catch (err) {
      console.error('Previous error:', err);
      setError(err.message);
      setIsTransitioning(false);
      setIsLoading(false);
    }
  };

  // Finish early
  const finishEarly = async () => {
    if (!sessionId) return;

    setIsLoading(true);

    try {
      const response = await fetch(`${process.env.REACT_APP_API_URL}/adaptive/finish`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ sessionId })
      });

      const data = await response.json();

      if (response.ok && data.success) {
        // Update final state values before displaying results
        setTraitsDiscovered(data.traits_discovered);
        setConfidence(data.confidence);
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
      <div style={styles.pageWrapper}>
        {/* TOP NAVIGATION */}
        <NavBar
          activePage={null}
          onNavigate={(page) => {
            if (page === 'home') onBack();
            else if (page === 'profile') onViewProfile && onViewProfile();
            else if (page === 'activity') onViewActivity && onViewActivity();
          }}
        />

        <main style={styles.mainContent}>
          <div style={styles.startScreen}>
            <div style={styles.heroBadge}>
              <span>🧠</span> AI-Powered Analysis
            </div>
            <h1 style={styles.heroTitle}>
              Smart Career <span style={styles.heroGradient}>Assessment</span>
            </h1>
            <p style={styles.heroSubtitle}>
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
      <div style={styles.pageWrapper}>
        <NavBar
          activePage={null}
          onNavigate={(page) => {
            if (page === 'home') onBack();
            else if (page === 'profile') onViewProfile && onViewProfile();
            else if (page === 'activity') onViewActivity && onViewActivity();
          }}
        />

        <main style={styles.mainContent}>
          <div style={styles.resultsHeader}>
            <div style={styles.heroBadge}>
              <span>🎉</span> Assessment Complete
            </div>
            <h1 style={styles.heroTitle}>
              Your <span style={styles.heroGradient}>Recommendations</span>
            </h1>
            <p style={styles.heroSubtitle}>
              Based on {currentRound} questions, here are your personalized career matches
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
            {results.slice(0, 6).map((course, index) => {
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

          {/* Save Results Section */}
          <div style={{
            display: 'flex',
            gap: '16px',
            justifyContent: 'center',
            flexWrap: 'wrap',
            marginTop: '60px',
            marginBottom: '24px'
          }}>
            <button 
              onClick={async () => {
                const userName = localStorage.getItem('userName') || 'Student';
                const userId = localStorage.getItem('userId');
                try {
                  // Fetch user's GWA and Strand from backend
                  const userRes = await fetch(`${process.env.REACT_APP_API_URL}/user/${userId}/academic-info`);
                  const userData = await userRes.json();
                  const userGwa = userData.academic_info?.gwa || null;
                  const userStrand = userData.academic_info?.strand || null;

                  const response = await fetch(`${process.env.REACT_APP_API_URL}/export/pdf`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                      user_name: userName,
                      user_gwa: userGwa,
                      user_strand: userStrand,
                      detected_traits: [],
                      recommendations: results.map(r => ({
                        course_name: r.course_name,
                        description: r.description || '',
                        compatibility_score: r.match_percentage || r.compatibility_score || 75,
                        matched_traits: r.matched_traits || [],
                        reasoning: r.reasoning || ''
                      }))
                    })
                  });
                  if (response.ok) {
                    const blob = await response.blob();
                    const url = window.URL.createObjectURL(blob);
                    const a = document.createElement('a');
                    a.href = url;
                    a.download = `CoursePro_Recommendations_${userName.replace(/\s+/g, '_')}.pdf`;
                    document.body.appendChild(a);
                    a.click();
                    window.URL.revokeObjectURL(url);
                    a.remove();
                  } else {
                    const error = await response.json();
                    console.error('PDF export error:', error);
                    alert('Failed to generate PDF: ' + (error.detail || 'Unknown error'));
                  }
                } catch (err) {
                  console.error('PDF export error:', err);
                  alert('Error generating PDF. Please try again.');
                }
              }}
              style={{
                background: 'rgba(99, 102, 241, 0.1)',
                color: '#a5b4fc',
                padding: '14px 28px',
                borderRadius: '12px',
                border: '1px solid rgba(99, 102, 241, 0.2)',
                fontWeight: '600',
                fontSize: '14px',
                cursor: 'pointer',
                display: 'flex',
                alignItems: 'center',
                gap: '8px'
              }}
            >
              📄 Download PDF
            </button>
            <button 
              onClick={async () => {
                const userEmail = localStorage.getItem('userEmail') || '';
                const email = prompt('Enter email address to receive your recommendations:', userEmail);
                if (email && email.includes('@')) {
                  const userName = localStorage.getItem('userName') || 'Student';
                  const userId = localStorage.getItem('userId');
                  try {
                    // Fetch user's GWA and Strand from backend
                    const userRes = await fetch(`${process.env.REACT_APP_API_URL}/user/${userId}/academic-info`);
                    const userData = await userRes.json();
                    const userGwa = userData.academic_info?.gwa || null;
                    const userStrand = userData.academic_info?.strand || null;
                    
                    fetch(`${process.env.REACT_APP_API_URL}/export/email`, {
                      method: 'POST',
                      headers: { 'Content-Type': 'application/json' },
                      body: JSON.stringify({
                        email: email,
                        user_name: userName,
                        user_gwa: userGwa,
                        user_strand: userStrand,
                        detected_traits: [],
                        recommendations: results.map(r => ({
                          course_name: r.course_name,
                          description: r.description || '',
                          compatibility_score: r.match_percentage || r.compatibility_score || 75,
                          matched_traits: r.matched_traits || [],
                          reasoning: r.reasoning || ''
                        }))
                      })
                    }).then(res => res.json()).then(data => {
                      if (data.success !== false) alert('Email sent successfully!');
                      else alert('Failed to send email: ' + (data.detail || 'Unknown error'));
                    }).catch(err => {
                      console.error('Email error:', err);
                      alert('Error sending email. Please try again.');
                    });
                  } catch (err) {
                    console.error('Error fetching user data:', err);
                    alert('Error sending email. Please try again.');
                  }
                }
              }}
              style={{
                background: 'rgba(99, 102, 241, 0.1)',
                color: '#a5b4fc',
                padding: '14px 28px',
                borderRadius: '12px',
                border: '1px solid rgba(99, 102, 241, 0.2)',
                fontWeight: '600',
                fontSize: '14px',
                cursor: 'pointer',
                display: 'flex',
                alignItems: 'center',
                gap: '8px'
              }}
            >
              ✉️ Send to Email
            </button>
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
    <div style={styles.questionPageWrapper}>
      {/* Compact top bar during questions */}
      <nav style={styles.questionNavbar}>
        <div style={styles.navContainer}>
          <div style={styles.navBrand} onClick={onBack}>
            <img src="/logo.png" alt="CoursePro" style={styles.navLogo} />
            <span style={styles.navBrandName}>CoursePro</span>
          </div>
          
          {/* Progress in navbar */}
          <div style={styles.navProgress}>
            <span style={styles.navProgressText}>Question {currentRound} of {maxRounds}</span>
            <div style={styles.navProgressBar}>
              <div style={{
                ...styles.navProgressFill,
                width: `${(currentRound / maxRounds) * 100}%`
              }} />
            </div>
            <span style={styles.navConfidence}>{confidence}% confidence</span>
          </div>

          <div style={styles.navRight}>
            {canFinishEarly && (
              <button onClick={finishEarly} style={styles.finishBtn}>
                ✅ Finish Early
              </button>
            )}
            <button onClick={onBack} style={styles.exitBtn}>← Exit</button>
          </div>
        </div>
      </nav>

      <main style={styles.questionMain}>
        {/* Side Info Panel */}
        <aside style={styles.infoPanel}>
          <div style={styles.infoPanelSection}>
            <h4 style={styles.infoPanelTitle}>
              <span style={{fontSize: '14px'}}>📊</span> Progress
            </h4>
            <div style={styles.statsSmall}>
              <div style={styles.statItem}>
                <span style={styles.statIcon}>📚</span>
                <span>{coursesRemaining} courses in consideration</span>
              </div>
              <div style={styles.statItem}>
                <span style={styles.statIcon}>🏷️</span>
                <span>{traitsDiscovered} traits discovered</span>
              </div>
            </div>
          </div>

          {/* Top Courses Preview */}
          {topCoursesPreview.length > 0 && (
            <div style={styles.previewSection}>
              <h4 style={styles.infoPanelTitle}>
                <span style={{fontSize: '14px'}}>🔥</span> Top Matches
              </h4>
              {topCoursesPreview.slice(0, 3).map((course, index) => (
                <div key={index} style={styles.previewCard}>
                  <div style={styles.previewRank}>#{index + 1}</div>
                  <div style={styles.previewName}>{course.course_name}</div>
                </div>
              ))}
            </div>
          )}
        </aside>

        {/* Question Card */}
        <div style={styles.questionArea}>
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
              {currentQuestion?.options?.map((option, index) => (
                <button
                  key={option.option_id}
                  onClick={() => submitAnswer(option.option_id)}
                  disabled={isLoading}
                  style={styles.optionButton}
                  onMouseEnter={(e) => {
                    e.currentTarget.style.background = 'rgba(99, 102, 241, 0.15)';
                    e.currentTarget.style.borderColor = '#6366f1';
                    e.currentTarget.style.transform = 'translateX(6px)';
                    e.currentTarget.style.boxShadow = '0 4px 20px rgba(99, 102, 241, 0.2)';
                  }}
                  onMouseLeave={(e) => {
                    e.currentTarget.style.background = 'rgba(30, 41, 59, 0.5)';
                    e.currentTarget.style.borderColor = 'rgba(255,255,255,0.06)';
                    e.currentTarget.style.transform = 'translateX(0)';
                    e.currentTarget.style.boxShadow = 'none';
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

            {/* Navigation buttons */}
            <div style={{
              display: 'flex',
              gap: '12px',
              marginTop: '28px',
              justifyContent: 'center'
            }}>
              <button
                onClick={goToPrevious}
                disabled={isLoading || currentRound <= 1}
                style={{
                  ...styles.navButton,
                  opacity: currentRound <= 1 ? 0.5 : 1,
                  cursor: currentRound <= 1 ? 'not-allowed' : 'pointer'
                }}
              >
                ← Previous Question
              </button>
              <button
                onClick={finishEarly}
                disabled={isLoading || currentRound < minRounds}
                style={{
                  ...styles.finishButton,
                  opacity: currentRound < minRounds ? 0.5 : 1,
                  cursor: currentRound < minRounds ? 'not-allowed' : 'pointer'
                }}
              >
                Finish Early ✓
              </button>
            </div>
          </div>

          {error && <p style={styles.error}>{error}</p>}
        </div>

        {/* Right Trait Panel */}
        <aside style={styles.traitPanel}>
          {lastTraitRecorded && (
            <div style={styles.infoPanelSection}>
              <h4 style={styles.infoPanelTitle}>
                <span style={{fontSize: '14px'}}>✨</span> Trait Recorded
              </h4>
              <div style={styles.traitDisplayContainer}>
                <div style={styles.traitDisplay}>
                  {lastTraitRecorded}
                </div>
              </div>
            </div>
          )}
        </aside>
      </main>
    </div>
  );
}

const styles = {
  // Page wrapper with top nav pattern
  pageWrapper: {
    minHeight: '100vh',
    background: '#050510',
    display: 'flex',
    flexDirection: 'column',
    color: 'white',
    position: 'relative',
    animation: 'fadeIn 0.5s cubic-bezier(0.4, 0, 0.2, 1)',
  },
  questionPageWrapper: {
    minHeight: '100vh',
    background: 'linear-gradient(180deg, #050510 0%, #0a0a1a 50%, #050510 100%)',
    display: 'flex',
    flexDirection: 'column',
    color: 'white',
    position: 'relative',
    animation: 'fadeIn 0.4s cubic-bezier(0.4, 0, 0.2, 1)',
    userSelect: 'none',
    WebkitUserSelect: 'none',
    MozUserSelect: 'none',
    msUserSelect: 'none',
  },
  
  // Navbar
  navbar: {
    position: 'sticky',
    top: 0,
    zIndex: 100,
    background: 'rgba(5, 5, 16, 0.75)',
    backdropFilter: 'blur(30px)',
    borderBottom: '1px solid rgba(255,255,255,0.04)',
    padding: '14px 0',
    transition: 'all 0.35s cubic-bezier(0.4, 0, 0.2, 1)',
  },
  questionNavbar: {
    position: 'sticky',
    top: 0,
    zIndex: 100,
    background: 'rgba(5, 5, 16, 0.92)',
    backdropFilter: 'blur(30px)',
    borderBottom: '1px solid rgba(255,255,255,0.04)',
    padding: '14px 0',
    transition: 'all 0.35s cubic-bezier(0.4, 0, 0.2, 1)',
  },
  navContainer: {
    maxWidth: '1400px',
    margin: '0 auto',
    padding: '0 48px',
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
  },
  navBrand: {
    display: 'flex',
    alignItems: 'center',
    gap: '14px',
    cursor: 'pointer',
  },
  navLogo: {
    width: '48px',
    height: '48px',
    objectFit: 'cover',
    borderRadius: '12px',
    background: 'linear-gradient(135deg, rgba(99, 102, 241, 0.15) 0%, rgba(139, 92, 246, 0.15) 100%)',
    padding: '0',
    boxShadow: '0 0 20px rgba(99, 102, 241, 0.4), 0 0 40px rgba(139, 92, 246, 0.2), inset 0 0 20px rgba(255, 255, 255, 0.05)',
    border: '1px solid rgba(139, 92, 246, 0.3)',
  },
  navBrandName: {
    fontSize: '21px',
    fontWeight: '700',
    background: 'linear-gradient(135deg, #f8fafc 0%, #94a3b8 100%)',
    WebkitBackgroundClip: 'text',
    WebkitTextFillColor: 'transparent',
  },
  navLinks: {
    display: 'flex',
    alignItems: 'center',
    gap: '36px',
  },
  navLink: {
    color: '#94a3b8',
    fontSize: '15px',
    fontWeight: '500',
    cursor: 'pointer',
    transition: 'all 0.35s cubic-bezier(0.4, 0, 0.2, 1)',
    padding: '10px 0',
  },
  navLinkActive: {
    color: '#a5b4fc',
    fontWeight: '600',
    borderBottom: '2px solid #6366f1',
  },
  navRight: {
    display: 'flex',
    alignItems: 'center',
    gap: '14px',
  },
  exitBtn: {
    background: 'rgba(239, 68, 68, 0.08)',
    border: '1px solid rgba(239, 68, 68, 0.15)',
    color: '#f87171',
    padding: '12px 24px',
    borderRadius: '12px',
    fontSize: '14px',
    fontWeight: '600',
    cursor: 'pointer',
    transition: 'all 0.35s cubic-bezier(0.4, 0, 0.2, 1)',
  },
  finishBtn: {
    background: 'rgba(16, 185, 129, 0.12)',
    border: '1px solid rgba(16, 185, 129, 0.25)',
    color: '#34d399',
    padding: '12px 24px',
    borderRadius: '12px',
    fontSize: '14px',
    fontWeight: '600',
    cursor: 'pointer',
    transition: 'all 0.35s cubic-bezier(0.4, 0, 0.2, 1)',
  },
  navButton: {
    background: 'rgba(99, 102, 241, 0.12)',
    border: '1px solid rgba(99, 102, 241, 0.25)',
    color: '#a5b4fc',
    padding: '12px 24px',
    borderRadius: '12px',
    fontSize: '14px',
    fontWeight: '600',
    cursor: 'pointer',
    transition: 'all 0.35s cubic-bezier(0.4, 0, 0.2, 1)',
  },
  finishButton: {
    background: 'rgba(16, 185, 129, 0.12)',
    border: '1px solid rgba(16, 185, 129, 0.25)',
    color: '#34d399',
    padding: '12px 24px',
    borderRadius: '12px',
    fontSize: '14px',
    fontWeight: '600',
    cursor: 'pointer',
    transition: 'all 0.35s cubic-bezier(0.4, 0, 0.2, 1)',
  },
  navProgress: {
    display: 'flex',
    alignItems: 'center',
    gap: '18px',
  },
  navProgressText: {
    fontSize: '14px',
    color: '#94a3b8',
    fontWeight: '500',
  },
  navProgressBar: {
    width: '220px',
    height: '7px',
    background: 'rgba(255,255,255,0.06)',
    borderRadius: '4px',
    overflow: 'hidden',
  },
  navProgressFill: {
    height: '100%',
    background: 'linear-gradient(90deg, #6366f1, #8b5cf6, #a855f7)',
    transition: 'width 0.5s cubic-bezier(0.4, 0, 0.2, 1)',
    borderRadius: '4px',
  },
  navConfidence: {
    fontSize: '14px',
    color: '#a5b4fc',
    fontWeight: '600',
  },
  
  // Main content areas
  mainContent: {
    flex: 1,
    padding: '52px 48px',
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center',
    maxWidth: '1200px',
    margin: '0 auto',
    width: '100%',
    boxSizing: 'border-box',
  },
  questionMain: {
    flex: 1,
    display: 'flex',
    gap: '40px',
    padding: '40px 60px',
    maxWidth: '1300px',
    margin: '0 auto',
    width: '100%',
    boxSizing: 'border-box',
    alignItems: 'flex-start',
    justifyContent: 'center',
  },
  
  // Hero elements
  heroBadge: {
    display: 'inline-flex',
    alignItems: 'center',
    gap: '10px',
    background: 'rgba(99, 102, 241, 0.08)',
    border: '1px solid rgba(99, 102, 241, 0.15)',
    borderRadius: '50px',
    padding: '10px 24px',
    fontSize: '14px',
    color: '#a5b4fc',
    fontWeight: '600',
    marginBottom: '28px',
    backdropFilter: 'blur(10px)',
  },
  heroTitle: {
    fontSize: '48px',
    fontWeight: '800',
    color: '#f8fafc',
    margin: '0 0 18px 0',
    lineHeight: 1.15,
    textAlign: 'center',
    letterSpacing: '-1px',
  },
  heroGradient: {
    background: 'linear-gradient(135deg, #6366f1 0%, #8b5cf6 40%, #a855f7 70%, #c084fc 100%)',
    backgroundSize: '300% 300%',
    WebkitBackgroundClip: 'text',
    WebkitTextFillColor: 'transparent',
    animation: 'gradientShift 6s ease infinite',
  },
  heroSubtitle: {
    color: '#64748b',
    fontSize: '18px',
    marginBottom: '52px',
    lineHeight: 1.7,
    textAlign: 'center',
    maxWidth: '620px',
  },
  
  // Start Screen
  startScreen: { textAlign: 'center', maxWidth: '840px' },
  featureGrid: { display: 'grid', gridTemplateColumns: 'repeat(2, 1fr)', gap: '24px', marginBottom: '52px' },
  featureCard: { background: 'rgba(15, 23, 42, 0.5)', border: '1px solid rgba(255,255,255,0.05)', borderRadius: '24px', padding: '32px', textAlign: 'center', backdropFilter: 'blur(20px)', transition: 'all 0.4s cubic-bezier(0.4, 0, 0.2, 1)' },
  featureIcon: { fontSize: '36px', marginBottom: '18px', display: 'block' },
  startButton: { padding: '20px 64px', background: 'linear-gradient(135deg, #6366f1 0%, #8b5cf6 50%, #a855f7 100%)', backgroundSize: '200% 200%', border: 'none', borderRadius: '16px', color: 'white', fontSize: '17px', fontWeight: '700', cursor: 'pointer', transition: 'all 0.4s cubic-bezier(0.4, 0, 0.2, 1)', boxShadow: '0 10px 35px rgba(99, 102, 241, 0.3)' },
  
  // Question Screen - Info Panel (Left Sidebar)
  infoPanel: {
    width: '260px',
    flexShrink: 0,
    display: 'flex',
    flexDirection: 'column',
    gap: '20px',
    position: 'sticky',
    top: '100px',
  },
  infoPanelSection: {
    background: 'rgba(15, 23, 42, 0.6)',
    backdropFilter: 'blur(20px)',
    border: '1px solid rgba(255,255,255,0.06)',
    borderRadius: '20px',
    padding: '20px',
    transition: 'all 0.4s cubic-bezier(0.4, 0, 0.2, 1)',
  },
  infoPanelTitle: {
    fontSize: '11px',
    color: '#818cf8',
    textTransform: 'uppercase',
    letterSpacing: '2px',
    fontWeight: '700',
    margin: '0 0 16px 0',
    display: 'flex',
    alignItems: 'center',
    gap: '8px',
  },
  statsSmall: { 
    fontSize: '14px', 
    color: '#94a3b8', 
    display: 'flex', 
    flexDirection: 'column', 
    gap: '10px',
    lineHeight: '1.5'
  },
  statItem: {
    display: 'flex',
    alignItems: 'center',
    gap: '10px',
    padding: '8px 12px',
    background: 'rgba(255,255,255,0.02)',
    borderRadius: '10px',
    transition: 'all 0.3s ease',
  },
  statIcon: {
    fontSize: '14px',
  },
  previewSection: { 
    background: 'rgba(16, 185, 129, 0.06)', 
    borderRadius: '20px', 
    padding: '20px', 
    border: '1px solid rgba(16, 185, 129, 0.12)' 
  },
  previewCard: { 
    display: 'flex', 
    alignItems: 'center', 
    gap: '12px', 
    padding: '12px 14px', 
    background: 'rgba(255,255,255,0.03)', 
    borderRadius: '12px', 
    marginBottom: '8px', 
    transition: 'all 0.35s cubic-bezier(0.4, 0, 0.2, 1)' 
  },
  previewRank: { 
    width: '26px', 
    height: '26px', 
    background: 'linear-gradient(135deg, #10b981, #059669)', 
    borderRadius: '8px', 
    display: 'flex', 
    alignItems: 'center', 
    justifyContent: 'center', 
    fontSize: '12px', 
    fontWeight: '700',
    color: 'white'
  },
  previewName: { 
    fontSize: '13px', 
    color: '#e2e8f0', 
    flex: 1, 
    fontWeight: '500',
    lineHeight: '1.3'
  },
  
  // Right Trait Panel
  traitPanel: {
    width: '260px',
    flexShrink: 0,
    display: 'flex',
    flexDirection: 'column',
    gap: '20px',
    position: 'sticky',
    top: '100px',
  },
  traitDisplayContainer: {
    display: 'flex',
    flexDirection: 'column',
    gap: '12px',
  },
  traitDisplay: {
    padding: '14px 16px',
    background: 'rgba(34, 197, 94, 0.08)',
    borderRadius: '12px',
    fontSize: '14px',
    color: '#4ade80',
    fontWeight: '600',
    border: '1px solid rgba(34, 197, 94, 0.25)',
    backdropFilter: 'blur(10px)',
    animation: 'fadeIn 0.4s ease',
    textAlign: 'center',
  },
  
  // Question Area (Main Content)
  questionArea: {
    flex: 1,
    maxWidth: '760px',
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
  },
  traitIndicator: { 
    padding: '12px 24px', 
    background: 'rgba(34, 197, 94, 0.1)', 
    borderRadius: '24px', 
    marginBottom: '24px', 
    fontSize: '14px', 
    color: '#4ade80', 
    fontWeight: '500', 
    border: '1px solid rgba(34, 197, 94, 0.2)', 
    backdropFilter: 'blur(10px)',
    animation: 'fadeIn 0.4s ease'
  },
  questionCard: { 
    background: 'linear-gradient(145deg, rgba(15, 23, 42, 0.7) 0%, rgba(30, 27, 75, 0.5) 100%)', 
    border: '1px solid rgba(255,255,255,0.08)', 
    borderRadius: '28px', 
    padding: '44px 48px', 
    width: '100%', 
    transition: 'all 0.4s cubic-bezier(0.4, 0, 0.2, 1)', 
    position: 'relative', 
    backdropFilter: 'blur(30px)', 
    boxShadow: '0 20px 60px rgba(0, 0, 0, 0.25)' 
  },
  questionHeader: { 
    display: 'flex', 
    justifyContent: 'space-between', 
    alignItems: 'center', 
    marginBottom: '28px' 
  },
  questionNumber: { 
    fontSize: '13px', 
    color: '#a5b4fc', 
    fontWeight: '600', 
    background: 'rgba(99, 102, 241, 0.12)', 
    padding: '10px 20px', 
    borderRadius: '20px',
    border: '1px solid rgba(99, 102, 241, 0.2)'
  },
  questionCategory: { 
    fontSize: '11px', 
    color: '#64748b', 
    textTransform: 'uppercase', 
    letterSpacing: '2px', 
    fontWeight: '600',
    background: 'rgba(255,255,255,0.05)',
    padding: '8px 14px',
    borderRadius: '8px'
  },
  questionText: { 
    fontSize: '22px', 
    fontWeight: '600', 
    lineHeight: '1.5', 
    marginBottom: '32px', 
    color: '#f1f5f9',
    letterSpacing: '-0.3px'
  },
  optionsContainer: { 
    display: 'flex', 
    flexDirection: 'column', 
    gap: '12px' 
  },
  optionButton: { 
    width: '100%', 
    padding: '18px 24px', 
    background: 'rgba(30, 41, 59, 0.5)', 
    border: '2px solid rgba(255,255,255,0.06)', 
    borderRadius: '14px', 
    color: '#e2e8f0', 
    fontSize: '15px', 
    textAlign: 'left', 
    cursor: 'pointer', 
    transition: 'all 0.3s cubic-bezier(0.4, 0, 0.2, 1)', 
    fontWeight: '500',
    display: 'flex',
    alignItems: 'center',
    gap: '14px'
  },
  optionLetter: {
    width: '32px',
    height: '32px',
    background: 'rgba(99, 102, 241, 0.15)',
    border: '1px solid rgba(99, 102, 241, 0.25)',
    borderRadius: '8px',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    fontSize: '14px',
    fontWeight: '700',
    color: '#a5b4fc',
    flexShrink: 0,
  },
  optionText: {
    flex: 1,
    lineHeight: '1.4',
  },
  loadingOverlay: { 
    position: 'absolute', 
    top: 0, 
    left: 0, 
    right: 0, 
    bottom: 0, 
    background: 'rgba(15, 23, 42, 0.95)', 
    borderRadius: '28px', 
    display: 'flex', 
    flexDirection: 'column', 
    alignItems: 'center', 
    justifyContent: 'center', 
    backdropFilter: 'blur(8px)',
    gap: '16px'
  },
  loadingSpinner: { 
    fontSize: '48px', 
    animation: 'spin 1s linear infinite' 
  },
  
  // Results
  resultsHeader: { textAlign: 'center', marginBottom: '52px' },
  statsRow: { display: 'flex', justifyContent: 'center', gap: '56px', marginTop: '36px' },
  stat: { textAlign: 'center', background: 'rgba(15, 23, 42, 0.5)', padding: '28px 36px', borderRadius: '20px', border: '1px solid rgba(255,255,255,0.05)', backdropFilter: 'blur(10px)' },
  statValue: { fontSize: '40px', fontWeight: '800', background: 'linear-gradient(135deg, #6366f1 0%, #8b5cf6 50%, #a855f7 100%)', WebkitBackgroundClip: 'text', WebkitTextFillColor: 'transparent', display: 'block' },
  statLabel: { fontSize: '15px', color: '#64748b', marginTop: '10px', display: 'block' },
  resultsGrid: { display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(340px, 1fr))', gap: '28px', width: '100%', maxWidth: '1200px' },
  resultCard: { background: 'rgba(15, 23, 42, 0.5)', border: '2px solid', borderRadius: '24px', padding: '32px', position: 'relative', backdropFilter: 'blur(20px)', transition: 'all 0.4s cubic-bezier(0.4, 0, 0.2, 1)' },
  resultRank: { position: 'absolute', top: '-14px', right: '28px', background: 'linear-gradient(135deg, #6366f1, #8b5cf6, #a855f7)', padding: '10px 22px', borderRadius: '28px', fontSize: '15px', fontWeight: '700', boxShadow: '0 6px 18px rgba(99, 102, 241, 0.3)' },
  resultName: { fontSize: '20px', fontWeight: '700', marginBottom: '18px', paddingRight: '70px', color: '#f1f5f9' },
  resultMatch: { display: 'flex', alignItems: 'center', gap: '16px', marginBottom: '18px' },
  matchBar: { flex: 1, height: '9px', background: 'rgba(255,255,255,0.06)', borderRadius: '5px', overflow: 'hidden' },
  matchFill: { height: '100%', transition: 'width 0.5s cubic-bezier(0.4, 0, 0.2, 1)', borderRadius: '5px' },
  matchPercent: { fontWeight: '700', color: '#34d399', minWidth: '55px', fontSize: '18px' },
  resultDesc: { fontSize: '15px', color: '#94a3b8', lineHeight: '1.7', marginBottom: '18px' },
  traitTags: { display: 'flex', flexWrap: 'wrap', gap: '10px' },
  traitTag: { fontSize: '13px', background: 'rgba(99, 102, 241, 0.12)', color: '#a5b4fc', padding: '8px 16px', borderRadius: '24px', fontWeight: '500' },
  viewFullButton: { marginTop: '48px', padding: '20px 56px', background: 'linear-gradient(135deg, #6366f1 0%, #8b5cf6 50%, #a855f7 100%)', backgroundSize: '200% 200%', border: 'none', borderRadius: '16px', color: 'white', fontSize: '17px', fontWeight: '700', cursor: 'pointer', boxShadow: '0 10px 35px rgba(99, 102, 241, 0.3)', transition: 'all 0.4s cubic-bezier(0.4, 0, 0.2, 1)' },
  
  error: { color: '#f87171', marginTop: '24px', textAlign: 'center', fontSize: '15px' }
};

export default AdaptiveAssessment;
