import React from 'react';

function ResultsView({ recommendation, profileData, onRetake, onBack }) {
  if (!recommendation || !profileData) return null;

  return (
    <div className="portal-layout">
      <main className="portal-main">
        <button onClick={onBack} className="btn-text" style={{color: '#3b82f6', marginBottom: '20px', cursor: 'pointer'}}>
          ← Back to Dashboard
        </button>

        <div className="portal-card" style={{maxWidth: '800px', margin: '0 auto', textAlign: 'center', padding: '40px'}}>
          <div style={{fontSize: '50px', marginBottom: '10px'}}>🎓</div>
          <h1 style={{margin: '0 0 10px 0'}}>Career Recommendation Results</h1>
          <p style={{color: '#666'}}>Based on your Academic Profile and Interest Assessment</p>
          
          <hr style={{margin: '30px 0', border: '0', borderTop: '1px solid #eee'}} />

          <div style={{background: '#f8fafc', padding: '30px', borderRadius: '12px', border: '1px dashed #cbd5e1', marginBottom: '30px'}}>
            <h3 style={{textTransform: 'uppercase', fontSize: '12px', letterSpacing: '1px', color: '#64748b', margin: '0 0 10px 0'}}>Top Match for you:</h3>
            <h2 style={{fontSize: '28px', color: '#1e293b', margin: 0}}>
              {recommendation.join(", ")}
            </h2>
          </div>

          <div style={{textAlign: 'left', display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '20px'}}>
            <div style={{padding: '20px', background: '#fff', border: '1px solid #e2e8f0', borderRadius: '8px'}}>
              <h4 style={{margin: '0 0 10px 0', color: '#3b82f6'}}>Academic Fit</h4>
              <p style={{fontSize: '14px', margin: 0}}>
                Matches your <strong>{profileData.shsStrand}</strong> strand background and academic performance in core subjects.
              </p>
            </div>
            <div style={{padding: '20px', background: '#fff', border: '1px solid #e2e8f0', borderRadius: '8px'}}>
              <h4 style={{margin: '0 0 10px 0', color: '#10b981'}}>Interest Match</h4>
              <p style={{fontSize: '14px', margin: 0}}>
                Your responses indicate a strong preference for the logical and situational demands of this field.
              </p>
            </div>
          </div>

          <div style={{marginTop: '40px', display: 'flex', gap: '15px', justifyContent: 'center'}}>
            <button onClick={onRetake} className="btn-solid" style={{padding: '12px 25px'}}>
              Retake Assessment
            </button>
            <button onClick={() => window.print()} className="btn-outline" style={{padding: '12px 25px'}}>
              Download PDF Report
            </button>
          </div>
        </div>
      </main>
    </div>
  );
}

export default ResultsView;