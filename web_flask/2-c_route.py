#!/usr/bin/python3
""" Running Flask Web App """

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hbnb_greetings():
    """ Hello HBNB """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ hbnb """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ C Text Replacing """
    return 'C ' + text.replace("_", " ")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
