while True:
    x = int(input())
    if x == 0:
        break

    sequence = []
    for i in range(1, x + 1):
        sequence.append(str(i))

    print(' '.join(sequence))