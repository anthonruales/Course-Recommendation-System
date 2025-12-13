import React, { useState } from 'react';
import axios from 'axios';
import { useGoogleLogin } from '@react-oauth/google';

function Login({ onSwitch, onLoginSuccess }) {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [showPassword, setShowPassword] = useState(false);

  // REAL GOOGLE LOGIN FUNCTION
  const handleGoogleLogin = useGoogleLogin({
    onSuccess: async (tokenResponse) => {
      try {
        // Fetch user details from Google API using the access token
        const res = await axios.get('https://www.googleapis.com/oauth2/v3/userinfo', {
          headers: { Authorization: `Bearer ${tokenResponse.access_token}` },
        });
        
        // Log the user in with their Google Name
        onLoginSuccess(res.data.name);
      } catch (err) {
        console.error("Google Fetch Error:", err);
        alert("Failed to get user info from Google.");
      }
    },
    onError: () => alert("Google Login Failed. Please check your console settings."),
  });

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post('http://localhost:8080/login', { email, password });
      onLoginSuccess(res.data.user);
    } catch (err) { 
      alert("Invalid login credentials."); 
    }
  };

  return (
    <div className="auth-split-container">
      <div className="auth-visual-side">
        <h1 style={{fontSize: '48px', fontWeight: 800}}>CoursePro</h1>
        <p style={{fontSize: '18px', opacity: 0.8, textAlign: 'center'}}>AI-powered academic track recommendations.</p>
      </div>

      <div className="auth-form-side">
        <h2 style={{fontSize: '32px', fontWeight: 700, marginBottom: '30px'}}>Sign In</h2>
        
        {/* FUNCTIONAL GOOGLE LOGIN BUTTON */}
        <button className="btn-google-auth" onClick={() => handleGoogleLogin()}>
          <img src="https://fonts.gstatic.com/s/i/productlogos/googleg/v6/24px.svg" alt="G" className="google-icon-svg" />
          Continue with Google
        </button>

        <div className="auth-divider">or sign in with email</div>

        <form onSubmit={handleSubmit} style={{width: '100%', maxWidth: '400px'}}>
          <div className="form-group">
            <label>Institutional Email</label>
            <input className="academic-input" type="email" placeholder="name@university.edu" required
                   onChange={(e) => setEmail(e.target.value)} />
          </div>

          <div className="form-group">
            <label>Password</label>
            <div className="input-container-inner">
              <input className="academic-input" type={showPassword ? "text" : "password"} placeholder="••••••••" required
                     onChange={(e) => setPassword(e.target.value)} />
              <button type="button" className="password-toggle-btn" onClick={() => setShowPassword(!showPassword)}>
                {showPassword ? "Hide" : "Show"}
              </button>
            </div>
          </div>

          <button type="submit" className="btn-solid" style={{width: '100%'}}>Login to Portal</button>
        </form>
        
        <p style={{marginTop: '25px', color: '#64748b'}}>
          New here? <span onClick={onSwitch} style={{color: '#1e40af', cursor: 'pointer', fontWeight: 600}}>Create Account</span>
        </p>
      </div>
    </div>
  );
}

export default Login;