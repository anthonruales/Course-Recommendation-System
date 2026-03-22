import axios from 'axios';

/**
 * Decode the JWT payload stored in localStorage.
 * Returns { user_id, username, email, is_admin } or null if no valid token.
 */
export function getTokenPayload() {
  const token = localStorage.getItem('accessToken');
  if (!token) return null;
  try {
    const base64Url = token.split('.')[1];
    const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
    const payload = JSON.parse(atob(base64));
    return payload;
  } catch {
    return null;
  }
}

/**
 * Pre-configured Axios instance that automatically attaches the JWT
 * Authorization header to every request.
 *
 * Usage:
 *   import api from './api';
 *   const res = await api.get('/user/1/academic-info');
 */
const api = axios.create({
  baseURL: process.env.REACT_APP_API_URL,
});

// ---- request interceptor: attach token ----
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('accessToken');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// ---- response interceptor: handle 401 ----
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response && error.response.status === 401) {
      // Token expired or invalid — clear auth state and redirect to login
      localStorage.removeItem('accessToken');
      localStorage.removeItem('userName');
      // Only reload if we're not already on the landing/login page
      if (window.location.hash !== '#/landing' && window.location.hash !== '#/login') {
        window.location.hash = '#/landing';
        window.location.reload();
      }
    }
    return Promise.reject(error);
  }
);

/**
 * Helper for native fetch() calls that need auth headers.
 * Returns a headers object with Authorization included.
 */
export function authHeaders(extra = {}) {
  const token = localStorage.getItem('accessToken');
  const headers = { 'Content-Type': 'application/json', ...extra };
  if (token) {
    headers['Authorization'] = `Bearer ${token}`;
  }
  return headers;
}

/**
 * Authenticated fetch wrapper.
 * Drop-in replacement for fetch() that adds the JWT header.
 */
export function authFetch(url, options = {}) {
  const token = localStorage.getItem('accessToken');
  const headers = { ...(options.headers || {}) };
  if (token) {
    headers['Authorization'] = `Bearer ${token}`;
  }
  return fetch(url, { ...options, headers });
}

export default api;
