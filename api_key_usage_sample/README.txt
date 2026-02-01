API KEY USAGE – SAMPLE DEMO (NO REAL API, NO COST)
================================================

Purpose
-------
This project is ONLY to teach:
✔ What an API key is
✔ How it is stored securely
✔ How it is sent in a request
✔ How applications read and use it

⚠ IMPORTANT
-----------
- This project DOES NOT call any real API
- This project DOES NOT cost anything
- This project DOES NOT need internet
- This project SIMULATES real-world API usage

Why this approach is correct for learning
-----------------------------------------
In companies, juniors are first taught:
1) How API keys are passed
2) How headers are formed
3) How validation works
BEFORE they are allowed to use paid APIs.

Project Flow
------------
Client App → API Key → Fake Server → Response

Step-by-Step Run Instructions
-----------------------------
1) Install Python 3.10+

2) Unzip this project

3) Open terminal inside the folder

4) Run the app
   python app.py

5) Observe:
   - API key loaded
   - API key sent
   - API key validated
   - Response returned

Files
-----
app.py            → Client + Server simulation
config.py         → API key storage (best practice)
README.txt        → This file
