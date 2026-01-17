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

  // Backend now sends a true percentage (0-98%) - no calculation needed
  const getDisplayPercentage = (item) => {
    // Check multiple possible field names for the score
    let score = item.compatibility_score ?? item.final_score ?? item.match_percentage ?? item.score;
    
    // Handle NaN or undefined
    if (score === undefined || score === null || isNaN(score)) {
      score = 75; // Default fallback
    }
    
    return Math.round(score);
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
            <div className="traits-container">
              <span style={{ color: '#94a3b8', fontSize: '14px' }}>Detected Traits:</span>
              {topTraits.map(([trait, count], idx) => (
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
            let rankBorderColor = 'rgba(240, 223, 223, 0.08)'; // Default color
            if (index === 0) rankBorderColor = 'gold';
            else if (index === 1) rankBorderColor = '#C0C0C0'; // Para saSilver 
            else if (index === 2) rankBorderColor = '#CD7F32'; // Para sa Bronze

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
                        color: rankBorderColor, 
                        border: `1px solid ${rankBorderColor}`,
                        background: 'transparent' 
                      }}
                    >
                      Rank #{index + 1} Match
                    </span>
                    <h3 className="course-title" style={{ color: index === 0 ? 'gold' : '#818cf8' }}>
                      {item.course_name}
                    </h3>
                    {item.description && <p className="header-subtitle">{item.description}</p>}
                  </div>
                  
                  <div className="score-display">
                    <div className="percentage-text" style={{ color: rankBorderColor }}>
                      {getDisplayPercentage(item)}%
                    </div>
                    <div className="nav-category" style={{ margin: 0 }}>Match Score</div>
                  </div>
                </div>

                {/* WHY THIS FITS BOX */}
                <div className="reasoning-box">
                  <div className="reasoning-label">Why this fits you:</div>
                  <p className="reasoning-text">{item.reasoning}</p>
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