# Resume Tailor

An AI-powered resume optimization tool that helps job seekers tailor their resumes to specific job descriptions. Built with FastAPI backend and Next.js frontend.

## 🚀 Features

- **Resume Upload**: Support for PDF, DOC, DOCX, and TXT files
- **Job Description Analysis**: Paste job descriptions for parsing and analysis
- **Real-time Processing**: Instant feedback on uploaded content
- **Modern UI**: Clean, responsive interface built with Tailwind CSS
- **API Integration**: RESTful API endpoints for resume and job description parsing

## 🛠️ Tech Stack

### Backend
- **FastAPI**: Modern Python web framework
- **Python 3.8+**: Core programming language
- **Uvicorn**: ASGI server for running FastAPI
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
│   │   ├── main.py          # FastAPI application entry point
│   │   ├── routes/
│   │   │   ├── parser.py    # Resume and job description parsing routes
│   │   │   └── tailor.py    # Resume tailoring routes
│   │   └── utils/
│   │       └── parser.py    # Resume parsing utilities
│   └── .venv/               # Python virtual environment
├── frontend/
│   ├── src/
│   │   ├── app/
│   │   │   ├── layout.tsx   # Root layout component
│   │   │   ├── page.tsx     # Home page
│   │   │   └── globals.css  # Global styles
│   │   └── components/
│   │       ├── ResumeParser.tsx      # Main parser component
│   │       ├── ResumeUpload.tsx      # File upload component
│   │       ├── JobDescriptionInput.tsx # Job description input
│   │       └── ResultsDisplay.tsx    # Results display component
│   ├── package.json
│   └── README.md
├── package.json              # Root package.json for development scripts
└── README.md                # This file
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
   pip install fastapi uvicorn python-multipart
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
- Character count statistics
- Loading states and error handling
- Responsive design

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

## 📝 Environment Variables

### Frontend (.env.local)
```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- FastAPI for the excellent Python web framework
- Next.js for the React framework
- Tailwind CSS for the utility-first CSS framework
- The open-source community for inspiration and tools

## 📞 Support

If you encounter any issues or have questions, please open an issue on GitHub or contact the development team. 