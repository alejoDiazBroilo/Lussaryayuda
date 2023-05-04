from utils.db import db
from sqlalchemy import Column, Integer, String, Date, func, ForeignKey
from datetime import datetime


class Persona(db.Model): # se pueden hacer las querys
    __tablename__ = 'persona'
    id_persona = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(70), nullable = False)
    apellido = db.Column(db.String(70), nullable = False)
    descripcion = db.Column(db.String(1000), default = None)

    contactos = db.relationship('Contacto', lazy=True)

    def __init__(self,nombre, apellido, descripcion):
        self.nombre = nombre
        self.apellido = apellido
        self.descripcion = descripcion

    def __repr__(self):
        return f'Nombre: {self.nombre}, Apellido: {self.apellido}\n'

"""
personas = Persona.query.all()
lista_agenda = personas[i].<agenda / colaborador_datos / cliente_datos> (te guarda todos los objetos de agenda que tengan persona)
lista_agenda[i].<datos agenda>
"""



class Medio(db.Model): # se pueden hacer las querys
    __tablename__ = 'medio'
    id_medio = db.Column(db.Integer, primary_key=True)
    nombre_medio = db.Column(db.String(70), nullable = False)
    link_contacto = db.Column(db.String(1000), nullable = False) #unique
    link_contacto_fin = db.Column(db.String(1000), nullable = False) #unique
    icono = db.Column(db.String(1000), nullable = True)

    def __init__(self, nombre_medio, link_contacto, link_contacto_fin):
        self.nombre_medio = nombre_medio
        self.link_contacto = link_contacto
        self.link_contacto_fin = link_contacto_fin
    
    def __repr__(self):
        return f'link: {self.link_contacto}_{self.link_contacto_fin}\n'
"""
medios = Medios.query.all()
lista_agenda = medios[i].<contacto_relacion> (te guarda todos los objetos de agenda que tengan persona)
lista_agenda[i].<datos agenda>
"""





class Contacto(db.Model): # se pueden hacer las querys
    __tablename__ = 'contacto'
    id_contacto = db.Column(db.Integer, primary_key=True)
    id_medio = db.Column(db.Integer, ForeignKey('medio.id_medio', ondelete='SET NULL', onupdate='CASCADE'))
    id_persona = db.Column(db.Integer, ForeignKey('persona.id_persona', ondelete='SET NULL', onupdate='CASCADE')) #persona_relatio
    info_contacto = db.Column(db.String(1000), nullable = False) 

    contacto_datos = db.relationship('Medio', lazy=True)#ignore
    
    def __init__(self, medio, persona, info_contacto):
        self.id_medio = medio
        self.id_persona = persona
        self.info_contacto = info_contacto
    
    def __repr__(self):
        return f'{self.info_contacto}\n'

    def getLink(self):
        return self.medio_relacion.link_contacto + self.info_contacto + self.medio_relacion.link_contacto_fin
"""
contactos = Contacto.query.all()
personas = contactos[i].<persona_agenda> usando el backref en las clases que tienen las relationships
"""






class Colaborador(db.Model):# se pueden hacer las querys
    __tablename__ = 'colaborador'
    id_colaborador = db.Column(db.Integer, ForeignKey('persona.id_persona', onupdate='CASCADE'), primary_key=True, autoincrement=False) #persona_relatio
    fecha_nacimiento = db.Column(db.Date)

    roles = db.relationship('Rol', lazy=True)

    def __init__(self, colaborador, fecha_nacimiento=None):
        self.id_colaborador = colaborador
        self.fecha_nacimiento = fecha_nacimiento
        if fecha_nacimiento is not None:
            self.fecha_nacimiento = fecha_nacimiento
    
    def __repr__(self):
        return f'{self.fecha_nacimiento}\n'

    def calcularEdad(self):
        fecha_actual = datetime.now()
        edad = fecha_actual.year - self.fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))
        return edad
    
    def getActividades(self):
        cadena = ''
        for x in self.roles:
            cadena += f"{x.actividad},"
        return cadena[:-1]

"""   
colaboradores = Colaborador.query.all()
lista_colaboradores = colaboradores[i].<persona> (te guarda todos los objetos de agenda que tengan persona)
colaboradores[i].<datos colaborador>
"""




class DescripcionColaborador(db.Model):# se pueden hacer las querys
    __tablename__ = 'descripcioncolaborador'
    id_descripcioncolaborador = db.Column(db.Integer, primary_key=True)
    id_colaborador = db.Column(db.Integer, ForeignKey('colaborador.id_colaborador', ondelete='SET NULL', onupdate='CASCADE'))
    titulo = db.Column(db.String(50), default = None)
    descripcion = db.Column(db.String(1000), default = None)
    
    def __init__(self, colaborador, titulo, descripcion):
        self.id_colaborador = colaborador
        self.titulo = titulo
        self.descripcion = descripcion
    
    def __repr__(self):
        return f'{self.colaborador} = {self.titulo}\n'





