from flask import Flask, make_response, render_template, request, redirect, url_for

from auth import auth
from profile import profile
from utils.token import Token

app = Flask(__name__, template_folder='templates', static_folder='public')
app.register_blueprint(auth)
app.register_blueprint(profile)

@app.route('/')
def home():
    user_token = request.cookies.get('auth')

    if user_token is None:
        return make_response(redirect(url_for('auth.login_func')))

    token_validate = Token(user_token).check_token()

    if not token_validate:
        return make_response(redirect(url_for('auth.login_func')))

    return make_response(render_template('index.html', user_data=token_validate), 200)

if __name__ == '__main__':
    app.run(debug=True, port=3000, host='0.0.0.0')