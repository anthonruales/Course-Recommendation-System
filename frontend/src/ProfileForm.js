import React, { useState } from 'react';

// Predefined options for Academic Interests
const INTEREST_OPTIONS = [
  // Science & Research
  { id: 'science', label: 'Science & Research', category: 'Science' },
  { id: 'biology', label: 'Biology & Life Sciences', category: 'Science' },
  { id: 'chemistry', label: 'Chemistry', category: 'Science' },
  { id: 'physics', label: 'Physics', category: 'Science' },
  { id: 'environment', label: 'Environment & Nature', category: 'Science' },
  
  // Technology
  { id: 'programming', label: 'Programming & Coding', category: 'Technology' },
  { id: 'computer', label: 'Computers & IT', category: 'Technology' },
  { id: 'data', label: 'Data & Analytics', category: 'Technology' },
  { id: 'ai', label: 'AI & Machine Learning', category: 'Technology' },
  { id: 'cybersecurity', label: 'Cybersecurity', category: 'Technology' },
  
  // Engineering
  { id: 'engineering', label: 'Engineering', category: 'Engineering' },
  { id: 'mechanical', label: 'Mechanical Systems', category: 'Engineering' },
  { id: 'electrical', label: 'Electrical & Electronics', category: 'Engineering' },
  { id: 'civil', label: 'Civil & Construction', category: 'Engineering' },
  
  // Business & Finance
  { id: 'business', label: 'Business & Entrepreneurship', category: 'Business' },
  { id: 'finance', label: 'Finance & Banking', category: 'Business' },
  { id: 'marketing', label: 'Marketing & Advertising', category: 'Business' },
  { id: 'accounting', label: 'Accounting', category: 'Business' },
  { id: 'economics', label: 'Economics', category: 'Business' },
  
  // Arts & Creative
  { id: 'art', label: 'Arts & Design', category: 'Arts' },
  { id: 'music', label: 'Music & Performance', category: 'Arts' },
  { id: 'film', label: 'Film & Media Production', category: 'Arts' },
  { id: 'writing', label: 'Writing & Literature', category: 'Arts' },
  { id: 'photography', label: 'Photography & Visual Arts', category: 'Arts' },
  
  // Healthcare
  { id: 'medical', label: 'Medicine & Healthcare', category: 'Healthcare' },
  { id: 'nursing', label: 'Nursing & Patient Care', category: 'Healthcare' },
  { id: 'psychology', label: 'Psychology & Mental Health', category: 'Healthcare' },
  
  // Social & Humanities
  { id: 'education', label: 'Education & Teaching', category: 'Social' },
  { id: 'law', label: 'Law & Justice', category: 'Social' },
  { id: 'politics', label: 'Politics & Government', category: 'Social' },
  { id: 'social', label: 'Social Work & Community', category: 'Social' },
  { id: 'history', label: 'History & Culture', category: 'Social' },
  
  // Others
  { id: 'sports', label: 'Sports & Fitness', category: 'Others' },
  { id: 'tourism', label: 'Tourism & Hospitality', category: 'Others' },
  { id: 'food', label: 'Culinary & Food Science', category: 'Others' },
  { id: 'agriculture', label: 'Agriculture & Farming', category: 'Others' },
];

