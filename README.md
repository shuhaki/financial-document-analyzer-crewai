# Financial Document Analyzer

## Project Overview

A comprehensive financial document analysis system that processes corporate reports, financial statements, and investment documents using AI-powered analysis agents. Built with FastAPI and CrewAI, it provides automated financial analysis, investment recommendations, risk assessment, and market insights.

## Features

- Upload financial documents (PDF format)
- AI-powered financial analysis using CrewAI agents
- Investment recommendations
- Risk assessment
- Market insights
- RESTful API endpoints
- Async processing for better performance

## Project Structure

```
financial-document-analyzer/
├── agents.py           # AI agent definitions
├── main.py             # FastAPI application and endpoints
├── task.py             # Task definitions for the crew
├── tools.py            # Custom tools for document processing
├── requirements.txt    # Python dependencies
├── data/               # Data directory for uploaded files
│   └── TSLA-Q2-2025-Update.pdf
└── outputs/            # Analysis output files
```

## Getting Started

### Prerequisites

- Python 3.8+
- OpenAI API key (set in `.env` file as `OPENAI_API_KEY`)

### Installation

1. Clone the repository:
```
sh
git clone <repository-url>
cd financial-document-analyzer
```

2. Install required libraries:
```
sh
pip install -r requirements.txt
```

3. Set up your OpenAI API key:
```
sh
echo "OPENAI_API_KEY=your_api_key_here" > .env
```

### Running the Application

Start the FastAPI server:
```
sh
python main.py
```

The API will be available at `http://localhost:8000`

## API Documentation

### Endpoints

#### Health Check
```
GET /
```
Returns the API status.

**Response:**
```
json
{
  "message": "Financial Document Analyzer API is running"
}
```

#### Analyze Document
```
POST /analyze
```
Analyze a financial document and provide investment insights.

**Parameters:**
- `file` (required): PDF file to upload
- `query` (optional): Custom analysis query (default: "Analyze this financial document for investment insights")

**Response:**
```
json
{
  "status": "success",
  "query": "Analyze this financial document for investment insights",
  "analysis": "...",
  "file_processed": "filename.pdf"
}
```

### Interactive API Documentation

FastAPI provides interactive API documentation:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Sample Document

The system includes a sample Tesla Q2 2025 financial update located at:
```
data/TSLA-Q2-2025-Update.pdf
```

## Usage Examples

### Using cURL

```
sh
curl -X POST "http://localhost:8000/analyze" \
  -F "file=@data/TSLA-Q2-2025-Update.pdf" \
  -F "query=What are the key financial highlights?"
```

### Using Python

```
python
import requests

url = "http://localhost:8000/analyze"
files = {"file": open("data/TSLA-Q2-2025-Update.pdf", "rb")}
data = {"query": "Provide investment recommendations based on this financial document"}

response = requests.post(url, files=files, data=data)
print(response.json())
```

## Technology Stack

- **FastAPI**: Modern Python web framework
- **CrewAI**: Multi-agent AI orchestration
- **LangChain**: AI development framework
- **PyPDF**: PDF processing
- **Uvicorn**: ASGI server



