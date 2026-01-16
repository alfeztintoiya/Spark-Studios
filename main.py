import os
import json
import requests
import feedparser
from datetime import datetime
from dateutil import parser as date_parser
from typing import List,Dict
from google import genai
from zoneinfo import ZoneInfo

#configuration
ARXIV_API_URL="http://export.arxiv.org/api/query"
SEARCH_QUERY="energy AND machine learning"
MAX_RESULTS=20
DAYS_LIMIT=180
TOP_K=5
GEMINI_MODEL="gemini-3-pro-preview"

#fetch arxiv papers
def fetch_arxiv_papers() -> List:
    try:
        params = {
            "search_query": SEARCH_QUERY,
            "start":0,
            "max_results":MAX_RESULTS,
            "sortBy":"submittedDate",
            "sortOrder":"descending",
        }

        response = requests.get(ARXIV_API_URL,params=params,timeout=10)
        response.raise_for_status()

        feed = feedparser.parse(response.text)

        if not feed.entries:
            print("Warning: No paper returned from arxiv")
            return []

        return feed.entries
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from arXiv: {e}")
        return []

#filter recent papers
def filter_recent_papers(entries: List) -> List[Dict]:
    recent_papers = []
    now = datetime.now(ZoneInfo("Asia/Kolkata"))

    for entry in entries:
        try:
            published_date = date_parser.parse(entry.published)
            days_diff = (now-published_date).days

            if days_diff > DAYS_LIMIT:
                continue

            paper = {
                "title": entry.title.strip(),
                "authors": [author.name for author in entry.authors],
                "published_date": published_date,
                "abstract":entry.summary,
                "pdf_link":entry.links[1].href
            }

            recent_papers.append(paper)
        except Exception as e:
            print(f"skipping paper due to parsing problem: {e}")
            continue
    
    return recent_papers[:TOP_K]

#llm(gemini) summary
def summarize_with_gemini(client: genai.Client,abstract: str)->str:
    prompt = f"""
    Summary the follwing research abstract in 2-3 sentences.
    Clearly mention:
    - Key innovations
    - Potential real-world impact
    - Technologies used

    Abstract:{abstract}
    """

    try:
        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt,
        )

        if not response or not response.text:
            return "Summary could not be generated."
        return response.text.strip()
    except Exception as e:
        return f"error generating summary: {e}"
