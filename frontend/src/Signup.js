import React, { useState } from 'react';
import axios from 'axios';

function Signup({ onSwitch }) {
  const [formData, setFormData] = useState({
    username: '', 
    email: '',
    password: '',
    confirmPassword: ''
  });
  const [loading, setLoading] = useState(false);
  const [showPassword, setShowPassword] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (formData.password !== formData.confirmPassword) {
      alert("Passwords do not match!");
      return;
    }

    if (formData.password.length < 6) {
      alert("Password must be at least 6 characters long.");
      return;
    }

    setLoading(true);
    try {
      // PATH FIXED: Changed to /signup to match main.py
      // KEYS FIXED: Changed username to fullname to match UserCreate schema
      const response = await axios.post('http://localhost:8000/signup', {
        fullname: formData.username,
        email: formData.email,
        password: formData.password
      });

      if (response.status === 200 || response.status === 201) {
        alert("Account created successfully! Please sign in.");
        onSwitch();
      }
    } catch (err) {
      alert(err.response?.data?.detail || "Registration failed. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={styles.authWrapper}>
      <div style={styles.glassCard}>
        <div style={styles.brandIcon}>C</div>
        
        <h2 style={styles.title}>Create Account</h2>
        <p style={styles.subtitle}>Join CoursePro to find your ideal career path</p>

        <form onSubmit={handleSubmit}>
          <div style={styles.inputWrapper}>
            <label style={styles.label}>Full Name</label>
            <input 
              style={styles.input} 
              type="text" 
              placeholder="Juan Dela Cruz"
              required
              onChange={(e) => setFormData({...formData, username: e.target.value})} 
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
    width: '56px',
    height: '56px',
    background: 'linear-gradient(135deg, #6366f1, #8b5cf6)',
    borderRadius: '14px',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    color: 'white',
    fontSize: '22px',
    fontWeight: '800',
    margin: '0 auto 20px',
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