import React from 'react';
import HomePage from './pages/HomePage';
import AdvocatePage from './pages/AdvocatePage';
import Nav from './components/Nav';
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
    <div className='container mx-auto'>
      <Nav />
      <RouterProvider router={router} />
    </div>
  );
}

export default App;
