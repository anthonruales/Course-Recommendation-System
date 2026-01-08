import React, { useState } from 'react';

function Dashboard({ userName, onLogout, onStart, onViewProfile, history }) {
  const [isExpanded, setIsExpanded] = useState(false);

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
          <div style={styles.navItem} onClick={onViewProfile}>👤 Academic Profile</div>
          <div style={{...styles.navItem, cursor: 'default', opacity: 0.7}}>
            📂 My Activity ({history ? history.length : 0})
          </div>

          <div style={styles.categoryLabel}>Support</div>
          <div style={styles.navItem}>❓ Help Center</div>
          <div style={styles.navItem}>💬 Feedback</div>
        </nav>

        <button onClick={onLogout} style={styles.logoutBtn}>
          Logout
        </button>
      </aside>

      {/* MAIN CONTENT */}
      <main style={styles.mainContent}>
        <header style={styles.header}>
          <h1 style={styles.headerTitle}>Student Overview</h1>
          <p style={styles.headerSubtitle}>Welcome back, {userName}. Track your progress and findings here.</p>
        </header>

        {/* ASSESSMENT CALL TO ACTION */}
        <div style={styles.actionCard}>
          <div style={styles.actionContent}>
            <div>
              <h3 style={styles.actionTitle}>Ready for your recommendation?</h3>
              <p style={styles.actionText}>
                Launch the assessment to begin the interest questionnaire. 
                We will use your saved Academic Profile for the final analysis.
              </p>
            </div>
            <button style={styles.startBtn} onClick={onStart}>
              Start New Assessment
            </button>
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
    fontSize: '14px', marginBottom: '4px', transition: '0.2s'
  },
  navActive: { background: 'rgba(99, 102, 241, 0.1)', color: '#818cf8', fontWeight: '600' },
  logoutBtn: {
    padding: '12px', borderRadius: '10px', border: '1px solid rgba(239, 68, 68, 0.2)',
    background: 'transparent', color: '#ef4444', cursor: 'pointer', fontWeight: '600'
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
    border: 'none', fontWeight: '700', cursor: 'pointer', boxShadow: '0 10px 20px rgba(99, 102, 241, 0.2)'
  },
  dashboardGrid: { display: 'grid', gridTemplateColumns: '1.5fr 1fr', gap: '25px' },
  portalCard: {
    background: 'rgba(255, 255, 255, 0.03)', border: '1px solid rgba(255, 255, 255, 0.08)',
    borderRadius: '20px', padding: '25px'
  },
  cardHeader: { display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '20px' },
  cardTitle: { fontSize: '17px', fontWeight: '700', margin: 0 },
  linkBtn: { background: 'none', border: 'none', color: '#6366f1', fontWeight: '700', fontSize: '12px', cursor: 'pointer' },
  activityList: { display: 'flex', flexDirection: 'column', gap: '12px' },
  activityItem: {
    padding: '15px', background: 'rgba(255,255,255,0.02)', borderRadius: '12px',
    border: '1px solid rgba(255,255,255,0.05)', display: 'flex', justifyContent: 'space-between', alignItems: 'center'
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