# initialising flask

from flask import Flask

app=Flask(__name__)


def create_app(config_name):
    """
    application factory function
    :param config_name:
    :return:
    """
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])
    # initialising bootstrap
    bootstrap.init_app(app)
    # initialising db model
    db.init_app(app)
    # initialising flask login
    login_manager.init_app(app)

    # configure uploads set
    # configure_uploads(app, photos)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/authenticate')

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    """
    registering blueprint instance
    url_prefix adds prefix to all routes registered with blueprint

    """
    mail.init_app(app)
    simple.init_app(app)
    db.init_app(app)

    return app