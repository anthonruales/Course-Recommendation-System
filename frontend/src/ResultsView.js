import React from 'react';
import './components/style/Dashboard.css';

function ResultsView({ recommendation, onRetake, onBack }) {
  // Loading state
  if (!recommendation || !recommendation.recommendations) {
    return (
      <div className="dashboard-wrapper">
        <main className="portal-main" style={{ textAlign: 'center', justifyContent: 'center', display: 'flex', flexDirection: 'column' }}>
          <h2 className="header-title">Analyzing your responses...</h2>
          <p className="header-subtitle">If this takes too long, please check your connection.</p>
          <button onClick={onBack} className="start-btn" style={{ marginTop: '20px', alignSelf: 'center' }}>
            Return to Dashboard
          </button>
        </main>
      </div>
    );
  }

  const calculatePercentage = (score) => {
    const maxScore = 20;
    const percentage = Math.min(100, Math.max(0, (score / maxScore) * 100));
    return Math.round(percentage);
  };

  const topTraits = recommendation.detected_traits || [];
  const { user_gwa, user_strand } = recommendation;

  return (
    <div className="dashboard-wrapper">
      <main className="portal-main results-container">
        {/* HEADER SECTION */}
        <header className="results-header-section">
          <button onClick={onBack} className="logout-btn">← Back to Dashboard</button>
          <h1 className="header-title" style={{ marginTop: '20px' }}>Your Career Recommendations</h1>
          <p className="header-subtitle">
            Based on your personality traits and academic profile
            {user_strand && ` as a ${user_strand} student`}
            {user_gwa && ` with GWA of ${user_gwa}`}.
          </p>

          {topTraits.length > 0 && (
            <div className="traits-container" style={{ marginTop: '15px' }}>
              <span style={{ color: '#94a3b8', fontSize: '14px', marginRight: '10px' }}>Top Detected Traits:</span>
              {topTraits.slice(0, 5).map(([trait, count], idx) => (
                <span key={idx} className="activity-badge badge-profile">
                  {trait} ({count})
                </span>
              ))}
            </div>
          )}
        </header>

        {/* RECOMMENDATIONS LIST */}
        <div className="results-grid">
          {recommendation.recommendations.map((item, index) => {
            // DYNAMIC BORDER LOGIC
            let rankBorderColor = '#6366f1'; // Default indigo
            if (index === 0) rankBorderColor = '#10b981'; // Green for top
            else if (index === 1) rankBorderColor = '#3b82f6'; // Blue for second
            else if (index === 2) rankBorderColor = '#f59e0b'; // Amber for third

            return (
              <div 
                key={index} 
                className="result-card" 
                style={{ borderLeft: `5px solid ${rankBorderColor}` }}
              >
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                  <div style={{ flex: 1 }}>
                    <span 
                      className="activity-badge" 
                      style={{ 
                        color: '#818cf8', 
                        border: `1px solid #818cf8`,
                        background: 'transparent',
                        fontSize: '12px'
                      }}
                    >
                      Rank #{index + 1}
                    </span>
                    <h3 className="course-title" style={{ color: '#818cf8' }}>
                      {item.course_name}
                    </h3>
                    {item.description && <p className="header-subtitle">{item.description}</p>}
                  </div>
                  
                  <div className="score-display">
                    <div className="percentage-text" style={{ color: rankBorderColor }}>
                      {calculatePercentage(item.compatibility_score)}%
                    </div>
                    <div className="nav-category" style={{ margin: 0 }}>Match Score</div>
                  </div>
                </div>

                {/* WHY THIS FITS BOX */}
                <div className="reasoning-box">
                  <div className="reasoning-label">Why this fits you:</div>
                  <p className="reasoning-text">
                    {item.reasoning}
                  </p>
                </div>
                
                {/* TAGS SECTION */}
                <div className="tags-row">
                  {item.matched_traits?.map((trait, idx) => (
                    <span key={idx} className="activity-badge badge-profile">{trait}</span>
                  ))}
                  {item.minimum_gwa && (
                    <span className="activity-badge badge-assessment">Min GWA: {item.minimum_gwa}</span>
                  )}
                  {item.recommended_strand && (
                    <span className="activity-badge badge-profile">Strand: {item.recommended_strand}</span>
                  )}
                </div>
              </div>
            );
          })}
        </div>

        {/* FOOTER ACTIONS */}
        <footer className="action-footer">
          <h3 className="header-title" style={{ fontSize: '20px' }}>Not satisfied with these results?</h3>
          <p className="header-subtitle" style={{ marginBottom: '25px' }}>You can always retake the assessment to explore other interests.</p>
          <div style={{ display: 'flex', gap: '15px', justifyContent: 'center' }}>
            <button onClick={onRetake} className="start-btn">
              Retake Assessment
            </button>
            <button onClick={onBack} className="logout-btn" style={{ marginTop: 0 }}>
              Go to Dashboard
            </button>
          </div>
        </footer>
      </main>
    </div>
  );
}

export default ResultsView;