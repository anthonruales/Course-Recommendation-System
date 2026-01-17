import React, { useState, useEffect } from 'react';
import './components/style/Dashboard.css';

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
          <div className="brand-logo">C</div>
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

                  {/* EXPANDED CONTENT */}
                  {expandedAttempt === activity.attempt_id && (
                    <div style={{ padding: '20px', background: 'rgba(0,0,0,0.2)' }}>
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

                      <div className="tab-content">
                        {expandedTab[activity.attempt_id] !== 'results' ? (
                          activity.answered_questions?.map((qa, qIdx) => (
                            <div key={qIdx} className="detail-item-card answer">
                              <div className="item-number-badge answer">{qIdx + 1}</div>
                              <div style={{ flex: 1 }}>
                                <span className="activity-badge badge-assessment" style={{ fontSize: '10px' }}>{qa.category}</span>
                                <h5 className="reasoning-text" style={{ fontWeight: '600', margin: '5px 0' }}>{qa.question_text}</h5>
                                <div className="reasoning-box">
                                  <span className="reasoning-label">Your Choice:</span>
                                  <p className="reasoning-text">{qa.chosen_option_text}</p>
                                </div>
                              </div>
                            </div>
                          ))
                        ) : (
                          activity.recommended_courses?.map((course, cIdx) => (
                            <div key={cIdx} className="detail-item-card">
                              <div className="item-number-badge">{cIdx + 1}</div>
                              <div style={{ flex: 1 }}>
                                <h5 className="course-title" style={{ fontSize: '16px', margin: 0 }}>{course.course_name}</h5>
                                <p className="header-subtitle" style={{ margin: '5px 0' }}>{course.description}</p>
                                <div className="reasoning-box">
                                  <p className="reasoning-text"><strong>Why:</strong> {course.reasoning}</p>
                                </div>
                              </div>
                            </div>
                          ))
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