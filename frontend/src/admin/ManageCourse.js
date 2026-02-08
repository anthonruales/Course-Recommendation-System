import React, { useState } from "react";

function ManageCourse() {
  const [courseName, setCourseName] = useState("");
  const [courseList, setCourseList] = useState([]);

  return (
    <div className="admin-page-container">
      <div className="admin-header-section">
        <h2 className="admin-title">Manage Courses</h2>
        <p className="admin-subtitle">Add, edit, or organize course list.</p>
      </div>

      <div className="admin-card">
        <form onSubmit={(e) => { e.preventDefault(); setCourseList([...courseList, {id: Date.now(), name: courseName}]); setCourseName(""); }} style={{display: 'flex', gap: '10px'}}>
          <input className="admin-input" style={{flex: 1}} type="text" placeholder="Enter course name..." value={courseName} onChange={(e) => setCourseName(e.target.value)} />
          <button className="admin-btn-primary">Add Course</button>
        </form>
      </div>

      <div className="admin-card">
        <table className="admin-table">
          <thead>
            <tr><th>Course Name</th><th>Actions</th></tr>
          </thead>
          <tbody>
            {courseList.map((c) => (
              <tr key={c.id}><td>{c.name}</td><td><button className="admin-btn-small">Edit</button></td></tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
export default ManageCourse;