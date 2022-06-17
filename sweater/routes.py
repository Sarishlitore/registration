from flask import render_template, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user
from sweater import app, chatdb, UserLogin
from sweater.forms import LoginForm, RegistrationForm
from werkzeug.security import generate_password_hash, check_password_hash


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/registration', methods=['POST', 'GET'])
def registration():
    form = RegistrationForm()

    if form.validate_on_submit():
        hash_psw = generate_password_hash(form.psw.data)
        if chatdb.add_user(name=form.name.data, email=form.email.data, hash_psw=hash_psw):
            flash("Вы успешно зарегистрированы", "success")
            return redirect(url_for('index'))
        else:
            flash("Ошибка при добавлении в БД", "error")
    return render_template('registration.html', form=form)


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = chatdb.get_user_by_email(form.email.data)
        if user and check_password_hash(user.psw, form.psw.data):
            user_login = UserLogin().create(user)
            login_user(user_login)
            return redirect(url_for('profile'))
    return render_template('login.html', form=form)


@app.route('/profile')
@login_required
def profile():
    return render_template('user.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')