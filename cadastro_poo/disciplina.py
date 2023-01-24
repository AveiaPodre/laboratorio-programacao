from aluno import Aluno
from professor import Professor

class Disciplina:
    codigo = 0
    nome = ''
    semestre = ''
    professores = []
    alunos = []
    carga = 0
    dias = []
    horario = 0

    def __init__(self, codigo, nome, semestre, professores, alunos, carga, dias, horario):
        self.codigo = codigo
        self.nome = nome
        self.semestre = semestre
        self.professores = professores
        self.alunos = alunos
        self.carga = carga
        self.dias = dias
        self.horario = horario

    def get_codigo(self):
        return self.codigo
    
    def get_nome(self):
        return self.nome

    def get_semestre(self):
        return self.semestre
    
    def get_professores(self):
        return self.professores
    
    def get_alunos(self):
        return self.alunos
    
    def get_carga(self):
        return self.carga
    
    def get_dias(self):
        return self.dias

    def get_horario(self):
        return self.horario

    def pesquisa_prof(self, cod_prof):
        for prof in self.professores:
            if(prof.get_codigo() == cod_prof):
                return prof
        return None

    def cadastra_prof(self):
        cod_prof = int(input("Informe o código do professor: "))
        if(self.pesquisa_prof(cod_prof) != None):
            print("Código de professor já cadastrado na disciplina.")
        else:
            nome_prof = input("Informe o nome do professor: ")
            prof = Professor(cod_prof, nome_prof)
            (self.professores).append(prof)

    def pesquisa_aluno(self, matricula_aluno):
        for alu in self.alunos:
            if(alu.get_matricula() == matricula_aluno):
                return alu
        return None

    def cadastra_aluno(self):
        matricula_aluno = int(input("Informe a matrícula do aluno: "))
        if(self.pesquisa_aluno(matricula_aluno)!=None):
            print("Matrícula de aluno já cadastrada no sistema.")
        else:
            nome_aluno = input("Informe o nome do aluno: ")
            curso_aluno = input("Informe o curso do aluno: ")
            notas = []
            alu = Aluno(matricula_aluno, nome_aluno, curso_aluno, notas)
            (self.alunos).append(alu)

    def insere_notas(self):
        while(True):
            if(len(self.get_alunos()) == 0):
                print("Não há alunos matriculados nessa disciplina.")
                break
            else:
                matricula_aluno = int(input("Informe a matrícula do aluno: "))
                alu = self.pesquisa_aluno(matricula_aluno)
                if(alu == None):
                    print("Aluno não matriculado nessa disciplina.")
                    break
                else:
                    alu.insere_notas()
                    break

    def lista_prof(self):
        if(len(self.get_professores()) == 0):
            print("Não há professores cadastrados nessa disciplina.")
        else:
            for professor in self.professores:
                print("Nome:"+ professor.get_nome() +"  Código:" + str(professor.get_codigo()))

    def lista_aluno(self):
        if(len(self.get_alunos()) == 0):
            print("Não há alunos matriculados nessa disciplina.")
        else:
            for alu in self.alunos:
                print("Nome:"+ alu.get_nome() +"  Matrícula:" + str(alu.get_matricula()) + " Curso:" + alu.get_curso())

    def lista_notas(self):
        if(len(self.get_alunos()) == 0):
            print("Não há alunos matriculados nessa disciplina.")
        else:
            for alu in self.alunos:
                alu.lista_notas()