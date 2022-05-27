from flask import Flask # Import the Flask class

app = Flask(__name__) # Instantiate our app

@app.route('/') # A python decorator, to tell our app which endpoint to listen to for connections

def index(): # route handler that listens for connections to the root route
    return 'Hello World!'