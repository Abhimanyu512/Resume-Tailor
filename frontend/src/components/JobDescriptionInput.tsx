'use client';

import { useState } from 'react';

interface JobDescriptionInputProps {
  onJobDescriptionParsed: (jobDescriptionText: string) => void;
  onError: (error: string) => void;
  onLoading: (loading: boolean) => void;
}

export default function JobDescriptionInput({ onJobDescriptionParsed, onError, onLoading }: JobDescriptionInputProps) {
  const [jobDescription, setJobDescription] = useState('');
  const [isSubmitted, setIsSubmitted] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    
    if (!jobDescription.trim()) {
      onError('Please enter a job description.');
      return;
    }

    onLoading(true);
    onError('');

    try {
      const response = await fetch('http://localhost:8000/api/parse-job-description', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          job_description: jobDescription.trim(),
        }),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Failed to parse job description');
      }

      const data = await response.json();
      onJobDescriptionParsed(data.job_description_text);
      setIsSubmitted(true);
    } catch (error) {
      onError(error instanceof Error ? error.message : 'Failed to parse job description');
    } finally {
      onLoading(false);
    }
  };

  const handleTextChange = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
    setJobDescription(e.target.value);
    if (isSubmitted) {
      setIsSubmitted(false);
    }
  };

  return (
    <div className="space-y-4">
      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label htmlFor="job-description" className="block text-sm font-medium text-gray-700 mb-2">
            Paste the job description here
          </label>
          <textarea
            id="job-description"
            rows={8}
            className="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 resize-none"
            placeholder="Paste the job description, requirements, and responsibilities here..."
            value={jobDescription}
            onChange={handleTextChange}
            required
          />
        </div>
        
        <div className="flex justify-between items-center">
          <div className="text-sm text-gray-500">
            {jobDescription.length} characters
          </div>
          <button
            type="submit"
            disabled={!jobDescription.trim()}
            className="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
          >
            Parse Job Description
          </button>
        </div>
      </form>

      {isSubmitted && (
        <div className="bg-green-50 border border-green-200 rounded-lg p-4">
          <div className="flex items-center">
            <svg className="h-5 w-5 text-green-400" fill="currentColor" viewBox="0 0 20 20">
              <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
            </svg>
            <span className="ml-2 text-sm text-green-800">
              Job description parsed successfully
            </span>
          </div>
        </div>
      )}
    </div>
  );
} 