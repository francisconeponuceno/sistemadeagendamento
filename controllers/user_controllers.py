from flask import render_template, redirect, request, url_for
from models.user import User, db


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