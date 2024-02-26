soma=0
l=int(input())
t=input()
for i in range(144):
    x=float(input())
    if i==l:
        soma+=x
        l+=12
if t=="S":
        print(f"{soma:.1f}")
if t=="M":
        media=soma/12
        print(f"{media:.1f}")