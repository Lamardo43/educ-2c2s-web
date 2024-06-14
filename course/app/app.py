import math
from datetime import datetime, time

from flask import Flask, render_template, session, request, redirect, url_for, flash, current_app, send_file
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
from functools import wraps
from io import BytesIO
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
    def __init__(self, user_id, user_login, user_role):
        self.id = user_id
        self.login = user_login
        self.role = user_role

    def is_guide(self):
        return self.role == current_app.config['GUIDE_ROLE_NAME']


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


def get_orders_by_user(user_id, role):
    result = []
    with db_connector.connect().cursor(named_tuple=True) as cursor:
        base_query = (
            "SELECT orders.id AS order_id, orders.duration, orders.user_id AS order_user_id, orders.order_date AS order_date, "
            "orders.route_id AS order_route_id, orders.person_count AS order_person_count, "
            "orders.total_price AS order_total_price, routes.name, routes.id AS route_id, routes.route, "
            "routes.guide_id, routes.price_per_person, users.id AS user_id, "
            "users.role, users.firstname, users.lastname, users.middlename, users.login, "
            "users.password_hash FROM orders LEFT JOIN routes ON orders.route_id = routes.id "
            "LEFT JOIN users ON routes.guide_id = users.id ")
        if role == current_app.config['GUIDE_ROLE_NAME']:
            cursor.execute(
                base_query + "WHERE users.id = %s;",
                (user_id,))

            result = cursor.fetchall()
        elif role == current_app.config['TOURIST_ROLE_NAME']:
            cursor.execute(
                base_query + "WHERE orders.user_id = %s;",
                (user_id,))
            result = cursor.fetchall()
    return result


def get_route_info(route_id):
    result = []
    with db_connector.connect().cursor(named_tuple=True) as cursor:
        cursor.execute(
            "SELECT routes.id, route, price_per_person, name, firstname, lastname, middlename "
            "FROM routes left join users on (users.id = routes.guide_id) WHERE routes.id = %s",
            [route_id])
        result = cursor.fetchone()
    return result


def get_order_info(order_id, role):
    result = []
    with db_connector.connect().cursor(named_tuple=True) as cursor:
        base_query = ("SELECT orders.id AS order_id, orders.user_id AS order_user_id, orders.order_date AS order_date, "
                      "orders.route_id AS order_route_id, orders.duration, orders.person_count AS order_person_count, "
                      "orders.total_price AS order_total_price, routes.id AS route_id, routes.route, "
                      "routes.guide_id, routes.price_per_person, routes.name, users.id AS user_id, "
                      "users.role, users.firstname, users.lastname, users.middlename, users.login, "
                      "users.password_hash FROM orders LEFT JOIN routes ON orders.route_id = routes.id "
                      "LEFT JOIN users ")
        if role == current_app.config['GUIDE_ROLE_NAME']:
            cursor.execute(
                base_query + "ON orders.user_id = users.id WHERE orders.id = %s",
                (order_id,))
            result = cursor.fetchone()
        elif role == current_app.config['TOURIST_ROLE_NAME']:
            cursor.execute(
                base_query + "ON routes.guide_id = users.id WHERE orders.id = %s;",
                (order_id,))
            result = cursor.fetchone()
    return result


def get_routes(contains=None):
    result = []
    with db_connector.connect().cursor(named_tuple=True) as cursor:
        if contains is None:
            cursor.execute("SELECT routes.id, route, price_per_person, name, firstname, lastname, middlename "
                           "FROM routes left join users on (users.id = routes.guide_id)")
        else:
            cursor.execute("SELECT routes.id, route, price_per_person, name, firstname, lastname, middlename "
                           "FROM routes LEFT JOIN users ON users.id = routes.guide_id "
                           "WHERE route LIKE %s", ('%' + contains + '%',))
        result = list(enumerate(cursor.fetchall(), start=1))
    return result


def get_routes_by_guide(guide_id):
    result = []
    with db_connector.connect().cursor(named_tuple=True) as cursor:
        cursor.execute("SELECT routes.id, route, price_per_person, name "
                       "FROM routes WHERE guide_id = %s", (guide_id,))
        result = cursor.fetchall()
    return result


