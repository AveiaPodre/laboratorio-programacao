class aluno:
    matricula = 0
    nome = ''
    curso =''
    notas = []

    def __init__(self, matricula, nome, curso, notas):
        self.matricula = matricula
        self.nome = nome
        self.curso = curso
        self.notas = notas
    
    def get_matricula(self):
        return self.matricula

    def get_nome(self):
        return self.nome

    def get_notas(self):
        return self.notas
        
    def get_curso(self):
        return self.curso