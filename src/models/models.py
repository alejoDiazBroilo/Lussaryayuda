
from utils.db import db
from sqlalchemy import Column, Integer, String, Date, func, ForeignKey

class Persona(db.Model): # se pueden hacer las querys
    __tablename__ = 'persona'
    id_persona = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(70), nullable = False)
    apellido = db.Column(db.String(70), nullable = False)
    descripcion = db.Column(db.String(1000), default = None)
    fecha_creacion = db.Column(db.Date, default=func.now())

    agenda = db.relationship('Contacto', back_populates='persona_contacto')
    colaborador_datos = db.relationship('Colaborador', backref='persona', uselist=False, lazy=True)
    cliente_datos = db.relationship('Cliente', backref='persona', uselist=False, lazy=True)

    def __init__(self,nombre, apellido, descripcion, fecha_creacion=None):
        self.nombre = nombre
        self.apellido = apellido
        self.descripcion = descripcion
        if fecha_creacion is not None:
            self.fecha_creacion = fecha_creacion

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
    fecha_creacion = db.Column(db.Date, default=func.now())

    dato_contacto = db.relationship('Contacto', back_populates = 'medio_contacto')

    def __init__(self, nombre_medio, link_contacto, link_contacto_fin, fecha_creacion = None):
        self.nombre_medio = nombre_medio
        self.link_contacto = link_contacto
        self.link_contacto_fin = link_contacto_fin
        if fecha_creacion is not None:
            self.fecha_creacion = fecha_creacion
    
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
    fecha_creacion = db.Column(db.Date, default=func.now())

    persona_contacto = db.relationship('Persona', back_populates='agenda')
    medio_contacto = db.relationship('Medio', back_populates='dato_contacto')

    
    def __init__(self, medio, persona, info_contacto, fecha_creacion=None):
        self.id_medio = medio
        self.id_persona = persona
        self.info_contacto = info_contacto
        if fecha_creacion is not None:
            self.fecha_creacion = fecha_creacion
    
    def __repr__(self):
        return f'{self.info_contacto}\n'

"""
contactos = Contacto.query.all()
personas = contactos[i].<persona_agenda> usando el backref en las clases que tienen las relationships
"""






class Colaborador(db.Model):# se pueden hacer las querys
    __tablename__ = 'colaborador'
    id_colaborador = db.Column(db.Integer, primary_key=True)
    id_persona = db.Column(db.Integer, ForeignKey('persona.id_persona', ondelete='SET NULL', onupdate='CASCADE')) #persona_relatio
    fecha_nacimiento = db.Column(db.Date)
    fecha_creacion = db.Column(db.Date, default=func.now())

    descripciones = db.relationship('DescripcionColaborador', backref='colaborador', lazy=True)
    clientes = db.relationship('Cliente', backref='colaborador', lazy=True)
    contribuciones = db.relationship('Contribucion', backref='colaborador', lazy=True)
    roles = db.relationship('Rol', backref='colaborador', lazy=True)

    def __init__(self, persona, fecha_nacimiento=None, fecha_creacion=None):
        self.id_persona = persona
        self.fecha_nacimiento = fecha_nacimiento
        if fecha_creacion is not None:
            self.fecha_creacion = fecha_creacion
        if fecha_nacimiento is not None:
            self.fecha_nacimiento = fecha_nacimiento
    
    def __repr__(self):
        return f'{self.fecha_nacimiento}\n'
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
    fecha_creacion = db.Column(db.Date, default=func.now())
    
    def __init__(self, colaborador, titulo, descripcion, fecha_creacion=None):
        self.id_colaborador = colaborador
        self.titulo = titulo
        self.descripcion = descripcion
        if fecha_creacion is not None:
            self.fecha_creacion = fecha_creacion
    
    def __repr__(self):
        return f'{self.colaborador} = {self.titulo}\n'





class Actividad(db.Model):# se pueden hacer las querys
    __tablename__ = 'actividad'
    id_actividad = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(50), default = None) #unique
    descripcion = db.Column(db.String(1000), default = None)
    fecha_creacion = db.Column(db.Date, default=func.now())

    actividad_rol = db.relationship('Rol', backref='actividad', lazy=True)
    actividad_contribucion = db.relationship('Contribucion', backref='actividad', lazy=True)

    def __init__(self, titulo, descripcion, fecha_creacion=None):
        self.titulo = titulo
        self.descripcion = descripcion
        if fecha_creacion is not None:
            self.fecha_creacion = fecha_creacion
    
    def __repr__(self):
        return f'{self.titulo}\n'






class Rol(db.Model):# se pueden hacer las querys
    __tablename__ = 'rol'
    id_rol = db.Column(db.Integer, primary_key=True)
    id_actividad = db.Column(db.Integer, ForeignKey('actividad.id_actividad', ondelete='SET NULL', onupdate='CASCADE'))
    id_colaborador = db.Column(db.Integer, ForeignKey('colaborador.id_colaborador', ondelete='SET NULL', onupdate='CASCADE'))
    fecha_creacion = db.Column(db.Date, default=func.now())

    def __init__(self, colaborador, actividad,fecha_creacion=None):
        self.id_colaborador = colaborador
        self.id_actividad = actividad
        if fecha_creacion is not None:
            self.fecha_creacion = fecha_creacion
    
    def __repr__(self):
        return f'{self.colaborador} = {self.actividad}\n'







