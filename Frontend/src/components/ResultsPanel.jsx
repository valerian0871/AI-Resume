function ResultsPanel({ result, loading }) {
  if (loading) {
    return (
      <section className="results-card loading-card">
        <h2>Analyzing your resume...</h2>
        <p>
          We are comparing your resume against the job description and generating
          ATS-aware rewrite suggestions.
        </p>
        <div className="loading-shimmer"></div>
      </section>
    );
  }

  if (!result) {
    return (
      <section className="results-card empty-results-card">
        <h2>Your insights will appear here</h2>
        <p>
          Once you run an analysis, you’ll see your score, matched skills,
          missing keywords, rewrite help, and an optimized resume draft here.
        </p>
      </section>
    );
  }

  const rewrite = result.tailored_resume_suggestions;
  const draft = result.optimized_resume_draft;

  return (
    <section className="results-wrapper">
      <div className="results-top-grid">
        <div className="result-score-card">
          <p className="score-label">Resume Match</p>
          <div className="score-circle">{result.match_score}%</div>
          <p className="score-description">
            This score reflects how closely your resume aligns with the target role.
          </p>
        </div>

        <div className="quick-insight-card">
          <h3>Quick Insight</h3>
          <p>
            {result.match_score >= 75
              ? "Strong alignment. Focus on polishing achievements and impact."
              : result.match_score >= 50
              ? "Decent alignment. You have a good base, but important terms are still missing."
              : "Low alignment. Your resume needs much stronger tailoring for this role."}
          </p>
        </div>
      </div>

      <div className="results-grid">
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

        <div className="result-list-card full-width rewrite-card">
          <h3>Tailored Resume Rewrite</h3>

          <div className="rewrite-block">
            <h4>Improved Summary</h4>
            <p>{rewrite.improved_summary}</p>
          </div>

          <div className="rewrite-block">
            <h4>Suggested Skills</h4>
            <div className="tag-list">
              {rewrite.suggested_skills.map((item, index) => (
                <span key={index} className="tag rewrite-tag">
                  {item}
                </span>
              ))}
            </div>
          </div>

          <div className="rewrite-block">
            <h4>Bullet Point Improvements</h4>
            <div className="suggestions-list">
              {rewrite.bullet_point_improvements.map((item, index) => (
                <div key={index} className="suggestion-item">
                  {item}
                </div>
              ))}
            </div>
          </div>

          <div className="rewrite-block">
            <h4>Project Suggestions</h4>
            <div className="suggestions-list">
              {rewrite.project_suggestions.map((item, index) => (
                <div key={index} className="suggestion-item">
                  {item}
                </div>
              ))}
            </div>
          </div>
        </div>

        <div className="result-list-card full-width optimized-draft-card">
          <h3>Optimized Resume Draft</h3>

          <div className="rewrite-block">
            <h4>Professional Summary</h4>
            <p>{draft.professional_summary}</p>
          </div>

          <div className="rewrite-block">
            <h4>Key Skills</h4>
            <div className="tag-list">
              {draft.key_skills.map((item, index) => (
                <span key={index} className="tag draft-tag">
                  {item}
                </span>
              ))}
            </div>
          </div>

          <div className="rewrite-block">
            <h4>Experience Bullets</h4>
            <div className="suggestions-list">
              {draft.experience_bullets.map((item, index) => (
                <div key={index} className="suggestion-item">
                  {item}
                </div>
              ))}
            </div>
          </div>

          <div className="rewrite-block">
            <h4>Project Bullets</h4>
            <div className="suggestions-list">
              {draft.project_bullets.map((item, index) => (
                <div key={index} className="suggestion-item">
                  {item}
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

export default ResultsPanel;