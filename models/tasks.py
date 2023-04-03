from utils.db import db
from sqlalchemy import Column, Integer, String, Date, func, ForeignKey

class Persona(db.Model):
    __tablename__ = 'Persona'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(70), nullable = False)
    apellido = db.Column(db.String(70), nullable = False)
    descripcion = db.Column(db.String(150), default = None)
    fecha_creacion = db.Column(db.Date, default=func.now())

    def __init__(self,nombre, apellido, descripcion, fecha_creacion=None):
        self.nombre = nombre
        self.apellido = apellido
        self.descripcion = descripcion
        if fecha_creacion is not None:
            self.fecha_creacion = fecha_creacion
    
    def __repr__(self):
        return f'Nombre: {self.nombre}, Apellido: {self.apellido}\n'


class Medio(db.Model):
    __tablename__ = 'Medio'
    id = db.Column(db.Integer, primary_key=True)
    nombre_medio = db.Column(db.String(70), nullable = False)
    link_contacto = db.Column(db.String(200), nullable = False)
    link_contacto_fin = db.Column(db.String(200), nullable = False)
    fecha_creacion = db.Column(db.Date, default=func.now())

    def __init__(self, nombre_medio, link_contacto, link_contacto_fin, fecha_creacion = None):
        self.nombre_medio = nombre_medio
        self.link_contacto = link_contacto
        self.link_contacto_fin = link_contacto_fin
        if fecha_creacion is not None:
            self.fecha_creacion = fecha_creacion
    
    def __repr__(self):
        return f'link: {self.link_contacto}_{self.link_contacto_fin}\n'

class Contacto(db.Model):
    __tablename__ = 'Contacto'
    id = db.Column(db.Integer, primary_key=True)
    medio = db.Column(db.Integer, ForeignKey('Medio.id', ondelete='SET NULL', onupdate='CASCADE'))
    persona = db.Column(db.Integer, ForeignKey('Persona.id', ondelete='SET NULL', onupdate='CASCADE'))
    info_contacto = db.Column(db.String(200), nullable = False)
    fecha_creacion = db.Column(db.Date, default=func.now())

    def __init__(self, medio, persona, info_contacto, fecha_creacion=None):
        self.medio = medio
        self.persona = persona
        self.info_contacto = info_contacto
        if fecha_creacion is not None:
            self.fecha_creacion = fecha_creacion
    
    def __repr__(self):
        return f'{self.info_contacto}\n'

class Colaborador(db.Model):
    __tablename__ = 'Colaborador'
    id = db.Column(db.Integer, primary_key=True)
    persona = db.Column(db.Integer, ForeignKey('Persona.id', ondelete='SET NULL', onupdate='CASCADE'))
    fecha_nacimiento = db.Column(db.Date)
    fecha_creacion = db.Column(db.Date, default=func.now())

    def __init__(self, persona, fecha_nacimiento, fecha_creacion=None):
        self.persona = persona
        self.fecha_nacimiento = fecha_nacimiento
        if fecha_creacion is not None:
            self.fecha_creacion = fecha_creacion
    
    def __repr__(self):
        return f'{self.fecha_nacimiento}\n'

class DescripcionColaborador(db.Model):
    __tablename__ = 'DescripcionColaborador'
    id = db.Column(db.Integer, primary_key=True)
    colaborador = db.Column(db.Integer, ForeignKey('Colaborador.id', ondelete='SET NULL', onupdate='CASCADE'))
    titulo = db.Column(db.String(50), default = None)
    descripcion = db.Column(db.String(150), default = None)
    fecha_creacion = db.Column(db.Date, default=func.now())

    def __init__(self, persona, titulo, descripcion, fecha_creacion=None):
        self.persona = persona
        self.titulo = titulo
        self.descripcion = descripcion
        if fecha_creacion is not None:
            self.fecha_creacion = fecha_creacion
    
    def __repr__(self):
        return f'{self.colaborador} = {self.titulo}\n'

class Actividad(db.Model):
    __tablename__ = 'Actividad'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(50), default = None)
    descripcion = db.Column(db.String(150), default = None)
    fecha_creacion = db.Column(db.Date, default=func.now())

    def __init__(self, titulo, descripcion, fecha_creacion=None):
        self.titulo = titulo
        self.descripcion = descripcion
        if fecha_creacion is not None:
            self.fecha_creacion = fecha_creacion
    
    def __repr__(self):
        return f'{self.titulo}\n'