import os
import requests

PETFINDER_API_KEY = os.environ["petfinder_API_key"]
PETFINDER_SECRET_KET = os.environ["petfinder_secret_key"]
PETFINDER_API_URL = "https://api.petfinder.com/v2/oauth2/token"


def update_auth_token():
    """Gets an OAuth token from Petfinder"""

    data = {"grant_type":"client_credentials"}
    response = requests.post(
        PETFINDER_API_URL,
        data=data,
        auth=(PETFINDER_API_KEY, PETFINDER_SECRET_KET)
        )
    token = response.json()["access_token"]

    return token