from flask import Blueprint,render_template,redirect,url_for, request
from utils.db import db

Fermag_contacto = Blueprint("Fermag_contacto",__name__)

@Fermag_contacto.route("/Fermag/contacto")    
def FermagContacto():
        return render_template('/clientes/Fermag/contacto.html')

    