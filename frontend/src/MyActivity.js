import React, { useState, useEffect } from 'react';

// Add keyframes for pulse animation
const pulseKeyframes = `
  @keyframes pulse {
    0% { transform: scale(1); opacity: 1; }
    50% { transform: scale(1.2); opacity: 0.7; }
    100% { transform: scale(1); opacity: 1; }
  }
`;

// Inject the keyframes into the document
if (typeof document !== 'undefined') {
  const styleSheet = document.createElement('style');
  styleSheet.textContent = pulseKeyframes;
  document.head.appendChild(styleSheet);
}

// Inline styles for modern top-nav layout
const styles = {
  pageWrapper: {
    minHeight: '100vh',
    background: '#050510',
    display: 'flex',
    flexDirection: 'column',
    position: 'relative',
  },
  navbar: {
    position: 'sticky',
    top: 0,
    zIndex: 100,
    background: 'rgba(5, 5, 16, 0.8)',
    backdropFilter: 'blur(20px)',
    borderBottom: '1px solid rgba(255,255,255,0.05)',
    padding: '12px 0',
  },
  navContainer: {
    maxWidth: '1400px',
    margin: '0 auto',
    padding: '0 40px',
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
  },
  navBrand: {
    display: 'flex',
    alignItems: 'center',
    gap: '12px',
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
    fontSize: '20px',
    fontWeight: '700',
    background: 'linear-gradient(135deg, #f8fafc 0%, #94a3b8 100%)',
    WebkitBackgroundClip: 'text',
    WebkitTextFillColor: 'transparent',
  },
  navLinks: {
    display: 'flex',
    alignItems: 'center',
    gap: '32px',
  },
  navLink: {
    color: '#94a3b8',
    fontSize: '14px',
    fontWeight: '500',
    cursor: 'pointer',
    transition: 'color 0.2s ease',
    padding: '8px 0',
  },
  navLinkActive: {
    color: '#a5b4fc',
    fontWeight: '600',
    borderBottom: '2px solid #6366f1',
  },
  navRight: {
    display: 'flex',
    alignItems: 'center',
    gap: '16px',
  },
  backBtn: {
    background: 'rgba(99, 102, 241, 0.1)',
    border: '1px solid rgba(99, 102, 241, 0.2)',
    color: '#a5b4fc',
    padding: '10px 20px',
    borderRadius: '10px',
    fontSize: '14px',
    fontWeight: '600',
    cursor: 'pointer',
    transition: 'all 0.2s ease',
  },
  mainContent: {
    flex: 1,
    padding: '48px 40px',
    maxWidth: '1400px',
    margin: '0 auto',
    width: '100%',
    boxSizing: 'border-box',
  },
  heroHeader: {
    textAlign: 'center',
    marginBottom: '48px',
  },
  heroBadge: {
    display: 'inline-flex',
    alignItems: 'center',
    gap: '8px',
    background: 'rgba(99, 102, 241, 0.1)',
    border: '1px solid rgba(99, 102, 241, 0.2)',
    borderRadius: '50px',
    padding: '8px 20px',
    fontSize: '13px',
    color: '#a5b4fc',
    fontWeight: '600',
    marginBottom: '24px',
  },
  heroTitle: {
    fontSize: '42px',
    fontWeight: '800',
    color: '#f8fafc',
    margin: '0 0 16px 0',
    lineHeight: 1.2,
  },
  heroGradient: {
    background: 'linear-gradient(135deg, #6366f1 0%, #8b5cf6 50%, #a855f7 100%)',
    WebkitBackgroundClip: 'text',
    WebkitTextFillColor: 'transparent',
  },
  heroSubtitle: {
    color: '#64748b',
    fontSize: '16px',
    maxWidth: '600px',
    margin: '0 auto',
    lineHeight: 1.6,
  },
  statsBar: {
    display: 'grid',
    gridTemplateColumns: 'repeat(3, 1fr)',
    gap: '24px',
    marginBottom: '48px',
    maxWidth: '900px',
    margin: '0 auto 48px',
  },
  statCard: {
    background: 'rgba(15, 23, 42, 0.6)',
    backdropFilter: 'blur(20px)',
    border: '1px solid rgba(255,255,255,0.06)',
    borderRadius: '16px',
    padding: '24px',
    textAlign: 'center',
  },
  statValue: {
    display: 'block',
    fontSize: '32px',
    fontWeight: '800',
    background: 'linear-gradient(135deg, #6366f1 0%, #a855f7 100%)',
    WebkitBackgroundClip: 'text',
    WebkitTextFillColor: 'transparent',
  },
  statLabel: {
    display: 'block',
    fontSize: '13px',
    color: '#64748b',
    marginTop: '8px',
  },
  activityList: {
    display: 'flex',
    flexDirection: 'column',
    gap: '20px',
    maxWidth: '1000px',
    margin: '0 auto',
  },
  activityCard: {
    background: 'rgba(15, 23, 42, 0.6)',
    backdropFilter: 'blur(20px)',
    border: '1px solid rgba(255,255,255,0.06)',
    borderRadius: '20px',
    overflow: 'hidden',
    transition: 'all 0.3s ease',
    position: 'relative',
  },
  activityCardUnseen: {
    border: '1px solid rgba(99, 102, 241, 0.5)',
    boxShadow: '0 0 20px rgba(99, 102, 241, 0.15)',
  },
  unseenDot: {
    position: 'absolute',
    top: '12px',
    right: '12px',
    width: '10px',
    height: '10px',
    borderRadius: '50%',
    background: 'linear-gradient(135deg, #6366f1 0%, #a855f7 100%)',
    boxShadow: '0 0 10px rgba(99, 102, 241, 0.5)',
    animation: 'pulse 2s infinite',
  },
  activityCardHeader: {
    padding: '24px',
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    cursor: 'pointer',
    transition: 'background 0.2s ease',
  },
  itemNumberBadge: {
    width: '48px',
    height: '48px',
    borderRadius: '14px',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    fontWeight: '800',
    fontSize: '16px',
    background: 'linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%)',
    color: '#ffffff',
    boxShadow: '0 4px 16px rgba(99, 102, 241, 0.3)',
  },
  courseName: {
    fontSize: '18px',
    fontWeight: '700',
    color: '#f1f5f9',
    margin: 0,
  },
  activityBadge: {
    padding: '6px 14px',
    borderRadius: '8px',
    fontSize: '12px',
    fontWeight: '600',
  },
  badgeAssessment: {
    background: 'rgba(99, 102, 241, 0.15)',
    color: '#a5b4fc',
  },
  badgeProfile: {
    background: 'rgba(16, 185, 129, 0.15)',
    color: '#10b981',
  },
  badgeConfidence: {
    background: 'rgba(139, 92, 246, 0.15)',
    color: '#d8b4fe',
  },
  expandedContent: {
    padding: '24px',
    background: 'linear-gradient(135deg, rgba(15, 23, 42, 0.9) 0%, rgba(30, 27, 75, 0.5) 100%)',
    borderTop: '1px solid rgba(255,255,255,0.04)',
  },
  tabsNav: {
    display: 'flex',
    gap: '12px',
    marginBottom: '20px',
  },
  tabBtn: {
    padding: '10px 20px',
    borderRadius: '10px',
    border: '1px solid rgba(255,255,255,0.08)',
    background: 'rgba(255,255,255,0.02)',
    color: '#94a3b8',
    fontSize: '13px',
    fontWeight: '600',
    cursor: 'pointer',
    transition: 'all 0.2s ease',
  },
  tabBtnActive: {
    background: 'linear-gradient(135deg, rgba(99, 102, 241, 0.2) 0%, rgba(139, 92, 246, 0.15) 100%)',
    borderColor: 'rgba(99, 102, 241, 0.3)',
    color: '#a5b4fc',
  },
  cardItem: {
    display: 'flex',
    gap: '16px',
    padding: '18px',
    background: 'rgba(30, 41, 59, 0.5)',
    borderRadius: '12px',
    marginBottom: '12px',
    borderLeft: '4px solid #6366f1',
    transition: 'all 0.2s ease'
  },
  cardItemAnswer: {
    display: 'flex',
    gap: '16px',
    padding: '18px',
    background: 'rgba(16, 185, 129, 0.05)',
    borderRadius: '12px',
    marginBottom: '12px',
    borderLeft: '4px solid #10b981',
    transition: 'all 0.2s ease'
  },
  badge: {
    width: '36px',
    height: '36px',
    borderRadius: '10px',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    fontWeight: '700',
    fontSize: '13px',
    flexShrink: 0,
    background: 'linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%)',
    color: '#ffffff',
    boxShadow: '0 4px 12px rgba(99, 102, 241, 0.25)'
  },
  badgeAnswer: {
    width: '36px',
    height: '36px',
    borderRadius: '10px',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    fontWeight: '700',
    fontSize: '13px',
    flexShrink: 0,
    background: 'linear-gradient(135deg, #10b981 0%, #34d399 100%)',
    color: '#ffffff',
    boxShadow: '0 4px 12px rgba(16, 185, 129, 0.25)'
  },
  categoryBadge: {
    padding: '5px 12px',
    borderRadius: '6px',
    fontSize: '10px',
    fontWeight: '700',
    textTransform: 'uppercase',
    letterSpacing: '0.5px',
    background: 'rgba(99, 102, 241, 0.15)',
    color: '#a5b4fc'
  },
  questionText: {
    fontWeight: '600',
    margin: '10px 0',
    color: '#e2e8f0',
    fontSize: '14px',
    lineHeight: '1.5'
  },
  courseTitle: {
    fontSize: '16px',
    margin: 0,
    color: '#f1f5f9',
    fontWeight: '600'
  },
  courseDesc: {
    margin: '6px 0',
    color: '#64748b',
    fontSize: '14px'
  },
  reasoningBox: {
    marginTop: '14px',
    padding: '16px 18px',
    background: 'rgba(15, 23, 42, 0.6)',
    borderRadius: '12px',
    border: '1px solid rgba(255, 255, 255, 0.04)'
  },
  reasoningLabel: {
    fontSize: '11px',
    fontWeight: '700',
    color: '#64748b',
    textTransform: 'uppercase',
    letterSpacing: '1px',
    display: 'block',
    marginBottom: '8px'
  },
  reasoningText: {
    color: '#cbd5e1',
    fontSize: '14px',
    margin: 0,
    lineHeight: '1.6'
  },
  emptyState: {
    textAlign: 'center',
    padding: '80px 40px',
    background: 'rgba(15, 23, 42, 0.6)',
    backdropFilter: 'blur(20px)',
    border: '1px solid rgba(255,255,255,0.06)',
    borderRadius: '24px',
    maxWidth: '500px',
    margin: '0 auto',
  },
  emptyIcon: {
    fontSize: '64px',
    marginBottom: '24px',
    display: 'block',
  },
  emptyTitle: {
    fontSize: '22px',
    fontWeight: '700',
    color: '#f1f5f9',
    margin: '0 0 12px 0',
  },
  emptyText: {
    color: '#64748b',
    fontSize: '15px',
    margin: 0,
  },
  topCoursePreview: {
    padding: '16px 24px',
    background: 'linear-gradient(135deg, rgba(99, 102, 241, 0.1), rgba(139, 92, 246, 0.1))',
    borderTop: '1px solid rgba(99, 102, 241, 0.15)',
    display: 'flex',
    alignItems: 'center',
    gap: '12px',
  },
  topCourseLabel: {
    margin: '0 0 2px 0',
    fontSize: '11px',
    color: '#64748b',
    textTransform: 'uppercase',
    letterSpacing: '0.5px',
  },
  topCourseName: {
    margin: 0,
    fontSize: '15px',
    fontWeight: '600',
    color: '#f1f5f9',
  }
};

