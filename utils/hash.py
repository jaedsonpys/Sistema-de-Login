import bcrypt
import os

class Hash:
    def __init__(self):
        self.key = os.environ.get('BCRYPT_KEY')

    def check_hash(self, password_attempted, original_password):
        '''
        Checa se o hash da senha tentada pelo usuário é válido ou não, passe os argumentos:

        password_attempted: A senha que foi tentada pelo usuário.
        original_password: A senha que foi guardada no banco de dados em formato de hash.
        '''

        hash_check = bcrypt.checkpw(bytes(password_attempted), bytes(original_password, 'utf8'))
        return hash_check

    def create_hash(self, original_password):
        '''
        Gera um novo hash de senha para o usuário e o retorna, informe apenas a senha original.

        :param original_password: str
        '''

        hashed_password = bcrypt.hashpw(bytes(original_password, 'utf8'), bcrypt.gensalt())
        return hashed_password.decode()