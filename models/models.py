from utils.db import db
from sqlalchemy import Column, Integer, String, Date, func, ForeignKey

class Persona(db.Model):
    __tablename__ = 'persona'
    id_persona = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(70), nullable = False)
    apellido = db.Column(db.String(70), nullable = False)
    descripcion = db.Column(db.String(150), default = None)
    fecha_creacion = db.Column(db.Date, default=func.now())

    contacto_relacion = db.relationship('Contacto', backref='persona', lazy=True, overlaps='persona_relacion')
    colaborador_relacion = db.relationship('Colaborador', backref='persona', lazy=True, overlaps='persona_relacion')

    def __init__(self,nombre, apellido, descripcion, fecha_creacion=None):
        self.nombre = nombre
        self.apellido = apellido
        self.descripcion = descripcion
        if fecha_creacion is not None:
            self.fecha_creacion = fecha_creacion

    def __repr__(self):
        return f'Nombre: {self.nombre}, Apellido: {self.apellido}\n'







class Medio(db.Model): #done
    __tablename__ = 'medio'
    id_medio = db.Column(db.Integer, primary_key=True)
    nombre_medio = db.Column(db.String(70), nullable = False)
    link_contacto = db.Column(db.String(200), nullable = False) #unique
    link_contacto_fin = db.Column(db.String(200), nullable = False) #unique
    fecha_creacion = db.Column(db.Date, default=func.now())

    contacto_relacion = db.relationship('Contacto', backref='medio', lazy=True, overlaps='contacto_relacion')

    def __init__(self, nombre_medio, link_contacto, link_contacto_fin, fecha_creacion = None):
        self.nombre_medio = nombre_medio
        self.link_contacto = link_contacto
        self.link_contacto_fin = link_contacto_fin
        if fecha_creacion is not None:
            self.fecha_creacion = fecha_creacion
    
    def __repr__(self):
        return f'link: {self.link_contacto}_{self.link_contacto_fin}\n'







class Contacto(db.Model): #done
    __tablename__ = 'contacto'
    id_contacto = db.Column(db.Integer, primary_key=True)
    id_medio = db.Column(db.Integer, ForeignKey('medio.id_medio', ondelete='SET NULL', onupdate='CASCADE'))
    id_persona = db.Column(db.Integer, ForeignKey('persona.id_persona', ondelete='SET NULL', onupdate='CASCADE')) #persona_relatio
    info_contacto = db.Column(db.String(200), nullable = False) 
    fecha_creacion = db.Column(db.Date, default=func.now())

    persona_relacion = db.relationship('Persona', backref='contacto', lazy=True, overlaps='persona_relacion')
    medio_relacion = db.relationship('Medio', backref='contacto', lazy=True, overlaps='medio_relacion')
    
    def __init__(self, medio, persona, info_contacto, fecha_creacion=None):
        self.id_medio = medio
        self.id_persona = persona
        self.info_contacto = info_contacto
        if fecha_creacion is not None:
            self.fecha_creacion = fecha_creacion
    
    def __repr__(self):
        return f'{self.info_contacto}\n'








class Colaborador(db.Model):
    __tablename__ = 'Colaborador'
    id_colaborador = db.Column(db.Integer, primary_key=True)
    id_persona = db.Column(db.Integer, ForeignKey('persona.id_persona', ondelete='SET NULL', onupdate='CASCADE')) #persona_relatio
    fecha_nacimiento = db.Column(db.Date)
    fecha_creacion = db.Column(db.Date, default=func.now())

    persona_relacion = db.relationship('Persona', backref='colaborador', lazy=True)
    decripcioncolaborador_relacion = db.relationship('DescripcionColaborador', backref='colaborador', lazy=True)
    rol_relacion = db.relationship('rol', backref='colaborador', lazy=True)

    def __init__(self, persona, fecha_nacimiento=None, fecha_creacion=None):
        self.id_persona = persona
        self.fecha_nacimiento = fecha_nacimiento
        if fecha_creacion is not None:
            self.fecha_creacion = fecha_creacion
        if fecha_nacimiento is not None:
            self.fecha_nacimiento = fecha_nacimiento
    
    def __repr__(self):
        return f'{self.fecha_nacimiento}\n'
    





