import { Route, Navigate } from 'react-router-dom';
import { jwtDecode } from 'jwt-decode';
import api from './api';
import { REFRESH_TOKEN, ACCESS_TOKEN } from './constants';
import { useEffect, useState } from 'react';

const PrivateRoute = ({ children }) => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [loading, setLoading] = useState(true);
  const refreshToken = async () => {
    // const refreshToken = localStorage.getItem(REFRESH_TOKEN);
    try {
      const response = await api.post('/api/token/refresh',
        {
          refresh: localStorage.getItem(REFRESH_TOKEN),
        });
      if (response.status === 200) {
        localStorage.setItem(ACCESS_TOKEN, response.data.access);
        setIsAuthenticated(true);
      } else {
        setIsAuthenticated(false);
        localStorage.removeItem(ACCESS_TOKEN);
        localStorage.removeItem(REFRESH_TOKEN);
      }
    } catch (error) {
      console.error('Error refreshing token:', error.message);
      setIsAuthenticated(false);
      localStorage.removeItem(ACCESS_TOKEN);
      localStorage.removeItem(REFRESH_TOKEN
      );
    }
  };
  useEffect(() => {
    checkAuth().catch(() => setIsAuthenticated(false));
  }, []);
  const checkAuth = async () => {
    const token = localStorage.getItem(ACCESS_TOKEN);
    if (!token) {
      setIsAuthenticated(false);
      setLoading(false);
      return;
    }
    const decoded = jwtDecode(token);
    if (decoded.exp * 1000 < Date.now()) {
      await refreshToken();
    } else {
      setIsAuthenticated(true);
      setLoading(false);
    }
  };
  console.log('private');
  return (
    loading ? (
      <div>Loading...</div>
    ) : isAuthenticated ? (
      children
    ) : (
      <Navigate to='/login' />
    )
  );
};
export default PrivateRoute;