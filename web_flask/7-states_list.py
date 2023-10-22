#!/usr/bin/python3
"""
import
"""

from flask import Flask, render_template
from models import storage
from models.state import State
"""
flask
"""


app = Flask(__name__)


states=storage.all(State)
@app.route("/states_list", strict_slashes=False)
def states(states):
    """
    hbnb
    """
    return render_template("7-states_list.html", states=states)


if __name__ == '__main__':
    """
    main
    """
    app.run(host='0.0.0.0', port=5000)
