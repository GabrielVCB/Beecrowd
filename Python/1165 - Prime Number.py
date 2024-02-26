n=int(input())
for i in range(n):
    x=int(input())
    divisor=0
    for i in range(1,x+1):
        if x%i==0:
            divisor+=1
    if divisor==2:
        print(x,"eh primo")
    else:
        print(x,"nao eh primo")