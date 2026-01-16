import React, { useState, useEffect } from 'react';
import './components/style/Dashboard.css';
function AssessmentForm({ onBack, onShowResults }) {
  const [questions, setQuestions] = useState([]);
  const [answers, setAnswers] = useState({});
  const [loading, setLoading] = useState(false);
  const [isFetching, setIsFetching] = useState(true);

  useEffect(() => {
    setIsFetching(true);
    fetch("http://localhost:8000/questions")
      .then(res => res.json())
      .then(data => {
        setQuestions(Array.isArray(data) ? data : []);
        setIsFetching(false);
      })
      .catch(err => {
        console.error("Fetch error:", err);
        setIsFetching(false);
      });
  }, []);

  const handleRadioChange = (questionId, optionId) => {
    setAnswers({ ...answers, [questionId]: optionId });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const unansweredCount = questions.length - Object.keys(answers).length;
    if (unansweredCount > 0) {
      alert(`Please answer all questions! You have ${unansweredCount} unanswered question(s).`);
      return;
    }
    
    setLoading(true);
    const userId = localStorage.getItem('userId');

    try {
      const response = await fetch("http://localhost:8000/recommend", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ 
          userId: parseInt(userId),
          answers: Object.entries(answers).map(([id, opt]) => ({ questionId: parseInt(id), chosenOptionId: parseInt(opt) }))
        }),
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
    <div className="assessment-container">
      <aside className="assessment-sidebar">
        <div style={{ display: 'flex', alignItems: 'center', marginBottom: '50px' }}>
          <div style={{ width: '32px', height: '32px', background: '#6366f1', borderRadius: '8px', display: 'flex', alignItems: 'center', justifyContent: 'center', fontWeight: 'bold', marginRight: '10px' }}>C</div>
          <h2 style={{ fontSize: '18px', fontWeight: 'bold' }}>CoursePro</h2>
        </div>
        <div className="sidebar-nav">
          <div className="nav-item active">🧠 Career Assessment</div>
          <div className="nav-item" style={{ color: '#666', cursor: 'pointer' }} onClick={onBack}>⬅ Exit</div>
        </div>
      </aside>

      <main className="assessment-main">
        <header className="assessment-header">
          <h1 className="assessment-title">Discovery Mode</h1>
          <p className="assessment-subtitle">Our AI is analyzing your interests from these random questions.</p>
          {questions.length > 0 && (
            <p className="assessment-progress">
              Progress: {Object.keys(answers).length} / {questions.length} questions answered
            </p>
          )}
        </header>

        <form onSubmit={handleSubmit} className="assessment-form">
          {isFetching ? (
            <div className="assessment-loading">Connecting to Question Bank...</div>
          ) : questions.length > 0 ? (
            <div className="assessment-scroll-area">
              {questions.map((q) => (
                <div key={q.question_id} className="question-card">
                  <p className="question-text">{q.question_text}</p>
                  <div className="options-container">
                    {q.options?.map(option => (
                      <label 
                        key={option.option_id} 
                        className={`option-item ${answers[q.question_id] === option.option_id ? 'selected' : ''}`}
                      >
                        <input 
                          type="radio" 
                          name={`q${q.question_id}`} 
                          style={{ display: 'none' }}
                          onChange={() => handleRadioChange(q.question_id, option.option_id)} 
                        />
                        {option.option_text}
                      </label>
                    ))}
                  </div>
                </div>
              ))}
              <button type="submit" disabled={loading} className="submit-btn">
                {loading ? "Analyzing..." : "Finish Assessment"}
              </button>
            </div>
          ) : (
            <div className="assessment-error">No questions found.</div>
          )}
        </form>
      </main>
    </div>
  );
}

export default AssessmentForm;