def get_selector_values():
    result = set()
    temp = get_routes()

    for i in temp:
        route_parts = i[1].route.split("&")
        result.update(route_parts)

    return sorted(result)


@login_manager.user_loader
def load_user(user_id):
    with db_connector.connect().cursor(named_tuple=True) as cursor:
        cursor.execute("SELECT id, login, role FROM users WHERE id = %s;", [user_id])
        user = cursor.fetchone()
    if user is not None:
        return User(user.id, user.login, user.role)
    return None


@app.route('/')
def index():
    return redirect(url_for('index_2', page=1))


@app.route('/<int:page>')
def index_2(page):
    selected = request.args.get('selected')
    if selected is not None:
        routes = get_routes(selected)
    else:
        routes = get_routes()
    return render_template('index.html', routes=routes, page=page, per_page_count=per_page_count,
                           total_count=math.ceil(len(routes) / per_page_count), selector_values=get_selector_values(),
                           selected=selected)


@app.route('/auth', methods=['POST', 'GET'])
def auth():
    error = ''
    if request.method == 'POST':
        login = request.form['username']
        password = request.form['password']
        remember_me = request.form.get('remember_me', None) == 'on'
        with db_connector.connect().cursor(named_tuple=True, buffered=True) as cursor:
            cursor.execute("SELECT id, login, role FROM users WHERE login = %s AND password_hash = SHA2(%s, 256)",
                           [login, password])
            user = cursor.fetchone()

        if user is not None:
            flash('Авторизация прошла успешно', 'success')
            login_user(User(user.id, user.login, user.role), remember=remember_me)
            next_url = request.args.get('next', url_for('index'))
            return redirect(next_url)
        flash('Invalid username or password', 'danger')
    return render_template('auth.html')


def validate_fields(fields):
    errors = {'date': [], 'time': []}

    if fields is not None:
        input_date = datetime.strptime(fields['date'], '%Y-%m-%d').date()
        if input_date < datetime.now().date():
            errors['date'].append('Дата не должна быть раньше текущей.')
        try:
            input_time = datetime.strptime(fields['time'], '%H:%M:%S').time()
        except ValueError:
            input_time = datetime.strptime(fields['time'], '%H:%M').time()

        if input_date == datetime.now().date() and input_time < datetime.now().time():
            errors['time'].append('Время не должно быть раньше текущего.')

        if not time(6, 0, 0) <= input_time <= time(23, 59, 59):
            errors['time'].append('Время должно быть в промежутке от 06 утра до 00 ночи.')

    return errors


@app.route('/route/<int:route_id>', methods=['GET', 'POST'])
def route(route_id):
    if request.method == 'POST':
        if not current_user.is_authenticated:
            flash('Чтобы оформить заказ, нужно войти в систему.', 'danger')
            return redirect(url_for('route', route_id=route_id))

        date = request.form.get('date')
        time = request.form.get('time')
        person_count = request.form.get('person_count')
        duration = request.form.get('duration')
        total_price = request.form.get('totalPrice')
        fields = {'date': date, 'time': time, 'person_count': person_count, 'duration': duration,
                  'totalPrice': total_price}

        errors = validate_fields(fields)

        if errors['date'] or errors['time']:
            return render_template("route_info.html", route_info=get_route_info(route_id), errors=errors,
                                   fields=fields)

        connection = db_connector.connect()
        try:

            with connection.cursor(named_tuple=True) as cursor:
                cursor.execute(
                    "INSERT INTO orders(user_id, route_id, person_count, total_price, order_date, duration) VALUES (%s, %s, %s, %s, %s, %s)",
                    [current_user.id, route_id, person_count, total_price, date + " " + time, duration])
                connection.commit()
            flash('Заказ успешно оформлен!', 'success')
        except connector.errors.DatabaseError as e:
            print(e)
            flash('Произошла ошибка при оформлении заказа.', 'danger')
            connection.rollback()

        return redirect(url_for('account'))

    return render_template("route_info.html", route_info=get_route_info(route_id), errors={})


@app.route('/order/<int:order_id>')
@login_required
def order(order_id):
    return render_template("order_info.html", order_info=get_order_info(order_id, current_user.role))


