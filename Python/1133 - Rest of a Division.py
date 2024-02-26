X= int(input())
Y= int(input())
i = X
j = Y
if X>Y:
    i = Y
    j = X
while i<j:
    i+=1
    if i%5==2 or i%5==3 and i!=j:
        print(i)