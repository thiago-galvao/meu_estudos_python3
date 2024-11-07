# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. 
# No final, mostre o conteúdo da estrutura na tela.

dados = dict()
dados["nome"] = str(input("Digite o nome do aluno: "))
dados["media"] = float(input("Digite a média do aluno: "))
if dados["media"] < 6:
    dados["Situacao"] = "REPROVADO"
elif dados["media"] < 7:
        dados["Situacao"] = "RECUPERAÇÃO"
elif dados["media"] > 7:
        dados["Situacao"] = "APROVADO"
print("=*="*10)
for k, v in dados.items():
    print(f" - {k} é igual a {v}.")
 