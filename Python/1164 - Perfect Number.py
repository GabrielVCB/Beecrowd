n=int(input())
for i in range(n):
    x=int(input())
    divisor=0    
    for i in range(1,x):
        if (x%i)<=0:
            divisor+=i
    if divisor==x:
        print(x,"eh perfeito")
    else:
        print(x,"nao eh perfeito")