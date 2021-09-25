from flask import Blueprint, request, make_response, render_template, redirect, url_for
from utils.token import Token
from mysql import MySQL

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['POST', 'GET'])
def register_func():
    if request.method == 'POST':
        user_data = request.form.to_dict()

        if 'email' not in user_data or 'password' not in user_data or 'email' not in user_data:
            return make_response(render_template('register.html', empty=True), 400)

        user_register = MySQL().insert_user(user_data['name'], user_data['email'], user_data['password'])

        if user_register is False:
            return make_response(render_template('register.html', emailInUse=True), 400)
        elif user_register:
            new_token = Token().generate_token(user_data['name'], user_data['email'])
            response = make_response(redirect(url_for('home')))
            response.set_cookie('auth', new_token)
            return response

    return render_template('register.html')

@auth.route('/login', methods=['POST', 'GET'])
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

@auth.route('/logout')
def logout_func():
    auth = request.cookies.get('auth')

    if auth is None:
        return make_response(redirect(url_for('auth.login_func')))

    validate_token = Token(auth).check_token()

    if validate_token is False:
        return make_response(redirect(url_for('auth.login_func')))

    response = make_response(redirect(url_for('auth.login_func')))
    response.delete_cookie('auth')

    return response