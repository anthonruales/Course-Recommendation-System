import axios from 'axios';

/**
 * Decode the JWT payload without a library.
 * JWTs are base64url-encoded JSON — we just parse the middle segment.
 * Returns { user_id, username, email, name, is_admin, exp } or null.
 */
export function getUserFromToken() {
  const token = localStorage.getItem('accessToken');
  if (!token) return null;
  try {
    const payload = token.split('.')[1];
    const json = atob(payload.replace(/-/g, '+').replace(/_/g, '/'));
    return JSON.parse(json);
  } catch {
    return null;
  }
}

/**
 * Pre-configured Axios instance that automatically attaches the JWT
 * Authorization header to every request.
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
      localStorage.removeItem('accessToken');
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
