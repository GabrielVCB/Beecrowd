numeros = []
for i in range(100):
    numero = int(input())
    numeros.append(numero)

maior = max(numeros)
posicao = numeros.index(maior) + 1 # adiciona 1 à posição para começar em 1 ao invés de 0

print(maior)
print(posicao)