# Import all necessary libraries
import openai
import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup

# Load environment variables from .env file for secure API key handling
load_dotenv()

# Define Search query with SerpApi Key
def search_query_serpapi(query, num_results=5):
    """Perform Google Search using SerpAPI and return top search result links.
    Falls back to mock search results if SerpAPI is unavailable or fails."""
    try:
        api_key = os.getenv('SERPAPI_KEY')  # Serp API
        params = {
            "engine": "google",
            "q": query,
            "num": num_results,
            "api_key": api_key
        }
        response = requests.get("https://serpapi.com/search", params=params)
        results = response.json().get("organic_results", [])
        links = [result['link'] for result in results]
        return links if links else mock_search_results(query)
    except Exception as e:
        print(f"Error using SerpAPI: {e}")
        return mock_search_results(query)

# Define Mock Search 
def mock_search_results(query):
    """Provides fallback mock search results if SerpAPI fails or is unavailable.
    Useful for testing and offline scenarios."""
    print(f"Returning mock search results for query: {query}")
    return [
        f"https://example.com/{query.replace(' ', '_')}/result1",
        f"https://example.com/{query.replace(' ', '_')}/result2",
        f"https://example.com/{query.replace(' ', '_')}/result3"
    ]

# Define Scrape Websites
def scrape_website(url):
    """Scrapes text content from the specified URL.
    Extracts text from paragraph and heading tags (p, h1, h2, h3).
    Handles scraping errors gracefully."""
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(response.content, 'html.parser')
        paragraphs = soup.find_all(['p', 'h1', 'h2', 'h3'])
        text = '\n'.join([para.get_text(strip=True) for para in paragraphs])
        return text if text else "No text found on this page."
    except Exception as e:
        print(f"Failed to scrape {url}: {e}")
        return "Error scraping this site."

# Define Summarize Content using OPENAI API
def summarize_content(content, query):
    """Uses OpenAI GPT-3.5 Turbo to summarize extracted web content.
    Takes the query context into account for generating accurate summaries.
    Handles summarization errors gracefully."""
    try:
        openai.api_key = os.getenv('OPENAI_API_KEY')  # OPENAI API KEY
        prompt = (
            f"The following is some text extracted from websites based on the query: '{query}'. "
            "Please summarize the key findings, latest research, and important points from this content. "
            "Make the summary clear and concise:\n\n"
            f"{content}\n\n"
            "Summary:"
        )
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=800,
            temperature=0.5
        )
        summary = response['choices'][0]['message']['content'].strip()
        return summary
    except Exception as e:
        print(f"Error during summarization: {e}")
        return "Could not summarize the content."
