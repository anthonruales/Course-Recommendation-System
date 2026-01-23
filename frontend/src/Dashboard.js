import React, { useState, useEffect } from 'react';

function Dashboard({ userName, onLogout, onStart, onStartAdaptive, onViewProfile, onViewActivity, history }) {
  const [isExpanded, setIsExpanded] = useState(false);
  const [hasAcademicInfo, setHasAcademicInfo] = useState(false);
  const [checkingProfile, setCheckingProfile] = useState(true);
  const [selectedQuestionCount, setSelectedQuestionCount] = useState(30);

  // Check if user has filled academic info
  useEffect(() => {
    const userId = localStorage.getItem('userId');
    if (userId) {
      fetch(`http://localhost:8000/user/${userId}/academic-info`)
        .then(res => res.json())
        .then(data => {
          setHasAcademicInfo(data.has_academic_info || false);
          setCheckingProfile(false);
        })
        .catch(err => {
          console.error('Error checking academic info:', err);
          setCheckingProfile(false);
        });
    } else {
      setCheckingProfile(false);
    }
  }, []);

  const handleStartAdaptive = () => {
    if (!hasAcademicInfo) {
      alert('⚠️ Please complete your Academic Profile first!\n\nYou need to fill in your GWA and SHS Strand before taking the assessment.');
      onViewProfile();
      return;
    }
    // Pass the selected question count to the assessment
    onStartAdaptive(selectedQuestionCount);
  };

  // Keeps your original logic for history display
  const displayHistory = isExpanded ? history : history?.slice(0, 5);

  return (
    <div style={styles.dashboardWrapper}>
      {/* SIDEBAR */}
      <aside style={styles.sidebar}>
        <div style={styles.brandContainer}>
          <div style={styles.logoIcon}>C</div>
          <h2 style={styles.brandName}>CoursePro</h2>
        </div>
        
        <nav style={styles.nav}>
          <div style={styles.categoryLabel}>Main Menu</div>
          <div style={{...styles.navItem, ...styles.navActive}}>📊 Dashboard</div>

          <div style={styles.categoryLabel}>Academics</div>
          <div style={styles.navItem} onClick={onViewProfile}
            onMouseEnter={(e) => { e.target.style.background = 'rgba(255, 255, 255, 0.05)'; e.target.style.color = '#cbd5e1'; e.target.style.transform = 'translateX(4px)'; }}
            onMouseLeave={(e) => { e.target.style.background = 'transparent'; e.target.style.color = '#94a3b8'; e.target.style.transform = 'translateX(0)'; }}
          >👤 Academic Profile</div>
          <div style={styles.navItem} onClick={onViewActivity}
            onMouseEnter={(e) => { e.target.style.background = 'rgba(255, 255, 255, 0.05)'; e.target.style.color = '#cbd5e1'; e.target.style.transform = 'translateX(4px)'; }}
            onMouseLeave={(e) => { e.target.style.background = 'transparent'; e.target.style.color = '#94a3b8'; e.target.style.transform = 'translateX(0)'; }}
          >📂 My Activity ({history ? history.length : 0})</div>

          <div style={styles.categoryLabel}>Support</div>
          <div style={styles.navItem}
            onMouseEnter={(e) => { e.target.style.background = 'rgba(255, 255, 255, 0.05)'; e.target.style.color = '#cbd5e1'; e.target.style.transform = 'translateX(4px)'; }}
            onMouseLeave={(e) => { e.target.style.background = 'transparent'; e.target.style.color = '#94a3b8'; e.target.style.transform = 'translateX(0)'; }}
          >❓ Help Center</div>
          <div style={styles.navItem}
            onMouseEnter={(e) => { e.target.style.background = 'rgba(255, 255, 255, 0.05)'; e.target.style.color = '#cbd5e1'; e.target.style.transform = 'translateX(4px)'; }}
            onMouseLeave={(e) => { e.target.style.background = 'transparent'; e.target.style.color = '#94a3b8'; e.target.style.transform = 'translateX(0)'; }}
          >💬 Feedback</div>
        </nav>

        <button onClick={onLogout} style={styles.logoutBtn}
          onMouseEnter={(e) => { e.target.style.background = 'rgba(239, 68, 68, 0.1)'; e.target.style.borderColor = 'rgba(239, 68, 68, 0.4)'; e.target.style.transform = 'translateY(-2px)'; }}
          onMouseLeave={(e) => { e.target.style.background = 'transparent'; e.target.style.borderColor = 'rgba(239, 68, 68, 0.2)'; e.target.style.transform = 'translateY(0)'; }}
        >
          Logout
        </button>
      </aside>

      {/* MAIN CONTENT */}
      <main style={styles.mainContent}>
        <header style={styles.header}>
          <h1 style={styles.headerTitle}>Dashboard</h1>
          <p style={styles.headerSubtitle}>Welcome back, {userName}</p>
        </header>

        {/* ASSESSMENT CALL TO ACTION */}
        <div style={styles.actionCard}>
          <div style={styles.actionContent}>
            <div style={{flex: 1}}>
              <h3 style={styles.actionTitle}>Take an Assessment</h3>
              <p style={styles.actionText}>
                Answer questions to receive personalized course recommendations based on your interests and skills.
              </p>
              {!checkingProfile && !hasAcademicInfo && (
                <p style={{color: '#f59e0b', fontSize: '13px', marginTop: '10px'}}>
                  ⚠️ Please complete your Academic Profile (GWA & Strand) before taking the assessment.
                </p>
              )}
            </div>
            <div style={styles.assessmentButtons}>
              <div style={styles.questionSelector}>
                <span style={styles.selectorLabel}>Number of Questions:</span>
                <div style={styles.selectorOptions}>
                  {[30, 50, 60].map((count) => (
                    <button
                      key={count}
                      style={{
                        ...styles.selectorBtn,
                        ...(selectedQuestionCount === count ? styles.selectorBtnActive : {})
                      }}
                      onClick={() => setSelectedQuestionCount(count)}
                    >
                      {count}
                    </button>
                  ))}
                </div>
              </div>
              <button 
                style={{
                  ...styles.adaptiveBtn,
                  ...((!hasAcademicInfo && !checkingProfile) ? {opacity: 0.7, cursor: 'not-allowed'} : {})
                }} 
                onClick={handleStartAdaptive}
                onMouseEnter={(e) => { if (hasAcademicInfo) { e.target.style.transform = 'translateY(-2px)'; e.target.style.boxShadow = '0 15px 30px rgba(99, 102, 241, 0.4)'; } }}
                onMouseLeave={(e) => { e.target.style.transform = 'translateY(0)'; e.target.style.boxShadow = '0 10px 20px rgba(99, 102, 241, 0.2)'; }}
              >
                {checkingProfile ? 'Checking...' : 'Start Assessment'}
              </button>
            </div>
          </div>
          <div style={styles.assessmentInfo}>
            <div style={styles.infoCard}>
              <span style={styles.infoIcon}>⚡</span>
              <strong>30 Questions</strong>
              <span style={styles.infoDesc}>Quick assessment (~10 min)</span>
            </div>
            <div style={styles.infoCard}>
              <span style={styles.infoIcon}>📊</span>
              <strong>50 Questions</strong>
              <span style={styles.infoDesc}>Standard assessment (~15 min)</span>
            </div>
            <div style={styles.infoCard}>
              <span style={styles.infoIcon}>🎯</span>
              <strong>60 Questions</strong>
              <span style={styles.infoDesc}>Comprehensive (~20 min)</span>
            </div>
          </div>
        </div>

        {/* DASHBOARD GRID */}
        <div style={styles.dashboardGrid}>
          
          {/* RECENT ACTIVITY CARD */}
          <div style={styles.portalCard}>
            <div style={styles.cardHeader}>
              <h4 style={styles.cardTitle}>Recent Activity</h4>
              {history && history.length > 5 && (
                <button 
                  style={styles.linkBtn}
                  onClick={() => setIsExpanded(!isExpanded)}
                  onMouseEnter={(e) => { e.target.style.color = '#818cf8'; e.target.style.textDecoration = 'underline'; }}
                  onMouseLeave={(e) => { e.target.style.color = '#6366f1'; e.target.style.textDecoration = 'none'; }}
                >
                  {isExpanded ? 'Show Less' : 'View All'}
                </button>
              )}
            </div>

            {history && history.length > 0 ? (
              <div style={styles.activityList}>
                {displayHistory.map((item, index) => (
                  <div key={index} style={styles.activityItem}>
                    <div style={styles.activityInfo}>
                      <div style={styles.activityName}>
                        {item.type === 'assessment' && Array.isArray(item.courses) && item.courses.length > 0
                          ? (typeof item.courses[0] === 'object' ? item.courses[0].course : item.courses[0])
                          : item.courses}
                      </div>
                      <div style={styles.activityDate}>{item.date}</div>
                    </div>
                    <span style={{
                      ...styles.badge,
                      ...(item.type === 'profile_update' ? styles.profileBadge : styles.assessmentBadge)
                    }}>
                      {item.type === 'profile_update' ? 'Profile' : 'Assessment'}
                    </span>
                  </div>
                ))}
              </div>
            ) : (
              <p style={styles.mutedText}>No history found.</p>
            )}
          </div>

          {/* ACCOUNT SUMMARY CARD */}
          <div style={styles.portalCard}>
            <h4 style={styles.cardTitle}>Account Summary</h4>
            <p style={styles.mutedText}>Your account is synchronized and up to date.</p>
            
            {history && history.length > 0 && (
              <div style={styles.summaryBox}>
                <div style={styles.summarySuccess}>
                  <span style={{ marginRight: '8px', color: '#10b981' }}>✓</span>
                  {history.filter(h => h.type === 'assessment').length} Assessment(s) Recorded
                </div>
                <p style={styles.summaryDate}>
                  Latest activity logged on {history[0].date}
                </p>
              </div>
            )}
          </div>
        </div>
      </main>
    </div>
  );
}