class Actividad(db.Model):# se pueden hacer las querys
    __tablename__ = 'actividad'
    id_actividad = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(50), default = None) #unique
    descripcion = db.Column(db.String(1000), default = None)

    def __init__(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion
    
    def __repr__(self):
        return f'{self.titulo}\n'






class Rol(db.Model):# se pueden hacer las querys
    __tablename__ = 'rol'
    id_rol = db.Column(db.Integer, primary_key=True)
    id_actividad = db.Column(db.Integer, ForeignKey('actividad.id_actividad', ondelete='SET NULL', onupdate='CASCADE'))
    id_colaborador = db.Column(db.Integer, ForeignKey('colaborador.id_colaborador', ondelete='SET NULL', onupdate='CASCADE'))

    actividades = db.relationship('Actividad', lazy = True)

    def __init__(self, colaborador, actividad):
        self.id_colaborador = colaborador
        self.id_actividad = actividad
    
    def __repr__(self):
        return f'{self.colaborador} = {self.actividad}\n'







class Proyecto(db.Model): 
    __tablename__ = 'proyecto'
    id_proyecto = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fecha_creacion = db.Column(db.Date, default=func.now(), nullable=False)
    titulo = db.Column(db.String(50), nullable=False, unique=True)
    descripcion = db.Column(db.String(1000), nullable=True)
    
    def __init__(self, titulo, descripcion=None, fecha_creacion=None):
        self.titulo = titulo
        self.descripcion = descripcion
        if fecha_creacion is not None:
            self.fecha_creacion = fecha_creacion
    
    def __repr__(self):
        return f'{self.titulo}\n'







class Cliente(db.Model): #Proyecto relacion done
    __tablename__ = 'cliente'
    id_cliente = db.Column(db.Integer, ForeignKey('persona.id_persona', onupdate='CASCADE'), primary_key=True, autoincrement=False) #persona_relatio
    id_colaborador = db.Column(db.Integer, ForeignKey('colaborador.id_colaborador', ondelete='SET NULL', onupdate='CASCADE'))
    id_proyecto = db.Column(db.Integer, ForeignKey('proyecto.id_proyecto', ondelete='SET NULL', onupdate='CASCADE'))

    fecha_creacion = db.Column(db.Date, default=func.now(), nullable=False)

    def __init__(self, cliente, colaborador, proyecto, fecha_creacion=None):
        self.id_cliente = cliente
        self.id_colaborador = colaborador
        self.id_proyecto = proyecto
        if fecha_creacion is not None:
            self.fecha_creacion = fecha_creacion
    def __repr__(self):
        return f'{self.persona}, {self.proyecto}\n'







class Area(db.Model):
    __tablename__ = 'area'
    id_area = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(50), default = None) #unique=True
    descripcion = db.Column(db.String(1000), default = None)
    puntaje = db.Column(db.Integer, default = None)

    def __init__(self, titulo, descripcion, puntaje):
        self.titulo = titulo
        self.descripcion = descripcion
        self.puntaje = puntaje

    
    def __repr__(self):
        return f'{self.titulo}, {self.puntaje}\n'







class Contribucion(db.Model): #Area relacion
    __tablename__ = 'contribucion' 
    id_contribucion = db.Column(db.Integer, primary_key=True)
    fecha_creacion = db.Column(db.Date, default=func.now())
    descripcion = db.Column(db.String(1000), default = None)
    id_colaborador = db.Column(db.Integer, ForeignKey('colaborador.id_colaborador', ondelete='SET NULL', onupdate='CASCADE'))
    id_proyecto = db.Column(db.Integer, ForeignKey('proyecto.id_proyecto', ondelete='SET NULL', onupdate='CASCADE'))
    id_area = db.Column(db.Integer, ForeignKey('area.id_area', ondelete='SET NULL', onupdate='CASCADE'))
        
    areas = db.relationship('Area', lazy = True)

    def __init__(self, colaborador, proyecto, area, descripcion, fecha_creacion=None):
        self.id_colaborador = colaborador
        self.id_area = area
        self.descripcion = descripcion
        self.id_proyecto = proyecto
        if fecha_creacion is not None:
            self.fecha_creacion = fecha_creacion
    
    def __repr__(self):
        return f'{self.colaborador} {self.proyecto} {self.area}\n'






class Categoria(db.Model):
    __tablename__ = 'categoria'
    id_categoria = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(50), default = None) # unique=True
    descripcion = db.Column(db.String(1000), default = None)
    
    def __init__(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion
    
    def __repr__(self):
        return f'{self.titulo}\n'






class SubProyecto(db.Model): #Proyecto relacion done
    __tablename__ = 'subproyecto'
    id_subproyecto = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(50), default = None) # unique=True
    descripcion = db.Column(db.String(1000), default = None)
    id_proyecto = db.Column(db.Integer, ForeignKey('proyecto.id_proyecto', ondelete='SET NULL', onupdate='CASCADE'))

    proyecto = db.relationship('Proyecto', lazy = True)
    atributos = db.relationship('AtributoGenerico', lazy=True)

    def __init__(self, proyecto, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion
        self.id_proyecto = proyecto

    def __repr__(self):
        return f'{self.titulo} {self.proyecto}\n'







class AtributoGenerico(db.Model):
    __tablename__ = 'atributogenerico'
    id_atributogenerico = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(50), default = None) # unique=True
    valor = db.Column(db.String(1000), default = None)
    id_subproyecto = db.Column(db.Integer, ForeignKey('subproyecto.id_subproyecto', ondelete='SET NULL', onupdate='CASCADE'))
    id_categoria = db.Column(db.Integer, ForeignKey('categoria.id_categoria', ondelete='SET NULL', onupdate='CASCADE'))
    
    categoria = db.relationship('Categoria', lazy = True)

    def __init__(self, titulo, valor, subproyecto, categoria):
        self.titulo = titulo
        self.valor = valor
        self.id_subproyecto = subproyecto
        self.id_categoria = categoria
    
    def __repr__(self):
        return f'{self.titulo} {self.valor}\n'