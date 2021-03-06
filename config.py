import os


class Config:
    """
    general configuration parent class

    """
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://eugene:necromancer@localhost/blog'
    # csrf secret key
    SECRET_KEY = os.environ.get('SECRET_KEY')

    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    # simplemde configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CON = True

    # email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


class ProdConfig(Config):
    """
    production configuration child class
    """
    pass


class TestConfig(Config):
    """
    tests configuration class
    """
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://eugene:necromancer@localhost/blog_test'


class DevConfig(Config):
    """
    development configuration child class
    """
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}
