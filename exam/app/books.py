import hashlib
import math
import os
import bleach
from datetime import datetime

from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user

from app import db_connector

bp = Blueprint('books', __name__, url_prefix='/books')

MAX_PER_PAGE = 8


def save_cover(background_image):
    if background_image:
        md5_hash = hashlib.md5(background_image.read()).hexdigest()
        mime_type = background_image.mimetype

        try:
            with db_connector.connect().cursor(named_tuple=True, buffered=True) as cursor:
                cursor.execute("SELECT id FROM covers WHERE filename=%s", (md5_hash + ".png",))
                count = cursor.fetchone()

                if count is not None:
                    cover_id = count.id
                else:
                    cursor.execute("INSERT INTO covers (mime_type, filename) VALUES (%s, %s)",
                                   (mime_type, f'{md5_hash}.png'))
                    cover_id = cursor.lastrowid

                    db_connector.connect().commit()
            filename = f"{md5_hash}.png"

            file_path = os.path.join('static/images', filename)
            background_image.seek(0)
            background_image.save(file_path)

            return cover_id
        except Exception as e:
            print(f"Ошибка сохранения обложки: {e}")
            db_connector.connect().rollback()

    return None


def insert_book_genres(book_id, genres_selected):
    with db_connector.connect().cursor(named_tuple=True, buffered=True) as cursor:
        cursor.executemany("INSERT IGNORE INTO book_genres (book_id, genre_id) VALUES (%s, %s)",
                           [(book_id, genre_id) for genre_id in genres_selected])
        db_connector.connect().commit()


@bp.route('/')
@login_required
def index():
    page = int(request.args.get('page', 1))
    offset = (page - 1) * MAX_PER_PAGE

    with db_connector.connect().cursor(named_tuple=True, buffered=True) as cursor:
        cursor.execute("SELECT COUNT(*) as count FROM books")
        total_books = cursor.fetchone().count

        cursor.execute("SELECT b.*, c.filename, "
                       "(SELECT GROUP_CONCAT(g.name SEPARATOR ', ') FROM book_genres bg "
                       "JOIN genres g ON bg.genre_id = g.id WHERE bg.book_id = b.id) AS genres, "
                       "(SELECT ROUND(AVG(r.rating), 1) FROM reviews r WHERE r.book_id = b.id) AS avg_rating, "
                       "(SELECT COUNT(r.id) FROM reviews r WHERE r.book_id = b.id) AS review_count "
                       "FROM books b LEFT JOIN covers c ON b.cover_id = c.id ORDER BY b.year DESC LIMIT %s OFFSET %s",
                       (MAX_PER_PAGE, offset))
        books = cursor.fetchall()

    books = [book._asdict() for book in books]

    page_count = math.ceil(total_books / MAX_PER_PAGE)
    pages = range(1, page_count + 1)

    return render_template('books/index.html', books=books, pages=pages, page=page, page_count=page_count)


@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    fields = ['title', 'author', 'description', 'year', 'publisher', 'pages']
    if current_user.is_admin():
        if request.method == 'POST':
            book_data = {field: request.form.get(field) for field in fields}
            selected_genres = request.form.getlist('genres[]')
            cover_image = request.files.get('cover_image')
            cover_id = save_cover(cover_image)
            book_data['description'] = bleach.clean(book_data['description'])

            with db_connector.connect().cursor(named_tuple=True, buffered=True) as cursor:
                cursor.execute("INSERT INTO books (title, description, year, publisher, author, pages, cover_id) VALUES"
                               " (%(title)s, %(description)s, %(year)s, %(publisher)s, %(author)s, %(pages)s, %(cover_id)s)",
                               {**book_data, 'cover_id': cover_id})
                book_id = cursor.lastrowid
                db_connector.connect().commit()

            insert_book_genres(book_id, selected_genres)

            flash("Книга успешно добавлена!", "success")
            return redirect(url_for('books.index'))

    with db_connector.connect().cursor(named_tuple=True, buffered=True) as cursor:
        cursor.execute("SELECT * FROM genres")
        genres = cursor.fetchall()

    return render_template('books/create.html', genres=genres, book_data={"genres": []})


@bp.route('/edit/<int:book_id>', methods=['GET', 'POST'])
@login_required
def edit(book_id):
    if current_user.is_admin() or current_user.is_moderator():
        if request.method == 'POST':
            fields = ['title', 'author', 'description', 'year', 'publisher', 'pages']
            book_data = {field: request.form.get(field) for field in fields}
            selected_genres = request.form.getlist('genres[]')
            book_data['description'] = bleach.clean(book_data['description'])

            with db_connector.connect().cursor(named_tuple=True, buffered=True) as cursor:
                cursor.execute("UPDATE books SET title = %(title)s, description = %(description)s, year = %(year)s, "
                               "publisher = %(publisher)s, author = %(author)s, pages = %(pages)s WHERE id = %(book_id)s",
                               {**book_data, 'book_id': book_id})
                db_connector.connect().commit()

            insert_book_genres(book_id, selected_genres)

            flash("Книга успешно обновлена!", "success")
            return redirect(url_for('books.view', book_id=book_id))

    with db_connector.connect().cursor(named_tuple=True, buffered=True) as cursor:
        cursor.execute("SELECT * FROM books WHERE id = %s", (book_id,))
        book = cursor.fetchone()

        if not book:
            flash("Книга не найдена.", "error")
            return redirect(url_for('books.index'))

        cursor.execute("SELECT * FROM genres")
        genres = cursor.fetchall()

        cursor.execute("SELECT genre_id FROM book_genres WHERE book_id = %s", (book_id,))
        selected_genres = cursor.fetchall()

    book_dict = book._asdict()
    book_dict["selected_genres"] = [id[0] for id in selected_genres]
    return render_template('books/edit.html', genres=genres, book_data=book_dict, book_id=book_id)


