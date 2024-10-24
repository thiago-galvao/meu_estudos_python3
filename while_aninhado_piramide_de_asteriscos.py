#n = int(input("Digite a altura da piramide: "))
#l = 0
#while l < n:
#   l += 1
#    print(l * "*")

n = int(input("Digite a altura da pirâmide: "))
l = 1  # Começamos com 1 para a primeira linha da pirâmide
while l <= n:  # Garantimos que a altura da pirâmide seja exatamente 'n'
    print(" " * (n - l) + "*" * (2 * l - 1))  # Ajuste para centralizar os asteriscos
    l += 1  # Incremento da linha
