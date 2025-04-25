
from utils import search_query_serpapi, scrape_website, summarize_content
import os

def test_normal_query():
    query = "latest advancements in diabetes research"
    results = search_query_serpapi(query)
    assert isinstance(results, list) and len(results) > 0, "No results found for normal query"
    print("✅ Test Passed: Normal query")

def test_empty_query():
    try:
        results = search_query_serpapi("")
        assert results == [] or results is not None, "Empty query did not handle correctly"
        print("✅ Test Passed: Empty query handled")
    except Exception as e:
        print(f"❌ Test Failed: Empty query error - {e}")

def test_scraping_invalid_url():
    content = scrape_website("https://thisurldoesnotexist.com")
    assert "Error scraping" in content or content == "Error scraping this site.", "Invalid URL scraping not handled"
    print("✅ Test Passed: Scraping invalid URL")

def test_long_query():
    query = "research about diabetes advancements and type 2 prevention strategies and treatment innovations in 2025 with focus on global health impact and cost effectiveness"
    results = search_query_serpapi(query)
    assert isinstance(results, list) and len(results) > 0, "No results for long query"
    print("✅ Test Passed: Long query handled")

def test_special_characters_query():
    query = "@@@!!!???###$$$ diabetes research"
    results = search_query_serpapi(query)
    assert isinstance(results, list), "Special characters caused failure"
    print("✅ Test Passed: Special characters in query handled")

def test_no_api_key_behavior():
    original_key = os.environ.get("SERPAPI_KEY")
    if "SERPAPI_KEY" in os.environ:
        del os.environ["SERPAPI_KEY"]
    try:
        results = search_query_serpapi("diabetes research")
        assert isinstance(results, list), "Agent did not fallback properly without API key"
        print("✅ Test Passed: Missing API key fallback works")
    finally:
        if original_key:
            os.environ["SERPAPI_KEY"] = original_key

if __name__ == "__main__":
    print("Running advanced test cases for the Web Research Agent...\n")
    test_normal_query()
    test_empty_query()
    test_scraping_invalid_url()
    test_long_query()
    test_special_characters_query()
    test_no_api_key_behavior()
