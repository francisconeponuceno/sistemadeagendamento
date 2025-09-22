import os
import secrets

#chave = secrets.token_hex()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', secrets.token_hex())
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', default='sqlite:///database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    