import React, { useState, useEffect } from 'react';

function ProfileForm({ onBack, onSave, initialData }) {
  // Initialize with initialData if it exists, otherwise empty defaults
  const [formData, setFormData] = useState({
    fullName: '', age: '', gender: '', shsStrand: '',
    mathGrade: '', englishGrade: '', scienceGrade: '', filipinoGrade: ''
  });

  // Sync the form state whenever initialData changes (e.g., when switching users)
  useEffect(() => {
    if (initialData) {
      setFormData(initialData);
    } else {
      setFormData({
        fullName: '', age: '', gender: '', shsStrand: '',
        mathGrade: '', englishGrade: '', scienceGrade: '', filipinoGrade: ''
      });
    }
  }, [initialData]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSave = (e) => {
    e.preventDefault();
    onSave(formData); 
    alert("Academic Profile Updated Successfully!");
  };

  const inputStyle = { 
    width: '100%', 
    padding: '10px', 
    marginTop: '5px', 
    borderRadius: '6px', 
    border: '1px solid #ccc', 
    boxSizing: 'border-box' 
  };

  return (
    <div className="portal-layout">
      <main className="portal-main">
        <button 
          onClick={onBack} 
          style={{marginBottom: '20px', cursor: 'pointer', background: 'none', border: 'none', color: '#3b82f6'}}
        >
          ← Back to Dashboard
        </button>

        <div className="portal-card" style={{maxWidth: '700px', margin: '0 auto'}}>
          <header style={{borderBottom: '1px solid #eee', marginBottom: '25px', paddingBottom: '10px'}}>
            <h2>Academic Profile Management</h2>
            <p style={{color: '#666', fontSize: '14px'}}>
              Your data is saved specifically to your account.
            </p>
          </header>

          <form onSubmit={handleSave}>
            <div style={{display: 'grid', gridTemplateColumns: '2fr 1fr 1fr', gap: '15px', marginBottom: '25px'}}>
              <div>
                <label>Full Name</label>
                <input name="fullName" type="text" value={formData.fullName} required onChange={handleChange} style={inputStyle} />
              </div>
              <div>
                <label>Age</label>
                <input name="age" type="number" min="0" max="100" value={formData.age} required onChange={handleChange} style={inputStyle} />
              </div>
              <div>
                <label>Gender</label>
                <select name="gender" value={formData.gender} onChange={handleChange} style={inputStyle}>
                  <option value="">Select</option>
                  <option value="Male">Male</option>
                  <option value="Female">Female</option>
                </select>
              </div>
            </div>

            <div style={{marginBottom: '20px'}}>
              <label>SHS Strand</label>
              <select name="shsStrand" value={formData.shsStrand} required onChange={handleChange} style={inputStyle}>
                <option value="">-- Choose your Strand --</option>
                <option value="STEM">STEM</option>
                <option value="ABM">ABM</option>
                <option value="HUMSS">HUMSS</option>
                <option value="TVL">TVL</option>
                <option value="GAS">GAS</option>
              </select>
            </div>

            <div style={{display: 'grid', gridTemplateColumns: '1fr 1fr 1fr 1fr', gap: '15px', marginBottom: '30px'}}>
              <div><label>Math</label><input name="mathGrade" type="number" min="0" max="100" value={formData.mathGrade} required onChange={handleChange} style={inputStyle} /></div>
              <div><label>English</label><input name="englishGrade" type="number" min="0" max="100" value={formData.englishGrade} required onChange={handleChange} style={inputStyle} /></div>
              <div><label>Science</label><input name="scienceGrade" type="number" min="0" max="100" value={formData.scienceGrade} required onChange={handleChange} style={inputStyle} /></div>
              <div><label>Filipino</label><input name="filipinoGrade" type="number" min="0" max="100" value={formData.filipinoGrade} required onChange={handleChange} style={inputStyle} /></div>
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

export default ProfileForm;