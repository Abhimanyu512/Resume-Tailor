'use client';

import { useState } from 'react';

interface ParsedData {
  resumeText?: string;
  jobDescriptionText?: string;
}

interface ResultsDisplayProps {
  parsedData: ParsedData;
  isLoading: boolean;
  error: string | null;
}

interface TailoredResume {
  name: string;
  summary: string;
  skills: string[];
  experience: {
    job_title: string;
    company: string;
    duration: string;
    description: string;
  }[];
  projects?: {
    title: string;
    description: string;
    tech_stack?: string[];
  }[];
  education?: {
    degree: string;
    institution: string;
    duration: string;
  }[];
}

export default function ResultsDisplay({ parsedData, isLoading, error }: ResultsDisplayProps) {
  const [tailoredResume, setTailoredResume] = useState<TailoredResume | null>(null);
  const [isTailoring, setIsTailoring] = useState(false);
  const [tailorError, setTailorError] = useState<string | null>(null);
  const [isDownloading, setIsDownloading] = useState(false);

  const handleGenerateTailoredResume = async () => {
    if (!parsedData.resumeText || !parsedData.jobDescriptionText) {
      setTailorError('Both resume and job description are required');
      return;
    }

    setIsTailoring(true);
    setTailorError(null);

    try {
      const response = await fetch('http://localhost:8000/api/generate-tailored-resume', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          resume_text: parsedData.resumeText,
          job_description: parsedData.jobDescriptionText,
          tone: 'formal',
          focus: 'impact'
        }),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Failed to generate tailored resume');
      }

      const data = await response.json();
      setTailoredResume(data.tailored_resume);
    } catch (error) {
      setTailorError(error instanceof Error ? error.message : 'Failed to generate tailored resume');
    } finally {
      setIsTailoring(false);
    }
  };

  const handleDownloadPDF = async () => {
    if (!parsedData.resumeText || !parsedData.jobDescriptionText) {
      setTailorError('Both resume and job description are required');
      return;
    }

    setIsDownloading(true);
    setTailorError(null);

    try {
      const response = await fetch('http://localhost:8000/api/generate-tailored-resume-pdf', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          resume_text: parsedData.resumeText,
          job_description: parsedData.jobDescriptionText,
          tone: 'formal',
          focus: 'impact'
        }),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Failed to generate PDF');
      }

      // Get the PDF blob
      const pdfBlob = await response.blob();
      
      // Create download link
      const url = window.URL.createObjectURL(pdfBlob);
      const link = document.createElement('a');
      link.href = url;
      
      // Get filename from response headers or use default
      const contentDisposition = response.headers.get('content-disposition');
      let filename = 'tailored_resume.pdf';
      if (contentDisposition) {
        const filenameMatch = contentDisposition.match(/filename="(.+)"/);
        if (filenameMatch) {
          filename = filenameMatch[1];
        }
      }
      
      link.download = filename;
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      window.URL.revokeObjectURL(url);
      
    } catch (error) {
      setTailorError(error instanceof Error ? error.message : 'Failed to download PDF');
    } finally {
      setIsDownloading(false);
    }
  };

  if (isLoading) {
    return (
      <div className="bg-white rounded-lg shadow-lg p-6">
        <div className="flex items-center justify-center py-8">
          <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600"></div>
          <span className="ml-3 text-gray-600">Processing...</span>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="bg-white rounded-lg shadow-lg p-6">
        <div className="bg-red-50 border border-red-200 rounded-lg p-4">
          <div className="flex items-center">
            <svg className="h-5 w-5 text-red-400" fill="currentColor" viewBox="0 0 20 20">
              <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clipRule="evenodd" />
            </svg>
            <span className="ml-2 text-sm text-red-800">{error}</span>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="bg-white rounded-lg shadow-lg p-6">
      <h2 className="text-2xl font-semibold text-gray-800 mb-6">Parsed Results</h2>
      
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Resume Text */}
        {parsedData.resumeText && (
          <div className="space-y-3">
            <h3 className="text-lg font-medium text-gray-700 flex items-center">
              <svg className="h-5 w-5 text-blue-600 mr-2" fill="currentColor" viewBox="0 0 20 20">
                <path fillRule="evenodd" d="M4 4a2 2 0 012-2h4.586A2 2 0 0112 2.586L15.414 6A2 2 0 0116 7.414V16a2 2 0 01-2 2H6a2 2 0 01-2-2V4zm2 6a1 1 0 011-1h6a1 1 0 110 2H7a1 1 0 01-1-1zm1 3a1 1 0 100 2h6a1 1 0 100-2H7z" clipRule="evenodd" />
              </svg>
              Resume Content
            </h3>
            <div className="bg-gray-50 rounded-lg p-4 max-h-96 overflow-y-auto">
              <pre className="text-sm text-gray-700 whitespace-pre-wrap font-sans">
                {parsedData.resumeText}
              </pre>
            </div>
            <div className="text-xs text-gray-500">
              {parsedData.resumeText.length} characters
            </div>
          </div>
        )}

        {/* Job Description Text */}
        {parsedData.jobDescriptionText && (
          <div className="space-y-3">
            <h3 className="text-lg font-medium text-gray-700 flex items-center">
              <svg className="h-5 w-5 text-green-600 mr-2" fill="currentColor" viewBox="0 0 20 20">
                <path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              Job Description Content
            </h3>
            <div className="bg-gray-50 rounded-lg p-4 max-h-96 overflow-y-auto">
              <pre className="text-sm text-gray-700 whitespace-pre-wrap font-sans">
                {parsedData.jobDescriptionText}
              </pre>
            </div>
            <div className="text-xs text-gray-500">
              {parsedData.jobDescriptionText.length} characters
            </div>
          </div>
        )}
      </div>

      {/* Tailor Resume Section */}
      {parsedData.resumeText && parsedData.jobDescriptionText && (
        <div className="mt-8 pt-6 border-t border-gray-200">
          <div className="flex items-center justify-between mb-4">
            <h3 className="text-lg font-medium text-gray-700">Resume Tailoring</h3>
            <div className="flex gap-3">
              <button
                onClick={handleGenerateTailoredResume}
                disabled={isTailoring}
                className="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
              >
                {isTailoring ? 'Generating...' : 'Generate Tailored Resume'}
              </button>
              <button
                onClick={handleDownloadPDF}
                disabled={isDownloading}
                className="px-4 py-2 bg-green-600 text-white rounded-md hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-green-500 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed transition-colors flex items-center"
              >
                <svg className="h-4 w-4 mr-2" fill="currentColor" viewBox="0 0 20 20">
                  <path fillRule="evenodd" d="M3 17a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zm3.293-7.707a1 1 0 011.414 0L9 10.586V3a1 1 0 112 0v7.586l1.293-1.293a1 1 0 111.414 1.414l-3 3a1 1 0 01-1.414 0l-3-3a1 1 0 010-1.414z" clipRule="evenodd" />
                </svg>
                {isDownloading ? 'Downloading...' : 'Download PDF'}
              </button>
            </div>
          </div>

          {tailorError && (
            <div className="bg-red-50 border border-red-200 rounded-lg p-4 mb-4">
              <div className="flex items-center">
                <svg className="h-5 w-5 text-red-400" fill="currentColor" viewBox="0 0 20 20">
                  <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clipRule="evenodd" />
                </svg>
                <span className="ml-2 text-sm text-red-800">{tailorError}</span>
              </div>
            </div>
          )}

          {isTailoring && (
            <div className="bg-blue-50 border border-blue-200 rounded-lg p-4">
              <div className="flex items-center">
                <div className="animate-spin rounded-full h-5 w-5 border-b-2 border-blue-600"></div>
                <span className="ml-3 text-sm text-blue-800">Generating tailored resume...</span>
              </div>
            </div>
          )}

          {isDownloading && (
            <div className="bg-green-50 border border-green-200 rounded-lg p-4">
              <div className="flex items-center">
                <div className="animate-spin rounded-full h-5 w-5 border-b-2 border-green-600"></div>
                <span className="ml-3 text-sm text-green-800">Generating and downloading PDF...</span>
              </div>
            </div>
          )}

          {tailoredResume && (
            <div className="bg-green-50 border border-green-200 rounded-lg p-6">
              <h4 className="text-lg font-medium text-green-800 mb-4">Tailored Resume Generated</h4>
              
              {/* Name and Summary */}
              <div className="space-y-4">
                <div>
                  <h5 className="font-medium text-gray-800">Name</h5>
                  <p className="text-gray-700">{tailoredResume.name}</p>
                </div>
                
                <div>
                  <h5 className="font-medium text-gray-800">Professional Summary</h5>
                  <p className="text-gray-700">{tailoredResume.summary}</p>
                </div>

                {/* Skills */}
                <div>
                  <h5 className="font-medium text-gray-800">Skills</h5>
                  <div className="flex flex-wrap gap-2 mt-2">
                    {tailoredResume.skills.map((skill, index) => (
                      <span key={index} className="px-3 py-1 bg-blue-100 text-blue-800 rounded-full text-sm">
                        {skill}
                      </span>
                    ))}
                  </div>
                </div>

                {/* Experience */}
                <div>
                  <h5 className="font-medium text-gray-800">Experience</h5>
                  <div className="space-y-3 mt-2">
                    {tailoredResume.experience.map((exp, index) => (
                      <div key={index} className="border-l-4 border-blue-500 pl-4">
                        <div className="flex justify-between items-start">
                          <h6 className="font-medium text-gray-800">{exp.job_title}</h6>
                          <span className="text-sm text-gray-500">{exp.duration}</span>
                        </div>
                        <p className="text-sm text-gray-600 mb-1">{exp.company}</p>
                        <p className="text-sm text-gray-700">{exp.description}</p>
                      </div>
                    ))}
                  </div>
                </div>

                {/* Projects */}
                {tailoredResume.projects && tailoredResume.projects.length > 0 && (
                  <div>
                    <h5 className="font-medium text-gray-800">Projects</h5>
                    <div className="space-y-3 mt-2">
                      {tailoredResume.projects.map((project, index) => (
                        <div key={index} className="border-l-4 border-green-500 pl-4">
                          <h6 className="font-medium text-gray-800">{project.title}</h6>
                          <p className="text-sm text-gray-700 mb-2">{project.description}</p>
                          {project.tech_stack && project.tech_stack.length > 0 && (
                            <div className="flex flex-wrap gap-1">
                              {project.tech_stack.map((tech, techIndex) => (
                                <span key={techIndex} className="px-2 py-1 bg-green-100 text-green-800 rounded text-xs">
                                  {tech}
                                </span>
                              ))}
                            </div>
                          )}
                        </div>
                      ))}
                    </div>
                  </div>
                )}

                {/* Education */}
                {tailoredResume.education && tailoredResume.education.length > 0 && (
                  <div>
                    <h5 className="font-medium text-gray-800">Education</h5>
                    <div className="space-y-2 mt-2">
                      {tailoredResume.education.map((edu, index) => (
                        <div key={index} className="border-l-4 border-purple-500 pl-4">
                          <div className="flex justify-between items-start">
                            <h6 className="font-medium text-gray-800">{edu.degree}</h6>
                            <span className="text-sm text-gray-500">{edu.duration}</span>
                          </div>
                          <p className="text-sm text-gray-600">{edu.institution}</p>
                        </div>
                      ))}
                    </div>
                  </div>
                )}
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  );
} 