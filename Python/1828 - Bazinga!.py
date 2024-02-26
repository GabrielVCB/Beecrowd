t = int(input())
count=1
for i in range(t):
    entrada=input()
    sheldon, raj = entrada.split()
    if sheldon == "tesoura":
        if raj == "tesoura":
            print(f"Caso #{count}: De novo!")
        if raj == "papel":
            print(f"Caso #{count}: Bazinga!")
        if raj == "Spock":
            print(f"Caso #{count}: Raj trapaceou!")
        if raj == "lagarto":
            print(f"Caso #{count}: Bazinga!")
        if raj == "pedra":
            print(f"Caso #{count}: Raj trapaceou!")
    if sheldon == "papel":
        if raj == "papel":
            print(f"Caso #{count}: De novo!")
        if raj == "tesoura":
            print(f"Caso #{count}: Raj trapaceou!")
        if raj == "Spock":
            print(f"Caso #{count}: Bazinga!")
        if raj == "pedra":
            print(f"Caso #{count}: Bazinga!")
        if raj == "lagarto":
             print(f"Caso #{count}: Raj trapaceou!")
    if sheldon == "pedra":
        if raj == "pedra":
            print(f"Caso #{count}: De novo!")
        if raj == "papel":
            print(f"Caso #{count}: Raj trapaceou!")
        if raj == "tesoura":
            print(f"Caso #{count}: Bazinga!")
        if raj == "Spock":
            print(f"Caso #{count}: Raj trapaceou!")
        if raj == "lagarto":
             print(f"Caso #{count}: Bazinga!")
    if sheldon == "Spock":
        if raj == "Spock":
            print(f"Caso #{count}: De novo!")
        if raj == "tesoura":
            print(f"Caso #{count}: Bazinga!")
        if raj == "pedra":
            print(f"Caso #{count}: Bazinga!")
        if raj == "papel":
            print(f"Caso #{count}: Raj trapaceou!")
        if raj == "lagarto":
            print(f"Caso #{count}: Raj trapaceou!")
    if sheldon == "lagarto":
        if raj == "lagarto":
            print(f"Caso #{count}: De novo!")
        if raj == "pedra":
            print(f"Caso #{count}: Raj trapaceou!")
        if raj == "papel":
            print(f"Caso #{count}: Bazinga!")
        if raj == "tesoura":
            print(f"Caso #{count}: Raj trapaceou!")
        if raj == "Spock":
            print(f"Caso #{count}: Bazinga!")
    count+=1