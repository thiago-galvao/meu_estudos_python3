# Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
# O programa vai ler o nome do jogador e quantas partidas ele jogou. 
# Depois vai ler a quantidade de gols feitos em cada partida. 
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

dados = {"nome":str(input("Digite o nome do jogador: "))
}
qtdpartidas = int(input("Quantidade de partidas: "))
partidas = []
for p in range(0, qtdpartidas):
    gols = int(input(f"Gols na {p+1}º partida: "))
    partidas.append(gols)
dados["Gols em Partidas"] = partidas
soma = 0
for v in dados["Gols em Partidas"]:
    soma += v
dados["total"] = soma
print("=-"*15)
print(dados)
print("=-"*15)
for k, v in dados.items():
    print(f"O campo {k} tem valor {v}")
print("=-"*15)
print(f"O jogador {dados['nome']} jogou {qtdpartidas} partidas.")
c = 1
for v in dados["Gols em Partidas"]:
    print(f"   => Na {c}º partida, foram {v} gols")
    c += 1
print(f"Foi um total de {soma} gols.")
print("=-"*15)
print(f"O jogador {dados['nome']} marcou um total de {soma} gols em todo o campeonato.")