import requests #basicamente estou importando request para esse arquivo


titulo = input("Qual manga você quer buscar? ")

#pede ao anlist
def buscar_manga(titulo):
    consulta = """ 
    query ($busca: String){
        Media(search: $busca, type: MANGA){
            id
            title { romaji }
            chapters
        }
    }
    """
    #reposta guarda tudo que o anlist devolve
    resposta = requests.post(
        "https://graphql.anilist.co",
        json={"query": consulta, "variables": {"busca": titulo}},
    )
    dados = resposta.json()
    manga = dados["data"]["Media"]
    return manga

manga = buscar_manga(titulo)

if manga is None:
    print("Desculpe, manga não encontrado")
else:
    print(manga["title"]["romaji"])
    print(manga["chapters"])