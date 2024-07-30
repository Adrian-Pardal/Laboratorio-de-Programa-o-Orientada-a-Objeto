class Retangulo :

    def __init__(self):
        self.comprimento = 0.0
        self.largura = 0.0
        self.LadoA = 0.0
        self.LadoB = 0.0
        self.perimetro = 0.0
        self.area = 0.0

    def setComprimento (self , comprimento):
        self.comprimento = comprimento
        self.LadoA = self.comprimento

    def getComprimento (self):

        return self.comprimento

    def setLargura (self , largura):
        self.largura = largura
        self.LadoB = self.largura

    def getLargura (self):

        return self.largura

    def setLadoA (self , ladoA):
        self.LadoA = ladoA

    def getLadoA(self):

        return self.LadoA

    def setLadoB (self , ladoB):
        self.LadoB = ladoB

    def getLadoB (self):

        return self.LadoB

    def setPerimetro(self , perimetro):
        self.perimetro = perimetro

    def getPerimetro (self):

        return self.perimetro

    def setArea (self , area):
        self.area = area

    def getArea (self):

        return self.area



    #metodos

    def mudarValorLados (self , comprimento , largura):
        self.comprimento = comprimento
        self.largura = largura 

    def retornarValorPrimeiroDados(self):
        self.LadoA
        self.LadoB
    def CalcularPerimetro(self):

        self.perimetro = 2 * (self.LadoA + self.LadoB)

    def CalcularArea(self):
        self.area = self.LadoA * self.LadoB


    def MostrarDados (self):

        return print(f"Primeiro Registro do Comprimento = {self.comprimento} cm\nPrimeiro Registro de Largura = {self.largura} cm\nComprimento Atual = {self.LadoA} cm\nLargura Atual = {self.largura} cm\nArea do Retangulo = {self.area}\nPerimetro do Retangulo = {self.perimetro}")

retangulo = Retangulo()

retangulo.setComprimento(15)
print(retangulo.getComprimento())

retangulo.setLargura(5)
print(retangulo.getLargura())

print("_________________________________________")

retangulo.mudarValorLados(10,3)
print(retangulo.getComprimento())
print(retangulo.getLargura())

retangulo.retornarValorPrimeiroDados()
print(retangulo.getLadoA())
print(retangulo.getLadoB())

retangulo.CalcularPerimetro()
print(retangulo.getPerimetro())

retangulo.CalcularArea()

print("_________________________________________")
retangulo.MostrarDados()
print("_________________________________________")
