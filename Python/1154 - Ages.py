n=0
quantity_n=0
soma_n=0
while n>=0:
    n=int(input())
    if n>=0:
        soma_n+=n
        quantity_n+=1
average=soma_n/quantity_n
print(f"{average:.2f}")