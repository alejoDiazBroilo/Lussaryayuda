from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'mysql+pymysql://root:i3eXbNRZa4GIGFN37K8s@containers-us-west-151.railway.app:5647/railway'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False