import React, { useState } from 'react';

function AssessmentForm({ onBack }) {
  const [formData, setFormData] = useState({ q1: '', q2: '', q3: '' });
  const [recommendation, setRecommendation] = useState(null); // To store the result
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
        // This formats your q1, q2, q3 into the list your backend expects
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
        setRecommendation(data); // Save the result to show on screen
      } else {
        alert("Failed to get recommendation. Check if backend is running.");
      }
    } catch (error) {
      console.error("Error:", error);
      alert("Connection error!");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="portal-layout">
      <main className="portal-main">
        <button onClick={onBack} style={{ marginBottom: '20px', cursor: 'pointer', background: 'none', border: 'none', color: '#3b82f6' }}>
          ← Cancel Assessment
        </button>

        <div className="portal-card" style={{ maxWidth: '700px', margin: '0 auto' }}>
          <header style={{ borderBottom: '1px solid #eee', marginBottom: '25px', paddingBottom: '10px' }}>
            <h2 style={{ margin: 0 }}>Career Interest Questionnaire</h2>
            <p style={{ color: '#666', fontSize: '14px' }}>Answer these situational questions for the Decision Tree analysis.</p>
          </header>

          {/* SHOW RECOMMENDATION HERE IF IT EXISTS */}
          {recommendation ? (
            <div style={{ padding: '20px', backgroundColor: '#f0f9ff', borderRadius: '8px', border: '1px solid #bae6fd', marginBottom: '20px' }}>
              <h3 style={{ color: '#0369a1', marginTop: 0 }}>Recommended Course:</h3>
              <p style={{ fontSize: '20px', fontWeight: 'bold' }}>{recommendation.recommendation}</p>
              <p style={{ color: '#555' }}>{recommendation.explanation}</p>
              <button onClick={() => setRecommendation(null)} className="btn-solid" style={{ marginTop: '10px' }}>Retake Assessment</button>
            </div>
          ) : (
            <form onSubmit={handleSubmit}>
              <div style={{ padding: '15px', borderBottom: '1px solid #f0f0f0', marginBottom: '10px' }}>
                <p>1. When faced with a broken gadget, do you prefer fixing it yourself rather than buying a new one?</p>
                <label><input type="radio" name="q1" value="yes" onChange={handleChange} required /> Yes</label>
                <label style={{ marginLeft: '20px' }}><input type="radio" name="q1" value="no" onChange={handleChange} /> No</label>
              </div>

              <div style={{ padding: '15px', borderBottom: '1px solid #f0f0f0', marginBottom: '10px' }}>
                <p>2. Do you enjoy analyzing data or conducting experiments to find the truth?</p>
                <label><input type="radio" name="q2" value="yes" onChange={handleChange} required /> Yes</label>
                <label style={{ marginLeft: '20px' }}><input type="radio" name="q2" value="no" onChange={handleChange} /> No</label>
              </div>

              <div style={{ padding: '15px', borderBottom: '1px solid #f0f0f0', marginBottom: '10px' }}>
                <p>3. Would you rather lead a team and pitch business ideas than work behind the scenes?</p>
                <label><input type="radio" name="q3" value="yes" onChange={handleChange} required /> Yes</label>
                <label style={{ marginLeft: '20px' }}><input type="radio" name="q3" value="no" onChange={handleChange} /> No</label>
              </div>

              <button type="submit" className="btn-solid" disabled={loading} style={{ width: '100%', padding: '15px', fontSize: '16px', marginTop: '20px' }}>
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