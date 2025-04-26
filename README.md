# Job Analyzer Agent

A web-based tool that allows users to upload their CVs, analyze the content, and receive detailed feedback with a quality score. The tool highlights errors, suggests improvements, and generates a downloadable feedback report.

## Features:
- **Upload CV**: Supports PDF, DOCX, JPG, JPEG, and PNG formats.
- **Text Extraction**: Extracts text from uploaded CVs using OCR and text processing APIs.
- **Grammar and Spelling Check**: Analyzes CV text for grammar and spelling errors using the [LanguageTool API](https://languagetool.org/).
- **Content Analysis**: Identifies missing details like photo, skills, and contact information using the [Cohere API](https://cohere.ai/).
- **Feedback Report**: Generates a feedback report with detailed suggestions and a quality score out of 100.
- **Download Report**: Allows users to download the feedback report in a `.txt` file.

## Tech Stack:
- **Python** for the backend.
- **Streamlit** for the web interface.
- **requests** for API calls.
- **PyPDF2** for extracting text from PDFs.
- **python-docx** for extracting text from Word documents.
- **OCR.Space API** for text extraction from images.

## Setup Instructions:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/job-analyzer-agent.git
   cd job-analyzer-agent
