class Funcionario:

    def __init__(self):
        self.nome = ""
        self.cargo = ""
        self.salario = 0.0
        self.departamento = ""

    def setNome(self , nome ):
        self.nome = nome

    def getNome(self):

        return self.nome

    def setCargo(self , cargo):
        self.cargo = cargo

    def getCargo(self):

        return self.cargo

    def setSalario (self , salario):

        self.salario = salario

    def getSalario (self):

        return self.salario


    def setDepartamento (self , departamento):

        self.departamento = departamento

    def getDepartamento(self):

        return self.departamento

    def receberAumento(self , percentual):
       if percentual > 0: 
        self.salario =  self.salario * ( 1 + ( percentual / 100))

    def mudarDepartamento (self , novoDepartamento):
        self.departamento = novoDepartamento  

    def exibirDados(self):
           
        return print(f"Nome = {self.nome}\nCargo = {self.cargo}\nSalario = {self.salario:.2f}\nDepartamento = {self.departamento}" )                    
    
funcionario = Funcionario() 
funcionario.setNome("godes")
funcionario.setCargo("Atendente")
funcionario.setSalario(10380)
funcionario.setDepartamento("ADM")

funcionario.receberAumento(35)

funcionario.mudarDepartamento("Financeiro")
funcionario.exibirDados()