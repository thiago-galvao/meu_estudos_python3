num = 0
c = -1
result = 0
while num != 999:
    c += 1
    num = int(input("Digite um número [999 para parar]: "))
    result += num
print("Você digitou {} números e a soma deles foi de {}. ".format(c, result - 999))