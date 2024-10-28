# 77 - Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ("Banana", "Armario", "Fogao", "Abacate", "Porta", "Sofa", "Tijolo")
for p in palavras:
    print(f"\nA palavra {p.lower()} possui as vogais ", end="")
    for pala in p:
        if pala.lower() in 'aeio':
            print(f"{pala.lower()} ", end="")