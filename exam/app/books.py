import asyncio
import hashlib
import logging
import math
import os

from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename

from app import db_connector

bp = Blueprint('books', __name__, url_prefix='/books')

MAX_PER_PAGE = 8

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_books_with_pagination(offset):
    with db_connector.connect().cursor(named_tuple=True, buffered=True) as cursor:
        cursor.execute("SELECT b.*, c.filename, GROUP_CONCAT(g.name SEPARATOR ', ') as genres,  "
                       "AVG(r.rating) as avg_rating, COUNT(r.id) as review_count FROM books b "
                       "LEFT JOIN covers c ON b.cover_id = c.id "
                       "LEFT JOIN book_genres bg ON b.id = bg.book_id "
                       "LEFT JOIN genres g ON bg.genre_id = g.id "
                       "LEFT JOIN reviews r ON b.id = r.book_id "
                       "GROUP BY b.id ORDER BY b.year DESC LIMIT %s OFFSET %s", (MAX_PER_PAGE, offset))
        return cursor.fetchall()


# def save_cover(background_image):
#     if background_image:
#         # Generate unique filename using MD5 hash
#         md5_hash = hashlib.md5(background_image.read()).hexdigest()
#         file_extension = background_image.filename.rsplit('.', 1)[-1].lower()  # Get file extension
#         filename = f"{md5_hash}.{file_extension}"
#
#         # Save the file to disk
#         file_path = os.path.join('media/images', filename)
#         background_image.seek(0)  # Reset file pointer
#         background_image.save(file_path)
#
#         return filename  # Return the filename saved
#
#     return None


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
            # Handle any exceptions, e.g., log the error
            print(f"Error saving cover: {e}")
            db_connector.connect().rollback()  # Rollback the transaction on error

    return None


def insert_book_genres(book_id, genres_selected):
    data = [(book_id, genre_id) for genre_id in genres_selected]

    with db_connector.connect().cursor(named_tuple=True, buffered=True) as cursor:
        insert_statement = "INSERT INTO book_genres (book_id, genre_id) VALUES (%s, %s)"
        cursor.executemany(insert_statement, data)
        db_connector.connect().commit()


#
# async def add_background_images(books):
#     for book in books:
#         filename = book['filename']
#         if filename:
#             file_data = await s3_client.get_file(filename)
#             if file_data:
#                 book['background_image'] = file_data


@bp.route('/')
@login_required
def index():
    page = int(request.args.get('page', 1))
    offset = (page - 1) * MAX_PER_PAGE

    with db_connector.connect().cursor(named_tuple=True, buffered=True) as cursor:
        cursor.execute("SELECT COUNT(*) as count FROM books")
        total_books = cursor.fetchone().count

    books = get_books_with_pagination(offset)
    logger.info(f'Fetched: {len(books)} books')
    books = [book._asdict() for book in books]

    # print(books)

    # asyncio.run(add_background_images(books))

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
            genres_selected = request.form.getlist('genre')
            background_image = request.files.get('background_image')
            # print(background_image.mimetype)
            cover_id = save_cover(background_image)

            print(cover_id)

            with db_connector.connect().cursor(named_tuple=True, buffered=True) as cursor:
                cursor.execute(
                    "INSERT INTO books (title, description, year, publisher, author, pages, cover_id) VALUES "
                    "(%(title)s, %(description)s, %(year)s, %(publisher)s, %(author)s, %(pages)s, %(cover_id)s)",
                    {**book_data, 'cover_id': cover_id})
                book_id = cursor.lastrowid
                db_connector.connect().commit()

            insert_book_genres(book_id, genres_selected)

            flash("Книга успешно добавлена!", "success")
            return redirect(url_for('books.index'))

    with db_connector.connect().cursor(named_tuple=True, buffered=True) as cursor:
        cursor.execute("SELECT * FROM genres")
        genres = cursor.fetchall()

    return render_template('books/create.html', genres=genres, book_data={"genres": []})


@bp.route('/update/<int:book_id>', methods=['GET', 'POST'])
@login_required
def update(book_id):
    if current_user.is_admin() or current_user.is_moderator():
        if request.method == 'POST':
            fields = ['title', 'author', 'description', 'year', 'publisher', 'pages']
            book_data = {field: request.form.get(field) for field in fields}
            genres_selected = request.form.getlist('genre')

            with db_connector.connect().cursor(named_tuple=True, buffered=True) as cursor:
                cursor.execute("UPDATE books SET title = %(title)s, description = %(description)s, year = %(year)s, "
                               "publisher = %(publisher)s, author = %(author)s, pages = %(pages)s WHERE id = %(book_id)s",
                               {**book_data, 'book_id': book_id})
                cursor.execute("DELETE FROM book_genres WHERE book_id = %s", (book_id,))
                db_connector.connect().commit()

            insert_book_genres(book_id, genres_selected)

            flash("Книга успешно обновлена!", "success")
            return redirect(url_for('books.index'))

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
    return render_template('books/update.html', genres=genres, book_data=book_dict, book_id=book_id)


@bp.route('/view/<int:book_id>')
@login_required
def view(book_id):
    with db_connector.connect().cursor(named_tuple=True, buffered=True) as cursor:
        cursor.execute("SELECT b.*, c.filename, GROUP_CONCAT(g.name SEPARATOR ', ') as genres, "
                       "AVG(r.rating) as avg_rating, COUNT(r.id) as review_count FROM "
                       "books b LEFT JOIN covers c ON b.cover_id = c.id "
                       "LEFT JOIN book_genres bg ON b.id = bg.book_id "
                       "LEFT JOIN genres g ON bg.genre_id = g.id "
                       "LEFT JOIN reviews r ON b.id = r.book_id "
                       "WHERE b.id = %s GROUP BY b.id", [book_id])
        book = cursor.fetchone()

    if not book:
        flash("Книга не найдена", "warning")
        return redirect(url_for('books.index'))

    book_dict = book._asdict()

    # filename = book_dict.get('filename')
    # if filename:
    #     file_data = asyncio.run(s3_client.get_file(filename))
    #     if file_data:
    #         book_dict['background_image'] = file_data

    return render_template('books/view.html', book=book_dict)


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
