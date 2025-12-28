import React, { useState, useEffect } from 'react';

function ProfileForm({ onBack, onSave, initialData }) {
  const [formData, setFormData] = useState({
    fullName: '', age: '', gender: '', shsStrand: '',
    mathGrade: '', englishGrade: '', scienceGrade: '', filipinoGrade: ''
  });

  useEffect(() => {
    if (initialData) {
      // If loading existing data, we need to flatten the 'grades' object 
      // back into the form fields so the user can edit them easily.
      setFormData({
        fullName: initialData.fullName || '',
        age: initialData.age || '',
        gender: initialData.gender || '',
        shsStrand: initialData.shsStrand || '',
        mathGrade: initialData.grades?.math || '',
        englishGrade: initialData.grades?.english || '',
        scienceGrade: initialData.grades?.science || '',
        filipinoGrade: initialData.grades?.filipino || ''
      });
    }
  }, [initialData]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSave = (e) => {
    e.preventDefault();
    
    // --- KEY UPDATE: RESTRUCTURE DATA FOR THE LOGIC ENGINE ---
    const restructuredData = {
      fullName: formData.fullName,
      age: formData.age,
      gender: formData.gender,
      shsStrand: formData.shsStrand,
      grades: {
        math: formData.mathGrade,
        english: formData.englishGrade,
        science: formData.scienceGrade,
        filipino: formData.filipinoGrade
      }
    };

    onSave(restructuredData); 
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
              Your data is saved specifically to your account and used for expert validation.
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
              <div><label>Math</label><input name="mathGrade" placeholder="60-100"type="number" min="0" max="100" value={formData.mathGrade} required onChange={handleChange} style={inputStyle} /></div>
              <div><label>English</label><input name="englishGrade" placeholder="60-100" type="number" min="0" max="100" value={formData.englishGrade} required onChange={handleChange} style={inputStyle} /></div>
              <div><label>Science</label><input name="scienceGrade" placeholder="60-100" type="number" min="0" max="100" value={formData.scienceGrade} required onChange={handleChange} style={inputStyle} /></div>
              <div><label>Filipino</label><input name="filipinoGrade" placeholder="60-100" type="number" min="0" max="100" value={formData.filipinoGrade} required onChange={handleChange} style={inputStyle} /></div>
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