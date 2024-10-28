# 83 - Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
exp = str(input("Digite a sua expressão: "))
abrindo = 0
fechando = 0
for c in exp:
    if c == "(":
        abrindo += 1
    elif c == ")":
        fechando += 1
if abrindo == fechando:
    print("Sua expresão é valida")
else:
    print("Sua expressão é inválida.")
