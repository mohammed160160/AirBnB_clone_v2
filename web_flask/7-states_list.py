#!/usr/bin/python3
""" Starts a Flash Web Application """

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def close_session(exception=None):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    states = list(storage.all("State").values())
    sorted_states = sorted(states, key=lambda x: x.name)
    return render_template('7-states_list.html', states=sorted_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
