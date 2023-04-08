from utils.db import db
from sqlalchemy import Column, Integer, String, Date, func, ForeignKey
"""
class Persona(db.Model): #done
    __tablename__ = 'Persona'
    id_persona = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(70), nullable = False)
    apellido = db.Column(db.String(70), nullable = False)
    descripcion = db.Column(db.String(150), default = None)
    fecha_creacion = db.Column(db.Date, default=func.now())
    
    contacto_relacion = db.relationship('Contacto')
    cliente_relacion = db.relationship('Cliente')
    colaborador_relacion = db.relationship('Colaborador')
    
    def __init__(self,nombre, apellido, descripcion, fecha_creacion=None):
        self.nombre = nombre
        self.apellido = apellido
        self.descripcion = descripcion
        if fecha_creacion is not None:
            self.fecha_creacion = fecha_creacion
    def __repr__(self):
        return f'Nombre: {self.nombre}, Apellido: {self.apellido}\n'


class Medio(db.Model): #done
    __tablename__ = 'Medio'
    id_medio = db.Column(db.Integer, primary_key=True)
    nombre_medio = db.Column(db.String(70), nullable = False)
    link_contacto = db.Column(db.String(200), nullable = False) #unique
    link_contacto_fin = db.Column(db.String(200), nullable = False) #unique
    fecha_creacion = db.Column(db.Date, default=func.now())

    contacto_relacion = db.relationship('Contacto')

    def __init__(self, nombre_medio, link_contacto, link_contacto_fin, fecha_creacion = None):
        self.nombre_medio = nombre_medio
        self.link_contacto = link_contacto
        self.link_contacto_fin = link_contacto_fin
        if fecha_creacion is not None:
            self.fecha_creacion = fecha_creacion
    
    def __repr__(self):
        return f'link: {self.link_contacto}_{self.link_contacto_fin}\n'

class Contacto(db.Model): #done
    __tablename__ = 'Contacto'
    id_contacto = db.Column(db.Integer, primary_key=True)
    medio = db.Column(db.Integer, ForeignKey('Medio.id_medio', ondelete='SET NULL', onupdate='CASCADE'))
    persona = db.Column(db.Integer, ForeignKey('Persona.id_persona', ondelete='SET NULL', onupdate='CASCADE')) #persona_relatio
    info_contacto = db.Column(db.String(200), nullable = False) 
    fecha_creacion = db.Column(db.Date, default=func.now())
    
    medio_relacion = db.relationship('Medio')
    persona_relacion = db.relationship('Persona')

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
    id_colaborador = db.Column(db.Integer, primary_key=True)
    persona = db.Column(db.Integer, ForeignKey('Persona.id_persona', ondelete='SET NULL', onupdate='CASCADE')) #persona_relatio
    fecha_nacimiento = db.Column(db.Date)
    fecha_creacion = db.Column(db.Date, default=func.now())

    persona_relacion = db.relationship('Persona')
    descripcionColaborador_relacion = db.relationship('DescripcionColaborador')
    rol_relacion = db.relationship('Rol')
    contribucion_relacion = db.relationship('Contribucion')
    cliente_relacion = db.relationship('Cliente')

    def __init__(self, persona, fecha_nacimiento=None, fecha_creacion=None):
        self.persona = persona
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
    colaborador = db.Column(db.Integer, ForeignKey('Colaborador.id_colaborador', ondelete='SET NULL', onupdate='CASCADE'))
    titulo = db.Column(db.String(50), default = None)
    descripcion = db.Column(db.String(150), default = None)
    fecha_creacion = db.Column(db.Date, default=func.now())
    
    colaborador_relacion = db.relationship('Colaborador')

    def __init__(self, colaborador, titulo, descripcion, fecha_creacion=None):
        self.colaborador = colaborador
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

    rol_relacion = db.relationship('Rol')

    def __init__(self, titulo, descripcion, fecha_creacion=None):
        self.titulo = titulo
        self.descripcion = descripcion
        if fecha_creacion is not None:
            self.fecha_creacion = fecha_creacion
    
    def __repr__(self):
        return f'{self.titulo}\n'
"""
class Rol(db.Model): #Colaborador relacion done
    __tablename__ = 'Rol'
    id_rol = db.Column(db.Integer, primary_key=True)
    actividad = db.Column(db.Integer, ForeignKey('Actividad.id_actividad', ondelete='SET NULL', onupdate='CASCADE'))
    colaborador = db.Column(db.Integer, ForeignKey('Colaborador.id_colaborador', ondelete='SET NULL', onupdate='CASCADE'))
    fecha_creacion = db.Column(db.Date, default=func.now())

    actividad_relacion = db.relationship('Actividad')
    colaborador_relacion = db.relationship('Colaborador')

    def __init__(self, colaborador, actividad,fecha_creacion=None):
        self.colaborador = colaborador
        self.actividad = actividad
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
    persona = db.Column(db.Integer, ForeignKey('Persona.id_persona', ondelete='SET NULL', onupdate='CASCADE')) #persona_relatio
    colaborador = db.Column(db.Integer, ForeignKey('Colaborador.id_colaborador', ondelete='SET NULL', onupdate='CASCADE'))
    proyecto = db.Column(db.Integer, ForeignKey('Proyecto.id_proyecto', ondelete='SET NULL', onupdate='CASCADE'))
    fecha_creacion = db.Column(db.Date, default=func.now())

    persona_relacion = db.relationship('Persona')
    proyecto_relacion = db.relationship('Proyecto')
    colaborador_relacion = db.relationship('Colaborador')

    def __init__(self, persona, colaborador, proyecto, fecha_creacion=None):
        self.persona = persona
        self.colaborador = colaborador
        self.proyecto = proyecto
        if fecha_creacion is not None:
            self.fecha_creacion = fecha_creacion
    
    def __repr__(self):
        return f'{self.persona}, {self.proyecto}\n'

