#Iguais ou diferentes:
numeros = [0, 0, 0]
while numeros[0] < 2:
    numeros[numeros[0] + 1] = int(input(f"Digite o {numeros[0] + 1}° número: "))
    numeros[0] = numeros[0] + 1
if numeros[1] == numeros[2]:
    print(f"{numeros[1]} e {numeros[2]} são iguais.")
elif numeros[1] > numeros[2]:
    print(f"{numeros[1]} é maior que {numeros[2]}.")
else: 
    print(f"{numeros[1]} é menor que {numeros[2]}.")