from flask import Blueprint,render_template,redirect,url_for
from utils.db import db

VEME_home = Blueprint("VEME_home",__name__)


@VEME_home.route("/clientes/VEME")
def getPrincipalPageVEME():
    return render_template("clientes/VEME/VEME.html")


"""

@Home.route("/")
def getHome():
    return render_template("home/home.html")


@Home.route("/db/añadir")
def añadir():
    newInstance = ExampleDatabase('Coca cola','Bebida bebible')
    db.session.add(newInstance)
    db.session.commit()
    return redirect(url_for('Home.getHome'))

@Home.route("/db/traer")
def traer():
    database = ExampleDatabase.query.all()
    print(database)
    return redirect(url_for('Home.getHome'))


"""
