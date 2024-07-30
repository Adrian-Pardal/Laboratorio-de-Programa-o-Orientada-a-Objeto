class Estado():
    def __init__(self):
        self.sigla = ""
        self.siglaCurso = ""
    
    def setSigla(self , sigla):
        self.sigla = sigla

    def getSigla(self):
        return self.sigla
    
    def setSiglaCurso(self , sigla):
        self.siglaCurso = sigla

    def getSiglaCurso(self):
        return self.siglaCurso
class Cidade():
    def __init__(self):
        self.nome = None
        self.estado = None
        self.estadoCurso = None
    def setNomeCidade(self , nome):
        self.nome = nome

    def getNomeCidade(self):
        return self.nome
    
    def setEstado(self , estado):
        self.estado = estado

    def getEstado(self):
        return self.estado
    
    def setEstadoCurso(self , estado):
        self.estado = estado

    def getEstadoCurso(self):
        return self.estado
    

    #Metodos#

    def getSiglaEstado(self):
        if self.estado == None:
            return "Cidade sem estado"
        else:
            return self.estado.getSigla()
        
    def getSiglaEstadoCurso(self):
        if self.estado == None:
            return "Cidade sem estado"
        else:
            return self.estado.getSiglaCurso()

class Escolaridade:
    def __init__(self):
        self.nome = ""
    def setNome(self, nome):
        self.nome = nome
    def getNome(self):
        return self.nome
    
class TipoEnsino:

    def __init__(self):
        self.nome = ""

    def setNome(self, nome):
        self.nome = nome
    def getNome(self):
        return self.nome



class Pessoa:
    def __init__(self):
        self.escolaridade = None
        self.cidade = None

    def setEscolaridade(self, escolaridade):
        self.escolaridade = escolaridade
    def getEscolaridade(self):
        return self.escolaridade
    
    def setCidade(self,cidade):
        self.cidade = cidade
    def getCidade(self):
        return self.cidade

    # Metodos #
    def getNomeEscolaridade(self):
        if self.escolaridade == None:
            return "Pessoa sem escolaridade"
        else:
            return self.escolaridade.getNome()
    def getNomeEstadoPessoa(self):
        if self.cidade == None:
            return "voce não tem estado"
        else:
            return self.cidade.getSiglaEstado()
        



class Professor(Pessoa):
    def __init__(self):
        Pessoa.__init__(self)
        self.cidade = None
        self.lecionar = None
        self.nome = ""
        self.nomeCoordenador = None
    
    def setNome(self , nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setLecionar(self , lecionar):
        self.lecionar = lecionar

    def getLecionar(self):
        return self.lecionar

    def setNomeCoordenador(self , nome):
        self.nomeCoordenador = nome

    def getNomeCooordenador(self):
        return self.nomeCoordenador


    def setCidadeProfessor(self , cidade):
        self.cidade = cidade

    def getCidadeProfessor(self):
        return self.cidade

    # METODOS #
    def getNomeLecionar(self):
        if self.lecionar == None:
            return "Não esta lecionando"
        else:
            return self.lecionar.getNome()

    def getNomeCidadeProfessor(self):
        if self.cidade == None:
            return "voce não tem estado"
        else:
            return self.cidade.getNomeCidade()
        
    def getNomeCoordenador(self):
        if self.nomeCoordenador == None:
            return "Sem nome Coordenador"
        else:
            return self.nomeCoordenador.getNome()
        
class Curso:
    def __init__(self):
        self.coordenador = None
        self.escola = None
        self.nomeCoordenador = None

    def setNomeCoordenador(self , nome):
        self.nomeCoordenador = nome
    
    def getNomeCoordenador(self):
        return self.nomeCoordenador


    def setCoordenador(self , professor):
        self.coordenador= professor

    def getCoordenador(self):
        return self.coordenador

    #teste 
    def setEscola(self , escola):
        self.escola = escola
    def getEscola(self):
        return self.escola


    # Metodos #
    def getCoordenadorEscolaridade(self):
        if self.coordenador == None:
            return "Pessoa sem escolaridade"
        else:
            return self.coordenador.getNomeEscolaridade()
        
    
    def getNomeCoordenador(self):
        if self.nomeCoordenador == None:
            return "Sem nome Coordenador"
        else:
            return self.nomeCoordenador.getNome()

class Escola:
    def __init__(self):
        self.diretor = None
        self.cidade = None
        self.nomeDiretor = None

    def setNomeDiretor(self , nome):
        self.nomeDiretor = nome

    def getNomeDiretor(self):
        return self.nomeDiretor

    def setDiretor(self , professor):
        self.diretor = professor
    
    def getDiretor(self):
        return self.diretor
    #teste
    def setCidade(self, cidade):
        self.cidade = cidade
    def getCidade(self):
        return self.cidade
    
    #Metodos#
    def getNomeEscolaridadeDiretor(self):
        if self.diretor == None:
            return "Diretor sem Escolariedade"
        else :
            return self.diretor.getNomeEscolaridade()
        
    def getNomeDiretor(self):
        if self.nomeDiretor == None:
            return "Sem Nome do Diretor"
        else:
            return self.nomeDiretor.getNome()

class Aluno(Pessoa):
    def __init__(self):
        Pessoa.__init__(self)
        self.curso = curso

    def setCurso(self , curso):
        self.curso = curso
        
    def getCurso(self):
        return self.curso    

     # METODOS #
    def getEstadoDoCurso(self):
        if self.cidade == None:
            return "voce não tem estado"
        else:
            return self.cidade.getSiglaEstadoCurso()
        





print('-------------------------------------------')

escolaridade = Escolaridade()
escolaridade.setNome("Doutorado")

print('-------------------------------------------')
tipoensino = TipoEnsino()


cidade = Cidade()
cidade.setNomeCidade("RJ")

professor = Professor()

professor.setEscolaridade(escolaridade)
print(professor.getNomeEscolaridade())

tipoensino.setNome("Superior")
professor.setLecionar(tipoensino)
print(professor.getNomeLecionar())

professor.setCidade(cidade)
print(professor.getNomeCidadeProfessor())

print('-------------------------------------------')

curso = Curso()

coordenador = Professor()

curso.setCoordenador(coordenador)
escolaridade.setNome("Mestrado")
curso.setNomeCoordenador(coordenador)
coordenador.setNome('BOB')


coordenador.setEscolaridade(escolaridade)
print(curso.getCoordenadorEscolaridade())
print(curso.getNomeCoordenador())
print('-------------------------------------------')

escola = Escola()

diretor = Professor()
escola.setDiretor(diretor)
diretor.setNome('Rubens')

escola.setNomeDiretor(diretor)

escolaridade.setNome("Ensino Superior")

diretor.setEscolaridade(escolaridade)
print(escola.getNomeEscolaridadeDiretor())
print(escola.getNomeDiretor())

print('-------------------------------------------')

estado = Estado()
estado.setSigla("RJ")

print('-------------------------------------------')

cidade = Cidade()
cidade.setEstado(estado)

print('-------------------------------------------')
curso = Curso()

aluno = Aluno()
aluno.setCidade(cidade)
print(aluno.getNomeEstadoPessoa())

escola = Escola()
cidade = Cidade()
estado = Estado()

estado.setSiglaCurso("SP")
aluno.setCurso(curso)
curso.setEscola(escola)
escola.setCidade(cidade)
cidade.setEstadoCurso(estado)

aluno.setCidade(cidade)
print(aluno.getEstadoDoCurso())


print('-------------------------------------------')

professor.setNomeCoordenador(coordenador)
print(professor.getNomeCoordenador())