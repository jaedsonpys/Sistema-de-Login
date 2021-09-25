import pymysql
import os
from utils.hash import Hash
from datetime import datetime

connect_mysql = pymysql.connect(
    user=os.environ.get('DATABASE_USER'),
    password=os.os.environ.get('DATABASE_PASSWORD'),
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
        sql.ping()

    def insert_user(self, name, email, password):
        user_exists = self.user_exists(email)

        if user_exists:
            return False # Já existe um usuário com esse email

        hashed_password = Hash().create_hash(password)
        create_at = datetime.utcnow()

        sql.execute('insert into usuarios(name, email, password, create_at) values(%s,%s,%s,%s)', (name, email, hashed_password, create_at, ))
        return True

    def user_exists(self, email):
        query = sql.execute('select id from usuarios where email = %s', (email,))
        data = query.fetchone()

        if not data:
            return False # Não existe nenhum usuário com esse email

        return True # Já existe um usuário com esse email