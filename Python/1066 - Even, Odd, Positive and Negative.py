n1=int(input())
n2=int(input())
n3=int(input())
n4=int(input())
n5=int(input())
original_n1 = n1
original_n2 = n2
original_n3 = n3
original_n4 = n4
original_n5 = n5
if n1%2==0:
  n1=1
else:
  n1=0
if n2%2==0:
  n2=1
else:
  n2=0
if n3%2==0:
  n3=1
else:
  n3=0
if n4%2==0:
  n4=1
else:
  n4=0
if n5%2==0:
  n5=1
else:
  n5=0
even_numbers=n1+n2+n3+n4+n5
print(even_numbers,"valor(es) par(es)")
n1 = original_n1
n2 = original_n2
n3 = original_n3
n4 = original_n4
n5 = original_n5
if n1%2==1:
  n1=1
else:
  n1=0
if n2%2==1:
  n2=1
else:
  n2=0
if n3%2==1:
  n3=1
else:
  n3=0
if n4%2==1:
  n4=1
else:
  n4=0
if n5%2==1:
  n5=1
else:
  n5=0
odd_numbers=n1+n2+n3+n4+n5
print(odd_numbers,"valor(es) impar(es)")
n1 = original_n1
n2 = original_n2
n3 = original_n3
n4 = original_n4
n5 = original_n5
if n1 > 0:
  n1=1
else:
  n1=0
if n2 > 0:
  n2=1
else:
  n2=0
if n3 > 0:
  n3=1
else:
  n3=0
if n4 > 0:
  n4=1
else:
  n4=0
if n5 > 0:
  n5=1
else:
  n5=0
positive_numbers=n1+n2+n3+n4+n5
print(positive_numbers,"valor(es) positivo(s)")
n1 = original_n1
n2 = original_n2
n3 = original_n3
n4 = original_n4
n5 = original_n5
if n1 < 0:
  n1=1
else:
  n1=0
if n2 < 0:
  n2=1
else:
  n2=0
if n3 < 0:
  n3=1
else:
  n3=0
if n4 < 0:
  n4=1
else:
  n4=0
if n5 < 0:
  n5=1
else:
  n5=0
negative_numbers=n1+n2+n3+n4+n5
print(negative_numbers,"valor(es) negativo(s)")