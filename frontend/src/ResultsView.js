import React from 'react';

function ResultsView({ recommendation, profileData, onRetake, onBack }) {
  // recommendation is now { courses: [], isAligned: bool, status: string, analysis: string }
  if (!recommendation || !profileData) return null;

  const isQualified = recommendation.status === 'Qualified';

  return (
    <div className="portal-layout">
      <main className="portal-main">
        <button onClick={onBack} className="btn-text" style={{color: '#3b82f6', marginBottom: '20px', cursor: 'pointer', border: 'none', background: 'none'}}>
          ← Back to Dashboard
        </button>

        <div className="portal-card" style={{maxWidth: '800px', margin: '0 auto', textAlign: 'center', padding: '40px'}}>
          <div style={{fontSize: '50px', marginBottom: '10px'}}>🎓</div>
          <h1 style={{margin: '0 0 10px 0'}}>Career Recommendation Results</h1>
          <p style={{color: '#64748b'}}>Based on your Academic Profile and Interest Assessment</p>
          
          <hr style={{margin: '30px 0', border: '0', borderTop: '1px solid #e2e8f0'}} />

          {/* TOP MATCH SECTION */}
          <div style={{background: '#f8fafc', padding: '30px', borderRadius: '12px', border: '1px dashed #cbd5e1', marginBottom: '30px'}}>
            <h3 style={{textTransform: 'uppercase', fontSize: '12px', letterSpacing: '1px', color: '#64748b', margin: '0 0 10px 0'}}>Top Match for you:</h3>
            <h2 style={{fontSize: '32px', color: '#1e293b', margin: 0}}>
              {recommendation.courses.join(", ")}
            </h2>
          </div>

          {/* EXPERT ANALYSIS SECTION (The Step 3 Feature) */}
          <div style={{
            textAlign: 'left', 
            padding: '25px', 
            borderRadius: '12px', 
            marginBottom: '30px',
            backgroundColor: isQualified ? '#f0fdf4' : '#fff7ed',
            border: `1px solid ${isQualified ? '#bbf7d0' : '#ffedd5'}`
          }}>
            <div style={{display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '12px'}}>
              <h4 style={{margin: 0, color: isQualified ? '#166534' : '#9a3412', fontSize: '18px'}}>Expert Path Validation</h4>
              <span style={{
                padding: '4px 12px',
                borderRadius: '20px',
                fontSize: '11px',
                fontWeight: 800,
                textTransform: 'uppercase',
                backgroundColor: isQualified ? '#22c55e' : '#f59e0b',
                color: '#fff'
              }}>
                {recommendation.status}
              </span>
            </div>
            <p style={{margin: 0, color: '#4b5563', fontSize: '15px', lineHeight: '1.6'}}>
              {recommendation.analysis}
            </p>
          </div>

          {/* TWO-COLUMN DETAILS */}
          <div style={{textAlign: 'left', display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '20px'}}>
            <div style={{padding: '20px', background: '#fff', border: '1px solid #e2e8f0', borderRadius: '8px'}}>
              <h4 style={{margin: '0 0 10px 0', color: '#3b82f6'}}>Strand Alignment</h4>
              <p style={{fontSize: '14px', margin: 0, color: '#64748b'}}>
                {recommendation.isAligned 
                  ? `Directly aligned with your ${profileData.shsStrand} background.` 
                  : `Typically associated with a different SHS track, but matches your skills.`}
              </p>
            </div>
            <div style={{padding: '20px', background: '#fff', border: '1px solid #e2e8f0', borderRadius: '8px'}}>
              <h4 style={{margin: '0 0 10px 0', color: '#10b981'}}>Interest Match</h4>
              <p style={{fontSize: '14px', margin: 0, color: '#64748b'}}>
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