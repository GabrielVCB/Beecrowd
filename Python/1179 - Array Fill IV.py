even = []
odd = []
for i in range(15):
    t = int(input())
    if t % 2 == 0:
        if len(even) < 5:
            even.append(t)
        else:
            for j in range(5):
                print(f"par[{j}] = {even[j]}")
            even = [t]
    else:
        if len(odd) < 5:
            odd.append(t)
        else:
            for j in range(5):
                print(f"impar[{j}] = {odd[j]}")
            odd = [t]
for j in range(len(odd)):
    print(f"impar[{j}] = {odd[j]}")
for j in range(len(even)):
    print(f"par[{j}] = {even[j]}")