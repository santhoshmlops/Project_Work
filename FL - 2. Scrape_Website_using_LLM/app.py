import os
import json
from scrapegraphai.graphs import SmartScraperGraph
from dotenv import load_dotenv

# Load environment variables 
load_dotenv()
api_key=os.getenv("GROQ_API_KEY")

graph_config = {
    "llm": {
        "model": "groq/mixtral-8x7b-32768",
        "api_key": api_key,
        "temperature": 0
    },
    "embeddings": {
        "model": "ollama/nomic-embed-text",
        "base_url": "http://localhost:11434",
    },
    "verbose": True,
    "max_results": 5,
}

smart_scraper_graph = SmartScraperGraph(
    prompt="List me all the project name",
    # also accepts a string with the already downloaded HTML code
    source="https://santhoshmlops.github.io/santhosh/",
    config=graph_config
)

result = smart_scraper_graph.run()

# Define the file name for the JSON file
output_file = "Response.json"

# Write the JSON data to a file
with open(output_file, "w") as file:
    json.dump(result, file, indent=2)

print("JSON response has been exported to:", output_file)