# **Sistema de login**
![BADGE](https://img.shields.io/badge/Made%20with-Python-blue?style=for-the-badge&logo=Python)
![BADGE](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![BADGE](https://img.shields.io/badge/MySQL-00000F?style=for-the-badge&logo=mysql&logoColor=white)

Uma página de login onde você pode criar sua conta, sair e deletar. Feito usando a linguagem Python e o micro framework web Flask!

# **Sobre**

A finalidade desse projeto é mostrar como funciona um sistema de autenticação de usuários, tendo como foco a segurança e privacidade do mesmo.

## **🚀 Tecnologias**

Aqui estão as tecnologias usadas:

### **Servidor**

Flask foi o micro framework usado para retornar páginas e gerenciar as rotas do site.

### **Banco de dados**

O MySQL foi o banco de dados escolhido para guardar as informações do usuário, desde nome, email e senha.

### **Segurança**

Para proteger a senha do usuário, utilizamos a biblioteca [Bcrypt no Python](https://pypi.org/project/bcrypt/), garantido que a conta esteja segura. Em autenticação, para gerar o token, nós escolhemos
o [JWT(JSON Web Token) no Python](https://pyjwt.readthedocs.io/en/stable/).

# **🔧 Faça seu teste**

Para rodar este projeto em sua máquina, é preciso ter instalado o Python3, já o resto das dependências, deixamos em um ***requirements.txt***!

1. Baixe o projeto clicando [aqui](https://github.com/jaedsonpys/Sistema-de-Login/archive/refs/heads/master.zip).

2. Abra seu terminal e entre na pasta raíz do projeto.

3. Digite o comando: **pip install -r requirements.txt**.

4. Mais uma vez, digite o comando: **python3 app.py**.

5. Pronto! 🎉
