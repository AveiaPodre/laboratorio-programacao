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