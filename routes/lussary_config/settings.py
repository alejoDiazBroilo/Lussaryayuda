from flask import Blueprint,render_template,redirect,url_for,jsonify
from utils.db import db

from models.models import *
Home = Blueprint("Home",__name__)
def Insert(obj):
    db.session.add(obj)
    db.session.commit()

@Home.route("/")
def getHomePrincipalPageLussary():
    return render_template("lussary_config/settings.html")

@Home.route("/home")
def getHome():
    return redirect(url_for('Home.getHomePrincipalPageLussary'))




@Home.route("/api")
def getExample():
    return jsonify({'message':'hello'})

@Home.route("/db/añadir")
def añadir():
    Insert(Persona('Alejo Luis', 'Díaz Broilo', ''))#1
    Insert(Persona('Agustín Jose', 'Salonia', ''))#2
    Insert(Persona('Marco', 'Fini Minué', ''))#3
    Insert(Persona('Máximo Tomas', 'Blázquez', ''))#4
    Insert(Persona('Joaquín', 'Morais', ''))#5
    Insert(Persona('Fernando Gabriel', 'Salonia', 'Ciente y principal comunicador de FERMAG'))#6
    Insert(Medio('Instagram', 'www.instagram.com/', '/'))#1
    Insert(Medio('GitHub', 'https://github.com/', ''))#2
    Insert(Medio('LinkedIn', 'https://ar.linkedin.com/in/', ''))#3
    Insert(Medio('Correo Electronico', '', ''))#4
    Insert(Medio('CHESS.COM', 'https://www.chess.com/member/', ''))#5
    Insert(Contacto(1, 1, 'alejo.diazbroilo'))#IG
    Insert(Contacto(2, 1, 'AlejoLuisDiazBroiloLussary'))#GIT
    Insert(Contacto(4, 1, 'diazbroiloalejolussary@gmail.com')) # MAIL END ALEJO
    Insert(Contacto(1, 2, 'agus04_Salonia'))#IG
    Insert(Contacto(2, 2, 'Salonia04'))#GIT
    Insert(Contacto(4, 2, 'agus'))
    Insert(Contacto(1, 3, 'marco_fm'))#IG
    Insert(Contacto(2, 3, 'MarcoFm1'))#GIT
    Insert(Contacto(1, 4, 'maximoblazquez'))#IG
    Insert(Contacto(1, 5, 'joa_mora05'))#IG
    Insert(Contacto(2, 5, 'JoaquinMorais'))#GIT
    Insert(Contacto(5, 5, 'joamora'))#GIT
    Insert(Colaborador(1, '2004-07-18'))#1
    Insert(Colaborador(2, '2004-08-04'))#2
    Insert(Colaborador(3, '2005-03-22'))#3
    Insert(Colaborador(4, '2005-04-02'))#4
    Insert(Colaborador(5, '2005-03-27'))#5
    Insert(DescripcionColaborador(1, 'pasatiempos', 'le encanta el lol y la pija'))
    Insert(Actividad('backend', ''))
    Insert(Actividad('frontend', ''))
    Insert(Actividad('project manager', ''))
    Insert(Actividad('economia', ''))
    Insert(Actividad('marketing', ''))
    Insert(Actividad('social media', ''))
    Insert(Actividad('diseño', ''))
    Insert(Rol(1, 1))
    Insert(Proyecto('Fermag', 'Lorem ut tortor vestibulum, eget suscipit leo consectetur.'))
    Insert(Proyecto('VEME', 'Lorem i ut tortor vestibulum, eget suscipit leo consectetur.'))
    Insert(SubProyecto(1, 'empresa1', 'almost null because this cries a lot'))
    Insert(Area('hacer el models', 'hacer el model siguiendo el uml', 5))
    Insert(Contribucion(1, 1, 1,  "alejo pudo hacer el models, pendiente revision"))
    Insert(Categoria('descripcion fermag', 'qsy que descripcion ah'))#1
    Insert(AtributoGenerico('titulo', 'nurstro trabajo', 1, 1))
    Insert(SubProyecto(1, 'place holder', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis in ullamcorper ipsum. Aliquam erat volutpat. Aenean quis nunc vel odio sollicitudin auctor vel in mauris. Sed id ex id turpis sollicitudin consectetur. Nam lobortis quam id sem accumsan, eu blandit libero lobortis.'))
    Insert(Categoria('H1', 'uso para titulos entre otros'))#2
    Insert(AtributoGenerico('nombre del proyecto', 'wallmart cables', 2, 1))
    Insert(Categoria('IMG', 'links de imagenes'))#3
    Insert(AtributoGenerico('Imagen proyecto 1', 'https://media.istockphoto.com/id/1334434982/es/foto/fantasma-aterrador-sobre-fondo-oscuro.jpg?s=612x612&w=0&k=20&c=GKJSU3NnvYt0G0m0pv6_PZHn47RL9zkUDHcNFkybPgM=', 1, 2))
    Insert(Categoria('descripcion proyecto', 'descripciones uwu'))#4
    Insert(AtributoGenerico('descripcion de subproyecto 1', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis in ullamcorper ipsum. Aliquam erat volutpat. Aenean quis nunc vel odio sollicitudin auctor vel in mauris. Sed id ex id turpis sollicitudin consectetur. Nam lobortis quam id sem accumsan, eu blandit libero lobortis.', 2, 3))
    Insert(AtributoGenerico('descripcion de subproyecto 2', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis in ullamcorper ipsum. Aliquam erat volutpat. Aenean quis nunc vel odio sollicitudin auctor vel in mauris. Sed id ex id turpis sollicitudin consectetur. Nam lobortis quam id sem accumsan, eu blandit libero lobortis.', 2, 3))
    Insert(Categoria('ubicacion', 'link o coordenadas de ub'))#5
    Insert(Categoria('idframe ubicacion', 'link o coordenadas de ub'))#5
    Insert(AtributoGenerico('ubicacion 1', 'Av. Ejército Argentino 0000, Córdoba', 1, 5))
    Insert(AtributoGenerico('iframe ubicacion 1', 'https://media.istockphoto.com/id/1334434982/es/foto/fantasma-aterrador-sobre-fondo-oscuro.jpg?s=612x612&w=0&k=20&c=GKJSU3NnvYt0G0m0pv6_PZHn47RL9zkUDHcNFkybPgM=', 1, 5))
    Insert(Categoria('Fondo', 'fondo de la pagina'))#6
    Insert(AtributoGenerico('fondo principal', 'https://imgs.search.brave.com/EpboDtNjJG46wigjM5xOWRZPjPCGCjHgHzrDh__b6lY/rs:fit:1200:675:1/g:ce/aHR0cHM6Ly9wYnMu/dHdpbWcuY29tL21l/ZGlhL0VKdDlzR09Y/MEFBdXA1Ny5qcGc', 1, 6))
    return redirect(url_for('Home.traer'))
"""
nombre #titulo del proyecto 
img #imagen representativa del proyecto
proyectoDescripcion #pequenia decripcion del proyecto
cliente #nombre del cliente
descripcion3 #descripcion grande del proyecto
ubicacion #ubicacion del proyecto
mapa #link del iframe de google maps
fondo #fondo del principio 
"""



@Home.route("/db/traer")
def traer():
    database = Persona.query.all()
    print("###########################################")
    for i in range(len(database)):
        print("//////////////////////////////////////////////////////////////////////////////////////////////////////")
        print(database[i].nombre)
        xd = database[i].agenda
        for x in range(len(xd)):
            print(xd[x].medio_relacion.nombre_medio)

    return redirect(url_for('Home.getHome'))
