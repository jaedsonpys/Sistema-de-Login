from werkzeug.wrappers import response
from utils.token import Token
from flask import Blueprint, request, make_response, redirect, url_for
from flask.templating import render_template
from mysql import MySQL

login = Blueprint('login', __name__)

@login.route('/login', methods=['POST', 'GET'])
def login_func():
    if request.method == 'POST':
        user_data = request.form.to_dict()

        if 'email' not in user_data or 'password' not in user_data:
            return render_template('login.html', empty=True)

        login_user = MySQL().login_user(user_data['email'], user_data['password'])
        if login_user is False:
            return make_response(render_template('login.html', invalid=True), 401)

        new_token = Token().generate_token(login_user['name'], login_user['email'])
        response = make_response(redirect(url_for('home')))
        response.set_cookie('auth', new_token)

        return response

    user_token = request.cookies.get('auth')

    if user_token is None:
        return render_template('login.html')

    validate_token = Token(user_token).check_token()
    if validate_token is not False:
        return make_response(redirect(url_for('home')))

    return render_template('login.html')