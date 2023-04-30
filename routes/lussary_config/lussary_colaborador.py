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




@Lussary_contribuidores.route("/colaborador/<nombre>")
def getContribuidor(nombre):
    try:
        #colaborador = Persona.query.filter_by(id_persona=1).first()
        colaborador = {
            'nombre' : nombre,
            'apellido' : 'Pepito',
            'edad': 18,
            'rol':'Developer and Businessman',
            'descripcion':'Lorem ipsum dolor sit amet consectetur adipisicing elit. Incidunt ipsam commodi corporis minima inventore? Quasi hic ratione alias consequatur illum?',
            'atributos': [
                {'atributo' :'Age','descripcion' :'Pepe'},
                
            ],
            'socialMedia':[
                {'clase':'fa fa-envelope','link': "https://wa.me/5493518147051/?text=Hola%20buenos%20dias!."},
                {'clase':'fab fa-whatsapp','link': "https://wa.me/5493518147051/?text=Hola%20buenos%20dias!."},
                {'clase':'fab fa-whatsapp','link': "https://wa.me/5493518147051/?text=Hola%20buenos%20dias!."},
                {'clase':'fab fa-whatsapp','link': "https://wa.me/5493518147051/?text=Hola%20buenos%20dias!."},
                {'clase':'fab fa-whatsapp','link': "https://wa.me/5493518147051/?text=Hola%20buenos%20dias!."},
            ]
        }

    except Exception as e:
        print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
        print(e)
        return redirect(url_for('Home.getHome'))

    return render_template("lussary_config/colaborador.html",navbar = True,colaborador = colaborador)