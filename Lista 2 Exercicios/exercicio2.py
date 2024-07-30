class Cliente:
    def __init__(self):
        self.nome = ""


    def setNome(self , nome):
        self.nome = nome
    
    def getNome(self):
        return self.nome
    


class Endereco:

    def __init__(self):
        self.logadouro = ""
        self.numero =""
        self.complemento = ""
        self.bairro = ""

    def setLogadouro(self , logadouro):
        self.logadouro = logadouro

    def getLogadouro(self):
        return self.logadouro
    
    def setNumero(self , numero ):
        self.numero = numero

    def getNumero(self):
        return self.numero
    
    def setComplemento(self , complemento):
        self.complemneto = complemento

    def getComplemento(self):
        return self.complemento
    
    def setBairro(self , bairro):
        self.bairro = bairro

    def getBairro(self):
        return self.bairro

class Cidade:
    def __init__(self):
        self.nome = ""

    def setNome(self , nome):
        self.nome = nome
    def getNome(self):
        return self.nome
    


class Estado:
    def __init__(self):
        self.nome = ""

    def setNome(self , nome):
        self.nome = nome
    def getNome(self):
        return self.nome
    




class Pais:
    def __init__(self):
        self.nome = ""

    def setNome(self , nome):
        self.nome = nome
    def getNome(self):
        return self.nome














cliente = Cliente()
cliente.setNome("Valdecir")
#print(cliente.getNome())

endereco = Endereco()
endereco.setLogadouro("Rua Diney Santos")
endereco.setBairro("Marcelo Budez")
endereco.setNumero("78")
endereco.setComplemento("casa")