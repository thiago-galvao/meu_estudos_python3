# 68 - Faça um programa que jogue par ou impar com o computador. 
# O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
print("="*15,end="")
print("JOGO DO íMPAR-PAR",end="")
print("="*15)
vitoria = 0
while True:
    computador = randint(0,10)
    jogador = int(input("Escolha um número: "))
    escolha = (input("Impar ou Par? ")).lower()
    print("="*30)
    soma = jogador + computador
    print(f"O jogador escolheu o número {jogador} e o computador o número {computador} portanto a soma foi de {soma}.")
    if soma % 2 == 0 and escolha == "par":
        print("E como o jogador escoheu par ele venceu!")
        vitoria += 1
    elif soma % 2 != 0 and escolha =="impar":
        print("E como o jogador escoheu impar ele venceu!")
        vitoria += 1
    else:
        print("O computador venceu!")
        print("="*30)
        print(f"E o total de vitórias do jogador foi de {vitoria}.")
        break