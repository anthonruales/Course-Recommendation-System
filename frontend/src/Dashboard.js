import React, { useState } from 'react';
import './App.css';

function Dashboard({ userName, onLogout, onStart, onViewProfile, history }) {
  const [isExpanded, setIsExpanded] = useState(false);

  // Limits the view to 5 items unless "View All" is clicked
  const displayHistory = isExpanded ? history : history?.slice(0, 5);

  return (
    <div className="portal-layout">
      <aside className="portal-sidebar">
        <h2 style={{color: 'var(--brand-primary)', fontWeight: 800, marginBottom: '40px'}}>CoursePro</h2>
        <nav style={{display: 'flex', flexDirection: 'column', gap: '10px'}}>
          <div className="nav-item active" style={{padding: '12px', borderRadius: '8px', background: '#eff6ff', color: 'var(--brand-primary)', fontWeight: 600, cursor: 'pointer'}}>
            Dashboard
          </div>
          <div className="nav-item" onClick={onViewProfile} style={{padding: '12px', color: 'var(--text-muted)', cursor: 'pointer'}}>
            Academic Profile
          </div>
          <div className="nav-item" style={{padding: '12px', color: 'var(--text-muted)', cursor: 'default'}}>
            My Activity ({history ? history.length : 0})
          </div>
        </nav>
        <button onClick={onLogout} style={{marginTop: 'auto', background: 'none', border: 'none', color: '#ef4444', cursor: 'pointer', textAlign: 'left', padding: '12px'}}>
          Logout
        </button>
      </aside>

      <main className="portal-main">
        <header style={{marginBottom: '40px'}}>
          <h1 style={{fontSize: '28px', fontWeight: 700}}>Student Overview</h1>
          <p style={{color: 'var(--text-muted)'}}>Welcome back, {userName}. Track your progress and findings here.</p>
        </header>

        {/* Action Card */}
        <div className="portal-card">
          <div style={{display: 'flex', justifyContent: 'space-between', alignItems: 'center'}}>
            <div>
              <h3 style={{fontSize: '20px', fontWeight: 700, margin: '0 0 10px 0'}}>Ready for your recommendation?</h3>
              <p style={{color: 'var(--text-muted)', maxWidth: '500px'}}>
                Launch the assessment to begin the interest questionnaire. We will use your saved Academic Profile for the final analysis.
              </p>
            </div>
            <button className="btn-solid" onClick={onStart}>Start New Assessment</button>
          </div>
        </div>

        <div style={{marginTop: '40px', display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '20px', alignItems: 'start'}}>
            {/* Left Column: Activity Feed */}
            <div className="portal-card">
               <div style={{display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '15px'}}>
                 <h4 style={{margin: 0}}>Recent Activity</h4>
                 {history && history.length > 5 && (
                   <button 
                    onClick={() => setIsExpanded(!isExpanded)}
                    style={{background: 'none', border: 'none', color: '#3b82f6', cursor: 'pointer', fontSize: '13px', fontWeight: 600}}
                   >
                     {isExpanded ? 'Show Less' : 'View All'}
                   </button>
                 )}
               </div>

               {history && history.length > 0 ? (
                 <div style={{display: 'flex', flexDirection: 'column', gap: '12px'}}>
                   {displayHistory.map((item, index) => (
                     <div key={index} style={{paddingBottom: '10px', borderBottom: '1px solid #f1f5f9'}}>
                       <div style={{display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start'}}>
                         <div style={{
                           fontWeight: 600, 
                           color: item.type === 'profile_update' ? '#64748b' : '#1e293b', 
                           fontSize: '14px',
                           maxWidth: '70%'
                         }}>
                           {/* item.courses contains the course name OR the Profile update message */}
                           {Array.isArray(item.courses) ? item.courses.join(", ") : item.courses}
                         </div>
                         
                         <span style={{
                           fontSize: '10px',
                           padding: '2px 8px',
                           borderRadius: '12px',
                           fontWeight: 700,
                           textTransform: 'uppercase',
                           backgroundColor: item.type === 'profile_update' ? '#f1f5f9' : '#e0f2fe',
                           color: item.type === 'profile_update' ? '#64748b' : '#0369a1'
                         }}>
                           {item.type === 'profile_update' ? 'Profile' : 'Assessment'}
                         </span>
                       </div>
                       <div style={{fontSize: '12px', color: '#94a3b8', marginTop: '4px'}}>{item.date}</div>
                     </div>
                   ))}
                 </div>
               ) : (
                 <p style={{fontSize: '14px', color: 'var(--text-muted)'}}>No history found.</p>
               )}
            </div>
            
            {/* Right Column: System Stats */}
            <div className="portal-card">
               <h4 style={{margin: '0 0 10px 0'}}>Account Summary</h4>
               <p style={{fontSize: '14px', color: 'var(--text-muted)'}}>Your account is synchronized and up to date.</p>
               {history && history.length > 0 && (
                 <div style={{marginTop: '15px', padding: '12px', borderRadius: '8px', background: '#f8fafc', border: '1px solid #e2e8f0'}}>
                   <div style={{display: 'flex', alignItems: 'center', gap: '8px', color: '#10b981', marginBottom: '8px'}}>
                      <span style={{fontSize: '16px'}}>✓</span>
                      <span style={{fontSize: '13px', fontWeight: 600}}>{history.filter(h => h.type === 'assessment').length} Assessment(s) Recorded</span>
                   </div>
                   <p style={{fontSize: '12px', color: '#64748b', margin: 0}}>
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