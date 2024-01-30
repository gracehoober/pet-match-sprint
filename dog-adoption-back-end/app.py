from flask import Flask, request
from utils import update_auth_token
import requests

PETFINDER_AUTH_TOKEN = None

app = Flask(__name__)

########## ROUTES ###########


@app.before_request
def update_credentials():
    """Get auth token from Petfinder and store globally"""
    global PETFINDER_AUTH_TOKEN
    PETFINDER_AUTH_TOKEN = update_auth_token() #TODO: save this is session, g??
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
    return """
        <html>
            <body>
            <h1> Welcome to Fetch </h1>
        <html>
        """


# TODO: add in error handling (search term couldnt find something)
@app.get("/search")
def searchDogs():
    """Handles dog breed search requests
    Example: "/search?breed=germanshepard"
    """
    # getting the search term from the request
    breed = request.args["breed"]

    # requesting a list of dogs from the apr
    dogs_by_breed = requests.get("https://api.petfinder.com/v2/dogs",
                                 params={"breed": breed},
                                 headers={"Authorization":
                                          f"Bearer {PETFINDER_AUTH_TOKEN}"},
                                 )
    dogs_by_breed = re
    # sending list of dogs back to the front end -> jsonify()??
    return dogs_by_breed
