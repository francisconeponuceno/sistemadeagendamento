from flask import render_template, redirect, request, url_for
from models.user import User, Cliente, Profissional, Servico, Agendamento, db


class UserController:
    @staticmethod
    def index():
        cardServico = Servico.query.all()
        if cardServico:
            return render_template('index.html', cardServico=cardServico)

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
        DadosServico = Servico.query.all()
        return render_template('admin.html',DadosProf=DadosProf, DadosServico=DadosServico)

    @staticmethod
    def agendar(Id_CardServico):
        
        ContEtapa = 1
        agendamento = Agendamento.query.get_or_404(Id_CardServico)
        if agendamento:
            return render_template('agendar.html',ContEtapa=ContEtapa, agendamento=agendamento)

    ####################################################INICO CRUD DO PROFISSIONAL#################################################################
    # ROTA CADASTRO DE PROFISSIONAL
    @staticmethod
    def CadProfissional():
        if request.method == 'POST':
            nome = request.form['nome'].upper()
            especialidade = request.form['especialidade'].upper()
            horadio_atendimento = request.form['h_atendimento'].upper()
            telefone = request.form['telefone']
            new_profissional = Profissional(No_Profissional=nome, Nr_Telefone=telefone, Hr_Atendimento=horadio_atendimento, No_Especialidade=especialidade,)
            db.session.add(new_profissional)
            db.session.commit()
            return redirect("admin")

    # ROTA UPDATE / DELETE
    @staticmethod
    def crudProfissional(Id_Profissional):
        if request.method == 'POST':
            profissional = Profissional.query.get_or_404(Id_Profissional)
            return render_template("crudProfissional.html", profissional=profissional)

    # ROTA UPDATE PROFISSIONAL
    @staticmethod
    def updateProfissional(Id_Profissional):
        if request.method == 'POST':
            profissional = Profissional.query.get_or_404(Id_Profissional)
            profissional.No_Profissional = request.form['nome'].upper()
            profissional.No_Especialidade = request.form['especialidade'].upper()
            profissional.Hr_Atendimento = request.form['h_atendimento'].upper()
            profissional.Nr_Telefone = request.form['telefone']
            db.session.commit()
            return redirect("/admin")

    # ROTA DELETE PROFISSIONAL
    @staticmethod
    def DeleteProfissional(Id_Profissional):
        profissional = Profissional.query.get_or_404(Id_Profissional)
        db.session.delete(profissional)
        db.session.commit()
        return redirect("/admin")

    ####################################################FIM  CRUD DO PROFISSIONAL#################################################################


    #####################################################INICO CRUD DO SERVIÇO#########################################################################
    # ROTA CADASTRO DE SEVIÇO
    @staticmethod
    def CadServico():
        if request.method == 'POST':
            servico = request.form['servico'].upper().strip()
            valor = request.form['valor']
            tempo = request.form['tempo'].upper().strip()
            descricao1 = request.form['descricao1'].upper().strip()
            descricao2 = request.form['descricao2'].upper().strip()
            descricao3 = request.form['descricao3'].upper().strip()
            descricao4 = request.form['descricao4'].upper().strip()

            new_servico = Servico(No_Servico=servico,
                                Pr_Servico=valor,
                                Tp_Estimado=tempo, 
                                Dc_Descricao1=descricao1,
                                Dc_Descricao2=descricao2,
                                Dc_Descricao3=descricao3,
                                Dc_Descricao4=descricao4
                                )
            db.session.add(new_servico)
            db.session.commit()
            return redirect("/admin")


    # ROTA UPDATE / DELETE
    @staticmethod
    def crudServico(Id_Servico):
        if request.method == 'POST':
            servico = Servico.query.get_or_404(Id_Servico)
            return render_template('crudServico.html', servico=servico)
        

    # ROTA UPDATE SERVICO
    @staticmethod
    def updateServico(Id_Servico):
        if request.method == 'POST':
            servico = Servico.query.get_or_404(Id_Servico)
            servico.No_Servico = request.form['servico'].upper().strip()
            servico.Pr_Servico = request.form['valor'].strip()
            servico.Tp_Estimado = request.form['tempo']
            servico.Dc_Descricao1 = request.form['descricao1']
            servico.Dc_Descricao2 = request.form['descricao2']
            servico.Dc_Descricao3 = request.form['descricao3']
            servico.Dc_Descricao4 = request.form['descricao4']
            db.session.commit()
            return redirect("/admin")
        
    @staticmethod
    def DeleteServico(Id_Servico):
        if request.method == 'POST':
            servico = Servico.query.get_or_404(Id_Servico)
            db.session.delete(servico)
            db.session.commit()
            return redirect("/admin")

        


