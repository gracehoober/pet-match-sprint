from flask import Flask, request
import os
# import requests

PETFINDER_ACCESS_TOKEN = os.environ["petfinder_access_token"]

app = Flask(__name__)


@app.get("/")
def getDogs():
    """Gets a list of 50 dogs"""
    return """
        <html>
            <body>
            <h1> Welcome to Fetch </h1>
        <html>
        """


@app.get("/search")
def searchDogs():
    """Handles dog breed search requests
    Example: "/search?breed=germanshepard"
    """
    breed = request.args["breed"]

    dogs_by_breed = requests.get("https://api.petfinder.com/v2/dogs",
                                 params={"breed": breed},
                                 headers={"Authorization":
                                          f"Bearer {PETFINDER_ACCESS_TOKEN}"},
                                 )
    return dogs_by_breed



