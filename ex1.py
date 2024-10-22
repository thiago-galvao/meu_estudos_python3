# Um jogo de adivinhação onde a maquina "adivinha" um número e você tem que tentar acertar!

import random

computador = random.randint(0, 10)
print(
        """Sou seu computador..
Acabei de pensar em um número entre 0 e 10,
Será que você consegue adivinhar em qual número eu pensei?"""
        )
acertou = False
palpite = 0
while not acertou:
    jogador = int(input("Qual o seu palpite? "))
    palpite += 1
    if jogador < computador:
        print("Mais... Tente novamente.")
    if jogador > computador:
        print("Menos... Tente novamente")
    elif jogador == computador:
        acertou = True
print("Meus parabéns, você acertou na {} tentativa.".format(palpite))
