# Resume Tailor

An AI-powered resume optimization tool that helps job seekers tailor their resumes to specific job descriptions. Built with FastAPI backend and Next.js frontend, featuring advanced AI integration and PDF generation capabilities.

## 🚀 Features

- **Resume Upload**: Support for PDF, DOC, DOCX, and TXT files
- **Job Description Analysis**: Paste job descriptions for parsing and analysis
- **AI-Powered Tailoring**: Advanced LLM integration for intelligent resume customization
- **PDF Generation**: Generate professional PDF resumes with custom styling
- **Real-time Processing**: Instant feedback on uploaded content
- **Modern UI**: Clean, responsive interface built with Tailwind CSS
- **RESTful API**: Comprehensive API endpoints for resume processing and tailoring

## 🛠️ Tech Stack

### Backend
- **FastAPI**: Modern Python web framework
- **Python 3.8+**: Core programming language
- **Uvicorn**: ASGI server for running FastAPI
- **Groq**: High-performance LLM API for AI-powered resume tailoring
- **LangChain**: Framework for LLM application development
- **ReportLab**: Professional PDF generation
- **PDFPlumber**: PDF text extraction
- **Python-docx**: Microsoft Word document processing
- **Pydantic**: Data validation and settings management
- **CORS**: Cross-origin resource sharing support

### Frontend
- **Next.js 14**: React framework with App Router
- **TypeScript**: Type-safe development
- **Tailwind CSS**: Utility-first CSS framework
- **React Hooks**: State management

## 📁 Project Structure

```
Resume-Tailor/
├── backend/
│   ├── app/
│   │   ├── main.py              # FastAPI application entry point
│   │   ├── routes/
│   │   │   ├── parser.py        # Resume and job description parsing routes
│   │   │   └── tailor.py        # Resume tailoring and PDF generation routes
│   │   ├── services/
│   │   │   ├── llm_service.py   # AI/LLM integration service
│   │   │   └── resume_prompt.py # Resume tailoring prompts
│   │   ├── schemas/
│   │   │   └── resume_output.py # Pydantic models for data validation
│   │   └── utils/
│   │       ├── parser.py        # Resume parsing utilities
│   │       └── pdf_generator.py # Professional PDF generation
│   ├── requirements.txt          # Python dependencies
│   └── .venv/                   # Python virtual environment
├── frontend/
│   ├── src/
│   │   ├── app/
│   │   │   ├── layout.tsx       # Root layout component
│   │   │   ├── page.tsx         # Home page
│   │   │   └── globals.css      # Global styles
│   │   └── components/
│   │       ├── ResumeParser.tsx      # Main parser component
│   │       ├── ResumeUpload.tsx      # File upload component
│   │       ├── JobDescriptionInput.tsx # Job description input
│   │       └── ResultsDisplay.tsx    # Results and tailoring display
│   ├── package.json
│   └── README.md
├── package.json                  # Root package.json for development scripts
└── README.md                    # This file
```

## 🚀 Quick Start

### Prerequisites

- **Node.js 18+** and npm
- **Python 3.8+** and pip
- **Git**

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd Resume-Tailor
   ```

2. **Install root dependencies**:
   ```bash
   npm install
   ```

3. **Install frontend dependencies**:
   ```bash
   npm run install:frontend
   ```

4. **Set up Python virtual environment**:
   ```bash
   cd backend
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

5. **Set up environment variables** (optional):
   ```bash
   # Create .env file in backend directory
   echo "GROQ_API_KEY=your_groq_api_key_here" > backend/.env
   ```

### Running the Application

#### Option 1: Run Both Frontend and Backend Together
```bash
npm run dev
```

This will start:
- Backend server on `http://localhost:8000`
- Frontend development server on `http://localhost:3000`

#### Option 2: Run Separately

**Backend only**:
```bash
npm run dev:backend
```

**Frontend only**:
```bash
npm run dev:frontend
```

## 🔧 API Endpoints

### Resume Parsing
- **POST** `/api/parse-resume`
  - Upload resume file (PDF, DOC, DOCX, TXT)
  - Returns parsed resume text

### Job Description Parsing
- **POST** `/api/parse-job-description`
  - Send job description text
  - Returns parsed job description

### Resume Tailoring
- **POST** `/api/generate-tailored-resume`
  - Generate AI-tailored resume based on job description
  - Parameters: `resume_text`, `job_description`, `tone`, `focus`
  - Returns structured resume data

### PDF Generation
- **POST** `/api/generate-tailored-resume-pdf`
  - Generate professional PDF resume
  - Parameters: `resume_text`, `job_description`, `tone`, `focus`
  - Returns downloadable PDF file

## 🎨 Frontend Features

### Resume Upload Component
- Drag and drop file upload
- File type validation (PDF, DOC, DOCX, TXT)
- File size limit (5MB)
- Real-time feedback

### Job Description Input
- Large text area for job descriptions
- Character count display
- Form validation
- Instant parsing

### Results Display
- Side-by-side comparison of parsed content
- AI-powered resume tailoring
- Professional PDF generation
- Character count statistics
- Loading states and error handling
- Responsive design

### AI Tailoring Features
- **Intelligent Analysis**: AI analyzes job requirements and resume content
- **Customizable Tone**: Formal, casual, or technical tone options
- **Focus Areas**: Impact-focused or skills-focused tailoring
- **Professional Formatting**: Structured output with proper sections
- **PDF Export**: Download tailored resumes as professional PDFs

## 🛠️ Development

### Backend Development
```bash
cd backend
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend Development
```bash
cd frontend
npm run dev
```

### Building for Production
```bash
npm run build
```

## 🔑 Environment Variables

Create a `.env` file in the `backend` directory:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Get your Groq API key from [Groq Console](https://console.groq.com/).

## 📝 Usage

1. **Upload Resume**: Drag and drop your resume file or click to browse
2. **Input Job Description**: Paste the job description you're applying for
3. **Generate Tailored Resume**: Click to generate an AI-optimized version
4. **Download PDF**: Export your tailored resume as a professional PDF
