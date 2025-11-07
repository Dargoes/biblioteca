from django.db import connection
from werkzeug.security import generate_password_hash, check_password_hash


# ---------- CRIAR USUÁRIO ----------
def criar_usuario(nome, email, telefone, data, multa, senha):
    """
    Cria um novo usuário na tabela Usuarios com a senha criptografada.
    """
    senha_hash = generate_password_hash(senha)
    with connection.cursor() as cursor:
        cursor.execute("""
            INSERT INTO Usuarios (Nome_usuario, Email, Numero_telefone, Data_inscricao, Multa_atual, Senha)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, [nome, email, telefone, data, multa, senha_hash])


# ---------- AUTENTICAR USUÁRIO ----------
def autenticar_usuario(email, senha):
    """
    Valida o login de um usuário comparando a senha informada com a senha criptografada no banco.
    Retorna o usuário (tupla) se for válido, ou None se for inválido.
    """
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Usuarios WHERE Email = %s", [email])
        user = cursor.fetchone()

        if not user:
            return None

        # Índice da senha — certifique-se de que a coluna "Senha" é a 7ª (posição 6)
        senha_hash = user[6]

        if check_password_hash(senha_hash, senha):
            return user

        return None
