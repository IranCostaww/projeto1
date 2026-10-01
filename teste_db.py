import psycopg
from getpass import getpass

senha = getpass("Senha do banco: ")

conexao = psycopg.connect(
    host="localhost",
    port=5432,
    dbname="caroco",
    user="app",
    password=senha,
)

cursor = conexao.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id SERIAL PRIMARY KEY,
        nome VARCHAR(50) UNIQUE NOT NULL,
        senha_hash VARCHAR(255) NOT NULL
    );
""")
conexao.commit()

cursor.close()
conexao.close()