class Area(db.Model):
    __tablename__ = 'Area'
    id_area = db.Column(db.Integer, primary_key=True)
    fecha_creacion = db.Column(db.Date, default=func.now())
    titulo = db.Column(db.String(50), default = None) #unique=True
    descripcion = db.Column(db.String(250), default = None)
    puntaje = db.Column(db.Integer, default = None)

    contribucion_relacion = db.relationship('Contribucion')

    def __init__(self, titulo, descripcion, puntaje, fecha_creacion=None):
        self.titulo = titulo
        self.descripcion = descripcion
        self.puntaje = puntaje

        if fecha_creacion is not None:
            self.fecha_creacion = fecha_creacion
    
    def __repr__(self):
        return f'{self.titulo}, {self.puntaje}\n'

class Contribucion(db.Model): #Area relacion
    __tablename__ = 'Contribucion' 
    id_contribucion = db.Column(db.Integer, primary_key=True)
    fecha_creacion = db.Column(db.Date, default=func.now())
    descripcion = db.Column(db.String(250), default = None)
    colaborador = db.Column(db.Integer, ForeignKey('Colaborador.id_colaborador', ondelete='SET NULL', onupdate='CASCADE'))
    proyecto = db.Column(db.Integer, ForeignKey('Proyecto.id_proyecto', ondelete='SET NULL', onupdate='CASCADE'))
    area = db.Column(db.Integer, ForeignKey('Area.id_area', ondelete='SET NULL', onupdate='CASCADE'))
    
    colaborador_relacion = db.relationship('Colaborador', back_populates='colaborador_relation')
    area_relacion = db.relationship('Area', back_populates='area_relation')
    proyecto_relacion = db.relationship('Proyecto', back_populates='proyecto_relation')
    
    def __init__(self, colaborador, proyecto, area, descripcion, fecha_creacion=None):
        self.colaborador = colaborador
        self.area = area
        self.descripcion = descripcion
        self.proyecto = proyecto
        if fecha_creacion is not None:
            self.fecha_creacion = fecha_creacion
    
    def __repr__(self):
        return f'{self.colaborador} {self.proyecto} {self.area}\n'

class Categoria(db.Model):
    __tablename__ = 'Categoria'
    id_categoria = db.Column(db.Integer, primary_key=True)
    fecha_creacion = db.Column(db.Date, default=func.now())
    titulo = db.Column(db.String(50), default = None) # unique=True
    descripcion = db.Column(db.String(250), default = None)
    
    atributo_relacion = db.relationship('AtributoGenerico', back_populates='atributo_relacion')

    def __init__(self, titulo, descripcion, fecha_creacion=None):
        self.titulo = titulo
        self.descripcion = descripcion
        if fecha_creacion is not None:
            self.fecha_creacion = fecha_creacion
    
    def __repr__(self):
        return f'{self.titulo}\n'

class SubProyecto(db.Model): #Proyecto relacion done
    __tablename__ = 'SubProyecto'
    id_subproyecto = db.Column(db.Integer, primary_key=True)
    fecha_creacion = db.Column(db.Date, default=func.now())
    titulo = db.Column(db.String(50), default = None) # unique=True
    descripcion = db.Column(db.String(250), default = None)
    proyecto = db.Column(db.Integer, ForeignKey('Proyecto.id_proyecto', ondelete='SET NULL', onupdate='CASCADE'))

    proyecto_relacion = db.relationship('Proyecto', back_populates='proyecto_relation')

    def __init__(self, proyecto, titulo, descripcion, fecha_creacion=None):
        self.titulo = titulo
        self.descripcion = descripcion
        self.proyecto = proyecto
        if fecha_creacion is not None:
            self.fecha_creacion = fecha_creacion
    def __repr__(self):
        return f'{self.titulo} {self.proyecto}\n'

class AtributoGenerico(db.Model):
    __tablename__ = 'AtributoGenerico'
    id_atributogenerico = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(50), default = None) # unique=True
    valor = db.Column(db.String(250), default = None)
    subproyecto = db.Column(db.Integer, ForeignKey('SubProyecto.id_subproyecto', ondelete='SET NULL', onupdate='CASCADE'))
    categoria = db.Column(db.Integer, ForeignKey('Categoria.id_categoria', ondelete='SET NULL', onupdate='CASCADE'))
    
    categoria_relacion = db.relationship('Categoria', back_populates='categoria_relation')
    subproyecto_relacion = db.relationship('SubProyecto', back_populates='subproyecto_relation')


    fecha_creacion = db.Column(db.Date, default=func.now())

    def __init__(self, titulo, valor, subproyecto, categoria, fecha_creacion=None):
        self.titulo = titulo
        self.valor = valor
        self.subproyecto = subproyecto
        self.categoria = categoria
        if fecha_creacion is not None:    
            self.fecha_creacion = fecha_creacion
    
    def __repr__(self):
        return f'{self.titulo} {self.valor}\n'

