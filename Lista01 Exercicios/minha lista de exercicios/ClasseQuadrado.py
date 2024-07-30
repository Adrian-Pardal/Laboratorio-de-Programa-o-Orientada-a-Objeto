class Quadrado:

    def __init__(self):
        self.tamanhoLados = 0.0
        self.ladosPrincipal = 0.0
        self.area = 0.0
    
    def setTamanhoLados (self , lados ):
      self.tamanhoLados = lados
      self.ladosPrincipal = self.tamanhoLados
        

    def getTamanhoLados (self):

        return self.tamanhoLados
       
    def setLadosPrincipal (self, lados):
        self.ladosPrincipal = lados

    def getLadosPrincipal (self):
        
        return self.ladosPrincipal
       
    def setArea (self , area):
        self.area = area

    def getArea(self):

        return self.area

    #metodos

    def mudarValorLados (self , lados) :
        self.tamanhoLados = lados

    def retornarValorLados (self):
        self.ladosPrincipal
        
    def calcularArea (self):
        self.area = self.tamanhoLados ** 2
     
    def MostrarDados (self):

        return print(f"Primeiro Registro do Lados = {self.ladosPrincipal} cm\nLados Atual = {self.tamanhoLados} cm\nCalculo Area QUadrado = {self.area} m²")




quadrado = Quadrado()

quadrado.setTamanhoLados(18)
print(quadrado.getTamanhoLados())

quadrado.mudarValorLados(5)
print(quadrado.getTamanhoLados())

quadrado.mudarValorLados(112.5)
print(quadrado.getTamanhoLados())

quadrado.mudarValorLados(18)
print(quadrado.getTamanhoLados())

quadrado.calcularArea()
print(quadrado.getArea())

quadrado.retornarValorLados()
print(quadrado.getLadosPrincipal())

print("______________________________________________")
quadrado.MostrarDados()
print("______________________________________________")

