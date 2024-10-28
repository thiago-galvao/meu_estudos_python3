# 78 - Faça um programa que leia 5 valores númericos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

num =[]
for c in range(0,5):
    num.append((int(input("Digite o valor: "))))
print(f"Os números digitados foram: {num}.")
pmax = 0
pmin = 0
print(f"O maior valor digitado foi: {max(num)}, e ele aparece nas posições: ", end="")
for i, c in enumerate(range(0, len(num))):
    if num[c] == max(num):
        print(f"{i + 1}...", end="")
print()
print(f"O menor valor digitado foi: {min(num)}, e ele aparece nas posições: ", end="" )
for i, c in enumerate(range(0, len(num))):
    if num[c] == min(num):
        print(f"{i + 1}...", end="")
print()
