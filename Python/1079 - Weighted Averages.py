try:
    n = int(input())
    for i in range(n):
        x1,x2,x3 = map(float,input().split())
        x4,x5,x6 = map(float,input().split())
        x7,x8,x9 = map(float,input().split())
        operation1=((x1*2)+(x2*3)+(x3*5))/10
        print(f"{operation1:.1f}")
        operation2=((x4*2)+(x5*3)+(x6*5))/10
        print(f"{operation2:.1f}")
        operation3=((x7*2)+(x8*3)+(x9*5))/10
        print(f"{operation3:.1f}")
except EOFError:
    pass 