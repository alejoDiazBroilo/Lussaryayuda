from flask import Blueprint,render_template,redirect,url_for
from utils.db import db

from models.models import *

Fermag_home = Blueprint("Fermag_home",__name__)

def getNavBar():
    return [
        ('Empresa','url_for','Fermag_home.FermagHome'),
        ('Noticias','url_for','Fermag_home.FermagNoticias'),
        ('Servicios','id','#servicios-servicios'),
        ('Ubicacion','link','https://www.google.com/maps/?hl=es'),
        ('Contacto','url_for','Fermag_contacto.FermagContacto')
    ]


#Yeah
@Fermag_home.route('/Fermag')
def FermagHome():
    NavBar = getNavBar()
    subproyectos = SubProyecto.query.filter_by(descripcion = "servicio").all()
    diccionario = {}
    for i in subproyectos:
        atributos = i.atributos
        atributos_diccionario = {}

        for j in atributos:
            
            atributos_diccionario[f'{j.titulo}']  = j.valor        

        diccionario[f'{i.titulo}'] = atributos_diccionario

    return render_template('/clientes/Fermag/fermag.html', navBar = NavBar, subpro=subproyectos, atrib = diccionario)


@Fermag_home.route('/Fermag/noticias')
def FermagNoticias():
    NavBar = getNavBar()
    Notis = [
        ('https://thumbs.dreamstime.com/t/animaci%C3%B3n-del-s%C3%ADmbolo-signo-de-interrogaci%C3%B3n-en-fondo-negro-abstracta-un-120634323.jpg', '???', 'Proximamente...'),
        ('https://thumbs.dreamstime.com/t/animaci%C3%B3n-del-s%C3%ADmbolo-signo-de-interrogaci%C3%B3n-en-fondo-negro-abstracta-un-120634323.jpg', '???', 'Proximamente...'),
        ('https://thumbs.dreamstime.com/t/animaci%C3%B3n-del-s%C3%ADmbolo-signo-de-interrogaci%C3%B3n-en-fondo-negro-abstracta-un-120634323.jpg', '???', 'Proximamente...'),
        ('https://thumbs.dreamstime.com/t/animaci%C3%B3n-del-s%C3%ADmbolo-signo-de-interrogaci%C3%B3n-en-fondo-negro-abstracta-un-120634323.jpg', '???', 'Proximamente...')
    ]
    return render_template('/clientes/Fermag/noticias.html', navBar = NavBar,notis = Notis)

@Fermag_home.route("/Fermag")
def getPrincipalPageFermag():
    return render_template("clientes/Fermag/fermag.html")



