import React, { useState, useEffect } from 'react';

/**
 * LANDING PAGE
 * Beautiful hero page for CoursePro
 */
function LandingPage({ onLogin, onSignup }) {
  const [scrolled, setScrolled] = useState(false);
  
  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 50);
    };
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const features = [
    {
      icon: '🎯',
      title: 'Smart Course Matching',
      description: 'Our system analyzes your interests, skills, and academic profile to find courses that fit you best.'
    },
    {
      icon: '📊',
      title: 'Adaptive Assessment',
      description: 'Answer questions that adapt to your responses for more accurate and personalized recommendations.'
    },
    {
      icon: '🎓',
      title: 'College Course Database',
      description: 'Explore various college courses with detailed information about career opportunities.'
    },
    {
      icon: '✨',
      title: 'Personalized Results',
      description: 'Get recommendations tailored to your unique personality traits and academic background.'
    }
  ];



  return (
    <div style={styles.pageWrapper}>
      {/* Animated Background */}
      <div style={styles.bgGradient} />
      <div style={styles.bgOrbs}>
        <div style={styles.orb1} />
        <div style={styles.orb2} />
        <div style={styles.orb3} />
      </div>

      {/* Navigation */}
      <nav style={{
        ...styles.navbar,
        background: scrolled ? 'rgba(5, 5, 16, 0.95)' : 'transparent',
        borderBottom: scrolled ? '1px solid rgba(255,255,255,0.05)' : 'none',
      }}>
        <div style={styles.navContainer}>
          <div style={styles.navBrand}>
            <img src="/logo.png" alt="CoursePro" style={styles.navLogo} />
            <span style={styles.navBrandName}>CoursePro</span>
          </div>
          
          <div style={styles.navLinks}>
            <a href="#features" style={styles.navLink}>Features</a>
            <a href="#how-it-works" style={styles.navLink}>How It Works</a>
          </div>

          <div style={styles.navRight}>
            <button onClick={onLogin} style={styles.signInBtn}>
              Sign In
            </button>
            <button onClick={onSignup} style={styles.getStartedBtn}>
              Get Started
              <span style={styles.btnArrow}>→</span>
            </button>
          </div>
        </div>
      </nav>

      {/* Hero Section */}
      <section style={styles.heroSection}>
        <div style={styles.heroContent}>
          <div style={styles.heroBadge}>
            <span style={styles.badgeDot} />
            AI-Powered Course Matching
            <span style={styles.badgeArrow}>→</span>
          </div>
          
          <h1 style={styles.heroTitle}>
            Find Your
            <br />
            <span className="gradient-text" style={styles.heroGradient}>Perfect Career Path</span>
          </h1>
          
          <p style={styles.heroSubtitle}>
            Not sure what course to take? Take our quick assessment to discover 
            your strengths and interests, then get matched with college courses 
            that fit your goals.
          </p>

          <div style={styles.heroCTA}>
            <button onClick={onSignup} style={styles.primaryBtn}>
              Start Assessment
              <span style={styles.btnArrow}>→</span>
            </button>
            <button onClick={onLogin} style={styles.secondaryBtn}>
              I Have an Account
            </button>
          </div>

          <p style={styles.heroNote}>
            ✨ Free to use • Quick and easy • Get results in minutes
          </p>
        </div>
      </section>

      {/* Features Section */}
      <section id="features" style={styles.featuresSection}>
        <div style={styles.sectionHeader}>
          <span style={styles.sectionBadge}>Features</span>
          <h2 style={styles.sectionTitle}>
            How CoursePro <span style={styles.highlight}>helps you</span>
          </h2>
          <p style={styles.sectionSubtitle}>
            Our system considers your interests, skills, and academic background to suggest the right courses for you
          </p>
        </div>

        <div style={styles.featuresGrid}>
          {features.map((feature, index) => (
            <div 
              key={index} 
              style={styles.featureCard}
              onMouseEnter={(e) => {
                e.currentTarget.style.transform = 'translateY(-8px)';
                e.currentTarget.style.borderColor = 'rgba(99, 102, 241, 0.3)';
                e.currentTarget.style.boxShadow = '0 20px 40px rgba(99, 102, 241, 0.15)';
              }}
              onMouseLeave={(e) => {
                e.currentTarget.style.transform = 'translateY(0)';
                e.currentTarget.style.borderColor = 'rgba(255,255,255,0.06)';
                e.currentTarget.style.boxShadow = '0 10px 30px rgba(0,0,0,0.2)';
              }}
            >
              <div style={styles.featureIcon}>{feature.icon}</div>
              <h3 style={styles.featureTitle}>{feature.title}</h3>
              <p style={styles.featureDesc}>{feature.description}</p>
            </div>
          ))}
        </div>
      </section>

      {/* How It Works Section */}
      <section id="how-it-works" style={styles.howSection}>
        <div style={styles.sectionHeader}>
          <span style={styles.sectionBadge}>How It Works</span>
          <h2 style={styles.sectionTitle}>
            Three simple steps to your <span style={styles.highlight}>future career</span>
          </h2>
        </div>

        <div style={styles.stepsContainer}>
          <div style={styles.stepCard}>
            <div style={styles.stepNumber}>1</div>
            <h3 style={styles.stepTitle}>Create Your Profile</h3>
            <p style={styles.stepDesc}>Enter your academic information, including your GWA and SHS strand.</p>
          </div>
          <div style={styles.stepConnector}>
            <div style={styles.connectorLine} />
          </div>
          <div style={styles.stepCard}>
            <div style={styles.stepNumber}>2</div>
            <h3 style={styles.stepTitle}>Take the Assessment</h3>
            <p style={styles.stepDesc}>Answer questions that adapt to your responses for accurate trait detection.</p>
          </div>
          <div style={styles.stepConnector}>
            <div style={styles.connectorLine} />
          </div>
          <div style={styles.stepCard}>
            <div style={styles.stepNumber}>3</div>
            <h3 style={styles.stepTitle}>Get Recommendations</h3>
            <p style={styles.stepDesc}>Receive personalized course matches based on your unique profile.</p>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section style={styles.ctaSection}>
        <div style={styles.ctaCard}>
          <h2 style={styles.ctaTitle}>Ready to find the right course for you?</h2>
          <p style={styles.ctaSubtitle}>
            Take our assessment and get personalized course recommendations
          </p>
          <button onClick={onSignup} style={styles.ctaButton}>
            Get Started Now
            <span style={styles.btnArrow}>→</span>
          </button>
        </div>
      </section>

      {/* Footer */}
      <footer style={styles.footer}>
        <div style={styles.footerContent}>
          <div style={styles.footerBrand}>
            <img src="/logo.png" alt="CoursePro" style={styles.footerLogo} />
            <span style={styles.footerBrandName}>CoursePro</span>
          </div>
          <p style={styles.footerText}>
            AI-Powered Course Recommendation System
          </p>
          <p style={styles.footerCopyright}>
            © 2026 CoursePro. All rights reserved.
          </p>
        </div>
      </footer>

      {/* Inject keyframe animations */}
      <style>{`
        @keyframes float {
          0%, 100% { transform: translateY(0) rotate(0deg); }
          50% { transform: translateY(-20px) rotate(5deg); }
        }
        @keyframes pulse {
          0%, 100% { opacity: 0.5; transform: scale(1); }
          50% { opacity: 0.8; transform: scale(1.05); }
        }
        @keyframes shimmer {
          0% { background-position: -200% 0; }
          100% { background-position: 200% 0; }
        }
      `}</style>
    </div>
  );
}

