from random import randint
from time import sleep
print("=-"*20)
print("           JOGOS MEA SENA         ")
print("=-"*20)
jogos = int(input("Digite a quantidade de jogos a serem sorteados: "))
sorteio = []
temp = []
for c in range(0, jogos):
    for c in range(0, 6):
        num = randint(1, 60) 
        while num in temp:
            num = randint(1, 60) 
        temp.append(num)
    sorteio.append(temp[:])
    temp.clear()
print("=======SORTEANDO JOGOS=======")
cont = 0
for c in range(0, len(sorteio)):
    sleep(1)
    print(f"Jogo {c + 1}: {sorted(sorteio[c])}")
print("Boa sorte!")