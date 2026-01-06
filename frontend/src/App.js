import React, { useState, useEffect } from 'react';
import { GoogleOAuthProvider } from '@react-oauth/google';
import Login from './Login';
import Signup from './Signup';
import Dashboard from './Dashboard';
import ProfileForm from './ProfileForm';
import AssessmentForm from './AssessmentForm';
import Admin from './admin/Admin'; // Correct based on your folder structure
import './App.css';

function App() {
  const [isLogin, setIsLogin] = useState(true);

  // Temporary lang yang 15 at 16 nilagay ko lang yan para ma-access ko yung admin page agad
  const [view, setView] = useState('admin'); 
  const [user, setUser] = useState('Admin User');
  
  // Kapag gusto mo bumalik sa Dashboard lagyan mo lang ng slash yung 15 at 16 para maging comment tapos yung 19 at 20 tanggalin mo lang yung slash para mapunta sa Dashboard
  // const [view, setView] = useState('dashboard');
  // const [user, setUser] = useState(localStorage.getItem('userName') || null);

  const [profileData, setProfileData] = useState(null);
  const [history, setHistory] = useState([]);

  const GOOGLE_CLIENT_ID = "324535586446-nbcj7tcp4373lrk5ct76u3v0od9n4vm3.apps.googleusercontent.com";

  useEffect(() => {
    if (user && user !== 'Admin User') { // Don't fetch if it's just the temporary admin string
      const savedProfile = localStorage.getItem(`userProfile_${user}`);
      setProfileData(savedProfile ? JSON.parse(savedProfile) : null);
      const savedHistory = localStorage.getItem(`assessmentHistory_${user}`);
      setHistory(savedHistory ? JSON.parse(savedHistory) : []);
    }
  }, [user]);

  const handleLoginSuccess = (name, email) => {
    localStorage.setItem('userName', name);
    setUser(name);

    if (email === "admin@gmail.com" || name === "Admin") {
      setView('admin');
    } else {
      setView('dashboard');
    }
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
          <>
            {view === 'admin' && <Admin onLogout={handleLogout} />}
            
            {view === 'dashboard' && (
              <Dashboard 
                userName={user} 
                onLogout={handleLogout} 
                onStart={() => setView('assessment')}
                onViewProfile={() => setView('profile')}
                history={history}
              />
            )}

            {view === 'profile' && (
              <ProfileForm 
                onBack={() => setView('dashboard')} 
                onSave={(data) => { setProfileData(data); setView('dashboard'); }} 
                initialData={profileData} 
              />
            )}

            {view === 'assessment' && (
              <AssessmentForm 
                onBack={() => setView('dashboard')} 
                onSubmit={(ans) => setView('dashboard')} 
              />
            )}
          </>
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