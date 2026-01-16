import React, { useState, useEffect } from 'react';

function MyActivity({ onBack }) {
  const [activityHistory, setActivityHistory] = useState([]);
  const [loading, setLoading] = useState(true);
  const [expandedAttempt, setExpandedAttempt] = useState(null);
  const [expandedTab, setExpandedTab] = useState({}); // Track which tab is expanded per attempt

  // Fetch assessment history
  useEffect(() => {
    const userId = localStorage.getItem('userId');
    if (userId) {
      fetch(`http://localhost:8000/user/${userId}/assessment-history`)
        .then(res => res.json())
        .then(data => {
          setActivityHistory(data.history || []);
          setLoading(false);
        })
        .catch(err => {
          console.error('Error fetching assessment history:', err);
          setLoading(false);
        });
    } else {
      setLoading(false);
    }
  }, []);

  const formatDate = (dateString) => {
    if (!dateString) return 'N/A';
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'short',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  const getTierLabel = (questionCount) => {
    if (questionCount <= 30) return '🚀 Quick';
    if (questionCount <= 80) return '⭐ Standard';
    return '🎯 Comprehensive';
  };

  return (
    <div style={styles.container}>
      {/* SIDEBAR */}
      <aside style={styles.sidebar}>
        <div style={styles.brandContainer}>
          <div style={styles.logoIcon}>C</div>
          <h2 style={styles.brandName}>CoursePro</h2>
        </div>
        
        <nav style={styles.nav}>
          <div style={styles.categoryLabel}>Main Menu</div>
          <div style={styles.navItem} onClick={onBack}
            onMouseEnter={(e) => { e.target.style.background = 'rgba(255, 255, 255, 0.05)'; e.target.style.color = '#cbd5e1'; e.target.style.transform = 'translateX(4px)'; }}
            onMouseLeave={(e) => { e.target.style.background = 'transparent'; e.target.style.color = '#94a3b8'; e.target.style.transform = 'translateX(0)'; }}
          >📊 Dashboard</div>

          <div style={styles.categoryLabel}>Academics</div>
          <div style={{...styles.navItem, ...styles.navActive}}>📂 My Activity</div>
        </nav>
      </aside>

      {/* MAIN CONTENT */}
      <main style={styles.mainContent}>
        <header style={styles.header}>
          <div style={styles.headerTop}>
            <button onClick={onBack} style={styles.backButton}>← Back</button>
            <h1 style={styles.headerTitle}>My Activity</h1>
          </div>
          <p style={styles.headerSubtitle}>View all your previous assessments and results</p>
        </header>

        {/* CONTENT */}
        <div style={styles.contentArea}>
          {loading ? (
            <div style={styles.loadingContainer}>
              <p>Loading your activity history...</p>
            </div>
          ) : activityHistory.length === 0 ? (
            <div style={styles.emptyState}>
              <div style={styles.emptyIcon}>📋</div>
              <h3>No Assessment History Yet</h3>
              <p>You haven't taken any assessments yet. Start one to see your results here!</p>
            </div>
          ) : (
            <div style={styles.activityList}>
              {activityHistory.map((activity, index) => (
                <div key={activity.attempt_id} style={styles.activityCard}>
                  {/* HEADER ROW - Always visible */}
                  <div 
                    style={styles.activityHeader}
                    onClick={() => setExpandedAttempt(expandedAttempt === activity.attempt_id ? null : activity.attempt_id)}
                  >
                    <div style={styles.activityInfo}>
                      <div style={styles.assessmentNumber}>#{activityHistory.length - index}</div>
                      <div>
                        <h3 style={styles.activityTitle}>{activity.test_name}</h3>
                        <p style={styles.activityDate}>{formatDate(activity.taken_at)}</p>
                      </div>
                    </div>
                    <div style={styles.activityStats}>
                      <div style={styles.statBadge}>
                        <span style={styles.statLabel}>Questions</span>
                        <span style={styles.statValue}>{activity.questions_answered}</span>
                      </div>
                      <div style={styles.statBadge}>
                        <span style={styles.statLabel}>Tier</span>
                        <span style={styles.statValue}>{getTierLabel(activity.questions_answered)}</span>
                      </div>
                      <div style={styles.statBadge}>
                        <span style={styles.statLabel}>Results</span>
                        <span style={styles.statValue}>{activity.recommendation_count}</span>
                      </div>
                      <button style={{
                        ...styles.expandButton,
                        transform: expandedAttempt === activity.attempt_id ? 'rotate(180deg)' : 'rotate(0deg)'
                      }}>▼</button>
                    </div>
                  </div>

                  {/* EXPANDED CONTENT - Tabs for Answers and Results */}
                  {expandedAttempt === activity.attempt_id && (
                    <div style={styles.activityDetails}>
                      {/* TAB NAVIGATION */}
                      <div style={styles.tabNavigation}>
                        <button 
                          style={{
                            ...styles.tabButton,
                            ...(expandedTab[activity.attempt_id] !== 'results' ? styles.tabButtonActive : {})
                          }}
                          onClick={() => setExpandedTab({...expandedTab, [activity.attempt_id]: 'answers'})}
                        >
                          📋 Your Answers ({activity.questions_answered})
                        </button>
                        <button 
                          style={{
                            ...styles.tabButton,
                            ...(expandedTab[activity.attempt_id] === 'results' ? styles.tabButtonActive : {})
                          }}
                          onClick={() => setExpandedTab({...expandedTab, [activity.attempt_id]: 'results'})}
                        >
                          🎯 Recommended Courses ({activity.recommendation_count})
                        </button>
                      </div>

                      {/* ANSWERS TAB */}
                      {expandedTab[activity.attempt_id] !== 'results' && (
                        <div style={styles.tabContent}>
                          {activity.answered_questions && activity.answered_questions.length > 0 ? (
                            <div style={styles.answersList}>
                              {activity.answered_questions.map((qa, qIndex) => (
                                <div key={qa.question_id} style={styles.answerCard}>
                                  <div style={styles.answerNumber}>{qIndex + 1}</div>
                                  <div style={styles.answerContent}>
                                    <div style={styles.categoryTag}>{qa.category}</div>
                                    <h5 style={styles.questionText}>{qa.question_text}</h5>
                                    <div style={styles.selectedAnswer}>
                                      <span style={styles.labelSmall}>Your choice:</span>
                                      <p style={styles.answerText}>{qa.chosen_option_text}</p>
                                      {qa.trait_tag && (
                                        <span style={styles.traitBadge}>{qa.trait_tag}</span>
                                      )}
                                    </div>
                                  </div>
                                </div>
                              ))}
                            </div>
                          ) : (
                            <div style={styles.noResults}>
                              <p>No answers recorded for this assessment</p>
                            </div>
                          )}
                        </div>
                      )}

                      {/* RESULTS TAB */}
                      {expandedTab[activity.attempt_id] === 'results' && (
                        <div style={styles.tabContent}>
                          {activity.recommendation_count === 0 ? (
                            <div style={styles.noResults}>
                              <p>Results pending or no courses recommended</p>
                            </div>
                          ) : (
                            <div style={styles.recommendationsList}>
                              {activity.recommended_courses.map((course, idx) => (
                                <div key={course.course_id} style={styles.courseCard}>
                                  <div style={styles.courseNumber}>{idx + 1}</div>
                                  <div style={styles.courseContent}>
                                    <h5 style={styles.courseName}>{course.course_name}</h5>
                                    <p style={styles.courseDescription}>{course.description}</p>
                                    {course.reasoning && (
                                      <div style={styles.reasoningBox}>
                                        <strong>Why recommended:</strong>
                                        <p>{course.reasoning}</p>
                                      </div>
                                    )}
                                  </div>
                                </div>
                              ))}
                            </div>
                          )}
                        </div>
                      )}
                    </div>
                  )}
                </div>
              ))}
            </div>
          )}
        </div>
      </main>
    </div>
  );
}

const styles = {
  container: {
    display: 'flex',
    height: '100vh',
    backgroundColor: 'rgb(2, 6, 23)',
    color: '#e2e8f0',
    fontFamily: "'Segoe UI', Tahoma, Geneva, Verdana, sans-serif",
    overflow: 'hidden'
  },

  // SIDEBAR
  sidebar: {
    width: '220px',
    backgroundColor: 'rgba(15, 23, 42, 0.8)',
    borderRight: '1px solid rgba(148, 163, 184, 0.1)',
    padding: '20px 0',
    display: 'flex',
    flexDirection: 'column',
    overflowY: 'auto',
  },
  brandContainer: {
    display: 'flex',
    alignItems: 'center',
    gap: '10px',
    padding: '0 20px',
    marginBottom: '30px',
  },
  logoIcon: {
    width: '40px',
    height: '40px',
    background: 'linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%)',
    borderRadius: '8px',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    fontSize: '20px',
    fontWeight: 'bold',
  },
  brandName: {
    fontSize: '18px',
    fontWeight: '700',
    margin: 0,
    color: '#f1f5f9',
  },
  nav: {
    flex: 1,
    paddingBottom: '20px',
  },
  categoryLabel: {
    fontSize: '11px',
    fontWeight: '700',
    textTransform: 'uppercase',
    color: '#94a3b8',
    padding: '15px 20px 10px',
    letterSpacing: '0.5px',
  },
  navItem: {
    padding: '12px 20px',
    cursor: 'pointer',
    color: '#94a3b8',
    fontSize: '14px',
    fontWeight: '500',
    transition: 'all 0.2s ease',
    userSelect: 'none',
  },
  navActive: {
    background: 'rgba(99, 102, 241, 0.1)',
    color: '#6366f1',
    borderRight: '3px solid #6366f1',
  },

  // MAIN CONTENT
  mainContent: {
    flex: 1,
    display: 'flex',
    flexDirection: 'column',
    overflow: 'hidden',
  },
  header: {
    padding: '30px 40px',
    borderBottom: '1px solid rgba(148, 163, 184, 0.1)',
    background: 'linear-gradient(to right, rgba(15, 23, 42, 0.5), rgba(30, 41, 59, 0.3))',
  },
  headerTop: {
    display: 'flex',
    alignItems: 'center',
    gap: '20px',
    marginBottom: '10px',
  },
  backButton: {
    padding: '8px 16px',
    background: 'rgba(99, 102, 241, 0.1)',
    border: '1px solid rgba(99, 102, 241, 0.3)',
    color: '#6366f1',
    borderRadius: '6px',
    cursor: 'pointer',
    fontSize: '14px',
    fontWeight: '500',
    transition: 'all 0.2s ease',
  },
  headerTitle: {
    margin: 0,
    fontSize: '28px',
    fontWeight: '700',
    color: '#f1f5f9',
  },
  headerSubtitle: {
    margin: '0',
    fontSize: '13px',
    color: '#94a3b8',
  },

  contentArea: {
    flex: 1,
    padding: '30px 40px',
    overflowY: 'auto',
  },

  // EMPTY STATE
  loadingContainer: {
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    height: '300px',
    color: '#94a3b8',
    fontSize: '16px',
  },
  emptyState: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center',
    height: '300px',
    color: '#94a3b8',
    textAlign: 'center',
  },
  emptyIcon: {
    fontSize: '60px',
    marginBottom: '20px',
  },

  // ACTIVITY LIST
  activityList: {
    display: 'flex',
    flexDirection: 'column',
    gap: '15px',
  },
  activityCard: {
    background: 'linear-gradient(135deg, rgba(30, 41, 59, 0.6) 0%, rgba(15, 23, 42, 0.6) 100%)',
    border: '1px solid rgba(148, 163, 184, 0.1)',
    borderRadius: '12px',
    overflow: 'hidden',
    transition: 'all 0.3s ease',
  },
  activityHeader: {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    padding: '20px',
    cursor: 'pointer',
    transition: 'all 0.2s ease',
  },
  activityInfo: {
    display: 'flex',
    alignItems: 'flex-start',
    gap: '15px',
    flex: 1,
  },
  assessmentNumber: {
    background: 'rgba(99, 102, 241, 0.2)',
    color: '#6366f1',
    width: '40px',
    height: '40px',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    borderRadius: '8px',
    fontSize: '14px',
    fontWeight: '700',
    flexShrink: 0,
  },
  activityTitle: {
    margin: '0 0 5px 0',
    fontSize: '16px',
    fontWeight: '600',
    color: '#f1f5f9',
  },
  activityDate: {
    margin: '0',
    fontSize: '12px',
    color: '#94a3b8',
  },

  activityStats: {
    display: 'flex',
    alignItems: 'center',
    gap: '15px',
  },
  statBadge: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    gap: '4px',
    padding: '8px 12px',
    background: 'rgba(99, 102, 241, 0.1)',
    borderRadius: '6px',
  },
  statLabel: {
    fontSize: '11px',
    color: '#94a3b8',
    fontWeight: '500',
    textTransform: 'uppercase',
  },
  statValue: {
    fontSize: '14px',
    fontWeight: '700',
    color: '#6366f1',
  },
  expandButton: {
    background: 'transparent',
    border: 'none',
    color: '#6366f1',
    cursor: 'pointer',
    fontSize: '16px',
    padding: '8px',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    transition: 'transform 0.3s ease',
  },

  // EXPANDED DETAILS
  activityDetails: {
    padding: '20px',
    borderTop: '1px solid rgba(148, 163, 184, 0.1)',
    background: 'rgba(15, 23, 42, 0.5)',
  },
  noResults: {
    padding: '20px',
    textAlign: 'center',
    color: '#94a3b8',
    fontSize: '13px',
    fontStyle: 'italic',
  },

  recommendationsList: {
    display: 'flex',
    flexDirection: 'column',
    gap: '12px',
  },
  resultsTitle: {
    margin: '0 0 15px 0',
    fontSize: '14px',
    fontWeight: '600',
    color: '#cbd5e1',
    textTransform: 'uppercase',
    letterSpacing: '0.5px',
  },
  courseCard: {
    display: 'flex',
    gap: '15px',
    padding: '15px',
    background: 'rgba(30, 41, 59, 0.5)',
    borderRadius: '8px',
    borderLeft: '3px solid #6366f1',
  },
  courseNumber: {
    background: '#6366f1',
    color: 'white',
    width: '32px',
    height: '32px',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    borderRadius: '6px',
    fontSize: '14px',
    fontWeight: '700',
    flexShrink: 0,
  },
  courseContent: {
    flex: 1,
  },
  courseName: {
    margin: '0 0 5px 0',
    fontSize: '14px',
    fontWeight: '600',
    color: '#f1f5f9',
  },
  courseDescription: {
    margin: '0 0 10px 0',
    fontSize: '13px',
    color: '#cbd5e1',
    lineHeight: '1.5',
  },
  reasoningBox: {
    background: 'rgba(99, 102, 241, 0.1)',
    padding: '10px',
    borderRadius: '6px',
    fontSize: '12px',
    borderLeft: '2px solid rgba(99, 102, 241, 0.3)',
  },

  // TAB NAVIGATION
  tabNavigation: {
    display: 'flex',
    gap: '10px',
    marginBottom: '15px',
    borderBottom: '1px solid rgba(148, 163, 184, 0.1)',
    paddingBottom: '0',
  },
  tabButton: {
    padding: '12px 16px',
    background: 'transparent',
    border: 'none',
    color: '#94a3b8',
    cursor: 'pointer',
    fontSize: '13px',
    fontWeight: '500',
    transition: 'all 0.2s ease',
    borderBottom: '2px solid transparent',
    marginBottom: '-1px',
  },
  tabButtonActive: {
    color: '#6366f1',
    borderBottomColor: '#6366f1',
  },

  // TAB CONTENT
  tabContent: {
    paddingTop: '15px',
  },

  // ANSWERS LIST
  answersList: {
    display: 'flex',
    flexDirection: 'column',
    gap: '12px',
  },
  answerCard: {
    display: 'flex',
    gap: '15px',
    padding: '15px',
    background: 'rgba(30, 41, 59, 0.5)',
    borderRadius: '8px',
    borderLeft: '3px solid #10b981',
  },
  answerNumber: {
    background: '#10b981',
    color: 'white',
    width: '32px',
    height: '32px',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    borderRadius: '6px',
    fontSize: '14px',
    fontWeight: '700',
    flexShrink: 0,
  },
  answerContent: {
    flex: 1,
  },
  categoryTag: {
    display: 'inline-block',
    background: 'rgba(99, 102, 241, 0.2)',
    color: '#6366f1',
    padding: '4px 10px',
    borderRadius: '4px',
    fontSize: '11px',
    fontWeight: '600',
    textTransform: 'uppercase',
    marginBottom: '8px',
  },
  questionText: {
    margin: '0 0 10px 0',
    fontSize: '14px',
    fontWeight: '600',
    color: '#f1f5f9',
    lineHeight: '1.5',
  },
  selectedAnswer: {
    background: 'rgba(16, 185, 129, 0.1)',
    padding: '10px',
    borderRadius: '6px',
    borderLeft: '2px solid rgba(16, 185, 129, 0.3)',
  },
  labelSmall: {
    fontSize: '11px',
    color: '#94a3b8',
    fontWeight: '600',
    textTransform: 'uppercase',
    display: 'block',
    marginBottom: '4px',
  },
  answerText: {
    margin: '0 0 8px 0',
    fontSize: '13px',
    color: '#cbd5e1',
    fontWeight: '500',
  },
  traitBadge: {
    display: 'inline-block',
    background: '#10b981',
    color: 'white',
    padding: '4px 10px',
    borderRadius: '4px',
    fontSize: '11px',
    fontWeight: '600',
  },
};

export default MyActivity;
