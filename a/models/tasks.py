from utils.db import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(70), unique=True)
    description = db.Column(db.String(100))
    
    def __init__(self,title,description):
        self.title = title
        self.description = description
    
    def __repr__(self):
        return f'Titulo: {self.title}, Descripcion: {self.description}\n'