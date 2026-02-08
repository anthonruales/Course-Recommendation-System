import React, { useState, useEffect, useRef } from 'react';
import API_BASE_URL from './config';
import Toast from './Toast';

// Bad words filter list (common inappropriate words)
const BAD_WORDS = [
  'fuck', 'shit', 'ass', 'bitch', 'damn', 'crap', 'bastard', 'dick', 'pussy', 'cock',
  'asshole', 'motherfucker', 'nigger', 'nigga', 'faggot', 'slut', 'whore', 'cunt',
  'retard', 'idiot', 'stupid', 'dumb', 'moron', 'loser', 'gay', 'homo', 'lesbian',
  'puta', 'gago', 'tangina', 'taena', 'bobo', 'tanga', 'putangina', 'ulol', 'lintik',
  'peste', 'punyeta', 'leche', 'hayop', 'animal', 'pokpok', 'malandi'
];

// Helper function to capitalize each word in a name properly
const capitalizeName = (name) => {
  if (!name) return '';
  return name
    .toLowerCase()
    .split(' ')
    .map(word => word.charAt(0).toUpperCase() + word.slice(1))
    .join(' ');
};

// Check if name contains bad words
const containsBadWords = (name) => {
  if (!name) return false;
  const lowerName = name.toLowerCase().replace(/[^a-z\s]/g, '');
  const words = lowerName.split(/\s+/);
  return words.some(word => BAD_WORDS.includes(word));
};

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
  const [interestModalOpen, setInterestModalOpen] = useState(false);
  const [skillsModalOpen, setSkillsModalOpen] = useState(false);
  const [toast, setToast] = useState(null);
  const [profilePhoto, setProfilePhoto] = useState(null);
  const fileInputRef = useRef(null);
  
  // Load saved profile photo from localStorage on mount (user-specific)
  useEffect(() => {
    const userId = localStorage.getItem('userId');
    if (userId) {
      const savedPhoto = localStorage.getItem(`profilePhoto_${userId}`);
      if (savedPhoto) {
        setProfilePhoto(savedPhoto);
      } else {
        setProfilePhoto(null); // Clear photo if switching accounts
      }
    }
  }, []);
  
  const showToast = (message, type = 'info') => {
    setToast({ message, type });
  };
  
  // Handle profile photo upload
  const handlePhotoUpload = (e) => {
    const file = e.target.files[0];
    if (file) {
      // Check file size (max 2MB)
      if (file.size > 2 * 1024 * 1024) {
        showToast('Image size must be less than 2MB', 'error');
        return;
      }
      
      // Check file type
      if (!file.type.startsWith('image/')) {
        showToast('Please upload an image file', 'error');
        return;
      }
      
      const reader = new FileReader();
      reader.onloadend = () => {
        const base64String = reader.result;
        const userId = localStorage.getItem('userId');
        setProfilePhoto(base64String);
        if (userId) {
          localStorage.setItem(`profilePhoto_${userId}`, base64String);
        }
        showToast('Profile photo updated!', 'success');
      };
      reader.readAsDataURL(file);
    }
  };
  
  const removePhoto = () => {
    const userId = localStorage.getItem('userId');
    setProfilePhoto(null);
    if (userId) {
      localStorage.removeItem(`profilePhoto_${userId}`);
    }
    showToast('Profile photo removed', 'info');
  };
  
  // Parse interests and skills from comma-separated string to array (trim each value!)
  const selectedInterests = formData?.interests 
    ? formData.interests.split(',').map(i => i.trim()).filter(i => i) 
    : [];
  const selectedSkills = formData?.skills 
    ? formData.skills.split(',').map(s => s.trim()).filter(s => s) 
    : [];
  
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
    
    // Auto-capitalize fullname and validate
    if (name === 'fullname') {
      const capitalizedName = capitalizeName(value);
      setFormData(prev => {
        const currentData = prev || {};
        return { ...currentData, fullname: capitalizedName };
      });
      return;
    }
    
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

  // Track original values to detect changes
  const originalDataRef = useRef(null);
  
  useEffect(() => {
    if (formData && !originalDataRef.current) {
      originalDataRef.current = {
        fullname: formData.fullname || '',
        gwa: formData.gwa || '',
        strand: formData.strand || '',
        age: formData.age || '',
        gender: formData.gender || '',
        interests: formData.interests || '',
        skills: formData.skills || ''
      };
    }
  }, [formData]);

  const getChangedFields = () => {
    const original = originalDataRef.current || {};
    const changes = [];
    const fieldLabels = {
      fullname: 'Full Name',
      gwa: 'GWA',
      strand: 'SHS Strand',
      age: 'Age',
      gender: 'Gender',
      interests: 'Academic Interests',
      skills: 'Skills'
    };
    
    const currentInterests = selectedInterests.join(', ');
    const currentSkills = selectedSkills.join(', ');
    
    if ((formData.fullname || '') !== original.fullname) changes.push(fieldLabels.fullname);
    if ((formData.gwa || '') !== original.gwa) changes.push(fieldLabels.gwa);
    if ((formData.strand || '') !== original.strand) changes.push(fieldLabels.strand);
    if ((formData.age || '') !== original.age) changes.push(fieldLabels.age);
    if ((formData.gender || '') !== original.gender) changes.push(fieldLabels.gender);
    if (currentInterests !== (original.interests || '')) changes.push(fieldLabels.interests);
    if (currentSkills !== (original.skills || '')) changes.push(fieldLabels.skills);
    
    return changes;
  };

  const handleSaveProfile = () => {
    // Validate required fields
    if (!formData.gwa || !formData.strand) {
      showToast('Please fill in both GWA and SHS Strand to save your profile', 'warning');
      return;
    }
    
    // Validate fullname if provided
    if (formData.fullname) {
      // Check for bad words in name
      if (containsBadWords(formData.fullname)) {
        showToast('Please use an appropriate name.', 'error');
        return;
      }
      
      // Check name only contains letters, spaces, hyphens, and apostrophes
      if (!/^[a-zA-Z\s'-]+$/.test(formData.fullname.trim())) {
        showToast('Name can only contain letters, spaces, hyphens, and apostrophes.', 'error');
        return;
      }
    }
    
    // Validate GWA range
    const gwaValue = parseFloat(formData.gwa);
    if (gwaValue > 100) {
      showToast('GWA cannot exceed 100', 'error');
      return;
    }
    if (gwaValue < 75) {
      showToast('GWA must be at least 75', 'error');
      return;
    }
    
    const userId = localStorage.getItem('userId');
    if (!userId) {
      showToast('User ID not found. Please log in again.', 'error');
      return;
    }
    
    console.log('Saving academic info for userId:', userId, 'with data:', formData);
    
    // Get what fields changed before saving
    const changedFields = getChangedFields();
    
    // Save to backend - include all profile fields
    fetch(`${API_BASE_URL}/user/${userId}/academic-info`, {
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
      showToast('Profile updated successfully!', 'success');
      onSave(changedFields);
    })
    .catch(err => {
      console.error('❌ Error saving to backend:', err);
      showToast('Profile saved locally but failed to sync with server. Please try again.', 'error');
    })
  };

  // Loading state if data isn't ready
  if (formData === null) {
    return (
      <div style={{...styles.pageWrapper, justifyContent: 'center', alignItems: 'center'}}>
        <div style={{color: '#6366f1', fontWeight: 'bold', fontSize: '18px'}}>Loading profile data...</div>
      </div>
    );
  }

  return (
    <div style={styles.pageWrapper}>
      {/* TOP NAVIGATION BAR */}
      <nav style={styles.navbar}>
        <div style={styles.navContainer}>
          <div style={styles.navBrand}>
            <img src="/logo.png" alt="CoursePro" style={styles.navLogo} />
            <span style={styles.navBrandName}>CoursePro</span>
          </div>
          
          <div style={styles.navLinks}>
            <span style={styles.navLink} onClick={onBack}>Dashboard</span>
            <span style={{...styles.navLink, ...styles.navLinkActive}}>Academic Profile</span>
          </div>

          <div style={styles.navRight}>
            <button onClick={onBack} style={styles.discardBtn}>← Back to Dashboard</button>
          </div>
        </div>
      </nav>

      {/* MAIN CONTENT */}
      <main style={styles.mainContent}>
        {/* Hero Header */}
        <div style={styles.heroHeader}>
          <div style={styles.heroBadge}>
            <span>📝</span> Configure Your Profile
          </div>
          <h1 style={styles.heroTitle}>
            Academic <span style={styles.heroGradient}>Profile</span>
          </h1>
          <p style={styles.heroSubtitle}>
            Personalize your background for more accurate AI-powered course recommendations.
          </p>
        </div>

        <div style={styles.formContainer}>
          <form style={styles.glassCard} onSubmit={(e) => { e.preventDefault(); onSave(); }}>
            
            <div style={styles.formSectionTitle}>Basic Information</div>
            
            {/* PROFILE PHOTO */}
            <div style={styles.photoSection}>
              <div style={styles.photoWrapper}>
                {profilePhoto ? (
                  <img src={profilePhoto} alt="Profile" style={styles.photoImage} />
                ) : (
                  <div style={styles.photoPlaceholder}>
                    <span style={styles.photoIcon}>👤</span>
                  </div>
                )}
                <div style={styles.photoOverlay} onClick={() => fileInputRef.current?.click()}>
                  <span>📷</span>
                </div>
              </div>
              <input
                type="file"
                ref={fileInputRef}
                onChange={handlePhotoUpload}
                accept="image/*"
                style={{ display: 'none' }}
              />
              <div style={styles.photoActions}>
                <button 
                  type="button"
                  onClick={() => fileInputRef.current?.click()} 
                  style={styles.uploadBtn}
                >
                  {profilePhoto ? 'Change Photo' : 'Upload Photo'}
                </button>
                {profilePhoto && (
                  <button 
                    type="button"
                    onClick={removePhoto} 
                    style={styles.removePhotoBtn}
                  >
                    Remove
                  </button>
                )}
              </div>
              <p style={styles.photoHint}>Max 2MB • JPG, PNG, or GIF</p>
            </div>
            
            {/* USERNAME FIELD - Read-only so user can see their username */}
            <div style={{...styles.inputGroup, marginBottom: '25px'}}>
              <label style={styles.label}>Username</label>
              <div style={{
                ...styles.input,
                backgroundColor: 'rgba(255,255,255,0.03)',
                color: 'rgba(255,255,255,0.7)',
                cursor: 'not-allowed',
                display: 'flex',
                alignItems: 'center',
                gap: '10px'
              }}>
                <span style={{ color: 'rgba(139, 92, 246, 0.8)' }}>@</span>
                <span>{localStorage.getItem('userUsername') || 'Unknown'}</span>
                <span style={{ 
                  marginLeft: 'auto', 
                  fontSize: '11px', 
                  color: 'rgba(255,255,255,0.4)',
                  backgroundColor: 'rgba(255,255,255,0.05)',
                  padding: '3px 8px',
                  borderRadius: '4px'
                }}>
                  Cannot be changed
                </span>
              </div>
            </div>
            
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
              <label style={styles.label}>Academic Interests</label>
              <div 
                onClick={() => setInterestModalOpen(true)}
                style={{
                  ...styles.clickableField,
                  minHeight: selectedInterests.length > 0 ? 'auto' : '50px'
                }}
              >
                {selectedInterests.length > 0 ? (
                  <div style={styles.selectedTagsContainer}>
                    {selectedInterests.map(id => {
                      const interest = INTEREST_OPTIONS.find(o => o.id === id);
                      return (
                        <div key={id} style={styles.selectedTag}>
                          <span>{interest?.label}</span>
                          <span 
                            onClick={(e) => {
                              e.stopPropagation();
                              toggleInterest(id);
                            }}
                            style={styles.removeBtn}
                          >
                            ×
                          </span>
                        </div>
                      );
                    })}
                  </div>
                ) : (
                  <span style={{color: 'rgba(255,255,255,0.4)'}}>Click to select interests...</span>
                )}
              </div>
            </div>

            <div style={{...styles.inputGroup, marginTop: '30px'}}>
              <label style={styles.label}>Technical & Soft Skills</label>
              <div 
                onClick={() => setSkillsModalOpen(true)}
                style={{
                  ...styles.clickableField,
                  minHeight: selectedSkills.length > 0 ? 'auto' : '50px'
                }}
              >
                {selectedSkills.length > 0 ? (
                  <div style={styles.selectedTagsContainer}>
                    {selectedSkills.map(id => {
                      const skill = SKILL_OPTIONS.find(o => o.id === id);
                      return (
                        <div key={id} style={styles.selectedTag}>
                          <span>{skill?.label}</span>
                          <span 
                            onClick={(e) => {
                              e.stopPropagation();
                              toggleSkill(id);
                            }}
                            style={styles.removeBtn}
                          >
                            ×
                          </span>
                        </div>
                      );
                    })}
                  </div>
                ) : (
                  <span style={{color: 'rgba(255,255,255,0.4)'}}>Click to select skills...</span>
                )}
              </div>
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
            <div style={styles.tipsList}>
              <div style={styles.tipItem}>✓ Add at least 3 interests</div>
              <div style={styles.tipItem}>✓ Include both technical & soft skills</div>
              <div style={styles.tipItem}>✓ Keep GWA accurate</div>
            </div>
          </div>
        </div>
      </main>

      {/* ACADEMIC INTERESTS MODAL */}
      {interestModalOpen && (
        <div style={styles.modalOverlay} onClick={() => setInterestModalOpen(false)}>
          <div style={styles.modalContent} onClick={(e) => e.stopPropagation()}>
            <div style={styles.modalHeader}>
              <h2 style={styles.modalTitle}>Select Academic Interests</h2>
              <button onClick={() => setInterestModalOpen(false)} style={styles.closeBtn}>✕</button>
            </div>
            <div style={styles.modalBody}>
              {Object.values(
                INTEREST_OPTIONS.reduce((acc, option) => {
                  if (!acc[option.category]) acc[option.category] = [];
                  acc[option.category].push(option);
                  return acc;
                }, {})
              ).map((categoryItems, idx) => (
                <div key={idx} style={styles.categorySection}>
                  <h3 style={styles.categoryTitle}>{categoryItems[0].category}</h3>
                  <div style={styles.tagsGrid}>
                    {categoryItems.map(option => (
                      <div
                        key={option.id}
                        onClick={() => toggleInterest(option.id)}
                        style={selectedInterests.includes(option.id) ? {
                          ...styles.modalTag,
                          ...styles.modalTagSelected
                        } : {
                          ...styles.modalTag,
                          borderColor: 'rgba(255, 255, 255, 0.06)',
                          boxShadow: 'none'
                        }}
                      >
                        <span>{option.label}</span>
                        {selectedInterests.includes(option.id) && (
                          <span style={styles.checkmark}>✓</span>
                        )}
                      </div>
                    ))}
                  </div>
                </div>
              ))}
            </div>
            <div style={styles.modalFooter}>
              <button onClick={() => setInterestModalOpen(false)} style={styles.modalCloseBtn}>
                Done ({selectedInterests.length} selected)
              </button>
            </div>
          </div>
        </div>
      )}

      {/* TECHNICAL & SOFT SKILLS MODAL */}
      {skillsModalOpen && (
        <div style={styles.modalOverlay} onClick={() => setSkillsModalOpen(false)}>
          <div style={styles.modalContent} onClick={(e) => e.stopPropagation()}>
            <div style={styles.modalHeader}>
              <h2 style={styles.modalTitle}>Select Technical & Soft Skills</h2>
              <button onClick={() => setSkillsModalOpen(false)} style={styles.closeBtn}>✕</button>
            </div>
            <div style={styles.modalBody}>
              {Object.values(
                SKILL_OPTIONS.reduce((acc, option) => {
                  if (!acc[option.category]) acc[option.category] = [];
                  acc[option.category].push(option);
                  return acc;
                }, {})
              ).map((categoryItems, idx) => (
                <div key={idx} style={styles.categorySection}>
                  <h3 style={styles.categoryTitle}>{categoryItems[0].category}</h3>
                  <div style={styles.tagsGrid}>
                    {categoryItems.map(option => (
                      <div
                        key={option.id}
                        onClick={() => toggleSkill(option.id)}
                        style={selectedSkills.includes(option.id) ? {
                          ...styles.modalTag,
                          ...styles.modalTagSelected
                        } : {
                          ...styles.modalTag,
                          borderColor: 'rgba(255, 255, 255, 0.06)',
                          boxShadow: 'none'
                        }}
                      >
                        <span>{option.label}</span>
                        {selectedSkills.includes(option.id) && (
                          <span style={styles.checkmark}>✓</span>
                        )}
                      </div>
                    ))}
                  </div>
                </div>
              ))}
            </div>
            <div style={styles.modalFooter}>
              <button onClick={() => setSkillsModalOpen(false)} style={styles.modalCloseBtn}>
                Done ({selectedSkills.length} selected)
              </button>
            </div>
          </div>
        </div>
      )}

      {toast && (
        <Toast 
          message={toast.message} 
          type={toast.type} 
          onClose={() => setToast(null)}
        />
      )}
    </div>
  );
}

