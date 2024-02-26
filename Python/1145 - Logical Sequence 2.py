x, y = map(int, input().split())
number = 1
while number <= y:
    sequence = ""
    for _ in range(x):
        if number > y:
            break
        sequence += str(number) + " "
        number += 1
    print(sequence.strip())