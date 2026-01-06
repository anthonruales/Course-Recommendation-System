import React, { useState } from 'react';
import './components/style/Dashboard.css'; // I-konek ang CSS

function AssessmentForm({ onBack }) {
  const [formData, setFormData] = useState({ q1: '', q2: '', q3: '' });
  const [recommendation, setRecommendation] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const response = await fetch("http://localhost:8000/recommend", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          answers: [
            { questionId: 1, response: formData.q1 },
            { questionId: 2, response: formData.q2 },
            { questionId: 3, response: formData.q3 },
          ],
        }),
      });
      const data = await response.json();
      if (response.ok) {
        setRecommendation(data);
      } else {
        alert("Failed to get recommendation.");
      }
    } catch (error) {
      alert("Connection error!");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="portal-layout"> {/* Parehong background ng Dashboard */}
      <main className="portal-main">
        <button onClick={onBack} className="link-btn" style={{ marginBottom: '20px' }}>
          ← Cancel Assessment
        </button>

        <div className="portal-card" style={{ maxWidth: '700px', margin: '0 auto' }}>
          <header className="main-header" style={{ borderBottom: '1px solid #eee', paddingBottom: '10px' }}>
            <h2 style={{ margin: 0 }}>Career Interest Questionnaire</h2>
            <p className="muted-text">Answer these situational questions for the Decision Tree analysis.</p>
          </header>

          {recommendation ? (
            <div className="summary-box" style={{ backgroundColor: '#f0f9ff' }}>
              <h3 className="summary-success" style={{ color: '#0369a1', marginTop: 0 }}>Recommended Course:</h3>
              <p style={{ fontSize: '20px', fontWeight: 'bold' }}>{recommendation.recommendation}</p>
              <p className="muted-text">{recommendation.explanation}</p>
              <button onClick={() => setRecommendation(null)} className="btn-solid" style={{ marginTop: '10px' }}>
                Retake Assessment
              </button>
            </div>
          ) : (
            <form onSubmit={handleSubmit}>
              {/* Ginamit ang activity-item class para sa spacing ng questions */}
              <div className="activity-item">
                <p>1. When faced with a broken gadget, do you prefer fixing it yourself?</p>
                <label><input type="radio" name="q1" value="yes" onChange={handleChange} required /> Yes</label>
                <label style={{ marginLeft: '20px' }}><input type="radio" name="q1" value="no" onChange={handleChange} /> No</label>
              </div>

              <div className="activity-item">
                <p>2. Do you enjoy analyzing data or conducting experiments?</p>
                <label><input type="radio" name="q2" value="yes" onChange={handleChange} required /> Yes</label>
                <label style={{ marginLeft: '20px' }}><input type="radio" name="q2" value="no" onChange={handleChange} /> No</label>
              </div>

              <div className="activity-item">
                <p>3. Would you rather lead a team and pitch business ideas?</p>
                <label><input type="radio" name="q3" value="yes" onChange={handleChange} required /> Yes</label>
                <label style={{ marginLeft: '20px' }}><input type="radio" name="q3" value="no" onChange={handleChange} /> No</label>
              </div>

              <button type="submit" className="btn-solid" disabled={loading} style={{ width: '100%', marginTop: '20px' }}>
                {loading ? "Processing..." : "Finish & Get Recommendations"}
              </button>
            </form>
          )}
        </div>
      </main>
    </div>
  );
}

export default AssessmentForm;