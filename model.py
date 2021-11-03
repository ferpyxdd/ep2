from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuarios(db.Model):
    __tablename__ = 'persona'
    nro_cedula = db.Column(db.Integer, primary_key=True, nullable=False)
    nombres = db.Column(db.String(45), nullable=False)
    apellidos = db.Column(db.String(45), nullable=False)
    
    def __init__(self,usua_cedula,usua_nombres,usua_apellidos):
        self.usua_cedula = nro_cedula
        self.usua_nombres = nombres
        self.usua_apellidos= apellidos