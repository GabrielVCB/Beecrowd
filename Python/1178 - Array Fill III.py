t=float(input())
order=0
for i in range(100):
    print(f"N[{order}] = {t:.4f}")
    order+=1
    t/=2