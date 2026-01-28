import React, { useState, useEffect } from 'react';
import './components/style/Dashboard.css';

// Inline styles to ensure dark theme visibility
const styles = {
  expandedContent: {
    padding: '20px',
    background: '#0f172a'
  },
  cardItem: {
    display: 'flex',
    gap: '15px',
    padding: '15px',
    background: '#1e293b',
    borderRadius: '8px',
    marginBottom: '10px',
    borderLeft: '4px solid #6366f1'
  },
  cardItemAnswer: {
    display: 'flex',
    gap: '15px',
    padding: '15px',
    background: '#1e293b',
    borderRadius: '8px',
    marginBottom: '10px',
    borderLeft: '4px solid #10b981'
  },
  badge: {
    width: '32px',
    height: '32px',
    borderRadius: '6px',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    fontWeight: '700',
    fontSize: '12px',
    flexShrink: 0,
    background: '#6366f1',
    color: '#ffffff'
  },
  badgeAnswer: {
    width: '32px',
    height: '32px',
    borderRadius: '6px',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    fontWeight: '700',
    fontSize: '12px',
    flexShrink: 0,
    background: '#10b981',
    color: '#ffffff'
  },
  categoryBadge: {
    padding: '4px 10px',
    borderRadius: '6px',
    fontSize: '10px',
    fontWeight: '800',
    textTransform: 'uppercase',
    background: 'rgba(99, 102, 241, 0.2)',
    color: '#818cf8'
  },
  questionText: {
    fontWeight: '600',
    margin: '8px 0',
    color: '#e2e8f0',
    fontSize: '14px'
  },
  courseTitle: {
    fontSize: '16px',
    margin: 0,
    color: '#f1f5f9',
    fontWeight: '600'
  },
  courseDesc: {
    margin: '5px 0',
    color: '#94a3b8',
    fontSize: '14px'
  },
  reasoningBox: {
    marginTop: '10px',
    padding: '12px 15px',
    background: '#0f172a',
    borderRadius: '8px',
    border: '1px solid rgba(255, 255, 255, 0.1)'
  },
  reasoningLabel: {
    fontSize: '11px',
    fontWeight: '600',
    color: '#94a3b8',
    textTransform: 'uppercase',
    letterSpacing: '0.5px',
    display: 'block',
    marginBottom: '4px'
  },
  reasoningText: {
    color: '#e2e8f0',
    fontSize: '14px',
    margin: 0
  }
};

function MyActivity({ onBack }) {
  const [activityHistory, setActivityHistory] = useState([]);
  const [loading, setLoading] = useState(true);
  const [expandedAttempt, setExpandedAttempt] = useState(null);
  const [expandedTab, setExpandedTab] = useState({});

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
          console.error('Error fetching history:', err);
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
      year: 'numeric', month: 'short', day: 'numeric',
      hour: '2-digit', minute: '2-digit'
    });
  };

  const getTierLabel = (count) => {
    if (count <= 30) return '🚀 Quick';
    if (count <= 80) return '⭐ Standard';
    return '🎯 Comprehensive';
  };

  return (
    <div className="dashboard-wrapper">
      {/* SIDEBAR (Reusable styles from Dashboard) */}
      <aside className="portal-sidebar">
        <div className="sidebar-brand">
          <img src="/logo.svg" alt="CoursePro" className="brand-logo" style={{ width: '40px', height: '40px', borderRadius: '10px' }} />
          <span className="brand-name">CoursePro</span>
        </div>
        
        <nav className="sidebar-nav">
          <div className="nav-category">Main Menu</div>
          <div className="nav-item" onClick={onBack}>📊 Dashboard</div>

          <div className="nav-category">Academics</div>
          <div className="nav-item active">📂 My Activity</div>
        </nav>
      </aside>

      {/* MAIN CONTENT */}
      <main className="portal-main">
        <header className="results-header-section">
          <button onClick={onBack} className="logout-btn">← Back</button>
          <h1 className="header-title" style={{ marginTop: '10px' }}>My Activity</h1>
          <p className="header-subtitle">View all your previous assessments and results</p>
        </header>

        <div className="activity-content-area">
          {loading ? (
            <div className="empty-state-container">Loading your activity history...</div>
          ) : activityHistory.length === 0 ? (
            <div className="empty-state-container">
              <span className="empty-icon-big">📋</span>
              <h3>No Assessment History Yet</h3>
              <p>Start an assessment to see your results here!</p>
            </div>
          ) : (
            <div className="activity-list">
              {activityHistory.map((activity, index) => (
                <div key={activity.attempt_id} className="activity-card">
                  {/* CARD HEADER */}
                  <div 
                    className="activity-card-header"
                    onClick={() => setExpandedAttempt(expandedAttempt === activity.attempt_id ? null : activity.attempt_id)}
                  >
                    <div style={{ display: 'flex', gap: '15px', alignItems: 'center' }}>
                      <div className="item-number-badge">#{activityHistory.length - index}</div>
                      <div>
                        <h3 className="course-name">{activity.test_name}</h3>
                        <p className="header-subtitle">{formatDate(activity.taken_at)}</p>
                      </div>
                    </div>
                    
                    <div style={{ display: 'flex', gap: '10px', alignItems: 'center' }}>
                       <span className="activity-badge badge-assessment">{activity.questions_answered} Qs</span>
                       <span className="activity-badge badge-profile">{getTierLabel(activity.questions_answered)}</span>
                       <span style={{ 
                         transform: expandedAttempt === activity.attempt_id ? 'rotate(180deg)' : 'rotate(0deg)',
                         transition: '0.3s'
                       }}>▼</span>
                    </div>
                  </div>

                  {/* TOP RECOMMENDED COURSE PREVIEW */}
                  {activity.top_course && (
                    <div style={{
                      padding: '12px 15px',
                      background: 'linear-gradient(135deg, rgba(100, 150, 255, 0.1), rgba(150, 100, 255, 0.1))',
                      borderTop: '1px solid rgba(100, 150, 255, 0.2)',
                      borderBottom: expandedAttempt === activity.attempt_id ? '1px solid rgba(100, 150, 255, 0.2)' : 'none'
                    }}>
                      <div style={{ display: 'flex', gap: '10px', alignItems: 'center' }}>
                        <span style={{ fontSize: '18px' }}>⭐</span>
                        <div style={{ flex: 1 }}>
                          <p style={{ margin: '0 0 2px 0', fontSize: '12px', color: '#888' }}>Top Recommended</p>
                          <p style={{ margin: 0, fontSize: '14px', fontWeight: '600', color: '#fff' }}>
                            {activity.top_course.course_name}
                          </p>
                        </div>
                      </div>
                    </div>
                  )}

                  {/* EXPANDED CONTENT */}
                  {expandedAttempt === activity.attempt_id && (
                    <div style={styles.expandedContent}>
                      <div className="activity-tabs-nav">
                        <button 
                          className={`activity-tab-btn ${expandedTab[activity.attempt_id] !== 'results' ? 'active' : ''}`}
                          onClick={() => setExpandedTab({...expandedTab, [activity.attempt_id]: 'answers'})}
                        >📋 Answers</button>
                        <button 
                          className={`activity-tab-btn ${expandedTab[activity.attempt_id] === 'results' ? 'active' : ''}`}
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
              ))}
            </div>
          )}
        </div>
      </main>
    </div>
  );
}

export default MyActivity;