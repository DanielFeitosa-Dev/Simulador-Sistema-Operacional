from filesystem import Arquivo, Diretorio

# def main(): 
#    print("===========================================")
#    print(" SIMULADOR DE SISTEMA DE ARQUIVOS")
#    print("===========================================")
#    print("Sistema iniciado com sucesso")

# def main():
#     home = Diretorio("home")

#     arquivo = Arquivo("notas.txt", "estudando SO")

#     home.adicionar(arquivo)

#     print("Diretório:", home.nome)
#     print("Arquivo:", arquivo.nome)
#     print("Conteúdo:", arquivo.conteudo)
#     print("Tamanho:", arquivo.obter_tamanho(), "bytes")

#     print("\nElementos dentro de home:")
#     for nome in home.filhos:
#         print("-", nome)

def exibir_arvore(diretorio, nivel = 0):
    for elemento in diretorio.filhos.values():

        if isinstance(elemento, Diretorio):
            print("    " * nivel + "📁 " + elemento.nome + "/")
            exibir_arvore(elemento, nivel + 1)

        else:
            print("    " * nivel + "📄 " + elemento.nome)

def main():
    # Criando o diretório raiz
    raiz = Diretorio("/")

    # Criando os diretórios
    sistema = Diretorio("sistema")
    logs = Diretorio("logs")

    # Criando um arquivo
    arquivo = Arquivo(
        "app.log",
        "Registro de eventos do sistema"
    )

    # Construindo a árvore
    raiz.adicionar(sistema)
    sistema.adicionar(logs)
    logs.adicionar(arquivo)

    # Exibindo a árvore
    print("[ÁRVORE DO SISTEMA DE ARQUIVOS]")
    print("/")

    exibir_arvore(raiz)

if __name__ == "__main__":
    main()

