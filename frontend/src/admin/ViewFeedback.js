import React, { useState, useEffect } from 'react';
import API_BASE_URL from '../config';
import './ViewFeedback.css';

function ViewFeedback() {
  const [activeTab, setActiveTab] = useState('stats');
  const [stats, setStats] = useState(null);
  const [courseFeedback, setCourseFeedback] = useState(null);
  const [lowRated, setLowRated] = useState(null);
  const [selectedCourseId, setSelectedCourseId] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    loadFeedbackStats();
  }, []);

  const loadFeedbackStats = async () => {
    setLoading(true);
    setError(null);
    try {
      const response = await fetch(`${API_BASE_URL}/admin/feedback/stats`);
      if (response.ok) {
        const data = await response.json();
        setStats(data);
      } else {
        setError('Failed to load feedback statistics');
      }
    } catch (err) {
      setError('Error loading data: ' + err.message);
    } finally {
      setLoading(false);
    }
  };

  const loadLowRated = async () => {
    setLoading(true);
    try {
      const response = await fetch(`${API_BASE_URL}/admin/feedback/low-rated?min_rating=3`);
      if (response.ok) {
        const data = await response.json();
        setLowRated(data);
      }
    } catch (err) {
      setError('Error loading low-rated feedback: ' + err.message);
    } finally {
      setLoading(false);
    }
  };

  const loadCourseFeedback = async (courseId) => {
    setLoading(true);
    try {
      const response = await fetch(`${API_BASE_URL}/admin/feedback/courses/${courseId}`);
      if (response.ok) {
        const data = await response.json();
        setCourseFeedback(data);
      }
    } catch (err) {
      setError('Error loading course feedback: ' + err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleDeleteFeedback = async (feedbackId) => {
    if (!window.confirm('Delete this feedback?')) return;
    
    try {
      const response = await fetch(`${API_BASE_URL}/admin/feedback/${feedbackId}`, {
        method: 'DELETE'
      });
      
      if (response.ok) {
        alert('Feedback deleted successfully');
        // Refresh current view
        if (activeTab === 'stats') {
          loadFeedbackStats();
        } else if (activeTab === 'course' && courseFeedback) {
          loadCourseFeedback(courseFeedback.course_id);
        } else if (activeTab === 'low-rated') {
          loadLowRated();
        }
      }
    } catch (err) {
      alert('Error deleting feedback: ' + err.message);
    }
  };

  const getRatingStars = (rating) => {
    return '★'.repeat(rating) + '☆'.repeat(5 - rating);
  };

  if (loading && !stats && !lowRated && !courseFeedback) {
    return <div className="view-feedback-container">Loading feedback data...</div>;
  }

  return (
    <div className="view-feedback-container">
      <h1>📊 Recommendation Feedback Analytics</h1>

      {error && <div className="error-message">{error}</div>}

      {/* Tabs */}
      <div className="feedback-tabs">
        <button
          className={`tab-btn ${activeTab === 'stats' ? 'active' : ''}`}
          onClick={() => {
            setActiveTab('stats');
            loadFeedbackStats();
          }}
        >
          📈 Overall Stats
        </button>
        <button
          className={`tab-btn ${activeTab === 'low-rated' ? 'active' : ''}`}
          onClick={() => {
            setActiveTab('low-rated');
            loadLowRated();
          }}
        >
          ⚠️ Low Ratings (Alerts)
        </button>
        <button
          className={`tab-btn ${activeTab === 'course' ? 'active' : ''}`}
          onClick={() => {
            setActiveTab('course');
            if (stats && stats.top_courses.length > 0) {
              loadCourseFeedback(stats.top_courses[0].course_id);
              setSelectedCourseId(stats.top_courses[0].course_id);
            }
          }}
        >
          🎓 Course Details
        </button>
      </div>

      {/* Overall Stats Tab */}
      {activeTab === 'stats' && stats && (
        <div className="tab-content">
          <div className="stats-grid">
            <div className="stat-card">
              <div className="stat-value">{stats.total_feedbacks}</div>
              <div className="stat-label">Total Feedbacks</div>
            </div>
            <div className="stat-card">
              <div className="stat-value">{stats.average_rating.toFixed(1)}/5</div>
              <div className="stat-label">Average Rating</div>
            </div>
            <div className="stat-card">
              <div className="stat-value">{stats.rating_distribution['5']}</div>
              <div className="stat-label">5-Star Reviews</div>
            </div>
            <div className="stat-card">
              <div className="stat-value">{stats.rating_distribution['1']}</div>
              <div className="stat-label">1-Star Reviews</div>
            </div>
          </div>

          {/* Rating Distribution */}
          <div className="chart-section">
            <h3>Rating Distribution</h3>
            <div className="rating-distribution">
              {[5, 4, 3, 2, 1].map((rating) => {
                const count = stats.rating_distribution[String(rating)];
                const percentage =
                  stats.total_feedbacks > 0
                    ? ((count / stats.total_feedbacks) * 100).toFixed(1)
                    : 0;

                return (
                  <div key={rating} className="rating-bar">
                    <div className="rating-label">
                      {'★'.repeat(rating)}
                      {'☆'.repeat(5 - rating)} ({count})
                    </div>
                    <div className="bar-container">
                      <div
                        className="bar-fill"
                        style={{
                          width: `${percentage}%`,
                          backgroundColor: rating >= 4 ? '#28a745' : rating === 3 ? '#ffc107' : '#dc3545'
                        }}
                      ></div>
                    </div>
                    <div className="percentage">{percentage}%</div>
                  </div>
                );
              })}
            </div>
          </div>

          {/* Top Courses by Feedback */}
          <div className="top-courses-section">
            <h3>Top Courses by Feedback</h3>
            <div className="courses-list">
              {stats.top_courses.map((course, idx) => (
                <div key={idx} className="course-item">
                  <div className="course-info">
                    <div className="rank">#{idx + 1}</div>
                    <div className="details">
                      <h4>{course.course_name}</h4>
                      <p>{course.feedback_count} feedbacks • {getRatingStars(Math.round(course.avg_rating))}</p>
                    </div>
                  </div>
                  <div className="avg-rating">{course.avg_rating.toFixed(1)}/5</div>
                </div>
              ))}
            </div>
          </div>
        </div>
      )}

      {/* Low Rated Alerts Tab */}
      {activeTab === 'low-rated' && lowRated && (
        <div className="tab-content">
          <div className="alert-header">
            <h3>⚠️ Low Ratings Alert (Below 3 Stars)</h3>
            <p>{lowRated.total_low_rated} recommendations rated as {lowRated.threshold} stars or below</p>
          </div>

          <div className="alerts-list">
            {lowRated.alerts.length > 0 ? (
              lowRated.alerts.map((alert, idx) => (
                <div key={idx} className="alert-item">
                  <div className="alert-rating">
                    {getRatingStars(alert.rating)}
                  </div>
                  <div className="alert-details">
                    <h4>{alert.course_name}</h4>
                    <p className="user-info">By {alert.user_name}</p>
                    {alert.feedback_text && (
                      <p className="feedback-text">"{alert.feedback_text}"</p>
                    )}
                    <p className="reasoning">
                      <strong>Why recommended:</strong> {alert.recommendation_reasoning}
                    </p>
                    <small>{new Date(alert.created_at).toLocaleDateString()}</small>
                  </div>
                  <button
                    className="delete-btn"
                    onClick={() => handleDeleteFeedback(alert.feedback_id)}
                    title="Delete feedback"
                  >
                    🗑️
                  </button>
                </div>
              ))
            ) : (
              <p className="no-data">✅ All recommendations have good ratings!</p>
            )}
          </div>
        </div>
      )}

      {/* Course Details Tab */}
      {activeTab === 'course' && stats && (
        <div className="tab-content">
          <div className="course-selector">
            <label>Select Course:</label>
            <select
              value={selectedCourseId || ''}
              onChange={(e) => {
                const courseId = parseInt(e.target.value);
                setSelectedCourseId(courseId);
                loadCourseFeedback(courseId);
              }}
            >
              {stats.top_courses.map((course, idx) => (
                <option key={idx} value={course.course_id || idx}>
                  {course.course_name}
                </option>
              ))}
            </select>
          </div>

          {courseFeedback && (
            <div className="course-feedback-detail">
              <div className="course-header">
                <h3>{courseFeedback.course_name}</h3>
                <div className="course-stats">
                  <span className="avg-rating-large">{courseFeedback.average_rating.toFixed(1)}/5</span>
                  <span className="feedback-count">{courseFeedback.total_feedbacks} feedbacks</span>
                </div>
              </div>

              {/* Rating Breakdown */}
              <div className="rating-breakdown">
                {[5, 4, 3, 2, 1].map((rating) => {
                  const count = courseFeedback.rating_breakdown[String(rating)];
                  const percentage =
                    courseFeedback.total_feedbacks > 0
                      ? ((count / courseFeedback.total_feedbacks) * 100).toFixed(1)
                      : 0;

                  return (
                    <div key={rating} className="breakdown-item">
                      <div className="stars">{getRatingStars(rating)}</div>
                      <div className="bar-container">
                        <div
                          className="bar-fill"
                          style={{
                            width: `${percentage}%`,
                            backgroundColor: rating >= 4 ? '#28a745' : rating === 3 ? '#ffc107' : '#dc3545'
                          }}
                        ></div>
                      </div>
                      <span className="count">{count}</span>
                    </div>
                  );
                })}
              </div>

              {/* All Feedbacks */}
              <h4>All Feedbacks</h4>
              <div className="feedbacks-grid">
                {courseFeedback.feedbacks.map((feedback, idx) => (
                  <div key={idx} className="feedback-card">
                    <div className="feedback-header-card">
                      <div className="stars-small">{getRatingStars(feedback.rating)}</div>
                      <button
                        className="delete-btn-small"
                        onClick={() => handleDeleteFeedback(feedback.feedback_id)}
                        title="Delete feedback"
                      >
                        ×
                      </button>
                    </div>
                    {feedback.feedback_text && (
                      <p className="feedback-comment">"{feedback.feedback_text}"</p>
                    )}
                    <p className="feedback-meta">
                      - {feedback.user_name} on {new Date(feedback.created_at).toLocaleDateString()}
                    </p>
                  </div>
                ))}
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  );
}

export default ViewFeedback;
