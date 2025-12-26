import React, { useState } from 'react';

function AssessmentForm({ onBack }) {
  // 1. This "state" stores all the input from the student
  const [formData, setFormData] = useState({
    fullName: '',
    age: '',
    gender: '',
    shsStrand: '',
    mathGrade: '',
    englishGrade: '',
    scienceGrade: '',
    filipinoGrade: ''
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Saving Student Data:", formData);
    alert("Profile saved! Let's proceed to the Interest Questionnaire.");
    // In the next step, we will code the Situational Questions
  };

  return (
    <div className="portal-layout">
      <main className="portal-main">
        <button onClick={onBack} className="btn-back" style={{marginBottom: '20px', cursor: 'pointer', background: 'none', border: 'none', color: '#3b82f6'}}>
          ← Back to Dashboard
        </button>

        <div className="portal-card" style={{maxWidth: '700px', margin: '0 auto'}}>
          <header style={{borderBottom: '1px solid #eee', marginBottom: '25px', paddingBottom: '10px'}}>
            <h2 style={{margin: 0}}>Step 1: Student Profile & Academic Data</h2>
            <p style={{color: '#666', fontSize: '14px'}}>Your grades and strand are used for the Rule-Based Filtering process.</p>
          </header>

          <form onSubmit={handleSubmit}>
            {/* --- PERSONAL DATA SECTION --- */}
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

            {/* --- ACADEMIC DATA SECTION --- */}
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

            <p style={{fontSize: '13px', color: '#888'}}>Enter your General Weighted Average (GWA) for the following subjects:</p>
            <div style={{display: 'grid', gridTemplateColumns: '1fr 1fr 1fr 1fr', gap: '15px', marginBottom: '30px'}}>
              <div>
                <label>Mathematics</label>
                <input name="mathGrade" type="number" placeholder="85-100" required onChange={handleChange} style={inputStyle} />
              </div>
              <div>
                <label>English</label>
                <input name="englishGrade" type="number" placeholder="85-100" required onChange={handleChange} style={inputStyle} />
              </div>
              <div>
                <label>Science</label>
                <input name="scienceGrade" type="number" placeholder="85-100" required onChange={handleChange} style={inputStyle} />
              </div>
              <div>
                <label>Filipino</label>
                <input name="filipinoGrade" type="number" placeholder="85-100" required onChange={handleChange} style={inputStyle} />
              </div>
            </div>

            <button type="submit" className="btn-solid" style={{width: '100%', padding: '15px', fontSize: '16px'}}>
              Save and Continue to Questionnaire →
            </button>
          </form>
        </div>
      </main>
    </div>
  );
}

// Simple styling object to keep the code clean for you
const inputStyle = {
  width: '100%',
  padding: '10px',
  marginTop: '5px',
  borderRadius: '6px',
  border: '1px solid #ccc',
  boxSizing: 'border-box'
};

export default AssessmentForm;