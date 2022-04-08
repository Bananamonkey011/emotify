import './App.css';
import UploadImage from './components/UploadImage';
import PythonCamera from './components/PythonCam'
function App() {
  return (
    <div className="App">
      {/* Webpage Header */}
      <h1 className='App-Title'>CV Spotify Recomendations</h1>

      {/* Main image capture component */}
      <UploadImage/>
      <PythonCamera/>
    </div>
  );
}

export default App;
