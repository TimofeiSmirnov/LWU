from flask import render_template, request, flash, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

from app.extensions import db
from app.module.modules import User, TemporaryMock, Subject
from app.main import mn


@mn.route('/')
def index():
    if 'authentificated' in session:
        return render_template('index-logged.html', fullname=session['name'] + session['surname'])
    else:
        return render_template('index.html')


@mn.route('/login', methods=('GET', 'POST'))
def login():
    error = None

    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')

        hashed_password = generate_password_hash(password)

        user = User.query.filter_by(login=login).first()

        if len(password) < 7:
            error = "Пароль слишком короткий"

        if not (error is None):
            if user is None:
                error = "Неверный логин или пароль"
            else:
                if not check_password_hash(user.password, password):
                    error = "Неверный логин или пароль"

        if error is None:

            session['authentificated'] = True
            session['id'] = user.id
            session['login'] = login
            session['name'] = user.name
            session['surname'] = user.surname

            return redirect(url_for('main.index'))
        else:
            flash(error)

    return render_template('login.html')


@mn.route('/signup', methods=('GET', 'POST'))
def signup():
    error = None

    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        name = request.form.get('name')
        surname = request.form.get('surname')

        hashed_password = generate_password_hash(password)

        user = User.query.filter_by(login=login).first()

        if len(password) < 7:
            error = "Пароль слишком короткий"

        if not (error is None):
            if not (user is None):
                error = "Логин уже занят"

        if error is None:
            new_user = User(name=name, surname=surname, login=login, password=hashed_password, reg_date=datetime.now())
            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for('main.login'))
        else:
            flash(error)

    return render_template('signup.html')


@mn.route('/info')
def info():
    info = [session["name"], session["surname"], session["login"]]
    return render_template("info.html", user=info)


@mn.route('/logout')
def logout():
    session.clear()
    return redirect(url_for("main.index"))


@mn.route('/mocks')
def mocks():
    if len(session) == 0:
        mocks = TemporaryMock.query.all()

        if len(mocks) == 0:
            no_mocks = True

        return render_template("mocks-not-logged.html", mocks=mocks, no_mocks=no_mocks)
    else:
        info = [session["name"], session["surname"], session["login"]]
        mocks = TemporaryMock.query.all()

        if len(mocks) == 0:
            no_mocks = True

        return render_template("mocks.html", user=info, mocks=mocks, no_mocks=no_mocks)

