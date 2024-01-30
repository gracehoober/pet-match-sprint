import os

from flask import Flask, request, session
from utils import update_auth_token
import requests

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ["session_secret_key"]

PETFINDER_AUTH_TOKEN = None



########## ROUTES ###########

@app.before_request
def update_credentials():
    """Get auth token from Petfinder and store globally"""

    global PETFINDER_AUTH_TOKEN
    PETFINDER_AUTH_TOKEN = update_auth_token()
    session["current_token"] = PETFINDER_AUTH_TOKEN #TODO: do i need to store this in a session for what reason?

    #TODO: save this is session, g??
    # so my idea is the before any route this function will reun and will result in
    # new token being generated
    # is there a way to only generate a token if the token is expired?? limit requests


# @app.route("/login", methods=["POST", "GET"])
# def login():
#     #get email from the form and see if it is in the db
#         #if in db then password form should show up
#         #if not in db redirect to a signup page


# @app.post("/signup")
# def signup():
#     #get signup info from the form and send it to the db
#     #login the person

@app.get("/")
def getDogs():
    """Gets a list of 50 dogs"""

    animal = requests.get("https://api.petfinder.com/v2/types/dog",
                                 params={"limit": 50},
                                 headers={"Authorization":
                                          f"Bearer {PETFINDER_AUTH_TOKEN}"},)
    return animal.json()


# TODO: add in error handling (search term couldnt find something)
# put a query string in the url and get info out of it
# send info with API req to petfinder
@app.get("/search")
def searchDogs():
    """Handles dog breed search requests and return list of dogs in JSON or
    Example: "/search?breed=germanshepard"
    """
    # getting the search term from the request
    breed = request.params["breed"] or None

    # requesting a list of dogs from the API
    dogs_by_breed = requests.get("https://api.petfinder.com/v2/types/dog/",
                                 params={"breed": breed},
                                 headers={"Authorization":
                                          f"Bearer {PETFINDER_AUTH_TOKEN}"},
                                 )

    # if auth token is expired update PETFINDER_AUTH_TOKEN and rerun request
    if dogs_by_breed.status_code == 401:
        update_credentials()


    #TODO: if request fails due to a 401 -> generate a new token and run again

    # sending list of dogs or 404 notfound back to the front end -> jsonify()??
    return dogs_by_breed.json()
