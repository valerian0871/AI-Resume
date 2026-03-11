# AI Resume Analyzer

A full-stack web application that allows users to upload their resumes (PDF) and paste a job description. The application then analyzes the resume against the target role using OpenAI's API to provide an ATS match score, keyword analysis, customized improvement suggestions, and a tailored resume summary and experience bullets.

## Features

- **Instant Analysis:** Compares your resume to a target job description in seconds.
- **Smart ATS Keyword Matching:** Identifies matched and missing keywords dynamically.
- **Actionable Rewrite Suggestions:** Uses AI to generate a tailored professional summary and custom bullet points designed to rank higher in ATS systems.
- **Premium User Interface:** A stunning, modern interface with glassmorphism, animated backgrounds, and dynamic typography (`Outfit` and `Plus Jakarta Sans`).

---

## Tech Stack

### Frontend
- **React 18** + **Vite**
- **Axios** for API requests
- **HTML5 & Vanilla CSS** with advanced custom keyframe animations and glassmorphic UI elements
- **Google Fonts:** `Outfit` (bodytext), `Plus Jakarta Sans` (headings)

### Backend
- **Python 3.10+**
- **FastAPI** (Web framework)
- **Uvicorn** (ASGI Server)
- **PyPDF2** (PDF text extraction)
- **OpenAI API** (GPT model generation for resume rewrites)
- **Pydantic** (Data validation)

---

## Prerequisites

Before running the application, make sure you have the following installed:
- [Node.js](https://nodejs.org/) (for the React frontend)
- [Python 3.10+](https://www.python.org/) (for the FastAPI backend)
- An **OpenAI API Key**

---

## Installation & Setup

### 1. Backend Setup

The backend handles PDF parsing, text extraction, data metrics, and communicating with the OpenAI API.

Open a terminal and navigate to the backend directory:
```bash
cd Backend
```

**Install dependencies:**
```bash
pip install -r requirements.txt
```

**Environment Variables:**
The backend requires an OpenAI API key to generate the targeted resume rewrites.
Set the environment variable in your terminal before running:

*On Windows (PowerShell):*
```powershell
$env:OPENAI_API_KEY="your-api-key-here"
```

*On macOS/Linux:*
```bash
export OPENAI_API_KEY="your-api-key-here"
```

**Run the Backend Server:**
```bash
uvicorn app.main:app --reload
```
The FastAPI backend will start running on `http://127.0.0.1:8000`. 
API docs are available at `http://127.0.0.1:8000/docs`.

---

### 2. Frontend Setup

The frontend provides the sleek user interface. 

Open a new terminal and navigate to the frontend directory:
```bash
cd Frontend
```

**Install dependencies:**
```bash
npm install
```

**Run the Frontend Development Server:**
```bash
npm run dev
```
The React app will start running on `http://localhost:5173` (or the port specified by Vite).

---

## Usage

1. Open the frontend URL in your browser (e.g., `http://localhost:5173`).
2. Upload a **PDF copy** of your resume.
3. Paste the **Job Description** of the role you are applying for into the text box.
4. Click **Analyze Resume Now**.
5. View your Match Score, Keyword Analysis, and customized rewrite suggestions on the Results Panel!

---

## Project Structure

```text
AI Resume/
├── Backend/
│   ├── app/
│   │   ├── main.py                 # FastAPI application entry point
│   │   ├── routes/
│   │   │   └── analyzer.py         # API route handlers
│   │   ├── schemas/
│   │   │   └── response_schema.py   # Pydantic models for structured output
│   │   └── services/
│   │       ├── pdf_parser.py       # PDF extraction logic
│   │       └── resume_analyzer.py  # Grading logic, NLP scoring, and OpenAI calls
│   └── requirements.txt
│
├── Frontend/
│   ├── index.html                  # Main HTML document and custom fonts
│   ├── package.json
│   ├── public/
│   │   └── logo.svg                # Animated primary visual logo and favicon
│   └── src/
│       ├── App.jsx                 # Primary layout shell
│       ├── index.css               # Global styling, CSS animations, variables
│       ├── main.jsx                # React mount point
│       ├── components/
│       │   ├── AnalyzerForm.jsx    # Input form handling
│       │   ├── Hero.jsx            # Introductory landing view
│       │   └── ResultsPanel.jsx    # Metrics and rewrite rendering
│       └── services/
│           └── api.js              # Axios configuration
└── README.md
```
