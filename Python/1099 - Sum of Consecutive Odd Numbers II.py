n = int(input())
for i in range(n):
    x, y = map(int, input().split()) 
    if x > y:
        x, y = y, x  
    odd_sum = 0
    for num in range(x+1, y):
        if (num % 2) != 0:
            odd_sum += num
    print(odd_sum)  