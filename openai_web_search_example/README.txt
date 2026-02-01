OpenAI Web Search (Text) Example — Python (Responses API)
========================================================

⚠️ IMPORTANT (API key safety)
- Do NOT hard-code your API key in code.
- Do NOT paste your API key into chat, GitHub, screenshots, or screen recordings.
- If you already shared a key publicly, revoke it and create a new one immediately.

What this project does
----------------------
This is a tiny CLI app that:
1) takes a question from the command line
2) calls OpenAI's Responses API
3) enables the built-in `web_search` tool (so the model can search the internet)
4) prints:
   - the final answer text
   - the web sources (citations) used by the web_search tool call

Prerequisites
-------------
- Python 3.10+ installed
- An OpenAI API key in an environment variable named: OPENAI_API_KEY

Step-by-step setup (Windows / macOS / Linux)
--------------------------------------------
1) Unzip this project.
2) Open a terminal in the unzipped folder.
3) Create a virtual environment:

   Windows (PowerShell):
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1

   macOS / Linux:
     python3 -m venv .venv
     source .venv/bin/activate

4) Install dependencies:
     pip install -r requirements.txt

5) Set your API key as an environment variable (DON'T put it in code):

   Windows (PowerShell):
     setx OPENAI_API_KEY "YOUR_KEY_HERE"
     # Close and reopen the terminal once, then activate venv again.

   macOS / Linux (bash/zsh):
     export OPENAI_API_KEY="YOUR_KEY_HERE"

6) Run the example:
     python main.py "What is the latest stable Java version and what's new in it?"

   You can add --model to change the model:
     python main.py "Tell me the top 3 headlines about AI today" --model gpt-4o-mini

Notes about "free model"
------------------------
OpenAI's API is pay-as-you-go. There isn't a permanently "free" model.
To keep cost low for demos, use a small model like `gpt-4o-mini` and keep your prompts short.
