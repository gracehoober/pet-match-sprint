import os
import requests

PETFINDER_API_KEY = os.environ["petfinder_API_key"]
PETFINDER_SECRET_KEY = os.environ["petfinder_secret_key"]


petfinder_api_url = "https://api.petfinder.com/v2/oauth2/token"


def update_auth_token():
    """Gets an OAuth token from Petfinder"""

    data = {"grant_type":"client_credentials"}
    response = requests.post(
        petfinder_api_url,
        data=data,
        auth=(PETFINDER_API_KEY, PETFINDER_SECRET_KEY)
        )

    json_response = response.json()
    token = json_response["access_token"]
    return token
