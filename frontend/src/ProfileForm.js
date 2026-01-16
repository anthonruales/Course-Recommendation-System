import React from 'react';

function ProfileForm({ formData = {}, setFormData, onSave, onBack }) {
  
  // Safe Change Handler
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => {
      const currentData = prev || {};
      return { ...currentData, [name]: value };
    });
  };

  // Save handler with backend sync
  const handleSaveProfile = () => {
    // Validate required fields
    if (!formData.gwa || !formData.strand) {
      alert('Please fill in both GWA and SHS Strand to save your profile');
      return;
    }
    
    const userId = localStorage.getItem('userId');
    if (!userId) {
      alert('User ID not found. Please log in again.');
      return;
    }
    
    console.log('Saving academic info for userId:', userId, 'with data:', formData);
    
    // Save to backend
    fetch(`http://localhost:8000/user/${userId}/academic-info`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        gwa: parseFloat(formData.gwa),
        strand: formData.strand
      })
    })
    .then(res => res.json())
    .then(data => {
      console.log('✅ Academic info saved to backend:', data);
      alert('✅ Profile updated successfully! Your academic information has been saved.');
      onSave();
    })
    .catch(err => {
      console.error('❌ Error saving to backend:', err);
      alert('⚠️ Profile saved locally but failed to sync with server. Please try again.');
    });
  };

  // Loading state if data isn't ready
  if (formData === null) {
    return (
      <div style={{...styles.dashboardWrapper, justifyContent: 'center', alignItems: 'center'}}>
        <div style={{color: '#6366f1', fontWeight: 'bold'}}>Loading profile data...</div>
      </div>
    );
  }

  return (
    <div style={styles.dashboardWrapper}>
      {/* SIDEBAR */}
      <aside style={styles.sidebar}>
        <div style={styles.brandContainer}>
          <div style={styles.logoIcon}>C</div>
          <h2 style={styles.brandName}>CoursePro</h2>
        </div>
        <nav style={styles.nav}>
          <div style={styles.categoryLabel}>Settings</div>
          <div style={styles.navItem} onClick={onBack}>📊 Back to Dashboard</div>
          <div style={{...styles.navItem, ...styles.navActive}}>📝 Edit Profile</div>
        </nav>
        <button onClick={onBack} style={styles.cancelBtn}>Discard Changes</button>
      </aside>

      {/* MAIN CONTENT */}
      <main style={styles.mainContent}>
        <header style={styles.header}>
          <h1 style={styles.headerTitle}>Personal Profile</h1>
          <p style={styles.headerSubtitle}>Configure your background for better AI precision.</p>
        </header>

        <div style={styles.formContainer}>
          <form style={styles.glassCard} onSubmit={(e) => { e.preventDefault(); onSave(); }}>
            
            <div style={styles.formSectionTitle}>Basic Information</div>
            
            {/* FULL NAME FIELD - Added back here */}
            <div style={{...styles.inputGroup, marginBottom: '25px'}}>
              <label style={styles.label}>Full Name</label>
              <input 
                style={styles.input} 
                type="text" 
                name="fullname"
                value={formData?.fullname || ''} 
                onChange={handleChange}
                placeholder="Juan Dela Cruz"
              />
            </div>

            <div style={styles.formGrid}>
              {/* AGE */}
              <div style={styles.inputGroup}>
                <label style={styles.label}>Age</label>
                <input 
                  style={styles.input} 
                  type="number" 
                  name="age"
                  value={formData?.age || ''} 
                  onChange={handleChange}
                  placeholder="e.g. 18"
                />
              </div>

              {/* GENDER */}
              <div style={styles.inputGroup}>
                <label style={styles.label}>Gender</label>
                <select 
                  style={styles.input} 
                  name="gender"
                  value={formData?.gender || ''} 
                  onChange={handleChange}
                >
                  <option value="" disabled>Select...</option>
                  <option value="Male">Male</option>
                  <option value="Female">Female</option>
                </select>
              </div>

              {/* SHS STRAND */}
              <div style={styles.inputGroup}>
                <label style={styles.label}>SHS Strand</label>
                <select 
                  style={styles.input} 
                  name="strand"
                  value={formData?.strand || ''} 
                  onChange={handleChange}
                >
                  <option value="" disabled>Select Strand</option>
                  <option value="STEM">STEM</option>
                  <option value="ABM">ABM</option>
                  <option value="HUMSS">HUMSS</option>
                  <option value="GAS">GAS</option>
                  <option value="TVL">TVL</option>
                </select>
              </div>

              {/* GWA */}
              <div style={styles.inputGroup}>
                <label style={styles.label}>General Weighted Average (GWA)</label>
                <input 
                  style={styles.input} 
                  type="number" 
                  step="0.1"
                  min="80.0"
                  max="100.0"
                  name="gwa"
                  value={formData?.gwa || ''} 
                  onChange={handleChange}
                  placeholder="e.g. 88.5"
                />
              </div>
            </div>

            {/* QUALITATIVE SECTION */}
            <div style={{...styles.formSectionTitle, marginTop: '40px'}}>Qualitative Analysis</div>
            
            <div style={styles.inputGroup}>
              <label style={styles.label}>Academic Interests</label>
              <textarea 
                style={{...styles.input, height: '100px', resize: 'none'}} 
                name="interests"
                placeholder="What subjects or topics do you enjoy?"
                value={formData?.interests || ''} 
                onChange={handleChange}
              />
            </div>

            <div style={{...styles.inputGroup, marginTop: '20px'}}>
              <label style={styles.label}>Technical & Soft Skills</label>
              <textarea 
                style={{...styles.input, height: '100px', resize: 'none'}} 
                name="skills"
                placeholder="e.g. Programming, Public Speaking, Drawing..."
                value={formData?.skills || ''} 
                onChange={handleChange}
              />
            </div>

            <div style={styles.footer}>
              <button type="button" onClick={handleSaveProfile} style={styles.saveBtn}>Update Profile Configuration</button>
            </div>
          </form>

          {/* RIGHT INFO COLUMN */}
          <div style={styles.infoCol}>
            <div style={styles.statusBox}>
              <div style={styles.statusDot}></div>
              <span style={{fontSize: '12px', fontWeight: '700', color: '#10b981'}}>AI READY</span>
            </div>
            <p style={styles.infoText}>
              Ensuring your interests and skills are accurate helps our engine find the best career matches beyond just grades.
            </p>
          </div>
        </div>
      </main>
    </div>
  );
}

