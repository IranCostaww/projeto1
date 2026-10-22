from fastapi import FastAPI,Form #importando o servidor da biblioteca/ o form é utilizado para ler formularios HTML
from fastapi.responses import FileResponse, JSONResponse #na parte responses, pegando a  função FileResponse
from anlist import buscar_manga
from seguranca import gerar_senha, verificar_senha 
from banco import conectar 
from psycopg.errors import UniqueViolation
from fastapi import Request

app = FastAPI() #guardar servidor na var app

@app.get("/") #quando o navegador pedir sobre a pagina inicial, execute:
def pagina_inicial():
    return FileResponse("index.html") #devolve o index.html

#entregar
@app.get("/teste-cookie")
def teste_cookie():
    resposta = JSONResponse({"mensagem": "cookie enviado"})
    resposta.set_cookie("visitante", "iran")
    return resposta


#ler o cookie
@app.get("/ler-cookie")
def ler_cookie(request: Request):
    return {"cookie": request.cookies.get("visitante")}

#login get
@app.get("/login")
def pagina_login():
    return FileResponse("login.html")

@app.post("/login")
def login(usuario: str = Form(...), senha: str = Form(...)):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "SELECT senha_hash FROM usuarios WHERE nome = %s",
        (usuario,),      
    )
    linha = cursor.fetchone()
    cursor.close()
    conexao.close()

    #se alguma informação de errado
    if linha is None:
        return {"erro": "Usuario ou senha incorretos"}

    hash_guardado = linha[0]

    if verificar_senha(senha, hash_guardado):
        return {"mensagem": "Login efeutado"}
    return {"erro": "Usuario ou senha incorretos"}


#cadastro de usuário post
@app.post("/cadastro")
def cadastro(usuario: str = Form(...), senha: str = Form(...)):
    hash_da_senha = gerar_senha(senha)

    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute(
            "INSERT INTO usuarios (nome, senha_hash) VALUES (%s, %s)",
            (usuario, hash_da_senha),
        )
        conexao.commit()
    except UniqueViolation:
        conexao.rollback()
        cursor.close()
        conexao.close()
        return {"erro": "Esse nome de usuário já existe"}
    
    return {"mensagem": "Conta criada"}
    

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
