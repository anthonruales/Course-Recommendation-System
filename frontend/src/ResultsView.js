import React from 'react';
import './components/style/Dashboard.css';

function ResultsView({ recommendation, profileData, onRetake, onBack }) {
  // Safety check: If data hasn't arrived or is malformed, show a loading state
  if (!recommendation || !recommendation.recommendations) {
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

  // Calculate percentage score (normalize compatibility_score to 0-100%)
  const calculatePercentage = (score) => {
    // Assuming max score is around 20-30, normalize to percentage
    const maxScore = 30;
    const percentage = Math.min(100, Math.max(0, (score / maxScore) * 100));
    return Math.round(percentage);
  };

  // Get top traits for display
  const topTraits = recommendation.detected_traits || [];
  const userGwa = recommendation.user_gwa;
  const userStrand = recommendation.user_strand;

  return (
    <div className="portal-layout">
      <main className="portal-main">
        <div className="results-header" style={{ marginBottom: '30px' }}>
          <button onClick={onBack} className="link-btn">← Back to Dashboard</button>
          <h1 style={{ marginTop: '20px' }}>Your Career Recommendations</h1>
          <p className="muted-text">
            Based on your personality traits and academic profile
            {userStrand && ` as a ${userStrand} student`}
            {userGwa && ` with GWA of ${userGwa}`}.
          </p>
          {topTraits.length > 0 && (
            <div style={{ marginTop: '15px', display: 'flex', gap: '10px', flexWrap: 'wrap' }}>
              <span style={{ color: '#64748b', fontSize: '14px' }}>Your top traits:</span>
              {topTraits.map(([trait, count], idx) => (
                <span key={idx} className="activity-badge profile">
                  {trait} ({count})
                </span>
              ))}
            </div>
          )}
        </div>

        <div className="results-grid" style={{ display: 'grid', gap: '20px' }}>
          {recommendation.recommendations.map((item, index) => (
            <div key={index} className="portal-card" style={{ borderLeft: index === 0 ? '5px solid #1e40af' : '1px solid #e2e8f0' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                <div>
                  <span className="activity-badge assessment" style={{ marginBottom: '10px', display: 'inline-block' }}>
                    Rank #{index + 1} Match
                  </span>
                  <h3 style={{ margin: '5px 0', fontSize: '22px', color: '#1e293b' }}>{item.course_name}</h3>
                  {item.description && (
                    <p style={{ color: '#64748b', fontSize: '14px', marginTop: '5px' }}>{item.description}</p>
                  )}
                </div>
                <div style={{ textAlign: 'right' }}>
                  <div style={{ fontSize: '24px', fontWeight: '800', color: '#1e40af' }}>
                    {calculatePercentage(item.compatibility_score)}%
                  </div>
                  <div className="muted-text" style={{ fontSize: '12px' }}>Match Score</div>
                </div>
              </div>

              <div style={{ marginTop: '15px', padding: '15px', backgroundColor: '#f8fafc', borderRadius: '8px' }}>
                <h4 style={{ margin: '0 0 8px 0', fontSize: '14px', color: '#64748b', textTransform: 'uppercase' }}>Why this fits you:</h4>
                <p style={{ margin: 0, lineHeight: '1.6', color: '#334155' }}>{item.reasoning}</p>
              </div>
              
              <div style={{ marginTop: '15px', display: 'flex', gap: '10px', flexWrap: 'wrap' }}>
                {item.matched_traits && item.matched_traits.length > 0 && (
                  <>
                    <span style={{ color: '#64748b', fontSize: '12px', width: '100%' }}>Matching traits:</span>
                    {item.matched_traits.map((trait, idx) => (
                      <span key={idx} className="activity-badge profile">{trait}</span>
                    ))}
                  </>
                )}
                {item.minimum_gwa && (
                  <span className="activity-badge assessment">Min GWA: {item.minimum_gwa}</span>
                )}
                {item.recommended_strand && (
                  <span className="activity-badge profile">Strand: {item.recommended_strand}</span>
                )}
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