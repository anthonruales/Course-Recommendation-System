import React, { useState } from 'react';
import './FeedbackForm.css';

function FeedbackForm({ recommendation, onSubmit, onClose }) {
  const [rating, setRating] = useState(0);
  const [hoverRating, setHoverRating] = useState(0);
  const [feedbackText, setFeedbackText] = useState('');
  const [loading, setLoading] = useState(false);
  const [submitted, setSubmitted] = useState(false);

  const isOverallFeedback = recommendation?.overall === true;

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (rating === 0) {
      alert('Please select a rating');
      return;
    }

    setLoading(true);

    try {
      const endpoint = isOverallFeedback ? '/feedback/submit' : '/feedback/submit';
      
      const payload = isOverallFeedback 
        ? { rating: rating, feedback_text: feedbackText || null }
        : {
            recommendation_id: recommendation.recommendation_id,
            rating: rating,
            feedback_text: feedbackText || null
          };

      const response = await fetch(`http://localhost:8000${endpoint}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(payload)
      });

      if (response.ok) {
        const data = await response.json();
        setSubmitted(true);
        if (onSubmit) {
          onSubmit(data);
        }
        // Auto close after 2 seconds
        setTimeout(() => onClose && onClose(), 2000);
      } else {
        alert('Error submitting feedback');
      }
    } catch (error) {
      console.error('Error:', error);
      alert('Failed to submit feedback');
    } finally {
      setLoading(false);
    }
  };

  if (submitted) {
    return (
      <div className="feedback-form">
        <div className="feedback-success">
          <h3>✅ Thank You!</h3>
          <p>Your feedback helps us improve recommendations.</p>
        </div>
      </div>
    );
  }

  return (
    <div className="feedback-form">
      <div className="feedback-overlay" onClick={onClose}></div>
      <div className="feedback-modal">
        <div className="feedback-header">
          <h2>Rate This Recommendation</h2>
          <button className="close-btn" onClick={onClose}>×</button>
        </div>

        <div className="feedback-content">
          <div className="course-info">
            <h3>{isOverallFeedback ? 'Rate Your Recommendations' : recommendation.course_name}</h3>
            {!isOverallFeedback && <p>{recommendation.reasoning}</p>}
          </div>

          <form onSubmit={handleSubmit}>
            <div className="rating-section">
              <label>{isOverallFeedback ? 'How helpful were these recommendations?' : 'How helpful was this recommendation?'}</label>
              <div className="star-rating">
                {[1, 2, 3, 4, 5].map((star) => (
                  <span
                    key={star}
                    className={`star ${star <= (hoverRating || rating) ? 'active' : ''}`}
                    onClick={() => setRating(star)}
                    onMouseEnter={() => setHoverRating(star)}
                    onMouseLeave={() => setHoverRating(0)}
                  >
                    ★
                  </span>
                ))}
              </div>
              <div className="rating-labels">
                <span>Not helpful</span>
                <span className="current-rating">
                  {rating > 0 ? ['Poor', 'Fair', 'Good', 'Very Good', 'Excellent'][rating - 1] : 'Select rating'}
                </span>
                <span>Very helpful</span>
              </div>
            </div>

            <div className="feedback-text-section">
              <label htmlFor="feedback">Additional Comments (Optional)</label>
              <textarea
                id="feedback"
                placeholder="Tell us why... (e.g., 'I love coding and this matches perfectly!' or 'Not interested in this field')"
                value={feedbackText}
                onChange={(e) => setFeedbackText(e.target.value)}
                maxLength={500}
              />
              <small>{feedbackText.length}/500 characters</small>
            </div>

            <div className="feedback-actions">
              <button type="button" className="btn-cancel" onClick={onClose}>
                Skip
              </button>
              <button type="submit" className="btn-submit" disabled={loading}>
                {loading ? 'Submitting...' : 'Submit Feedback'}
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}

export default FeedbackForm;
