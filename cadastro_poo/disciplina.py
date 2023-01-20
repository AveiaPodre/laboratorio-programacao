import aluno
import professor

class disciplina:
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
                return professor
        return None

    def cadastra_prof(self):
        cod_prof = int(input("Informe o código do professor: "))
        if(pesquisa_prof(cod_prof) != None):
            print("Código de professor já cadastrado na disciplina.")
        else:
            nome_prof = input("Informe o nome do professor: ")
            prof = professor(cod_prof, nome_prof)
            (self.professores).append(prof)

    def pesquisa_aluno(self, matricula_aluno):
        for alu in self.alunos:
            if(alu.get_matricula() == matricula_aluno):
                return alu
        return None

    def cadastra_aluno(self):
        matricula_aluno = int(input("Informe a matrícula do aluno: "))
        if(pesquisa_aluno(matricula_aluno)!=None):
            print("Matrícula de aluno já cadastrada no sistema.")
        else:
            nome_aluno = input("Informe o nome do aluno: ")
            curso_aluno = input("Informe o curso do aluno: ")
            notas = []
            alu = aluno(matricula_aluno, nome_aluno, curso_aluno, notas)
            (self.alunos).append(alu)


