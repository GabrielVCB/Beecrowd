notas_validas = 0
total_notas = 0

while notas_validas < 2:
    n = float(input())
    if n < 0 or n > 10:
        print("nota invalida")
    else:
        total_notas += n
        notas_validas += 1

media = total_notas / 2
print(f"media = {media:.2f}")

x = 0
while x != 2:
    print("novo calculo (1-sim 2-nao)")
    x = int(input())

    if x < 1 or x > 2:
        continue

    if x == 1:
        novas_notas_validas = 0
        novo_total = 0

        while novas_notas_validas < 2:
            new_n = float(input())
            if new_n < 0 or new_n > 10:
                print("nota invalida")
            else:
                novo_total += new_n
                novas_notas_validas += 1

        media_nova = novo_total / 2
        print(f"media = {media_nova:.2f}")