import React from 'react';
import './components/style/Dashboard.css';

function ResultsView({ recommendation, profileData, onRetake, onBack }) {
  // Safety check: If data hasn't arrived or is malformed, show a loading state
  if (!recommendation || !recommendation.courses) {
    return (
      <div className="portal-layout">
        <main className="portal-main" style={{ textAlign: 'center', marginTop: '50px' }}>
          <h2>Analyzing your responses...</h2>
          <p>If this takes too long, please check your connection.</p>
          <button onClick={onBack} className="btn-solid">Return to Dashboard</button>
        </main>
      </div>
    );
  }

  return (
    <div className="portal-layout">
      <main className="portal-main">
        <div className="results-header" style={{ marginBottom: '30px' }}>
          <button onClick={onBack} className="link-btn">← Back to Dashboard</button>
          <h1 style={{ marginTop: '20px' }}>Your Career Recommendations</h1>
          <p className="muted-text">Based on your interests and academic profile as a {profileData?.strand || 'student'}.</p>
        </div>

        <div className="results-grid" style={{ display: 'grid', gap: '20px' }}>
          {recommendation.courses.map((item, index) => (
            <div key={index} className="portal-card" style={{ borderLeft: index === 0 ? '5px solid #1e40af' : '1px solid #e2e8f0' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                <div>
                  <span className="activity-badge assessment" style={{ marginBottom: '10px', display: 'inline-block' }}>
                    Rank #{index + 1} Match
                  </span>
                  <h3 style={{ margin: '5px 0', fontSize: '22px', color: '#1e293b' }}>{item.course}</h3>
                </div>
                <div style={{ textAlign: 'right' }}>
                  <div style={{ fontSize: '24px', fontWeight: '800', color: '#1e40af' }}>
                    {/* Render score (e.g., 95%) */}
                    {typeof item.score === 'number' ? `${item.score}%` : item.score}
                  </div>
                  <div className="muted-text" style={{ fontSize: '12px' }}>Match Score</div>
                </div>
              </div>

              <div style={{ marginTop: '15px', padding: '15px', backgroundColor: '#f8fafc', borderRadius: '8px' }}>
                <h4 style={{ margin: '0 0 8px 0', fontSize: '14px', color: '#64748b', textTransform: 'uppercase' }}>Why this fits you:</h4>
                <p style={{ margin: 0, lineHeight: '1.6', color: '#334155' }}>{item.analysis}</p>
              </div>
              
              <div style={{ marginTop: '15px', display: 'flex', gap: '10px' }}>
                <span className="activity-badge profile">{item.status || "Qualified"}</span>
              </div>
            </div>
          ))}
        </div>

        <div style={{ marginTop: '40px', textAlign: 'center', paddingBottom: '50px' }}>
          <p className="muted-text">Not satisfied with these results?</p>
          <button onClick={onRetake} className="btn-solid" style={{ marginRight: '15px' }}>
            Retake Assessment
          </button>
          <button onClick={onBack} className="link-btn">
            Go to Dashboard
          </button>
        </div>
      </main>
    </div>
  );
}

export default ResultsView;