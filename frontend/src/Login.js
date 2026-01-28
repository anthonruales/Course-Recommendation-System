import React, { useState } from 'react';
import axios from 'axios';
import { useGoogleLogin } from '@react-oauth/google';

function Login({ onSwitch, onLoginSuccess }) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [showPassword, setShowPassword] = useState(false);
  const [loading, setLoading] = useState(false);
  
  // Google username selection modal state
  const [showUsernameModal, setShowUsernameModal] = useState(false);
  const [googleUsername, setGoogleUsername] = useState('');
  const [googleUserData, setGoogleUserData] = useState(null);

  const handleGoogleLogin = useGoogleLogin({
    onSuccess: async (tokenResponse) => {
      try {
        setLoading(true);
        const res = await axios.get('https://www.googleapis.com/oauth2/v3/userinfo', {
          headers: { Authorization: `Bearer ${tokenResponse.access_token}` },
        });
        
        // Call backend to check if user exists
        const backendRes = await axios.post('http://localhost:8000/google-login', {
          email: res.data.email,
          name: res.data.name
        });
        
        if (backendRes.data.needs_username) {
          // New user - show username selection modal
          setGoogleUserData({
            email: backendRes.data.email,
            name: backendRes.data.name
          });
          // Suggest username from email
          setGoogleUsername(backendRes.data.email.split('@')[0]);
          setShowUsernameModal(true);
        } else {
          // Existing user - login directly
          localStorage.setItem('userId', backendRes.data.user_id);
          onLoginSuccess(backendRes.data.user, res.data.email);
        }
      } catch (err) {
        console.error('Google login error:', err);
        alert("Google Login Failed: " + (err.response?.data?.detail || err.message));
      } finally {
        setLoading(false);
      }
    },
    onError: () => alert("Google Login Failed."),
  });

  const handleGoogleRegister = async (e) => {
    e.preventDefault();
    
    if (googleUsername.length < 3) {
      alert("Username must be at least 3 characters long.");
      return;
    }
    
    if (!/^[a-zA-Z0-9_]+$/.test(googleUsername)) {
      alert("Username can only contain letters, numbers, and underscores.");
      return;
    }
    
    setLoading(true);
    try {
      const res = await axios.post('http://localhost:8000/google-register', {
        email: googleUserData.email,
        name: googleUserData.name,
        username: googleUsername
      });
      
      localStorage.setItem('userId', res.data.user_id);
      setShowUsernameModal(false);
      onLoginSuccess(res.data.user, googleUserData.email);
    } catch (err) {
      alert(err.response?.data?.detail || "Registration failed. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const res = await axios.post('http://localhost:8000/login', { username, password });
      localStorage.setItem('userId', res.data.user_id);
      onLoginSuccess(res.data.user, username); 
    } catch (err) { 
      alert(err.response?.data?.detail || "Invalid login credentials."); 
    } finally {
      setLoading(false);
    }
  };

  // Username selection modal for Google users
  if (showUsernameModal) {
    return (
      <div style={styles.authWrapper}>
        <div style={styles.glassCard}>
          <img src="/logo.svg" alt="CoursePro" style={styles.brandIcon} />
          
          <h2 style={styles.title}>Choose Username</h2>
          <p style={styles.subtitle}>Create a username for your account</p>
          
          <form onSubmit={handleGoogleRegister}>
            <div style={styles.inputWrapper}>
              <label style={styles.label}>Username</label>
              <input 
                style={styles.input} 
                type="text" 
                placeholder="Enter username"
                value={googleUsername}
                onChange={(e) => setGoogleUsername(e.target.value)}
                required 
              />
            </div>

            <button type="submit" style={styles.loginBtn} disabled={loading}>
              {loading ? "Creating..." : "Continue"}
            </button>
          </form>

          <p style={styles.footerText}>
            <span onClick={() => setShowUsernameModal(false)} style={styles.link}>← Back</span>
          </p>
        </div>
      </div>
    );
  }

  return (
    <div style={styles.authWrapper}>
      <div style={styles.glassCard}>
        <img src="/logo.svg" alt="CoursePro" style={styles.brandIcon} />
        
        <h2 style={styles.title}>Sign In</h2>
        <p style={styles.subtitle}>Welcome back</p>

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
            <label style={styles.label}>Username</label>
            <input 
              style={styles.input} 
              type="text" 
              placeholder="Enter your username"
              onChange={(e) => setUsername(e.target.value)}
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
    width: '64px',
    height: '64px',
    borderRadius: '14px',
    margin: '0 auto 24px',
    objectFit: 'contain'
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