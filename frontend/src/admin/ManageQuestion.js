import React, { useState } from "react";

const ManageQuestion = () => {
  const [questions] = useState([
    { id: 1, question: "What motivates you to study the most?", category: "General" },
  ]);

  return (
    <div className="admin-page-container">
      <div className="admin-header-section">
        <h1 className="admin-title">Manage Questions</h1>
        <button className="admin-btn-primary" style={{marginTop: '10px'}}>+ Add Question</button>
      </div>

      <div className="admin-card">
        <table className="admin-table">
          <thead>
            <tr><th>ID</th><th>Question</th><th>Category</th><th>Actions</th></tr>
          </thead>
          <tbody>
            {questions.map((q) => (
              <tr key={q.id}>
                <td>{q.id}</td><td>{q.question}</td><td>{q.category}</td>
                <td>
                  <button className="admin-btn-small">Edit</button>
                  <button className="admin-btn-small" style={{color: 'red'}}>Delete</button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};
export default ManageQuestion;