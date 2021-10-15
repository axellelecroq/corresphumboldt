from flask import render_template

from app.app import app, statics
from .utils.generic import get_json


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

@app.route("/search", methods=["GET", "POST"])
def search():
    """
    Route permettant l'affichage de la page à propos
    :return: template about.html
    :rtype: template
    """
    data = get_json(statics + "/records.json")
    return render_template("pages/search.html")
