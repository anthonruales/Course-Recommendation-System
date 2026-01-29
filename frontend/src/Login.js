import React, { useState } from 'react';
import axios from 'axios';
import { useGoogleLogin } from '@react-oauth/google';

function Login({ onSwitch, onLoginSuccess, onBack }) {
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
          localStorage.setItem('userUsername', backendRes.data.username || '');
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
      localStorage.setItem('userUsername', googleUsername);
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
      localStorage.setItem('userUsername', res.data.username || username);
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
        <div style={styles.bgGradient1}></div>
        <div style={styles.bgGradient2}></div>
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
      <div style={styles.bgGradient1}></div>
      <div style={styles.bgGradient2}></div>
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
        
        {onBack && (
          <p style={styles.backLink} onClick={onBack}>
            ← Back to Home
          </p>
        )}
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
    padding: '52px 56px',
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
    margin: '0 auto 28px',
    objectFit: 'contain',
    background: 'linear-gradient(135deg, #6366f1 0%, #8b5cf6 50%, #a855f7 100%)',
    padding: '15px',
    boxShadow: '0 15px 40px rgba(99, 102, 241, 0.35)'
  },
  title: { 
    fontSize: '28px', 
    fontWeight: '700', 
    color: '#fff', 
    margin: '0 0 8px',
    letterSpacing: '-0.5px'
  },
  subtitle: { 
    color: '#64748b', 
    fontSize: '15px', 
    marginBottom: '36px',
    fontWeight: '400'
  },
  googleBtn: {
    width: '100%',
    padding: '16px 22px',
    borderRadius: '16px',
    border: '1px solid rgba(255, 255, 255, 0.08)',
    background: 'rgba(255, 255, 255, 0.03)',
    color: '#e2e8f0',
    fontWeight: '500',
    fontSize: '15px',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    gap: '14px',
    cursor: 'pointer',
    marginBottom: '28px',
    transition: 'all 0.35s cubic-bezier(0.4, 0, 0.2, 1)',
    backdropFilter: 'blur(10px)'
  },
  divider: { 
    display: 'flex', 
    alignItems: 'center', 
    gap: '18px', 
    margin: '28px 0' 
  },
  line: { 
    flex: 1, 
    height: '1px', 
    background: 'linear-gradient(90deg, transparent, rgba(255,255,255,0.08), transparent)' 
  },
  dividerText: { 
    color: '#475569', 
    fontSize: '11px', 
    fontWeight: '600',
    textTransform: 'uppercase',
    letterSpacing: '2px'
  },
  inputWrapper: { 
    textAlign: 'left', 
    marginBottom: '20px' 
  },
  label: { 
    display: 'block', 
    fontSize: '12px', 
    fontWeight: '600', 
    color: '#94a3b8', 
    marginBottom: '10px',
    letterSpacing: '0.5px',
    textTransform: 'uppercase'
  },
  input: {
    width: '100%',
    padding: '16px 20px',
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
  loginBtn: {
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
    marginTop: '32px', 
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

export default Login;