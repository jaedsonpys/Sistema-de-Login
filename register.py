from flask import Blueprint, request, make_response, render_template
from mysql import MySQL

login = Blueprint('login', __name__)

@login.route('/register', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user_data = request.form.get()

# Criar rotas de cadastro.