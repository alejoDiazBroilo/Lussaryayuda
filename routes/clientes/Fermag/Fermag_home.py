from flask import Blueprint,render_template,redirect,url_for
from utils.db import db

Fermag_home = Blueprint("Fermag_home",__name__)


@Fermag_home.route("/clientes/Fermag")
def getPrincipalPageFermag():
    return render_template("clientes/Fermag/fermag.html")


@Fermag_home.route("/clientes/Fermag/proyectos")
def getProjectPageFermag():
    return render_template("clientes/Fermag/proyectos.html")