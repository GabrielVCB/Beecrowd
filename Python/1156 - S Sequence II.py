numerador=1
denominador=1
result_s=0
while numerador<=39:
    s=numerador/denominador
    denominador*=2
    numerador+=2
    result_s+=s
print(f"{result_s:.2f}")