import pymysql
import os
from utils.hash import Hash
from datetime import datetime

os.environ.setdefault('DATABASE_USER', 'root')
os.environ.setdefault('DATABASE_PASSWORD', 'Firlastdatabase@2021')

connect_mysql = pymysql.connect(
    user=os.environ.get('DATABASE_USER'),
    password=os.environ.get('DATABASE_PASSWORD'),
    autocommit=True,
    charset='utf8',
)

sql = connect_mysql.cursor()

# Configurando Banco de Dados
sql.execute('create database if not exists LoginSystem;')
sql.execute('use LoginSystem;')

table_config = 'id int primary key auto_increment, name varchar(50), email varchar(50), password varchar(150), create_at datetime'
sql.execute(f'create table if not exists usuarios({table_config})')

class MySQL:
    def __init__(self):
        connect_mysql.ping()

    def insert_user(self, name, email, password):
        user_exists = self.user_exists(email)

        if user_exists:
            return False # Já existe um usuário com esse email

        hashed_password = Hash().create_hash(password)
        create_at = datetime.utcnow()

        sql.execute('insert into usuarios(name, email, password, create_at) values(%s,%s,%s,%s)', (name, email, hashed_password, create_at, ))
        return True

    def login_user(self, email, password):
        sql.execute('select name, email, password from usuarios where email = %s', (email,))
        user_data = sql.fetchone()

        if user_data is None:
            return False

        verify_hash = Hash().check_hash(password, user_data[2])

        if not verify_hash:
            return False

        return {'name': user_data[0],'email': user_data[1]}

    def delete_user(self, email):
        sql.execute('delete from usuarios where email = %s', (email, ))
        return True

    def user_exists(self, email):
        sql.execute('select id from usuarios where email = %s', (email,))
        data = sql.fetchone()

        if not data:
            return False # Não existe nenhum usuário com esse email

        return True # Já existe um usuário com esse email