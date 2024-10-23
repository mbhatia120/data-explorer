import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate  } from 'react-router-dom';
import Upload from './components/Upload'; // Import the Upload component
import User from './components/User'; // Import the User component
import './App.css'
import SearchGames from './components/SearchGames';


function App() {
  
  // const VITE_FRONTEND  = import.meta.env.VITE_FRONTEND;

  return (
    <Router>
      <Routes>
        <Route path={`/home`}element={<Upload />} />
        <Route path={`/user/:username`} element={<User />} />
        {/* <Route path="/search" element={<SearchGames />} /> */}
        <Route path={`/`} element={<Navigate to={`/home`} replace />} />  
      </Routes>
    </Router>
  );
}

export default App;