from flask import render_template, redirect, request, url_for
from models.user import User, db


class UserController:
    @staticmethod
    def index():
        users = User.query.all()
        return render_template('index.html', users=users)
    
    @staticmethod
    def contact():
        if request.method == 'POST':
            nome = request.form['nome']
            email = request.form['email']
            senha = request.form['senha']
            tipo = request.form['useradmin']

            new_user = User(nome=nome, email=email, senha=senha, tipo=tipo)
            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for('index'))

        return render_template('contact.html')