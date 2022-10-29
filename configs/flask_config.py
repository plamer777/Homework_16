"""This unit contains a FlaskConfig class to configure a Flask application"""
from os import path
# ------------------------------------------------------------------------


class FlaskConfig:
    """FlaskConfig class with necessary settings"""
    SQLALCHEMY_DATABASE_URI = f'sqlite:///' \
                              f'{path.abspath(path.join("data", "work.db"))}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False
    JSON_SORT_KEYS = False

    def __repr__(self):

        return f"FlaskConfig({self.SQLALCHEMY_DATABASE_URI})"


class FlaskTestingConfig:
    """Configuration class for Flask application"""
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False
    JSON_SORT_KEYS = False

    def __repr__(self):

        return f"FlaskConfig({self.SQLALCHEMY_DATABASE_URI})"