function MyActivity({ onBack }) {
  const [activityHistory, setActivityHistory] = useState([]);
  const [loading, setLoading] = useState(true);
  const [expandedAttempt, setExpandedAttempt] = useState(null);
  const [expandedTab, setExpandedTab] = useState({});
  const [seenActivities, setSeenActivities] = useState([]);

  useEffect(() => {
    const userId = localStorage.getItem('userId');
    if (userId) {
      // Load previously seen activities
      const savedSeen = JSON.parse(localStorage.getItem(`seenActivities_${userId}`) || '[]');
      setSeenActivities(savedSeen);
      
      fetch(`http://localhost:8000/user/${userId}/assessment-history`)
        .then(res => res.json())
        .then(data => {
          setActivityHistory(data.history || []);
          setLoading(false);
        })
        .catch(err => {
          console.error('Error fetching history:', err);
          setLoading(false);
        });
    } else {
      setLoading(false);
    }
  }, []);

  // Mark an activity as seen when clicked/expanded
  const markAsSeen = (attemptId) => {
    const userId = localStorage.getItem('userId');
    if (!userId) return;
    
    if (!seenActivities.includes(attemptId)) {
      const newSeenActivities = [...seenActivities, attemptId];
      setSeenActivities(newSeenActivities);
      localStorage.setItem(`seenActivities_${userId}`, JSON.stringify(newSeenActivities));
    }
  };

  // Handle activity card click - expand and mark as seen
  const handleActivityClick = (attemptId) => {
    setExpandedAttempt(expandedAttempt === attemptId ? null : attemptId);
    markAsSeen(attemptId);
  };

  const formatDate = (dateString) => {
    if (!dateString) return 'N/A';
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', {
      year: 'numeric', month: 'short', day: 'numeric',
      hour: '2-digit', minute: '2-digit'
    });
  };

  const getTierLabel = (count) => {
    if (count <= 30) return '⚡ Quick';
    if (count <= 80) return '📊 Standard';
    return '🎯 Deep';
  };

  const totalQuestions = activityHistory.reduce((sum, a) => sum + (a.questions_answered || 0), 0);
  const avgQuestions = activityHistory.length > 0 ? Math.round(totalQuestions / activityHistory.length) : 0;

  return (
    <div style={styles.pageWrapper}>
      {/* TOP NAVIGATION BAR */}
      <nav style={styles.navbar}>
        <div style={styles.navContainer}>
          <div style={styles.navBrand}>
            <img src="/logo.png" alt="CoursePro" style={styles.navLogo} />
            <span style={styles.navBrandName}>CoursePro</span>
          </div>
          
          <div style={styles.navLinks}>
            <span style={styles.navLink} onClick={onBack}>Dashboard</span>
            <span style={{...styles.navLink, ...styles.navLinkActive}}>My Activity</span>
          </div>

          <div style={styles.navRight}>
            <button onClick={onBack} style={styles.backBtn}>← Back to Dashboard</button>
          </div>
        </div>
      </nav>

      {/* MAIN CONTENT */}
      <main style={styles.mainContent}>
        {/* Hero Header */}
        <div style={styles.heroHeader}>
          <div style={styles.heroBadge}>
            <span>📂</span> Assessment History
          </div>
          <h1 style={styles.heroTitle}>
            My <span style={styles.heroGradient}>Activity</span>
          </h1>
          <p style={styles.heroSubtitle}>
            Review all your previous assessments, answers, and course recommendations.
          </p>
        </div>

        {/* Stats Bar */}
        <div style={styles.statsBar}>
          <div style={styles.statCard}>
            <span style={styles.statValue}>{activityHistory.length}</span>
            <span style={styles.statLabel}>Total Assessments</span>
          </div>
          <div style={styles.statCard}>
            <span style={styles.statValue}>{totalQuestions}</span>
            <span style={styles.statLabel}>Questions Answered</span>
          </div>
          <div style={styles.statCard}>
            <span style={styles.statValue}>{avgQuestions}</span>
            <span style={styles.statLabel}>Avg per Assessment</span>
          </div>
        </div>

        {/* Activity List */}
        {loading ? (
          <div style={styles.emptyState}>
            <span style={styles.emptyIcon}>⏳</span>
            <h3 style={styles.emptyTitle}>Loading your activity...</h3>
          </div>
        ) : activityHistory.length === 0 ? (
          <div style={styles.emptyState}>
            <span style={styles.emptyIcon}>📋</span>
            <h3 style={styles.emptyTitle}>No Assessment History Yet</h3>
            <p style={styles.emptyText}>Start an assessment to see your results here!</p>
          </div>
        ) : (
          <div style={styles.activityList}>
            {activityHistory.map((activity, index) => {
              const isUnseen = !seenActivities.includes(activity.attempt_id);
              return (
              <div 
                key={activity.attempt_id} 
                style={{
                  ...styles.activityCard,
                  ...(isUnseen ? styles.activityCardUnseen : {})
                }}
              >
                {/* Unseen indicator dot */}
                {isUnseen && <div style={styles.unseenDot} />}
                
                {/* CARD HEADER */}
                <div 
                  style={styles.activityCardHeader}
                  onClick={() => handleActivityClick(activity.attempt_id)}
                >
                  <div style={{ display: 'flex', gap: '16px', alignItems: 'center' }}>
                    <div style={styles.itemNumberBadge}>#{activityHistory.length - index}</div>
                    <div>
                      <h3 style={styles.courseName}>{activity.test_name}</h3>
                      <p style={{ margin: '4px 0 0 0', fontSize: '13px', color: '#64748b' }}>{formatDate(activity.taken_at)}</p>
                    </div>
                  </div>
                  
                  <div style={{ display: 'flex', gap: '10px', alignItems: 'center' }}>
                     <span style={{...styles.activityBadge, ...styles.badgeAssessment}}>{activity.max_questions || activity.questions_answered} Q</span>
                     <span style={{...styles.activityBadge, ...styles.badgeProfile}}>{activity.traits_found || 0} Traits</span>
                     <span style={{...styles.activityBadge, ...styles.badgeConfidence}}>{activity.confidence_score || 0}%</span>
                     <span style={{ 
                       color: '#64748b',
                       transform: expandedAttempt === activity.attempt_id ? 'rotate(180deg)' : 'rotate(0deg)',
                       transition: '0.3s'
                     }}>▼</span>
                  </div>
                </div>

                {/* TOP RECOMMENDED COURSE PREVIEW */}
                {activity.top_course && (
                  <div style={styles.topCoursePreview}>
                    <span style={{ fontSize: '20px' }}>⭐</span>
                    <div style={{ flex: 1 }}>
                      <p style={styles.topCourseLabel}>Top Recommended</p>
                      <p style={styles.topCourseName}>{activity.top_course.course_name}</p>
                    </div>
                  </div>
                )}

                {/* EXPANDED CONTENT */}
                {expandedAttempt === activity.attempt_id && (
                  <div style={styles.expandedContent}>
                    <div style={styles.tabsNav}>
                      <button 
                        style={{...styles.tabBtn, ...(expandedTab[activity.attempt_id] !== 'results' ? styles.tabBtnActive : {})}}
                        onClick={() => setExpandedTab({...expandedTab, [activity.attempt_id]: 'answers'})}
                      >📋 Answers</button>
                      <button 
                        style={{...styles.tabBtn, ...(expandedTab[activity.attempt_id] === 'results' ? styles.tabBtnActive : {})}}
                        onClick={() => setExpandedTab({...expandedTab, [activity.attempt_id]: 'results'})}
                      >🎯 Recommended Courses</button>
                    </div>

                    <div style={{ marginTop: '15px' }}>
                      {expandedTab[activity.attempt_id] !== 'results' ? (
                        activity.answered_questions?.map((qa, qIdx) => (
                          <div key={qIdx} style={styles.cardItemAnswer}>
                            <div style={styles.badgeAnswer}>{qIdx + 1}</div>
                            <div style={{ flex: 1 }}>
                              <span style={styles.categoryBadge}>{qa.category}</span>
                              <h5 style={styles.questionText}>{qa.question_text}</h5>
                              <div style={styles.reasoningBox}>
                                <span style={styles.reasoningLabel}>Your Choice:</span>
                                <p style={styles.reasoningText}>{qa.chosen_option_text}</p>
                              </div>
                            </div>
                          </div>
                        ))
                      ) : (
                        activity.recommended_courses?.length > 0 ? (
                          activity.recommended_courses.map((course, cIdx) => (
                            <div key={cIdx} style={styles.cardItem}>
                              <div style={styles.badge}>{cIdx + 1}</div>
                              <div style={{ flex: 1 }}>
                                <h5 style={styles.courseTitle}>{course.course_name}</h5>
                                <p style={styles.courseDesc}>{course.description}</p>
                                <div style={styles.reasoningBox}>
                                  <p style={styles.reasoningText}><strong style={{color: '#94a3b8'}}>Why:</strong> {course.reasoning || 'Based on your assessment responses'}</p>
                                </div>
                              </div>
                            </div>
                          ))
                        ) : (
                          <div style={{ textAlign: 'center', padding: '40px', color: '#94a3b8' }}>
                            <p>No course recommendations found for this assessment.</p>
                          </div>
                        )
                      )}
                    </div>
                  </div>
                )}
              </div>
            );
            })}
          </div>
        )}
      </main>
    </div>
  );
}

export default MyActivity;
