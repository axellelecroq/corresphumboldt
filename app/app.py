# Import des libraires standards
import os

# Import des libraires tierces
from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
#from flask_login import LoginManager

from .constantes import CONFIG

# Déclarations liées au module os :
current_path = os.path.dirname(os.path.abspath(__file__))

# Stockage des différents chemins dans des variables
templates = os.path.join(current_path, "templates")
statics = os.path.join(current_path, "static")

app = Flask("CorrespHumboldt", template_folder=templates, static_folder=statics)

#login = LoginManager(app)

# On initie l'extension SQLAlchemy à l'application Flask;
# la DB est stockée dans une variable db
#db = SQLAlchemy(app)


# Imports locaux
from .routes import home, about, search


def config_app(config_name="test"):
    """ Create the application """
    app.config.from_object(CONFIG[config_name])

    # Set up extensions
    #db.init_app(app)
    # assets_env = Environment(app)
    #login.init_app(app)

    # Register Jinja template functions

    return app
    