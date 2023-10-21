#!/usr/bin/python3
"""
import
"""

from flask import Flask
"""
flask
"""


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """
    hbnb
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    hbnb
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def text(text):
    """
    hbnb
    """
    t = ""
    for i in text:
        if i == '_':
            t += ' '
        else:
            t += i
    return "C " + t


@app.route("/python/<text>", strict_slashes=False)
def text_p(text="is cool"):
    """
    hbnb
    """
    t = ""
    for i in text:
        if i == '_':
            t += ' '
        else:
            t += i
    return "C " + t


if __name__ == '__main__':
    """
    main
    """
    app.run(host='0.0.0.0', port=5000)
