n = int(input())
for i in range(n):
    x = int(input())
    if x < 0:
        if x % 2 == 1:
            print("ODD NEGATIVE")
        elif x % 2 == 0:
            print("EVEN NEGATIVE")
    elif x > 0:
        if x % 2 == 1:
            print("ODD POSITIVE")
        elif x % 2 == 0:
            print("EVEN POSITIVE")
    else:
        print("NULL")