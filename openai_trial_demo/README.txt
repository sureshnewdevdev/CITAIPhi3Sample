OPENAI TRIAL CREDITS – REAL API KEY DEMO (LIMITED, PAID AFTER TRIAL)
=================================================================

Purpose
-------
This project demonstrates:
✔ Using a REAL OpenAI API key
✔ Using TRIAL / PROMO credits (₹0 initially, limited)
✔ How an API key is created
✔ How an API key is used in code

IMPORTANT TRUTH (Read this first)
--------------------------------
- OpenAI does NOT provide a permanently free API.
- New accounts MAY receive trial / promo credits.
- When credits finish → API stops unless billing is enabled.
- This demo is for LEARNING & TRAINING only.

--------------------------------
STEP 1: CREATE OPENAI ACCOUNT
--------------------------------
1) Open browser
2) Go to: https://platform.openai.com/
3) Sign up using:
   - Google account OR
   - Email + password

--------------------------------
STEP 2: CHECK TRIAL CREDITS
--------------------------------
1) Login to OpenAI dashboard
2) Open: https://platform.openai.com/account/usage
3) Check:
   - Remaining credits
   - Expiry date (if any)

If credits = 0 → this demo will NOT work.

--------------------------------
STEP 3: CREATE API KEY
--------------------------------
1) Go to: https://platform.openai.com/api-keys
2) Click "Create new secret key"
3) Copy the key immediately
   Example:
   sk-xxxxxxxxxxxxxxxxxxxx

⚠ IMPORTANT:
- You cannot see this key again.
- DO NOT share it.
- DO NOT commit it to GitHub.

--------------------------------
STEP 4: STORE API KEY (SAFE WAY)
--------------------------------
We will use Environment Variables.

Windows (PowerShell):
--------------------
setx OPENAI_API_KEY "PASTE_YOUR_KEY_HERE"
(close & reopen terminal)

Linux / macOS:
--------------
export OPENAI_API_KEY="PASTE_YOUR_KEY_HERE"

--------------------------------
STEP 5: PROJECT SETUP
--------------------------------
1) Install Python 3.10+
2) Unzip this project
3) Open terminal inside folder

Create virtual environment:
---------------------------
Windows:
  python -m venv .venv
  .venv\Scripts\activate

Linux / macOS:
  python3 -m venv .venv
  source .venv/bin/activate

Install dependencies:
---------------------
pip install -r requirements.txt

--------------------------------
STEP 6: RUN THE DEMO
--------------------------------
python app.py

--------------------------------
EXPECTED OUTPUT
--------------------------------
- Program sends text to OpenAI
- OpenAI returns extracted keywords
- Trial credits are consumed (very small amount)

--------------------------------
COMMON ERRORS
--------------------------------
401 Unauthorized:
- API key wrong OR not set

insufficient_quota:
- Trial credits exhausted

--------------------------------
FILES
--------------------------------
app.py            → Real OpenAI API call
requirements.txt  → Dependencies
README.txt        → This guide
