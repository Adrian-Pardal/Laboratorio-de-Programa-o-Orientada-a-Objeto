class Pessoa:

    def __init__(self):

        self.nome = ""
        self.idade = 0
        self.altura = 0
        self.peso = 0
        #self.estado = "vivo"

    def setNome (self , nome):
        self.nome = nome


    def getNome (self):

        return self.nome    

    def setIdade (self , idade):
        self.idade = idade

    def getIdade (self):

        return self.idade

    def setAltura (self , altura):
        self.altura = altura 

    def getAltura (self):

        return self.altura

    def setPeso (self , peso):
        self.peso = peso

    def getPeso (self):

        return self.peso 

    def setEstado (self , estado):
        self.estado = estado

    def getEstado (self):

        return self.estado
    



    #def vivo (self):

        #self.estado = "vivo"

    #def morto (self):

        #self.estado = "morto"    

    def envelhecer (self):
      #if self.estado == "vivo":  
        self.idade += 1

    def crescer (self , quantidadeCentimetros):
     #if self.estado == "vivo":  
       if self.idade < 21: 
         self.altura += quantidadeCentimetros

    def ganharPeso (self , quantidadeQuilos):
      #if self.estado == "vivo":  
         self.peso +=  quantidadeQuilos 

    def perderPeso (self , quantidadeQuilos):
      #if self.estado == "vivo": 
       if quantidadeQuilos  <= self.peso :
         self.peso -= quantidadeQuilos     
        
pessoa = Pessoa()

pessoa.setIdade(15)
pessoa.setAltura(175)
pessoa.setPeso(70)

pessoa.vivo()

pessoa.ganharPeso(10)
print(pessoa.getPeso())

pessoa.envelhecer()
pessoa.envelhecer()
pessoa.envelhecer()
pessoa.envelhecer()
pessoa.envelhecer()


print(pessoa.getIdade())

pessoa.crescer(20)
pessoa.crescer(10)
print(pessoa.getAltura())

pessoa.envelhecer()
pessoa.envelhecer()
print(pessoa.getIdade())

pessoa.crescer(15)
print(pessoa.getAltura())

pessoa.ganharPeso(50)
print(pessoa.getPeso())

pessoa.perderPeso(130)
print(pessoa.getPeso())


