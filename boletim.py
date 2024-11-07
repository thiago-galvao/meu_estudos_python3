# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
notas = list()
add = list()
while True:
    add.append(str(input("Digite o nome do aluno: ")))
    add.append(float(input("Nota 1: ")))
    add.append(float(input("Nota 2: ")))
    notas.append(add[:])
    add.clear()
    pergunta = " "
    while not pergunta in "sn":
        pergunta = str(input("Deseja adicionar mais algum aluno? [S/N]: ")).lower().strip()[0]
    if pergunta == 'n':
        break
print("======BOLETIM DE NOTAS======")
print("Nº  NOME               MÉDIA")
for i, c in enumerate(range(0, len(notas))):
    media = notas[c][1] + notas[c][2]
    print(f"{i + 1}   {notas[c][0]:<12}",end="")
    print(f"{media/2:>10.2f}")
print("============================")
while True:
    pergunta = int(input("Deseja ver as notas de qual aluno?[999 para interromper]:  "))
    if pergunta == 999:
        break
    print(f"As notas de {notas[pergunta-1][0]} são {notas[pergunta-1][1:]}")
    
        