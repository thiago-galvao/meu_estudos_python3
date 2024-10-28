# 82 - Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apnas os valores pares e os valores ímpares digitados, respectivamente.
# No final, mostre o conteúdo das três listas geradas.

n = list()
while True:
    n.append(int(input("Digite um número: ")))
    pergunta = str(input("Deseja adicionar mais algum valor? [S/N]: ")).lower().strip()[0]
    if pergunta in "n":
        break
listap = list()
listai = list()
for i, v in enumerate(n):
    if v % 2 == 0:
        listap.append(v)
    else:
        listai.append(v)
print(f"A lista geral ficou assim: {n}\nA lista dos número pares fiou assim: {listap}\nE a lista dos ímpares ficou assim: {listai}")
    
