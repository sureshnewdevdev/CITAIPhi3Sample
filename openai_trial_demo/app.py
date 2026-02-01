# app.py
# ======
# REAL OpenAI API demo using TRIAL credits (limited)
# Uses environment variable for API key (best practice)

import os
import json
from openai import OpenAI

# Step 1: Read API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise RuntimeError(
        "OPENAI_API_KEY not found. Set it as environment variable."
    )

# Step 2: Create OpenAI client
client = OpenAI(api_key=api_key)

# Step 3: Choose a small, low-cost model
MODEL_NAME = "gpt-4o-mini"

def extract_keywords(text: str):
    """
    Sends text to OpenAI and extracts search keywords.
    """

    response = client.responses.create(
        model=MODEL_NAME,
        input=[
            {
                "role": "system",
                "content": (
                    "Extract 5 to 8 search keywords. "
                    "Return ONLY a JSON array."
                )
            },
            {
                "role": "user",
                "content": text
            }
        ],
        max_output_tokens=100
    )

    # Extract model text output
    raw_output = response.output_text.strip()

    # Convert JSON string to Python list
    return json.loads(raw_output)

if __name__ == "__main__":
    print("OpenAI Trial Credits Demo")
    print("-------------------------")

    paragraph = input("Enter text:\n")

    keywords = extract_keywords(paragraph)

    print("\nExtracted Keywords:")
    for k in keywords:
        print("-", k)
