import React, { useState, useEffect } from 'react';
import { GoogleOAuthProvider } from '@react-oauth/google';
import Login from './Login';
import Signup from './Signup';
import Dashboard from './Dashboard';
import ProfileForm from './ProfileForm';
import AssessmentForm from './AssessmentForm';
import ResultsView from './ResultsView';
import { calculateRecommendation } from './logicEngine';
import './App.css';

function App() {
  const [isLogin, setIsLogin] = useState(true);
  const [user, setUser] = useState(localStorage.getItem('userName') || null);
  const [view, setView] = useState('dashboard');
  const [result, setResult] = useState(null);
  const [profileData, setProfileData] = useState(null);
  const [history, setHistory] = useState([]);

  const GOOGLE_CLIENT_ID = "324535586446-nbcj7tcp4373lrk5ct76u3v0od9n4vm3.apps.googleusercontent.com";

  useEffect(() => {
    if (user) {
      const savedProfile = localStorage.getItem(`userProfile_${user}`);
      setProfileData(savedProfile ? JSON.parse(savedProfile) : null);

      const savedHistory = localStorage.getItem(`assessmentHistory_${user}`);
      setHistory(savedHistory ? JSON.parse(savedHistory) : []);
    } else {
      setProfileData(null);
      setHistory([]);
    }
    setResult(null); 
  }, [user]);

  const handleLoginSuccess = (name) => {
    localStorage.setItem('userName', name);
    setUser(name);
  };

  const handleLogout = () => {
    localStorage.removeItem('userName');
    setUser(null);
    setView('dashboard');
  };

  // FIX: Defensive logic to prevent "reading 'math' of undefined"
  const handleProfileSave = (newData) => {
    const changes = [];

    if (profileData) {
      if (profileData.fullName !== newData.fullName) changes.push(`Name: ${newData.fullName}`);
      if (profileData.age !== newData.age) changes.push(`Age: ${newData.age}`);
      if (profileData.gender !== newData.gender) changes.push(`Gender: ${newData.gender}`);
      if (profileData.shsStrand !== newData.shsStrand) changes.push(`Strand: ${newData.shsStrand}`);
      
      // Safety check for grades comparison
      const oldGrades = profileData.grades || {};
      const newGrades = newData.grades || {};

      if (JSON.stringify(oldGrades) !== JSON.stringify(newGrades)) {
        const updatedSubjects = [];
        Object.keys(newGrades).forEach(subject => {
          // Optional chaining ensures we don't crash if oldGrades is missing this subject
          if (oldGrades[subject] !== newGrades[subject]) {
            updatedSubjects.push(subject);
          }
        });
        if (updatedSubjects.length > 0) {
          changes.push(`Grades (${updatedSubjects.join(", ")})`);
        }
      }
    } else {
      changes.push("Initial Profile Setup");
    }

    // Update States
    localStorage.setItem(`userProfile_${user}`, JSON.stringify(newData));
    setProfileData(newData);

    const changeMessage = changes.length > 0 
      ? `Update Profile: ${changes.join(", ")}` 
      : "Profile Saved (No changes)";

    const profileLog = {
      type: 'profile_update',
      courses: [changeMessage], 
      date: new Date().toLocaleDateString(),
      timestamp: Date.now()
    };

    const updatedHistory = [profileLog, ...history];
    setHistory(updatedHistory);
    localStorage.setItem(`assessmentHistory_${user}`, JSON.stringify(updatedHistory));
    
    setView('dashboard');
  };

  const handleAssessmentSubmit = (answers) => {
    if (!profileData) {
      alert("Please complete your Academic Profile first!");
      setView('profile');
      return;
    }
    
    const recommendationObj = calculateRecommendation(profileData, answers);
    
    const newResult = {
      type: 'assessment',
      courses: recommendationObj.courses,
      isAligned: recommendationObj.isAligned,
      status: recommendationObj.status,
      analysis: recommendationObj.analysis,
      date: new Date().toLocaleDateString(),
      timestamp: Date.now()
    };

    const updatedHistory = [newResult, ...history];
    setHistory(updatedHistory);
    localStorage.setItem(`assessmentHistory_${user}`, JSON.stringify(updatedHistory));

    setResult(newResult);
    setView('results');
  };

  return (
    <GoogleOAuthProvider clientId={GOOGLE_CLIENT_ID}>
      <div className="App">
        {user ? (
          <>
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
                onSave={handleProfileSave}
                initialData={profileData}
              />
            )}

            {view === 'assessment' && (
              <AssessmentForm 
                onBack={() => setView('dashboard')} 
                onSubmit={handleAssessmentSubmit}
              />
            )}

            {view === 'results' && (
              <ResultsView 
                recommendation={result} 
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