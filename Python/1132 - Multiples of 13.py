X= int(input())
Y= int(input())
if X>Y:
    X,Y=Y,X
total=0
for number in range(X,Y+1):
    if (number%13) != 0:
        total+=number
print(total)