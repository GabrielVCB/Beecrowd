n1,n2,n3,n4=map(float,input().split())
average=(n1*2+n2*3+n3*4+n4*1)/10
if average >=7.0:
    print(f"Media: {average:.1f}")
    print("Aluno aprovado.")
elif average < 5.0:
    print(f"Media: {average:.1f}")
    print("Aluno reprovado.")
elif average>=5.0 and average<=6.9:
    examScore=float(input())
    print(f"Media: {average:.1f}")
    print("Aluno em exame.")
    print(f"Nota do exame: {examScore:.1f}")
    print("Aluno aprovado.")
    mediaFinal=(average+examScore)/2
    print(f"Media final: {mediaFinal:.1f}")