# 81 - Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B)A lista de valores ordenada de forma decrescente.
# C)Se o valor 5 foi digitado e está ou não na lista.
lista = []
while True:
    n = int(input("Digite um número: "))
    lista.append(n)
    print("Níumero adicionado com sucesso.")
    continua = str(input("Deseja adicionar mais algum número? [S/N]: ")).lower().strip()[0]
    while not continua in "sn":
        print("Desculpe, não entendi...")
        continua = str(input("Deseja adicionar mais algum número? [S/N]: ")).lower().strip()[0]
    if continua == "n":
        break
print(f"Você digitou {len(lista)} números na lista.")
lista.sort(reverse=True)
print(f"A lista em ordem decrescente fica: {lista}")
if 5 in lista:
    print("O número 5 está na lista.")
else:
    print("O número 5 não está na lista.")
