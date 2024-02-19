v1 = float(input())
v2 = float(input())
v3 = float(input())
v4 = float(input())
v5 = float(input())
v6 = float(input())

# contar quantos valores são positivos
count_positive = 0
if v1 > 0:
    count_positive += 1
if v2 > 0:
    count_positive += 1
if v3 > 0:
    count_positive += 1
if v4 > 0:
    count_positive += 1
if v5 > 0:
    count_positive += 1
if v6 > 0:
    count_positive += 1

# calcular a média dos valores positivos
if count_positive > 0:
    sum_positive = 0
    if v1 > 0:
        sum_positive += v1
    if v2 > 0:
        sum_positive += v2
    if v3 > 0:
        sum_positive += v3
    if v4 > 0:
        sum_positive += v4
    if v5 > 0:
        sum_positive += v5
    if v6 > 0:
        sum_positive += v6
    average_positive = sum_positive / count_positive
else:
    average_positive = 0

# exibir os resultados
print(f"{count_positive} valores positivos")
print(f"{average_positive:.1f}")