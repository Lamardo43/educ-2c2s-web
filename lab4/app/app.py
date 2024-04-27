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
    if not re.match("[~!@#$%^&*_\-+=()\[\]{}><\\/|\"'.,:;]", password):
        errors.append(
            "Пароль может содержать только латинские или кириллические буквы, арабские цифры и указанные символы.")
    return errors


def get_roles():
    result = []
    with db_connector.connect().cursor(named_tuple=True) as cursor:
        cursor.execute("SELECT * FROM roles")
        result = cursor.fetchall()
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
    return render_template('index.html')


@app.route('/secret')
@login_required
def secret():
    return render_template('secret.html')


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


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/counter')
def counter():
    session['counter'] = session.get('counter', 0) + 1
    return render_template('counter.html')

@app.route('/change-password', methods=['GET', 'POST'])
@login_required
def change_password():
    errors = {}
    if request.method == 'POST':
        user_id = current_user.id
        old_password = request.form['old_password']
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']
        if confirm_password != new_password:
            errors['confirm_password'] = ['Пароли должны совпадать']

        connection = db_connector.connect()

        try:
            with connection.cursor(named_tuple=True, buffered=True) as cursor:
                cursor.execute("SELECT id FROM users WHERE id = %s AND password_hash = SHA2(%s, 256)", [user_id, old_password])
                if not cursor.fetchone():
                    errors['old_password'] = ['Введён неверный пароль']

                errors['new_password'] = check_password(new_password)
                if not errors['new_password'] and not errors['new_password']:
                    cursor.execute("UPDATE users SET password_hash = SHA2(%s, 256) WHERE id = %s", [new_password, user_id])
                    flash("Вы успешно сменили пароль", "susses")
                    return redirect(url_for('users'))
        except connector.errors.DatabaseError:
            flash('Произошла ошибка при создании записи. Проверьте, что все необходимые поля заполнены', 'danger')
            connection.rollback()

    return render_template('change_password.html', errors=errors)

@app.route('/users')
def users():
    with db_connector.connect().cursor(named_tuple=True) as cursor:
        cursor.execute("SELECT users.*, roles.name AS role FROM users LEFT JOIN roles ON users.role_id = roles.id")
        print(cursor.statement)
        users = cursor.fetchall()
    return render_template('users.html', users=users)


@app.route('/users/new', methods=['POST', 'GET'])
@login_required
def users_new():
    user_data = {}
    errors = {}
    if request.method == 'POST':
        fields = ('login', 'password', 'first_name', 'middle_name', 'last_name', 'role_id')
        user_data = {field: request.form[field] or None for field in fields}
        errors['login'] = check_login(user_data['login'])
        errors['password'] = check_password(user_data['password'])

        if errors['login'] or errors['password']:
            return render_template(
                'users_new.html',
                user_data=user_data,
                roles=get_roles()
            )
        connection = db_connector.connect()
        try:

            with connection.cursor(named_tuple=True) as cursor:
                cursor.execute(
                    "INSERT INTO users (login, password_hash, first_name, middle_name, last_name, role_id) VALUES "
                    "(%(login)s, SHA2(%(password)s, 256), %(first_name)s, %(middle_name)s, %(last_name)s, %(role_id)s)",
                    [user_data])
                print(cursor.statement)
                connection.commit()
            flash('Учетная запись успешно создана', 'success')
            return redirect(url_for('users'))
        except connector.errors.DatabaseError:
            flash('Произошла ошибка при создании записи. Проверьте, что все необходимые поля заполнены', 'danger')
            connection.rollback()
    return render_template('users_new.html', user_data=user_data, roles=get_roles())


@app.route('/users/<int:user_id>')
def users_view(user_id):
    with db_connector.connect().cursor(named_tuple=True) as cursor:
        cursor.execute("SELECT * FROM users WHERE id = %s", [user_id])
        user_data = cursor.fetchone()
        if not user_data:
            flash('Пользователя нет в базе данных', 'error')
            return redirect(url_for('users'))
        cursor.execute("SELECT name FROM roles WHERE id = %s", [user_data.role_id])
        user_role = cursor.fetchone()
    return render_template('users_view.html', user_data=user_data, user_role=user_role.name)


@app.route('/users/<int:user_id>/edit', methods=['POST', 'GET'])
@login_required
def users_edit(user_id):
    user_data = {}
    with db_connector.connect().cursor(named_tuple=True, buffered=True) as cursor:
        cursor.execute("SELECT first_name, middle_name, last_name, role_id FROM users WHERE id = %s",
                       [user_id])
        user_data = cursor.fetchone()
        if user_data is None:
            flash('Пользователя нет в базе данных', 'danger')
            return redirect(url_for('users'))
    if request.method == 'POST':
        fields = ('first_name', 'middle_name', 'last_name', 'role_id')
        user_data = {field: request.form[field] or None for field in fields}
        user_data['id'] = user_id
        try:
            with db_connector.connect().cursor(named_tuple=True, buffered=True) as cursor:
                cursor.execute(
                    "UPDATE users SET first_name = %(first_name)s, "
                    "middle_name = %(middle_name)s, last_name = %(last_name)s, "
                    "role_id = %(role_id)s WHERE id = %(id)s",
                    [user_data])
                flash('Учетная запись успешно изменена', 'success')
                return redirect(url_for('users'))
        except connector.errors.DatabaseError:
            flash('Произошла ошибка при изменении записи.', 'danger')
    return render_template('users_edit.html', user_data=user_data, roles=get_roles())


@app.route('/users/<int:user_id>/delete', methods=['POST'])
@login_required
def users_delete(user_id):
    connection = db_connector.connect()
    try:
        with connection.cursor(named_tuple=True, buffered=True) as cursor:
            cursor.execute("DELETE FROM users WHERE id = %s", [user_id])
            flash('Учетная запись успешно удалена', 'success')
            return redirect(url_for('users'))
    except connector.errors.DatabaseError:
        flash("Произошла ошибка при удалении записи.", "danger")
        connection.rollback()


# python -m venv ve
# . ve/bin/activate -- Linux
# ve\Scripts\activate -- Windows
# pip install flask python-dotenv
# cd app
# flask run
if __name__ == '__main__':
    app.run(debug=True)
