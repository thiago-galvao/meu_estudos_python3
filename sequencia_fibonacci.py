print("=" * 20)
print("Sequência Fibonacci")
print("=" * 20)

termos = int(input("Digite quantos termos você gostaria de visualizar: "))
l = 0
while l < termos:
    l += 1
    soma = 0
    while soma < l:
        soma += 2
        print(l, soma)