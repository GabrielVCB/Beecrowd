while True:
    m, n = map(int, input().split())
    if m <= 0 or n <= 0:
        break
    soma = 0
    if m > n:
        m, n = n, m
    numeros = ""
    for i in range(m, n + 1):
        soma += i
        numeros += str(i) + " "
    print(f"{numeros}Sum={soma}")