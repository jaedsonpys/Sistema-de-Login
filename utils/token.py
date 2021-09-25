import jwt
import os
from datetime import datetime, timedelta

class Token:
    def __init__(self, token=None):
        self.key = os.environ.get('JWT_KEY')
        self.token = token

    def check_token(self):
        if self.token is None:
            raise ValueError('Token não foi passado como argumento em __init__.')

        try:
            user_data = jwt.decode(self.token, self.key, algorithms=['HS256'])
        except:
            return False # Token Inválido
        else:
            return user_data # Retornando o conteúdo do Token

    def generate_token(self, name, email):
        try:
            user_token = jwt.encode(
                payload={'exp': datetime.utcnow() + timedelta(minutes=5), 'iat': datetime.utcnow(), 'name': name, 'email': email},
                key=self.key,
                algorithm='HS256'
            )
        except:
            return False
        else:
            self.token = user_token # Atualizando token
            return user_token