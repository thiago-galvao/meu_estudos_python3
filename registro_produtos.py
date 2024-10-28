# 70 - Crie um programa que leia o nome e preço de vários produtos. 
# O programa deverá perguntar se o usuário vai continuar. No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1.000
# C) Qual é o nome do produto mais barato.
print("{:^40}".format("CADASTRO DE PRODUTOS"))
total = maior_que_mil = barato = caro = 0
mais_barato = " "
while True:
    nome_produto = str(input("Digite o nome do produto: "))
    valor_produto = float(input("Digite o valor do produto: R$"))
    if valor_produto > 1000:
        maior_que_mil += 1
    if barato == 0 or barato > valor_produto:
        barato = valor_produto
        mais_barato = nome_produto
    total += valor_produto
    print("PRODUTO CADASTRADO.")
    confirmacao = " "
    while confirmacao not in "sn":
        confirmacao = str(input("Deseja cadastrar mais algum produto [S/N]? ")).lower().strip()[0]
    if confirmacao == "n":
        break
print(f"Total {total:10.2f}")
print(f"Maiores de R$1.000,00 {maior_que_mil:10}")
print(f"Mais barato: {mais_barato:.10}")
