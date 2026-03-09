function Hero() {
  return (
    <section className="hero-section">
      <div className="hero-left">
        <div className="badge">Smart ATS Resume Intelligence</div>

        <h1 className="hero-title">
          Turn Your Resume Into a <span>Job-Matching Machine</span>
        </h1>

        <p className="hero-text">
          Upload your resume, paste a job description, and instantly uncover
          your match score, missing keywords, and sharp improvements that make
          your application stronger.
        </p>

        <div className="hero-mini-stats">
          <div className="mini-stat">
            <span className="mini-stat-number">Fast</span>
            <span className="mini-stat-label">Instant analysis</span>
          </div>
          <div className="mini-stat">
            <span className="mini-stat-number">Smart</span>
            <span className="mini-stat-label">Keyword matching</span>
          </div>
          <div className="mini-stat">
            <span className="mini-stat-number">Clear</span>
            <span className="mini-stat-label">Actionable suggestions</span>
          </div>
        </div>
      </div>

      <div className="hero-right">
        <div className="hero-preview-card">
          <div className="preview-header">
            <span className="preview-dot pink"></span>
            <span className="preview-dot blue"></span>
            <span className="preview-dot cyan"></span>
          </div>

          <div className="preview-score-block">
            <p className="preview-label">Sample Match Score</p>
            <h2>86%</h2>
          </div>

          <div className="preview-bars">
            <div className="preview-bar long"></div>
            <div className="preview-bar medium"></div>
            <div className="preview-bar short"></div>
          </div>

          <div className="preview-tags">
            <span>Python</span>
            <span>FastAPI</span>
            <span>React</span>
            <span>REST API</span>
          </div>
        </div>
      </div>
    </section>
  );
}

export default Hero;