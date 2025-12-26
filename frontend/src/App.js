import React, { useState } from 'react';
import { GoogleOAuthProvider } from '@react-oauth/google';
import Login from './Login';
import Signup from './Signup';
import Dashboard from './Dashboard';
import AssessmentForm from './AssessmentForm'; 
import './App.css';

function App() {
  const [isLogin, setIsLogin] = useState(true);
  const [user, setUser] = useState(localStorage.getItem('userName') || null);
  
  // THIS IS THE SWITCH: It can be 'dashboard' or 'assessment'
  const [view, setView] = useState('dashboard');

  const GOOGLE_CLIENT_ID = "324535586446-nbcj7tcp4373lrk5ct76u3v0od9n4vm3.apps.googleusercontent.com";

  const handleLoginSuccess = (name) => {
    localStorage.setItem('userName', name);
    setUser(name);
  };

  const handleLogout = () => {
    localStorage.removeItem('userName');
    setUser(null);
    setView('dashboard');
  };

  return (
    <GoogleOAuthProvider clientId={GOOGLE_CLIENT_ID}>
      <div className="App">
        {user ? (
          /* IF LOGGED IN, CHECK THE VIEW STATE */
          view === 'dashboard' ? (
            <Dashboard 
              userName={user} 
              onLogout={handleLogout} 
              onStart={() => setView('assessment')} /* This flips the switch */
            />
          ) : (
            <AssessmentForm onBack={() => setView('dashboard')} /> /* This flips it back */
          )
        ) : (
          <div className="auth-shell">
            {isLogin ? (
              <Login onSwitch={() => setIsLogin(false)} onLoginSuccess={handleLoginSuccess} />
            ) : (
              <Signup onSwitch={() => setIsLogin(true)} />
            )}
          </div>
        )}
      </div>
    </GoogleOAuthProvider>
  );
}

export default App;