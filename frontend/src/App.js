import React, { useState, useEffect } from 'react';
import { GoogleOAuthProvider } from '@react-oauth/google';
import Login from './Login';
import Signup from './Signup';
import Dashboard from './Dashboard';
import ProfileForm from './ProfileForm';
import AdaptiveAssessment from './AdaptiveAssessment';
import MyActivity from './MyActivity';
import Admin from './admin/Admin'; 
import ResultsView from './ResultsView'; 
import './App.css';

function App() {
  const [isLogin, setIsLogin] = useState(true);
  const [view, setView] = useState('dashboard');
  const [user, setUser] = useState(localStorage.getItem('userName') || null);
  const [recommendationData, setRecommendationData] = useState(null);
  const [selectedQuestionCount, setSelectedQuestionCount] = useState(30);
  
  // Initialize as empty object to prevent "is not a function" errors
  const [profileData, setProfileData] = useState({});
  const [history, setHistory] = useState([]);

  const GOOGLE_CLIENT_ID = "324535586446-nbcj7tcp4373lrk5ct76u3v0od9n4vm3.apps.googleusercontent.com";

  useEffect(() => {
    if (user && user !== 'Admin User') {
      // Load profile from backend
      const userId = localStorage.getItem('userId');
      if (userId) {
        fetch(`http://localhost:8000/user/${userId}/academic-info`)
          .then(res => res.json())
          .then(data => {
            if (data.academic_info) {
              setProfileData({
                fullname: data.fullname || '',
                gwa: data.academic_info.gwa || '',
                strand: data.academic_info.strand || '',
                age: data.academic_info.age || '',
                gender: data.academic_info.gender || '',
                interests: data.academic_info.interests || '',
                skills: data.academic_info.skills || ''
              });
            }
          })
          .catch(err => {
            console.error('Error loading profile:', err);
            // Fallback to localStorage
            const savedProfile = localStorage.getItem(`userProfile_${user}`);
            if (savedProfile) {
              setProfileData(JSON.parse(savedProfile));
            }
          });
      }
      
      const savedHistory = localStorage.getItem(`assessmentHistory_${user}`);
      try {
        const parsedHistory = savedHistory ? JSON.parse(savedHistory) : [];
        setHistory(Array.isArray(parsedHistory) ? parsedHistory : []);
      } catch (e) {
        setHistory([]);
      }
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
    localStorage.removeItem('userId');
    setUser(null);
    setRecommendationData(null);
    setProfileData({}); // Clear state on logout
    setView('dashboard');
  };

  const handleAssessmentResults = (data) => {
    setRecommendationData(data);
    
    const newHistoryItem = {
      type: 'assessment',
      courses: data.courses && data.courses[0] ? (data.courses[0].course || data.courses[0]) : "Career Match",
      date: new Date().toLocaleDateString()
    };

    const updatedHistory = [newHistoryItem, ...history];
    setHistory(updatedHistory);
    localStorage.setItem(`assessmentHistory_${user}`, JSON.stringify(updatedHistory));
    
    setView('results');
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
                onStartAdaptive={(questionCount) => {
                  setSelectedQuestionCount(questionCount || 30);
                  setView('adaptive');
                }}
                onViewProfile={() => setView('profile')}
                onViewActivity={() => setView('activity')}
                history={history}
              />
            )}

            {view === 'profile' && (
              <ProfileForm 
                onBack={() => setView('dashboard')} 
                onSave={(changedFields) => { 
                  // Save to local storage
                  localStorage.setItem(`userProfile_${user}`, JSON.stringify(profileData));
                  
                  // Build specific description of what changed
                  let changeDescription = 'Profile Updated';
                  if (changedFields && changedFields.length > 0) {
                    if (changedFields.length === 1) {
                      changeDescription = `Updated ${changedFields[0]}`;
                    } else if (changedFields.length === 2) {
                      changeDescription = `Updated ${changedFields[0]} & ${changedFields[1]}`;
                    } else {
                      changeDescription = `Updated ${changedFields.slice(0, 2).join(', ')} +${changedFields.length - 2} more`;
                    }
                  }
                  
                  // Log the update in history with specific changes
                  const updateLog = {
                    type: 'profile_update',
                    courses: changeDescription,
                    changedFields: changedFields || [],
                    date: new Date().toLocaleDateString()
                  };
                  setHistory([updateLog, ...history]);
                  
                  // Delay navigation to allow toast to be seen
                  setTimeout(() => {
                    setView('dashboard');
                  }, 1500);
                }} 
                // These props must match the names in ProfileForm.js
                formData={profileData} 
                setFormData={setProfileData} 
              />
            )}

            {/* OLD ASSESSMENT FORM REMOVED - Only adaptive assessment is used now */}

            {view === 'adaptive' && (
              <AdaptiveAssessment 
                onBack={() => setView('dashboard')} 
                onShowResults={handleAssessmentResults}
                maxQuestions={selectedQuestionCount}
              />
            )}

            {view === 'activity' && (
              <MyActivity 
                onBack={() => setView('dashboard')}
              />
            )}

            {view === 'results' && recommendationData && (
              <ResultsView 
                recommendation={recommendationData}
                profileData={profileData}
                onRetake={() => setView('assessment')}
                onBack={() => setView('dashboard')}
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