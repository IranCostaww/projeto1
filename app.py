from fastapi import FastAPI,Form #importando o servidor da biblioteca/ o form é utilizado para ler formularios HTML
from fastapi.responses import FileResponse #na parte responses, pegando a  função FileResponse
from anlist import buscar_manga


app = FastAPI() #guardar servidor na var app

@app.get("/") #quando o navegador pedir sobre a pagina inicial, execute:
def pagina_inicial():
    return FileResponse("index.html") #devolve o index.html

#consulta de login
@app.get("/login")
def pagina_login():
    return FileResponse("login.html")

#aqui vamos receber do formulario do HTML através do Form,
@app.post("/cadastro")
def cadastro(usuario: str = Form(...), senha: str = Form(...)):
    return{"usuario_digitado": usuario,"senha_digitada": senha}
    

#passando o style ao url
@app.get("/style.css")
def css_login():
    return FileResponse("style.css")

#consulta de busca
@app.get("/buscar")
def rota_buscar(titulo: str):
    manga = buscar_manga(titulo)
    if manga is None:
        return {"erro": "Mangá não encontrado"}
    return {
        "titulo": manga["title"]["romaji"],
        "capitulos": manga["chapters"],
    }
