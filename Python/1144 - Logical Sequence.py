n=int(input())
loop=0
number = 1
while loop < n:
    print(f'{number} {number**2} {number**3}')
    print(f'{number} {(number**2)+1} {(number**3)+1}')
    number+=1
    loop+=1