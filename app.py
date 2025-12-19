from flask import Flask
import os
from config import Config
from controllers.user_controllers import UserController
from models.user import db, migrate


# INSTANCIANDO O FLASK
app = Flask(__name__, template_folder=os.path.join('views', 'templates' ))
app.config.from_object(Config)

# INICIALIZANDO O BANCO DE DADOS
db.init_app(app)
migrate.init_app(app, db)

# REGISTRANDO AS ROTAS
app.add_url_rule('/', 'index', UserController.index)
app.add_url_rule('/login','login', UserController.login, methods=['POST','GET'])
app.add_url_rule('/cadastro', 'cadastro', UserController.cadastro, methods=['POST','GET'])
app.add_url_rule('/cliente', 'cliente', UserController.cliete, methods=['POST', 'GET'])
app.add_url_rule('/admin', 'admin', UserController.admin, methods=['POST', 'GET'])
app.add_url_rule('/agendar', 'agendar', UserController.agendar, methods=['POST', 'GET'])


# ROTAS DA DO CRUD PROFISSIONAL
app.add_url_rule('/CadProfissional', 'CadProfissional', UserController.CadProfissional, methods=['POST','GET'])
app.add_url_rule("/DeleteProfissional/<int:Id_Profissional>","DeleteProfissional/<int:Id_Profissional>",UserController.DeleteProfissional,methods=["POST", "GET"],
)


if __name__ == '__main__':
    app.run(debug=True)
