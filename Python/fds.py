from random import randint

x = randint(-1000, 1000)
print(x)
y = -1001
while y != x:
    y = int(input("Digite um número: "))
    if y > x:
        print("Menor!")
    elif y < x:
        print("Maior!")
    else:
        print("Você acertou!")