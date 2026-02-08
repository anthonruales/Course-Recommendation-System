import React, { useState, useEffect } from "react";
import API_BASE_URL from '../config';

function ViewUser() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(false);
  const [selectedUser, setSelectedUser] = useState(null);
  const [searchTerm, setSearchTerm] = useState("");

  // Fetch all users on component mount
  useEffect(() => {
    fetchUsers();
    
    // Auto-refresh users list every 10 seconds
    const interval = setInterval(fetchUsers, 10000);
    return () => clearInterval(interval);
  }, []);

  const fetchUsers = async () => {
    setLoading(true);
    try {
      const response = await fetch(`${API_BASE_URL}/admin/users`);
      const data = await response.json();
      setUsers(data.users || []);
    } catch (err) {
      console.error('Error fetching users:', err);
    } finally {
      setLoading(false);
    }
  };

  const fetchUserDetails = async (userId) => {
    try {
      const response = await fetch(`${API_BASE_URL}/admin/users/${userId}`);
      const data = await response.json();
      setSelectedUser(data);
    } catch (err) {
      console.error('Error fetching user details:', err);
    }
  };

  const handleUserClick = (userId) => {
    fetchUserDetails(userId);
  };

  // Auto-refresh selected user details every 5 seconds when modal is open
  useEffect(() => {
    if (!selectedUser) return;
    
    const interval = setInterval(() => {
      fetchUserDetails(selectedUser.user_id);
    }, 5000);
    
    return () => clearInterval(interval);
  }, [selectedUser]);

  const handleRefresh = () => {
    fetchUsers();
  };

  const handleCloseModal = () => {
    setSelectedUser(null);
  };

  const filteredUsers = users.filter(user =>
    user.fullname.toLowerCase().includes(searchTerm.toLowerCase()) ||
    user.email.toLowerCase().includes(searchTerm.toLowerCase())
  );

  const formatDateTime = (dateTimeString) => {
    if (!dateTimeString) return "Never";
    try {
      const date = new Date(dateTimeString);
      return date.toLocaleString();
    } catch (e) {
      return dateTimeString;
    }
  };

  return (
    <div className="admin-page-container">
      <div className="admin-header-section">
        <h2 className="admin-title">View Users</h2>
        <p className="admin-subtitle">This section displays all registered users of the system.</p>
      </div>

      <div className="admin-card">
        <div style={{display: 'flex', gap: '10px', marginBottom: '20px'}}>
          <input 
            type="text" 
            className="admin-input" 
            placeholder="Search user..." 
            style={{flex: 1}} 
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
          />
          <button className="admin-btn-primary" onClick={handleRefresh}>
            {loading ? 'Loading...' : 'Refresh'}
          </button>
        </div>

        <div className="admin-table-wrapper">
          <table className="admin-table">
            <thead>
              <tr>
                <th>NAME</th>
                <th>EMAIL</th>
                <th>STRAND</th>
                <th>GWA</th>
                <th>TESTS TAKEN</th>
                <th>LAST ACTIVE</th>
                <th>ACTIONS</th>
              </tr>
            </thead>
            <tbody>
              {filteredUsers.length > 0 ? (
                filteredUsers.map((user) => (
                  <tr key={user.user_id}>
                    <td>{user.fullname || '-'}</td>
                    <td>{user.email}</td>
                    <td>
                      {user.academic_info && user.academic_info.strand ? (
                        <span className="admin-badge">{user.academic_info.strand}</span>
                      ) : (
                        <span className="admin-badge">-</span>
                      )}
                    </td>
                    <td>{user.academic_info && user.academic_info.gwa ? user.academic_info.gwa : 'N/A'}</td>
                    <td>{user.tests_taken}</td>
                    <td>{formatDateTime(user.last_active)}</td>
                    <td>
                      <button 
                        className="admin-btn-primary" 
                        style={{padding: '6px 12px', fontSize: '12px'}}
                        onClick={() => handleUserClick(user.user_id)}
                      >
                        View
                      </button>
                    </td>
                  </tr>
                ))
              ) : (
                <tr>
                  <td colSpan="7" style={{textAlign: 'center', color: '#999'}}>
                    {loading ? 'Loading users...' : 'No users found'}
                  </td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      </div>

      {/* User Details Modal */}
      {selectedUser && (
        <div style={modalStyles.overlay} onClick={handleCloseModal}>
          <div style={modalStyles.modal} onClick={(e) => e.stopPropagation()}>
            <div style={modalStyles.header}>
              <h2>{selectedUser.fullname}</h2>
              <button 
                onClick={handleCloseModal}
                style={modalStyles.closeBtn}
              >
                ✕
              </button>
            </div>
            
            <div style={modalStyles.content}>
              <div style={modalStyles.row}>
                <div style={modalStyles.column}>
                  <label style={modalStyles.label}>NAME:</label>
                  <p style={modalStyles.value}>{selectedUser.fullname}</p>
                </div>
                <div style={modalStyles.column}>
                  <label style={modalStyles.label}>EMAIL:</label>
                  <p style={modalStyles.value}>{selectedUser.email}</p>
                </div>
              </div>

              <div style={modalStyles.row}>
                <div style={modalStyles.column}>
                  <label style={modalStyles.label}>STRAND:</label>
                  <p style={modalStyles.value}>
                    {selectedUser.academic_info && selectedUser.academic_info.strand ? (
                      <span style={{background: '#006ba6', color: 'white', padding: '4px 8px', borderRadius: '4px', display: 'inline-block'}}>
                        {selectedUser.academic_info.strand}
                      </span>
                    ) : (
                      'N/A'
                    )}
                  </p>
                </div>
                <div style={modalStyles.column}>
                  <label style={modalStyles.label}>GWA:</label>
                  <p style={modalStyles.value}>{selectedUser.academic_info && selectedUser.academic_info.gwa ? selectedUser.academic_info.gwa : 'N/A'}</p>
                </div>
              </div>

              <div style={modalStyles.row}>
                <div style={modalStyles.column}>
                  <label style={modalStyles.label}>TESTS TAKEN:</label>
                  <p style={modalStyles.value}>{selectedUser.total_assessments}</p>
                </div>
                <div style={modalStyles.column}>
                  <label style={modalStyles.label}>LAST TEST:</label>
                  <p style={modalStyles.value}>{formatDateTime(selectedUser.last_test || selectedUser.last_active)}</p>
                </div>
              </div>

              <div style={modalStyles.row}>
                <div style={modalStyles.column}>
                  <label style={modalStyles.label}>LAST ACTIVE:</label>
                  <p style={modalStyles.value}>{formatDateTime(selectedUser.last_active)}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

const modalStyles = {
  overlay: {
    position: 'fixed',
    top: 0,
    left: 0,
    right: 0,
    bottom: 0,
    backgroundColor: 'rgba(0, 0, 0, 0.5)',
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    zIndex: 1000
  },
  modal: {
    backgroundColor: '#1e2a47',
    borderRadius: '8px',
    padding: '24px',
    maxWidth: '600px',
    width: '90%',
    maxHeight: '80vh',
    overflowY: 'auto',
    color: '#fff',
    border: '1px solid #3a4a63'
  },
  header: {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: '20px',
    borderBottom: '1px solid #3a4a63',
    paddingBottom: '12px'
  },
  closeBtn: {
    background: 'none',
    border: 'none',
    color: '#fff',
    fontSize: '24px',
    cursor: 'pointer'
  },
  content: {
    display: 'flex',
    flexDirection: 'column',
    gap: '16px'
  },
  row: {
    display: 'flex',
    gap: '32px',
    flexWrap: 'wrap'
  },
  column: {
    flex: '1',
    minWidth: '200px'
  },
  label: {
    display: 'block',
    fontSize: '12px',
    fontWeight: '600',
    color: '#7a8fa6',
    marginBottom: '6px',
    textTransform: 'uppercase',
    letterSpacing: '0.5px'
  },
  value: {
    fontSize: '14px',
    color: '#e0e6ed',
    margin: 0
  }
};

export default ViewUser;