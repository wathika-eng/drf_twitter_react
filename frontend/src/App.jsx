// src/App.jsx
import React from 'react';
import HomePage from './pages/HomePage';
import AdvocatePage from './pages/AdvocatePage';
import Layout from './components/Layout';
import Login from './pages/Login';
import Signup from './pages/Signup';
import { createBrowserRouter, RouterProvider, Navigate } from 'react-router-dom';
import PrivateRoute from './utils/PrivateRoute';

const Logout = () => {
  localStorage.clear();
  return <Navigate to='/login' />;
};
const router = createBrowserRouter([
  {
    path: "/",
    element: <Layout />,
    children: [
      {
        path: "/",
        element: <PrivateRoute>
          <HomePage />
        </PrivateRoute>
      },
      {
        path: "/advocate/:username",
        element: <AdvocatePage />,
      },
      {
        path: "/login",
        element: <Login />,

      },
      {
        path: "/signup",
        element: <Signup />,
      },
      {
        path: "/logout",
        element: <Logout />,
      },
      // redirect on wrong path
      {
        path: "*",
        element: <Navigate to="/" />
      }
    ]
  }
]);

function App() {
  return (
    <RouterProvider router={router} />
  );
}

export default App;

// const Logout = () => {
//   localStorage.clear();
//   return <Navigate to='/login' />;
// };
// const RegandLogout = () => {
//   localStorage.clear();
//   return <Signup />;
// };