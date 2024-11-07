# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e 
# todos os dicionários em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas 
# B) A média de idade 
# C) Uma lista com as mulheres 
# D) Uma lista de pessoas com idade acima da média

pessoas = list()
caracteristicas = dict()
soma = 0
while True:
    caracteristicas["nome"] = str(input("Nome: "))
    while True:
        caracteristicas["sexo"] = str(input("Sexo [M/F]: ")).upper().strip()[0]
        if caracteristicas["sexo"] in "MF":
            break
        print("ERRO! Por favor, digite apenas M ou F.")
    caracteristicas["idade"] = int(input("Idade: "))
    soma += caracteristicas["idade"]
    pessoas.append(caracteristicas.copy())
    while True:
        pergunta = str(input("Cadastrar mais uma pessoa? [S/N]: ")).lower().strip()[0]
        if pergunta in "sn":
            break
        print("ERRO! Por favor, digite apenas S ou N.")
    if pergunta == "n":
            break
print(f"A) Você cadastrou um total de {len(pessoas)} pessoas.")
media = soma / len(pessoas)
print(f"B) A média de idade é de {media:.2f} anos.")
print(f"C) As mulheres cadastradas foram: ",end="")
for c in range(0, len(pessoas)):
    if pessoas[c]["sexo"] == "F":
        print(pessoas[c]["nome"], end=". ")
print(f"\nLista de pessoas acima da média: ")
for c in range(0, len(pessoas)):
    if pessoas[c]["idade"] >= media:
        print(f"Nome => {pessoas[c]["nome"]}; Sexo => {pessoas[c]["sexo"]}; Idade => {pessoas[c]["idade"]} anos.")