// Predefined options for Skills
const SKILL_OPTIONS = [
  // Technical Skills
  { id: 'programming_skill', label: 'Programming / Coding', category: 'Technical' },
  { id: 'data_analysis', label: 'Data Analysis', category: 'Technical' },
  { id: 'web_development', label: 'Web Development', category: 'Technical' },
  { id: 'graphic_design', label: 'Graphic Design', category: 'Technical' },
  { id: 'video_editing', label: 'Video Editing', category: 'Technical' },
  { id: 'math_skills', label: 'Mathematics', category: 'Technical' },
  { id: 'laboratory', label: 'Laboratory Work', category: 'Technical' },
  { id: 'technical_writing', label: 'Technical Writing', category: 'Technical' },
  
  // Communication Skills
  { id: 'public_speaking', label: 'Public Speaking', category: 'Communication' },
  { id: 'writing_skill', label: 'Writing & Composition', category: 'Communication' },
  { id: 'presentation', label: 'Presentation Skills', category: 'Communication' },
  { id: 'negotiation', label: 'Negotiation', category: 'Communication' },
  { id: 'foreign_language', label: 'Foreign Languages', category: 'Communication' },
  
  // Leadership & Management
  { id: 'leadership', label: 'Leadership', category: 'Leadership' },
  { id: 'project_management', label: 'Project Management', category: 'Leadership' },
  { id: 'team_management', label: 'Team Management', category: 'Leadership' },
  { id: 'decision_making', label: 'Decision Making', category: 'Leadership' },
  { id: 'planning', label: 'Planning & Organization', category: 'Leadership' },
  
  // Interpersonal Skills
  { id: 'teamwork', label: 'Teamwork & Collaboration', category: 'Interpersonal' },
  { id: 'empathy', label: 'Empathy & Compassion', category: 'Interpersonal' },
  { id: 'customer_service', label: 'Customer Service', category: 'Interpersonal' },
  { id: 'mentoring', label: 'Mentoring & Teaching', category: 'Interpersonal' },
  { id: 'conflict_resolution', label: 'Conflict Resolution', category: 'Interpersonal' },
  
  // Analytical Skills
  { id: 'critical_thinking', label: 'Critical Thinking', category: 'Analytical' },
  { id: 'problem_solving', label: 'Problem Solving', category: 'Analytical' },
  { id: 'research', label: 'Research & Investigation', category: 'Analytical' },
  { id: 'attention_detail', label: 'Attention to Detail', category: 'Analytical' },
  { id: 'logical_reasoning', label: 'Logical Reasoning', category: 'Analytical' },
  
  // Creative Skills
  { id: 'creativity', label: 'Creativity & Innovation', category: 'Creative' },
  { id: 'artistic', label: 'Artistic Ability', category: 'Creative' },
  { id: 'music_skill', label: 'Musical Ability', category: 'Creative' },
  { id: 'storytelling', label: 'Storytelling', category: 'Creative' },
  { id: 'design_thinking', label: 'Design Thinking', category: 'Creative' },
];

