from flask import Blueprint,render_template,redirect,url_for
from utils.db import db

Info_Politica = Blueprint("Info_Politica",__name__)

@Info_Politica.route('/informacion-legal')
def informacion_legal():
    titulo = 'Informacion legal de Team Lussary'
    contenido = [
        ['Limitación de Responsabilidad', 'No nos hacemos responsables de cualquier daño o pérdida que resulte del uso de este sitio web, incluyendo cualquier virus informático o daño causado a tu equipo.'],
        ['Enlaces a Terceros', 'Este sitio web puede contener enlaces a sitios web de terceros. No somos responsables por el contenido o las prácticas de privacidad de estos sitios.'],
        ['Modificaciones', 'Nos reservamos el derecho de modificar o actualizar estos términos y condiciones de uso en cualquier momento sin previo aviso.'],
        ['Política de Privacidad', 'Por favor revisa nuestra Política de Privacidad para entender cómo manejamos y protegemos la información personal que recopilamos de los usuarios de nuestro sitio web.'],
        ['Contacto', 'Si tienes preguntas o comentarios sobre nuestras Condiciones de Uso, contáctanos a través del formulario de contacto en nuestro sitio web.'] 
    ]
    return render_template('lussary_config/info-politica.html', contenido=contenido, titulo=titulo, navbar = True)

@Info_Politica.route('/politica-de-privacidad')
def politica_de_privacidad():
    titulo = 'Politica de privacidad de Team Lussary'
    contenido = [
        ['Política de Privacidad', 'En este sitio web, nos tomamos la privacidad de nuestros usuarios muy en serio. Esta Política de Privacidad describe cómo manejamos y protegemos la información personal que recopilamos de los usuarios de nuestro sitio.'],
        ['Información Personal Recopilada', 'Podemos recopilar información personal de los usuarios, incluyendo su nombre, dirección de correo electrónico, número de teléfono y otra información de contacto. También podemos recopilar información sobre la actividad del usuario en nuestro sitio web.'],
        ['Cambios', 'Nos reservamos el derecho de modificar o actualizar esta Política de Privacidad en cualquier momento sin previo aviso. Se alentará a los usuarios a revisar esta Política de Privacidad periódicamente para estar al tanto de los cambios.'],
        ['Contacto', 'Si tienes preguntas o comentarios sobre nuestras Condiciones de Uso, contáctanos a través del formulario de contacto en nuestro sitio web.'] 
    ]
    return render_template('lussary_config/info-politica.html', contenido=contenido, titulo=titulo, navbar = True)