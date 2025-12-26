import React, { useState } from 'react';

function AssessmentForm({ onBack }) {
  const [formData, setFormData] = useState({ q1: '', q2: '', q3: '' });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Questionnaire Data:", formData);
    alert("Assessment Complete! We are analyzing your interests against your saved profile.");
    onBack();
  };

  return (
    <div className="portal-layout">
      <main className="portal-main">
        <button onClick={onBack} className="btn-back" style={{marginBottom: '20px', cursor: 'pointer', background: 'none', border: 'none', color: '#3b82f6'}}>
          ← Cancel Assessment
        </button>

        <div className="portal-card" style={{maxWidth: '700px', margin: '0 auto'}}>
          <header style={{borderBottom: '1px solid #eee', marginBottom: '25px', paddingBottom: '10px'}}>
            <h2 style={{margin: 0}}>Career Interest Questionnaire</h2>
            <p style={{color: '#666', fontSize: '14px'}}>Answer these situational questions for the Decision Tree analysis.</p>
          </header>

          <form onSubmit={handleSubmit}>
            <div style={questionStyle}>
              <p>1. When faced with a broken gadget, do you prefer fixing it yourself rather than buying a new one?</p>
              <label><input type="radio" name="q1" value="yes" onChange={handleChange} required /> Yes</label>
              <label style={{marginLeft: '20px'}}><input type="radio" name="q1" value="no" onChange={handleChange} /> No</label>
            </div>

            <div style={questionStyle}>
              <p>2. Do you enjoy analyzing data or conducting experiments to find the truth?</p>
              <label><input type="radio" name="q2" value="yes" onChange={handleChange} required /> Yes</label>
              <label style={{marginLeft: '20px'}}><input type="radio" name="q2" value="no" onChange={handleChange} /> No</label>
            </div>

            <div style={questionStyle}>
              <p>3. Would you rather lead a team and pitch business ideas than work behind the scenes?</p>
              <label><input type="radio" name="q3" value="yes" onChange={handleChange} required /> Yes</label>
              <label style={{marginLeft: '20px'}}><input type="radio" name="q3" value="no" onChange={handleChange} /> No</label>
            </div>

            <button type="submit" className="btn-solid" style={{width: '100%', padding: '15px', fontSize: '16px', marginTop: '20px'}}>
              Finish & Get Recommendations
            </button>
          </form>
        </div>
      </main>
    </div>
  );
}

const questionStyle = { padding: '15px', borderBottom: '1px solid #f0f0f0', marginBottom: '10px' };

export default AssessmentForm;