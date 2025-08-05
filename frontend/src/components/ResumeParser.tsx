'use client';

import { useState } from 'react';
import ResumeUpload from './ResumeUpload';
import JobDescriptionInput from './JobDescriptionInput';
import ResultsDisplay from './ResultsDisplay';

interface ParsedData {
  resumeText?: string;
  jobDescriptionText?: string;
}

export default function ResumeParser() {
  const [parsedData, setParsedData] = useState<ParsedData>({});
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleResumeParsed = (resumeText: string) => {
    setParsedData(prev => ({ ...prev, resumeText }));
    setError(null);
  };

  const handleJobDescriptionParsed = (jobDescriptionText: string) => {
    setParsedData(prev => ({ ...prev, jobDescriptionText }));
    setError(null);
  };

  const handleError = (errorMessage: string) => {
    setError(errorMessage);
  };

  const handleLoading = (loading: boolean) => {
    setIsLoading(loading);
  };

  return (
    <div className="max-w-4xl mx-auto">
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        {/* Resume Upload Section */}
        <div className="bg-white rounded-lg shadow-lg p-6">
          <h2 className="text-2xl font-semibold text-gray-800 mb-4">
            Upload Resume
          </h2>
          <ResumeUpload 
            onResumeParsed={handleResumeParsed}
            onError={handleError}
            onLoading={handleLoading}
          />
        </div>

        {/* Job Description Section */}
        <div className="bg-white rounded-lg shadow-lg p-6">
          <h2 className="text-2xl font-semibold text-gray-800 mb-4">
            Job Description
          </h2>
          <JobDescriptionInput 
            onJobDescriptionParsed={handleJobDescriptionParsed}
            onError={handleError}
            onLoading={handleLoading}
          />
        </div>
      </div>

      {/* Results Section */}
      {(parsedData.resumeText || parsedData.jobDescriptionText) && (
        <div className="mt-8">
          <ResultsDisplay 
            parsedData={parsedData}
            isLoading={isLoading}
            error={error}
          />
        </div>
      )}
    </div>
  );
} 