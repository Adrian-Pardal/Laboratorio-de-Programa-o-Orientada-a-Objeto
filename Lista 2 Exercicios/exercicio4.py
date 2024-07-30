class Pessoa():
    def __init__(self):
        self.nome = ""
    
    def setNome(self , nome):
        self.nome = nome

    def getNome(self):
        return self.nome

class Disciplina():
    def __init__(self):
        self.nome = ""
    
    def setNome(self , nome):
        self.nome = nome

    def getNome(self):
        return self.nome

class Aluno(Pessoa):
    def __init__(self):
        Pessoa.__init__(self)
    
class Professor(Pessoa):
    def __init__(self):
        Pessoa.__init__(self)

class Curso():

    def __init__(self):
        self.turmas = []
        self.alunos= []

    def matricularAlunoCurso(self , aluno):
        self.alunos.append(aluno) 

    def exibirNomesAlunosCurso(self):
        for aluno in self.alunos:
            print(aluno.getNome())

    def matricularTurma(self,turma):
        self.turmas.append(turma)

    def exibirTurma(self):
        for turma in self.turmas:
            print(turma.getNome())

    def  mostrarProfessoresTurma(self):    
        for turma in self.turmas:
            print(turma.exibirProfessor())
    
    def mostrarAlunosTurma(self):
        for turma in self.turmas:
            print(turma.exibirNomesAlunos())

    def verificarAluno(self , aluno):
        return aluno in self.alunos
    
    def verificarTurma(self , turma):
        return turma in self.turmas
    
    def excluirTurma(self , turma):
        self.turmas.remove(turma)

    def excluirAluno(self , aluno):
        self.alunos.remove(aluno)

class Turma():


    def __init__(self):
        self.nome = ""
        self.alunos = []
        self.professores = []
        self.disciplinas = []

    def setNome(self , nome):
        self.nome = nome

    def getNome(self):
        return self.nome
    
    #Metodos#
    def exibirNomesAlunos(self):
        for aluno in self.alunos:
            print(aluno.getNome())
    
    def verificarAluno(self , aluno):
        return aluno in self.alunos
    
    def excluirAluno(self , aluno):
        self.alunos.remove(aluno)

    def matricular(self , aluno):
        self.alunos.append(aluno)

    def matricularProfessor(self , professor):
        self.professores.append(professor)

    def matricularDisciplina(self , disciplina):
        self.disciplinas.append(disciplina)

    def mostrarDisciplina(self):
        for disciplina in self.disciplinas:
            print(disciplina.getNome())

    def exibirProfessor(self):
        for professor in self.professores:
            print(professor.getNome())

turma = Turma()
aluno1 = Aluno()
aluno1.setNome("Joao")
aluno2 = Aluno()
aluno2.setNome("Maria")
aluno3 = Aluno()
aluno3.setNome("Ana")

print("# Questão 1 #")
professor1 = Professor()
professor2 = Professor()

professor1.setNome("Sergio")
professor2.setNome("lucas")

#turma.matricularProfessor(professor1)
#turma.matricularProfessor(professor2)

#turma.exibirProfessor()



print("# Questão 2 #")
turma.matricular(aluno1)
turma.matricular(aluno2)
#turma.exibirNomesAlunos()

print("# Questão 3 #")
curso = Curso()
turma2 = Turma()
turma3 = Turma()

#turma2.setNome("Engenharia 2")
#turma3.setNome("Engenharia 1")

curso.matricularTurma(turma)
curso.matricularTurma(turma3)
curso.matricularTurma(turma2)



turma3.matricularProfessor(professor2)
turma3.matricularProfessor(professor1)


curso.mostrarProfessoresTurma()

print("# Questão 4 #")

curso.mostrarAlunosTurma()


print("# Questão 5 #")

curso.matricularAlunoCurso(aluno1)
curso.matricularAlunoCurso(aluno2)
curso.matricularAlunoCurso(aluno3)

curso.exibirNomesAlunosCurso()

print("# Questão 6 #")
displina1 = Disciplina()
displina2 = Disciplina()

displina1.setNome("Foster")
displina2.setNome("Guser")

turma2.matricularDisciplina(displina1)
turma2.matricularDisciplina(displina2)

turma2.mostrarDisciplina()

print("# Questão 7 #")
print(turma.verificarAluno(aluno1))
print(turma.verificarAluno(aluno3))

print("# Questão 8 #")

print(curso.verificarAluno(aluno2))

print("# Questão 9 #")

print(curso.verificarTurma(turma2))

print("# Questão 10 #")
turma.excluirAluno(aluno1)
print(turma.verificarAluno(aluno1))


print("# Questão 11 #")

curso.excluirTurma(turma2)
print(curso.verificarTurma(turma2))


print("# Questão 12 #")

curso.excluirAluno(aluno1)
print(curso.verificarAluno(aluno1))