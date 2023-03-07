from app import app
from utils.db import db
from models.tasks import Task

from routes.lussary_config.settings import Home
from routes.clientes.VEME.VEME_home import VEME_home


with app.app_context():
    db.create_all()
    

app.register_blueprint(Home)
app.register_blueprint(VEME_home)

if __name__ == '__main__':
    app.run(debug=True)




