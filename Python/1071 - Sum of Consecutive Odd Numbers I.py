x=int(input())
y=int(input())
start=min(x,y)+1
end=max(x,y)
sum_odd_numbers=0
for i in range(start,end):
    if i%2==1:
        sum_odd_numbers += i
print(sum_odd_numbers)