
from app import app
from utils.db import db

"""
with app.app_context():
    db.create_all()
"""
from flask import Flask
#from flask_sqlalchemy import SQLAlchemy

from routes.lussary_config.settings import Home

if __name__=='__main__':
    app.run(debug=True)