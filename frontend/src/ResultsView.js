import React, { useState } from 'react';
import FeedbackForm from './FeedbackForm';
import NavBar from './components/NavBar';

const styles = {
  pageWrapper: {
    minHeight: '100vh',
    background: '#050510',
    display: 'flex',
    flexDirection: 'column',
    color: 'white',
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
    gap: '12px',
  },
  backBtn: {
    background: 'rgba(99, 102, 241, 0.1)',
    border: '1px solid rgba(99, 102, 241, 0.2)',
    color: '#a5b4fc',
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
    maxWidth: '1200px',
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
    background: 'rgba(16, 185, 129, 0.1)',
    border: '1px solid rgba(16, 185, 129, 0.2)',
    borderRadius: '50px',
    padding: '8px 20px',
    fontSize: '13px',
    color: '#34d399',
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
    margin: '0 auto 24px',
    lineHeight: 1.6,
  },
  traitsContainer: {
    display: 'flex',
    gap: '10px',
    justifyContent: 'center',
    flexWrap: 'wrap',
  },
  traitBadge: {
    padding: '6px 14px',
    borderRadius: '8px',
    fontSize: '12px',
    fontWeight: '600',
    background: 'rgba(99, 102, 241, 0.15)',
    color: '#a5b4fc',
  },
  resultsGrid: {
    display: 'flex',
    flexDirection: 'column',
    gap: '24px',
    marginBottom: '48px',
  },
  resultCard: {
    background: 'rgba(15, 23, 42, 0.6)',
    backdropFilter: 'blur(20px)',
    border: '1px solid rgba(255,255,255,0.06)',
    borderRadius: '20px',
    padding: '32px',
    position: 'relative',
    transition: 'all 0.3s ease',
  },
  cardHeader: {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'flex-start',
    marginBottom: '20px',
  },
  rankBadge: {
    padding: '6px 16px',
    borderRadius: '8px',
    fontSize: '12px',
    fontWeight: '700',
    background: 'transparent',
    marginBottom: '12px',
    display: 'inline-block',
  },
  courseTitle: {
    fontSize: '22px',
    fontWeight: '700',
    margin: '0 0 8px 0',
    color: '#f1f5f9',
  },
  courseDesc: {
    color: '#64748b',
    fontSize: '14px',
    margin: 0,
    lineHeight: 1.5,
  },
  scoreDisplay: {
    textAlign: 'right',
    flexShrink: 0,
    marginLeft: '24px',
  },
  percentageText: {
    fontSize: '48px',
    fontWeight: '800',
    lineHeight: 1,
  },
  matchLabel: {
    fontSize: '12px',
    color: '#64748b',
    textTransform: 'uppercase',
    letterSpacing: '1px',
    marginTop: '4px',
  },
  reasoningBox: {
    background: 'rgba(30, 41, 59, 0.5)',
    borderRadius: '12px',
    padding: '20px',
    marginBottom: '20px',
    borderLeft: '3px solid #6366f1',
  },
  reasoningLabel: {
    fontSize: '11px',
    fontWeight: '700',
    color: '#64748b',
    textTransform: 'uppercase',
    letterSpacing: '1px',
    marginBottom: '8px',
  },
  reasoningText: {
    color: '#cbd5e1',
    fontSize: '14px',
    margin: 0,
    lineHeight: 1.6,
  },
  tagsRow: {
    display: 'flex',
    gap: '10px',
    flexWrap: 'wrap',
  },
  tagBadge: {
    padding: '6px 14px',
    borderRadius: '8px',
    fontSize: '12px',
    fontWeight: '600',
    background: 'rgba(99, 102, 241, 0.15)',
    color: '#a5b4fc',
  },
  tagBadgeSecondary: {
    padding: '6px 14px',
    borderRadius: '8px',
    fontSize: '12px',
    fontWeight: '600',
    background: 'rgba(16, 185, 129, 0.15)',
    color: '#10b981',
  },
  footer: {
    textAlign: 'center',
    padding: '40px',
    background: 'rgba(15, 23, 42, 0.6)',
    backdropFilter: 'blur(20px)',
    border: '1px solid rgba(255,255,255,0.06)',
    borderRadius: '20px',
  },
  footerTitle: {
    fontSize: '20px',
    fontWeight: '700',
    color: '#f1f5f9',
    margin: '0 0 8px 0',
  },
  footerSubtitle: {
    color: '#64748b',
    fontSize: '14px',
    margin: '0 0 24px 0',
  },
  buttonGroup: {
    display: 'flex',
    gap: '16px',
    justifyContent: 'center',
    flexWrap: 'wrap',
  },
  primaryBtn: {
    background: 'linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%)',
    color: 'white',
    padding: '14px 28px',
    borderRadius: '12px',
    border: 'none',
    fontWeight: '600',
    fontSize: '14px',
    cursor: 'pointer',
    transition: 'all 0.2s ease',
    boxShadow: '0 4px 14px rgba(99, 102, 241, 0.25)',
  },
  secondaryBtn: {
    background: 'rgba(255,255,255,0.05)',
    color: '#94a3b8',
    padding: '14px 28px',
    borderRadius: '12px',
    border: '1px solid rgba(255,255,255,0.1)',
    fontWeight: '600',
    fontSize: '14px',
    cursor: 'pointer',
    transition: 'all 0.2s ease',
  },
  loadingState: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center',
    minHeight: '60vh',
    textAlign: 'center',
  },
  loadingTitle: {
    fontSize: '24px',
    fontWeight: '700',
    color: '#f1f5f9',
    marginBottom: '12px',
  },
  loadingText: {
    color: '#64748b',
    marginBottom: '24px',
  },
  // Export Section Styles
  exportSection: {
    textAlign: 'center',
    padding: '32px',
    background: 'rgba(15, 23, 42, 0.6)',
    backdropFilter: 'blur(20px)',
    border: '1px solid rgba(255,255,255,0.06)',
    borderRadius: '20px',
    marginBottom: '24px',
  },
  exportTitle: {
    fontSize: '18px',
    fontWeight: '700',
    color: '#f1f5f9',
    margin: '0 0 8px 0',
  },
  exportSubtitle: {
    color: '#64748b',
    fontSize: '14px',
    margin: '0 0 20px 0',
  },
  exportButtons: {
    display: 'flex',
    gap: '16px',
    justifyContent: 'center',
    flexWrap: 'wrap',
  },
  exportBtn: {
    background: 'rgba(99, 102, 241, 0.1)',
    color: '#a5b4fc',
    padding: '14px 28px',
    borderRadius: '12px',
    border: '1px solid rgba(99, 102, 241, 0.2)',
    fontWeight: '600',
    fontSize: '14px',
    cursor: 'pointer',
    transition: 'all 0.2s ease',
    display: 'flex',
    alignItems: 'center',
    gap: '8px',
  },
  exportMessage: {
    padding: '12px 20px',
    borderRadius: '10px',
    border: '1px solid',
    marginBottom: '20px',
    fontSize: '14px',
    fontWeight: '500',
  },
  // Email Modal Styles
  modalOverlay: {
    position: 'fixed',
    top: 0,
    left: 0,
    right: 0,
    bottom: 0,
    background: 'rgba(0, 0, 0, 0.7)',
    backdropFilter: 'blur(8px)',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    zIndex: 1000,
  },
  emailModal: {
    background: 'rgba(15, 23, 42, 0.95)',
    border: '1px solid rgba(255,255,255,0.1)',
    borderRadius: '20px',
    padding: '32px',
    maxWidth: '400px',
    width: '90%',
    textAlign: 'center',
  },
  emailModalTitle: {
    fontSize: '20px',
    fontWeight: '700',
    color: '#f1f5f9',
    margin: '0 0 8px 0',
  },
  emailModalSubtitle: {
    color: '#64748b',
    fontSize: '14px',
    margin: '0 0 24px 0',
  },
  emailInput: {
    width: '100%',
    padding: '14px 18px',
    borderRadius: '12px',
    border: '1px solid rgba(255,255,255,0.1)',
    background: 'rgba(255,255,255,0.05)',
    color: '#f1f5f9',
    fontSize: '14px',
    marginBottom: '20px',
    outline: 'none',
    boxSizing: 'border-box',
  },
  emailModalButtons: {
    display: 'flex',
    gap: '12px',
    justifyContent: 'center',
  },
};

