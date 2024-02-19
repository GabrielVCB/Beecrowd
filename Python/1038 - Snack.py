x,y=map(int,input().split())
if x==1:
    x=4.00
elif x==2:
    x=4.50
elif x==3:
    x=5.00
elif x==4:
    x=2.00
elif x==5:
    x=1.50
result=x*y    
result=f"{result:.2f}"
print("Total: R$",result)