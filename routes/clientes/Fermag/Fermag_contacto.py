from flask import Blueprint,render_template,redirect,url_for, request
from utils.db import db

Fermag_contacto = Blueprint("Fermag_contacto",__name__)



class Servicios:
    def __init__(self,nombre, fondo):
        self.nombre = nombre
        self.fondo = fondo

        

    def __str__(self):
        return f'{self.nombre}, {self.fondo}'

@Fermag_contacto.route("/clientes/Fermag/contacto")    
def procesar_formulario():
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.form['nombre']
        email = request.form['email']
        mensaje = request.form['mensaje']

        # Hacer algo con los datos del formulario, por ejemplo, enviar un correo electrónico
        destinatario = "marcosuperfm@gmail.com"
        asunto = "xd"
        cuerpo = f"Nombre: {nombre}\nEmail: {email}\nMensaje: {mensaje}"
        # Código para enviar correo electrónico

        # Redirigir al usuario a una página de confirmación
        return render_template('/clientes/Fermag/confirmacion.html')
    else:
        return render_template('/clientes/Fermag/contacto.html')

    