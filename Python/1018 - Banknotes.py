valor= int(input())
print(valor)
cedulas_100= valor // 100
valor-= cedulas_100* 100
cedulas_50= valor // 50 
valor-= cedulas_50 * 50
cedulas_20= valor // 20 
valor-= cedulas_20 * 20
cedulas_10= valor // 10
valor-= cedulas_10 * 10
cedulas_5= valor // 5 
valor-= cedulas_5 * 5 
cedulas_2= valor // 2 
valor-= cedulas_2 * 2 
cedulas_1= valor // 1 
valor-= cedulas_1 * 1 
print(cedulas_100,"nota(s) de R$ 100,00")
print(cedulas_50,"nota(s) de R$ 50,00")
print(cedulas_20,"nota(s) de R$ 20,00")
print(cedulas_10,"nota(s) de R$ 10,00")
print(cedulas_5,"nota(s) de R$ 5,00")
print(cedulas_2,"nota(s) de R$ 2,00")
print(cedulas_1,"nota(s) de R$ 1,00")