function ResultsView({ recommendation, profileData, onRetake, onBack, onViewProfile, onViewActivity }) {
  const [showFeedback, setShowFeedback] = useState(null);
  const [exporting, setExporting] = useState(false);
  const [emailSending, setEmailSending] = useState(false);
  const [exportMessage, setExportMessage] = useState(null);
  const userId = localStorage.getItem('userId');
  const userName = localStorage.getItem('userName') || 'Student';
  const userEmail = localStorage.getItem('userEmail') || '';
  
  console.log('[ResultsView] userId from localStorage:', userId);

  // Export to PDF
  const handleExportPDF = async () => {
    setExporting(true);
    setExportMessage(null);
    try {
      const userId = localStorage.getItem('userId');
      
      // Fetch user's GWA and Strand from backend
      const userRes = await fetch(`${process.env.REACT_APP_API_URL}/user/${userId}/academic-info`);
      const userData = await userRes.json();
      const userGwa = userData.academic_info?.gwa || null;
      const userStrand = userData.academic_info?.strand || null;
      
      const response = await fetch(`${process.env.REACT_APP_API_URL}/export/pdf`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          user_name: userName,
          user_gwa: userGwa,
          user_strand: userStrand,
          detected_traits: recommendation.detected_traits || [],
          recommendations: recommendation.recommendations.map(r => ({
            course_name: r.course_name,
            description: r.description || '',
            compatibility_score: r.compatibility_score || r.match_percentage || 75,
            matched_traits: r.matched_traits || [],
            reasoning: r.reasoning || ''
          }))
        })
      });
      
      if (response.ok) {
        const blob = await response.blob();
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `CoursePro_Recommendations_${userName.replace(/\s+/g, '_')}.pdf`;
        document.body.appendChild(a);
        a.click();
        window.URL.revokeObjectURL(url);
        a.remove();
        setExportMessage({ type: 'success', text: 'PDF downloaded successfully!' });
      } else {
        const error = await response.json();
        setExportMessage({ type: 'error', text: error.detail || 'Failed to generate PDF' });
      }
    } catch (err) {
      console.error('PDF export error:', err);
      setExportMessage({ type: 'error', text: 'Error generating PDF. Please try again.' });
    }
    setExporting(false);
  };

  // Send to Email (auto-sends to user's account email)
  const handleSendEmail = async () => {
    if (!userEmail || !userEmail.includes('@')) {
      setExportMessage({ type: 'error', text: 'No email address found on your account. Please add one in Settings.' });
      return;
    }
    
    setEmailSending(true);
    setExportMessage(null);
    try {
      const response = await fetch(`${process.env.REACT_APP_API_URL}/export/email`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          email: userEmail,
          user_name: userName,
          user_gwa: recommendation.user_gwa,
          user_strand: recommendation.user_strand,
          detected_traits: recommendation.detected_traits || [],
          recommendations: recommendation.recommendations
        })
      });
      
      const result = await response.json();
      if (response.ok) {
        setExportMessage({ type: 'success', text: result.message || `Email sent to ${userEmail}!` });
      } else if (response.status === 503) {
        setExportMessage({ type: 'error', text: '📧 Email service is in testing mode. Please use "Download PDF" to save your results instead.' });
      } else {
        setExportMessage({ type: 'error', text: result.detail || 'Failed to send email' });
      }
    } catch (err) {
      setExportMessage({ type: 'error', text: 'Error sending email. Please try again.' });
    }
    setEmailSending(false);
  };
  
  // Loading state
  if (!recommendation || !recommendation.recommendations) {
    return (
      <div style={styles.pageWrapper}>
        <NavBar
          activePage={null}
          onNavigate={(page) => {
            if (page === 'home') onBack();
            else if (page === 'profile') onViewProfile && onViewProfile();
            else if (page === 'activity') onViewActivity && onViewActivity();
          }}
        />
        <main className="results-main-content" style={styles.mainContent}>
          <div style={styles.loadingState}>
            <h2 style={styles.loadingTitle}>Analyzing your responses...</h2>
            <p style={styles.loadingText}>If this takes too long, please check your connection.</p>
            <button onClick={onBack} style={styles.primaryBtn}>
              Return to Dashboard
            </button>
          </div>
        </main>
      </div>
    );
  }

  const getDisplayPercentage = (item) => {
    let score = item.compatibility_score ?? item.final_score ?? item.match_percentage ?? item.score;
    if (score === undefined || score === null || isNaN(score)) {
      score = 75;
    }
    return Math.round(score);
  };

  const getRankColor = (index) => {
    if (index === 0) return '#fbbf24'; // Gold
    if (index === 1) return '#9ca3af'; // Silver
    if (index === 2) return '#d97706'; // Bronze
    return '#6366f1';
  };

  // Deduplicate traits by consolidating counts for the same trait name
  const rawTraits = recommendation.detected_traits || [];
  const traitMap = {};
  rawTraits.forEach(([trait, count]) => {
    traitMap[trait] = (traitMap[trait] || 0) + count;
  });
  const topTraits = Object.entries(traitMap).sort((a, b) => b[1] - a[1]);
  const { user_gwa, user_strand } = recommendation;

  return (
    <div style={styles.pageWrapper}>
      {/* TOP NAVIGATION */}
      <NavBar
        activePage={null}
        onNavigate={(page) => {
          if (page === 'home') onBack();
          else if (page === 'profile') onViewProfile && onViewProfile();
          else if (page === 'activity') onViewActivity && onViewActivity();
        }}
      />

      {/* MAIN CONTENT */}
      <main className="results-main-content" style={styles.mainContent}>
        {/* Hero Header */}
        <div style={styles.heroHeader}>
          <div style={styles.heroBadge}>
            <span>🎯</span> Analysis Complete
          </div>
          <h1 className="results-hero-title" style={styles.heroTitle}>
            Your Career <span style={styles.heroGradient}>Recommendations</span>
          </h1>
          <p style={styles.heroSubtitle}>
            Based on your personality traits and academic profile
            {user_strand && ` as a ${user_strand} student`}
            {user_gwa && ` with GWA of ${user_gwa}`}.
          </p>

          {topTraits.length > 0 && (
            <div style={styles.traitsContainer}>
              <span style={{color: '#94a3b8', fontSize: '14px', marginRight: '8px'}}>Detected Traits:</span>
              {topTraits.map(([trait, count], idx) => (
                <span key={idx} style={styles.traitBadge}>
                  {trait} ({count})
                </span>
              ))}
            </div>
          )}
        </div>

        {/* Export Section - Moved to top */}
        <div style={styles.exportSection}>
          <h3 style={styles.exportTitle}>📥 Save Your Results</h3>
          <p style={styles.exportSubtitle}>Download or share your recommendations</p>
          
          {exportMessage && (
            <div style={{
              ...styles.exportMessage,
              background: exportMessage.type === 'success' ? 'rgba(16, 185, 129, 0.1)' : 'rgba(239, 68, 68, 0.1)',
              borderColor: exportMessage.type === 'success' ? 'rgba(16, 185, 129, 0.3)' : 'rgba(239, 68, 68, 0.3)',
              color: exportMessage.type === 'success' ? '#10b981' : '#ef4444'
            }}>
              {exportMessage.text}
            </div>
          )}
          
          <div className="results-export-buttons" style={styles.exportButtons}>
            <button 
              onClick={handleExportPDF}
              disabled={exporting}
              style={styles.exportBtn}
            >
              {exporting ? '⏳ Generating...' : '📄 Download PDF'}
            </button>
            <button 
              onClick={handleSendEmail}
              disabled={emailSending}
              style={styles.exportBtn}
            >
              {emailSending ? '⏳ Sending...' : '✉️ Send to Email'}
            </button>
          </div>
        </div>

        {/* Results List */}
        <div className="results-grid" style={styles.resultsGrid}>
          {recommendation.recommendations.map((item, index) => {
            const rankColor = getRankColor(index);
            
            return (
              <div 
                key={index} 
                style={{
                  ...styles.resultCard,
                  borderLeft: `4px solid ${rankColor}`
                }}
              >
                <div className="results-card-header" style={styles.cardHeader}>
                  <div style={{ flex: 1 }}>
                    <span 
                      style={{
                        ...styles.rankBadge,
                        color: rankColor,
                        border: `1px solid ${rankColor}`,
                      }}
                    >
                      Rank #{index + 1} Match
                    </span>
                    <h3 style={{...styles.courseTitle, color: index === 0 ? '#fbbf24' : '#a5b4fc'}}>
                      {item.course_name}
                    </h3>
                    {item.description && <p style={styles.courseDesc}>{item.description}</p>}
                  </div>
                  
                  <div className="results-score-display" style={styles.scoreDisplay}>
                    <div className="results-percentage-text" style={{...styles.percentageText, color: rankColor}}>
                      {getDisplayPercentage(item)}%
                    </div>
                    <div style={styles.matchLabel}>Match Score</div>
                  </div>
                </div>

                {/* Reasoning Box */}
                <div style={styles.reasoningBox}>
                  <div style={styles.reasoningLabel}>Why this fits you:</div>
                  <p style={styles.reasoningText}>{item.reasoning}</p>
                </div>
                
                {/* Tags */}
                <div style={styles.tagsRow}>
                  {item.matched_traits?.map((trait, idx) => (
                    <span key={idx} style={styles.tagBadge}>{trait}</span>
                  ))}
                  {item.minimum_gwa && (
                    <span style={styles.tagBadgeSecondary}>Min GWA: {item.minimum_gwa}</span>
                  )}
                  {item.recommended_strand && (
                    <span style={styles.tagBadge}>Strand: {item.recommended_strand}</span>
                  )}
                </div>
              </div>
            );
          })}
        </div>

        {/* Footer Actions */}
        <footer style={styles.footer}>
          <h3 style={styles.footerTitle}>How helpful were these recommendations?</h3>
          <p style={styles.footerSubtitle}>Your feedback helps us improve our recommendation engine.</p>
          
          <div style={styles.buttonGroup}>
            <button 
              onClick={() => setShowFeedback({ overall: true })}
              style={styles.primaryBtn}
            >
              💬 Provide Feedback
            </button>
            <button onClick={onRetake} style={styles.secondaryBtn}>
              Retake Assessment
            </button>
            <button onClick={onBack} style={styles.secondaryBtn}>
              Go to Dashboard
            </button>
          </div>
        </footer>
      </main>

      {showFeedback && (
        <FeedbackForm
          recommendation={showFeedback}
          userId={parseInt(userId) || null}
          onSubmit={() => {}}
          onClose={() => setShowFeedback(null)}
        />
      )}
    </div>
  );
}

export default ResultsView;
