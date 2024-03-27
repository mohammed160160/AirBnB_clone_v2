#!/usr/bin/python3
""" Starts a Flash Web Application """

from flask import Flask
from flask import render_template
app = Flask(__name__)



@app.route('/states_list', strict_slashes=False)


@app.teardown_appcontext



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
