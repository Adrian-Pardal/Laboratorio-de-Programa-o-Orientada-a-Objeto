class Bola:

    def __init__(self):
        self.cor = ""
        self.circunferencia = 0.0
        self.material = ""
        self.raio = 0.0
        self.diametro = 0.0
        self.area = 0.0

    def setCor (self , cor):
        self.cor = cor

    def getCor (self):

        return self.cor


    def setMaterial (self , material):
        self.material = material

    def getMaterial (self):

        return self.material
    

    def setCircunferencia (self , circunferencia) :
        self.circunferencia = circunferencia

    def getCircunferencia (self):

        return self.circunferencia
    
    def setRaio (self , raio):
        self.raio = raio

    def getRaio (self):

        return self.raio 

    def setArea (self , area):
        self.area = area

    def getArea (self):

        return self.area       
    
    def setDiametro(self , diametro):
        self.diametro = diametro

    def getDiametro(self):

        return self.diametro    




    def trocarCor(self , mudarCor):

        self.cor = mudarCor


    def trocarMaterial (self , mudarMaterial):

        self.material = mudarMaterial

    def cacularArea(self):
        self.area = 3.14 * (self.raio ** 2)

        return self.area
    
    def calcularCircunferencia(self):
        self.circunferencia = 2 * 3.14 * self.raio
    
        return self.circunferencia
    
    def calcularDiametro(self):
        self.diametro = self.raio * 2

        return self.diametro
    
    def MostrarDados (self):
    
     return print(f"Cor = {self.cor}\nMaterial = {self.material}\nRaio = {self.raio}\nDiametro = {self.diametro}\nArea = {self.area}\nCircunferencia = {self.circunferencia}")    


bola = Bola()


bola.setCor("Red")
print(bola.getCor())

bola.setMaterial("plastico")

bola.trocarCor("Blue")
bola.MostrarDados()
bola.trocarMaterial("Ferro")
bola.trocarCor("Green")
bola.setRaio(56)
bola.calcularDiametro()
bola.cacularArea()
bola.calcularCircunferencia()




print("__________________________")
bola.MostrarDados()
print("__________________________")