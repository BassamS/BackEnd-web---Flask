from flask import Flask


def create_app():
    app = Flask(__name__)
    # SECRET_KEY should be secure safely!
    app.config['SECRET_KEY'] = 'abcdefg h1234'

    return app
