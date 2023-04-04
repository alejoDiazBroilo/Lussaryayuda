from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'mysql+pymysql://root:9Rtcn2nInmjU8TVIFmg9@containers-us-west-47.railway.app:6674/railway'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False