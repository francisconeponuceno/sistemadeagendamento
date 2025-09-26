from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import date, datetime

hora = datetime.now()
hora = hora.strftime('%I:%M:%S')

db = SQLAlchemy()
migrate = Migrate()

class User(db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    telefone = db.Column(db.String(20), nullable=False, key='sem telefone')
    senha = db.Column(db.String(100), nullable=False, unique=True)
    tipo = db.Column(db.String(20), nullable=False)
    data_criacao = db.Column(db.Date, default=date.today)
    hora_cadastro = db.Column(db.DateTime, default=datetime.now)


#------------------
# TABLELA CLIENTE
#------------------
class Cliente(db.Model):
    __tablename__ = "clientes"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)

    # relacionamento: um cliente pode ter vários agendamentos
    agendamentos = db.relationship("Agendamento", back_populates="cliente")


#--------------------
# TABELA PROFISSIONAIS
#--------------------
class Profissional(db.Model):
    __tablename__ = 'profissionais'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    especialidade = db.Column(db.String(100))

    # relacionamento: um profissional pode ter vários agendamentos
    agendamentos = db.relationship('Agendamento', back_populates='profissional')


#--------------------
# TABELA SERVIÇO
#--------------------

class Servico(db.Model):
    __tablename__ = 'servicos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False)

    # relacionamento: um serviço pode estar em vários agendamentos
    agendamentos = db.relationship('Agendamento', back_populates='servico')


#--------------------
# TABELA AGENDAMENTOS
#--------------------

class Agendamento(db.Model):
    __tablename__ = 'agendamentos'

    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'),nullable=False)
    profissional_id = db.Column(db.Integer, db.ForeignKey('profissionais.id'),nullable=False)
    servico_id = db.Column(db.Integer, db.ForeignKey('servicos.id'), nullable=False)

    data = db.Column(db.Date, nullable=False)
    hora = db.Column(db.Time, nullable=False)
    status = db.Column(db.String(20), default='pendente')

    # RELACIONAMENTOS REVERSOS
    cliente = db.relationship('Cliente', back_populates='agendamentos')
    profissional = db.relationship('Profissional', back_populates='agendamentos')
    servico = db.relationship('Servico', back_populates='agendamentos')
    
    
