import React from "react";

function ViewUser() {
  return (
    <div className="admin-page-container">
      <div className="admin-header-section">
        <h2 className="admin-title">View Users</h2>
        <p className="admin-subtitle">This section displays all registered users of the system.</p>
      </div>

      <div className="admin-card">
        <div style={{display: 'flex', gap: '10px', marginBottom: '20px'}}>
          <input type="text" className="admin-input" placeholder="Search user..." style={{flex: 1}} />
          <button className="admin-btn-primary">Search</button>
        </div>

        <table className="admin-table">
          <thead>
            <tr><th>User ID</th><th>Full Name</th><th>Email</th><th>Role</th></tr>
          </thead>
          <tbody>
            <tr><td>101</td><td>John Vincent Bonotan</td><td>onlineclass@gmail.com</td><td>Student</td></tr>
          </tbody>
        </table>
      </div>
    </div>
  );
}
export default ViewUser;