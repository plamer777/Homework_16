"""This unit contains a configured Flask app and database object to import
in another modules"""
import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from configs.flask_config import FlaskConfig, FlaskTestingConfig
# ------------------------------------------------------------------------

# creation of a Flask app
app = Flask(__name__)

if os.environ.get('CURRENT_MODE') == 'Test':
    app.config.from_object(FlaskTestingConfig)

else:
    app.config.from_object(FlaskConfig)
# creation a database object
db = SQLAlchemy(app)
