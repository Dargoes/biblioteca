from django.apps import AppConfig
from django.db import connection, OperationalError


class BibliotecaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'biblioteca'

    def ready(self):
        try:
            self.criar_tabelas_mysql()
        except OperationalError:
            pass

    def criar_tabelas_mysql(self):
        tabelas = [
            """
            CREATE TABLE IF NOT EXISTS Autores (
                ID_autor INT AUTO_INCREMENT PRIMARY KEY,
                Nome_autor VARCHAR(255) NOT NULL,
                Nacionalidade VARCHAR(255),
                Data_nascimento DATE,
                Biografia TEXT
            ) ENGINE=InnoDB;
            """,
            """
            CREATE TABLE IF NOT EXISTS Generos (
                ID_genero INT AUTO_INCREMENT PRIMARY KEY,
                Nome_genero VARCHAR(255) NOT NULL
            ) ENGINE=InnoDB;
            """,
            """
            CREATE TABLE IF NOT EXISTS Editoras (
                ID_editora INT AUTO_INCREMENT PRIMARY KEY,
                Nome_editora VARCHAR(255) NOT NULL,
                Endereco_editora TEXT
            ) ENGINE=InnoDB;
            """,
            """
            CREATE TABLE IF NOT EXISTS Livros (
                ID_livro INT AUTO_INCREMENT PRIMARY KEY,
                Titulo VARCHAR(255) NOT NULL,
                Autor_id INT,
                ISBN VARCHAR(13) NOT NULL,
                Ano_publicacao INT,
                Genero_id INT,
                Editora_id INT,
                Quantidade_disponivel INT,
                Resumo TEXT,
                FOREIGN KEY (Autor_id) REFERENCES Autores(ID_autor) ON DELETE CASCADE,
                FOREIGN KEY (Genero_id) REFERENCES Generos(ID_genero) ON DELETE CASCADE,
                FOREIGN KEY (Editora_id) REFERENCES Editoras(ID_editora) ON DELETE CASCADE
            ) ENGINE=InnoDB;
            """,
            """
            CREATE TABLE IF NOT EXISTS Usuarios (
                ID_usuario INT AUTO_INCREMENT PRIMARY KEY,
                Nome_usuario VARCHAR(255) NOT NULL,
                Email VARCHAR(255),
                Numero_telefone VARCHAR(15),
                Data_inscricao DATE,
                Multa_atual DECIMAL(10, 2),
                Senha VARCHAR(255) NOT NULL
            ) ENGINE=InnoDB;
            """,
            """
            CREATE TABLE IF NOT EXISTS Emprestimos (
                ID_emprestimo INT AUTO_INCREMENT PRIMARY KEY,
                Usuario_id INT,
                Livro_id INT,
                Data_emprestimo DATE,
                Data_devolucao_prevista DATE,
                Data_devolucao_real DATE,
                Status_emprestimo ENUM('pendente', 'devolvido', 'atrasado'),
                FOREIGN KEY (Usuario_id) REFERENCES Usuarios(ID_usuario) ON DELETE CASCADE,
                FOREIGN KEY (Livro_id) REFERENCES Livros(ID_livro) ON DELETE CASCADE
            ) ENGINE=InnoDB;
            """
        ]

        with connection.cursor() as cursor:
            for comando in tabelas:
                cursor.execute(comando)