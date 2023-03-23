from flask import Blueprint,render_template,redirect,url_for
from utils.db import db

Fermag_home = Blueprint("Fermag_home",__name__)


@Fermag_home.route("/clientes/Fermag")
def getPrincipalPageFermag():
    return render_template("clientes/Fermag/fermag.html")

#NOMBRES DE GALERIA
class Proyectos:
    def __init__(self,nombre,descripcion, boton, img):
        self.nombre = nombre
        self.descripcion = descripcion
        self.boton = boton
        self.img = img
        

    def __str__(self):
        return f'{self.nombre}: {self.img} correspondiente al boton: {self.boton} en: {self.descripcion}'

class Descripcion:
    def __init__(self, nombre, descripcion1, descripcion2, fondo):
        self.nombre = nombre
        self.descripcion1 = descripcion1
        self.descripcion2 = descripcion2
        self.fondo = fondo

    def __str__(self):
        return f'{self.nombre}: {self.descripcion1} : {self.descripcion2}'


@Fermag_home.route("/clientes/Fermag/proyectos")
def getProjectPageFermag():
    nombres = [
        Proyectos('HIPERMERCADOS LIBERTAD', 'https://images.unsplash.com/photo-1415018255745-0ec3f7aee47b?dpr=1&auto=format&fit=crop&w=1500&h=938&q=80&cs=tinysrgb&crop=', 'Ver mas', 'Buenos Aires, Argentina'),
        Proyectos('TERMINAL DE OMNIBUS' ,'https://images.unsplash.com/photo-1440688807730-73e4e2169fb8?dpr=1&auto=format&fit=crop&w=1500&h=1001&q=80&cs=tinysrgb&crop=', 'Ver mas', 'Santiago del Estero, Argentina'),
        Proyectos('HOSPITAL PASTEUR', 'https://images.unsplash.com/photo-1415018255745-0ec3f7aee47b?dpr=1&auto=format&fit=crop&w=1500&h=938&q=80&cs=tinysrgb&crop=', 'Ver mas', 'Cordoba, Argentina')
        ]
    
    return render_template("clientes/Fermag/proyectos.html", nombres=nombres)


@Fermag_home.route("/clientes/Fermag/proyectos/x")
def getProjectDates():
    descripciones = [
        Descripcion('Aca iria el nombre','Aca va una descripcion breve','ccc', 'https://www.yachtandboat.com/wp-content/uploads/2018/12/hero-image-2.jpg')
    ]

    return render_template("clientes/Fermag/proyectoss.html", descripciones=descripciones)


