from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    """Return simple "Welcome" greeting."""

    return "welcome"

@app.route('/welcome/home')
def welcome_home():
    """Return simple "Welcome Home" message"""

    return "welcome home"

@app.route('/welcome/back')
def welcome_back():
    """Return simple "weclome back" string"""

    return "welcome back"