const styles = {
  pageWrapper: {
    minHeight: '100vh',
    background: '#050510',
    color: 'white',
    position: 'relative',
    overflow: 'hidden',
  },
  
  // Background effects
  bgGradient: {
    position: 'absolute',
    top: 0,
    left: 0,
    right: 0,
    height: '100vh',
    background: 'radial-gradient(ellipse 80% 50% at 50% -20%, rgba(99, 102, 241, 0.15) 0%, transparent 50%)',
    pointerEvents: 'none',
  },
  bgOrbs: {
    position: 'absolute',
    top: 0,
    left: 0,
    right: 0,
    bottom: 0,
    overflow: 'hidden',
    pointerEvents: 'none',
  },
  orb1: {
    position: 'absolute',
    top: '10%',
    right: '10%',
    width: '400px',
    height: '400px',
    borderRadius: '50%',
    background: 'radial-gradient(circle, rgba(139, 92, 246, 0.1) 0%, transparent 70%)',
    animation: 'float 8s ease-in-out infinite',
  },
  orb2: {
    position: 'absolute',
    bottom: '20%',
    left: '5%',
    width: '300px',
    height: '300px',
    borderRadius: '50%',
    background: 'radial-gradient(circle, rgba(99, 102, 241, 0.08) 0%, transparent 70%)',
    animation: 'float 10s ease-in-out infinite reverse',
  },
  orb3: {
    position: 'absolute',
    top: '50%',
    left: '50%',
    width: '500px',
    height: '500px',
    borderRadius: '50%',
    background: 'radial-gradient(circle, rgba(168, 85, 247, 0.05) 0%, transparent 70%)',
    animation: 'pulse 6s ease-in-out infinite',
  },

  // Navbar
  navbar: {
    position: 'fixed',
    top: 0,
    left: 0,
    right: 0,
    zIndex: 1000,
    padding: '16px 0',
    backdropFilter: 'blur(20px)',
    transition: 'all 0.4s cubic-bezier(0.4, 0, 0.2, 1)',
  },
  navContainer: {
    maxWidth: '1200px',
    margin: '0 auto',
    padding: '0 48px',
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
    fontSize: '22px',
    fontWeight: '700',
    background: 'linear-gradient(135deg, #f8fafc 0%, #94a3b8 100%)',
    WebkitBackgroundClip: 'text',
    WebkitTextFillColor: 'transparent',
  },
  navLinks: {
    display: 'flex',
    gap: '40px',
  },
  navLink: {
    color: '#94a3b8',
    textDecoration: 'none',
    fontSize: '15px',
    fontWeight: '500',
    transition: 'color 0.3s ease',
    cursor: 'pointer',
  },
  navRight: {
    display: 'flex',
    gap: '12px',
    alignItems: 'center',
  },
  signInBtn: {
    background: 'transparent',
    border: '1px solid rgba(255,255,255,0.15)',
    color: '#e2e8f0',
    padding: '10px 24px',
    borderRadius: '10px',
    fontSize: '14px',
    fontWeight: '600',
    cursor: 'pointer',
    transition: 'all 0.3s ease',
  },
  getStartedBtn: {
    background: 'linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%)',
    border: 'none',
    color: 'white',
    padding: '10px 24px',
    borderRadius: '10px',
    fontSize: '14px',
    fontWeight: '600',
    cursor: 'pointer',
    display: 'flex',
    alignItems: 'center',
    gap: '8px',
    transition: 'all 0.3s ease',
    boxShadow: '0 4px 20px rgba(99, 102, 241, 0.3)',
  },
  btnArrow: {
    fontSize: '16px',
    transition: 'transform 0.3s ease',
  },

  // Hero Section
  heroSection: {
    minHeight: '100vh',
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'center',
    alignItems: 'center',
    padding: '120px 48px 80px',
    textAlign: 'center',
    position: 'relative',
  },
  heroContent: {
    maxWidth: '800px',
  },
  heroBadge: {
    display: 'inline-flex',
    alignItems: 'center',
    gap: '12px',
    background: 'rgba(15, 23, 42, 0.8)',
    border: '1px solid rgba(255,255,255,0.1)',
    borderRadius: '50px',
    padding: '12px 24px',
    fontSize: '14px',
    color: '#e2e8f0',
    fontWeight: '500',
    marginBottom: '32px',
    backdropFilter: 'blur(10px)',
  },
  badgeDot: {
    width: '8px',
    height: '8px',
    background: '#22c55e',
    borderRadius: '50%',
    boxShadow: '0 0 10px #22c55e',
  },
  badgeArrow: {
    color: '#64748b',
  },
  heroTitle: {
    fontSize: '72px',
    fontWeight: '800',
    lineHeight: '1.1',
    marginBottom: '28px',
    letterSpacing: '-2px',
  },
  heroGradient: {
    fontSize: '72px',
    fontWeight: '800',
  },
  heroSubtitle: {
    fontSize: '20px',
    color: '#94a3b8',
    lineHeight: '1.7',
    marginBottom: '40px',
    maxWidth: '600px',
    margin: '0 auto 40px',
  },
  heroCTA: {
    display: 'flex',
    gap: '16px',
    justifyContent: 'center',
    marginBottom: '32px',
  },
  primaryBtn: {
    background: 'linear-gradient(135deg, #6366f1 0%, #8b5cf6 50%, #a855f7 100%)',
    border: 'none',
    color: 'white',
    padding: '16px 32px',
    borderRadius: '14px',
    fontSize: '16px',
    fontWeight: '600',
    cursor: 'pointer',
    display: 'flex',
    alignItems: 'center',
    gap: '10px',
    transition: 'all 0.4s cubic-bezier(0.4, 0, 0.2, 1)',
    boxShadow: '0 8px 30px rgba(99, 102, 241, 0.4)',
  },
  secondaryBtn: {
    background: 'rgba(255,255,255,0.05)',
    border: '1px solid rgba(255,255,255,0.1)',
    color: '#e2e8f0',
    padding: '16px 32px',
    borderRadius: '14px',
    fontSize: '16px',
    fontWeight: '600',
    cursor: 'pointer',
    transition: 'all 0.3s ease',
    backdropFilter: 'blur(10px)',
  },
  heroNote: {
    color: '#64748b',
    fontSize: '14px',
  },

  // Features Section
  featuresSection: {
    padding: '120px 48px',
    maxWidth: '1200px',
    margin: '0 auto',
  },
  sectionHeader: {
    textAlign: 'center',
    marginBottom: '64px',
  },
  sectionBadge: {
    display: 'inline-block',
    background: 'rgba(99, 102, 241, 0.1)',
    border: '1px solid rgba(99, 102, 241, 0.2)',
    color: '#a5b4fc',
    padding: '8px 20px',
    borderRadius: '50px',
    fontSize: '13px',
    fontWeight: '600',
    marginBottom: '20px',
    textTransform: 'uppercase',
    letterSpacing: '1px',
  },
  sectionTitle: {
    fontSize: '42px',
    fontWeight: '700',
    marginBottom: '16px',
    letterSpacing: '-1px',
  },
  highlight: {
    background: 'linear-gradient(135deg, #6366f1 0%, #a855f7 100%)',
    WebkitBackgroundClip: 'text',
    WebkitTextFillColor: 'transparent',
  },
  sectionSubtitle: {
    color: '#64748b',
    fontSize: '18px',
    maxWidth: '600px',
    margin: '0 auto',
  },
  featuresGrid: {
    display: 'grid',
    gridTemplateColumns: 'repeat(2, 1fr)',
    gap: '24px',
  },
  featureCard: {
    background: 'rgba(15, 23, 42, 0.5)',
    border: '1px solid rgba(255,255,255,0.06)',
    borderRadius: '24px',
    padding: '36px',
    transition: 'all 0.4s cubic-bezier(0.4, 0, 0.2, 1)',
    backdropFilter: 'blur(20px)',
    boxShadow: '0 10px 30px rgba(0,0,0,0.2)',
    cursor: 'default',
  },
  featureIcon: {
    fontSize: '40px',
    marginBottom: '20px',
  },
  featureTitle: {
    fontSize: '20px',
    fontWeight: '600',
    marginBottom: '12px',
    color: '#f1f5f9',
  },
  featureDesc: {
    color: '#94a3b8',
    fontSize: '15px',
    lineHeight: '1.6',
  },

  // How It Works Section
  howSection: {
    padding: '120px 48px',
    background: 'linear-gradient(180deg, transparent 0%, rgba(99, 102, 241, 0.03) 50%, transparent 100%)',
  },
  stepsContainer: {
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    gap: '0',
    maxWidth: '1000px',
    margin: '0 auto',
  },
  stepCard: {
    background: 'rgba(15, 23, 42, 0.6)',
    border: '1px solid rgba(255,255,255,0.06)',
    borderRadius: '24px',
    padding: '40px 32px',
    textAlign: 'center',
    width: '280px',
    backdropFilter: 'blur(20px)',
  },
  stepNumber: {
    width: '56px',
    height: '56px',
    background: 'linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%)',
    borderRadius: '16px',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    fontSize: '24px',
    fontWeight: '700',
    margin: '0 auto 20px',
    boxShadow: '0 8px 25px rgba(99, 102, 241, 0.3)',
  },
  stepTitle: {
    fontSize: '18px',
    fontWeight: '600',
    marginBottom: '12px',
    color: '#f1f5f9',
  },
  stepDesc: {
    color: '#94a3b8',
    fontSize: '14px',
    lineHeight: '1.6',
  },
  stepConnector: {
    width: '60px',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
  },
  connectorLine: {
    width: '100%',
    height: '2px',
    background: 'linear-gradient(90deg, rgba(99, 102, 241, 0.5), rgba(168, 85, 247, 0.5))',
  },

  // CTA Section
  ctaSection: {
    padding: '80px 48px 120px',
    display: 'flex',
    justifyContent: 'center',
  },
  ctaCard: {
    background: 'linear-gradient(135deg, rgba(99, 102, 241, 0.15) 0%, rgba(139, 92, 246, 0.1) 100%)',
    border: '1px solid rgba(99, 102, 241, 0.2)',
    borderRadius: '32px',
    padding: '64px 80px',
    textAlign: 'center',
    maxWidth: '700px',
    backdropFilter: 'blur(20px)',
  },
  ctaTitle: {
    fontSize: '36px',
    fontWeight: '700',
    marginBottom: '16px',
    letterSpacing: '-0.5px',
  },
  ctaSubtitle: {
    color: '#94a3b8',
    fontSize: '18px',
    marginBottom: '32px',
  },
  ctaButton: {
    background: 'linear-gradient(135deg, #6366f1 0%, #8b5cf6 50%, #a855f7 100%)',
    border: 'none',
    color: 'white',
    padding: '18px 40px',
    borderRadius: '14px',
    fontSize: '17px',
    fontWeight: '600',
    cursor: 'pointer',
    display: 'inline-flex',
    alignItems: 'center',
    gap: '10px',
    transition: 'all 0.4s cubic-bezier(0.4, 0, 0.2, 1)',
    boxShadow: '0 8px 30px rgba(99, 102, 241, 0.4)',
  },

  // Footer
  footer: {
    padding: '48px',
    borderTop: '1px solid rgba(255,255,255,0.05)',
    textAlign: 'center',
  },
  footerContent: {
    maxWidth: '1200px',
    margin: '0 auto',
  },
  footerBrand: {
    display: 'inline-flex',
    alignItems: 'center',
    gap: '10px',
    marginBottom: '16px',
  },
  footerLogo: {
    width: '44px',
    height: '44px',
    objectFit: 'cover',
    borderRadius: '10px',
    background: 'linear-gradient(135deg, rgba(99, 102, 241, 0.15) 0%, rgba(139, 92, 246, 0.15) 100%)',
    padding: '0',
    boxShadow: '0 0 15px rgba(99, 102, 241, 0.4), 0 0 30px rgba(139, 92, 246, 0.2)',
    border: '1px solid rgba(139, 92, 246, 0.3)',
  },
  footerBrandName: {
    fontSize: '18px',
    fontWeight: '700',
    color: '#e2e8f0',
  },
  footerText: {
    color: '#64748b',
    fontSize: '14px',
    marginBottom: '8px',
  },
  footerCopyright: {
    color: '#475569',
    fontSize: '13px',
  },
};

export default LandingPage;
