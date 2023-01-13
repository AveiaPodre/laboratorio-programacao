import csv
import os

menu = '''--- Mini Controle Acadêmico ---
1. Cadastrar disciplina
2. Pesquisar disciplina
3. Listar disciplinas cadastradas
4. Cadastrar professor em disciplina
5. Matricular aluno em disciplina
6. Lançar notas do aluno em uma disciplina
7. Listar professores de uma disciplina
8. Listar alunos de uma disciplina
9. Listar notas dos alunos de uma disciplina
10. Salvar arquivo
11. Salvar e sair
12. Sair sem salvar'''

disciplinas = []

def arquivo_para_lista():
    if os.path.isfile('disciplinas.csv'):
        arquivo_disc = open('disciplinas.csv', 'r', newline='', encoding='utf-8')
    else:
        arquivo_disc = open('disciplinas.csv', 'w', newline='', encoding='utf-8')
        return
    with open('disciplinas.csv', mode='r') as arquivo_disc:
        csv_reader = csv.reader(arquivo_disc, delimiter = ',')

        for linha in csv_reader:
            cod_disc = int(linha[0])
            nome_disc = linha[1]
            semestre_disc = linha[2]
            professores_disc = []
            if(linha[3] != " "):
                professores = []
                professores = (linha[3].split(';'))
                for prof in professores:
                    info =(str(prof).split('-'))
                    cod_prof = int(info[0])
                    nome_prof = info[1]
                    professor = (cod_prof, nome_prof)
                    professores_disc.append(professor)
                
            alunos_disc = []
            if(linha[4] != " "):
                alunos = []
                alunos = (linha[4].split(';'))
                for aluno in alunos:
                    info = (str(aluno).split('-'))
                    matricula_aluno = int(info[0])
                    nome_aluno = info[1]
                    curso_aluno = info[2]
                    notas_aluno = []
                    if(info[3] != " "):
                        notas = (str(info[3]).split('#'))
                        for nota in notas:
                            nota_float = float(nota)
                            notas_aluno.append(nota_float)
                    alu = (matricula_aluno, nome_aluno, curso_aluno, notas_aluno)
                    alunos_disc.append(alu)
                
            carga_disc = int(linha[5])
            dias_disc = []
            dias = str(linha[6]).split(';')
            for dia in dias:
                dias_disc.append(dia)
            horario_disc = linha[7]
            disciplina = ((cod_disc, nome_disc, semestre_disc, professores_disc, alunos_disc, carga_disc),(dias_disc, horario_disc))
            disciplinas.append(disciplina)       
    arquivo_disc.close()
def lista_para_arquivos():
    arquivo_disc = open('disciplinas.csv', 'w', newline='', encoding='utf-8')
    for disc in disciplinas:
        # disciplina = ((cod_disc, nome_disc, semestre_disc, professores, alunos, carga_disc), (dias_disc, horarios_disc))
        cod_disc = disc[0][0]
        nome_disc = disc[0][1]
        semestre_disc = disc[0][2]
        professores = ""
        if len(disc[0][3]) > 0:
            for professor in disc[0][3]:
                cod_prof = professor[0]
                nome_prof = professor[1]
                professores += str(cod_prof)+"-"+nome_prof+";"
            professores = professores[0:-1]
        else:
            professores = " "
        alunos = ""
        if len(disc[0][4]) > 0:
            for aluno in disc[0][4]:
                matricula_aluno = aluno[0]
                nome_aluno = aluno[1]
                curso_aluno = aluno[2]
                notas_aluno = ""
                if len(aluno[3]) > 0:
                    list_notas = aluno[3]
                    n1 = list_notas[0]
                    n2 = list_notas[1]
                    n3 = list_notas[2]
                    notas_aluno += str(n1)+"#"+str(n2)+"#"+str(n3)
                else:
                    notas_aluno = " "
                alunos += str(matricula_aluno)+"-"+nome_aluno+"-"+curso_aluno+"-"+notas_aluno+";"
            alunos = alunos[0:-1]
        else:
            alunos = " "
        carga_disc = disc[0][5]
        if len(disc[1][0]) == 2:
            dias_disc = str((disc[1][0])[0])+";"+str((disc[1][0])[1])
        else:
            dias_disc = str((disc[1][0])[0])+";"+str((disc[1][0])[1])+";"+str((disc[1][0])[2])
        horarios_disc = disc[1][1]
        nova_disc = str(cod_disc)+","+str(nome_disc)+","+str(semestre_disc)+","+professores+","+alunos+","+str(carga_disc)+","+dias_disc+","+str(horarios_disc)
        arquivo_disc.write(nova_disc+"\n")
    arquivo_disc.close()
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
            alunos = []
            disciplina = ((cod_disc, nome_disc, semestre_disc, professores, alunos, carga_disc), (dias_disc, horario_disc))
            disciplinas.append(disciplina)
            break
