# Import all necessary libraries 
import gradio as gr
from utils import search_query_serpapi, scrape_website, summarize_content
from dotenv import load_dotenv

# Load environment variables from .env file for secure API key access
load_dotenv()

# Define Web Research Agent
def web_research_agent(user_query):
    """Main agent function that handles the research workflow:
    1. Searches the web for relevant content.
    2. Scrapes text from top results.
    3. Summarizes the content into a structured report."""
    results = search_query_serpapi(user_query)
    final_report = ""
    for url in results:
        content = scrape_website(url)
        summary = summarize_content(content, user_query)
        final_report += f"\n\nSummary from {url}:\n{summary}\n{'-'*80}\n"
    return final_report

# Define the Gradio user interface using Blocks layout
with gr.Blocks() as demo:
    gr.Markdown("# 🌐 Masonry Web Research Agent")
    gr.Markdown("Enter your research query below. The agent will search, scrape, analyze, and generate a research report automatically.")

    with gr.Row():
        query_input = gr.Textbox(label="Enter your research query", placeholder="Enter any research query here...")
    with gr.Row():
        submit_btn = gr.Button("Generate Research Report")
        clear_btn = gr.Button("Clear")

    output_box = gr.Textbox(label="Research Report", lines=20)

    # Button functionalities
    submit_btn.click(fn=web_research_agent, inputs=query_input, outputs=output_box)  # Submit button
    clear_btn.click(fn=lambda: ("", ""), inputs=None, outputs=[query_input, output_box])    # Clear button

# Launch the application if this file is run directly
if __name__ == "__main__":
    demo.launch()   # This will launch the agent
