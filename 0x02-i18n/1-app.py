#!/usr/bin/env python3
""" This module defines a basic Flask App. """
from flask_babel import Babel
from flask import Flask, render_template


class Config:
    """ Flask Babel configuration class. """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@app.route('/')
def root() -> str:
    """ The root route to the flask application. """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
