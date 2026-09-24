import unicodedata
from difflib import get_close_matches

livros = []

def normalizar(texto):
    texto = unicodedata.normalize("NFD", texto)

    texto = "".join(
        caractere
        for caractere in texto
        if unicodedata.category(caractere) != "Mn"
    )
    return texto.lower()

def procurar_livro():
    busca = input("Digite o nome do livro ou autor: ")

    busca_normalizada = normalizar(busca)

    encontrados = []

    # Procura pelo nome ou autor
    for livro in livros:
        nome = normalizar(livro["nome"])
        autor = normalizar(livro["autor"])

        if busca_normalizada in nome or busca_normalizada in autor:
            encontrados.append(livro)

    # Se não encontrou exatamente, procura nomes parecidos
    if not encontrados:
        nomes = [normalizar(livro["nome"]) for livro in livros]

        sugestoes = get_close_matches(
            busca_normalizada,
            nomes,
            n=3,
            cutoff=0.4
        )

        for sugestao in sugestoes:
            indice = nomes.index(sugestao)
            encontrados.append(livros[indice])

    if encontrados:
        print("\nLivros encontrados:")

        for livro in encontrados:
            print(f"- {livro['nome']} | {livro['autor']}")

    else:
        print("\nNenhum livro encontrado.")

def adicionar_livro():
    nome = input("Nome do livro: ")
    autor = input("Autor: ")

    livros.append({
        "nome": nome,
        "autor": autor
    })
    print("Livro adicionado!")

def remover_livro():
    nome = input("Digite o nome do livro que deseja remover: ")

    nome_normalizado = normalizar(nome)

    for livro in livros:
        if normalizar(livro["nome"]) == nome_normalizado:
            livros.remove(livro)
            print("Livro removido!")
            return
    print("Livro não encontrado.")

while True:
    print("\n===== BIBLIOTECA =====")
    print("1 - Procurar livro")
    print("2 - Adicionar livro")
    print("3 - Remover livro")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        procurar_livro()

    elif opcao == "2":
        adicionar_livro()

    elif opcao == "3":
        remover_livro()

    elif opcao == "4":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")
#colocando esse texto para teste de branch
#Novo comentario da branch