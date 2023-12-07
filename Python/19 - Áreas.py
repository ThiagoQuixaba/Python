#Áreas:
while True:
    largura_triangulo = float(input("Inserir a largura do triângulo: "))
    while largura_triangulo < 0:
        largura_triangulo = float(input("largura invalida! Inserir a largura do triângulo: "))
    altura_triangulo = float(input("Inserir a altura do triângulo: "))
    while altura_triangulo < 0:
        altura_triangulo = float(input("Altura invalida! Inserir a altura do triângulo: "))
    area_triangulo = largura_triangulo * altura_triangulo / 2
    print(f"A área do triangulo é de {area_triangulo}")

    largura_quadrado = float(input("Inserir a largura do quadrado: "))
    while largura_quadrado < 0:
        largura_quadrado = float(input("largura invalida! Inserir a largura do quadrado: "))
    altura_quadrado = float(input("Inserir a altura do quadrado: "))
    while altura_quadrado < 0:
        altura_quadrado = float(input("Altura invalida! Inserir a altura do quadrado: "))
    area_quadrado = largura_quadrado * altura_quadrado
    print(f"A área do quadrado é de {area_quadrado}")

    base_inferio_trapezio = float(input("Inserir a base inferior do trapézio: "))
    while base_inferio_trapezio < 0:
        base_inferio_trapezio = float(input("Base inferior invalida! Inserir a base inferior do trapézio: "))
    base_superior_trapezio = float(input("Inserir a base superior do trapézio: "))
    while base_superior_trapezio < 0:
        base_superior_trapezio = float(input("Base superior invalida! Inserir a base superior do trapézio: "))
    altura_trapezio = float(input("Inserir a altura do trapézio: "))
    while altura_trapezio < 0:
        altura_trapezio = float(input("Altura invalida! Inserir a altura do trapézio: "))
    area_trapezio = (base_inferio_trapezio + base_superior_trapezio) * altura_quadrado / 2
    print(f"A área do trapésio é de {area_trapezio}")

    area = area_triangulo + area_quadrado +area_trapezio
    print(f"A área total é de {area}")

    x = ""
    while x != "s" and x != "S" and x != "n" and x != "N":
        x = str(input("Deseja recomeçar? [S/N]: "))
        if x != "s" and x != "S" and x != "n" and x != "N":
            print ("ERR0R!")
    if x == "s" or x == "S":
        pass
    elif x == "n" or x == "N":
        break