while True:
    x1,x2=map(int,input().split())
    if x1>0 and x2>0:
        print("primeiro")
    elif x1>0 and x2<0:
        print("quarto")
    elif x1<0 and x2>0:
        print("segundo")
    elif x1<0 and x2<0:
        print("terceiro")
    if x1==0 or x2==0:
        break