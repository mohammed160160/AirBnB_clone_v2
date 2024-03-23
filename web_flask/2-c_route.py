#!/usr/bin/python3
""" Starts a Flash Web Application """

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def show_c_text(text):
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
