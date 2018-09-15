# importation of packages
from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_simplemde import SimpleMDE

# creation of instance of login
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

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