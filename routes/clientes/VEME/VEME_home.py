from flask import Blueprint,render_template,redirect,url_for
from utils.db import db
import random
VEME_home = Blueprint("VEME_home",__name__)

def mezclar_lista(lista):
    random.shuffle(lista)
    return lista

@VEME_home.route("/clientes/VEME")
def getPrincipalPageVEME():
    prendas = ['remeras','vestidos','pantalones','camperas']
    navbar_imgs = []
    for i in prendas:
        navbar_imgs.append(f'{i}6')
        navbar_imgs.append(f'{i}7')
    
    print(mezclar_lista(navbar_imgs[:7]))
    return render_template("clientes/VEME/VEME.html",prendas = mezclar_lista(prendas),navbar_imgs = mezclar_lista(navbar_imgs[:7]))


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
