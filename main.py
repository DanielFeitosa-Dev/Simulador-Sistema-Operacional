from filesystem import Arquivo, Diretorio, Disco, SistemaArquivos, RequisicaoES, Disco

def main(): 
#    print("===========================================")
#    print(" SIMULADOR DE SISTEMA DE ARQUIVOS")
#    print("===========================================")
#    print("Sistema iniciado com sucesso")

#    home = Diretorio("home")
#    arquivo = Arquivo("notas.txt", "estudando SO")
#    home.adicionar(arquivo)

#    print("Diretório:", home.nome)
#    print("Arquivo:", arquivo.nome)
#    print("Conteúdo:", arquivo.conteudo)
#    print("Tamanho:", arquivo.obter_tamanho(), "bytes")
#    print("\nElementos dentro de home:")
#    for nome in home.filhos:
#     print("-", nome)

    def exibir_arvore(diretorio, nivel = 0):
        for elemento in diretorio.filhos.values():

            if isinstance(elemento, Diretorio):
                print("    " * nivel + "📁 " + elemento.nome + "/")
                exibir_arvore(elemento, nivel + 1)

            else:
                print("    " * nivel + "📄 " + elemento.nome)



    # # Criando o diretório raiz
    # raiz = Diretorio("/")

    # # Criando os diretórios
    # sistema = Diretorio("sistema")
    # logs = Diretorio("logs")

    # # Criando um arquivo
    # arquivo = Arquivo(
    #     "app.log",
    #     "Registro de eventos do sistema"
    # )

    # # Construindo a árvore
    # raiz.adicionar(sistema)
    # sistema.adicionar(logs)
    # logs.adicionar(arquivo)

    # # Exibindo a árvore
    # print("[ÁRVORE DO SISTEMA DE ARQUIVOS]")
    # print("/")

    # exibir_arvore(raiz)

    # # testando a busca de caminhos
    # print("\n[TESTE DE BUSCA]")

    # encontrado = raiz.buscar("/sistema/logs")

    # print("Diretório encontrado:", encontrado.nome)

    # # testando a busca de arquivos dentro do diretorio
    # arquivo_encontrado = raiz.buscar("/sistema/logs/app.log")

    # print("Arquivo encontrado:", arquivo_encontrado.nome)
    # print("Tamanho:", arquivo_encontrado.obter_tamanho(), "bytes")



    # # criando sistema de arquivos 
    # sistema_arquivos = SistemaArquivos()
    # raiz = sistema_arquivos.raiz

    # # criando os diretorios 
    # sistema = Diretorio("sistema")
    # logs = Diretorio("logs")

    # # criando o arquivo 
    # arquivo = Arquivo(
    #     "app.log", 
    #     "Registro de eventos do sistema"
    # )

    #  # Construindo a árvore
    # raiz.adicionar(sistema)
    # sistema.adicionar(logs)
    # logs.adicionar(arquivo)

    # # Exibindo a árvore
    # print("[ÁRVORE DO SISTEMA DE ARQUIVOS]")
    # print("/")
    # exibir_arvore(raiz)

    # # Teste de caminho absoluto
    # print("\n[TESTE DE CAMINHO ABSOLUTO]")
    # encontrado = sistema_arquivos.buscar("/sistema/logs")
    # print("Diretório encontrado:", encontrado.nome)

    # # Mudando o diretório atual
    # sistema_arquivos.mudar_diretorio("/sistema")

    # print("\nDiretório atual:",
    #       sistema_arquivos.diretorio_atual.nome)

    # # Teste de caminho relativo
    # print("\n[TESTE DE CAMINHO RELATIVO]")
    # encontrado = sistema_arquivos.buscar("logs/app.log")

    # print("Arquivo encontrado:", encontrado.nome)
    # print("Tamanho:",
    #       encontrado.obter_tamanho(), "bytes")

    # sistema_arquivos = SistemaArquivos()

    # # Criando diretórios usando caminhos absolutos
    # sistema_arquivos.criar_diretorio("/sistema")
    # sistema_arquivos.criar_diretorio("/sistema/logs")

    # print("[ÁRVORE DO SISTEMA DE ARQUIVOS]")
    # print("/")
    # exibir_arvore(sistema_arquivos.raiz)


    # testando criaçao por caminhos relativos 
  
    # sistema_arquivos = SistemaArquivos()

    # # Criando diretórios por caminhos absolutos
    # sistema_arquivos.criar_diretorio("/sistema")
    # sistema_arquivos.criar_diretorio("/sistema/logs")

    # # Entrando no diretório sistema
    # sistema_arquivos.mudar_diretorio("/sistema")

    # # Criando diretório usando caminho relativo
    # sistema_arquivos.criar_diretorio("documentos")
    # sistema_arquivos.criar_diretorio("documentos/trabalhos")

    # sistema_arquivos.mudar_diretorio("documentos")
    # sistema_arquivos.criar_diretorio("projetos")

    # try:
    #     sistema_arquivos.criar_diretorio("nao existe/novo")
    # except FileNotFoundError as erro:
    #     print("erro esperado1:", erro)

    #     arquivo = Arquivo("relatorio.txt")
    #     sistema_arquivos.diretorio_atual.adicionar(arquivo)

    # try:
    #     sistema_arquivos.criar_diretorio("relatorio.txt/novo")  # Tentativa de criar um diretório dentro de um arquivo
    # except ValueError as erro:
    #     print("erro esperado:", erro)

    # try:
    #     sistema_arquivos.criar_diretorio("/sistema/logs")  # Tentativa de criar um diretório que já existe  
    # except ValueError as erro:
    #     print("erro esperado3:", erro)

    # print("[ÁRVORE DO SISTEMA DE ARQUIVOS]")
    # print("/")
    # exibir_arvore(sistema_arquivos.raiz)



