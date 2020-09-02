#!/usr/bin/python3
""" Running Flask Web App """

from flask import Flask, render_template
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

@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """ display defined txt """
    return 'Python ' + text.replace("_", " ")

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Display n is a number if type(n) == int"""
    if type(n) == int:
        return "{} is a number".format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def numbersandtemplates(n):
    """display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
