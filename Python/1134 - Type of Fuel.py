alcohol=0
gasoline=0
diesel=0
x=0
while x!=4:
    x=int(input())
    if x==4:
        break
    elif x==1:
        alcohol+=1
    elif x==2:
        gasoline+=1
    elif x==3:
        diesel+=1
print("MUITO OBRIGADO")
print(f"Alcool: {alcohol}")
print(f"Gasolina: {gasoline}")
print(f"Diesel: {diesel}")