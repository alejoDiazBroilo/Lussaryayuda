from flask import Flask
#from flask_sqlalchemy import SQLAlchemy

from routes.home import Home

app = Flask(__name__)
app.secret_key = '3594ea6944dfc5dcd8eaadf8dff0759e'

"""
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://bdi:pepe1234@localhost/CatolicaDb"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


SQLAlchemy(app)
"""
app.register_blueprint(Home)


