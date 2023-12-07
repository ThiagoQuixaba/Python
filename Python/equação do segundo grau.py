a = 0
while a == 0:
    a = float(input("Digite o valor de A: "))
    if a == 0:
        print("O valor digitado é inválido! Tente novamente.")

b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

delta = (b * b) - (4 * a * c)
if delta < 0:
    print("O valor de x não existe no conjunto dos números Reais!")
elif delta == 0:
    x = -b / (2 * a)
    print("x =", x)
else:
    x1 = (-b + (delta ** (1 / 2))) / (2 * a)
    x2 = (-b - (delta ** (1 / 2))) / (2 * a)
    print("x =", x1, "ou", x2)