class DescripcionColaborador(db.Model): #Colaborador relacion done
    __tablename__ = 'DescripcionColaborador'
    id_descripcioncolaborador = db.Column(db.Integer, primary_key=True)
    id_colaborador = db.Column(db.Integer, ForeignKey('Colaborador.id_colaborador', ondelete='SET NULL', onupdate='CASCADE'))
    titulo = db.Column(db.String(50), default = None)
    descripcion = db.Column(db.String(150), default = None)
    fecha_creacion = db.Column(db.Date, default=func.now())
    
    colaborador_relacion = db.relationship('Colaborador', backref='descripcioncolaborador', lazy=True)

    def __init__(self, colaborador, titulo, descripcion, fecha_creacion=None):
        self.id_colaborador = colaborador
        self.titulo = titulo
        self.descripcion = descripcion
        if fecha_creacion is not None:
            self.fecha_creacion = fecha_creacion
    
    def __repr__(self):
        return f'{self.colaborador} = {self.titulo}\n'





class Actividad(db.Model): #done
    __tablename__ = 'Actividad'
    id_actividad = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(50), default = None) #unique
    descripcion = db.Column(db.String(150), default = None)
    fecha_creacion = db.Column(db.Date, default=func.now())

    rol_relacion = db.relationship('Rol', backref='actividad', lazy=True)

    def __init__(self, titulo, descripcion, fecha_creacion=None):
        self.titulo = titulo
        self.descripcion = descripcion
        if fecha_creacion is not None:
            self.fecha_creacion = fecha_creacion
    
    def __repr__(self):
        return f'{self.titulo}\n'






class Rol(db.Model): #Colaborador relacion done
    __tablename__ = 'Rol'
    id_rol = db.Column(db.Integer, primary_key=True)
    id_actividad = db.Column(db.Integer, ForeignKey('Actividad.id_actividad', ondelete='SET NULL', onupdate='CASCADE'))
    id_colaborador = db.Column(db.Integer, ForeignKey('Colaborador.id_colaborador', ondelete='SET NULL', onupdate='CASCADE'))
    fecha_creacion = db.Column(db.Date, default=func.now())

    actividad_relacion = db.relationship('Actividad', backref='rol', lazy=True)
    colaborador_relacion = db.relationship('Colaborador', backref='rol', lazy=True)

    def __init__(self, colaborador, actividad,fecha_creacion=None):
        self.id_colaborador = colaborador
        self.id_actividad = actividad
        if fecha_creacion is not None:
            self.fecha_creacion = fecha_creacion
    
    def __repr__(self):
        return f'{self.colaborador} = {self.actividad}\n'








class Proyecto(db.Model): 
    __tablename__ = 'Proyecto'
    id_proyecto = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fecha_creacion = db.Column(db.Date, default=func.now(), nullable=False)
    titulo = db.Column(db.String(50), nullable=False, unique=True)
    descripcion = db.Column(db.String(250), nullable=True)

    cliente_relacion = db.relationship('Cliente')
    contribucion_relacion = db.relationship('Contribucion')
    subProyecto_relacion = db.relationship('SubProyecto')

    def __init__(self, titulo, descripcion=None, fecha_creacion=None):
        self.titulo = titulo
        self.descripcion = descripcion
        if fecha_creacion is not None:
            self.fecha_creacion = fecha_creacion
    
    def __repr__(self):
        return f'{self.titulo}\n'








class Cliente(db.Model): #Proyecto relacion done
    __tablename__ = 'Cliente'
    id_cliente = db.Column(db.Integer, primary_key=True)
    id_persona = db.Column(db.Integer, ForeignKey('Persona.id_persona', ondelete='SET NULL', onupdate='CASCADE')) #persona_relatio
    id_colaborador = db.Column(db.Integer, ForeignKey('Colaborador.id_colaborador', ondelete='SET NULL', onupdate='CASCADE'))
    id_proyecto = db.Column(db.Integer, ForeignKey('Proyecto.id_proyecto', ondelete='SET NULL', onupdate='CASCADE'))
    fecha_creacion = db.Column(db.Date, default=func.now())

    persona_relacion = db.relationship('Persona')
    proyecto_relacion = db.relationship('Proyecto')
    colaborador_relacion = db.relationship('Colaborador')

    def __init__(self, persona, colaborador, proyecto, fecha_creacion=None):
        self.id_persona = persona
        self.id_colaborador = colaborador
        self.id_proyecto = proyecto
        if fecha_creacion is not None:
            self.fecha_creacion = fecha_creacion
    
    def __repr__(self):
        return f'{self.persona}, {self.proyecto}\n'