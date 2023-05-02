from flask import Blueprint,render_template,redirect,url_for
from utils.db import db

CDL_home = Blueprint("CDL_home",__name__)
CDL_servicios = Blueprint("CDL_servicios",__name__)


#Yeah
@CDL_home.route('/CDL')
def CDLHome():
    Servicios = [
        ('Traslados de', 'discapacidad', 'https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8bWFuZWphbmRvfGVufDB8fDB8fA%3D%3D&w=1000&q=80', '#CC0000'),
        ('Traslados de', 'ART', 'https://siempreauto.com/wp-content/uploads/sites/9/2022/02/serjan-midili-YWoiQV4XrfM-unsplash.jpg?w=4096', '#990000'),
        ('Traslados de', 'baja complicidad', 'https://caracol.com.co/resizer/Cdd4FCGOdI5y04aii2EbuY6eRrc=/1440x1440/filters:format(jpg):quality(70)/cloudfront-us-east-1.images.arcpublishing.com/prisaradioco/CGSL5V2PTZIFXPWNWVYGYFYV6Q.jpg', '#660000')
    ]
    return render_template('/clientes/CDL/cdl.html', servicios = Servicios)

@CDL_servicios.route('/CDL/servicios')
def CDLServicios():
    return render_template('/clientes/CDL/servicios.html')
