num = int(input("Digite um número para calcular seu fatorial: "))
f = 1
print("Calculando {}! = ".format(num), end="")
for c in range(num, 0, -1):
    print("{} " .format(c), end="")
    print("x " if c > 1 else "=", end="")
    f *= c
    result = f * c
print(" {}".format(result))
    
