# 75 - Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9
# B)Em que posição foi digitado o primeiro valor 3
# C)Quais foram os números pares.
tupla = (int(input("Digite um número: ")), 
            int(input("Digite outro número: ")), 
            int(input("Digite mais um número: ")), 
            int(input("Digite o último número: ")))
print(f"O número 9 foi digitado {tupla.count(9)} vezes.")
for n in tupla:
    if n == 3:
        print(f"O número 3 foi digitado na {tupla.index(3)+1}º posição.")
print("Você não digitou nenhunma vez o número 3.")
print("Os valores pares digitados foram: ", end="")
for n in tupla:
    print(f"{n} ",end="")

