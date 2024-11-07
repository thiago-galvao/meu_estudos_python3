# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar
from datetime import datetime
dados = {"Nome":str(input("Qual seu nome? ")),
         "Nascimento":int(input("Qual seu ano de nascimento? ")),
         "CTPS":int(input("Qual o número da sua CTPS? (0 não tem): "))}
idade = datetime.now().year - dados["Nascimento"]
dados["Idade"] = idade
if dados["CTPS"] != 0:
    dados["Ano de Contratação"] = int(input("Ano de contratação: "))
    dados["Salario"] = float(input("Salário atual: R$"))
    dados["Idade de Aposentadoria"] = dados["Ano de Contratação"] + 35 - datetime.now().year + dados["Idade"]
print("=-"*20)
print(f"=== DADOS DO TRABALHADOR ===")
print("=-"*20)
for k, v in dados.items():
    print(f" - {k} é > {v}")
#print(f" -Nome > {dados["nome"]}\n -Ano de Nascimento > {dados['nascimento']}\n -Idade > {dados['idade']}")