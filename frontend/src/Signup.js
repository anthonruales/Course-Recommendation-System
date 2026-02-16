import React, { useState } from 'react';
import axios from 'axios'; // This fixes the 'axios' is not defined error

// Email validation function - ensures proper format with dot in domain
const validateEmail = (email) => {
  // Regex requires: text@domain.tld (must have dot in domain part)
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
};

function Signup({ onSwitch }) { // This fixes the 'onSwitch' is not defined error
  const [formData, setFormData] = useState({ fullname: '', email: '', password: '' });
  const [showPassword, setShowPassword] = useState(false);
  const [emailError, setEmailError] = useState('');

  // The handleSubmit MUST be inside the Signup function
  const handleSubmit = async (e) => {
    e.preventDefault();
    
    // Validate email format before submitting
    if (!validateEmail(formData.email)) {
      setEmailError('Please enter a valid email address (e.g., name@gmail.com)');
      return;
    }
    setEmailError('');
    
    console.log("Sending data:", formData); 
    try {
      const response = await axios.post('http://localhost:8000/signup', {
        fullname: formData.fullname,
        email: formData.email,
        password: formData.password
      });
      console.log(response.data); // Using response to clear the warning
      alert("Registration Successful!"); 
      onSwitch();
    } catch (err) {
      console.error("Signup Error Details:", err.response?.data);
      alert(err.response?.data?.detail || "Error during signup.");
    }
  };

  return (
    <div className="auth-split-container">
      <div className="auth-visual-side">
        <h1 style={{fontSize: '48px', fontWeight: 800}}>CoursePro</h1>
        <p style={{fontSize: '18px', opacity: 0.8}}>Join thousands of successful students.</p>
      </div>

      <div className="auth-form-side">
        <h2 style={{fontSize: '32px', fontWeight: 700, marginBottom: '30px'}}>Create Account</h2>
        <form onSubmit={handleSubmit} style={{width: '100%', maxWidth: '400px'}}>
          <div className="form-group">
            <label>Full Name</label>
            <input className="academic-input" type="text" placeholder="Name" required
                   onChange={(e) => setFormData({...formData, fullname: e.target.value})} />
          </div>
          <div className="form-group">
            <label>Email Address</label>
            <input 
              className="academic-input" 
              type="email" 
              placeholder="email@example.com" 
              required
              value={formData.email}
              onChange={(e) => {
                setFormData({...formData, email: e.target.value});
                // Clear error when user starts typing
                if (emailError) setEmailError('');
              }}
              onBlur={() => {
                // Validate on blur
                if (formData.email && !validateEmail(formData.email)) {
                  setEmailError('Please enter a valid email address (e.g., name@gmail.com)');
                }
              }}
              style={emailError ? {borderColor: '#ef4444'} : {}}
            />
            {emailError && <p style={{color: '#ef4444', fontSize: '12px', marginTop: '4px'}}>{emailError}</p>}
          </div>
          <div className="form-group">
            <label>Password</label>
            <div className="input-container-inner">
              <input className="academic-input" type={showPassword ? "text" : "password"} placeholder="••••••••" required
                     onChange={(e) => setFormData({...formData, password: e.target.value})} />
              <button type="button" className="password-toggle-btn" onClick={() => setShowPassword(!showPassword)}>
                {showPassword ? "Hide" : "Show"}
              </button>
            </div>
          </div>
          <button type="submit" className="btn-solid" style={{width: '100%'}}>Register Student</button>
        </form>
        <p style={{marginTop: '25px'}}>Already registered? <span onClick={onSwitch} style={{color: '#1e40af', cursor: 'pointer', fontWeight: 600}}>Log In</span></p>
      </div>
    </div>
  );
}

export default Signup;