menu = '''--- Mini Controle Acadêmico ---
1. Cadastrar disciplina
2. Pesquisar disciplina
3. Listar disciplinas cadastradas
4. Cadastrar professor em disciplina
5. Matricular aluno em disciplina
6. Lançar notas do aluno em uma disciplina
7. Listar alunos de uma disciplina
8. Listar notas dos alunos de uma disciplina
9. Sair'''

disciplinas = []

def cadastra_disc():
    while(True):
        cod_disc = int(input("Informe o código da disciplina a cadastrar: "))
        if(pesquisa_disc(cod_disc) != None):
            print("Código de disciplina em uso, tente outro código.")
        else:
            nome_disc = input("Informe o nome da disciplina:")

            ano = input("Informe o ano da disciplina: ")
            semestre = 0
            while(semestre !=1 and semestre !=2):
                semestre = int(input("Informe o semestre de ocorrência da disciplina[1/2]: "))
                if(semestre !=1 and semestre !=2):
                    print("Semestre inválido, informe uma resposta coerente.")
            semestre_disc = str(ano) + "." + str(semestre)

            carga_disc = int(input("Informe a carga horária da disciplina: "))

            quant_dias = 0
            while(quant_dias != 2 and quant_dias != 3):
                quant_dias = int(input("Em quantos dias por semana será lecionada a disciplina[2/3]: "))
                if(quant_dias !=2 and quant_dias !=3):
                    print("Quantidade inválida, informe um valor adequado.")

            dias_disc = []

            print("Informe os dias em que a disciplina será lecionada:\n 2-Segunda\n 3-Terça\n 4-Quarta\n 5-Quinta\n 6-Sexta\n 7-Sábado\n")
            for i in range(0, quant_dias):
                while(True):
                    dia = int(input())
                    if(dia<2 or dia>7):
                        print("Resposta inválida, informe um valor correto.")
                    else:
                        dias_disc.append(dia)
                        break
            
            print("Informe o horário no qual a disciplina será lecionada: \n1-8h às 10h\n2-10h às 12h\n3-12h às 14h\n4-14h às 16h\n5-16h às 18h\n6-18h às 20h\n7-20h às 22h\n")        
            while(True):
                horario_disc = int(input())
                if(horario_disc<1 or horario_disc>7):
                    print("Valor inválido, informe um horário correto")
                else:
                    break
            
            professores = []
            disciplina = ((cod_disc, nome_disc, semestre_disc, professores, carga_disc), (dias_disc, horario_disc))
            disciplinas.append(disciplina)
            break

def pesquisa_disc(cod):
    for disciplina in disciplinas:
        if(cod == disciplina[0][0]):
            return disciplina
    return None

def cadastra_prof():
def pesquisa_prof():
def cadastra_aluno():
def pesquisa_aluno():
def lista_prof():
def lista_aluno():
def insere_notas():


while(True):
    print(menu)
    resp = int(input("Informe a função a ser usada: "))

    if(resp == 1):
        #cadastro da disciplina
        cadastra_disc()
        print()
    
    elif(resp == 2):
        #pesquisar disciplina
        cod = int(input("Qual o código da disciplina a ser pesquisada: "))
        cod_disc = pesquisa_disc(cod)
        if(cod_disc == None):
            print("Disciplina não existente no sistema")
        else:
            i = 0
            for disciplina in disciplinas:
                

    elif(resp == 3):
        #listar disciplinas
    elif(resp == 4):
        #cadastrar professor em disciplina
    elif(resp == 5):
        #cadastrar aluno em disciplina
    elif(resp == 6):
        #matricular ano em disciplina
    elif(resp == 7):
        #lançar notas de aluno em disciplina
    elif(resp == 8):
        #listar notas dos alunos em disciplina
    elif(resp == 9):
        #sair do programa
        break
    else:
        print("Opção inválida, tente novamente!")