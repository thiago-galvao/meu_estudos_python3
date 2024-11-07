# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna
# C) O maior valor da segunda linha.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0
soma3 = 0
for c in range(0, 3):
    for l in range(0, 3):
        num = int(input(f"Digite o número da posição [{c} - {l}]: "))
        matriz[c][l] = num
        if num % 2 == 0:
            soma += num
        if l == 2:
            soma3 += num
    if c == 1:
        max = max(matriz[c])
for c in range(0, 3):
    for l in range(0, 3):
        print(f"|{matriz[c][l]:^5}|", end="")
    print()
print(f"A soma dos valores pares é de: {soma}")
print(f"A soma dos valores da terceira coluna é de: {soma3}")
print(f"O maior valor da segunda linha é: {max}")
