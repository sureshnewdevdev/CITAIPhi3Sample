#!/usr/bin/env python3
"""OpenAI Responses API example using the built-in web_search tool.

This file is intentionally *over-commented* (line-by-line style) for learning.
"""

# 1) Import standard-library modules (come with Python)
import os  # For reading environment variables like OPENAI_API_KEY
import argparse  # For parsing command-line arguments like the prompt text
import json  # For pretty-printing JSON (we use it to print sources nicely)

# 2) Import the OpenAI SDK (installed via requirements.txt)
from openai import OpenAI  # OpenAI client for calling the API


def build_arg_parser() -> argparse.ArgumentParser:
    """Create and return the command-line argument parser."""

    # Create an ArgumentParser object (helps us accept input from the command line).
    parser = argparse.ArgumentParser(
        description="Ask a question and let the model use web_search (Responses API)."
    )

    # Positional argument: the user's question (required).
    parser.add_argument(
        "question",
        type=str,
        help="The question you want to ask (example: "What happened in tech news today?")",
    )

    # Optional argument: choose which model to use (default is a small, affordable one).
    parser.add_argument(
        "--model",
        type=str,
        default="gpt-4o-mini",
        help="Model name (default: gpt-4o-mini).",
    )

    # Optional flag: print full raw API output (useful for debugging).
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Print the full raw response JSON (for learning/debugging).",
    )

    # Return the parser so main() can use it.
    return parser


def require_api_key() -> str:
    """Read OPENAI_API_KEY from environment; fail with a clear error if missing."""

    # Read the API key from the environment variable.
    api_key = os.getenv("OPENAI_API_KEY")

    # If the key doesn't exist, show a helpful error message and stop.
    if not api_key:
        raise SystemExit(
            "ERROR: OPENAI_API_KEY is not set.\n"
            "Set it first, for example:\n"
            "  Windows PowerShell:  setx OPENAI_API_KEY \"YOUR_KEY_HERE\"\n"
            "  macOS/Linux:        export OPENAI_API_KEY=\"YOUR_KEY_HERE\"\n"
        )

    # Return the key string.
    return api_key


def extract_web_sources(response) -> list[dict]:
    """Extract web sources (citations) from the Responses API output.

    Why this is needed:
    - When you enable tools=[{type:'web_search'}], the response contains a tool-call item
      (web_search_call) and a message item. Sources typically live inside annotations/sources.

    This function tries to be robust across slightly different output shapes.
    """

    sources: list[dict] = []

    # The SDK provides output items under response.output (list of items).
    for item in getattr(response, "output", []):

        # We are looking for tool call items of type 'web_search_call'.
        if getattr(item, "type", None) == "web_search_call":
            # Some SDK versions expose sources under item.action.sources if included.
            action = getattr(item, "action", None)
            if action:
                action_sources = getattr(action, "sources", None)
                if action_sources:
                    for s in action_sources:
                        # Each source may have url/title; store a normalized dict.
                        sources.append(
                            {
                                "title": getattr(s, "title", None),
                                "url": getattr(s, "url", None),
                            }
                        )

        # Sometimes sources also appear as annotations inside message content.
        if getattr(item, "type", None) == "message":
            # item.content is usually a list (e.g., output_text blocks).
            for c in getattr(item, "content", []):

                # Look for annotations inside each content block.
                for ann in getattr(c, "annotations", []) or []:
                    # We only care about URL citations for this demo.
                    if getattr(ann, "type", None) in ("url_citation", "web_search_result"):
                        sources.append(
                            {
                                "title": getattr(ann, "title", None),
                                "url": getattr(ann, "url", None),
                            }
                        )

    # Remove duplicates (same URL).
    deduped = []
    seen = set()
    for s in sources:
        url = s.get("url")
        if url and url not in seen:
            seen.add(url)
            deduped.append(s)

    return deduped


def main() -> None:
    """Program entry point."""

    # 1) Parse CLI args.
    parser = build_arg_parser()
    args = parser.parse_args()

    # 2) Ensure API key exists (and read it).
    api_key = require_api_key()

    # 3) Create the OpenAI client using the key.
    client = OpenAI(api_key=api_key)

    # 4) Call the Responses API:
    #    - model: which model to use
    #    - input: your question
    #    - tools: enable built-in web_search
    #    - include: ask the API to include web_search sources (so we can print them)
    response = client.responses.create(
        model=args.model,
        input=args.question,
        tools=[{"type": "web_search"}],
        include=["web_search_call.action.sources"],
    )

    # 5) Print the final answer text in a friendly way.
    #    response.output_text is a convenience that concatenates assistant text output.
    print("\n=== ANSWER ===\n")
    print(response.output_text.strip())

    # 6) Extract and print sources (citations).
    sources = extract_web_sources(response)

    print("\n=== SOURCES (if any) ===\n")
    if not sources:
        print("(No sources returned. Try a more 'current events' question or run with --debug.)")
    else:
        for i, s in enumerate(sources, start=1):
            title = s.get("title") or "(no title)"
            url = s.get("url") or "(no url)"
            print(f"{i}. {title}\n   {url}\n")

    # 7) If --debug was provided, print the full raw output so learners can see structure.
    if args.debug:
        print("\n=== DEBUG: FULL RESPONSE JSON ===\n")
        # The SDK objects may not be directly JSON serializable, so use model_dump if present.
        if hasattr(response, "model_dump"):
            print(json.dumps(response.model_dump(), indent=2))
        else:
            # Fallback: print the object's __dict__ representation.
            print(json.dumps(response.__dict__, default=lambda o: getattr(o, "__dict__", str(o)), indent=2))


# Standard Python pattern: run main() only if this file is executed directly.
if __name__ == "__main__":
    main()
