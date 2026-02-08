import React, { useState, useEffect } from 'react';

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

function ProfileView({ profileData, onBack, onSettings }) {
  const [profilePhoto, setProfilePhoto] = useState(null);
  const [assessmentStats, setAssessmentStats] = useState({ total: 0, lastDate: null });
  
  // Load profile photo and stats
  useEffect(() => {
    const userId = localStorage.getItem('userId');
    if (userId) {
      const savedPhoto = localStorage.getItem(`profilePhoto_${userId}`);
      if (savedPhoto) {
        setProfilePhoto(savedPhoto);
      }
      
      // Fetch assessment history stats
      fetch(`${process.env.REACT_APP_API_URL}/user/${userId}/assessment-history`)
        .then(res => res.json())
        .then(data => {
          setAssessmentStats({
            total: data.total_attempts || 0,
            lastDate: data.history && data.history[0] ? data.history[0].date : null
          });
        })
        .catch(err => console.error('Error fetching stats:', err));
    }
  }, []);
  
  // Get label for interest/skill ID
  const getInterestLabel = (id) => {
    const found = INTEREST_OPTIONS.find(o => o.id === id);
    return found ? found.label : id;
  };
  
  const getSkillLabel = (id) => {
    const found = SKILL_OPTIONS.find(o => o.id === id);
    return found ? found.label : id;
  };
  
  // Parse interests and skills
  const interests = profileData?.interests 
    ? profileData.interests.split(',').map(i => i.trim()).filter(i => i) 
    : [];
  const skills = profileData?.skills 
    ? profileData.skills.split(',').map(s => s.trim()).filter(s => s) 
    : [];

  const userName = localStorage.getItem('userName') || 'User';
  const userEmail = localStorage.getItem('userEmail') || '';
  const userUsername = localStorage.getItem('userUsername') || '';

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
            <span style={{...styles.navLink, ...styles.navLinkActive}}>Profile</span>
          </div>

          <div style={styles.navRight}>
            <button onClick={onSettings} style={styles.settingsBtn}>
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                <circle cx="12" cy="12" r="3"/>
                <path d="M19.4 15a1.65 1.65 0 00.33 1.82l.06.06a2 2 0 010 2.83 2 2 0 01-2.83 0l-.06-.06a1.65 1.65 0 00-1.82-.33 1.65 1.65 0 00-1 1.51V21a2 2 0 01-2 2 2 2 0 01-2-2v-.09A1.65 1.65 0 009 19.4a1.65 1.65 0 00-1.82.33l-.06.06a2 2 0 01-2.83 0 2 2 0 010-2.83l.06-.06a1.65 1.65 0 00.33-1.82 1.65 1.65 0 00-1.51-1H3a2 2 0 01-2-2 2 2 0 012-2h.09A1.65 1.65 0 004.6 9a1.65 1.65 0 00-.33-1.82l-.06-.06a2 2 0 010-2.83 2 2 0 012.83 0l.06.06a1.65 1.65 0 001.82.33H9a1.65 1.65 0 001-1.51V3a2 2 0 012-2 2 2 0 012 2v.09a1.65 1.65 0 001 1.51 1.65 1.65 0 001.82-.33l.06-.06a2 2 0 012.83 0 2 2 0 010 2.83l-.06.06a1.65 1.65 0 00-.33 1.82V9a1.65 1.65 0 001.51 1H21a2 2 0 012 2 2 2 0 01-2 2h-.09a1.65 1.65 0 00-1.51 1z"/>
              </svg>
              Settings
            </button>
          </div>
        </div>
      </nav>

      {/* MAIN CONTENT */}
      <main style={styles.mainContent}>
        {/* Profile Header Card */}
        <div style={styles.profileHeader}>
          <div style={styles.coverPhoto}></div>
          <div style={styles.profileInfo}>
            <div style={styles.avatarWrapper}>
              {profilePhoto ? (
                <img src={profilePhoto} alt="Profile" style={styles.avatarImage} />
              ) : (
                <div style={styles.avatarPlaceholder}>
                  <span style={styles.avatarIcon}>{userName.charAt(0).toUpperCase()}</span>
                </div>
              )}
              <div style={styles.onlineDot}></div>
            </div>
            
            <div style={styles.profileDetails}>
              <h1 style={styles.profileName}>{profileData?.fullname || userName}</h1>
              <p style={styles.profileUsername}>@{userUsername}</p>
              <div style={styles.profileMeta}>
                {profileData?.age && (
                  <span style={styles.metaItem}>
                    <span style={styles.metaIcon}>🎂</span>
                    {profileData.age} years old
                  </span>
                )}
                {profileData?.gender && (
                  <span style={styles.metaItem}>
                    <span style={styles.metaIcon}>{profileData.gender === 'Male' ? '♂️' : '♀️'}</span>
                    {profileData.gender}
                  </span>
                )}
                {profileData?.strand && (
                  <span style={styles.metaItem}>
                    <span style={styles.metaIcon}>🎓</span>
                    {profileData.strand} Strand
                  </span>
                )}
              </div>
            </div>

            <button onClick={onSettings} style={styles.editProfileBtn}>
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                <path d="M11 4H4a2 2 0 00-2 2v14a2 2 0 002 2h14a2 2 0 002-2v-7"/>
                <path d="M18.5 2.5a2.121 2.121 0 013 3L12 15l-4 1 1-4 9.5-9.5z"/>
              </svg>
              Edit Profile
            </button>
          </div>
        </div>

        {/* Stats Cards */}
        <div style={styles.statsGrid}>
          <div style={styles.statCard}>
            <div style={styles.statIcon}>📊</div>
            <div style={styles.statValue}>{assessmentStats.total}</div>
            <div style={styles.statLabel}>Assessments Taken</div>
          </div>
          <div style={styles.statCard}>
            <div style={styles.statIcon}>📚</div>
            <div style={styles.statValue}>{profileData?.gwa || '—'}</div>
            <div style={styles.statLabel}>GWA</div>
          </div>
          <div style={styles.statCard}>
            <div style={styles.statIcon}>💡</div>
            <div style={styles.statValue}>{interests.length}</div>
            <div style={styles.statLabel}>Interests</div>
          </div>
          <div style={styles.statCard}>
            <div style={styles.statIcon}>⚡</div>
            <div style={styles.statValue}>{skills.length}</div>
            <div style={styles.statLabel}>Skills</div>
          </div>
        </div>

        {/* Profile Content Grid */}
        <div style={styles.contentGrid}>
          {/* About Section */}
          <div style={styles.contentCard}>
            <div style={styles.cardHeader}>
              <h2 style={styles.cardTitle}>
                <span style={styles.cardIcon}>👤</span>
                About
              </h2>
            </div>
            <div style={styles.aboutGrid}>
              <div style={styles.aboutItem}>
                <span style={styles.aboutLabel}>Full Name</span>
                <span style={styles.aboutValue}>{profileData?.fullname || 'Not set'}</span>
              </div>
              <div style={styles.aboutItem}>
                <span style={styles.aboutLabel}>Email</span>
                <span style={styles.aboutValue}>{userEmail || 'Not set'}</span>
              </div>
              <div style={styles.aboutItem}>
                <span style={styles.aboutLabel}>Age</span>
                <span style={styles.aboutValue}>{profileData?.age ? `${profileData.age} years old` : 'Not set'}</span>
              </div>
              <div style={styles.aboutItem}>
                <span style={styles.aboutLabel}>Gender</span>
                <span style={styles.aboutValue}>{profileData?.gender || 'Not set'}</span>
              </div>
            </div>
          </div>

          {/* Academic Info Section */}
          <div style={styles.contentCard}>
            <div style={styles.cardHeader}>
              <h2 style={styles.cardTitle}>
                <span style={styles.cardIcon}>🎓</span>
                Academic Information
              </h2>
            </div>
            <div style={styles.aboutGrid}>
              <div style={styles.aboutItem}>
                <span style={styles.aboutLabel}>SHS Strand</span>
                <span style={styles.aboutValue}>
                  {profileData?.strand ? (
                    <span style={styles.strandBadge}>{profileData.strand}</span>
                  ) : 'Not set'}
                </span>
              </div>
              <div style={styles.aboutItem}>
                <span style={styles.aboutLabel}>General Weighted Average</span>
                <span style={styles.aboutValue}>
                  {profileData?.gwa ? (
                    <span style={styles.gwaBadge}>{profileData.gwa}</span>
                  ) : 'Not set'}
                </span>
              </div>
            </div>
          </div>

          {/* Interests Section */}
          <div style={styles.contentCard}>
            <div style={styles.cardHeader}>
              <h2 style={styles.cardTitle}>
                <span style={styles.cardIcon}>💡</span>
                Academic Interests
              </h2>
            </div>
            {interests.length > 0 ? (
              <div style={styles.tagsContainer}>
                {interests.map((id, index) => (
                  <span key={index} style={styles.interestTag}>
                    {getInterestLabel(id)}
                  </span>
                ))}
              </div>
            ) : (
              <p style={styles.emptyText}>No interests added yet</p>
            )}
          </div>

          {/* Skills Section */}
          <div style={styles.contentCard}>
            <div style={styles.cardHeader}>
              <h2 style={styles.cardTitle}>
                <span style={styles.cardIcon}>⚡</span>
                Technical & Soft Skills
              </h2>
            </div>
            {skills.length > 0 ? (
              <div style={styles.tagsContainer}>
                {skills.map((id, index) => (
                  <span key={index} style={styles.skillTag}>
                    {getSkillLabel(id)}
                  </span>
                ))}
              </div>
            ) : (
              <p style={styles.emptyText}>No skills added yet</p>
            )}
          </div>
        </div>
      </main>

      {/* Footer */}
      <footer style={styles.footer}>
        <div style={styles.footerContent}>
          <span style={styles.footerLogo}>CoursePro</span>
          <span style={styles.footerText}>© 2026 CoursePro</span>
        </div>
      </footer>
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
    animation: 'breathe 20s ease-in-out infinite',
    pointerEvents: 'none'
  },
  bgGradient2: {
    position: 'fixed',
    bottom: '-30%',
    right: '-30%',
    width: '160%',
    height: '160%',
    background: 'radial-gradient(ellipse at 70% 70%, rgba(139, 92, 246, 0.1) 0%, transparent 60%)',
    animation: 'breathe 25s ease-in-out infinite reverse',
    pointerEvents: 'none'
  },
  bgGrid: {
    position: 'fixed',
    inset: 0,
    backgroundImage: 'linear-gradient(rgba(255,255,255,0.015) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.015) 1px, transparent 1px)',
    backgroundSize: '80px 80px',
    pointerEvents: 'none',
    opacity: 0.8
  },
  navbar: {
    position: 'sticky',
    top: 0,
    zIndex: 100,
    background: 'rgba(5, 5, 16, 0.85)',
    backdropFilter: 'blur(24px)',
    WebkitBackdropFilter: 'blur(24px)',
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
    boxShadow: '0 0 20px rgba(99, 102, 241, 0.4), 0 0 40px rgba(139, 92, 246, 0.2)',
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
    alignItems: 'center',
    gap: '12px'
  },
  settingsBtn: {
    display: 'flex',
    alignItems: 'center',
    gap: '8px',
    padding: '10px 20px',
    background: 'rgba(99, 102, 241, 0.1)',
    border: '1px solid rgba(99, 102, 241, 0.2)',
    borderRadius: '10px',
    color: '#a5b4fc',
    fontSize: '14px',
    fontWeight: '600',
    cursor: 'pointer',
    transition: 'all 0.2s ease'
  },
  mainContent: {
    position: 'relative',
    zIndex: 1,
    maxWidth: '1000px',
    margin: '0 auto',
    padding: '40px 40px'
  },
  profileHeader: {
    background: 'rgba(15, 23, 42, 0.6)',
    backdropFilter: 'blur(20px)',
    border: '1px solid rgba(255, 255, 255, 0.06)',
    borderRadius: '24px',
    overflow: 'hidden',
    marginBottom: '30px'
  },
  coverPhoto: {
    height: '140px',
    background: 'linear-gradient(135deg, #6366f1 0%, #8b5cf6 50%, #a855f7 100%)',
    position: 'relative'
  },
  profileInfo: {
    display: 'flex',
    alignItems: 'flex-end',
    gap: '24px',
    padding: '0 32px 32px',
    marginTop: '-50px',
    position: 'relative'
  },
  avatarWrapper: {
    position: 'relative',
    flexShrink: 0
  },
  avatarImage: {
    width: '120px',
    height: '120px',
    borderRadius: '50%',
    border: '4px solid #0a0a18',
    objectFit: 'cover',
    boxShadow: '0 8px 32px rgba(0, 0, 0, 0.3)'
  },
  avatarPlaceholder: {
    width: '120px',
    height: '120px',
    borderRadius: '50%',
    border: '4px solid #0a0a18',
    background: 'linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%)',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    boxShadow: '0 8px 32px rgba(0, 0, 0, 0.3)'
  },
  avatarIcon: {
    fontSize: '48px',
    fontWeight: '700',
    color: 'white'
  },
  onlineDot: {
    position: 'absolute',
    bottom: '8px',
    right: '8px',
    width: '20px',
    height: '20px',
    borderRadius: '50%',
    background: '#10b981',
    border: '3px solid #0a0a18',
    boxShadow: '0 0 12px rgba(16, 185, 129, 0.5)'
  },
  profileDetails: {
    flex: 1,
    paddingTop: '60px'
  },
  profileName: {
    fontSize: '28px',
    fontWeight: '700',
    color: '#f8fafc',
    margin: '0 0 4px 0'
  },
  profileUsername: {
    fontSize: '15px',
    color: '#64748b',
    margin: '0 0 12px 0'
  },
  profileMeta: {
    display: 'flex',
    flexWrap: 'wrap',
    gap: '16px'
  },
  metaItem: {
    display: 'flex',
    alignItems: 'center',
    gap: '6px',
    fontSize: '14px',
    color: '#94a3b8'
  },
  metaIcon: {
    fontSize: '14px'
  },
  editProfileBtn: {
    display: 'flex',
    alignItems: 'center',
    gap: '8px',
    padding: '12px 24px',
    background: 'rgba(99, 102, 241, 0.1)',
    border: '1px solid rgba(99, 102, 241, 0.3)',
    borderRadius: '12px',
    color: '#a5b4fc',
    fontSize: '14px',
    fontWeight: '600',
    cursor: 'pointer',
    transition: 'all 0.2s ease',
    marginTop: '60px'
  },
  statsGrid: {
    display: 'grid',
    gridTemplateColumns: 'repeat(4, 1fr)',
    gap: '16px',
    marginBottom: '30px'
  },
  statCard: {
    background: 'rgba(15, 23, 42, 0.6)',
    backdropFilter: 'blur(20px)',
    border: '1px solid rgba(255, 255, 255, 0.06)',
    borderRadius: '16px',
    padding: '24px',
    textAlign: 'center'
  },
  statIcon: {
    fontSize: '28px',
    marginBottom: '12px'
  },
  statValue: {
    fontSize: '28px',
    fontWeight: '700',
    color: '#f8fafc',
    marginBottom: '4px'
  },
  statLabel: {
    fontSize: '13px',
    color: '#64748b'
  },
  contentGrid: {
    display: 'grid',
    gridTemplateColumns: 'repeat(2, 1fr)',
    gap: '24px'
  },
  contentCard: {
    background: 'rgba(15, 23, 42, 0.6)',
    backdropFilter: 'blur(20px)',
    border: '1px solid rgba(255, 255, 255, 0.06)',
    borderRadius: '20px',
    padding: '28px'
  },
  cardHeader: {
    marginBottom: '20px',
    paddingBottom: '16px',
    borderBottom: '1px solid rgba(255, 255, 255, 0.06)'
  },
  cardTitle: {
    fontSize: '16px',
    fontWeight: '700',
    color: '#f8fafc',
    margin: 0,
    display: 'flex',
    alignItems: 'center',
    gap: '10px'
  },
  cardIcon: {
    fontSize: '18px'
  },
  aboutGrid: {
    display: 'flex',
    flexDirection: 'column',
    gap: '16px'
  },
  aboutItem: {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center'
  },
  aboutLabel: {
    fontSize: '14px',
    color: '#64748b'
  },
  aboutValue: {
    fontSize: '14px',
    color: '#e2e8f0',
    fontWeight: '500'
  },
  strandBadge: {
    padding: '6px 14px',
    background: 'linear-gradient(135deg, rgba(99, 102, 241, 0.2), rgba(139, 92, 246, 0.15))',
    border: '1px solid rgba(99, 102, 241, 0.3)',
    borderRadius: '8px',
    color: '#a5b4fc',
    fontWeight: '600'
  },
  gwaBadge: {
    padding: '6px 14px',
    background: 'rgba(16, 185, 129, 0.15)',
    border: '1px solid rgba(16, 185, 129, 0.3)',
    borderRadius: '8px',
    color: '#10b981',
    fontWeight: '600'
  },
  tagsContainer: {
    display: 'flex',
    flexWrap: 'wrap',
    gap: '10px'
  },
  interestTag: {
    padding: '8px 16px',
    background: 'rgba(99, 102, 241, 0.12)',
    border: '1px solid rgba(99, 102, 241, 0.25)',
    borderRadius: '10px',
    color: '#a5b4fc',
    fontSize: '13px',
    fontWeight: '500'
  },
  skillTag: {
    padding: '8px 16px',
    background: 'rgba(139, 92, 246, 0.12)',
    border: '1px solid rgba(139, 92, 246, 0.25)',
    borderRadius: '10px',
    color: '#c4b5fd',
    fontSize: '13px',
    fontWeight: '500'
  },
  emptyText: {
    color: '#64748b',
    fontSize: '14px',
    fontStyle: 'italic',
    margin: 0
  },
  footer: {
    borderTop: '1px solid rgba(255, 255, 255, 0.04)',
    padding: '24px 40px',
    marginTop: 'auto'
  },
  footerContent: {
    maxWidth: '1200px',
    margin: '0 auto',
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center'
  },
  footerLogo: {
    fontSize: '16px',
    fontWeight: '700',
    color: '#475569'
  },
  footerText: {
    fontSize: '13px',
    color: '#475569'
  }
};

export default ProfileView;
