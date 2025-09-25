from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime, date

db = SQLAlchemy()
migrate = Migrate()

class User(db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    senha = db.Column(db.String(100), nullable=False, unique=True)
    tipo = db.Column(db.String(20), nullable=False)
    data = db.Column(db.Date, default=datetime.now())
