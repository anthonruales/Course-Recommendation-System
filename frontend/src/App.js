import React, { useState, useEffect } from 'react';
import { GoogleOAuthProvider } from '@react-oauth/google';
import axios from 'axios'; // Import axios for backend communication
import Login from './Login';
import Signup from './Signup';
import Dashboard from './Dashboard';
import ProfileForm from './ProfileForm';
import AssessmentForm from './AssessmentForm';
import ResultsView from './ResultsView';
import './App.css';

function App() {
  const [isLogin, setIsLogin] = useState(true);
  const [user, setUser] = useState(localStorage.getItem('userEmail') || null); // Changed to email for DB matching
  const [view, setView] = useState('dashboard');
  const [result, setResult] = useState(null);
  const [profileData, setProfileData] = useState(null);
  const [history, setHistory] = useState([]);

  const GOOGLE_CLIENT_ID = "324535586446-nbcj7tcp4373lrk5ct76u3v0od9n4vm3.apps.googleusercontent.com";
  const API_BASE_URL = "http://localhost:8000";

  // --- 1. Fetch Data from PostgreSQL via FastAPI on Load ---
  useEffect(() => {
    const fetchData = async () => {
      if (user) {
        try {
          // In a real app, you'd fetch the specific user's profile and history from DB
          const historyRes = await axios.get(`${API_BASE_URL}/history`);
          setHistory(historyRes.data);
          
          // Assuming profile data is stored/fetched here
          const savedProfile = localStorage.getItem(`userProfile_${user}`);
          setProfileData(savedProfile ? JSON.parse(savedProfile) : null);
        } catch (err) {
          console.error("Error fetching data from database", err);
        }
      } else {
        setProfileData(null);
        setHistory([]);
      }
      setResult(null);
    };
    fetchData();
  }, [user]);

  const handleLoginSuccess = (userData) => {
    // Expecting userData to be the object returned from your FastAPI /login route
    localStorage.setItem('userEmail', userData);
    setUser(userData);
  };

  const handleLogout = () => {
    localStorage.removeItem('userEmail');
    setUser(null);
    setView('dashboard');
  };

  // --- 2. Save Profile to Backend ---
  const handleProfileSave = async (newData) => {
    try {
      // You would typically call an axios.post(`${API_BASE_URL}/update-profile`, newData) here
      localStorage.setItem(`userProfile_${user}`, JSON.stringify(newData));
      setProfileData(newData);
      
      // Update history log (This could also be a DB call)
      const profileLog = {
        type: 'profile_update',
        courses: ["Profile Updated"], 
        date: new Date().toLocaleDateString(),
      };
      setHistory([profileLog, ...history]);
      setView('dashboard');
    } catch (err) {
      alert("Failed to save profile to database.");
    }
  };

  // --- 3. Run Decision Tree & Rule-Based Logic via Backend ---
  const handleAssessmentSubmit = async (answers) => {
    if (!profileData) {
      alert("Please complete your Academic Profile first!");
      setView('profile');
      return;
    }

    try {
      // Step A: Run Decision Tree on Backend
      const formattedAnswers = Object.entries(answers).map(([id, val]) => ({
        questionId: parseInt(id.replace('q', '')),
        response: val
      }));

      const recResponse = await axios.post(`${API_BASE_URL}/recommend`, {
        answers: formattedAnswers
      });

      // Step B: Get specific course matches from PostgreSQL (Rule-Based)
      // Note: We use a placeholder ID '1' or fetch based on logged-in user
      const dbMatches = await axios.get(`${API_BASE_URL}/get-recommendations/1`);

      const finalResult = {
        type: 'assessment',
        courses: dbMatches.data.map(course => ({
          course: course.course_name,
          status: course.alignment_score === "High" ? "Qualified" : "Bridging Required",
          analysis: recResponse.data.explanation, // Reason from Decision Tree
          isAligned: course.alignment_score === "High"
        })),
        date: new Date().toLocaleDateString(),
      };

      setHistory([finalResult, ...history]);
      setResult(finalResult);
      setView('results');
    } catch (err) {
      console.error(err);
      alert("Error processing assessment. Ensure FastAPI server is running.");
    }
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