from flask import Flask

app = Flask(__name__)
"""
drop database MoraSeLaCome; create database MoraSeLaCome; use MoraSeLaCome;
"""
app.config['SQLALCHEMY_DATABASE_URI']= 'mysql+pymysql://root:9Rtcn2nInmjU8TVIFmg9@containers-us-west-47.railway.app:6674/railway'
#app.config['SQLALCHEMY_DATABASE_URI']= "mysql+pymysql://bdi:pepe1234@localhost/MoraSeLaCome"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False