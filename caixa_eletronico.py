# 71 - Crie um programa que simule o funcionamento de um caixa eletrônico. 
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. 
# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1
from time import sleep
print("="*10, "CAIXA ELETRÔNICO", "="*10)
cont50 = cont20 = cont10 = cont1 = saldo = 0
while True:
    saque = int(input("Digite o valor a ser sacado: R$"))
    saldo = saque
    while saldo >= 50:
        saldo -= 50
        cont50 += 1
    while saldo >= 20:
        saldo -= 20
        cont20 += 1
    while saldo >= 10:
        saldo -= 10
        cont10 += 1
        cont10
    while saldo >= 1:
        saldo -= 1
        cont1 += 1
    break
print ("="*20)
print("SAQUE AUTORIZADO")
print ("="*20)
print("TOTAIS:")
print(f"{cont50} notas de R$50")
print(f"{cont20} notas de R$20")
print(f"{cont10} notas de R$10")
print(f"{cont1} notas de R$1")
print("="*20)
print("Contando cédulas...")
sleep(4)
print("Saque realizado.")
