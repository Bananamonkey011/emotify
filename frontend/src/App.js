import './App.css';
import UploadImage from './components/UploadImage';
import React, { Component }  from 'react';
function App() {
  return (
    <div className="App">
      {/* Webpage Header */}
      <h1 className='App-Title'>CV Spotify Recomendations</h1>

      {/* Main image capture component */}
      <UploadImage/>
    </div>
  );
}

export default App;
