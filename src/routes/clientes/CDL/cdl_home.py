from flask import Blueprint,render_template,redirect,url_for
from utils.db import db

CDL_home = Blueprint("CDL_home",__name__)

#Yeah
@CDL_home.route('/CDL')
def CDLHome():
    return render_template('/clientes/CDL/cdl.html')