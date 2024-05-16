from flask import Flask, render_template, request, make_response

app = Flask(__name__)
application = app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/headers')
def headers():
    return render_template('infoTable.html', header='Заголовки', data=request.headers)


@app.route('/cookies')
def cookies():
    response = make_response(
        render_template('infoTable.html', header='cookies', data=request.cookies)
    )
    response.set_cookie("cookie1", "cookie1")
    return response


@app.route('/url_params')
def url_params():
    return render_template('infoTable.html', header='url_params', data=request.args)


@app.route('/form', methods=['GET', 'POST'])
def form():
    return render_template('form.html')


@app.route('/phone', methods=['GET', 'POST'])
def phone():
    if request.method == 'GET':
        return render_template('phone.html')

    to_replace_array = {'+', ' ', '(', ')', '-', '.'}

    original_phone = request.form.get('phone_number')
    original_phone_without_symbols = ""

    for i in original_phone:
        if i not in to_replace_array:
            original_phone_without_symbols += i

    errors = []

    if not original_phone_without_symbols.isdigit():
        errors.append('В номере телефона встречаются недопустимые символы.')
    elif len(original_phone_without_symbols) not in [10, 11]:
        errors.append('Неверное количество цифр.')

    if not errors:
        formatted_phone = f'8-{original_phone_without_symbols[-10:-7]}-{original_phone_without_symbols[-7:-4]}-{original_phone_without_symbols[-4:-2]}-{original_phone_without_symbols[-2:]}'
    else:
        formatted_phone = original_phone

    return render_template('phone.html', phone_number=formatted_phone, errors=errors)


if __name__ == '__main__':
    app.run(debug=True)
