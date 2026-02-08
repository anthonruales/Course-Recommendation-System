import React, { useState, useEffect, useRef } from 'react';
import API_BASE_URL from './config';
import Toast from './Toast';

// Bad words filter list
const BAD_WORDS = [
  'fuck', 'shit', 'ass', 'bitch', 'damn', 'crap', 'bastard', 'dick', 'pussy', 'cock',
  'asshole', 'motherfucker', 'nigger', 'nigga', 'faggot', 'slut', 'whore', 'cunt',
  'retard', 'idiot', 'stupid', 'dumb', 'moron', 'loser', 'gay', 'homo', 'lesbian',
  'puta', 'gago', 'tangina', 'taena', 'bobo', 'tanga', 'putangina', 'ulol', 'lintik',
  'peste', 'punyeta', 'leche', 'hayop', 'animal', 'pokpok', 'malandi'
];

const capitalizeName = (name) => {
  if (!name) return '';
  return name.toLowerCase().split(' ').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');
};

const containsBadWords = (name) => {
  if (!name) return false;
  const lowerName = name.toLowerCase().replace(/[^a-z\s]/g, '');
  const words = lowerName.split(/\s+/);
  return words.some(word => BAD_WORDS.includes(word));
};

// Predefined options for Academic Interests
const INTEREST_OPTIONS = [
  { id: 'science', label: 'Science & Research', category: 'Science' },
  { id: 'biology', label: 'Biology & Life Sciences', category: 'Science' },
  { id: 'chemistry', label: 'Chemistry', category: 'Science' },
  { id: 'physics', label: 'Physics', category: 'Science' },
  { id: 'environment', label: 'Environment & Nature', category: 'Science' },
  { id: 'programming', label: 'Programming & Coding', category: 'Technology' },
  { id: 'computer', label: 'Computers & IT', category: 'Technology' },
  { id: 'data', label: 'Data & Analytics', category: 'Technology' },
  { id: 'ai', label: 'AI & Machine Learning', category: 'Technology' },
  { id: 'cybersecurity', label: 'Cybersecurity', category: 'Technology' },
  { id: 'engineering', label: 'Engineering', category: 'Engineering' },
  { id: 'mechanical', label: 'Mechanical Systems', category: 'Engineering' },
  { id: 'electrical', label: 'Electrical & Electronics', category: 'Engineering' },
  { id: 'civil', label: 'Civil & Construction', category: 'Engineering' },
  { id: 'business', label: 'Business & Entrepreneurship', category: 'Business' },
  { id: 'finance', label: 'Finance & Banking', category: 'Business' },
  { id: 'marketing', label: 'Marketing & Advertising', category: 'Business' },
  { id: 'accounting', label: 'Accounting', category: 'Business' },
  { id: 'economics', label: 'Economics', category: 'Business' },
  { id: 'art', label: 'Arts & Design', category: 'Arts' },
  { id: 'music', label: 'Music & Performance', category: 'Arts' },
  { id: 'film', label: 'Film & Media Production', category: 'Arts' },
  { id: 'writing', label: 'Writing & Literature', category: 'Arts' },
  { id: 'photography', label: 'Photography & Visual Arts', category: 'Arts' },
  { id: 'medical', label: 'Medicine & Healthcare', category: 'Healthcare' },
  { id: 'nursing', label: 'Nursing & Patient Care', category: 'Healthcare' },
  { id: 'psychology', label: 'Psychology & Mental Health', category: 'Healthcare' },
  { id: 'education', label: 'Education & Teaching', category: 'Social' },
  { id: 'law', label: 'Law & Justice', category: 'Social' },
  { id: 'politics', label: 'Politics & Government', category: 'Social' },
  { id: 'social', label: 'Social Work & Community', category: 'Social' },
  { id: 'history', label: 'History & Culture', category: 'Social' },
  { id: 'sports', label: 'Sports & Fitness', category: 'Others' },
  { id: 'tourism', label: 'Tourism & Hospitality', category: 'Others' },
  { id: 'food', label: 'Culinary & Food Science', category: 'Others' },
  { id: 'agriculture', label: 'Agriculture & Farming', category: 'Others' },
];

