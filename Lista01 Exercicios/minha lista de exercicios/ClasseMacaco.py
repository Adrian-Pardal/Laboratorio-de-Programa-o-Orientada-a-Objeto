class Macaco:
    def __init__(self): 
        self.nome = ""
        self.estomago = 0

    def setNome(self,nome):
        self.nome = nome

    def getNome(self):

        return self.nome

    def setEstomago(self , estomago):
        self.estomago = estomago

    def getEstomago(self):

        return self.estomago 

    def comer(self, comer):

        self.estomago += comer

    def verEstomago(self):

        return print(f"Estomago : {self.estomago }")
    
    def digerir(self):
        self.estomago -= (self.estomago)/2



macaco = Macaco()

macaco.setNome("mongo")
print(macaco.getNome())

macaco.setEstomago(0)
print(macaco.getEstomago())

macaco.comer(100)
macaco.verEstomago()

macaco.digerir()
macaco.verEstomago()

macaco.digerir()
macaco.verEstomago()