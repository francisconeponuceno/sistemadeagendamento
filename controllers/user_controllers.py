from flask import render_template, redirect, request, url_for
from models.user import User, Cliente, Profissional, Servico, Agendamento, db


class UserController:
    @staticmethod
    def index():
        users = User.query.all()
        return render_template('index.html', users=users)

    @staticmethod
    def login():
        if request.method == 'POST':
            nome = request.form['nome']
            email = request.form['email']
            fone = request.form['fone']
            senha = request.form['senha']
            tipo = request.form['useradmin']

            if not nome or not email or not senha or not tipo:
                return render_template('login.html', error='por favor preencha todos os campos')

            new_user = User(nome=nome, email=email, telefone=fone, senha=senha, tipo=tipo)
            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for('index'))

        return render_template('login.html')

    @staticmethod
    def cadastro():
        return render_template('cadastro.html')

    @staticmethod
    def cliete():
        return render_template('cliente.html')

    # ROTA DO ADMINISTRADOR
    @staticmethod
    def admin():
        DadosProf = Profissional.query.all()
        return render_template('admin.html',DadosProf=DadosProf)

    @staticmethod
    def agendar():
        ContEtapa = 1
        return render_template('agendar.html',ContEtapa=ContEtapa)

    # ROTA CADASTRO DE PROFISSIONAL
    @staticmethod
    def CadProfissional():
        if request.method == 'POST':
            nome = request.form['nome']
            especialidade = request.form['especialidade']
            horadio_atendimento = request.form['h_atendimento']
            telefone = request.form['telefone']
            new_profissional = Profissional(No_Profissional=nome, Nr_Telefone=telefone, Hr_Atendimento=horadio_atendimento, No_Especialidade=especialidade,)
            db.session.add(new_profissional)
            db.session.commit()
            return redirect("admin")

    @staticmethod
    def updatedelete(Id_Profissional):

        if request.method == 'POST':
            profissional = Profissional.query.get_or_404(Id_Profissional)
            
            return render_template("updatedelete.html", profissional=profissional)

    # ROTA DELETE PROFISSIONAL
    @staticmethod
    def DeleteProfissional(Id_Profissional):

        profissional = Profissional.query.get_or_404(Id_Profissional)
        db.session.delete(profissional)
        db.session.commit()
        return redirect("/admin")
