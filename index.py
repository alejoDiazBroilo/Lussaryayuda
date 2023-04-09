from app import app
from utils.db import db
from models.tasks import *

from routes.lussary_config.settings import Home
from routes.clientes.VEME.VEME_home import VEME_home
from routes.clientes.Fermag.Fermag_home import Fermag_home
from routes.clientes.Fermag.Fermag_proyectos import Fermag_proyectos
from routes.clientes.Fermag.Fermag_contacto import Fermag_contacto

app.register_blueprint(Home)
app.register_blueprint(VEME_home)
app.register_blueprint(Fermag_home)
app.register_blueprint(Fermag_proyectos)
app.register_blueprint(Fermag_contacto)


if __name__ == '__main__':
    app.run(debug=True)
    