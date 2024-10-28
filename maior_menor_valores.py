# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, 
# mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

num = soma = media = cont = menor = maior = 0
continua = "s"
while not continua in "Nn":
    cont += 1
    num = int(input("Digite um número: "))
    soma += num
    continua = str(input("Quer continuar [S/N]? ")).lower().strip()[0]
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = soma / cont
print("A média dos valores digitados foi de {}".format(media))
print(f"O menor número digitado foi {menor} e o maior foi {maior}.")    


