from flask import render_template, request
from nested_lookup import nested_lookup

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
    contributors = set(nested_lookup("contributor", data))


    if "on" in search_list:
        results = data

    if search_list[0]:
        for i in data:
            if search_list[0] in i["title"]:
                results.append(i)
    
    elif search_list[1]:
        for i in data:
            try:
                if search_list[1] in i["coverage"]:
                    results.append(i)
            except: continue
    
    elif search_list[2]:
        for i in data:
            try:
                if search_list[2] in i["date"]:
                    results.append(i)
            except: continue

    elif search_list[3]:
        for i in data:
            try:
                if search_list[3] in i["contributor"]:
                    results.append(i)
            except: continue


    count_letters= len(results)
    return render_template("pages/search.html", results=results, count=count_letters, institutions=contributors)