def pesquisa_disc(cod):
    for disciplina in disciplinas:
        if(cod == disciplina[0][0]):
            return disciplina
    return None
def cadastra_prof():
    while(True):
        cod_disc = int(input("Informe o código da disciplina: "))
        disciplina = pesquisa_disc(cod_disc)
        if(disciplina == None):
            print("Disciplina não existente no sistema, tente novamente com um código válido")
        else:      
            cod_prof = int(input("Informe o código do professor: "))
            if(pesquisa_prof(cod_prof, disciplina)!=None):
                print("Código de professor já cadastrado na disciplina.")
            else:
                nome_prof = input("Informe o nome do professor: ")
                professor = (cod_prof, nome_prof)
                (disciplina[0][3]).append(professor)
                break
def pesquisa_prof(cod_prof, disciplina):
    for professor in disciplina[0][3]:
        if(professor[0] == cod_prof):
            return professor
    return None
def cadastra_aluno():
    while(True):
        cod_disc = int(input("Informe o código da disciplina: "))
        disciplina = pesquisa_disc(cod_disc)
        if(disciplina == None):
            print("Disciplina não existente no sistema, tente novamente com um código válido")
        else:      
            matricula_aluno = int(input("Informe a matrícula do aluno: "))
            if(pesquisa_aluno(matricula_aluno, disciplina)!=None):
                print("Matrícula de aluno já cadastrada no sistema.")
            else:
                nome_aluno = input("Informe o nome do aluno: ")
                curso_aluno = input("Informe o curso do aluno: ")
                notas = []
                aluno = (matricula_aluno, nome_aluno, curso_aluno, notas)
                (disciplina[0][4]).append(aluno)
                break
def pesquisa_aluno(matricula_aluno, disciplina):
    for aluno in disciplina[0][4]:
        if(aluno[0] == matricula_aluno):
            return aluno
    return None
def lista_prof():
    while(True):
        cod_disc = int(input("Informe o código da disciplina: "))
        disciplina = pesquisa_disc(cod_disc)
        if(disciplina == None):
            print("Disciplina não existente no sistema, tente novamente com um código válido")
        else:
            if(len(disciplina[0][3])==0):
                print("Não há professores cadastrados nessa disciplina.")
            for professor in disciplina[0][3]:
                print("Nome:"+professor[1]+"  Código:"+str(professor[0]))
            break
def lista_aluno():
    while(True):
        cod_disc = int(input("Informe o código da disciplina: "))
        disciplina = pesquisa_disc(cod_disc)
        if(disciplina == None):
            print("Disciplina não existente no sistema, tente novamente com um código válido")
        else:
            if(len(disciplina[0][4])==0):
                print("Não há alunos matriculados nessa disciplina.")
            for aluno in disciplina[0][4]:
                print("Nome:"+aluno[1]+"  Matrícula:"+str(aluno[0])+"  Curso:"+aluno[2])
            break
def insere_notas():
    while(True):
        cod_disc = int(input("Informe o código da disciplina: "))
        disciplina = pesquisa_disc(cod_disc)
        if(disciplina == None):
            print("Disciplina não existente no sistema, tente novamente com um código válido")
        elif(len(disciplina[0][4])==0):
            print("Não há alunos matriculados nessa disciplina.")
            break
        else:
            matricula_aluno = int(input("Informe a matrícula do aluno: "))
            aluno = pesquisa_aluno(matricula_aluno, disciplina)
            if(aluno == None):
                print("Aluno não matriculado nessa disciplina.")
                break
            else:
                for i in range(0,3):
                    while(True):
                        nota = float(input("Informe a "+str((i+1))+"° nota: "))
                        if(nota<0 or nota>10):
                            print("Nota inválida, insira um valor coerente")
                        else:
                            aluno[3].append(nota)
                            break
                break
