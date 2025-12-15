from flask import Flask
import os
from config import Config
from controllers.user_controllers import UserController
from models.user import db, migrate


app = Flask(__name__, template_folder=os.path.join('views', 'templates' ))
app.config.from_object(Config)

# inicializa o banco de dados
db.init_app(app)
migrate.init_app(app, db)


app.add_url_rule('/', 'index', UserController.index)
app.add_url_rule('/login','login', UserController.login, methods=['POST','GET'])
app.add_url_rule('/cadastro', 'cadastro', UserController.cadastro, methods=['POST','GET'])
app.add_url_rule('/cliente', 'cliente', UserController.cliete, methods=['POST', 'GET'])
app.add_url_rule('/admin', 'admin', UserController.admin, methods=['POST', 'GET'])
app.add_url_rule('/agendar', 'agendar', UserController.agendar, methods=['POST', 'GET'])






if __name__ == '__main__':
    app.run(debug=True)