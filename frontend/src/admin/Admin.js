import React, { useState } from "react";
import "../components/style/Admin.css"; 

import ManageQuestion from "./ManageQuestion";
import ViewReport from "./ViewReport";
import ManageCourse from "./ManageCourse";
import ViewUser from "./ViewUser";
import ViewFeedback from "./ViewFeedback";

function Admin({ onLogout }) {
  const [activeTab, setActiveTab] = useState("viewuser");

  return (
    <div className="admin-layout">
      
      {/* 1. SIDEBAR */}
      <div className="admin-sidebar">
        <h2>CoursePro Admin</h2>
        
        <nav>
          <ul>
            <li 
              className={`sidebar-item ${activeTab === "viewuser" ? "active" : ""}`}
              onClick={() => setActiveTab("viewuser")}
            >
              View Users
            </li>
            <li 
              className={`sidebar-item ${activeTab === "courses" ? "active" : ""}`}
              onClick={() => setActiveTab("courses")}
            >
              Manage Courses
            </li>
            <li 
              className={`sidebar-item ${activeTab === "reports" ? "active" : ""}`}
              onClick={() => setActiveTab("reports")}
            >
              View Reports
            </li>
            <li 
              className={`sidebar-item ${activeTab === "questions" ? "active" : ""}`}
              onClick={() => setActiveTab("questions")}
            >
              Manage Questions
            </li>
            <li 
              className={`sidebar-item ${activeTab === "feedback" ? "active" : ""}`}
              onClick={() => setActiveTab("feedback")}
            >
              Feedback Analytics
            </li>
          </ul>
        </nav>

        <button onClick={onLogout} className="logout-btn-sidebar">
          Logout
        </button>
      </div>

      {/* 2. MAIN CONTENT */}
      <div className="admin-main-content">
        {activeTab === "viewuser" && <ViewUser />}
        {activeTab === "courses" && <ManageCourse />}
        {activeTab === "reports" && <ViewReport />}
        {activeTab === "questions" && <ManageQuestion />}
        {activeTab === "feedback" && <ViewFeedback />}
      </div>

    </div>
  );
}

export default Admin;