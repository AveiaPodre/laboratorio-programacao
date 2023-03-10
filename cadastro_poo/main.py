from disciplina import Disciplina
from aluno import Aluno
from professor import Professor
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
                    prof = Professor(cod_prof, nome_prof)
                    professores_disc.append(prof)
                
            alunos_disc = []
            if(linha[4] != " "):
                alunos = []
                alunos = (linha[4].split(';'))
                for alu in alunos:
                    info = (str(alu).split('-'))
                    matricula_aluno = int(info[0])
                    nome_aluno = info[1]
                    curso_aluno = info[2]
                    notas_aluno = []
                    if(info[3] != " "):
                        notas = (str(info[3]).split('#'))
                        for nota in notas:
                            nota_float = float(nota)
                            notas_aluno.append(nota_float)
                    alu = Aluno(matricula_aluno, nome_aluno, curso_aluno, notas_aluno)
                    alunos_disc.append(alu)
                
            carga_disc = int(linha[5])
            dias_disc = []
            dias = str(linha[6]).split(';')
            for dia in dias:
                dias_disc.append(dia)
            horario_disc = linha[7]
            disc = Disciplina(cod_disc, nome_disc, semestre_disc, professores_disc, alunos_disc, carga_disc, dias_disc, horario_disc)
            disciplinas.append(disc)       
    arquivo_disc.close()
def lista_para_arquivos():
    arquivo_disc = open('disciplinas.csv', 'w', newline='', encoding='utf-8')
    for disc in disciplinas:
        # disciplina = (cod_disc, nome_disc, semestre_disc, professores, alunos, carga_disc, dias_disc, horarios_disc)
        cod_disc = disc.get_codigo()
        nome_disc = disc.get_nome()
        semestre_disc = disc.get_semestre()
        professores = ""
        if len(disc.get_professores()) > 0:
            for prof in disc.get_professores():
                cod_prof = prof.get_codigo()
                nome_prof = prof.get_nome()
                professores += str(cod_prof)+"-"+nome_prof+";"
            professores = professores[0:-1]
        else:
            professores = " "
        alunos = ""
        if len(disc.get_alunos()) > 0:
            for alu in disc.get_alunos():
                matricula_aluno = alu.get_matricula()
                nome_aluno = alu.get_nome()
                curso_aluno = alu.get_curso()
                notas_aluno = ""
                if len(alu.get_notas()) > 0:
                    list_notas = alu.get_notas()
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
        carga_disc = disc.get_carga()
        dias = disc.get_dias()
        if len(disc.get_dias()) == 2:
            dias_disc = str(dias[0])+";"+str(dias[1])
        else:
            dias_disc = str(dias[0])+";"+str(dias[1])+";"+str(dias[2])
        horarios_disc = disc.get_horario()
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
            disc = Disciplina(cod_disc, nome_disc, semestre_disc, professores, alunos, carga_disc, dias_disc, horario_disc)
            disciplinas.append(disc)
            break
def pesquisa_disc(cod):
    for disc in disciplinas:
        if(cod == disc.get_codigo()):
            return disc
    return None

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
            disc = pesquisa_disc(cod)
            if(disc == None):
                print("Disciplina não existente no sistema, tente novamente com um código válido")
                continue
            else:
                print("Nome:"+str(disc.get_nome()))
                print("Codigo:"+ str(disc.get_codigo()))
                print("Semestre:"+ str(disc.get_semestre()))
                print("Professores:"+ str(disc.get_professores()))
                print("Carga Horária:"+ str(disc.get_carga()))
                print("Dias da semana:"+ str(disc.get_dias()))
                print("Horário:"+ str(disc.get_horario()))
                break
                
    elif(resp == 3):
        #listar disciplinas
        if(len(disciplinas)==0):
            print("Não há nenhum disciplina cadastrada no sistema")
        else:
            for disc in disciplinas:
                print("Nome:"+str(disc.get_nome())+"\nCódigo:"+str(disc.get_codigo())+"\n")

    elif(resp == 4):
        #cadastrar professor em disciplina   
        if(len(disciplinas)==0):
            print("Não há nenhuma disciplina cadastrada no sistema")
        else:
            while(True):
                cod_disc = int(input("Informe o código da disciplina: "))
                disc = pesquisa_disc(cod_disc)
                if(disc == None):
                    print("Disciplina não existente no sistema, tente novamente com um código válido")
                else:
                    disc.cadastra_prof()
                    break

    elif(resp == 5):
        #matricular aluno em disciplina
        if(len(disciplinas)==0):
            print("Não há nenhuma disciplina cadastrada no sistema")
        else:
            while(True):
                cod_disc = int(input("Informe o código da disciplina: "))
                disc = pesquisa_disc(cod_disc)
                if(disc == None):
                    print("Disciplina não existente no sistema, tente novamente com um código válido")
                else:
                    disc.cadastra_aluno()
                    break

    elif(resp == 6):
        #lançar notas de aluno em disciplina
        if(len(disciplinas)==0):
            print("Não há nenhuma disciplina cadastrada no sistema")
        else:
            while(True):
                cod_disc = int(input("Informe o código da disciplina: "))
                disc = pesquisa_disc(cod_disc)
                if(disc == None):
                    print("Disciplina não existente no sistema, tente novamente com um código válido")
                else:
                    disc.insere_notas()
                    break
    
    elif(resp == 7):
        #listar professores de uma disciplina
        if(len(disciplinas)==0):
            print("Não há nenhuma disciplina cadastrada no sistema")
        else:
            while(True):
                cod_disc = int(input("Informe o código da disciplina: "))
                disc = pesquisa_disc(cod_disc)
                if(disc == None):
                    print("Disciplina não existente no sistema, tente novamente com um código válido")
                else:
                    disc.lista_prof()
                    break

    elif(resp == 8):
        #listar alunos de uma disciplina
        if(len(disciplinas)==0):
            print("Não há nenhuma disciplina cadastrada no sistema")
        else:
            while(True):
                cod_disc = int(input("Informe o código da disciplina: "))
                disc = pesquisa_disc(cod_disc)
                if(disc == None):
                    print("Disciplina não existente no sistema, tente novamente com um código válido")
                else:
                    disc.lista_aluno()
                    break

    elif(resp == 9):
        #listar notas dos alunos de uma disciplina
        if(len(disciplinas)==0):
            print("Não há nenhuma disciplina cadastrada no sistema")
        else:
            while(True):
                cod_disc = int(input("Informe o código da disciplina: "))
                disc = pesquisa_disc(cod_disc)
                if(disc == None):
                    print("Disciplina não existente no sistema, tente novamente com um código válido")
                else:
                    disc.lista_notas()
                    break

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