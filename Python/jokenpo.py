from random import randint

while True:
    x = 0
    print("1 = Pedra; 2 = Papel; 3 = Tesoura")
    while x <= 0 or x >= 4:
        x = int(input("Digite sua ação: "))
        if x <= 0 or x >= 4:
            print("Ação inválida!")
    y = randint(1,3)

    if x == 1:
        print("Jogador: Pedra!")
    if x == 2:
        print("Jogador: Papel!")    
    if x == 3:
        print("Jogador: Tesoura!")
    if y == 1:
        print("Máquina: Pedra!")
    if y == 2:
        print("Máquina: Papel!")
    if y == 3:
        print("Máquina: Tesoura!")
        
    if x == y:
        print("Empate!")
    if x == 1 and y == 2:
        print("Derrota!")
    if x == 1 and y == 3:
        print("Vitória!")
    if x == 2 and y == 1:
        print("Vitória!")
    if x == 2 and y == 3:
        print("Derrota!")
    if x == 3 and y == 1:
        print("Derrota!")
    if x == 3 and y == 2:
        print("Vitória!")    
    print(5 % 3)
    z = ""
    while z != "s" and z != "S" and z != "n" and z != "N":
        z = str(input("Deseja recomeçar? [S/N]: "))
        if z != "s" and z != "S" and z != "n" and z != "N":
            print ("ERR0R!")
    if z == "s" or z == "S":
        pass
    elif z == "n" or z == "N":
        break