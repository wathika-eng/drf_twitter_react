import React from 'react';
import HomePage from './pages/HomePage';
import AdvocatePage from './pages/AdvocatePage';
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";

const router = createBrowserRouter([
  {
    path: "/",
    element: < HomePage />,
  },
  {
    path: "/advocate/:username",
    element: <AdvocatePage />,
  }
]);
function App() {

  return (
    <RouterProvider router={router} />
  );
}

export default App;
