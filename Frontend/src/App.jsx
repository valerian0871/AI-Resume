import { useState } from "react";
import Hero from "./components/Hero";
import AnalyzerForm from "./components/AnalyzerForm";
import ResultsPanel from "./components/ResultsPanel";
import "./index.css";

function App() {
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [resumeFile, setResumeFile] = useState(null);
  const [jobDescription, setJobDescription] = useState("");

  return (
    <div className="app-shell">
      <div className="mesh mesh-1"></div>
      <div className="mesh mesh-2"></div>
      <div className="mesh mesh-3"></div>
      <div className="floating-orb orb-1"></div>
      <div className="floating-orb orb-2"></div>
      <div className="floating-orb orb-3"></div>
      <div className="floating-orb orb-4"></div>
      <div className="floating-orb orb-5"></div>
      <div className="floating-orb orb-6"></div>
      <div className="floating-orb orb-7"></div>

      <main className="main-container">
        <header className="app-header">
          <img src="/logo.svg" alt="AI Resume Analyzer Logo" className="app-logo" />
          <span className="app-name">AI Resume Analyzer</span>
        </header>

        <Hero />
        <AnalyzerForm
          setResult={setResult}
          loading={loading}
          setLoading={setLoading}
          resumeFile={resumeFile}
          setResumeFile={setResumeFile}
          jobDescription={jobDescription}
          setJobDescription={setJobDescription}
        />
        <ResultsPanel
          result={result}
          loading={loading}
          resumeFile={resumeFile}
          jobDescription={jobDescription}
        />
      </main>
    </div>
  );
}

export default App;