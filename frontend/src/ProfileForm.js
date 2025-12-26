import React, { useState } from 'react';

function ProfileForm({ onBack }) {
  const [formData, setFormData] = useState({
    fullName: '', age: '', gender: '', shsStrand: '',
    mathGrade: '', englishGrade: '', scienceGrade: '', filipinoGrade: ''
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSave = (e) => {
    e.preventDefault();
    console.log("Saving Academic Profile:", formData);
    alert("Academic Profile Updated Successfully!");
    onBack(); 
  };

  return (
    <div className="portal-layout">
      <main className="portal-main">
        <button onClick={onBack} style={{marginBottom: '20px', cursor: 'pointer', background: 'none', border: 'none', color: '#3b82f6'}}>
          ← Back to Dashboard
        </button>

        <div className="portal-card" style={{maxWidth: '700px', margin: '0 auto'}}>
          <header style={{borderBottom: '1px solid #eee', marginBottom: '25px', paddingBottom: '10px'}}>
            <h2 style={{margin: 0}}>Academic Profile Management</h2>
            <p style={{color: '#666', fontSize: '14px'}}>Update your permanent records here.</p>
          </header>

          <form onSubmit={handleSave}>
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
              <label>SHS Strand</label>
              <select name="shsStrand" required onChange={handleChange} style={inputStyle}>
                <option value="">-- Choose your Strand --</option>
                <option value="STEM">STEM</option>
                <option value="ABM">ABM</option>
                <option value="HUMSS">HUMSS</option>
                <option value="TVL">TVL</option>
                <option value="GAS">GAS</option>
              </select>
            </div>

            <div style={{display: 'grid', gridTemplateColumns: '1fr 1fr 1fr 1fr', gap: '15px', marginBottom: '30px'}}>
              <div><label>Math</label><input name="mathGrade" type="number" placeholder="65-100" required onChange={handleChange} style={inputStyle} /></div>
              <div><label>English</label><input name="englishGrade" type="number" placeholder="65-100" required onChange={handleChange} style={inputStyle} /></div>
              <div><label>Science</label><input name="scienceGrade" type="number" placeholder="65-100" required onChange={handleChange} style={inputStyle} /></div>
              <div><label>Filipino</label><input name="filipinoGrade" type="number" placeholder="65-100" required onChange={handleChange} style={inputStyle} /></div>
            </div>

            <button type="submit" className="btn-solid" style={{width: '100%', padding: '15px'}}>
              Save Academic Records
            </button>
          </form>
        </div>
      </main>
    </div>
  );
}

const inputStyle = { width: '100%', padding: '10px', marginTop: '5px', borderRadius: '6px', border: '1px solid #ccc', boxSizing: 'border-box' };

export default ProfileForm;