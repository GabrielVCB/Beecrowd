while True:
    try:
        l=int(input())
        v = list(map(int, input().split()))
    except EOFError:
        break
    faster_slum=max(v)
    if faster_slum<10:
        print(1)
    if 10<=faster_slum<20:
        print(2)
    if faster_slum>=20:
        print(3)