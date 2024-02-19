salary=float(input())
if 0<=salary<=400:
  money_earned= (salary * 15) / 100
  new_salary= salary + money_earned
  print(f"Novo salario: {new_salary:.2f}")
  print(f"Reajuste ganho: {money_earned:.2f}")
  print("Em percentual: 15 %")
elif 400.01<=salary<=800:
  money_earned=(salary * 12) /100
  new_salary= salary + money_earned
  print(f"Novo salario: {new_salary:.2f}")
  print(f"Reajuste ganho: {money_earned:.2f}")
  print("Em percentual: 12 %")
elif 800.01<=salary<=1200:
  money_earned=(salary * 10) /100
  new_salary= salary + money_earned
  print(f"Novo salario: {new_salary:.2f}")
  print(f"Reajuste ganho: {money_earned:.2f}")
  print("Em percentual: 10 %")
elif 1200.01<=salary<=2000:
  money_earned=(salary * 7) /100
  new_salary= salary + money_earned
  print(f"Novo salario: {new_salary:.2f}")
  print(f"Reajuste ganho: {money_earned:.2f}")
  print("Em percentual: 7 %")
elif 2000.01<=salary:
  money_earned=(salary * 4) /100
  new_salary= salary + money_earned
  print(f"Novo salario: {new_salary:.2f}")
  print(f"Reajuste ganho: {money_earned:.2f}")
  print("Em percentual: 4 %")