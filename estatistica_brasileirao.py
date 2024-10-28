# 73 - Crie uma tupla com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de colocação. 
# Depois mostre:
# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C)Uma lista com os times em ordem alfabética.
# D)Em que posição na tabela está o time do Cruzeiro.
tabela = ("Botafogo", "Palmeiras", "Fortaleza", "Flamengo", "São Paulo", "Internacional", "Bahia", "Cruzeiro", "Atlético-MG", "Vasco", "Fluminense", "Criciúma", "Grêmio", "Red Bull Bragantino", "Juventude", "Vitória", "Corinthians", "Athletico-PR", "Cuiabá", "Atlético-GO")
print("Os 5 primeiros colocados da tabela são:")
print("="*20)
colocacao = 1
for time in range(0, 5, 1):
    print("{}º {}".format(colocacao, tabela[time]))
    colocacao += 1

print("="*20)
print("Os 4 últimos colocados são: ")
colocado = len(tabela) - 4
for time in tabela[-4:]:
    colocado += 1
    print("{}º {}". format(colocado, time))

print("="*20)
print("Tabela em ordem alfabética: ")
ordenada = sorted(tabela)
ctime = 1
for time in range(len(ordenada)):
    print("{} - {}".format(ctime, ordenada[time]))
    ctime += 1

print("="*20)
print("Posição do Cruzeiro  : ")
conttime = 0
for time in range(len(tabela)):
    conttime += 1
    if tabela[time] == "Cruzeiro":
        print("O Cruzeiro está na {}º posição na tabela.".format(conttime))

