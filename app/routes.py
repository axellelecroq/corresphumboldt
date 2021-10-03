from flask import render_template
import json

from .app import app, db


"""
/
/toutes
/chiffres
/a_propos 
"""


@app.route("/")
def home():
    """
    Route permettant l'affichage de la page d'accueil
    :return: template home.html de la page d'accueil
    :rtype: template
    """
    return render_template("pages/home.html")


@app.route("/about")
def about():
    """
    Route permettant l'affichage de la page à propos
    :return: template about.html
    :rtype: template
    """
    return render_template("pages/about.html")

@app.route("/all")
def all_correspondents():
    """
    Route permettant l'affichage de la page à propos
    :return: template about.html
    :rtype: template
    """
    all = db
    return render_template("pages/all.html", person = all)

