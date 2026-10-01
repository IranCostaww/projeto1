from fastapi import FastAPI #importando o servidor da biblioteca
from fastapi.responses import FileResponse #na parte responses, pegando a  função FileResponse

app = FastAPI() #guardar servidor na var app

@app.get("/") #quando o navegador pedir sobre a pagina inicial, execute:
def pagina_inicial():
    return FileResponse("index.html") #devolve o index.html

@app.get("/login")
def pagina_login():
    return FileResponse("login.html")

@app.get("/style.css")
def css_login():
    return FileResponse("style.css")