function ResultsPanel({ result, loading }) {
  if (loading) {
    return (
      <section className="results-card">
        <h2>Analyzing your resume...</h2>
        <p>Please wait while we compare it with the job description.</p>
      </section>
    );
  }

  if (!result) {
    return (
      <section className="results-card">
        <h2>Your results will appear here</h2>
        <p>
          Upload your resume and paste a job description to see your match
          score, matched keywords, missing keywords, and improvement tips.
        </p>
      </section>
    );
  }

  return (
    <section className="results-grid">
      <div className="result-score-card">
        <h2>Match Score</h2>
        <div className="score-circle">{result.match_score}%</div>
      </div>

      <div className="result-list-card">
        <h3>Matched Keywords</h3>
        <div className="tag-list">
          {result.matched_keywords.length > 0 ? (
            result.matched_keywords.map((item, index) => (
              <span key={index} className="tag success-tag">
                {item}
              </span>
            ))
          ) : (
            <p>No matched keywords yet.</p>
          )}
        </div>
      </div>

      <div className="result-list-card">
        <h3>Missing Keywords</h3>
        <div className="tag-list">
          {result.missing_keywords.length > 0 ? (
            result.missing_keywords.map((item, index) => (
              <span key={index} className="tag danger-tag">
                {item}
              </span>
            ))
          ) : (
            <p>No missing keywords.</p>
          )}
        </div>
      </div>

      <div className="result-list-card full-width">
        <h3>Improvement Suggestions</h3>
        <div className="suggestions-list">
          {result.improvement_suggestions.map((item, index) => (
            <div key={index} className="suggestion-item">
              {item}
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

export default ResultsPanel;