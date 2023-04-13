from flask import Flask

app = Flask(__name__)
<<<<<<< HEAD
"""app.config['SQLALCHEMY_DATABASE_URI']= 'mysql+pymysql://root:i3eXbNRZa4GIGFN37K8s@containers-us-west-151.railway.app:5647/railway'"""
app.config['SQLALCHEMY_DATABASE_URI']= 'mysql://facha:46131849@localhost/Flask_utils'
=======
"""
drop database MoraSeLaCome; create database MoraSeLaCome; use MoraSeLaCome;
"""
#app.config['SQLALCHEMY_DATABASE_URI']= 'mysql+pymysql://root:9Rtcn2nInmjU8TVIFmg9@containers-us-west-47.railway.app:6674/railway'
app.config['SQLALCHEMY_DATABASE_URI']= "mysql+pymysql://bdi:pepe1234@localhost/MoraSeLaCome"
>>>>>>> d997e2c7f38af0cb97262b3f451b9c4ae885a1ec
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False