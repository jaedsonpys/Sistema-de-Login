from mysql import MySQL
from flask import Blueprint, request, make_response, redirect, url_for, render_template
from utils.token import Token

profile = Blueprint('profile', __name__)

@profile.route('/profile')
def profile_func():
    auth = request.cookies.get('auth')

    if auth is None:
        return make_response(redirect(url_for('auth.login_func')))

    validate_token = Token(auth).check_token()

    if validate_token is False:
        return make_response(redirect(url_for('auth.login_func')))

    return make_response(render_template('profile.html', user_data=validate_token))

@profile.route('/delete')
def delete_func():
    auth = request.cookies.get('auth')

    if auth is None:
        return make_response(redirect(url_for('auth.login_func')))

    validate_token = Token(auth).check_token()

    if validate_token is False:
        return make_response(redirect(url_for('auth.login_func')))

    MySQL().delete_user(validate_token['email'])
    response = make_response(redirect(url_for('auth.login_func')))
    response.delete_cookie('auth')

    return response