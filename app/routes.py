from flask import render_template, request

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


@app.route("/search")
def search():
    """
    Route permettant l'affichage de la page à propos
    :return: template about.html
    :rtype: template
    """
    data = get_json(statics + "/records.json")
    search_list = [i for i in request.args.values()]
    results = []

    if "on" in search_list:
        results = data

    count_letters= len(results)
    return render_template("pages/search.html", results=results, count=count_letters)