const styles = {
  dashboardWrapper: { display: 'flex', width: '100vw', height: '100vh', background: 'transparent', color: 'white' },
  sidebar: {
    width: '260px', background: 'rgba(255, 255, 255, 0.02)', backdropFilter: 'blur(20px)',
    borderRight: '1px solid rgba(255, 255, 255, 0.08)', display: 'flex', flexDirection: 'column', padding: '40px 20px'
  },
  brandContainer: { display: 'flex', alignItems: 'center', marginBottom: '40px', paddingLeft: '10px' },
  logoIcon: {
    width: '35px', height: '35px', background: 'linear-gradient(135deg, #6366f1, #8b5cf6)',
    borderRadius: '8px', display: 'flex', alignItems: 'center', justifyContent: 'center', fontWeight: '800', marginRight: '12px'
  },
  brandName: { fontSize: '18px', fontWeight: '700', margin: 0 },
  nav: { flex: 1 },
  categoryLabel: { fontSize: '11px', fontWeight: '700', color: '#64748b', textTransform: 'uppercase', letterSpacing: '1px', margin: '20px 0 10px 10px' },
  navItem: {
    padding: '12px 15px', borderRadius: '10px', color: '#94a3b8', cursor: 'pointer',
    fontSize: '14px', marginBottom: '4px', transition: 'all 0.3s ease',
    ':hover': { background: 'rgba(255, 255, 255, 0.05)', color: '#cbd5e1', transform: 'translateX(4px)' }
  },
  navActive: { background: 'rgba(99, 102, 241, 0.1)', color: '#818cf8', fontWeight: '600' },
  logoutBtn: {
    padding: '12px', borderRadius: '10px', border: '1px solid rgba(239, 68, 68, 0.2)',
    background: 'transparent', color: '#ef4444', cursor: 'pointer', fontWeight: '600',
    transition: 'all 0.3s ease'
  },
  mainContent: { flex: 1, padding: '40px 60px', overflowY: 'auto' },
  header: { marginBottom: '30px' },
  headerTitle: { fontSize: '28px', fontWeight: '800', margin: 0 },
  headerSubtitle: { color: '#94a3b8', fontSize: '15px', marginTop: '5px' },
  actionCard: {
    background: 'linear-gradient(135deg, rgba(99, 102, 241, 0.15) 0%, rgba(168, 85, 247, 0.05) 100%)',
    border: '1px solid rgba(255,255,255,0.08)', borderRadius: '20px', padding: '30px', marginBottom: '30px'
  },
  actionContent: { display: 'flex', justifyContent: 'space-between', alignItems: 'center' },
  actionTitle: { fontSize: '20px', fontWeight: '700', margin: '0 0 10px 0' },
  actionText: { color: '#cbd5e1', fontSize: '14px', maxWidth: '500px', margin: 0, lineHeight: '1.5' },
  startBtn: {
    background: '#6366f1', color: 'white', padding: '14px 24px', borderRadius: '12px',
    border: 'none', fontWeight: '700', cursor: 'pointer', boxShadow: '0 10px 20px rgba(99, 102, 241, 0.2)',
    transition: 'all 0.3s ease', fontSize: '14px'
  },
  adaptiveBtn: {
    background: 'linear-gradient(135deg, #6366f1, #8b5cf6)', color: 'white', padding: '16px 32px', borderRadius: '12px',
    border: 'none', fontWeight: '700', cursor: 'pointer', boxShadow: '0 10px 20px rgba(99, 102, 241, 0.2)',
    transition: 'all 0.3s ease', fontSize: '15px', letterSpacing: '0.5px'
  },
  recommendedBadge: {
    position: 'absolute', top: '-8px', right: '-8px', background: '#f59e0b', color: 'white',
    fontSize: '9px', fontWeight: '800', padding: '3px 8px', borderRadius: '10px', textTransform: 'uppercase'
  },
  assessmentButtons: {
    display: 'flex', gap: '15px', alignItems: 'center', flexDirection: 'column'
  },
  questionSelector: {
    display: 'flex', alignItems: 'center', gap: '15px', marginBottom: '10px'
  },
  selectorLabel: {
    fontSize: '14px', color: '#94a3b8', fontWeight: '600'
  },
  selectorOptions: {
    display: 'flex', gap: '8px'
  },
  selectorBtn: {
    padding: '10px 20px', borderRadius: '10px', border: '1px solid rgba(255,255,255,0.15)',
    background: 'rgba(255,255,255,0.03)', color: '#94a3b8', cursor: 'pointer',
    fontWeight: '700', fontSize: '15px', transition: 'all 0.2s ease'
  },
  selectorBtnActive: {
    background: 'linear-gradient(135deg, #6366f1, #8b5cf6)', color: 'white',
    borderColor: '#6366f1', boxShadow: '0 5px 15px rgba(99, 102, 241, 0.3)'
  },
  assessmentInfo: {
    display: 'flex', gap: '20px', marginTop: '20px', paddingTop: '20px', borderTop: '1px solid rgba(255,255,255,0.08)'
  },
  infoCard: {
    display: 'flex', alignItems: 'center', gap: '10px', fontSize: '13px', color: '#94a3b8'
  },
  infoIcon: { fontSize: '20px' },
  infoDesc: { color: '#64748b', fontSize: '12px', marginLeft: '5px' },
  dashboardGrid: { display: 'grid', gridTemplateColumns: '1.5fr 1fr', gap: '25px' },
  portalCard: {
    background: 'rgba(255, 255, 255, 0.03)', border: '1px solid rgba(255, 255, 255, 0.08)',
    borderRadius: '20px', padding: '25px', transition: 'all 0.3s ease'
  },
  cardHeader: { display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '20px' },
  cardTitle: { fontSize: '17px', fontWeight: '700', margin: 0 },
  linkBtn: { background: 'none', border: 'none', color: '#6366f1', fontWeight: '700', fontSize: '12px', cursor: 'pointer', transition: 'all 0.3s ease' },
  activityList: { display: 'flex', flexDirection: 'column', gap: '12px' },
  activityItem: {
    padding: '15px', background: 'rgba(255,255,255,0.02)', borderRadius: '12px',
    border: '1px solid rgba(255,255,255,0.05)', display: 'flex', justifyContent: 'space-between', alignItems: 'center',
    transition: 'all 0.3s ease'
  },
  activityName: { fontSize: '14px', fontWeight: '600', color: 'white' },
  activityDate: { fontSize: '12px', color: '#64748b', marginTop: '4px' },
  badge: { padding: '4px 10px', borderRadius: '6px', fontSize: '10px', fontWeight: '800', textTransform: 'uppercase' },
  assessmentBadge: { background: 'rgba(99, 102, 241, 0.1)', color: '#818cf8' },
  profileBadge: { background: 'rgba(244, 63, 94, 0.1)', color: '#fb7185' },
  mutedText: { color: '#64748b', fontSize: '14px' },
  summaryBox: { marginTop: '20px', padding: '15px', background: 'rgba(255,255,255,0.02)', borderRadius: '12px' },
  summarySuccess: { fontSize: '14px', fontWeight: '600', color: '#e2e8f0', display: 'flex', alignItems: 'center' },
  summaryDate: { fontSize: '12px', color: '#64748b', marginTop: '8px' }
};

export default Dashboard;