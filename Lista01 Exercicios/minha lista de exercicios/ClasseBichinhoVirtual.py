class BichinhoVirtual :

    def __init__(self):
        self.nome = ""
        self.fome = 0
        self.saude = 0
        self.idade = 0
        self.DadosPrincipais = 0
        self.primerioDadoNome = ""
        self.humor = 0.0
    def setNome (self , nome):
        self.nome = nome
        self.primerioDadoNome = self.nome
    def getNome (self):

        return self.nome

    def setFome (self , fome):
        self.fome = fome
        self.DadosPrincipais = self.fome
    def getFome (self):

        return self.fome

    def setSaude (self , saude):
        self.saude = saude
        self.DadosPrincipais = self.saude
    def getSaude (self):

        return self.saude

    def setIdade (self , idade):
        self.idade = idade
        self.DadosPrincipais = self.idade
    def getIdade (self):

        return self.idade 

    def setHumor(self):
        self.humor 

    def getHumor(self):

        return self.humor    


    #   METODOS   #  

    def alterarNome (self , nome):
        self.nome = nome

    def alterarFome (self , fome):
        self.fome = fome

    def alterarSaude (self , saude):
        self.saude = saude  

    def alterarIdade (self , idade):
        self.idade = idade

    def Humor(self):
        self.humor = 10 * ((self.fome + self.saude) / 100) 
        return self.humor
    
    def mostrardados(self):

        return print(f" {self.primerioDadoNome} {self.DadosPrincipais} ")
bichinho = BichinhoVirtual()

print("__________________________________")
print("Primeiros dados")
print("__________________________________")
bichinho.setNome("JUJUBA")
print(bichinho.getNome())
bichinho.setFome(100)
print(bichinho.getFome())
bichinho.setSaude(100)
print(bichinho.getSaude())
bichinho.setIdade(1)
print(bichinho.getIdade())

bichinho.Humor()
print(f"|Humor : {bichinho.getHumor()}|")
print("__________________________________")

print("||||||||||||||||||||||||||||||||||")

print("__________________________________")
print("Dados alterados")
print("__________________________________")
bichinho.alterarNome("POU")
print(bichinho.getNome())
bichinho.alterarFome(10)
print(bichinho.getFome())
bichinho.alterarSaude(10)
print(bichinho.getSaude())
bichinho.alterarIdade(10)
print(bichinho.getIdade())
print("__________________________________")
print("Humor Do Bicihnho Virtual")
bichinho.Humor()
print(f"|Humor : {bichinho.getHumor()}|")
print("__________________________________")