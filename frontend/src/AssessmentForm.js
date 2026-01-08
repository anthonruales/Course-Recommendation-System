import React, { useState, useEffect } from 'react';

function AssessmentForm({ onBack, onShowResults }) {
  const [questions, setQuestions] = useState([]);
  const [answers, setAnswers] = useState({});
  const [loading, setLoading] = useState(false);
  const [isFetching, setIsFetching] = useState(true);

  // GET RANDOMIZED QUESTIONS
  useEffect(() => {
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
  }, []);

  const handleRadioChange = (questionId, value) => {
    setAnswers({ ...answers, [questionId]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    const formattedAnswers = Object.entries(answers).map(([id, response]) => ({
      questionId: parseInt(id),
      response: response
    }));

    try {
      const response = await fetch("http://localhost:8000/recommend", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ answers: formattedAnswers }),
      });
      const data = await response.json();
      if (response.ok) onShowResults(data);
      else alert("Failed to generate recommendation.");
    } catch (error) {
      alert("Connection error!");
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
          <div style={styles.navLink} onClick={onBack}>⬅ Exit</div>
        </div>
      </aside>

      {/* MAIN */}
      <main style={styles.main}>
        <header style={styles.header}>
          <h1 style={styles.title}>Discovery Mode</h1>
          <p style={styles.subtitle}>Our AI is analyzing your interests from these random questions.</p>
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
                    {['yes', 'no'].map(choice => (
                      <label key={choice} style={{
                        ...styles.option,
                        ...(answers[q.question_id] === choice ? styles.selected : {})
                      }}>
                        <input 
                          type="radio" 
                          name={`q${q.question_id}`} 
                          style={{display: 'none'}}
                          onChange={() => handleRadioChange(q.question_id, choice)} 
                          required 
                        />
                        {choice.toUpperCase()}
                      </label>
                    ))}
                  </div>
                </div>
              ))}
              <button type="submit" disabled={loading} style={styles.btn}>
                {loading ? "Analyzing..." : "Finish Assessment"}
              </button>
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
  container: { display: 'flex', width: '100vw', height: '100vh', background: '#0a0a0c', color: 'white' },
  sidebar: { width: '260px', borderRight: '1px solid #222', padding: '40px 20px', display: 'flex', flexDirection: 'column' },
  brand: { display: 'flex', alignItems: 'center', marginBottom: '50px' },
  logo: { width: '32px', height: '32px', background: '#6366f1', borderRadius: '8px', display: 'flex', alignItems: 'center', justifyContent: 'center', fontWeight: 'bold', marginRight: '10px' },
  brandName: { fontSize: '18px', fontWeight: 'bold' },
  nav: { flex: 1 },
  navActive: { padding: '12px', background: 'rgba(99, 102, 241, 0.1)', color: '#818cf8', borderRadius: '8px', fontWeight: '600' },
  navLink: { padding: '12px', color: '#666', cursor: 'pointer', marginTop: '10px' },
  main: { flex: 1, padding: '60px', display: 'flex', flexDirection: 'column' },
  header: { marginBottom: '40px' },
  title: { fontSize: '32px', fontWeight: '800' },
  subtitle: { color: '#666', marginTop: '10px' },
  form: { flex: 1, overflow: 'hidden', maxWidth: '700px' },
  scrollArea: { height: '100%', overflowY: 'auto', paddingRight: '20px' },
  card: { background: '#111', border: '1px solid #222', padding: '25px', borderRadius: '16px', marginBottom: '20px' },
  questionText: { fontSize: '18px', fontWeight: '500', marginBottom: '20px' },
  options: { display: 'flex', gap: '10px' },
  option: { flex: 1, padding: '12px', border: '1px solid #333', borderRadius: '10px', textAlign: 'center', cursor: 'pointer', transition: '0.2s' },
  selected: { background: '#6366f1', borderColor: '#6366f1' },
  btn: { width: '100%', padding: '18px', background: '#6366f1', border: 'none', borderRadius: '12px', color: 'white', fontWeight: 'bold', cursor: 'pointer', marginTop: '20px' },
  loading: { textAlign: 'center', color: '#6366f1', padding: '50px' },
  error: { color: '#ef4444', textAlign: 'center', padding: '50px' }
};

export default AssessmentForm;