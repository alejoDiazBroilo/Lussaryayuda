from flask import Blueprint,render_template,redirect,url_for
from utils.db import db
from models.models import *


Lussary_contribuidores = Blueprint("Lussary_contribuidores",__name__)


@Lussary_contribuidores.route("/colaboradores")
def getContribuidores():

    iconos = [
        'Trebol.png',
        'Heart.png',
        'Diamond.png',
        'Spade.png',
    ]

    cartas = [
        {
            'url_foto':'1.jpg',
            'simbol' : 'A',
            'cant_simbol' : 1,
            'icon' : 'Heart.png',
            'redirect':'1'
        },
        {
            'url_foto':'1.jpg',
            'simbol' : '9',
            'cant_simbol' : 9,
            'icon' : 'Spade.png',
            'redirect':'2'
        },
        {
            'url_foto':'1.jpg',
            'simbol' : 'K',
            'cant_simbol' : 1,
            'icon' : 'Trebol.png',
            'redirect':'3'
        },
        {
            'url_foto':'1.jpg',
            'simbol' : '2',
            'cant_simbol' : 2,
            'icon' : 'Diamond.png',
            'redirect':'4'
        },
        {
            'url_foto':'1.jpg',
            'simbol' : 'Q',
            'cant_simbol' : 1,
            'icon' : 'Spade.png',
            'redirect':'5'
        },
    ]

    return render_template("lussary_config/colaboradores.html",navbar = True,cant_cards = len(cartas),cartas = cartas )




@Lussary_contribuidores.route("/colaborador/<int:id>")
def getContribuidor(id):
    colaborador = Colaborador.query.filter_by(id_colaborador = id).first()
    persona = Persona.query.filter_by(id_persona = id).first()
    contactos = Contacto.query.filter_by(id_persona = id).all()
    descripcionColaborador = DescripcionColaborador.query.filter_by(id_colaborador = id).all()
    data = {
        'nombre' : persona.nombre,
        'apellido' : persona.apellido,
        'rol':colaborador.getActividades().title(),
        'descripcion':persona.descripcion,
        'atributos': 
        [{'atributo':x.titulo,'descripcion': x.descripcion} for x in descripcionColaborador]
        ,
        'socialMedia':
            [{'clase':x.getIcono(),'link': x.getLink()} for x in contactos if (x.isLink()==True)]
    }


    return render_template("lussary_config/colaborador.html",navbar = True,colaborador = data)