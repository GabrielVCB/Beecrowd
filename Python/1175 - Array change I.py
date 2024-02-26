order=0
lista=[]
for i in range(20):
    x=int(input())
    lista.append(x)
for i in lista[::-1]:
    print(f"N[{order}] = {i}") 
    order+=1