def mensagem(nome):
    return f"Olá, {nome}! Seja bem-vindo ao sistema."

def despedida(nome):
    return f"Até mais, {nome}!"

if __name__ == "__main__":
    nome = "Usuário"
    print(mensagem(nome))
    print(despedida(nome))