# 76 - Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivoc preços na sequência. 
# No final, mostre uma listagem de preços organizando os dados em forma tabular.

produtos = ("Arroz", 15, "Feijão", 12, "Computador", 1500, "Mouse", 50, "Cadeira", 2000, "Notebook", 500)
print("="*38)
print(f"{"----LISTA DE COMPRAS----":^38}")
print("="*38)
for prod in range(0, len(produtos)):
    if prod % 2 == 0:
        print(f"{produtos[prod]:.<30}",end="")
    else:
        print(f"R${produtos[prod]:8.2F}")