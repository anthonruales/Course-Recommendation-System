import React, { useState } from 'react';

function AssessmentForm({ onBack }) {
  const [stage, setStage] = useState(1); 
  
  const [formData, setFormData] = useState({
    fullName: '',
    age: '',
    gender: '',
    shsStrand: '',
    mathGrade: '',
    englishGrade: '',
    scienceGrade: '',
    filipinoGrade: '',
    q1: '',
    q2: '',
    q3: ''
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleNext = (e) => {
    e.preventDefault();
    setStage(2);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Final Assessment Data:", formData);
    alert("Assessment Complete! The Decision Tree is now analyzing your results.");
  };

  return (
    <div className="portal-layout">
      <main className="portal-main">
        <button onClick={onBack} className="btn-back" style={{marginBottom: '20px', cursor: 'pointer', background: 'none', border: 'none', color: '#3b82f6'}}>
          ← Back to Dashboard
        </button>

        <div className="portal-card" style={{maxWidth: '700px', margin: '0 auto'}}>
          
          {stage === 1 && (
            <>
              <header style={{borderBottom: '1px solid #eee', marginBottom: '25px', paddingBottom: '10px'}}>
                <h2 style={{margin: 0}}>Step 1: Student Profile & Academic Data</h2>
                <p style={{color: '#666', fontSize: '14px'}}>Your grades and strand are used for the Rule-Based Filtering process.</p>
              </header>

              <form onSubmit={handleNext}>
                <h4 style={{color: 'var(--brand-primary)'}}>Personal Information</h4>
                <div style={{display: 'grid', gridTemplateColumns: '2fr 1fr 1fr', gap: '15px', marginBottom: '25px'}}>
                  <div>
                    <label>Full Name</label>
                    <input name="fullName" type="text" placeholder="Juan Dela Cruz" required onChange={handleChange} style={inputStyle} />
                  </div>
                  <div>
                    <label>Age</label>
                    <input name="age" type="number" placeholder="18" required onChange={handleChange} style={inputStyle} />
                  </div>
                  <div>
                    <label>Gender</label>
                    <select name="gender" onChange={handleChange} style={inputStyle}>
                      <option value="">Select</option>
                      <option value="Male">Male</option>
                      <option value="Female">Female</option>
                    </select>
                  </div>
                </div>

                <h4 style={{color: 'var(--brand-primary)'}}>Academic Performance</h4>
                <div style={{marginBottom: '20px'}}>
                  <label>Current/Completed SHS Strand</label>
                  <select name="shsStrand" required onChange={handleChange} style={inputStyle}>
                    <option value="">-- Choose your Strand --</option>
                    <option value="STEM">STEM (Science, Technology, Engineering, Math)</option>
                    <option value="ABM">ABM (Accountancy, Business, Management)</option>
                    <option value="HUMSS">HUMSS (Humanities and Social Sciences)</option>
                    <option value="TVL">TVL (Technical-Vocational-Livelihood)</option>
                    <option value="GAS">GAS (General Academic Strand)</option>
                  </select>
                </div>

                <p style={{fontSize: '13px', color: '#888'}}>Enter your GWA for the following subjects:</p>
                <div style={{display: 'grid', gridTemplateColumns: '1fr 1fr 1fr 1fr', gap: '15px', marginBottom: '30px'}}>
                  <div>
                    <label>Mathematics</label>
                    <input name="mathGrade" type="number" required onChange={handleChange} style={inputStyle} />
                  </div>
                  <div>
                    <label>English</label>
                    <input name="englishGrade" type="number" required onChange={handleChange} style={inputStyle} />
                  </div>
                  <div>
                    <label>Science</label>
                    <input name="scienceGrade" type="number" required onChange={handleChange} style={inputStyle} />
                  </div>
                  <div>
                    <label>Filipino</label>
                    <input name="filipinoGrade" type="number" required onChange={handleChange} style={inputStyle} />
                  </div>
                </div>

                <button type="submit" className="btn-solid" style={{width: '100%', padding: '15px', fontSize: '16px'}}>
                  Save and Continue to Questionnaire →
                </button>
              </form>
            </>
          )}

          {stage === 2 && (
            <>
              <header style={{borderBottom: '1px solid #eee', marginBottom: '25px', paddingBottom: '10px'}}>
                <h2 style={{margin: 0}}>Step 2: Interest Questionnaire</h2>
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
                  Finish Assessment & Get Recommendations
                </button>
                
                <button type="button" onClick={() => setStage(1)} style={{width: '100%', marginTop: '10px', background: 'none', border: 'none', color: '#666', cursor: 'pointer'}}>
                  ← Back to Academic Profile
                </button>
              </form>
            </>
          )}

        </div>
      </main>
    </div>
  );
}

const inputStyle = {
  width: '100%',
  padding: '10px',
  marginTop: '5px',
  borderRadius: '6px',
  border: '1px solid #ccc',
  boxSizing: 'border-box'
};

const questionStyle = {
  padding: '15px',
  borderBottom: '1px solid #f0f0f0',
  marginBottom: '10px'
};

export default AssessmentForm;