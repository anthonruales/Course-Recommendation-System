import React, { useState, useEffect } from 'react';

function AssessmentForm({ onBack, onShowResults }) {
  const [questions, setQuestions] = useState([]);
  const [answers, setAnswers] = useState({});
  const [loading, setLoading] = useState(false);
  const [isFetching, setIsFetching] = useState(false);
  const [profileCheck, setProfileCheck] = useState({ checking: true, hasProfile: false });
  const [selectedTier, setSelectedTier] = useState(null);
  const [tiers, setTiers] = useState(null);
  const [tierLoading, setTierLoading] = useState(true);
  const [userStrand, setUserStrand] = useState(null);

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
            // Store the user's strand for strand-based question filtering
            const strand = data.academic_info?.strand;
            setUserStrand(strand || 'GAS');
            console.log('User strand loaded:', strand);
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

  // GET ASSESSMENT TIERS (only if profile is complete)
  useEffect(() => {
    if (!profileCheck.hasProfile) return;
    
    setTierLoading(true);
    fetch("http://localhost:8000/assessment/tiers")
      .then(res => {
        if (!res.ok) throw new Error("Failed to fetch assessment tiers");
        return res.json();
      })
      .then(data => {
        setTiers(data.tiers);
        setTierLoading(false);
      })
      .catch(err => {
        console.error("Fetch error:", err);
        setTierLoading(false);
      });
  }, [profileCheck.hasProfile]);

  // GET RANDOMIZED QUESTIONS (only after tier is selected)
  useEffect(() => {
    if (!selectedTier) return;
    
    // Reset answers when tier changes
    setAnswers({});
    setIsFetching(true);
    
    // Include strand in the request for strand-based question prioritization
    const strandParam = userStrand ? `?strand=${userStrand}` : '';
    fetch(`http://localhost:8000/assessment/start/${selectedTier}${strandParam}`)
      .then(res => {
        if (!res.ok) throw new Error("Server error or Route not found");
        return res.json();
      })
      .then(data => {
        // Questions now come directly from database with proper IDs
        setQuestions(data.questions || []);
        console.log(`Loaded ${data.question_count} questions for ${data.strand_name || 'general'} strand`);
        setIsFetching(false);
      })
      .catch(err => {
        console.error("Fetch error:", err);
        setIsFetching(false);
      });
  }, [selectedTier, userStrand]);

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

  // RENDER TIER SELECTION SCREEN
  if (!selectedTier) {
    return (
      <div style={styles.container}>
        {/* SIDEBAR */}
        <aside style={styles.sidebar}>
          <div style={styles.brand}>
            <img src="/logo.svg" alt="CoursePro" style={styles.logo} />
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
            <h1 style={styles.title}>Choose Your Assessment Level</h1>
            <p style={styles.subtitle}>Select an assessment duration that fits your schedule. More questions = More accurate recommendations.</p>
            {userStrand && (
              <p style={styles.strandBadge}>
                🎯 Questions personalized for <strong>{userStrand}</strong> strand
              </p>
            )}
          </header>

          {tierLoading ? (
            <div style={styles.loading}>Loading assessment options...</div>
          ) : tiers ? (
            <div style={styles.tierGrid}>
              {Object.entries(tiers).map(([tierKey, tier]) => (
                <div 
                  key={tierKey}
                  style={{
                    ...styles.tierCard,
                    cursor: 'pointer',
                    border: selectedTier === tierKey ? '2px solid #6366f1' : '1px solid rgba(255, 255, 255, 0.1)',
                  }}
                  onClick={() => setSelectedTier(tierKey)}
                  onMouseEnter={(e) => {
                    e.currentTarget.style.background = 'rgba(99, 102, 241, 0.1)';
                    e.currentTarget.style.transform = 'translateY(-8px)';
                    e.currentTarget.style.borderColor = '#6366f1';
                    e.currentTarget.style.boxShadow = '0 20px 40px rgba(99, 102, 241, 0.2)';
                  }}
                  onMouseLeave={(e) => {
                    e.currentTarget.style.background = 'rgba(255, 255, 255, 0.02)';
                    e.currentTarget.style.transform = 'translateY(0)';
                    e.currentTarget.style.borderColor = 'rgba(255, 255, 255, 0.1)';
                    e.currentTarget.style.boxShadow = 'none';
                  }}
                >
                  <div style={styles.tierName}>{tier.name}</div>
                  <div style={styles.tierCount}>{tier.question_count} Questions</div>
                  <div style={styles.tierTime}>⏱️ {tier.estimated_time}</div>
                  <div style={styles.tierAccuracy}>📊 {tier.accuracy}</div>
                  <div style={styles.tierDescription}>{tier.description}</div>
                </div>
              ))}
            </div>
          ) : (
            <div style={styles.error}>Failed to load assessment tiers. Please try again.</div>
          )}
        </main>
      </div>
    );
  }

  // RENDER ASSESSMENT QUESTIONS
  return (
    <div style={styles.container}>
      {/* SIDEBAR */}
      <aside style={styles.sidebar}>
        <div style={styles.brand}>
          <img src="/logo.svg" alt="CoursePro" style={styles.logo} />
          <h2 style={styles.brandName}>CoursePro</h2>
        </div>
        <div style={styles.nav}>
          <div style={styles.navActive}>🧠 Career Assessment</div>
          <div style={styles.navLink} onClick={() => setSelectedTier(null)}
            onMouseEnter={(e) => { e.target.style.background = 'rgba(255, 255, 255, 0.05)'; e.target.style.color = '#cbd5e1'; }}
            onMouseLeave={(e) => { e.target.style.background = 'transparent'; e.target.style.color = '#94a3b8'; }}
          >↩️ Back to Tiers</div>
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
          <p style={styles.subtitle}>Our AI is analyzing your interests from these questions.</p>
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
  logo: { width: '40px', height: '40px', borderRadius: '10px', marginRight: '10px', objectFit: 'contain' },
  brandName: { fontSize: '18px', fontWeight: 'bold' },
  nav: { flex: 1 },
  navActive: { padding: '12px', background: 'rgba(99, 102, 241, 0.1)', color: '#818cf8', borderRadius: '8px', fontWeight: '600' },
  navLink: { padding: '12px', color: '#94a3b8', cursor: 'pointer', marginTop: '10px', borderRadius: '10px', transition: 'all 0.3s ease' },
  main: { flex: 1, padding: '40px 60px', display: 'flex', flexDirection: 'column', maxWidth: '1400px', margin: '0 auto', width: '100%' },
  header: { marginBottom: '40px' },
  title: { fontSize: '32px', fontWeight: '800', color: 'white' },
  subtitle: { color: '#94a3b8', marginTop: '10px' },
  strandBadge: { color: '#10b981', marginTop: '15px', fontSize: '15px', fontWeight: '500', background: 'rgba(16, 185, 129, 0.1)', padding: '10px 18px', borderRadius: '30px', display: 'inline-block', border: '1px solid rgba(16, 185, 129, 0.3)' },
  progress: { color: '#818cf8', marginTop: '10px', fontSize: '16px', fontWeight: '500' },
  form: { flex: 1, overflow: 'hidden', width: '100%' },
  scrollArea: { height: '100%', overflowY: 'auto', paddingRight: '20px', display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(450px, 1fr))', gap: '20px', alignContent: 'start' },
  card: { background: 'rgba(255, 255, 255, 0.03)', border: '1px solid rgba(255, 255, 255, 0.08)', borderRadius: '20px', padding: '30px', height: 'fit-content', transition: 'all 0.3s ease' },
  questionText: { fontSize: '17px', fontWeight: '600', marginBottom: '20px', lineHeight: '1.5', color: 'white' },
  options: { display: 'flex', flexDirection: 'column', gap: '12px' },
  option: { padding: '14px 18px', background: 'rgba(255,255,255,0.02)', border: '1px solid rgba(255,255,255,0.08)', borderRadius: '10px', textAlign: 'left', cursor: 'pointer', transition: 'all 0.3s ease', fontSize: '15px', color: '#cbd5e1' },
  selected: { background: 'rgba(99, 102, 241, 0.2)', borderColor: '#6366f1', color: 'white' },
  btn: { width: '100%', padding: '18px', background: '#6366f1', border: 'none', borderRadius: '12px', color: 'white', fontWeight: '700', cursor: 'pointer', marginTop: '20px', boxShadow: '0 10px 20px rgba(99, 102, 241, 0.2)', transition: 'all 0.3s ease' },
  tierGrid: { display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '30px', marginTop: '40px' },
  tierCard: { background: 'rgba(255, 255, 255, 0.02)', border: '1px solid rgba(255, 255, 255, 0.1)', borderRadius: '20px', padding: '40px 30px', transition: 'all 0.3s ease', textAlign: 'center' },
  tierName: { fontSize: '24px', fontWeight: '700', color: 'white', marginBottom: '15px' },
  tierCount: { fontSize: '20px', fontWeight: '600', color: '#818cf8', marginBottom: '10px' },
  tierTime: { fontSize: '15px', color: '#cbd5e1', marginBottom: '10px' },
  tierAccuracy: { fontSize: '15px', color: '#cbd5e1', marginBottom: '15px', fontWeight: '500' },
  tierDescription: { fontSize: '14px', color: '#94a3b8', lineHeight: '1.6' },
  loading: { textAlign: 'center', color: '#6366f1', padding: '50px' },
  error: { color: '#ef4444', textAlign: 'center', padding: '50px' }
};

export default AssessmentForm;