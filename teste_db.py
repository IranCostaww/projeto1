import psycopg
from getpass import getpass
from pwdlib import PasswordHash

senha = getpass("Senha do banco: ")

conexao = psycopg.connect(
    host="localhost",
    port=5432,
    dbname="caroco",
    user="app",
    password=senha,
)

#tabelas dos usuarios
cursor = conexao.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id SERIAL PRIMARY KEY,
        nome VARCHAR(50) UNIQUE NOT NULL,
        senha_hash VARCHAR(255) NOT NULL
    );
""")

#Tabela dos mangas sql
cursor.execute("""
    CREATE TABLE IF NOT EXISTS mangas (
        id SERIAL PRIMARY KEY,
        titulo_manga VARCHAR(50) UNIQUE NOT NULL,
        capitulos INTEGER NOT NULL DEFAULT 0,
        manga_autor VARCHAR(50) NOT NULL,
        capitulo_lidos INTEGER NOT NULL DEFAULT 0
    );
""")

conexao.commit()

cursor.close()
conexao.close()

#testando o hash da bilbioteca pwdlib.

password_hash = PasswordHash.recommended()

# aplicando hash ao passward

hashed = password_hash.hash("senha1207")

# verificando a senha:

is_valid = password_hash.verify("senha1208", hashed)  #verdade
is_valid = password_hash.verify("nao_e", hashed) # falso