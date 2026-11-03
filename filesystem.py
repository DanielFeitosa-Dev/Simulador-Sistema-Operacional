class Arquivo:
    def __init__(self, nome, conteudo=""):
        self.nome = nome
        self.conteudo = conteudo

    def obter_tamanho(self):
        return len(self.conteudo.encode("utf-8"))   # definir como utf-8 vai facilitar as contas de tamanho no futuro

class Diretorio:
    def __init__(self, nome):
        self.nome = nome    # o self serve para referenciar os atributos de cada classe 
        self.filhos = {}    # forma de criar um dicionario

    def adicionar(self, elemento):
        if elemento.nome in self.filhos:
            raise ValueError("já existe um elemento com esse nome")

        self.filhos[elemento.nome] = elemento

    def buscar(self, caminho):
        # o caminho deve começar com /
        if not caminho.startswith("/"):
            raise ValueError("O caminho deve ser absoluto")

        # o caminho / representa o diretorio raiz
        if caminho == "/":
            return self

        partes = caminho.strip("/").split("/")

        atual = self

        for parte in partes: 
            if not isinstance(atual, Diretorio):
                raise ValueError(
                    f"'{atual.nome}' não é um diretório"
                )
            
            if parte not in atual.filhos:
                raise FileNotFoundError(
                    f"elemento '{parte}' não encontrado"
                )
            atual = atual.filhos[parte]

        return atual

class SistemaArquivos:
    def __init__(self):
        self.raiz = Diretorio("/")  # define o "/" como raiz
        self.diretorio_atual = self.raiz    # define o diretorio atual como a raiz 


    # Usado para navegação geral
    def buscar(self, caminho):
        if caminho.startswith("/"):
            atual = self.raiz
        else:
            atual = self.diretorio_atual
        if caminho == "/" or caminho == "":
            return atual

        partes = caminho.strip("/").split("/")

        for parte in partes:
            if not isinstance(atual, Diretorio):
                raise ValueError(
                    f"'{atual.nome}' não é um diretório"
                )
            if parte not in atual.filhos:
                raise FileNotFoundError(
                    f"Elemento '{parte}' não encontrado"
                )
            atual = atual.filhos[parte]

        return atual

    def mudar_diretorio(self, caminho):
        destino = self.buscar(caminho)

        if not isinstance(destino, Diretorio):
            raise ValueError(
                f"'{destino.nome}' não é um diretório"
            )

        self.diretorio_atual = destino

    def criar_diretorio(self, caminho):
        if caminho == "/" or caminho == "":
            raise ValueError("Caminho inválido para criação de diretório.")

        caminho = caminho.rstrip("/")

        partes = caminho.rsplit("/", 1)

        if len(partes) == 1:
            nome = partes[0]
            pai = self.diretorio_atual
        else:
            caminho_pai = partes[0]
            nome = partes[1]

            if caminho_pai == "":
                caminho_pai = "/"

            pai = self.buscar(caminho_pai)

        if not isinstance(pai, Diretorio):
            raise ValueError("O local de destino não é um diretório.")

        novo_diretorio = Diretorio(nome)
        pai.adicionar(novo_diretorio)



