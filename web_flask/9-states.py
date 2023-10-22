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


@app.route("/states", strict_slashes=False)
def states():
    """
    hbnb
    """
    states = sorted(list(storage.all(State).values()), key=lambda x: x.name)
    return render_template("9-states.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def cities_by_state_id(id):
    """
    hbnb
    """
    state_id = None
    for i in storage.all(State).values():
        if i.id == id:
            state_id = i
    return render_template("9-states.html", state_id=state_id)


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
