# 67 - Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
# O programa será interrompido quando o número solicitado for negativo.
while True:
    print("="*25, "TABUADA V3.0", "="*25)
    num = int(input("Digite um número para visualizar sua tabuada: "))
    if num < 0:
        break
    for c in range(1, 11):
        print(f"{num} x {c} = {num * c}")
print("Obrigado por utilizar a tabuada v3.0!")