function ProfileForm({ formData = {}, setFormData, onSave, onBack }) {
  const [gwaError, setGwaError] = useState('');
  
  // Parse interests and skills from comma-separated string to array
  const selectedInterests = formData?.interests ? formData.interests.split(',').filter(i => i.trim()) : [];
  const selectedSkills = formData?.skills ? formData.skills.split(',').filter(s => s.trim()) : [];
  
  // Toggle interest selection
  const toggleInterest = (interestId) => {
    const current = [...selectedInterests];
    const index = current.indexOf(interestId);
    if (index > -1) {
      current.splice(index, 1);
    } else {
      current.push(interestId);
    }
    setFormData(prev => ({
      ...prev,
      interests: current.join(',')
    }));
  };
  
  // Toggle skill selection
  const toggleSkill = (skillId) => {
    const current = [...selectedSkills];
    const index = current.indexOf(skillId);
    if (index > -1) {
      current.splice(index, 1);
    } else {
      current.push(skillId);
    }
    setFormData(prev => ({
      ...prev,
      skills: current.join(',')
    }));
  };
  
  // Safe Change Handler
  const handleChange = (e) => {
    const { name, value } = e.target;
    
    // GWA validation
    if (name === 'gwa') {
      const gwaValue = parseFloat(value);
      if (value && gwaValue > 100) {
        setGwaError('GWA cannot exceed 100');
      } else if (value && gwaValue < 75) {
        setGwaError('GWA must be at least 75');
      } else {
        setGwaError('');
      }
    }
    
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
    
    // Validate GWA range
    const gwaValue = parseFloat(formData.gwa);
    if (gwaValue > 100) {
      alert('GWA cannot exceed 100');
      return;
    }
    if (gwaValue < 75) {
      alert('GWA must be at least 75');
      return;
    }
    
    const userId = localStorage.getItem('userId');
    if (!userId) {
      alert('User ID not found. Please log in again.');
      return;
    }
    
    console.log('Saving academic info for userId:', userId, 'with data:', formData);
    
    // Save to backend - include all profile fields
    fetch(`http://localhost:8000/user/${userId}/academic-info`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        gwa: parseFloat(formData.gwa),
        strand: formData.strand,
        fullname: formData.fullname || null,
        age: formData.age ? parseInt(formData.age) : null,
        gender: formData.gender || null,
        interests: selectedInterests.join(', ') || null,
        skills: selectedSkills.join(', ') || null
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
                placeholder=""
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
                  placeholder=""
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
                  style={{
                    ...styles.input,
                    ...(gwaError ? {borderColor: '#ef4444'} : {})
                  }} 
                  type="number" 
                  step="0.01"
                  min="75"
                  max="100"
                  name="gwa"
                  value={formData?.gwa || ''} 
                  onChange={handleChange}
                  placeholder="75.00 - 100.00"
                />
                {gwaError && (
                  <span style={{color: '#ef4444', fontSize: '12px', marginTop: '4px', display: 'block'}}>
                    {gwaError}
                  </span>
                )}
                {!gwaError && (
                  <span style={{color: 'rgba(255,255,255,0.5)', fontSize: '12px', marginTop: '4px', display: 'block'}}>
                    Enter a value between 75 and 100
                  </span>
                )}
              </div>
            </div>

            {/* QUALITATIVE SECTION */}
            <div style={{...styles.formSectionTitle, marginTop: '40px'}}>Qualitative Analysis</div>
            
            <div style={styles.inputGroup}>
              <label style={styles.label}>Academic Interests <span style={{color: 'rgba(255,255,255,0.5)', fontWeight: 'normal'}}>(Select all that apply)</span></label>
              <div style={styles.checkboxGrid}>
                {INTEREST_OPTIONS.map(option => (
                  <label 
                    key={option.id} 
                    style={{
                      ...styles.checkboxLabel,
                      ...(selectedInterests.includes(option.id) ? styles.checkboxLabelSelected : {})
                    }}
                  >
                    <input
                      type="checkbox"
                      checked={selectedInterests.includes(option.id)}
                      onChange={() => toggleInterest(option.id)}
                      style={styles.checkbox}
                    />
                    <span>{option.label}</span>
                  </label>
                ))}
              </div>
              <span style={{color: 'rgba(255,255,255,0.5)', fontSize: '12px', marginTop: '8px', display: 'block'}}>
                {selectedInterests.length} selected
              </span>
            </div>

            <div style={{...styles.inputGroup, marginTop: '30px'}}>
              <label style={styles.label}>Technical & Soft Skills <span style={{color: 'rgba(255,255,255,0.5)', fontWeight: 'normal'}}>(Select all that apply)</span></label>
              <div style={styles.checkboxGrid}>
                {SKILL_OPTIONS.map(option => (
                  <label 
                    key={option.id} 
                    style={{
                      ...styles.checkboxLabel,
                      ...(selectedSkills.includes(option.id) ? styles.checkboxLabelSelected : {})
                    }}
                  >
                    <input
                      type="checkbox"
                      checked={selectedSkills.includes(option.id)}
                      onChange={() => toggleSkill(option.id)}
                      style={styles.checkbox}
                    />
                    <span>{option.label}</span>
                  </label>
                ))}
              </div>
              <span style={{color: 'rgba(255,255,255,0.5)', fontSize: '12px', marginTop: '8px', display: 'block'}}>
                {selectedSkills.length} selected
              </span>
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
  checkboxGrid: {
    display: 'grid',
    gridTemplateColumns: 'repeat(auto-fill, minmax(180px, 1fr))',
    gap: '10px',
    maxHeight: '300px',
    overflowY: 'auto',
    padding: '15px',
    background: 'rgba(30, 30, 50, 0.6)',
    borderRadius: '12px',
    border: '1px solid rgba(255,255,255,0.1)',
  },
  checkboxLabel: {
    display: 'flex',
    alignItems: 'center',
    gap: '8px',
    padding: '10px 14px',
    background: 'rgba(255,255,255,0.03)',
    borderRadius: '8px',
    cursor: 'pointer',
    fontSize: '13px',
    color: 'rgba(255,255,255,0.7)',
    border: '1px solid rgba(255,255,255,0.08)',
    transition: 'all 0.2s ease',
  },
  checkboxLabelSelected: {
    background: 'rgba(99, 102, 241, 0.15)',
    borderColor: 'rgba(99, 102, 241, 0.4)',
    color: '#a5b4fc',
  },
  checkbox: {
    width: '16px',
    height: '16px',
    accentColor: '#6366f1',
    cursor: 'pointer',
  },
};

export default ProfileForm;