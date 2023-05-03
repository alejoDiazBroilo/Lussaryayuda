from flask import Blueprint,render_template,redirect,url_for
from utils.db import db

CDL_home = Blueprint("CDL_home",__name__)
CDL_servicios = Blueprint("CDL_servicios",__name__)


@CDL_home.route('/CDL')
def CDLHome():
    Servicios = [
        ('Traslados de', 'discapacidad', 'https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8bWFuZWphbmRvfGVufDB8fDB8fA%3D%3D&w=1000&q=80', '#CC0000'),
        ('Traslados de', 'ART', 'https://siempreauto.com/wp-content/uploads/sites/9/2022/02/serjan-midili-YWoiQV4XrfM-unsplash.jpg?w=4096', '#990000'),
        ('Traslados de', 'baja complicidad', 'https://caracol.com.co/resizer/Cdd4FCGOdI5y04aii2EbuY6eRrc=/1440x1440/filters:format(jpg):quality(70)/cloudfront-us-east-1.images.arcpublishing.com/prisaradioco/CGSL5V2PTZIFXPWNWVYGYFYV6Q.jpg', '#660000')
    ]
    return render_template('/clientes/CDL/cdl.html', servicios = Servicios)


servicios = {
    'art': {
        'bg': 'https://cdn.computerhoy.com/sites/navi.axelspringer.es/public/media/image/2021/07/conducir-2409011.jpg?tf=1200x',
        'nombre': 'Traslado de ART',
        'descripcion': 'Transporte de personas que necesitan trasladarse por motivos médicos, ya sea para realizar consultas, tratamientos o cirugías.'
    },
    'discapacidad': {
        'bg': 'https://arc-anglerfish-arc2-prod-infobae.s3.amazonaws.com/public/X7GBEM6QFRHVZFVSVMHCTJH2WQ.jpg',
        'nombre': 'Traslado por discapacidad',
        'descripcion': 'Este servicio está diseñado para atender a personas que tienen alguna discapacidad física o mental, como problemas de movilidad, sordera, ceguera o trastornos del espectro autista, entre otros.'
    },
    'adl': {
        'bg': 'https://img2.rtve.es/imagenes/delitos-odio-hacia-personas-discapacidad/1627897048689.jpg',
        'nombre': 'Traslados de Baja Complejidad',
        'descripcion': 'Este servicio está diseñado para personas que necesitan ayuda para realizar las Actividades de la Vida Diaria (ADL), como vestirse, bañarse, comer o tomar medicamentos.'
    }
}

@CDL_servicios.route('/CDL/<servicio_id>')
def getCDLServicio(servicio_id):
    servicio = servicios.get(servicio_id, {'nombre': 'Servicio no encontrado', 'descripcion': ''})
    if servicio_id != 'art' and servicio_id != 'discapacidad' and servicio_id != 'adl':
        return redirect(url_for('CDL_home.CDLHome'))

    return render_template('/clientes/CDL/servicios.html', servicio=servicio)
    

