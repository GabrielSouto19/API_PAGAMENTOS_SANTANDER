

import httpx
from settings import settings

def generate_token(timeout: float = 30.0) -> dict:
    """Request an access token using client credentials.

    Returns the parsed JSON response (includes access_token, expires_in, etc.).
    Raises httpx.HTTPStatusError on non-2xx responses.
    """

    params = {"grant_type": "client_credentials"}
    form_data = {
        "client_id": settings.CLIENT_ID,
        "client_secret": settings.CLIENT_SECRET,
    }

    with httpx.Client(
        cert=(settings.MTLS_CERT_FILE, settings.MTLS_KEY_FILE),
        timeout=30,
        # Set verify=False if you need to bypass CA validation during testing.
    ) as client:
        response = client.post(
            settings.TOKEN_URL,
            params=params,
            data=form_data,
            auth=(settings.CLIENT_ID,settings.CLIENT_SECRET),  # Basic Auth header
        )
        response.raise_for_status()
        return response.json()


if __name__ == "__main__":
    try:
        token_response = generate_token()
        print(token_response)
        print()
        print("TOken a seguir")
        print(token_response.get("access_token"))
    except httpx.HTTPError as exc:
        print(f"Token request failed: {exc}")


if __name__ == "__main__":
    generate_token()