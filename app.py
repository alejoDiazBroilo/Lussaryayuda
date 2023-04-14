from flask import Flask

app = Flask(__name__)
"""
CREAR USUARIO CON - NOMBRE:bdi - y - CONTRASEÑA: pepe1234 - y despues escribir lo de abajo en mysql ->
drop database LussaryTest; create database LussaryTest; use LussaryTest;
"""
#app.config['SQLALCHEMY_DATABASE_URI']= 'mysql+pymysql://root:9Rtcn2nInmjU8TVIFmg9@containers-us-west-47.railway.app:6674/railway'
app.config['SQLALCHEMY_DATABASE_URI']= "mysql+pymysql://bdi:pepe1234@localhost/LussaryTest"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False