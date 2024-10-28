# 72 - Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extensão, de zero até vinte. 
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numeros = "zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte"
continua = "s"
while True:
    while not continua in "n":
        leitura = int(input("Digite um número de entre 0 e 20: "))
        if 0 <= leitura and leitura <= 20 :
            print("O número informado é o:",numeros[leitura])
            break
        else: 
            print("Digite um número válido... ")
    continua = str(input("Deseje ler mais algum número? [S/N]")).lower().strip()[0]
    if continua == "n":
        break
print("Obrigado por utilizar nosso serviço.")
