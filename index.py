"""
from app import app
from utils.db import db


with app.app_context():
    db.create_all()
"""
from flask import Flask
#from flask_sqlalchemy import SQLAlchemy

from routes.home import Home

app = Flask(__name__)
app.secret_key = '3594ea6944dfc5dcd8eaadf8dff0759e'

app.register_blueprint(Home)

if __name__=='__main__':
    app.run(debug=True)