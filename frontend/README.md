# Resume Tailor Frontend

A modern Next.js frontend application for the Resume Tailor project, built with TypeScript and Tailwind CSS.

## Features

- **Resume Upload**: Drag and drop or click to upload resume files (PDF, DOC, DOCX, TXT)
- **Job Description Input**: Paste job descriptions for analysis
- **Real-time Parsing**: Instant feedback on uploaded content
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Modern UI**: Clean, professional interface with Tailwind CSS

## Tech Stack

- **Next.js 14**: React framework with App Router
- **TypeScript**: Type-safe development
- **Tailwind CSS**: Utility-first CSS framework
- **React Hooks**: State management and side effects

## Getting Started

### Prerequisites

- Node.js 18+ 
- npm or yarn
- Backend server running on `http://localhost:8000`

### Installation

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

4. Open [http://localhost:3000](http://localhost:3000) in your browser.

## Project Structure

```
src/
├── app/
│   ├── layout.tsx          # Root layout component
│   ├── page.tsx            # Home page
│   └── globals.css         # Global styles
├── components/
│   ├── ResumeParser.tsx    # Main parser component
│   ├── ResumeUpload.tsx    # File upload component
│   ├── JobDescriptionInput.tsx # Job description input
│   └── ResultsDisplay.tsx  # Results display component
```

## API Integration

The frontend integrates with the following backend endpoints:

- `POST /api/parse-resume`: Upload and parse resume files
- `POST /api/parse-job-description`: Parse job description text

## Development

### Available Scripts

- `npm run dev`: Start development server
- `npm run build`: Build for production
- `npm run start`: Start production server
- `npm run lint`: Run ESLint

### Environment Variables

Create a `.env.local` file in the frontend directory:

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## Features

### Resume Upload
- Supports PDF, DOC, DOCX, and TXT files
- File size limit: 5MB
- Drag and drop functionality
- Real-time validation

### Job Description Input
- Large text area for pasting job descriptions
- Character count display
- Form validation

### Results Display
- Clean presentation of parsed content
- Side-by-side comparison
- Character count statistics
- Loading states and error handling

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is part of the Resume Tailor application.
