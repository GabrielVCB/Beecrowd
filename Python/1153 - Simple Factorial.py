n=int(input())
fat=1
for i in range(n):
    fat*=n
    n-=1
print(fat)