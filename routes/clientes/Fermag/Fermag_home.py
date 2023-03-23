from flask import Blueprint,render_template,redirect,url_for
from utils.db import db

Fermag_home = Blueprint("Fermag_home",__name__)


@Fermag_home.route("/clientes/Fermag")
def getPrincipalPageFermag():
    return render_template("clientes/Fermag/fermag.html")

#NOMBRES DE GALERIA
class Proyectos:
    def __init__(self,nombre,descripcion, boton):
        self.nombre = nombre
        self.descripcion = descripcion
        self.boton = boton

    def __str__(self):
        return f'{self.nombre}: {self.descripcion} correspondiente al boton: {self.boton}'

@Fermag_home.route("/clientes/Fermag/proyectos")
def getProjectPageFermag():
    nombres = [
        Proyectos('Pene','https://images.unsplash.com/photo-1415018255745-0ec3f7aee47b?dpr=1&auto=format&fit=crop&w=1500&h=938&q=80&cs=tinysrgb&crop=', 'Ver mas'),
        Proyectos('Pito','https://images.unsplash.com/photo-1440688807730-73e4e2169fb8?dpr=1&auto=format&fit=crop&w=1500&h=1001&q=80&cs=tinysrgb&crop=', 'Ver mas'),
        Proyectos('Banana','https://images.unsplash.com/photo-1415018255745-0ec3f7aee47b?dpr=1&auto=format&fit=crop&w=1500&h=938&q=80&cs=tinysrgb&crop=', 'Ver mas')
        ]
    
    return render_template("clientes/Fermag/proyectos.html", nombres=nombres)


