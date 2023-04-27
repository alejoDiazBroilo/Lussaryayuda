from flask import Blueprint,render_template,redirect,url_for
from utils.db import db

Lussary_contact = Blueprint("Lussary_contact",__name__)

@Lussary_contact.route('/contacto')
def LussaryContact():
    return render_template('lussary_config/contacto_lussary.html',navbar = True)