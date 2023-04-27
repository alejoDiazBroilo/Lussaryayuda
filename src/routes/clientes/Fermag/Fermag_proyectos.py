
from flask import Blueprint,render_template,redirect,url_for
from utils.db import db

from models.models import *

Fermag_proyectos = Blueprint("Fermag_proyectos",__name__)

@Fermag_proyectos.route("/Fermag/proyectos/<x>")    
def FermagProyectos(x):
    subproyectos = SubProyecto.query.filter_by(descripcion = x).all()
    diccionario = {}
    for i in subproyectos:
        atributos = i.atributos
        atributos_diccionario = {}

        for j in atributos:
            
            atributos_diccionario[f'{j.titulo}']  = j.valor        

        diccionario[f'{i.titulo}'] = atributos_diccionario
    return render_template("clientes/Fermag/proyectos.html", subpro=subproyectos, atrib = diccionario)


@Fermag_proyectos.route("/Fermag/proyectos/x")
def FermagProyectoInd():
    return render_template("clientes/Fermag/proyectoss.html", descripciones=descripciones)
