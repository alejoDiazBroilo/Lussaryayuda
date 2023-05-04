from flask import Blueprint,render_template,redirect,url_for
from utils.db import db

Lussary_galeria = Blueprint("Lussary_galeria",__name__)

@Lussary_galeria.route('/galeria')
def LussaryGaleria():
    Galeria = [
        ('src/Lussary/LogoFermag.jpeg', 'FERMAG S.A.', 'src/Lussary/FermagPreview.png', 'Fermag'),
        ('src/Lussary/LogoVeme.jpeg', 'VEME', 'src/Lussary/VemePreview.png', 'VEME'),
        ('/src/Lussary/logoCDL.png', 'GRUPO CDL', 'src/Lussary/CDL_Preview.png', 'CDL')
    ]
    return render_template('lussary_config/galeria.html', galeria = Galeria,navbar = True)