# 74 - Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

tupla = (randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9))
print("Os números sorteados foram: ",end="")
for n in tupla:
    print(f"{n} ",end="")
print(f"\nO menor número foi: {min(tupla)}")
print(f"O maior número foi: {max(tupla)}")
