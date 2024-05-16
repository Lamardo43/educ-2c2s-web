import math

from flask import Flask, render_template, session, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
from functools import wraps
from mysqldb import DBConnector
import mysql.connector as connector
import re

app = Flask(__name__)
application = app
app.config.from_pyfile('config.py')

db_connector = DBConnector(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth'
login_manager.login_message = 'Авторизуйтесь для доступа к этому ресурсу'
login_manager.login_message_category = 'warning'

per_page_count = 7
class User(UserMixin):
    def __init__(self, user_id, user_login):
        self.id = user_id
        self.user_login = user_login


def check_for_login(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        if not current_user.is_authenticated:
            flash('Вы не авторизованы', 'warning')
            return redirect(url_for('index'))
        return function(*args, **kwargs)

    return wrapper


def check_login(login):
    errors = []
    if len(login) < 5:
        errors.append("Длина логина должна быть не менее 5 символов.")
    if not re.match("^[a-zA-Z0-9]+$", login):
        errors.append("Логин должен содержать только латинские буквы и цифры.")
    return errors


def check_password(password):
    errors = []
    if len(password) < 8 or len(password) > 128:
        errors.append("Длина пароля должна быть от 8 до 128 символов.")
    if not re.search("[a-z]", password):
        errors.append("Пароль должен содержать как минимум одну строчную букву.")
    if not re.search("[A-Z]", password):
        errors.append("Пароль должен содержать как минимум одну заглавную букву.")
    if not re.search("[0-9]", password):
        errors.append("Пароль должен содержать как минимум одну цифру.")
    if not re.search(r"[~!@#$%^&*_\-+=()\[\]{}><\\/|\"'.,:;]", password):
        errors.append("Пароль должен содержать хотя бы один специальный символ")
    return errors
def get_roles():
    result = []
    with db_connector.connect().cursor(named_tuple=True) as cursor:
        cursor.execute("SELECT * FROM roles")
        result = cursor.fetchall()
    return result

def get_route_info(route_id):
    result = []
    with db_connector.connect().cursor(named_tuple=True) as cursor:
        cursor.execute("SELECT routes.id, route, duration, price_per_person, firstname, lastname, middlename FROM routes left join users on (users.id = routes.guide_id) WHERE routes.id = %s", [route_id])
        result = cursor.fetchone()
    return result
def get_routes():
    result = []
    with db_connector.connect().cursor(named_tuple=True) as cursor:
        cursor.execute("SELECT routes.id, route, duration, price_per_person, firstname, lastname, middlename FROM routes left join users on (users.id = routes.guide_id)")
        result = list(enumerate(cursor.fetchall(), start=1))
    return result

@login_manager.user_loader
def load_user(user_id):
    with db_connector.connect().cursor(named_tuple=True) as cursor:
        cursor.execute("SELECT id, login FROM users WHERE id = %s;", [user_id])
        user = cursor.fetchone()
    if user is not None:
        return User(user.id, user.login)
    return None


@app.route('/')
def index():
    return redirect(url_for('index_2', page=1))

@app.route('/<int:page>')
def index_2(page):
    routes=get_routes()
    return render_template('index.html', routes=routes, page=page, per_page_count=per_page_count,total_count=math.ceil(len(routes)/per_page_count))

@app.route('/auth', methods=['POST', 'GET'])
def auth():
    error = ''
    if request.method == 'POST':
        login = request.form['username']
        password = request.form['password']
        remember_me = request.form.get('remember_me', None) == 'on'
        with db_connector.connect().cursor(named_tuple=True, buffered=True) as cursor:
            print(login)
            cursor.execute("SELECT id, login FROM users WHERE login = %s AND password_hash = SHA2(%s, 256)",
                           [login, password])
            print(cursor.statement)
            user = cursor.fetchone()

        if user is not None:
            flash('Авторизация прошла успешно', 'success')
            login_user(User(user.id, user.login), remember=remember_me)
            next_url = request.args.get('next', url_for('index'))
            return redirect(next_url)
        flash('Invalid username or password', 'danger')
    return render_template('auth.html')


@app.route('/route/<int:route_id>')
def route(route_id):
    return render_template("route_info.html", route_info=get_route_info(route_id))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth'))

if __name__ == '__main__':
    app.run(debug=True)