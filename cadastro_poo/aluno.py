class Aluno:
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

    def insere_notas(self):
        for i in range(0,3):
            while(True):
                nota = float(input("Informe a "+str((i+1))+"° nota: "))
                if(nota<0 or nota>10):
                    print("Nota inválida, insira um valor coerente")
                else:
                    (self.notas).append(nota)
                    break

    def lista_notas(self):
        if(len(self.notas) == 0):
            print("Aluno " + self.nome + " não tem notas cadastradas\n")
        else:
            print("Aluno: " + self.nome)
            for i in range(0,3):
                print("Nota " + str(i+1) + ": " + str(self.notas[i]))
            media = (self.notas[0] + self.notas[1] + self.notas[2])/3
            print("Media: " + str(media))
            print("")