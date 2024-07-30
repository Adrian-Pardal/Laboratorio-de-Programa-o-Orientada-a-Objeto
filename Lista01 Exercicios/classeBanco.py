class ContaBancaria:

    def __init__(self):
        self.titular = ""
        self.numero_da_conta = 0
        self.saldo = 0.0
        self.estado = "Ativa"

    def setTitular(self , titular):
        self.titular = titular

    def getTitular(self):

        return self.titular   

    def setNumeroDaConta(self ,numero_da_conta):
        self.numero_da_conta = numero_da_conta

    def getNumeroDaConta(self):

            return self.numero_da_conta 

    def setSaldo(self , saldo):
         if self.estado == "Ativa": 
            self.saldo = saldo         

    def getSaldo(self):

         return self.saldo     

    def setEstado(self, estado):
        if estado == "Ativa" or estado == "inativa":
            self.estado = estado

    def getEStado(self):

        return self.estado    

    def depositar(self , quantidade):
         if self.estado == "Ativa": 
            if quantidade > 0:
                self.saldo += quantidade

    def sacar(self , quantidade):
       if self.estado == "Ativa":
        if quantidade > 0:
            if quantidade <= self.saldo: 
                self.saldo -= quantidade 

    def ativar(self):
        self.estado = "Ativa"

    def inativar(self):
        self.estado = "Inativa"

contabancaria = ContaBancaria() 

contabancaria.setTitular("Jonas")
print(contabancaria.getTitular())

contabancaria.setNumeroDaConta(1234)
print(contabancaria.getNumeroDaConta())

contabancaria.setSaldo(0)
print(contabancaria.getSaldo())

contabancaria.depositar(400)
print(contabancaria.getSaldo())

contabancaria.sacar(0)
print(contabancaria.getSaldo())

contabancaria.inativar()
contabancaria.depositar(400)

contabancaria.ativar()
contabancaria.sacar(30)
print(contabancaria.getSaldo())

