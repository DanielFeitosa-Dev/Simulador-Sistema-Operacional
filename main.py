from filesystem import Arquivo, Diretorio, SistemaArquivos

def main(): 
   print("===========================================")
   print(" SIMULADOR DE SISTEMA DE ARQUIVOS")
   print("===========================================")
   print("Sistema iniciado com sucesso")

   home = Diretorio("home")
   arquivo = Arquivo("notas.txt", "estudando SO")
   home.adicionar(arquivo)

   print("Diretório:", home.nome)
   print("Arquivo:", arquivo.nome)
   print("Conteúdo:", arquivo.conteudo)
   print("Tamanho:", arquivo.obter_tamanho(), "bytes")
   print("\nElementos dentro de home:")
   for nome in home.filhos:
    print("-", nome)

    def exibir_arvore(diretorio, nivel = 0):
        for elemento in diretorio.filhos.values():

            if isinstance(elemento, Diretorio):
                print("    " * nivel + "📁 " + elemento.nome + "/")
                exibir_arvore(elemento, nivel + 1)

            else:
                print("    " * nivel + "📄 " + elemento.nome)



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

    # testando a busca de caminhos
    print("\n[TESTE DE BUSCA]")

    encontrado = raiz.buscar("/sistema/logs")

    print("Diretório encontrado:", encontrado.nome)

    # testando a busca de arquivos dentro do diretorio
    arquivo_encontrado = raiz.buscar("/sistema/logs/app.log")

    print("Arquivo encontrado:", arquivo_encontrado.nome)
    print("Tamanho:", arquivo_encontrado.obter_tamanho(), "bytes")



    # criando sistema de arquivos 
    sistema_arquivos = SistemaArquivos()
    raiz = sistema_arquivos.raiz

    # criando os diretorios 
    sistema = Diretorio("sistema")
    logs = Diretorio("logs")

    # criando o arquivo 
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

    # Teste de caminho absoluto
    print("\n[TESTE DE CAMINHO ABSOLUTO]")
    encontrado = sistema_arquivos.buscar("/sistema/logs")
    print("Diretório encontrado:", encontrado.nome)

    # Mudando o diretório atual
    sistema_arquivos.mudar_diretorio("/sistema")

    print("\nDiretório atual:",
          sistema_arquivos.diretorio_atual.nome)

    # Teste de caminho relativo
    print("\n[TESTE DE CAMINHO RELATIVO]")
    encontrado = sistema_arquivos.buscar("logs/app.log")

    print("Arquivo encontrado:", encontrado.nome)
    print("Tamanho:",
          encontrado.obter_tamanho(), "bytes")


if __name__ == "__main__":
    main()

