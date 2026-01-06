import React, { useState } from 'react';
import './components/style/Dashboard.css';

function Dashboard({ userName, onLogout, onStart, onViewProfile, history }) {
  const [isExpanded, setIsExpanded] = useState(false);

  // Kinukuha lang ang unang 5 history items kapag hindi "Expanded"
  const displayHistory = isExpanded ? history : history?.slice(0, 5);

  return (
    <div className="portal-layout">
      {/* SIDEBAR */}
      <aside className="portal-sidebar">
        <h2 className="brand-title">CoursePro</h2>
        
        <nav className="sidebar-nav">
          <div>
            <p className="category-label">Main Menu</p>
            <div className="nav-item active">Dashboard</div>
          </div>

          <div>
            <p className="category-label">Academics</p>
            <div className="sidebar-nav">
              <div className="nav-item" onClick={onViewProfile}>
                Academic Profile
              </div>
              <div className="nav-item disabled">
                My Activity ({history ? history.length : 0})
              </div>
            </div>
          </div>

          <div>
            <p className="category-label">Support</p>
            <div className="sidebar-nav">
              <div className="nav-item">Help Center</div>
              <div className="nav-item">Feedback</div>
            </div>
          </div>
        </nav>

        <button onClick={onLogout} className="logout-btn">
          Logout
        </button>
      </aside>

      {/* MAIN CONTENT */}
      <main className="portal-main">
        <header className="main-header">
          <h1>Student Overview</h1>
          <p>Welcome back, {userName}. Track your progress and findings here.</p>
        </header>

        {/* ASSESSMENT CALL TO ACTION */}
        <div className="portal-card action-card">
          <div className="action-content">
            <div>
              <h3 style={{ fontSize: '20px', fontWeight: 700, margin: '0 0 10px 0' }}>
                Ready for your recommendation?
              </h3>
              <p className="muted-text" style={{ maxWidth: '500px', margin: 0 }}>
                Launch the assessment to begin the interest questionnaire. 
                We will use your saved Academic Profile for the final analysis.
              </p>
            </div>
            <button className="btn-solid" onClick={onStart}>
              Start New Assessment
            </button>
          </div>
        </div>

        {/* DASHBOARD GRID (History and Summary) */}
        <div className="dashboard-grid">
            
            {/* RECENT ACTIVITY CARD */}
            <div className="portal-card">
               <div className="card-header">
                 <h4 style={{ margin: 0 }}>Recent Activity</h4>
                 {history && history.length > 5 && (
                   <button 
                    className="link-btn"
                    onClick={() => setIsExpanded(!isExpanded)}
                   >
                     {isExpanded ? 'Show Less' : 'View All'}
                   </button>
                 )}
               </div>

               {history && history.length > 0 ? (
                 <div className="activity-list">
                   {displayHistory.map((item, index) => (
                     <div key={index} className="activity-item">
                       <div className="activity-top">
                         <div className="activity-text">
                            {/* Logic para ipakita ang course name */}
                           {item.type === 'assessment' && Array.isArray(item.courses) && item.courses.length > 0
                             ? (typeof item.courses[0] === 'object' ? item.courses[0].course : item.courses[0])
                             : item.courses}
                         </div>
                         
                         <span className={`activity-badge ${item.type === 'profile_update' ? 'profile' : 'assessment'}`}>
                           {item.type === 'profile_update' ? 'Profile' : 'Assessment'}
                         </span>
                       </div>
                       <div className="activity-date">{item.date}</div>
                     </div>
                   ))}
                 </div>
               ) : (
                 <p className="muted-text">No history found.</p>
               )}
            </div>
            
            {/* ACCOUNT SUMMARY CARD */}
            <div className="portal-card">
               <h4 style={{ margin: '0 0 10px 0' }}>Account Summary</h4>
               <p className="muted-text">Your account is synchronized and up to date.</p>
               
               {history && history.length > 0 && (
                 <div className="summary-box">
                   <div className="summary-success">
                      <span style={{ marginRight: '8px' }}>✓</span>
                      {history.filter(h => h.type === 'assessment').length} Assessment(s) Recorded
                   </div>
                   <p className="summary-date">
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