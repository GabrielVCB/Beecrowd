order=0
for i in range(100):
    x=float(input())
    if x<=10:
        if x==1:
            for i in range(int(x)):
                print(f"A[{order}] = {x:.1f}")
                order+=1 
        else:
            print(f"A[{order}] = {x:.1f}")
            order+=1 
    else:
        order+=1