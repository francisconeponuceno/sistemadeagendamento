from flask import Flask
import os
from config import Config
from controllers.user_controllers import UserController
from models.user import db


app = Flask(__name__, template_folder=os.path.join('views', 'templates' ))
app.config.from_object(Config)

# inicializa o banco de dados
db.init_app(app)

# Criar as tabelas
with app.app_context():
    db.create_all()



app.add_url_rule('/', 'index', UserController.index)


if __name__ == '__main__':
    app.run(debug=True)