import React from 'react';
import './App.css';

function Dashboard({ userName, onLogout, onStart }) {
  return (
    <div className="portal-layout">
      <aside className="portal-sidebar">
        <h2 style={{color: 'var(--brand-primary)', fontWeight: 800, marginBottom: '40px'}}>CoursePro</h2>
        <nav style={{display: 'flex', flexDirection: 'column', gap: '10px'}}>
          <div className="nav-item active" style={{padding: '12px', borderRadius: '8px', background: '#eff6ff', color: 'var(--brand-primary)', fontWeight: 600}}>Dashboard</div>
          <div className="nav-item" style={{padding: '12px', color: 'var(--text-muted)'}}>Career Assessment</div>
          <div className="nav-item" style={{padding: '12px', color: 'var(--text-muted)'}}>My Results</div>
          <div className="nav-item" style={{padding: '12px', color: 'var(--text-muted)'}}>University Catalog</div>
        </nav>
        <button onClick={onLogout} style={{marginTop: 'auto', background: 'none', border: 'none', color: '#ef4444', cursor: 'pointer', textAlign: 'left', padding: '12px'}}>Logout</button>
      </aside>

      <main className="portal-main">
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
      </main>
    </div>
  );
}

export default Dashboard;