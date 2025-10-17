import { Routes, Route } from "react-router-dom";
import LandingPage from "./components/landingPage/LandingPage";
import Application from "./components/app/Application";

function App() {
  return (
    <Routes>
      <Route path="/" element={<LandingPage />} />
      <Route path="/app" element={<Application />} />
    </Routes>
  );
}

export default App;
