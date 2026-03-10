import { useState } from "react";
import { analyzeResume, exportResumeDocx } from "../services/api";

function AnalyzerForm({ setResult, loading, setLoading }) {
  const [resumeFile, setResumeFile] = useState(null);
  const [jobDescription, setJobDescription] = useState("");
  const [exporting, setExporting] = useState(false);

  const validateInputs = () => {
    if (!resumeFile || !jobDescription.trim()) {
      alert("Please upload a resume and paste a job description.");
      return false;
    }
    return true;
  };

  const buildFormData = () => {
    const formData = new FormData();
    formData.append("resume", resumeFile);
    formData.append("job_description", jobDescription);
    return formData;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!validateInputs()) return;

    try {
      setLoading(true);
      const data = await analyzeResume(buildFormData());
      setResult(data);
    } catch (error) {
      console.error(error);
      alert("Something went wrong while analyzing the resume.");
    } finally {
      setLoading(false);
    }
  };

  const handleExportDocx = async () => {
    if (!validateInputs()) return;

    try {
      setExporting(true);

      const blob = await exportResumeDocx(buildFormData());
      const url = window.URL.createObjectURL(
        new Blob([blob], {
          type: "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        })
      );

      const link = document.createElement("a");
      link.href = url;
      link.setAttribute("download", "optimized_resume.docx");
      document.body.appendChild(link);
      link.click();
      link.remove();

      window.URL.revokeObjectURL(url);
    } catch (error) {
      console.error(error);
      alert("Something went wrong while exporting the resume.");
    } finally {
      setExporting(false);
    }
  };

  return (
    <section className="form-card">
      <div className="section-heading">
        <h2>Start Your Analysis</h2>
        <p>
          Upload your resume and compare it against a target role in seconds.
        </p>
      </div>

      <form onSubmit={handleSubmit} className="analyzer-form">
        <div className="form-grid">
          <div className="upload-panel">
            <label className="upload-label">Upload Resume (PDF)</label>

            <label className="upload-box">
              <input
                type="file"
                accept=".pdf"
                onChange={(e) => setResumeFile(e.target.files[0])}
                hidden
              />
              <div className="upload-icon">↑</div>
              <p className="upload-title">
                {resumeFile ? resumeFile.name : "Drop your resume here or click to upload"}
              </p>
              <span className="upload-subtext">
                PDF only • Optimized for ATS-style analysis
              </span>
            </label>
          </div>

          <div className="textarea-panel">
            <label className="upload-label">Paste Job Description</label>
            <textarea
              rows="10"
              placeholder="Paste the full job description here so the analyzer can compare skills, phrases, and section relevance..."
              value={jobDescription}
              onChange={(e) => setJobDescription(e.target.value)}
            />
          </div>
        </div>

        <div className="form-actions">
          <button type="submit" className="analyze-btn" disabled={loading}>
            {loading ? "Analyzing Resume..." : "Analyze Resume Now"}
          </button>

          <button
            type="button"
            className="export-btn"
            disabled={exporting || loading}
            onClick={handleExportDocx}
          >
            {exporting ? "Exporting DOCX..." : "Download Optimized Resume"}
          </button>
        </div>
      </form>
    </section>
  );
}

export default AnalyzerForm;