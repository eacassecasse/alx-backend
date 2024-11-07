#!/usr/bin/env python3
""" This module defines a basic Flask App. """
from typing import Union, Dict

from flask_babel import Babel
from flask import Flask, render_template, request, g


class Config:
    """ Flask Babel configuration class. """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale() -> str:
    """ Retrieves the current locale to use. """
    locale = request.args.get("locale", "")

    if locale in app.config["LANGUAGES"]:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])

def get_user() -> Union[Dict, None]:
    """ Retrieves the user if one exists. """
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request() -> None:
    """ Action to be perfomed before the request is resolved. """
    user = get_user()
    g.user = user


@app.route('/')
def root() -> str:
    """ The root route to the flask application. """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
