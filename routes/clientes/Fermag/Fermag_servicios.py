from flask import Blueprint,render_template,redirect,url_for
from utils.db import db

Fermag_servicios = Blueprint("Fermag_servicios",__name__)



class Servicios:
    def __init__(self,nombre):
        self.nombre = nombre

        

    def __str__(self):
        return f'{self.nombre}'

@Fermag_servicios.route("/clientes/Fermag/servicios")    
def FermagServicios():
    infos = [ 
        Servicios('DOMOTICA'),
        Servicios('ENERGIAS RENOVABLES'),
        Servicios('UPS'),
        Servicios('INSTALACIONES ELECTRICAS'),
        Servicios('BMS'), Servicios('AUTOMOTIZACIONES ESPECIALES')             
        ]
    
    return render_template("clientes/Fermag/servicios.html", infos=infos)