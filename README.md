# Energy Tech Innovation Scout

## Project Summary

Energy Tech Innovation Scout is a Python-based mini project that automatically discovers recent research papers from **arXiv** related to **Energy Technology and Machine Learning**, analyzes them, and generates concise summaries using **Google Gemini (LLM)**.

The goal of this project is to demonstrate practical skills in:
- API integration
- Data filtering and processing
- Large Language Model (LLM) usage
- Error handling
- Clean project setup and documentation

The final output is a structured **JSON report** containing research details and AI-generated insights.

---

## Features

- Fetches real research papers from the arXiv API
- Filters papers published in the last 6 months
- Extracts title, authors, publication date, abstract, and PDF link
- Uses Google Gemini to summarize each paper
- Generates a clean and readable JSON output
- Secure API key handling using environment variables
- Uses virtual environment (venv) for dependency isolation

---

## Project Structure
```bash
SPARK_STUDIOS/
│
├── main.py #main application
├── requirements.txt #python dependencies
├── README.md #project documentation
├── output.json #generated output file
├── .gitignore #ignored files and folders
├── .env.local #sample environment config (API key placeholder)
├── venv/ #virtual environment (not committed)
└── .git/ #git repository
```
## Technologies Used

- Python3
- arXiv API
- Google Gemini API
- google-genai SDK
- requests
- feedparser
- python-dotenv
- Virtual Environment (venv)


### How the System Works
1. Fetches recent papers from arXiv using a search query
2. Filters papers published in the last 180 days
3. Extracts metadata and abstracts
4. Sends abstracts to Gemini for summarization
5. Stores final results in a JSON file


## Setup Instructions

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd SPARK_STUDIOS
```

### Step 2: Create and Activate Virtual Environment

## macOS / Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

## Windows
```bash
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Environment Variable Setup

For security reasons, the Gemini API key is not included directly.

A sample file named .env.local is provided.

## To run the project:
1. Rename .env.local to .env
2. Add your Gemini API key inside the file

Example:
```bash
GEMINI_API_KEY=your_gemini_api_key_here
```

### Step 5: Run the Application
```bash
python3 main.py
```

### Output

After execution, an output.json file is generated.

Each record contains:

- **Paper title**
- **Authors**
- **Published date and time**
- **PDF link**
- **Gemini-generated summary**

```bash
{
  "title": "Advanced Manufacturing with Renewable Materials",
  "authors": ["Author A", "Author B"],
  "published_date": "Date: 2026-01-16 Time: 00:26:54+05:30",
  "pdf_link": "https://arxiv.org/pdf/xxxx.xxxx.pdf",
  "llm_summary": "This paper proposes a novel approach to improve sustainability using renewable materials."
}
```

### Assumptions
Only papers from the last 6 months are considered.
Relevance is based on keyword matching.
Gemini API access is available during execution.
Output is intended for reporting and analysis.

### Security Considerations
API keys are stored in environment files
.env, .env.local, and venv/ are excluded using .gitignore
No sensitive information is committed to the repository

## 🙋‍♂️ **Support**

- 📧 **Email:** [alfez.tintoiya25@domain.com](mailto:your-email@domain.com)
- 💻 **Portfolio:** [https://alfeztintoiya.netlify.app/]
- 🐛 **Issues:** [GitHub Issues](https://github.com/yourusername/resume-analyzer/issues)
- 💬 **Discussions:** [GitHub Discussions](https://github.com/yourusername/resume-analyzer/discussions)
