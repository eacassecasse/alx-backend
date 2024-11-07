#!/usr/bin/env python3
""" This module defines a basic Flask App. """
from flask_babel import Babel
from flask import Flask, render_template, request


class Config:
    """ Flask Babel configuration class. """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """ Retrieves the current locale to use. """
    query_string = request.query_string.decode('utf-8').split('&')
    queries_dict = dict(map(
        lambda x: (x if '=' in x else '{}='.format(x)).split('='),
        query_string,
    ))
    if 'locale' in queries_dict:
        if queries_dict['locale'] in app.config["LANGUAGES"]:
            return queries_dict['locale']
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def root() -> str:
    """ The root route to the flask application. """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
