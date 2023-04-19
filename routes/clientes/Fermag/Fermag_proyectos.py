
from flask import Blueprint,render_template,redirect,url_for
from utils.db import db

Fermag_proyectos = Blueprint("Fermag_proyectos",__name__)





#NOMBRES DE GALERIA
class Proyectos:
    def __init__(self,nombre,descripcion, boton, img):
        self.nombre = nombre
        self.descripcion = descripcion
        self.boton = boton
        self.img = img
        

    def __str__(self):
        return f'{self.nombre}: {self.img} correspondiente al boton: {self.boton} en: {self.descripcion}'

class Descripcion:
    def __init__(self, nombre, descripcion1, descripcion2, img, proyectoDescripcion, cliente, descripcion3, ubicacion, mapa, fondo):
        self.nombre = nombre
        self.descripcion1 = descripcion1
        self.descripcion2 = descripcion2
        self.img = img
        self.proyectoDescripcion = proyectoDescripcion
        self.cliente = cliente
        self.descripcion3 = descripcion3
        self.ubicacion = ubicacion
        self.mapa = mapa
        self.fondo = fondo       


    def __str__(self):
        return f'{self.nombre}: {self.descripcion1} : {self.descripcion2}'


@Fermag_proyectos.route("/Fermag/proyectos")    
def FermagProyectos():
    nombres = [ 
        Proyectos('HIPERMERCADOS LIBERTAD', 'https://images.unsplash.com/photo-1415018255745-0ec3f7aee47b?dpr=1&auto=format&fit=crop&w=1500&h=938&q=80&cs=tinysrgb&crop=', 'Ver mas', 'Buenos Aires, Argentina'),
        Proyectos('TERMINAL DE OMNIBUS' ,'https://images.unsplash.com/photo-1440688807730-73e4e2169fb8?dpr=1&auto=format&fit=crop&w=1500&h=1001&q=80&cs=tinysrgb&crop=', 'Ver mas', 'Santiago del Estero, Argentina'),
        Proyectos('HOSPITAL PASTEUR', 'https://images.unsplash.com/photo-1415018255745-0ec3f7aee47b?dpr=1&auto=format&fit=crop&w=1500&h=938&q=80&cs=tinysrgb&crop=', 'Ver mas', 'Cordoba, Argentina')
        ]
    
    return render_template("clientes/Fermag/proyectos.html", nombres=nombres)


@Fermag_proyectos.route("/Fermag/proyectos/x")
def FermagProyectoInd():
    descripciones = [
        Descripcion('Titulo del proyecto','Aca va una descripcion breve','Este proyecto se trata de bla bla bla', '/static/src/clientes/Fermag/imgrepre.jpg',
        'Aca va el nombre completo del proyecto', 'Hola, soy el cliente! (nombre cliente/empresa)', 'Aca iria una larga descripcion del proyecto', 'Este proyecto fue hecho en Timbuctu',
        'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d30560.850821222513!2d-3.0079794!3d16.77138355!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0xe17ce977cbc8733%3A0x546f01bc8958b7c6!2zVG9tYnVjdMO6LCBNYWzDrQ!5e0!3m2!1ses!2sar!4v1680099088733!5m2!1ses!2sar',
        'https://hiperlibertad.vteximg.com.br/arquivos/ids/155421/banners-04.jpg?v=637231814047630000')
    ]

    return render_template("clientes/Fermag/proyectoss.html", descripciones=descripciones)
