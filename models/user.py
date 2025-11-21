from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import date, datetime

hora = datetime.now()
hora = hora.strftime('%I:%M:%S')

db = SQLAlchemy()
migrate = Migrate()

class User(db.Model):
    __tablename__ = "administrador"

    Id_admin = db.Column(db.Integer, primary_key=True)
    No_admin = db.Column(db.String(100), nullable=False)
    No_email_admin = db.Column(db.String(100), nullable=False, unique=True)
    Nu_tel_admin = db.Column(db.String(20), nullable=False)
    No_senha_admin = db.Column(db.String(100), unique=True)
    Tp_admin = db.Column(db.String(1), nullable=False, default='A')
    At_admin = db.Column(db.Integer, nullable=False, default=1)
    Dt_criacao = db.Column(db.Date, default=date.today)
    Hr_cadastro = db.Column(db.DateTime, default=datetime.now)


# ------------------
# TABLELA CLIENTE
# ------------------
class Cliente(db.Model):
    __tablename__ = "clientes"

    Id_cliente = db.Column(db.Integer, primary_key=True)
    No_cliente = db.Column(db.String(100), nullable=False)
    No_email_cliente = db.Column(db.String(100), nullable=False, unique=True)
    Nu_tel_cliente = db.Column(db.String(20), nullable=False)
    No_senha_cliente = db.Column(db.String(100), unique=True)
    Tp_cliente = db.Column(db.String(20), nullable=False, default='C')
    At_cliente = db.Column(db.Integer, nullable=False, default=1)
    Dt_criacao = db.Column(db.Date, default=date.today)
    Hr_cadastro = db.Column(db.DateTime, default=datetime.now)

    # relacionamento: um cliente pode ter vários agendamentos
    agendamentos = db.relationship("Agendamento", back_populates="cliente")


# --------------------
# TABELA PROFISSIONAIS
# --------------------
class Profissional(db.Model):
    __tablename__ = 'profissionais'

    Id_profissional = db.Column(db.Integer, primary_key=True)
    No_profissional = db.Column(db.String(100), nullable=False)
    Es_profissional = db.Column(db.String(100))
    No_email_profissional = db.Column(db.String(100), nullable=False, unique=True)
    Nu_tel_profissional = db.Column(db.String(20), nullable=False)
    No_senha_profissional = db.Column(db.String(100), unique=True)
    Tp_profissional = db.Column(db.String(20), nullable=False, default='P')
    At_profissional = db.Column(db.Integer, nullable=False, default=1)
    Dt_criacao = db.Column(db.Date, default=date.today)
    Hr_cadastro = db.Column(db.DateTime, default=datetime.now)

    # relacionamento: um profissional pode ter vários agendamentos
    agendamentos = db.relationship('Agendamento', back_populates='profissional')


# --------------------
# TABELA SERVIÇO
# --------------------

class Servico(db.Model):
    __tablename__ = 'servicos'

    Id_servico = db.Column(db.Integer, primary_key=True)
    No_servico = db.Column(db.String(100), nullable=False)
    Pr_servico = db.Column(db.Float, nullable=False)
    At_servico = db.Column(db.Integer, nullable=False, default=1)
    Dt_criacao = db.Column(db.Date, default=date.today)
    Hr_cadastro = db.Column(db.DateTime, default=datetime.now)

    # relacionamento: um serviço pode estar em vários agendamentos
    agendamentos = db.relationship('Agendamento', back_populates='servico')


# --------------------
# TABELA AGENDAMENTOS
# --------------------

class Agendamento(db.Model):
    __tablename__ = 'agendamentos'

    Id_agendamento = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.Id_cliente'),nullable=False)
    profissional_id = db.Column(db.Integer, db.ForeignKey('profissionais.Id_profissional'),nullable=False)
    servico_id = db.Column(db.Integer, db.ForeignKey('servicos.Id_servico'), nullable=False)

    Dt_agendamento = db.Column(db.Date, nullable=False)
    Hr_agendamento = db.Column(db.Time, nullable=False)
    status_agendamento = db.Column(db.String(20), default='pendente')

    # RELACIONAMENTOS REVERSOS
    cliente = db.relationship('Cliente', back_populates='agendamentos')
    profissional = db.relationship('Profissional', back_populates='agendamentos')
    servico = db.relationship('Servico', back_populates='agendamentos')
