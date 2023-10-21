#!/usr/bin/python3
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


if __name__ == '__main__':
    """
    main
    """
    app.run(host='0.0.0.0', port=5000)
#!/usr/bin/python3
""" 0. Script to start a Flask web application """

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """ Returns some text. """
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    