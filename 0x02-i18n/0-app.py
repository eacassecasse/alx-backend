#!/usr/bin/env python3
""" This module defines a basic Flask App. """
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def root() -> str:
    """ The root route to the flask application. """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
