n=int(input())
number=1
divisors=[]
while number<=n:
    if n%number==0:
        divisors.append(number)
    number+=1
for i in divisors:
    print(i)