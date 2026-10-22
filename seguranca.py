from pwdlib import PasswordHash

#criando o has
hasher = PasswordHash.recommended()


def gerar_senha(senha: str) -> str:
    hash_guardado = hasher.hash(senha)
    return hash_guardado


def verificar_senha(senha: str, hash_guardado: str) -> bool:
  return hasher.verify(senha, hash_guardado)

    




