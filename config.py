import os
import secrets
from dotenv import load_dotenv

#chave = secrets.token_hex()

load_dotenv()
class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', secrets.token_hex())
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', default='sqlite:///database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    