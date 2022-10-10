from flask import Flask


def create_app():
    app = Flask(__name__)
    # SECRET_KEY should be secure safely!
    app.config['SECRET_KEY'] = 'abcdefg h1234'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
