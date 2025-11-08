from django.db import connection
from werkzeug.security import generate_password_hash, check_password_hash


def criar_usuario(nome, email, telefone, data, multa, senha):
    senha_hash = generate_password_hash(senha)
    with connection.cursor() as cursor:
        cursor.execute("""
            INSERT INTO Usuarios (Nome_usuario, Email, Numero_telefone, Data_inscricao, Multa_atual, Senha)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, [nome, email, telefone, data, multa, senha_hash])


def autenticar_usuario(email, senha):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Usuarios WHERE Email = %s", [email])
        user = cursor.fetchone()

        if not user:
            return None

        senha_hash = user[6]

        if check_password_hash(senha_hash, senha):
            return user

        return None
