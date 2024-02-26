order=0
for i in range(10):
    x=int(input())
    if x<=0:
        x=1
    if x==1:
        for i in range(x):
            print(f"X[{order}] = {x}")
            order+=1 
    else:
        print(f"X[{order}] = {x}")
        order+=1 