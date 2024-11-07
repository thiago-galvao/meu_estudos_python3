# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
nome = list()
peso = list()
while True:
    nome.append(str(input("Nome: ")))
    peso.append(int(input("Peso: ")))
    pergunta = " "
    while not pergunta in "sn":
        pergunta = str(input("Deseja cadastrar mais alguma pessoa? [S/N]: ")).lower().strip()[0]
    if pergunta == "n":
        break
galera = list()
galera.append(nome[:])
galera.append(peso[:])
print(f"Você cadastrou ao todo {len(galera[0])} pessoas.")
print(f"O maior peso foi de {max(peso):.2f}Kg. Peso de: ",end="")
for i, p in enumerate(range(0, len(galera[1]))):
    if galera[1][p] >= max(galera[1]):
        print(f"[{galera[0][i]}] ", end="")
print(f"\nO menor peso foi de {min(peso):.2f}Kg. Peso de: ",end="")
for i, p in enumerate(range(0, len(galera[1]))):
    if galera[1][p] <= min(galera[1]):
        print(f"[{galera[0][i]}] ", end="")
