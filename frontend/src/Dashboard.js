import React, { useState, useEffect, useCallback } from 'react';

// Add CSS keyframes for smooth animations
const keyframes = `
  @keyframes gradientShift {
    0%, 100% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
  }
  @keyframes float {
    0%, 100% { transform: translateY(0px) rotate(0deg); }
    33% { transform: translateY(-8px) rotate(1deg); }
    66% { transform: translateY(-4px) rotate(-1deg); }
  }
  @keyframes pulse {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.7; transform: scale(0.98); }
  }
  @keyframes glow {
    0%, 100% { box-shadow: 0 0 20px rgba(99, 102, 241, 0.2), 0 0 60px rgba(99, 102, 241, 0.1); }
    50% { box-shadow: 0 0 30px rgba(139, 92, 246, 0.3), 0 0 80px rgba(139, 92, 246, 0.15); }
  }
  @keyframes slideUp {
    from { opacity: 0; transform: translateY(30px) scale(0.98); }
    to { opacity: 1; transform: translateY(0) scale(1); }
  }
  @keyframes slideIn {
    from { opacity: 0; transform: translateX(-20px); }
    to { opacity: 1; transform: translateX(0); }
  }
  @keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
  }
  @keyframes shimmer {
    0% { background-position: -200% 0; }
    100% { background-position: 200% 0; }
  }
  @keyframes breathe {
    0%, 100% { transform: scale(1); opacity: 0.5; }
    50% { transform: scale(1.05); opacity: 0.8; }
  }
  @keyframes dotPulse {
    0%, 100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(34, 197, 94, 0.4); }
    50% { transform: scale(1.1); box-shadow: 0 0 0 8px rgba(34, 197, 94, 0); }
  }
`;

