import { useState } from "react";
import Hero from "./components/Hero";
import AnalyzerForm from "./components/AnalyzerForm";
import ResultsPanel from "./components/ResultsPanel";
import "./index.css";

function App() {
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  return (
    <div className="app-shell">
      <div className="background-glow glow-one"></div>
      <div className="background-glow glow-two"></div>
      <div className="background-glow glow-three"></div>

      <main className="main-container">
        <Hero />
        <AnalyzerForm
          setResult={setResult}
          loading={loading}
          setLoading={setLoading}
        />
        <ResultsPanel result={result} loading={loading} />
      </main>
    </div>
  );
}

export default App;