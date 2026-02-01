# app.py
# ======
# This program SIMULATES how an API key is used in real applications.
# No real server. No internet. No cost.

from config import API_KEY


def fake_server(api_key_from_client: str) -> dict:
    """
    This function represents a BACKEND SERVER.
    It receives an API key and validates it.
    """

    # Step 1: Server has its own expected API key
    SERVER_API_KEY = "FREE-DEMO-KEY-123"

    # Step 2: Validate the key
    if api_key_from_client != SERVER_API_KEY:
        return {
            "status": 401,
            "message": "Unauthorized - Invalid API Key"
        }

    # Step 3: If key is valid, return data
    return {
        "status": 200,
        "message": "Success",
        "data": ["search", "keyword", "api", "demo"]
    }


def client_request():
    """
    This function represents a CLIENT APPLICATION.
    """

    print("Client: Reading API key from config...")

    # Step 1: Read API key
    api_key = API_KEY

    print("Client: API key loaded")

    # Step 2: Send API key to server
    print("Client: Sending API key to server...")

    response = fake_server(api_key)

    # Step 3: Receive response
    print("Client: Response received\n")

    print("Final Response:")
    print(response)


if __name__ == "__main__":
    client_request()
