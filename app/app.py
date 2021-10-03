import os

from flask import Flask
from .constantes import CONFIG

current_path = os.path.dirname(os.path.abspath(__file__))

templates = os.path.join(current_path, "templates")
statics = os.path.join(current_path, "static")
db = os.path.join(current_path, "data")

app = Flask("CorrespHumboldt", template_folder=templates, static_folder=statics)


# local imports
from .routes import *

def config_app(config_name="test"):
    """ Create the application """
    app.config.from_object(CONFIG[config_name])

    return app
