from flask import Flask, request

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
    #breed = request.args["breed"]
    # make API request based on breed

@app.post("/login")
def login():
    """Logs in a user or returns error message"""
    #