const styles = {
  pageWrapper: { 
    minHeight: '100vh',
    background: '#050510',
    display: 'flex',
    flexDirection: 'column',
    position: 'relative',
  },
  navbar: {
    position: 'sticky',
    top: 0,
    zIndex: 100,
    background: 'rgba(5, 5, 16, 0.8)',
    backdropFilter: 'blur(20px)',
    borderBottom: '1px solid rgba(255,255,255,0.05)',
    padding: '12px 0',
  },
  navContainer: {
    maxWidth: '1400px',
    margin: '0 auto',
    padding: '0 40px',
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
  },
  navBrand: {
    display: 'flex',
    alignItems: 'center',
    gap: '12px',
  },
  navLogo: {
    width: '48px',
    height: '48px',
    objectFit: 'cover',
    borderRadius: '12px',
    background: 'linear-gradient(135deg, rgba(99, 102, 241, 0.15) 0%, rgba(139, 92, 246, 0.15) 100%)',
    padding: '0',
    boxShadow: '0 0 20px rgba(99, 102, 241, 0.4), 0 0 40px rgba(139, 92, 246, 0.2), inset 0 0 20px rgba(255, 255, 255, 0.05)',
    border: '1px solid rgba(139, 92, 246, 0.3)',
  },
  navBrandName: {
    fontSize: '20px',
    fontWeight: '700',
    background: 'linear-gradient(135deg, #f8fafc 0%, #94a3b8 100%)',
    WebkitBackgroundClip: 'text',
    WebkitTextFillColor: 'transparent',
  },
  navLinks: {
    display: 'flex',
    alignItems: 'center',
    gap: '32px',
  },
  navLink: {
    color: '#94a3b8',
    fontSize: '14px',
    fontWeight: '500',
    cursor: 'pointer',
    transition: 'color 0.2s ease',
    padding: '8px 0',
  },
  navLinkActive: {
    color: '#a5b4fc',
    fontWeight: '600',
    borderBottom: '2px solid #6366f1',
  },
  navRight: {
    display: 'flex',
    alignItems: 'center',
    gap: '16px',
  },
  discardBtn: {
    background: 'rgba(239, 68, 68, 0.1)',
    border: '1px solid rgba(239, 68, 68, 0.2)',
    color: '#f87171',
    padding: '10px 20px',
    borderRadius: '10px',
    fontSize: '14px',
    fontWeight: '600',
    cursor: 'pointer',
    transition: 'all 0.2s ease',
  },
  mainContent: { 
    flex: 1, 
    padding: '48px 40px',
    maxWidth: '1400px',
    margin: '0 auto',
    width: '100%',
    boxSizing: 'border-box',
  },
  heroHeader: {
    textAlign: 'center',
    marginBottom: '48px',
  },
  heroBadge: {
    display: 'inline-flex',
    alignItems: 'center',
    gap: '8px',
    background: 'rgba(99, 102, 241, 0.1)',
    border: '1px solid rgba(99, 102, 241, 0.2)',
    borderRadius: '50px',
    padding: '8px 20px',
    fontSize: '13px',
    color: '#a5b4fc',
    fontWeight: '600',
    marginBottom: '24px',
  },
  heroTitle: {
    fontSize: '42px',
    fontWeight: '800',
    color: '#f8fafc',
    margin: '0 0 16px 0',
    lineHeight: 1.2,
  },
  heroGradient: {
    background: 'linear-gradient(135deg, #6366f1 0%, #8b5cf6 50%, #a855f7 100%)',
    WebkitBackgroundClip: 'text',
    WebkitTextFillColor: 'transparent',
  },
  heroSubtitle: {
    color: '#64748b',
    fontSize: '16px',
    maxWidth: '600px',
    margin: '0 auto',
    lineHeight: 1.6,
  },
  formContainer: { 
    display: 'grid', 
    gridTemplateColumns: '1fr 320px', 
    gap: '40px', 
    alignItems: 'start',
    maxWidth: '1200px',
    margin: '0 auto',
  },
  glassCard: { 
    background: 'rgba(15, 23, 42, 0.6)', 
    backdropFilter: 'blur(20px)',
    WebkitBackdropFilter: 'blur(20px)',
    border: '1px solid rgba(255, 255, 255, 0.06)', 
    borderRadius: '24px', 
    padding: '40px', 
    boxShadow: '0 20px 40px rgba(0,0,0,0.2)' 
  },
  formSectionTitle: { 
    fontSize: '13px', 
    fontWeight: '700', 
    color: '#a5b4fc', 
    textTransform: 'uppercase', 
    letterSpacing: '1px', 
    marginBottom: '24px',
    display: 'flex',
    alignItems: 'center',
    gap: '8px',
  },
  
  // Profile Photo Styles
  photoSection: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    marginBottom: '32px',
    padding: '24px',
    background: 'rgba(255, 255, 255, 0.02)',
    borderRadius: '16px',
    border: '1px solid rgba(255, 255, 255, 0.04)',
  },
  photoWrapper: {
    position: 'relative',
    width: '120px',
    height: '120px',
    borderRadius: '50%',
    overflow: 'hidden',
    marginBottom: '16px',
    border: '3px solid rgba(99, 102, 241, 0.3)',
    boxShadow: '0 8px 32px rgba(99, 102, 241, 0.2)',
  },
  photoImage: {
    width: '100%',
    height: '100%',
    objectFit: 'cover',
  },
  photoPlaceholder: {
    width: '100%',
    height: '100%',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    background: 'linear-gradient(135deg, #1e293b 0%, #0f172a 100%)',
  },
  photoIcon: {
    fontSize: '48px',
    opacity: 0.5,
  },
  photoOverlay: {
    position: 'absolute',
    bottom: 0,
    left: 0,
    right: 0,
    height: '36px',
    background: 'rgba(0, 0, 0, 0.7)',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    cursor: 'pointer',
    fontSize: '16px',
    opacity: 0.8,
    transition: 'opacity 0.2s ease',
  },
  photoActions: {
    display: 'flex',
    gap: '10px',
    marginBottom: '8px',
  },
  uploadBtn: {
    padding: '10px 20px',
    background: 'linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%)',
    border: 'none',
    borderRadius: '10px',
    color: 'white',
    fontSize: '13px',
    fontWeight: '600',
    cursor: 'pointer',
    transition: 'all 0.2s ease',
  },
  removePhotoBtn: {
    padding: '10px 20px',
    background: 'rgba(239, 68, 68, 0.1)',
    border: '1px solid rgba(239, 68, 68, 0.2)',
    borderRadius: '10px',
    color: '#f87171',
    fontSize: '13px',
    fontWeight: '600',
    cursor: 'pointer',
    transition: 'all 0.2s ease',
  },
  photoHint: {
    margin: 0,
    fontSize: '12px',
    color: '#64748b',
  },
  
  formGrid: { 
    display: 'grid', 
    gridTemplateColumns: '1fr 1fr', 
    gap: '24px' 
  },
  inputGroup: { 
    display: 'flex', 
    flexDirection: 'column' 
  },
  label: { 
    fontSize: '13px', 
    fontWeight: '600', 
    color: '#94a3b8', 
    marginBottom: '10px', 
    marginLeft: '4px' 
  },
  input: { 
    padding: '14px 18px', 
    background: 'rgba(30, 41, 59, 0.8)', 
    border: '1px solid rgba(255,255,255,0.06)', 
    borderRadius: '12px', 
    color: '#f1f5f9', 
    fontSize: '15px', 
    outline: 'none',
    boxSizing: 'border-box',
    transition: 'all 0.2s ease'
  },
  option: {
    background: '#1e293b', 
    color: '#f1f5f9'
  },
  footer: { 
    marginTop: '40px', 
    borderTop: '1px solid rgba(255,255,255,0.06)', 
    paddingTop: '32px', 
    display: 'flex', 
    justifyContent: 'flex-end' 
  },
  saveBtn: { 
    background: 'linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%)', 
    color: 'white', 
    padding: '16px 36px', 
    borderRadius: '14px', 
    border: 'none', 
    fontWeight: '700', 
    fontSize: '15px', 
    cursor: 'pointer', 
    boxShadow: '0 8px 24px rgba(99, 102, 241, 0.25)',
    transition: 'all 0.3s ease'
  },
  infoCol: { 
    background: 'rgba(15, 23, 42, 0.6)', 
    backdropFilter: 'blur(20px)',
    border: '1px solid rgba(99, 102, 241, 0.15)', 
    borderRadius: '20px', 
    padding: '28px',
    position: 'sticky',
    top: '120px',
  },
  statusBox: { 
    display: 'flex', 
    alignItems: 'center', 
    gap: '10px', 
    marginBottom: '16px',
    background: 'rgba(16, 185, 129, 0.1)',
    padding: '10px 14px',
    borderRadius: '10px',
  },
  statusDot: { 
    width: '10px', 
    height: '10px', 
    borderRadius: '50%', 
    background: '#10b981', 
    boxShadow: '0 0 12px rgba(16, 185, 129, 0.5)',
    animation: 'pulse 2s infinite',
  },
  infoText: { 
    fontSize: '14px', 
    color: '#94a3b8', 
    lineHeight: '1.7', 
    margin: '0 0 20px 0' 
  },
  tipsList: {
    display: 'flex',
    flexDirection: 'column',
    gap: '10px',
  },
  tipItem: {
    fontSize: '13px',
    color: '#64748b',
    padding: '10px 14px',
    background: 'rgba(255,255,255,0.02)',
    borderRadius: '8px',
    border: '1px solid rgba(255,255,255,0.04)',
  },
  checkboxGrid: {
    display: 'grid',
    gridTemplateColumns: 'repeat(auto-fill, minmax(180px, 1fr))',
    gap: '12px',
    maxHeight: '320px',
    overflowY: 'auto',
    padding: '18px',
    background: 'rgba(30, 41, 59, 0.5)',
    borderRadius: '14px',
    border: '1px solid rgba(255,255,255,0.06)',
  },
  checkboxLabel: {
    display: 'flex',
    alignItems: 'center',
    gap: '10px',
    padding: '12px 16px',
    background: 'rgba(255,255,255,0.02)',
    borderRadius: '10px',
    cursor: 'pointer',
    fontSize: '13px',
    color: '#94a3b8',
    border: '1px solid rgba(255,255,255,0.04)',
    transition: 'all 0.2s ease',
  },
  checkboxLabelSelected: {
    background: 'rgba(99, 102, 241, 0.12)',
    borderColor: 'rgba(99, 102, 241, 0.3)',
    color: '#a5b4fc',
  },
  checkbox: {
    width: '18px',
    height: '18px',
    accentColor: '#6366f1',
    cursor: 'pointer',
  },
  tagsContainer: {
    display: 'flex',
    flexWrap: 'wrap',
    gap: '14px',
    padding: '24px',
    background: 'rgba(30, 41, 59, 0.4)',
    borderRadius: '16px',
    border: '1px solid rgba(255,255,255,0.06)',
    minHeight: '140px',
    alignContent: 'flex-start',
  },
  tagItem: {
    padding: '12px 20px',
    background: 'rgba(255,255,255,0.03)',
    border: '2px solid rgba(255,255,255,0.06)',
    borderRadius: '12px',
    cursor: 'pointer',
    fontSize: '13px',
    color: '#94a3b8',
    fontWeight: '500',
    transition: 'all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1)',
    whiteSpace: 'nowrap',
    transform: 'scale(1)',
    boxShadow: 'none',
  },
  tagItemSelected: {
    background: 'linear-gradient(135deg, rgba(99, 102, 241, 0.2), rgba(139, 92, 246, 0.12))',
    borderColor: 'rgba(99, 102, 241, 0.5)',
    color: '#a5b4fc',
    fontWeight: '600',
    transform: 'scale(1.03)',
    boxShadow: '0 8px 20px rgba(99, 102, 241, 0.2)',
  },
  clickableField: {
    padding: '14px 18px',
    background: 'rgba(30, 41, 59, 0.8)',
    border: '1px solid rgba(255,255,255,0.06)',
    borderRadius: '12px',
    color: '#f1f5f9',
    fontSize: '15px',
    outline: 'none',
    boxSizing: 'border-box',
    cursor: 'pointer',
    transition: 'all 0.2s ease',
    display: 'flex',
    alignItems: 'flex-start',
    flexWrap: 'wrap',
    gap: '10px',
  },
  selectedTagsContainer: {
    display: 'flex',
    flexWrap: 'wrap',
    gap: '10px',
    width: '100%',
  },
  selectedTag: {
    display: 'flex',
    alignItems: 'center',
    gap: '8px',
    padding: '8px 14px',
    background: 'rgba(99, 102, 241, 0.15)',
    border: '1px solid rgba(99, 102, 241, 0.3)',
    borderRadius: '8px',
    color: '#a5b4fc',
    fontSize: '12px',
    fontWeight: '600',
  },
  removeBtn: {
    cursor: 'pointer',
    fontWeight: 'bold',
    fontSize: '16px',
    color: '#f87171',
    transition: 'color 0.2s ease',
  },
  modalOverlay: {
    position: 'fixed',
    top: 0,
    left: 0,
    right: 0,
    bottom: 0,
    background: 'rgba(0, 0, 0, 0.7)',
    backdropFilter: 'blur(8px)',
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    zIndex: 1000,
  },
  modalContent: {
    background: 'rgba(15, 23, 42, 0.95)',
    backdropFilter: 'blur(20px)',
    border: '1px solid rgba(255, 255, 255, 0.08)',
    borderRadius: '24px',
    width: '90%',
    maxWidth: '720px',
    maxHeight: '85vh',
    display: 'flex',
    flexDirection: 'column',
    boxShadow: '0 25px 60px rgba(0, 0, 0, 0.4)',
  },
  modalHeader: {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    padding: '28px 32px',
    borderBottom: '1px solid rgba(255, 255, 255, 0.06)',
  },
  modalTitle: {
    fontSize: '22px',
    fontWeight: '700',
    background: 'linear-gradient(135deg, #f8fafc 0%, #cbd5e1 100%)',
    WebkitBackgroundClip: 'text',
    WebkitTextFillColor: 'transparent',
    margin: 0,
  },
  closeBtn: {
    background: 'none',
    border: 'none',
    color: '#64748b',
    fontSize: '24px',
    cursor: 'pointer',
    padding: '4px 8px',
    transition: 'color 0.2s ease',
  },
  modalBody: {
    flex: 1,
    overflowY: 'auto',
    padding: '28px 32px',
  },
  categorySection: {
    marginBottom: '32px',
  },
  categoryTitle: {
    fontSize: '12px',
    fontWeight: '700',
    color: '#a5b4fc',
    textTransform: 'uppercase',
    letterSpacing: '1px',
    marginBottom: '16px',
    margin: '0 0 16px 0',
  },
  tagsGrid: {
    display: 'grid',
    gridTemplateColumns: 'repeat(auto-fill, minmax(170px, 1fr))',
    gap: '12px',
  },
  modalTag: {
    padding: '14px 16px',
    background: 'rgba(255, 255, 255, 0.03)',
    border: '2px solid rgba(255, 255, 255, 0.06)',
    borderRadius: '12px',
    cursor: 'pointer',
    fontSize: '13px',
    color: '#94a3b8',
    fontWeight: '500',
    transition: 'all 0.2s ease',
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    gap: '10px',
  },
  modalTagSelected: {
    background: 'rgba(99, 102, 241, 0.15)',
    borderColor: 'rgba(99, 102, 241, 0.5)',
    color: '#a5b4fc',
    fontWeight: '600',
    boxShadow: '0 0 20px rgba(99, 102, 241, 0.15)',
  },
  checkmark: {
    color: '#10b981',
    fontSize: '16px',
    fontWeight: 'bold',
  },
  modalFooter: {
    padding: '24px 32px',
    borderTop: '1px solid rgba(255, 255, 255, 0.06)',
    display: 'flex',
    justifyContent: 'flex-end',
  },
  modalCloseBtn: {
    background: 'linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%)',
    color: 'white',
    padding: '14px 28px',
    borderRadius: '12px',
    border: 'none',
    fontWeight: '600',
    fontSize: '14px',
    cursor: 'pointer',
    transition: 'all 0.2s ease',
    boxShadow: '0 4px 16px rgba(99, 102, 241, 0.2)',
  },
};

export default ProfileForm;
