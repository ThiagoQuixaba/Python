lados = [1, 0, 0, 0]
triangulo = True
while lados[0] <= 3:
    while True:
        lados[lados[0]] = int(input(f"Digite o comprimento do {lados[0]}° lado: "))
        if lados[lados[0]] >= 0:
            break
        else:
            print("Comprimento invalido! Tente novamente.")
            pass
    if lados[lados[0]] == 0:
        print("Não é um triangulo")
        triangulo = False
        break
    else:
        pass
    lados[0] = lados[0] + 1
if triangulo == True:
    if (lados[1] + lados[2]) < lados[3]:
        triangulo = False
    elif (lados[2] + lados[3]) < lados[1]:
        triangulo = False
    elif (lados[1] + lados[3]) < lados[2]:
        triangulo = False
    else:
        triangulo = True
    if triangulo == False:
        print("Não é um triangulo!")
    else:
        if lados[1] == lados[2] and lados[2] == lados[3]:
            print("É um triângulo equilátero!")
        elif lados[1] != lados[2] and lados[2] != lados[3]:
            print("É um triângulo escaleno!")
        else:
            print("É um triângulo isósceles!")