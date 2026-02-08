import React from "react";

function ViewReport() {
  return (
    <div className="admin-page-container">
      <div className="admin-header-section">
        <h2 className="admin-title">View Reports</h2>
        <p className="admin-subtitle">Here you can generate and view system usage reports.</p>
      </div>

      <div className="admin-card">
        <div className="admin-controls-row">
          <input type="date" className="admin-input flex-1" />
          <select className="admin-input flex-1">
            <option>Filter by Activity Type</option>
            <option>User Login</option>
            <option>Test Results</option>
            <option>Course Recommendations</option>
          </select>
          <button className="admin-btn-primary">Apply Filter</button>
        </div>
      </div>

      <div className="admin-card">
        <div className="admin-table-wrapper">
          <table className="admin-table">
            <thead>
              <tr>
                <th>Date</th>
                <th>User</th>
                <th>Activity</th>
                <th>Details</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td className="text-muted">wala muna</td>
                <td className="text-muted">wala muna</td>
                <td className="text-centered-placeholder">No data available</td>
                <td className="text-muted">wala muna</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

export default ViewReport;