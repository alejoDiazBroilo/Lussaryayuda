from flask import Blueprint,render_template,redirect,url_for,jsonify
from utils.db import db

from models.tasks import *
Home = Blueprint("Home",__name__)


@Home.route("/")
def getHomePrincipalPageLussary():
    return render_template("lussary_config/settings.html")

@Home.route("/home")
def getHome():
    return redirect(url_for('Home.getHomePrincipalPageLussary'))

@Home.route("/galeria")
def getGaleria():
    return render_template("lussary_config/galeria.html")


@Home.route("/api")
def getExample():
    return jsonify({'message':'hello'})

@Home.route("/db/añadir")
def añadir():
    newInstance = Persona('firstPerson','apellido', 'cosa que hice')
    db.session.add(newInstance)
    db.session.commit()
    return redirect(url_for('Home.getHome'))

@Home.route("/db/traer")
def traer():
    database = Persona.query.all()
    print(database)
    return redirect(url_for('Home.getHome'))
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
