#!/usr/bin/env python3
"""
Flask app with Babel for i18n support, including mock user login.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext as _

app = Flask(__name__)


class Config:
    """
    Configuration for Flask app.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """Retrieve user by `login_as` parameter."""
    user_id = request.args.get('login_as')
    if user_id is None:
        return None
    try:
        user_id = int(user_id)
        return users.get(user_id)
    except ValueError:
        return None


@app.before_request
def before_request():
    """Set `g.user` to the current user if logged in."""
    g.user = get_user()


@babel.localeselector
def get_locale():
    """Determine the best match for supported languages."""
    # 1. Locale from URL parameters
    url_locale = request.args.get('locale')
    if url_locale in app.config['LANGUAGES']:
        return url_locale

    # 2. Locale from user settings
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user['locale']

    # 3. Locale from request header
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Render the index page with user-specific or default messages."""
    if g.user:
        message = _(
            "You are logged in as %(username)s.", username=g.user['name'])
    else:
        message = _("You are not logged in.")
    return render_template('5-index.html', message=message)


if __name__ == "__main__":
    app.run(debug=True)
