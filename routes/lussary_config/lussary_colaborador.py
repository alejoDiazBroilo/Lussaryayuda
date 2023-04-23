from flask import Blueprint,render_template,redirect,url_for
from utils.db import db
from models.models import Persona,Colaborador,Medio,Contacto,DescripcionColaborador,Rol


Lussary_contribuidores = Blueprint("Lussary_contribuidores",__name__)


@Lussary_contribuidores.route("/colaboradores")
def getContribuidores():
    return render_template("lussary_config/colaboradores.html",navbar = True)




@Lussary_contribuidores.route("/colaborador/<nombre>")
def getContribuidor(nombre):
    try:
        #colaborador = Persona.query.filter_by(id_persona=1).first()
        colaborador = {
            'nombre' : nombre,
            'apellido' : 'Morais',
            'edad': 18,
            'rol':'Developer and Businessman',
        }

    except Exception as e:
        print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
        print(e)
        return redirect(url_for('Home.getHome'))

    return render_template("lussary_config/colaborador.html",navbar = True,colaborador = colaborador)