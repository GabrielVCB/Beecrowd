t=int(input())
order=0
initial_t=0
for i in range(1000):
    print(f"N[{order}] = {initial_t}")
    order+=1
    initial_t+=1
    if initial_t==t:
        initial_t=0