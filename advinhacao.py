import random
import time
import os

def menu():
    print("--Menu de Opções--")
    print("F-Fácil")
    print("M-Médio")
    print("D-Difícil")
    print("Qual a sua opção?")
    
def vitu_careca(x, acertou, tentativas):
    palpite = int(input("Qual o seu palpite? "))
    if(palpite == x):
        acertou = True
        tentativas-=1
    elif(palpite < x):
        print("Você errou para baixo...tente um número maior")
        tentativas-=1
        print("Tentativas restantes:", tentativas)
    else:
        print("Você errou para cima...tente um número menor")
        tentativas-=1
        print("Tentativas restantes:", tentativas)
    return tentativas, acertou

while True:
    print("Bem vindo(a) ao jogo de advinhação")
    nome = input("Qual o seu nome? ")

    tentativas = 0
    tentativas_totais =''
    x = random.randint(1,100)
    acertou = False

    while(tentativas == 0):
        menu()
        resp = input()
        match resp.upper():
            case "F":
                tentativas += 10
                tentativas_totais = tentativas
            case "M":
                tentativas += 5
                tentativas_totais = tentativas
            case "D":
                tentativas += 3
                tentativas_totais = tentativas
            case _:
                print("Resposta inválida, dê outra resposta")

    tempo_inicial = time.time()

    while(tentativas != 0 and acertou == False):
        tentativas, acertou = vitu_careca(x, acertou, tentativas)
        print("")
    tempo_final = time.time()

    if(acertou == False):
        print("Acabaram suas tentativas! Você perdeu!")
        print("O número secreto era", x)
    else:
        print("Parabéns! Você ganhou!")
        print("O número secreto era", x)
        print("Nome:", nome)
        print("Tentativas usadas:",tentativas_totais-tentativas)
        print("Tempo gasto:",tempo_final - tempo_inicial, "segundos")

    continuar = input("Você deseja jogar novamente?[s/n]")
    if(continuar.upper() == "S"):
        os.system('cls')
    elif(continuar.upper() == "N"):
        break
    else:
        print("Resposta inválida, assumimos que você não deseja continuar!")
        break