print("GERADOR DE PA")
print("-" * 20)
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))
termo = primeiro
c = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        print("{} __ ".format(termo), end="")
        termo += razao
        c += 1
    print("PAUSA")
    mais = int(input("Quantos termos quer mostrar a mais? "))
print("Progressão finalizada com {} termos mostrados.".format(total))
