from app import app
from utils.db import db
from models.models import *

from routes.lussary_config.settings import Home
from routes.lussary_config.Lussary_galeria import Lussary_galeria
from routes.clientes.VEME.VEME_home import VEME_home
from routes.clientes.Fermag.Fermag_home import Fermag_home
from routes.clientes.Fermag.Fermag_proyectos import Fermag_proyectos
from routes.clientes.Fermag.Fermag_contacto import Fermag_contacto
from routes.lussary_config.info_politica import Info_Politica

with app.app_context():
    db.create_all()

app.register_blueprint(Home)
app.register_blueprint(VEME_home)
app.register_blueprint(Fermag_home)
app.register_blueprint(Fermag_proyectos)
app.register_blueprint(Fermag_contacto)
app.register_blueprint(Lussary_galeria)
app.register_blueprint(Info_Politica)


if __name__ == '__main__':
    app.run(debug=True)
    