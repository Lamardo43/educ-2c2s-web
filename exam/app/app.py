from flask import Flask, redirect, url_for
from mysqldb import DBConnector

app = Flask(__name__)
application = app
app.config.from_pyfile('config.py')

db_connector = DBConnector(app)

from auto import bp as auto_bp, init_login_manager

app.register_blueprint(auto_bp)
init_login_manager(app)


from books import bp as books_bp

app.register_blueprint(books_bp)


@app.route('/')
def index():
    return redirect(url_for('books.index'))
