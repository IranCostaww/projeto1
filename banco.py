import os
import psycopg

def conectar():
    return psycopg.connect(
        host="localhost",
        port=5432,
        dbname="caroco",
        user="app",
        password=os.environ["DB_SENHA"],
    )