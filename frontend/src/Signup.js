import React, { useState } from 'react';
import axios from 'axios';
import Toast from './Toast';

function Signup({ onSwitch, onBack }) {
  const [formData, setFormData] = useState({
    username: '',
    fullname: '', 
    email: '',
    password: '',
    confirmPassword: ''
  });
  const [loading, setLoading] = useState(false);
  const [showPassword, setShowPassword] = useState(false);
  const [toast, setToast] = useState(null);

  const showToast = (message, type = 'info') => {
    setToast({ message, type });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (formData.password !== formData.confirmPassword) {
      showToast("Passwords do not match!", "error");
      return;
    }

    if (formData.password.length < 6) {
      showToast("Password must be at least 6 characters long.", "error");
      return;
    }

    if (formData.username.length < 3) {
      showToast("Username must be at least 3 characters long.", "error");
      return;
    }

    if (!/^[a-zA-Z0-9_]+$/.test(formData.username)) {
      showToast("Username can only contain letters, numbers, and underscores.", "error");
      return;
    }

    setLoading(true);
    try {
      const response = await axios.post('http://localhost:8000/signup', {
        username: formData.username,
        fullname: formData.fullname,
        email: formData.email,
        password: formData.password
      });

      if (response.status === 200 || response.status === 201) {
        showToast("✓ Account created successfully! Redirecting to sign in...", "success");
        setTimeout(() => onSwitch(), 2000);
      }
    } catch (err) {
      showToast(err.response?.data?.detail || "Registration failed. Please try again.", "error");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={styles.authWrapper}>
      <div style={styles.bgGradient1}></div>
      <div style={styles.bgGradient2}></div>
      <div style={styles.glassCard}>
        <img src="/logo.svg" alt="CoursePro" style={styles.brandIcon} />
        
        <h2 style={styles.title}>Create Account</h2>
        <p style={styles.subtitle}>Get personalized course recommendations</p>

        <form onSubmit={handleSubmit}>
          <div style={styles.inputWrapper}>
            <label style={styles.label}>Username</label>
            <input 
              style={styles.input} 
              type="text" 
              placeholder="Choose a username"
              required
              onChange={(e) => setFormData({...formData, username: e.target.value})} 
            />
          </div>

          <div style={styles.inputWrapper}>
            <label style={styles.label}>Full Name</label>
            <input 
              style={styles.input} 
              type="text" 
              placeholder="Enter your full name"
              required
              onChange={(e) => setFormData({...formData, fullname: e.target.value})} 
            />
          </div>

          <div style={styles.inputWrapper}>
            <label style={styles.label}>Email Address</label>
            <input 
              style={styles.input} 
              type="email" 
              placeholder="name@example.com"
              required
              onChange={(e) => setFormData({...formData, email: e.target.value})} 
            />
          </div>

          <div style={styles.inputWrapper}>
            <label style={styles.label}>Password</label>
            <div style={{ position: 'relative' }}>
              <input 
                style={styles.input} 
                type={showPassword ? "text" : "password"} 
                placeholder="••••••••"
                required
                onChange={(e) => setFormData({...formData, password: e.target.value})} 
              />
              <button 
                type="button" 
                onClick={() => setShowPassword(!showPassword)}
                style={styles.viewBtn}
              >
                {showPassword ? "HIDE" : "SHOW"}
              </button>
            </div>
          </div>

          <div style={styles.inputWrapper}>
            <label style={styles.label}>Confirm Password</label>
            <div style={{ position: 'relative' }}>
              <input 
                style={styles.input} 
                type={showPassword ? "text" : "password"} 
                placeholder="••••••••"
                required
                onChange={(e) => setFormData({...formData, confirmPassword: e.target.value})} 
              />
               <button 
                type="button" 
                onClick={() => setShowPassword(!showPassword)}
                style={styles.viewBtn}
              >
                {showPassword ? "HIDE" : "SHOW"}
              </button>
            </div>
          </div>

          <button type="submit" style={styles.signupBtn} disabled={loading}
            onMouseEnter={(e) => { if (!loading) { e.target.style.transform = 'translateY(-2px)'; e.target.style.boxShadow = '0 15px 25px rgba(99, 102, 241, 0.5)'; } }}
            onMouseLeave={(e) => { e.target.style.transform = 'translateY(0)'; e.target.style.boxShadow = '0 10px 15px rgba(99, 102, 241, 0.3)'; }}
          >
            {loading ? "Creating Account..." : "Register Now"}
          </button>
        </form>

        <p style={styles.footerText}>
          Already have an account? <span onClick={onSwitch} style={styles.link}>Sign In</span>
        </p>
        
        {onBack && (
          <p style={styles.backLink} onClick={onBack}>
            ← Back to Home
          </p>
        )}
      </div>

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
  authWrapper: {
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    width: '100%',
    minHeight: '100vh',
    padding: '40px 20px',
    background: '#050510',
    position: 'relative',
    overflow: 'hidden'
  },
  bgGradient1: {
    position: 'fixed',
    top: '-50%',
    left: '-50%',
    width: '200%',
    height: '200%',
    background: 'radial-gradient(ellipse at 30% 30%, rgba(99, 102, 241, 0.12) 0%, transparent 55%)',
    pointerEvents: 'none',
    animation: 'breathe 8s ease-in-out infinite'
  },
  bgGradient2: {
    position: 'fixed',
    bottom: '-50%',
    right: '-50%',
    width: '200%',
    height: '200%',
    background: 'radial-gradient(ellipse at 70% 70%, rgba(139, 92, 246, 0.1) 0%, transparent 55%)',
    pointerEvents: 'none',
    animation: 'breathe 8s ease-in-out infinite 2s'
  },
  glassCard: {
    position: 'relative',
    background: 'linear-gradient(145deg, rgba(15, 23, 42, 0.85) 0%, rgba(30, 27, 75, 0.75) 100%)',
    backdropFilter: 'blur(40px)',
    WebkitBackdropFilter: 'blur(40px)',
    border: '1px solid rgba(255, 255, 255, 0.08)',
    borderRadius: '32px',
    padding: '44px 52px',
    width: '100%',
    maxWidth: '440px',
    boxShadow: '0 30px 100px rgba(0, 0, 0, 0.5), 0 0 0 1px rgba(255, 255, 255, 0.03) inset',
    textAlign: 'center',
    zIndex: 1,
    animation: 'slideIn 0.6s cubic-bezier(0.4, 0, 0.2, 1)'
  },
  brandIcon: {
    width: '64px',
    height: '64px',
    borderRadius: '20px',
    margin: '0 auto 24px',
    objectFit: 'contain',
    background: 'linear-gradient(135deg, #6366f1 0%, #8b5cf6 50%, #a855f7 100%)',
    padding: '15px',
    boxShadow: '0 15px 40px rgba(99, 102, 241, 0.35)'
  },
  title: { 
    fontSize: '26px', 
    fontWeight: '700', 
    margin: '0 0 8px', 
    color: '#fff',
    letterSpacing: '-0.5px'
  },
  subtitle: { 
    color: '#64748b', 
    fontSize: '15px', 
    marginBottom: '32px',
    fontWeight: '400'
  },
  inputWrapper: { 
    textAlign: 'left', 
    marginBottom: '18px' 
  },
  label: { 
    display: 'block', 
    fontSize: '11px', 
    fontWeight: '600', 
    color: '#94a3b8', 
    marginBottom: '10px',
    letterSpacing: '0.5px',
    textTransform: 'uppercase'
  },
  input: {
    width: '100%',
    padding: '16px 18px',
    background: 'rgba(15, 23, 42, 0.5)',
    border: '1px solid rgba(255, 255, 255, 0.06)',
    borderRadius: '14px',
    color: '#f1f5f9',
    fontSize: '15px',
    outline: 'none',
    boxSizing: 'border-box',
    transition: 'all 0.3s cubic-bezier(0.4, 0, 0.2, 1)'
  },
  viewBtn: {
    position: 'absolute',
    right: '16px',
    top: '50%',
    transform: 'translateY(-50%)',
    background: 'rgba(99, 102, 241, 0.12)',
    border: 'none',
    color: '#818cf8',
    fontWeight: '700',
    fontSize: '10px',
    cursor: 'pointer',
    letterSpacing: '0.5px',
    padding: '7px 12px',
    borderRadius: '8px',
    transition: 'all 0.3s cubic-bezier(0.4, 0, 0.2, 1)'
  },
  signupBtn: {
    width: '100%',
    padding: '18px 28px',
    background: 'linear-gradient(135deg, #6366f1 0%, #8b5cf6 50%, #a855f7 100%)',
    backgroundSize: '200% 200%',
    color: 'white',
    border: 'none',
    borderRadius: '16px',
    fontWeight: '600',
    fontSize: '16px',
    cursor: 'pointer',
    marginTop: '14px',
    boxShadow: '0 10px 35px rgba(99, 102, 241, 0.35)',
    transition: 'all 0.35s cubic-bezier(0.4, 0, 0.2, 1)',
    letterSpacing: '0.3px'
  },
  footerText: { 
    marginTop: '28px', 
    color: '#64748b', 
    fontSize: '15px' 
  },
  link: { 
    color: '#a5b4fc', 
    fontWeight: '600', 
    cursor: 'pointer', 
    marginLeft: '6px',
    transition: 'color 0.3s cubic-bezier(0.4, 0, 0.2, 1)'
  },
  backLink: {
    marginTop: '16px',
    color: '#64748b',
    fontSize: '14px',
    cursor: 'pointer',
    transition: 'color 0.3s ease',
  }
};

export default Signup;