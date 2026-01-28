import React, { useState } from 'react';
import axios from 'axios';
import Toast from './Toast';

function Signup({ onSwitch }) {
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
    padding: '20px'
  },
  glassCard: {
    background: 'rgba(255, 255, 255, 0.05)', 
    backdropFilter: 'blur(20px) saturate(180%)',
    WebkitBackdropFilter: 'blur(20px) saturate(180%)',
    border: '1px solid rgba(255, 255, 255, 0.15)',
    borderRadius: '28px',
    padding: '50px 70px',
    width: '540px',
    boxShadow: '0 25px 50px -12px rgba(0,0,0,0.5)',
    textAlign: 'center',
    boxSizing: 'border-box'
  },
  brandIcon: {
    width: '64px',
    height: '64px',
    borderRadius: '14px',
    margin: '0 auto 20px',
    objectFit: 'contain'
  },
  title: { fontSize: '32px', fontWeight: '700', margin: '0 0 10px', color: 'white' },
  subtitle: { color: 'rgba(255,255,255,0.6)', fontSize: '15px', marginBottom: '30px' },
  inputWrapper: { textAlign: 'left', marginBottom: '18px' },
  label: { display: 'block', fontSize: '13px', fontWeight: '600', color: 'rgba(255,255,255,0.8)', marginBottom: '8px', marginLeft: '4px' },
  input: {
    width: '100%',
    padding: '16px',
    background: 'rgba(255, 255, 255, 0.03)',
    border: '1px solid rgba(255, 255, 255, 0.1)',
    borderRadius: '12px',
    color: 'white',
    fontSize: '15px',
    outline: 'none',
    boxSizing: 'border-box',
    transition: 'all 0.3s ease'
  },
  viewBtn: {
    position: 'absolute',
    right: '12px',
    top: '50%',
    transform: 'translateY(-50%)',
    background: 'none',
    border: 'none',
    color: '#818cf8',
    fontWeight: '700',
    fontSize: '10px',
    cursor: 'pointer'
  },
  signupBtn: {
    width: '100%',
    padding: '16px',
    background: '#6366f1',
    color: 'white',
    border: 'none',
    borderRadius: '12px',
    fontWeight: '700',
    fontSize: '16px',
    cursor: 'pointer',
    marginTop: '15px',
    boxShadow: '0 10px 15px rgba(99, 102, 241, 0.3)',
    transition: 'all 0.3s ease'
  },
  footerText: { marginTop: '25px', color: 'rgba(255,255,255,0.5)', fontSize: '14px' },
  link: { color: '#818cf8', fontWeight: '700', cursor: 'pointer', marginLeft: '5px' }
};

export default Signup;