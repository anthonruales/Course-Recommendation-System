import React, { useState } from 'react'; // 1. I-import ang useState
import PersonalAcademicInfo from './PersonalAcademicInfo';
import './App.css';

function Dashboard({ userName, onLogout, onStart }) {
  // 2. State para malaman kung anong section ang ipapakita
  const [activeTab, setActiveTab] = useState('overview');

  return (
    <div className="portal-layout">
      <aside className="portal-sidebar">
        <h2 style={{color: 'var(--brand-primary)', fontWeight: 800, marginBottom: '40px'}}>CoursePro</h2>
        <nav style={{display: 'flex', flexDirection: 'column', gap: '10px'}}>
<<<<<<< Updated upstream
          <div className="nav-item active" style={{padding: '12px', borderRadius: '8px', background: '#eff6ff', color: 'var(--brand-primary)', fontWeight: 600}}>Dashboard</div>
          <div className="nav-item" style={{padding: '12px', color: 'var(--text-muted)'}}>Career Assessment</div>
          <div className="nav-item" style={{padding: '12px', color: 'var(--text-muted)'}}>My Results</div>
          <div className="nav-item" style={{padding: '12px', color: 'var(--text-muted)'}}>University Catalog</div>
=======
          
          {/* Dashboard Tab */}
          <div 
            className={`nav-item ${activeTab === 'overview' ? 'active' : ''}`} 
            onClick={() => setActiveTab('overview')}
            style={{
              padding: '12px', 
              borderRadius: '8px', 
              background: activeTab === 'overview' ? '#eff6ff' : 'transparent', 
              color: activeTab === 'overview' ? 'var(--brand-primary)' : 'var(--text-muted)', 
              fontWeight: 600,
              cursor: 'pointer'
            }}
          >
            Dashboard
          </div>

          {/* Personal Academic Info Tab - NGAYON AY CLICKABLE NA */}
          <div 
            className={`nav-item ${activeTab === 'academic' ? 'active' : ''}`} 
            onClick={() => setActiveTab('academic')}
            style={{
              padding: '12px', 
              borderRadius: '8px',
              background: activeTab === 'academic' ? '#eff6ff' : 'transparent',
              color: activeTab === 'academic' ? 'var(--brand-primary)' : 'var(--text-muted)',
              fontWeight: activeTab === 'academic' ? 600 : 400,
              cursor: 'pointer'
            }}
          >
            Personal Academic Info
          </div>

          <div className="nav-item" style={{padding: '12px', color: 'var(--text-muted)', cursor: 'pointer'}}>
            My Results
          </div>
>>>>>>> Stashed changes
        </nav>
        <button onClick={onLogout} style={{marginTop: 'auto', background: 'none', border: 'none', color: '#ef4444', cursor: 'pointer', textAlign: 'left', padding: '12px'}}>Logout</button>
      </aside>

      <main className="portal-main">
        {/* 3. DYNAMIC CONTENT: Dito magbabago ang screen base sa activeTab */}
        
        {activeTab === 'overview' ? (
          /* --- DASHBOARD VIEW --- */
          <>
            <header style={{marginBottom: '40px'}}>
              <h1 style={{fontSize: '28px', fontWeight: 700}}>Student Overview</h1>
              <p style={{color: 'var(--text-muted)'}}>Welcome back, {userName}. Track your progress and findings here.</p>
            </header>

            <div className="portal-card">
              <div style={{display: 'flex', justifyContent: 'space-between', alignItems: 'center'}}>
                <div>
                  <h3 style={{fontSize: '20px', fontWeight: 700, margin: '0 0 10px 0'}}>Ready for your recommendation?</h3>
                  <p style={{color: 'var(--text-muted)', maxWidth: '500px'}}>Our Rule-Based Decision Tree will analyze your GWA and strand to find the best fit for your future.</p>
                </div>
                <button className="btn-solid" onClick={onStart}>Start New Assessment</button>
              </div>
            </div>

            <div style={{marginTop: '40px', display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '20px'}}>
               <div className="portal-card">
                  <h4 style={{margin: '0 0 10px 0'}}>Recent Activity</h4>
                  <p style={{fontSize: '14px', color: 'var(--text-muted)'}}>No history found.</p>
               </div>
               <div className="portal-card">
                  <h4 style={{margin: '0 0 10px 0'}}>System Notifications</h4>
                  <p style={{fontSize: '14px', color: 'var(--text-muted)'}}>System is running normally.</p>
               </div>
            </div>
          </>
        ) : (
          /* --- PERSONAL ACADEMIC INFO VIEW --- */
          <PersonalAcademicInfo />
        )}
      </main>
    </div>
  );
}

export default Dashboard;