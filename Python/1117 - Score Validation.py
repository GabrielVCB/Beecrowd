notas_validas=0
total_notas=0
while notas_validas<2:
    n=float(input())
    if n<0 or n>10:
        print("nota invalida")
    else:
        total_notas+=n
        notas_validas+=1
media=total_notas/2
print(f"media = {media:.2f}")