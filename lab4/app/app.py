from flask import Flask, render_template, session, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
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


def check_login(login):
    errors = []
    if login is None or len(login) < 5:
        errors.append("Длина логина должна быть не менее 5 символов.")
    if login and not re.match("^[a-zA-Z0-9]+$", login):
        errors.append("Логин должен содержать только латинские буквы и цифры.")
    return errors


def check_password(password):
    errors = []
    if password is None or len(password) < 8 or len(password) > 128:
        errors.append("Длина пароля должна быть от 8 до 128 символов.")
    if password is None or not re.search("[a-z]", password):
        errors.append("Пароль должен содержать как минимум одну строчную букву.")
    if password is None or not re.search("[A-Z]", password):
        errors.append("Пароль должен содержать как минимум одну заглавную букву.")
    if password is None or not re.search("[0-9]", password):
        errors.append("Пароль должен содержать как минимум одну цифру.")
    if password is None or not re.search(r"[~!@#$%^&*_\-+=()\[\]{}><\\/|\"'.,:;]", password):
        errors.append("Пароль должен содержать хотя бы один специальный символ")
    return errors

def validate_name(name):
    errors = []
    if name is None or len(name) == 0:
        errors.append("Имя не должно быть пустым")

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
    return redirect(url_for('auth'))


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
        errors['confirm_password'] = ''
        if confirm_password != new_password:
            errors['confirm_password'] = ['Пароли должны совпадать']

        connection = db_connector.connect()

        try:
            with connection.cursor(named_tuple=True, buffered=True) as cursor:
                cursor.execute("SELECT id FROM users WHERE id = %s AND password_hash = SHA2(%s, 256)",
                               [user_id, old_password])
                errors['old_password'] = ''
                if not cursor.fetchone():
                    errors['old_password'] = ['Введён неверный пароль']

                errors['new_password'] = check_password(new_password)
                print(errors)
                if not errors['old_password'] and not errors['new_password'] and not errors['confirm_password']:
                    cursor.execute("UPDATE users SET password_hash = SHA2(%s, 256) WHERE id = %s",
                                   [new_password, user_id])
                    connection.commit()
                    flash("Вы успешно сменили пароль", "success")
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
        errors['first_name'] = validate_name(user_data['first_name'])
        errors['last_name'] = validate_name(user_data['last_name'])

        if errors['login'] or errors['password']:
            return render_template(
                'users_new.html',
                user_data=user_data,
                roles=get_roles(),
                errors=errors
            )
        connection = db_connector.connect()
        try:

            with connection.cursor(named_tuple=True) as cursor:
                print(user_data)
                cursor.execute(
                    "INSERT INTO users (login, password_hash, first_name, middle_name, last_name, role_id) VALUES "
                    "(%s, SHA2(%s, 256), %s, %s, %s, %s)",
                    [user_data["login"], user_data["password"], user_data["first_name"], user_data["middle_name"], user_data["last_name"], user_data["role_id"]])
                print(cursor.statement)
                connection.commit()
            flash('Учетная запись успешно создана', 'success')
            return redirect(url_for('users'))
        except connector.errors.DatabaseError:
            flash('Произошла ошибка при создании записи. Проверьте, что все необходимые поля заполнены', 'danger')
            connection.rollback()
    return render_template('users_new.html', user_data=user_data, roles=get_roles(), errors=errors)


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
    errors = {}
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
        errors['first_name'] = validate_name(user_data['first_name'])
        errors['last_name'] = validate_name(user_data['last_name'])
        if errors['first_name'] or errors['last_name']:
            return render_template(
                'users_edit.html',
                user_data=user_data,
                roles=get_roles(),
                errors=errors
            )
        user_data['id'] = user_id

        try:
            with db_connector.connect() as conn:
                with conn.cursor(named_tuple=True, buffered=True) as cursor:
                    cursor.execute(
                        "UPDATE users SET first_name = %(first_name)s, "
                        "middle_name = %(middle_name)s, last_name = %(last_name)s, "
                        "role_id = %(role_id)s WHERE id = %(id)s",
                        user_data)
                conn.commit()
            flash('Учетная запись успешно изменена', 'success')
            return redirect(url_for('users'))
        except connector.errors.DatabaseError as e:
            flash('Произошла ошибка при изменении записи: {}'.format(e), 'danger')

    return render_template('users_edit.html', user_data=user_data, roles=get_roles(), errors=errors)



@app.route('/users/<int:user_id>/delete')
@login_required
def users_delete(user_id):
    connection = db_connector.connect()
    try:
        with connection.cursor(named_tuple=True, buffered=True) as cursor:
            cursor.execute("DELETE FROM users WHERE id = %s", [user_id])
            connection.commit()
            flash('Учетная запись успешно удалена', 'success')
            return redirect(url_for('users'))
    except connector.errors.DatabaseError:
        flash("Произошла ошибка при удалении записи.", "danger")
        connection.rollback()

if __name__ == '__main__':
    app.run(debug=True)