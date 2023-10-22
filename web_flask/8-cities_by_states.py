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


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_state():
    """
    hbnb
    """
    cities = sorted(list(storage.all(State).values()), key=lambda x: x.name)
    return render_template("7-states_list.html", states=cities)


@app.teardown_appcontext
def teardown(exception):
    """
    teardown app context
    """
    storage.close()


if __name__ == '__main__':
    """
    main
    """
    app.run(host='0.0.0.0', port=5000)
