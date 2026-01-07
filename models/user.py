from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import date, datetime

hora = datetime.now()
hora = hora.strftime('%I:%M:%S')

db = SQLAlchemy()
migrate = Migrate()

class User(db.Model):
    __tablename__ = "administrador"

    Id_Admin = db.Column(db.Integer, primary_key=True)
    No_Admin = db.Column(db.String(100), nullable=False)
    Nr_Telefone = db.Column(db.String(20), nullable=False)
    No_Email = db.Column(db.String(100), nullable=False, unique=True)
    No_Senha = db.Column(db.String(100), unique=True)
    Tp_Entrada = db.Column(db.String(1), nullable=False, default='A')
    Fl_Situacao = db.Column(db.String(1), nullable=False, default='S')
    Dt_Cadastro = db.Column(db.Date, default=date.today)
    Hr_Cadastro = db.Column(db.DateTime, default=datetime.now)
    No_Usualt = db.Column(db.String(50))
    Dt_Altera = db.Column(db.Date, default=date.today)
    Hr_Altera = db.Column(db.DateTime, default=datetime.now)
    No_Usudel = db.Column(db.String(50))
    Dt_Delete = db.Column(db.Date, default=date.today)
    Hr_Delete = db.Column(db.DateTime, default=datetime.now)
    Fl_Delete = db.Column(db.String(1), default="N")


# ------------------
# TABLELA CLIENTE
# ------------------
class Cliente(db.Model):
    __tablename__ = "clientes"

    Id_Cliente = db.Column(db.Integer, primary_key=True)
    No_Cliente = db.Column(db.String(50), nullable=False)
    Nr_Telefone = db.Column(db.String(20), nullable=False)
    No_Email = db.Column(db.String(50), nullable=False)
    No_Senha = db.Column(db.String(30), unique=True)
    Tp_Entrada = db.Column(db.String(1), nullable=False, default='C')
    Fl_Situacao = db.Column(db.String(1), nullable=False, default='S')
    Dt_Cadastro = db.Column(db.Date, default=date.today)
    Hr_Cadastro = db.Column(db.DateTime, default=datetime.now)
    No_Usualt = db.Column(db.String(50))
    Dt_Altera = db.Column(db.Date, default=date.today)
    Hr_Altera = db.Column(db.DateTime, default=datetime.now)
    No_Usudel = db.Column(db.String(50))
    Dt_Delete = db.Column(db.Date, default=date.today)
    Hr_Delete = db.Column(db.DateTime, default=datetime.now)
    Fl_Delete = db.Column(db.String(1), default='N')


# --------------------
# TABELA PROFISSIONAIS
# --------------------
class Profissional(db.Model):
    __tablename__ = 'profissionais'

    Id_Profissional = db.Column(db.Integer, primary_key=True)
    No_Profissional = db.Column(db.String(50), nullable=False)
    Nr_Telefone = db.Column(db.String(20), nullable=False)
    Hr_Atendimento = db.Column(db.String(30), nullable=False)
    No_Especialidade = db.Column(db.String(50))
    No_Senha = db.Column(db.String(50), unique=True)
    Tp_Entrada = db.Column(db.String(1), nullable=False, default='P')
    Fl_Situacao = db.Column(db.String(1), nullable=False, default='S')
    Dt_Cadastro = db.Column(db.Date, default=date.today)
    Hr_Cadastro = db.Column(db.DateTime, default=datetime.now)
    No_Usualt = db.Column(db.String(50))
    Dt_Altera = db.Column(db.Date, default=date.today)
    Hr_Altera = db.Column(db.DateTime, default=datetime.now)
    No_Usudel = db.Column(db.String(50))
    Dt_Delete = db.Column(db.Date, default=date.today)
    Hr_Delete = db.Column(db.DateTime, default=datetime.now)
    Fl_Delete = db.Column(db.String(1), default="N")


# --------------------
# TABELA SERVIÇO
# --------------------

class Servico(db.Model):
    __tablename__ = 'servicos'

    Id_Servico = db.Column(db.Integer, primary_key=True)
    No_Servico = db.Column(db.String(100), nullable=False)
    Pr_Servico = db.Column(db.Float, nullable=False)
    Tp_Estimado = db.Column(db.String(15))
    Dc_Descricao1 = db.Column(db.String(30))
    Dc_Descricao2 = db.Column(db.String(30))
    Dc_Descricao3 = db.Column(db.String(30))
    Dc_Descricao4 = db.Column(db.String(30))
    Fl_Situacao = db.Column(db.String(1), nullable=False, default='S')
    Dt_Cadastro = db.Column(db.Date, default=date.today)
    Hr_cadastro = db.Column(db.DateTime, default=datetime.now)
    No_Usualt = db.Column(db.String(50))
    Dt_Altera = db.Column(db.Date, default=date.today)
    Hr_Altera = db.Column(db.DateTime, default=datetime.now)
    No_Usudel = db.Column(db.String(50))
    Dt_Delete = db.Column(db.Date, default=date.today)
    Hr_Delete = db.Column(db.DateTime, default=datetime.now)
    Fl_Delete = db.Column(db.String(1), default="N")


# --------------------
# TABELA AGENDAMENTOS
# --------------------

class Agendamento(db.Model):
    __tablename__ = 'agendamentos'

    Id_Agendamento = db.Column(db.Integer, primary_key=True)
    No_Cliente = db.Column(db.String(50),nullable=False)
    No_Profissional = db.Column(db.String(50),nullable=False)
    No_Servico = db.Column(db.String(50), nullable=False)
    Dt_Agendamento = db.Column(db.Date, nullable=False)
    Hr_Agendamento = db.Column(db.Time, nullable=False)
    Status_agendamento = db.Column(db.String(20), default='pendente')
    Fl_Situacao = db.Column(db.String(1), nullable=False, default="S")
    Dt_Cadastro = db.Column(db.Date, default=date.today)
    Hr_cadastro = db.Column(db.DateTime, default=datetime.now)
    No_Usualt = db.Column(db.String(50))
    Dt_Altera = db.Column(db.Date, default=date.today)
    Hr_Altera = db.Column(db.DateTime, default=datetime.now)
    No_Usudel = db.Column(db.String(50))
    Dt_Delete = db.Column(db.Date, default=date.today)
    Hr_Delete = db.Column(db.DateTime, default=datetime.now)
    Fl_Delete = db.Column(db.String(1), default="N")


# TABELA DADOS ESTABELECIMENTO
#-----------------------------

class Estabelecimento(db.Model):
    __tablename__ = 'estabelecimento'

    Id_endereco = db.Column(db.Integer, primary_key=True)
    No_Estabelecimento = db.Column(db.String(50))
    Nr_telefone = db.Column(db.String(11))
    No_Rua = db.Column(db.String(50))
    Nr_Numero = db.Column(db.String(40))
    No_Bairro = db.Column(db.String(40))
    No_Cidade = db.Column(db.String(50))
    Uf_Estado = db.Column(db.String(20))
    No_Email = db.Column(db.String(50))
    No_HorarioSegSex = db.Column(db.String(40))
    No_HorarioSab = db.Column(db.String(40))
    No_HorarioDom = db.Column(db.String(40))
    No_Instagran = db.Column(db.String(80))
    No_Twiter = db.Column(db.String(80))
    No_Linkedin = db.Column(db.String(80))
    No_Facebook = db.Column(db.String(80))
    

