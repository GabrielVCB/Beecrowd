answer=1
grenais=0
v_inter=0
v_gremio=0
empate=0
while answer == 1:
    g_inter,g_gre=map(int,input().split())
    print("Novo grenal (1-sim 2-nao)")
    answer=int(input())
    grenais+=answer
    if g_inter>g_gre:
        v_inter+=1
    if g_gre>g_inter:
        v_gremio+=1
    if g_inter==g_gre:
        empate+=1        
else:
    print(f"{grenais-1} grenais")
    print(f"Inter:{v_inter}")
    print(f"Gremio:{v_gremio}")
    print(f"Empates:{empate}")
    if v_inter>v_gremio:
        print("Inter venceu mais")
    else:
        print("Gremio venceu mais")