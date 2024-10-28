# 69 - Crie um programa que leia a idade e o sexo de várias pessoas. 
# A cada pessoa cadastrada o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.
qtdhomem = qtdi = mulhermenos20 = 0
while True:
    print("="*10, "CADASTRE UMA PESSOA", "="*10)
    i = int(input("Idade: "))
    s = " "
    while s not in "mf":
        s = str(input("Sexo[M/F]: ")).lower().strip()[0]
    print("="*15)
    print("CADASTRO REALIZADO!")
    confirmacao = " "
    while confirmacao not in "sn":
        confirmacao = str(input("Realizar mais algum cadastro? [S/N]: ")).lower().strip()[0]
    if i > 18:
        qtdi += 1
    if s == "m":
        qtdhomem += 1
    if s == "f" and i < 20:
        mulhermenos20 += 1
    if confirmacao == "n":
        break
print("Você finalizou o cadastro")
print(f"O total de pessoas maiores de 18 anos foi de: {qtdi}.")
print(f"O total de homens cadastrados foi de: {qtdhomem}.")
print(f"O total de mulheres com menos de 20 anos foi de: {mulhermenos20}.")
