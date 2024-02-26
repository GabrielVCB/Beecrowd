x=int(input())
z=0
current_number=x
while z<=x:
    z=int(input())
while current_number<=z:
    current_number+=x+1
    x+=1
rest=current_number-z
print(rest)