@bp.route('/view/<int:book_id>')
@login_required
def view(book_id):
    with db_connector.connect().cursor(named_tuple=True, buffered=True) as cursor:
        cursor.execute("SELECT b.*, c.filename, "
                       "(SELECT GROUP_CONCAT(g.name SEPARATOR ', ') FROM book_genres bg "
                       "JOIN genres g ON bg.genre_id = g.id WHERE bg.book_id = b.id) AS genres, "
                       "(SELECT ROUND(AVG(r.rating), 1) FROM reviews r WHERE r.book_id = b.id) AS avg_rating, "
                       "(SELECT COUNT(r.id) FROM reviews r WHERE r.book_id = b.id) AS review_count "
                       "FROM books b LEFT JOIN covers c ON b.cover_id = c.id WHERE b.id = %s;", [book_id])
        book = cursor.fetchone()

        cursor.execute("SELECT rating, review_text, date_added, "
                       "CONCAT(first_name, "
                       "IF(middle_name IS NOT NULL, CONCAT(' ', middle_name), ''), ' ', last_name) AS full_name "
                       "FROM reviews "
                       "LEFT JOIN users on reviews.user_id = users.id "
                       "WHERE reviews.book_id = %s", (book_id,))
        reviews = cursor.fetchall()

        cursor.execute("SELECT * FROM reviews WHERE user_id = %s and book_id = %s", (current_user.id, book_id))
        is_commented = cursor.fetchone() is not None

    if not book:
        flash("Книга не найдена", "warning")
        return redirect(url_for('books.index'))

    book_dict = book._asdict()

    return render_template('books/view.html', book=book_dict, reviews=reviews, is_commented=is_commented)


@bp.route('/delete/<int:book_id>', methods=['POST', 'GET'])
@login_required
def delete(book_id):
    page = str(request.args.get('page', 1))
    if current_user.is_admin():
        if request.method == 'POST':
            connection = db_connector.connect()
            try:
                with connection.cursor(named_tuple=True, buffered=True) as cursor:
                    cursor.execute("SELECT * FROM books WHERE id = %s", (book_id,))
                    book = cursor.fetchone()
                    cursor.execute("SELECT filename FROM covers WHERE id = %s", (book.cover_id,))
                    cover = cursor.fetchone()
                    cursor.execute("SELECT COUNT(*) as count FROM books where cover_id = %s", (book.cover_id,))
                    cover_count = cursor.fetchone()

                    if not book:
                        flash("Книга не найдена", "warning")
                        return redirect(url_for('books.index'))

                    cursor.execute("DELETE FROM books WHERE id = %s", (book_id,))
                    cursor.execute("DELETE FROM book_genres WHERE book_id = %s", (book_id,))
                    cursor.execute("DELETE FROM reviews WHERE book_id = %s", (book_id,))
                    if cover_count.count == 1:
                        cursor.execute("DELETE FROM covers WHERE id = %s", (book.cover_id,))
                        try:
                            os.remove(os.path.join('static/images', cover.filename))
                        except FileNotFoundError:
                            pass

                    connection.commit()
                    flash('Книга успешно удалена', 'success')
                    # print(url_for('static', filename=f'images/{cover.filename}'))

            except Exception as e:
                print(e)
                flash("Произошла ошибка при удалении книги.", "danger")
                connection.rollback()
            return redirect(url_for('books.index') + '?page=' + page)
    return render_template("books/delete.html", book_id=book_id, page=page)


@bp.route('/add_review/<int:book_id>', methods=['POST', 'GET'])
@login_required
def add_review(book_id):
    if request.method == 'POST':
        try:
            connection = db_connector.connect()
            with connection.cursor(named_tuple=True, buffered=True) as cursor:
                cursor.execute("INSERT INTO reviews(book_id, user_id, rating, review_text, date_added) "
                               "VALUES (%s, %s, %s, %s, %s)",
                               (book_id, current_user.id, request.form['rating'],
                                request.form['review_text'], datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
            connection.commit()
            flash('Рецензия успешно добавлена!', 'success')
        except Exception as e:
            print(e)
            flash("Произошла ошибка при написании рецензии.", "danger")
            connection.rollback()
        finally:
            connection.close()

        return redirect(url_for('books.view', book_id=book_id))

    return render_template("books/add_review.html", book_id=book_id)
