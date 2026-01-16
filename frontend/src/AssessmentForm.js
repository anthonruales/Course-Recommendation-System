import React, { useState, useEffect } from 'react';

function AssessmentForm({ onBack, onShowResults }) {
  const [questions, setQuestions] = useState([]);
  const [answers, setAnswers] = useState({});
  const [loading, setLoading] = useState(false);
  const [isFetching, setIsFetching] = useState(true);
  const [profileCheck, setProfileCheck] = useState({ checking: true, hasProfile: false });

  // CHECK ACADEMIC PROFILE FIRST
  useEffect(() => {
    const userId = localStorage.getItem('userId');
    if (userId) {
      fetch(`http://localhost:8000/user/${userId}/academic-info`)
        .then(res => res.json())
        .then(data => {
          if (!data.has_academic_info) {
            alert('⚠️ Please complete your Academic Profile first!\n\nYou need to fill in your GWA and SHS Strand before taking the assessment.');
            onBack();
          } else {
            setProfileCheck({ checking: false, hasProfile: true });
          }
        })
        .catch(err => {
          console.error('Error checking academic info:', err);
          setProfileCheck({ checking: false, hasProfile: false });
        });
    } else {
      alert('User ID not found. Please log in again.');
      onBack();
    }
  }, [onBack]);

  // GET RANDOMIZED QUESTIONS (only if profile is complete)
  useEffect(() => {
    if (!profileCheck.hasProfile) return;
    
    setIsFetching(true);
    fetch("http://localhost:8000/questions")
      .then(res => {
        if (!res.ok) throw new Error("Server error or Route not found");
        return res.json();
      })
      .then(data => {
        // Ensure we handle the data as an array
        setQuestions(Array.isArray(data) ? data : []);
        setIsFetching(false);
      })
      .catch(err => {
        console.error("Fetch error:", err);
        setIsFetching(false);
      });
  }, [profileCheck.hasProfile]);

  const handleRadioChange = (questionId, optionId) => {
    setAnswers({ ...answers, [questionId]: optionId });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    // Validate that all questions are answered
    const unansweredCount = questions.length - Object.keys(answers).length;
    if (unansweredCount > 0) {
      alert(`Please answer all questions! You have ${unansweredCount} unanswered question(s).`);
      return;
    }
    
    setLoading(true);

    const formattedAnswers = Object.entries(answers).map(([id, chosenOptionId]) => ({
      questionId: parseInt(id),
      chosenOptionId: parseInt(chosenOptionId)
    }));

    // Get userId from localStorage
    const userId = localStorage.getItem('userId');
    if (!userId) {
      alert('User ID not found. Please log in again.');
      setLoading(false);
      return;
    }
    
    console.log('Submitting assessment for userId:', userId);

    try {
      const response = await fetch("http://localhost:8000/recommend", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ 
          userId: parseInt(userId),
          answers: formattedAnswers
        }),
      });
      const data = await response.json();
      if (response.ok) {
        console.log('Recommendation received:', data);
        onShowResults(data);
      } else {
        alert(`Failed to generate recommendation: ${data.detail || 'Unknown error'}`);
      }
    } catch (error) {
      console.error('Assessment submission error:', error);
      alert("Connection error! Please check if the backend server is running.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={styles.container}>
      {/* SIDEBAR */}
      <aside style={styles.sidebar}>
        <div style={styles.brand}>
          <div style={styles.logo}>C</div>
          <h2 style={styles.brandName}>CoursePro</h2>
        </div>
        <div style={styles.nav}>
          <div style={styles.navActive}>🧠 Career Assessment</div>
          <div style={styles.navLink} onClick={onBack}
            onMouseEnter={(e) => { e.target.style.background = 'rgba(255, 255, 255, 0.05)'; e.target.style.color = '#cbd5e1'; }}
            onMouseLeave={(e) => { e.target.style.background = 'transparent'; e.target.style.color = '#94a3b8'; }}
          >⬅ Exit</div>
        </div>
      </aside>

      {/* MAIN */}
      <main style={styles.main}>
        <header style={styles.header}>
          <h1 style={styles.title}>Discovery Mode</h1>
          <p style={styles.subtitle}>Our AI is analyzing your interests from these random questions.</p>
          {questions.length > 0 && (
            <p style={styles.progress}>
              Progress: {Object.keys(answers).length} / {questions.length} questions answered
            </p>
          )}
        </header>

        <form onSubmit={handleSubmit} style={styles.form}>
          {isFetching ? (
            <div style={styles.loading}>Connecting to Question Bank...</div>
          ) : questions.length > 0 ? (
            <div style={styles.scrollArea}>
              {questions.map((q) => (
                <div key={q.question_id} style={styles.card}>
                  <p style={styles.questionText}>{q.question_text}</p>
                  <div style={styles.options}>
                    {q.options && q.options.length > 0 ? (
                      q.options.map(option => (
                        <label key={option.option_id} style={{
                          ...styles.option,
                          ...(answers[q.question_id] === option.option_id ? styles.selected : {})
                        }}
                        onMouseEnter={(e) => { 
                          if (answers[q.question_id] !== option.option_id) {
                            e.currentTarget.style.background = 'rgba(255,255,255,0.05)'; 
                            e.currentTarget.style.borderColor = 'rgba(99, 102, 241, 0.3)';
                            e.currentTarget.style.transform = 'translateX(4px)';
                          }
                        }}
                        onMouseLeave={(e) => { 
                          if (answers[q.question_id] !== option.option_id) {
                            e.currentTarget.style.background = 'rgba(255,255,255,0.02)'; 
                            e.currentTarget.style.borderColor = 'rgba(255,255,255,0.08)';
                            e.currentTarget.style.transform = 'translateX(0)';
                          }
                        }}
                        >
                          <input 
                            type="radio" 
                            name={`q${q.question_id}`} 
                            style={{display: 'none'}}
                            onChange={() => handleRadioChange(q.question_id, option.option_id)} 
                            required 
                          />
                          {option.option_text}
                        </label>
                      ))
                    ) : (
                      <p style={{color: '#ef4444'}}>No options available for this question</p>
                    )}
                  </div>
                </div>
              ))}
              <div style={{ gridColumn: '1 / -1' }}>
                <button type="submit" disabled={loading} style={styles.btn}
                  onMouseEnter={(e) => { if (!loading) { e.target.style.transform = 'translateY(-2px)'; e.target.style.boxShadow = '0 15px 30px rgba(99, 102, 241, 0.4)'; } }}
                  onMouseLeave={(e) => { e.target.style.transform = 'translateY(0)'; e.target.style.boxShadow = '0 10px 20px rgba(99, 102, 241, 0.2)'; }}
                >
                  {loading ? "Analyzing..." : 
                   Object.keys(answers).length === questions.length 
                     ? "Finish Assessment" 
                     : `Answer All Questions (${Object.keys(answers).length}/${questions.length})`}
                </button>
              </div>
            </div>
          ) : (
            <div style={styles.error}>No questions found. Check your backend <code>/questions</code> route.</div>
          )}
        </form>
      </main>
    </div>
  );
}