#     sistema_arquivos = SistemaArquivos()

#     # =================================
#     # 1. CRIANDO DIRETÓRIOS
#     # =================================

#     # Caminhos absolutos
#     sistema_arquivos.criar_diretorio("/sistema")
#     sistema_arquivos.criar_diretorio("/sistema/logs")

#     # Entrando em /sistema
#     sistema_arquivos.mudar_diretorio("/sistema")

#     # Caminhos relativos
#     sistema_arquivos.criar_diretorio("documentos")
#     sistema_arquivos.criar_diretorio("documentos/trabalhos")

#     # Entrando em documentos
#     sistema_arquivos.mudar_diretorio("documentos")

#     sistema_arquivos.criar_diretorio("imagens")

#     # =================================
#     # 2. CRIANDO ARQUIVOS
#     # =================================

#     # Arquivo no diretório atual (/sistema/documentos)
#     sistema_arquivos.criar_arquivo("leia-me.txt")

#     # Arquivo com conteúdo em caminho relativo
#     sistema_arquivos.criar_arquivo(
#         "relatorio.txt",
#         "Meu primeiro arquivo no simulador."
#     )

#     # Arquivo em caminho absoluto
#     sistema_arquivos.criar_arquivo(
#         "/sistema/logs/erro.txt",
#         "Registro de erro do sistema."
#     )

#     # Arquivo dentro de um subdiretório relativo
#     sistema_arquivos.criar_arquivo(
#         "trabalhos/atividade.txt",
#         "Atividade de Sistemas Operacionais."
#     )

#     # =================================
#     # 3. EXIBINDO A ÁRVORE
#     # =================================

#     print("[ÁRVORE DO SISTEMA DE ARQUIVOS]")
#     print("/")
#     exibir_arvore(sistema_arquivos.raiz)


#     # =================================
#     # 4. TESTANDO A CRIAÇÃO DE ARQUIVOS
#     # =================================

# # Teste 1: Verificar o conteúdo e o tamanho
#     arquivo = sistema_arquivos.buscar("relatorio.txt")

#     print("\n[TESTE 1 - CONTEÚDO E TAMANHO]")
#     print("Conteúdo:", arquivo.conteudo)
#     print("Tamanho:", arquivo.obter_tamanho(), "bytes")

# # Teste 2: Verificar arquivo vazio
#     arquivo_vazio = sistema_arquivos.buscar("leia-me.txt")

#     print("\n[TESTE 2 - ARQUIVO VAZIO]")
#     print("Conteúdo:", repr(arquivo_vazio.conteudo))
#     print("Tamanho:", arquivo_vazio.obter_tamanho(), "bytes")


#     # =================================
# # 5. TESTANDO SITUAÇÕES DE ERRO
# # =================================

#     print("\n[TESTE 3 - ARQUIVO DUPLICADO]")

#     try:
#         sistema_arquivos.criar_arquivo("relatorio.txt")
#     except ValueError as erro:
#         print("Erro esperado:", erro)


#     print("\n[TESTE 4 - DIRETÓRIO INEXISTENTE]")

#     try:
#         sistema_arquivos.criar_arquivo(
#             "nao_existe/arquivo.txt"
#         )
#     except FileNotFoundError as erro:
#         print("Erro esperado:", erro)


#     print("\n[TESTE 5 - DESTINO NÃO É DIRETÓRIO]")

#     try:
#         sistema_arquivos.criar_arquivo(
#             "relatorio.txt/arquivo.txt"
#         )
#     except ValueError as erro:
#         print("Erro esperado:", erro)


    # requisicao = RequisicaoES(
    #     "ESCRITA",
    #     "/sistema/logs/app.log",
    #     5000
    # )

    # print("[TESTE DE REQUISIÇÃO DE E/S]")

    # print("Tipo:", requisicao.tipo)
    # print("Arquivo:", requisicao.caminho)
    # print("Tamanho:", requisicao.tamanho, "bytes")
    # print("Blocos necessários:", requisicao.quantidade_blocos)


    disco = Disco()

    requisicao1 = RequisicaoES(
        "ESCRITA",
        "/sistema/logs/app.log",
        5000
    )

    requisicao2 = RequisicaoES(
        "LEITURA",
        "/sistema/logs/app.log",
        5000
    )

    disco.executar_requisicao(requisicao1)
    disco.executar_requisicao(requisicao2)

    print("\n[HISTÓRICO DE OPERAÇÕES]")
    print("Total de requisições:", len(disco.historico))


if __name__ == "__main__":
    main()

