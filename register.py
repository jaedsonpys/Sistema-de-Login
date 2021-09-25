from flask import Blueprint, make_response, render_template, request
from flask.helpers import url_for
from werkzeug.utils import redirect
from utils.token import Token

from mysql import MySQL

register = Blueprint('register', __name__)

@register.route('/register', methods=['POST', 'GET'])
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

# Criar rotas de cadastro.