// Predefined options for Skills
const SKILL_OPTIONS = [
  { id: 'programming_skill', label: 'Programming / Coding', category: 'Technical' },
  { id: 'data_analysis', label: 'Data Analysis', category: 'Technical' },
  { id: 'web_development', label: 'Web Development', category: 'Technical' },
  { id: 'graphic_design', label: 'Graphic Design', category: 'Technical' },
  { id: 'video_editing', label: 'Video Editing', category: 'Technical' },
  { id: 'math_skills', label: 'Mathematics', category: 'Technical' },
  { id: 'laboratory', label: 'Laboratory Work', category: 'Technical' },
  { id: 'technical_writing', label: 'Technical Writing', category: 'Technical' },
  { id: 'public_speaking', label: 'Public Speaking', category: 'Communication' },
  { id: 'writing_skill', label: 'Writing & Composition', category: 'Communication' },
  { id: 'presentation', label: 'Presentation Skills', category: 'Communication' },
  { id: 'negotiation', label: 'Negotiation', category: 'Communication' },
  { id: 'foreign_language', label: 'Foreign Languages', category: 'Communication' },
  { id: 'leadership', label: 'Leadership', category: 'Leadership' },
  { id: 'project_management', label: 'Project Management', category: 'Leadership' },
  { id: 'team_management', label: 'Team Management', category: 'Leadership' },
  { id: 'decision_making', label: 'Decision Making', category: 'Leadership' },
  { id: 'planning', label: 'Planning & Organization', category: 'Leadership' },
  { id: 'teamwork', label: 'Teamwork & Collaboration', category: 'Interpersonal' },
  { id: 'empathy', label: 'Empathy & Compassion', category: 'Interpersonal' },
  { id: 'customer_service', label: 'Customer Service', category: 'Interpersonal' },
  { id: 'mentoring', label: 'Mentoring & Teaching', category: 'Interpersonal' },
  { id: 'conflict_resolution', label: 'Conflict Resolution', category: 'Interpersonal' },
  { id: 'critical_thinking', label: 'Critical Thinking', category: 'Analytical' },
  { id: 'problem_solving', label: 'Problem Solving', category: 'Analytical' },
  { id: 'research', label: 'Research & Investigation', category: 'Analytical' },
  { id: 'attention_detail', label: 'Attention to Detail', category: 'Analytical' },
  { id: 'logical_reasoning', label: 'Logical Reasoning', category: 'Analytical' },
  { id: 'creativity', label: 'Creativity & Innovation', category: 'Creative' },
  { id: 'artistic', label: 'Artistic Ability', category: 'Creative' },
  { id: 'music_skill', label: 'Musical Ability', category: 'Creative' },
  { id: 'storytelling', label: 'Storytelling', category: 'Creative' },
  { id: 'design_thinking', label: 'Design Thinking', category: 'Creative' },
];

