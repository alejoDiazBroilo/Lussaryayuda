from flask import Blueprint,render_template,redirect,url_for
from utils.db import db

Fermag_servicios = Blueprint("Fermag_servicios",__name__)


@Fermag_servicios.route("/clientes/Fermag/servicios")
def getServicePageFermag():
    return render_template("clientes/Fermag/servicios.html")


