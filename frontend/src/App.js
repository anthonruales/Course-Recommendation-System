import React, { useState } from 'react';
import { GoogleOAuthProvider } from '@react-oauth/google';
import Login from './Login';
import Signup from './Signup';
import Dashboard from './Dashboard';
import './App.css';

function App() {
  const [isLogin, setIsLogin] = useState(true);
  const [user, setUser] = useState(localStorage.getItem('userName') || null);

  // YOUR ACTUAL CLIENT ID
  const GOOGLE_CLIENT_ID = "324535586446-nbcj7tcp4373lrk5ct76u3v0od9n4vm3.apps.googleusercontent.com";

  const handleLoginSuccess = (name) => {
    localStorage.setItem('userName', name);
    setUser(name);
  };

  const handleLogout = () => {
    localStorage.removeItem('userName');
    setUser(null);
  };

  return (
    // This provider must wrap everything for the Google Button to work
    <GoogleOAuthProvider clientId={GOOGLE_CLIENT_ID}>
      <div className="App">
        {user ? (
          <Dashboard userName={user} onLogout={handleLogout} />
        ) : (
          <div className="auth-shell">
            {isLogin ? (
              <Login 
                onSwitch={() => setIsLogin(false)} 
                onLoginSuccess={handleLoginSuccess} 
              />
            ) : (
              <Signup 
                onSwitch={() => setIsLogin(true)} 
              />
            )}
          </div>
        )}
      </div>
    </GoogleOAuthProvider>
  );
}

export default App;