function Dashboard({ userName, onLogout, onStart, onStartAdaptive, onViewProfile, onViewActivity, onViewSettings, history }) {
  const [hasAcademicInfo, setHasAcademicInfo] = useState(false);
  const [checkingProfile, setCheckingProfile] = useState(true);
  const [selectedQuestionCount, setSelectedQuestionCount] = useState(30);
  const [showHelpCenter, setShowHelpCenter] = useState(false);
  const [activityCount, setActivityCount] = useState(0);
  const [unseenActivityCount, setUnseenActivityCount] = useState(0);
  const [profilePhoto, setProfilePhoto] = useState(null);
  const [showUserMenu, setShowUserMenu] = useState(false);

  // Load profile photo from localStorage (user-specific)
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

  // Check if user has filled academic info and fetch activity count
  useEffect(() => {
    const userId = localStorage.getItem('userId');
    if (userId) {
      fetch(`${process.env.REACT_APP_API_URL}/user/${userId}/academic-info`)
        .then(res => res.json())
        .then(data => {
          setHasAcademicInfo(data.has_academic_info || false);
          setCheckingProfile(false);
        })
        .catch(err => {
          console.error('Error checking academic info:', err);
          setCheckingProfile(false);
        });
      
      // Fetch actual activity count from API and calculate unseen
      fetch(`${process.env.REACT_APP_API_URL}/user/${userId}/assessment-history`)
        .then(res => res.json())
        .then(data => {
          const totalAttempts = data.total_attempts || 0;
          setActivityCount(totalAttempts);
          
          // Calculate unseen activities
          const seenActivities = JSON.parse(localStorage.getItem(`seenActivities_${userId}`) || '[]');
          const allAttemptIds = (data.history || []).map(h => h.attempt_id);
          const unseenCount = allAttemptIds.filter(id => !seenActivities.includes(id)).length;
          setUnseenActivityCount(unseenCount);
        })
        .catch(err => {
          console.error('Error fetching activity count:', err);
        });
    } else {
      setCheckingProfile(false);
    }
  }, []);

  // Periodically update activity to keep user marked as online
  useEffect(() => {
    const userId = localStorage.getItem('userId');
    if (!userId) return;

    // Update activity immediately on mount
    const updateActivity = async () => {
      try {
        await fetch(`${process.env.REACT_APP_API_URL}/user/${userId}/update-activity`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' }
        });
      } catch (err) {
        console.error('Error updating activity:', err);
      }
    };

    updateActivity();

    // Update activity every 5 minutes (300000ms)
    const activityInterval = setInterval(updateActivity, 5 * 60 * 1000);

    // Cleanup interval on unmount
    return () => clearInterval(activityInterval);
  }, []);

  // Handle logout with activity tracking - memoized to prevent re-renders
  const handleLogout = useCallback(async () => {
    const userId = localStorage.getItem('userId');
    
    // Call logout endpoint to mark user as offline
    if (userId) {
      try {
        await fetch(`${process.env.REACT_APP_API_URL}/logout`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ user_id: userId })
        });
      } catch (err) {
        console.error('Error during logout:', err);
      }
    }
    
    // Call the original logout handler
    onLogout();
  }, [onLogout]);

  // Memoized handler for starting adaptive assessment
  const handleStartAdaptive = useCallback(() => {
    if (!hasAcademicInfo) {
      alert('⚠️ Please complete your Academic Profile first!\n\nYou need to fill in your GWA and SHS Strand before taking the assessment.');
      onViewProfile();
      return;
    }
    // Pass the selected question count to the assessment
    onStartAdaptive(selectedQuestionCount);
  }, [hasAcademicInfo, onViewProfile, onStartAdaptive, selectedQuestionCount]);

  // Inject keyframes into document
  useEffect(() => {
    const styleSheet = document.createElement('style');
    styleSheet.textContent = keyframes;
    document.head.appendChild(styleSheet);
    return () => document.head.removeChild(styleSheet);
  }, []);

  return (
    <div style={styles.pageWrapper}>
      {/* Animated background elements */}
      <div style={styles.bgGradient1}></div>
      <div style={styles.bgGradient2}></div>
      <div style={styles.bgGrid}></div>

      {/* TOP NAVIGATION */}
      <nav style={styles.navbar}>
        <div style={styles.navContainer}>
          <div style={styles.navBrand}>
            <img src="/logo.png" alt="CoursePro" style={styles.navLogo} />
            <span style={styles.navBrandName}>CoursePro</span>
          </div>

          <div style={styles.navLinks}>
            <span style={{...styles.navLink, ...styles.navLinkActive}}>Home</span>
            <span style={styles.navLink} onClick={onViewProfile}>Profile</span>
            <span style={styles.navLink} onClick={onViewActivity}>
              Activity
              {unseenActivityCount > 0 && <span style={styles.navBadge}>{unseenActivityCount}</span>}
            </span>
          </div>

          <div style={styles.navRight}>
            <div style={styles.userPillWrapper}>
              <div 
                style={styles.userPill} 
                onClick={() => setShowUserMenu(!showUserMenu)}
              >
                {profilePhoto ? (
                  <img src={profilePhoto} alt="Profile" style={styles.userAvatarImg} />
                ) : (
                  <div style={styles.userAvatar}>{userName?.charAt(0)?.toUpperCase() || 'U'}</div>
                )}
                <span style={styles.userName}>{userName}</span>
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" style={{marginLeft: '4px', opacity: 0.6}}>
                  <path d="M6 9l6 6 6-6"/>
                </svg>
              </div>
              
              {/* User Dropdown Menu */}
              {showUserMenu && (
                <>
                  <div style={styles.menuBackdrop} onClick={() => setShowUserMenu(false)}></div>
                  <div style={styles.userMenu}>
                    <div style={styles.userMenuHeader}>
                      <div style={styles.userMenuAvatar}>
                        {profilePhoto ? (
                          <img src={profilePhoto} alt="Profile" style={styles.userMenuAvatarImg} />
                        ) : (
                          <span>{userName?.charAt(0)?.toUpperCase() || 'U'}</span>
                        )}
                      </div>
                      <div style={styles.userMenuInfo}>
                        <span style={styles.userMenuName}>{userName}</span>
                        <span style={styles.userMenuEmail}>{localStorage.getItem('userEmail') || ''}</span>
                      </div>
                    </div>
                    <div style={styles.userMenuDivider}></div>
                    <div 
                      style={styles.userMenuItem} 
                      onClick={() => { setShowUserMenu(false); onViewProfile(); }}
                    >
                      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                        <path d="M20 21v-2a4 4 0 00-4-4H8a4 4 0 00-4 4v2"/>
                        <circle cx="12" cy="7" r="4"/>
                      </svg>
                      <span>View Profile</span>
                    </div>
                    <div 
                      style={styles.userMenuItem} 
                      onClick={() => { setShowUserMenu(false); onViewSettings && onViewSettings(); }}
                    >
                      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                        <circle cx="12" cy="12" r="3"/>
                        <path d="M19.4 15a1.65 1.65 0 00.33 1.82l.06.06a2 2 0 010 2.83 2 2 0 01-2.83 0l-.06-.06a1.65 1.65 0 00-1.82-.33 1.65 1.65 0 00-1 1.51V21a2 2 0 01-2 2 2 2 0 01-2-2v-.09A1.65 1.65 0 009 19.4a1.65 1.65 0 00-1.82.33l-.06.06a2 2 0 01-2.83 0 2 2 0 010-2.83l.06-.06a1.65 1.65 0 00.33-1.82 1.65 1.65 0 00-1.51-1H3a2 2 0 01-2-2 2 2 0 012-2h.09A1.65 1.65 0 004.6 9a1.65 1.65 0 00-.33-1.82l-.06-.06a2 2 0 010-2.83 2 2 0 012.83 0l.06.06a1.65 1.65 0 001.82.33H9a1.65 1.65 0 001-1.51V3a2 2 0 012-2 2 2 0 012 2v.09a1.65 1.65 0 001 1.51 1.65 1.65 0 001.82-.33l.06-.06a2 2 0 012.83 0 2 2 0 010 2.83l-.06.06a1.65 1.65 0 00-.33 1.82V9a1.65 1.65 0 001.51 1H21a2 2 0 012 2 2 2 0 01-2 2h-.09a1.65 1.65 0 00-1.51 1z"/>
                      </svg>
                      <span>Settings</span>
                    </div>
                    <div 
                      style={styles.userMenuItem} 
                      onClick={() => { setShowUserMenu(false); setShowHelpCenter(true); }}
                    >
                      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                        <circle cx="12" cy="12" r="10"/>
                        <path d="M9.09 9a3 3 0 015.83 1c0 2-3 3-3 3"/>
                        <line x1="12" y1="17" x2="12.01" y2="17"/>
                      </svg>
                      <span>Help Center</span>
                    </div>
                    <div style={styles.userMenuDivider}></div>
                    <div 
                      style={{...styles.userMenuItem, ...styles.userMenuItemDanger}} 
                      onClick={() => { setShowUserMenu(false); handleLogout(); }}
                    >
                      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                        <path d="M9 21H5a2 2 0 01-2-2V5a2 2 0 012-2h4M16 17l5-5-5-5M21 12H9"/>
                      </svg>
                      <span>Log Out</span>
                    </div>
                  </div>
                </>
              )}
            </div>
          </div>
        </div>
      </nav>

      {/* HERO SECTION */}
      <main style={styles.mainContent}>
        <section style={styles.heroSection}>
          <div style={styles.heroContent}>
            <h1 style={styles.heroTitle}>
              <span style={styles.heroLine1}>Welcome back,</span>
              <span className="gradient-text" style={styles.heroLine2}>{userName}</span>
            </h1>

            {!checkingProfile && !hasAcademicInfo && (
              <div style={styles.warningCard}>
                <div style={styles.warningIcon}>⚠️</div>
                <div style={styles.warningText}>
                  <strong>Complete your profile</strong>
                  <span>Add your GWA & Strand for accurate recommendations</span>
                </div>
                <button style={styles.warningBtn} onClick={onViewProfile}>Setup Profile</button>
              </div>
            )}
          </div>
        </section>

        {/* BENTO GRID SECTION */}
        <section style={styles.bentoGrid}>
          {/* Assessment Card - Large - MAIN CTA */}
          <div style={styles.bentoCardLarge}>
            <div style={styles.cardGlow}></div>
            <div style={styles.cardContent}>
              <div style={styles.cardHeader}>
                <span style={styles.cardIcon}>🎯</span>
                <span style={styles.cardTagHighlight}>TAKE ASSESSMENT</span>
              </div>
              <h2 style={styles.cardTitleLarge}>Find Your Perfect Course</h2>
              <p style={styles.cardDescLarge}>Answer questions and get personalized course recommendations based on your interests and skills.</p>
              
              <div style={styles.quizLengthLabel}>Select Quiz Length:</div>
              <div style={styles.assessmentOptions}>
                {[
                  { count: 30, label: 'Quick', icon: '⚡', color: '#22c55e' },
                  { count: 50, label: 'Standard', icon: '📊', color: '#6366f1' },
                  { count: 60, label: 'Comprehensive', icon: '🎯', color: '#f59e0b' }
                ].map((option) => (
                  <div
                    key={option.count}
                    style={selectedQuestionCount === option.count ? {
                      ...styles.assessmentOption,
                      ...styles.assessmentOptionActive,
                      borderColor: option.color,
                      boxShadow: `0 0 30px ${option.color}30`
                    } : {
                      ...styles.assessmentOption,
                      borderColor: 'rgba(255, 255, 255, 0.08)',
                      boxShadow: 'none'
                    }}
                    onClick={() => setSelectedQuestionCount(option.count)}
                  >
                    <span style={styles.optionEmoji}>{option.icon}</span>
                    <div style={styles.optionInfo}>
                      <strong style={styles.optionName}>{option.label}</strong>
                    </div>
                    {selectedQuestionCount === option.count && (
                      <div style={{...styles.checkMark, background: option.color}}>✓</div>
                    )}
                  </div>
                ))}
              </div>

              <button 
                style={{
                  ...styles.startBtn,
                  ...((!hasAcademicInfo && !checkingProfile) ? styles.startBtnDisabled : {})
                }}
                onClick={handleStartAdaptive}
              >
                <span style={styles.btnText}>{checkingProfile ? 'Loading...' : 'Start Assessment'}</span>
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5">
                  <path d="M5 12h14M12 5l7 7-7 7"/>
                </svg>
              </button>
              
              {(!hasAcademicInfo && !checkingProfile) && (
                <p style={styles.profileWarning}>
                  ⚠️ Please <span style={styles.profileLink} onClick={onViewProfile}>complete your profile</span> first
                </p>
              )}
            </div>
          </div>

          {/* Profile Card */}
          <div 
            style={styles.bentoCardSmall}
            onClick={onViewProfile}
          >
            <div style={styles.smallCardIcon}>👤</div>
            <h3 style={styles.smallCardTitle}>Academic Profile</h3>
            <p style={styles.smallCardDesc}>Update your GWA & strand</p>
            <div style={styles.cardArrow}>→</div>
          </div>

          {/* Activity Card */}
          <div 
            style={styles.bentoCardSmall}
            onClick={onViewActivity}
          >
            <div style={styles.smallCardIcon}>📊</div>
            <h3 style={styles.smallCardTitle}>My Activity</h3>
            <p style={styles.smallCardDesc}>View assessment history</p>
            {activityCount > 0 && <span style={styles.activityBadge}>{activityCount} tests taken</span>}
            <div style={styles.cardArrow}>→</div>
          </div>

          {/* Recent Activity Card */}
          {history && history.length > 0 && (
          <div style={styles.bentoCardActivity}>
            <div style={styles.activityHeader}>
              <h3 style={styles.activityTitle}>Recent Activity</h3>
              {history.length > 3 && (
                <button style={styles.viewAllBtn} onClick={() => onViewActivity()}>View All</button>
              )}
            </div>
            
            <div style={styles.activityList}>
              {history.slice(0, 3).map((item, index) => (
                <div key={index} style={styles.activityItem}>
                  <div style={{
                    ...styles.activityDot,
                    background: item.type === 'assessment' ? '#6366f1' : '#f43f5e'
                  }}></div>
                  <div style={styles.activityInfo}>
                    <span style={styles.activityItemName}>
                      {item.type === 'assessment' && Array.isArray(item.courses) && item.courses.length > 0
                        ? (typeof item.courses[0] === 'object' ? item.courses[0].course : item.courses[0])
                        : item.courses}
                    </span>
                    <span style={styles.activityItemDate}>{item.date}</span>
                  </div>
                  <span style={{
                    ...styles.activityItemBadge,
                    background: item.type === 'assessment' ? 'rgba(99, 102, 241, 0.15)' : 'rgba(244, 63, 94, 0.15)',
                    color: item.type === 'assessment' ? '#818cf8' : '#fb7185'
                  }}>
                    {item.type === 'profile_update' ? 'Profile' : 'Test'}
                  </span>
                </div>
              ))}
            </div>
          </div>
          )}
        </section>
      </main>

      {/* Footer */}
      <footer style={styles.footer}>
        <div style={styles.footerContent}>
          <span style={styles.footerLogo}>CoursePro</span>
          <span style={styles.footerText}>© 2026 CoursePro</span>
        </div>
      </footer>

      {/* HELP CENTER MODAL */}
      {showHelpCenter && (
        <div style={styles.modalOverlay} onClick={() => setShowHelpCenter(false)}>
          <div style={styles.modalContent} onClick={(e) => e.stopPropagation()}>
            <div style={styles.modalHeader}>
              <h2 style={styles.modalTitle}>Help Center</h2>
              <button style={styles.closeBtn} onClick={() => setShowHelpCenter(false)}>✕</button>
            </div>
            
            <div style={styles.modalBody}>
              <div style={styles.helpSection}>
                <h3 style={styles.helpSectionTitle}>🚀 Getting Started</h3>
                <div style={styles.helpItem}>
                  <strong>1. Complete Your Profile</strong>
                  <p>Fill in your Academic Profile with your GWA and SHS Strand.</p>
                </div>
                <div style={styles.helpItem}>
                  <strong>2. Take the Assessment</strong>
                  <p>Answer questions honestly. Choose what best describes you.</p>
                </div>
                <div style={styles.helpItem}>
                  <strong>3. View Recommendations</strong>
                  <p>Get personalized course recommendations instantly.</p>
                </div>
              </div>

              <div style={styles.helpSection}>
                <h3 style={styles.helpSectionTitle}>📋 Assessment Types</h3>
                <div style={styles.helpItem}>
                  <strong>Quick (30 questions) ~10 min</strong>
                  <p>Fast overview of your interests and skills.</p>
                </div>
                <div style={styles.helpItem}>
                  <strong>Standard (50 questions) ~15 min</strong>
                  <p>Balanced assessment for better accuracy.</p>
                </div>
                <div style={styles.helpItem}>
                  <strong>Deep (60 questions) ~20 min</strong>
                  <p>Most thorough analysis for best results.</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

const styles = {
  // Page wrapper with animated background
  pageWrapper: {
    minHeight: '100vh',
    background: 'linear-gradient(180deg, #030308 0%, #0a0a18 50%, #050510 100%)',
    color: '#f8fafc',
    position: 'relative',
    overflow: 'hidden'
  },

  // Animated background gradients - smoother
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

  // Navigation - smoother
  navbar: {
    position: 'sticky',
    top: 0,
    zIndex: 100,
    background: 'rgba(5, 5, 16, 0.85)',
    backdropFilter: 'blur(24px)',
    WebkitBackdropFilter: 'blur(24px)',
    borderBottom: '1px solid rgba(255, 255, 255, 0.04)',
    transition: 'all 0.3s cubic-bezier(0.4, 0, 0.2, 1)'
  },
  navContainer: {
    maxWidth: '1400px',
    margin: '0 auto',
    padding: '14px 40px',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'space-between',
    position: 'relative'
  },
  navBrand: {
    display: 'flex',
    alignItems: 'center',
    gap: '14px',
    zIndex: 1
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
    transition: 'transform 0.3s cubic-bezier(0.4, 0, 0.2, 1)',
  },
  navBrandName: {
    fontSize: '19px',
    fontWeight: '700',
    color: '#fff',
    letterSpacing: '-0.3px'
  },
  navLinks: {
    position: 'absolute',
    left: '50%',
    transform: 'translateX(-50%)',
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
    transition: 'all 0.25s cubic-bezier(0.4, 0, 0.2, 1)',
    display: 'flex',
    alignItems: 'center',
    gap: '8px',
    position: 'relative'
  },
  navLinkActive: {
    background: 'rgba(255, 255, 255, 0.1)',
    color: '#fff'
  },
  navBadge: {
    background: 'linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%)',
    color: 'white',
    fontSize: '10px',
    fontWeight: '700',
    padding: '3px 7px',
    borderRadius: '6px',
    minWidth: '18px',
    textAlign: 'center',
    boxShadow: '0 2px 8px rgba(99, 102, 241, 0.4)'
  },
  navRight: {
    display: 'flex',
    alignItems: 'center',
    zIndex: 1
  },
  userPill: {
    display: 'flex',
    alignItems: 'center',
    gap: '10px',
    padding: '6px 14px 6px 6px',
    background: 'rgba(255, 255, 255, 0.04)',
    borderRadius: '14px',
    border: '1px solid rgba(255, 255, 255, 0.06)',
    transition: 'all 0.25s cubic-bezier(0.4, 0, 0.2, 1)',
    cursor: 'pointer'
  },
  userAvatar: {
    width: '34px',
    height: '34px',
    borderRadius: '10px',
    background: 'linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%)',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    fontSize: '14px',
    fontWeight: '700',
    color: 'white',
    boxShadow: '0 2px 10px rgba(99, 102, 241, 0.3)'
  },
  userAvatarImg: {
    width: '34px',
    height: '34px',
    borderRadius: '10px',
    objectFit: 'cover',
    border: '2px solid rgba(99, 102, 241, 0.3)',
  },
  userName: {
    fontSize: '14px',
    fontWeight: '500',
    color: '#e2e8f0',
    paddingRight: '6px'
  },
  logoutBtn: {
    width: '34px',
    height: '34px',
    borderRadius: '10px',
    background: 'rgba(244, 63, 94, 0.1)',
    border: '1px solid rgba(244, 63, 94, 0.2)',
    color: '#f87171',
    cursor: 'pointer',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    transition: 'all 0.2s ease'
  },
  
  // User dropdown menu
  userPillWrapper: {
    position: 'relative'
  },
  menuBackdrop: {
    position: 'fixed',
    top: 0,
    left: 0,
    right: 0,
    bottom: 0,
    zIndex: 99
  },
  userMenu: {
    position: 'absolute',
    top: 'calc(100% + 10px)',
    right: 0,
    width: '280px',
    background: 'rgba(15, 23, 42, 0.98)',
    backdropFilter: 'blur(20px)',
    border: '1px solid rgba(255, 255, 255, 0.08)',
    borderRadius: '16px',
    boxShadow: '0 20px 60px rgba(0, 0, 0, 0.5)',
    overflow: 'hidden',
    zIndex: 100,
    animation: 'slideUp 0.2s ease-out'
  },
  userMenuHeader: {
    display: 'flex',
    alignItems: 'center',
    gap: '14px',
    padding: '20px',
    background: 'rgba(99, 102, 241, 0.05)'
  },
  userMenuAvatar: {
    width: '48px',
    height: '48px',
    borderRadius: '12px',
    background: 'linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%)',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    fontSize: '20px',
    fontWeight: '700',
    color: 'white',
    flexShrink: 0
  },
  userMenuAvatarImg: {
    width: '48px',
    height: '48px',
    borderRadius: '12px',
    objectFit: 'cover'
  },
  userMenuInfo: {
    display: 'flex',
    flexDirection: 'column',
    gap: '2px',
    overflow: 'hidden'
  },
  userMenuName: {
    fontSize: '15px',
    fontWeight: '600',
    color: '#f8fafc',
    whiteSpace: 'nowrap',
    overflow: 'hidden',
    textOverflow: 'ellipsis'
  },
  userMenuEmail: {
    fontSize: '13px',
    color: '#64748b',
    whiteSpace: 'nowrap',
    overflow: 'hidden',
    textOverflow: 'ellipsis'
  },
  userMenuDivider: {
    height: '1px',
    background: 'rgba(255, 255, 255, 0.06)',
    margin: '0'
  },
  userMenuItem: {
    display: 'flex',
    alignItems: 'center',
    gap: '14px',
    padding: '14px 20px',
    fontSize: '14px',
    fontWeight: '500',
    color: '#94a3b8',
    cursor: 'pointer',
    transition: 'all 0.2s ease'
  },
  userMenuItemDanger: {
    color: '#f87171'
  },

  // Main Content
  mainContent: {
    position: 'relative',
    zIndex: 1,
    maxWidth: '1200px',
    margin: '0 auto',
    padding: '0 40px 40px'
  },

  // Hero Section
  heroSection: {
    padding: '40px 0 32px',
    textAlign: 'center',
    animation: 'fadeIn 0.6s ease-out'
  },
  heroContent: {
    maxWidth: '600px',
    margin: '0 auto'
  },
  announcementBanner: {
    display: 'inline-flex',
    alignItems: 'center',
    gap: '12px',
    padding: '10px 18px 10px 14px',
    background: 'linear-gradient(90deg, rgba(99, 102, 241, 0.08) 0%, rgba(139, 92, 246, 0.08) 100%)',
    border: '1px solid rgba(99, 102, 241, 0.15)',
    borderRadius: '100px',
    fontSize: '14px',
    color: '#c4b5fd',
    marginBottom: '32px',
    cursor: 'pointer',
    transition: 'all 0.3s cubic-bezier(0.4, 0, 0.2, 1)',
    backdropFilter: 'blur(10px)'
  },
  announcementDot: {
    width: '8px',
    height: '8px',
    borderRadius: '50%',
    background: '#22c55e',
    animation: 'dotPulse 2s ease-in-out infinite'
  },
  heroTitle: {
    fontSize: '42px',
    fontWeight: '700',
    lineHeight: '1.15',
    marginBottom: '0',
    letterSpacing: '-1px'
  },
  heroLine1: {
    display: 'block',
    color: '#94a3b8',
    fontSize: '18px',
    fontWeight: '500',
    marginBottom: '8px'
  },
  heroLine2: {
    display: 'block'
  },
  heroSubtitle: {
    fontSize: '18px',
    color: '#64748b',
    lineHeight: '1.75',
    marginBottom: '36px',
    fontWeight: '400'
  },

  // Warning Card
  warningCard: {
    display: 'inline-flex',
    alignItems: 'center',
    gap: '18px',
    padding: '18px 24px',
    background: 'rgba(245, 158, 11, 0.06)',
    border: '1px solid rgba(245, 158, 11, 0.15)',
    borderRadius: '18px',
    marginBottom: '28px',
    backdropFilter: 'blur(10px)',
    transition: 'all 0.3s cubic-bezier(0.4, 0, 0.2, 1)'
  },
  warningIcon: {
    fontSize: '26px'
  },
  warningText: {
    textAlign: 'left',
    display: 'flex',
    flexDirection: 'column',
    gap: '4px'
  },
  warningBtn: {
    padding: '12px 24px',
    background: 'linear-gradient(135deg, #f59e0b 0%, #d97706 100%)',
    border: 'none',
    borderRadius: '12px',
    color: 'white',
    fontSize: '14px',
    fontWeight: '600',
    cursor: 'pointer',
    boxShadow: '0 6px 20px rgba(245, 158, 11, 0.25)',
    transition: 'all 0.3s cubic-bezier(0.4, 0, 0.2, 1)'
  },

  // Bento Grid
  bentoGrid: {
    display: 'grid',
    gridTemplateColumns: '1fr 1fr',
    gap: '20px',
    maxWidth: '800px',
    margin: '0 auto',
    animation: 'slideIn 0.7s cubic-bezier(0.4, 0, 0.2, 1)'
  },

  // Large Assessment Card - MAIN CTA
  bentoCardLarge: {
    gridColumn: 'span 2',
    position: 'relative',
    padding: '28px 32px',
    background: 'linear-gradient(145deg, rgba(15, 23, 42, 0.8) 0%, rgba(30, 27, 75, 0.6) 100%)',
    border: '1px solid rgba(99, 102, 241, 0.2)',
    borderRadius: '24px',
    overflow: 'hidden',
    backdropFilter: 'blur(20px)',
    transition: 'all 0.4s cubic-bezier(0.4, 0, 0.2, 1)',
  },
  cardGlow: {
    position: 'absolute',
    top: '-150px',
    right: '-150px',
    width: '400px',
    height: '400px',
    background: 'radial-gradient(circle, rgba(99, 102, 241, 0.2) 0%, transparent 70%)',
    pointerEvents: 'none',
    animation: 'breathe 6s ease-in-out infinite'
  },
  cardPulse: {
    position: 'absolute',
    top: '20px',
    left: '20px',
    width: '12px',
    height: '12px',
    borderRadius: '50%',
    background: '#22c55e',
    boxShadow: '0 0 20px #22c55e',
    animation: 'dotPulse 2s ease-in-out infinite'
  },
  cardContent: {
    position: 'relative',
    zIndex: 1
  },
  cardHeader: {
    display: 'flex',
    alignItems: 'center',
    gap: '12px',
    marginBottom: '12px'
  },
  cardIcon: {
    fontSize: '28px'
  },
  cardTag: {
    padding: '5px 10px',
    background: 'rgba(99, 102, 241, 0.15)',
    borderRadius: '8px',
    fontSize: '10px',
    fontWeight: '700',
    color: '#a5b4fc',
    letterSpacing: '1px'
  },
  cardTagHighlight: {
    padding: '6px 12px',
    background: 'linear-gradient(135deg, #22c55e 0%, #16a34a 100%)',
    borderRadius: '16px',
    fontSize: '11px',
    fontWeight: '700',
    color: 'white',
    letterSpacing: '0.5px',
  },
  cardTitle: {
    fontSize: '22px',
    fontWeight: '700',
    color: '#fff',
    marginBottom: '6px',
    letterSpacing: '-0.3px'
  },
  cardTitleLarge: {
    fontSize: '24px',
    fontWeight: '700',
    color: '#fff',
    marginBottom: '8px',
    letterSpacing: '-0.3px',
    lineHeight: '1.2'
  },
  cardDesc: {
    fontSize: '14px',
    color: '#94a3b8',
    marginBottom: '20px',
    lineHeight: '1.5'
  },
  cardDescLarge: {
    fontSize: '14px',
    color: '#94a3b8',
    marginBottom: '16px',
    lineHeight: '1.5',
    maxWidth: '90%'
  },

  // Assessment Steps
  assessmentSteps: {
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'flex-start',
    gap: '12px',
    marginBottom: '28px',
    padding: '16px 20px',
    background: 'rgba(255, 255, 255, 0.03)',
    borderRadius: '16px',
    border: '1px solid rgba(255, 255, 255, 0.05)'
  },
  stepItem: {
    display: 'flex',
    alignItems: 'center',
    gap: '10px'
  },
  stepNumber: {
    width: '28px',
    height: '28px',
    borderRadius: '50%',
    background: 'linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%)',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    fontSize: '13px',
    fontWeight: '700',
    color: 'white'
  },
  stepText: {
    fontSize: '14px',
    color: '#e2e8f0',
    fontWeight: '500'
  },
  stepArrow: {
    color: '#475569',
    fontSize: '16px'
  },
  quizLengthLabel: {
    fontSize: '12px',
    fontWeight: '600',
    color: '#94a3b8',
    marginBottom: '10px',
    textTransform: 'uppercase',
    letterSpacing: '1px'
  },

  // Assessment Options
  assessmentOptions: {
    display: 'flex',
    gap: '14px',
    marginBottom: '20px'
  },
  assessmentOption: {
    flex: 1,
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    gap: '8px',
    padding: '18px 14px',
    background: 'rgba(255, 255, 255, 0.03)',
    border: '2px solid rgba(255, 255, 255, 0.08)',
    borderRadius: '16px',
    cursor: 'pointer',
    transition: 'all 0.3s ease',
    position: 'relative',
    textAlign: 'center'
  },
  assessmentOptionActive: {
    background: 'rgba(99, 102, 241, 0.1)',
    borderColor: 'rgba(99, 102, 241, 0.4)',
    boxShadow: '0 8px 32px rgba(99, 102, 241, 0.2)'
  },
  optionEmoji: {
    fontSize: '24px',
    marginBottom: '2px'
  },
  optionInfo: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    gap: '2px'
  },
  optionName: {
    display: 'block',
    fontSize: '15px',
    fontWeight: '600',
    color: '#fff'
  },
  optionMeta: {
    fontSize: '11px',
    color: '#64748b'
  },
  optionDesc: {
    fontSize: '12px',
    fontWeight: '600',
    marginTop: '4px'
  },
  checkMark: {
    position: 'absolute',
    top: '8px',
    right: '8px',
    width: '20px',
    height: '20px',
    borderRadius: '50%',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    fontSize: '11px',
    fontWeight: '700',
    color: '#fff'
  },
  recommendedBadge: {
    position: 'absolute',
    top: '-8px',
    right: '-8px',
    width: '24px',
    height: '24px',
    borderRadius: '50%',
    background: 'linear-gradient(135deg, #f59e0b 0%, #d97706 100%)',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    fontSize: '12px',
    color: 'white',
    boxShadow: '0 4px 12px rgba(245, 158, 11, 0.4)'
  },

  // Start Button
  startBtn: {
    width: '100%',
    padding: '16px 28px',
    background: 'linear-gradient(135deg, #6366f1 0%, #8b5cf6 50%, #a855f7 100%)',
    border: 'none',
    borderRadius: '14px',
    color: 'white',
    fontSize: '16px',
    fontWeight: '600',
    cursor: 'pointer',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    gap: '10px',
    boxShadow: '0 8px 24px rgba(99, 102, 241, 0.3)',
    transition: 'all 0.3s ease',
  },
  startBtnDisabled: {
    opacity: 0.5,
    cursor: 'not-allowed',
    animation: 'none'
  },
  btnIcon: {
    fontSize: '22px'
  },
  btnText: {
    flex: 1
  },
  profileWarning: {
    marginTop: '12px',
    fontSize: '13px',
    color: '#f59e0b',
    textAlign: 'center'
  },
  profileLink: {
    color: '#a5b4fc',
    fontWeight: '600',
    cursor: 'pointer',
    textDecoration: 'underline'
  },

  // Stats Card
  bentoCardStats: {
    gridColumn: 'span 4',
    background: 'linear-gradient(145deg, rgba(34, 197, 94, 0.06) 0%, rgba(16, 185, 129, 0.03) 100%)',
    border: '1px solid rgba(34, 197, 94, 0.12)',
    borderRadius: '28px',
    padding: '28px',
    display: 'flex',
    alignItems: 'center',
    backdropFilter: 'blur(20px)',
    transition: 'all 0.4s cubic-bezier(0.4, 0, 0.2, 1)'
  },
  statsInner: {
    width: '100%',
    display: 'flex',
    flexDirection: 'column',
    gap: '24px'
  },
  statItem: {
    textAlign: 'center'
  },
  statNumber: {
    display: 'block',
    fontSize: '36px',
    fontWeight: '700',
    color: '#fff',
    marginBottom: '6px',
    letterSpacing: '-1px'
  },
  statText: {
    fontSize: '12px',
    color: '#64748b',
    textTransform: 'uppercase',
    letterSpacing: '1.5px',
    fontWeight: '500'
  },
  statDivider: {
    height: '1px',
    background: 'linear-gradient(90deg, transparent, rgba(255,255,255,0.08), transparent)'
  },

  // Small Bento Cards
  bentoCardSmall: {
    gridColumn: 'span 1',
    padding: '22px',
    background: 'rgba(15, 23, 42, 0.6)',
    border: '1px solid rgba(255, 255, 255, 0.06)',
    borderRadius: '18px',
    cursor: 'pointer',
    transition: 'all 0.3s ease',
    position: 'relative',
    backdropFilter: 'blur(10px)'
  },
  bentoCardHover: {
    background: 'rgba(255, 255, 255, 0.03)',
    transform: 'translateY(-4px)',
    boxShadow: '0 15px 40px rgba(0, 0, 0, 0.2)',
    borderColor: 'rgba(255, 255, 255, 0.1)'
  },
  smallCardIcon: {
    fontSize: '32px',
    marginBottom: '14px',
    display: 'block'
  },
  smallCardTitle: {
    fontSize: '16px',
    fontWeight: '600',
    color: '#fff',
    marginBottom: '6px'
  },
  smallCardDesc: {
    fontSize: '13px',
    color: '#64748b',
    lineHeight: '1.5'
  },
  cardArrow: {
    position: 'absolute',
    bottom: '18px',
    right: '18px',
    fontSize: '16px',
    color: '#475569',
    transition: 'all 0.3s ease'
  },
  activityBadge: {
    marginTop: '10px',
    display: 'inline-block',
    padding: '4px 10px',
    background: 'rgba(99, 102, 241, 0.12)',
    borderRadius: '6px',
    fontSize: '11px',
    color: '#a5b4fc',
    fontWeight: '500'
  },

  // Activity Card
  bentoCardActivity: {
    gridColumn: 'span 2',
    padding: '22px',
    background: 'rgba(15, 23, 42, 0.6)',
    border: '1px solid rgba(255, 255, 255, 0.06)',
    borderRadius: '18px',
    backdropFilter: 'blur(10px)',
    transition: 'all 0.3s ease'
  },
  activityHeader: {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: '14px'
  },
  activityTitle: {
    fontSize: '15px',
    fontWeight: '600',
    color: '#fff',
    margin: 0
  },
  viewAllBtn: {
    padding: '6px 12px',
    background: 'rgba(255, 255, 255, 0.04)',
    border: '1px solid rgba(255, 255, 255, 0.06)',
    borderRadius: '8px',
    color: '#94a3b8',
    fontSize: '12px',
    fontWeight: '500',
    cursor: 'pointer',
    transition: 'all 0.3s ease'
  },
  activityList: {
    display: 'flex',
    flexDirection: 'column',
    gap: '10px'
  },
  activityItem: {
    display: 'flex',
    alignItems: 'center',
    gap: '12px',
    padding: '12px 14px',
    background: 'rgba(255, 255, 255, 0.015)',
    borderRadius: '10px',
    border: '1px solid rgba(255, 255, 255, 0.03)',
    transition: 'all 0.3s ease'
  },
  activityDot: {
    width: '10px',
    height: '10px',
    borderRadius: '50%',
    flexShrink: 0,
    boxShadow: '0 0 10px currentColor'
  },
  activityInfo: {
    flex: 1,
    minWidth: 0
  },
  activityItemName: {
    display: 'block',
    fontSize: '15px',
    fontWeight: '500',
    color: '#e2e8f0',
    whiteSpace: 'nowrap',
    overflow: 'hidden',
    textOverflow: 'ellipsis'
  },
  activityItemDate: {
    fontSize: '13px',
    color: '#64748b'
  },
  activityItemBadge: {
    padding: '5px 12px',
    borderRadius: '8px',
    fontSize: '11px',
    fontWeight: '600',
    textTransform: 'uppercase',
    letterSpacing: '0.5px'
  },
  emptyActivity: {
    textAlign: 'center',
    padding: '48px 24px',
    color: '#475569'
  },
  emptyIcon: {
    fontSize: '40px',
    marginBottom: '14px',
    display: 'block',
    opacity: 0.4
  },

  // Features Card
  bentoCardFeatures: {
    gridColumn: 'span 6',
    padding: '28px',
    background: 'linear-gradient(145deg, rgba(244, 63, 94, 0.05) 0%, rgba(251, 113, 133, 0.02) 100%)',
    border: '1px solid rgba(244, 63, 94, 0.1)',
    borderRadius: '24px',
    backdropFilter: 'blur(10px)',
    transition: 'all 0.4s cubic-bezier(0.4, 0, 0.2, 1)'
  },
  featuresTitle: {
    fontSize: '17px',
    fontWeight: '600',
    color: '#fff',
    marginBottom: '24px'
  },
  featuresList: {
    display: 'flex',
    flexDirection: 'column',
    gap: '16px'
  },
  featureItem: {
    display: 'flex',
    alignItems: 'center',
    gap: '14px',
    fontSize: '15px',
    color: '#94a3b8'
  },
  featureIcon: {
    fontSize: '20px'
  },

  // Footer
  footer: {
    position: 'relative',
    zIndex: 1,
    borderTop: '1px solid rgba(255, 255, 255, 0.04)',
    padding: '28px 40px'
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
    fontSize: '14px',
    color: '#475569'
  },

  // Modal
  modalOverlay: {
    position: 'fixed',
    top: 0,
    left: 0,
    right: 0,
    bottom: 0,
    background: 'rgba(0, 0, 0, 0.8)',
    backdropFilter: 'blur(20px)',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    zIndex: 1000,
    animation: 'fadeIn 0.3s cubic-bezier(0.4, 0, 0.2, 1)'
  },
  modalContent: {
    background: 'linear-gradient(145deg, rgba(15, 23, 42, 0.95) 0%, rgba(30, 27, 75, 0.95) 100%)',
    borderRadius: '28px',
    width: '90%',
    maxWidth: '540px',
    maxHeight: '85vh',
    border: '1px solid rgba(255, 255, 255, 0.08)',
    overflow: 'hidden',
    boxShadow: '0 30px 100px rgba(0, 0, 0, 0.5)',
    animation: 'slideIn 0.4s cubic-bezier(0.4, 0, 0.2, 1)'
  },
  modalHeader: {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    padding: '24px 28px',
    borderBottom: '1px solid rgba(255, 255, 255, 0.05)'
  },
  modalTitle: {
    margin: 0,
    fontSize: '20px',
    fontWeight: '600',
    color: '#f1f5f9'
  },
  closeBtn: {
    background: 'rgba(255, 255, 255, 0.05)',
    border: 'none',
    color: '#94a3b8',
    width: '40px',
    height: '40px',
    borderRadius: '12px',
    cursor: 'pointer',
    fontSize: '18px',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    transition: 'all 0.3s cubic-bezier(0.4, 0, 0.2, 1)'
  },
  modalBody: {
    padding: '28px',
    overflowY: 'auto',
    maxHeight: 'calc(85vh - 80px)'
  },
  helpSection: {
    marginBottom: '28px'
  },
  helpSectionTitle: {
    fontSize: '13px',
    fontWeight: '600',
    color: '#818cf8',
    margin: '0 0 16px 0',
    textTransform: 'uppercase',
    letterSpacing: '1.5px'
  },
  helpItem: {
    marginBottom: '12px',
    padding: '18px',
    background: 'rgba(255, 255, 255, 0.02)',
    borderRadius: '14px',
    border: '1px solid rgba(255, 255, 255, 0.04)',
    fontSize: '15px',
    color: '#94a3b8',
    lineHeight: '1.6',
    transition: 'all 0.3s cubic-bezier(0.4, 0, 0.2, 1)'
  }
};

export default Dashboard;
