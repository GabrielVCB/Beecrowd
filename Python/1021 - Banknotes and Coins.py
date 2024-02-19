valor=int(float(input()) * 100)
notas100= valor // 10000 
valor -= notas100 * 10000
notas50= valor // 5000 
valor-= notas50 * 5000
notas20= valor // 2000 
valor-= notas20 * 2000
notas10= valor // 1000 
valor-= notas10 * 1000
notas5= valor // 500 
valor-= notas5 * 500
notas2= valor // 200 
valor-= notas2 * 200 
print("NOTAS:")
print(int(notas100),"nota(s) de R$ 100.00")
print(int(notas50),"nota(s) de R$ 50.00")
print(int(notas20),"nota(s) de R$ 20.00")
print(int(notas10),"nota(s) de R$ 10.00")
print(int(notas5),"nota(s) de R$ 5.00")
print(int(notas2),"nota(s) de R$ 2.00")
moedas1= valor // 100 
valor-= moedas1 * 100
moedas050= valor // 50 
valor-= moedas050 * 50 
moedas025= valor // 25 
valor-= moedas025 * 25
moedas010= valor // 10
valor-= moedas010 * 10 
moedas005= valor // 5 
valor-= moedas005 * 5 
print("MOEDAS:")
print(int(moedas1),"moeda(s) de R$ 1.00")
print(int(moedas050),"moeda(s) de R$ 0.50")
print(int(moedas025),"moeda(s) de R$ 0.25")
print(int(moedas010),"moeda(s) de R$ 0.10")
print(int(moedas005),"moeda(s) de R$ 0.05")
print(int(valor),"moeda(s) de R$ 0.01")