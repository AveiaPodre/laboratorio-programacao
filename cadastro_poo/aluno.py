class aluno:
    matricula = 0
    nome = ''
    notas = []

    def __init__(self, matricula, nome, notas):
        self.matricula = matricula
        self.nome = nome
        self.notas = notas
    
    def get_matricula(self):
        return self.matricula

    def get_nome(self):
        return self.nome

    def get_notas(self):
        return self.notas
        