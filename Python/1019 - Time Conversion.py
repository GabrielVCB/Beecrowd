N=int(input())
hour= N // 3600
minutes= (N % 3600) // 60 
N= N % 60
if minutes < 10 or N < 10: 
    print("{0}:{1:01d}:{2:01d}".format(hour, minutes, N))
else:
    print("{0}:{1:02d}:{2:02d}".format(hour, minutes, N))