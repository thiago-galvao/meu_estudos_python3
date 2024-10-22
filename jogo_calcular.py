import time

valor1 = int(input("Primeiro valor: "))
valor2 = int(input("Sgundo valor: "))

escolha = 0

while escolha != 5:
    print("""Escolha uma opção:
[1] - Somar
[2] - Multiplicar
[3] - Maior
[4] - Novos números
[5] - Sair do programa""")
    escolha = int(input(">>>>Qual a sua opção? "))
    if escolha == 1:
        soma = valor1 + valor2
        print("---" * 10)
        print("A soma dos valores é igual a: {}".format(soma))
        print("---" * 10)
        print("""Seu primeiro número é: {}
Seu segundo número é: {}""".format(valor1, valor2))
    elif escolha == 2:
        multi = valor1 * valor2
        print("---" * 10)
        print("O resultado da multiplacação é igual a: {}".format(multi))
        print("---" * 10)
        print("""Seu primeiro número é: {}
Seu segundo número é: {}""".format(valor1, valor2))
    elif escolha == 3:
        if valor1 > valor2:
            print("---" * 10)
            print("O maior valor é o primeiro: {}".format(valor1))
            print("---" * 10)
            print("""Seu primeiro número é: {}
Seu segundo número é: {}""".format(valor1, valor2))
        elif valor2 > valor1:
            print("---" * 10)
            print("O maior valor é o segundo: {}".format(valor2))
            print("---" * 10)
            print("""Seu primeiro número é: {}
Seu segundo número é: {}""".format(valor1, valor2))
        else:
            print("---" * 10)
            print("Os valores são iguais.")
            print("---" * 10)
            print("""Seu primeiro número é: {}
Seu segundo número é: {}""".format(valor1, valor2))
    elif escolha == 4:
        print("---" * 10)
        print("Por favor, digite os novos números.")
        print("---" * 10)
        valor1 = int(input("Primeiro valor: "))
        valor2 = int(input("Sgundo valor: "))
    elif escolha == 5:
        print("---" * 10)
        print("Finalizando...")
        print("---" * 10)
        time.sleep(1)
    else:
        print("---" * 10)
        print("ERRO. Escolha uma opção válida.")
        print("---" * 10)
        print("""Seu primeiro número é: {}
Seu segundo número é: {}""".format(valor1, valor2))
print("Obrigado por utilizar nosso serviço, volte sempre.")