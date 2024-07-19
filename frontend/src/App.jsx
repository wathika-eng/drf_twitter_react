// src/App.jsx
import React from 'react';
import HomePage from './pages/HomePage';
import AdvocatePage from './pages/AdvocatePage';
import Layout from './components/Layout'; // Import the Layout component
import { createBrowserRouter, RouterProvider } from 'react-router-dom';

const router = createBrowserRouter([
  {
    path: "/",
    element: <Layout />, // Use the Layout component
    children: [
      {
        path: "/", // Home page route
        element: <HomePage />,
      },
      {
        path: "/advocate/:username", // Advocate page route
        element: <AdvocatePage />,
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