const styles = {
  container: { 
    display: 'flex', 
    width: '100vw', 
    height: '100vh', 
    background: '#020617',
    backgroundImage: 'radial-gradient(at 0% 0%, hsla(253,16%,7%,1) 0, transparent 50%), radial-gradient(at 50% 0%, hsla(225,39%,30%,1) 0, transparent 50%), radial-gradient(at 100% 0%, hsla(339,49%,30%,1) 0, transparent 50%)',
    color: 'white' 
  },
  sidebar: { width: '260px', background: 'rgba(255, 255, 255, 0.02)', backdropFilter: 'blur(20px)', borderRight: '1px solid rgba(255, 255, 255, 0.08)', padding: '40px 20px', display: 'flex', flexDirection: 'column' },
  brand: { display: 'flex', alignItems: 'center', marginBottom: '50px' },
  logo: { width: '32px', height: '32px', background: '#6366f1', borderRadius: '8px', display: 'flex', alignItems: 'center', justifyContent: 'center', fontWeight: 'bold', marginRight: '10px' },
  brandName: { fontSize: '18px', fontWeight: 'bold' },
  nav: { flex: 1 },
  navActive: { padding: '12px', background: 'rgba(99, 102, 241, 0.1)', color: '#818cf8', borderRadius: '8px', fontWeight: '600' },
  navLink: { padding: '12px', color: '#94a3b8', cursor: 'pointer', marginTop: '10px', borderRadius: '10px', transition: 'all 0.3s ease' },
  main: { flex: 1, padding: '40px 60px', display: 'flex', flexDirection: 'column', maxWidth: '1400px', margin: '0 auto', width: '100%' },
  header: { marginBottom: '40px' },
  title: { fontSize: '32px', fontWeight: '800', color: 'white' },
  subtitle: { color: '#94a3b8', marginTop: '10px' },
  progress: { color: '#818cf8', marginTop: '10px', fontSize: '16px', fontWeight: '500' },
  form: { flex: 1, overflow: 'hidden', width: '100%' },
  scrollArea: { height: '100%', overflowY: 'auto', paddingRight: '20px', display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(450px, 1fr))', gap: '20px', alignContent: 'start' },
  card: { background: 'rgba(255, 255, 255, 0.03)', border: '1px solid rgba(255, 255, 255, 0.08)', borderRadius: '20px', padding: '30px', height: 'fit-content', transition: 'all 0.3s ease' },
  questionText: { fontSize: '17px', fontWeight: '600', marginBottom: '20px', lineHeight: '1.5', color: 'white' },
  options: { display: 'flex', flexDirection: 'column', gap: '12px' },
  option: { padding: '14px 18px', background: 'rgba(255,255,255,0.02)', border: '1px solid rgba(255,255,255,0.08)', borderRadius: '10px', textAlign: 'left', cursor: 'pointer', transition: 'all 0.3s ease', fontSize: '15px', color: '#cbd5e1' },
  selected: { background: 'rgba(99, 102, 241, 0.2)', borderColor: '#6366f1', color: 'white' },
  btn: { width: '100%', padding: '18px', background: '#6366f1', border: 'none', borderRadius: '12px', color: 'white', fontWeight: '700', cursor: 'pointer', marginTop: '20px', boxShadow: '0 10px 20px rgba(99, 102, 241, 0.2)', transition: 'all 0.3s ease' },
  loading: { textAlign: 'center', color: '#6366f1', padding: '50px' },
  error: { color: '#ef4444', textAlign: 'center', padding: '50px' }
};

export default AssessmentForm;