@app.route('/order/<int:order_id>/edit', methods=['GET', 'POST'])
@login_required
def order_edit(order_id):
    if request.method == 'POST':
        if not current_user.is_authenticated:
            flash('Чтобы изменить заказ, нужно войти в систему.', 'danger')
            return redirect(url_for('order', order_id=order_id))

        order_info_query = get_order_info(order_id, current_user.role)
        date = request.form.get('date')
        time = request.form.get('time')
        person_count = request.form.get('person_count')
        duration = request.form.get('duration')
        total_price = request.form.get('totalPrice')
        fields = {'date': date, 'time': time, 'person_count': person_count, 'duration': duration,
                  'totalPrice': total_price}

        errors = validate_fields(fields)

        if errors['date'] or errors['time']:
            return render_template("order_edit.html", order_info=get_order_info(order_id, current_user.role),
                                   errors=errors)

        connection = db_connector.connect()
        try:

            with connection.cursor(named_tuple=True) as cursor:
                cursor.execute(
                    "UPDATE orders SET user_id = %s, route_id = %s, person_count = %s, total_price = %s, order_date = %s, duration = %s"
                    "WHERE orders.id = %s", (
                        current_user.id, order_info_query.route_id, person_count, total_price, date + " " + time,
                        duration,
                        order_id))
                connection.commit()
            flash('Заказ успешно оформлен!', 'success')
        except connector.errors.DatabaseError as e:
            print(e)
            flash('Произошла ошибка при оформлении заказа.', 'danger')
            connection.rollback()

        return redirect(url_for('account'))

    return render_template("order_edit.html", order_info=get_order_info(order_id, current_user.role), errors={})


@app.route('/order/<int:order_id>/delete', methods=['GET', 'POST'])
@login_required
def order_delete(order_id):
    if request.method == 'POST':
        connection = db_connector.connect()
        try:
            with connection.cursor(named_tuple=True, buffered=True) as cursor:
                cursor.execute("DELETE FROM orders WHERE id = %s", [order_id])
                connection.commit()
                flash('Заказ успешно удален', 'success')
        except db_connector.errors.DatabaseError:
            flash("Произошла ошибка при удалении заказа.", "danger")
            connection.rollback()
        return redirect(url_for('account'))
    return render_template("order_delete.html", order_id=order_id)


@app.route('/export_orders.csv')
@login_required
def export_orders():
    orders = get_orders_by_user(current_user.id, current_user.role)
    file = ''
    fields_in_file = ['Номер заказа', 'Длительность', 'Дата экскурсии', 'Количество персон', 'Суммарная стоимость',
                      'Название', 'Маршрут', 'Имя гида', 'Фамилия гида', 'Отчество гида']
    fields_in_db = ['order_id', 'duration', 'order_date', 'order_person_count', 'order_total_price', 'name', 'route',
                    'firstname', 'lastname', 'middlename']
    file += ','.join(fields_in_file) + '\n'
    for order in orders:
        file += ','.join([str(getattr(order, field)) for field in fields_in_db]) + '\n'

    return send_file(BytesIO(file.encode()), as_attachment=True, mimetype='text/csv', download_name='export_orders.csv')


@app.route('/export_routes.csv')
@login_required
def export_routes():
    if current_user.is_guide():
        routes = get_routes_by_guide(current_user.id)
        # print(routes)
        file = ''
        fields_in_file = ['Номер Маршрута', 'Название', 'Достопримечательности', 'Цена за человека']
        fields_in_db = ['id', 'name', 'route', 'price_per_person']
        file += ','.join(fields_in_file) + '\n'
        for route in routes:
            file += ','.join([str(getattr(route, field)) for field in fields_in_db]) + '\n'

        return send_file(BytesIO(file.encode()), as_attachment=True, mimetype='text/csv',
                         download_name='export_routes.csv')


@app.route('/account')
@login_required
def account():
    if current_user.is_guide():
        return render_template("account.html", orders=get_orders_by_user(current_user.id, current_user.role),
                               routes=get_routes_by_guide(current_user.id))
    else:
        return render_template("account.html", orders=get_orders_by_user(current_user.id, current_user.role))


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
