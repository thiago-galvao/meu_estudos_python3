# 80 - Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, 
# já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.

lista = []
for n in range(0,5):
    num = int(input("Digite um número: "))
    lista.append(num)
    if num <= lista[0]:
        lista.insert(0, num)
        del lista[-1]
print(lista)
