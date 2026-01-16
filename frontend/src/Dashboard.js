import React, { useState } from 'react';
import './components/style/Dashboard.css';

function Dashboard({ userName, onLogout, onStart, onViewProfile, history }) {
  const [isExpanded, setIsExpanded] = useState(false);
  const displayHistory = isExpanded ? history : history?.slice(0, 5);

  return (
    <div className="dashboard-wrapper">
      {/* SIDEBAR */}
      <aside className="portal-sidebar">
        <div className="brand-container">
          <div className="logo-icon">C</div>
          <h2 style={{ fontSize: '18px', fontWeight: '700', margin: 0 }}>CoursePro</h2>
        </div>
        
        <nav style={{ flex: 1 }}>
          <div className="nav-category">Main Menu</div>
          <div className="nav-item active">📊 Dashboard</div>

          <div className="nav-category">Academics</div>
          <div className="nav-item" onClick={onViewProfile}>👤 Academic Profile</div>
          <div className="nav-item" style={{ cursor: 'default', opacity: 0.7 }}>
            📂 My Activity ({history ? history.length : 0})
          </div>

          <div className="nav-category">Support</div>
          <div className="nav-item">❓ Help Center</div>
          <div className="nav-item">💬 Feedback</div>
        </nav>

        <button onClick={onLogout} className="logout-btn">
          Logout
        </button>
      </aside>

      {/* MAIN CONTENT */}
      <main className="portal-main">
        <header style={{ marginBottom: '30px' }}>
          <h1 className="header-title">Student Overview</h1>
          <p className="header-subtitle">Welcome back, {userName}. Track your progress and findings here.</p>
        </header>

        {/* ASSESSMENT CALL TO ACTION */}
        <div className="action-card">
          <div>
            <h3 style={{ fontSize: '20px', fontWeight: '700', margin: '0 0 10px 0' }}>Ready for your recommendation?</h3>
            <p style={{ color: '#cbd5e1', fontSize: '14px', maxWidth: '500px', margin: 0, lineHeight: '1.5' }}>
              Launch the assessment to begin the interest questionnaire. 
              We will use your saved Academic Profile for the final analysis.
            </p>
          </div>
          <button className="start-btn" onClick={onStart}>
            Start New Assessment
          </button>
        </div>

        {/* DASHBOARD GRID */}
        <div className="dashboard-grid">
          {/* RECENT ACTIVITY CARD */}
          <div className="portal-card">
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '20px' }}>
              <h4 style={{ fontSize: '17px', fontWeight: '700', margin: 0 }}>Recent Activity</h4>
              {history && history.length > 5 && (
                <button 
                  style={{ background: 'none', border: 'none', color: '#6366f1', fontWeight: '700', fontSize: '12px', cursor: 'pointer' }}
                  onClick={() => setIsExpanded(!isExpanded)}
                >
                  {isExpanded ? 'Show Less' : 'View All'}
                </button>
              )}
            </div>

            {history && history.length > 0 ? (
              <div>
                {displayHistory.map((item, index) => (
                  <div key={index} className="activity-item">
                    <div>
                      <div style={{ fontSize: '14px', fontWeight: '600', color: 'white' }}>
                        {item.type === 'assessment' && Array.isArray(item.courses) && item.courses.length > 0
                          ? (typeof item.courses[0] === 'object' ? item.courses[0].course : item.courses[0])
                          : item.courses}
                      </div>
                      <div style={{ fontSize: '12px', color: '#64748b', marginTop: '4px' }}>{item.date}</div>
                    </div>
                    <span className={`activity-badge ${item.type === 'profile_update' ? 'badge-profile' : 'badge-assessment'}`}>
                      {item.type === 'profile_update' ? 'Profile' : 'Assessment'}
                    </span>
                  </div>
                ))}
              </div>
            ) : (
              <p style={{ color: '#64748b', fontSize: '14px' }}>No history found.</p>
            )}
          </div>

          {/* ACCOUNT SUMMARY CARD */}
          <div className="portal-card">
            <h4 style={{ fontSize: '17px', fontWeight: '700', margin: 0 }}>Account Summary</h4>
            <p style={{ color: '#64748b', fontSize: '14px', marginTop: '10px' }}>Your account is synchronized and up to date.</p>
            
            {history && history.length > 0 && (
              <div style={{ marginTop: '20px', padding: '15px', background: 'rgba(219, 36, 36, 0.02)', borderRadius: '12px' }}>
                <div style={{ fontSize: '14px', fontWeight: '600', color: '#e2e8f0', display: 'flex', alignItems: 'center' }}>
                  <span style={{ marginRight: '8px', color: '#10b981' }}>✓</span>
                  {history.filter(h => h.type === 'assessment').length} Assessment(s) Recorded
                </div>
                <p style={{ fontSize: '12px', color: '#64748b', marginTop: '8px' }}>
                  Latest activity logged on {history[0].date}
                </p>
              </div>
            )}
          </div>
        </div>
      </main>
    </div>
  );
}

export default Dashboard;