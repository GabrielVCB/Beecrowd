a,b,c=map(float,input().split())
if a>=(b+c):
  print("NAO FORMA TRIANGULO")
elif  b>=a+c:
     print("NAO FORMA TRIANGULO")
elif c>=b+a:
     print("NAO FORMA TRIANGULO")
else:
    if a**2 == (b**2 + c**2):
      print("TRIANGULO RETANGULO")
    elif b**2 == (a**2 + c**2):
        print("TRIANGULO RETANGULO")
    elif c**2 == (a**2 + b**2):
        print("TRIANGULO RETANGULO")
    if (a**2) > (b**2 + c**2):
        print("TRIANGULO OBTUSANGULO")
    elif (b**2) > (a**2 + c**2):
        print("TRIANGULO OBTUSANGULO")
    elif (c**2) > (a**2 + b**2):
        print("TRIANGULO OBTUSANGULO")
    if (a**2) < (b**2 + c**2):
      if (b**2) < (a**2 + c**2):
        if (c**2) < (a**2 + b**2):
           print("TRIANGULO ACUTANGULO")
    if a==b==c:
        print("TRIANGULO EQUILATERO")
    if a == b != c:
        print("TRIANGULO ISOSCELES")
    elif a == c != b:
        print("TRIANGULO ISOSCELES")
    elif b == c != a: 
        print("TRIANGULO ISOSCELES")