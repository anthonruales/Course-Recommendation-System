import React from 'react';

function ResultsView({ recommendation, profileData, onRetake, onBack }) {
  if (!recommendation || !recommendation.courses || !profileData) return null;

  return (
    <div className="portal-layout">
      <main className="portal-main">
        <button onClick={onBack} className="btn-text" style={{color: '#3b82f6', marginBottom: '20px', cursor: 'pointer', border: 'none', background: 'none'}}>
          ← Back to Dashboard
        </button>

        <div className="portal-card" style={{maxWidth: '850px', margin: '0 auto', padding: '40px'}}>
          <header style={{textAlign: 'center', marginBottom: '40px'}}>
            <div style={{fontSize: '50px', marginBottom: '10px'}}>🎯</div>
            <h1 style={{margin: '0 0 10px 0'}}>Your Top 5 Career Matches</h1>
            <p style={{color: '#64748b'}}>{recommendation.overallAnalysis}</p>
          </header>

          <div style={{display: 'flex', flexDirection: 'column', gap: '20px'}}>
            {recommendation.courses.map((item, index) => {
              const isQualified = item.status === 'Qualified';
              const isTopMatch = index === 0;

              return (
                <div 
                  key={index} 
                  style={{
                    display: 'grid',
                    gridTemplateColumns: '60px 1fr auto',
                    alignItems: 'center',
                    gap: '20px',
                    padding: '20px',
                    background: isTopMatch ? '#f0f9ff' : '#fff',
                    border: `1px solid ${isTopMatch ? '#bae6fd' : '#e2e8f0'}`,
                    borderRadius: '12px',
                    boxShadow: isTopMatch ? '0 4px 6px -1px rgb(0 0 0 / 0.1)' : 'none',
                    position: 'relative'
                  }}
                >
                  <div style={{
                    fontSize: '24px', 
                    fontWeight: 800, 
                    color: isTopMatch ? '#0ea5e9' : '#cbd5e1',
                    textAlign: 'center'
                  }}>
                    #{index + 1}
                  </div>

                  <div>
                    <h3 style={{margin: '0 0 5px 0', color: '#1e293b', fontSize: '18px'}}>
                      {item.course}
                      {item.isAligned && (
                        <span title="Strand Aligned" style={{marginLeft: '8px', cursor: 'help'}}>✅</span>
                      )}
                    </h3>
                    <p style={{margin: 0, fontSize: '14px', color: '#64748b'}}>
                      {item.analysis}
                    </p>
                  </div>

                  <div style={{textAlign: 'right'}}>
                    <span style={{
                      display: 'inline-block',
                      padding: '6px 14px',
                      borderRadius: '20px',
                      fontSize: '11px',
                      fontWeight: 700,
                      textTransform: 'uppercase',
                      backgroundColor: isQualified ? '#22c55e' : item.status === 'Profile Incomplete' ? '#64748b' : '#f59e0b',
                      color: '#fff'
                    }}>
                      {item.status}
                    </span>
                  </div>
                </div>
              );
            })}
          </div>

          <div style={{
            marginTop: '40px', 
            padding: '20px', 
            background: '#f8fafc', 
            borderRadius: '8px', 
            border: '1px solid #e2e8f0',
            textAlign: 'center'
          }}>
            <p style={{fontSize: '14px', color: '#64748b', margin: 0}}>
              <strong>Expert Note:</strong> Recommendations are ranked based on your interest assessment and validated against your {recommendation.primaryStrand} academic records.
            </p>
          </div>

          <div style={{marginTop: '40px', display: 'flex', gap: '15px', justifyContent: 'center'}}>
            <button onClick={onRetake} className="btn-solid" style={{padding: '12px 25px'}}>
              Retake Assessment
            </button>
            <button onClick={() => window.print()} className="btn-outline" style={{padding: '12px 25px'}}>
              Download Results (PDF)
            </button>
          </div>
        </div>
      </main>
    </div>
  );
}

export default ResultsView;