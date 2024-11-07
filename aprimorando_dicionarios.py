# Aprimore o desafio 93 para que ele funcione com vários jogadores, 
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
galera = list()
jogador = dict()
while True:
    jogador["nome"] = str(input("Digite o nome do jogador: "))
    qtdpartidas = int(input("Quantidade de partidas: "))
    partidas = []
    for p in range(0, qtdpartidas):
        gols = int(input(f"Gols na {p+1}º partida: "))
        partidas.append(gols)
    jogador["Gols em Partidas"] = partidas
    soma = 0
    for v in jogador["Gols em Partidas"]:
        soma += v
    jogador["total"] = soma
    galera.append(jogador.copy())
    jogador.clear()
    while True:
        pergunta = str(input("Gostaria de cadastrar mais algum jogador? [S/N]: ")).lower().strip()[0]
        if pergunta in 'sn':
            break
        print("ERRO! Por favor, digite apenas S ou N")
    if pergunta in "n":
        break
print("=-"*15)
print(f"Cód.   NOME               TOT. GOLS")
for j in range(0, len(galera)):
    print(f"{j}      {galera[j]["nome"]}       {galera[j]["total"]}")
while True:
    codigo = int(input("Digite o código do jogador para ver mais detalhes [999 para parar]: "))
    if codigo == 999:
        print("Obrigado por utiliar nosso sistema.")
        break
    if codigo > len(galera):
        print(f"Não existe jogador com código {codigo}!")
    else:
        print(f"==== Levantamento do jogador {galera[codigo]["nome"]} ====")
        c = 1
        for v in galera[codigo]["Gols em Partidas"]:
            print(f"   => Na {c}º partida, foram {v} gols")
            c += 1
        print(f"Foi um total de {galera[codigo]["total"]} gols.")
