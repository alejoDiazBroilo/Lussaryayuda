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

@Home.route("/galeria")
def getGaleria():
    return render_template("lussary_config/galeria.html")


@Home.route("/api")
def getExample():
    return jsonify({'message':'hello'})

@Home.route("/db/añadir")
def añadir():
    lista_inserts = []
    """                             Proyecto
    lista_inserts.append(Proyecto('Fermag', 'Lorem ut tortor vestibulum, eget suscipit leo consectetur.'))
    lista_inserts.append(Proyecto('VEME', 'Lorem i ut tortor vestibulum, eget suscipit leo consectetur.'))
                                    SubProyecto
    lista_inserts.append(SubProyecto(1, 'empresa1', 'almost null because this cries a lot'))
                                    Persona
    lista_inserts.append(Persona('Alejo Luis', 'Diaz Broilo', 'el pibe mas lindo de la empresa'))
    lista_inserts.append(Persona('PAPA SALO', 'Apellido', 'insert generico'))
                                    Medio
    lista_inserts.append(Medio('instagram', 'www.instagram.com/', '/'))
                                    Contacto
    lista_inserts.append(Contacto(1, 1, 'alejo.diazbroilo'))
    print(f"{database[i].persona_relacion.nombre}, {database[i].medio_relacion.link_contacto}{database[i].info_contacto}{database[i].medio_relacion.link_contacto_fin}")
                                    Colaborador
    lista_inserts.append(Colaborador(4))#fecha_nacimiento peta, probablemente porque tenga que insertarlo como atributo de clase
                                    DescripcionColaborador
    lista_inserts.append(DescripcionColaborador(5, 'pasatiempos', 'le encanta el lol y la pija'))
    print(f"{database[i].colaborador_relacion.persona_relacion.nombre}, {database[i].titulo}: {database[i].descripcion}")
                                    Actividad
    lista_inserts.append(Actividad('backend', 'back de atras, end de tu nariz contra mis bolas'))
    print(f"{database[i].titulo} {database[i].descripcion}")
                                    Rol
    lista_inserts.append(Rol(5, 1))
    print(f"{database[i].actividad_relacion.titulo} {database[i].actividad_relacion.descripcion} {database[i].colaborador_relacion.persona_relacion.nombre}")
                                    Cliente
    lista_inserts.append(Cliente(5, 2, 1))
    print(f"{database[i].persona_relacion.nombre} {database[i].colaborador_relacion.persona_relacion.nombre}")
                                    Area
    lista_inserts.append(Area('hacer el models', 'hacer el model siguiendo el uml', 5))
    print(f"{database[i].titulo} {database[i].descripcion}")
                                    Contribucion
    lista_inserts.append(Contribucion(5, 1, 1,  "alejo pudo hacer el models, pendiente revision"))
    print(f"{database[i].area_relacion.titulo} {database[i].proyecto_relacion.titulo} {database[i].colaborador_relacion.persona_relacion.nombre}")
                                    Categoria
    lista_inserts.append(Categoria('descripcion fermag', 'qsy que descripcion ah'))
    print(database[i].titulo, database[i].descripcion)
                                    AtributoGenerico
    lista_inserts.append(AtributoGenerico('titulo', 'nurstro trabajo', 1, 1))
    print(database[i].titulo, database[i].subproyecto_relacion.proyecto_relacion.titulo)
    """
    Insert(Persona('Alejo Luis', 'Diaz Broilo', 'el pibe mas lindo de la empresa'))
    Insert(Persona('PAPA SALO', 'Apellido', 'insert generico'))
    Insert(Medio('instagram', 'www.instagram.com/', '/'))
    Insert(Contacto(1, 1, 'alejo.diazbroilo'))
    Insert(Colaborador(1, '2004-07-18'))#fecha_nacimiento peta, probablemente porque tenga que insertarlo como atributo de clase
    Insert(DescripcionColaborador(1, 'pasatiempos', 'le encanta el lol y la pija'))
    Insert(Actividad('backend', 'back de atras, end de tu nariz contra mis bolas'))
    Insert(Rol(1, 1))
    Insert(Proyecto('Fermag', 'Lorem ut tortor vestibulum, eget suscipit leo consectetur.'))
    Insert(Proyecto('VEME', 'Lorem i ut tortor vestibulum, eget suscipit leo consectetur.'))
    return redirect(url_for('Home.traer'))


@Home.route("/db/traer")
def traer():
    database = DescripcionColaborador.query.all()
    print("###########################################")
    for i in range(len(database)):
        print("//////////////////////////////////////////////////////////////////////////////////////////////////////")
        print(f"{database[i].colaborador_relacion.persona_relacion.nombre}, {database[i].titulo}: {database[i].descripcion}")
        
    return redirect(url_for('Home.getHome'))
    
    """
                                    EJEMPLO DE QUERY DENTRO DE RELACION
    database = Persona.query.all()
    print("###########################################")
    for i in range(len(database)):
        ultraquery = database[i].contacto_relacion
        for x in range(len(ultraquery)):
            print(f"{ultraquery[i].medio_relacion.link_contacto}{database[i].nombre}{ultraquery[i].medio_relacion.link_contacto_fin}")
        print("//////////////////////////////////////////////////////////////////////////////////////////////////////")
    return redirect(url_for('Home.getHome'))
    
    """
"""

@Home.route("/")
def getHome():
    return render_template("home/home.html")


@Home.route("/db/añadir")
def añadir():
    newInstance = ExampleDatabase('Coca cola','Bebida bebible')
    db.session.add(newInstance)
    db.session.commit()
    return redirect(url_for('Home.getHome'))

@Home.route("/db/traer")
def traer():
    database = ExampleDatabase.query.all()
    print(database)
    return redirect(url_for('Home.getHome'))


"""
