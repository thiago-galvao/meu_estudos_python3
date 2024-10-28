# 79 - Crie um programa aonde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = []
while True:
    repete = 0
    num = int(input("Digite um número: "))
    lista.append(num)   
    for i, numero in enumerate(range(0, len(lista))):
        if lista[numero] == num:
            repete +=1
            if repete == 2:
                print(f"O número {num} está repetido e não foi adicionado.")
                del lista[-1]
    pergunta = str(input("Deseja adicionar mais um número? [S/N]: ")).lower().strip()[0]
    while not pergunta in "sn":
        print("Desculpe, não entendi...")
        pergunta = str(input("Deseja adicionar mais um número? [S/N]: ")).lower().strip()[0]
    if pergunta == "n":
        break
print(f"A sua lista de números é: {sorted(lista)}")
    
