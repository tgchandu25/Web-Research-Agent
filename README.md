
# 🧠 Web Research Agent

## 🚀 Project Overview
This project implements a fully autonomous **Web Research Agent** that performs automated research based on user queries. Unlike traditional chatbots, this agent actively:
- Searches the web using a search API.
- Scrapes relevant content from the top search results.
- Summarizes and analyzes the gathered information using AI models.
- Presents a structured, comprehensive research report.


## ⚙️ Technologies Used
- **Python**
- **Gradio (v4.44.1)** - User Interface
- **OpenAI GPT-3.5 Turbo** - Content Summarization
- **SerpAPI / Mock Search** - Web Search Integration
- **BeautifulSoup4** - Web Scraping
- **Hugging Face Spaces** - Deployment Platform
- **python-dotenv** - Secure environment variable loading

## 📂 Project Structure
```
Masonry-Web-Research-Agent/
│
├── app.py               # Main application (Gradio Blocks UI with Clear Button)
├── utils.py             # Core logic: search, scraping, summarization
├── requirements.txt     # Python dependencies
├── test_cases.py        # Testing script to verify agent behavior
```

## 🟢 How to Set Up Locally

1. **Clone the Repository:**
```bash
git clone https://github.com/tgchandu25/Web-Research-Agent.git
cd Web-Research-Agent
```

2. **Install Dependencies:**
```bash
pip install -r requirements.txt
```

3. **Create a `.env` File in the Project Root:**
```
SERPAPI_KEY=your-serpapi-key-here
OPENAI_API_KEY=your-openai-api-key-here
```
> Do **not** upload your `.env` file to GitHub. This file should remain local for security.

4. **Run the Application:**
```bash
python app.py
```
This will launch the agent locally with a Gradio-based web interface.

## 🧪 Testing Instructions

To verify that the agent handles different scenarios correctly:
```bash
python test_cases.py
```
This runs tests for:
- Normal queries.
- Empty input handling.
- Invalid URLs.
- Long and complex queries.
- Missing API key fallback.
- Queries with special characters.

## 🧩 How the Agent Works (Design and Architecture)
The Web Research Agent follows these steps:
1. **Query Analysis:** Understands the user’s query and generates search terms.
2. **Web Search:** Uses SerpAPI (or fallback to mock search) to find top results.
3. **Content Extraction:** Scrapes relevant content from the search results.
4. **Information Synthesis:** Summarizes and analyzes content using OpenAI GPT-3.5 Turbo.
5. **Report Generation:** Presents the output in a structured, readable format via the Gradio web interface.

## ❌ Error Handling & Resilience
- ✅ Handles unreachable websites and scraping errors.
- ✅ Provides fallback to mock search results if the search API key is missing.
- ✅ Skips invalid links without stopping the process.
- ✅ Prevents crashes on empty inputs.

## 📹 Loom Video Link
> Loom Video - 1 [https://www.loom.com/share/894f197a17d14a9abf8955b101c22a6d?sid=1ac5d2c4-0076-4b84-9a37-32a4987262cc] (Explained Overview, Live Demonstration & Challenges Faced)

> Loom Video - 2 [https://www.loom.com/share/30b10ee575fc4988b7b1f19cfc117c77?sid=70e09f97-d9dd-4687-a874-f04ba691a7a2] (A Code Walkthrough)


## 🟢 Live Demo Link (Hugging Face Spaces)
> [https://huggingface.co/spaces/TGChandu/Web-Research-Agent]

## 📝 License
This project was developed for the **AI Agent Development** and is intended for evaluation purposes only.
