n = int(input())
animals = {'C': 0, 'R': 0, 'S': 0}

for i in range(n):
    amount, animal_type = input().split()
    animals[animal_type] += int(amount)

total = sum(animals.values())
coelhos = animals['C']
ratos = animals['R']
sapos = animals['S']

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {coelhos/total*100:.2f} %")
print(f"Percentual de ratos: {ratos/total*100:.2f} %")
print(f"Percentual de sapos: {sapos/total*100:.2f} %")