n=float(input())
if n < 0 or n > 100:
    print("Fora de intervalo")
elif (0 <= n <= 25):
    print("Intervalo [0,25]")
elif (25 <= n <= 50):
    print("Intervalo (25,50]")
elif (50 <= n <= 75):
    print("Intervalo (50,75]")
elif (75 <= n <= 100):
    print("Intervalo (75,100]")