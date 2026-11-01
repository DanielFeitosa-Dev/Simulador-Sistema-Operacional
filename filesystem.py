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


# ainda falta realizar o teste no main, começar por lá