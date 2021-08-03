import './App.css';
import React, { useState, useEffect } from 'react';
import {BrowserRouter as Router, Route} from 'react-router-dom'
import HomePage from './pages/HomePage';

function App() {
  return (
    <div className="App">
      <Router>
        <Route exact path = '/' component={HomePage} />
      </Router>
    </div>
  );
}

export default App;
