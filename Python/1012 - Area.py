A,B,C= map(float,input().split())
Pi=3.14159
a_tri_retangled= A*C/2
a_circle=Pi*C**2
a_trapezium=(A+B)*C/2
a_square=B**2
a_rectangle=A*B
print("TRIANGULO: {:.3f}".format(a_tri_retangled))
print("CIRCULO: {:.3f}".format(a_circle))
print("TRAPEZIO: {:.3f}".format(a_trapezium))
print("QUADRADO: {:.3f}".format(a_square))
print("RETANGULO: {:.3f}".format(a_rectangle))