from flask import Blueprint,render_template,redirect,url_for
from utils.db import db
from models.models import Persona,Colaborador,Medio,Contacto,DescripcionColaborador,Rol


Lussary_contribuidores = Blueprint("Lussary_contribuidores",__name__)


@Lussary_contribuidores.route("/colaboradores")
def getContribuidores():

    iconos = [
        'trebol.png',
        'heart.svg',
        'diamond.svg',
        'spade.png',
    ]
    simbols = [
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        '10',
        'J',
        'Q',
        'K',
        'A'
    ]
    s = 3
    n = 7
    if(simbols[n] in ['A','J','Q','K']):
        cant=1
    else:
        cant = int(simbols[n])
    return render_template("lussary_config/colaboradores.html",navbar = True,cant_cards = 2, icon = iconos[s],simbol = simbols[n],cant = cant)




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