class Proyecto(db.Model): 
    __tablename__ = 'proyecto'
    id_proyecto = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fecha_creacion = db.Column(db.Date, default=func.now(), nullable=False)
    titulo = db.Column(db.String(50), nullable=False, unique=True)
    descripcion = db.Column(db.String(1000), nullable=True)

    clientes = db.relationship('Cliente', backref='proyecto', lazy=True)
    contribuciones = db.relationship('Contribucion', backref='proyecto', lazy=True)
    subproyectos = db.relationship('SubProyecto', backref='proyecto', lazy=True)
    
    def __init__(self, titulo, descripcion=None, fecha_creacion=None):
        self.titulo = titulo
        self.descripcion = descripcion
        if fecha_creacion is not None:
            self.fecha_creacion = fecha_creacion
    
    def __repr__(self):
        return f'{self.titulo}\n'







class Cliente(db.Model): #Proyecto relacion done
    __tablename__ = 'cliente'
    id_cliente = db.Column(db.Integer, primary_key=True)
    id_persona = db.Column(db.Integer, ForeignKey('persona.id_persona', ondelete='SET NULL', onupdate='CASCADE')) #persona_relatio
    id_colaborador = db.Column(db.Integer, ForeignKey('colaborador.id_colaborador', ondelete='SET NULL', onupdate='CASCADE'))
    id_proyecto = db.Column(db.Integer, ForeignKey('proyecto.id_proyecto', ondelete='SET NULL', onupdate='CASCADE'))
    fecha_creacion = db.Column(db.Date, default=func.now())

    #persona_relacion = db.relationship('Persona')
    #proyecto_relacion = db.relationship('Proyecto')
    #colaborador_relacion = db.relationship('Colaborador')

    def __init__(self, persona, colaborador, proyecto, fecha_creacion=None):
        self.id_persona = persona
        self.id_colaborador = colaborador
        self.id_proyecto = proyecto
        if fecha_creacion is not None:
            self.fecha_creacion = fecha_creacion
    
    def __repr__(self):
        return f'{self.persona}, {self.proyecto}\n'



"""
commit nuevo xd
"""



class Contribucion(db.Model): #Area relacion
    __tablename__ = 'contribucion' 
    id_contribucion = db.Column(db.Integer, primary_key=True)
    puntaje = db.Column(db.Integer)
    fecha_creacion = db.Column(db.Date, default=func.now())
    descripcion = db.Column(db.String(1000), default = None)
    id_colaborador = db.Column(db.Integer, ForeignKey('colaborador.id_colaborador', ondelete='SET NULL', onupdate='CASCADE'))
    id_proyecto = db.Column(db.Integer, ForeignKey('proyecto.id_proyecto', ondelete='SET NULL', onupdate='CASCADE'))
    id_actividad = db.Column(db.Integer, ForeignKey('actividad.id_actividad', ondelete='SET NULL', onupdate='CASCADE'))
        
    def __init__(self, colaborador, proyecto, actividad, descripcion, puntaje, fecha_creacion=None):
        self.id_colaborador = colaborador
        self.id_actividad = actividad
        self.puntaje = puntaje
        self.descripcion = descripcion
        self.id_proyecto = proyecto
        if fecha_creacion is not None:
            self.fecha_creacion = fecha_creacion
    
    def __repr__(self):
        return f'{self.colaborador} {self.proyecto} {self.area}\n'






class Categoria(db.Model):
    __tablename__ = 'categoria'
    id_categoria = db.Column(db.Integer, primary_key=True)
    fecha_creacion = db.Column(db.Date, default=func.now())
    titulo = db.Column(db.String(50), default = None) # unique=True
    descripcion = db.Column(db.String(1000), default = None)
    
    atributos = db.relationship('AtributoGenerico', backref='categoria')

    def __init__(self, titulo, descripcion, fecha_creacion=None):
        self.titulo = titulo
        self.descripcion = descripcion
        if fecha_creacion is not None:
            self.fecha_creacion = fecha_creacion
    
    def __repr__(self):
        return f'{self.titulo}\n'






class SubProyecto(db.Model): #Proyecto relacion done
    __tablename__ = 'subproyecto'
    id_subproyecto = db.Column(db.Integer, primary_key=True)
    fecha_creacion = db.Column(db.Date, default=func.now())
    titulo = db.Column(db.String(50), default = None) # unique=True
    descripcion = db.Column(db.String(1000), default = None)
    id_proyecto = db.Column(db.Integer, ForeignKey('proyecto.id_proyecto', ondelete='SET NULL', onupdate='CASCADE'))

    atributos = db.relationship('AtributoGenerico', backref='subproyecto')

    def __init__(self, proyecto, titulo, descripcion, fecha_creacion=None):
        self.titulo = titulo
        self.descripcion = descripcion
        self.id_proyecto = proyecto
        if fecha_creacion is not None:
            self.fecha_creacion = fecha_creacion
    def __repr__(self):
        return f'{self.titulo} {self.proyecto}\n'








class AtributoGenerico(db.Model):
    __tablename__ = 'atributogenerico'
    id_atributogenerico = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(50), default = None) # unique=True
    valor = db.Column(db.String(1000), default = None)
    id_subproyecto = db.Column(db.Integer, ForeignKey('subproyecto.id_subproyecto', ondelete='SET NULL', onupdate='CASCADE'))
    id_categoria = db.Column(db.Integer, ForeignKey('categoria.id_categoria', ondelete='SET NULL', onupdate='CASCADE'))
    
    fecha_creacion = db.Column(db.Date, default=func.now())

    def __init__(self, titulo, valor, subproyecto, categoria, fecha_creacion=None):
        self.titulo = titulo
        self.valor = valor
        self.id_subproyecto = subproyecto
        self.id_categoria = categoria
        if fecha_creacion is not None:    
            self.fecha_creacion = fecha_creacion
    
    def __repr__(self):
        return f'{self.titulo} {self.valor}\n'