const styles = {
  dashboardWrapper: { display: 'flex', width: '100vw', height: '100vh', background: 'transparent' },
  sidebar: { width: '260px', background: 'rgba(255, 255, 255, 0.02)', backdropFilter: 'blur(20px)', borderRight: '1px solid rgba(255, 255, 255, 0.08)', display: 'flex', flexDirection: 'column', padding: '40px 20px' },
  logoIcon: { width: '35px', height: '35px', background: 'linear-gradient(135deg, #6366f1, #8b5cf6)', borderRadius: '8px', display: 'flex', alignItems: 'center', justifyContent: 'center', fontWeight: '800', color: 'white', marginRight: '12px' },
  brandContainer: { display: 'flex', alignItems: 'center', marginBottom: '40px', paddingLeft: '10px' },
  brandName: { fontSize: '18px', fontWeight: '700', color: 'white', margin: 0 },
  nav: { flex: 1 },
  categoryLabel: { fontSize: '11px', fontWeight: '700', color: '#64748b', textTransform: 'uppercase', letterSpacing: '1px', margin: '20px 0 10px 10px' },
  navItem: { padding: '12px 15px', borderRadius: '10px', color: '#94a3b8', cursor: 'pointer', fontSize: '14px', marginBottom: '4px' },
  navActive: { background: 'rgba(99, 102, 241, 0.1)', color: '#818cf8', fontWeight: '600' },
  cancelBtn: { padding: '12px', borderRadius: '10px', border: '1px solid rgba(255,255,255,0.1)', background: 'transparent', color: '#94a3b8', cursor: 'pointer', fontWeight: '600', fontSize: '13px' },
  mainContent: { flex: 1, padding: '40px 60px', overflowY: 'auto' },
  header: { marginBottom: '30px' },
  headerTitle: { fontSize: '28px', fontWeight: '800', color: 'white', margin: 0 },
  headerSubtitle: { color: 'rgba(255,255,255,0.6)', fontSize: '15px', marginTop: '5px' },
  formContainer: { display: 'grid', gridTemplateColumns: '1fr 280px', gap: '40px', alignItems: 'start' },
  glassCard: { 
    background: 'rgba(255, 255, 255, 0.05)', 
    backdropFilter: 'blur(20px) saturate(180%)',
    WebkitBackdropFilter: 'blur(20px) saturate(180%)',
    border: '1px solid rgba(255, 255, 255, 0.15)', 
    borderRadius: '24px', 
    padding: '40px', 
    boxShadow: '0 20px 40px rgba(0,0,0,0.3)' 
  },
  formSectionTitle: { fontSize: '14px', fontWeight: '700', color: '#818cf8', textTransform: 'uppercase', letterSpacing: '1px', marginBottom: '20px' },
  formGrid: { display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '25px' },
  inputGroup: { display: 'flex', flexDirection: 'column' },
  label: { fontSize: '13px', fontWeight: '600', color: 'rgba(255,255,255,0.8)', marginBottom: '8px', marginLeft: '4px' },
  input: { 
    padding: '14px 16px', 
    background: 'rgba(30, 30, 50, 0.9)', // Solid dark background for dropdown compatibility
    border: '1px solid rgba(255,255,255,0.1)', 
    borderRadius: '12px', 
    color: 'white', 
    fontSize: '15px', 
    outline: 'none',
    boxSizing: 'border-box'
  },
  // Added this to style the options inside the select
  option: {
    background: '#1a1a2e', 
    color: 'white'
  },
  footer: { marginTop: '40px', borderTop: '1px solid rgba(255,255,255,0.05)', paddingTop: '30px', display: 'flex', justifyContent: 'flex-end' },
  saveBtn: { background: '#6366f1', color: 'white', padding: '16px 32px', borderRadius: '14px', border: 'none', fontWeight: '700', fontSize: '15px', cursor: 'pointer', boxShadow: '0 10px 15px rgba(99, 102, 241, 0.2)' },
  infoCol: { background: 'rgba(99, 102, 241, 0.03)', border: '1px solid rgba(99, 102, 241, 0.1)', borderRadius: '20px', padding: '25px' },
  statusBox: { display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '15px' },
  statusDot: { width: '8px', height: '8px', borderRadius: '50%', background: '#10b981', boxShadow: '0 0 10px #10b981' },
  infoText: { fontSize: '13px', color: '#94a3b8', lineHeight: '1.6', margin: 0 },
};

export default ProfileForm;