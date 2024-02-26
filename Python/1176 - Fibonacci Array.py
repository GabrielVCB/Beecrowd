fibonacci = []
n = int(input())
first = 0
second = 1
number_f = 0
for i in range(60):
        sequence = first + second
        fibonacci.append(first)
        fibonacci.append(second)
        fibonacci.append(sequence)
        first = sequence + second
        second = sequence + first
for o in range(n):
    f=int(input())
    print(f"Fib({f}) = {fibonacci[f]}")