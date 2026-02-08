// API Configuration
// In development: uses localhost
// In production: uses the deployed backend URL

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

export default API_BASE_URL;
