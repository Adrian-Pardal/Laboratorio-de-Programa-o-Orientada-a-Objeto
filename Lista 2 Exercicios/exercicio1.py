class Funcionario:
    def __init__(self , departamento):
        self.nome = ""
        if departamento is None:
            print("Erro")
            exit()
        else:
            self.departamento = departamento

    def setNome(self , nome):
        self.nome = nome

    def getNome(self):
        return self.nome
    
    def setDepartamento(self , departamento):
        if departamento == None:
            return "departamento não existe"
        else:
            self.departamento = departamento

    def getDepartamento(self):
        self.departamento 

    def getNomeDepartamento(self):
        if self.departamento == None:
            return print("Invalido")
        else:
            return self.departamento.getNome()

class Departamento:
    def __init__(self):
        self.nome = ""
        self.mentor = None

    def setNome(self , nome):
        self.nome = nome

    def getNome(self):
        return self.nome
    

    def setMentor(self , nome):
        self.mentor = nome

    def getMentor(self):
        return self.mentor


    def getNomeMentor(self):
        return self.mentor.getNome()

class Mentor:
    def __init__(self):
        self.nome = ""

    def setNome(self , nome):
        self.nome = nome

    def getNome(self):
        return self.nome

departamento = Departamento()
#departamento.setNome("RH")


funcionario = Funcionario(departamento)
funcionario.setNome("Fernando")


gestor = Mentor()
gestor.setNome('Roger')
departamento.setMentor(gestor)


print(departamento.getNomeMentor())
print(funcionario.getNomeDepartamento())