def lista_notas():
    while(True):
        cod_disc = int(input("Informe o código da disciplina: "))
        disciplina = pesquisa_disc(cod_disc)
        if(disciplina == None):
            print("Disciplina não existente no sistema, tente novamente com um código válido")
        elif(len(disciplina[0][4])==0):
            print("Não há alunos matriculados nessa disciplina.")
            break
        else:
            for aluno in disciplina[0][4]:
                if(len(aluno[3]) == 0):
                    print("Aluno " + aluno[1] + " não possui nenhuma nota cadastrada")
                    continue
                soma_notas = 0
                for nota in aluno[3]:
                    soma_notas += nota
                media_aluno = soma_notas/len(aluno[3])
                print("Aluno:"+aluno[1])
                i = 1
                for nota in aluno[3]:
                    print("Nota"+str(i)+":"+str(nota))
                    i +=1
                print("Média:"+str(media_aluno)+"\n")
            break

arquivo_para_lista()
print(menu)
while(True):
    print("")
    resp = int(input("Informe a função a ser usada: "))

    if(resp == 1):
        #cadastro da disciplina
        cadastra_disc()
        print()
    
    elif(resp == 2):
        #pesquisar disciplina
        while(True):
            if(len(disciplinas)==0):
                print("Não há nenhuma disciplina cadastrada no sistema")
                break
            cod = int(input("Qual o código da disciplina a ser pesquisada: "))
            disciplina = pesquisa_disc(cod)
            if(disciplina == None):
                print("Disciplina não existente no sistema, tente novamente com um código válido")
                continue
            else:
                print("Nome:"+str(disciplina[0][1]))
                print("Codigo:"+ str(disciplina[0][0]))
                print("Semestre:"+ str(disciplina[0][2]))
                print("Professores:"+ str(disciplina[0][3]))
                print("Carga Horária:"+ str(disciplina[0][5]))
                print("Dias da semana:"+ str(disciplina[1][0]))
                print("Horário:"+ str(disciplina[1][1]))
                break
                
    elif(resp == 3):
        #listar disciplinas
        if(len(disciplinas)==0):
            print("Não há nenhum disciplina cadastrada no sistema")
        else:
            for disciplina in disciplinas:
                print("Nome:"+str(disciplina[0][1])+"\nCódigo:"+str(disciplina[0][0])+"\n")

    elif(resp == 4):
        #cadastrar professor em disciplina   
        if(len(disciplinas)==0):
            print("Não há nenhuma disciplina cadastrada no sistema")
        else:
            cadastra_prof()

    elif(resp == 5):
        #matricular aluno em disciplina
        if(len(disciplinas)==0):
            print("Não há nenhuma disciplina cadastrada no sistema")
        else:
            cadastra_aluno()

    elif(resp == 6):
        #lançar notas de aluno em disciplina
        if(len(disciplinas)==0):
            print("Não há nenhuma disciplina cadastrada no sistema")
        else:
            insere_notas()
    
    elif(resp == 7):
        #listar professores de uma disciplina
        if(len(disciplinas)==0):
            print("Não há nenhuma disciplina cadastrada no sistema")
        else:
            lista_prof()

    elif(resp == 8):
        #listar alunos de uma disciplina
        if(len(disciplinas)==0):
            print("Não há nenhuma disciplina cadastrada no sistema")
        else:
            lista_aluno()

    elif(resp == 9):
        #listar notas dos alunos de uma disciplina
        if(len(disciplinas)==0):
            print("Não há nenhuma disciplina cadastrada no sistema")
        else:
            lista_notas()

    elif(resp == 10):
        #salvar o programa
        lista_para_arquivos()

    elif(resp == 11):
        #salvar e sair do programa
        lista_para_arquivos()
        break
    elif(resp == 12):
        #sair sem salvar
        break
    else:
        print("Opção inválida, tente novamente!")