class Carro():

    def __init__(self):

        self.marca = ""
        self.modelo = ""
        self.ano = 0
        self.cor = ""
        self.velocidade_atual = 0
        self.estado = "desligado"

    def  setMarca(self , marca):
        
        self.marca = marca

    def getMarca(self):

        return self.marca
    
    def setModelo(self , modelo):
        
        self.modelo = modelo

    def getModelo(self):

        return self.modelo
    
    def  setAno(self , ano):
        
        self.ano = ano

    def getAno(self):

        return self.ano
    
    def  setCor(self , cor):
        
        self.cor = cor

    def getCor(self):

        return self.cor
    
    def setVelocidadeAtual(self , velocidade_atual):
        if self.estado == "ligado":
            if velocidade_atual >= 0:
             self.velocidade_atual = velocidade_atual

    def getVelocidadeAtual(self):
        
            return self.velocidade_atual
    
    def setEstado(self , estado):
        
        self.estado = estado

    def getEstado(self):

        return self.estado
    



    def desligar(self):
        self.estado = "desligado"
        self.velocidade_atual = 0

    def ligar(self):

        self.estado = "ligado"    

    def Acelerar(self , quantidade):
        if self.estado == "ligado":
            self.Acelerar = quantidade
            self.velocidade_atual += quantidade

    def Frear(self , quantidade):
        if self.estado == "ligado":
            self.Frear = quantidade
            if self.Frear <= 0 :
                self.velocidade_atual = self.velocidade_atual
            if self.Frear >= 0 :    
                self.velocidade_atual = self.velocidade_atual - quantidade
            if self.velocidade_atual <0:
             self.velocidade_atual = 0


carro = Carro()
print("------------------------")

carro.setMarca("BMW")
print(carro.getMarca())

print("------------------------")

print("------------------------")

carro.setModelo("X1")
print(carro.getModelo())

print("------------------------")

print("------------------------")

carro.setAno(2008)
print(carro.getAno())

print("------------------------")

carro.setCor("Azul-Marinho")
print(carro.getCor())

print("------------------------")



print(carro.getEstado())

carro.ligar()
print(carro.getEstado())

carro.desligar()
print(carro.getEstado())

carro.ligar()
print(carro.getEstado())


carro.setVelocidadeAtual(50)

carro.Acelerar(50)
print(carro.getVelocidadeAtual())

carro.Frear(-50)
print(carro.getVelocidadeAtual())