function Settings({ formData = {}, setFormData, onSave, onBack }) {
  const [activeSection, setActiveSection] = useState('profile');
  const [gwaError, setGwaError] = useState('');
  const [interestModalOpen, setInterestModalOpen] = useState(false);
  const [skillsModalOpen, setSkillsModalOpen] = useState(false);
  const [toast, setToast] = useState(null);
  const [profilePhoto, setProfilePhoto] = useState(null);
  const [newEmail, setNewEmail] = useState('');
  const [emailError, setEmailError] = useState('');
  const [passwordData, setPasswordData] = useState({
    currentPassword: '',
    newPassword: '',
    confirmPassword: ''
  });
  const [passwordError, setPasswordError] = useState('');
  const [showPasswords, setShowPasswords] = useState({
    current: false,
    new: false,
    confirm: false
  });
  const fileInputRef = useRef(null);
  
  // Load saved profile photo and email
  useEffect(() => {
    const userId = localStorage.getItem('userId');
    if (userId) {
      const savedPhoto = localStorage.getItem(`profilePhoto_${userId}`);
      if (savedPhoto) {
        setProfilePhoto(savedPhoto);
      }
    }
    const savedEmail = localStorage.getItem('userEmail');
    if (savedEmail) {
      setNewEmail(savedEmail);
    }
  }, []);
  
  const showToast = (message, type = 'info') => {
    setToast({ message, type });
  };
  
  // Handle profile photo upload
  const handlePhotoUpload = (e) => {
    const file = e.target.files[0];
    if (file) {
      if (file.size > 2 * 1024 * 1024) {
        showToast('Image size must be less than 2MB', 'error');
        return;
      }
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
  
  // Parse interests and skills
  const selectedInterests = formData?.interests 
    ? formData.interests.split(',').map(i => i.trim()).filter(i => i) 
    : [];
  const selectedSkills = formData?.skills 
    ? formData.skills.split(',').map(s => s.trim()).filter(s => s) 
    : [];
  
  const toggleInterest = (interestId) => {
    const current = [...selectedInterests];
    const index = current.indexOf(interestId);
    if (index > -1) {
      current.splice(index, 1);
    } else {
      current.push(interestId);
    }
    setFormData(prev => ({ ...prev, interests: current.join(',') }));
  };
  
  const toggleSkill = (skillId) => {
    const current = [...selectedSkills];
    const index = current.indexOf(skillId);
    if (index > -1) {
      current.splice(index, 1);
    } else {
      current.push(skillId);
    }
    setFormData(prev => ({ ...prev, skills: current.join(',') }));
  };
  
  const handleChange = (e) => {
    const { name, value } = e.target;
    
    if (name === 'fullname') {
      const capitalizedName = capitalizeName(value);
      setFormData(prev => ({ ...prev, fullname: capitalizedName }));
      return;
    }
    
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
    
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  // Track original values
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
    
    if ((formData.fullname || '') !== original.fullname) changes.push(fieldLabels.fullname);
    if ((formData.gwa || '') !== original.gwa) changes.push(fieldLabels.gwa);
    if ((formData.strand || '') !== original.strand) changes.push(fieldLabels.strand);
    if ((formData.age || '') !== original.age) changes.push(fieldLabels.age);
    if ((formData.gender || '') !== original.gender) changes.push(fieldLabels.gender);
    if (selectedInterests.join(', ') !== (original.interests || '')) changes.push(fieldLabels.interests);
    if (selectedSkills.join(', ') !== (original.skills || '')) changes.push(fieldLabels.skills);
    
    return changes;
  };

  const handleSaveProfile = async () => {
    if (!formData.gwa || !formData.strand) {
      showToast('Please fill in both GWA and SHS Strand to save your profile', 'warning');
      return;
    }
    
    if (formData.fullname) {
      if (containsBadWords(formData.fullname)) {
        showToast('Please use an appropriate name.', 'error');
        return;
      }
      if (!/^[a-zA-Z\s'-]+$/.test(formData.fullname.trim())) {
        showToast('Name can only contain letters, spaces, hyphens, and apostrophes.', 'error');
        return;
      }
    }
    
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
    
    const changedFields = getChangedFields();
    const currentEmail = localStorage.getItem('userEmail') || '';
    
    // Check if email was changed
    if (newEmail && newEmail !== currentEmail) {
      // Validate email format
      if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(newEmail)) {
        setEmailError('Please enter a valid email address');
        showToast('Invalid email format', 'error');
        return;
      }
      
      try {
        const emailRes = await fetch(`${API_BASE_URL}/user/${userId}/change-email`, {
          method: 'PUT',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ new_email: newEmail })
        });
        
        const emailData = await emailRes.json();
        
        if (!emailRes.ok) {
          setEmailError(emailData.detail || 'Failed to update email');
          showToast(emailData.detail || 'Failed to update email', 'error');
          return;
        }
        
        // Update localStorage with new email
        localStorage.setItem('userEmail', newEmail);
        changedFields.push('Email');
        setEmailError('');
      } catch (err) {
        console.error('Error changing email:', err);
        showToast('Failed to update email. Please try again.', 'error');
        return;
      }
    }
    
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
      showToast('Profile updated successfully!', 'success');
      onSave(changedFields);
    })
    .catch(err => {
      console.error('Error saving to backend:', err);
      showToast('Failed to save profile. Please try again.', 'error');
    });
  };

  const handlePasswordChange = async () => {
    setPasswordError('');
    
    if (!passwordData.currentPassword) {
      setPasswordError('Please enter your current password');
      return;
    }
    if (!passwordData.newPassword) {
      setPasswordError('Please enter a new password');
      return;
    }
    if (passwordData.newPassword.length < 6) {
      setPasswordError('New password must be at least 6 characters');
      return;
    }
    if (passwordData.newPassword !== passwordData.confirmPassword) {
      setPasswordError('New passwords do not match');
      return;
    }
    
    const userId = localStorage.getItem('userId');
    if (!userId) {
      showToast('User ID not found. Please log in again.', 'error');
      return;
    }
    
    try {
      const response = await fetch(`${API_BASE_URL}/user/${userId}/change-password`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          current_password: passwordData.currentPassword,
          new_password: passwordData.newPassword
        })
      });
      
      const data = await response.json();
      
      if (!response.ok) {
        setPasswordError(data.detail || 'Failed to change password');
        return;
      }
      
      showToast('Password changed successfully!', 'success');
      setPasswordData({ currentPassword: '', newPassword: '', confirmPassword: '' });
    } catch (err) {
      console.error('Error changing password:', err);
      setPasswordError('Failed to change password. Please try again.');
    }
  };

  const userName = localStorage.getItem('userName') || 'User';
  const userEmail = localStorage.getItem('userEmail') || '';
  const userUsername = localStorage.getItem('userUsername') || '';

  const settingsSections = [
    { id: 'profile', label: 'Profile Information', icon: '👤' },
    { id: 'security', label: 'Password & Security', icon: '🔒' },
  ];

  return (
    <div style={styles.pageWrapper}>
      {/* Background */}
      <div style={styles.bgGradient1}></div>
      <div style={styles.bgGradient2}></div>
      <div style={styles.bgGrid}></div>

      {/* TOP NAVIGATION BAR */}
      <nav style={styles.navbar}>
        <div style={styles.navContainer}>
          <div style={styles.navBrand}>
            <img src="/logo.png" alt="CoursePro" style={styles.navLogo} />
            <span style={styles.navBrandName}>CoursePro</span>
          </div>
          
          <div style={styles.navLinks}>
            <span style={styles.navLink} onClick={onBack}>Dashboard</span>
            <span style={{...styles.navLink, ...styles.navLinkActive}}>Settings</span>
          </div>

          <div style={styles.navRight}>
            <button onClick={onBack} style={styles.backBtn}>← Back</button>
          </div>
        </div>
      </nav>

      {/* MAIN CONTENT */}
      <main style={styles.mainContent}>
        <div style={styles.settingsHeader}>
          <h1 style={styles.pageTitle}>
            <span style={styles.pageTitleIcon}>⚙️</span>
            Settings
          </h1>
          <p style={styles.pageSubtitle}>Manage your account settings and preferences</p>
        </div>

        <div style={styles.settingsLayout}>
          {/* Sidebar Navigation */}
          <div style={styles.sidebar}>
            {settingsSections.map(section => (
              <div
                key={section.id}
                onClick={() => setActiveSection(section.id)}
                style={activeSection === section.id ? {
                  ...styles.sidebarItem,
                  ...styles.sidebarItemActive
                } : styles.sidebarItem}
              >
                <span style={styles.sidebarIcon}>{section.icon}</span>
                <span>{section.label}</span>
              </div>
            ))}
          </div>

          {/* Content Area */}
          <div style={styles.contentArea}>
            {/* Profile Information Section - Combined */}
            {activeSection === 'profile' && (
              <div style={styles.section}>
                <h2 style={styles.sectionTitle}>Profile Information</h2>
                <p style={styles.sectionDesc}>Update your personal details, academic info, and preferences</p>
                
                {/* Profile Photo */}
                <div style={styles.photoSection}>
                  <div style={styles.photoWrapper}>
                    {profilePhoto ? (
                      <img src={profilePhoto} alt="Profile" style={styles.photoImage} />
                    ) : (
                      <div style={styles.photoPlaceholder}>
                        <span style={styles.photoIcon}>{userName.charAt(0).toUpperCase()}</span>
                      </div>
                    )}
                  </div>
                  <div style={styles.photoInfo}>
                    <h3 style={styles.photoLabel}>Profile Photo</h3>
                    <p style={styles.photoHint}>JPG, PNG or GIF. Max 2MB.</p>
                    <div style={styles.photoActions}>
                      <input
                        type="file"
                        ref={fileInputRef}
                        onChange={handlePhotoUpload}
                        accept="image/*"
                        style={{ display: 'none' }}
                      />
                      <button onClick={() => fileInputRef.current?.click()} style={styles.uploadBtn}>
                        Change Photo
                      </button>
                      {profilePhoto && (
                        <button onClick={removePhoto} style={styles.removeBtn}>
                          Remove
                        </button>
                      )}
                    </div>
                  </div>
                </div>

                {/* Basic Info Subsection */}
                <div style={styles.subsectionTitle}>Basic Information</div>
                <div style={styles.formGrid}>
                  <div style={styles.inputGroup}>
                    <label style={styles.label}>Username</label>
                    <div style={styles.readOnlyField}>
                      <span style={styles.atSymbol}>@</span>
                      {userUsername}
                      <span style={styles.readOnlyBadge}>Cannot be changed</span>
                    </div>
                  </div>
                  
                  <div style={styles.inputGroup}>
                    <label style={styles.label}>Email Address</label>
                    <input
                      style={{
                        ...styles.input,
                        ...(emailError ? { borderColor: '#ef4444' } : {})
                      }}
                      type="email"
                      value={newEmail}
                      onChange={(e) => {
                        setNewEmail(e.target.value);
                        setEmailError('');
                      }}
                      placeholder="Enter your email address"
                    />
                    {emailError && (
                      <span style={styles.inputError}>{emailError}</span>
                    )}
                  </div>
                  
                  <div style={styles.inputGroup}>
                    <label style={styles.label}>Full Name</label>
                    <input
                      style={styles.input}
                      type="text"
                      name="fullname"
                      value={formData?.fullname || ''}
                      onChange={handleChange}
                      placeholder="Enter your full name"
                    />
                  </div>
                  
                  <div style={styles.inputGroup}>
                    <label style={styles.label}>Age</label>
                    <input
                      style={styles.input}
                      type="number"
                      name="age"
                      value={formData?.age || ''}
                      onChange={handleChange}
                      placeholder="Enter your age"
                    />
                  </div>
                  
                  <div style={styles.inputGroup}>
                    <label style={styles.label}>Gender</label>
                    <select
                      style={styles.input}
                      name="gender"
                      value={formData?.gender || ''}
                      onChange={handleChange}
                    >
                      <option value="" disabled>Select gender</option>
                      <option value="Male">Male</option>
                      <option value="Female">Female</option>
                    </select>
                  </div>
                </div>

                {/* Academic Details Subsection */}
                <div style={{...styles.subsectionTitle, marginTop: '32px'}}>Academic Details</div>
                <div style={styles.formGrid}>
                  <div style={styles.inputGroup}>
                    <label style={styles.label}>SHS Strand</label>
                    <select
                      style={styles.input}
                      name="strand"
                      value={formData?.strand || ''}
                      onChange={handleChange}
                    >
                      <option value="" disabled>Select your strand</option>
                      <option value="STEM">STEM</option>
                      <option value="ABM">ABM</option>
                      <option value="HUMSS">HUMSS</option>
                      <option value="GAS">GAS</option>
                      <option value="TVL">TVL</option>
                    </select>
                  </div>
                  
                  <div style={styles.inputGroup}>
                    <label style={styles.label}>General Weighted Average (GWA)</label>
                    <input
                      style={{
                        ...styles.input,
                        ...(gwaError ? { borderColor: '#ef4444' } : {})
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
                    {gwaError ? (
                      <span style={styles.inputError}>{gwaError}</span>
                    ) : (
                      <span style={styles.inputHint}>Enter a value between 75 and 100</span>
                    )}
                  </div>
                </div>

                {/* Interests & Skills Subsection */}
                <div style={{...styles.subsectionTitle, marginTop: '32px'}}>Interests & Skills</div>
                
                <div style={styles.inputGroup}>
                  <label style={styles.label}>Academic Interests</label>
                  <div
                    onClick={() => setInterestModalOpen(true)}
                    style={styles.clickableField}
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
                                style={styles.tagRemoveBtn}
                              >
                                ×
                              </span>
                            </div>
                          );
                        })}
                      </div>
                    ) : (
                      <span style={styles.placeholderText}>Click to select your interests...</span>
                    )}
                  </div>
                </div>
                
                <div style={{...styles.inputGroup, marginTop: '20px'}}>
                  <label style={styles.label}>Technical & Soft Skills</label>
                  <div
                    onClick={() => setSkillsModalOpen(true)}
                    style={styles.clickableField}
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
                                style={styles.tagRemoveBtn}
                              >
                                ×
                              </span>
                            </div>
                          );
                        })}
                      </div>
                    ) : (
                      <span style={styles.placeholderText}>Click to select your skills...</span>
                    )}
                  </div>
                </div>

                <div style={styles.sectionFooter}>
                  <button onClick={handleSaveProfile} style={styles.saveBtn}>
                    Save Changes
                  </button>
                </div>
              </div>
            )}

            {/* Password & Security Section */}
            {activeSection === 'security' && (
              <div style={styles.section}>
                <h2 style={styles.sectionTitle}>Password & Security</h2>
                <p style={styles.sectionDesc}>Keep your account secure by updating your password</p>
                
                <div style={styles.passwordForm}>
                  <div style={styles.inputGroup}>
                    <label style={styles.label}>Current Password</label>
                    <div style={styles.passwordInputWrapper}>
                      <input
                        style={styles.input}
                        type={showPasswords.current ? 'text' : 'password'}
                        value={passwordData.currentPassword}
                        onChange={(e) => setPasswordData({...passwordData, currentPassword: e.target.value})}
                        placeholder="Enter current password"
                      />
                      <button
                        type="button"
                        onClick={() => setShowPasswords({...showPasswords, current: !showPasswords.current})}
                        style={styles.eyeBtn}
                      >
                        {showPasswords.current ? '👁️' : '👁️‍🗨️'}
                      </button>
                    </div>
                  </div>
                  
                  <div style={styles.inputGroup}>
                    <label style={styles.label}>New Password</label>
                    <div style={styles.passwordInputWrapper}>
                      <input
                        style={styles.input}
                        type={showPasswords.new ? 'text' : 'password'}
                        value={passwordData.newPassword}
                        onChange={(e) => setPasswordData({...passwordData, newPassword: e.target.value})}
                        placeholder="Enter new password"
                      />
                      <button
                        type="button"
                        onClick={() => setShowPasswords({...showPasswords, new: !showPasswords.new})}
                        style={styles.eyeBtn}
                      >
                        {showPasswords.new ? '👁️' : '👁️‍🗨️'}
                      </button>
                    </div>
                    <span style={styles.inputHint}>Must be at least 6 characters</span>
                  </div>
                  
                  <div style={styles.inputGroup}>
                    <label style={styles.label}>Confirm New Password</label>
                    <div style={styles.passwordInputWrapper}>
                      <input
                        style={styles.input}
                        type={showPasswords.confirm ? 'text' : 'password'}
                        value={passwordData.confirmPassword}
                        onChange={(e) => setPasswordData({...passwordData, confirmPassword: e.target.value})}
                        placeholder="Confirm new password"
                      />
                      <button
                        type="button"
                        onClick={() => setShowPasswords({...showPasswords, confirm: !showPasswords.confirm})}
                        style={styles.eyeBtn}
                      >
                        {showPasswords.confirm ? '👁️' : '👁️‍🗨️'}
                      </button>
                    </div>
                  </div>
                  
                  {passwordError && (
                    <div style={styles.errorBox}>
                      <span>⚠️</span> {passwordError}
                    </div>
                  )}
                </div>

                <div style={styles.sectionFooter}>
                  <button onClick={handlePasswordChange} style={styles.saveBtn}>
                    Update Password
                  </button>
                </div>
              </div>
            )}
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
                        } : styles.modalTag}
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

      {/* SKILLS MODAL */}
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
                        } : styles.modalTag}
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
    background: 'linear-gradient(180deg, #030308 0%, #0a0a18 50%, #050510 100%)',
    color: '#f8fafc',
    position: 'relative',
    overflow: 'hidden'
  },
  bgGradient1: {
    position: 'fixed',
    top: '-30%',
    left: '-30%',
    width: '160%',
    height: '160%',
    background: 'radial-gradient(ellipse at 30% 30%, rgba(99, 102, 241, 0.12) 0%, transparent 60%)',
    pointerEvents: 'none'
  },
  bgGradient2: {
    position: 'fixed',
    bottom: '-30%',
    right: '-30%',
    width: '160%',
    height: '160%',
    background: 'radial-gradient(ellipse at 70% 70%, rgba(139, 92, 246, 0.1) 0%, transparent 60%)',
    pointerEvents: 'none'
  },
  bgGrid: {
    position: 'fixed',
    inset: 0,
    backgroundImage: 'linear-gradient(rgba(255,255,255,0.015) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.015) 1px, transparent 1px)',
    backgroundSize: '80px 80px',
    pointerEvents: 'none'
  },
  navbar: {
    position: 'sticky',
    top: 0,
    zIndex: 100,
    background: 'rgba(5, 5, 16, 0.85)',
    backdropFilter: 'blur(24px)',
    borderBottom: '1px solid rgba(255, 255, 255, 0.04)'
  },
  navContainer: {
    maxWidth: '1400px',
    margin: '0 auto',
    padding: '14px 40px',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'space-between'
  },
  navBrand: {
    display: 'flex',
    alignItems: 'center',
    gap: '14px'
  },
  navLogo: {
    width: '48px',
    height: '48px',
    objectFit: 'cover',
    borderRadius: '12px',
    background: 'linear-gradient(135deg, rgba(99, 102, 241, 0.15) 0%, rgba(139, 92, 246, 0.15) 100%)',
    boxShadow: '0 0 20px rgba(99, 102, 241, 0.4)',
    border: '1px solid rgba(139, 92, 246, 0.3)'
  },
  navBrandName: {
    fontSize: '19px',
    fontWeight: '700',
    color: '#fff'
  },
  navLinks: {
    display: 'flex',
    alignItems: 'center',
    gap: '2px',
    background: 'rgba(255, 255, 255, 0.03)',
    padding: '5px',
    borderRadius: '14px',
    border: '1px solid rgba(255, 255, 255, 0.04)'
  },
  navLink: {
    padding: '10px 20px',
    borderRadius: '10px',
    color: '#8892a6',
    fontSize: '14px',
    fontWeight: '500',
    cursor: 'pointer',
    transition: 'all 0.25s ease'
  },
  navLinkActive: {
    background: 'rgba(255, 255, 255, 0.1)',
    color: '#fff'
  },
  navRight: {
    display: 'flex',
    alignItems: 'center'
  },
  backBtn: {
    padding: '10px 20px',
    background: 'rgba(239, 68, 68, 0.1)',
    border: '1px solid rgba(239, 68, 68, 0.2)',
    borderRadius: '10px',
    color: '#f87171',
    fontSize: '14px',
    fontWeight: '600',
    cursor: 'pointer'
  },
  mainContent: {
    position: 'relative',
    zIndex: 1,
    maxWidth: '1100px',
    margin: '0 auto',
    padding: '40px'
  },
  settingsHeader: {
    marginBottom: '32px'
  },
  pageTitle: {
    fontSize: '32px',
    fontWeight: '700',
    color: '#f8fafc',
    margin: '0 0 8px 0',
    display: 'flex',
    alignItems: 'center',
    gap: '12px'
  },
  pageTitleIcon: {
    fontSize: '32px'
  },
  pageSubtitle: {
    fontSize: '15px',
    color: '#64748b',
    margin: 0
  },
  settingsLayout: {
    display: 'grid',
    gridTemplateColumns: '260px 1fr',
    gap: '32px'
  },
  sidebar: {
    background: 'rgba(15, 23, 42, 0.6)',
    backdropFilter: 'blur(20px)',
    border: '1px solid rgba(255, 255, 255, 0.06)',
    borderRadius: '16px',
    padding: '12px',
    height: 'fit-content',
    position: 'sticky',
    top: '120px'
  },
  sidebarItem: {
    display: 'flex',
    alignItems: 'center',
    gap: '12px',
    padding: '14px 16px',
    borderRadius: '10px',
    color: '#94a3b8',
    fontSize: '14px',
    fontWeight: '500',
    cursor: 'pointer',
    transition: 'all 0.2s ease'
  },
  sidebarItemActive: {
    background: 'rgba(99, 102, 241, 0.15)',
    color: '#a5b4fc'
  },
  sidebarIcon: {
    fontSize: '18px'
  },
  contentArea: {
    minHeight: '500px'
  },
  section: {
    background: 'rgba(15, 23, 42, 0.6)',
    backdropFilter: 'blur(20px)',
    border: '1px solid rgba(255, 255, 255, 0.06)',
    borderRadius: '20px',
    padding: '32px'
  },
  sectionTitle: {
    fontSize: '20px',
    fontWeight: '700',
    color: '#f8fafc',
    margin: '0 0 8px 0'
  },
  sectionDesc: {
    fontSize: '14px',
    color: '#64748b',
    margin: '0 0 32px 0'
  },
  subsectionTitle: {
    fontSize: '15px',
    fontWeight: '600',
    color: '#94a3b8',
    marginBottom: '16px',
    paddingBottom: '8px',
    borderBottom: '1px solid rgba(255, 255, 255, 0.06)'
  },
  photoSection: {
    display: 'flex',
    alignItems: 'center',
    gap: '24px',
    padding: '24px',
    background: 'rgba(255, 255, 255, 0.02)',
    borderRadius: '16px',
    marginBottom: '32px'
  },
  photoWrapper: {
    width: '100px',
    height: '100px',
    borderRadius: '50%',
    overflow: 'hidden',
    border: '3px solid rgba(99, 102, 241, 0.3)',
    flexShrink: 0
  },
  photoImage: {
    width: '100%',
    height: '100%',
    objectFit: 'cover'
  },
  photoPlaceholder: {
    width: '100%',
    height: '100%',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    background: 'linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%)'
  },
  photoIcon: {
    fontSize: '36px',
    fontWeight: '700',
    color: 'white'
  },
  photoInfo: {
    flex: 1
  },
  photoLabel: {
    fontSize: '16px',
    fontWeight: '600',
    color: '#f8fafc',
    margin: '0 0 4px 0'
  },
  photoHint: {
    fontSize: '13px',
    color: '#64748b',
    margin: '0 0 12px 0'
  },
  photoActions: {
    display: 'flex',
    gap: '10px'
  },
  uploadBtn: {
    padding: '10px 20px',
    background: 'linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%)',
    border: 'none',
    borderRadius: '10px',
    color: 'white',
    fontSize: '13px',
    fontWeight: '600',
    cursor: 'pointer'
  },
  removeBtn: {
    padding: '10px 20px',
    background: 'rgba(239, 68, 68, 0.1)',
    border: '1px solid rgba(239, 68, 68, 0.2)',
    borderRadius: '10px',
    color: '#f87171',
    fontSize: '13px',
    fontWeight: '600',
    cursor: 'pointer'
  },
  formGrid: {
    display: 'grid',
    gridTemplateColumns: 'repeat(2, 1fr)',
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
    marginBottom: '10px'
  },
  input: {
    padding: '14px 18px',
    background: 'rgba(30, 41, 59, 0.8)',
    border: '1px solid rgba(255,255,255,0.06)',
    borderRadius: '12px',
    color: '#f1f5f9',
    fontSize: '15px',
    outline: 'none',
    width: '100%',
    boxSizing: 'border-box'
  },
  inputHint: {
    fontSize: '12px',
    color: '#64748b',
    marginTop: '6px'
  },
  inputError: {
    fontSize: '12px',
    color: '#ef4444',
    marginTop: '6px'
  },
  readOnlyField: {
    padding: '14px 18px',
    background: 'rgba(255,255,255,0.03)',
    border: '1px solid rgba(255,255,255,0.04)',
    borderRadius: '12px',
    color: 'rgba(255,255,255,0.6)',
    fontSize: '15px',
    display: 'flex',
    alignItems: 'center',
    gap: '8px'
  },
  atSymbol: {
    color: 'rgba(139, 92, 246, 0.8)'
  },
  readOnlyBadge: {
    marginLeft: 'auto',
    fontSize: '11px',
    color: 'rgba(255,255,255,0.4)',
    background: 'rgba(255,255,255,0.05)',
    padding: '3px 8px',
    borderRadius: '4px'
  },
  clickableField: {
    padding: '14px 18px',
    background: 'rgba(30, 41, 59, 0.8)',
    border: '1px solid rgba(255,255,255,0.06)',
    borderRadius: '12px',
    cursor: 'pointer',
    minHeight: '56px',
    display: 'flex',
    alignItems: 'flex-start',
    flexWrap: 'wrap',
    gap: '10px'
  },
  placeholderText: {
    color: 'rgba(255,255,255,0.4)',
    fontSize: '15px'
  },
  selectedTagsContainer: {
    display: 'flex',
    flexWrap: 'wrap',
    gap: '10px',
    width: '100%'
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
    fontWeight: '600'
  },
  tagRemoveBtn: {
    cursor: 'pointer',
    fontWeight: 'bold',
    fontSize: '16px',
    color: '#f87171'
  },
  infoBox: {
    display: 'flex',
    gap: '16px',
    padding: '20px',
    background: 'rgba(99, 102, 241, 0.08)',
    border: '1px solid rgba(99, 102, 241, 0.15)',
    borderRadius: '12px',
    marginTop: '24px'
  },
  infoIcon: {
    fontSize: '20px'
  },
  infoText: {
    fontSize: '13px',
    color: '#94a3b8',
    margin: '6px 0 0 0',
    lineHeight: 1.6
  },
  tipBox: {
    padding: '20px',
    background: 'rgba(16, 185, 129, 0.08)',
    border: '1px solid rgba(16, 185, 129, 0.15)',
    borderRadius: '12px',
    marginTop: '24px'
  },
  tipTitle: {
    fontSize: '14px',
    fontWeight: '600',
    color: '#10b981',
    margin: '0 0 12px 0'
  },
  tipList: {
    margin: 0,
    paddingLeft: '20px',
    fontSize: '13px',
    color: '#94a3b8',
    lineHeight: 1.8
  },
  passwordForm: {
    display: 'flex',
    flexDirection: 'column',
    gap: '20px',
    maxWidth: '400px'
  },
  passwordInputWrapper: {
    position: 'relative',
    display: 'flex',
    alignItems: 'center'
  },
  eyeBtn: {
    position: 'absolute',
    right: '14px',
    background: 'none',
    border: 'none',
    cursor: 'pointer',
    fontSize: '16px',
    padding: '4px'
  },
  errorBox: {
    display: 'flex',
    alignItems: 'center',
    gap: '8px',
    padding: '12px 16px',
    background: 'rgba(239, 68, 68, 0.1)',
    border: '1px solid rgba(239, 68, 68, 0.2)',
    borderRadius: '10px',
    color: '#f87171',
    fontSize: '13px'
  },
  sectionFooter: {
    marginTop: '32px',
    paddingTop: '24px',
    borderTop: '1px solid rgba(255,255,255,0.06)',
    display: 'flex',
    justifyContent: 'flex-end'
  },
  saveBtn: {
    padding: '14px 32px',
    background: 'linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%)',
    border: 'none',
    borderRadius: '12px',
    color: 'white',
    fontSize: '14px',
    fontWeight: '600',
    cursor: 'pointer',
    boxShadow: '0 4px 16px rgba(99, 102, 241, 0.25)'
  },
  // Modal styles
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
    zIndex: 1000
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
    flexDirection: 'column'
  },
  modalHeader: {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    padding: '28px 32px',
    borderBottom: '1px solid rgba(255, 255, 255, 0.06)'
  },
  modalTitle: {
    fontSize: '22px',
    fontWeight: '700',
    color: '#f8fafc',
    margin: 0
  },
  closeBtn: {
    background: 'none',
    border: 'none',
    color: '#64748b',
    fontSize: '24px',
    cursor: 'pointer'
  },
  modalBody: {
    flex: 1,
    overflowY: 'auto',
    padding: '28px 32px'
  },
  categorySection: {
    marginBottom: '32px'
  },
  categoryTitle: {
    fontSize: '12px',
    fontWeight: '700',
    color: '#a5b4fc',
    textTransform: 'uppercase',
    letterSpacing: '1px',
    margin: '0 0 16px 0'
  },
  tagsGrid: {
    display: 'grid',
    gridTemplateColumns: 'repeat(auto-fill, minmax(170px, 1fr))',
    gap: '12px'
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
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    gap: '10px',
    transition: 'all 0.2s ease'
  },
  modalTagSelected: {
    background: 'rgba(99, 102, 241, 0.15)',
    borderColor: 'rgba(99, 102, 241, 0.5)',
    color: '#a5b4fc'
  },
  checkmark: {
    color: '#10b981',
    fontSize: '16px',
    fontWeight: 'bold'
  },
  modalFooter: {
    padding: '24px 32px',
    borderTop: '1px solid rgba(255, 255, 255, 0.06)',
    display: 'flex',
    justifyContent: 'flex-end'
  },
  modalCloseBtn: {
    padding: '14px 28px',
    background: 'linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%)',
    border: 'none',
    borderRadius: '12px',
    color: 'white',
    fontSize: '14px',
    fontWeight: '600',
    cursor: 'pointer'
  }
};

export default Settings;
