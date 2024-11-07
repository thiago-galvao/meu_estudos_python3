# Crie um programa onde o usuário possa digitar sete valores numéricos 
# e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.
num = [[], []]
for c in range(1,8):
    numero = int(input(f"Digite o {c}º número: "))
    if numero % 2 == 0:
        num[0].append(numero)
    else:
        num[1].append(numero)
print("=-"*30)
print(f"Os valores pares digitados foram: {sorted(num[0])})")
print(f"Os valores ímpares digitados foram: {sorted(num[1])}")
