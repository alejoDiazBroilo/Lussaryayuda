from flask import Blueprint,render_template,redirect,url_for
from utils.db import db
from models.models import Persona,Colaborador,Medio,Contacto,DescripcionColaborador,Rol


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




@Lussary_contribuidores.route("/colaborador/<id>")
def getContribuidor(id):
    try:
        database = Colaborador.query.filter_by(id_colaborador = id).first()
        colaborador = {
            'nombre' : database.persona.nombre,
            'apellido' : database.persona.apellido,
            'rol':database.getActividades().title(),
            'descripcion':'Lorem ipsum dolor sit amet consectetur adipisicing elit. Incidunt ipsam commodi corporis minima inventore? Quasi hic ratione alias consequatur illum?',
            'atributos': 
            [{'atributo':'fa fa-envelope','descripcion': x.getLink()} for x in database.persona.agenda]
            ,
            'socialMedia':
                [{'clase':'fa fa-envelope','link': x.getLink()} for x in database.persona.agenda]
        }

    except Exception as e:
        print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
        print(e)
        return redirect(url_for('Home.getHome'))

    return render_template("lussary_config/colaborador.html",navbar = True,colaborador = colaborador)