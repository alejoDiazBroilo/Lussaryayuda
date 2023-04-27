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

    Insert(Cliente(6, 1, 1))
    
    Insert(Contribucion(1, 1, 1,  "alejo pudo hacer el models, pendiente revision", 15))

    Insert(Categoria('descripcion', 'varchar'))#1
    Insert(Categoria('titulo', 'h1'))#2
    Insert(Categoria('IMG_link', 'link'))#3
    Insert(Categoria('ubicacion_link', 'link'))#4
    Insert(Categoria('idframe_ubicacion_link', 'link'))#5
    Insert(Categoria('Fondo_link', 'link'))#6
    Insert(Categoria('info', 'varchar'))#7

    Insert(SubProyecto(1, 'Domotica', 'servicio'))#1

    Insert(SubProyecto(1, 'CENTRO CULTURAL LOLA MORA','servicio_1'))#2
    
    Insert(AtributoGenerico('descripcion principal', 'Ejecucion de Proyecto, provision e instalación de los siguientes sistemas: Generación Fotovoltaica, Generación Eólica, Sistema de control BMS (Building Management System), Sistema de control de Accesos, Sistema de Vigilancia por Circuito Cerrado de TV (CCTV), Sistema de Voz y Datos por IP, Sistema de Detección temprana de Incendio', 2, 1))
    Insert(AtributoGenerico('ubicacion', 'https://goo.gl/maps/1NqdjNhLxUNsfEYSA', 2, 4))
    Insert(AtributoGenerico('año', '2023', 2, 1))
    Insert(AtributoGenerico('descripcion detalles', 'La i nstalación de todo lo contartado forma parte del concepto para el cual esta destinado el edificio y es en lograra la certificación LEED (Liderazgo en Energía y Diseño Ambiental, por sus siglas en inglés). Algunos datos que resaltan nuestra provision son:'))
    

    return redirect(url_for('Home.traer'))

@Home.route("/db/traer")
def traer():
    query = Colaborador.query.filter_by(id_colaborador = 1).all()
    for i in query:
        print(i.persona.nombre)        

    return redirect(url_for('Home.getHome'))

"""
||||||||||||||||||||||||||||||||
    query persona all:
    
    query = Persona.query.all()
    for i in query:
        print(i.nombre)
NOTA: ojo por donde empiezan las queries, persona tiene tanto 
colaborador, como cliente, si se usa el backref para llegar
a cualquiera, antento con los atributos que se usan.
Si tenes que sacar datos de colaborador, usa el backref a persona, no al revez.
Como estan los clientes en algunas Personas te va a salir como resultado None, y si
intentas acceder a los datos de None, te peta la pagina.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
get agenda
    query = Persona.query.all()
    for i in query:
        extra_data = i.agenda
        for j in extra_data:
            print(j.info_contacto)
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
get colaborador
    query = Persona.query.all()
    for i in query:
        print(i.colaborador_datos)
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
get cliente
    query = Persona.query.all()
    for i in range(len(query)):
        print(query[i].cliente_datos)
||||||||||||||||||||||||||||||||
    query medio all:
    
    query = Medio.query.all()
    for i in query:
        print(i.nombre_medio)
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
get Contacto
def traer():
    query = Medio.query.all()
    for i in query:
        extra_info = i.dato_contacto
        for j in extra_info:
            print(j.info_contacto, i.nombre_medio)
################################
tambien se puede acceder a persona y desde a persona a colaborador/proyecto/subproyectos/atributos/categorias
tenes que usar los backrefs
||||||||||||||||||||||||||||||||
    query Contacto all:
    
    query = Contacto.query.all()
    for i in query:
        print(i.nombre_medio)
"""