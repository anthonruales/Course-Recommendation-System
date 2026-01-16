import React, { useState } from 'react';
import axios from 'axios';
import { useGoogleLogin } from '@react-oauth/google';

function Login({ onSwitch, onLoginSuccess }) {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [showPassword, setShowPassword] = useState(false);
  const [loading, setLoading] = useState(false);

  const handleGoogleLogin = useGoogleLogin({
    onSuccess: async (tokenResponse) => {
      try {
        setLoading(true);
        const res = await axios.get('https://www.googleapis.com/oauth2/v3/userinfo', {
          headers: { Authorization: `Bearer ${tokenResponse.access_token}` },
        });
        
        // Call backend to create/login Google user
        const backendRes = await axios.post('http://localhost:8000/google-login', {
          email: res.data.email,
          name: res.data.name
        });
        
        // Store userId in localStorage
        localStorage.setItem('userId', backendRes.data.user_id);
        onLoginSuccess(backendRes.data.user, res.data.email);
      } catch (err) {
        console.error('Google login error:', err);
        alert("Google Login Failed: " + (err.response?.data?.detail || err.message));
      } finally {
        setLoading(false);
      }
    },
    onError: () => alert("Google Login Failed."),
  });

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const res = await axios.post('http://localhost:8000/login', { email, password });
      localStorage.setItem('userId', res.data.user_id);
      onLoginSuccess(res.data.user, email); 
    } catch (err) { 
      alert(err.response?.data?.detail || "Invalid login credentials."); 
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={styles.authWrapper}>
      <div style={styles.glassCard}>
        <div style={styles.brandIcon}>C</div>
        
        <h2 style={styles.title}>Sign In</h2>
        <p style={styles.subtitle}>Welcome back to CoursePro AI</p>

        <button 
          style={styles.googleBtn} 
          onClick={() => handleGoogleLogin()}
          disabled={loading}
          onMouseEnter={(e) => { if (!loading) { e.target.style.transform = 'translateY(-2px)'; e.target.style.boxShadow = '0 10px 20px rgba(0, 0, 0, 0.15)'; } }}
          onMouseLeave={(e) => { e.target.style.transform = 'translateY(0)'; e.target.style.boxShadow = 'none'; }}
        >
          <img src="https://fonts.gstatic.com/s/i/productlogos/googleg/v6/24px.svg" alt="G" style={{width: 18}} />
          <span>Continue with Google</span>
        </button>

        <div style={styles.divider}>
          <div style={styles.line}></div>
          <span style={styles.dividerText}>OR</span>
          <div style={styles.line}></div>
        </div>

        <form onSubmit={handleSubmit}>
          <div style={styles.inputWrapper}>
            <label style={styles.label}>Email Address</label>
            <input 
              style={styles.input} 
              type="email" 
              placeholder="name@example.com"
              onChange={(e) => setEmail(e.target.value)}
              required 
            />
          </div>

          <div style={styles.inputWrapper}>
            <label style={styles.label}>Password</label>
            <div style={{ position: 'relative' }}>
              <input 
                style={styles.input} 
                type={showPassword ? "text" : "password"} 
                placeholder="••••••••"
                onChange={(e) => setPassword(e.target.value)}
                required 
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

          <button type="submit" style={styles.loginBtn} disabled={loading}
            onMouseEnter={(e) => { if (!loading) { e.target.style.transform = 'translateY(-2px)'; e.target.style.boxShadow = '0 15px 25px rgba(99, 102, 241, 0.5)'; } }}
            onMouseLeave={(e) => { e.target.style.transform = 'translateY(0)'; e.target.style.boxShadow = '0 10px 15px rgba(99, 102, 241, 0.3)'; }}
          >
            {loading ? "Verifying..." : "Login to Portal"}
          </button>
        </form>

        <p style={styles.footerText}>
          New here? <span onClick={onSwitch} style={styles.link}>Create Account</span>
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
    // TRANSPARENT GLASS
    background: 'rgba(255, 255, 255, 0.05)', 
    backdropFilter: 'blur(20px) saturate(180%)', // Makes background "shine" through blurred
    WebkitBackdropFilter: 'blur(20px) saturate(180%)',
    border: '1px solid rgba(255, 255, 255, 0.15)', // Light border to define the box
    borderRadius: '28px',
    padding: '60px 70px', 
    width: '540px', // Large Boxy Size
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
    margin: '0 auto 24px',
  },
  title: { fontSize: '32px', fontWeight: '700', color: 'white', margin: '0 0 10px' },
  subtitle: { color: 'rgba(255,255,255,0.6)', fontSize: '15px', marginBottom: '35px' },
  googleBtn: {
    width: '100%',
    padding: '14px',
    borderRadius: '14px',
    border: 'none',
    background: 'white',
    color: '#1e293b',
    fontWeight: '600',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    gap: '12px',
    cursor: 'pointer',
    marginBottom: '20px',
    transition: 'all 0.3s ease'
  },
  divider: { display: 'flex', alignItems: 'center', gap: '15px', margin: '25px 0' },
  line: { flex: 1, height: '1px', background: 'rgba(255,255,255,0.2)' },
  dividerText: { color: 'rgba(255,255,255,0.4)', fontSize: '11px', fontWeight: '800' },
  inputWrapper: { textAlign: 'left', marginBottom: '20px' },
  label: { display: 'block', fontSize: '13px', fontWeight: '600', color: 'rgba(255,255,255,0.8)', marginBottom: '8px', marginLeft: '4px' },
  input: {
    width: '100%',
    padding: '16px',
    // GLASS INPUTS
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
    fontSize: '11px',
    cursor: 'pointer'
  },
  loginBtn: {
    width: '100%',
    padding: '16px',
    background: '#6366f1',
    color: 'white',
    border: 'none',
    borderRadius: '12px',
    fontWeight: '700',
    fontSize: '16px',
    cursor: 'pointer',
    marginTop: '10px',
    boxShadow: '0 10px 15px rgba(99, 102, 241, 0.3)',
    transition: 'all 0.3s ease'
  },
  footerText: { marginTop: '30px', color: 'rgba(255,255,255,0.5)', fontSize: '14px' },
  link: { color: '#818cf8', fontWeight: '700', cursor: 'pointer', marginLeft: '5px' }
};

export default Login;