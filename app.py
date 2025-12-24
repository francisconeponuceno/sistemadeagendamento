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
app.add_url_rule("/agendar/<int:Id_CardServico>", "agendar", UserController.agendar, methods=['POST', 'GET'])


# ROTAS DO CRUD PROFISSIONAL
app.add_url_rule('/CadProfissional', 'CadProfissional', UserController.CadProfissional, methods=['POST','GET'])
app.add_url_rule("/crudProfissional/<int:Id_Profissional>","crudProfissional",UserController.crudProfissional,methods=["POST", "GET"])
app.add_url_rule("/updateProfissional/<int:Id_Profissional>", "updateProfissional", UserController.updateProfissional, methods=['POST', 'GET'])
app.add_url_rule("/DeleteProfissional/<int:Id_Profissional>","DeleteProfissional",UserController.DeleteProfissional,methods=["POST", "GET"])


# ROTAS DO CRUD SERVIÇO
app.add_url_rule('/CadServico', 'cadServico', UserController.CadServico, methods=['POST', 'GET'])
app.add_url_rule('/crudServico/<int:Id_Servico>', 'crudServico', UserController.crudServico, methods=['POST', 'GET'])
app.add_url_rule('/updateServico/<int:Id_Servico>', 'updateServico', UserController.updateServico, methods=['POST', 'GET'])
app.add_url_rule('/DeleteServico/<int:Id_Servico>', 'DeleteServico', UserController.DeleteServico, methods=['POST', 'GET'])

if __name__ == '__main__':
    app.run(debug=True)
